# Budget Logbook Kanban

**Board status:** Assumed all work is unstarted. The first three cards are **Ready**; the rest are in **Backlog**. Move a card to In **Progress** when you start it, **Blocked** if it needs a decision or dependency, and **Done** once its acceptance criteria are met.

## Ready

### BUD-01 — Define tracked financial records · Milestone 1

- [x] List record types: income, spending, recurring bills, investments, savings goals, and planned purchases.
- [x] Decide which records need an account, category, date, and optional note.
- [x] Decide how cash and investments are distinguished.

- **Done when:** The record types and their required information are documented.

### BUD-02 — Define affordability rules · Milestone 1

- [ ] Decide how to calculate available cash after upcoming bills and planned savings.
- [ ] Define a user-set minimum cash reserve.
- [ ] Decide how investments are treated in purchase checks.
- [ ] Specify what happens when financial data is missing or outdated.

- **Done when:** The rules are clear enough to apply consistently to a purchase.

### BUD-03 — Define purchase-check recommendations · Milestone 1

- [ ] Choose plain-language outcomes, such as “Looks affordable” or “May put your reserve at risk.”
- [ ] Decide which amounts and obligations to show with each outcome.
- [ ] Write example scenarios and expected results, including irregular income and large purchases.

- **Done when:** Scenarios have clear, explainable expected recommendations.
Backlog

### BUD-04 — Sketch the main user journeys · Milestone 2

- [ ] Map how a user adds records, reviews their budget, and checks a purchase.
- [ ] Include correcting a record and updating a recurring item.

- **Done when:** The main journeys are documented and can be reviewed before implementation.

### BUD-05 — Design the core screens · Milestone 2

- [ ] Sketch an overview, transaction list and form, recurring items, savings goals, and purchase checker.
- [ ] Show how users move between the screens.

- **Done when:** Each MVP task has an obvious place in the proposed experience.
### BUD-06 — Define overview summaries · Milestone 2

- [ ] Specify income and spending for a selected period.
- [ ] Specify how upcoming bills, savings-goal progress, and available-to-spend are shown.

- **Done when:** Each summary has a defined meaning and time period.

### BUD-07 — Create the core data model · Milestone 3

- [ ] Define records for transactions, recurring items, categories, and goals.
- [ ] Include fields needed by the agreed affordability rules.

- **Done when:** The model supports all MVP records and calculations.

### BUD-08 — Build transaction record management · Milestone 3

- [ ] Add, view, edit, and delete financial records.
- [ ] Validate amounts and dates.
- [ ] Confirm destructive actions where appropriate.

- **Done when:** Users can maintain records and receive clear validation feedback.

### BUD-09 — Add recurring income and bills · Milestone 3

- [ ] Support recurring schedules for salary, subscriptions, and other regular items.
- [ ] Make recurrence details clear and editable.

- **Done when:** Upcoming recurring items can be reviewed and updated.

### BUD-10 — Add transaction filtering · Milestone 3

- [ ] Filter records by date range, type, and category.

- **Done when:** Users can find records using each supported filter.

### BUD-11 — Add export and backup · Milestone 3

- [ ] Provide a portable export of user data.
- [ ] Define a dependable backup approach.
- [ ] Document how to restore or recover data.

- **Done when:** Users can retrieve a usable copy of their records and understand how to recover 
them.

### BUD-12 — Build the budget overview · Milestone 4

- [ ] Calculate income and spending for a selected period.
- [ ] Show upcoming bills and savings-goal contributions.
- [ ] Show estimated available-to-spend using the agreed rules.

- **Done when:** Overview figures are consistent with the underlying records.

### BUD-13 — Build the purchase checker · Milestone 4

- [ ] Apply the agreed affordability rules to a planned purchase.
- [ ] Display a plain-language recommendation.
- [ ] Explain the amounts and obligations behind the result.
- [ ] Clearly flag incomplete or outdated information.

- **Done when:** Users can understand both the recommendation and its basis.

### BUD-14 — Test affordability calculations · Milestone 4

- [ ] Test the scenarios defined in BUD-03.
- [ ] Cover boundary cases, upcoming bills, and missing information.
- [ ] Confirm investments are treated according to the agreed policy.

- **Done when:** Results match expected outcomes and uncertainty is not hidden.

### BUD-15 — Test the end-to-end user journeys · Milestone 5

- [ ] Test adding records and recurring items.
- [ ] Test reviewing the overview and checking a purchase.
- [ ] Test editing and deleting records.

- **Done when:** The core journeys work from start to finish.

### BUD-16 — Review date and recurrence edge cases · Milestone 5

- [ ] Check recurring schedules and period boundaries.
- [ ] Check edits to past records and their effect on summaries.

- **Done when:** Calculations remain correct across the supported dates and schedules.

### BUD-17 — Review usability and accessibility · Milestone 5

- [ ] Check mobile usability and accessibility.
- [ ] Review errors and confirmation messages for clarity.

- **Done when:** Users can complete core tasks on supported screen sizes and understand errors.

### BUD-18 — Run a sample-data trial · Milestone 5

- [ ] Enter realistic sample income, expenses, bills, and goals.
- [ ] Review whether summaries and purchase recommendations are understandable.
- [ ] Refine unclear screens or explanations.

- **Done when:** The trial surfaces no unresolved issues that prevent core use.

## Later / Optional

**Keep these out of the MVP unless priorities change:**

- Multiple accounts or household budgets
- Bank transaction import
- Investment performance analysis
- Notifications for bills or budget thresholds
- Custom reports and charts
- Shared household access

**Suggested flow:** Complete BUD-01 through BUD-03 first; use their decisions to guide the screen design and data model before building the overview and purchase checker.