# WANGA Insurance Pilot Factory — Status

## Current implementation state

**Factory:** BUILT  
**Case specifications:** 10 / 10 READY_FOR_CAPTURE  
**Live model captures:** 0 / 10  
**Verified cases:** 0 / 10

The repository intentionally does not fabricate real-model outputs.

## To execute

The factory requires:

1. A provider adapter with valid access to the selected model provider(s).
2. A criterion evaluator.
3. The existing RFC3161 evidence workflow.
4. A reproducible replay mechanism.

Example:

```bash
python3 factory/run_factory.py \
  --provider-command "python3 adapters/provider_adapter.py" \
  --criterion-command "python3 adapters/criterion_adapter.py"
```

The provider adapter must perform the actual model call. The factory stores the returned response, metadata and hashes and evaluates the same captured response under both criteria.

## VERIFIED gate

A case is VERIFIED only after:

```text
LIVE_CAPTURE
+ RESPONSE_HASH
+ CRITERION_A/B
+ DECISION_TRACE
+ MANIFEST_SHA256
+ RFC3161_TOKEN
+ REPLAY_RESULT
+ INDEPENDENT_VERIFY
```

No repository document should describe the 10-case pack as "10 verified real-world artifacts" until all ten cases satisfy this gate.
