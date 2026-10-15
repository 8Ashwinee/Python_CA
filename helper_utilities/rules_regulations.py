"""MVP purchase affordability rules.

Opening balances are user-entered start-of-day balances. Dated income and
spending on or after that date are applied through the check date. Only
scheduled bills and savings contributions after the check date and through
the purchase date are forecast; future income is not assumed. Investments
are excluded from spendable cash. Balances older than 30 days make the result
inconclusive.
"""

from __future__ import annotations

from calendar import monthrange
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from typing import Iterable, Mapping

from data_models.record_data import Income, RecurringBills, SavingsGoals, Spending


_CYCLE_MONTHS = {"monthly": 1, "quarterly": 3, "annually": 12}
_ZERO = Decimal("0")


def _money(value: Decimal | int | float, field_name: str) -> Decimal:
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError(f"{field_name} must be a valid amount") from None
    if not amount.is_finite():
        raise ValueError(f"{field_name} must be a finite amount")
    return amount


def _validate_cycle(cycle: str) -> int:
    try:
        return _CYCLE_MONTHS[cycle.lower()]
    except (AttributeError, KeyError):
        supported = ", ".join(_CYCLE_MONTHS)
        raise ValueError(f"cycle must be one of: {supported}") from None


def _validate_date(value: date, field_name: str) -> None:
    if not isinstance(value, date) or isinstance(value, datetime):
        raise ValueError(f"{field_name} must be a date")


def _shift_month(anchor: date, month_offset: int) -> date:
    month_index = anchor.year * 12 + anchor.month - 1 + month_offset
    year, month = divmod(month_index, 12)
    month += 1
    return date(year, month, min(anchor.day, monthrange(year, month)[1]))


