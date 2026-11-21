# Paley theta project: status after round 193 (summary for an outside reader)

*Draft prepared by a Claude agent on 2026-11-21 from the repository at commit `02ef535`. It summarises; it does not add mathematics. Every result below is accepted only by AI agents (a research agent, then one or more independent agent audits or reviews). **No human has checked any of it.** The project owner has said they cannot check the mathematics.*

Links point to `https://github.com/lyw-ops/Paleygraph1/blob/02ef535/<path>`. Below, "R*n*" means research round *n*.

**Evidence labels used in this summary**

- **Proved (agent-accepted):** a proof is written out. Agents checked it, and sometimes exact small-$p$ scripts check its identities. No human has read it.
- **Conditional:** proved from a stated hypothesis that is not proved.
- **Finite evidence:** computations at small or moderate $p$. They are not proofs.
- **Agent expectation:** an opinion recorded by an agent.

---

## 1. The question

Let $p\equiv1\pmod 4$ be prime, $Q\subset\mathbb F_p^\times$ the nonzero squares, $n=(p-1)/2$, and $H$ the Paley graph induced on $Q$ (the neighbourhood of $0$). The target is
$$\vartheta(\overline H)/\sqrt n\to1\qquad(p\to\infty),$$
where $\vartheta$ is the ordinary Lovász theta function. Equivalently $\vartheta(\overline{G_{p,1}})\sim\sqrt{p/2}$.

- **Sources.** This is Conjecture 26 of the Randomstrasse101 post (<https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/>), linked from [`README.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/README.md). It is also Entry 12 of arXiv:2603.29571 (§12, Bandeira), which the acceptance records cite as `source_statement_url` <https://arxiv.org/html/2603.29571v1#S12>, and open problem OP-00041.
- **Link to cliques.** The R191 audit notes that the conjecture would recover the Hanson–Petridis clique bound up to $1+o(1)$, through $\omega(G_p)\le\vartheta(\overline{G_{p,1}})+1$.
- **Status: open.** Nothing in the repository proves or refutes it.

## 2. Where the project stands

**Strategy in plain words.** I am reading the R151–R160 notes and the R191 assembly report §1. These are terse, so my paraphrase may be imperfect.

1. **The contradiction set-up.** The "ordinary line" argues by contradiction. Assume a fixed hypothetical "ordinary gap" (as I read it, a failure of the limit along a sequence of primes). A signed projected "repair" iteration (R150–R151) produces a nonnegative deficit vector $b$ on $\mathbb Z/n\cong\widehat Q$. Its normalisation $\nu=b/\sum b$ is a probability on the characters of $Q$.
2. **The objects.** Write $f=\sum_\eta\nu_\eta\,\eta$ (a function on $Q$) and $g=|f|^2$.
3. **The hypothetical critical branch (NC).** On the branch where the effective support of $b$ has the critical size $m_0=n/\sqrt p$, the vector $\nu$ is nearly uniform on a set $S$ with $|S|\sim m_0$. Precisely, (NC) is $\|L_\sigma b\|/r\to0$ and $m_{\rm eff}/m_0\to1$ (R183 line 53).
4. **What must be bounded.** On (NC), a deficit-weighted five-factor correlation sum $\mathcal M_\nu(F)$ is forced to be $\gg pD$ with $D\to\infty$ (R152, R157). So an $O(p)$ upper bound on it would exclude the branch.
5. **The two halves.** Rounds 152–191 cut this upper bound into pieces. R191 showed it splits into a *slope* part (A-slope) and a *vertex* part (A-vertex), for one fixed vertex level $a\le\tfrac12$ (R191 acceptance; [`research/native-claude-ordinary-fixed-block-assembly-191.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-fixed-block-assembly-191.md) §§3–6).

