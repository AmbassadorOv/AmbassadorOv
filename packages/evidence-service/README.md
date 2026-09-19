# WANGA Evidence-as-a-Service v0.1

Provider-neutral evidence boundary for canonicalization, SHA-256 integrity, replay identifiers, and optional RFC3161 proof attachment.

## Contract

POST /evidence accepts JSON:
{"canonical": <JSON value>, "replay_id": "optional"}

Response:
{"canonical": <canonical JSON>, "sha256": "<64 hex>", "timestamp_proof": null, "replay_id": "...", "status": "HASHED_NOT_TIMESTAMP_VERIFIED"}

The service never claims RFC3161 verification unless a valid token is supplied and independently verified by the configured verification command.

## Status boundary
BUILT: service code exists.
TESTED: local contract tests pass.
VERIFIED: requires an externally generated RFC3161 token plus independent verification.