def _scheduled_occurrences(
    first_date: date, cycle_months: int, after: date, through: date
) -> Iterable[date]:
    month_delta = (after.year - first_date.year) * 12 + after.month - first_date.month
    periods = max(0, month_delta // cycle_months)
    occurrence = _shift_month(first_date, periods * cycle_months)
    if occurrence <= after:
        occurrence = _shift_month(first_date, (periods + 1) * cycle_months)

    while occurrence <= through:
        yield occurrence
        periods += 1
        occurrence = _shift_month(first_date, periods * cycle_months)


@dataclass(frozen=True)
class AccountBalance:
    """A user-entered account balance and the date it applies from."""

    amount: Decimal | int | float
    as_of: date


@dataclass(frozen=True)
class PurchaseCheck:
    """Explainable result for a planned purchase."""

    status: str
    message: str
    estimated_cash: Decimal | None
    purchase_amount: Decimal
    remaining_cash: Decimal | None
    minimum_reserve: Decimal
    upcoming_bills: Decimal | None
    planned_savings: Decimal | None
    issues: tuple[str, ...] = ()


class FinancialRules:
    """Calculate spendable cash without treating investments as cash."""

    def __init__(self, max_balance_age_days: int = 30):
        if max_balance_age_days < 0:
            raise ValueError("max_balance_age_days cannot be negative")
        self.max_balance_age_days = max_balance_age_days

    def check_purchase(
        self,
        amount: Decimal | int | float,
        purchase_date: date,
        account_balances: Mapping[str, AccountBalance],
        *,
        income: Iterable[Income] = (),
        spending: Iterable[Spending] = (),
        upcoming_bills: Iterable[RecurringBills] = (),
        planned_savings: Iterable[SavingsGoals] = (),
        minimum_cash_reserve: Decimal | int | float = 0,
        as_of: date | None = None,
    ) -> PurchaseCheck:
        """Check a purchase against cash after known obligations and reserve.

        Transactions dated through ``as_of`` update their account balance.
        Future scheduled bills and savings contributions due by ``purchase_date``
        are deducted once. Future income is deliberately not forecast.
        """
        check_date = date.today() if as_of is None else as_of
        _validate_date(check_date, "as_of")
        _validate_date(purchase_date, "purchase_date")
        purchase_amount = _money(amount, "amount")
        reserve = _money(minimum_cash_reserve, "minimum_cash_reserve")
        if purchase_amount < _ZERO:
            raise ValueError("amount cannot be negative")
        if reserve < _ZERO:
            raise ValueError("minimum_cash_reserve cannot be negative")
        if purchase_date < check_date:
            raise ValueError("purchase_date cannot be before as_of")

        balances: dict[str, Decimal] = {}
        issues: list[str] = []
        for account, opening in account_balances.items():
            if not account:
                raise ValueError("account names cannot be empty")
            if not isinstance(opening, AccountBalance):
                raise ValueError(f"opening balance for {account!r} must be an AccountBalance")
            _validate_date(opening.as_of, f"balance date for {account!r}")
            balances[account] = _money(opening.amount, f"balance for {account!r}")
            age_days = (check_date - opening.as_of).days
            if age_days < 0:
                issues.append(f"Opening balance for {account} is dated in the future.")
            elif age_days > self.max_balance_age_days:
                issues.append(
                    f"Opening balance for {account} is {age_days} days old; "
                    f"the limit is {self.max_balance_age_days} days."
                )

        if not account_balances:
            issues.append("No user-entered opening balances are available.")

        actual_income = tuple(income)
        actual_spending = tuple(spending)
        bills = tuple(upcoming_bills)
        savings = tuple(planned_savings)

        def apply_transactions(records: Iterable[Income] | Iterable[Spending]) -> None:
            for record in records:
                record_amount = _money(record.amount, "record amount")
                if record_amount < _ZERO:
                    raise ValueError("record amounts cannot be negative")
                _validate_date(record.date, "record date")
                if record.date > check_date:
                    continue
                if record.account not in balances:
                    issues.append(
                        f"No opening balance is available for account {record.account!r}."
                    )
                    continue
                if record.date >= account_balances[record.account].as_of:
                    balances[record.account] += (
                        record_amount if isinstance(record, Income) else -record_amount
                    )

        apply_transactions(actual_income)
        apply_transactions(actual_spending)

        bill_total = _ZERO
        for bill in bills:
            bill_amount = _money(bill.amount, "bill amount")
            if bill_amount < _ZERO:
                raise ValueError("bill amounts cannot be negative")
            cycle_months = _validate_cycle(bill.cycle)
            _validate_date(bill.date, "bill date")
            if bill.account not in balances:
                issues.append(f"No opening balance is available for account {bill.account!r}.")
                continue
            bill_total += bill_amount * sum(
                1
                for _ in _scheduled_occurrences(
                    bill.date, cycle_months, check_date, purchase_date
                )
            )

        savings_total = _ZERO
        for goal in savings:
            contribution = _money(goal.amount, "savings contribution")
            if contribution < _ZERO:
                raise ValueError("savings contributions cannot be negative")
            cycle_months = _validate_cycle(goal.cycle)
            _validate_date(goal.date, "savings date")
            savings_total += contribution * sum(
                1
                for _ in _scheduled_occurrences(
                    goal.date, cycle_months, check_date, purchase_date
                )
            )

        if issues:
            return PurchaseCheck(
                status="unknown",
                message="Not enough information to check this purchase reliably.",
                estimated_cash=None,
                purchase_amount=purchase_amount,
                remaining_cash=None,
                minimum_reserve=reserve,
                upcoming_bills=None,
                planned_savings=None,
                issues=tuple(dict.fromkeys(issues)),
            )

        cash_before_obligations = sum(balances.values(), _ZERO)
        estimated_cash = cash_before_obligations - bill_total - savings_total
        remaining_cash = estimated_cash - purchase_amount
        if remaining_cash < _ZERO:
            status = "insufficient_funds"
            message = "This purchase exceeds the estimated cash available after obligations."
        elif remaining_cash < reserve:
            status = "reserve_risk"
            message = "This purchase may reduce cash below your minimum reserve."
        else:
            status = "affordable"
            message = "This purchase appears affordable while preserving your minimum reserve."

        return PurchaseCheck(
            status=status,
            message=message,
            estimated_cash=estimated_cash,
            purchase_amount=purchase_amount,
            remaining_cash=remaining_cash,
            minimum_reserve=reserve,
            upcoming_bills=bill_total,
            planned_savings=savings_total,
        )
