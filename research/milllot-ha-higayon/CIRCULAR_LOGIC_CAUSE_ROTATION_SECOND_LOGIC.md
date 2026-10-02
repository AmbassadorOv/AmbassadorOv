# Circular Logic — Causes, Transformations, and the Second Logic Layer

**Research status:** SOURCE_EXPLICIT + STRUCTURAL_MODEL
**Primary corpus:** Maimonides, *Millot HaHigayon* extraction corpus in this repository.

## 1. Core observation

The current research axis is not semantic interpretation. It is the movement of already-defined units through ordered combinations and relations.

`unit -> combination -> relation -> transformation -> convergence -> result`

## 2. Gate 4: relation between propositions

Two propositions with the same subject and predicate but opposite quality are classified as מתנגדים. With quantified forms, the source distinguishes היפך, תחת המתהפכים, and two forms of סתירה.

Computational abstraction:
`RELATE(P1,P2) -> opposition_type`

Status: SOURCE_ANALYSIS / DERIVED.

## 3. Gate 5: inversion as an operation

Gate 5 distinguishes היפוך המשפט from הפך המשפט. The defining constraint is preservation or non-preservation of truth, while quality and quantity are also tracked.

Computational abstraction:
`INVERT(P) -> P'`
`VALID_INVERSION(P,P') = preserves_required_structure`

This is the clearest textual basis for treating 'rotation' as a transformation operator over an ordered proposition.

Status: SOURCE_EXPLICIT for inversion; STRUCTURAL_ANALOGY for the geometric word 'rotation'.

## 4. Gates 6–7: combination creates a new logical object

Gate 6 states that two unrelated propositions do not by themselves yield a consequence. When they share one element in a way that permits a third proposition, their composition is an היקש.

The source defines:
- two premises / הקדמות;
- a derived conclusion / תולדה or רדיפה;
- a shared middle boundary / גבול אמצעי;
- two distinct endpoints / קצוות.

Thus:
`P1 + P2 + shared_middle -> P3`

Gate 7 then partitions the possible arrangements into three figures:
`Figure 1: middle term is subject in one premise and predicate in the other`
`Figure 2: middle term is predicate in both premises`
`Figure 3: middle term is subject in both premises`

The source states that the three figures contain 108 possible combinations, of which 14 are valid syllogistic combinations: 4 + 4 + 6.

Therefore the second logic layer has an explicit combinatorial search space:
`candidate_combinations -> figure classification -> valid/invalid -> consequence`

## 5. Gate 8: premise provenance changes the kind of inference

Gate 8 classifies propositions known without demonstration into four sources:
- מוחשים
- מושכלות ראשונות
- מושכלות שניות
- מפורסמות
- מקובלות

It then classifies resulting inferences according to the type of premises: מופת, נצוח, הלצה, הטעיה, שיר.

This creates a provenance-conditioned inference operator:
`INFER(P1,P2, provenance_constraints) -> inference_type`

The source also describes hidden-premise behavior in one rhetorical class, so provenance and visibility of premises are separate variables.

## 6. Gate 9: causes produce a causal relation graph

Gate 9 explicitly gives four causes:
`material -> form -> agent -> purpose`

It also distinguishes near and remote causes and gives a chained example in which multiple events contribute to one later event.

Computational representation:
`CAUSE_CHAIN = [remote_cause -> intermediate_cause -> proximate_cause -> effect]`

The source further states that the same ordering applies to form and purpose, including near and remote purpose.

This is the strongest source basis for the project's 'cause movement' model.

## 7. The circular model

The structural model can therefore be stated without semantic primitives:

`CAUSE -> ACTION/TRANSITION -> RELATION -> COMBINATION -> INVERSION/REORIENTATION -> INFERENCE -> RESULT`

and, for causal depth:
`REMOTE_CAUSE -> INTERMEDIATE_CAUSE -> PROXIMATE_CAUSE -> EFFECT`

The 'circular' term is a computational metaphor for reorientation and return through a relation graph. It must not be treated as a source claim that Maimonides defines a geometric circular logic.

## 8. Connection to the earlier 231-gate layer

The earlier 231-pair system supplies ordered two-letter substrates. The present logic supplies operators that can act on ordered structures:

`letter_pair -> ordered_pair -> proposition_unit -> relation -> inversion -> inference`

The common primitive across the two domains is not meaning but **structured combination under constraints**.

## 9. Connection to the six-way / directional material

The repository's current finding already records that six permutations, wheel/rotation, polarity, and six-direction sealing are only structural hypotheses. They remain distinct from the six shared-name subtypes and from the three logical figures.

Do not collapse:
`6 permutations != 6 seals != 6 name subtypes != 3 syllogistic figures`

The correct research question is whether these structures implement a common operation such as bounded differentiation, orientation, signature, or re-combination.

## 10. Proposed machine representation

```python
LogicalState = {
    'unit': unit,
    'order': ordered_form,
    'relation': relation_type,
    'cause': cause_position,
    'figure': syllogistic_figure,
    'provenance': premise_provenance,
    'transformation': transformation,
    'status': source_status,
}

def transform(state, operator):
    validate_operator(operator, state)
    next_state = apply(operator, state)
    record_transition(state, next_state, operator)
    return next_state
```

Every transition should preserve source provenance and identify whether it is source-explicit, source-analysis, derived, analogy, or not-yet-verified.

## 11. Next extraction

Continue from Gates 10–14 and build one unified operator table containing:
`INPUT_TYPE | OPERATOR | ORDER_CONDITION | SHARED_COMPONENT | OUTPUT_TYPE | SOURCE_GATE | STATUS`.

The critical next target is to determine how the genus/species/differentia/property/accident hierarchy feeds back into the inference engine, rather than treating taxonomy and inference as separate vocabularies.