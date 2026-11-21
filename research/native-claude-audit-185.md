# Independent audit of Round 185 (session/r185-audit)

- **Auditor:** Claude Opus 5.5 side session started by the Round 185 coordinator. This is an agent audit, not human acceptance and not a mathematical certification. The auditor wrote neither report and is not the coordinator.
- **Status of this file:** written incrementally. The "Blind overlap review" section below was saved before any file under `coordination/shared-obligations/`, `coordination/drafts/` or any `coordination/round-*-inflight.json` was opened.
- **Read before the blind review:** `AGENTS.md`, `docs/WORKFLOW.md`, `docs/ROUND_REVIEW.md`, `coordination/checkpoints/round-184.md`, `research/native-claude-audit-184.md`, the two missions in `coordination/missions/round-185/`, and the two reports.

Verdict key (per claim the report labels as proved):
- **ACCEPTED:** correct as written, for the stated hypotheses.
- **ACCEPTED WITH CORRECTION:** true after the stated correction, which does not change the report's main conclusion.
- **CONDITIONAL:** correct given a named input that is not proved or not checked.
- **REJECTED:** false as written, or not supported.

Reports, abbreviated:
- **BAND** = `native-claude-ordinary-prime-near-critical-band-autocorrelation-185.md` (one-match form of `cand:slope-row-mass-x`; \(\sup_{\lambda\ne1}C\), \(\max W\), \(\sum W^{3/2}\));
- **COLD** = `native-claude-cold-prime-picard-leaf-inequivalence-185.md` (signed model \(A_{\mathcal X}\)-price of \(h-h_1\) and \(h\)).

## 1. Blind overlap review

Written after reading the two reports and their missions. No shared-obligation, draft or inflight file had been opened.

| Pair | Classification | Reason |
|---|---|---|
| BAND – COLD | **independent** | BAND bounds point–line incidence sums of the ordinary weight \(g=|f|^2\) on \(\mathbb F_p\) (Stevens–de Zeeuw, BSG/Lemma SE, Rudnev–Shkredov chain). COLD prices transported two-fibre simples of the cold frozen-base iteration at \(V_{602}\) in the compact sheaf model. No object, lemma, estimate, external theorem or script is common. Neither report cites the other or any input the other proves. |

- **No shared estimate, no shared input beyond the project's general setting** (\(p\equiv1\bmod4\), \(n=(p-1)/2\), \(Q\) the squares). The cold report's mean-field mechanism (trivial constituent of \(K(J^k)\otimes K(J^k)\)) and the band report's level-set decomposition of \(g\) live on different objects.
- **Not duplicated.** Each call answered its own mission question.
- **Would an overlap review have changed dispatch?** No. The two calls are on different routes (ordinary one-match; cold dimension price) and either outcome of one leaves the other's question unchanged.
- **Within BAND (not a pair, recorded for the closeout):** BAND's §5–§6 touch the X/first-mass obligation (Round 184 (b3), Proposition 6). That is the same shared estimate `cand:slope-row-mass-x` already named in the mission, not a new overlap. BAND explicitly does not use the near-critical support-energy quantity \(\Gamma_2\) (no Lemma Y), so `cand:near-critical-square-mass` is not touched.

### After unblinding

Opened afterwards: `coordination/round-185-inflight.json`, `coordination/shared-obligations/round-185-before.json` and `coordination/drafts/round-185-dependency-assessment.json`.

- The coordinator's pre-dispatch comparison (`comparison_status: assessed`, `known_shared: []`, empty `candidate_ids_by_call`) dispatched the two calls as independent. It names `cand:slope-row-mass-x` (one-match form) as carried by the ordinary call alone and asks the ordinary report to state any power bound on \(\Gamma_2\) (`cand:near-critical-square-mass`).
- **Agreement.** My blind classification (independent) matches. BAND honoured the request: it states that no power bound on \(\Gamma_2\) is proved and Lemma Y is not used (BAND result item 6).
- **Dispatch effect:** none. No overlap was missed.

## Summary of verdicts

| Report | Main verdict | Corrections / conditions |
|---|---|---|
| BAND. Band autocorrelation | (a1) Lemma 4, (a2) Lemma 5, (a3) **Theorem 1**, (a4) **Theorem 2**, (a5) **Corollary 3**, (a6) Prop. 6 **ACCEPTED**; (a7) §5 Warren–Wheeler method statement **ACCEPTED WITH CORRECTION** (wording). Verdict "supported for \(\sup C\) and \(\sum W^{3/2}\); inconclusive for \(\max W\)" is honest. | **The headline survives.** \(\sup_{\lambda\ne1}C(\lambda)=O(p^{11/8-1/664})\), uniformly in \(\lambda\in\mathbb F_p\setminus\{0,1\}\); hence \(\sum_\xi W_\xi^{3/2},\ \mathcal E(\mu)=O(p^{43/16-1/1328})\) and one-match covariance \(O(p^{115/64-1/5312})=O(p^{1193/664})\). Same hypotheses as the accepted Round 180 bound (actual \(g=|f|^2\), \(\nu\) a probability on \(\widehat Q\) with the cap \(n\max\nu\le C_{\rm cap}\sqrt p\)); no (NC) input. Inherited inputs: Stevens–de Zeeuw Thm 4, BSG (Reiher–Schoen form) and Lemma SE inside Round 182's extraction, Round 184 Prop. 3, the Round 178/180 chain. **Correction to the Round 184 record:** "only band level sets can block the one-match improvement" (Round 184 acceptance, line 271; checkpoint) holds for the \(X\)/\(\max W\) route only, not for \(\sup C\). |
| COLD. Picard leaf inequivalence | (a1) Lemma 0, (a2) Prop. 1, (a3) Prop. 2 **ACCEPTED** (compact model); (a4) Theorem 3 **ACCEPTED** as a statement about the **depth-≤3 truncation**; (a5) Prop. 4 **ACCEPTED**; (a6) Corollary 5 **ACCEPTED** in its stated conditional form. The verdict "route retired" is **CONDITIONAL** on (H-N5) for the full compact model. | Certified: \(A_{\mathcal X}((h-h_1)_{\le3})\ge0.434571>0.3411\) and \(A_{\mathcal X}(h_{\le3})\ge0.912537>0.7499\), uniform on \(Q\times\{p\ge10^6\}\), both lifts. Full model: \(A_{\mathcal X}(h-h_1)\ge0.416286-N_5\), \(N_5\) uncertified (route needs \(N_5\ge0.0751\)). The two opposite-sign collision families are **evidence** (model-consistent, physically confirmed), as the report labels them. Retiring the per-simple route is a sound coordinator decision on this evidence; it is not a certified full-model statement. |

