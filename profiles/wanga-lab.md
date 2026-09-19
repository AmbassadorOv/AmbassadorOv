# WANGA-LAB — Systems Architecture

WANGA-LAB is the systems architecture layer for coordinating model infrastructure, execution, evidence and verification.

## Architectural chain

**WANGA OS → Global Work Manager → Model Fabric → Digital Model Agents → Providers/Runtimes → Evidence & Provenance → Drift Forensics & Verification → Rational Logic ↔ Neural Thinking Machine → Work Memory**

A Perspective Layer provides lateral views across the system. GitHub is treated as the technical source of truth, with publication layers connected separately.

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

## Research status

Architecture documents may exist at different maturity levels. Each artifact should explicitly state whether it is BUILT, SPECIFIED, PROTOTYPED, TESTED, VERIFIED, PLANNED or HYPOTHETICAL.
