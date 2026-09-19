# WANGA Pilot Factory Capture Protocol

This protocol defines the only accepted input path for live-model capture.

## Provider adapter contract

The factory invokes a provider adapter command once per case:

```text
ADAPTER_COMMAND CASE_SPEC_JSON > CAPTURE_JSON
```

The adapter must emit one JSON object with:

- provider
- model
- model_version (if available)
- request
- raw_response
- captured_at_utc
- reproducibility_metadata
- tool_state

The adapter must return a non-zero exit code when no live model call was performed.

## Criterion adapter contract

A criterion adapter receives:

```json
{
  "case_spec": {},
  "prompt": {},
  "response": {},
  "criterion": {}
}
```

and must emit:

```json
{
  "decision": {},
  "reasoning_trace": {},
  "evaluation_metadata": {}
}
```

## Verification invariant

The same captured response artifact must be passed to criterion A and criterion B.

The factory must not re-query the model while evaluating the two criteria.

## Evidence states

- READY_FOR_CAPTURE
- CAPTURED
- TESTED
- VERIFIED
- REJECTED

A case cannot transition directly from READY_FOR_CAPTURE to VERIFIED.
