# Logic Spreadsheet System

## Purpose
A structured spreadsheet layer for representing logical material so the system can continue extending the analysis without collapsing distinct examinations into a single label.

## Design rule
Philosophical interpretation alone is not sufficient for this dataset. The spreadsheet must preserve operational structure: source, reference, aspect, relation, operation, condition, validity criterion and evidence status.

## Recommended workbook

1. RAW_SOURCE — immutable source transcription/reference.
2. SOURCE_NODES — first/primary information nodes.
3. REFERENCE_GRAPH — reference links and targets.
4. OPERATIONAL_ASPECTS — atomic examinations.
5. RELATIONS — source/target/relation records.
6. OPERATIONS — transformations/actions extracted from the source.
7. CONDITIONS — preconditions and scope constraints.
8. VALIDITY_CRITERIA — conditions under which a transformation or statement is accepted.
9. QUESTIONS_ANSWERS — question/answer corpus, including reconstructed questions.
10. DRIFT_ERRORS — structural mistakes detected by the Kernel.
11. PROVENANCE — source location, evidence and verification status.
12. INDEX — stable IDs and cross-sheet navigation.

## Stable identifiers

Every record receives a stable ID. References point to IDs rather than duplicating the underlying content.

## Extension rule

New material extends the graph by adding nodes/relations/aspects. It must not overwrite an existing source merely because the wording is similar.

## Status
SPECIFIED / ACTIVE DEVELOPMENT
