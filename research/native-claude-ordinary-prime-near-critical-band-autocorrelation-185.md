# Round 185 native Claude draft: band autocorrelation and the one-match exponent

- **call_id:** `ordinary-prime-near-critical-band-autocorrelation` (one-match form of `cand:slope-row-mass-x`).
- **agent_label:** `session/r185-band-autocorrelation` (native Claude Opus 5.5 research session, started by the Round 185 coordinator session).
- **Mission:** `coordination/missions/round-185/ordinary-prime-near-critical-band-autocorrelation.md`, exported from `coordination/round-184.json` (SHA-256 `46fb9ed1…2d4f`; the file still matches).
- **Inputs read.** All eleven SHA-256 values match the mission:
  - `research/round-183-acceptance.json`, `research/round-184-acceptance.json`
  - `research/native-claude-audit-184.md`
  - `research/native-claude-ordinary-prime-near-critical-slope-row-mass-184.md`
  - `research/native-claude-ordinary-prime-near-critical-support-energy-184.md`
  - `research/paley-184-rowmass-models.py`
  - `research/ordinary-mixed-row-autocorrelation-180.md`, `research/ordinary-weighted-slope-product-incidence-178.md`
  - `research/native-claude-ordinary-prime-shifted-level-energy-182.md`
  - `research/ordinary-prime-coset-spread-151.md`, `research/anchored-repair-20.md`

  Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-184.md`, and line 53 of `research/native-claude-ordinary-prime-row-deleted-one-match-183.md` (the (NC) definition).
- **Scripts** (both new):
  - `research/paley-185-band-exponents.py`: exact Fractions, standard library.
  - `research/paley-185-band-models.py`: `--check` mode uses exact integers; model mode uses floating point.
- **Status:** agent assessment only. It is not an audit, not human acceptance, and not a mathematical certification.

## Result summary

**Verdict: supported for \(\sup_{\lambda\ne1}C(\lambda)\) and \(\sum_\xi W_\xi^{3/2}\); not decided for \(\max_\xi W_\xi\)** (mission definitions; see the Verdict section).

1. **Theorem 2 (main).** For the actual weight \(g=|f|^2\), uniformly in \(\lambda\in\mathbb F_p\setminus\{0,1\}\):
   \[\sup_{\lambda\ne1}C(\lambda)=O\big(p^{11/8-1/664}\big).\]
   - Hypotheses: only (H1)/(H2) with the cap, through Lemma S1. **No near-critical input is used.**
   - A simpler form, Theorem 1, gives \(O(p^{11/8-1/856})\). It uses only accepted statements as black boxes.
2. **Corollary 3.**
   - \(\sum_\xi W_\xi^{3/2}=O(p^{43/16-1/1328})\) and \(\mathcal E(\mu)=O(p^{43/16-1/1328})\).
   - The matching-number-one covariance is \(O(p^{115/64-1/5312}\log^{1/4}p)\).
   - This would be the first move in the one-match exponent since Round 180.
3. **Why the band does not block \(\sup C\).** Round 184 (Proposition 3) found that the band blocks \(X\), and hence the route through \(\max W\le X\). It does not block \(\sup C\).
   - Round 180's bound \(C(\lambda)\ll G^{11/4}+G^2+p^{-1/8}G^3\) uses Jensen's inequality on every level set. Jensen is tight only when \(g\) takes the values \(0\) and \(1\).
   - For mass at height \(a\), the Stevens–de Zeeuw count gains a factor \(a^{1/4}\) or better (Lemma 4). So all band and light levels are already **below** \(p^{11/8}\) by a power.
   - The only exactly critical configuration is mass at height \(\asymp1\) in all four roles. Round 184's Proposition 3 heavy bound prices that configuration at \(p^{15/11+O(\varepsilon)}\), through the Hölder inequality \(C(\lambda)\le\prod_i\mathcal N(v_i)\) (Lemma 5).
   - The mission's premise that "only band level sets can block" is therefore correct for \(X\) and \(\max W\), but not for \(\sup C\). No structure of the band level sets beyond Lemma S1 is needed for \(\sup C\).
4. **\(\max_\xi W_\xi\) is not improved (§5).**
   - For \(W_\xi\) the curve family is a two-parameter family of Möbius hyperbolae. The available positive-characteristic bound, Warren–Wheeler Theorem 3 (quoted with hypotheses in §5), is trivial (\(N^3\)) at the scale \(N\times N\) points with \(N^2\) curves.
   - Their Theorem 4, even granting the smallest possible energy \(E(T)=|T|^2\), gives \(N^{14/5}=p^{7/5}>p^{11/8}\) at height one. A height-\(a\) gain beats \(p^{11/8}\) only for \(a<p^{-1/48}\). That leaves the levels \((p^{-1/48},p^{-1/192})\) uncovered.
   - Round 184's band criterion (Proposition 3, (b3)) stays the exact remaining condition for \(\max W\le X\).
5. **Structural input on the actual \(g\) (Proposition 6, proved, not new in kind).** A higher-energy form of Lemma S1: \(t^k|W|^{2k}\le n\max\nu\,T_k(W)\) for \(W\subseteq S_t\) and every \(k\ge2\). It is stronger than Lemma S1 plus Hölder only when \(t|W|\ll\sqrt p\). It does not move \(X\) or \(\max W\) with known tools.
6. **No power bound on \(\Gamma_2=n\,\mathcal E(\nu)-1\)** is proved. Lemma Y is not used.
7. **Evidence** (floating, flat laws with band mass, the `ap+rand` family, \(p\le256021\)):
   - \(\sup C/p\le0.75\), \(\max W/p\le0.76\) and \(X/p\le1.5\), with no growth in \(p\).
   - The band \(L^2\) mass reaches \(2p^{3/8}\) (`ap+rand b=2`, \(p=256021\)) while every slope-row quantity stays at its floor up to a constant. This agrees with Round 184.

## Setup and hypotheses

Notation and normalizations are those of Rounds 171–184, with counting norms throughout.

- **Field and law.** \(p\equiv1\pmod4\) prime, \(n=(p-1)/2\), \(Q\) the squares. \(\nu\) is the actual probability on \(\widehat Q\), \(f=\sum_\eta\nu_\eta\eta\) on \(Q\) (zero off \(Q\)), and \(g=|f|^2\).
- **(H1)/(H2).** \(0\le g\le1\), \(g(1)=1\), \(\operatorname{supp}g\subseteq Q\), and \(G=\sum_xg(x)\le n\max\nu\le C_{\rm cap}\sqrt p\) (Round 182, lines 32–38).
- **Exclusion of \(x=1\).** Every role below excludes \(x=1\). The interior exclusions of Round 171 put all coordinates in \(\mathbb F_p\setminus\{0,1\}\).
- **Slope rows.**
  - \(m(r)=\sum_b\mu(r,b)\) with \(\mu(r,b)=g(Y)g(D)\), on the chart of Round 178.
  - \(C(\lambda)=\sum_rm(r)m(\lambda r)\), \(W_\xi=\sum_rm(r)m(\xi/r)\), \(X=C(1)\), \(M_1=\sum_rm(r)\le G^2\).
  - Identities: \(\sum_\lambda C(\lambda)^2=\sum_\xi W_\xi^2=E^\times(m)\) (Round 180, line 15).
- **Shifted objects.**
  - \(h(z)=g(1-z)\) for \(z\in\mathbb F_p^\times\), so \(h\) never sees \(x=1\).
  - For \(v,v'\ge0\) on \(\mathbb F_p^\times\): \(c_{v,v'}(\kappa)=\sum_zv'(z)v(\kappa z)\), \(E^\times(v)=\sum_\kappa c_{v,v}(\kappa)^2\), and \(\mathcal N(v)=E^\times(v)^{1/4}\).
  - \(\mathcal N\) is a monotone norm on nonnegative functions (Round 182, line 48).
- **Level sets.** \(S_t=\{x\ne1:g(x)\ge t\}\), with \(|S_t|\le G/t\).

**Inputs used, each with its source.**

| input | statement | source |
|---|---|---|
| R180-rel | \(C^\sharp(\lambda)=\sum g(Y_1)g(D_1)g(Y_3)g(D_3)\) over tuples with all coordinates in \(\mathbb F_p\setminus\{0,1\}\), \(Y_i\ne D_i\), \((Y_1-D_1)(1-D_3)=\lambda(Y_3-D_3)(1-D_1)\); \(C\le C^\sharp\) (mask dropped) | Round 180, lines 18–22 |
| R180-lines | for \(\lambda\ne0,1\) the lines \(\ell_{D_1,D_3}:(1-D_3)(X-D_1)=\lambda(1-D_1)(Z-D_3)\) are distinct, nonvertical and nonhorizontal; the point \((Y_1,Y_3)\) lies on \(\ell_{D_1,D_3}\) iff the relation holds | Round 180, lines 25–28, 41–42 |
| R180-det | each of the four variables is determined by the other three on the relation | Round 180, lines 32–35 |
| SdZ4 | Stevens–de Zeeuw Theorem 4 (quoted in §1) | arXiv:1609.06284; quoted verbatim in Round 182, lines 120–122; used in Rounds 180 and 182 |
| R180-sup | \(C(\lambda)\ll G^{11/4}+G^2+p^{-1/8}G^3=O(p^{11/8})\); \(E^\times(m)\le C(1)^2+\sup_{\lambda\ne1}C\cdot M_1^2\); \(\sum W^{3/2}\le M_1E^\times(m)^{1/2}\) | Round 180, lines 45–59 |
| S1 | \(E^\times(W)\ge t^2|W|^4/(n\max\nu)\) for \(W\subseteq S_t\) | Round 182, lines 100–110 (Rounds 163/173) |
| R182-ext | single-level extraction (BSG in the Reiher–Schoen form plus Lemma SE): \(S_t=\bigsqcup_jB_{j,t}\sqcup S_t^{\rm small}\), \(|S_t^{\rm small}|<p^{1/2-\delta}\), \(\sum_j\mathcal N(1_{1-B_{j,t}})\ll p^{1/3}t^{-8/3}+p^{1/3}t^{-5/3}p^{\delta/6}\) | Round 182, lines 166–180, accepted in Round 182; general-\((\varepsilon,\delta)\) display, line 183 |
| R184-P3 | heavy part: \(\mathcal N(h_{\ge})\ll p^{\eta(\varepsilon)}\) for \(h_\ge=h\,1[g(1-z)\ge p^{-\varepsilon}]\), with \(\eta(\varepsilon)=\max(\frac13+\frac53\varepsilon,\ \frac{15}{44}+\frac6{11}\varepsilon)\), \(0\le\varepsilon\le1/16\) | Round 184 slope-row-mass report, lines 170–181; ACCEPTED (audit line 73; `round-184-acceptance.json` line 271) |
| R182-P3 | \(X\le E^\times(h)=O(p^{34/23})\) | Round 182, line 159; accepted |
| R184-P1 | \(\sup_{\lambda\ne1}C=O(p^{1+\varepsilon})\) gives \(\mathcal E(\mu)=O(p^{5/2+\varepsilon/2})\) and covariance \(O(p^{7/4+\varepsilon/8}\log^{1/4}p)\); equivalently covariance \(O(p^{9/8}\mathcal E^{1/4}+p^{3/2})\) | Round 184 slope-row-mass report, lines 90–120; ACCEPTED |
| R178 | \(\mathcal E(\mu)\ll\sum_\xi(W_\xi^2/p+W_\xi^{3/2}+G\log p\,W_\xi)\) | Round 178, lines 27–33 |

Near-critical inputs ((NC-a)–(NC-d) of Round 184, lines 69–77) are **not** used by Theorems 1–2 or Corollary 3. They appear only in the discussion of \(\max W\) and of the band (§5, §6), where each one is cited.

## 1. External input: Stevens–de Zeeuw, Theorem 4

Quoted from arXiv:1609.06284v4, exactly as in the accepted Round 182 report (lines 120–122):

> "Let \(A,B\subset\mathbb F\) be sets with \(|A|=a\), \(|B|=b\), \(a\le b\) and \(ab^2\le n^3\). Let \(\mathcal L\) be a finite set of lines of size \(n\). If \(\mathbb F\) has positive characteristic \(p\), assume \(an\ll p^2\). Then \(I(A\times B,\mathcal L)\ll a^{3/4}b^{1/2}n^{3/4}+n\)."

Here \(an\ll p^2\) means \(an\le c_0p^2\) for an absolute \(c_0>0\). The use in Round 180 (lines 37–43) adds two observations. If \(ab^2>n^3\), the same bound holds, because nonvertical lines give \(I\le an\le a^{3/4}b^{1/2}n^{3/4}\). And because the lines are nonhorizontal, the coordinates may be swapped. The combined form used below is
\[I(U_1\times U_3,\{\ell_{D_1,D_3}\}_{V_1\times V_3})\ \ll\ (|U_1||U_3|)^{5/8}(|V_1||V_3|)^{3/4}+|V_1||V_3|,\tag{SdZ}\]
valid when \(\min(|U_1|,|U_3|)\cdot|V_1||V_3|\le c_0p^2\).

No other incidence theorem is used in Theorems 1–2.

## 2. Two lemmas on the quadrilinear form

For nonnegative \(f_1,\dots,f_4\) on \(Q\setminus\{1\}\), let \(C^\sharp_\lambda[f_1,f_2,f_3,f_4]\) be the sum in R180-rel with \(g(Y_1)g(D_1)g(Y_3)g(D_3)\) replaced by \(f_1(Y_1)f_2(D_1)f_3(Y_3)f_4(D_3)\). It is linear and monotone in each slot, and \(C(\lambda)\le C^\sharp_\lambda[g,g,g,g]\). We call \(Y_1,Y_3\) the *point roles* and \(D_1,D_3\) the *line roles*.

**Lemma 4 (height gain in the incidence count).** Let \(0<\tau_0\le1\) with \((C_{\rm cap}\sqrt p/\tau_0)^3\le c_0p^2\). Let each \(f_i\) satisfy \(f_i\le g\) and \(f_i\in\{0\}\cup[\tau_0,a_i]\) pointwise, with \(a_i\le1\). Put \(\theta_i=5/8\) for the point roles and \(3/4\) for the line roles. Then
\[C^\sharp_\lambda[f_1,\dots,f_4]\ \ll\ \prod_{i=1}^4a_i^{1-\theta_i}\Big(\sum_xf_i(x)\Big)^{\theta_i}+G^2\ \le\ \prod_i a_i^{1-\theta_i}\cdot G^{11/4}+G^2 .\]

*Proof.*
- Layer cake in all four slots: \(f_i=\int_0^{a_i}1_{U_i(t)}\,dt\) with \(U_i(t)=\{f_i>t\}\), so
\[C^\sharp_\lambda[f_1,\dots,f_4]=\int\!\!\int\!\!\int\!\!\int I\big(U_1(t_1)\times U_3(t_3),\{\ell_{D_1,D_3}\}_{U_2(t_2)\times U_4(t_4)}\big)\,dt.\]
  This uses R180-rel and R180-lines: each admissible tuple is one point–line incidence, and the exclusions only remove incidences.
- Each \(U_i(t)\subseteq\{g\ge\tau_0\}\) has size at most \(G/\tau_0\le C_{\rm cap}\sqrt p/\tau_0\). So the hypothesis of (SdZ) holds for every \(t\).
- By (SdZ), the integrand is \(\ll(|U_1||U_3|)^{5/8}(|U_2||U_4|)^{3/4}+|U_2||U_4|\).
- Jensen on \([0,a_i]\) (concavity of \(u\mapsto u^{\theta}\)) gives \(\int_0^{a_i}|U_i(t)|^{\theta_i}dt\le a_i^{1-\theta_i}\big(\int_0^{a_i}|U_i(t)|\,dt\big)^{\theta_i}=a_i^{1-\theta_i}(\sum f_i)^{\theta_i}\).
- The \(+n\) term integrates to at most \(\sum f_2\sum f_4\le G^2\), since \(\int_0^{a_1}\!\int_0^{a_3}dt\le1\).
- Finally \(\sum f_i\le G\). ∎

With \(a_i=1\) this is Round 180's heavy bound \(G^{11/4}\), and Jensen is tight there only for 0/1 weights. **The gain \(a^{1/4}\) (line role) or \(a^{3/8}\) (point role) for mass at height \(\le a\) is the slack in Round 180 that this report uses.**

**Lemma 5 (Hölder bound).** Put \(v_i(z)=f_i(1-z)\) for \(z\ne0\). Then
\[C^\sharp_\lambda[f_1,f_2,f_3,f_4]\ \le\ \prod_{i=1}^4\mathcal N(v_i).\]

*Proof.*
- The relation says \(r_1=\lambda r_3\) with \(r_i=(Y_i-D_i)/(1-D_i)\). So \(C^\sharp_\lambda=\sum_{r}m_{12}(\lambda r)\,m_{34}(r)\), where \(m_{ab}(r)=\sum f_a(Y)f_b(D)\) over \(Y\ne D\) in \(\mathbb F_p\setminus\{0,1\}\) with \((Y-D)/(1-D)=r\).
- Since \(1-Y=(1-r)(1-D)\), writing \(z=1-D\) gives \(m_{ab}(r)\le\sum_{z}v_b(z)v_a((1-r)z)=c_{v_a,v_b}(1-r)\). Here \(r\ne1\), because \(Y\ne1\).
- Cauchy–Schwarz in \(r\) gives \(C^\sharp_\lambda\le\|c_{v_1,v_2}\|_2\|c_{v_3,v_4}\|_2\), using that \(r\mapsto\lambda r\) is a bijection.
- By multiplicative Parseval, \(\|c_{v,v'}\|_2^2=\frac1{p-1}\sum_\chi|\hat v(\chi)|^2|\hat v'(\chi)|^2\le\mathcal N(v)^2\mathcal N(v')^2\), by Cauchy–Schwarz in \(\chi\). ∎

In particular \(C^\sharp_\lambda[f,f,f,f]\le E^\times(v)\). For \(f=g\) this is \(C(\lambda)\le X\le E^\times(h)\).

`paley-185-band-models.py --check 13 17 29 37` verifies the following exactly (integers), for random integer weights and every \(\lambda\notin\{0,1\}\):
- the brute-force quadrilinear sum equals the row formula;
- \(m_{ab}\le c_{v_a,v_b}\);
- \((C^\sharp_\lambda)^4\le\prod_iE^\times(v_i)\);
- the line family is injective.

## 3. The theorems

Fix \(\tau_0=p^{-1/7}\). Then \((C_{\rm cap}\sqrt p/\tau_0)^3=C_{\rm cap}^3p^{27/14}\le c_0p^2\) for large \(p\). Fix \(\tau_1=p^{-\varepsilon}\) with \(0<\varepsilon\le1/16\). Split
\[g=g_L+g_B+g_H,\qquad g_L=g\,1[g<\tau_0],\quad g_B=g\,1[\tau_0\le g<\tau_1],\quad g_H=g\,1[g\ge\tau_1].\]
By multilinearity, \(C^\sharp_\lambda[g,g,g,g]\) is the sum of the \(81\) terms \(C^\sharp_\lambda[g_{c_1},\dots,g_{c_4}]\) with \(c_i\in\{L,B,H\}\).

**Step L (some role light).** If some \(c_i=L\), the term is at most \(\tau_0G^3\), by R180-det: the light variable is determined by the other three. The \(65\) such terms cost \(O(p^{3/2-1/7})=O(p^{19/14})\).

**Step B (no light role, some band role).** Apply Lemma 4 with \(a_i=\tau_1\) in the band slots and \(a_i=1\) in the heavy slots. A band line role gains \(\tau_1^{1/4}\) and a band point role gains \(\tau_1^{3/8}\). So each of these \(15\) terms is \(\ll p^{-\varepsilon/4}G^{11/4}+G^2=O(p^{11/8-\varepsilon/4})\).

**Step H (all heavy).** This is the single term \(C^\sharp_\lambda[g_H,g_H,g_H,g_H]\).

### Theorem 1 (simple form; accepted inputs as black boxes)

For the actual \(g\) under (H1)/(H2), uniformly in \(\lambda\in\mathbb F_p\setminus\{0,1\}\),
\[C(\lambda)\ \ll\ p^{11/8-\varepsilon/4}+p^{4\eta(\varepsilon)}+p^{19/14}\qquad(0<\varepsilon\le1/16).\]
At \(\varepsilon=1/214\) both leading terms equal \(p^{147/107}\), so
\[\sup_{\lambda\ne1}C(\lambda)=O(p^{11/8-1/856}).\]

*Proof.* Steps L and B are above. For Step H, Lemma 5 gives \(C^\sharp_\lambda[g_H^{\otimes4}]\le E^\times(v_H)\), where \(v_H(z)=g_H(1-z)=h_\ge(z)\) for \(z\ne0\). R184-P3 gives \(E^\times(h_\ge)\ll p^{4\eta(\varepsilon)}\). At \(\varepsilon=1/214\) the second branch of \(\eta\) is active: \(4\eta=\frac{15}{11}+\frac{24}{11}\cdot\frac1{214}=\frac{147}{107}=\frac{11}8-\frac1{856}\). Exact arithmetic is in `paley-185-band-exponents.py`. ∎

### Theorem 2 (refined form)

Under the same hypotheses,
\[\sup_{\lambda\ne1}C(\lambda)=O(p^{11/8-1/664}).\]

*Proof.* Steps L and B are as before, now with \(\varepsilon=1/166\). For Step H we re-open R182-ext and price its leftover by incidence instead of by Young's inequality.

*Layer cake on the heavy part.* \(g_H=\int1_{S'_t}\,d\mu(t)\), where \(\mu=\tau_1\delta_{\tau_1}+\mathrm{Leb}|_{(\tau_1,1)}\), \(S'_{\tau_1}=S_{\tau_1}\), and \(S'_t=\{g>t\}\) for \(t>\tau_1\). The total mass of \(\mu\) is at most \(1\), and \(|S'_t|\le G/t\).

*Decomposition.* For each \(t\) use R182-ext with a parameter \(\delta\in(0,1/2]\): \(1_{S'_t}=A_t+L_t\), with \(A_t=\sum_j1_{B_{j,t}}\) and \(L_t=1_{S_t^{\rm small}}\), \(|S^{\rm small}_t|<p^{1/2-\delta}\). Expanding \(C^\sharp_\lambda[g_H^{\otimes4}]\) multilinearly in the four slots and in \(t_1,\dots,t_4\) gives two kinds of terms.

- *(H-a) all four slots structured.* By Lemma 5 and the triangle inequality for \(\mathcal N\),
\[\int\!\!\cdots\!\!\int\prod_i\mathcal N(A_{t_i}(1-\cdot))\,d\mu^{\otimes4}\le\Big(\int\sum_j\mathcal N(1_{1-B_{j,t}})\,d\mu(t)\Big)^4\ll\big(p^{1/3+5\varepsilon/3}+p^{1/3+2\varepsilon/3+\delta/6}\big)^4 .\]
  The integration of R182-ext over \([\tau_1,1]\), and the atom at \(\tau_1\), are exactly as in Round 182, line 183.
- *(H-b) some slot leftover.* Each slot is \(A_t\), \(L_t\) or \(1_{S'_t}\) (re-combining as convenient), all of them sets inside \(S_{\tau_1}\), of size at most \(G/\tau_1\). (SdZ) applies to every \(4\)-tuple of such sets. Integrating against \(d\mu^{\otimes4}\):
  - a leftover point slot contributes \(\int|L_t|^{5/8}d\mu\le p^{(1/2-\delta)5/8}\);
  - a leftover line slot contributes \(p^{(1/2-\delta)3/4}\);
  - any other slot contributes at most \(\int(G/t)^{\theta}d\mu\le(1+\frac1{1-\theta})G^\theta\);
  - the \(+n\) term contributes \(\le(\int|S'_t|d\mu)^2\le(2G)^2\).

  So each of these \(15\) terms is \(\ll p^{11/8-5\delta/8}+p\). The point slot is the worse case, since \(5/8<3/4\).

Collecting all the exponents:

| term | exponent | at \(\varepsilon=1/166\), \(\delta=1/415\) |
|---|---|---|
| L | \(19/14\) | \(11/8-1/56\) |
| B | \(11/8-\varepsilon/4\) | \(11/8-1/664\) |
| H-a, Phase 1 | \(4/3+20\varepsilon/3\) | \(11/8-1/664\) |
| H-a, Phase 2 | \(4/3+8\varepsilon/3+2\delta/3\) | \(11/8-239/9960\) |
| H-b | \(11/8-5\delta/8\) | \(11/8-1/664\) |

Any \(\delta\in[1/415,3/83]\) works. The maximum is \(11/8-1/664\) (exponent script). ∎

**Remarks.**
- The binding pair is the band gain \(\tau_1^{1/4}\) against the Phase-1 BSG price \(p^{1/3}t^{-8/3}\) of Round 182. Any improvement of Lemma S1 or of the BSG loss at heights near \(1\) raises the admissible \(\varepsilon\) and so \(\delta\). By Round 182's Proposition 4 (method cap \(p^{4/3}\) for the heavy route) and Step B, this route cannot go below \(\max(4/3,\ 11/8-\varepsilon/4)\). So it cannot do better than \(11/8-1/24\) even with perfect inputs at the heavy levels.
- **Consistency with the square-field cap** (Round 184, Proposition 5). Both char-dependent inputs (SdZ, and Lemma SE inside R182-ext) fail in \(\mathbb F_{r^2}\) for sets of size \(\asymp r\). The theorem therefore does not contradict the cap. It is exactly a "quantitative prime-only input applied to the level structure", as Proposition 5 requires.
- **No (NC) input is used.** The bound holds for every admissible law with the cap, on or off the near-critical branch.

### Corollary 3 (propagation)

With \(\sup_{\lambda\ne1}C=O(p^{11/8-\delta_C})\) and \(\delta_C=1/664\) (or \(1/856\) from Theorem 1):
- \(E^\times(m)\le X^2+\sup_{\lambda\ne1}C\cdot M_1^2=O(p^{3+3/8-\delta_C})\), since \(X^2=O(p^{68/23})\) (R182-P3) and \(68/23<27/8\).
- \(\sum_\xi W_\xi^{3/2}\le M_1E^\times(m)^{1/2}=O(p^{43/16-\delta_C/2})=O(p^{43/16-1/1328})\).
- \(\mathcal E(\mu)=O(p^{43/16-1/1328})\) (R178; the other two sums are smaller).
- One-match covariance \(O(p^{115/64-\delta_C/8}\log^{1/4}p)=O(p^{1193/664}\log^{1/4}p)\), with \(115/64-1/5312=1193/664\) (R184-P1 (iii), with \(\varepsilon=3/8-\delta_C\)).
- Theorem 1 alone gives \(\sum W^{3/2}=O(p^{43/16-1/1712})\) and covariance \(O(p^{115/64-1/6848})\).

The other entries of the Round 180 propagation table move accordingly: \(\|H_\alpha\|_2=O(p^{147/128-\delta_C/16})\) and \(\sum w|H_\alpha|^2=O(p^{179/64-\delta_C/8})\), by the same linear chain. The one-match target \(O(p^{3/2})\) remains far away. The point–plane floor \(p^{7/4}\) (Round 183 row-deleted report, (2.5b), line 235; Round 184 slope-row-mass report, line 126) still applies to this route.

## 4. What the band question becomes

| quantity | before (accepted) | now | status |
|---|---|---|---|
| \(\sup_{\lambda\ne1}C(\lambda)\) | \(O(p^{11/8})\) (R180) | \(O(p^{11/8-1/664})\) | proved here (Theorem 2); no (NC) |
| \(\sum_\xi W_\xi^{3/2}\) | \(O(p^{43/16})\) (R180) | \(O(p^{43/16-1/1328})\) | proved here (Corollary 3) |
| \(\max_\xi W_\xi\) | \(\le X=O(p^{34/23})\) (R182) | unchanged | open; Round 184 (b3) remains the criterion |
| one-match covariance | \(O(p^{115/64})\) | \(O(p^{115/64-1/5312+o(1)})\) | proved here (Corollary 3) |

The three quantities are kept separate as the mission asks. The covariance improvement comes from \(\sup C\), through \(E^\times(m)\) and \(\sum W^{3/2}\). It does not come from \(\max W\).

## 5. \(\max_\xi W_\xi\): why the same argument does not apply

\(W_\xi=\sum_rm(r)m(\xi/r)\) unfolds to the relation \((Y_1-D_1)(Y_3-D_3)=\xi(1-D_1)(1-D_3)\). The three possible "point" coordinate pairs behave as follows:
- **\((Y_1,Y_3)\):** the curve for \((D_1,D_3)\) is the Möbius graph \(Y_3=\frac{D_3Y_1+\xi(1-D_1)(1-D_3)-D_1D_3}{Y_1-D_1}\). Its determinant is \(-\xi(1-D_1)(1-D_3)\ne0\), and the normalized entries \((a,d)=(D_3,-D_1)\) show that the curves are distinct.
- **\((Y_1,D_1)\):** the relation is linear, but the line depends on \((Y_3,D_3)\) only through \(r_3\). It is a pencil, which carries no incidence gain.
- **\((Y_1,D_3)\) and \((D_1,D_3)\):** these contain bilinear terms (for \(\xi\ne1\)), so they are not lines.

This matches Round 180, line 30.

**External input checked: Warren–Wheeler.** Source: *Incidences of Möbius transformations in \(\mathbb F_p\)*, arXiv:2107.12286v1, Discrete Comput. Geom. (2022). The statements are paraphrased from the arXiv HTML rendering; the theorem numbers, hypotheses and exponents are as in the source.
- *Theorem 3.* If \(|A||T|\ll p^2\), then for any set \(T\) of Möbius transformations, \(I(A\times B,T)\ll|A|^{4/5}|B|^{3/5}|T|^{4/5}+|A|^{6/5}|B|^{7/5}|T|^{1/5}+|T|\).
- *Theorem 4.* If \(|B|\le p^{1/2}\), then \(I(A\times B,T)\ll|A|^{1/2}|B|^{7/10}|T|^{3/5}E(T)^{1/10}+|B|^{1/2}|T|\), with \(E(T)=\#\{f_1f_2^{-1}=f_3f_4^{-1}\}\).
- Rudnev–Wheeler (arXiv:2104.10534v1, Theorems 1.3–1.4) and Warren–Wheeler Theorem 5 treat translates of one fixed hyperbola \(xy=\lambda\). Our family has \(\lambda=\xi(1-D_1)(1-D_3)\), which varies with the curve, so it is not covered.

At the relevant scale \(|A|=|B|=N\asymp\sqrt p\), \(|T|=N^2\):
- Theorem 3 gives \(N^3\), the trivial bound.
- Theorem 4 with the smallest conceivable \(E(T)=|T|^2\) gives \(N^{14/5}=p^{7/5}>p^{11/8}\).
- With all four roles at height \(a\) (mass \(\sqrt p\)), the Theorem 4 count is \(p^{7/5}a^{6/5}\). That is below \(p^{11/8}\) only for \(a<p^{-1/48}\).
- R184-P3 covers only \(a\ge p^{-1/192}\) below \(p^{11/8}\). So even an ideal \(E(T)\) leaves the levels \((p^{-1/48},p^{-1/192})\) uncovered.

(Exponent script, last block.) No positive-characteristic incidence theorem we know of gives Stevens–de Zeeuw strength \(N^{11/4}\) for this family. The \(\max W\) version therefore still needs Round 184's criterion (b3), \(\Lambda(p^{-\varepsilon})=O(p^{3/8-\delta})\) for some \(\varepsilon<1/192\), or a new hyperbola incidence bound.

## 6. Structural input on the actual \(g\): higher-energy Lemma S1

**Proposition 6 (any law with the cap).** For \(t>0\), \(W\subseteq S_t\) and every integer \(k\ge2\),
\[t^k|W|^{2k}\ \le\ n\max\nu\cdot T_k(W)\ \le\ C_{\rm cap}\sqrt p\;T_k(W),\]
where \(T_k(W)=\#\{x_1\cdots x_k=y_1\cdots y_k\}\) in \(Q\). The case \(k=2\) is Lemma S1.

*Proof.*
- Take unit \(e_x\) with \(e_xf(x)=|f(x)|\ge\sqrt t\), and put \(F(\eta)=\sum_{x\in W}e_x\eta(x)\). Then \(\sqrt t|W|\le\sum_\eta\nu_\eta|F(\eta)|\).
- Hölder with exponent \(2k\), and \(\sum\nu=1\), give \(\le(\max\nu\sum_\eta|F(\eta)|^{2k})^{1/2k}\).
- By orthogonality, \(\sum_{\eta\in\widehat Q}|F(\eta)|^{2k}\le nT_k(W)\). ∎

*Reading.* Lemma S1 plus Hölder (\(T_k\ge E^{k-1}/|W|^{k-2}\)) gives \(t^{2k-2}|W|^{3k-2}/(C\sqrt p)^{k-1}\). Proposition 6 is stronger by the factor \((C\sqrt p/(t|W|))^{k-2}\). That factor is \(\ge1\), and it is large only when the level set carries mass \(t|W|\ll\sqrt p\). In the band configuration that blocks \(X\) (band \(L^2\) mass \(\gtrsim p^{3/8}\), Round 184 §7), the gain is at most a factor \(p^{(1/8+o(1))(k-2)}\) at the lowest band heights. With known tools (BSG for \(T_k\), Lemma SE), the extraction of R182-ext is still limited by its size loss (Round 182, Proposition 4). So Proposition 6 does not move \(X\) or \(\max W\). It is recorded as the large-spectrum (Chang-type) structure the mission asked about: band level sets are large spectra of \(\nu\), and all their known structure is multiplicative energy of every order. No power bound on \(\Gamma_2\) was found.

**Near-critical inputs and the band (for the record).** On (NC):
- the band level sets are large-spectrum sets of a flat support \(S\) of size \((1+o(1))m_0\) ((NC-b), Round 20 lines 74–76; Round 151 line 47);
- they lie mostly in one square class of \(1-x\) ((NC-a), Round 183 Proposition 1.2, accepted at `round-183-acceptance.json` line 264);
- they are not bounded coset unions ((NC-d), Round 151 lines 36–47).

None of these is quantitative, and none is needed for Theorems 1–2.

## 7. Evidence (floating; flat-law models with band mass, not the actual optimiser)

`paley-185-band-models.py` builds flat laws \(\nu=1_S/|S|\) as in Round 184:
- `ap+rand b`: \(S=A+B\), \(A\) an arithmetic progression of length \(\approx m_0/b\) maximizing sector alignment (\(\rho=+1\)), \(B\) random of size \(b\);
- `aphalf`;
- `rand`.

For each model it reports \(\sup C\), \(\max W\), \(X\), \(\sum W^{3/2}\), the band mass, and the split of \(C(\lambda)\) into the L/B/H classes of §3, the latter both at the theorem's cut \(\tau_1=p^{-1/214}\) and at \(\tau_1=1/2\).

Selected rows. Here bandL1 is the fraction of \(G\) at band heights, and \(\Lambda\) is the band \(L^2\) mass. The last four columns are at \(\tau_1=1/2\).

| p | model | bandL1 | \(\Lambda/p^{3/8}\) | \(X/p\) | \(\max W/p\) | \(\sup C/p\) | \(\sup C/p^{11/8}\) | \(\sum W^{3/2}/p^{43/16}\) | H/p | B/p | L/p | \(E^\times(h_H)/p\) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 16001 | ap+rand 2 | 0.653 | 1.410 | 0.747 | 0.437 | 0.321 | 0.0085 | 0.0259 | 0.030 | 0.078 | 0.216 | 0.391 |
| 16001 | ap+rand 16 | 0.004 | 0.005 | 1.485 | 0.754 | 0.744 | 0.0197 | 0.1036 | 0.000 | 0.000 | 0.744 | 0.000 |
| 64013 | ap+rand 2 | 0.672 | 1.626 | 0.656 | 0.344 | 0.270 | 0.0042 | 0.0165 | 0.019 | 0.084 | 0.167 | 0.352 |
| 256021 | aphalf | 0.295 | 0.937 | 0.579 | 0.310 | 0.260 | 0.0024 | 0.0126 | 0.008 | 0.007 | 0.247 | 0.210 |
| 256021 | ap+rand 2 | 0.704 | 1.976 | 0.653 | 0.336 | 0.265 | 0.0025 | 0.0129 | 0.021 | 0.094 | 0.151 | 0.377 |
| 256021 | ap+rand 4 | 0.558 | 1.187 | 0.558 | 0.282 | 0.259 | 0.0024 | 0.0126 | 0.001 | 0.042 | 0.216 | 0.033 |
| 256021 | rand | 0.000 | 0.000 | 0.496 | 0.249 | 0.248 | 0.0023 | 0.0120 | 0.000 | 0.000 | 0.248 | 0.000 |

(H, B and L are the suprema over \(\lambda\ne1\) of each class separately. Their sum need not equal \(\sup C\).)

**Readings** (about these models only):
- Band mass above \(p^{3/8}\) occurs (\(\Lambda/p^{3/8}\) rises \(1.41\to1.63\to1.98\) along `ap+rand b=2`). Yet \(X\), \(\max W\) and \(\sup C\) stay within constant factors of \(p\), with no growth. This confirms Round 184's remark that (b3) is sufficient but far from necessary for \(X\).
- In every model the all-heavy term is a small part of \(\sup C\), and \(E^\times(h_H)\le0.4p\). At these \(p\) the classes are numerically dominated by \(L\), because \(\tau_0=p^{-1/7}\ge0.17\) is not small. The split illustrates the bookkeeping but does not test the exponents.
- No model gives evidence against Theorem 2 or for growth of \(\max W/p\). These are floating computations at finite \(p\) and cannot test an exponent \(1/664\).

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved here** (ordinary arguments from accepted inputs; exponent algebra in exact Fractions; identities checked exactly at \(p\le37\)):
- (a1) Lemma 4: height gain \(\prod a_i^{1-\theta_i}\) in the Round 180 incidence count, for weights in \(\{0\}\cup[p^{-1/7},a_i]\).
- (a2) Lemma 5: \(C^\sharp_\lambda[f_1,\dots,f_4]\le\prod_i\mathcal N(v_i)\).
- (a3) Theorem 1: \(\sup_{\lambda\ne1}C=O(p^{11/8-1/856})\), from R180 and R184-P3 as black boxes.
- (a4) Theorem 2: \(\sup_{\lambda\ne1}C=O(p^{11/8-1/664})\), re-using R182-ext with the leftover priced by (SdZ).
- (a5) Corollary 3: \(\sum_\xi W_\xi^{3/2}\) and \(\mathcal E(\mu)=O(p^{43/16-1/1328})\); one-match covariance \(O(p^{115/64-1/5312}\log^{1/4}p)\).
- (a6) Proposition 6: \(t^k|W|^{2k}\le n\max\nu\,T_k(W)\) on level sets, for all \(k\ge2\).
- (a7) §5 (method statement): Warren–Wheeler Theorems 3–4 give no gain for \(W_\xi\) at height one, and none for heights in \((p^{-1/48},1]\) even with ideal \(E(T)\).

Hypotheses for (a1)–(a6): (H1)/(H2) with the cap. No (NC) input is used. External inputs: Stevens–de Zeeuw Theorem 4 (§1). Inherited through accepted rounds: BSG in the Reiher–Schoen form and Lemma SE (inside R182-ext and R184-P3), the PRNRW point–plane bound and the Rudnev–Shkredov second norm (inside R178/R184-P1).

**(b) Conditional:**
- (b1) Unchanged from Round 184 (b3): \(\Lambda(p^{-\varepsilon})=O(p^{3/8-\delta})\) for some \(\varepsilon<1/192\) gives \(\max W\le X=O(p^{11/8-\delta'})\).
- (b2) Any improvement of the Phase-1 price \(p^{1/3}t^{-8/3}\) at heights near \(1\) raises \(\delta_C\). The route is capped at \(\sup C=O(p^{4/3})\) (\(\delta_C\le1/24\)), by Round 182's Proposition 4 and Step L.
- (b3) An incidence bound of strength \(N^{11/4}\) (with the analogous height gain) for Cartesian products against the two-parameter Möbius family of §5 would give \(\max W=O(p^{11/8-\delta})\) by the same three-step argument.

**(c) Evidence:** exact integer checks at \(p=13,17,29,37\); floating flat-law models at \(p\le256021\) (§7).

## Remaining gap

- **\(\max_\xi W_\xi=O(p^{11/8-\delta})\):** open. It needs (b1) or (b3). The band \((p^{-1/8},p^{-1/192})\) is the obstruction exactly as Round 184 stated, now **only** for this version.
- **One-match target \(O(p^{3/2})\):** far away. The covariance is now \(p^{1193/664+o(1)}\approx p^{1.7967}\). The point–plane route floor is \(p^{7/4}\), and the generic six-word class and zero-match estimate are unchanged.
- **X version / first mass:** unchanged (\(O(p^{34/23})\)). No power bound on \(\Gamma_2\).
- **Review needed.** The result is an agent draft. An auditor should check:
  - the multilinear bookkeeping (81 terms);
  - the use of R182-ext's per-level statements inside the quadrilinear expansion;
  - the (SdZ) hypothesis \(an\le c_0p^2\) at \(\tau_0=p^{-1/7}\).

## Replay

| script | SHA-256 |
|---|---|
| `research/paley-185-band-exponents.py` | `27472f8dba15fe323a7818b99e4386fd51887742073cb01d6f7840901e4ceeb3` |
| `research/paley-185-band-models.py` | `efbd54959e3329b27edfb4e13d25bedc5a47daf6bda8dc3619a7ce85951fdabc` |

```bash
.venv/bin/python -B research/paley-185-band-exponents.py
```
Exact Fractions, standard library, under 1 s. It reproduces Round 180's balance and checks the (SdZ) hypothesis at \(\tau_0=p^{-1/6},p^{-1/7}\). It also checks Theorem 1 (\(\varepsilon=1/214\Rightarrow11/8-1/856\)), Theorem 2 (\(\varepsilon=1/166\), \(\delta\in[1/415,3/83]\Rightarrow11/8-1/664\)), Corollary 3 and the Warren–Wheeler exponents. The output ends `ALL OK`.

```bash
.venv/bin/python -B research/paley-185-band-models.py --check 13 17 29 37
```
Exact integers, under 1 s. The output ends `EXACT CHECKS OK`.

```bash
.venv/bin/python -B research/paley-185-band-models.py 1009 4001 16001 64013 256021
```
Floating, numpy, deterministic seeds, a few minutes. It prints the table of §7.

## What would change the proof plan

- **If an audit accepts Theorem 2:** the accepted one-match exponent moves from \(115/64\) to \(115/64-1/5312\). The shared estimate `cand:slope-row-mass-x` (one-match form) is then settled for \(\sup C\) and \(\sum W^{3/2}\), and remains open only for \(\max W\).
- **Larger \(\delta_C\):** a better heavy-level price (Lemma S1 in a higher-energy BSG, or a level-set input without BSG size loss) feeds Theorem 2 directly.
- **The \(\max W\) line:** it now needs either the band \(L^2\) bound (b1) or a Möbius-family incidence bound (b3). The latter is an incidence-geometry question independent of \(g\).

## Ranked next tests

1. **Audit Theorem 2 and Corollary 3** (multilinear split, re-use of R182-ext, (SdZ) hypothesis). If accepted, record the new one-match exponent \(1193/664\).
2. **Optimize the heavy price** within the same scheme. The binding pair is the band gain \(\tau_1^{1/4}\) against the Phase-1 price \(p^{1/3}t^{-8/3}\). The route's own ceiling is \(\delta_C=1/24\) (sup C at \(p^{4/3}\)).
3. **\(\max W\):** look for a Cartesian-product incidence bound for the family \((x-a)(y-b)=\xi(1-a)(1-b)\) (two parameters, varying \(\lambda\)). Alternatively, prove (b1) from the band structure, using Proposition 6 as the available multiplicative input.

## Verdict

**Supported** (mission definition: "for some \(\delta>0\)") **for \(\sup_{\lambda\ne1}C(\lambda)\) and for \(\sum_\xi W_\xi^{3/2}\):**
- \(\sup_{\lambda\ne1}C=O(p^{11/8-1/664})\) and \(\sum_\xi W_\xi^{3/2}=O(p^{43/16-1/1328})\);
- one-match covariance \(O(p^{115/64-1/5312+o(1)})\);
- proved from accepted inputs plus Stevens–de Zeeuw Theorem 4, with no near-critical hypothesis.

**Inconclusive for \(\max_\xi W_\xi\):** the best value is still \(\le X=O(p^{34/23})\). The blocking configuration is band-level \(L^2\) mass \(\gtrsim p^{3/8}\) in \((p^{-1/8},p^{-1/192})\), together with the absence of a Stevens–de Zeeuw-strength incidence bound for the Möbius family of \(W_\xi\).

This is an agent draft awaiting audit. It does not prove or refute the ordinary theta-limit target.
