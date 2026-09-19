#!/usr/bin/env python3
import argparse, hashlib, json
from collections import Counter
from pathlib import Path

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",required=True)
    ap.add_argument("--output-dir",required=True)
    args=ap.parse_args()
    inp=Path(args.input_dir); out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    records=[]
    for p in sorted(inp.rglob("batch-*.jsonl")):
        for line_no,line in enumerate(p.read_text(encoding="utf-8").splitlines(),1):
            if not line.strip(): continue
            try: r=json.loads(line)
            except Exception as e: r={"_parse_error":str(e)}
            r["_source"]=str(p); r["_line"]=line_no; records.append(r)
    by_repo={}; duplicates=[]
    for r in records:
        repo=r.get("repository")
        if not repo: continue
        if repo in by_repo: duplicates.append(repo)
        by_repo[repo]=r
    families=Counter(); deps=Counter(); evidence=Counter()
    for r in by_repo.values():
        for x in r.get("architecture_families",[]): families[x]+=1
        for x in r.get("dependency_signals",[]): deps[x]+=1
        for x in r.get("evidence_patterns",[]): evidence[x]+=1
    errors=sum("error" in r or "_parse_error" in r for r in by_repo.values())
    with (out/"normalized.jsonl").open("w",encoding="utf-8") as f:
        for repo in sorted(by_repo):
            r=by_repo[repo]
            f.write(json.dumps({
                "repository":repo,
                "status":"ERROR" if ("error" in r or "_parse_error" in r) else "OBSERVED",
                "default_branch":r.get("default_branch"),
                "stars":r.get("stars",0),
                "architecture_families":sorted(r.get("architecture_families",[])),
                "dependency_signals":sorted(r.get("dependency_signals",[])),
                "evidence_patterns":sorted(r.get("evidence_patterns",[])),
                "candidate_adapter_files":sorted(r.get("candidate_adapter_files",[])),
                "scanner_version":r.get("scanner_version"),
                "error":r.get("error") or r.get("_parse_error")
            },ensure_ascii=False,sort_keys=True)+"\n")
    total=len(by_repo); observed=total-errors
    report={"analysis_version":"0.1.0","classification_boundary":"Repository architecture/evidence signals only; not a claim of model drift.","repositories":total,"observed":observed,"errors":errors,"duplicate_repository_records":len(duplicates),"architecture_families":families.most_common(),"dependency_signals":deps.most_common(),"evidence_patterns":evidence.most_common()}
    (out/"FORENSIC_SUMMARY.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    md=["# Vitruvius 5000 — Stage 3 Forensic Analysis","","## Scope","Deterministic normalization and aggregation of scanner observations. This does not infer model behavior or prove drift.","",f"- Repository records: {total}",f"- Observed successfully: {observed}",f"- Scan errors: {errors}",f"- Duplicate repository records: {len(duplicates)}","","## Architecture families"]
    md += [f"- {k}: {v}" for k,v in families.most_common()]
    md += ["","## Dependency signals"]+[f"- {k}: {v}" for k,v in deps.most_common()]
    md += ["","## Evidence/provenance patterns"]+[f"- {k}: {v}" for k,v in evidence.most_common()]
    md += ["","## Verification boundary","- Raw batch JSONL remains the observation layer.","- normalized.jsonl is the deterministic normalized layer.","- FORENSIC_SUMMARY.json is the aggregate layer.","- ARTIFACT_MANIFEST.json provides integrity references."]
    (out/"FORENSIC_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    manifest=[]
    for p in sorted(out.iterdir()):
        if p.is_file(): manifest.append({"file":p.name,"sha256":sha256(p),"bytes":p.stat().st_size})
    (out/"ARTIFACT_MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__": main()
