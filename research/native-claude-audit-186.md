# Independent audit of Round 186 (session/r186-audit)

- **Auditor:** Claude subagent started by the Round 186 coordinator (session/r186-audit). This is an agent audit, not human acceptance and not a mathematical certification. The auditor wrote neither report and is not the coordinator.
- **Status of this file:** written incrementally. The "Blind overlap review" section below was saved before any file under `coordination/shared-obligations/`, `coordination/drafts/` or any `coordination/round-*-inflight.json` was opened.
- **Read before the blind review:** `AGENTS.md`, `docs/WORKFLOW.md`, `docs/ROUND_REVIEW.md`, `coordination/checkpoints/round-185.md`, `research/native-claude-audit-185.md`, the two missions in `coordination/missions/round-186/`, and the two reports.

Verdict key (per claim the report labels as proved):
- **ACCEPTED:** correct as written, for the stated hypotheses.
- **ACCEPTED WITH CORRECTION:** true after the stated correction, which does not change the report's main conclusion.
- **CONDITIONAL:** correct given a named input that is not proved or not checked.
- **REJECTED:** false as written, or not supported.

Reports, abbreviated:
- **SUPC** = `native-claude-ordinary-prime-sup-c-heavy-price-186.md` (one-match; \(\sup_{\lambda\ne1}C\), Lemma M, Theorems A/B, Proposition X);
- **COLD** = `native-claude-cold-prime-hybrid-price-186.md` (hybrid price for the non-seed multiplier; Theorem N).

## 1. Blind overlap review

Written after reading the two reports and their missions. No shared-obligation, draft or inflight file had been opened.

| Pair | Classification | Reason |
|---|---|---|
| SUPC – COLD | **independent** | SUPC bounds point–line incidence and multiplicative pair energies of the ordinary weight \(g=|f|^2\) on \(\mathbb F_p\) (Stevens–de Zeeuw Thm 4, Reiher–Schoen BSG, Lemma S1, the Round 178/180/184 chain). COLD studies operator prices for the cold frozen-base map at \(V_{602}\) on \(\mathbb Z/n\) (dimension price \(A_{\mathcal X}\), counting and sup norms, Round 182 Prop. 2, Criterion D). No object, lemma, estimate, external theorem or script is common. Neither report cites the other or any input the other proves. |

- **No shared estimate, no shared input beyond the project's general setting** (\(p\equiv1\bmod4\), \(n=(p-1)/2\), \(Q\) the squares). Both mention the Paley operator / quadratic character, but SUPC uses only additive-multiplicative incidence on \(\mathbb F_p\), and COLD only the spectrum of \(K\) (Lemma 1); neither result feeds the other.
- **Not duplicated.** Each call answered its own mission question.
- **Would an overlap review have changed dispatch?** No. The two calls are on different routes (ordinary one-match; cold dimension price) and either outcome of one leaves the other's question unchanged.
- **Within SUPC (not a pair, recorded for the closeout):** SUPC's Proposition X touches the X / first-mass form of `cand:slope-row-mass-x` (the estimate that remained under that ID after Round 185). It is the same shared estimate already named in the coordinator record, not a new overlap. SUPC states it does not touch \(\Gamma_2\), so `cand:near-critical-square-mass` is not touched.

### After unblinding

Opened afterwards: `coordination/round-186-inflight.json`, `coordination/shared-obligations/round-186-before.json` and `coordination/drafts/round-186-dependency-assessment.json`.

