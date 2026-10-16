# Budget Logbook — Purchase-check Example Scenarios

This scenario catalogue records proposed requirements for
[issue #7](https://github.com/KomeOn/Python_CA/issues/7). It is a
requirements-level test set for the offline MVP, not implementation or
financial advice.

## Scope and feasibility

Numerical purchase-check scenarios are feasible offline and can be reproduced
from user-entered balances and obligations. Issue #7's full catalogue spans
debts, investment liquidation, alternative recommendations, competing
priorities, and many kinds of cash-flow forecasts. Those areas exceed the
current purchase-check MVP and do not yet have agreed calculation rules.

This catalogue tests the agreed four outcomes and the core cash, obligation,
reserve, freshness, and no-double-counting rules. Do not treat deferred cases
as supported behavior until separate requirements define them.

## Shared assumptions

- Evaluation/check date: 15 October 2026.
- Unless a scenario says otherwise, the accessible cash account has an
  opening balance of 2,000 dated 1 October 2026, with no unlisted activity.
  Its balance is within the 30-day freshness limit.
- The date used for the opening balance is its effective date; included
  transactions are recorded cash transactions dated on or after that date
  through the check date.
- All amounts in a scenario use the same currency, are user-entered, and have
  valid dates and accounts unless the scenario tests invalid data.
- The purchase date is 2 November 2026 unless specified otherwise.
- `C` is estimated cash on the check date. `B` and `S` are unpaid bills and
  planned savings contributions due after the check date and on or before the
  purchase date. `P` is total purchase cost; `R` is the minimum reserve.

```text
Cash before purchase = C − B − S
Cash after purchase = C − B − S − P
Purchase margin = Cash after purchase − R
```

Expected future income, investments, unused credit, and unreceived borrowing
are excluded. Count paid or completed scheduled occurrences only if not
already reflected in the balance. A balance missing, future-dated, over 30
days old, or unreconciled produces `unknown`; do not present a reliable
cash-after-purchase figure.

## Scenario summary

| ID | Scenario | Key rule | Expected outcome |
| --- | --- | --- | --- |
| PC-01 | Purchase preserves reserve | Ordinary purchase with obligations | `affordable` |
| PC-02 | Exactly at reserve | Reserve boundary is inclusive | `affordable` |
| PC-03 | Below reserve but cash-positive | Reserve breach differs from shortfall | `reserve_risk` |
| PC-04 | Purchase exceeds remaining cash | Negative post-purchase cash | `insufficient_funds` |
| PC-05 | No cash remains, reserve already breached | Zero is not a cash shortfall | `reserve_risk` |
| PC-06 | Expected income not received | Future income excluded | `affordable` based on cash only |
| PC-07 | Bill paid and recorded | Do not deduct occurrence twice | `affordable` |
| PC-08 | Balance too old | Stale critical input | `unknown` |
| PC-09 | Cash transaction has no account | Cannot reconcile cash | `unknown` |
| PC-10 | Bill amount is an estimate | Show estimate and limitation | `affordable` if inputs otherwise valid |
| PC-11 | Missing reserve | Required input absent | `unknown` |

## Detailed scenarios

### PC-01 — Purchase preserves the minimum reserve

**Objective:** Verify a normal purchase with upcoming obligations.

**Inputs:** Opening cash 2,000; recorded income since opening balance 500;
recorded spending 200; unpaid bill 500 due 25 October; planned savings
contribution 300 due 28 October; purchase cost 400; reserve 1,000.

**Calculation:**

```text
C = 2,000 + 500 − 200 = 2,300
Cash before purchase = 2,300 − 500 − 300 = 1,500
Cash after purchase = 1,500 − 400 = 1,100
Purchase margin = 1,100 − 1,000 = 100
```

**Expected:** `affordable`. Explain that estimated cash after the purchase is
1,100, which is 100 above the 1,000 reserve. Show the bill and planned
contribution separately.

### PC-02 — Purchase leaves exactly the reserve

**Objective:** Verify the inclusive reserve boundary.

**Inputs:** Opening cash 2,000; no transactions or obligations; purchase cost
1,000; reserve 1,000.

**Calculation:** Cash before purchase is 2,000; cash after purchase is 1,000;
purchase margin is 0.

**Expected:** `affordable`. Exactly meeting the reserve is affordable; do not
require a positive margin.

### PC-03 — Purchase fits but leaves cash below the reserve

**Objective:** Distinguish a reserve risk from insufficient funds.

**Inputs:** Opening cash 2,000; no transactions or obligations; purchase cost
1,200; reserve 1,000.

**Calculation:** Cash before purchase is 2,000; cash after purchase is 800;
purchase margin is -200.

**Expected:** `reserve_risk`. Explain that the purchase fits within estimated
cash, but leaves it 200 below the reserve.

### PC-04 — Purchase exceeds cash after obligations

**Objective:** Verify a shortfall after known commitments.

**Inputs:** Opening cash 2,000; unpaid bill 500 due 25 October; purchase cost
1,700; reserve 1,000.

**Calculation:** Cash before purchase is 1,500; cash after purchase is -200;
the purchase exceeds cash after obligations by 200.

**Expected:** `insufficient_funds`. State the 200 shortfall. Do not present a
negative amount as money available to spend.

### PC-05 — Purchase uses all remaining cash but does not create a shortfall

**Objective:** Confirm precedence between reserve risk and insufficient
funds.

**Inputs:** Opening cash 2,000; no transactions or obligations; purchase cost
2,000; reserve 500.

**Calculation:** Cash after purchase is 0; purchase margin is -500.

**Expected:** `reserve_risk`, not `insufficient_funds`, because the purchase
cost is covered exactly and remaining cash is non-negative. Explain that it
would use all estimated cash and breach the reserve by 500.

### PC-06 — Expected income is not yet received

**Objective:** Verify that future income does not increase purchase capacity.

**Inputs:** Opening cash 1,200; recorded income 450; recorded spending 150;
expected but unreceived income 900 due 25 October; no bills or savings
contributions due; purchase cost 1,000; reserve 500.

**Calculation:**

```text
C = 1,200 + 450 − 150 = 1,500
Cash after purchase = 1,500 − 1,000 = 500
Purchase margin = 500 − 500 = 0
```

**Expected:** `affordable`. Exclude the expected 900 and say that the result is
based on recorded cash only. If the income is later received and recorded, a
new check may use the updated cash balance.

### PC-07 — A bill already paid is represented in cash transactions

**Objective:** Prevent a paid scheduled bill from being deducted twice.

**Inputs:** Opening cash 2,000; a 500 bill was paid on 10 October and its
500 payment is included in recorded spending; the bill occurrence is marked
paid and linked to that transaction; purchase cost 400; reserve 1,000.

**Calculation:** Cash at check date is 1,500 after the recorded payment. The
paid occurrence contributes zero to unpaid bills. Cash after purchase is
1,100.

**Expected:** `affordable`. Do not subtract the 500 bill again. The explanation
may show the paid transaction as history, but not as an upcoming obligation.

### PC-08 — Opening balance is stale

**Objective:** Verify freshness handling of required cash data.

**Inputs:** The only opening balance is 2,000 dated 1 September 2026; check
date is 15 October 2026; purchase cost 100; reserve 500.

**Expected:** `unknown`, because the balance is more than 30 days old. Name
the outdated balance and request review. Do not show a reliable cash-after-
purchase estimate.

### PC-09 — Cash transaction cannot be reconciled to an account

**Objective:** Verify missing account handling.

**Inputs:** Opening balance 2,000 dated 1 October; a recorded cash spending
entry of 300 has no known account; purchase cost 100; reserve 500.

**Expected:** `unknown`. Identify the unreconciled spending record and ask the
user to assign or correct its account. Do not silently ignore the 300 or
present an affordability result.

### PC-10 — Variable bill is an estimate

**Objective:** Verify that estimates are visible in an otherwise usable result.

**Inputs:** Opening cash 2,000; variable utility bill estimate 200 due
25 October; purchase cost 500; reserve 1,000. Assume the user-entered
estimate is confirmed for this check and all required balance data is fresh.

**Calculation:** Cash before purchase is 1,800; cash after purchase is 1,300;
purchase margin is 300.

**Expected:** `affordable`, with the bill explicitly labelled as an estimate.
The explanation must not imply that the final bill is known.

### PC-11 — Minimum reserve is missing

**Objective:** Verify handling of a missing required input.

**Inputs:** Opening cash 2,000 dated 1 October; purchase cost 100; no minimum
reserve has been entered.

**Expected:** `unknown`. Request the user to enter a reserve before producing
an affordability result. Do not substitute zero.

## Deferred coverage

The following issue #7 categories cannot be assigned reliable expected
recommendations from the current MVP rules. Defer them to separately defined
requirements rather than inventing assumptions in this test set:

- Future salary or other expected income making a purchase affordable.
- Investment sale, valuation, settlement, return, or contribution scenarios.
- Releasing savings automatically or changing a goal allocation.
- Ranking competing goals, purchases, and user priorities.
- Predicting a date when a purchase becomes affordable or calculating a
  contribution plan.
- Debt amortization, loan principal/interest split, or new borrowing.
- Multiple currencies, pending transactions, disputed balances, and
  partial/missed bill occurrences.
- Configurable “small surplus” thresholds or additional recommendation
  statuses.

These cases are possible to model offline only after their input fields,
timing, account treatment, and decision rules are agreed.

## Validation assertions

- Repeating a scenario with the same inputs and evaluation date produces the
  same outcome and figures.
- `affordable` requires cash after purchase to be greater than or equal to
  the reserve.
- `reserve_risk` requires a non-negative cash-after-purchase amount below the
  reserve.
- `insufficient_funds` requires a negative cash-after-purchase amount.
- `unknown` takes precedence whenever a critical input fails validation or
  freshness checks and must not display a reliable cash-after-purchase
  amount.
- Expected income, investments, unused credit, and unreceived borrowing do
  not increase cash in these MVP scenarios.
- Paid bills and completed savings contributions already reflected in cash
  are not deducted again.
- Planned savings contributions are obligations only when unpaid and due by
  the purchase date; they are not actual spending.
- Explanations use the same dates, currency, figures, and assumptions as the
  calculation and disclose estimated inputs.
- Scenarios change no actual records or balances.
