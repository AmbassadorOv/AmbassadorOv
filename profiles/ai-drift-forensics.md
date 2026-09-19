# AI Drift Forensics & Reliability

## Scope

AI Drift Forensics treats model behavior as an evidence-bearing process rather than a collection of isolated answers.

The central investigation chain is:

**Baseline → Observation → Drift Detection → Evidence Preservation → Reconstruction → Attribution → Risk Quantification → Intervention → Verification**

## Drift classes

The research distinguishes at least:

- Point error
- Definition Drift
- Premise Drift
- Inference Drift
- Criterion Drift
- Question-fidelity drift
- Evidence/source-fidelity drift
- Terminological instability
- Response-trajectory drift

A key test is whether an apparent correction actually changes the underlying criterion used to evaluate the answer.

## Evaluation chain

**Model → Answer → Evaluation → Correction → Criterion Change → Re-evaluation**

This makes it possible to investigate whether a system corrected an answer, changed its premise, changed its evaluation rule, or merely changed its wording.

## Evidence discipline

Forensic records should preserve model/version, runtime, prompt or trigger, tools and retrieval conditions, outputs, evaluation criteria, corrections, hashes/signatures where applicable, and verification status.

Example evidence states include:

- STRUCTURALLY_VALID
- NOT_YET_VERIFIED
- REPRESENTATION_ONLY

A result is not called verified until the required replay, integrity and audit checks have actually been completed.

## Relationship to WANGA-LAB

AI Drift Forensics is the verification/evidence layer of the broader WANGA architecture, connecting model execution to provenance, reconstruction and verification.