- The coordinator's pre-dispatch comparison (`comparison_status: assessed`, `known_shared: []`, empty `candidate_ids_by_call`) dispatched the two calls as independent. It asked the ordinary call to state any input that also bounds \(X\) or \(\Gamma_2=n\mathcal E(\nu)-1\).
- **Agreement.** My blind classification (independent) matches. SUPC honoured the request: Proposition X is stated separately as an \(X\) bound, and SUPC says it does not touch \(\Gamma_2\).
- **Dispatch effect:** none. No overlap was missed. (The inflight lane labels are `session/r186-supc-heavy` and `session/r186-cold-hybrid`; SUPC's header says `session/r186-sup-c-heavy-price`. This is a label slip in the report header only.)

## Summary of verdicts

| Report | Main verdict | Corrections / conditions |
|---|---|---|
| SUPC. sup C heavy price | (a1) **Lemma M ACCEPTED**; (a2) Prop. P **ACCEPTED**; (a3) **Theorem B ACCEPTED**; (a4) Theorem A **ACCEPTED**; (a5) Corollary C **ACCEPTED**; (a6) Prop. X **ACCEPTED** (one table row implicit); (a7) method statements **ACCEPTED WITH CORRECTION**; (b1) (HC) criterion **ACCEPTED WITH CORRECTION** (height range); (b2) **ACCEPTED** as a formula. Verdict "supported" is honest. | **The headline survives.** \(\sup_{\lambda\ne1}C(\lambda)\ll p^{11/8-5/296}(\log p)^8\), uniformly in \(\lambda\in\mathbb F_p\setminus\{0,1\}\); hence \(\sum_\xi W_\xi^{3/2},\ \mathcal E(\mu)\ll p^{43/16-5/592}(\log p)^4\) and one-match covariance \(O(p^{2125/1184}(\log p)^2)\), \(2125/1184=115/64-5/2368\). Same hypotheses as the accepted Round 180/185 bound; no (NC) input. New external input: none beyond Stevens–de Zeeuw Thm 4 (re-read at source) and Reiher–Schoen BSG (accepted since Round 183). Corrections: (i) (HC) must be assumed down to height \(cp^{-1/6}\), not only on \([p^{-1/15},1]\) (explicit configuration in §2.4); (ii) the BSG ceiling is \(\approx0.02386\) at the Reiher–Schoen exponent \(2.649\), not \(15/632\) (which is the value at \(c=8/3\)); (iii) wording items listed in §2. Side result: \(X\le E^\times(h)\ll p^{31/21}(\log p)^8\). |
| COLD. Hybrid price | Lemma 1, Lemmas 2–3, Prop. 1 (table), **Theorem N ACCEPTED**; Cor. N1 and N2 **ACCEPTED WITH CORRECTION** (normalisation of the symmetric norm; (I1) range for small-\(n\) thresholds); Remark N3 **ACCEPTED**; Prop. 3 **CONDITIONAL** (inherited D1–D4 and the non-mark bad coordinates in the counting part); Props. 4–5, Cor. 6 **ACCEPTED** (method statements; Cor. 6 inherits Round 180); §5 remark arithmetic **ACCEPTED**. Verdict **refuted as posed: ACCEPTED.** | Proved: no seminorm with sup domination at good coordinates and \(P(S)\le s_p\) admits a bound \(P(B_gf)\le F(\|g\|_\infty)P(f)\) (or \(F(\|g\|_{2,n})\)) uniformly in \(n\); the loss is \(\ge c_N(\gamma,n)\sim(8\gamma m''(\gamma)/s^3)\sqrt n\), and \(\sqrt n\) is the exact order. The decision "the cold dimension-price programme reduces to Criterion D or sup transfer" is a **justified coordinator reading, not a theorem**: it excludes size-only (rearrangement-invariant) prices of \(h\); structured information about \(h\) other than its size remains logically open (the per-simple route is retired on model evidence only, and COLD itself names an unproposed "signed price" option). |

## 2. Report SUPC: `native-claude-ordinary-prime-sup-c-heavy-price-186.md`

**Sources checked by line.**
- `native-claude-ordinary-prime-shifted-level-energy-182.md` lines 20–200: (H1)–(H4), Lemma S1 and its proof, the verbatim Stevens–de Zeeuw quote, Lemma SE with its proof (in particular where \(N\le\sqrt p\) is used), the Round 182 extraction (Proposition 3) and Proposition 4.
- `native-claude-ordinary-prime-near-critical-band-autocorrelation-185.md` lines 36–170: R180-rel/lines/det, the definition of \(C^\sharp_\lambda[f_1,\dots,f_4]\), Lemma 4, Lemma 5 and its proof (line 121 is exactly the Cauchy–Schwarz form (CS) SUPC uses), Steps L/B/H.
- `native-claude-ordinary-prime-near-critical-slope-row-mass-184.md` lines 88–122: Proposition 1 (i)–(v).
- `native-claude-audit-185.md` §2 (accepted items a1–a6).

**External sources, fetched for this audit** by two fetch subagents from the arXiv HTML renderings (the PDFs came back as undecodable binary):
- **Stevens–de Zeeuw**, arXiv:1609.06284v4 (18 Jul 2017), Theorem 4. Hypotheses \(|A|=a\le b=|B|\), \(ab^2\le n^3\), \(\mathcal L\) a set of \(n\) lines, and \(an\ll p^2\) in characteristic \(p\); conclusion \(I(A\times B,\mathcal L)\ll a^{3/4}b^{1/2}n^{3/4}+n\). This agrees word for word with SUPC's quote. The proof removes vertical lines (they contribute \(\le ab\)); horizontal lines are allowed. \(\ll\) is an unspecified absolute constant. The paper has no energy corollary for shifted sets, so Lemma M is new to the project and is not a quoted result.
- **Reiher–Schoen**, arXiv:2308.10245v2 (Combinatorica 44 (2024)), Theorem 1.2: any abelian group, \(E(A)\ge|A|^3/K\), \(\varepsilon\in(0,1/2)\) (open interval), \(A'\subseteq A\) with \(|A'|\ge(1-\varepsilon)K^{-1/2}|A|\) and \(|A'-A'|\le2^{33}\varepsilon^{-9}K^4|A'|\). SUPC's form "\(|B|\ge\frac12K^{-1/2}|R|\), \(|B/B|\le CK^4|B|\)" follows from \(\varepsilon=1/4\) (the report and the Round 183 citation write \(\varepsilon=1/2\), which is outside the stated range; this is a citation slip with no effect). The optimality remark reads, in substance, that the exponent 4 "cannot be replaced by any number smaller than \(\log4/\log(27/16)\approx2.649\)", citing Shao (2014). The paper does not say which subset-size regime the example concerns.
- **Murphy–Petridis–Roche-Newton–Rudnev–Shkredov**, arXiv:1702.01003v5, Lemma 33: \(A,B\subset\mathbb F\), \(|A||AA||B|\le p^2\), \(\max(|AA|,|B|)\le(|A||AA||B|)^{1/2}\), \(\alpha\in\mathbb F^*\); then \(\mathsf E^\times(A+\alpha,B)\ll|AA|^{3/2}|B|^{3/2}/|A|^{1/2}\). This agrees with SUPC's quote. The paper gives no proof (it is "implicit in" a cited reference). The mixed-energy definition is the natural multiplicative analogue of the paper's additive \(E(A,B)\) (an inference; no verbatim definition was located).
- **Not fetched:** Bloom arXiv:2501.09470, Shkredov arXiv:1802.09066, Rudnev–Shkredov arXiv:1812.01671, Macourt–Shkredov–Shparlinski arXiv:1701.06192. SUPC uses none of them in a proof.

### 2.1 Lemma M, re-derived line by line

Setting: \(A,B\subseteq\mathbb F_p\setminus\{0,1\}\), \(V\subseteq\mathbb F_p^\times\), \(|A|=\alpha\), \(|V|=|B|=N\), \(|VB|\le K'N\), \(m_{A,B}(u)=\#\{(x,y)\in A\times B:1-y=u(1-x)\}\), \(E(A;B)=\sum_{u\ne0}m^2\).

1. **Lines.** \(\ell_{u,v}:Z=v(uX+1-u)\) has slope \(vu\ne0\) (so it is neither vertical nor horizontal) and intercept \(v(1-u)\); slope plus intercept is \(v\), so \((u,v)\mapsto\ell_{u,v}\) is injective. The lines form a set, as SdZ requires.
2. **Incidences.** If \(1-y=u(1-x)\) then \(v(ux+1-u)=v(1-u(1-x))=vy\), so \((x,vy)\in A\times VB\) lies on \(\ell_{u,v}\). The map \((u,v,x,y)\mapsto(\ell_{u,v},(x,vy))\) is injective (\(y=vy/v\)). Hence \(I(A\times VB,\{\ell_{u,v}\}_{u\in T_h,v\in V})\ge h|T_h|N\). (Replayed exactly, every \(h\), at \(p=13,17,29\).)
3. **SdZ.** Order the coordinate sizes as \(s\le b'\). If the smaller set is the \(Z\)-coordinate, swap coordinates; the lines stay lines and stay distinct. If \(sb'^2>n^3\), then \(I\le sn\) (each line is a graph over either coordinate) and \(sn\le s^{3/4}b'^{1/2}n^{3/4}\) because \(sn<s^{4/3}b'^{2/3}\le b'^2\). So \(htN\le C_1(s^{3/4}b'^{1/2}(tN)^{3/4}+tN)\) in all cases, and for \(h\ge2C_1\), \(tN\le16C_1^4s^3b'^2/h^4\). Monotonicity in \(|VB|\) and \(s^3b'^2=(\alpha|VB|)^2\min(\alpha,|VB|)\) give \(t(h)\le C_2\alpha^2K'^2N\min(\alpha,K'N)/h^4\).
4. **SdZ hypothesis \(an\ll p^2\).** Here \(a=s\le\min(\alpha,K'N)\) and \(n=tN\le\alpha N^2/h\), since \(\sum_um=\alpha N\) (\(x,y\ne1\); checked exactly). At \(h\ge H\ge(\alpha K'^2\min)^{1/3}\): if \(\alpha\le K'N\), \(an\le\alpha^2N^2/\alpha^{2/3}=\alpha^{4/3}N^2\); otherwise \(an\le\alpha^{2/3}N^{8/3}\le\alpha^{4/3}N^2\) because \(N\le K'N<\alpha\). So \(\alpha^{4/3}N^2\le c_1p^2\) suffices, with \(c_1\) fixed by the SdZ constant. My script checks the case split and the balance on 4000 random rational exponent points.
5. **Energy.** Rows with \(m<H\) give \(\le H\alpha N\); dyadic classes above \(H\) give \(\ll\alpha^2K'^2N\min/H^2\). Both equal \(\alpha^{4/3}NK'^{2/3}\min^{1/3}\) at \(H^3=\alpha K'^2\min\). The bound is never below the trivial \(\alpha N\).

**Verdict (a1): ACCEPTED.** I found no gap. **Does Lemma M need the \(\sqrt p\) cap?** No. In Lemma SE (Round 182, Lemma SE proof) the cap \(N\le\sqrt p\) is used only once, to get \(an\le N^4/h\le p^2/h\). Lemma M replaces that step by its own hypothesis \(\alpha^{4/3}N^2\le c_1p^2\), obtained from the larger threshold \(H\). (Even Lemma SE could have run to \(N\le p^{3/5}\) by the same device.) Lemma M is a new lemma of this round, proved from SdZ Thm 4; it is not a quoted literature result.

### 2.2 Uncapped extraction and the doubling claim

- **Lemma S1 for large sets.** The Round 182 proof (Jensen plus orthogonality) has no size restriction: \(E^\times(W)\ge t^2|W|^4/(n\max\nu)\) for any \(W\subseteq\{g\ge t\}\). My float replay (actual-type \(g=|f|^2\), \(\nu\) uniform on random character sets, \(p=101,197,389\); whole level sets and random halves, sizes above \(\sqrt p\) included) never violates it (minimum ratio 2.41).
- **BSG on the whole remainder.** Reiher–Schoen holds in any abelian group for any finite set. So taking \(R\) itself (not a \(\sqrt p\) block) is legitimate.
- **Phase parameters.** For a remainder of size \(m\in[M,2M)\), \(M=p^{1/2-\mu}\), height \(a=p^{-e}\) and \(R\subseteq S_{a/2}\): \(K=m^3/E^\times(R)\le4C_{\rm cap}\sqrt p/(a^2m)\le Cp^{2e+\mu}\), \(|B|\ge\frac12K^{-1/2}m\ge cp^{1/2-3\mu/2-e}\), \(K'\le CK^4\), and the pieces of one group have total size \(\le2M\) (they are disjoint subsets of the first remainder of the group). \(\mu\ge-e-O(1/\log p)\) because \(|U_k|\le2G/a_k\). All re-derived (script A2).
- **Doubling claim "\(K\le p^e\) at height \(p^{-e}\)".** True for a whole level set of the maximal size \(\asymp\sqrt p/a\) (\(\mu=-e\)): \(K\le C\sqrt p/(a^2\cdot\sqrt p/a)=C/a\). Smaller remainders have larger \(K\le p^{2e+\mu}\); the report tracks this through \(\mu\), so the claim is used correctly.
- **Hypothesis of Lemma M at every scale used.** In Theorem B's case 3 all heights are \(e\le1/12\), so \(|D|,|B|\le Cp^{1/2+1/12}\) and \(\alpha^{4/3}N^2\le Cp^{35/18}=o(p^2)\). In Theorem A and Prop. X the pieces are \(\le\sqrt p\) and the heights are \(\le1/12\) (resp. \(\le1/42\)). For the light layer cake of Prop. X, \(\alpha\le G/s\), \(N\le\sqrt p\), and the hypothesis holds iff \(s\ge C'p^{-1/4}\), as SUPC says. Heights \(e>1/12\) are never priced by Lemma M (case 2 uses SdZ alone).

**Verdict (removal of the cap): legitimate.**

### 2.3 Per-four-tuple pricing, components, and 5/296

- **Components.** Levels \(U_k=\{x\ne1:\max(\tau_0,a_k/2)\le g\le a_k\}\), \(k=O(\log p)\); per level \(O(\log p)\) dyadic phase groups plus one leftover. So there are \(O(\log^2p)\) components per slot and \(O(\log^8p)\) four-tuples. The light part is handled by Step L in the Round 185 way (four terms, each \(\le\tau_0G^3\) by R180-det). **Wording correction:** consecutive \(U_k\) share the boundary value \(g=a_k/2\), so "\(g-g_L=\sum_k\sum_Xg1_X\)" is an inequality \(\le\), not an identity. By monotonicity of \(C^\sharp\) this only weakens the bound; no effect.
- **(SdZ) price per tuple.** Sets inside \(\{g\ge\tau_0\}\), sizes \(\le Cp^{1/2-\mu_i}\), heights \(a_i\): \(\prod a_i\cdot I\ll p^{11/8-\sum(e_i+\theta_i\mu_i)}+G^2\). This is Round 185 Lemma 4 applied to indicator weights with \(a_i^{1-\theta_i}(a_i|X_i|)^{\theta_i}\). The SdZ hypothesis holds as in Round 185 (\(p^{27/14}\)).
- **(Pair) price per tuple.** (CS) is Round 185 Lemma 5's proof (line 121): \(C^\sharp\le\|c_{v_1,v_2}\|_2\|c_{v_3,v_4}\|_2\), with pairs (point 1, line 2) and (point 3, line 4). It is monotone, and the triangle inequality over pieces holds because \(c\) is bilinear. I replayed (CS) **exactly with integer weights** at \(p=13,17,29\) for every \(\lambda\), including the identity \(C^\sharp=\sum_rm_{12}(\lambda r)m_{34}(r)\) against brute force.
- **Prop. P.** My own derivation from Lemma M form I, S1 and RS gives \(E(X_s;D)^{1/2}\ll p^{\frac56A+\frac14+\frac{19}6e_s+\frac{13}{12}\mu_s}\), and pair excess \(c=\frac{13}6e_s+\frac{13}{12}\mu_s-e_g-\frac56\mu_g\) (form I) and \(\frac{10}3e_s+\frac32\mu_s-e_g-\frac23\mu_g\) (form II). Both agree with SUPC. **(a2) ACCEPTED.**
- **The \(u=2e+\mu\) reduction.** \(\frac{13}6e+\frac{13}{12}\mu=\frac{13}{12}u\); \(e_g+\frac56\mu_g=\frac16u_g+\frac23(e_g+\mu_g)\ge\frac16u_g\) since \(\mu_g\ge-e_g\); gain \(=\theta u-(2\theta-1)e\ge(1-\theta)u\) since \(e\le u\) and \(\theta>1/2\). Choosing the structured side with the smaller \(u\) gives \(c_{\rm pair}\le\frac{11}{12}\min u\le\frac{22}{15}{\rm gain}_{\rm pair}\). Every step checks.
- **Case exhaustion.** Each slot is light, leftover, or a phase component; cases 1 (some leftover: gain \(\ge\frac58\delta=\frac5{296}\)), 2 (some \(e_i>1/12\): gain \(>1/48\)) and 3 cover everything.
- **The value 5/296.** \(\Gamma(1+\frac{22}{15})=\frac1{24}\) gives \(\Gamma=\frac{15}{888}=\frac5{296}\). Exact. Both binding families, \((0,0,\frac1{37},\frac1{37})\) and \((\frac1{74})^4\) as whole level sets, give SdZ \(=\) pair price \(=\frac{11}8-\frac5{296}\) exactly, and form II is not cheaper there (script A3). **My independent LP** (own formulas; options form I and II in both directions; \(e\le1/12\), \(\mu\in[-e,\delta]\)) returns \(11/8-0.0168919=11/8-5/296\).

**Verdict (a3) Theorem B: ACCEPTED.** \(\sup_{\lambda\ne1}C(\lambda)\ll p^{11/8-5/296}(\log p)^8\), uniformly in \(\lambda\ne0,1\).

**Adversarial checks with no defect found.**
1. *Hidden near-critical use:* none. The inputs are \(0\le g\le1\), \(\operatorname{supp}g\subseteq Q\), \(g=|f|^2\) of a probability \(\nu\) (for S1), and the cap. \(\Gamma_2\) and Lemma Y are not used.
2. *Uniformity in \(\lambda\):* Lemma M, Prop. P and (CS) do not involve \(\lambda\) (\(r\mapsto\lambda r\) is a bijection). The SdZ price uses Round 180's distinct nonvertical, nonhorizontal lines for \(\lambda\ne0,1\).
3. *Constants depending on \(p\):* none. The constants are the SdZ constant, \(c_1\), the RS constant at \(\varepsilon=1/4\), \(C_{\rm cap}\), and factors \(p^{O(1/\log p)}=O(1)\) from the dyadic slack in \(\mu\). The number of pieces per group is not \(O(1)\), but it enters only through \(\sum_B|B|^{1/2}\le2M(\min|B|)^{-1/2}\), which is already in the exponent.
4. *Excluded point \(x=1\):* all components exclude \(x=1\), as do \(C^\sharp\)'s variables; \(v_i(0)=0\), so \(\kappa=0\) never enters \(E\).

**Theorem A (a4): ACCEPTED.** It uses Round 182's extraction verbatim, **but it still needs Lemma M** (a structured piece against an arbitrary partner), so it is not free of new input. Phase-1 excess \(\frac{19}6e_s-\frac16e_g\le3\min e\) against gain \(\frac58\min e\) gives ratio \(\frac{24}5\); Phase-2 excess \(\le\frac{24}5\) times the Phase-2 slot's gain (partner terms \(\le0\)). \(\Gamma=\frac1{24}/\frac{29}5=\frac5{696}\), \(\delta=1/87\). My LP (Phase-1/Phase-2 kinds in all 16 slot patterns) returns \(11/8-5/696\). Covariance \(625/348\).

### 2.4 Proposition X, cap analysis and (HC)

- **Prop. X (a6): ACCEPTED.** At \(\lambda=1\) the SdZ lines form a pencil, so only pair prices are available, and SUPC uses only those. I re-derived every row of its table at \(\varepsilon=1/42\), \(\delta=1/126\). **The table omits the row "Phase-1 structured vs leftover".** It costs \(\frac23+\frac{19}6\varepsilon-\frac56\delta=\frac{139}{189}<\frac{31}{42}\); the report's script checks it, only the table leaves it out. The binding balance \(\frac34-\frac\varepsilon2=\frac23+3\varepsilon\) is at \(\varepsilon=1/42\). Below the Lemma M range \(s<C'p^{-1/4}\), the bound \(\|c_{X,L_s}\|_2\le|X||L_s|^{1/2}\) integrates to \(p^{5/8}\). So \(X\le E^\times(h)\ll p^{31/21}(\log p)^8\), with \(31/21<34/23\). This is consistent with Round 182 Prop. 4's cap (\(\ge p^{4/3}\)). It does not touch \(\Gamma_2\), and the \(X\) target \(p^{1+1/1280}\) is untouched.
- **BSG sensitivity, (b2): ACCEPTED as a formula.** With doubling \(K^c\) and size loss \(K^{-\sigma}\), the pair excess is \((\frac c3+\frac\sigma2-\frac23)\min u\) and \(\delta_C=\frac1{24}/(1+\frac85(\frac c3+\frac\sigma2-\frac23))\). This reproduces \(5/296\) (\(c=4\)), \(5/232\) (\(c=3\)) and \(15/632\) (\(c=8/3\)).
- **The ceiling "\(\delta_C\le15/632\)" (a7): ACCEPTED WITH CORRECTION.** \(15/632\) is the value at \(c=8/3\). At the Reiher–Schoen lower exponent \(c=\log4/\log(27/16)=2.6494\) (with \(\sigma=1/2\)) the formula gives \(\approx0.023859>15/632\approx0.023734\). The correct statement is "BSG of the Reiher–Schoen shape (size \(\asymp K^{-1/2}|A|\)) cannot push this pricing beyond \(\delta_C\approx0.0239\)". It also assumes that the RS lower-bound example applies in the \(K^{-1/2}\) regime, which the source does not state explicitly.
- **MPRRS Lemma 33: ACCEPTED as quoted and applied.** At height 1, \(A=-B_{\rm piece}\), \(\alpha=1\), \(B=1-D\): \(|AA|=|BB|\), the hypotheses reduce to \(MN^2|D|\le p^2\), \(M\le|D|\) and \(|D|\le MN^2\), and the pair price is \(p^{5/8}\). \(\mathsf E^\times(1-X,1-D)\) is exactly \(E(X;D)\) (\((1-y)(1-x')=(1-y')(1-x)\)). It is used in no proof. At \((e,e,e,e)\), \(e=1/74\), Lemma M is cheaper, so \(\delta_C\) does not move.
- **(HC), (b1): ACCEPTED WITH CORRECTION.** The implication "(HC) on heights \([p^{-1/15},1]\Rightarrow\sup C=O(p^{4/3})\)" is **not established as stated**. The report's reduction considers pairs at a common height only. Counter-configuration, all exact (script A7):
  - slot 1 (point) is a whole level set at height \(p^{-1/14}\), outside (HC)'s range;
  - slot 2 (line) is a height-1 phase component with \(\mu=1/60\);
  - slots 3 and 4 are whole height-1 sets.

  The SdZ gain is \(\frac{11}{280}<\frac1{24}\). Pair (3,4) costs \(p^{2/3}\). For pair (1,2) the best available price (form II, structured slot 2) has excess \(+\frac1{840}\); the others have \(\frac{31}{5040}\), \(\frac4{63}\), \(\frac{151}{1260}\) and \(\frac{13}{420}\), and (HC) does not apply. So this tuple costs \(p^{4/3+1/840}\).

  **Fix:** assume (HC) for all heights \(a,a'\in[cp^{-1/6},1]\). It is automatic when \(\max(e,e')\ge1/6\). Then every pair is \(\le p^{2/3}\) with no extraction, and \(\sup C=O(p^{4/3}(\log p)^4)\). Step L at \(\tau_0=cp^{-1/6}\) needs \(c\) **large** (so that \((C_{\rm cap}\sqrt p/\tau_0)^3\le c_0p^2\) for Lemma 4), not small. This changes the exact form of the conditional criterion that Round 187 should test (§5).
