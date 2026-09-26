# Sefer Tagin / Language Logic / Nekudim Orchestration Configuration

## Purpose
Canonical configuration for an evidence-preserving research pipeline connecting:
1. Sefer Tagin extraction
2. Maimonides, Millot HaHigayon — logical/linguistic preparation
3. Maimonides, Guide for the Perplexed — uncertainty/interpretive diagnostics
4. Lurianic Nekudim / Raphach (288) research
5. Atzilut → Nekudim → Beriah/Yetzirah/Assiah hitlabshut modeling
6. Provenance, verification, drift control, and versioned archival

This file defines the orchestration boundary. It does not certify historical, textual, kabbalistic, or scientific claims merely because they appear in the working model.

## Source Intake
### Primary source supplied for the current research branch
- Wikisource: https://he.wikisource.org/wiki/קל%22ח_פתחי_חכמה_(לו_-_נח)
- Scope supplied: Pitchei Chokhmah, openings 36–58 (לו–נח), including the material used here for Nekudim and hitlabshut.
- Intake status: SOURCE_SUPPLIED / NOT_YET_INDEPENDENTLY_VERIFIED

### Existing research source families
- Millot HaHigayon by Maimonides, Hebrew text / R. Moses ibn Tibbon translation as supplied in the working corpus.
- Guide for the Perplexed, introduction and chapter 29, as supplied in the working corpus.
- Etz Chaim / Sha'ar HaNekudim and Raphach material as supplied in the working corpus.
- Sefer Tagin / altered-letter research corpus.

For every source family, preserve exact source location separately from interpretation.

## Research Layers
### Layer A — Cognitive / Linguistic Preparation
Millot HaHigayon
Operational concepts: subject/predicate/proposition; quantity/quality; contradiction/opposition/conversion; necessary/possible/impossible; syllogism and middle term; demonstrative/dialectical/rhetorical/fallacious/poetic inference; equivocal/shared/metaphorical/transferred terminology; genus/species/difference/property/accident; actuality/potentiality; prior/simultaneous relations; internal/external speech; logic as protection against error.
Rule: this layer is a preprocessing and classification layer, not a numerical doubt-weighting layer.

### Layer B — Uncertainty / Interpretation Diagnostics
Guide for the Perplexed
Working classification supplied in the corpus: shared names; metaphor/parable; non-obvious ordering; depth of subject; deliberate concealment; prerequisite introductions; distinction between internal and external discourse.
Rule: classify the source of interpretive difficulty before assigning any downstream research weight.

### Layer C — Nekudim / Raphach Research
Core model: Nekudim → breaking of vessels → Raphach sparks → Beriah/Yetzirah/Assiah → בירור → return/upward integration.
Current research assertions are represented as hypotheses/working mappings unless independently sourced.
Raphach (288): preserve the textual claim of residual/minimal vitality where supported by the supplied source; represent hidden roots/minimal existence weight as a modeling abstraction, not a literal textual equivalence; do not invent a fixed numerical allocation of 288 across Beriah, Yetzirah, and Assiah; do not infer a numerical ascent order without a source.

### Layer D — Hitlabshut / Atzilut-to-BY'A
Working architecture supplied from openings 100–111 / ק–קו: Atzilut structure → hitlabshut by measured portion → downstream manifestation.
Current conceptual components: RDL'A / Atik / Arich Anpin / Abba-Imma / Zeir Anpin; head and dikna distinctions; source/transmission distinctions; measured portion of the mitlabesh and corresponding scope of action; reflection/manifestation into Beriah, Yetzirah, Assiah.
Rule: preserve the distinction between what the source explicitly states and the computational analogy built on top of it.

## Orchestration Pipeline
SOURCE INTAKE → TEXT PRESERVATION → LOCATION/CITATION NORMALIZATION → TERM EXTRACTION → LINGUISTIC CLASSIFICATION → UNCERTAINTY-CAUSE CLASSIFICATION → NEKUDIM/RAPHACH EXTRACTION → HITLABSHUT RELATION EXTRACTION → MODEL MAPPING → PROVENANCE CHECK → CONTRADICTION/DRIFT CHECK → VERIFICATION GATE → ARCHIVAL

### Gate 1 — Text Fidelity
Preserve wording, source location, spelling/transliteration where relevant, and distinguish quotation, paraphrase, inference, and model abstraction.
### Gate 2 — Logical Classification
Apply the Millot HaHigayon vocabulary before downstream weighting.
### Gate 3 — Uncertainty Classification
Classify ambiguity/uncertainty using the working Guide diagnostic map.
### Gate 4 — Raphach Constraint
Any statement about 288 must carry SOURCE_EXPLICIT, DERIVED_FROM_SOURCE, MODEL_ABSTRACTION, or NOT_YET_VERIFIED. A numerical split between BY'A layers is prohibited unless a source explicitly supports it.
### Gate 5 — Hitlabshut Constraint
Any computational representation of hitlabshut must record source passage, component, direction of relation, measured/relative portion if explicitly supplied, and whether the representation is textual, interpretive, or computational.
### Gate 6 — Verification
Allowed states: NOT_YET_VERIFIED, STRUCTURALLY_VALID, REPRESENTATION_ONLY, VERIFIED.
VERIFIED requires the project's existing evidence policy: supporting evidence plus verification receipt. Git history alone is not proof.

## Weighting Boundary
The system may compute a doubt_score only after upstream classification gates have completed.
Dependency: source fidelity → term class → uncertainty cause → evidence status → model representation → optional weighting.
Do not assign a numerical weight directly from a mystical or linguistic label without an explicit transformation rule.

## Storage
### Notion
Role: persistent structured working store. Store daily Sefer Tagin extraction records, four-day syntheses, normalized terminology, source mappings, research notes, and verification status.
### GitHub
Role: canonical versioned research/evidence archive.
Repository: AmbassadorOv/AmbassadorOv
Branch: main
Recommended paths: research/sefer-tagin/; research/milllot-ha-higayon/; research/moreh-nevukhim/; research/nekudim-raphach/; research/hitlabshut/; evidence/sefer-tagin/; evidence/nekudim-raphach/; evidence/hitlabshut/; research/ORCHESTRATION_INDEX.md
Git commits provide repository version history and provenance of repository changes; they are not independent external proof of the underlying historical/textual claims.

## Automation Schedule
Existing: Sefer-Tagin-Daily-Extraction daily at 08:00; four-day synthesis 2026-09-28 22:00.
The configuration records these schedules but does not claim GitHub Actions or another scheduler is currently executing them unless an execution workflow is separately verified.

## Final Output Contract
Every generated research record should expose: source; source_location; extracted_text; classification; interpretation; model_abstraction; provenance; verification_status; verification_evidence; timestamp; commit_or_version.
No field may silently convert interpretation into source fact.

## Current Status
- Sefer Tagin persistence: configured
- GitHub archival: configured
- Millot HaHigayon preprocessing layer: configured
- Guide uncertainty-diagnostic layer: configured
- Nekudim/Raphach branch: configured
- Hitlabshut branch: configured
- Fixed 288 BY'A numerical allocation: NOT DEFINED
- Exact hitlabshut matrices: NOT_YET_VERIFIED
- Full automated execution: NOT CLAIMED
- Next source package: pending user-supplied final file