# Round 186 native Claude draft: pricing the heavy part of sup C pair by pair

- **call_id:** `ordinary-prime-sup-c-heavy-price` (one-match form of `cand:slope-row-mass-x`, settled for sup C at δ = 1/664 in Round 185).
- **agent_label:** `session/r186-sup-c-heavy-price`, a native Claude Opus 5.5 research session started by the Round 186 coordinator session.
- **Mission:** `coordination/missions/round-186/ordinary-prime-sup-c-heavy-price.md`, exported from `coordination/round-185.json` (SHA-256 `f5b2ff1f…8344`).
- **Inputs read.** All ten SHA-256 values match the mission:
  - `research/round-184-acceptance.json`, `research/round-185-acceptance.json`
  - `research/native-claude-audit-185.md` (§2 and §5 in full)
  - `research/native-claude-ordinary-prime-near-critical-band-autocorrelation-185.md`
  - `research/paley-185-band-exponents.py`, `research/paley-185-audit-band-check.py`
  - `research/native-claude-ordinary-prime-near-critical-slope-row-mass-184.md` (lines 60–190)
  - `research/native-claude-ordinary-prime-shifted-level-energy-182.md` (lines 20–260)
  - `research/ordinary-mixed-row-autocorrelation-180.md`, `research/ordinary-weighted-slope-product-incidence-178.md`

  Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-185.md`, the Round 183 acceptance entry on the BSG citation (`round-183-acceptance.json` line 265), and the sibling hand-over notes `r185-band-autocorrelation.md` and `r185-audit.md`.
- **Scripts** (both new):
  - `research/paley-186-supc-exponents.py`: exact Fractions. With `--lp` it adds a float LP cross-check (numpy, scipy).
  - `research/paley-186-supc-mixed-check.py`: `--check` mode uses exact integers; model mode uses floating point.
- **Status:** agent assessment only. It is not an audit, not human acceptance, and not a mathematical certification.

## Result summary

**Verdict: supported.** The proved value is \(\delta_C=5/296\), against Round 185's \(1/664\).

1. **Theorem B (main).** For the actual weight \(g=|f|^2\), under the hypotheses of the accepted Round 180/185 bound (the cap \(n\max\nu\le C_{\rm cap}\sqrt p\), with no near-critical input), uniformly in \(\lambda\in\mathbb F_p\setminus\{0,1\}\):
   \[\sup_{\lambda\ne1}C(\lambda)\ \ll\ p^{11/8-5/296}(\log p)^8 .\]
   - So \(\sup C=O(p^{11/8-\delta})\) for every \(\delta<5/296\). Since \(5/296\approx0.01689\), this is \(11.2\) times Round 185's \(1/664\approx0.00151\).
   - The only external theorem in the proof is Stevens–de Zeeuw Theorem 4. BSG enters only in the accepted Reiher–Schoen form (Round 183 citation).
2. **Corollary C.**
   - \(\sum_\xi W_\xi^{3/2}\) and \(\mathcal E(\mu)\) are \(O(p^{43/16-5/592+o(1)})\).
   - The one-match covariance is \(O(p^{2125/1184+o(1)})\). Here \(2125/1184=115/64-5/2368\approx1.79476\), against \(1193/664\approx1.79669\) in Round 185 and the scheme floor \(43/24\approx1.79167\).
3. **New ingredient: Lemma M (mixed shifted energy).** It is proved here from Stevens–de Zeeuw Theorem 4 by the method of Round 182's Lemma SE. Let \(B\) have small ratio set, and let \(A\) be an arbitrary set of size \(\alpha\). Then the pair energy that appears in Lemma 5's Cauchy–Schwarz satisfies
   \[E(A;B)\ll\alpha^{4/3}NK'^{2/3}\min(\alpha,K'N)^{1/3}.\]
   This prices a structured slot against an unstructured partner. Round 185 instead priced every slot separately, through Hölder to \(\prod\mathcal N(v_i)\).
4. **Why it moves δ_C.** Round 185 priced the all-heavy term at the worst heavy height in all four slots, with exponent \(4/3+20\varepsilon/3\). It balanced this against one band slot gaining only \(\varepsilon/4\).
   - Here each four-tuple of level/size components is priced separately, by the cheaper of two bounds:
     - the quadrilinear Stevens–de Zeeuw bound (the Lemma 4 form);
     - the Cauchy–Schwarz pair bound with Lemma M.
   - Extraction blocks are no longer capped at \(\sqrt p\). Lemma M does not need the cap that Lemma SE needed, and larger blocks have smaller doubling (\(K\le p^{e}\) instead of \(p^{2e}\) at height \(p^{-e}\)).
   - The binding configurations are a point–line pair at height \(p^{-e}\) whose structured side pays \(p^{(11/12)e}\) while Stevens–de Zeeuw gains \(p^{(5/8)e}\). Two families bind: \((0,0,e,e)\) with \(e=1/37\), and \((e,e,e,e)\) with \(e=1/74\).
5. **Intermediate Theorem A.** With Round 182's extraction kept exactly as accepted (blocks of size \(\sqrt p\)), the same method gives \(\sup C\ll p^{11/8-5/696}(\log p)^8\), and covariance \(p^{625/348+o(1)}\).
6. **Is the cap \(p^{4/3}\) attainable?**
   - **Not with current inputs.** Reaching \(4/3\) needs the pair excess at heights \(p^{-e}\), \(e\le1/15\), to vanish. The available BSG has doubling \(K^4\), and even an optimal BSG of this kind has doubling \(\ge K^{2.649}\) (Reiher–Schoen's remark, as reported by the literature subagent). So the excess stays positive, and \(\delta_C\le15/632\) for BSG-based pricing of this shape.
   - **Yes, conditionally**, under a K-free pair-energy criterion (HC) for level sets at heights in \([p^{-1/15},1]\) (§7).
   - The floor of the extended scheme at height 1 is \(p^{4/3}\) from Lemma M/SE. A newly quoted external bound, MPRRS Lemma 33, lowers that height-1 floor to \(p^{5/4}\), but it does **not** move \(\delta_C\) (§6.3).
7. **Side result (Proposition X, stated separately as the mission asks).** The same lemma gives \(X\le E^\times(h)\ll p^{31/21}(\log p)^8\). This improves Round 182's \(p^{34/23}\) slightly: \(31/21\approx1.4762\) against \(34/23\approx1.4783\). It has no effect on the one-match chain, it does not touch \(\Gamma_2\), and \(\max W\) is not separately improved.
8. **Evidence** (floating; Round 185's flat laws, \(p\le64013\)): pair energies of level sets satisfy \(E(1-U_a;1-U_b)\le2|U_a||U_b|(1+|U_a||U_b|/p)\). The largest pair price is \(0.07\)–\(0.29\,p^{2/3}\), and it decreases in \(p\). The true heavy prices are far below every proved bound, so the models give no sign of a \(p^{4/3+c}\) obstruction.

## Setup and hypotheses

Notation is that of Rounds 171–185, with counting norms throughout.

- **Field and law.** \(p\equiv1\pmod4\) prime, \(n=(p-1)/2\), \(Q\) the squares. \(\nu\) is a probability on \(\widehat Q\), \(f=\sum_\eta\nu_\eta\eta\) on \(Q\), \(g=|f|^2\).
- **(H1)/(H2).** \(0\le g\le1\), \(g(1)=1\), \(\operatorname{supp}g\subseteq Q\), \(G=\sum_xg\le n\max\nu\le C_{\rm cap}\sqrt p\). No near-critical (NC) input is used anywhere in this report.
- **Quadrilinear form.** \(C(\lambda)\le C^\sharp_\lambda[g,g,g,g]\) with point roles \(Y_1,Y_3\) (slots 1, 3) and line roles \(D_1,D_3\) (slots 2, 4) (Round 185 §2, R180-rel/lines/det).
- **Cauchy–Schwarz pairs.** Lemma 5's proof gives, before the Parseval step,
  \[C^\sharp_\lambda[f_1,f_2,f_3,f_4]\le\|c_{v_1,v_2}\|_2\,\|c_{v_3,v_4}\|_2,\qquad v_i(z)=f_i(1-z),\quad c_{v,v'}(\kappa)=\sum_zv'(z)v(\kappa z).\tag{CS}\]
  This step was accepted in Round 185 (audit item a2). The pairs are (slot 1, slot 2) and (slot 3, slot 4), i.e. one point role and one line role each.
- **Pair energy.** For sets \(A,B\subseteq\mathbb F_p\setminus\{0,1\}\) put \(m_{A,B}(u)=\#\{(x,y)\in A\times B:1-y=u(1-x)\}\) and \(E(A;B)=\sum_{u\in\mathbb F_p^\times}m_{A,B}(u)^2\).
  - If \(v_a=1_{X_a}(1-\cdot)\) and \(v_b=1_{X_b}(1-\cdot)\), then \(\|c_{v_a,v_b}\|_2^2=E(X_a;X_b)\), and \(E\) is symmetric (\(u\mapsto1/u\)).
  - \(\|c_{v,v'}\|_2\) is bilinear in \((v,v')\), so it satisfies the triangle inequality in each argument and is monotone on nonnegative functions.
  - These facts are checked exactly by the check script, parts (ii)–(iv).
- **Level sets.** \(S_t=\{x\ne1:g(x)\ge t\}\), \(|S_t|\le G/t\).

**Inputs, each with its source.**

| input | statement | source |
|---|---|---|
| R180-rel/lines/det, (SdZ) | quadrilinear relation; distinct nonvertical nonhorizontal lines for \(\lambda\ne0,1\); each variable determined by the other three; \(I(U_1\times U_3,\{\ell\}_{V_1\times V_3})\ll(|U_1||U_3|)^{5/8}(|V_1||V_3|)^{3/4}+|V_1||V_3|\) if \(\min(|U_1|,|U_3|)|V_1||V_3|\le c_0p^2\) | Round 180 lines 18–43; Round 185 §1 (accepted, audit a1) |
| SdZ4 | Stevens–de Zeeuw Theorem 4 (quoted below) | arXiv:1609.06284v4; quoted in Round 182 lines 120–122; re-read by the Round 185 audit |
| Lemma 4, Lemma 5 | height gain; Hölder bound, and its Cauchy–Schwarz form (CS) | Round 185 §2, accepted |
| S1 | \(E^\times(W)\ge t^2|W|^4/(n\max\nu)\) for \(W\subseteq S_t\) | Round 182 lines 100–110 (Rounds 163/173), accepted |
| BSG (RS) | if \(E^\times(R)\ge|R|^3/K\), there is \(B\subseteq R\) with \(|B|\ge\frac12K^{-1/2}|R|\) and \(|B/B|\le CK^4|B|\) | Reiher–Schoen arXiv:2308.10245v2, Theorem 1.2 (\(\varepsilon=1/2\)); citation fixed in `round-183-acceptance.json` line 265; used in accepted Rounds 163/173/177/182/184/185 |
| Lemma SE | \(E^\times(1-B)\ll K^{2/3}N^{8/3}\), \(N\le\sqrt p\) | Round 182 line 126, accepted (used only in Theorem A) |
| R182 extraction | per-level BSG extraction, Phase 1 / Phase 2, stopping below \(p^{1/2-\delta}\) | Round 182 lines 166–183; re-used in Round 185 Theorem 2 (accepted) |
| R184-P1(iii), R178, R180 chain | \(\sup C=O(p^{1+\varepsilon})\Rightarrow\) covariance \(O(p^{7/4+\varepsilon/8}\log^{1/4}p)\), via \(E^\times(m)\le X^2+\sup C\,M_1^2\) and the output \(p^{1/8}\mathcal E^{1/4}M_1\) | Round 184 slope-row-mass report lines 90–120, accepted |

**External theorem used in proofs.** Only Stevens–de Zeeuw Theorem 4 (arXiv:1609.06284v4), exactly as quoted in the accepted Round 182 report:

> "Let \(A,B\subset\mathbb F\) be sets with \(|A|=a\), \(|B|=b\), \(a\le b\) and \(ab^2\le n^3\). Let \(\mathcal L\) be a finite set of lines of size \(n\). If \(\mathbb F\) has positive characteristic \(p\), assume \(an\ll p^2\). Then \(I(A\times B,\mathcal L)\ll a^{3/4}b^{1/2}n^{3/4}+n\)."

Two elementary facts from Round 180 (lines 37–43) are re-used:
- If \(ab^2>n^3\), the bound still holds, because lines that are graphs over the \(A\)-coordinate give \(I\le an\le a^{3/4}b^{1/2}n^{3/4}\).
- Coordinates may be swapped for lines that are neither vertical nor horizontal.

Its hypothesis is checked at every scale used below.

## 1. Lemma M (mixed shifted energy)

**Lemma M.** Let \(A,B\subseteq\mathbb F_p\setminus\{0,1\}\) and \(V\subseteq\mathbb F_p^\times\), with \(|A|=\alpha\), \(|V|=|B|=N\) and \(|VB|\le K'N\) (\(K'\ge1\)). Suppose \(\alpha^{4/3}N^2\le c_1p^2\), where \(c_1>0\) is a constant fixed by the constant in SdZ4. Then
\[E(A;B)\ \le\ C\,\alpha^{4/3}N\,K'^{2/3}\min(\alpha,K'N)^{1/3},\]
with \(C\) absolute. In particular:
- **(form I)** \(E(A;B)\le C\alpha^{5/3}NK'^{2/3}\);
- **(form II)** \(E(A;B)\le C\alpha^{4/3}N^{4/3}K'\).

With \(A=B\) and \(\alpha=N\) it reduces to Lemma SE's \(K'^{2/3}N^{8/3}\), and it does not need \(N\le\sqrt p\).

*Proof.* Round 182's Lemma SE argument, with the point set changed.

*Lines and incidences.*
- For \((u,v)\in\mathbb F_p^\times\times V\), let \(\ell_{u,v}\) be the line \(Z=v(uX+1-u)\). Its slope is \(vu\ne0\) and its intercept is \(v(1-u)\). The slope plus the intercept equals \(v\), so the map \((u,v)\mapsto\ell_{u,v}\) is injective, and every line is neither vertical nor horizontal.
- For each row solution \((x,y)\in A\times B\) of \(1-y=u(1-x)\), and each \(v\in V\), the point \((x,vy)\in A\times VB\) lies on \(\ell_{u,v}\).
- The map \((u,v,x,y)\mapsto(\ell_{u,v},(x,vy))\) is injective, because \(y=(vy)/v\).

*Rich lines.* Let \(T_h=\{u:m_{A,B}(u)\ge h\}\) with \(t=|T_h|\), and use the \(n=tN\) lines \(\{\ell_{u,v}\}_{u\in T_h,v\in V}\). Then \(I(A\times VB,\cdot)\ge htN\).
- Write \(s\le b'\) for the sizes \(\alpha\) and \(|VB|\) in increasing order.
- SdZ4, with the two reductions above, gives \(htN\le C_1(s^{3/4}b'^{1/2}(tN)^{3/4}+tN)\).
- For \(h\ge2C_1\) this yields \(tN\le16C_1^4s^3b'^2/h^4\).
- The bound \(s^{3/4}b'^{1/2}\) is nondecreasing in both sizes, and \(s^3b'^2\le\alpha^2(K'N)^2\min(\alpha,K'N)\). Hence
  \[t(h)\le C_2\,\alpha^2K'^2N\min(\alpha,K'N)/h^4 .\]

*Hypothesis of SdZ4.* Since \(t\le\sum_um(u)/h=\alpha N/h\), we have \(a\cdot n\le\min(\alpha,K'N)\,\alpha N^2/h\). Put \(H=\max(H_0,(\alpha K'^2\min(\alpha,K'N))^{1/3})\). For \(h\ge H\):
- if \(\alpha\le K'N\), then \(an\le\alpha^2N^2/\alpha^{2/3}=\alpha^{4/3}N^2\);
- otherwise \(an\le\alpha^{2/3}N^{8/3}\le\alpha^{4/3}N^2\).

Both are \(\le c_1p^2\). The exponent script verifies this case split at sample points.

*Energy.* Rows with \(m<H\) contribute \(\le H\sum m=H\alpha N\). Dyadic classes \(h_i=2^iH\) contribute \(\le\sum_i4h_i^2t(h_i)\ll\alpha^2K'^2N\min/H^2\). With the stated \(H\), both are \(\ll\alpha^{4/3}NK'^{2/3}\min^{1/3}\).

If \(H=H_0\), the bound is \(O(\alpha N)\), which is smaller, because \(\alpha,K',\min\ge1\). ∎

`paley-186-supc-mixed-check.py --check 13 17 29 37` verifies exactly:
- distinctness of the lines;
- that every incidence point lies in \(A\times VB\);
- injectivity of the incidence map;
- \(I\ge h|T_h||V|\);
- \(\sum_um=\alpha N\);
- \(E(A;B)=\|c\|_2^2=E(B;A)\);
- the triangle inequality for \(E^{1/2}\);
- \((C^\sharp_\lambda)^2\le E(X_1;X_2)E(X_3;X_4)\) for all \(\lambda\notin\{0,1\}\).

## 2. Decomposition into components

Fix \(\tau_0=p^{-1/7}\), as in Round 185, and a parameter \(\delta>0\).

- **Light.** \(g_L=g1[g<\tau_0]\). Any four-tuple with a light slot costs \(\le\tau_0G^3=O(p^{19/14})\) by R180-det (Step L, unchanged).
- **Levels.** For \(k\ge0\) with \(a_k=2^{-k}\ge\tau_0\), let \(U_k=\{x\ne1:\max(\tau_0,a_k/2)\le g(x)\le a_k\}\subseteq S_{a_k/2}\), so \(|U_k|\le2G/a_k\). Write \(a=p^{-e}\) with \(0\le e\le1/7\).
- **Uncapped extraction** (used for Theorem B). Put \(R\leftarrow U_k\). While \(|R|\ge p^{1/2-\delta}\):
  - take the **whole** remainder \(R\), with \(m=|R|\);
  - Lemma S1 at \(t=a/2\) gives \(K:=m^3/E^\times(R)\le4C_{\rm cap}\sqrt p/(a^2m)\);
  - Reiher–Schoen gives \(B\subseteq R\) with \(|B|\ge\frac12K^{-1/2}m\) and \(|B/B|\le CK^4|B|\);
  - remove \(B\) from \(R\).

  Group the pieces by the dyadic size \(M\le|R|<2M\) of the remainder at the time they were extracted, and write \(M=p^{1/2-\mu}\), where \(-e-O(1/\log p)\le\mu\le\delta\). The union of the pieces of one group is a **phase component** \(X_{k,\mu}\). It has
  \[|X|\le2M,\qquad K\le Cp^{2e+\mu},\qquad |B|\ge c\,a\,M^{3/2}p^{-1/4}=c\,p^{1/2-3\mu/2-e},\qquad K'=|B/B|/|B|\le CK^4 .\]
  The final remainder is the **leftover** \(LO_k\), with \(|LO_k|<p^{1/2-\delta}\).
- **Round 182's capped extraction** (used for Theorem A and Proposition X) takes blocks of size \(\lfloor\sqrt p\rfloor\) while \(|R|\ge\sqrt p\) (Phase 1), and then the whole remainder (Phase 2). It is the special case in which Phase 1 is one component with \(K\le Ca^{-2}\) and \(|B|\ge c\sqrt p\,a\), and Phase 2 has \(\mu\ge0\).

So \(g-g_L=\sum_k\sum_{X}g1_X\) over \(O((\log p)^2)\) components per slot: \(O(\log p)\) levels, each with \(O(\log p)\) phases and one leftover. Expanding \(C^\sharp_\lambda[g,g,g,g]\) multilinearly gives \(O((\log p)^8)\) four-tuples of components, plus the light terms.

**Two prices for a four-tuple** \((X_1,\dots,X_4)\), where \(X_i\) has height \(a_i=p^{-e_i}\) and size \(\le Cp^{1/2-\mu_i}\) (leftover: \(\mu_i=\delta\)):

- **(SdZ)** By Lemma 4's incidence count applied to the sets (all inside \(\{g\ge\tau_0\}\), so (SdZ) applies, Round 185 Lemma 4):
  \[C^\sharp\le\prod a_i\cdot I\ll p^{11/8-\sum_i\mathrm{gain}_i}+G^2,\qquad \mathrm{gain}_i=e_i+\theta_i\mu_i\ \ (\theta=5/8\text{ point},\ 3/4\text{ line}).\]
  Because \(\mu_i\ge-e_i\), \(\mathrm{gain}_i\ge(1-\theta_i)e_i\ge0\). This is the per-component form of Round 185's Steps B and H-b.
- **(Pair)** By (CS) and monotonicity, \(C^\sharp\le a_1a_2a_3a_4\,E(X_1;X_2)^{1/2}E(X_3;X_4)^{1/2}\). Each pair is priced by Proposition P below.

## 3. Proposition P (pair price)

Let \(X_s\) be a phase component (height \(p^{-e_s}\), parameter \(\mu_s\)), and \(D\subseteq Q\setminus\{1\}\) any set with \(|D|\le Cp^{A}\). If Lemma M's hypothesis holds for every piece of \(X_s\) against \(D\), then
\[E(X_s;D)^{1/2}\ \ll\ p^{\frac56A+\frac14+\frac{19}6e_s+\frac{13}{12}\mu_s}.\]

*Proof.*
- Apply the triangle inequality over the pieces \(B\) of \(X_s\).
- Apply Lemma M, form I, with \(V=B^{-1}\), so that \(VB=B/B\) and \(K'\le CK^4\):
  \[E(X_s;D)^{1/2}\le\sum_BC\,|D|^{5/6}|B|^{1/2}K'^{1/3}\le C|D|^{5/6}K^{4/3}\cdot2M\cdot(\min|B|)^{-1/2}.\]
- Insert \(K\le Cp^{2e+\mu}\), \(M=p^{1/2-\mu}\) and \(\min|B|\ge cp^{1/2-3\mu/2-e}\). ∎

**Pair exponent.** Take \(D=X_g\), a phase component of the partner slot, so \(A=\tfrac12-\mu_g\), and include the heights \(a_sa_g\). The pair is priced at \(p^{2/3+c}\) with
\[c(s\to g)=\tfrac{13}6e_s+\tfrac{13}{12}\mu_s-e_g-\tfrac56\mu_g .\]
For whole level sets (\(\mu=-e\)) this is \(c=\frac{13}{12}e_s-\frac16e_g\).

Form II gives \(p^{2/3+\frac{10}3e_s+\frac32\mu_s-e_g-\frac23\mu_g}\). It is never needed below, but it is checked in the LP.

**Hypothesis.** All sizes are \(\le Cp^{1/2+e}\), so \(\alpha^{4/3}N^2\le Cp^{(10/3)(1/2+\max e)}\). This is \(\le C p^{35/18}=o(p^2)\) whenever every height satisfies \(e\le1/12\).

## 4. Theorem B

**Theorem B.** Under (H1)/(H2) with the cap, uniformly in \(\lambda\in\mathbb F_p\setminus\{0,1\}\),
\[\sup_{\lambda\ne1}C(\lambda)\ \ll\ p^{11/8-5/296}(\log p)^8 .\]

*Proof.* Take \(\delta=1/37\). There are \(O((\log p)^8)\) four-tuples of components, plus the light terms (\(\ll p^{19/14}\), and \(19/14<11/8-5/296\)) and the \(G^2\)-terms. It suffices to show that every four-tuple costs \(\ll p^{11/8-5/296}\).

1. **A leftover in some slot.** That slot has \(\mathrm{gain}\ge\theta\delta\ge\frac58\cdot\frac1{37}=\frac5{296}\). Then (SdZ) suffices.
2. **Some height \(e_i>1/12\).** Then \(\mathrm{gain}_i\ge e_i/4>1/48>5/296\). Again (SdZ) suffices.
3. **Otherwise** all slots are phase components with \(e_i\le1/12\), and Proposition P applies to both pairs.
   - For a component put \(u=2e+\mu\in[e,\,2e+\delta]\).
   - **Pair excess.** \(\frac{13}6e_s+\frac{13}{12}\mu_s=\frac{13}{12}u_s\). Also \(e_g+\frac56\mu_g=\frac16u_g+\frac23(e_g+\mu_g)\ge\frac16u_g\). Choosing as structured side the slot \(s\) with \(u_s\le u_g\) gives
     \[c_{\rm pair}\le\tfrac{13}{12}u_s-\tfrac16u_g\le\tfrac{11}{12}\min(u_i,u_j).\]
   - **Pair gain.** \(\mathrm{gain}=e+\theta\mu=\theta u-(2\theta-1)e\ge(1-\theta)u\), because \(e\le u\). One slot is a point role (\(1-\theta=3/8\)) and the other a line role (\(1/4\)), so
     \[\mathrm{gain}_{\rm pair}\ge\tfrac38u_{\rm pt}+\tfrac14u_{\rm ln}\ge\tfrac58\min(u_i,u_j).\]
   - Hence \(c_{\rm pair}\le\frac{22}{15}\,\mathrm{gain}_{\rm pair}\) for both pairs.
   - With \(\Gamma=\) total gain, the four-tuple costs
     \[\ll p^{\min(11/8-\Gamma,\ 4/3+\frac{22}{15}\Gamma)}\le p^{11/8-5/296},\]
     since the two exponents are equal at \(\Gamma(1+\frac{22}{15})=\frac1{24}\), i.e. \(\Gamma=\frac5{296}\).

All constants are absolute or depend only on \(C_{\rm cap}\). No bound depends on \(\lambda\). ∎

**Sharpness of the bookkeeping.** Two configurations of whole level sets attain \(11/8-5/296\) with equality, so the exponent cannot be improved by re-choosing \(\delta\) or the cases:
- \((e_1,e_2,e_3,e_4)=(0,0,\frac1{37},\frac1{37})\);
- \((\frac1{74},\frac1{74},\frac1{74},\frac1{74})\).

A float LP over all configurations confirms \(5/296\) (`--lp`). That LP includes forms I and II, the trivial pair bound \(E\le|X||Y|\min(|X|,|Y|)\), and all signs of \(\mu\).

**Theorem A (Round 182's extraction unchanged).** The same proof with \(\sqrt p\)-capped Phase 1 gives
\[\sup_{\lambda\ne1}C(\lambda)\ll p^{11/8-5/696}(\log p)^8,\qquad\delta=1/87 .\]
- With \(K\le Ca^{-2}\), the Phase-1 pair excess is \(\frac{19}6e_s-\frac16e_g\le3\min(e)\), against gain \(\ge\frac58\min(e)\), giving ratio \(24/5\).
- Phase-2 pairs have excess \(\le\frac{13}6e+\frac{13}{12}\mu\le\frac{24}5(e+\frac58\mu)\).

The exact script checks every case. Theorem A is recorded because it uses Round 182's accepted extraction verbatim. Theorem B differs only in letting the first block be the whole remainder: that is legal for Lemma S1 and BSG, and it is needed only because Lemma SE required \(N\le\sqrt p\), which Lemma M does not.

**Ablation** (float LP, same component model):

| pricing | \(\delta_C\) |
|---|---|
| Round 185 (Hölder to \(E^\times(h_\ge)\), uniform \(\tau_1\)) | \(1/664\) |
| per-height split, Hölder \(\prod\mathcal N\) only | \(1/184\) |
| + Lemma M, capped blocks (Theorem A) | \(5/696\) |
| + uncapped blocks (Theorem B) | \(5/296\) |

## 5. Corollary C (propagation)

The chain is Round 184 Proposition 1(iii) and Round 180's \(E^\times(m)\le X^2+\sup C\cdot M_1^2\), with \(X^2=O(p^{68/23})\) below \(\sup C\cdot M_1^2\). With \(\delta_C=5/296\):

| quantity | before (R185) | now |
|---|---|---|
| \(\sup_{\lambda\ne1}C\) | \(p^{11/8-1/664}\) | \(p^{11/8-5/296}(\log p)^8\) |
| \(\sum_\xi W_\xi^{3/2}\), \(\mathcal E(\mu)\) | \(p^{43/16-1/1328}\) | \(p^{43/16-5/592}(\log p)^4\) |
| \(\|H_\alpha\|_2\) | \(p^{147/128-1/10624}\) | \(p^{147/128-5/4736+o(1)}\) |
| \(\sum w\|H_\alpha\|^2\) | \(p^{179/64-1/5312}\) | \(p^{179/64-5/2368+o(1)}\) |
| one-match covariance | \(p^{1193/664}\) | \(p^{2125/1184}(\log p)^{2}\) |

\(2125/1184=115/64-5/2368\). The fixed-slope first mass \(C(a)\), \(a\ne1\), improves in the same way to \(O(p^{11/8-5/296+o(1)})\). The downstream Round 176/180 fixed-\(a\) generic squared mass is not re-derived here.

## 6. The three routes named by the mission

### 6.1 All-heavy term priced directly in the quadrilinear form — **done; this is Theorem B**

Instead of Hölder to \(\prod\mathcal N(v_i)\le E^\times(h_\ge)\), the all-heavy and mixed terms are priced pairwise inside (CS). A structured slot (BSG pieces) is priced against an arbitrary partner by Lemma M, and the result is compared, four-tuple by four-tuple, with Stevens–de Zeeuw.

The gain over Round 185 has two sources:
- **(i)** A configuration with one slot at height \(p^{-e}\) and its partner at height 1 now costs \(p^{4/3-e/6}\) instead of \(p^{4/3+5e/3}\). The structured partner carries the price; the generic slot even gains.
- **(ii)** Larger blocks have smaller doubling.

### 6.2 BSG with smaller loss, or higher energies (Proposition 6) — **no gain available**

With the binding at whole level sets (\(K\le p^{e}\)), a BSG with doubling \(K^c\) and size loss \(K^{-\sigma}\) gives pair excess \((\frac c3+\frac\sigma2-\frac23)e\).
- Reiher–Schoen (\(c=4\), \(\sigma=\frac12\)) gives \(\frac{11}{12}e\), the value used here.

The alternatives below were found by a literature subagent that read the arXiv PDFs. They are reported here as its findings; I did not re-read them, and they are used in **no** proof.
- **Bloom, arXiv:2501.09470v1, Theorem 8** (\(c=\frac{100}{27}+\epsilon\), \(\sigma=\frac{100}{81}+\epsilon\)) gives \(\frac{32}{27}e\), which is worse.
- **Bloom's \(E_3\) form (Theorem 15)**, fed by \(E_3\ge E^2/|W|^2\), has size loss \(K^{-4/3}\), which is worse.
- **Reiher–Schoen remark.** No BSG of this shape can have \(c<\log4/\log(27/16)\approx2.649\). Even an optimal BSG would give at most \(\delta_C\approx15/632\) by this pricing (\(c=8/3\) in the script).
- **Prop. 6 (\(T_k\)).** For a whole level set it gives \(T_k\ge|W|^{2k-1}t^{k-1}\). No BSG for \(T_k\) with better losses is known.

So BSG variants are not the lever.

### 6.3 Stronger incidence input for structured Cartesian products — **lowers the height-1 floor only**

Found by the literature subagent:
- **Stevens–de Zeeuw Theorem 4** remains the state of the art for \(A\times B\) at \(|A|,|B|\asymp\sqrt p\). Shkredov, arXiv:1802.09066v2, Lemma 12, has the same exponent with no \(p\)-condition. Rudnev–Shkredov, arXiv:1812.01671v3, Theorem 8, gains only through the energy of the line set.
- **Murphy–Petridis–Roche-Newton–Rudnev–Shkredov**, arXiv:1702.01003v5 (Mathematika 65 (2019)). I read Lemma 33 myself in the text extracted from the arXiv PDF:

  > "Lemma 33. Let A, B ⊂ F such that |A||AA||B| ≤ p^2 and also max(|AA|, |B|) ≤ (|A||AA||B|)^{1/2}. Then for any α ∈ F^*, E^×(A + α, B) ≪ |AA|^{3/2}|B|^{3/2}/|A|^{1/2}."

  - Applied with \(A=-B_{\rm piece}\), \(\alpha=1\), and \(B=1-D\), it gives \(E(B_{\rm piece};D)\ll M^{3/2}N|D|^{3/2}\), with \(|AA|=M|A|\).
  - At height 1 (\(M=O(1)\), \(N=|D|\asymp\sqrt p\)) the hypotheses hold: \(Mp^{3/2}\le p^2\), \(M\le|D|\), \(|D|\le N^2M\). A height-1 pair then costs \(p^{5/8}\) instead of \(p^{2/3}\), so the height-1 floor becomes \(p^{5/4}\).
  - Away from height 1, BSG gives only \(|B/B|\le K^4|B|\), hence \(M\le K^8\) by Plünnecke–Ruzsa, and the \(M^{3/2}\) factor makes Lemma 33 worse than Lemma M.
  - The family \((e,e,e,e)\), \(e=\frac1{74}\), is unaffected, so **\(\delta_C\) stays \(5/296\)**. The float LP with Lemma 33 allowed everywhere confirms this.
  - Lemma 33 is therefore **not used** in Theorem B. It is recorded for the cap question.
- **Exact subgroups.** Macourt–Shkredov–Shparlinski, arXiv:1701.06192v2, Corollary 4.1 (reported by the subagent; not re-read), give \(E^\times(\Gamma+\lambda)\ll|\Gamma|^2\log|\Gamma|\) at \(|\Gamma|\asymp\sqrt p\). That is near-sharp, but level sets are not subgroups.

## 7. Is the cap \(p^{4/3}\) attainable?

**Within Round 185's scheme** (Hölder to \(E^\times(h_\ge)\), uniform cut \(\tau_1\)): no. The audit's cap \(\delta_C\le1/24\) stands, and that scheme reached only \(1/664\).

**Within the extended scheme of Theorem B:**
- The configurations whose (SdZ) price exceeds \(p^{4/3}\) are those with total gain \(<1/24\). For a pair at common height \(p^{-e}\) that means \(e<1/15\); for a single line role, \(e<1/6\).
- Reaching \(\sup C=O(p^{4/3})\) therefore needs the pair excess \(c(e)\) to vanish for heights \(e\in[0,1/15]\).
- With current inputs \(c(e)=\frac{11}{12}e>0\). The excess comes from the BSG doubling \(K^4\) (\(\frac43e\)) and the size loss (\(\frac14e\)), net of the height and generic-side credit.
- By §6.2 no BSG of this shape removes it. **Not attainable with current inputs.**

**Conditional criterion (HC).** Suppose that for all heights \(a,a'\in[p^{-1/15},1]\) and level-set pieces \(U\subseteq S_a\), \(U'\subseteq S_{a'}\):
\[E(U;U')\le C\,p^{4/3}(aa')^{-2}.\]
Then the pair price is \(\le p^{2/3}\) at those heights, and the scheme gives \(\sup C=O(p^{4/3})\), i.e. covariance \(p^{43/24}\). Step L must then use \(\tau_0=cp^{-1/6}\), which is admissible.

Facts about (HC):
- It is the trivial bound at \(a=p^{-1/6}\).
- It is weaker than a \(K\)-free Lemma M (\((|U||U'|)^{4/3}\)) for whole level sets.
- It holds with enormous room in every model (§8).

So (HC) is a level-set statement with no BSG size loss, the analogue of Round 182's criterion (b1) at heavy heights.

**Beyond \(4/3\).** With MPRRS Lemma 33 the height-1 floor is \(p^{5/4}\). The extended scheme is then limited by the moderate-height pairs, not by height 1.

## 8. Proposition X (side result: \(X\) and \(E^\times(h)\))

**Proposition X.** Under (H1)/(H2) with the cap, \(X\le E^\times(h)\ll p^{31/21}(\log p)^8\).

*Proof.* Use (CS) with \(\lambda=1\), in the form \(E^\times(h)^{1/2}=\|c_{h,h}\|_2\le\sum_{i,j}E(v_i,v_j)^{1/2}\) over components. Here Stevens–de Zeeuw is **not** available (the lines form a pencil), so every pair is priced alone. Take light \(g<p^{-1/42}\) and the capped extraction with \(\delta=1/126\). Each pair exponent is \(\le31/42\), with exact values in the script:

| pair | bound | exponent |
|---|---|---|
| light–light | Young, \(\|v\|_1^2\|v\|_2^2\le\tau G^3\) | \(3/4-\varepsilon/2\) |
| Phase-1–Phase-1 | form I | \(\le2/3+3\min e\) |
| Phase-2 structured vs anything | form I | \(\le157/216\) |
| leftover–leftover | trivial | \(3/4-3\delta/2\) |
| leftover–light | \(\|c\|_\infty\|c\|_1\) | \(3/4-3\delta/4-\varepsilon/4=31/42\) |
| structured–light | layer cake in the light function, Lemma M for \(s\ge C'p^{-1/4}\) (hypothesis \(\alpha^{4/3}N^2\le c_1p^2\) with \(\alpha\le G/s\)), trivial below | \(\le2/3-\varepsilon/6+\frac{19}6e\) |

The binding balance is \(3/4-\varepsilon/2=2/3+3\varepsilon\) at \(\varepsilon=1/42\). ∎

**Reading.**
- \(31/21<34/23\) (Round 182). This is an input that bounds \(X\), stated separately as the mission asks.
- It does not touch \(\Gamma_2\), and \(\max W\le X\) moves only to \(p^{31/21+o(1)}>p^{11/8}\).
- The X target \(p^{1+1/1280}\) is untouched: the light–light Young bound is the barrier, exactly as Round 182 Proposition 4 says.
- The uncapped extraction might improve Proposition X further. That was not examined, because small phases paired with the light part need separate pricing.

## 9. Evidence (floating; flat-law models, not the actual optimiser)

`paley-186-supc-mixed-check.py 1009 4001 16001 64013` uses Round 185's laws (`rand`, `aphalf`, `ap+rand b=2,4`) and dyadic level sets \(U_a\), \(a\ge p^{-1/7}\).

| p | model | \(\max_{a,b}E(U_a;U_b)/(|U_a||U_b|(1+|U_a||U_b|/p))\) | max pair price \(ab\,E^{1/2}/p^{2/3}\) |
|---|---|---|---|
| 4001 | ap+rand 2 | 1.672 | 0.286 |
| 16001 | ap+rand 2 | 1.696 | 0.236 |
| 64013 | ap+rand 2 | 1.811 | 0.169 |
| 64013 | aphalf | 1.943 | 0.107 |
| 64013 | ap+rand 4 | 1.895 | 0.068 |

Readings:
- Pair energies are near-sharp, about \(2|U||U'|\). Pair prices are about \(p^{1/2}\), and their ratio to \(p^{2/3}\) falls with \(p\).
- The measured \(K=|U|^3/E^\times(U)\) of level sets is \(1.5\)–\(6\).
- At these \(p\) every level \(a\ge p^{-1/7}\) is within a constant of \(1\), so the models do not test the exponents. They only show that no heavy configuration approaches the proved bounds, and they give no sign of a \(p^{4/3+c}\) obstruction.
- `rand` has no level above \(p^{-1/7}\) at \(p\ge4001\).

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved here.** These are ordinary arguments from accepted inputs plus Stevens–de Zeeuw Theorem 4. Exponent algebra is in exact Fractions; identities are checked exactly at \(p\le37\).
- (a1) Lemma M: \(E(A;B)\ll\alpha^{4/3}NK'^{2/3}\min(\alpha,K'N)^{1/3}\) under \(\alpha^{4/3}N^2\le c_1p^2\).
- (a2) Proposition P: pair price of an extraction component against any set.
- (a3) Theorem B: \(\sup_{\lambda\ne1}C\ll p^{11/8-5/296}(\log p)^8\).
- (a4) Theorem A: \(\sup_{\lambda\ne1}C\ll p^{11/8-5/696}(\log p)^8\), with Round 182's extraction unchanged.
- (a5) Corollary C: \(\sum W^{3/2},\mathcal E(\mu)\ll p^{43/16-5/592+o(1)}\); covariance \(p^{2125/1184+o(1)}\).
- (a6) Proposition X: \(X\le E^\times(h)\ll p^{31/21}(\log p)^8\).
- (a7) Method statements:
  - the bookkeeping of Theorem B is attained by two configurations;
  - the BSG sensitivity \(\delta_C(c)\);
  - Lemma 33 of MPRRS does not move \(\delta_C\).

Hypotheses for (a1)–(a6): (H1)/(H2) with the cap only. **No (NC) input.** Inherited: Lemma S1, Reiher–Schoen Theorem 1.2, Round 180/185 incidence set-up, and the Round 178/180/184 chain for (a5).

**(b) Conditional.**
- (b1) (HC) at heights \([p^{-1/15},1]\) gives \(\sup C=O(p^{4/3})\) and covariance \(p^{43/24}\) (§7).
- (b2) A BSG of the Reiher–Schoen shape with doubling \(K^c\) gives \(\delta_C=\frac1{24}\big/\big(1+\frac85(\frac c3-\frac5{12})\big)\). For example, \(c=3\) gives \(5/232\). Such a theorem is not available.

**(c) Evidence.** Exact checks at \(p=13,17,29,37\). Floating models at \(p\le64013\) (§9). Float LPs cross-check Theorems A and B and the ablation.

## Remaining gap

- **One-match:** covariance \(p^{2125/1184+o(1)}\approx p^{1.79476}\). This is still above the scheme floor \(p^{43/24}\approx p^{1.79167}\), far above the point–plane floor \(p^{7/4}\), and far above the target \(p^{3/2}\).
  - Within point–line pricing, the lever is now a level-set pair-energy bound without BSG size loss, (HC).
  - Below \(p^{7/4}\), a non-point–plane input is still required. The generic six-word class and the zero-match estimate are unchanged.
- **X / first mass:** \(X=O(p^{31/21+o(1)})\) is proved here, but the target \(p^{1+1/1280}\) still needs a prime-only input at light levels.
- **\(\max W\):** not addressed, as the mission asks.
- **Review needed.** The auditor should check:
  - Lemma M, especially the SdZ hypothesis case split and the use of the upper bound \(K'N\) for \(|VB|\);
  - the uncapped extraction, especially Lemma S1 and BSG for blocks larger than \(\sqrt p\), and the phase parameters;
  - the \(u=2e+\mu\) reduction in Theorem B;
  - that the \(O((\log p)^8)\) four-tuples exhaust the expansion.

## Replay

| script | SHA-256 |
|---|---|
| `research/paley-186-supc-exponents.py` | `93debdd567a6b99fb5c77dc382f72dc2e895b478bd9e9dfd2acb2b67f7a67b8f` |
| `research/paley-186-supc-mixed-check.py` | `068621075f749cbbd36edcf1c463ec60feef8e49a5b2ff838f53942717f79cae` |

```bash
.venv/bin/python -B research/paley-186-supc-exponents.py --lp
```
Exact Fractions, plus a float LP (numpy, scipy); under 2 s. The output ends `ALL OK`.

```bash
.venv/bin/python -B research/paley-186-supc-mixed-check.py --check 13 17 29 37
```
Exact integers; under 1 s. The output ends `EXACT CHECKS OK`.

```bash
.venv/bin/python -B research/paley-186-supc-mixed-check.py 1009 4001 16001 64013
```
Floating models; a few seconds.

## What would change the proof plan

- **If an audit accepts Theorem B:** the accepted one-match exponent moves from \(1193/664\) to \(2125/1184\), and \(\sup C\) to \(11/8-5/296\). Proposition X moves \(X\) to \(31/21\).
- **Next lever for \(\sup C\):** (HC), a whole-level pair-energy bound without BSG loss at heights \(\ge p^{-1/15}\). It would give the scheme floor \(p^{4/3}\).
  - A first test is numerical: compute \(\max E(U;U')/(|U||U'|)\) for admissible level sets at growing \(p\), with heights near \(p^{-1/37}\) reached by larger models.
  - A first theoretical test is to look for a version of Lemma M whose structured side uses \(E^\times(W)\ge|W|^3/K\) directly, without passing to a BSG piece.
- **Beyond \(4/3\):** MPRRS Lemma 33 shows that height-1 pairs can be priced at \(p^{5/8}\), so the floor is not \(4/3\) for structured inputs. Any further progress, however, runs into the moderate-height doubling loss.

## Verdict

**Supported.** Under the mission definition, any \(\delta_C>1/664\) counts.
- \(\sup_{\lambda\ne1}C(\lambda)\ll p^{11/8-5/296}(\log p)^8\), with \(5/296\approx0.0169\), against \(1/664\approx0.0015\).
- Hence one-match covariance \(O(p^{2125/1184+o(1)})\).
- Proved from accepted inputs plus Stevens–de Zeeuw Theorem 4, with no near-critical hypothesis.
- The scheme cap \(p^{4/3}\) is **not** attainable with current inputs. The binding pair is a point–line pair of whole level sets at height \(p^{-1/37}\) (or all four slots at \(p^{-1/74}\)), where the BSG doubling loss \(p^{(11/12)e}\) meets the Stevens–de Zeeuw gain \(p^{(5/8)e}\).
- The cap is reachable under the K-free criterion (HC).

This is an agent draft awaiting audit. It does not prove or refute the ordinary theta-limit target.
