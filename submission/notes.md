# Stack of four accepted, independent cuts: 471 steps

Effort: high. The protected checker measures **471 steps** against the paper's 528. This entry introduces no new mathematics: it combines, line by line, four changes that the hosted review has each accepted in a separate entry on this track, all relative to the same 477-step ancestor `e68454e8-d2c0-4117-a5a5-e2cea9310047`. Because the four changes touch disjoint lines, the combination is a mechanical three-way merge; the merge was made with a line-level script that stops if a changed line is not found verbatim, and the result was diffed against each component.

| component (accepted entry) | score there | what it contributes here | steps |
|---|---|---|---|
| `dad113ab-354f-4a8e-9840-223fe341c7d5` | 474 | `lem:ledger` replaced by the four-step `new:ledger`; the two notation lines of `new:view-coefficients` (coordinates $x=y-B(\tau)$, $\widehat a$, $\beta_{a,j,\mathrm{leg},\mathsf s}$) stated in the node's statement | -3 |
| `cea90cbe-2a59-4b68-958c-eb7961d0be7e` | 476 | `new:tensor-witness`: "common fixed field of $\sigma^a$ and $\sigma^b$ is $\mathbb F_q$ since $\gcd(a,b)=1$" in place of two lines | -1 |
| `7347dc8a-35fa-4a89-be5a-06e0fe730913` (this solver) | 475 | `new:view-coefficients`: clause (b) without its unused locus half and without the one step proving it | -1 |
| same | | `new:tensor-witness`: the restated Frobenius identity $L(h_s,-,-)=\sigma^s(L)(h_0,-,-)$ deleted; the case $\ell_0=0$ compares entries of $Z_s$ in the two original identities | -1 |
| total from 477 | | | **471** |

Per-node step counts of the added nodes in this entry: `new:rounded-prefix` 26, `new:view-coefficients` 48, `new:initial-zero-stacks` 1, `new:kernel-packing` 4, `new:tensor-witness` 47, `new:circuit-time` 35, `new:fiber-count` 7, `new:rounded-range` 7, `new:ledger` 4. Packed size 15,934 of 16,384 bytes. The gate lists 24 obligations (15 discharges, 9 proofs), the same set as in `dad113ab`.

## Why the pieces do not interact

- The ledger replacement touches only `lem:ledger`, `new:ledger` and the discharge of `lem:ledger > thm:extraction`.
- In `new:view-coefficients`, the notation move concerns lines 12 and 13 of the proof and the last paragraph of the statement; the locus cut concerns clause (b) of the statement and three lines near the end of the proof ("This difference vanishes if ...", deleted; "that change is zero for every $r'$"; "By the zero-stack result"). The locus lines do not use $x$, $\widehat a$ or $\beta$, and the notation lines do not use clause (b).
- In `new:tensor-witness`, the Frobenius cut concerns the lines of the case $\ell_0=0$ (the restated identity and the two lines that compare entries); the fixed-field merge concerns the two lines after "Thus $x_\delta=c_\delta/z_\delta$ is fixed by $\sigma^a$ and $\sigma^b$". The later line "Comparing pair-tensor coefficients in the Frobenius identities" is common to all versions and refers to $Z_a=\sigma^a(Z_c)$ and $Z_b=\sigma^b(Z_b)$, which are kept verbatim.
- No edge and no discharge other than the ledger one differs from the 477-step ancestor.

## The two cuts contributed by this solver, in full

**Locus half of clause (b).** The ancestor's clause (b) said that an identity at $r$ persists at every $r'$ on the fiber $W_c^{\mathsf s}r'=u_c^{\mathsf s}$, and then that zero stacks imply a formal identity and $\chi=0$. Only the second sentence is consumed: edge `lem:view > lem:charged` needs the fiber direction of clause (a) and "that stack is nonzero" (kept half of (b) with (d)); the discharge of `lem:init > thm:extraction` uses "zero stacks, so nonidentical at every $r$ by (b)"; the other two consumers use usability, the paired-leaf support, the cell and row identification and equality of stacks. Inside the proof the zero-stack line follows from the change formula $\sum\ldots W_c(r'-r)$ alone, and clause (e) cites only the zero-stack result.

**Restated Frobenius identity.** With $Z_s=L(h_s,-,-)$ for every $s$ and $L$ supported on the permutations of one basis triple with value $t$, the entry of $Z_s$ at the pair complementary to $k$ is $t(h_s)_k$. Frobenius acts on coefficients in a base-field basis, so $Z_a=\sigma^a(Z_c)$ reads $t(h_a)_k=\sigma^a(t)(h_0)_k$ because $a+c=n$, and $Z_b=\sigma^b(Z_b)$ reads $t(h_b)_k=\sigma^b(t)(h_0)_k$ because $2b=n$. This gives $t h_s=\sigma^s(t)h_0$ for $s=a,b$ without first rewriting the identities as $L(h_s,-,-)=\sigma^s(L)(h_0,-,-)$.

## Results on this track at the time of submission

| entry | steps | verdict |
|---|---|---|
| `e68454e8` (ancestor) | 477 | valid |
| `cea90cbe` | 476 | valid |
| `7347dc8a` | 475 | valid |
| `dad113ab` | 474 | valid |
| this entry | 471 | submitted |
| Minkowski's first theorem taken from the cited second theorem (`b24949c7`) | 477 | rejected: the cited node's statement does not state the successive-minima inequality; not used here |

Not included, on purpose: cuts that are still under review in other entries (removing `lem:names` by a discharge, a replacement of `lem:sparse`, a new interpolation argument in `new:tensor-witness`, a shorter lazy-sampling passage in `new:circuit-time`), and three cuts this solver examined and judged too risky (dropping the product-structure line before Schwartz-Zippel in `new:view-coefficients`; replacing the last two lines of `new:tensor-witness` by a line leaning on the tests blob; deleting the three lines of `new:circuit-time` that argue the law of the lazily sampled label injection, on the ground that the node states only a running time).

