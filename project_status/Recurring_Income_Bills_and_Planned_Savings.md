# Budget Logbook — Recurring Income, Bills, and Planned Savings

This document records proposed requirements for [issue #4](https://github.com/KomeOn/Python_CA/issues/4). It defines product behavior, not implementation.

## Offline-first feasibility

Recurring schedules and their projections can work offline using schedules
entered and maintained by the user. The app does not need a bank connection,
external data feed, or server to calculate dates and estimates.

- Store schedule details locally and calculate due dates on the device.
- Treat a schedule as an estimate or commitment, not evidence that money was
  received or paid.
- Let users update, pause, or cancel schedules and correct actual transactions.
- Do not promise that a reminder will fire while the app or device is
  unavailable; use local notifications only if supported.
- Clearly label user-entered amounts and estimates. For variable bills, do not
  imply the estimate is the final amount.

## Recurring income

- A recurring-income schedule records an expected amount, frequency, next
  expected date, and receiving account. An optional end date, category/source,
  confidence (confirmed or estimated), and note may also be recorded.
- Use the amount the user expects to receive in the account (net amount).
  Do not calculate taxes, deductions, or withholdings.
- Keep expected occurrences separate from actual income transactions.
  Recording received income must satisfy or link to its scheduled occurrence
  so the same receipt is not counted twice.
- Do not classify transfers, loans, or investment-sale proceeds as recurring
  income.
- A schedule may be displayed in a cash-flow forecast, but the purchase-check
  policy in [Purchase-check recommendations](./Purchase_Check_Recommendations.md)
  excludes future income until it has actually been received and recorded.
  Issue #4's request to include expected income in future affordability
  conflicts with that existing policy. Keep this exclusion for the MVP unless
  issue #5 or a product decision explicitly changes it. Never mix expected
  income into a result that is presented as current available cash.

## Bills

- A bill schedule records a category or payee, amount or estimate, frequency,
  next due date, payment account, and status. Optional fields include start
  date, end date, note, and whether the commitment is essential or optional.
- For a variable bill, store a user-entered estimate and label it as such.
  The actual paid amount is recorded separately.
- Count only unpaid occurrences due within the calculation's time window.
  When the actual payment is recorded, link it to the occurrence and remove
  that occurrence from unpaid projections.
- Do not deduct an occurrence again if its payment is already represented in
  the opening balance or posted transactions.
- A bill can contain both expense and non-expense components, such as loan
  interest and principal. The MVP may treat the full payment as a cash
  obligation for affordability; any expense-vs-principal breakdown requires
  separate data and rules.

## Planned savings

- A savings plan records a goal (if applicable), intended amount, frequency,
  next contribution date, and status. An optional target amount/date and note
  may also be recorded.
- A planned contribution is an allocation/commitment, not an expense, income,
  or completed transfer.
- For affordability, count an unpaid planned contribution once when it falls
  within the calculation window. When the contribution is completed, link it
  to its planned occurrence and record the actual movement once.
- A contribution can be assigned to at most one goal occurrence. A goal
  allocation labels existing funds and must not create additional cash.
- Savings held in locked or inaccessible accounts cannot be assumed available
  to pay a bill or emergency. A withdrawal must be explicitly recorded and
  treated as available only when the funds are accessible in a cash account.

## Calculation periods and no-double-counting rules

- Every projection must state its as-of date and end date.
- For a purchase check, follow the existing policy: start with balances
  reconciled from valid opening balances and actual income/spending through
  the check date; subtract unpaid bills and planned savings contributions
  due after the check date and through the planned purchase date; exclude
  future income.
- For a general cash-flow forecast, show scheduled income and obligations by
  their occurrence dates, but label them as forecast rather than actual.
  Do not add a forecast occurrence when the same amount is already reflected
  in the opening balance or a posted transaction.
- If a scheduled occurrence cannot be reconciled with an actual transaction,
  flag it for review rather than silently counting or dropping it.
- Avoid subtracting the same commitment as both a recurring bill and a
  separate planned commitment. A minimum cash reserve is a comparison
  threshold, not another transaction or bill.
- Hypothetical changes to a schedule or release of savings must not modify
  actual records unless the user explicitly saves those changes.

For a cash-flow forecast that includes future income, the conceptual formula
for a selected period is:

`Projected surplus = opening cash + scheduled income received/expected in period`
`− unpaid bills due in period − planned savings contributions due in period`
`− other distinct planned cash commitments in period`

This forecast is not the purchase-check calculation. It must not be presented
as spendable cash without the purchase-check data-quality rules and the
explicit future-income policy.

## Emergency handling

The issue's emergency workflow is feasible offline, but requires an explicit
user action to release savings; a projection must not assume locked or
goal-allocated funds can be withdrawn immediately. The MVP may record the
emergency expense and any actual withdrawal as ordinary linked records. A
special emergency workflow and shortfall alerts can be deferred.

## Scope and decisions

The issue's core distinction between schedules and actual transactions is
correct and offline-friendly. Resolve or defer these points before
implementation:

- Whether future recurring income may affect any affordability recommendation
  (it is excluded from purchase checks by the existing policy).
- Which recurrence frequencies the MVP supports; existing project rules
  specify monthly, quarterly, and annually, not arbitrary daily or weekly
  schedules.
- How variable bill estimates are chosen and refreshed.
- How a scheduled occurrence is linked to a payment or contribution, and how
  edits, cancellations, partial payments, and missed occurrences are handled.
- Whether bills with principal and interest are broken down in the MVP or
  treated as a single cash obligation.
- Whether emergency releases are a separate workflow or ordinary account
  transfers and spending records.

## Acceptance criteria

- Recurring income, bills, and planned savings are user-maintained schedules
  that work without internet access and are clearly distinguished from actual
  transactions.
- Occurrences are counted at most once; a completed occurrence is reconciled
  with its actual transaction.
- Projections use an explicit time period, exclude already-paid obligations,
  and identify estimates and missing or inconsistent data.
- The purchase checker excludes unreceived future income and deducts only
  unpaid bills and planned savings due before the planned purchase.
- Savings releases do not create income and are treated as available only
  when accessible funds are explicitly recorded.
- Product decisions that change the existing purchase-check policy are
  resolved before the affected behavior is implemented.
