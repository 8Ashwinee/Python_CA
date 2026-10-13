# Budget Logbook — Language-Independent Build Plan

## Objective

Build a personal finance logbook that lets you record income, spending, investments, subscriptions, and savings goals, then gives a clear, explainable estimate of whether a planned purchase fits your budget.

The app should support good decisions—not make them for you. Purchase checks should be guidance based on the information you enter, not financial advice.


## Suggested MVP scope

**Include:**
---
- Income and expense records, including recurring salary and subscriptions
- Categories and transaction history
- A monthly budget overview
- Savings goals and a user-defined minimum cash reserve
- A purchase checker that explains its recommendation
- Data editing, deletion, and export
- Keep bank connections, investment performance analysis, shared accounts, and automatic transaction imports out of the first release.

## Milestones

**Milestone 1 — Define the budget rules**
---

**Objective: Decide what *“Can I afford this?”* means before building calculations.**

**Tasks and subtasks:**

1. Define the financial information the app will track.
    - Distinguish cash and savings from investments.
    - Record income, expenses, recurring bills, savings goals, and planned purchases.
    - Decide whether records are associated with an account, a category, or both.
2. Define the affordability calculation.
    - Estimate cash available after upcoming bills and planned savings.
    - Protect the user’s chosen minimum cash reserve.
    - Treat investments as unavailable for purchases by default.
    - Decide how the app handles missing or outdated information.
3. Define recommendation wording.
    - For example: “Looks affordable,” “This may put your reserve at risk,” or “Not enough information.”
    - Show the amounts and upcoming obligations behind the result.
4. Write example scenarios and expected recommendations.

<code>
Milestone exit: The rules are written down and produce sensible results for common scenarios, including irregular income, upcoming bills, and a purchase larger than available cash.
</code>

**Milestone 2 — Design the core experience**
---

**Objective: Make it easy to add records and understand the current budget.**

Tasks and subtasks:

1. Sketch the main screens.
    - Overview
    - Transaction list and transaction form
    - Recurring income and bills
    - Savings goals
    - Purchase checker
2. Define the information each record requires.
    - Amount, date, type, category, and optional note
    - Recurrence details for salary, subscriptions, and other regular entries
3. Plan useful overview summaries.
    - Income and spending for the selected period
    - Upcoming recurring expenses
    - Progress toward savings goals
    - Estimated available-to-spend amount
4. Review the flow for correcting mistakes and updating recurring records.

<code>
Milestone exit: A user can describe how they would enter their finances, find upcoming obligations, and check a planned purchase without confusion.
</code>

**Milestone 3 — Build the logbook**
---

**Objective: Implement reliable financial record keeping.**

Tasks and subtasks:

1. Create the app’s data model for transactions, recurring items, categories, and goals.
2. Implement creating, viewing, editing, and deleting records.
3. Add basic validation.
    - Reject invalid amounts and dates.
    - Make recurring schedules clear.
    - Confirm destructive actions where appropriate.
4. Add filtering by date range, type, and category.
5. Add export and a dependable backup approach.

<code>
Milestone exit: Users can maintain and review their records, and can retrieve a portable copy of their data.
</code>

**Milestone 4 — Add the budget overview and purchase checker**
---

**Objective: Turn records into useful, understandable guidance.**

Tasks and subtasks:

1. Calculate period income, spending, upcoming bills, and goal contributions.
2. Implement the affordability rules from Milestone 1.
3. Show purchase-check results with a plain-language explanation.
4. Handle incomplete data explicitly instead of presenting a misleading “yes.”
5. Test calculations against the scenarios from Milestone 1, including boundary cases.

<code>
Milestone exit: Recommendations are consistent, explainable, and tested against representative financial situations.
</code>

**Milestone 5 — Validate and release the MVP**
---

**Objective: Make the app dependable and comfortable to use.**

Tasks and subtasks:

1. Test the main user journeys from adding records through checking a purchase.
2. Verify calculations for recurring schedules, date boundaries, and edits to past records.
3. Review accessibility, mobile usability, and error messages.
4. Confirm backup/export works and document how users can recover their data.
5. Run a small trial with realistic sample data and refine unclear screens or recommendations.

<code>
Milestone exit: A user can enter their finances, understand the overview, check a purchase, and recover their data if needed.
</code>

## Later enhancements

**After the MVP is working, consider:**

1. Multiple accounts or household budgets
2. Bank transaction import
3. Investment tracking and performance summaries
4. Notifications for upcoming bills or budget thresholds
5. Custom reports and charts
6. Shared access with another household member

A useful guiding principle for the purchase checker is: **show the calculation and uncertainty, not just a green or red answer.**