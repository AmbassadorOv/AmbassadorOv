# Sefer Tagin Automation Configuration

## Purpose

Canonical configuration for the systematic Sefer Tagin extraction workflow and its evidence-preserving storage destinations.

## Extraction

- Daily extraction: `Sefer-Tagin-Daily-Extraction`
- Cadence: daily at 08:00
- Unit: next missing letter
- Output fields:
  - letter
  - tagin count
  - verse references
  - form/type classification
  - source reference
  - extraction timestamp
  - verification/status

## Synthesis

- Four-day synthesis
- Schedule: 2026-09-28 22:00
- Input: preceding four daily extraction records
- Output:
  - consolidated table
  - missing items
  - status of each extracted item
  - provenance references

## Storage Destinations

### Notion

- Role: persistent structured working store
- Use: cumulative extraction records and synthesis

### GitHub

- Role: canonical versioned research/evidence archive
- Repository: `AmbassadorOv/AmbassadorOv`
- Default branch: `main`
- Recommended path:
  - `research/sefer-tagin/` — extraction records and research artifacts
  - `evidence/sefer-tagin/` — preserved evidence and verification artifacts
- Every persisted record should retain provenance and status.
- GitHub commits provide version history; a commit must not be treated as independent external proof of the underlying historical/textual claim.

## Integrity Rules

1. Preserve the source wording and source location.
2. Separate extracted text from interpretation.
3. Do not invent missing numerical allocations, including any proposed allocation of the 288 ניצוצות.
4. Use explicit status values such as `NOT_YET_VERIFIED`, `STRUCTURALLY_VALID`, and `REPRESENTATION_ONLY` where applicable.
5. Do not promote a record to `VERIFIED` without the required evidence and verification receipt.
6. Notion is the working store; GitHub is the versioned archival/source-of-truth layer for committed research artifacts.

## Current Scope

This configuration records GitHub as an additional persistence destination. It does not claim that the daily extraction automation is currently executing from GitHub Actions.
