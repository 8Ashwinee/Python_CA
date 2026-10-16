# Budget Logbook — Core Screen Design

This is a low-fidelity, platform-independent screen proposal for BUD-05. It
describes screen contents and navigation; it does not specify visual styling
or implementation. Exact overview calculations and time-period semantics are
defined in [Overview Summary Definitions](./Overview_Summaries.md).

## Navigation

```text
Overview
├── Transactions ── Add / edit transaction
├── Recurring items ── Add / edit recurring income or bill
├── Savings goals ── Add / edit goal
├── Purchase checker ── Check a planned purchase
└── Accounts ── Add / edit account and opening balance
```

The primary navigation provides direct access to Overview, Transactions,
Recurring items, Savings goals, and Purchase checker. Accounts is available
from the account selector wherever an account is needed and from account
management on the Overview. Record details return to the screen that opened
them.

## 1. Overview

```text
Budget Logbook                         [Add record]
[Overview] [Transactions] [Recurring] [Goals] [Purchase check]

Period: [Selected period v]
Income summary             Spending summary
Upcoming bills             Savings-goal progress
Estimated available-to-spend

Accounts                                      [Manage accounts]
  Account name     Balance status     [Edit]

[View transactions] [View recurring items] [Check a purchase]
```

- Shows the period summaries, upcoming obligations, goal progress, and
  available-to-spend estimate.
- Each summary links to the relevant list or detail: transactions, recurring
  items, savings goals, or accounts.
- Provides a prominent route to add a record and to check a purchase.
- Exact figures, definitions, and time periods are specified in
  [Overview Summary Definitions](./Overview_Summaries.md).

## 2. Transaction list and form

```text
Transactions                           [Add income] [Add spending]
[Date filter] [Type filter] [Category filter]

Date       Type       Description       Account       Amount
...        ...        ...               ...           ...
```

Selecting a row opens its saved details for editing or deletion. Add income
and Add spending open the same form with the chosen type preselected.

```text
Add transaction
Type: [Income / Spending]
Amount: [             ]  Date: [             ]
Category: [         v]   Account: [         v] [Manage accounts]
Note (optional): [                           ]
[Cancel]                                  [Save]
```

The form makes required values apparent, displays validation beside the
relevant field, and keeps entered values available for correction. The user
reviews the transaction before saving. Deletion requires confirmation.

## 3. Recurring items

```text
Recurring items                     [Add income] [Add bill]
[All] [Income] [Bills]

Name / category     Amount     Next date     Interval     Account
...                 ...        ...           ...          ...
```

Opening an item shows its amount, category, first or next date, interval,
account, and optional note, with Edit and Delete actions. The add/edit form
shows a preview of the next expected date before saving.

When editing, the user is told which future scheduled entries will be
affected and confirms the change. The policy for already scheduled, unpaid
occurrences remains a product decision noted in [Core User Journeys](./User_Journeys.md);
posted transactions are corrected from the transaction list.

## 4. Savings goals

```text
Savings goals                              [Add goal]

Goal name       Progress toward target       Next contribution
...             ...                          ...
```

Opening a goal shows its target, planned contribution amount and schedule,
and contribution date. Add/edit includes those fields and a goal name. The
goal detail links back to the Overview, where progress is summarized.

## 5. Purchase checker

```text
Purchase checker
Purchase amount: [             ]
Planned date:    [             ]
[Check affordability]

Result
Recommendation and explanation
Estimated cash / upcoming bills / planned savings
Cash remaining after purchase / minimum reserve
[Review accounts] [Review obligations] [Check another purchase]
```

The result area presents the recommendation and its explanation together.
When the information is incomplete or outdated, it identifies the account or
record to review and does not show a reassuring remaining-cash estimate. The
review links open the relevant account, transaction, or recurring item; the
user can return to the checker and run the check again.

## 6. Account setup and editing

```text
Account
Name: [                         ]
Opening balance: [              ]
Balance applies from: [          ]
The opening balance is the amount at the start of this date.
[Cancel]                                  [Save]
```

The account form is reachable from account management and from an account
selector when no suitable account exists. Editing an account makes the saved
opening balance and effective date visible together. The account list shows
whether an opening balance is available and links to edit it.

## Screen coverage

| MVP task | Screen or entry point |
|---|---|
| Review the budget | Overview |
| Add, find, or correct income and spending | Transaction list and form |
| Add or update regular income and bills | Recurring items |
| Review and maintain savings goals | Savings goals |
| Check a planned purchase | Purchase checker |
| Enter or correct an opening balance and effective date | Account setup and editing |
| Move between tasks | Primary navigation, summary links, and record return paths |
