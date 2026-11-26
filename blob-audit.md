# Blob audit: what a proof may take from each blob

The 26 blobs of the protected DAG were read sentence by sentence (250 assertions). Each assertion is one of:

- **D**: a definition, notation, model, construction, algorithm, assumption or parameter condition. Usable as background.
- **R**: a fact the blob attributes to an earlier paper or a named theorem. Usable as background, as a reference to earlier work.
- **S**: standard mathematics a first-year graduate textbook proves. Usable.
- **U**: a claim of this paper's own that the blob asserts without proof. **Unverified: not usable.** An added proof that needs a U claim must prove it in its own steps, or take it by a `uses` edge from a result or external whose statement gives it. A U claim never meets a demand.

Every U and R assertion is quoted below, exactly as it appears in the blob's statement. Assertions not quoted are D or S.

Totals: D 139, S 33, R 2, U 76.

## blob:ggm

- U: "a string fixed before the injections are sampled is a label with probability $q/2^{\ell_{\mathsf{lab}}}$"

## blob:rom

- U: "The reductions and the extractor of the extraction theorem (Theorem 5.9) see none of the adversary's RO queries, and only the reductions program an oracle: $H_{\mathsf{seed}}$, at one fresh seed, where they place their Module-SIS challenge."
- U: "So they are non-observing, and for $H_{\mathsf{key}}$ also non-programming."

## blob:msis

- R: "Module-SIS (MSIS) is the module version of Ajtai's short integer solution problem." (reference: Ajtai (SIS); module version (Langlois-Stehle) not named. No citation or locator in the blob. Historical attribution, not a mathematical fact used in proofs.)

## blob:we

- U: "So if $\mathcal{A}$ guesses $b$ with probability $\frac12 + \varepsilon$, then $\mathcal{E}$ outputs a witness with probability at least $\varepsilon - \delta(t, Q, Q_H)$."

## blob:bqs

- U: "BQS express every NP relation: a witness-checking circuit gives one constraint per gate, such as $e_i(w)\, e_j(w) = w_0\, e_k(w)$ for an AND gate $w_k = w_i w_j$, plus $e_o(w)\, e_0(w) = w_0\, e_0(w)$, setting the output $w_o$ to $1$; a witness is an accepting input with the values of all gates."
- U: "The systems of one shape and their witnesses form the NP relation of the scheme."
- U: "the systems of Boolean circuits above have linear size, with $F_{\max} = 1$ and $n_{\mathsf{c}} \le N + 1$."

## blob:tests

- U: "$w w^\top$ passes exactly when the assignment $w$ is a witness"
- U: "a false system can have cheats too"

## blob:sampler-search

- U: "As $r_0$ subtracts half the sum of the others, each other $r_i$ enters $r(w) - c_w$ as $\pm \frac{1}{2} ( r_i - \frac{g+3}{2} )$, symmetric about zero, so with the same law for $w_i = 0$ and $1$."
- U: "Through $r_\star$, $r_0$ is uniform on $g$ consecutive integers given the others."
- U: "We search outward from the center: one fixed table of the names of the baby steps $b \cdot \Psi^\alpha$ for $0 \le b < \bar b$, with $\bar b$ of order $\sqrt{g}\, N^{1/4}$, serves $b$ and $-b$ at once, and the giant steps $\Lambda' - j(2\bar b - 1) \cdot \Psi^\alpha$ for $j = 0, \pm 1, \pm 2, \dots$ cover the integers outward from $0$." (restates `ext:bsgs; prop:efficiency (d)`)

## blob:stacks-gp

- U: "The entries $r_1, \dots, r_N$ are independent and uniform on $\{2, \dots, g+1\}$, and $r_0$, given them, is uniform on $g$ consecutive integers."

## blob:qap

- U: "So for a polynomial of degree below $\nu\,n_{\mathsf{c}}$, the sums over the cosets $\mathcal{K}_t = \delta_t \mathcal{G}$ are, up to the nonzero factor $\nu$, the $n_{\mathsf{c}} \times n_{\mathsf{c}}$ Vandermonde matrix of the values $\delta_t^\nu$, distinct as the cosets are, applied to the polynomial's coefficients at the exponents divisible by $\nu$; they all vanish exactly when the polynomial is allowed." (restates `lem:qap (the coset-sum step of its proof)`)
- U: "By the QAP criterion (Lemma 4.7) there are unique polynomials $h_{\mathrm{key}}$ and $h_{\mathrm{oth}}$ and a unique allowed $R_w := R_{w w^\top}$, the quotients of $w$ for the key copy and the other copies of the scheme and the remainder of $w$, with $A_w B_w - L_\rho = h_{\mathrm{key}} \cdot Z \cdot (X - \rho) + Z_0\, R_w$ and $A_w B_w = h_{\mathrm{oth}} \cdot Z + Z_0\, R_w$." (restates `lem:qap`)
- U: "The theorems of the construction hold for every admissible choice of evaluation points." (restates `thm:correct; thm:extraction`)

