import unittest
from datetime import date
from decimal import Decimal

from data_models.record_data import Income, RecurringBills, SavingsGoals, Spending
from helper_utilities.rules_regulations import AccountBalance, FinancialRules


class FinancialRulesTests(unittest.TestCase):
    def setUp(self):
        self.check_date = date(2026, 10, 15)
        self.rules = FinancialRules()
        self.balances = {
            "checking": AccountBalance(Decimal("2000"), date(2026, 10, 1))
        }

    def test_calculates_cash_after_records_bills_savings_and_reserve(self):
        result = self.rules.check_purchase(
            Decimal("400"),
            date(2026, 11, 2),
            self.balances,
            income=[
                Income(500, "salary", date(2026, 10, 10), "checking"),
            ],
            spending=[
                Spending(200, "groceries", date(2026, 10, 12), "checking"),
            ],
            upcoming_bills=[
                RecurringBills(
                    500, "rent", "monthly", date(2026, 10, 20), "checking"
                ),
            ],
            planned_savings=[
                SavingsGoals(
                    300,
                    "savings",
                    "Emergency fund",
                    5000,
                    date(2026, 10, 25),
                    "monthly",
                ),
            ],
            minimum_cash_reserve=1000,
            as_of=self.check_date,
        )

        self.assertEqual(result.status, "affordable")
        self.assertEqual(result.estimated_cash, Decimal("1500"))
        self.assertEqual(result.remaining_cash, Decimal("1100"))
        self.assertEqual(result.upcoming_bills, Decimal("500"))
        self.assertEqual(result.planned_savings, Decimal("300"))

    def test_future_income_is_not_assumed(self):
        result = self.rules.check_purchase(
            2500,
            self.check_date,
            self.balances,
            income=[
                Income(10000, "salary", date(2026, 10, 20), "checking"),
            ],
            as_of=self.check_date,
        )

        self.assertEqual(result.status, "insufficient_funds")
        self.assertEqual(result.estimated_cash, Decimal("2000"))

    def test_purchase_that_breaks_reserve_is_flagged(self):
        result = self.rules.check_purchase(
            1100,
            self.check_date,
            self.balances,
            minimum_cash_reserve=1000,
            as_of=self.check_date,
        )

        self.assertEqual(result.status, "reserve_risk")
        self.assertEqual(result.remaining_cash, Decimal("900"))

    def test_missing_balance_returns_unknown(self):
        result = self.rules.check_purchase(
            100,
            self.check_date,
            {},
            as_of=self.check_date,
        )

        self.assertEqual(result.status, "unknown")
        self.assertIsNone(result.estimated_cash)
        self.assertTrue(result.issues)

    def test_balance_older_than_30_days_returns_unknown(self):
        result = self.rules.check_purchase(
            100,
            self.check_date,
            {"checking": AccountBalance(2000, date(2026, 9, 1))},
            as_of=self.check_date,
        )

        self.assertEqual(result.status, "unknown")
        self.assertIsNone(result.estimated_cash)

    def test_missing_account_for_a_cash_transaction_returns_unknown(self):
        result = self.rules.check_purchase(
            100,
            self.check_date,
            self.balances,
            spending=[
                Spending(50, "food", date(2026, 10, 10), "cash"),
            ],
            as_of=self.check_date,
        )

        self.assertEqual(result.status, "unknown")
        self.assertIsNone(result.estimated_cash)

    def test_invalid_amount_and_cycle_are_rejected(self):
        with self.assertRaises(ValueError):
            self.rules.check_purchase(
                -1, self.check_date, self.balances, as_of=self.check_date
            )

        with self.assertRaises(ValueError):
            self.rules.check_purchase(
                1,
                date(2026, 11, 1),
                self.balances,
                upcoming_bills=[
                    RecurringBills(
                        10, "rent", "weekly", date(2026, 10, 20), "checking"
                    ),
                ],
                as_of=self.check_date,
            )


if __name__ == "__main__":
    unittest.main()
