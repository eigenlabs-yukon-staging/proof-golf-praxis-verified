#!/usr/bin/env python3
"""paper-dag/1: lint, score, hash and verify a substitution. Standard library only.

The reference verifier of the paper-dag skill. It implements the structural checks S1 to S8 of
references/format.md and lists the semantic obligations; it judges none of them. S6 includes the
full-proofs floor: a proof that names a removed node or uses deferral or sketch wording is refused.

  python3 paperdag.py lint dag.json
  python3 paperdag.py score dag.json
  python3 paperdag.py hash dag.json
  python3 paperdag.py verify dag.json substitution.json --out result.json [--write-dag new_dag.json]
"""
import hashlib
import json
import math
import re
import sys

RESULTS = ("theorem", "lemma", "proposition", "corollary")

# The full-proofs floor of S6. A proof must be complete in its own words: wording that defers to the paper, to
# the original or a removed proof, or to the reader, and wording that announces a sketch or an idea, is refused
# by code before any reviewer reads it. Passing this floor proves nothing: the reviewer still judges the proof.
DEFERRAL = [
    r"\b(?:the|this|that|their) (?:paper|article|preprint|manuscript|source)\b",
    r"\b(?:original|published|authors'?|author's|base|previous|former|old|replaced|removed|deleted|existing) "
    r"(?:proof|proofs|argument|arguments|derivation|text|version|paper|lemma|node|nodes|dag)\b",
    r"\b(?:same|identical) (?:proof|argument|reasoning|derivation) as\b",
    r"\b(?:proof|argument|derivation|reasoning) (?:is|remains|stays|goes|carries over) (?:the same|unchanged|as before|identical|verbatim)\b",
    r"\bas (?:before|in the original|originally|in the base)\b",
    r"\b(?:unchanged|verbatim|mutatis mutandis)\b",
    r"\bpraxis-lean\b|\beprint\b|\barxiv\b",
    r"\bleft (?:to|for) the reader\b|\bleft as an exercise\b|\bexercise for the reader\b",
    r"\b(?:proof|proofs|details?|verification|calculation|computation|argument|rest|remainder|remaining cases?|other cases?) "
    r"(?:is |are |was |were )?(?:omitted|left out|skipped|routine|not given|not shown)\b",
    r"\bwe (?:omit|skip|leave|do not give|do not prove)\b|\bomitted\b",
    r"\b(?:todo|tbd|to be completed|to be filled|to be written|placeholder)\b",
    r"\b(?:proof )?(?:sketch|outline)\b|\bsketch of\b|\b(?:the|main|key|proof) idea\b|\bidea of (?:the )?proof\b|^\s*idea\b",
    r"\bin (?:brief|outline)\b|\broughly speaking\b|\bheuristically\b|\bintuitively\b",
]
_DEFERRAL = [re.compile(p, re.I) for p in DEFERRAL]


def deferral(proof, removed_nodes):
    """The first wording in `proof` that the full-proofs floor refuses, or "" if there is none."""
    text = norm(proof)
    for rx in _DEFERRAL:
        m = rx.search(text)
        if m:
            return m.group(0)
    for n in removed_nodes:
        for name in (n.get("id"), n.get("label")):
            if isinstance(name, str) and len(name) >= 3:
                m = re.search(r"(?<![\w:.-])" + re.escape(name) + r"(?![\w'\u2032\u2019:-]|\.\d)", text, re.I)
                if m:
                    return m.group(0)
    return ""

SUB_FORMAT = "paper-dag-substitution/1"
DAG_FORMAT = "paper-dag/1"


