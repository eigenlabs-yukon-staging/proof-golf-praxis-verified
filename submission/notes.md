# Two redundant steps removed: the unused locus claim and a restated Frobenius identity

Effort: high. The protected checker measures **475 steps** against the paper's 528. The direct parent is the 477-step entry `e68454e8-d2c0-4117-a5a5-e2cea9310047` (valid at the time of writing); every byte outside the lines listed below is the parent's. Two steps are removed, one in each of the two largest added proofs. Nothing is added, no node is removed, no edge or discharge changes, and the packed substitution is smaller than the parent's (15,642 against 15,814 bytes).

| node | parent | this entry | what changed |
|---|---|---|---|
| `new:view-coefficients` | 51 | 50 | clause (b) loses its unused first half; the one step that proved only that half is deleted |
| `new:tensor-witness` | 49 | 48 | the reformulated Frobenius identity is deleted; its one use reads the two original identities directly |
| total | 477 | 475 | |

## Cut 1: the locus half of clause (b) of `new:view-coefficients`

Parent statement, clause (b): "That identity persists at every $r'$ with $W_c^{\mathsf s}r'=u_c^{\mathsf s}$ in all cells and sectors. In particular zero stacks in (a) imply a formal identity and $\chi=0$." This entry keeps only the second sentence: "(b) Zero stacks in (a) imply a formal identity and $\chi=0$."

Proof lines changed (three, all in the last ten lines):

- deleted: "This difference vanishes if the equations $W_c r'=u_c$ hold in both sectors, establishing the locus claim."
- next line, one word: "If both stacks vanish, that **change** is zero for every $r'$, giving a formal identity." (was "that difference"; its referent is the change $\sum\ldots W_c(r'-r)$ computed in the line before, which is unchanged.)
- "By the zero-stack result, this nonformal difference is nonidentical at every fixed $r$." (was "zero-stack locus result".)

Why nothing needs the deleted half:

- Edge `lem:view > lem:charged` demands "(a): every r that makes it succeed lies in one fiber W_c r = u_c" and "(b), (d): that stack is nonzero". The fiber direction is clause (a). Nonzero follows from the kept half of (b) with (d): a zero stack would give a formal identity with $\chi=0$, and the kept proof of that lemma argues exactly so.
- Edge `lem:init > thm:extraction` is discharged with "a formally distinct target pair has zero stacks, so it is nonidentical at every $r$ by (b)": the contrapositive of the kept half.
- Edges `lem:view > lem:extractor` and `lem:view > lem:reduction` use usability, the paired-leaf support, the cell and row identification and equality of stacks, none of which is (b).
- Inside the proof, the zero-stack line follows from the change formula alone (with $W_c=0$ the change is zero for every $r'$), and clause (e) cites only the zero-stack result.

The converse direction (an identity at $r$ persists along the fiber) is true but is not consumed anywhere in the resulting DAG, so it is a statement clause with a proof step that serves nothing.

## Cut 2: the contraction form of the Frobenius identities in `new:tensor-witness`

The parent proves $Z_a=\sigma^a(Z_c)$ and $Z_b=\sigma^b(Z_b)$ (two lines, kept verbatim) and then restates them as "$L(h_s,-,-)=\sigma^s(L)(h_0,-,-)$ for $s=a,b$". That restatement is used once, in the case $\ell_0=0$, to compare one entry of each side. This entry deletes the restatement and compares entries of $Z_s$ in the two original identities:

- deleted: "For $s=a,b$, the identities $Z_s=\sigma^s(Z_{n-s})$ in contraction notation give $L(h_s,-,-)=\sigma^s(L)(h_0,-,-)$ using $\sigma^s(h_{n-s})=h_0$."
- was: "For a form supported on permutations of that triple with value $t'$ there, contraction at $u$ has complementary off-diagonal entries $t' u_k$ by trilinearity, where $u_k$ are coordinates in this basis." now: "As $L$ is supported on permutations of that triple with value $t$ there, its contraction $Z_s$ at $h_s$ has complementary off-diagonal entries $t(h_s)_k$ by trilinearity, where $(h_s)_k$ are coordinates in this basis."
- was: "With $t$ the value of $L$ on the triple, the Frobenius contraction identities give $t h_s=\sigma^s(t)h_0$ on these entries for $s=a,b$." now: "Comparing these entries in the two Frobenius identities gives $t h_s=\sigma^s(t)h_0$ for $s=a,b$, since $\sigma^a(h_c)=\sigma^b(h_b)=h_0$."

Check of the new comparison. In the chosen base-field basis, $Z_s=L(h_s,-,-)$ (established earlier in the proof for every $s$) has entry $t(h_s)_k$ at the pair complementary to $k$. Frobenius acts on coefficients in a base-field basis (fixed in the statement), so $\sigma^a(Z_c)$ has entry $\sigma^a(t)(\sigma^a h_c)_k=\sigma^a(t)(h_0)_k$ because $a+c=n$; equating with $Z_a$ for all three $k$ gives $t h_a=\sigma^a(t)h_0$. The same with $2b=n$ gives $t h_b=\sigma^b(t)h_0$. The later line "Comparing pair-tensor coefficients in the Frobenius identities" already referred to the two original identities and is unchanged: applying $\sigma^s$ to the expansion of $Z_{n-s}$ and comparing with that of $Z_s$ on the independent pair tensors is what it does.

## Results

| candidate | steps | packed bytes | status |
|---|---|---|---|
| parent `e68454e8` | 477 | 15,814 | valid |
| parent + cut 1 | 476 | 15,706 | checked locally, not submitted separately |
| parent + cut 1 + cut 2 (this entry) | 475 | 15,642 | submitted |

Cuts examined and not used (unsuccessful or too risky): deleting "The valid coin samples form an independent product by their sampling rules" in `new:view-coefficients` (it supports a Schwartz-Zippel hypothesis the reviewer has asked for before); replacing the last two lines of `new:tensor-witness` by one line that leans on a sentence of the tests blob next to a claim the audit lists as unverified; folding the rounding, chord and combination lines of `new:rounded-prefix` (26 steps) from three sentences into two, which is a merge of inferences and not a shorter argument; statement slack in `new:rounded-prefix`, `new:rounded-range`, `new:fiber-count` and `new:kernel-packing` (every clause is named by a discharge or used by a kept proof); excluding the case $\ell_0=0$ of `new:tensor-witness` without the Frobenius comparison (for rank three the symmetrised monomial tensor survives every other argument).

## Next steps for other solvers

Both cuts are line-local and independent of the other pending entries on this track (a shorter ledger lemma, Minkowski's first theorem taken from the second, notation moved into the statement of `new:view-coefficients`, the fixed-field merge in `new:tensor-witness`), so they stack with any of those that the review accepts.

