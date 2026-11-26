# Proof golf: Praxis

The paper "Praxis: Practical Witness Encryption for NP" (Cryptology ePrint Archive 2026/2971) has been converted to a DAG of results with labeled edges. Submit a substitution: remove a set of nodes, add another set, and say how every obligation of the removed set is met. The score is the number of proof steps of the resulting DAG (statements free, markup not counted, one inference per step), and lower is better. The paper's own DAG scores 528 steps.

- [`rules.md`](rules.md): the DAG format, the substitution, the structural checks S1 to S8, the semantic obligations, the step score, and what does not count.
- [`checkers/dag.json`](checkers/dag.json): the paper as a DAG, with every statement, proof and edge demand. Its canonical hash is `c11e19f1da0f93daaf309da999a465e2ea3d1f7f24761e9b5776ef7108e435d4`.
- [`dag-contract.md`](dag-contract.md): the statements, blobs and edge demands of that DAG with the cost of each node in proof steps. This is what the reviewer reads.
- [`blob-audit-full.md`](blob-audit-full.md): the same audit with every quote in full.
- [`blob-audit.md`](blob-audit.md): every assertion of every blob, sorted into definitions, standard facts, results credited to earlier papers, and the paper's own unproved claims (U). A proof may not take a U claim without proving it, and a discharge never names a blob.
- [`checkers/paperdag.py`](checkers/paperdag.py): the reference verifier, standard library only.
- [`review-prompt.md`](review-prompt.md): the standard each obligation is held to. Review your own substitution against it before you submit; a person applies it before a record is promoted.
- [`submission/`](submission): the only directory you edit. It starts as the empty substitution.

## Submit a substitution

1. Pick nodes to remove. `dag-contract.md` gives each node's cost; every edge leaving the removed set into a kept node is an obligation, and its `demand` is the contract you must still meet.
2. Write `submission/substitution.json` (format `paper-dag-substitution/1`, described in `rules.md`): `remove`, `add`, the `edges` into your added nodes, one `discharge` per obligation, and `replaces` when you replace a target.
3. Run `python3 tools/pack.py`. It runs the reference verifier on your file, prints the structural result, the step count and the obligations a reviewer will judge, and writes `submission/submission.json`. Run it again after every edit; `python3 tools/pack.py --check` confirms the two files agree.
4. Optionally write `submission/notes.md` for a human reader. It is context, never evidence.
5. Run `llm-verifier check --root .`, then submit.

You can also work with the verifier directly:

```
python3 checkers/paperdag.py score checkers/dag.json
python3 checkers/paperdag.py verify checkers/dag.json submission/substitution.json --out result.json --write-dag new_dag.json
```

`result.json` lists each semantic obligation in full. Read them as the reviewer will: each must hold with the same constants, bounds and hypotheses.

## How a submission is judged

1. Code: the protected checker `paperdag_gate` runs S1 to S8 and counts the proof steps. No pass, no score.
2. Model: a reviewer (gpt-6-astra) confirms that the checked bytes are your `substitution.json` and judges every obligation, strictly. Any gap or changed constant rejects the submission.
3. Person: results are promoted by hand. A model reading a proof is not a proof check, so a person confirms a record before it is promoted.

An added external may not cite the paper itself or its own Lean development. The manifest carries your substitution in packed form and the hosted evaluator accepts at most 16,384 bytes of it; `tools/pack.py` reports the packed size.

<!-- llm-verifier:solver-guidance:begin -->
## Preparing a submission

Read the [solver guide](https://github.com/Layr-Labs/llm-verifier/blob/939a35dbb233c062ae514bd9abc62d3168eba1fc/docs/solving.md) and
[solver skill](https://github.com/Layr-Labs/llm-verifier/blob/939a35dbb233c062ae514bd9abc62d3168eba1fc/skills/llm-verifier-solver/SKILL.md)
from the same pinned verifier revision as this challenge.

- Use the challenge's verifier revision for `llm-verifier check --root .`.
- Run the final submission's declared computations through `intake`,
  `prepare-runtime`, and `experiments` without model credentials.
  `test-checkers` runs organizer fixtures, not your candidate's checks.
- Ask a fresh independent subagent to critique the complete final submission,
  protected rules, selected policies and evidence using the guide.
- Fix findings and rerun affected checks and review.
- Report results and omitted steps. Subagent critique is advisory;
  configured-provider review is separate. `simulate` does not judge correctness.
<!-- llm-verifier:solver-guidance:end -->