def load(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def norm(text):
    return " ".join(text.split()) if isinstance(text, str) else ""


# Score: proof steps (paper-dag-steps-v1).
# A proof is split into steps: a new line, or the end of a sentence or clause (".", ";" or ":" followed by space).
# A step costs 1, plus 1 for every further STEP_TOKENS canonical tokens in it. Canonical tokens are words, numbers
# and single symbols after LaTeX markup is dropped, so $\mathbf{W}$, \mathbf{W} and W are each one token. A
# result costs the steps of its proof; its statement is free, so merging or splitting results does not change the
# score. A cited theorem costs 1.
STEP_TOKENS = 60
_ENV = re.compile(r"\\(begin|end)\{[^}]*\}(\[[^\]]*\])?")
_REF = re.compile(r"\\(cref|Cref|ref|cite|label|eqref)\*?(\[[^\]]*\])?\{[^}]*\}")
_STYLE = re.compile(r"\\(mathbf|mathrm|mathsf|mathcal|mathbb|mathfrak|mathit|bm|textsf|textit|textbf|textrm|text|"
                    r"emph|operatorname|hat|tilde|bar|overline|left|right|big|Big|bigl|bigr|Bigl|Bigr|displaystyle)\b\s*")
_MACRO = re.compile(r"\\[a-zA-Z]+")
_MARK = re.compile(r"[{}$&]|\\[,;:! ]|~")
_TOKEN = re.compile(r"[^\W\d_]+|\d+|[^\w\s]")
_PUNCT = set(".,;:()[]")
_SPLIT = re.compile(r"(?<=[.;:])\s+|\n+")


def plain(text):
    """Drop LaTeX markup: environments, references, style macros, braces and dollars; other macros become one symbol."""
    t = text if isinstance(text, str) else ""
    t = _ENV.sub(" ", t)
    t = _REF.sub(" R ", t)
    t = _STYLE.sub(" ", t)
    t = _MACRO.sub(" x ", t)
    return _MARK.sub(" ", t)


def tokens(unit):
    return [x for x in _TOKEN.findall(unit) if x not in _PUNCT]


def steps(text):
    total = 0
    for unit in _SPLIT.split(plain(text)):
        n = len(tokens(unit))
        if n:
            total += 1 + (n - 1) // STEP_TOKENS
    return total


def cost(node, width=None):
    kind = node.get("kind")
    if kind in RESULTS:
        return steps(node.get("proof"))
    if kind == "external":
        return 1
    return 0


def score(dag):
    by_node = {n["id"]: cost(n) for n in dag["nodes"] if n.get("kind") != "blob"}
    return {"steps": sum(by_node.values()), "by_node": by_node}


def canonical_hash(dag):
    text = json.dumps(dag, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _acyclic(ids, edges):
    indegree = {i: 0 for i in ids}
    out = {i: [] for i in ids}
    for a, b in edges:
        if a in out and b in indegree:
            out[a].append(b)
            indegree[b] += 1
    queue = [i for i, d in indegree.items() if d == 0]
    seen = 0
    while queue:
        i = queue.pop()
        seen += 1
        for j in out[i]:
            indegree[j] -= 1
            if indegree[j] == 0:
                queue.append(j)
    return seen == len(indegree)


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def lint(dag):
    errors, warnings = [], []
    if not isinstance(dag, dict) or dag.get("format") != DAG_FORMAT:
        return {"errors": ["format is not " + DAG_FORMAT], "warnings": []}
    ids = set()
    for n in dag.get("nodes", []):
        i = n.get("id")
        if not _text(i) or " " in i or i in ids:
            errors.append(f"node id missing, repeated or with a space: {i!r}")
            continue
        ids.add(i)
        kind = n.get("kind")
        if kind not in RESULTS + ("external", "blob"):
            errors.append(f"{i}: unknown kind {kind!r}")
        if not _text(n.get("statement")):
            errors.append(f"{i}: empty statement")
        if kind in RESULTS and not _text(n.get("proof")):
            errors.append(f"{i}: a result needs a proof")
    kinds = {n.get("id"): n.get("kind") for n in dag.get("nodes", [])}
    for e in dag.get("edges", []):
        a, b = e.get("from"), e.get("to")
        if a not in ids or b not in ids:
            errors.append(f"edge {a} -> {b}: unknown node")
            continue
        if e.get("kind") not in ("uses", "background"):
            errors.append(f"edge {a} -> {b}: kind must be uses or background")
        if e.get("kind") == "uses" and not _text(e.get("demand")):
            errors.append(f"edge {a} -> {b}: a uses edge needs a demand")
        if e.get("kind") == "background" and kinds.get(a) != "blob":
            errors.append(f"edge {a} -> {b}: a background edge starts at a blob")
        if e.get("leaky"):
            warnings.append(f"edge {a} -> {b}: leaky")
    if not _acyclic(ids, [(e.get("from"), e.get("to")) for e in dag.get("edges", [])]):
        errors.append("the graph has a cycle")
    for t in dag.get("targets", []):
        if kinds.get(t) not in RESULTS:
            errors.append(f"target {t} is missing or not a result")
    return {"errors": errors, "warnings": warnings}


def _plan(dag, sub):
    """Everything S1 to S7 needs, with the errors found on the way."""
    errors = []

    def err(check, message):
        errors.append({"check": check, "message": message})

    nodes = {n["id"]: n for n in dag["nodes"]}
    remove = sub.get("remove")
    add = sub.get("add")
    edges = sub.get("edges")
    discharge = sub.get("discharge")
    replaces = sub.get("replaces", {})
    for name, value, kind in (("remove", remove, list), ("add", add, list), ("edges", edges, list),
                              ("discharge", discharge, list), ("replaces", replaces, dict)):
        if not isinstance(value, kind):
            err("format", f"`{name}` is missing or not a {kind.__name__}")
    if sub.get("format") != SUB_FORMAT:
        err("format", "format is not " + SUB_FORMAT)
    if errors:
        return None, errors

    # S1
    held = canonical_hash(dag)
    if sub.get("base") != held:
        err("S1", f"base is not the hash of the DAG the verifier holds ({held})")

    # S2
    removed = set()
    for i in remove:
        if not isinstance(i, str) or i not in nodes:
            err("S2", f"remove lists {i!r}, which is not a node of the base")
        elif nodes[i].get("kind") == "blob":
            err("S2", f"remove lists the blob {i}; blobs are fixed")
        elif i in removed:
            err("S2", f"remove lists {i} twice")
        else:
            removed.add(i)
    added = {}
    for n in add:
        i = n.get("id") if isinstance(n, dict) else None
        if not _text(i) or " " in i:
            err("S2", f"an added node has no usable id: {i!r}")
        elif i in nodes:
            err("S2", f"added id {i} is already a node of the base")
        elif i in added:
            err("S2", f"added id {i} is used twice")
        elif n.get("kind") not in RESULTS + ("external",):
            err("S2", f"added node {i} has kind {n.get('kind')!r}; only results and externals can be added")
        else:
            added[i] = n
    kept = {i for i in nodes if i not in removed}

    # S3
    targets = list(dag.get("targets", []))
    new_targets = []
    for key, value in replaces.items():
        if key not in added or added[key].get("kind") not in RESULTS:
            err("S3", f"replaces maps {key!r}, which is not an added result")
        if value not in removed:
            err("S3", f"replaces names {value!r}, which is not a removed node")
    for t in targets:
        if t not in removed:
            new_targets.append(t)
            continue
        heirs = [k for k, v in replaces.items() if v == t and k in added and added[k].get("kind") in RESULTS]
        if len(heirs) != 1:
            err("S3", f"target {t} is removed and replaces maps {len(heirs)} added results to it, not exactly one")
        elif norm(added[heirs[0]].get("statement")) != norm(nodes[t].get("statement")):
            err("S3", f"the statement of {heirs[0]} is not identical to that of the target {t}")
        else:
            new_targets.append(heirs[0])

    # S4
    obligations = {(e["from"], e["to"]): e for e in dag["edges"] if e["from"] in removed and e["to"] in kept}
    met = {}
    for d in discharge:
        edge = d.get("edge") if isinstance(d, dict) else None
        key = tuple(edge) if isinstance(edge, list) and len(edge) == 2 and all(isinstance(x, str) for x in edge) else None
        if key is None or key not in obligations:
            err("S4", f"discharge names {edge!r}, which is not an obligation of this cut")
            continue
        if key in met:
            err("S4", f"edge {key[0]} -> {key[1]} is discharged more than once")
            continue
        by = d.get("by")
        if not isinstance(by, list) or not by or any(b not in added and b not in kept for b in by):
            err("S4", f"edge {key[0]} -> {key[1]}: `by` must be a non-empty list of added or kept nodes")
            continue
        if any(nodes.get(b, {}).get("kind") == "blob" for b in by):
            err("S4", f"edge {key[0]} -> {key[1]}: `by` names a blob; blobs give background, not results, "
                      "so an obligation is discharged only by results and externals")
            continue
        if not _text(d.get("argument")):
            err("S4", f"edge {key[0]} -> {key[1]}: empty argument")
            continue
        met[key] = d
    for key in obligations:
        if key not in met:
            err("S4", f"edge {key[0]} -> {key[1]} leaves the removed set and is not discharged")

    # S5
    good_edges = []
    for e in edges:
        a, b = (e.get("from"), e.get("to")) if isinstance(e, dict) else (None, None)
        if b not in added:
            err("S5", f"edge {a} -> {b} does not end at an added node")
        elif a not in added and a not in kept:
            err("S5", f"edge {a} -> {b} does not start at an added node, a kept node or a blob")
        elif e.get("kind") not in ("uses", "background"):
            err("S5", f"edge {a} -> {b}: kind must be uses or background")
        elif e.get("kind") == "uses" and nodes.get(a, {}).get("kind") == "blob":
            err("S5", f"edge {a} -> {b}: an edge from a blob is a background edge, never uses")
        elif e.get("kind") == "uses" and not _text(e.get("demand")):
            err("S5", f"edge {a} -> {b}: a uses edge carries a non-empty demand")
        else:
            good_edges.append(e)

    # S6
    deny = [d.lower() for d in dag.get("import_denylist", []) if isinstance(d, str) and d]
    for i, n in added.items():
        if n.get("kind") in RESULTS:
            if not _text(n.get("statement")) or not _text(n.get("proof")):
                err("S6", f"added result {i} needs a non-empty statement and proof")
            else:
                bad = deferral(n.get("proof"), [nodes[r] for r in (remove if isinstance(remove, list) else []) if isinstance(r, str) and r in nodes])
                if bad:
                    err("S6", f"added result {i}: the proof must be complete in its own words, and {bad!r} defers to "
                              "the paper, to a removed or original proof or to the reader, or announces a sketch")
        else:
            ref = n.get("ref") if isinstance(n.get("ref"), dict) else {}
            if not _text(n.get("statement")):
                err("S6", f"added external {i} needs a non-empty statement")
            if not all(_text(ref.get(k)) for k in ("citation", "locator", "quote")):
                err("S6", f"added external {i} needs ref.citation, ref.locator and ref.quote")
            for field in ("citation", "url", "quote"):
                value = ref.get(field)
                hit = [d for d in deny if isinstance(value, str) and d in value.lower()]
                if hit:
                    err("S6", f"added external {i}: ref.{field} names {hit[0]!r}, which is on the import_denylist")

    # S7
    new_ids = kept | set(added)
    new_edges = [(e["from"], e["to"]) for e in dag["edges"] if e["from"] in kept and e["to"] in kept]
    new_edges += [(e["from"], e["to"]) for e in good_edges]
    new_edges += [(b, key[1]) for key, d in met.items() for b in d["by"]]
    if not _acyclic(new_ids, new_edges):
        err("S7", "the resulting graph has a cycle")
    for t in new_targets:
        if t not in new_ids:
            err("S7", f"target {t} is not in the resulting graph")

    return {"nodes": nodes, "removed": removed, "added": added, "kept": kept, "edges": good_edges,
            "met": met, "obligations": obligations, "targets": new_targets}, errors


def apply(dag, sub):
    plan, _ = _plan(dag, sub)
    if plan is None:
        raise ValueError("the substitution is not well formed")
    new = {k: v for k, v in dag.items() if k not in ("nodes", "edges", "targets")}
    new["targets"] = plan["targets"]
    new["nodes"] = [n for n in dag["nodes"] if n["id"] in plan["kept"]] + list(plan["added"].values())
    new["edges"] = [e for e in dag["edges"] if e["from"] in plan["kept"] and e["to"] in plan["kept"]]
    new["edges"] += plan["edges"]
    for (a, b), d in plan["met"].items():
        base = plan["obligations"][(a, b)]
        for by in d["by"]:
            new["edges"].append({"from": by, "to": b, "kind": "uses", "demand": base.get("demand", ""),
                                 "clause": "discharges " + a + " -> " + b, "where": base.get("where", "")})
    return new


def _obligations(dag, plan):
    nodes, added = plan["nodes"], plan["added"]

    def view(i):
        n = added.get(i) or nodes.get(i) or {}
        return {"id": i, "label": n.get("label", ""), "kind": n.get("kind", ""), "statement": n.get("statement", "")}

    out = []
    for (a, b), d in plan["met"].items():
        base = plan["obligations"][(a, b)]
        out.append({"id": f"O-discharge:{a}>{b}", "type": "discharge",
                    "question": "Given only the statements of the `by` nodes, does the demand follow as stated, "
                                "with the same constants, bounds and hypotheses?",
                    "given": {"demand": base.get("demand", ""), "clause": base.get("clause", ""),
                              "consumer": view(b), "by": [view(x) for x in d["by"]]},
                    "argument": d.get("argument", "")})
    for i, n in added.items():
        if n.get("kind") in RESULTS:
            incoming = [e for e in plan["edges"] if e["to"] == i]
            out.append({"id": f"O-proof:{i}", "type": "proof",
                        "question": "Is the proof complete and correct, using only the node's own incoming demands, "
                                    "the blobs it is linked to, and standard mathematics?",
                        "given": {"statement": n.get("statement", ""), "proof": n.get("proof", ""),
                                  "incoming": [{"from": view(e["from"]), "kind": e.get("kind"),
                                                "demand": e.get("demand", "")} for e in incoming]},
                        "argument": ""})
        else:
            out.append({"id": f"O-cite:{i}", "type": "cite",
                        "question": "Does the cited source state this, at this locator, as quoted, and is the node's "
                                    "statement a faithful reading of the quote?",
                        "given": {"statement": n.get("statement", ""), "ref": n.get("ref", {})},
                        "argument": ""})
    return out


def verify(dag, sub):
    base = score(dag)
    result = {"structural_ok": False, "errors": [], "warnings": [], "base_steps": base["steps"], "steps": None,
              "saved": None, "by_node": {}, "obligations": []}
    if not isinstance(sub, dict):
        result["errors"] = [{"check": "format", "message": "the substitution is not a JSON object"}]
        return result
    plan, errors = _plan(dag, sub)
    result["errors"] = errors
    if plan is None or errors:
        return result
    new = apply(dag, sub)
    scored = score(new)  # S8
    result.update(structural_ok=True, steps=scored["steps"], saved=base["steps"] - scored["steps"],
                  by_node=scored["by_node"], obligations=_obligations(dag, plan))
    return result


def main(argv):
    try:
        command = argv[1]
        dag = load(argv[2])
        if command == "lint":
            out = lint(dag)
            print(json.dumps(out, indent=1, ensure_ascii=False))
            return 1 if out["errors"] else 0
        if command == "score":
            print(json.dumps(score(dag), ensure_ascii=False))
            return 0
        if command == "hash":
            print(canonical_hash(dag))
            return 0
        if command == "verify":
            sub = load(argv[3])
            result = verify(dag, sub)
            if "--out" in argv:
                with open(argv[argv.index("--out") + 1], "w", encoding="utf-8") as handle:
                    json.dump(result, handle, indent=1, ensure_ascii=False)
            else:
                print(json.dumps(result, indent=1, ensure_ascii=False))
            if "--write-dag" in argv and result["structural_ok"]:
                with open(argv[argv.index("--write-dag") + 1], "w", encoding="utf-8") as handle:
                    json.dump(apply(dag, sub), handle, indent=1, ensure_ascii=False)
            return 0 if result["structural_ok"] else 1
    except (OSError, ValueError, IndexError, KeyError, TypeError) as exc:
        print("unreadable input: " + str(exc), file=sys.stderr)
        return 2
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
