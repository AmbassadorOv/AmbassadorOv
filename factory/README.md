# WANGA Insurance Pilot Factory

## Objective

Produce ten **real-model** insurance evidence cases without inventing model outputs or verification results.

## Execution flow

```
case spec
  -> live model capture
  -> canonical response
  -> criterion A evaluation
  -> criterion B evaluation
  -> decision comparison
  -> SHA-256 manifest
  -> RFC3161 timestamp
  -> replay
  -> verification_result
```

## Model capture

The factory is provider-neutral. A run may use public model endpoints or another reproducible capture mechanism. Each capture must record:

- provider;
- model identifier;
- version/snapshot where available;
- request parameters;
- capture timestamp;
- raw response;
- normalized response;
- transport metadata needed for replay;
- tool-use state, if applicable.

The factory must never fabricate a model response or imply that an unexecuted call was executed.

## Criterion Drift Test

For each case:

1. Freeze the original prompt.
2. Capture the model response.
3. Freeze the response artifact.
4. Evaluate the exact same response under criterion A.
5. Evaluate the exact same response under criterion B.
6. Record both decisions.
7. Determine whether the decision changes.
8. Separately replay the model request, if reproducible, to determine whether the model response itself changes.
9. Attribute the observed change only from evidence.

## VERIFIED gate

A case may be marked VERIFIED only when:

```text
LIVE_CAPTURE
+ RESPONSE_HASH
+ CRITERION_A_HASH
+ CRITERION_B_HASH
+ DECISION_TRACE
+ MANIFEST_SHA256
+ RFC3161_TOKEN
+ REPLAY_RESULT
+ INDEPENDENT_VERIFY
= VERIFIED
```

Missing any component => NOT_YET_VERIFIED.

## Output

The completed pack should be consumable as one evidence package by an insurer without requiring access to the private development environment.
