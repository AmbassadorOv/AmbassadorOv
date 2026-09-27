# Second Logic — Talmudic Operator / Modern Model Interoperability

Status: SPECIFIED  
Scope: Golem Stage — C1 + C2 only

## Purpose

The Talmudic operator set is treated as an operational layer of the Second Logic architecture. Its role is not to replace contemporary neural models, but to provide a deterministic, provenance-preserving interface through which model outputs can propagate without being treated as truth by default.

The architecture separates:

```
Modern Model
    ↓
Candidate Claim
    ↓
Provenance Guard
    ↓
Talmudic Operator Layer
    ├── C1 Attribution
    └── C2 Temporal Revision
    ↓
State + Trace
    ↓
Downstream Model / Agent / Human
```

The central interoperability principle is:

`oxed{\text{Neural generation} \neq \text{logical commitment}}}

A model may generate a candidate. The operator layer determines how that candidate is routed, attributed, versioned, and traced.

## 1. Why This Layer Exists

Contemporary models communicate primarily through probabilistic natural-language representations. The Golem layer cannot require those models to natively "speak" Talmudic logic.

Instead, the Talmudic operators become a **protocol / intermediate representation (IR)** between model generation and downstream propagation.

Thus:

```
Model-native language
       ↓
Claim / Evidence / SourceReference
       ↓
Second-Logic IR
       ↓
C1 / C2 gates
       ↓
Model-compatible output
```

The Talmudic vocabulary is therefore an executable semantic discipline, not a requirement that external models implement the historical vocabulary themselves.

## 2. Claim Envelope

Every candidate entering the Golem stage must be normalized into:

```
ClaimEnvelope {
  claim_id,
  claim_text,
  source_ref,
  author,
  stage,
  retraction_flag,
  evidence,
  provenance_status
}
```

A missing SourceReference causes:

```
E_PROVENANCE
```

The neural model may propose a candidate, but it cannot bypass this guard.

## 3. Minimal State

```
S = (T, P, A, V)
```

- T = truth-status placeholder; not assigned from model confidence.
- P = provenance/commitment state.
- A = attribution state (C1).
- V = temporal/version state (C2).

No gate may silently modify state.

## 4. C1 — Attribution

Operators:

- מי אמר / מני → K_ATTRIBUTE
- היכי תני / היכי כתיב → K_SOURCE
- איכא דאמרי → K_ATTRIBUTE + branch

Core transition:

```
different attribution
    → NO_DIRECT_CONTRADICTION
same attribution
    → PASS_TO_C2
```

This is a provenance operation, not a truth judgment.

## 5. C2 — Temporal Revision

Operators:

- מעיקרא / השתא → K_TEMPORAL_STAGE
- הדר ביה → K_VERSION
- לא קשיא / תריץ → K_RESOLVE_C2 / K_COMMIT only after valid C1/C2 resolution

Core transition:

```
different stage OR explicit retraction
    → REVISION
same stage
    → remaining conflict / minimal FOL
```

## 6. Modern-Model Interoperability

The external model does not need to understand the entire Second Logic architecture.

It communicates through a stable envelope:

```
INPUT:
  claim
  source_ref
  evidence
  author
  temporal_stage

PROCESS:
  K_ATTRIBUTE
  K_SOURCE
  K_TEMPORAL_STAGE
  K_VERSION

OUTPUT:
  state
  resolution_class
  trace
  candidate_next_action
```

A model can therefore remain a language model, reasoning model, retrieval model, or agent while the Golem layer controls the admissibility and propagation of its claims.

## 7. Propagation Rule

The key system boundary is:

`oxed{\text{Propagation carries state + provenance, not merely text}}]

A downstream model should receive, where available:

```
Claim
+ SourceReference
+ Attribution State
+ Temporal State
+ Evidence
+ Operator Trace
+ Verification Status
```

This prevents a rewritten model response from appearing equivalent to the original source.

## 8. Neural Role

Neural systems are permitted to:

- generate candidate claims;
- identify possible source references;
- propose attribution candidates;
- propose temporal-stage candidates;
- produce alternative formulations.

They are not permitted, at this stage, to:

- convert confidence into truth;
- bypass provenance;
- silently revise state;
- invoke blocked C3+ operators;
- manufacture missing evidence.

Any unsupported candidate remains a candidate.

## 9. Scope Lock

Active:

- Provenance Guard
- C1 Attribution
- C2 Temporal Revision
- Shev Prior, as confidence prior only
- mandatory trace

Blocked:

- מתיבי
- רמינהי
- איבעיא להו
- מאי בינייהו
- לא צריכא
- תסתיים
- ופליג
- all other C3+ dialectical expansion

Blocked calls return:

```
E_SCOPE
```

## 10. Architectural Interpretation

The Mishnah is treated as a canonical knowledge object for this stage.

The Talmudic operators are the executable transformation layer.

Modern neural models are external candidate-generating / consuming components.

Therefore:

```
Canonical Corpus
      ↓
Claim Extraction
      ↓
Second-Logic IR
      ↓
C1 / C2 Golem
      ↓
State + Provenance + Trace
      ↓
Modern Models / Agents
```

The architecture is designed so that modern models do not need to "become Talmudic." They need only exchange the structured state required by the protocol.

## 11. Non-Equivalence Rule

Historical Talmudic categories and modern computational constructs must remain explicitly distinct.

The following mapping is a formal engineering representation:

```
historical operator
      ≠
modern opcode
      ≠
historical doctrine about computation
```

The opcode is an implementation choice used to operationalize a textual/analytical function.

## 12. Verification Boundary

This document specifies an architecture. It does not establish that contemporary models will reliably obey the protocol without an enforcement layer.

Verification requires executable tests demonstrating:

1. provenance rejection;
2. correct attribution branching;
3. correct temporal revision branching;
4. preservation of trace;
5. refusal of blocked operators;
6. no truth assignment from neural confidence;
7. deterministic replay of identical inputs.

Until those tests pass, the interoperability layer remains SPECIFIED, not VERIFIED.
