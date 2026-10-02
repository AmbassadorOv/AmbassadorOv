# Logic Operation Matrix — Gates 1–4

**Purpose:** source-locked extraction of operations for the project's combination-first logic.

| Gate | Source-defined structure | Operation extracted | Status |
|---|---|---|---|
| א | נושא + נשוא → משפט | COMBINE | SOURCE_ANALYSIS |
| ב | כמות + איכות determine proposition type | CLASSIFY / NORMALIZE | SOURCE_EXPLICIT + DERIVED |
| ג | predicate/action/name + temporal/existence/modal connector | CONNECT / MODALIZE | SOURCE_ANALYSIS |
| ד | same subject/predicate with quality/quantity variation | RELATE / CONTRADICT / OPPOSITION / MODAL-CLASSIFY | SOURCE_EXPLICIT |

## Gate 1 operators

`C(subject, predicate) -> proposition`

Additional source-derived decomposition:
`proposition -> subject + predicate`

Predicate inputs explicitly include name, verb, word, and compound.

## Gate 2 operators

`Q = quantity`
`A = quality`
`P = proposition(Q,A)`

Four quantified forms:
- מחייב כללי
- מחייב חלקי
- שולל כללי
- שולל חלקי

Additional types:
- סתמי
- אישי

Normalization:
`unquantified proposition -> particular force`

## Gate 3 operators

`CONNECT(subject, predicate, temporal_existence)`
`MODALIZE(proposition, side)`

Source terms include:
- המשפט השניי
- השלישיי
- דיבור המציאות
- הצדדים

## Gate 4 relation operators

### 1. Opposition
`OPPOSE(P1,P2)` when subject and predicate are the same and one proposition affirms while the other denies.

### 2. Contrariety / היפך
Source distinguishes quantified oppositions and names the relevant relation.

### 3. Contradiction / סתירה
Source distinguishes cases where one has universal quantity and the other particular quantity, with opposite quality; it explicitly identifies two forms.

### 4. Modal classification
The gate explicitly distinguishes:
`NECESSARY`, `POSSIBLE`, `IMPOSSIBLE`, and later `DETERMINATE/PRESENT` forms.

Important source rule: the modal status can change when a future possibility becomes an actual/present state. This is recorded as a source-derived temporal-state transition, not as an external modal-logic claim.

## Cross-gate composition

`Gate 1: units -> proposition`
`Gate 2: proposition -> typed proposition`
`Gate 3: proposition -> temporally/modalized proposition`
`Gate 4: proposition + proposition -> relation`

This produces a recursive architecture:
`unit -> combine -> proposition -> classify -> transform/modalize -> relate to another proposition`

## Boundary

This file records structural operations. It does not introduce a semantic layer. Any analogy to modern formal logic must be tagged as a comparison, not source identity.