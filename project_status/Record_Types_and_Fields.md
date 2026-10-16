# Budget Logbook — Record Types and Fields

This document records the proposed data requirements for issue #2. It is a
requirements document, not an implementation specification.

## Offline-first requirements

- Core record creation, viewing, editing, deletion, and purchase checks must
  work without an internet connection.
- Users enter and maintain financial information themselves. The MVP does not
  connect to banks, import transactions, or require a remote service.
- Records and any optional receipt files are stored locally. A receipt must
  not be required to create or understand a financial record.
- Expected schedules and reminders are calculated from locally stored data.
  A reminder may use the device's local notification facility; it must not
  depend on a server or an internet connection.
- Investment prices, currency exchange rates, and other external data are not
  fetched automatically. Any later investment valuation must be entered by
  the user or clearly identified as unavailable while offline.
- Offline operation does not by itself guarantee backup or recovery. Export
  and backup behavior must be specified separately.

## Shared conventions

- Store an amount with an explicit currency. The MVP should use one selected
  currency consistently; it must not add unlike currencies together or imply
  an exchange-rate conversion.
- Use dates for financial event dates and due dates. A schedule is a plan, not
  proof that a payment occurred.
- Distinguish actual events (received, spent, transferred, or contributed)
  from expected or planned events.
- Associate cash activity with the relevant account. An account's opening
  balance includes the date from which that balance applies.
- Give each record a category or clear type where it helps users understand
  the entry. Notes are optional.
- Do not count an internal transfer as income or spending. Do not count a
  planned goal contribution as a completed transaction.
- Keep investment balances separate from spendable cash. Do not treat
  investment purchases as ordinary consumption spending.

## MVP record types

### Account

An account provides context for a cash balance and cash activity.

| Field | Requirement |
| --- | --- |
| Name | Required; user-entered account label |
| Opening balance | Required to make a reliable cash estimate |
| Balance effective date | Required; identifies when the opening balance applies |
| Currency | Required and consistent with MVP currency |

An account is maintained manually in the offline MVP. It does not imply a
linked bank account or a live balance.

### Income

Income records money actually received. Expected future income belongs to a
recurring schedule, not to actual received income.

| Field | Requirement |
| --- | --- |
| Amount | Required; greater than zero |
| Received date | Required |
| Category/source | Required category; source may be included in the description |
| Receiving account | Required |
| Note | Optional |

Do not include an expected payment in available cash until the user records it
as received.

### Spending

Spending records money actually paid for goods, services, or charges.

| Field | Requirement |
| --- | --- |
| Amount | Required; greater than zero |
| Payment date | Required |
| Category | Required |
| Paying account | Required |
| Payment method | Optional for the MVP |
| Note | Optional |

If refunds are supported, link them to the original spending record and keep
their amount and date explicit. Do not silently change the original payment.

### Recurring income and bills

A recurring record describes expected future occurrences. Each occurrence
must remain distinguishable from the actual income or spending transaction
that may later record it.

| Field | Requirement |
| --- | --- |
| Type | Required: expected income or bill |
| Amount | Required; for variable bills, a user-entered estimate |
| Category | Required |
| Account | Required for cash records |
| First/next date | Required |
| Frequency | Required; MVP supports monthly, quarterly, and annually |
| End date | Optional |
| Status | Active, paused, or cancelled |
| Note | Optional |

The app can calculate upcoming dates locally. It must not count an expected
income occurrence as cash, and must not count a bill twice after its actual
payment has been recorded. Variable amounts and edits to already scheduled
occurrences need explicit handling before implementation.

### Savings goal

A savings goal is a target, not a separate cash account or transaction.

| Field | Requirement |
| --- | --- |
| Name | Required |
| Target amount | Required; greater than zero |
| Target date | Optional |
| Priority | Optional |
| Planned contribution amount and frequency | Optional |
| Actual contribution link | Needed to calculate progress from recorded activity |

Show planned contributions separately from completed contributions. Do not
count a planned contribution as cash already moved or as spending already
paid.

### Planned purchase

A planned purchase represents a possible future expense and is not an actual
spending record until completed.

| Field | Requirement |
| --- | --- |
| Item or description | Required |
| Estimated amount | Required; greater than zero |
| Planned date | Required |
| Priority | Optional |
| Status | Planned, postponed, cancelled, on hold, or completed |
| Note | Optional |

The purchase checker uses its amount and date with the locally entered cash
and obligations. When completed, record the actual spending separately so the
plan is not counted again.

## Later or separately scoped record types

These record types are possible in an offline application when entered
manually, but are not required for the purchase-check MVP described by the
project plan. Add them only after their balance and cash-flow rules are agreed.

### Transfers

A transfer records money moved between two accounts owned by the user. It
needs a source account, destination account, amount, and date. It must not
increase income or spending totals. Any fee is a separate spending record.
Transfers between an account and an investment account need an explicit rule
so that cash is not counted twice.

### Investments

An investment record may include the instrument, account or provider,
quantity, acquisition date, cost, and fees. Investment purchases are not
ordinary spending, and sale proceeds are not wholly income. Market valuation
and performance reporting require price data; in an offline-first design such
data must be entered by the user or omitted, not presented as live.

### Debts and liabilities

A liability may include the lender, original principal, current balance,
interest rate, repayment schedule, due date, and status. A manually maintained
balance can be used offline. Forecast interest and repayment projections
require agreed assumptions and are outside the MVP.

## Scope and consistency notes for issue #2

- The issue's full list of eight types is broader than the project's stated
  MVP. Accounts, income, spending, recurring bills/income, savings goals, and
  planned purchases directly support the purchase checker; investments,
  transfers, and debts need separate scope and calculation rules.
- Market valuation, investment performance, automatic imports, cloud sync,
  and server-based reminders are not prerequisites for offline record
  keeping. They must not be implied by the MVP requirements.
- The issue allows expected income in projections, while the purchase-check
  rules say not to assume future income. Keep expected income visible as a
  schedule, but exclude it from purchase affordability until received unless
  that policy is explicitly changed.
- The issue's daily and weekly recurrence options are not needed by the
  current MVP plan, which defines monthly, quarterly, and annual recurrence.
- The issue should define the required fields and the distinction between
  actual and planned records; detailed investment, liability, alert, and
  scenario-analysis behavior can be deferred to later tickets.

## Acceptance criteria

- Each MVP record type has a clear purpose and required fields.
- Actual, expected, and planned financial activity are distinguishable.
- Transfers, goals, investments, and planned purchases cannot silently
  double-count cash, income, or spending.
- The core logbook and purchase-check requirements do not require internet
  access or external financial data.
- Any value that cannot be determined from locally stored, user-entered data
  is identified as unavailable or uncertain rather than shown as current.
