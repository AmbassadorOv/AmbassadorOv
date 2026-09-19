from scanner import classify
def test_classification():
    fam,deps,evidence=classify(["pyproject.toml","README.md"],"fastapi provenance sha256")
    assert "python-service" in fam
    assert "fastapi" in deps
    assert "provenance" in evidence and "sha256" in evidence
if __name__=="__main__":
    test_classification(); print("PASS")
