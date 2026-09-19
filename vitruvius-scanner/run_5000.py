#!/usr/bin/env python3
import argparse, concurrent.futures, json, os, subprocess, sys, time
from pathlib import Path

def chunks(items, size):
    for i in range(0, len(items), size):
        yield i // size + 1, items[i:i+size]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repos-file", required=True)
    ap.add_argument("--out-dir", default="vitruvius-runs")
    ap.add_argument("--batch-size", type=int, default=100)
    ap.add_argument("--workers", type=int, default=20)
    ap.add_argument("--retries", type=int, default=3)
    ap.add_argument("--scanner", default="vitruvius-scanner/scanner.py")
    args=ap.parse_args()
    repos=[x.strip() for x in open(args.repos_file,encoding="utf-8") if x.strip() and not x.startswith("#")]
    if not repos: raise SystemExit("No repositories found")
    if len(set(repos)) != len(repos): raise SystemExit("Repository corpus contains duplicates")
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    batches=list(chunks(repos,args.batch_size))
    summary={"requested":len(repos),"batch_size":args.batch_size,"batches":len(batches),"completed":0,"failed":0}
    def run(item):
        n, rs=item
        inp=out/f"batch-{n:04d}.repos"
        result=out/f"batch-{n:04d}.jsonl"
        status=out/f"batch-{n:04d}.status.json"
        if status.exists():
            try:
                s=json.loads(status.read_text())
                if s.get("status")=="COMPLETED": return n,"SKIPPED_COMPLETED"
            except Exception: pass
        inp.write_text("\n".join(rs)+"\n",encoding="utf-8")
        env=os.environ.copy()
        env["GITHUB_TOKEN"]=os.environ.get("GITHUB_TOKEN","")
        cmd=[sys.executable,args.scanner,"--repos-file",str(inp),"--out",str(result)]
        p=None
        attempts=0
        for attempt in range(args.retries+1):
            attempts=attempt+1
            p=subprocess.run(cmd,env=env,text=True,capture_output=True)
            if p.returncode==0:
                break
            if attempt < args.retries:
                time.sleep(min(60,5*(attempt+1)))
        status.write_text(json.dumps({"batch":n,"requested":len(rs),"attempts":attempts,"status":"COMPLETED" if p.returncode==0 else "FAILED","returncode":p.returncode,"stdout":p.stdout[-4000:],"stderr":p.stderr[-4000:]},ensure_ascii=False,indent=2),encoding="utf-8")
        return n,"COMPLETED" if p.returncode==0 else "FAILED"
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        for n,state in ex.map(run,batches):
            if state in ("COMPLETED","SKIPPED_COMPLETED"): summary["completed"]+=1
            else: summary["failed"]+=1
            print(json.dumps({"batch":n,"state":state}),flush=True)
    summary["status"]="COMPLETED" if summary["failed"]==0 else "PARTIAL_FAILURE"
    (out/"SUMMARY.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(summary))
    raise SystemExit(0 if summary["failed"]==0 else 2)

if __name__=="__main__":
    main()