## 2. Report BAND: `native-claude-ordinary-prime-near-critical-band-autocorrelation-185.md`

**Sources checked by line.**
- `ordinary-mixed-row-autocorrelation-180.md` lines 1–80. This covers the unfolding to \(C^\sharp\), the line family, the determination property, the Stevens–de Zeeuw use (including the \(ab^2>n^3\) and coordinate-swap extensions), the heavy/light split at \(p^{-1/8}\), \(E^\times(m)\le C(1)^2+\sup C\,M_1^2\), the propagation table and the one-match output \(p^{1/8}\mathcal E^{1/4}M_1\).
- `native-claude-ordinary-prime-shifted-level-energy-182.md` lines 25–200. This covers (H1)–(H4), \(\mathcal N\) as a norm, Lemma S1, the verbatim Stevens–de Zeeuw quote, Lemma SE with its proof, and Proposition 3 with the two-phase extraction and its general-\((\varepsilon,\delta)\) display.
- The Round 184 slope-row-mass report, lines 60–185: the input table, Proposition 1 (i)–(v) and Proposition 3 (heavy bound valid for \(0\le\varepsilon\le1/16\), \(\delta=1/22-8\varepsilon/11\)).
- `round-184-acceptance.json`, lines 266–277.

**External sources, fetched for this audit** by a fetch subagent from the arXiv HTML renderings; the PDFs were unreadable.
- **Stevens–de Zeeuw**, arXiv:1609.06284v4 (latest, 18 Jul 2017), Theorem 4. Hypotheses: \(|A|=a\le b=|B|\), \(ab^2\le n^3\), \(n\) lines, and \(an\ll p^2\) in characteristic \(p\). Conclusion: \(I(A\times B,\mathcal L)\ll a^{3/4}b^{1/2}n^{3/4}+n\). The statement agrees with the quote in BAND §1 and in Round 182. No non-vertical hypothesis is imposed; \(\mathcal L\) is a set, so its lines are distinct. The paper defines \(\ll\) by an unspecified constant.
  - **Hypothesis at the scales used.** In Lemma 4 every level set has size \(\le G/\tau_0=O(p^{9/14})\), so \(an\le O(p^{27/14})\). In Theorem 2 (H-b), \(an\le O(p^{3/2+3/166})\). Both are \(o(p^2)\) by a power, so the condition holds for large \(p\) whatever the constant in \(\ll\).
  - The two reductions BAND inherits from Round 180 are elementary and correct (my script checks them on random sizes):
    - the case \(ab^2>n^3\), via \(I\le an\) for nonvertical lines when \(a\le b\);
    - \(a^{3/4}b^{1/2}\le(ab)^{5/8}\) for \(a\le b\).
- **Warren–Wheeler**, arXiv:2107.12286v1 (only version; Discrete Comput. Geom. 2022). Theorem 3 (\(|A||T|\ll p^2\)) and Theorem 4 (\(|B|\le p^{1/2}\); energy \(E(T)\)) agree with BAND §5's paraphrase in hypotheses and exponents. Theorem 5 concerns translates of \(xy=\pm1\), as BAND says.
- **Not fetched:** Rudnev–Wheeler arXiv:2104.10534 (BAND cites it only to say that it does not apply), and Reiher–Schoen (inherited from Round 183).

