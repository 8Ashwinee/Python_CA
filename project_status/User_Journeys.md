# Budget Logbook — Core User Journeys

These journeys describe the proposed user experience for Milestone 2. They are
flow descriptions, not screen mockups; the screen layout and navigation are
covered in [Core Screen Design](./Core_Screen_Design.md).

## Shared record conventions

- Cash entries are associated with an account and have an amount, date, type,
  and category. A note is optional.
- Regular income and bills also have recurrence details. The currently agreed
  recurrence intervals are monthly, quarterly, and annually.
- Savings goals record a goal name, target amount, contribution amount, date,
  and contribution interval.
- Investments are tracked separately from spendable cash. A planned purchase
  records its amount and planned date.
- An account's opening balance is entered by the user and applies from the
  start of its effective date.

## 1. Set up an account

1. The user chooses to add an account and enters its name, opening balance, and
   the date that balance applies from.
2. The form explains that the balance is a start-of-day amount. The user can
   correct either the amount or date before saving.
3. After saving, the account is available when the user records cash income,
   spending, or bills.
4. If no balance has been entered, the user can still record information, but
   the purchase checker must identify the missing balance and return “Not
   enough information” rather than imply that an estimate is reliable.

## 2. Add income or spending

1. From the overview or transaction list, the user chooses to add income or
   spending.
2. The user enters the amount, date, category, and account, and optionally a
   note. The type is clear from the chosen action and can be reviewed before
   saving.
3. The form identifies missing or invalid required values and keeps the user
   in the form to correct them.
4. On save, the new entry appears in the transaction list and is reflected in
   the relevant overview period and subsequent purchase checks.

## 3. Add or update regular income and bills

1. From the recurring-items area, the user chooses to add regular income or a
   bill.
2. The user enters the amount, category, first payment or due date, recurrence
   interval, and account; a note is optional.
3. The user reviews the interval and next expected date before saving.
   Upcoming items are then available to review alongside one-time entries.
4. To update an item, the user opens it from the recurring-items area, changes
   its details, reviews which future entries will be affected, and confirms
   the change. The upcoming list and future estimates are refreshed.

   **Policy to settle before implementation:** Decide whether editing a
   recurring item changes only future occurrences or also changes already
   scheduled, unpaid occurrences. A recurrence edit should not silently rewrite
   past posted transactions; those are corrected through the transaction
   journey below.

## 4. Review the budget and savings goals

1. The user opens the overview and selects the period they want to review.
2. The overview helps the user find income and spending for that period,
   upcoming bills, and progress toward savings goals.
3. To add a goal, the user enters its name, target amount, planned contribution,
   contribution date and interval, then saves it. The goal is available to
   review from the overview.
4. The user can move from an upcoming bill or savings goal to its details to
   understand the amount and timing behind the summary.

## 5. Check a planned purchase

1. The user opens the purchase checker and enters the purchase amount and
   planned date, then starts the check.
2. The result explains the recommendation and, when the underlying data is
   reliable, shows estimated cash, upcoming bills, planned savings
   contributions, cash remaining after the purchase, and the user's minimum
   reserve.
3. The calculation uses recorded income and spending on or after each
   opening-balance date through the check date. It deducts scheduled bills and
   savings contributions due after the check date and through the purchase
   date. It does not assume future income, and excludes investments from
   spendable cash.
4. If an opening balance is missing, future-dated, or more than 30 days old,
   or a cash record refers to an account without an opening balance, the
   checker explains the issue and returns “Not enough information.” It does
   not show a reassuring remaining-cash estimate.
5. The user can follow the explanation back to the relevant account, entry, or
   recurring item, correct it, and run the check again.

## 6. Correct an existing transaction

1. The user finds the transaction in the transaction list and opens it for
   editing.
2. The form shows the saved amount, date, type, category, account, and note.
   The user corrects the mistaken values and reviews the changes.
3. On save, the corrected transaction replaces the previous values in the
   record. The overview and subsequent purchase checks use the corrected
   record, including when its date or account changes.
4. If the user decides the transaction should not exist, they use the
   transaction's delete action and confirm before it is removed.

## Journey handoff

The user can start by entering account balances, add one-time and recurring
records, review the overview, and check a purchase. When something is wrong or
stale, the user can return to the relevant record, correct it, and repeat the
check. The recurring-edit policy above needs a product decision before that
flow is implemented.