- **"Cap \(p^{4/3}\) not attainable with current inputs" (a7):** a correct method statement within point–line plus BSG pricing; not a lower bound for \(\sup C\).

### 2.5 Corollary C (a5): ACCEPTED

- The input is Round 184 Prop. 1(iii) (lines 94, 114): \(E^\times(m)\le X^2+\sup C\cdot M_1^2\), with \(X^2\le p^{68/23}\) (or \(p^{62/21}\)) below \(p^{27/8-5/296}\). From it, \(\sum W^{3/2}\le M_1E^\times(m)^{1/2}\ll p^{43/16-5/592}(\log p)^4\), and through (i), \(9/8+e/4\), the covariance is \(\ll p^{2125/1184}(\log p)^{5/4}\). The report's \((\log p)^2\) is a valid overestimate.
- Every exponent was checked with exact Fractions: \(2125/1184=115/64-5/2368\), \(\|H_\alpha\|_2=p^{147/128-5/4736+o(1)}\), \(\sum w|H_\alpha|^2=p^{179/64-5/2368+o(1)}\), and Theorem A gives \(625/348\).
- The chain uses the Round 180/184 output \(p^{1/8}\mathcal E^{1/4}M_1\) with \(M_1\le G^2\), with no (NC) value. The fixed-slope first mass \(C(a)\), \(a\ne1\), improves in the same way, directly. The Round 176/180 fixed-\(a\) generic squared mass is still not re-derived.

