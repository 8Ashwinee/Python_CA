# Budget Logbook — Available Cash, Savings, and Investments

This document records proposed requirements for [issue #3](https://github.com/KomeOn/Python_CA/issues/3). It defines product behavior, not implementation.

## Offline-first feasibility

These rules can work offline when users enter account balances, transactions,
allocations, and investment valuations themselves. The app must not imply that
manually entered values are live bank balances or current market prices.

- Calculate balances and projections from locally stored records.
- Do not require bank connections, remote services, market feeds, or exchange
  rates for the core logbook or purchase checker.
- Allow users to enter an investment valuation and its as-of date manually if
  investment values are shown. Mark that valuation as user-entered and stale
  or unavailable when it fails the freshness rule agreed in issue #5.
- Local operation does not itself provide backup or recovery; define export
  and backup separately.

## Definitions

### Cash and available-to-spend

- **Cash balance** is the estimated amount held in a user-entered cash account.
  It is calculated from the opening balance and posted cash transactions on
  or after the balance's effective date.
- **Liquid cash** is cash in accounts the user identifies as accessible for
  spending. Do not assume that a deposit or other product is immediately
  withdrawable; the user must classify its accessibility.
- **Available-to-spend** is an estimate, not an account balance:

  `Estimated cash after known obligations − minimum cash reserve`

  It may be negative. Show the estimated cash and reserve separately so a
  negative result is not mistaken for an account overdraft.
- The minimum reserve is a threshold for purchase recommendations. Do not
  also subtract it as a transaction or obligation.
- Exclude investments, unused credit, and unreceived borrowing from spendable
  cash. Include proceeds from an investment sale only after the user records
  them as settled cash in a cash account.

### Savings

- **Savings goal** is an objective and allocation of funds, not another
  account or source of money.
- **Savings account balance** is cash held in an account. Count it once as
  cash if the user classifies that account as accessible; a goal allocation
  against it does not create additional funds.
- **Goal allocation** labels part of existing cash for a purpose. Allocated
  funds are not available for unrelated purchases, but remain part of the
  account balance and overall assets.
- **Contribution** must be distinguished as planned or completed. A planned
  contribution is a future obligation when due; it is not a completed
  transfer, expense, or increase in savings progress.

### Investments

- **Invested capital** is the recorded cost contributed to holdings, not their
  current value or profit.
- **Current market value** is a dated estimate entered by the user in the
  offline MVP. It is not automatically refreshed.
- **Realized gain or loss** is based on net disposal proceeds compared with
  the applicable cost basis, including relevant fees and adjustments.
- **Unrealized gain or loss** compares a dated market value with adjusted cost
  basis. Show the valuation date and do not describe it as guaranteed return.
- Investment income (such as dividends or interest), fees, and taxes are
  recorded separately from investment purchases and sale proceeds.
- Investment assets are not spendable cash. Record a withdrawal or sale as
  investment activity and separately record the cash received when settled;
  do not count the same proceeds as both investment value and cash.

## Accounting rules

1. Record each real-world movement once. Internal transfers change account
   balances but are not income or spending.
2. A transfer between two cash accounts reduces the source balance and
   increases the destination balance by matching amounts, excluding any fee.
   Record a fee as spending.
3. Moving cash into a savings account or investment account is an asset
   transfer, not automatically an expense. Savings goals and investment
   allocations must not be added to the assets they label.
4. An actual purchase funded from a savings allocation reduces cash and the
   allocation; record the actual spending once. Do not deduct the same amount
   again as a planned purchase or future savings contribution.
5. Expected income does not increase cash or purchase affordability before it
   is received and recorded.
6. Subtract each known unpaid bill or planned savings contribution at most
   once. When an occurrence is recorded as paid or contributed, exclude that
   occurrence from future-obligation totals.
7. Keep actual balances and transactions separate from forecasts and
   hypothetical scenarios. A scenario must not modify the user's records.
8. If required records are missing, inconsistent, or stale, identify the
   issue and do not present an unreliable result as current.

## Purchase-check application

For the existing purchase-check policy:

- Start from cash balances estimated from valid opening balances and recorded
  income and spending through the check date.
- Exclude investments and future income.
- Subtract unpaid bills and planned savings contributions due after the check
  date and through the planned purchase date.
- Compare the remaining estimated cash after the purchase with the minimum
  reserve. Do not deduct the reserve twice.
- Apply issue #5's account-balance freshness and missing-data rules. Investment
  valuations are not needed for the MVP purchase check.

## Scope for this milestone

The issue's principles are sound, but its current wording is too broad to
implement without further decisions. In particular, detailed portfolio
performance, historical valuations, investment liabilities, scenario analysis,
pending bank transactions, and automatic data refreshes exceed the offline
purchase-check MVP. Keep those out of scope unless a later issue defines them.

Resolve these policy questions before implementation:

- Which account types count as accessible liquid cash, and how should users
  represent locked or restricted savings?
- Are savings allocations tracked against cash accounts, savings goals, or
  both, and how does the app prevent their total from exceeding the underlying
  cash?
- How are pending card transactions and other unsettled cash outflows entered
  and treated?
- What minimum investment information is required in the MVP, if any? The
  purchase checker can exclude investment tracking entirely.
- What freshness threshold applies to manually entered investment valuations?
  Do not assume issue #5's cash-balance threshold automatically applies.

## Acceptance criteria

- Cash balances, savings allocations, and investment values are distinct and
  are not added together as duplicate funds.
- Transfers, goal allocations, planned contributions, investment purchases,
  and investment sale proceeds have explicit treatment and cannot silently
  inflate income, spending, or available cash.
- The purchase checker uses only locally available cash and known obligations,
  excludes investments and unreceived income, and compares its result with
  the reserve exactly once.
- Offline results identify their data basis and do not imply live balances or
  market valuations.
- The outstanding policy questions above are resolved or explicitly deferred
  before implementing the affected behavior.
