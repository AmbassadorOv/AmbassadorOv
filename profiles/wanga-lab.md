# WANGA-LAB — Systems Architecture

WANGA-LAB is the systems architecture layer for coordinating model infrastructure, execution, evidence, drift forensics and verification.

## Core distinction

WANGA-LAB is not primarily an AI engine.

Its public role is an **independent evidence and verification layer around AI systems**:

**Evidence Protocol → Drift Artifact → Verification Chain → Governance Interface**

The model under examination may be internal, external, proprietary, open-source or supplied by another organization.

## Architectural chain

**WANGA OS → Global Work Manager → Model Fabric → Digital Model Agents → Providers / Runtimes → Evidence & Provenance → Drift Forensics & Verification → Rational Logic ↔ Neural Thinking Machine → Work Memory**

A Perspective Layer provides lateral views across the system. GitHub is treated as the technical source of truth, with publication layers connected separately.

Rational Logic is a protected reasoning component in this architecture. Its public role is documented; its proprietary implementation is intentionally not disclosed.

## Operating discipline

The preferred engineering sequence is:

**READ → CLAIM → IMPLEMENT → TEST → VERIFY → COMMIT → PR → REVIEW**

No component is treated as complete merely because code exists.

## Architectural principles

- Separate planning from execution.
- Preserve evidence and provenance.
- Keep verification independent from the component being evaluated where practical.
- Distinguish model slots from active model instances.
- Treat Rational Logic as a core reasoning/verification layer rather than an ordinary agent.
- Preserve the ability to redesign a system instead of reducing all work to micro-tasks.

## Evidence derivatives

The public architecture can produce reusable research/service artifacts without exposing the protected reasoning implementation:

**Evidence Protocol** — preservation requirements for AI-event evidence.

**Drift Artifact** — a canonical case package for an observed or investigated behavioral deviation.

**Verification Chain** — integrity, replay, comparison and verification structures.

**Governance Interface** — technical evidence structures for institutional and risk contexts.

## Research status

Architecture documents may exist at different maturity levels. Each artifact should explicitly state whether it is BUILT, SPECIFIED, PROTOTYPED, TESTED, VERIFIED, PLANNED or HYPOTHETICAL.

No public documentation should imply external verification merely because implementation exists.
