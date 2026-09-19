# Vitruvius Scanner v0.1

A provider-neutral GitHub repository architecture scanner. It collects repository metadata and selected source/config manifests, then classifies architecture families, dependencies, and evidence/provenance patterns.

## Safe operating boundary
The scanner is designed for public repositories and respects GitHub API limits. A 5,000-repository map is a scan target, not a completed scan.

## Output
Each repository produces a JSON record. A run also produces a manifest with counts, timestamps, errors, and scanner version.

## Status
Scanner implementation: BUILT.
Local deterministic classification test: TESTED when the test suite passes.
5,000-repository corpus: PLANNED until an authenticated/API-enabled run is executed.
