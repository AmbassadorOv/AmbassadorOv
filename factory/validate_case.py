#!/usr/bin/env python3
"""Validate the structure and integrity requirements of one WANGA pilot case.

This validator does not claim that a case is real or verified by itself.
It checks that required artifacts exist, hashes are internally consistent,
and the case explicitly distinguishes evidence states.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


REQUIRED_FILES = {
    "case_spec.json",
    "prompt.json",
    "response.json",
    "model_metadata.json",
    "criteria_a.json",
    "criteria_b.json",
    "decision_a.json",
    "decision_b.json",
    "manifest.json",
    "manifest.sha256",
    "verification_result.json",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def validate_case(case_dir: Path) -> int:
    missing = sorted(name for name in REQUIRED_FILES if not (case_dir / name).exists())
    if missing:
        print("FAIL: missing required files:")
        for name in missing:
            print(f"  - {name}")
        return 2

    verification = load_json(case_dir / "verification_result.json")
    status = verification.get("status", "NOT_YET_VERIFIED")

    manifest_sha = (case_dir / "manifest.sha256").read_text(encoding="utf-8").strip()
    if not manifest_sha:
        print("FAIL: manifest.sha256 is empty")
        return 2

    manifest_digest = sha256_file(case_dir / "manifest.json")
    recorded_digest = manifest_sha.split()[0]
    if manifest_digest != recorded_digest:
        print("FAIL: manifest SHA-256 mismatch")
        print(f"  computed: {manifest_digest}")
        print(f"  recorded: {recorded_digest}")
        return 2

    spec = load_json(case_dir / "case_spec.json")
    for required_flag in ("model_answer_must_be_captured_live", "target_pattern"):
        if required_flag not in spec:
            print(f"FAIL: case_spec.json missing {required_flag}")
            return 2

    if status == "VERIFIED":
        tsr = case_dir / "manifest.tsr"
        if not tsr.exists() or tsr.stat().st_size == 0:
            print("FAIL: VERIFIED case requires non-empty manifest.tsr")
            return 2

    print(f"PASS: structural validation complete; status={status}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-dir", type=Path, required=True)
    args = parser.parse_args()
    return validate_case(args.case_dir)


if __name__ == "__main__":
    raise SystemExit(main())
