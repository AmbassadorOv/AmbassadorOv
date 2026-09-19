#!/usr/bin/env python3
"""Execute the WANGA Insurance Pilot Factory through external provider adapters.

No fake model responses are generated here. A provider adapter must perform
an actual live capture and emit the documented JSON contract.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shlex
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "cases" / "2026-06-drift-pack-insurance-10"


def canonical(obj: Any) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def write_json(path: Path, obj: Any) -> None:
    path.write_bytes(canonical(obj))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def run_adapter(command: str, spec_path: Path) -> dict[str, Any]:
    env = os.environ.copy()
    env["WANGA_CASE_SPEC"] = str(spec_path)
    proc = subprocess.run(
        shlex.split(command),
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"provider adapter failed for {spec_path}: rc={proc.returncode}\n{proc.stderr}"
        )
    try:
        result = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"provider adapter emitted invalid JSON for {spec_path}") from exc
    required = ("provider", "model", "request", "raw_response", "captured_at_utc")
    missing = [k for k in required if k not in result]
    if missing:
        raise RuntimeError(f"provider adapter missing fields: {missing}")
    return result


def run_criterion(command: str, case_dir: Path, criterion_path: Path) -> dict[str, Any]:
    env = os.environ.copy()
    env["WANGA_CASE_DIR"] = str(case_dir)
    env["WANGA_CRITERION"] = str(criterion_path)
    proc = subprocess.run(
        shlex.split(command),
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"criterion adapter failed for {case_dir.name}: rc={proc.returncode}\n{proc.stderr}"
        )
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"criterion adapter emitted invalid JSON for {case_dir.name}") from exc


def capture_case(spec_path: Path, provider_command: str, criterion_command: str) -> None:
    case_dir = spec_path.parent
    response = run_adapter(provider_command, spec_path)
    captured = {
        "case_id": json.loads(spec_path.read_text())["case_id"],
        "provider": response["provider"],
        "model": response["model"],
        "model_version": response.get("model_version"),
        "captured_at_utc": response["captured_at_utc"],
        "request": response["request"],
        "raw_response": response["raw_response"],
        "reproducibility_metadata": response.get("reproducibility_metadata", {}),
        "tool_state": response.get("tool_state", {}),
    }
    write_json(case_dir / "response.json", captured)
    write_json(case_dir / "prompt.json", {"source": json.loads(spec_path.read_text())["question"]})
    write_json(case_dir / "model_metadata.json", {
        "provider": response["provider"],
        "model": response["model"],
        "model_version": response.get("model_version"),
        "captured_at_utc": response["captured_at_utc"],
    })

    spec = json.loads(spec_path.read_text())
    write_json(case_dir / "criteria_a.json", {"criterion": spec["criterion_a"]})
    write_json(case_dir / "criteria_b.json", {"criterion": spec["criterion_b"]})

    a = run_criterion(criterion_command, case_dir, case_dir / "criteria_a.json")
    b = run_criterion(criterion_command, case_dir, case_dir / "criteria_b.json")
    write_json(case_dir / "decision_a.json", a)
    write_json(case_dir / "decision_b.json", b)

    response_hash = sha256(case_dir / "response.json")
    decision_a_hash = sha256(case_dir / "decision_a.json")
    decision_b_hash = sha256(case_dir / "decision_b.json")

    manifest = {
        "case_id": spec["case_id"],
        "state": "CAPTURED",
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "response_sha256": response_hash,
        "decision_a_sha256": decision_a_hash,
        "decision_b_sha256": decision_b_hash,
        "criterion_drift": {
            "decision_a": a,
            "decision_b": b,
            "changed": a != b,
        },
        "verification_pending": True,
        "requires": [
            "manifest SHA-256",
            "external RFC3161 token",
            "replay result",
            "independent verification",
        ],
    }
    write_json(case_dir / "manifest.json", manifest)
    (case_dir / "manifest.sha256").write_text(f"{sha256(case_dir / 'manifest.json')}  manifest.json\n")
    write_json(case_dir / "verification_result.json", {
        "status": "CAPTURED",
        "verified": False,
        "reason": "Live capture and criterion evaluation completed; RFC3161, replay and independent verification remain.",
    })


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider-command", required=True)
    parser.add_argument("--criterion-command", required=True)
    parser.add_argument("--case", action="append", help="case directory name; repeatable")
    args = parser.parse_args()

    specs = sorted(PACK.glob("case-*/case_spec.json"))
    if args.case:
        wanted = set(args.case)
        specs = [p for p in specs if p.parent.name in wanted]

    if not specs:
        raise SystemExit("No case specifications selected.")

    failures = 0
    for spec in specs:
        try:
            capture_case(spec, args.provider_command, args.criterion_command)
            print(f"CAPTURED {spec.parent.name}")
        except Exception as exc:
            failures += 1
            print(f"FAILED {spec.parent.name}: {exc}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
