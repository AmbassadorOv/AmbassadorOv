#!/usr/bin/env python3
import argparse,json,os,re,sys,time,urllib.request
from urllib.error import HTTPError

VERSION="0.1.0"
ARCH_FILES={"pyproject.toml","package.json","go.mod","Cargo.toml","pom.xml","build.gradle","requirements.txt","Dockerfile","docker-compose.yml","terraform.tf","main.tf"}
EVIDENCE_TERMS=("provenance","evidence","audit","trace","hash","sha256","rfc3161","timestamp","verification","replay")
FAMILY_RULES=[
("python-service",("pyproject.toml","requirements.txt")),
("node-service",("package.json",)),
("go-service",("go.mod",)),
("rust-service",("Cargo.toml",)),
("java-service",("pom.xml","build.gradle")),
("infrastructure-as-code",("terraform.tf","main.tf")),
]
def classify(names,text):
    names=set(names); families=[]
    for fam,need in FAMILY_RULES:
        if any(x in names for x in need): families.append(fam)
    low=text.lower()
    evidence=[t for t in EVIDENCE_TERMS if t in low]
    deps=[x for x in ("openai","anthropic","google","gemini","langchain","llamaindex","pydantic","fastapi","django","kubernetes","terraform","docker") if x in low]
    return sorted(set(families)),sorted(set(deps)),sorted(set(evidence))
def fetch_json(url,token=None):
    req=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","User-Agent":"WANGA-Vitruvius-Scanner/0.1"})
    if token: req.add_header("Authorization","Bearer "+token)
    with urllib.request.urlopen(req,timeout=30) as r: return json.load(r)
def scan_repo(full_name,token=None):
    meta=fetch_json("https://api.github.com/repos/"+full_name,token)
    tree=fetch_json("https://api.github.com/repos/"+full_name+"/git/trees/"+meta["default_branch"]+"?recursive=1",token)
    names=[x["path"].split("/")[-1] for x in tree.get("tree",[]) if x.get("type")=="blob"]
    candidates=[x for x in names if x in ARCH_FILES or x.lower().endswith((".yaml",".yml",".json",".toml"))]
    text="\n".join(candidates)
    fam,deps,evidence=classify(names,text)
    return {"repository":full_name,"default_branch":meta["default_branch"],"stars":meta.get("stargazers_count",0),"architecture_families":fam,"dependency_signals":deps,"evidence_patterns":evidence,"candidate_adapter_files":candidates[:200],"scanner_version":VERSION}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repos-file"); ap.add_argument("--out",default="vitruvius-map.jsonl"); ap.add_argument("--token",default=os.getenv("GITHUB_TOKEN")); args=ap.parse_args()
    if not args.repos_file: ap.error("--repos-file is required")
    repos=[x.strip() for x in open(args.repos_file) if x.strip() and not x.startswith("#")]
    ok=err=0
    with open(args.out,"w",encoding="utf-8") as f:
        for repo in repos:
            try: f.write(json.dumps(scan_repo(repo,args.token),ensure_ascii=False)+"\n"); ok+=1
            except Exception as e: f.write(json.dumps({"repository":repo,"error":str(e),"scanner_version":VERSION})+"\n"); err+=1
            time.sleep(0.1)
    print(json.dumps({"scanner_version":VERSION,"requested":len(repos),"scanned":ok,"errors":err,"status":"BUILT_NOT_VERIFIED"}))
if __name__=="__main__": main()
