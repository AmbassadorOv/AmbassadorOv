# AI Drift Forensics & Reliability

## Scope

AI Drift Forensics treats model behavior as an **evidence-bearing process**, not a collection of isolated answers.

The objective is to establish what changed, preserve the relevant evidence, reconstruct the event, and verify the finding without requiring the evaluated AI system to be owned by the evaluator.

The central investigation chain is:

**Baseline → Observation → Drift Detection → Evidence Preservation → Reconstruction → Causal / Dependency Analysis → Attribution → Risk Quantification → Intervention → Verification**

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

## Evidence protocol

Forensic records should preserve, where available and appropriate:

**model/version · runtime · prompt/trigger · context · tools/retrieval conditions · outputs · evaluation criteria · corrections · provenance · hashes/signatures · verification status · limitations**

The evidence layer is designed to remain conceptually independent from the system being evaluated.

## Verification chain

A representative evidence path is:

**Canonical Representation → SHA-256 Integrity → Timestamp Evidence → Deterministic Replay → Comparison → Verification Result**

The mechanism set depends on the case. External timestamping or anchoring is not treated as complete until actual proof is received and checked.

## Research artifact

The current empirical fixture is:

**CASE_REF_2026_DRIFT_KNOWN_RISK_001**

Current status: **PLANNED**

The artifact structure supports evidence inventory, replay inputs, normalized outputs and verification gates. A planned fixture is not represented as a completed client investigation or external finding.

## Public / protected boundary

The public research layer documents drift methodology, evidence structures, verification interfaces and reproducible artifacts where disclosure is appropriate.

Rational Logic remains a protected reasoning/IP component. Its architectural role is documented publicly; its proprietary implementation is intentionally not disclosed.

See [Protected Core → Independent Evidence Infrastructure](../research/PROTECTED_CORE_AND_EVIDENCE_INFRASTRUCTURE.md) and [Rational Logic — Protected IP Boundary](../research/RATIONAL_LOGIC_IP_BOUNDARY.md).

## Relationship to WANGA-LAB

AI Drift Forensics is a core evidence and verification research layer within WANGA-LAB, connecting model execution to provenance, reconstruction and verification.

Evidence status remains explicit:

**BUILT · SPECIFIED · PROTOTYPED · TESTED · VERIFIED · PLANNED · HYPOTHETICAL**
