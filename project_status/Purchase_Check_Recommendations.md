# Purchase-check recommendations

The purchase checker provides an estimate based on the financial information
entered by the user. It is guidance, not financial advice or a guarantee that
funds will be available.

## Recommendation wording

| Result | Plain-language recommendation | Meaning |
| --- | --- | --- |
| `affordable` | “This purchase appears affordable while preserving your minimum reserve.” | Estimated cash after known obligations and the purchase is at least the user’s minimum cash reserve. |
| `reserve_risk` | “This purchase may reduce cash below your minimum reserve.” | The purchase fits within estimated cash, but estimated cash left afterward is below the reserve. |
| `insufficient_funds` | “This purchase exceeds the estimated cash available after obligations.” | The purchase is larger than estimated cash after known obligations. |
| `unknown` | “Not enough information to check this purchase reliably.” | Missing, future-dated, or outdated balance information, or a cash record without a known account, prevents a reliable estimate. Show the reason and do not present amounts as reliable. |

## Figures and explanation

For a result other than `unknown`, show:

- Planned purchase amount and purchase date.
- Estimated cash after recorded income and spending through the check date, less upcoming bills and planned savings contributions due by the purchase date.
- Upcoming bills and planned savings totals separately.
- Estimated cash remaining after the purchase.
- The user’s minimum cash reserve, so they can compare it with the remaining cash.

For `unknown`, show the purchase amount and date, the recommendation, and the specific data issue(s) to resolve. Do not show a reassuring remaining-cash estimate.

Investments are excluded from spendable cash. Future income is not assumed, including expected salary, freelance, or other irregular income that has not yet been recorded as received. Forecast obligations include only scheduled bills and savings contributions due after the check date and through the purchase date.

## Example scenarios

Amounts are in the same currency. Unless otherwise stated, the check date is
15 October 2026, and opening balances are dated 1 October 2026.

### 1. Purchase fits and preserves the reserve

- Opening cash: 2,000.
- Recorded income since the opening balance: 500; recorded spending: 200.
- One 500 bill and one 300 savings contribution are due before the 2 November purchase.
- Purchase: 400; minimum reserve: 1,000.
- Calculation: estimated cash is `2,000 + 500 - 200 - 500 - 300 = 1,500`; remaining cash is `1,500 - 400 = 1,100`.
- Expected: `affordable` — “This purchase appears affordable while preserving your minimum reserve.”

### 2. Irregular income expected, but not yet received

- Opening cash: 1,200.
- Recorded freelance income received by the check date: 450; recorded spending: 150.
- An additional 900 freelance payment is expected after the check date but has not been received. No other obligations are due before the purchase.
- Purchase: 1,000 on 5 November; minimum reserve: 500.
- Calculation: estimated cash is `1,200 + 450 - 150 = 1,500`; the expected 900 is not counted; remaining cash is `1,500 - 1,000 = 500`.
- Expected: `affordable` — the remaining cash is exactly the reserve. If the expected freelance payment arrives and is recorded, a later check can include it.

### 3. Purchase fits, but puts the reserve at risk

- Opening cash: 2,000; no transactions or obligations.
- Purchase: 1,100; minimum reserve: 1,000.
- Calculation: estimated cash is `2,000`; remaining cash is `900`.
- Expected: `reserve_risk` — “This purchase may reduce cash below your minimum reserve.”

### 4. Large purchase exceeds available cash

- Opening cash: 2,000; no transactions or obligations.
- Purchase: 2,500; minimum reserve: 1,000.
- Calculation: estimated cash is `2,000`; remaining cash is `-500`.
- Expected: `insufficient_funds` — “This purchase exceeds the estimated cash available after obligations.”

### 5. Balance is too old to support a recommendation

- The only opening balance is 2,000 dated 1 September 2026, more than 30 days before the check date.
- Purchase: 100; minimum reserve: 500.
- Expected: `unknown` — “Not enough information to check this purchase reliably.” Explain that the opening balance is outdated, and do not infer available or remaining cash.
