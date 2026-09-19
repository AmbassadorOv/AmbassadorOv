# Protected Core → Independent Evidence Infrastructure → Research Derivatives

## Purpose

The public research architecture is intentionally organized around a separation between a protected reasoning core and the evidence infrastructure that can evaluate AI systems independently.

The central distinction is:

**Protected Core → Evidence Infrastructure → Reusable Research Derivatives → Governance Interface**

The protected core is **Rational Logic**. The public layer does not attempt to reproduce or disclose its proprietary implementation. Instead, the public corpus documents the interfaces, evidence discipline, forensic methodology, and verification structures that can be applied to AI systems more broadly.

## 1. Protected reasoning core

**Rational Logic** is a core research direction for structured reasoning, explicit logical evaluation, constraint handling, and verification around probabilistic systems.

Its public status is:

- Research role: **SPECIFIED / ARCHITECTURAL**
- IP status: **PROTECTED_IP / PROPRIETARY_IMPLEMENTATION**
- Public implementation: **NOT DISCLOSED**
- Public research role: **DOCUMENTED**

The absence of source code from the public corpus is intentional.

**INTERFACE / ROLE DISCLOSED** does not imply **IMPLEMENTATION DISCLOSED**.

This document does not claim that the protected implementation is uniquely unreproducible or commercially exclusive. It states a deliberate separation of public research evidence from proprietary implementation.

## 2. What the public layer is for

The public layer is designed to answer a different question from the protected core:

> How can an external observer establish what an AI system did, what changed, what evidence supports that finding, and whether the finding can be reproduced?

This creates an independent evidence layer around model behavior.

The research sequence is:

**Baseline → Observation → Drift Detection → Evidence Preservation → Reconstruction → Causal / Dependency Analysis → Attribution → Risk Quantification → Intervention → Verification**

The corresponding evaluation chain is:

**Model → Answer → Evaluation → Correction → Criterion Change → Re-evaluation**

The important boundary is that the system being evaluated is not automatically the authority on whether its own correction or reasoning is valid.

## 3. Reusable research derivatives

The public research layer produces artifacts and protocols that can be reused without exposing the Rational Logic implementation.

### Evidence Protocol

Defines the information that should be preserved when an AI behavior claim is investigated:

- model and runtime identity;
- prompt or trigger conditions;
- relevant context and tool/retrieval conditions;
- outputs and intermediate evidence where available;
- evaluation criteria;
- corrections and re-evaluations;
- provenance;
- hashes or signatures where applicable;
- verification status and limitations.

### Drift Artifact

A canonical case package can preserve the evidence chain for a particular investigation.

The current research fixture is:

**CASE_REF_2026_DRIFT_KNOWN_RISK_001**

The intended package includes case metadata, evidence inventory, replay material, normalized observations, verification results, and integrity checks.

Its current status remains **PLANNED**. A planned case is not represented as a completed client investigation.

### Verification Chain

The verification layer can combine, as applicable:

**Canonical representation → SHA-256 integrity → timestamp evidence → deterministic replay → comparison → verification result**

Different mechanisms answer different evidentiary questions. An external timestamp or anchor is not treated as complete until actual proof is received and checked.

### Governance Interface

The governance layer describes how technical evidence can interface with institutions and risk-bearing organizations while keeping research, decision support, legal authority, regulation, and proprietary implementation as distinct objects.

This includes potential applications in:

- AI reliability evaluation;
- model-behavior analysis;
- operational AI drift;
- evidence and provenance infrastructure;
- institutional risk analysis;
- insurance and financial-sector exposure to AI-dependent systems;
- public-sector and governance interfaces.

These are research and service domains. They are not, by themselves, claims of regulatory authority, insurance underwriting authority, certification, or governmental status.

## 4. Why this separation matters

The public corpus is not primarily an attempt to publish an AI engine.

It is an attempt to make **AI behavior independently observable and evidentially reconstructable**.

That means the public value proposition is not:

**"Use our model because we built it."**

It is:

**"Use an independent evidence layer to examine what an AI system did, preserve the relevant evidence, reconstruct the event, and verify the resulting claim."**

The evaluated system may be internal, external, proprietary, open-source, or supplied by another organization. The evidence methodology is designed to remain conceptually separate from the engine under investigation.

## 5. Architectural relationship

Within the broader WANGA research architecture:

**WANGA OS → Global Work Manager → Model Fabric → Digital Model Agents → Providers / Runtimes → Evidence & Provenance → Drift Forensics & Verification → Rational Logic ↔ Neural Thinking Machine → Work Memory**

Rational Logic is therefore a protected reasoning component inside the architecture.

The public evidence layer documents how evidence moves around model execution and verification without exposing the protected implementation.

## 6. Evidence maturity

The public corpus maintains explicit evidence states:

**BUILT · SPECIFIED · PROTOTYPED · TESTED · VERIFIED · PLANNED · HYPOTHETICAL**

The maturation gate is:

**SPECIFIED → IMPLEMENTED / BUILT → TESTED → VERIFIED → PUBLISHED**

No direct transition from **SPECIFIED** to **VERIFIED**.

For the current drift-known-risk-001 fixture, the repository contains the structure for evidence, replay and verification, while the case itself remains **PLANNED** until the required evidence and verification gates are actually completed.

## 7. Research and service boundary

The architecture supports a research/service model in which protected intellectual property can remain private while independently useful evidence protocols, forensic artifacts, and verification mechanisms can be documented and, where appropriate, delivered to external organizations.

The economic model is therefore conceptually closer to **licensing or delivering a reusable architecture and evidence capability around a protected core** than to open-sourcing the core engine itself.

Any commercial licensing structure, pricing, exclusivity, or royalty model would require separate contractual and legal definition and should not be inferred from this research document.

## 8. Non-claims

This architecture does **not** by itself establish:

- that Rational Logic is patented;
- that Rational Logic cannot be independently recreated;
- that every public derivative depends technically on the proprietary implementation;
- that a research artifact is automatically admissible evidence in every jurisdiction;
- that WANGA-LAB is a regulator, insurer, certifier, or governmental authority;
- that a planned research framework is an existing formal institution.

The purpose of the boundary is clarity: disclose the research architecture and evidence methodology while preserving proprietary implementation and maintaining explicit limits on what the public record proves.

## Status

**PUBLIC RESEARCH MODEL:** DOCUMENTED  
**PROTECTED CORE:** Rational Logic — PROTECTED_IP / PROPRIETARY_IMPLEMENTATION  
**PUBLIC EVIDENCE LAYER:** WANGA-LAB / Drift Forensics / Evidence & Verification  
**CURRENT EMPIRICAL FIXTURE:** drift-known-risk-001 — PLANNED  
**GOVERNANCE FRAMEWORK:** Global Algorithmic Governance Institute — PLANNED / CONCEPTUAL
