#!/usr/bin/env python3
"""Check a substitution and write the manifest that declares it. Standard library only.

Run from the repository root:

  python3 tools/pack.py            check submission/substitution.json with the protected
                                   verifier and DAG, print what the hosted gate will
                                   answer, and write submission/submission.json
  python3 tools/pack.py --check    confirm that submission/submission.json declares exactly
                                   the bytes of submission/substitution.json (exit 0 or 1)

The manifest carries the substitution to the protected gate as base64 text of one zlib
stream, in parts of at most 4000 characters. The hosted evaluator allows a declared
input of at most 16,384 bytes, so a substitution whose packed form is larger cannot be
submitted; this tool says so and writes nothing.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True  # a __pycache__ directory must not end up in the repository

ROOT = Path(__file__).resolve().parent.parent
SUBSTITUTION = ROOT / "submission" / "substitution.json"
MANIFEST = ROOT / "submission" / "submission.json"
INPUT_LIMIT = 16384


def gate_module():
    spec = importlib.util.spec_from_file_location("paperdag_gate", str(ROOT / "checkers" / "paperdag_gate.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def canonical_size(value):
    return len(json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":")))


def main(argv):
    gate = gate_module()
    data = SUBSTITUTION.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if "--check" in argv:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        declared = [c for c in manifest.get("checks", []) if c.get("check") == "paperdag_gate"]
        same = len(declared) == 1 and gate.decode(declared[0]["inputs"]["substitution"]) == data
        print(("MATCH" if same else "MISMATCH") + ": submission.json declares "
              + ("exactly" if same else "something other than") + f" the bytes of substitution.json (sha256 {digest})")
        return 0 if same else 1
    inputs = {"substitution": gate.encode(data)}
    answer = gate.run(inputs, root=ROOT)
    print(json.dumps(answer, indent=1, ensure_ascii=False))
    packed = canonical_size(inputs)
    print(f"substitution.json: {len(data)} bytes, sha256 {digest}; declared input: {packed} of {INPUT_LIMIT} bytes")
    if packed > INPUT_LIMIT or len(inputs["substitution"]) > 8:
        print("NOT WRITTEN: the packed substitution is larger than the hosted evaluator accepts. Shorten it.")
        return 1
    if not answer["passed"]:
        print("NOT WRITTEN: the structural checks fail, so this substitution would get no score.")
        return 1
    try:
        title = json.loads(data.decode("utf-8")).get("title") or "Substitution"
    except ValueError:
        title = "Substitution"
    manifest = {
        "version": 1,
        "title": " ".join(str(title).split())[:300],
        "claims": [
            "substitution.json is a VALID substitution of the Praxis paper DAG in the sense of rules.md: "
            "structural checks S1 to S8 pass on exactly these bytes, and "
            + (f"each of the {answer['obligations']} semantic obligations the verifier lists for it (O-discharge, "
               "O-proof, O-cite) holds as stated, with the same constants, bounds and hypotheses."
               if answer["obligations"] else "the verifier lists no semantic obligation for it.")
        ],
        "experiments": [],
        "checks": [{"check": "paperdag_gate", "inputs": inputs}],
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {MANIFEST.relative_to(ROOT)}: {answer['steps']} steps "
          f"({answer['saved']} saved from {answer['base_steps']}), {answer['obligations']} obligations for review")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
