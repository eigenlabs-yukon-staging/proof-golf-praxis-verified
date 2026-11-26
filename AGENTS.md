# Working on this challenge

Edit only `submission/`. Read `rules.md` first, then `dag-contract.md` and `blob-audit.md` (blobs are background: never discharge with a blob, never use a claim it lists as U without proving it). Write `submission/substitution.json`, then run `python3 tools/pack.py`: it checks the substitution with the protected verifier and writes `submission/submission.json`. Never write the manifest by hand, add no other file except an optional `submission/notes.md`, and declare no experiment.

The score is the number of proof steps of the resulting DAG (see rules.md, Score), lower is better, and it is computed by code. Write one inference per sentence or line; packing steps together is rejected. A reviewer model then judges every semantic obligation strictly: keep every constant, bound and hypothesis of each demand, put each proof in full in its `proof` field, and do not cite the paper itself or its own Lean development.

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