## blob:forms-weights

- U: "A vector $v$ with $v_0 = 0$ is in the kernel of every form exactly when the columns $1, \dots, \ell$ of $M$, a matrix in $R_q^{k \times \ell}$, map $(\hat v_1, \dots, \hat v_\ell)$ to zero." (restates `lem:heavy (c) (partly)`)
- U: "The third product, $z \cdot \sigma^{n/2+1}(z)$, is the conjugate under $\sigma^{n/2+1}$ of $U$, as $\sigma^n$ is the identity, so it needs no copies of its own"
- U: "$V$ is fixed by $\sigma^{n/2}$, which maps $T$ to $-T$, so it has only even powers of $T$."

## blob:copies-ties

- U: "The ties ask that $W_U\, \sigma^{n/2}(z) = W_V\, \sigma^{n/2-1}(z)$, $W_U\, \sigma^{n/2+1}(z) = \sigma^{n/2+1}(W_U)\, \sigma^{n/2-1}(z)$, and $W_V\, \sigma^{n/2+1}(z) = \sigma^{n/2+1}(W_U)\, \sigma^{n/2}(z)$, identities in $\mathbb{F}_{q^n}^{N+1}$ whose differences, before reduction modulo $P(T)$, are the tie polynomials."
- U: "As $\sigma^j$ maps $a(T)$ to $a(\omega^j T)$ and $\omega^{n/2} = -1$, $P(T)$ divides the tie polynomials exactly if the stack satisfies the ties as stated in this second form."
- U: "The stack $\mathbf{H}(v) := (\xi_c(v)\, v v^\top)_{c \in C}$ of every vector $v$ satisfies the ties"
- U: "For the stack of $v$, $W_U$, $W_V$, and $\sigma^{n/2+1}(W_U) = W_U(-\omega T)$ are $v v^\top$ times the three products at $v$, and both sides of each tie are the same product of three conjugates of $z(v)$ times $v$; for the first, $z(v)\, \sigma^{n/2-1}(z(v))\, \sigma^{n/2}(z(v))\, v$."
- U: "every copy is exactly one cell, and the key copy is $(0, (\mathrm{E}, 0))$"

## blob:enc

- U: "What the factors encode. $F^{k_1}_i H^{\mathrm{leg}}_j = \gamma_c ( y_i\, r_j + y_i\, A_j(\tau) - A_i(\tau)\, y_j + A_i(\tau)\, B_j(\tau) ) + \pi_{k_1}\, y_i\, \vartheta_{\mathrm{leg},j}$" (restates `lem:honest (uses it)`)
- U: "$k + j\Delta$ takes each value below $J\Delta$ once, so the combinations encode $\gamma_c\, Z_c(\tau)\, h(\tau)$ for $h \in \mathbb{F}_q^{<J\Delta}[X]$, as one chunk of $J\Delta$ powers would"
- U: "likewise for the allowed remainders, as $\nu$ divides $\Delta'$"

## blob:cancellation-mask

- U: "$x^{\pm}_a \in \mathbb{F}_q^{<2n-1}[T]$ for the cross terms and $x^0_a \in \mathbb{F}_q^{<n-1}[T]$ for the others" (restates `lem:honest (exactness of the divisions)`)
- U: "the part without $\varepsilon$ of $\pi_{k_1} \vartheta_{\mathrm{leg}}$ is $\pi ( \upsilon^{k_c} (\eta_1 z_\circ + \eta_2 z_+) - (-\omega\upsilon)^{k_c} (\eta_2 z_- + \eta_3 z_\circ) )$ for the kinds E and O and $\pi\, \upsilon^{k_c} (\eta_3 z_+ - \eta_1 z_-)$ for V; the terms with $\varepsilon$ or $\varepsilon^{-1}$ are the cross terms."
- U: "Summed with the $W_c$ of a stack $\mathbf{W}$, the part without $\varepsilon$ gives $\pi \sum_a \eta_a\, t_a(\upsilon)$"
- U: "summed with the $\xi_c(w)\, w^\top$ for a witness $w$, all parts give the second identity below"
- U: "$\sum_{c = (k_1, \mathrm{leg}) \in C} \pi_{k_1} W_c\, \vartheta_{\mathrm{leg}} = \pi \sum_{a \in [3]} \eta_a\, t_a(\upsilon) + \varepsilon\, \Theta^{+} + \varepsilon^{-1} \Theta^{-}$"
- U: "$\sum_{c = (k_1, \mathrm{leg}) \in C} \pi_{k_1} \xi_c(w)\, w^\top \vartheta_{\mathrm{leg}} = \pi \sum_{a \in [3]} \eta_a ( P\, x^0_a + \varepsilon\, x^+_a + \varepsilon^{-1} x^-_a )(\upsilon)$"

