# SY_NeuroKernel

Minimal computational sandbox for structural-relational experimentation.

## Scope
- 22 canonical nodes
- 231 unordered pair gates
- explicit forward/backward relation views
- 3 / 7 / 12 structural partitions
- graph construction from relations
- deterministic message passing as the first neural sandbox
- reproducible run metrics

Node labels are addresses in the representation. The computational object is the relation graph.

## Status
PROTOTYPED — experimental research sandbox.

Source-derived rules and computational hypotheses remain separately labeled.

## Layout
- src/sy_neurokernel/core.py — deterministic structural kernel
- tests/test_core.py — structural invariants
- schemas/run_metrics.json — run-output contract

First invariant: C(22,2) = 231.
The 231 gates are canonical unordered pairs. Direction is an operation/view, not a second canonical gate.
