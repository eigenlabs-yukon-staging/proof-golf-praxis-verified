"""Organizer-owned structural gate for proof-golf-praxis.

Reads one declared input from stdin: {"substitution": ["<part>", ...]}. The parts,
joined, are the base64 text of one zlib stream whose content is the exact bytes of
the submitted substitution.json (tools/pack.py writes them). The gate rebuilds those
bytes, parses them, and runs the protected reference verifier (checkers/paperdag.py)
against the protected DAG (checkers/dag.json).

It reports:
  passed               every structural check S1 to S8 holds
  steps                the score of the resulting DAG, or -1 when passed is false
  substitution_sha256  SHA-256 of the bytes it checked, so that a reader can see
                       that the scored bytes are the submitted substitution.json
  obligation_ids       the semantic obligations the verifier lists
  first_failed_check   the earliest check that fails ("input", "format", "S1" ... "S8"), or ""

It never sees the submitted files and judges no mathematics: a pass says the cut is
well formed and gives its step count. Whether each obligation holds is decided in
review, not here.
"""
import base64
import binascii
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import zlib

# Fixed protected path inside the checker sandbox, never a path supplied by the requester.
SNAPSHOT = Path("/snapshot/files")
MAX_SUBSTITUTION_BYTES = 262144
MAX_OUTPUT_BYTES = 15000  # the runner refuses a result above 16384 canonical bytes
CHECK_ORDER = ["input", "format", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"]


def encode(data, part=4000):
    """Bytes of substitution.json -> the list of parts a submission declares."""
    packed = base64.b64encode(zlib.compress(data, 9)).decode("ascii")
    return [packed[i:i + part] for i in range(0, len(packed), part)]


def decode(parts):
    """The declared parts -> the exact bytes of substitution.json. Raises ValueError."""
    try:
        raw = base64.b64decode("".join(parts).encode("ascii"), validate=True)
    except (binascii.Error, UnicodeError):
        raise ValueError("the parts are not base64 text") from None
    stream = zlib.decompressobj()
    try:
        data = stream.decompress(raw, MAX_SUBSTITUTION_BYTES + 1)
    except zlib.error:
        raise ValueError("the parts are not a zlib stream") from None
    if len(data) > MAX_SUBSTITUTION_BYTES:
        raise ValueError(f"the substitution is larger than {MAX_SUBSTITUTION_BYTES} bytes")
    if not stream.eof or stream.unused_data or stream.unconsumed_tail:
        raise ValueError("the parts are not exactly one complete zlib stream")
    return data


def parse(data):
    """Strict JSON: UTF-8, one object, no repeated key, no NaN or Infinity."""
    def pairs(items):
        seen = {}
        for key, value in items:
            if key in seen:
                raise ValueError(f"the key {key!r} is repeated; a repeated key can be read two ways")
            seen[key] = value
        return seen

    def constant(name):
        raise ValueError(f"{name} is not a JSON value")

    try:
        text = data.decode("utf-8")
    except UnicodeError:
        raise ValueError("the substitution is not UTF-8 text") from None
    try:
        value = json.loads(text, object_pairs_hook=pairs, parse_constant=constant)
    except RecursionError:
        raise ValueError("the substitution is nested too deeply") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"the substitution is not JSON: {exc.msg} at line {exc.lineno}") from None
    if not isinstance(value, dict):
        raise ValueError("the substitution is not a JSON object")
    return value


def reference(root):
    """Load the protected reference verifier from its fixed path."""
    spec = importlib.util.spec_from_file_location("paperdag", str(root / "checkers" / "paperdag.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def clip(text, limit):
    text = " ".join(str(text).split())
    return text if len(text) <= limit else text[:limit - 3] + "..."


def size(value):
    return len(json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":")))


def run(inputs, root=SNAPSHOT):
    out = {"passed": False, "steps": -1, "base_steps": -1, "saved": 0, "removed": 0, "added": 0,
           "obligations": 0, "obligation_ids": [], "first_failed_check": "", "failed_checks": [], "errors": [],
           "substitution_sha256": "", "base": "", "message": ""}
    try:
        paperdag = reference(root)
        dag = paperdag.load(str(root / "checkers" / "dag.json"))
        out["base"] = paperdag.canonical_hash(dag)
        out["base_steps"] = int(paperdag.score(dag)["steps"])
    except Exception as exc:  # the protected bundle itself is broken: never a pass
        out["failed_checks"], out["first_failed_check"] = ["input"], "input"
        out["errors"] = [clip(f"input: the protected DAG or verifier could not be loaded ({type(exc).__name__})", 300)]
        out["message"] = "organizer error: protected bundle unreadable"
        return out
    try:
        data = decode(inputs["substitution"])
        out["substitution_sha256"] = hashlib.sha256(data).hexdigest()
        sub = parse(data)
    except ValueError as exc:
        out["failed_checks"], out["first_failed_check"] = ["input"], "input"
        out["errors"] = [clip(f"input: {exc}", 300)]
        out["message"] = "the declared input is not a readable substitution"
        return out
    try:
        result = paperdag.verify(dag, sub)
        errors = list(result.get("errors") or [])
        ok = result.get("structural_ok") is True and not errors
        steps = result.get("steps")
        if ok and (type(steps) is not int or steps < 0):
            ok, errors = False, [{"check": "S8", "message": "the verifier returned no step count"}]
    except Exception as exc:  # a substitution that breaks the verifier does not pass
        ok, result = False, {}
        errors = [{"check": "format", "message": f"the verifier could not read this substitution ({type(exc).__name__})"}]
    failed = {clip(e.get("check", "format"), 32) if isinstance(e, dict) else "format" for e in errors}
    out["failed_checks"] = sorted(failed, key=lambda c: (CHECK_ORDER.index(c) if c in CHECK_ORDER else 99, c))[:10]
    out["errors"] = [clip(f"{e.get('check', 'format')}: {e.get('message', '')}" if isinstance(e, dict) else e, 300)
                     for e in errors[:12]]
    remove, add = sub.get("remove"), sub.get("add")
    out["removed"] = len(remove) if isinstance(remove, list) else 0
    out["added"] = len(add) if isinstance(add, list) else 0
    if ok:
        obligations = [o for o in (result.get("obligations") or []) if isinstance(o, dict)]
        out.update(passed=True, steps=steps, saved=out["base_steps"] - steps, obligations=len(obligations),
                   obligation_ids=[clip(o.get("id", ""), 120) for o in obligations[:64]],
                   message="structural checks S1 to S8 pass; the semantic obligations are decided in review")
    else:
        out["message"] = clip("structural checks failed: " + ", ".join(out["failed_checks"]), 300)
    out["first_failed_check"] = out["failed_checks"][0] if out["failed_checks"] else ""
    while size(out) > MAX_OUTPUT_BYTES and (out["obligation_ids"] or len(out["errors"]) > 1):
        (out["obligation_ids"] or out["errors"]).pop()
    return out


if __name__ == "__main__":
    print(json.dumps(run(json.load(sys.stdin)), ensure_ascii=True, sort_keys=True))
