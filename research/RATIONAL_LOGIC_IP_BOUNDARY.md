# Rational Logic — Research Architecture & Protected IP Boundary

**Related public architecture:** [Protected Core → Independent Evidence Infrastructure → Research Derivatives](PROTECTED_CORE_AND_EVIDENCE_INFRASTRUCTURE.md)

## Purpose

Rational Logic is a core research direction within the broader Eran Oved Awat research corpus. It concerns structured reasoning, explicit logical evaluation, verification, and the separation of reasoning criteria from the probabilistic behavior of a model.

The public research record documents the conceptual role, architectural interfaces, research lineage, and testable questions surrounding Rational Logic. The proprietary implementation is intentionally not published in the public GitHub corpus.

## Why the implementation is not in the public repositories

The absence of the Rational Logic implementation from the public repositories is an explicit **intellectual-property boundary**, not an indication that an architectural component is missing.

The public corpus is designed to expose:

- research lineage;
- architectural relationships;
- methodology;
- evidence and provenance structures;
- evaluation and drift-analysis methods;
- verification interfaces;
- reproducible research artifacts where disclosure is appropriate.

The protected layer may contain implementation details, algorithms, mechanisms, or other technical material that is intentionally withheld from public disclosure.

Accordingly:

**INTERFACE / ROLE DISCLOSED** does not imply **IMPLEMENTATION DISCLOSED**.

## Architectural role

Within the broader WANGA research architecture, Rational Logic is positioned as a reasoning and verification layer that can interact with the Neural Thinking Machine (NTM) and other system components.

Conceptually:

**WANGA OS → Global Work Manager → Model Fabric → Digital Model Agents → Providers/Runtimes → Evidence & Provenance → Drift Forensics & Verification → Rational Logic ↔ Neural Thinking Machine → Work Memory**

This diagram describes architectural relationships. It does not constitute disclosure of the protected Rational Logic implementation.

## Research significance

The research direction asks how explicit logical structure can be used to:

1. represent reasoning constraints;
2. distinguish premises from conclusions;
3. detect changes in evaluation criteria;
4. support re-evaluation after model responses;
5. provide a structured verification layer around probabilistic systems;
6. preserve the distinction between model output and independent evaluation.

This is particularly relevant to AI systems where a probabilistic model should not be treated as the sole judge of whether its own reasoning or correction is valid.

The related research corpus includes work on structured reasoning, inference-time computation, neuro-symbolic verification, memory and re-evaluation, Python/Z3 constraint checking, and AI²³¹.

These related repositories and documents are research inputs and specifications unless an implementation and verification record establishes otherwise.

## Public / protected separation

| Layer | Public status |
|---|---|
| Research lineage | DISCLOSED |
| Conceptual model | DISCLOSED |
| Architectural role | DISCLOSED |
| Interfaces / boundaries | DISCLOSABLE WHERE APPROPRIATE |
| Research specifications | DISCLOSED WHERE APPROPRIATE |
| Experimental evidence | DISCLOSED WHEN VERIFIED / PUBLISHABLE |
| Rational Logic implementation | PROTECTED_IP |
| Proprietary algorithms / mechanisms | PROPRIETARY_IMPLEMENTATION |
| Non-public technical details | IMPLEMENTATION_WITHHELD |

The repository therefore uses explicit status language rather than implying that every architectural component must be open-source.

## Evidence-status rule

Rational Logic is not presented as a publicly verified implementation merely because it appears in the architecture.

The research corpus maintains the distinction:

**SPECIFIED → IMPLEMENTED / BUILT → TESTED → VERIFIED → PUBLISHED**

No implementation claim should be inferred from an architectural reference alone.

## Relationship to WANGA-LAB

**Global Algorithmic Governance Institute** is the proposed governance research framework and remains separate from WANGA-LAB.

**WANGA-LAB** is the systems, evidence, drift, and verification layer.

**Rational Logic** is a protected research/IP component whose architectural role can be referenced by the public corpus without exposing its proprietary implementation.

This separation preserves both research traceability and intellectual-property boundaries.

## Status

**RESEARCH STATUS:** SPECIFIED / ARCHITECTURAL  
**IP STATUS:** PROTECTED_IP / PROPRIETARY_IMPLEMENTATION  
**PUBLIC IMPLEMENTATION:** NOT DISCLOSED  
**PUBLIC RESEARCH ROLE:** DOCUMENTED

The purpose of this document is to prevent a reader from interpreting the absence of public Rational Logic source code as an accidental gap in the research architecture. The absence is deliberate and reflects the separation between publicly documented research and protected intellectual property.
