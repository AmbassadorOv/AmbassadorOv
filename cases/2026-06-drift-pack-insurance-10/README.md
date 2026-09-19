# WANGA Insurance Drift Pilot Factory — 10-Case Pack

This directory defines a repeatable factory for producing **real-model, evidence-preserving insurance AI drift cases**.

## Evidence rule

A case is not labeled `VERIFIED` until all required evidence exists and the verification checks pass.

Required evidence:

1. Original prompt with canonical serialization.
2. Exact model/provider response.
3. Model/provider/version metadata.
4. Evaluation criteria version A.
5. Evaluation criteria version B.
6. Decision/output under each criterion.
7. SHA-256 hashes of canonical artifacts.
8. External RFC3161 timestamp token for the evidence manifest.
9. Replay procedure and replay result.
10. Independent verification result.

## Current status

The case specifications are **READY FOR CAPTURE**.

The repository does not claim that the ten cases below have already been produced from live model executions. Live model capture must populate each case and pass the verification gates before publication as VERIFIED.

## Target artifact

`wanga-lab/cases/2026-06-drift-pack-insurance-10/`

Each completed case should contain:

```text
case-XX/
  case_spec.json
  prompt.json
  response.json
  model_metadata.json
  criteria_a.json
  criteria_b.json
  decision_a.json
  decision_b.json
  replay.py
  manifest.json
  manifest.sha256
  manifest.tsr
  verification_result.json
```

The intended forensic pattern is:

`same question -> same captured answer -> criterion change -> decision change`

The factory must record whether the decision change is caused by a criterion change, a model response change, or both. It must not assume the cause before measurement.
