# Budget Logbook — Overview Summary Definitions

This specification defines the Overview figures for BUD-06. It describes
summary behavior, not implementation. The available-to-spend estimate follows
the affordability rules in the project plan and purchase-check
recommendations.

## Selected-period income and spending

- The default period is the current calendar month. The user can select a
  custom date range.
- Both ends of the selected range are inclusive.
- Income and spending are separate totals of recorded cash transactions dated
  within the selected range. They are not netted together.
- Only transactions already recorded as received or spent count. Expected
  recurring income and unpaid scheduled bills do not count in these totals.
- Investments are excluded.
- Changing the selected period does not change the upcoming-obligations or
  available-to-spend windows.

## Upcoming bills and planned savings

- Show unpaid scheduled bills and planned savings-goal contributions due from
  tomorrow through 30 calendar days after today, inclusive.
- Show bills and planned contributions separately, with their due dates and
  amounts; do not combine them into a single unlabeled total.
- Exclude an occurrence already represented by a recorded transaction, so a
  paid bill or completed contribution is not counted twice.
- These figures use a rolling 30-day window and do not depend on the selected
  income-and-spending period.

## Savings-goal progress

- For each goal, show the amount of recorded contributions credited to it
  through today, the target amount, and the percentage of the target reached.
- Future planned contributions are not completed progress; show them only in
  the upcoming-savings summary.
- Contributions must be attributable to a goal. The data model must support
  linking a recorded contribution to its goal; otherwise, the overview cannot
  claim an accurate per-goal progress figure.

## Estimated available-to-spend

- This is a rolling estimate as of today, independent of the selected
  income-and-spending period.
- Start with cash balances estimated from each account's opening balance and
  recorded income and spending dated on or after that balance's effective
  date, through today. Exclude investments.
- Subtract unpaid scheduled bills and planned savings contributions due from
  tomorrow through 30 calendar days after today. Do not assume future income.
- Subtract the user's minimum cash reserve from the estimated cash remaining
  after those obligations. The result is available-to-spend; a negative result
  indicates how far the estimate falls below the reserve, not an amount that
  can be spent.
- Show the estimated cash after obligations and the minimum reserve alongside
  the result, so users can understand its basis.
- Follow the purchase-check data-quality rules: if a required opening balance
  is missing, future-dated, or more than 30 days old, or a cash record cannot
  be reconciled to an account with a valid opening balance, do not present a
  reliable available-to-spend amount. Identify the data that needs attention.

## Data-model handoff

Implementation needs to distinguish recorded transactions from unpaid
scheduled occurrences, avoid counting a scheduled occurrence after it has
been recorded, and associate recorded savings contributions with goals.
Define the necessary links/statuses in BUD-07 before implementing these
summaries in BUD-12.
