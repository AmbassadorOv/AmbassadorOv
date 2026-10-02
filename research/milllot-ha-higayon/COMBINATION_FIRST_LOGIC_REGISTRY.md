# Combination-First Logic — Extraction Registry

**Status:** ACTIVE RESEARCH / SOURCE-LOCKED
**Primary source:** Maimonides, *Millot HaHigayon* (מילות ההגיון), Sivan22/otzaria-library, ref d1106d9a66528dc3e39cf1ea0732782927d9f678.
**Repository:** AmbassadorOv/AmbassadorOv

## 0. Governing rule

The project treats **combination/composition (צירוף)** as the primitive analytical operation. “Semantics” is not introduced as an independent computational layer.

Every computational abstraction must be tagged:
- SOURCE_EXPLICIT — stated by the primary source.
- SOURCE_ANALYSIS — structural extraction from source text.
- DERIVED — formalization generated from source structure.
- STRUCTURAL_ANALOGY — comparison, not source identity.
- NOT_YET_VERIFIED — open research question.

## 1. שער א — sentence construction

The source defines: התחלה → נושא; סיפור ההתחלה → נשוא; the predicate may be a name, verb, word, or compound; the complete discourse formed from subject and predicate, affirmative or negative, is משפט / גזירה / מאמר פוסק; a sentence has two structural parts: subject and predicate, even when the sentence contains many words.

### Combination extraction

`C(Subject, Predicate) -> Proposition`

Canonical structural object:
```json
{
  "type": "proposition",
  "subject": "S",
  "predicate": "P",
  "quality": "affirmative|negative",
  "source_status": "SOURCE_ANALYSIS"
}
```

## 2. שער ב — quantity and quality

The source explicitly distinguishes מחייב / שולל; מחייב כללי; מחייב חלקי; שולל כללי; שולל חלקי; סתמי; אישי; כמות המשפט; איכות המשפט.

The four quantified forms arise from the two dimensions quantity × quality. The source also states that an unquantified/סתמי proposition is treated, in logical force, like a particular proposition.

Canonical object:
```json
{
  "type": "proposition",
  "subject": "S",
  "predicate": "P",
  "quantity": "universal|particular|unquantified|individual",
  "quality": "affirmative|negative",
  "source_status": "SOURCE_EXPLICIT"
}
```

Normalization rule:
`unquantified -> particular_force`

## 3. שער ג — temporal/modal operators

The source introduces המשפט השניי, השלישיי, דיבור המציאות, and הצדדים. The second/third distinction concerns how subject and predicate are connected; existence speech supplies specified temporal forms; צדדים include possibilities, impossibility, necessity, requirement and related forms.

Formal research model:
`C(Subject, Predicate, TemporalExistence)`
`C(Proposition, ModalOperator)`

These formulas are SOURCE_ANALYSIS/DERIVED formalizations, not source notation.

## 4. שער ד onward — relation operations

Later extraction files identify operations including contradiction/opposition, conversion, prior/simultaneous relations, genus/species/difference/property/accident, definition versus descriptive indication, shared-name classification, syllogistic structure and middle term, and inference types.

These must be added gate-by-gate rather than collapsed into one semantic layer.

## 5. Source-controlled distinction

Do not write that the six shared-name types are the six seals. The source record distinguishes שער יג (three higher-level name types, with six subdivisions inside משותפים) from Sefer Yetzirah's six-direction/seal structure. Their relationship remains STRUCTURAL_ANALOGY / NOT_YET_VERIFIED.

## 6. Research pipeline

`extract -> classify -> verify status -> formalize -> checkpoint -> commit`

## 7. Next extraction targets

1. Complete שער ג–ח as operation tables.
2. Extract שער ט: transformations/conversions.
3. Extract שער י: genus/species/difference/property/accident and definition/description.
4. Extract שער יא: syllogistic/inference structure.
5. Extract שער יב: prior/simultaneous relations.
6. Preserve שער יג shared-name classification.
7. Extract שער יד as meta-taxonomy and tool status.

## 8. Existing corpus inventory

The repository already contains source extraction files for all 14 gates: `research/milllot-ha-higayon/extractions/GATE_01.md` through `GATE_14.md`, plus integrated files and bundles.

`extractions/INDEX.md` states that source sentences are preserved under their source gate and that mechanical classifications must not be converted into semantic conclusions without source verification.