| Item | Statement | Verdict | Notes |
|---|---|---|---|
| (a1) | **Lemma 4**: for \(f_i\le g\), \(f_i\in\{0\}\cup[\tau_0,a_i]\), \((C_{\rm cap}\sqrt p/\tau_0)^3\le c_0p^2\): \(C^\sharp_\lambda[f_1..f_4]\ll\prod a_i^{1-\theta_i}(\sum f_i)^{\theta_i}+G^2\), \(\theta=5/8\) (points), \(3/4\) (lines) | **ACCEPTED** | Re-derived step by step. **Layer cake:** each admissible tuple is one incidence of the point \((Y_1,Y_3)\) with the distinct line \(\ell_{D_1,D_3}\); my script checks the identity \(C^\sharp=\sum_{t}I(\cdot)\) **exactly** for integer weights at \(p=13\)–\(41\). **Size control:** every \(U_i(t)\subseteq\{g\ge\tau_0\}\), so (SdZ) applies at every \(t\). **Jensen:** \(\int_0^a|U(t)|^\theta dt\le a^{1-\theta}(\int_0^a|U|)^\theta\) for concave \(u^\theta\) on a measure of mass \(a\). **Factorization:** the (SdZ) bound is a product over the four roles, so the 4-fold integral factorizes. **The \(+n\) term:** \(\int\!\int dt_1dt_3\le1\). With \(a_i=1\) this is exactly Round 180's \(G^{11/4}\). The gain is real: Round 180 bounded \(\int|U|^\theta\le G^\theta\), which is tight only when the weights are \(0/1\). |
| (a2) | **Lemma 5**: \(C^\sharp_\lambda[f_1..f_4]\le\prod\mathcal N(v_i)\), \(v_i(z)=f_i(1-z)\) | **ACCEPTED** | \(r=(Y-D)/(1-D)\); the relation is \(r_1=\lambda r_3\); \(1-Y=(1-r)(1-D)\) gives \(m_{ab}(r)\le c_{v_a,v_b}(1-r)\). The rest is Cauchy–Schwarz in \(r\), multiplicative Parseval and Cauchy–Schwarz in \(\chi\). For \(f=g\), \(m^\sharp(r)=c_h(1-r)\) exactly, because \(h(1)=g(0)=0\) removes \(Y,D=0\). Checked exactly: \(C^{\sharp4}\le\prod E^\times(v_i)\) for four different integer weights; \(\sup C\le X\le E^\times(h)\) for actual-type \(g=|f|^2\). |
| (a3) | **Theorem 1**: \(\sup_{\lambda\ne1}C=O(p^{11/8-1/856})\) | **ACCEPTED** | 81-term split at \(\tau_0=p^{-1/7}\), \(\tau_1=p^{-\varepsilon}\). **Step L** (65 terms; a light slot is determined by the other three, R180-det): \(\le\tau_0G^3=O(p^{19/14})\). Checked exactly: the 81 terms sum to \(C^\sharp\), and each light term is \(\le\tau_0\prod(\text{other sums})\). **Step B** (15 terms): Lemma 4 with \(a=\tau_1\) in band slots; the weakest gain is one band line role, \(p^{-\varepsilon/4}\). **Step H:** Lemma 5 gives \(\le E^\times(h_\ge)\), and the accepted Round 184 Prop. 3 heavy bound gives \(\ll p^{4\eta(\varepsilon)}\) for \(\varepsilon\le1/16\). Exact: the balance \(11/8-\varepsilon/4=15/11+24\varepsilon/11\) gives \(\varepsilon=1/214\) and \(147/107=11/8-1/856\); the first branch of \(\eta\) is inactive; neighbouring \(\varepsilon\) are worse. All constants are absolute or \(C_{\rm cap}\), and every bound is uniform in \(\lambda\). |
| (a4) | **Theorem 2**: \(\sup_{\lambda\ne1}C=O(p^{11/8-1/664})\) | **ACCEPTED** | **Layer cake** \(g_H=\int1_{S'_t}d\mu\), \(\mu=\tau_1\delta_{\tau_1}+\mathrm{Leb}|_{(\tau_1,1)}\), total mass \(\le1\); checked exactly. **Per-level Round 182 extraction**, re-read: \(B_{j,t}\) disjoint subsets of \(S'_t\) of size \(\le\sqrt p\), with Lemma SE hypotheses met (\(N\le\sqrt p\), \(V=B^{-1}\), \(B\subset\mathbb F_p\setminus\{0,1\}\)). The two phase sums re-derived: \(p^{1/3}t^{-8/3}\) and \(p^{1/3+\delta/6}t^{-5/3}\), with no log loss (geometric in \(M^{-1/6}\)); leftover \(<p^{1/2-\delta}\). **(H-a):** Lemma 5 and the triangle inequality for \(\mathcal N\) (an \(\ell^4\) norm of the Mellin transform); integration as in Round 182, fourth power. **(H-b):** \(\prod(A+L)-\prod A\) expands into nonnegative terms, each with at least one leftover slot. All slots are sets inside \(S_{\tau_1}\) of size \(\le G/\tau_1\), so (SdZ) applies. A leftover slot gives \(\le p^{(1/2-\delta)\theta}\) after integration against \(\mu\). Other slots give \(\int(G/t)^\theta d\mu\le(\tau_1^{1-\theta}+\frac1{1-\theta})G^\theta\). The \(+n\) term is \(\le G^2\), since \(\int|S'_t|d\mu=\sum g_H\le G\). Exponent table re-derived exactly: \(\varepsilon=1/166\), \(\delta\in[1/415,3/83]\subset(0,1/2]\), maximum \(114/83=11/8-1/664\). **This is the step that improves Theorem 1.** Round 182 priced the leftover by \(\mathcal N\le|S^{\rm small}|^{3/4}\), which forced \(\delta\approx1/22\); pricing it in the quadrilinear form by incidence costs only \(p^{11/8-5\delta/8}\). |
| (a5) | **Corollary 3**: \(\sum W^{3/2},\ \mathcal E(\mu)=O(p^{43/16-1/1328})\); covariance \(O(p^{115/64-1/5312})\) | **ACCEPTED** | \(E^\times(m)\le X^2+\sup C\cdot M_1^2\) (the \(\lambda=0\) term vanishes); \(68/23<27/8-\delta_C\). Cauchy–Schwarz \(\sum W^{3/2}\le(\sum W)^{1/2}(\sum W^2)^{1/2}=M_1E^\times(m)^{1/2}\). In Round 178's three sums the other two are \(p^{19/8}\) and \(p^{5/2}\log p\). Then Round 184 Prop. 1(i): \(9/8+e/4\). Equivalently (iii) with \(\varepsilon=3/8-1/664\); both give \(1193/664\). The \(\log^{1/4}p\) is harmless and not even needed, because \(e>5/2\). **This uses the Round 184 corrected output \(p^{1/8}\mathcal E^{1/4}M_1\) correctly**, with \(M_1\le G^2=O(p)\) and no (NC) value of \(M_1\). Derived rows: \(\|H_\alpha\|_2=O(p^{147/128-1/10624})\), \(\sum w|H_\alpha|^2=O(p^{179/64-1/5312})\). |
| (a6) | **Prop. 6**: \(t^k|W|^{2k}\le n\max\nu\,T_k(W)\), \(W\subseteq S_t\), \(k\ge2\) | **ACCEPTED** | Re-derived. The gain factor \((C\sqrt p/(t|W|))^{k-2}\) over Lemma S1 plus Hölder was checked through \(E^{k-1}\le|W|^{k-2}T_k\) (interpolation). Checked numerically for \(k=2,3\) on actual-type \(g\) (\(p\le73\)). No headline use, as BAND says. |
| (a7) | §5: Warren–Wheeler gives no gain for \(W_\xi\) at height one, nor for heights in \((p^{-1/48},1]\) | **ACCEPTED WITH CORRECTION** (wording) | Theorem 3 is trivial (\(N^3\)), and Theorem 4 with \(E(T)\ge|T|^2\) gives \(N^{14/5}=p^{7/5}\); both checked exactly. **Correction:** at height \(a<1\) the level sets have size \(\sqrt p/a>\sqrt p\), so Theorem 4's hypothesis \(|B|\le p^{1/2}\) fails. The "\(a<p^{-1/48}\)" computation is therefore outside the theorem's range. This strengthens the negative conclusion rather than weakening it. The Möbius-family analysis (curve distinctness, pencil, bilinear cases) agrees with Round 180 line 30. |
| (b1)–(b3) | Conditional | Honest | (b2)'s route cap \(\delta_C\le1/24\) (\(\sup C\ge p^{4/3}\) for this scheme) follows from Round 182 Prop. 4 and from Step L at the smallest admissible \(\tau_0=p^{-1/6}\). It gives covariance no better than \(7/4+1/24=43/24\) by this route. |
| (c) | Models | Honest as evidence | The table reproduces line for line (§4). As BAND says, the L/B/H split at these \(p\) tests bookkeeping, not exponents. |

**Adversarial checks with no defect found.**
1. *Hidden near-critical use:* none. Theorems 1–2 use only \(0\le g\le1\), \(\operatorname{supp}g\subseteq Q\), \(g=|f|^2\) with \(\nu\) a probability (Lemma S1) and the cap. Corollary 3 uses \(M_1\le G^2\) and the unconditional \(X=O(p^{34/23})\).
2. *Uniformity in \(\lambda\):* every bound is independent of \(\lambda\notin\{0,1\}\). Round 180's line family is distinct, nonvertical and nonhorizontal for each such \(\lambda\) (replayed exactly).
3. *Constants depending on \(p\):* none. The constants are the SdZ constant, the BSG and Lemma SE constants, \(C_{\rm cap}\), and integration constants \(\le1+1/(1-\theta)\le5\). The cuts are fixed powers of \(p\).
4. *Level-set decomposition:* \(g\) takes finitely many values, so every layer-cake integral is a finite sum. Using \(\{g>t\}\) for \(t>\tau_1\) and \(S_{\tau_1}\) for the atom is consistent with Lemma S1, which needs only \(\subseteq\{g\ge t\}\).
5. *Hypotheses of the accepted inputs at the new scales:* the Round 184 Prop. 3 range \(\varepsilon\le1/16\) contains \(1/214\). Round 182's extraction accepts any \(\delta\in(0,1/2]\). The SdZ condition holds with a power to spare.
6. *Mask:* \(C\le C^\sharp\) because \(m(r)=c_h(1-r)1_{Q\setminus\{1\}}(1-r)\le m^\sharp(r)=c_h(1-r)\). Checked exactly for all \(\lambda\) at \(p\le41\).

**Exactly what is proved (agent audit):** for the actual weight \(g=|f|^2\) of a probability \(\nu\) on \(\widehat Q\) with the accepted cap \(n\max\nu\le C_{\rm cap}\sqrt p\) (the hypotheses of the accepted Round 180 bound), and for large primes \(p\equiv1\pmod4\):
- \(\sup_{\lambda\in\mathbb F_p\setminus\{0,1\}}C(\lambda)=O(p^{11/8-1/664})\);
- \(\sum_\xi W_\xi^{3/2}=O(p^{43/16-1/1328})\);
- \(\mathcal E(\mu)=O(p^{43/16-1/1328})\);
- the matching-number-one covariance is \(O(p^{1193/664})\), where \(1193/664=115/64-1/5312\).

The inputs are inherited from accepted rounds: Stevens–de Zeeuw Theorem 4; BSG in the Reiher–Schoen form and Lemma SE (inside Round 182's extraction and Round 184 Prop. 3); and the Round 178/180 point–plane and Rudnev–Shkredov chain with the Round 184 output \(p^{1/8}\mathcal E^{1/4}M_1\).

**What is not proved:**
- \(\max_\xi W_\xi\) is not improved.
- \(X\) and the first mass are not improved.
- The one-match target \(O(p^{3/2})\) is not reached (point–plane floor \(p^{7/4}\)).
- The original theta-limit target is untouched.

**An unclaimed direct consequence, not re-derived here.** Round 180 line 72 bounds the fixed-slope first mass by \(\sum_c\Delta(a,c)=C(a)=O(p^{11/8})\) for every \(a\ne1\). Theorem 2 gives \(O(p^{11/8-1/664})\) for the same quantity. The downstream "fixed-\(a\) generic squared mass" exponent was not re-derived.

## 3. Report COLD: `native-claude-cold-prime-picard-leaf-inequivalence-185.md`

**Sources checked.**
- Round 184 audit §3 and §6.3: the per-simple price identity, Prop. C allowances \(0.3411\) and \(0.7499\), and the \(g_S\) value.
- `astra-dissipation-80.md` line 90: "injectivity of both line multiplication and transport", "positive nonpunctual transport preserves inequivalence". COLD cites "line 104" and "line 108". The statement is at line 90 of the current file. This is a citation slip only.
- The model rules as stated in the `paley-185-cold-model.py` docstring, re-implemented independently in my script.

| Item | Statement | Verdict | Notes |
|---|---|---|---|
| (a1) | **Lemma 0**: lift symmetry of the whole expansion | **ACCEPTED** | All coefficient functions are functions of \(\cos\theta\), so \(\hat b_{-k}=\hat b_k\) and so on. Fibre exchange maps \(J^k\to J^{-k}\) and commutes with the rules. The report checks \(W(-p)\) and \(c(-p)=c(p)\) for every path. |
| (a2) | **Prop. 1**: the 55,986 linear path simples (depth \(\le5\), kept ranges) are pairwise inequivalent | **ACCEPTED** (compact model, (b4), (b-Jk)) | **Independent replay:** 55,986 paths, 55,982 distinct weight data, 4 colliding classes (the same four pairs), every pair with different pre-transport data (dims 24/22), both signs \(-1\). Dimension increases strictly along every path. **Remark:** the conclusion "no opposite-sign collision in the linear chain" does **not** need the Round 80 injectivity (C2), because the 4 undecided pairs have equal signs. (C2) is needed only for the stronger statement that they are distinct. That each path object is one simple is part of the (b4) reading (Round 80 line 90). |
| (a3) | **Prop. 2**: no nonlinear depth-\(\le3\) object has the full weight data of a linear simple; opposite-sign touching mass \(\le0.002608\) (depth 1–3), \(\le0.001617\) (roots) | **ACCEPTED** (compact model, plus (b-T) and purity for (C3)) | **Independent float replay** (my own weight rules and FFT coefficients at \(t=a\), \(s^2=8\)). Object counts are 147/882/1512/336. Unsigned prices agree to \(10^{-6}\): \(Q_1\) 0.024198, \(L_SQ_1\) 0.013503, \(X_1\) 0.026803, \(C_1\) 0.000668, total 0.065172. Touching masses: 0.010629 (depth 1–3) and 0.027188 (depth 0–3). Opposite-sign masses: 0.002608 and 0.001616. The report's certified values are 0.010630, 0.027188, 0.002608 and 0.001617, outward. No equal-full-weight-data coincidence with any linear simple of depth \(\le5\). **(C3) is necessary only:** \(K\) additive and injective on non-punctual simples, semisimple pre-transport products, and union of weight data. It is used only to *subtract*, which is conservative. |
| (a4) | **Theorem 3**: \(A_{\mathcal X}((h-h_1)_{\le3})\in[0.434571,0.510376]\); \(A_{\mathcal X}(h_{\le3})\in[0.912537,1.004901]\) | **ACCEPTED** for the truncation | **Dual functional bound.** Every representation \(\sum a_jH_j\) satisfies \(\sum_M\dim M|{\rm coef}_M|\le\sum|a_j|r(H_j)\). Perturbing coordinate \(M\) by nonlinear pieces costs at most their prices. **Same-sign refinement** (0.442593): valid because coefficient real parts have determined signs and multiplicities are \(\ge0\). **Outward rounding:** lower bounds use `lower_abs` of the balls \((1-10^{-12})\) and are printed by floor; subtractions use `upper_abs` and are printed by ceiling. The parameter balls contain \(Q\times[8,8+8/(10^6-1)]\) (re-checked: \(S^2\) ball \([8-10^{-7},8+8.1\cdot10^{-6}]\)). The printed decomposition lines add to within \(\le3\cdot10^{-6}\) of the printed totals; the totals come from unrounded internal values (my script shows this). **Scope:** this is the price of the **truncation**, not of \(h-h_1\). By itself it does not decide the route. |
| (a5) | **Prop. 4**: T1 Fourier tails, T2 \(\sum_{j\ge6}P(L_S^jh_1)\le0.022598\), T3 depth-4 nonlinear 0.043795 (opposite-sign overlap 0.003542) | **ACCEPTED** | T2 is \(0.015393\times1.468064\le0.022598\) (checked exactly), with the accepted Round 184 \(g_S\). Subtracting the full tail price is conservative. T3 was replayed, not re-implemented. The report's T3 heading says "evidence" while (a5) says "certified". The numbers are outward-rounded exact enumerations of the kept ranges, so "certified for the kept ranges" is the right label. Depth-4/5 linear simples are inequivalent to depth-\(\le3\) simples by Prop. 1, so they do not touch the dual coordinates. |
| (a6) | **Corollary 5**: \(A_{\mathcal X}(h-h_1)\ge0.416286-N_5\), \(A_{\mathcal X}(h)\ge0.904816-N_5\) | **ACCEPTED** as stated (conditional form) | Survival thresholds \(N_5\ge0.0751\) and \(0.1549\) are rounded down. Recomputed from the outward-rounded *printed* components they are still \(>0.0750\) and \(>0.1548\). |
| Verdict | "Route retired" | **CONDITIONAL** on (H-N5): \(N_5<0.0751\) | The certified content is the depth-3 truncation. The full-model retirement needs \(N_5<0.0751\). The crude majorant has no fixed point. Nonlinear unsigned mass per depth does not decay (0.0242, 0.0410, 0.0438, 0.0429). Containment stops excluding anything at depth 5 (80%). So no certificate is in sight inside the weight-data model. The evidence for (H-N5) is the physical \(\ell^2\) data, the depth-4 exact overlap bound 0.0035, and the mean-field mechanism. It is fairly strong. The report states its own \(\ell^2\) blind spot: simples with small \(|c|/\dim\) carry 0.197 of 0.445. |
| §5 | Two opposite-sign collision families: \(Q_1\supseteq\) roots \(K(J^{\pm2})\) (\(-3.79\cdot10^{-5}\) per object, two objects per root, total \(-7.58\cdot10^{-5}\)); \(C_1\supseteq\) dim-3 simples of \(L_Sh_1\) | **Honest as evidence (c)**, as labelled | My replay gives the coefficients \(-3.791\cdot10^{-5}\) for \(K(J^{\pm2}\otimes K(J^k)\otimes K(J^k))\), \(k=\pm2\). The mechanism is consistent with the model: \(K(J^2)\) has weight data \(A=(-2,2)\), \(B=(0,0)\), symmetric under negation, so it can be self-dual and \(K(J^2)^{\otimes2}\supseteq\mathbf 1\). By contrast \(K(J^2)\otimes K(J^{-2})\) contains no trivial constituent (different data). Accordingly the merged off-diagonal object \(('Q',2,(-2,2))\) touches only the root \(J^4\), as the report's listing shows. Physical inner products match the predictions to about 1.4% (\(\langle h_1,Q_1\rangle\)) and 0.3% (\(\langle l_1,C_1\rangle\)) at \(p=4\cdot10^6\). Their price effect (\(\approx1.2\cdot10^{-4}\) on \(h-h_1\)) lies inside the certified subtractions. |
| Criterion | (C1)–(C3) identification | **ACCEPTED** as model statements | (C1) is invariance of weight data. (C2) is Round 80 injectivity, inherited and not re-proved; Prop. 1's sign conclusion does not need it. (C3) is a necessary condition used conservatively. "Possibly equal" merging only lowers the block price, so block prices are valid lower bounds. |

**On the mission's branches.** The mission's "supported" branch expected the model price \(A_{\mathcal X}(h-h_1)\ge0.50\) under "no opposite-sign collisions". The facts are:
- collisions exist but are tiny;
- the certified depth-3 lower bound is 0.4346, not 0.50;
- the full-model bound is conditional on \(N_5\).

The decision rule (model price above the allowance 0.3411, and \(h\) above 0.7499) is met with margin \(\ge0.093\) and \(\ge0.162\) at depth 3. **My reading:** retiring the per-simple dimension-price route is justified as a coordinator decision on certified truncation bounds plus strong evidence. It should be recorded as "retired on model evidence; full-model certificate conditional on (H-N5)", not as a certified retirement. Spending a call on certifying \(N_5\) is low value, as COLD itself says.

## 4. Replay log

Run from the repository root on 2026-11-21 with `.venv/bin/python`. "Matches" means every quoted output line or table row appears in the run output, timing text excepted. All eight report-script SHA-256 values equal those quoted in the reports.

| Script | Command | rc | Time | Result |
|---|---|---|---|---|
| band exponents | `.venv/bin/python -B research/paley-185-band-exponents.py` | 0 | <1 s | Matches; `ALL OK` |
| band exact check | `… paley-185-band-models.py --check 13 17 29 37` | 0 | <1 s | Matches; `EXACT CHECKS OK` |
| band models | `… paley-185-band-models.py 1009 4001 16001 64013 256021` | 0 | 30 s | All seven quoted §7 rows match to every digit |
| cold leaves | `… paley-185-cold-picard-leaves.py` | 0 | 4 s | Matches (all 62 quoted lines) |
| cold tails | `… paley-185-cold-tails.py` | 0 | 8 s | Matches (two lines differ only in timing text) |
| cold brute force | `… paley-185-cold-bruteforce.py` | 0 | 17 s | Matches; `BRUTE FORCE DONE` |
| cold depth-5 | `… paley-185-cold-depth5-evidence.py` | 0 | 23 s | Matches (floating) |
| cold physical Gram | `… paley-185-cold-physical-gram.py` | 0 | 67 s | Matches (floating) |
| audit band | `.venv/bin/python -B research/paley-185-audit-band-check.py` | 0 | <1 s | `ALL AUDIT CHECKS OK` (Part A exact Fractions; Part B exact integers/Fractions at \(p=13,17,29,37,41\); Part C float at \(p\le73\)) |
| audit cold | `.venv/bin/python -B research/paley-185-audit-cold-check.py` | 0 | 2 s | `ALL AUDIT CHECKS OK` (independent rules; float coefficients at one parameter point) |

Audit script SHA-256:
- `paley-185-audit-band-check.py` `f1c95aa42a90638e99cb0faccd9c17ebca63dbf3b4c5874a81eede899a29d557`
- `paley-185-audit-cold-check.py` `1f5c68d3256cd42002b7606c4ad1a7fca7c6c2b3e5b68cc49c2a615fd642039d`

**Not checked:**
- The proofs of Stevens–de Zeeuw Theorem 4, the Reiher–Schoen BSG theorem and the Rudnev–Shkredov second norm. They are inherited, and only the statement and hypotheses of SdZ Theorem 4 were re-read from source.
- Rudnev–Wheeler arXiv:2104.10534 was not fetched; BAND uses it only negatively.
- Asymptotic constants cannot be tested by small-\(p\) replays. The exact replays check the identities and inequalities each step uses, not the \(\ll\) constants.
- COLD's ball arithmetic was replayed, not re-implemented. My cold replay is float at \(t=a\), \(s^2=8\), so it confirms values, not uniformity on \(Q\).
- COLD's T3 and depth-5 enumerations were replayed only.
- The Round 80 weight calculus behind (b4), (b-Jk), (b-T), and D2–D4.
- Whether \(K(J^{\pm2})\) is self-dual in the actual sheaf setting. Only model consistency and the physical inner products support it.
- The downstream Round 176/180 fixed-\(a\) generic squared-mass exponent after Theorem 2.

## 5. Ranked closeout

### 5.1 What Round 185 changes, obligation by obligation

| Obligation | Before (Round 184 acceptance) | After Round 185 (as audited) | Effect |
|---|---|---|---|
| **One-match covariance** (target \(O(p^{3/2})\)) | \(O(p^{115/64})\), \(115/64=1.796875\). \(\sup_{\lambda\ne1}C=O(p^{11/8})\) exactly at the threshold \(\varepsilon<3/8\). "Only band level sets \((p^{-1/8},p^{-1/192})\) can block." | **\(O(p^{1193/664})\)**, \(1193/664=115/64-1/5312\approx1.796687\). \(\sup_{\lambda\ne1}C=O(p^{11/8-1/664})\). \(\sum W^{3/2},\ \mathcal E(\mu)=O(p^{43/16-1/1328})\). \(\|H_\alpha\|_2=O(p^{147/128-1/10624})\). \(\sum w|H_\alpha|^2=O(p^{179/64-1/5312})\). No (NC) input. The band does **not** block \(\sup C\): Stevens–de Zeeuw gains \(a^{1/4}\) at height \(a\). The binding pair is now the band gain against the Phase-1 BSG price at heights near 1. Route cap: \(\sup C\ge p^{4/3}\) for this scheme, i.e. covariance \(\ge p^{43/24}\). Point–plane floor \(p^{7/4}\) unchanged. | **weakened** (first exponent move since Round 180) |
| \(\max_\xi W_\xi\) (one-match variant) | \(\le X=O(p^{34/23})\). Criterion: band \(L^2\) mass \(\Lambda(p^{-\varepsilon})=O(p^{3/8-\delta})\), \(\varepsilon<1/192\). | Unchanged. Warren–Wheeler Theorems 3–4 give nothing for the Möbius family of \(W_\xi\) at the relevant scale. \(\max W\) is no longer needed for the one-match chain: \(\sup C\) gives the same covariance function. | unchanged (now redundant for one-match) |
| **First mass \(\mathcal M_w\) / \(X\)** (target \(X=O(p^{1+1/1280})\)) | \(\mathcal M_w=O(p^{11/8})\), \(X=O(p^{34/23})\); square-field method cap | Unchanged. Prop. 6 (higher-energy Lemma S1) is the only new structural input on \(g\), with no exponent effect. Fixed-slope first mass \(C(a)\), \(a\ne1\): \(O(p^{11/8})\to O(p^{11/8-1/664})\) (direct). | unchanged (one side quantity improved) |
| Support energy | Only \(n\mathcal E(\nu)-1=O(p^\gamma)\), \(\gamma<3/8\), matters | Unchanged; BAND proves no power bound on \(\Gamma_2\) | unchanged |
| **Cold growing-prefix confinement** | \(A_{\mathcal X}(h-h_1)<0.3411\) (joint) or \(A_{\mathcal X}(h)<0.7499\), uniformly on \(Q\), both lifts. Model unsigned price \(0.51\)–\(0.57\). Leaf inequivalence open. | Linear Picard chain collision-free (depth \(\le5\)). Certified model prices of the depth-3 truncation, \(\ge0.4346\) and \(\ge0.9125\), exceed both allowances. Full model \(\ge0.4163-N_5\) and \(\ge0.9048-N_5\), with \(N_5\) uncertified; the route needs \(N_5\ge0.0751\). Only mean-field collisions found, of size \(10^{-4}\). **The per-simple dimension-price route for \(h\) is retired on model evidence.** | **new obstruction** (model; full-model certificate conditional on (H-N5)) |
| Generic J sum \(O(p^{9/4})\); zero match; generic six-word class; cold complex stationary domain; derivative transfer; D2–D4; the target | open | unchanged | unchanged |

### 5.2 Precise remaining obligations

1. **One-match (ordinary).** Push \(\delta_C\) in \(\sup_{\lambda\ne1}C=O(p^{11/8-\delta_C})\) beyond \(1/664\).
   - The binding terms are Step B, \(p^{11/8-\varepsilon/4}\), and the H-a Phase-1 price \((p^{1/3}\tau_1^{-5/3})^4\).
   - Within this scheme the cap is \(\delta_C=1/24\): covariance \(p^{43/24}\).
   - Below that needs an all-heavy price below \(p^{4/3}\), without BSG size loss, or a better incidence input for Cartesian products of size \(\asymp\sqrt p\) against \(\asymp p\) lines.
   - Reaching \(O(p^{3/2})\) needs a non-point–plane input (floor \(p^{7/4}\)) and the generic six-word class below \(p^{9/2}\).
2. **First mass (ordinary).** \(X=E_Q(h)=O(p^{1+1/1280})\) via a quantitative prime-only input; unchanged. Prototype: \(E^\times(1-P_N)=O(N^{2+o(1)})\) for geometric progressions with \(N\asymp\sqrt p\).
3. **Support energy.** Only \(n\mathcal E(\nu)-1=O(p^{\gamma})\), \(\gamma<3/8\), matters; unchanged.
4. **Cold.** With the per-simple \(A\)-price route retired, the cold obligation returns to Criterion D, sup transfer, or a hybrid price.
   - The hybrid keeps the per-simple dimension price for the seed structure and prices multiplication by \(h\) through a counting or sup bound.
   - Floating \(\sup|h|\approx0.61<0.7499\); inputs are the Round 128 counting rate 0.5145 and the Round 177 rate 0.545.
   - Plus D2–D4, (b4), (b-Jk), (b-T), the uniform complex stationary domain and derivative transfer.
   - Optional: (H-N5) or (MF), for a certified full-model retirement.
5. Unchanged: generic J sum, zero-match estimate. The original target remains open.

### 5.3 Recommended Round 186 calls (most valuable first)

**1. `ordinary-prime-sup-c-heavy-price` (ordinary; the live lever on the one-match exponent).**
- **Question:** within the Round 185 three-step scheme (Steps L/B/H for \(C^\sharp_\lambda\)), how large can \(\delta_C\) in \(\sup_{\lambda\ne1}C(\lambda)=O(p^{11/8-\delta_C})\) be made? Possible routes:
  - pricing the all-heavy term \(C^\sharp_\lambda[g_H^{\otimes4}]\) directly in the quadrilinear form, not through Hölder to \(E^\times(h_\ge)\);
  - using Prop. 6 (higher energies) or a BSG variant with smaller size loss in the extraction;
  - a stronger incidence input for structured Cartesian products at size \(\asymp\sqrt p\).
  Is the scheme's cap \(4/3\) attainable?
- **Why now:** Round 185 moved the exponent for the first time since Round 180 and identified the binding pair exactly: the band gain \(\tau_1^{1/4}\) against the Phase-1 price \(p^{1/3}t^{-8/3}\). The gap to the scheme's cap (\(1/664\) vs \(1/24\)) is large.
- **Scope:** actual \(g=|f|^2\) with the cap; no (NC) unless stated and marked. Use Round 185 Lemmas 4–5 and Theorems 1–2 as accepted. Keep \(\sup C\) separate from \(X\) and \(\max W\). Quote any new external theorem from source with hypotheses at the scales used. Exact exponent arithmetic.
- **If yes** (any \(\delta_C>1/664\)): covariance \(O(p^{115/64-\delta_C/8})\), up to \(p^{43/24}\).
- **If no** (a model or argument showing the all-heavy term needs \(p^{4/3+c}\) for these inputs): the one-match line within point–plane methods stalls near \(1193/664\), and the next lever is a non-point–plane input.
- **If inconclusive:** the best \(\delta_C\) and the binding term.

**2. `cold-prime-hybrid-price` (cold; the route COLD hands back).**
- **Question:** can a hybrid price meet the Round 184 Duhamel allowance for \(h=V_{602}-S\), uniformly on \(Q\), both lifts? The hybrid keeps the per-simple dimension price for the seed iteration and bounds multiplication by \(h\) through a sup or counting norm (Round 128 rate 0.5145, Round 177 rate 0.545; floating \(\sup|h|\approx0.61\) against the seed-only allowance 0.7499).
- **Why now:** Round 185 retires, on certified depth-3 bounds plus evidence, the cheap \(A\)-price of \(h\) through its Picard expansion. That was the only alternative to a hybrid.
- **Scope:** compact model under (b4), (b-Jk), (b-T); certified outward arithmetic; state precisely which price is submultiplicative against which. D2–D4 stay inherited.
- **If yes:** a concrete certified cold criterion with a computable input.
- **If no:** the cold dimension-price programme reduces to Criterion D or sup transfer.
- **If inconclusive:** the certified gap.

**3. (Optional, coordinator-level rather than a research call) propagate Theorem 2.**
- Re-derive the Round 176/180 fixed-\(a\) generic squared-mass exponent with \(C(a)=O(p^{11/8-1/664})\).
- Restate `cand:slope-row-mass-x`: the one-match form is settled for \(\sup C\) at \(\delta=1/664\); the remaining shared estimate is the X / first-mass form only.

**Retire or do not renew:**
- **The cold per-simple dimension-price route for \(h\) through its Picard expansion** (\(A_{\mathcal X}(h-h_1)<0.3411\), \(A_{\mathcal X}(h)<0.7499\)). Record it as retired on model evidence. The full-model certificate is conditional on (H-N5), and certifying \(N_5\) is not worth a call.
- **\(\max_\xi W_\xi\) as a separate one-match target:** \(\sup C\) yields the same covariance function and is now ahead. Keep \(\max W\le X\) only inside the first-mass obligation. A Möbius-family incidence search (BAND (b3)) is not worth a call without a located theorem.
- **The "band level-set structure" framing for one-match:** the band blocks only the \(X\)/\(\max W\) route. Remove the Round 184 sentence "only band levels can block the one-match improvement" from the forward record, or scope it to \(X\).

## 6. Status of this audit

This is an agent audit, not human acceptance or certification.

**What I checked:**
- every claim the two reports label as proved;
- BAND's Lemmas 4–5, Theorems 1–2, Corollary 3 and Proposition 6, re-derived by hand, together with the accepted Round 180, 182 and 184 statements they use, read at source by line;
- Stevens–de Zeeuw Theorem 4 and Warren–Wheeler Theorems 3–5, re-read from arXiv through a fetch subagent;
- every exponent, with exact Fractions;
- the identities used in each step, replayed exactly at small \(p\);
- COLD's linear chain and depth-\(\le3\) nonlinear pieces, replayed independently with my own implementation of the model rules (float coefficients);
- all eight report scripts, re-run.

**What I did not check:** listed under "Not checked" in §4.

**Files:** nothing was committed. Only this file and the two `research/paley-185-audit-*.py` scripts were written.
