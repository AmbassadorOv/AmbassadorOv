# Rational Logic — 28-Question Forensic Reasoning Method

## Purpose

The 28-question method is the public methodological description of the research program's forensic reasoning layer.

It is **not** the proprietary implementation of Rational Logic.

The public record explains what is examined, why it is examined, and how evidence can be preserved around the examination. The underlying decision procedure, algorithms, weighting mechanisms, and implementation of the Rational Logic core remain protected intellectual property.

## Public research-depth boundary

The 28-question material shown in this repository is intentionally **not a complete representation of the underlying Rational Logic research program**.

The public GitHub corpus exposes a methodological surface: enough to establish the research question, the classes of reasoning failure under investigation, the evidence discipline, and the relationship between reasoning and forensic verification.

It does **not** attempt to compress the full research into a small public matrix, a simplified scoring table, or a minimal implementation example.

That omission is methodological, not accidental.

The underlying research is broader than the public presentation currently disclosed here. The 28 questions should therefore be understood as a **publicly describable research interface**, not as a claim that the entire research program can be captured by 28 rows in a table.

A small matrix would risk collapsing distinctions that the research is specifically designed to preserve:

**definition vs. premise → premise vs. inference → inference vs. evaluation → evaluation vs. criterion → correction vs. criterion change → re-evaluation vs. apparent self-correction**

For that reason, this repository documents the conceptual structure and selected representative controls while intentionally withholding the deeper research machinery and complete formal treatment.

This boundary is separate from, but compatible with, the protected Rational Logic implementation boundary. Some material is withheld because it belongs to protected IP; other material is withheld because a public summary would materially distort the depth, dependency structure, or research context of the underlying work.

See also: [Protected Core → Independent Evidence Infrastructure](PROTECTED_CORE_AND_EVIDENCE_INFRASTRUCTURE.md).

## WANGA as a distinct computational architecture

WANGA is treated in this research program as a **distinct computational system/architecture**, rather than merely a wrapper around a conventional AI model.

Within that architecture:

**Rational Logic = the canonical logic and reasoning layer of WANGA**

The distinction is therefore:

**WANGA → computational system / architecture**

**Rational Logic → logic and reasoning substrate**

This describes a computational architecture and does **not** claim a separate physical computer or hardware platform. The public repository documents the architectural relationship; the deeper formal treatment and protected implementation remain outside the public disclosure boundary.

## Core idea

A conventional evaluation asks:

> Is the model's answer correct?

The forensic method asks a deeper sequence:

> What definition was used? What premises were assumed? What evidence supports them? Does the inference follow? Did context change? What criterion was used for evaluation? Did that criterion remain stable during correction and re-evaluation?

The 28 questions therefore operate as a **reasoning-control network**, not merely as a questionnaire.

## Reasoning chain

```text
Definition → Premise → Evidence → Inference → Answer
                         ↓
Evaluation → Correction → Criterion Stability → Re-evaluation
```

The forensic objective is to identify **which element of the chain changed** when an output, evaluation, or conclusion changed.

## Representative control questions

The complete research suite contains 28 questions. These representative controls illustrate the method without disclosing the protected implementation:

| Control layer | Representative question | Drift / failure class |
|---|---|---|
| Definition | What exactly does the key term mean in the current context? | Definition Drift |
| Premise | Which premise must be true for the conclusion to follow? | Premise Drift |
| Evidence | What evidence supports that premise? | Evidence Fidelity |
| Inference | Does the conclusion follow from the stated premises? | Logical Consistency |
| Context | Did anything in the conversation change the meaning or scope? | Context Drift |
| Criterion | By what rule was the answer judged correct or incorrect? | Criterion Stability |
| Re-evaluation | Is the same criterion still being used after correction? | Evaluation Drift |

These are **control dimensions**, not a disclosure of the proprietary decision procedure.

## Controlled example: criterion drift

Consider:

```text
Model output = 0.75

Criterion v1:
pass if score ≥ 0.80
→ REJECT

Criterion v2:
pass if score ≥ 0.60
→ ACCEPT
```

The model output did not change.

The evaluation changed because the **criterion changed**:

```text
CRITERION_DRIFT
model_output_changed = false
criterion_changed = true
evaluation_changed = true
```

This prevents every changed decision from being incorrectly attributed to a changed model.

Verified empirical anchor:

**CASE_REF_2026_DRIFT_KNOWN_RISK_001**

[Open the verified case in WANGA-LAB](https://github.com/AmbassadorOv/WANGA-LAB/tree/main/artifacts/drift-known-risk-001)

## From correction to forensics

A model may appear to self-correct:

```text
Answer A → REJECT → Correction → Answer B → ACCEPT
```

The forensic method does not treat correction itself as proof of improvement. It asks what changed:

```text
Output?
Definition?
Premise?
Evidence?
Inference?
Context?
Criterion?
Evaluation procedure?
```

This distinguishes point error from definition, premise, inference, context, evidence/source, criterion, and evaluation drift.

## Public methodology vs. protected core

**Public:** research questions, control dimensions, taxonomy, evidence structures, replay fixtures, verification protocols, research artifacts, and observed results.

**Protected:** Rational Logic implementation, proprietary algorithms, internal decision procedures, weighting mechanisms, and implementation-specific IP.

The absence of the Rational Logic implementation from public repositories is therefore an **intentional IP boundary**, not an incomplete component.

## Architectural position

```text
PROTECTED CORE
Rational Logic
      ↓
28-Question Forensic Method
      ↓
Drift Detection
      ↓
Evidence Preservation
      ↓
Reconstruction
      ↓
Verification
      ↓
Research / Governance / Insurance Interfaces
```

The public layer makes the research understandable and testable at the artifact/protocol level without exposing the protected computational core.

## Relationship to NTM and WANGA-LAB

Rational Logic is the protected reasoning component.

The Neural Thinking Machine (NTM) research line concerns inference-time reasoning, thought modes, memory, search, and related reasoning architectures.

WANGA-LAB provides the public systems/evidence environment in which outputs, drift events, replay artifacts, verification results, and provenance can be recorded and tested.

The 28-question method is the methodological bridge between **reasoning behavior** and **forensic evidence**.

## Evidence status

This document describes the public research methodology. It does **not** claim that every 28-question capability is fully implemented in production.

Current verified empirical anchor:

**CASE_REF_2026_DRIFT_KNOWN_RISK_001 — VERIFIED (repository-level synthetic fixture)**

External timestamping, third-party audit, and production/client validation remain separate evidence states.

## Research principle

The central question is not simply:

> Did the model change?

It is:

> **What changed in the reasoning/evaluation chain, when did it change, what evidence establishes the change, and can the finding be independently reconstructed?**

That is the forensic purpose of the 28-question method.
