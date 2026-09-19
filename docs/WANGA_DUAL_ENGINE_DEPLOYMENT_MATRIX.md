# WANGA Dual-Engine Deployment Matrix

| Deployment model | Target | WANGA boundary | Example evidence | Operational output | Current status |
|---|---|---|---|---|---|
| 1. Models | model/provider/runtime | Model Adapter | model/version/input/output metadata | evaluated model result | SPECIFIED |
| 2. Agents | agent/tool runtime | Agent Adapter | task/tool/action trace | authorized action request | SPECIFIED |
| 3. Organizations | enterprise workflow | Organization Adapter | policy, approval, decision trace | governed workflow result | SPECIFIED |
| 4. Industries | industrial/operational systems | Industry Adapter | operational event + verification state | authorized operational instruction | SPECIFIED |
| 5. Insurance / Banking / Property Evidence | high-consequence financial/evidence workflows | Financial Evidence Adapter | policy, claim, transaction, property/asset evidence | auditable decision/evidence package | SPECIFIED |

## Core invariant

No deployment profile should be described as VERIFIED merely because the architecture exists.

Verification requires execution evidence appropriate to the deployment.

## Insurance example

Claim
→ Document ingestion
→ Model/Agent analysis
→ Evidence capture
→ Criterion evaluation
→ Drift check
→ Verification
→ Human/organizational authorization
→ Claim workflow

## Banking example

Transaction / credit workflow
→ Model/Agent analysis
→ Evidence capture
→ Policy/criterion evaluation
→ Verification
→ Authorization
→ Banking workflow

## Property evidence example

Property/asset record
→ Source documents
→ Evidence canonicalization
→ Provenance
→ Verification status
→ Evidence package

This can support an evidence workflow; it does not itself establish legal ownership.