## blob:dec

No U or R assertion: definitions and standard facts only.

## blob:kernel-short

No U or R assertion: definitions and standard facts only.

## blob:inverse-conditions

No U or R assertion: definitions and standard facts only.

## blob:bound-e

- U: "$L_1$, $L_2$, and $L_T = 2$ are in $\mathbb{G}_1$, $\mathbb{G}_2$, and $\mathbb{G}_T$"
- U: "$\varepsilon_f := (3D + 2n + 2K_1 + 67)/(q - D)$ bounds the probability of a coincidence in $\mathbb{F}_q$" (restates `lem:view (c), (e); lem:degree; ext:sz`)
- U: "which is positive under admissibility condition (P2), $3(L + 3 \cdot 2^{\lambda+1} + 1) \le q$"
- U: "It pays for what the generic model leaves to chance in $Q$ calls: guessed labels, coincidences in $\mathbb{F}_q$, comparisons that succeed with a light stack, and unlucky coins of the extractor and the reductions." (restates `thm:extraction (proof); lem:init, lem:charged, lem:names`)

## blob:admissibility

- U: "which bounds the degrees of the published exponents in the coins of $\mathsf{Enc}$" (restates `lem:degree`)
- U: "so that a run touches a small part of each group"
- U: "which include $g^{-4} < \theta$ and $2\beta < q$"
- U: "Under them, a nonzero vector in the row space of a heavy stack on which all forms vanish has a short multiple, which solves MSIS." (restates `lem:heavy (b), (c); lem:inverse`)
- U: "so that the lifting step finds a short multiple if one exists, in polynomial time (Lemma B.9)" (restates `lem:lift`)
- U: "the quadratic polynomial $E$ of Definition B.1" (restates `lem:ledger`)
- U: "so that the proof's generic term $E(2Q+2)$ is at most $(Q+1)/2^\lambda$ (Lemma B.2)" (restates `lem:ledger`)
- U: "this requires $\theta < 2^{-(2\lambda+1)}$" (restates `lem:ledger`)

## blob:expressions

- U: "The matrix $M$ is fixed: the bounds on expressions, runs, and marks hold for each $M$, and the reductions, like the proof of the extraction bound, take $M$ uniform." (restates `lem:view, lem:init, lem:charged, lem:names (forward claim about them)`)
- U: "The fourth term of $E(2)$ is $24\,\varepsilon_f$ and no term is negative; so $24\,\varepsilon_f \le E(2) \le 2^{-\lambda}$ by (P5), and $\varepsilon_f < 1$."
- U: "which has at least $q - D$ elements, as $K_1 < n \le D$"
- U: "so $r$ enters only through the term $s_{\mathrm{leg}}\, r_j$ of the $\mathsf{H}^{\mathrm{leg}}_{j,1}$ and their $\alpha$-copies"
- U: "Each exponent is homogeneous in each of $\pi$, $\zeta$, $\zeta'$, $\zeta''$ and, jointly, in $(\Omega_{12}, \Omega_{22})$" (restates `lem:degree / lem:view (used there)`)

## blob:monitor

- U: "we may assume it on every sequence of answers, as stopping $\mathcal{A}$ before a call or query beyond these changes no such run"
- U: "a run in $\mathsf{Tgt}$ has one (M4)"
- U: "this stack is then usable (by the view lemma, Lemma B.4(a)), of rank at most three (by the heavy stacks lemma, Lemma B.8(a))" (restates `lem:view (a); lem:heavy (a)`)
- U: "so a first mark is $\mathsf{init}$, $\mathsf{guess}$, charged, or good"

## blob:symbolic-game

- U: "In $\mathsf{R}_m$ the value of $H_{\mathsf{key}}$ at the target label is uniform and enters only the masked message and answers to queries there."
- U: "So $\mathsf{R}_m$ has the law of $\mathsf{R}_\$$ with $H_{\mathsf{key}}$ answering $h \oplus m$ at the target label, and on the same coins they agree up to and including the first query of $\mathcal{A}$ there, without its answer." (restates `ext:br (partly)`)
- U: "This part, with the label injections and the coins of $\mathsf{Enc}$, determines $\mathsf{Tgt}$ and the first mark; so their probabilities may be computed in $\mathsf{R}_\$$, where $h$ and $H_{\mathsf{key}}$ are independent of the label injections and the coins of $\mathsf{Enc}$." (restates `ext:br (partly)`)
- U: "which exists by (P2)"
- U: "So the game uses no coin of $\mathsf{Enc}$, which allows a union bound"

