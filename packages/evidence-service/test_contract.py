import hashlib, json
from server import canonical_bytes

def test_canonicalization_is_stable():
    a={"z":1,"a":[2,{"b":True,"a":"x"}]}
    b={"a":[2,{"a":"x","b":True}],"z":1}
    assert canonical_bytes(a)==canonical_bytes(b)
    assert hashlib.sha256(canonical_bytes(a)).hexdigest()==hashlib.sha256(canonical_bytes(b)).hexdigest()

if __name__=="__main__":
    test_canonicalization_is_stable()
    print("PASS")
