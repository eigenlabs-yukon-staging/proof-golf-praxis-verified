# Blob audit

Every assertion of every blob (250) is D (definition, model, construction, assumption), S (standard mathematics), R (credited to an earlier paper) or U (this paper's own claim, stated without proof). D, S and R are usable background. **U claims are unverified and not usable**: a proof that needs one proves it in its own steps or takes it by a `uses` edge from a result or external; a U claim never meets a demand, and a discharge never names a blob. Below: every R and U assertion, quoted from the blob's statement by its opening words (… marks a cut). Totals: D 139, S 33, R 2, U 76.

blob:ggm:
- U: "a string fixed before the injections are sampled is a label with probability $q/…"
blob:rom:
- U: "The reductions and the extractor of the extraction theorem (Theorem 5.9) see non…"
- U: "So they are non-observing, and for $H_{\mathsf{key}}$ also non-programming."
blob:msis:
- R: "Module-SIS (MSIS) is the module version of Ajtai's short integer solution proble…"
blob:we:
- U: "So if $\mathcal{A}$ guesses $b$ with probability $\frac12 + \varepsilon$, then $…"
blob:bqs:
- U: "BQS express every NP relation: a witness-checking circuit gives one constraint p…"
- U: "The systems of one shape and their witnesses form the NP relation of the scheme."
- U: "the systems of Boolean circuits above have linear size, with $F_{\max} = 1$ and…"
blob:tests:
- U: "$w w^\top$ passes exactly when the assignment $w$ is a witness"
- U: "a false system can have cheats too"
blob:sampler-search:
- U: "As $r_0$ subtracts half the sum of the others, each other $r_i$ enters $r(w) - c…"
- U: "Through $r_\star$, $r_0$ is uniform on $g$ consecutive integers given the others…"
- U: "We search outward from the center: one fixed table of the names of the baby step…"
blob:stacks-gp:
- U: "The entries $r_1, \dots, r_N$ are independent and uniform on $\{2, \dots, g+1\}$…"
blob:qap:
- U: "So for a polynomial of degree below $\nu\,n_{\mathsf{c}}$, the sums over the cos…"
- U: "By the QAP criterion (Lemma 4.7) there are unique polynomials $h_{\mathrm{key}}$…"
- U: "The theorems of the construction hold for every admissible choice of evaluation…"
blob:forms-weights:
- U: "A vector $v$ with $v_0 = 0$ is in the kernel of every form exactly when the colu…"
- U: "The third product, $z \cdot \sigma^{n/2+1}(z)$, is the conjugate under $\sigma^{…"
- U: "$V$ is fixed by $\sigma^{n/2}$, which maps $T$ to $-T$, so it has only even powe…"
blob:copies-ties:
- U: "The ties ask that $W_U\, \sigma^{n/2}(z) = W_V\, \sigma^{n/2-1}(z)$, $W_U\, \sig…"
- U: "As $\sigma^j$ maps $a(T)$ to $a(\omega^j T)$ and $\omega^{n/2} = -1$, $P(T)$ div…"
- U: "The stack $\mathbf{H}(v) := (\xi_c(v)\, v v^\top)_{c \in C}$ of every vector $v$…"
- U: "For the stack of $v$, $W_U$, $W_V$, and $\sigma^{n/2+1}(W_U) = W_U(-\omega T)$ a…"
- U: "every copy is exactly one cell, and the key copy is $(0, (\mathrm{E}, 0))$"
blob:enc:
- U: "What the factors encode. $F^{k_1}_i H^{\mathrm{leg}}_j = \gamma_c ( y_i\, r_j +…"
- U: "$k + j\Delta$ takes each value below $J\Delta$ once, so the combinations encode…"
- U: "likewise for the allowed remainders, as $\nu$ divides $\Delta'$"
blob:cancellation-mask:
- U: "$x^{\pm}_a \in \mathbb{F}_q^{<2n-1}[T]$ for the cross terms and $x^0_a \in \math…"
- U: "the part without $\varepsilon$ of $\pi_{k_1} \vartheta_{\mathrm{leg}}$ is $\pi (…"
- U: "Summed with the $W_c$ of a stack $\mathbf{W}$, the part without $\varepsilon$ gi…"
- U: "summed with the $\xi_c(w)\, w^\top$ for a witness $w$, all parts give the second…"
- U: "$\sum_{c = (k_1, \mathrm{leg}) \in C} \pi_{k_1} W_c\, \vartheta_{\mathrm{leg}} =…"
- U: "$\sum_{c = (k_1, \mathrm{leg}) \in C} \pi_{k_1} \xi_c(w)\, w^\top \vartheta_{\ma…"
blob:bound-e:
- U: "$L_1$, $L_2$, and $L_T = 2$ are in $\mathbb{G}_1$, $\mathbb{G}_2$, and $\mathbb{…"
- U: "$\varepsilon_f := (3D + 2n + 2K_1 + 67)/(q - D)$ bounds the probability of a coi…"
- U: "which is positive under admissibility condition (P2), $3(L + 3 \cdot 2^{\lambda+…"
- U: "It pays for what the generic model leaves to chance in $Q$ calls: guessed labels…"
blob:admissibility:
- U: "which bounds the degrees of the published exponents in the coins of $\mathsf{Enc…"
- U: "so that a run touches a small part of each group"
- U: "which include $g^{-4} < \theta$ and $2\beta < q$"
- U: "Under them, a nonzero vector in the row space of a heavy stack on which all form…"
- U: "so that the lifting step finds a short multiple if one exists, in polynomial tim…"
- U: "the quadratic polynomial $E$ of Definition B.1"
- U: "so that the proof's generic term $E(2Q+2)$ is at most $(Q+1)/2^\lambda$ (Lemma B…"
- U: "this requires $\theta < 2^{-(2\lambda+1)}$"
blob:expressions:
- U: "The matrix $M$ is fixed: the bounds on expressions, runs, and marks hold for eac…"
- U: "The fourth term of $E(2)$ is $24\,\varepsilon_f$ and no term is negative; so $24…"
- U: "which has at least $q - D$ elements, as $K_1 < n \le D$"
- U: "so $r$ enters only through the term $s_{\mathrm{leg}}\, r_j$ of the $\mathsf{H}^…"
- U: "Each exponent is homogeneous in each of $\pi$, $\zeta$, $\zeta'$, $\zeta''$ and,…"
blob:monitor:
- U: "we may assume it on every sequence of answers, as stopping $\mathcal{A}$ before…"
- U: "a run in $\mathsf{Tgt}$ has one (M4)"
- U: "this stack is then usable (by the view lemma, Lemma B.4(a)), of rank at most thr…"
- U: "so a first mark is $\mathsf{init}$, $\mathsf{guess}$, charged, or good"
blob:symbolic-game:
- U: "In $\mathsf{R}_m$ the value of $H_{\mathsf{key}}$ at the target label is uniform…"
- U: "So $\mathsf{R}_m$ has the law of $\mathsf{R}_\$$ with $H_{\mathsf{key}}$ answeri…"
- U: "This part, with the label injections and the coins of $\mathsf{Enc}$, determines…"
- U: "which exists by (P2)"
- U: "So the game uses no coin of $\mathsf{Enc}$, which allows a union bound"
blob:records:
- U: "Until the monitor sets a mark, a label with a record has an entry $\mathsf{X}$,…"
- U: "By induction: $\mathsf{X} \mapsto \mathsf{X}^\circ$ commutes with linear combina…"
- U: "So at a first mark $\mathsf{diff}(\mathsf{D})$, set by a result $\mathsf{F}$ at…"
- U: "Formally equal expressions of $\mathbb{G}_T$ have equal stacks, by the view lemm…"
blob:reductions:
- U: "recovers the row space of its mark stack from three random combinations of the r…"
- U: "sampling them lazily instead gives the same law and an algorithm without oracle…"
- U: "with the exponents taken there, its entry $j$ is $\alpha_{\mathsf{s}} \sum_{\mat…"
- U: "Here $\mathsf{LIFT}$ is the algorithm of the lifting step (Lemma B.9), which ret…"
blob:extractor:
- U: "the $9n$ numbers"
- U: "A pairing has $W^{\mathsf{s}}_c = a_{k_1} b_{\mathrm{leg},\mathsf{s}}^\top$ and…"
- U: "at most four, as the pivot entries determine a vector of $\mathcal{V}'$, and non…"
blob:lattices:
- U: "$r_I$ is uniform on it, as $r_1, \dots, r_N$ are independent and uniform on $[2,…"
- U: "$\operatorname{gp}(v^\top)$ is the guessing probability of the matrix $v^\top$,…"
- U: "Conditioning on $r_{i+1}$ shows that $\operatorname{gp}(v_{[i]}^\top)$ does not…"
- U: "so $\theta < \operatorname{gp}(v^\top) = \operatorname{gp}(v_{[N_0]}^\top) \le \…"
- R: "its largest fiber density $m(\Theta)$ is the largest density of one, at most $g^…"
- U: "As $(BU)^\top = U^\top B^\top$, none of these depends on $B$."
blob:trimming:
- U: "Neither depends on $B$: replacing $B$ by $BU$ replaces $B^\top r_I - y_\Theta$ b…"
