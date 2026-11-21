# Round 184 native Claude draft: the near-critical slope-row mass

- **call_id:** `ordinary-prime-near-critical-slope-row-mass` (shared estimate `cand:slope-row-mass-x`).
- **agent_label:** `session/r184-slope-row-mass` (native Claude Opus 5.5 research session, started by the Round 184 coordinator session).
- **Mission:** `coordination/missions/round-184/ordinary-prime-near-critical-slope-row-mass.md`, exported from `coordination/round-183.json` (SHA-256 `1231bfe2…f9e`).
- **Inputs read.** All ten SHA-256 values match the mission:
  - `research/round-182-acceptance.json`, `research/round-183-acceptance.json`
  - `research/native-claude-audit-183.md`
  - `research/native-claude-ordinary-prime-first-mass-fibre-dilation-183.md`
  - `research/native-claude-ordinary-prime-row-deleted-one-match-183.md`
  - `research/ordinary-prime-coset-spread-151.md`, `research/anchored-repair-20.md`
  - `research/ordinary-weighted-slope-product-incidence-178.md`
  - `research/ordinary-mixed-row-autocorrelation-180.md`
  - `research/native-claude-ordinary-prime-shifted-level-energy-182.md`

  Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-183.md`, the `proof_scope` of `research/round-151-acceptance.json`, and `research/ordinary-weighted-affine-vertical-saving-173.md` (for the priced endpoints).
- **Scripts** (all new):
  - `research/paley-184-rowmass-exponents.py`: exact Fractions.
  - `research/paley-184-rowmass-square-control.py`: exact integers and Fractions in \(\mathbb F_{r^2}\).
  - `research/paley-184-rowmass-models.py`: floating.
  - `research/paley-184-rowmass-sector-trend.py`: floating.
- **Status:** agent assessment only. It is not an audit, not human acceptance, and not a mathematical certification.

## Result summary

**Verdict: inconclusive** (mission definitions). Neither version of the question is proved or refuted for the actual near-critical \(g\). The report does, however, change what each version asks for.

1. **The max-convolution threshold is \(3/8\), not \(3/16\) (Proposition 1; proved from accepted inputs).** The accepted Rounds 178/180 route takes the affine energy to the one-match covariance as \(p^{1/8}\mathcal E(\mu)^{1/4}M_1\). With \(\max_\xi W_\xi=O(p^{1+\varepsilon})\) this gives covariance \(O(p^{7/4+\varepsilon/8}\log^{1/4}p)\), which is below \(115/64\) **iff \(\varepsilon<3/8\)**.
   - The Round 183 threshold \(\varepsilon<3/16\) (and the mission's \(7/4+\varepsilon/4\)) comes from the weaker Round 182 operator route. That route is never better once \(\mathcal E\ge p^{5/2}\).
   - The same threshold applies to Round 180's \(\sup_{\lambda\ne1}C(\lambda)\). Round 180 sits **exactly at** \(\varepsilon=3/8\) there, and that is where \(115/64\) comes from. So the one-match use of `cand:slope-row-mass-x` is: \(\max_\xi W_\xi\) or \(\sup_{\lambda\ne1}C(\lambda)\) is \(O(p^{11/8-\delta})\).
2. **Floors (Proposition 2; (NC)).** \(X\ge(2-o(1))p\), \(\max_\xi W_\xi\ge(1-o(1))p\) and \(\sup_{\lambda\ne1}C(\lambda)\ge(1-o(1))p\). The X target \(O(p^{1+1/1280})\) therefore says that \(X\) sits at its floor up to \(p^{1/1280}\).
3. **Shared structural lemma with the support-energy call (Lemma Y; any \(0\le g\le1\)).**
   \[X\le R_*M_1\le\Gamma_2M_1\le(G-1)^2\,\Gamma_2,\qquad \Gamma_2=\sum_{x\ne1}g(x)^2=n\,\mathcal E(\nu)-1 .\]
   - On (NC), \(X\le(1+o(1))\,p\,\Gamma_2\).
   - Hence \(\Gamma_2=O(p^{\gamma})\) gives the one-match improvement if \(\gamma<3/8\), and the X target if \(\gamma\le1/1280\).
   - The inequality cannot be reversed: \(g_H\) has \(\Gamma_2\asymp\sqrt p\) but \(X\ll p\log p\).
   - **Light-band refinement (Proposition 3).** Only the \(L^2\) mass of \(g\) on levels below \(p^{-\varepsilon}\), \(\varepsilon<1/192\), matters for the one-match use. All mass at levels \(\ge c\) costs at most \(p^{15/11}<p^{11/8}\).
4. **Round 151 closes Round 183's open coset subclass (Proposition 4; accepted input).** The accepted Round 151 rich-ratio bound gives \(E^\times((1-B)\setminus\{0\})\ll p\log p\) for every bounded union \(B\) of cosets of subgroups of size \(\asymp\sqrt p\).
   - So \(E_{\rm off}(H)\), \(X(g_H)\) and \(\mathcal M_w(g_H)\) are \(O(p\log p)\) for \(c\sqrt p\le|H|\le2C_{\rm cap}\sqrt p\).
   - Round 183 (Corollary C3) had \(O(p^{4/3})\) there and called the subclass open.
5. **Square-field method cap (Proposition 5; exact).** In \(\mathbb F_{r^2}\) the subfield gives the exactly critical configuration of Round 20's square control.
   - It satisfies every **field-general** near-critical input: a flat law with \(m_{\rm eff}/m_0\to1\), sector concentration with \(G_-\to1\), and Lemma S2 tight.
   - It has \(X,\ \max_\xi W_\xi,\ \sup_{\lambda\ne1}C(\lambda)\ge(1-o(1))q^{3/2}\), which is the Young bound, and \(\mathcal M_w\to0\).
   - It violates exactly the two prime-only inputs: the Round 20 energy gap and the Round 151 coset mass.
   - So any power saving for either version must use a prime-only input. The accepted (NC) forms of those inputs are qualitative (\(o(1)\), fixed constants), so the saving must come from a quantitative prime-field incidence or Stepanov input applied to the level structure.
6. **Best exponents from (NC) structure.**
   - **X version:** \(O(p^{34/23})\) unconditionally (Round 182). Conditionally, \(\min\{p^{34/23},(1+o(1))p\Gamma_2\}\).
   - **Max-convolution version:** \(\max_\xi W_\xi\le X=O(p^{34/23})\), i.e. \(\varepsilon=11/23\). The quantity that matters, \(\sum_\xi W_\xi^{3/2}\), is \(O(p^{43/16})\) (Round 180), which is exactly the \(\varepsilon=3/8\) threshold.
   - **No near-critical input moves either exponent.** The blocking level-set configurations are identified in §7.
7. **Evidence** (floating, models only).
   - No admissible flat-law model on primes gets near the near-critical branch: the best sector tightness falls from \(0.58\) at \(p=1009\) to about \(0.25\) at \(p=1.3\cdot10^5\).
   - In every flat-law model, \(X/p\le2.2\) and \(X\) stays within a factor \(2\) of its floor, with no growth in \(p\).
   - Pushing a model toward sector concentration raises the additive energy of \(S\) (up to \(0.47|S|^3\)) and the ratios \(X/\)floor, \(\max W/\)floor and \(\sup C/\)floor, but only by constant factors (up to \(1.7\), \(2.7\), \(2.1\)).

## Setup and hypotheses

Notation and normalizations are those of Rounds 171–183, with counting norms throughout.
- \(p\equiv1\pmod4\) prime, \(n=(p-1)/2\), \(Q\) the squares, \(\chi\) the Legendre symbol, \(m_0=n/\sqrt p\).
- **Law and weight.** \(\nu\) is a probability on \(\widehat Q\cong\mathbb Z/n\), \(f=\sum_j\nu_jj\) on \(Q\) (zero off \(Q\)), and \(g=|f|^2\).
  - (H1) and (H2): \(0\le g\le1\), \(g(1)=1\), \(G=\sum g\le n\max\nu\le C_{\rm cap}\sqrt p\).
  - (H4): \(w=g(1-g)\). Inversion symmetry (H3) is not used.
- **Shifted objects.** \(h(z)=g(1-z)\) and \(c_h(\kappa)=\sum_zh(z)h(\kappa z)\).
- **Slope rows.** \(m(r)=c_h(1-r)\) for \(1-r\in Q\setminus\{1\}\) and \(0\) otherwise (Round 183, Proposition A).
  - \(M_1=\sum_rm(r)\).
  - \(X=\sum_rm(r)^2=E_Q(h)=\sum_{\kappa\in Q\setminus\{1\}}c_h(\kappa)^2\).
  - \(W_\xi=\sum_rm(r)m(\xi/r)\) and \(C(\lambda)=\sum_rm(r)m(\lambda r)\), so \(C(1)=X\), \(\sum_\xi W_\xi=\sum_\lambda C(\lambda)=M_1^2\), and \(\sum_\xi W_\xi^2=\sum_\lambda C(\lambda)^2=E^\times(m)\) (Round 180, line 15).
- **Level quantities.** \(\Gamma_2=\sum_{x\ne1}g(x)^2=c_h(1)\), \(R_*=\max_{\kappa\in Q\setminus\{1\}}c_h(\kappa)\), \(S_t=\{x\ne1:g(x)\ge t\}\), and \(\Lambda(\tau)=\sum_{x\ne1,\,g(x)<\tau}g(x)^2\).

**The near-critical branch (NC)** is the hypothetical sequence of Rounds 151–154, as stated in the Round 183 row-deleted report (line 53): \(\|L_\sigma b\|_{2,n}/r\to0\) and \(m_{\rm eff}/m_0\to1\). The near-critical inputs used below, each with its source, are:

| input | statement used | source (accepted) |
|---|---|---|
| (NC-a) sector concentration | \(G_{-\rho}=O(1)\), \(G=(1+o(1))\sqrt p\), \(M_1=(1+o(1))p\), and \(\rho\sum_xg(x)\chi(1-x)=(1+o(1))\sqrt p\) (Lemma S2 tight) | Round 183 row-deleted report, Proposition 1.2 (lines 76–91), from Round 151 `ordinary-prime-coset-spread-151.md` line 41; accepted in `round-183-acceptance.json` line 264 |
| (NC-b) flat law | \(b_j^2/\sum b^2\to1_S/|S|\) in \(\ell^1\) with \(|S|=(1+o(1))m_0\), and the signed \(S\times S\) deficit is \(o(1)\) | Round 20 `anchored-repair-20.md` lines 74–76 (flattening); Round 151 line 47 |
| (NC-c) energy gap | eventually \(\mathcal E(S_\tau)<(\frac12+\Delta)|S_\tau|^3\), so \(\Gamma_2/\sqrt p=\mathcal E(S)/|S|^3+o(1)\le\frac12+o(1)\) | Round 20 lines 66–76; Round 183 Proposition 1.4 (lines 104–120); accepted in Round 183 |
| (NC-d) coset mass | the relative Fourier mass of \(f\) outside every bounded union \(B\) of cosets of subgroups of size \(\asymp\sqrt p\) is \(\ge c_0>0\) | Round 151 lines 36–39 and 47; `round-151-acceptance.json` proof scope, item 3 |
| (R151-rr) rich ratios | \(\#\{u\ne0,1:|Y\cap uY|\ge t\}\ll p/t^2\) for \(Y=(1-B)\setminus\{0\}\), \(B\) as in (NC-d), \(t\ge1\) | Round 151 line 13; proof scope, item 2 |
| Prop. 1.1 | \(\sum_xg(x)^2=n\,\mathcal E(\nu)\), \(G=n/m_{\rm eff}\) (any law) | Round 183 row-deleted report, lines 63–70 |
| Lemma S1 | \(E^\times(W)\ge t^2|W|^4/(n\max\nu)\) for \(W\subseteq S_t\) | Round 182 shifted-level report, line 100 |
| Lemma S2 | \(|\hat h(\psi)|\le\sqrt p\) for \(\psi\ne1\) | Round 182, line 108 |
| Lemma SE | \(E^\times(1-B)\ll K^{2/3}N^{8/3}\), \(N\le\sqrt p\) | Round 182, line 126; acceptance line 258 |
| Prop. 3 (R182) | \(E^\times(h)=O(p^{34/23})\) (BSG via Reiher–Schoen 2024, Theorem 1.2, as corrected in Round 183) | Round 182, line 159; acceptance line 259 |
| R178 | \(\mathcal E(\mu)\ll\sum_\xi(W_\xi^2/p+W_\xi^{3/2}+G\log p\,W_\xi)\), and the Rudnev–Shkredov second norm | `ordinary-weighted-slope-product-incidence-178.md` lines 29 and 41–62 |
| R180 | \(\sup_{\lambda\ne1}C(\lambda)=O(p^{11/8})\), \(E^\times(m)\le C(1)^2+\sup C\cdot M_1^2\), and the propagation table; one-match output \(p^{1/8}\mathcal E^{1/4}M_1\) | `ordinary-mixed-row-autocorrelation-180.md` lines 51, 58–68 and 79 |

Statements marked (NC) assume the branch. Unmarked statements hold for every \(g\) with \(0\le g\le1\) supported on \(Q\).

## 1. The one-match threshold (max-convolution version)

**Proposition 1.** Let \(G\le C\sqrt p\) and \(M_1\le Cp\) (always true, with \(M_1\le G^2\)).

- **(i)** If \(\mathcal E(\mu)\le p^e\) with \(e\ge3/2\), then the matching-number-one covariance is \(O(p^{9/8+e/4}+p^{3/2})\).
- **(ii)** If \(\max_\xi W_\xi=O(p^{1+\varepsilon})\) with \(0\le\varepsilon\le1\), then \(\mathcal E(\mu)=O(p^{5/2+\varepsilon/2}+p^{5/2}\log p)\), and the covariance is \(O(p^{7/4+\varepsilon/8}\log^{1/4}p)\).
- **(iii)** If \(\sup_{\lambda\ne1}C(\lambda)=O(p^{1+\varepsilon})\) with \(\varepsilon\ge0\), the conclusions of (ii) hold.
- **(iv)** In (ii) and (iii) the covariance is below the accepted \(O(p^{115/64})\) **if and only if \(\varepsilon<3/8\)**.
- **(v)** The Round 182 operator route gives covariance \(\le(p\,\mathcal E)^{1/2}\), i.e. \(p^{7/4+\varepsilon/4}\) in (ii), hence Round 183's threshold \(3/16\). For every \(e\ge5/2\) it is at least as large as the route in (i): the exponents differ by \(e/4-5/8\ge0\).

*Proof.*

*(i).* This is Round 178's chain, used as Round 180 uses it.
- The twisted chart gives the second norm \(\|H_\alpha\|_2\ll G^{5/8}\mathcal E^{1/8}M_1^{1/2}+M_1(1+G/\sqrt p)\), uniformly in \(t\) (R178, lines 39–57).
- Squaring and summing \(w(t)\le g(t)\) gives \(\sum w|H_\alpha|^2\le G\|H_\alpha\|_2^2\).
- The already-priced endpoints cost \(O(p^{5/2})\) (Round 173, line 61).
- Dividing by \(p\), as in Rounds 173/178/180, gives the covariance.
- With \(G=O(\sqrt p)\) and \(M_1=O(p)\), the first term is \(p^{9/8+e/4}\). This is Round 180's audit-corrected "one-match output \(p^{1/8}\mathcal E^{1/4}M_1\)" (line 79).
- The \(M_1\)-term contributes \(O(p^{5/2})\) to \(\sum w|H|^2\), and so does the endpoint term.

The exact script reproduces both accepted rows: Round 178 (\(e=11/4-3/836\to29/16-3/3344\)) and Round 180 (\(e=43/16\to115/64\), with intermediate values \(147/128\) and \(179/64\)).

*(ii).* By Round 178's inequality (line 29),
\[\mathcal E(\mu)\ll\max W\cdot M_1^2/p+(\max W)^{1/2}M_1^2+G\log p\,M_1^2,\]
using \(\sum_\xi W_\xi=M_1^2\). This gives exponent \(\max(2+\varepsilon,\ 5/2+\varepsilon/2,\ 5/2)=5/2+\varepsilon/2\) for \(\varepsilon\le1\). Then apply (i).

*(iii).* We have \(E^\times(m)=\sum_\lambda C(\lambda)^2\le C(1)^2+\sup_{\lambda\ne1}C\cdot M_1^2\) and \(C(1)=X\le p^{34/23}\) (Round 182). Since \(2\cdot34/23=68/23<3\), we get \(E^\times(m)=O(p^{3+\varepsilon})\).
- Then \(\sum W^{3/2}\le M_1E^\times(m)^{1/2}=O(p^{5/2+\varepsilon/2})\) and \(\sum W^2/p=E^\times(m)/p=O(p^{2+\varepsilon})\) (Round 180, line 58).
- Conclude as in (ii).

*(iv).* \(7/4+\varepsilon/8<115/64=7/4+3/64\iff\varepsilon<3/8\).

*(v).* The operator bound is Round 182's accepted \(k=2\) bound: covariance \(118/64\) at \(\mathcal E=p^{43/16}\). Then \((1+e)/2-(9/8+e/4)=e/4-5/8\). ∎

**Reading.**
- Round 180 proved (iii) at exactly \(\varepsilon=3/8\), and that is the source of \(115/64\). The current bound on \(\max W\) is \(\max W\le X=O(p^{34/23})\), i.e. \(\varepsilon=11/23>3/8\).
- So the correct one-match form of `cand:slope-row-mass-x` is: \(\max_\xi W_\xi=O(p^{11/8-\delta})\), or \(\sup_{\lambda\ne1}C(\lambda)=O(p^{11/8-\delta})\), or directly \(\sum_\xi W_\xi^{3/2}=O(p^{43/16-\delta})\). Each gives the covariance \(O(p^{115/64-\delta/8+o(1)})\) or better.
- This is a sharpening of Round 180's next test 2, not a new kind of estimate. The Round 183 statement "\(\varepsilon<3/16\) suffices" remains true, but it is not sharp.
- Proposition 2.5's floor remark in Round 183 is unaffected: the point–plane route cannot give \(\mathcal E(\mu)\) below \(p^{5/2}\), so this route alone can reach at best covariance \(p^{7/4+o(1)}\).

## 2. Floors on (NC)

**Proposition 2 ((NC)).**
- \(X\ge M_1^2/(n-1)=(2-o(1))p\).
- \(\max_\xi W_\xi\ge M_1^2/(p-1)=(1-o(1))p\).
- \(\sup_{\lambda\ne1}C(\lambda)\ge(M_1^2-X)/(p-2)=(1-o(1))p\).

*Proof.* Each is Cauchy–Schwarz or averaging:
- \(m\) is supported on the \(n-1\) values with \(1-r\in Q\setminus\{1\}\), and \(\sum m=M_1\).
- \(\sum_\xi W_\xi=M_1^2\) over \(p-1\) values of \(\xi\).
- \(\sum_{\lambda\ne1}C(\lambda)=M_1^2-X\) over \(p-2\) values, with \(X=O(p^{34/23})=o(p^2)\).
- Finally \(M_1=(1+o(1))p\) by (NC-a). ∎

So the X target \(O(p^{1+1/1280})\) is the statement that \(X\) is at its Cauchy–Schwarz floor up to \(p^{1/1280}\). This is a near-sharp, "random-like" multiplicative-energy statement for the shifted function \(h\).

## 3. Lemma Y: the shared input with the support-energy call

**Lemma Y (any \(0\le g\le1\) on \(Q\) with \(g(1)=1\)).**
\[X\ \le\ R_*\,M_1\ \le\ \Gamma_2\,M_1\ \le\ (G-1)^2\,\Gamma_2 ,\qquad \Gamma_2=n\,\mathcal E(\nu)-1\ \text{ for } g=|f|^2 .\]
On (NC), \(X\le(1+o(1))\,p\,\Gamma_2\).

*Proof.*
- \(X=\sum_{\kappa\in Q\setminus\{1\}}c_h(\kappa)^2\le\max_\kappa c_h(\kappa)\cdot\sum_\kappa c_h(\kappa)=R_*M_1\).
- Cauchy–Schwarz gives \(c_h(\kappa)\le\|h\|_2^2=\Gamma_2\).
- \(M_1\le(G-1)^2\) (Round 183, Proposition B).
- \(\sum_xg^2=n\,\mathcal E(\nu)\) is Round 183's Proposition 1.1, and \(g(1)^2=1\).
- On (NC), \(M_1=(1+o(1))p\). ∎

The bound \(E^\times(h)\le\max(p,(G-1)^2)\,\Gamma_2\), obtained from Lemma S2 and Parseval, is the same inequality up to the diagonal. Round 182 recorded the Young form as the light-level barrier. What is new here is the bookkeeping that links it to the support-energy call and to the corrected one-match threshold.

**Corollary Y.** Suppose \(\Gamma_2=O(p^{\gamma})\), equivalently \(\mathcal E(\nu)=O(p^{\gamma}/n)\). Then:
- \(\gamma<3/8\) gives \(\max W\le X=O(p^{1+\gamma})\), hence one-match covariance \(O(p^{7/4+\gamma/8}\log^{1/4}p)\), below \(115/64\);
- \(\gamma\le1/1280\) gives the X target, hence \(\mathcal M_w\le X/4=O(p^{1+1/1280})\) and \(\mathcal D_0+\mathcal D_1=O(p^{3/2})\) through Round 180;
- for the first mass alone, Round 183's (G2), \(\gamma\le1/4+1/2560\), is weaker and suffices directly (\(\mathcal M_w\le(G-1)\Gamma_2^2\)).

**What this does and does not give the support-energy call.**
- The support-energy call asks whether \(\mathcal E(S)=o(|S|^3)\). On (NC), \(\Gamma_2/\sqrt p=\mathcal E(S)/|S|^3+o(1)\) (Round 183, Proposition 1.4), so a qualitative \(o(1)\) yields only \(X=o(p^{3/2})\), no power.
- A power rate is needed, and it must be stated for the exact \(\Gamma_2=n\,\mathcal E(\nu)-1\) of the actual law. The \(S\)-form has an unquantified \(o(\sqrt p)\) error.
- Lemma Y is **not reversible**. In the admissible family \(g_H\), \(\Gamma_2\asymp|H|/16\asymp\sqrt p\), yet \(X\ll p\log p\) (Proposition 4). A support-energy outcome \(\mathcal E(S)\asymp|S|^3\) would therefore not refute either version here.

### Proposition 3 (light-band refinement; (H1)/(H2) with the cap, Lemma S1, BSG, Lemma SE)

For \(\tau=p^{-\varepsilon}\) with \(0\le\varepsilon\le1/16\),
\[E^\times(h)^{1/4}\ \ll\ \big((G-1)^2\Lambda(\tau)\big)^{1/4}+p^{\eta(\varepsilon)},\qquad \eta(\varepsilon)=\max\Big(\tfrac13+\tfrac53\varepsilon,\ \tfrac{15}{44}+\tfrac{6}{11}\varepsilon\Big).\]
In particular, for every fixed \(c\in(0,1]\), \(E^\times(h)\ll(G-1)^2\Lambda(c)+p^{15/11}\). Moreover, suppose \(\Lambda(p^{-\varepsilon})=O(p^{3/8-\delta})\) for some \(\varepsilon<1/192\) and \(\delta>0\). Then \(\max_\xi W_\xi\le X=O(p^{11/8-\delta'})\) with \(\delta'>0\), and the one-match covariance is below \(115/64\).

*Proof.* This is Round 182's Proposition 3 with one change: the light part is bounded by \(\Lambda(\tau)\) instead of \(\tau G\).
- \(\mathcal N=E^{\times1/4}\) is a monotone norm. Split \(h=h_<+h_\ge\) at \(g(1-z)<\tau\).
- Young: \(\mathcal N(h_<)^4\le\|h_<\|_1^2\|h_<\|_2^2\le(G-1)^2\Lambda(\tau)\).
- The heavy part is Round 182's displayed estimate, which is valid for every \(\varepsilon\): after layer cake and level-by-level BSG plus Lemma SE,
\[\mathcal N(h_\ge)\ll p^{1/3+5\varepsilon/3}+p^{1/3+2\varepsilon/3+\delta/6}+p^{3/8-3\delta/4}.\]
- Choosing \(\delta=1/22-8\varepsilon/11\ge0\) balances the last two terms at \(15/44+6\varepsilon/11\).
- At \(\varepsilon=1/192\), \(\eta=11/32\) exactly, and \(4\eta<11/8\) for \(\varepsilon<1/192\).
- All exponent identities are checked in `paley-184-rowmass-exponents.py`. ∎

**Reading.**
- Since \(\Lambda(\tau)\le\min(\Gamma_2,\tau G)\), Proposition 3 contains both Round 182's \(34/23\) (take \(\varepsilon=1/46\)) and Corollary Y's one-match part.
- For the one-match use, **all mass of \(g\) at levels \(\ge p^{-1/192}\) is harmless**, including the saturated regime \(\Gamma_2\asymp\sqrt p\) with mass at constant height. So is mass at levels \(\le p^{-1/8-\delta}\), because it contributes at most \(p^{-1/8-\delta}G\) to \(\Lambda\).
- The only obstruction is \(L^2\) mass \(\gtrsim p^{3/8}\) at levels in the band \((p^{-1/8},p^{-1/192})\). See §7.
- Proposition 3 cannot reach the X target. By Round 182's Proposition 4, its heavy part is capped at \(p^{4/3}\) because of the BSG size loss.

## 4. Round 151 closes the coset classes

**Proposition 4 (accepted input (R151-rr)).** Let \(B\subset Q\) be a union of at most \(k\) cosets \(a_iH_i\) with \(c_1\sqrt p\le|H_i|\le c_2\sqrt p\), with \(k,c_1,c_2\) fixed. Put \(Y=(1-B)\setminus\{0\}\). Then
\[E^\times(1_Y)\ll_{k,c_1,c_2}p\log p .\]
Consequences:
- if \(\operatorname{supp}g\subseteq B\cup\{1\}\), then \(X\le E^\times(h)\ll p\log p\), \(\max_\xi W_\xi\le X\), and \(\mathcal M_w\le X/4\ll p\log p\);
- for Round 183's family \(g_H\) with \(c\sqrt p\le|H|\le2C_{\rm cap}\sqrt p\) (any fixed \(c>0\)), \(E_{\rm off}(H)\ll p\log p\), so \(\mathcal M_w(g_H)=\frac3{4096}E_{\rm off}(H)\ll p\log p\) and \(X(g_H)\ll p\log p\).

*Proof.*
- \(E^\times(1_Y)=|Y|^2+\sum_{u\ne1}|Y\cap uY|^2\le|Y|^2+\sum_{j=0}^{\lceil\log_2|Y|\rceil}4^{j+1}\#\{u\ne0,1:|Y\cap uY|\ge2^j\}\).
- By (R151-rr) each dyadic term is \(O(p)\), and \(|Y|^2\le(kc_2)^2p\).
- Since \(0\le g\le1\), \(h\le1_Y\) on \(\mathbb F_p^\times\), and \(E^\times\) is monotone on nonnegative functions.
- For \(g_H\): \(c(\kappa)=\#\{(Y',D)\in(H\setminus\{1\})^2:1-Y'=\kappa(1-D)\}\le|Y\cap\kappa Y|\) with \(B=H\). Hence \(E_{\rm off}(H)\le\sum_{\kappa\ne1}c(\kappa)^2\le E^\times(1_Y)\). ∎

**Status of the coset family after this.** Round 183's Corollary C3 records \(O(p^{4/3})\) as the best bound for \(\sqrt p\le|H|\le2C_{\rm cap}\sqrt p\) and calls that subclass open. With the accepted Round 151 bound it meets the first-mass target (indeed \(O(p\log p)\)). The size ranges now stand as follows:

| subgroup size | status | input |
|---|---|---|
| \(|H|\le p^{3/8+3/10240}\) | unconditional: \(|H|^{8/3}\le p^{1+1/1280}\) | Lemma SE |
| \(|H|^2<p\) | conditional on Shkredov Theorem 6 | Round 183 C2 |
| \(c\sqrt p\le|H|\le2C_{\rm cap}\sqrt p\) | unconditional | Round 151 |

The admissible coset family is therefore **not** a counterexample anywhere. Corollary C1 of Round 183 stays a correct necessity statement: (H1)/(H2)/(H4)-only arguments must reproduce Mit'kin/Stepanov-strength shifted-coset energies. These coset configurations are excluded on (NC) by (NC-d), so Proposition 4 is about the obstruction family, not about the actual \(g\).

## 5. The square-field control: what field-general near-critical structure allows

**Proposition 5 (exact).** Let \(r\) be an odd prime and \(q=r^2\). Let \(Q\) be the squares of \(\mathbb F_q^\times\), \(n=(q-1)/2\), and \(I\le\widehat Q\) the annihilator of \(\mathbb F_r^\times\), so \(|I|=(r+1)/2\). Take \(\nu\) uniform on \(I\setminus\{0\}\) (Round 20's square control: the stationary defect is proportional to \(1_{I\setminus\{0\}}\); `anchored-repair-20.md` line 88). Then:

- **(a) The weight.** \(f=\big(\frac{r+1}2 1_{\mathbb F_r^\times}-1\big)/\frac{r-1}2\) on \(Q\), so \(g=1\) on \(\mathbb F_r^\times\) and \(g=\beta=4/(r-1)^2\) on \(Q\setminus\mathbb F_r^\times\).
  - \(G=n\max\nu=r+1=\sqrt q+1\).
  - \(m_{\rm eff}=(r-1)/2\) and \(m_{\rm eff}/m_0=r/(r+1)\to1\): the law is exactly flat.
- **(b) Sector concentration with \(\rho=+1\).** \(\mathbb F_r\setminus\{0,1\}\subseteq T_+\), because every element of \(\mathbb F_r\) is a square in \(\mathbb F_q\).
  - \(G_-=\beta\cdot\#\{x\in Q\setminus\mathbb F_r:\chi(1-x)=-1\}\), computed exactly as \(1.5,\dots,1.043\) for \(r=5,\dots,47\).
  - \(\sum g(x)\chi(1-x)=(1-o(1))\sqrt q\), so Lemma S2 is asymptotically tight.
  - The Rayleigh deficit \((2G_-+1)/G\) is \(O(q^{-1/2})\), the Round 151 rate.
- **(c) The slope-row quantities.**
  - \(X\ge(r-2)(r-3)^2\), \(\max_\xi W_\xi\ge(r-2)(r-3)^2\) and \(\sup_{\lambda\ne1}C(\lambda)\ge(r-3)^3\). All three are \((1-o(1))q^{3/2}\), the Young bound \((G-1)^2\Gamma_2\approx q^{3/2}\).
  - \(\mathcal M_w\to0\): exact values \(0.45\) and \(0.52\) at \(r=5,7\), then decreasing to \(0.10\) at \(r=23\). Every nonzero term carries at least three factors \(\beta\), and there are \(O(r^4)\) such terms, so \(\mathcal M_w=O(1/r^2)\).
- **(d) Violated inputs.** The configuration violates exactly three things:
  - the Round 20 gap, since \(\mathcal E(I\setminus\{0\})=(1-o(1))|I|^3\);
  - the Round 151 coset mass, since the relative Fourier mass outside the coset \(\mathbb F_r^\times\) is \(t_B=2/(r+1)\to0\);
  - the characteristic hypothesis of the prime-field incidence theorems (\(an\ll(\operatorname{char})^2\) in Stevens–de Zeeuw), since the sets have size \(\asymp r=\operatorname{char}\).

*Proof.*
- (a) Orthogonality: the characters in \(I\) are exactly those trivial on \(\mathbb F_r^\times\). Then \(G=(r-1)+\beta\cdot(r-1)^2/2=r+1\).
- (b) As stated.
- (c) For the subfield part \(g_0=1_{\mathbb F_r^\times}\le g\):
  - \(c_{h_0}(\kappa)=r-3\) for \(\kappa\in\mathbb F_r^\times\setminus\{1\}\) (exclude \(z=0,1,1/\kappa\)), and \(0\) otherwise.
  - Hence \(m_0(s)=r-3\) on \(s\in\mathbb F_r\setminus\{0,1\}\).
  - Counting gives \(X_0=(r-2)(r-3)^2\), \(W_1=(r-2)(r-3)^2\), and \(C(\lambda)=(r-3)^3\) for \(\lambda\in\mathbb F_r^\times\setminus\{1\}\).
  - Monotonicity in \(g\) gives the lower bounds.
- (d) \(\|1_{Q\setminus\mathbb F_r}f\|^2/\|f\|^2=\beta(r-1)^2/2/(r+1)=2/(r+1)\). ∎

`paley-184-rowmass-square-control.py` builds the configuration from the Fourier sum for \(r=5,\dots,47\). It checks the closed form \(X_0=(r-2)(r-3)^2\), \(C(1)=X\), \(\sum W=M_1^2\) and \(\max W\le X\) exactly. Selected output:

| \(r\) | \(q\) | \(G/\sqrt q\) | \(G_-\) | \(\sum g\chi(1-x)/\sqrt q\) | \(m_{\rm eff}/m_0\) | \(t_B\) | \(X/q^{3/2}\) | \(\max W/q^{3/2}\) | \(\sup C/q^{3/2}\) | Young\(/q^{3/2}\) | \(\mathcal M_w\) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 11 | 121 | 1.091 | 1.200 | 0.782 | 0.917 | 0.167 | 0.440 | 0.437 | 0.389 | 0.826 | 0.331 |
| 23 | 529 | 1.043 | 1.091 | 0.905 | 0.958 | 0.083 | 0.692 | 0.691 | 0.658 | 0.914 | 0.101 |
| 47 | 2209 | 1.021 | 1.043 | 0.956 | 0.979 | 0.042 | 0.839 | 0.839 | 0.821 | 0.958 | n/a |

**Method cap.** Any argument that proves \(X\), \(\max_\xi W_\xi\) or \(\sup_{\lambda\ne1}C(\lambda)=O(q^{3/2-\delta})\) from hypotheses this configuration satisfies is invalid. Those hypotheses include:
- (H1), (H2), (H4) and Lemmas S1/S2;
- sector concentration and the flat law with \(m_{\rm eff}\sim m_0\);
- tightness of Lemma S2;
- any field-general incidence or energy inequality.

A proof of either version must therefore use at least one of:
- (NC-c), the Round 20 gap;
- (NC-d), the Round 151 coset mass;
- an incidence or Stepanov-type theorem whose hypotheses involve the characteristic, as in Stevens–de Zeeuw, Rudnev, Mit'kin or Shkredov.

The accepted (NC) forms of (NC-c) and (NC-d) are qualitative: an energy below \(\frac12|S|^3\) eventually, and a fixed positive mass. They were obtained by contradiction and compactness. Neither supplies a power of \(p\) by itself. Every power saving available today enters through the third kind of input applied to level sets, and there the BSG size loss stops the bound (Round 182, Proposition 4).

This complements Round 183's \(g_H\) cap, which concerns (H1)/(H2)/(H4) only. The square control obeys every **near-critical** input that is field-general, yet \(X\) is maximal.

It also contrasts with the first mass. Here \(\mathcal M_w\to0\) while \(X\asymp q^{3/2}\): in the exactly critical 0/1 configuration, \(w\) is worth nothing, whereas in \(g_H\) it is worth \(3/4\). On prime (NC), however, \(\sum w=G-\sum g^2\ge(\frac12-o(1))\sqrt p\) by (NC-c), so this 0/1 escape is not available.

## 6. Evidence on primes (floating; models, not the actual optimiser)

These are admissible **flat** laws: \(\nu\) is uniform on \(S\subset\mathbb Z/n\setminus\{0\}\) with \(|S|=\operatorname{round}(m_0)\), so (H1), (H2) and (H4) hold and \(m_{\rm eff}=|S|\). The near-critical requirement left open is sector concentration. For flat laws,
\[s:=\rho\sum_{x}g(x)\chi(1-x)/\sqrt p=\rho\,|S|^{-2}\sum_{i,j\in S}k(i-j),\qquad k(d)=p^{-1/2}\sum_{x\in Q}\chi(1-x)\bar d(x)\in[-1,1],\]
so (NC-a) means \(s\to1\). This is an average-Jacobi-sum alignment of \(S-S\), i.e. a near-clique of size \(\asymp\sqrt p\) in a pseudo-random weighted Cayley graph on \(\mathbb Z/n\). The ordinary theta-limit target predicts that such sets do not exist for large \(p\).

The models (`paley-184-rowmass-models.py`) are:

| model | choice of \(S\) |
|---|---|
| `rand` | random |
| `opt` | local search on \(s\) |
| `apbest` | the progression \(a\{1..m\}\) maximizing \(s\): a Fejér kernel on a log-interval; it violates (NC-c), since its energy is \(\frac23|S|^3\) |
| `aphalf` | a random half of the best progression of length \(2m\): energy \(\approx\frac13|S|^3\), so (NC-c)-admissible; a positive mass fraction lies on a log-interval of length \(\approx\sqrt p/2\) |
| `ap+rand b` | \(A+B\), with \(A\) a progression and \(B\) random of size \(b\): mass at heights \(\approx1/b\) on a lobe of length \(\approx b\sqrt p\) |
| `coset` | subgroup control |

Selected rows (\(\rho=+1\)):

| p | model | \(s\) | \(G_{-\rho}\) | \(\mathcal E(S)/|S|^3\) | \(\Gamma_2/\sqrt p\) | \(X/p\) | \(\max W/p\) | \(\sup C/p\) | \(X/\)Young | \(X/\)floor | max \(c_h\) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1009 | rand | 0.012 | 15.1 | 0.135 | 0.102 | 0.423 | 0.225 | 0.213 | 0.141 | 1.006 | 1.15 |
| 1009 | opt | 0.563 | 6.3 | 0.271 | 0.237 | 1.006 | 0.702 | 0.634 | 0.145 | 1.339 | 5.00 |
| 1009 | apbest | 0.341 | 9.8 | 0.668 | 0.631 | 0.785 | 0.526 | 0.356 | 0.043 | 1.570 | 4.20 |
| 16001 | opt | 0.434 | 35.6 | 0.164 | 0.157 | 0.839 | 0.546 | 0.434 | 0.043 | 1.210 | 5.73 |
| 16001 | aphalf | 0.211 | 49.7 | 0.340 | 0.333 | 0.619 | 0.370 | 0.299 | 0.015 | 1.165 | 4.99 |
| 16001 | ap+rand 16 | 0.025 | 81.3 | 0.089 | 0.109 | 1.474 | 0.748 | 0.738 | 0.062 | 1.003 | 2.09 |
| 16001 | coset 64 | 0.000 | 63.0 | 0.984 | 0.980 | 0.936 | 0.470 | 0.267 | 0.008 | 1.964 | 5.03 |
| 128021 | opt | 0.245 | 134.5 | 0.015 | 0.012 | 0.555 | 0.279 | 0.277 | 0.132 | 1.000 | 1.09 |
| 128021 | apbest | 0.232 | 136.8 | 0.667 | 0.664 | 0.808 | 0.474 | 0.288 | 0.003 | 1.484 | 5.19 |
| 256021 | aphalf | 0.136 | 218.0 | 0.336 | 0.334 | 0.577 | 0.309 | 0.261 | 0.003 | 1.125 | 4.43 |
| 256021 | ap+rand 4 | 0.096 | 229.3 | 0.292 | 0.291 | 0.556 | 0.279 | 0.258 | 0.004 | 1.085 | 2.77 |

(Here `coset 64` has \(\rho=0\), i.e. no sign is optimized.)

**Sector trend** (`paley-184-rowmass-sector-trend.py`, annealing on \(s\), \(2\cdot10^5\) steps, seed 1; floors as in Proposition 2):

| p | \(\rho\) | snapshot | \(s\) | \(\mathcal E(S)/|S|^3\) | \(\Gamma_2/\sqrt p\) | \(X/p\) | \(X/\)floor | \(\max W/\)floor | \(\sup C/\)floor |
|---|---|---|---|---|---|---|---|---|---|
| 1009 | +1 | 0.3 | 0.312 | 0.152 | 0.120 | 0.519 | 1.011 | 1.081 | 1.029 |
| 1009 | +1 | best | 0.576 | 0.473 | 0.437 | 1.262 | 1.674 | 2.720 | 2.102 |
| 1009 | −1 | best | 0.582 | 0.328 | 0.294 | 1.009 | 1.304 | 1.937 | 1.595 |
| 4001 | +1 | 0.4 | 0.401 | 0.096 | 0.079 | 0.613 | 1.007 | 1.058 | 1.016 |
| 4001 | +1 | best | 0.509 | 0.178 | 0.160 | 0.974 | 1.354 | 1.746 | 1.549 |
| 16001 | +1 | best | 0.364 | 0.045 | 0.037 | 0.632 | 1.001 | 1.021 | 1.004 |
| 64013 | +1 | best | 0.278 | 0.021 | 0.017 | 0.564 | 1.000 | 1.008 | 1.001 |

**Readings** (evidence about these models only):
- **No flat-law model approaches (NC).** The best sector tightness found (local search or annealing) falls with \(p\): \(0.58\) (1009), \(0.52\) (4001), \(0.43\) (16001), \(0.28\) (64013), \(0.25\) (128021), \(0.22\) (256021). Local search and annealing are heuristics, so this is not a proof of anything, but it is consistent with the (NC) branch being vacuous, as the target predicts.
- **The slope-row quantities stay at their floors up to constants.** \(X/\)floor \(\le1.97\) (the coset control is the largest), \(X/p\le2.2\), \(\max W/p\le1.11\), \(\sup C/p\le0.93\), with no growth in \(p\). Lemma Y is very lossy in these models: \(X/\)Young falls like \(p^{-1/2}\) whenever \(\Gamma_2\asymp\sqrt p\). The square control, in contrast, attains the Young bound.
- **Pushing toward (NC) builds additive structure.** At \(p=1009\) and \(4001\) the annealer reaches \(s\ge0.5\) only with additively structured \(S\): \(\mathcal E(S)/|S|^3\) rises to \(0.18\)–\(0.47\), and at \(p=1009\) the best set is a rank-3 cube-like progression. Then \(X\), \(\max W\) and \(\sup C\) move off their floors, by factors up to \(1.7\), \(2.7\) and \(2.1\). At \(p\ge16001\) the annealer stays below \(s=0.37\), with \(S\) unstructured and all ratios within \(2\%\) of their floors. This is the square-control mechanism of Proposition 5, seen at finite \(p\) and constant strength. It is the direction in which a refutation would have to be sought; nothing here shows power growth.
- The intermediate-height model `ap+rand` with \(b=16\) (mass at heights \(\approx1/16\)) gives the largest \(X/p\) among the flat non-coset models (1.47–1.86 at \(p=8009\)–\(16001\), where \(|S|/m_0\approx0.7\)). It still stays at the floor (\(X/\)floor \(=1.003\)).

## 7. Exact remaining gap and the blocking configurations

**Targets and current values.**

| version | needed | proved | conditional |
|---|---|---|---|
| one-match (corrected) | \(\max_\xi W_\xi\) or \(\sup_{\lambda\ne1}C(\lambda)=O(p^{11/8-\delta})\), or \(\sum_\xi W_\xi^{3/2}=O(p^{43/16-\delta})\) | \(\sup C=O(p^{11/8})\) (R180), \(\max W\le X=O(p^{34/23})\) (R182) | Lemma Y with \(\Gamma_2=O(p^{3/8-\delta})\); Proposition 3 with \(\Lambda(p^{-1/192+})=O(p^{3/8-\delta})\) |
| X (first mass) | \(X=O(p^{1+1/1280})\), i.e. at the floor \(2p\) up to \(p^{1/1280}\) | \(O(p^{34/23})\) (R182) | \(\Gamma_2=O(p^{1/1280})\); Round 182 (b1), near-sharp whole-level shifted energy for \(t\ge p^{-1/2}\) |

**Blocking configuration, max-convolution version.** By Proposition 3 the only harmful mass is a band of levels:
\[\sum_{x:\ p^{-1/8}<g(x)<p^{-1/192}}g(x)^2\ \gtrsim\ p^{3/8}.\]
- A level set \(W=S_t\) in that band with \(t^2|W|\gtrsim p^{3/8}\) has, by Lemma S1, doubling only \(K=|W|^3/E^\times(W)\le C\sqrt p/(t^2|W|)\lesssim p^{1/8}\). That is the only multiplicative structure known for it.
- BSG then loses a factor \(K^{1/2}\lesssim p^{1/16}\) in size, and the leftover goes to Young. This is exactly where the \(15/11\) heavy bound degrades to \(34/23\).
- An illustrative shape: \(S=A+B\) with \(A\) a progression and \(B\) generic, \(|B|=p^\theta\), \(1/192<\theta<1/8\). Then \(g\) carries its mass at heights \(\approx p^{-\theta}\) on a log-interval lobe of length \(\approx p^{1/2+\theta}\).
  - It has \(\mathcal E(S)\approx\frac43|S|^3p^{-\theta}\), so it passes (NC-c), and it is not a coset union, so it passes (NC-d).
  - Its sector concentration is exactly the open (NC) question.
  - For this particular shape the level sets lie in a log-interval, where Corollary SE applies without BSG and gives \(X\ll p^{4/3}\). So the obstruction is one of **knowledge** (the actual band level sets are structured only through Lemma S1), not a configuration with large \(X\).

**Blocking configuration, X version.** In addition, every level, including constant height, needs whole-level near-sharp shifted energy. The prototype is a positive-mass part of \(g\) on a log-interval (or a bounded-rank multiplicative Bohr set) \(P\) of length \(\asymp\sqrt p\) inside \(T_\rho\); the `aphalf` model is (NC-c)- and (NC-d)-admissible and has this shape.
- Its \(X\) is governed by the shifted geometric-progression energy \(E^\times(1-P_N)\), \(N\asymp\sqrt p\).
- Proved: \(\ll N^{8/3}\) (Corollary SE). Observed: \(\approx3N^2\) (Round 182, (c1)). Needed: \(N^{2+o(1)}\).
- Neither (NC-c) nor (NC-d) excludes it. (NC-d) excludes coset unions only, and (NC-c) excludes only energy above \(\frac12|S|^3\); a full interval (\(\frac23\)) is excluded, a half-interval (\(\frac13\)) is not.
- Under (NC-a) such a \(P\) would be a Paley-type near-clique: \(\chi(1-x)=\rho\) on most of a geometric progression of length \(\asymp\sqrt p\). The square control (Proposition 5) is its exact field-general model, with \(X\asymp q^{3/2}\).

**Hypotheses used.** (H1), (H2) with the cap, and (H4); (NC-a)–(NC-d) where marked. External inputs enter only through accepted rounds: Stevens–de Zeeuw Theorem 4 (via Lemma SE), BSG in the Reiher–Schoen form, the PRNRW point–plane bound and the Rudnev–Shkredov second norm (via Rounds 178/180), and the Mit'kin two-subgroup inequality (via Round 151). No new external input is used. Shkredov's Theorem 6 appears only in the inherited conditional range of Proposition 4's table. No statement here proves or refutes the ordinary theta-limit target.

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved** (ordinary arguments from accepted inputs; exponent algebra checked in exact Fractions):
- (a1) Proposition 1: the covariance is \(O(p^{9/8}\mathcal E^{1/4}+p^{3/2})\). Hence \(\max_\xi W_\xi\) or \(\sup_{\lambda\ne1}C=O(p^{1+\varepsilon})\) gives covariance \(O(p^{7/4+\varepsilon/8}\log^{1/4}p)\), which improves \(115/64\) iff \(\varepsilon<3/8\). This corrects the threshold \(3/16\) of Round 183 and the mission, which comes from the weaker operator route. Round 180 sits at \(\varepsilon=3/8\).
- (a2) Proposition 2 ((NC)): the floors \(X\ge(2-o(1))p\), \(\max W\ge(1-o(1))p\) and \(\sup_{\lambda\ne1}C\ge(1-o(1))p\).
- (a3) Lemma Y (any \(g\)): \(X\le R_*M_1\le\Gamma_2M_1\le(G-1)^2\Gamma_2\), with \(\Gamma_2=n\,\mathcal E(\nu)-1\). It is not reversible (\(g_H\)).
- (a4) Proposition 3: \(E^\times(h)\ll(G-1)^2\Lambda(p^{-\varepsilon})+p^{4\eta(\varepsilon)}\). In particular all mass at levels \(\ge c\) costs at most \(O(p^{15/11})\).
- (a5) Proposition 4: \(E^\times((1-B)\setminus\{0\})\ll p\log p\) for bounded unions of cosets of subgroups of size \(\asymp\sqrt p\), from the accepted Round 151 rich-ratio bound. Hence \(E_{\rm off}(H)\), \(X(g_H)\) and \(\mathcal M_w(g_H)\) are \(O(p\log p)\) for \(c\sqrt p\le|H|\le2C_{\rm cap}\sqrt p\). This closes Round 183's Corollary C3 subclass.
- (a6) Proposition 5: the exact square-field control. It is flat, sector-concentrated and tight for Lemma S2, with \(X,\max W,\sup C\ge(1-o(1))q^{3/2}\) and \(\mathcal M_w\to0\). It violates only the prime-only inputs. Method cap: field-general (NC) arguments give no power saving for either version.

**(b) Conditional:**
- (b1) \(\Gamma_2=n\,\mathcal E(\nu)-1=O(p^{\gamma})\) with \(\gamma<3/8\) implies the one-match covariance is \(O(p^{7/4+\gamma/8+o(1)})\), below \(115/64\).
- (b2) \(\Gamma_2=O(p^{1/1280})\) implies \(X=O(p^{1+1/1280})\), hence the first-mass target and \(\mathcal D_0+\mathcal D_1=O(p^{3/2})\) (Round 180). Round 183's (G2) remains the weaker sufficient condition for the first mass alone.
- (b3) If \(\Lambda(p^{-\varepsilon})=O(p^{3/8-\delta})\) for some \(\varepsilon<1/192\), then \(X=O(p^{11/8-\delta'})\) and the one-match covariance is below \(115/64\).
- (b4) Unchanged from Round 182: whole-level near-sharp shifted energy (b1) for \(t\ge p^{-1/2}\) implies the X target.

**(c) Evidence.**
- Exact integer and rational computations of the square control for \(r\le47\). These are exact in finite fields, but they say nothing about primes beyond the method cap.
- Floating flat-law models at \(p\le256021\) and annealing trends at \(p\le64013\), described in §6.

## What would change the proof plan

- A bound \(\sum_\xi W_\xi^{3/2}=O(p^{43/16-\delta})\), via \(\max W\) or \(\sup C\) below \(p^{11/8}\), moves the one-match exponent. By Proposition 3 it is enough to control the \(L^2\) mass of \(g\) in the level band \((p^{-1/8},p^{-1/192})\), or the doubling of those level sets beyond Lemma S1.
- A **power-rate** version of the support-energy statement, \(n\,\mathcal E(\nu)=O(p^{3/8-\delta})\), moves the one-match exponent. At \(O(p^{1/1280})\) it closes X.
- An (NC)-admissible family in which \(X/\)floor grows by a power of \(p\) would refute the X version. Proposition 5 shows where it would have to come from: a prime-field analogue of the subfield, i.e. a Paley-type near-clique of geometric-progression or Bohr type of size \(\asymp\sqrt p\) in \(T_\rho\). §6 finds only constant-factor movement.

## Ranked next tests

1. **Band doubling (one-match version).** Prove a Lemma S1 improvement for level sets \(S_t\) of the actual flat law in the band \(p^{-1/8}<t<p^{-1/192}\): doubling \(p^{o(1)}\) instead of \(\sqrt p/(t^2|S_t|)\). Alternatively prove the band \(L^2\) bound \(\Lambda(p^{-1/192})=O(p^{3/8-\delta})\) from (NC). Either gives \(\max W\le X=O(p^{11/8-\delta'})\) and a one-match exponent below \(115/64\) (Proposition 3, (b3)). Equivalently, go directly at Round 180's \(\sup_{\lambda\ne1}C(\lambda)\) with a line family that sees the band structure.
2. **Power rate for the support energy (shared with the support-energy call).** Decide whether (NC) forces \(n\,\mathcal E(\nu)=O(p^{\gamma})\) for some \(\gamma<3/8\). This is the quantitative form that Lemma Y needs. A qualitative \(\mathcal E(S)=o(|S|^3)\) does not help.
3. **Shifted geometric-progression energy (X version).** Prove \(E^\times(1-P_N)=O(N^{2+o(1)})\) for log-intervals \(N\asymp\sqrt p\), or for bounded-rank multiplicative Bohr sets, ideally inside \(T_\rho\). This is the prototype blocking configuration that (NC-c) and (NC-d) leave open. Proved: \(N^{8/3}\).

## Replay

Script SHA-256 values for the quoted outputs:

| script | SHA-256 |
|---|---|
| `paley-184-rowmass-exponents.py` | `253d9e6f952a6dbcf92114e46f992b28a812df2baf8225d7b1bb56a0f35b5327` |
| `paley-184-rowmass-square-control.py` | `108136f213b164400978513e77fc9edbfb01fb787e339088f4fb4bc0b1c3fe0c` |
| `paley-184-rowmass-models.py` | `3ce9208c77e3fd125ca9ec45b997926c030984fe49bb6e62999f79b42e3743ba` |
| `paley-184-rowmass-sector-trend.py` | `f228dd36aa0be9f98cae0c8c5b76ed2ea679f7f326fb0c4433bf8b7881327c4b` |

The models and trend scripts need numpy (tested with the repository `.venv`).

The linear relation in Proposition 1(i), covariance exponent \(=9/8+e/4\), is pinned down by the two accepted data points alone. Round 178 gives \(e=11/4-3/836\mapsto29/16-3/3344\), and Round 180 gives \(e=43/16\mapsto115/64\). The slope between them is exactly \(1/4\), and the exponent script reproduces both rows.

```bash
.venv/bin/python -B research/paley-184-rowmass-exponents.py
```
(rc 0, under 1 s, standard library only.) It reproduces the accepted Round 178/180/182 rows and checks Propositions 1 and 3 and Corollary Y. The output ends:
```
max W = p^(1+eps): E = p^(5/2+eps/2), covariance p^(7/4+eps/8) (RS) vs p^(7/4+eps/4) (operator);
   improvement over 115/64 iff eps < 3/8 (RS route); the operator route needs eps < 3/16
