# Budget Logbook — Recommendation Outcomes and Explanations

This document records proposed requirements for
[issue #6](https://github.com/KomeOn/Python_CA/issues/6). It defines the
offline MVP's user-facing purchase-check result, not financial advice or
implementation.

## Feasibility and scope

Clear recommendations are feasible offline. The app can explain a result
using locally stored, user-entered data and the calculation in
[Purchase Affordability and Data Freshness](./Purchase_Affordability_and_Data_Freshness.md).
It must not imply access to live bank balances, market data, or expert
financial advice.

Issue #6's principles are useful: explain the reason, show relevant amounts,
identify uncertainty, and never make a financial change on the user's behalf.
Its eight proposed outcomes, configurable ranking, detailed goal/investment
trade-offs, and alternative planning are too broad for the current MVP and
conflict with the four outcomes already specified in
[Purchase-check recommendations](./Purchase_Check_Recommendations.md).
Use the established four outcomes for the MVP; consider richer planning
outcomes only after the underlying rules and inputs are agreed.

## MVP outcomes

| Outcome | When to show | Suggested wording |
| --- | --- | --- |
| `affordable` | Required data is usable, the purchase cost is covered, and estimated cash after the purchase is at least the minimum reserve. | “This purchase appears affordable while preserving your minimum reserve.” |
| `reserve_risk` | Required data is usable and the purchase cost is covered, but estimated cash after the purchase is below the minimum reserve. | “This purchase may reduce cash below your minimum reserve.” |
| `insufficient_funds` | Required data is usable, but the purchase cost exceeds estimated cash after known obligations. | “This purchase exceeds the estimated cash available after obligations.” |
| `unknown` | Critical data is missing, stale, or inconsistent, so a reliable result cannot be calculated. | “Not enough information to check this purchase reliably.” |

Apply outcomes in this order:

1. If critical inputs fail validation or freshness checks, show `unknown`.
2. If estimated cash after known obligations and the purchase is negative,
   show `insufficient_funds`.
3. Otherwise, if that remaining cash is below the minimum reserve, show
   `reserve_risk`.
4. Otherwise, show `affordable`.

Exactly meeting the reserve is `affordable`. A positive amount below the
reserve is `reserve_risk`. A negative remaining amount is `insufficient_funds`,
even though it also falls below the reserve.

Do not add “Affordable with caution” to the MVP: it needs an agreed threshold,
whereas the reserve already provides a concrete boundary. “Save first,”
“Postpone,” “Reduce purchase cost,” and “Reallocate eligible funds” describe
possible planning actions rather than distinct calculation outcomes. In the
MVP, show the applicable result and relevant shortfall or reserve amount;
users decide what to do next.

## Explanation contents

For `affordable`, `reserve_risk`, or `insufficient_funds`, show:

- Outcome and short plain-language reason.
- Planned purchase amount, date, and whether the amount is estimated.
- Cash estimate at the check date, and unpaid bills and planned savings
  contributions due before the purchase, shown separately.
- Estimated cash after those obligations and after the purchase.
- User's minimum reserve and, where useful, the amount above or below it.
- A note that future income and investments are excluded from the MVP
  purchase check.
- Any estimates or other material limitations affecting the result.

For `unknown`, show the purchase amount and date, the outcome, and each
specific data problem to resolve (for example, a missing opening balance, a
balance older than 30 days, or a cash record that cannot be matched to an
account). Do not show an unsupported cash-after-purchase estimate or
reassuring recommendation.

Only include figures that affect the result. Keep amounts in the same
currency, label estimates, and use the same evaluation date and assumptions
as the calculation. Do not claim that a fresh entry is necessarily correct.

## Trade-offs and actions

- The checker may explain that reducing the purchase amount or postponing it
  could change the result, but the MVP does not need to calculate an
  alternative purchase plan or predict a future affordable date.
- Do not assume future income, future savings accumulation, or investment
  returns to make a purchase appear affordable.
- Do not propose releasing protected savings or changing bills, goals, or
  investment contributions unless those rules are explicitly supported and
  the source, destination, amount, and consequences can be calculated.
- Recommendations must never execute a transfer, withdrawal, cancellation,
  or other financial change. Any future supported adjustment requires an
  explicit user action and confirmation.
- Present results as estimates and guidance, not guarantees or personalized
  financial advice.

## Offline and data-quality behavior

- Generate the explanation entirely from locally available records and the
  purchase-check result.
- Identify locally entered data as user-provided; do not imply it was
  synchronized or independently verified.
- Use the freshness and required-data rules in
  [Purchase Affordability and Data Freshness](./Purchase_Affordability_and_Data_Freshness.md).
- Missing or stale critical data must produce `unknown`, not a definitive
  “affordable” or “not affordable” outcome.
- A variable bill or estimated purchase cost may be used only if clearly
  identified as estimated and the result remains appropriately qualified.

## Example

Suppose the purchase costs 400, cash after known obligations is 1,500, and
the minimum reserve is 1,000. The estimated cash after purchase is 1,100,
which is 100 above the reserve. The result is `affordable`; the explanation
shows each amount and states that it is based on user-entered information.

If the same purchase left 900, the result is `reserve_risk` and the
explanation says it would leave cash 100 below the reserve. If cash after
known obligations were only 300, the result is `insufficient_funds` and the
shortfall against the purchase price is 100. If the balance data were stale,
the result is `unknown` instead, without presenting those calculations as
reliable.

## Acceptance criteria

- Every result maps to one of the four defined MVP outcomes and follows the
  stated precedence and boundary rules.
- The explanation gives the relevant amounts and the reason for the outcome,
  using the same inputs and assumptions as the calculation.
- `unknown` identifies actionable data-quality problems and does not display
  a reliable-looking remaining-cash estimate.
- Future income, investments, and hypothetical reallocations do not
  strengthen an MVP purchase recommendation.
- The app makes no financial changes based on a recommendation and does not
  present the result as a guarantee or financial advice.
- All outcomes and explanations can be produced without an internet
  connection.