### 2.6 Evidence (c): honest as evidence

The floating table (§9) reproduces to every printed digit. As SUPC says, at \(p\le64013\) every level \(\ge p^{-1/7}\) is within a constant of 1. So the models test no exponent, and in particular they do not test (HC) at heights \(p^{-e}\), \(e\in(1/15,1/6)\).

**Exactly what is proved (agent audit).** Take the actual weight \(g=|f|^2\) of a probability \(\nu\) on \(\widehat Q\) with the cap \(n\max\nu\le C_{\rm cap}\sqrt p\), the hypotheses of the accepted Round 180/185 bounds, and large primes \(p\equiv1\pmod4\). Then:
- \(\sup_{\lambda\in\mathbb F_p\setminus\{0,1\}}C(\lambda)\ll p^{11/8-5/296}(\log p)^8\);
- \(\sum_\xi W_\xi^{3/2},\ \mathcal E(\mu)\ll p^{43/16-5/592}(\log p)^4\);
- the matching-number-one covariance is \(O(p^{2125/1184}(\log p)^2)\), with \(2125/1184=115/64-5/2368\);
- \(X\le E^\times(h)\ll p^{31/21}(\log p)^8\).

The inputs are Stevens–de Zeeuw Thm 4, Reiher–Schoen Thm 1.2, Lemma S1 and the Round 178/180/184 chain, plus the new Lemma M proved in SUPC and re-derived here.

