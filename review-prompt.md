# Reviewing a substitution: instructions for the reviewer

You are given the result of `paperdag.py verify`: a substitution that passed the structural checks S1 to S8, and a list
of obligations. Code has already checked the structure. You check the mathematics. You are a model, a person, or a
proof assistant operator; the standard is the same.

## The standard

- Judge **one obligation at a time**, using only what is listed under `given` for that obligation, the blobs of the
  DAG, and standard mathematics (what a first-year graduate textbook proves). Nothing else is available: not the
  removed nodes, not the paper's original proofs, not the submitter's notes.
- **Reject on any gap.** A step you cannot confirm is a gap. "Clearly", "similarly", "as in the paper", "by a
  standard argument" in place of a step is a gap.
- **Constants are part of the contract.** A demand with a bound, a probability, a running time, a range of parameters
  or a set of hypotheses is met only by the same or a stronger one. A weaker constant, a looser bound, an extra
  hypothesis, a narrower parameter range or a different probability space is a rejection, even when the sentence
  reads alike.
- **One inference per step.** The score counts proof steps (sentences and lines). Reject an added proof in which a
  step packs several inferences into one sentence, or uses an abbreviation, symbol or notation that is not defined in
  the node itself or in a blob linked to it.
- Do not repair the submission, and do not accept it for being close.
- You do not choose or recount the score. The verifier computed it.

## The three kinds of obligation

**O-discharge** (one per obligation edge of the cut). `given`: the demand on the edge, the consumer, the statements
of the `by` nodes, the submitter's `argument`. Question: do the statements of the `by` nodes, as written, imply the
demand, as written? Accept only if every hypothesis the demand grants is enough to apply the `by` statements, and
every conclusion the demand asks for is delivered with the same constants.

**O-proof** (one per added result). `given`: the statement, the proof, the demands on the node's incoming edges, the
statements of the blobs it is linked to. Question: is the proof complete and correct, using only those incoming
demands, those blobs and standard mathematics? Reject if it uses a removed node, a kept node it has no edge from, a
step from inside another proof, a symbol it does not define and no linked blob defines, or if any step does not
follow. A proof that restates the claim is not a proof.

**Blobs are background, not results.** From a linked blob a proof may take definitions, notation, models,
constructions, assumptions, parameter conditions, standard mathematics and facts the blob attributes to an earlier
paper. It may not take a claim that `blob-audit.md` lists as U (unverified) unless it proves it in its own steps or
takes it by a `uses` edge from a result or external. A discharge never names a blob.

**O-cite** (one per added external). `given`: the statement, the citation, the locator, the quote. Question: does
the cited source state this, at this locator, as quoted, and is the node's statement a faithful reading of the quote
(not stronger, not under weaker hypotheses)? If you cannot open the source, say so and reject unless you recognise the
result as stated there with certainty; a person must open the source before a record that rests on it is promoted.
A citation of the paper itself or of its own companion artifacts is rejected.

## Output

One block per obligation, in the order given, then one line for the whole submission:

```
id: O-discharge:lem:inverse>lem:heavy
verdict: ACCEPT | REJECT
reason: for REJECT, the first sentence or step that fails and why; for ACCEPT, one sentence on why the demand follows.
```

```
overall: VALID | INVALID      (VALID only if every obligation is ACCEPT)
reviewed_by: model <name> | person <name> | proof assistant <name and version>
```

Say who reviewed. "Accepted by a model" is a weaker claim than "checked by a person" or "checked by a kernel", and a
report must not blur them.
