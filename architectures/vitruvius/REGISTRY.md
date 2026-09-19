# Vitruvius Model Architecture Registry

Status: SPECIFIED

| Branch | Function |
|---|---|
| vitruvius-model-lineage | origin → parent → model → descendant lineage |
| vitruvius-model-provenance | evidence-backed origin/state metadata |
| vitruvius-model-routing | destination and deployment topology |
| vitruvius-model-descendants | parent/child/derived artifact graph |
| vitruvius-model-family-map | families, subfamilies and endpoints |
| vitruvius-institutional-map | institutional and governance topology |

## Unified map
Origin → Provenance → Lineage → Family → Model/Agent → Routing → Deployment → Operational Consequence → Descendants

All relationships are evidence-backed where known. Unknown relationships remain UNKNOWN rather than inferred as fact.

## WANGA connection
The registry feeds the dedicated Vitruvius Dual-Engine layer, which connects through the Vitruvius ↔ WANGA Main Bridge. Verification and authorization remain WANGA responsibilities.
