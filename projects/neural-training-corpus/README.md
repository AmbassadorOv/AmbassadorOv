# Neural Training Corpus

## Purpose
A dedicated research project for preparing high-quality training/evaluation material for language-model systems.

## Core principle
The corpus is not a word-counting exercise. Each record preserves the distinction between:

- SOURCE_NODE — the location where information is first established;
- REFERENCE_LINK — a pointer back to an existing source, not automatically new information;
- OPERATIONAL_ASPECT — an independently addressable examination/aspect of the source;
- RELATION — an explicit connection between elements;
- INFERENCE — a derived hypothesis that must not be promoted to extracted fact without evidence.

## Anti-hallucination boundary
Prediction may generate a hypothesis, but prediction cannot promote a hypothesis to verified structure.

Status vocabulary:

EXTRACTED · REFERENCED · INFERRED · UNKNOWN · CONTRADICTED

## Pipeline

RAW SOURCE → SOURCE RESOLUTION → REFERENCE RESOLUTION → ATOMIC DECOMPOSITION → RELATION EXTRACTION → QUESTION/ANSWER RECONSTRUCTION → STRUCTURAL AUDIT → TRAINING/EVALUATION RECORD

## Dataset design

The project is intended to absorb a longitudinal corpus of existing questions, answers, tags and source references. Existing historical tags are preserved as raw evidence before normalization; erroneous tags are not silently deleted because they can become error/negative examples for evaluation.

## Training vs evaluation

Training examples and benchmark examples must remain separately identified. A benchmark record is not treated as ground truth merely because the system generated it.

## Status
SPECIFIED / ACTIVE DEVELOPMENT
