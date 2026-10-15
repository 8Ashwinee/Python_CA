"""Budget record models.

Cash vs investment distinction:
- Cash records (income, spending, recurring bills) affect available spendable cash.
- Investment records are tracked separately because they are not the same as liquid cash.
- Savings goals and planned purchases are planning records; they are not bank transactions
  unless they are tied to a real payment.

Shared policy:
- All records must record the date of the item or plan.
- `category` identifies the kind of entry (salary, groceries, mortgage, brokerage, etc.).
- `account` is required for cash entries and optional for investment entries.
- `transaction_id` is optional because planned or estimated entries may not have one yet.
- `optional_note` is optional for all record types.
"""

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Income:
    """Cash inflow into a financial account."""

    amount: float  # Amount credited
    category: str  # Income category, e.g. salary, freelance, refund
    date: date  # Date the income was received
    account: str  # Account receiving the funds
    transaction_id: Optional[str] = None  # External transaction or ledger ID if available
    optional_note: Optional[str] = None  # Optional details about the income


@dataclass
class Spending:
    """Cash outflow from an account."""

    amount: float  # Amount spent
    category: str  # Spend category, e.g. groceries, rent, travel
    date: date  # Date the purchase or payment occurred
    account: str  # Account funding the spend
    transaction_id: Optional[str] = None  # External transaction or ledger ID if available
    optional_note: Optional[str] = None  # Spend reason or extra information


@dataclass
class RecurringBills:
    """Regular cash bills that repeat on a schedule."""

    amount: float  # Amount due each cycle
    category: str  # Bill category, e.g. rent, internet, insurance
    cycle: str  # Bill cycle: monthly, quarterly, annually
    date: date  # Due date or first payment date
    account: str  # Account funding the recurring bill
    transaction_id: Optional[str] = None  # External transaction or ledger ID if available
    optional_note: Optional[str] = None  # Extra information


@dataclass
class Investments:
    """Investment contributions tracked separately from liquid cash."""

    amount: float  # Amount invested
    category: str  # Investment type, e.g. retirement, brokerage, ETF
    cycle: str  # Investment cycle: monthly, quarterly, annually
    date: date  # Investment date or scheduled contribution date
    investment_firm: str  # Investment company or brokerage
    account: Optional[str] = None  # Optional account or fund name backing the investment
    transaction_id: Optional[str] = None  # External transaction or ledger ID if available
    optional_note: Optional[str] = None  # Extra information


@dataclass
class SavingsGoals:
    """Planned savings target and contribution model."""

    amount: float  # Planned contribution per cycle
    category: str  # Savings goal category, e.g. emergency fund, vacation
    goal_name: str  # Name of the goal being saved for
    target_amount: float  # Total amount the goal is expected to reach
    date: date  # Date for the goal plan or next review
    cycle: str  # Savings cycle: monthly, quarterly, annually
    fixed_years: Optional[int] = None  # Optional number of years the plan is locked in
    suggested_savings: Optional[float] = None  # Suggested contribution based on inflation, market, and deposits
    suggested_savings_note: Optional[str] = None  # Explanation of the suggested savings
    transaction_id: Optional[str] = None  # Optional external reference for an actual transfer
    optional_note: Optional[str] = None  # Extra context for the goal


@dataclass
class PlannedPurchases:
    """Planned purchase that may depend on available cash and affordability rules."""

    amount: float  # Amount of the planned purchase
    category: str  # Planned purchase category, e.g. car, electronics, travel
    date: date  # Planned purchase date
    plan: str  # Plan type or purchase strategy
    transaction_id: Optional[str] = None  # Optional external reference for a scheduled payment
    optional_note: Optional[str] = None  # Explanation of the plan