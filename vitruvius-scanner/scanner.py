#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from urllib.error import HTTPError, URLError

VERSION = "0.1.1"

ARCH_FILES = {
    "pyproject.toml", "package.json", "go.mod", "Cargo.toml", "pom.xml",
    "build.gradle", "requirements.txt", "Dockerfile", "docker-compose.yml",
    "terraform.tf", "main.tf",
}
EVIDENCE_TERMS = (
    "provenance", "evidence", "audit", "trace", "hash",
    "sha256", "rfc3161", "timestamp", "verification", "replay",
)
FAMILY_RULES = [
    ("python-service", ("pyproject.toml", "requirements.txt")),
    ("node-service", ("package.json",)),
    ("go-service", ("go.mod",)),
    ("rust-service", ("Cargo.toml",)),
    ("java-service", ("pom.xml", "build.gradle")),
    ("infrastructure-as-code", ("terraform.tf", "main.tf")),
]

TRANSIENT_HTTP = {429, 500, 502, 503, 504}

def classify(names, text):
    names = set(names)
    families = []
    for fam, need in FAMILY_RULES:
        if any(x in names for x in need):
            families.append(fam)
    low = text.lower()
    evidence = [t for t in EVIDENCE_TERMS if t in low]
    deps = [
        x for x in (
            "openai", "anthropic", "google", "gemini", "langchain",
            "llamaindex", "pydantic", "fastapi", "django",
            "kubernetes", "terraform", "docker",
        ) if x in low
    ]
    return sorted(set(families)), sorted(set(deps)), sorted(set(evidence))

def fetch_json(url, token=None, retries=6):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "WANGA-Vitruvius-Scanner/0.1.1",
    }
    if token:
        headers["Authorization"] = "Bearer " + token
    for attempt in range(retries):
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except HTTPError as e:
            reset = e.headers.get("X-RateLimit-Reset")
            remaining = e.headers.get("X-RateLimit-Remaining")
            if e.code in TRANSIENT_HTTP or (e.code == 403 and remaining == "0"):
                wait = 5 * (2 ** attempt)
                if reset:
                    try:
                        wait = max(wait, int(reset) - int(time.time()) + 2)
                    except ValueError:
                        pass
                wait = min(wait, 3700)
                print(
                    json.dumps({
                        "event": "rate_limit_or_transient",
                        "status": e.code,
                        "attempt": attempt + 1,
                        "sleep_seconds": wait,
                    }),
                    file=sys.stderr,
                    flush=True,
                )
                time.sleep(wait)
                continue
            raise
        except (URLError, TimeoutError):
            if attempt == retries - 1:
                raise
            time.sleep(min(30, 2 ** attempt))
    raise RuntimeError("exhausted retries for " + url)

def scan_repo(full_name, token=None):
    safe_name = urllib.parse.quote(full_name, safe="")
    meta = fetch_json("https://api.github.com/repos/" + safe_name, token)
    branch = meta["default_branch"]
    tree_ref = urllib.parse.quote(branch, safe="")
    tree = fetch_json(
        "https://api.github.com/repos/" + safe_name +
        "/git/trees/" + tree_ref + "?recursive=1",
        token,
    )
    names = [
        x["path"].split("/")[-1]
        for x in tree.get("tree", [])
        if x.get("type") == "blob"
    ]
    candidates = [
        x for x in names
        if x in ARCH_FILES or x.lower().endswith((".yaml", ".yml", ".json", ".toml"))
    ]
    text = "\n".join(candidates)
    fam, deps, evidence = classify(names, text)
    return {
        "repository": full_name,
        "default_branch": branch,
        "stars": meta.get("stargazers_count", 0),
        "architecture_families": fam,
        "dependency_signals": deps,
        "evidence_patterns": evidence,
        "candidate_adapter_files": candidates[:200],
        "scanner_version": VERSION,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos-file", required=True)
    ap.add_argument("--out", default="vitruvius-map.jsonl")
    ap.add_argument("--token", default=os.getenv("GITHUB_TOKEN"))
    args = ap.parse_args()

    repos = [
        x.strip()
        for x in open(args.repos_file, encoding="utf-8")
        if x.strip() and not x.startswith("#")
    ]
    ok = err = 0
    with open(args.out, "w", encoding="utf-8") as f:
        for repo in repos:
            try:
                f.write(json.dumps(scan_repo(repo, args.token), ensure_ascii=False) + "\n")
                ok += 1
            except Exception as e:
                f.write(json.dumps({
                    "repository": repo,
                    "error": str(e),
                    "scanner_version": VERSION,
                }, ensure_ascii=False) + "\n")
                err += 1
            f.flush()
    status = "COMPLETED" if err == 0 and ok == len(repos) else "FAILED"
    print(json.dumps({
        "scanner_version": VERSION,
        "requested": len(repos),
        "scanned": ok,
        "errors": err,
        "status": status,
    }))
    raise SystemExit(0 if status == "COMPLETED" else 2)

if __name__ == "__main__":
    main()
