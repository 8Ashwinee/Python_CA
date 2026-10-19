# Recurring Income, Bills, and Savings Goals — User Experience

This document specifies how users view and manage recurring income,
bills, and savings goals for Issue #12.

## Recurring items list

Provide a Recurring Items screen with these filters:

* All
* Income
* Bills

Each row displays the item name or category, amount, next expected
or due date, recurrence interval, account, and status where available.

Expected income must be clearly distinguished from income already received.
Variable bill amounts must be labelled as estimates.

## Item details and actions

Opening an item displays its saved details and provides Edit and Delete
actions. Ask for confirmation before deleting an item.

The add/edit form must validate required fields and preview the next
expected date before saving.

When a recurring item is edited, explain which future occurrences are
affected and ask the user to confirm. Do not silently modify actual
transactions or previously scheduled unpaid occurrences.

## Savings goals

Provide a Savings Goals screen listing each goal name, target amount,
progress toward the target, and planned contribution schedule when available.

Users can open a goal to review its details and add or edit a goal.
Show planned contributions separately from completed contributions.
A planned contribution must not be represented as a completed transaction.

## Shared behavior

* Support monthly, quarterly, and annual recurrence.
* Keep core viewing and editing available offline.
* Show validation errors clearly and preserve entered values for correction.
* Keep schedules separate from actual financial transactions.
* Do not count expected future income as cash already received.
* Keep goal allocations separate from spendable cash calculations.

## Acceptance criteria

* Users can find recurring income and bills using the list filters.
* Users can inspect, edit, and delete recurring items.
* Users can review and maintain savings goals.
* Schedule estimates and actual transactions are clearly distinguished.
* Editing and deletion behavior is clear to the user.
* The screens follow the existing offline-first requirements.

