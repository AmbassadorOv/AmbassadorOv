# WANGA Insurance Drift Pilot — One-Page Proposal

## The problem

Insurance organizations increasingly rely on AI-assisted decisions across underwriting, claims, fraud review, policy interpretation, prioritization, and vendor-risk workflows.

The operational problem is not only whether an AI system produces a plausible answer. It is whether the organization can later establish:

- what the system was asked;
- what it actually returned;
- what evidence existed at the time;
- which evaluation criterion was applied;
- whether that criterion changed;
- whether the resulting decision changed;
- and whether the evidence can be independently verified.

## Proposed WANGA pilot

WANGA Insurance Drift Pilot Factory produces a controlled set of **ten real-model evidence cases** across representative insurance decision domains.

The central forensic experiment is:

**same question → same captured answer → criterion change → decision comparison**

Where a decision changes, the evidence chain records whether the cause is:

- criterion drift;
- response drift;
- both; or
- no material change.

No causal attribution is made without evidence.

## Deliverables

The pilot produces:

**10 case folders**

Each containing:

- canonical prompt;
- captured model response;
- provider/model metadata;
- evaluation criterion A;
- evaluation criterion B;
- decision traces;
- SHA-256 manifest;
- RFC3161 timestamp token;
- replay procedure/result;
- verification result.

The completed pack is delivered as one reproducible evidence package.

## What the insurer receives

The customer receives a concrete demonstration of how AI behavioral change can be converted into a preserved, auditable evidence object rather than an informal model-monitoring alert.

The pilot is designed to support internal:

- AI risk review;
- model governance;
- audit preparation;
- incident investigation;
- third-party AI assessment;
- insurance claims/underwriting assurance workflows.

## Commercial path

The pilot is a technical entry point into the WANGA licensing model.

Following successful evaluation, the customer may progress to a scoped **WANGA INSURANCE** deployment under a separate non-exclusive software license.

Reference pricing published for the WANGA Insurance configuration is **USD $50,000/year + USD $5,000 per additional model**, subject to final scope, deployment, integration, security, evidence volume, support, and contractual terms.

## Verification boundary

This proposal does not claim that the ten live cases have already been executed.

The repository contains the factory, specifications, schema, and verification gates required to produce them. A case becomes VERIFIED only after the corresponding real capture, evidence, RFC3161 token, replay, and verification results exist.

## Contact

**Eran Oved Awat — Principal Researcher / Systems Architect**

Collaboration contact: **beywolf@gmail.com**

WANGA is offered through non-exclusive software licensing and scoped technical collaboration. Under the intended institutional model, the underlying IP is not transferred by the software license.
