# Budget Logbook — Purchase Affordability and Data Freshness

This document records proposed requirements for
[issue #5](https://github.com/KomeOn/Python_CA/issues/5). It defines the MVP
purchase-check behavior, not its implementation.

## Offline-first feasibility

The calculation is feasible offline because it can use locally stored,
user-entered account balances, transactions, obligations, savings plans, and
purchase details. It does not require bank synchronization, market data, or a
remote service.

- Treat all inputs as user-entered records, not live bank data.
- Let the user confirm or correct balances and obligations locally.
- Do not claim that fresh data is necessarily accurate; freshness indicates
  only when the user last confirmed it.
- Do not make a recent app launch or recalculation count as confirmation.
- Store the evaluation date, input values or references, and assumptions for
  the result shown. Durable history of past checks can be deferred if it is
  outside the MVP.

## MVP calculation

Use one currency and one purchase date. Reject or request correction of a
missing, non-positive, or invalid purchase amount/date. The purchase amount
must include mandatory taxes, fees, delivery, and other costs when known; if
the total is only estimated, label it as an estimate.

For each accessible cash account, estimate cash at the check date using the
opening balance and recorded income/spending dated on or after its effective
date through the check date. Require the account opening balance and its
effective date to pass the freshness and consistency checks below.

Let:

- `C` = estimated eligible cash across valid accessible cash accounts at the
  check date.
- `B` = unpaid bills due after the check date and on or before the purchase
  date.
- `S` = planned savings contributions due after the check date and on or
  before the purchase date, not already included in `B` or `C`.
- `P` = total estimated purchase cost.
- `R` = user-defined minimum cash reserve.

Calculate:

```text
Cash before purchase = C − B − S
Cash after purchase = C − B − S − P
Purchase margin = Cash after purchase − R
```

Do not include expected income, investments, unused credit, or unreceived
borrowing in `C`. A savings release may be considered only after the user
explicitly records that funds are released and available in an eligible cash
account. A reserve is a comparison threshold: subtract it once in the margin,
not again as a bill or transaction.

Count an obligation only if it is not already reflected in the opening
balance or posted transactions. Reconcile paid bills and completed
contributions to their scheduled occurrences to prevent double-counting.
Investment contributions are not part of the MVP calculation unless the user
has explicitly decided to include them as a due commitment; if included, count
each only once.

## Result interpretation

This calculation is consistent with
[Purchase-check recommendations](./Purchase_Check_Recommendations.md):

- **Affordable:** data is usable, `Cash after purchase >= R`, and the
  purchase cost is covered.
- **Reserve risk:** data is usable, the purchase cost is covered, but
  `Cash after purchase < R`.
- **Insufficient funds:** data is usable, but the purchase cost exceeds cash
  remaining after known obligations (`Cash after purchase < 0`).
- **Unknown:** required data is missing, stale, or inconsistent; do not show
  cash-after-purchase as a reliable figure.

Boundary policy: a purchase leaving exactly the reserve is affordable. A
purchase leaving exactly zero but below the reserve is reserve risk, not
insufficient funds. If issue #6 adopts different labels, keep these
underlying distinctions and update the wording consistently.

The proposed issue statuses “Affordable with caution” and “Insufficient data”
do not match the existing four statuses. Do not add a configurable caution
threshold in the MVP; it adds a policy and setting without being needed for
the existing rules. Agree any status changes with issue #6 before
implementation.

## Data freshness and validation

Freshness is evaluated only for inputs used by this purchase check, not by
averaging all financial records in the logbook.

### Required data checks

- **Cash balance:** each cash account used must have a user-entered opening
  balance and effective date; the balance must not be future-dated or more
  than 30 calendar days old on the check date.
- **Transactions:** cash transactions must have valid amounts, dates, and
  accounts whose balances can be reconciled. Transactions before an account's
  opening-balance effective date must not silently affect that balance.
- **Bills and savings contributions:** scheduled amounts and due dates must be
  known through the purchase date, and paid/completed occurrences must be
  distinguishable from unpaid ones. Variable amounts may be estimates but
  must be labelled.
- **Reserve:** the user's minimum reserve must be known and in the same
  currency.
- **Purchase:** amount, date, and any estimated mandatory costs must be
  disclosed.

If a required balance is older than 30 days, future-dated, missing, or cannot
be reconciled to the cash transactions, return `unknown`, name the data issue,
and direct the user to review or re-enter the balance. Do not infer a
reassuring available-cash amount. Optional information not used in this
calculation (for example, investment market valuations) must not make the
purchase check appear stale.

The 30-day threshold is the existing purchase-check policy. Review
frequencies for other record types in issue #5 are guidance, not an automatic
reason to block this calculation. Revisit any thresholds as explicit product
decisions rather than deriving them from update-frequency ratios.

## Conflicts and scope to resolve

The issue is directionally correct about using consistent dates, separating
actuals from forecasts, avoiding duplicate deductions, and flagging stale
inputs. Its draft is not yet fully consistent with established project rules:

- It proposes expected income in a future purchase projection. Existing
  purchase-check requirements exclude income until received and recorded;
  this document preserves that conservative MVP rule.
- Its formula subtracts the reserve in purchase capacity, then describes
  affordability and statuses differently from the existing recommendations.
  The formulas above make the reserve a single comparison threshold and
  preserve separate reserve-risk and insufficient-funds outcomes.
- It includes planned investment contributions and configured priorities,
  while the MVP purchase check excludes investments. Resolve any desired
  inclusion in a later product decision.
- Its “small reserve margin” caution result needs a threshold. The existing
  recommendation rules instead use the user's reserve boundary, without an
  extra configurable threshold.
- Its broad freshness table includes investment valuations, income review,
  debts, and historical records. Only inputs required by this check should
  determine whether this check is unknown.
- Its automatic recalculation, persistent assessment history, and scenario
  behavior are useful extensions, but are not necessary for the offline MVP.

Resolve these differences with issue #6 (recommendation labels) and issue #7
(expected scenarios) before the final milestone rules are treated as approved.

## Acceptance criteria

- The calculation is reproducible from a stated check date, purchase date,
  currency, input records, and assumptions.
- Actual balances, unpaid obligations, planned savings, and purchase cost are
  each counted at most once.
- Future income and investment values do not increase MVP purchase capacity.
- A balance missing, future-dated, older than 30 days, or unreconciled yields
  `unknown` with a specific reason and no reliable remaining-cash estimate.
- The result distinguishes affordable, reserve risk, insufficient funds, and
  unknown data, including the boundary where cash after purchase equals the
  reserve.
- Users can enter and review all required data without an internet connection.