...
heavy part with tau constant: N << p^(15/44), i.e. E^x(h_heavy) = O(p^(15/11)), 15/11 = 1.3636 < 11/8
...
ALL OK
```

```bash
.venv/bin/python -B research/paley-184-rowmass-square-control.py
```
(rc 0, about 15 s, numpy.) Default \(r=5,\dots,47\); exact \(\mathcal M_w\) for \(q\le529\). Output: the table of §5, ending with the line `checks: closed form X0 = (p-2)(p-3)^2, C(1) = X, sum_xi W_xi = M_1^2, max W <= X, f = (h 1_F - 1)/(h-1): OK`.

```bash
.venv/bin/python -B research/paley-184-rowmass-models.py 1009 2017 4001 8009 16001 32009 64013 128021 256021
```
(rc 0, about 10 s, floating, deterministic seeds.) Output: one line per model, sign and prime. §6 quotes selected rows.

```bash
for P in 1009 4001 16001 64013; do .venv/bin/python -B research/paley-184-rowmass-sector-trend.py $P 200000 1; done
```
(rc 0, a few minutes in all, floating.) Output: the sector-trend table of §6, plus the intermediate snapshots.

## Verdict

**Inconclusive** (mission definition).
- **Max-convolution version:** not decided. The question as posed (\(\varepsilon<3/16\)) is stronger than needed: the accepted Round 178/180 route improves \(115/64\) for every \(\varepsilon<3/8\) (Proposition 1). Round 180's \(\sup_{\lambda\ne1}C=O(p^{11/8})\) is exactly at that threshold, and the best bound on \(\max_\xi W_\xi\) itself is \(\le X=O(p^{34/23})\).
- **X version:** not decided. \(X\) lies between its floor \((2-o(1))p\) and \(O(p^{34/23})\).
- **What the near-critical structure gives.** Field-general (NC) inputs cannot give a power for either version (the square control, Proposition 5). The prime-only inputs are qualitative. Coset configurations are fully closed (Proposition 4). The remaining obstruction is a band of intermediate levels for the one-match use (Proposition 3) and the shifted-progression energy for the X use.
- **Shared lemma for the closeout.** Lemma Y, \(X\le(G-1)^2\,(n\,\mathcal E(\nu)-1)\), links this estimate to the support-energy call. Only a power rate on the law's additive energy transfers.
- **No refutation.** No admissible model shows power growth of \(X/p\), \(\max W/p\) or \(\sup C/p\).
