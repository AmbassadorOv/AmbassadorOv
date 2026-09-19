#!/usr/bin/env python3
import hashlib, json, os, secrets
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST=os.getenv("WANGA_EVIDENCE_HOST","127.0.0.1")
PORT=int(os.getenv("WANGA_EVIDENCE_PORT","8080"))

def canonical_bytes(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",",":")).encode("utf-8")

class Handler(BaseHTTPRequestHandler):
    def send_json(self, code, obj):
        body=json.dumps(obj, ensure_ascii=False, sort_keys=True).encode("utf-8")
        self.send_response(code); self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body)
    def do_POST(self):
        if self.path!="/evidence": self.send_json(404,{"error":"not_found"}); return
        try:
            n=int(self.headers.get("Content-Length","0")); payload=json.loads(self.rfile.read(n))
            if "canonical" not in payload: raise ValueError("canonical is required")
            raw=canonical_bytes(payload["canonical"])
            replay_id=payload.get("replay_id") or secrets.token_hex(16)
            self.send_json(200,{"canonical":json.loads(raw.decode("utf-8")),
                "sha256":hashlib.sha256(raw).hexdigest(),
                "timestamp_proof":None,"replay_id":replay_id,
                "status":"HASHED_NOT_TIMESTAMP_VERIFIED"})
        except Exception as e: self.send_json(400,{"error":str(e)})
    def log_message(self,*args): pass

if __name__=="__main__":
    HTTPServer((HOST,PORT),Handler).serve_forever()