**Bottom line (as recorded in [`coordination/checkpoints/round-193.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/coordination/checkpoints/round-193.md)).** The internal programme has reduced the ordinary line to:

- two **external** problems about geometric progressions in $\mathbb F_p$, either of which would give (A-slope) through the arguments recorded in R189–R191;
- one **internal** estimate, (A-vertex), which the project records as being of "target depth".

The second, "cold" line has been paused since R189. Decision after R193: hold.

**Important caveat: this is only the critical branch.** All the obligations above concern the hypothetical *critical* branch (NC). Closing them would **not** prove the target. The R152 acceptance record says "even a critical exclusion would leave diffuse branches". The R157 acceptance record says an $O(p)$ upper bound "would exclude only the critical branch. The original all-primes ordinary theta limit remains open." The coordinator searched the R150–R193 acceptance records and found no later statement that the diffuse (non-critical) branches are closed. *(This paragraph was checked and rewritten by the coordinator after drafting.)*

## 3. Results proved (agent-accepted, agent-reviewed, not human-checked)

There are three load-bearing results from R187–R190. Each has:

- the original agent report;
- an agent audit in its round;
- a second independent agent review in R193 ([`research/native-claude-review-lemma-mprime-theorem-a-193.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-review-lemma-mprime-theorem-a-193.md));
- the R193 audit of that review ([`research/native-claude-audit-193.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-audit-193.md) §2).

The R193 reviewer says it re-derived each step before reading the earlier audits. The R193 auditor marks that claim "NOT CHECKED (unverifiable)".

### 3.1 Lemma M′ and Proposition P′ (R187): pair energy without Balog–Szemerédi–Gowers

Source: [`research/native-claude-ordinary-prime-level-pair-energy-187.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-prime-level-pair-energy-187.md) §§1–5.

**Notation.**

- *Pair energy.* For $A,B\subseteq\mathbb F_p\setminus\{0,1\}$ put $m_{A,B}(u)=\#\{(x,y)\in A\times B:1-y=u(1-x)\}$ and $E(A;B)=\sum_{u\in\mathbb F_p^\times}m_{A,B}(u)^2$.
- *Multiplicative energy.* $E^\times(R)=\#\{y_1y_2=y_3y_4,\ y_i\in R\}$.

**Lemma C** (chunked Stevens–de Zeeuw). For $p$ larger than an absolute constant, let $X,Z\subseteq\mathbb F_p$ and let $\mathcal L$ be $n$ distinct lines, none vertical or horizontal. With $s=\min(|X|,|Z|)$ and $b=\max(|X|,|Z|)$,
$$I(X\times Z,\mathcal L)\le C_2\big(s^{3/4}b^{1/2}n^{3/4}+s\,b^{1/2}n\,p^{-1/2}+n\big).$$
There is no condition linking $s$, $n$ and $p$. The only external input is Stevens–de Zeeuw Theorem 4 (arXiv:1609.06284v4).

**Lemma M′.** Let $A,R\subseteq\mathbb F_p\setminus\{0,1\}$ with $|A|=\alpha\ge1$ and $|R|=m\ge1$. Write $E^\times(R)=m^3/K$ (so $1\le K\le m$) and $L_0=\lfloor\log_2m\rfloor+1$. Then:

- there is a set $B=B(R)\subseteq R$, depending only on $R$, with $|B|\ge m/(4L_0\sqrt K)$;
- for every such $A$ ("form I"),
$$E(A;B)\le C_3\Big(L_0^{4/3}\alpha^{5/3}|B|^{2/3}K^{2/3}m^{1/3}+L_0K\alpha|B|+L_0\,\alpha^2|B|(Km)^{1/2}p^{-1/2}\Big),$$
with $C_3$ absolute.

A sharper form with $\mu_*=\min(\alpha,4L_0^2Km)$ is in the file.

- **How it works.** $B$ is the set of $y\in R$ lying in many quotients $y/y'$ from one popular dyadic class $F$. The incidence argument runs on $A\times F$.
- **Why it matters (the report's claim).** The effective doubling cost is $K$, not $K^4$ as through Reiher–Schoen BSG.

**Proposition P′ and its consequences.** These are stated under the project's standing hypotheses (H1)/(H2). (H1) is: $g=|f|^2$, $0\le g\le1$, $g(1)=1$, $\operatorname{supp}g\subseteq Q$. (H2) is the cap: $G=\sum g\le n\max\nu\le C_{\rm cap}\sqrt p$. The only structural input on $g$ is "Lemma S1": $E^\times(W)\ge t^2|W|^4/(n\max\nu)$ for every $W\subseteq\{g\ge t\}$. S1 is inherited from R163/R173; the R193 review did not re-derive it.

- **(3.1).** Level sets are extracted greedily by Lemma M′ (report §3). For any two resulting components at heights $a_s,a_g\ge c\,p^{-1/6}$,
$$a_sa_g\,E(X_s;X_g)^{1/2}\le C(\log p)^{4/3}p^{2/3}.$$
- **Theorem 2.** With $h(z)=g(1-z)$ on $\mathbb F_p^\times$, $E^\times(h)=\sum_\kappa\big(\sum_zh(z)h(\kappa z)\big)^2\le C\,p^{4/3}(\log p)^{32/3}$.
- **Corollary 4.** $X\le E^\times(h)\ll p^{4/3}(\log p)^{32/3}$ and $\mathcal M_w\le E^\times(h)/4$. Here $X$ is the masked version
$$X=\sum_{\kappa\in Q\setminus\{1\}}\Big(\sum_z g(1-z)\,g(1-\kappa z)\Big)^2$$
(R188 setup: $X=E_Q(h)$). The first mass $\mathcal M_w$ is defined in R183 Prop. A.

**Why it matters.** This is the best unconditional bound on the (A-slope) quantity $X$: $p^{4/3+o(1)}$, against the needed $O(p)$. R182 Prop. 4 identified $p^{4/3}$ as the cap of this whole method. The light levels $g<p^{-1/6}$ are priced only by Young's inequality, so going below $p^{4/3}$ needs a new idea there.

**Review status: correct as stated.** Lemma C, Lemma M′ and P′ were accepted by the R187 audit, the R193 review and the R193 audit. The R187 audit's only correction is cosmetic (wording "$K^{5/4}$ against $|B|$"). Inputs inherited and not re-derived: Lemma S1, R185 Lemma 5, R182 Prop. 1(iv), and the R178/R180/R184 chain (R193 review §4).

### 3.2 Theorem A (R188): a twisted second-norm bound without affine energy

Source: [`research/native-claude-ordinary-prime-beyond-point-plane-188.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-prime-beyond-point-plane-188.md) §3. The setup section defines everything precisely; this is a compressed version.

**Hypotheses.**

- $\nu\ge0$, so $g=\sum_\alpha\omega(\alpha)\alpha$ on $\mathbb F_p^\times$ with $\omega\ge0$ and $\sum\omega=1$.
- (H3): $g(1/x)=g(x)$.

**Definitions.**

- *Chart.* $\mu(r,b)=g(Y)g(D)$ for $Y\ne D\in\mathbb F_p\setminus\{0,1\}$, with $r=(Y-D)/(1-D)$, $b=D(1-Y)/(Y(1-D))$, and the mask $b\in Q$.
- *Operator.* $F_\mu v(s)=\sum_{r,b}\mu(r,b)\,v((s-b)/r)$, and $\pi(\mu)=F_\mu|_{\mathbf 1^\perp}$.
- *Test vectors.* $h_t(e)=g(t/e)$ for $e\neq0$ and $h_t(0)=0$; $\varphi_t=h_t-G/p$.
- *Correlations.* $\Delta(\lambda,\beta)=\sum_{r,b}\mu(r,b)\mu(\lambda r,b+r\beta)$, $T_0=\sum_\lambda g(\lambda)\Delta(\lambda,0)$, $\mathcal T=\sum_\lambda c_g(\lambda)\Delta(\lambda,0)$ with $c_g(\lambda)=\sum_xg(x)g(\lambda x)$, and $\Gamma_{\rm tot}=\sum_x g(x)^2$.
- *Slope-row moment.* $X=\sum_rm(r)^2$ with $m(r)=\sum_b\mu(r,b)$. This equals the masked shifted energy above (R183 Prop. A).

**Statement.**

- (i) $\|\pi(\mu)\varphi_t\|^2\le p\,T_0\le p\,X$ for every $t\in\mathbb F_p^\times$.
- (ii) $\sum_{t}\|\pi(\mu)\varphi_t\|^2\le p\,\mathcal T-G^2X\le p\,\Gamma_{\rm tot}X$.

Consequently the project's "one-match covariance" (defined in R169/R173) is $O\big(p^{3/2}+\min(W,\Gamma_{\rm tot}/4)\,X\big)$, with $W=\sum_tg(t)(1-g(t))$.

The proof uses only three facts:

1. horizontal and slope row masses coincide: $\Lambda_0=X$ (Lemma A1, uses (H3));
2. the Gauss-sum identity $\|F_\mu\chi\|^2=p\,S_0(\chi)-|\hat m(\chi)|^2$ (Lemma A2);
3. orthogonality of the dilations $t$.

**Why it matters.**

- It made $X$ (and $T_0$) the single quantity controlling the one-match covariance: $X=O(p)$ gives the one-match target $O(p^{3/2})$, with no affine-energy or point–plane input.
- Unconditionally it gives only $p^{11/6+o(1)}$, which is worse than the accepted $43/24$.
- R189–R191 build on $T_0$ and $X$. R190 later moved one-match itself off the critical path; $X=O(p)$ is now the (A-slope) target for a different reason (R191 Prop. 2).

**Review status: correct as stated, for every $t$** (R188 audit, R193 review, R193 audit). The R188 audit's corrections concern scope and notation: (H3) is needed in Cor. A, and $W=\sum_tw(t)$ is not $\max_\xi W_\xi$. R193 adds an exact identity for the slack in (ii), and exact rational checks on 40 laws with $\omega\ge0$ ($p\le73$).

### 3.3 Application of MPRRS Theorem 37 (R190): status of the shifted geometric-progression energy

Source: [`research/native-claude-ordinary-gp-shifted-energy-literature-190.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-gp-shifted-energy-literature-190.md) §1.

**The quoted theorem** (Murphy–Petridis–Roche-Newton–Rudnev–Shkredov, arXiv:1702.01003v5, Mathematika 65 (2019), Theorem 37, p. 45). Let $A\subset F$, where $F$ has characteristic $p$, with $|AA|=M|A|$ and $|A|\le p^{13/23}M^{10/23}$. Then for every $\alpha\in F^*$,
$$E^\times(A+\alpha)\lesssim M^{33/13}|A|^{32/13},$$
where $\lesssim$ hides $(\log|A|)^{18/13}$. The source's remark writes $E^\times(A)$; from context it means $E^\times(A+\alpha)$.

**Application.**

- *The set.* Take $I=\{\gamma^{2k}:|k|\le K\}\subset Q$ (a symmetric geometric progression with distinct elements), $|I|=N=2K+1\asymp\sqrt p$. Put $I'=I\setminus\{1\}$; then $M\le2+1/(2K)$ and $0\notin I'-1$.
- *The size condition* holds because $1/2<13/23$.
- *The bound.* With $\alpha=-1$:
$$E^\times(I'-1)\ll N^{32/13}(\log N)^{18/13}=p^{16/13+o(1)},\qquad X(1_I)\le E^\times(I'-1).$$
- *What it changes.* This replaces the $|I|^{5/2}$ that R186–R189 had used from MPRRS Lemma 33. It weakens the R189 "admissible-only" obstruction from $p^{5/4}$ to $p^{16/13}$ (one-match level $45/26$).
- *What it is not.* It is a weakened obstruction level, **not an upper bound** on $T_0$, $X$ or any covariance for the actual law.

**The one-line repair (R190 audit, R193 review and R193 audit).** The printed proof of Theorem 37 invokes Lemma 33 checking only its first condition $M|A|^2|B|\le p^2$. Lemma 33's second condition, $\max(|AA|,|B|)\le(|A||AA||B|)^{1/2}$, is equivalent to $M\le|B|\le M|A|^2$, and the proof does not address it.

- **Top end.** Without loss of generality $E^\times(A+\alpha)\ge4M^{33/13}|A|^{32/13}$. Then $|B|\le4|A|^4/E^\times\le|A|^{20/13}M^{-33/13}\le M|A|^2$.
- **Bottom end.** For $|B|<M$, the trivial bound $E^\times(A+\alpha,B)\le|A||B|^2\le M^{1/2}|A||B|^{3/2}$ suffices.

**Review status: correct with that repair.** Theorem 37 was read verbatim at source by four separate agent text extractions. Not read by any agent: the proofs of MPRRS Theorem 34 (from Shkredov 2013), Theorem 11 and Lemma 33. These support only the *status line* of `cand:gp-shifted-energy`; no project proof uses them. A minor attribution correction: $X(1_I)\le E^\times(I-1)$ was already in R190; R193 only replaced $I$ by $I'$.

## 4. Conditional results

### 4.1 Theorem E (R192), conditional on (SS*)

Source: [`research/native-claude-ordinary-nc-vertex-tightness-192.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-nc-vertex-tightness-192.md) §3, with the corrected quantifiers from the R192 audit §2.9, restated in [`research/native-claude-ordinary-ss-star-literature-193.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-ss-star-literature-193.md) §1.

**Notation.**

- $S\subseteq\mathbb Z/N$, $g_S(\xi)=|\widehat{1_S}(\xi)|^2/|S|^2$ and $M=N/|S|-1$.
- $S$ is *sharp at level $a$* (along a sequence) if $\sum_{\xi\ne0,\,g_S(\xi)<a}g_S(\xi)=o(M)$.
- On (NC), $T_\rho=\{y\in Q\setminus\{1\}:\chi(1-y)=\rho\}$, where $\rho=-\sigma$ and $\sigma$ is the sign of the hypothetical gap.
- $m_{<a}=\sum_{y\in T_\rho,\ g(y)<a}g(y)$ is the low-level vertex mass.

**(SS\*)**, a field-free statement that is **not proved**. For every $a\in(0,\tfrac12]$ there are $L\in\mathbb N$ and $c\in(0,1]$ with the following property. No sequence $S_k\subseteq\mathbb Z/N_k$ with $|S_k|\sim\sqrt{N_k/2}$, sharp at level $a$, has
$$\liminf_k\ \min_B\ \sum_{\xi\notin B}g_k(\xi)/M_k>0,$$
where $B$ ranges over unions of at most $L$ subgroups of the dual with orders in $[cN_k/|S_k|,\,N_k/(c|S_k|)]$.

(SS\*) is the weakest form R192 uses; R192 also states a stronger form (SS). A variant (SS\*\*) adds further hypotheses the near-critical $S$ satisfies (flatness, energy bounds, (A5), (A6)); see the R193 report §1.

**Theorem E.** Assume (SS\*). On (NC), with the hypotheses of R157 line 3 and R160 line 3, for every fixed $a\in(0,1]$,
$$\liminf\ m_{<a}/\sqrt p>0.$$
Since $m_{<a}\le(1+o(1))\sqrt p$, this means $m_{<a}\asymp\sqrt p$, so vertex tightness (V) fails (§5.2).

**Proof outline.** Low vertex mass $o(\sqrt p)$ would make the near-critical support $S$ (with $N=n$) sharp at level $a/2$. Then (SS\*) would put almost all of its spectral mass on $\le L$ subgroups of $Q$ of order $\asymp\sqrt p$. That contradicts (A4) from R151: on (NC), $t_B=\|1_{Q\setminus B}f\|^2/\|f\|^2\ge c_0(k,c_1,c_2)>0$ for every union $B$ of at most $k$ cosets of subgroups of order in $[c_1\sqrt p,c_2\sqrt p]$. (A4) is proved from Mit'kin's estimate.

**Status.** The R192 audit accepts Theorem E as a correct implication. Its main correction: given (SS\*), (V) is not "false for the actual law" but of target depth. Proving (V) would by itself close the critical branch, so a "yes" for (V) requires the near-critical support to be a counterexample to (SS\*).

### 4.2 What the literature gives for (SS\*) (R193)

Source: [`research/native-claude-ordinary-ss-star-literature-193.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-ss-star-literature-193.md), corrected by the R193 audit §3. The search found no published theorem implying (SS\*) or (SS\*\*); as the report says, a search cannot prove absence.

**The exact case is a theorem.** If $g_S(\xi)\in\{0\}\cup[a,1]$ for every $\xi$, then $\|1_S\|_A\le a^{-1/2}$ (Lemma 2), where $\|f\|_A=\sum_\xi|N^{-1}\sum_xf(x)e(-x\xi/N)|$.

- *Composite $N$.* Green–Sanders Theorem 1.3 (arXiv:math/0611286, read at source) writes $1_S$ as $\sum_{j\le L}\pm1_{x_j+H_j}$, with $L\le e^{e^{Ca^{-2}}}$ and at most $a^{-1/2}+\tfrac1{100}$ distinct $H_j$. This gives an "$\varepsilon$-form" of the (SS) window (Proposition 3), not the fixed-$c$ form.
- *Prime $N$.* No exactly sharp set of size $\sim\sqrt{N/2}$ exists for large $N$. This follows from Green–Sanders alone; Konyagin–Shkredov Theorem 3 gives a rate.

**The robust sparse case is open in the sources read.** The (SS) hypothesis is an $L^2$ statement with relative error $o(1)$ at density $N^{-1/2}$.

- Every approximate-idempotent theorem read (Green–Sanders Lemma 3.1, Sanders, Cheung–Hatami–Zhao–Zilberstein) assumes sup-norm hypotheses.
- The one $L^2$-robust theorem found (Gopalan–O'Donnell–Servedio–Shpilka–Wimmer, $\mathbb F_2^n$) needs error $\lesssim\alpha^3$.
- Chang, Croot–Sisask and Sanders-type almost-periodicity results lose $\log(1/\alpha)\asymp\log N$, which is fatal at $\alpha=N^{-1/2}$.

**Where the gap sits (R193 audit's correction).** Let $h$ be the truncation of $1_S$ to the frequencies $\Lambda=\{g_S\ge a\}$. Then $\|h\|_A\le a^{-1/2}$ and $h\approx1_S$ off $o(|S|)$ points. The missing input is
$$(\mathrm{Clean}_a):\qquad \sup_x d(h(x),\mathbb Z)\le e^{-C_0a^{-2}}\ \text{along the sequence,}$$
that is, sup-norm near-integrality of $h$. It is not "an empty exceptional set for $1_S-h$".

- The auditor sketches, without a stated theorem, how (Clean$_a$) would feed the Green–Sanders iteration.
- A second open point: whether R151's constant $c_0(k,c_1,c_2)$ in (A4) allows the $\varepsilon$-form to suffice for Theorem E. This is the optional call `ordinary-a4-c1-dependence`.
- **Theorem E stays conditional.**

## 5. The open problems blocking the target

These are as recorded in the R191–R193 acceptance records `failed_paths_and_open_bounds` and in the R193 checkpoint. All concern the critical branch (NC).

### 5.1 (A-slope): $X=O(p)$, or $\mathcal M_{\sqrt g}=O(p)$, without logarithms, for the actual near-critical law

Here $\mathcal M_{\sqrt g}=\sum_{t\ne1}\sqrt{g(t)}P_t$, with $P_t$ the completed positive majorant at slope $t$ (R191 §4). R191 Prop. 2 (bookkeeping, exact check) shows that $X=O(p)$ pays every slope $t\ne1$ at a fixed vertex level, at cost $a^{-2}X$. The weaker $\mathcal M_w=O(p)$ does not.

- **Known values.** $X\ll p^{4/3+o(1)}$ (§3.1), at its method cap. On (NC), $X\ge(2-o(1))p$ (R184), so the target sits at the floor.
- **Method obstruction (implication, not a lower bound for the actual law).** Consider any argument that uses only the "admissible" hypotheses (probability, cap, $\omega\ge0$, (H3)), or only the sector-free (NC) consequences. If it bounds $\mathcal M_w$ (hence also $\mathcal M_{\sqrt g}$ or $X$) by $p^{16/13-\delta}$, it must also prove $E^\times(I'-1)\ll|I'|^{32/13-2\delta}$ for symmetric geometric progressions $I$ of length $\asymp\sqrt p$. To reach $O(p)$ it must prove $E^\times(I'-1)=O(|I'|^2)$ without logarithms. Sources: R189 Cor. 3.1, R190 Theorem 4, R191 Cor. 3.1/4.1. The witnesses are interval laws and "diluted-interval" laws $D_\theta$, which satisfy every sector-free (NC) consequence. Exact subgroup laws already give a *logarithmic* obstruction to admissible-only arguments (R190).
- **External form 1, `cand:gp-shifted-energy`.**
  - *Statement:* $E^\times(I-1)\ll|I|^{2}$, logarithm-free, for symmetric geometric progressions $I\subset Q$ (not subgroups) with $|I|\asymp\sqrt p$.
  - *Known:* $|I|^{32/13+o(1)}$ (MPRRS Theorem 37, §3.3).
  - *For subgroups only:* $|\Gamma|^2\log|\Gamma|$ (Macourt–Shkredov–Shparlinski Cor. 4.1, Stepanov method). So the log-free form is not recorded as known even for subgroups.
  - *Finite evidence:* about $2.5$–$2.9\,|I|^2$ for $|I|\le201$ (R189 audit).
  - The R190 search (MPRRS citers screened, related papers read at source) found nothing below $32/13$.
- **External form 2, `cand:gp-sector-constancy`**, needed by arguments that use the sector condition (NC2). Its two forms are defined in [`research/native-claude-ordinary-gp-sector-constancy-literature-191.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-gp-sector-constancy-literature-191.md) §1, with $R(\zeta)=\max\{R:\chi(1-\zeta^k)=\chi(1-\zeta),\ 1\le k\le R\}$:
  - **(GP-Sub$_c$).** For large $p$, every $\zeta\in Q$ with $\operatorname{ord}\zeta>c\sqrt p$ has $R(\zeta)<c\sqrt p$. Known only for $c>1/\sqrt2$ (Hanson–Petridis: a constant run is a Paley clique).
  - **(GP-Sub$_\kappa$)**, re-quantified in R191. For every $c_0>0$ there is $\kappa>0$ such that every symmetric $\{\zeta^k:|k|\le M\}\subset Q$ with $c_0\sqrt p\le M<\operatorname{ord}\zeta/2$ has $\ge p^\kappa$ points $y$ with $\chi(1-y)=\varepsilon$, for each sign $\varepsilon$. Known only for $c_0>1$ (Vinogradov's bilinear bound).
  - *Range needed:* $c\approx\theta/2<1/4$ (to exclude the $D_\theta$ laws).
  - *Implied by* the Paley graph conjecture, by $\omega(G_p)=o(\sqrt p)$, and by Shparlinski's 2016 Problem 1. It is a special case of Chang's Problem 3.
  - *Primality is necessary:* in $\mathbb F_{r^2}$ it fails for every $c<1$.

### 5.2 (A-vertex): a signed estimate on the low vertex layers ("target depth")

**Statement.** Under $X=O(p)$, the contradiction on (NC) holds if and only if, for one fixed $a\in(0,\tfrac12]$,
$$(\mathrm A_V)\qquad\sqrt{\mathcal M_\nu(F)}-\sqrt{\mathcal M_\nu(F_{\ge a})}=o(\sqrt{pD}),$$
where $F(x)=f(1-vx)$ with $\chi(v)=\rho$, $F_{\ge a}$ cuts the vertex values with $g<a$, and $D\to\infty$ slowly with $D\le p^{1/4}/\log(2\sqrt p)$ (R191 §5, R192 §1, R157). This is a bookkeeping composition of accepted statements.

**Its only accepted sufficient form is vertex tightness (V):** $m_{<a}=o(D)$, robustly $O(1)$.

**Known.**

- (V) cannot be reached from the sector-free (NC) consequences (R192 Prop. B, proved).
- Every accepted device loses at least $p^{1/2}$ on the layers $C^2/p<|F|^2<a$.
- Given (SS\*), (V) is false (Theorem E). So (A-vertex) would then need a genuinely signed estimate with no accepted tool.
- Proving (V) would itself close the critical branch, which is why the project labels it "target depth".

### 5.3 $\sum g^2\gg\sqrt p$ (the Round 20 question)

- On (NC) this is equivalent to $\mathcal E(S)\gg|S|^3$ for the additive energy of the flat support $S$ (R183 Prop. 1.4).
- It is open in $[O(1),(\tfrac12+o(1))\sqrt p]$.
- It is necessary for (V), not sufficient.

### 5.4 The cold line

- Per-simple unsigned contraction prices for the Picard representation were retired in R189.
- The minimal-price version is conditional on (NCP); only signed mechanisms remain.
- The line has been paused since R189 with no new input. See the R189 acceptance record.

## 6. Questions for an expert

1. **Shifted geometric-progression energy.** For a symmetric geometric progression $I\subset\mathbb F_p^\times$ that is not a subgroup, with $|I|\asymp\sqrt p$:
   - Is $E^\times(I-1)=O(|I|^2)$ (log-free, or even $|I|^{2+o(1)}$) known?
   - Is it equivalent to, or does it imply, a named open problem?
   - Is any improvement of MPRRS's $32/13$ known?
   - Is the log-free form known even for subgroups?
2. **Constant Legendre runs along progressions.** Is it known whether $\chi(1-\zeta^k)$ can be constant for $1\le k\le c\sqrt p$ with some $c<1/\sqrt2$?
   - Is this known to be as hard as $\omega(G_p)=o(\sqrt p)$?
   - The target itself yields only $\omega(G_p)\le(1+o(1))\sqrt{p/2}$. Is a route whose sector branch needs (GP-Sub) at $c<1/4$ asking for more than the target? This is my observation, not a recorded project claim.
3. **(SS\*) / (Clean$_a$).** For $S\subseteq\mathbb Z/N$ with $|S|\sim\sqrt{N/2}$ whose spectrum is sharp at a fixed level $a$ (all but $o(1)$ of the Fourier mass at $g_S\ge a$):
   - Must the mass concentrate on boundedly many subgroups of order $\asymp N/|S|$?
   - Is a counterexample known?
   - Is the Λ-truncation $h$ necessarily close to integer-valued in sup norm?
4. **Soundness of the reduction.** Is there a known reason why an $O(p)$ upper bound on the deficit-weighted five-factor sum $\mathcal M_\nu(F)$ (R152) cannot hold, or is strictly stronger than the target? The project's records say excluding the critical branch $m_{\rm eff}/m_0\to1$ does **not** by itself give the target, because the "diffuse branches" (R152, R157) remain. Is there a known way to handle the diffuse branches, or a reason to expect them to be easier or harder than the critical one?
5. **Lemma M′ (§3.1).** Is this popular-quotient replacement for BSG known, with doubling cost $K$ and size loss $K^{-1/2}$? A short proof is in the R187 report §2, and it is the step most worth a human check.

## 7. How to check

Set up from the repository root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

All scripts below test identities or exponent arithmetic exactly, or are labelled floating evidence. **None tests an asymptotic exponent.** I re-ran each command marked ✓ on 2026-11-21 and got the stated final line.

| result | read | replay (exact unless noted) |
|---|---|---|
| Lemma C, M′, P′, Thms 1–2 (R187) | [`research/native-claude-ordinary-prime-level-pair-energy-187.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-prime-level-pair-energy-187.md) §§1–5; [`research/native-claude-audit-187.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-audit-187.md) | `.venv/bin/python -B research/paley-187-pair-lemma-check.py` → `EXACT CHECKS OK` ✓; `.venv/bin/python -B research/paley-187-pair-exponents.py` → `ALL OK` ✓ (`--lp` adds a float LP); `.venv/bin/python -B research/paley-187-audit-pair-check.py` → `ALL AUDIT CHECKS OK` |
| Theorem A (R188) | [`research/native-claude-ordinary-prime-beyond-point-plane-188.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-prime-beyond-point-plane-188.md) §3; [`research/native-claude-audit-188.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-audit-188.md) | `.venv/bin/python -B research/paley-188-bpp-exponents.py` → `ALL OK` ✓; `.venv/bin/python -B research/paley-188-bpp-models.py --check` (exact plus floating identities); `.venv/bin/python -B research/paley-188-audit-bpp-check.py` |
| MPRRS Thm 37 application (R190) | [`research/native-claude-ordinary-gp-shifted-energy-literature-190.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-gp-shifted-energy-literature-190.md) §1; [`research/native-claude-audit-190.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-audit-190.md); MPRRS arXiv:1702.01003v5 pp. 41–46 | `.venv/bin/python -B research/paley-190-gplit-exponents.py` → `ALL OK` ✓; `.venv/bin/python -B research/paley-190-audit-check.py` |
| R193 second review of all three | [`research/native-claude-review-lemma-mprime-theorem-a-193.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-review-lemma-mprime-theorem-a-193.md); [`research/native-claude-audit-193.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-audit-193.md) §2 | `python3 -B research/paley-193-review-checks.py` → `ALL EXACT CHECKS OK` ✓ (standard library, < 1 s) |
| Theorem E, (SS\*) (R192) | [`research/native-claude-ordinary-nc-vertex-tightness-192.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-nc-vertex-tightness-192.md) §§1–3, §7; [`research/native-claude-audit-192.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-audit-192.md) §2.9 | `.venv/bin/python -B research/paley-192-vertex-exponents.py` → `ALL OK` ✓; `.venv/bin/python -B research/paley-192-audit-check.py` |
| (SS\*) literature (R193) | [`research/native-claude-ordinary-ss-star-literature-193.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-ss-star-literature-193.md); [`research/native-claude-audit-193.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-audit-193.md) §3 | `python3 -B research/paley-193-ssstar-checks.py` → `ALL OK` ✓ (floating, evidence); `python3 -B research/paley-193-audit-ssstar.py` (floating, evidence) |
| Obligation map (A-slope)/(A-vertex) | [`research/native-claude-ordinary-fixed-block-assembly-191.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/native-claude-ordinary-fixed-block-assembly-191.md) §§1–7; [`research/round-191-acceptance.json`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/round-191-acceptance.json) | `python3 research/paley-191-assembly-exponents.py` → `ALL OK` (per report; not re-run here) |

Background for the notation:

- [`research/ordinary-prime-coset-spread-151.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/ordinary-prime-coset-spread-151.md) for (A4);
- [`research/ordinary-affine-correlations-152.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/ordinary-affine-correlations-152.md) for $\mathcal M_\nu(F)$;
- [`research/ordinary-marked-frequency-localization-157.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/ordinary-marked-frequency-localization-157.md) for the lower bound $\gg pD$;
- R183 `native-claude-ordinary-prime-first-mass-fibre-dilation-183.md` for $\mathcal M_w$.

Current state is in [`research/round-193-acceptance.json`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/round-193-acceptance.json) and [`coordination/round-193.json`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/coordination/round-193.json).

## 8. Inconsistencies and unclear points noticed

1. **Critical branch versus target.** The R152 acceptance (`failed_paths_and_open_bounds`) says "even a critical exclusion would leave diffuse branches". The R183–R193 records describe what would "close the critical branch", and the checkpoints call (A-vertex) "of target depth". The coordinator then checked: R157's acceptance says an $O(p)$ upper bound "would exclude only the critical branch. The original all-primes ordinary theta limit remains open", and no R150–R193 acceptance record closes the diffuse branches. So the reduction covers only the critical branch. "Target depth" for (A-vertex) means as hard as closing that branch, not as hard as the whole target.
2. **One ID, two thresholds.** `cand:gp-sector-constancy` is reported as "known only for $c>1/\sqrt2$" (R190/R191 checkpoints) and as "open for $c_0\le1$" (R193 audit and checkpoint). These are the two different forms, (GP-Sub$_c$) and (GP-Sub$_\kappa$), under one ID.
3. **"Needed at $|I|^2$" is a method statement.** $E^\times(I-1)=O(|I|^2)$ is needed only by admissible-only or sector-free arguments. It is not a proven necessary condition for $X=O(p)$ for the actual law. Some summary lines omit that qualifier.
4. **The R192 report text predates its corrections.** The text says "(V) and high energy independent in both directions", which the acceptance rejects ((V) implies high energy). It also uses looser (SS\*) quantifiers, and gives Green–Sanders "from memory" as $\|1_S\|_A\le1/a$ with $\exp\exp(O(a^{-4}))$. R193 has $a^{-1/2}$ and $e^{e^{Ca^{-2}}}$, which agree once $M=a^{-1/2}$.
5. **The R193 report's own gap statement was rejected.** Its location of the (SS\*) gap ("an exceptional set") was rejected as stated by its audit and relocated to (Clean$_a$).
6. **Fixed-$c$ versus $\varepsilon$-form.** The exact-case source result gives only an $\varepsilon$-form of (SS). Whether that is enough for Theorem E depends on the unexamined dependence of R151's $c_0(k,c_1,c_2)$.
7. **Logarithms.** R187 proves $X\ll p^{4/3}(\log p)^{32/3}$ and states (HC′) "up to logarithms", whereas (A-slope) needs a logarithm-free $O(p)$.
8. **Independence is self-reported.** The R193 reviewer's claim to have worked independently cannot be verified. The R193 audit says it gives "no evidence of independence by itself" that the reviewer agreed with all earlier audits.
9. **Navigation.** [`research/ledger.md`](https://github.com/lyw-ops/Paleygraph1/blob/02ef535/research/ledger.md), which `README.md` points to for comparing approaches, has no entries after Round 180.
10. **Typo at source.** The remark after MPRRS Theorem 37 writes $E^\times(A)$ for $E^\times(A+\alpha)$. All agents read it the latter way.
