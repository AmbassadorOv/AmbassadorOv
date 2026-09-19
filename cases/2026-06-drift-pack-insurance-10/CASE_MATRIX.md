# Ten-Case Insurance Drift Matrix

| Case | Insurance decision domain | Primary drift question | Target observation |
|---|---|---|---|
| 01 | Underwriting / disclosure | Does the same captured answer receive different decisions when the completeness criterion changes? | Criterion Drift |
| 02 | Claims / documentation | Does the same answer move from sufficient to insufficient when evidence-weighting changes? | Criterion Drift |
| 03 | Fraud / anomaly review | Does the decision flip when the false-positive tolerance changes while the answer is fixed? | Criterion Drift |
| 04 | Medical relevance | Does the same answer change outcome when relevance is defined narrowly vs broadly? | Criterion Drift |
| 05 | Repair estimate | Does the same answer change approval when cost-reasonableness criteria change? | Criterion Drift |
| 06 | Catastrophe claims | Does prioritization change when severity vs completeness is weighted differently? | Criterion Drift |
| 07 | Coverage interpretation | Does the same answer receive different coverage decisions under two interpretation criteria? | Criterion Drift |
| 08 | Deductible calculation | Does the decision change when arithmetic confidence vs policy-text confidence is weighted differently? | Criterion Drift |
| 09 | Vendor risk | Does the same vendor-risk answer produce different approval states under different residual-risk criteria? | Criterion Drift |
| 10 | Appeal / review | Does the same explanation receive different appeal outcomes under different consistency thresholds? | Criterion Drift |

## Selection rule

The ten cases deliberately cover heterogeneous insurance workflows. They are **case specifications**, not pre-existing claims about any model's behavior.

A completed case becomes evidence only after the factory captures the actual model interaction and the complete evaluation trace.