## blob:records

- U: "Until the monitor sets a mark, a label with a record has an entry $\mathsf{X}$, and the record is that of an expression formally equal to $\mathsf{X}^\circ$; an entry whose label has no record is a guess variable that no answered call had as an operand, so it occurs in no result." (restates `lem:reduction (c); lem:extractor (b) (partly)`)
- U: "By induction: $\mathsf{X} \mapsto \mathsf{X}^\circ$ commutes with linear combinations and pairings, and a result that sets no mark meets no entry or one formally equal to it."
- U: "So at a first mark $\mathsf{diff}(\mathsf{D})$, set by a result $\mathsf{F}$ at a label with the entry $\mathsf{X}$, the label has a record, at the latest from this call if it is one of its operands, as $\mathsf{F} - \mathsf{X}$ has no guess variable, and the result's record minus the label's is that of $\mathsf{D}$, up to formal equality." (restates `lem:reduction (c); lem:extractor (b) (partly)`)
- U: "Formally equal expressions of $\mathbb{G}_T$ have equal stacks, by the view lemma (Lemma B.4(a)) for their difference at every $r$, so equal sketches." (restates `lem:view (a)`)

## blob:reductions

- U: "recovers the row space of its mark stack from three random combinations of the rows, gradients in $r$, which cost $O(1)$ operations for each call of $\mathcal{A}$" (restates `lem:reduction (d); ext:bs; prop:reduction-time`)
- U: "sampling them lazily instead gives the same law and an algorithm without oracle access" (restates `lem:reduction (a); ext:shoup (lazy sampling)`)
- U: "with the exponents taken there, its entry $j$ is $\alpha_{\mathsf{s}} \sum_{\mathrm{leg}} s_{\mathrm{leg}} \sum_{a \in \mathcal{X}_1} a\, \mathsf{D}_{a b}$ for $b = (\mathsf{H}^{\mathrm{leg}}_{j,1})^{\mathsf{s}}$"
- U: "Here $\mathsf{LIFT}$ is the algorithm of the lifting step (Lemma B.9), which returns a short multiple of $v$, or $\bot$ if there is none" (restates `lem:lift`)

## blob:extractor

- U: "the $9n$ numbers"
- U: "A pairing has $W^{\mathsf{s}}_c = a_{k_1} b_{\mathrm{leg},\mathsf{s}}^\top$ and the sketches $\sum_c \langle b_{\mathrm{leg},\mathsf{s}}, v^{(l,\mathsf{s})}_c \rangle\, a_{k_1}$."
- U: "at most four, as the pivot entries determine a vector of $\mathcal{V}'$, and none unless $0$ is a pivot" (restates `lem:extractor (c) (partly)`)

## blob:lattices

- R: "its largest fiber density $m(\Theta)$ is the largest density of one, at most $g^{-d}$, as fixing the entries outside a set $J$ with $\det B_J \ne 0$ leaves at most one value of $r_J$, as in Odlyzko's lemma" (reference: Odlyzko's lemma, named only; no citation, no locator (ext:odl cites Nguyen-Wood, Invent. Math. 2022, Lemma 3.1))
- U: "$r_I$ is uniform on it, as $r_1, \dots, r_N$ are independent and uniform on $[2, g+1]$ for both samplers"
- U: "$\operatorname{gp}(v^\top)$ is the guessing probability of the matrix $v^\top$, as $v_0 = 0$"
- U: "Conditioning on $r_{i+1}$ shows that $\operatorname{gp}(v_{[i]}^\top)$ does not increase with $i$"
- U: "so $\theta < \operatorname{gp}(v^\top) = \operatorname{gp}(v_{[N_0]}^\top) \le \operatorname{gp}(v_{[i]}^\top) \le 1/g$ for $i \in [N_0]$" (restates `lem:gp-rank (a) (gp <= g^-rank, partly)`)
- U: "As $(BU)^\top = U^\top B^\top$, none of these depends on $B$."

## blob:trimming

- U: "Neither depends on $B$: replacing $B$ by $BU$ replaces $B^\top r_I - y_\Theta$ by $U^\top (B^\top r_I - y_\Theta)$ and $\Sigma_\Theta$ by $U^\top \Sigma_\Theta U$."