**What is not proved:**
- \(\sup C=O(p^{4/3})\) (it would need (HC) on the full height range);
- any bound on \(\max W\) beyond \(X\);
- \(X=O(p^{1+1/1280})\);
- the one-match target \(O(p^{3/2})\) (point–plane floor \(p^{7/4}\));
- the original theta-limit target.

## 3. Report COLD: `native-claude-cold-prime-hybrid-price-186.md`

**Sources.** I read the mission, the full report, and the inherited statements as COLD quotes them, cross-checked against the Round 184/185 acceptance records and `native-claude-audit-185.md` §3: the Round 184 Prop. C allowances \(0.3411\) and \(0.7499\), the budget \(\beta'<0.24310\), \(g_S\le2.467879\), and Round 185 Theorem 3. The Round 80/96/173/177/180 notes were **not** re-read line by line; their statements are taken as COLD quotes them, and the Round 184/185 audits used the same quotes.

| Item | Statement | Verdict | Notes |
|---|---|---|---|
| (a1) | **Lemma 1**: \(\sum_j\lambda_j=-1\), unique zero, \(\lambda_{n-j}=\lambda_j\); hence \(\|K\|_{2\to2}=1\), \(\sum S^2=4(n-1)\), \(S_0=-2/\sqrt n\) | **ACCEPTED** | The proof is correct: \(\sum_x\chi(1-x^2)=-\chi(-1)=-1\) (discriminant \(4\ne0\)), and \(\chi(-y^{-1})=1\) for squares \(y\). I checked it exactly, by my own code (Euler's criterion), for all 211 primes \(p\equiv1\pmod4\), \(p<3000\). Float FFT at \(p=10009,100049,400009\) reproduces \(\sum S^2=4(n-1)\) and \(\sqrt nS_0=-2\). |
| (a2) | **Lemma 2** \(\|K\|_{\infty\to\infty}\ge2(n-1)/(s\sqrt n)\); **Lemma 3** \(\|L_S\|_{\infty\to\rm good}\ge c_{LS}(n)\sim0.1183\sqrt n\) | **ACCEPTED** (under (I1)) | \(\sum|\kappa|\ge\sum\kappa^2/\max|\kappa|\) with \(\max|\kappa|\le s/(2\sqrt n)\). In Lemma 3 the bad-row subtraction is not divided by \(\sqrt{4a+s^2}\), so the stated \(c_{LS}\) is smaller than necessary: valid, slightly conservative. Replayed directly with aligned sign vectors at three primes; the observed values exceed both bounds. |
| (a2') | **Prop. 1** (pairing table) | **ACCEPTED** | The A rows are inherited (Round 181 algebra property; Round 184 Prop. A and Cor. A2). The counting and sup rows follow from Lemmas 1–3. The reading "no space dominating sup and receiving sup-priced products on which \(L_S\) is bounded" is made precise by Theorem N. |
| (a3) | **Theorem N**: for any seminorm \(P\) with (S) and (P_S), \(\sup_{\|g\|_\infty\le\gamma}P(B_gS)\ge c_N(\gamma,n)P(S)\) | **ACCEPTED** | Re-derived. (1) At real \(t=a\), \(\Phi_a'(y)=y/\sqrt{4a+y^2}\) has \(\Phi_a''=4a/(4a+y^2)^{3/2}>0\), even and decreasing in \(|y|\); the mean value theorem gives a term-by-term sign. (2) Alignment \(g_x=\gamma\,{\rm sgn}(\kappa(x_0-x)S_x)\) makes every term \(\ge\gamma m''|\kappa||S_x|\). (3) Averaging: \(\sum_{x_0}W=(\sum|\kappa|)(\sum_{x\ne0}|S_x|)\), with \(\sum_{x\ne0}|S_x|\ge(4(n-1)-4/n)/s\) and \(W(x_0)\le\|\kappa\|_2\|S\|_2\le2\sqrt{n-1}\) for each of the \(\le b_0\) bad rows. (4) (S) and (P_S). One point \(t=a\) and one real lift suffice for a negative statement about a uniform bound. My direct evaluation of the aligned multiplier (my own FFT construction of \(\kappa\)) gives \((B_gS)(x_0)/s_p=2.78,\ 8.74,\ 17.43\) at \(\gamma=0.61\) and \(p=10009,100049,400009\), against \(c_N=1.48,\ 4.69,\ 9.37\); the ratio to \(\sqrt n\) is stable (0.110). **Scope:** \(g\) is an arbitrary real multiplier of the given size, not the actual \(h\), and the input is \(f=S\). So the theorem refutes every bound on the operator \(B_g\) in \(P\) that uses only the size of \(g\). It says nothing about the actual \(\|B_h\|_P\); COLD states this (Remark N5). |
| (a3') | **Cor. N1** | **ACCEPTED WITH CORRECTION** | For \(\|\cdot\|_\infty\) and \(\|\cdot\|_{2,n}\) it is exactly right. "Any rearrangement-invariant norm \(N\)" needs a normalisation: the constant-modulus witness must have \(N_n(\gamma1_{x\ne0})\) bounded in \(n\) (true for the normalised \(\ell^q\) and Orlicz averages, false for the unnormalised \(\ell^2\)). Rearrangement-invariant information about the **actual** modulus profile of \(h\) is covered only by the floating "same-modulus" evidence (about \(0.026\sqrt n\)), not by the proof. |
| (a3'') | **Cor. N2** thresholds | **ACCEPTED WITH CORRECTION** | The constants \(m''(\gamma)\), the slopes and the bisections are certified for the stated \(s=2.828428539\). That value of \(s\) is (I1)'s bound **for \(p\ge10^6\)**. At small \(n\) the actual \(s_p\) is larger (2.828568 at \(p=10009\)), so the thresholds "\(n\ge151\)", "\(n\ge1478\)", … are formal. For every \(p\ge10^6\) the conclusion holds with large margin (\(c_N(0.61,n)\ge14.8\)). |
| (a3''') | **Remark N3** | **ACCEPTED** | \(\|B_gf\|_\infty\le\kappa_2\gamma\sqrt n\|f\|_\infty\). Together with Theorem N this gives \(\sqrt n\) as the exact order of the loss. |
| (a4) | **Prop. 3**: Round 182 Prop. 2 applies to \(H_\lambda=A_{\mathcal X}\,\square\,\lambda\|\cdot\|_2\); \(\kappa^*_H=\kappa^*_A\), \(g_H=g_S\) | **CONDITIONAL** | (i)–(iv) are correct: an infimal convolution of sublinear functionals is a finite seminorm, and sup domination holds at good coordinates since \(\lambda\ge1\). The (v) split \(T(a+b)=T(a)+K(b\int_0^1[\Phi'(V+a+\sigma b)-\Phi'(V)]d\sigma)\) is right, and so are \(\lambda\|\Delta\|_2\le\kappa_2xy+\kappa_2y^2/(2\lambda)\) and \(\max(c_A,\kappa_2/2)=c_A\) (numbers replayed). **Condition:** the pointwise bound \(|a_x|\le A_{\mathcal X}(a)\) holds only at good coordinates. The counting part handles the mark (\(\Phi''_{t_0}=O(n^{-1/2})\)) but not the up to two non-mark bad cyclic coordinates, which are left to the inherited D2–D4 conventions. Also conditional on D1–D4, (b4), (b-Jk) and (b-T), as COLD says. This does not affect the refutation, which needs only (S) and (P_S) for \(H_\lambda\), and those are proved. \(g_H=g_S\) is a nicety: \(\sum_m\max(G_m,q_S^m)\) is finite either way. |
| (a5) | **Prop. 4** (√n off-diagonal upper bound); **Prop. 5** (horizon fractions); **Cor. 6** (Criterion D with \(\Lambda_n\asymp\sqrt n\); window \(n<10^{414.197}\)) | **ACCEPTED** as method statements | Prop. 4 and 5 are upper-bound bookkeeping. Read correctly, "gets no help" means "this chain gives no bound better than trivial"; the lower bound is Theorem N. Every Prop. 5 fraction and the Cor. 6 window were recomputed with 50-digit decimals and match. \(0.545^8<2^{-7}\) holds, with margin \(<10^{-4}\) (exact Fractions). Cor. 6's "fails for all large \(n\)" inherits Round 180 (\(\liminf\|R_{602}\|_{2,n}>0\), an ineffective limsup). |
| (a6) | §5 remark arithmetic | **ACCEPTED** | \(1.91541\times0.912537/(2|\sqrt a|)=0.219398\) at \(t=a\) (the report prints \(\ge0.219397\), outward over \(Q\)). The leftover budget is \(0.023703\) and the free ceiling 1.01112. The ceiling \(0.8192\) is a float print, as labelled. The interpretation (the retirement uses a nonzero h-higher cost) is a fair reading and opens nothing. |
| (b) | Remark N4 (test vector \(R_{602}\)); §3 heuristic \(H_\lambda=A_{\mathcal X}\) on model simples | **Honest as conditional / heuristic** | Correctly labelled. |
| (c) | Witness table | **Honest as evidence** | Reproduced to every printed digit (run in 9 s, not 1–2 min). |
| Verdict | "Refuted, for the hybrid as posed" | **ACCEPTED** | The question posed is a hybrid with the per-simple seed price and multiplication by \(h\) priced through a sup or counting norm. Theorem N (proved), Prop. 5 and Cor. 6 settle it negatively: no size-only price of the non-seed multiplier can meet a fixed allowance uniformly in \(n\). |

**Is "the cold dimension-price programme reduces to Criterion D or sup transfer" justified?** Partly, and it should be recorded with its scope.
- **What is proved:** every price that dominates the sup and prices \(h\) only through a normalised rearrangement-invariant size (sup, RMS) fails by \(\gtrsim\sqrt n\).
- **What remains logically open:** pricing \(B_h\) through structured information about \(h\) other than its size.
  - One such route is the A-type price. Round 185 retired it on certified depth-3 bounds plus model evidence, conditional on (H-N5); that retirement is not a certificate, and COLD's §5 remark locates one more lower bound it would need.
  - Another is a "signed price" that sees cancellation between the rows of \(K\) and \(h\). COLD names it but no round has formulated it. The floating evidence (actual \(\|B_hS\|_\infty\approx0.2\) against same-size witnesses of \(\approx0.11\sqrt n\)) says the actual operator is benign, so such a price is not excluded.
- **My reading:** the mission's "refuted" branch applies. Criterion D or sup transfer for the B-generated part is the most concrete remaining route. The statement "reduces to" is an exhaustion over price types proposed so far, not a theorem.

## 4. Replay log

Run from the repository root on 2026-11-21 with `.venv/bin/python -B`. "Matches" means every quoted output line or table row appears in the run output, timing text excepted. All four report-script SHA-256 values equal those quoted in the reports (the cold report quotes none; its hashes are recorded here).

| Script | Command | rc | Time | Result |
|---|---|---|---|---|
| supc exponents | `.venv/bin/python -B research/paley-186-supc-exponents.py --lp` | 0 | <1 s | `ALL OK`; LP rows 1/184, 5/696, 5/296 reproduced |
| supc exact | `… paley-186-supc-mixed-check.py --check 13 17 29 37` | 0 | <1 s | `EXACT CHECKS OK` |
| supc models | `… paley-186-supc-mixed-check.py 1009 4001 16001 64013` | 0 | few s | All five quoted §9 rows match to every digit |
| cold constants | `… paley-186-cold-hybrid-constants.py` | 0 | <1 s | Matches the report's printed output exactly (diff empty) |
| cold witness | `… paley-186-cold-hybrid-witness.py` | 0 | 9 s | Matches the report's printed output exactly (diff empty), float |
| audit supc | `.venv/bin/python -B research/paley-186-audit-supc-check.py` | 0 | 2 s | `ALL AUDIT CHECKS OK` (Part A exact Fractions; Part B float LP; Part C exact integers at \(p=13,17,29\) and float S1 at \(p\le389\)) |
| audit cold | `.venv/bin/python -B research/paley-186-audit-cold-check.py` | 0 | <1 s | `ALL AUDIT CHECKS OK` (Lemma 1 exact for 211 primes; Theorem N / Lemmas 2–3 float at three primes; 50-digit decimals) |

SHA-256:
- `paley-186-supc-exponents.py` `93debdd567a6b99fb5c77dc382f72dc2e895b478bd9e9dfd2acb2b67f7a67b8f`
- `paley-186-supc-mixed-check.py` `068621075f749cbbd36edcf1c463ec60feef8e49a5b2ff838f53942717f79cae`
- `paley-186-cold-hybrid-constants.py` `c46cf29a6676c85dbba8b1ef64dc0919e9500dc34c6210f25457df54f5c4ea4d`
- `paley-186-cold-hybrid-witness.py` `b810fa5115e98ce921b8e5bec9cae51d8641752f65aa6a26afcaefbd20f6aa6e`
- `paley-186-audit-supc-check.py` `3380c48f1954d2ca7bcbab5447f1df30e80c3923841c3bcaa4f3becb8e0b6521`
- `paley-186-audit-cold-check.py` `a23d78b2b66a95497170f5f4e7b2f33ce03595299cb93aaf6210b1974bd385c6`
- reports as audited: SUPC `9220d8860c7039ce143e730e76946a903946a16900f167b29666d4854045f0d3`, COLD `6a597c9a88b7b6e370fffe17a97eda014302c245d0c5a254e067cfff4845f738`

**Not checked:**
- The proofs of Stevens–de Zeeuw Theorem 4 and Reiher–Schoen Theorem 1.2. Only their statements and hypotheses were re-read from source.
- MPRRS Lemma 33 has no proof in its source. It is used in no SUPC proof.
- Bloom, Shkredov, Rudnev–Shkredov and Macourt–Shkredov–Shparlinski were not fetched; SUPC uses none of them in a proof.
- The Reiher–Schoen optimality example (Shao 2014) was not read; its subset-size regime is unverified.
- Asymptotic constants cannot be tested by small-\(p\) replays. The exact replays check the identities and inequalities each step uses, not the \(\ll\) constants.
- My LPs are float cross-checks of hand derivations; the proof is the inequality chain in §2.3.
- COLD's ball arithmetic (python-flint) was replayed, not re-implemented. My cold checks are float at \(t=a\), one real lift.
- The Round 80/96/173/177/180/181/184 inherited cold inputs ((I1), sup domination, D1–D4, (b4), (b-Jk), (b-T), \(q_0<0.518\), the Round 177 geometry, Round 180's \(\liminf\|R_{602}\|_{2,n}>0\)) were not re-derived.
- The downstream Round 176/180 fixed-\(a\) generic squared mass was not re-derived.

## 5. Ranked closeout

### 5.1 What Round 186 changes

| Obligation | Before (Round 185 acceptance) | After Round 186 (as audited) | Effect |
|---|---|---|---|
| **One-match covariance** (target \(O(p^{3/2})\)) | \(O(p^{1193/664})\), \(1193/664=115/64-1/5312\approx1.796687\). \(\sup_{\lambda\ne1}C=O(p^{11/8-1/664})\); \(\sum W^{3/2},\mathcal E(\mu)=O(p^{43/16-1/1328})\). Scheme cap \(\delta_C\le1/24\) (cov. \(43/24\)). | **\(O(p^{2125/1184}(\log p)^2)\)**, \(2125/1184=115/64-5/2368\approx1.794764\). \(\sup_{\lambda\ne1}C\ll p^{11/8-5/296}(\log p)^8\) (\(\delta_C\): \(1/664\to5/296\), ×11.2). \(\sum W^{3/2},\mathcal E(\mu)\ll p^{43/16-5/592}(\log p)^4\). \(\|H_\alpha\|_2=p^{147/128-5/4736+o(1)}\), \(\sum w|H_\alpha|^2=p^{179/64-5/2368+o(1)}\). New input: Lemma M (mixed shifted energy, proved from SdZ Thm 4); per-four-tuple pricing; uncapped BSG extraction. No (NC) input. Binding: point–line pair of whole level sets at \(p^{-1/37}\) (or all four at \(p^{-1/74}\)), BSG doubling loss \(\frac{11}{12}e\) against SdZ gain \(\frac58e\). Scheme floor \(p^{4/3}\) (cov. \(43/24\approx1.791667\)) still not reached; BSG of RS shape cannot pass \(\delta_C\approx0.0239\). Point–plane floor \(p^{7/4}\) unchanged. | **weakened** (second consecutive exponent move) |
| **First mass \(X\)** (target \(p^{1+1/1280}\)) | \(X=O(p^{34/23})\approx p^{1.47826}\) | \(X\le E^\times(h)\ll p^{31/21}(\log p)^8\approx p^{1.47619}\) (Prop. X). Target untouched; light–light Young barrier unchanged. | weakened (side quantity) |
| \(\max W\), support energy \(\Gamma_2\) | \(\max W\le X\); only \(n\mathcal E(\nu)-1=O(p^\gamma)\), \(\gamma<3/8\) matters | \(\max W\le X=O(p^{31/21+o(1)})\); \(\Gamma_2\) untouched | unchanged |
| **Cold growing-prefix confinement** | Criterion D, sup transfer or a hybrid price (per-simple seed price; sup/counting price for \(h\)) | Hybrid with size-only price of \(h\) is **refuted** (Theorem N, proved): loss \(\ge c_N\sim(8\gamma m''/s^3)\sqrt n\) in every sup-dominating price with \(P(S)\le s_p\); counting branch = Criterion D with \(\Lambda_n\asymp\sqrt n\). The hybrid seminorm \(H_\lambda\) satisfies Round 182 Prop. 2's hypotheses (conditional on D1–D4) with the same allowance \(\|B\|<0.24310\). Remaining: structured (non-size) information about \(h\): Criterion D / sup transfer for the B-generated part, or a new signed price. | **new obstruction** (proved, method-level) |
| Generic J sum \(O(p^{9/4})\); zero match; generic six-word class; cold complex stationary domain; derivative transfer; D2–D4; the target | open | unchanged | unchanged |

### 5.2 Precise remaining obligations

1. **One-match (ordinary).**
   - Push \(\delta_C\) beyond \(5/296\). The binding term is the BSG doubling loss in the pair price at heights \(p^{-e}\), \(e\in(0,1/15)\): excess \(\frac{11}{12}u\) against gain \(\frac58u\).
   - To reach the scheme floor \(\sup C=O(p^{4/3+o(1)})\) (covariance \(p^{43/24}\)), it suffices to prove **(HC′)**: \(E(U;U')\le Cp^{4/3}(aa')^{-2}\) for all pieces \(U\subseteq S_a\), \(U'\subseteq S_{a'}\), \(a,a'\in[cp^{-1/6},1]\). This is the corrected range; the report's \([p^{-1/15},1]\) is not enough.
   - Any partial result helps: a pair excess \(c(e)=\kappa e\) with \(\kappa<\frac{11}{12}\) gives \(\delta_C=\frac1{24}/(1+\frac85\kappa)\).
   - Below \(4/3\) needs a better incidence or energy input. MPRRS Lemma 33 lowers only the height-1 floor to \(p^{5/4}\).
   - Reaching \(O(p^{3/2})\) needs a non-point–plane input (floor \(p^{7/4}\)) and the generic six-word class below \(p^{9/2}\).
2. **First mass.** \(X=O(p^{1+1/1280})\) still needs a prime-only input at light levels. \(31/21\) is the new unconditional value.
3. **Support energy.** Unchanged.
4. **Cold.**
   - Criterion D or sup transfer for the B-generated words, i.e. an \(n\)-independent bound on \(\|w\|_\infty/\|w\|_{2,n}\) for \(w=L^bBL_S^aR_{602}\); or a fixed-height sup transfer through 611.
   - Alternatively, a new signed price that sees row–multiplier cancellation.
   - Plus D2–D4, (b4), (b-Jk), (b-T), the uniform complex stationary domain and derivative transfer.
   - The proved frozen rate stays 1.066.
5. Bookkeeping: propagate \(\delta_C=5/296\) to the Round 176/180 fixed-\(a\) generic squared mass. Generic J sum and zero-match unchanged. The original target remains open.

**Shared estimates.** `cand:slope-row-mass-x`: the one-match form now stands at \(\delta=5/296\) for \(\sup C\). The X / first-mass form moves only to \(31/21\), so the shared estimate under that ID stays open. If Round 187 tests (HC′), record it as a new candidate ID: it is a level-set pair-energy bound used only by the \(\sup C\) route; Prop. X's light–light barrier does not need it.

### 5.3 Recommended Round 187 calls (most valuable first)

**1. `ordinary-prime-level-pair-energy` (ordinary; the live lever on \(\delta_C\)).**
- **Question:** for the actual \(g=|f|^2\) with the cap, can the pair energy of level-set pieces be bounded with less BSG loss than Lemma M plus Reiher–Schoen gives? The full target is (HC′): \(E(U;U')\ll p^{4/3}(aa')^{-2}\) for \(U\subseteq S_a\), \(U'\subseteq S_{a'}\), \(a,a'\in[cp^{-1/6},1]\). A partial target is any pair excess \(\kappa e\) with \(\kappa<\frac{11}{12}\), for example a Lemma M variant whose structured side uses \(E^\times(W)\ge t^2|W|^4/(C\sqrt p)\) (Lemma S1) directly, with no BSG piece.
- **Why now:** Round 186 moved \(\delta_C\) from \(1/664\) to \(5/296\) and located the binding term exactly: BSG doubling \(K^4\) and size loss \(K^{-1/2}\) at heights \(p^{-e}\), \(e<1/15\). §6.2 of SUPC and this audit show that no Reiher–Schoen-shape BSG passes \(\delta_C\approx0.0239\). So the lever is a K-free or BSG-free level-set input.
- **Scope:** actual \(g\) with the cap; no (NC) input unless marked. Use Lemma M, Prop. P and Theorem B as audited, and the corrected (HC′) height range. Keep \(\sup C\) separate from \(X\). Quote any new external theorem from source. Exact exponent arithmetic. Large-\(p\) models should reach heights \(p^{-e}\) with \(e\) visibly positive, which needs \(p\ge10^7\) or tailored laws.
- **If yes:** (HC′) gives \(\sup C=O(p^{4/3+o(1)})\) and covariance \(p^{43/24+o(1)}\), the floor of point–line pricing. A partial \(\kappa\) gives \(\delta_C=\frac1{24}/(1+\frac85\kappa)\).
- **If no** (a model of admissible level sets with \(E(U;U')\ge p^{4/3+c}(aa')^{-2}\) at some height in range): point–line pricing of \(\sup C\) stalls near \(2125/1184\); the next lever is a non-point–plane input.
- **If inconclusive:** return the best \(\kappa\) and the configuration that binds.

**2. `cold-prime-b-word-delocalization` (cold; what COLD hands back).**
- **Question:** is \(\|w\|_{\infty,\rm good}/\|w\|_{2,n}\) bounded uniformly in \(n\) for the B-generated Duhamel words \(w=L^bB_hL_S^aR_{602}\) (Criterion D with an \(n\)-independent \(\Lambda\)), uniformly on \(Q\), both lifts? Alternatively, does a fixed-height sup transfer through 611 hold?
- **Why now:** Theorem N proves that no size-only price of the non-seed multiplier works. The actual operator is benign: \(\|B_hS\|_\infty\approx0.2\), with sup/RMS \(4.1\)–\(5.3\), close to \(\sqrt{2\ln n}\). Bounded versus \(\sqrt{\ln n}\) growth is exactly what Criterion D needs settled.
- **Scope:** physical rows at \(p\) up to about \(10^8\) with the full nine-centre row (evidence), plus any proof attempt. Separate certified from floating. Inherit Round 180's Criterion D statement exactly.
- **If yes** (a provably bounded ratio): the cold criterion closes through Criterion D, modulo D2–D4 and the stationary-domain inputs.
- **If no** (provable \(\sqrt{\ln n}\) growth): Criterion D fails in its \(n\)-independent form. Only a signed sup transfer or a new signed price remains.
- **If inconclusive:** the measured growth law, and the term that blocks a proof.

**3. (Optional; coordinator bookkeeping or a short call) propagate Theorem B.**
- Re-derive the Round 176/180 fixed-\(a\) generic squared-mass exponent with \(C(a)=O(p^{11/8-5/296+o(1)})\).
- Record (HC′) with its corrected height range.
- Optionally test whether the uncapped extraction improves Prop. X (SUPC left this open). This is low value, because the light–light Young barrier binds \(X\).

**Retire or do not renew:**
- **BSG-variant searches for \(\sup C\):** no available or possible Reiher–Schoen-shape BSG moves \(\delta_C\) past about 0.0239. Bloom's variants are worse, per the report's literature subagent (not re-read).
- **Structured-product incidence inputs at height 1** (MPRRS-type) as a lever on \(\delta_C\): they lower only the height-1 floor.
- **Hölder-to-\(E^\times(h_\ge)\) pricing of the all-heavy term** (the Round 185 Step H): superseded by per-tuple pricing.
- **Cold hybrid prices with \(h\) priced through \(\|h\|_\infty\), \(\|h\|_{2,n}\) or any normalised symmetric norm** (Theorem N), and counting-rate arguments inside the Round 173 horizon (Prop. 5).
- **The Round 184 test-2 cost** \(\rho_0\|h\|_\infty/\sqrt N+H(\|h\|_\infty)\) as an operator bound: false for every large \(n\).

## 6. Status of this audit

This is an agent audit, not human acceptance or certification.

**What I checked:**
- every claim the two reports label as proved;
- SUPC's Lemma M, Prop. P, Theorems A/B, Corollary C and Prop. X, re-derived by hand against the accepted Round 180/182/184/185 statements, read at source by line;
- Stevens–de Zeeuw Thm 4, Reiher–Schoen Thm 1.2 with its optimality remark, and MPRRS Lemma 33, re-read from arXiv through fetch subagents;
- every exponent, with exact Fractions, plus my own float LPs for Theorems A and B;
- the identities each step uses, replayed exactly at small \(p\);
- COLD's Lemma 1, exactly for 211 primes;
- COLD's Theorem N and Lemmas 2–3, by direct independent construction at three primes;
- COLD's Prop. 5, Cor. 6 and §5 arithmetic, at 50 digits;
- all five report scripts, re-run.

**What I did not check:** listed under "Not checked" in §4.

**Files:** nothing was committed. Only this file and the two `research/paley-186-audit-*.py` scripts were written.
