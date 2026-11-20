# Independent audit of Round 182 (session/r182-audit)

- **Auditor:** Claude Opus 5.5 side session `session/r182-audit`. This is an agent audit, not human acceptance and not a mathematical certification. The auditor wrote none of the three reports and is not the coordinator.
- **Read:** `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-181.md`, the three missions in `coordination/missions/round-182/`, and the sources each report cites where a check needed them:
  - Rounds 169, 171, 173, 177, 178 and 180 (ordinary);
  - Round 80 `astra-dissipation-80.md` lines 82–112, Round 180 `cold-growing-prefix-delocalization-180.md`, and `native-claude-cold-prime-delocalization-price-181.md` / `native-claude-audit-181.md` §3.1 (cold).
- **External theorem:** Stevens–de Zeeuw, arXiv:1609.06284v4. Theorem 4 was read in the arXiv HTML rendering of v4 through a fetch subagent.
- **Blind review:** `coordination/shared-obligations/`, `coordination/drafts/` and `coordination/round-182-inflight.json` were not opened before the blind overlap section below was written. They were not opened afterwards either.
- **Files written:** this file; `research/paley-182-audit-shifted-energy-check.py`, `research/paley-182-audit-opnorm-check.py` and `research/paley-182-audit-cold-check.py`.

Verdict key:
- **CONFIRMED:** the proof is correct as written, for the stated hypotheses.
- **CONFIRMED-WITH-CORRECTION:** true after the stated correction, which does not change the main conclusion.
- **GAP:** a step is missing or unsupported.
- **ERROR:** the statement is false as written.

## Summary

| Report | Main verdict | ERROR / GAP |
|---|---|---|
| 1. One-match operator norm | (a1)–(a3), (a5), (a6) CONFIRMED; (a4), (a7) CONFIRMED-WITH-CORRECTION. "Inconclusive, sharpened criterion" is honest. | None. Two label corrections: (a4) is conditional on (H_sat); (a7) is a method comparison. One replay-note correction: peak memory is about 500 MB, not 140 MB. |
| 2. Shifted level energy | (a1)–(a7) CONFIRMED, (a8) CONFIRMED-WITH-CORRECTION. **The 8/3 lemma and \(E^\times(h)=O(p^{34/23})\) are CONFIRMED.** Stevens–de Zeeuw Theorem 4 is quoted correctly, its hypotheses hold for these sets, and the exponent arithmetic is correct and optimal for this bookkeeping. This is a genuine improvement of the Round 177 input 36/13. It does not improve \(\mathcal M_w\) (34/23 > 11/8), and the report says so. | None in (a). Corrections: (a8) is a bookkeeping statement for one scheme, not a theorem about all BSG arguments. The BSG input (Schoen form) was not re-checked against its paper by the report or by this audit; it is accepted from Rounds 163/173/177. |
| 3. Cold signed non-seed price | (a1), (a5), (a6) CONFIRMED; (a3), (a4) CONFIRMED-WITH-CORRECTION; (a2) ERROR (minor, numerical). "Inconclusive" is honest. | **(a2) ERROR (minor, numerical):** the "exact bracket" \(\kappa^*\in[0.7741471,0.7741472]\) is wrong in the 7th digit. The true value is \(\kappa^*=0.77414706\ldots\), below the printed lower end, because the script prints certified lower bounds rounded to nearest. The same holds for \(p_0=10^{-3},10^{-6}\). Corrections: Corollary 2.2 needs \(C_S\ge1\). In "What survives", the seed-only higher Taylor part (crude 0.104) also has to fit in the 0.2416 budget, which cuts the h-linear allowance to \(\rho A(h)\lesssim1.09\), not 1.925. |

Blind overlap: no two reports reduce to a genuinely shared estimate at the same hypotheses and scale. There is an exact identity linking reports 1 and 2 (§4): they share one object, but they need different estimates of it, in opposite directions. Report 3 is disjoint from both.

---

## 1. Report: `native-claude-ordinary-prime-one-match-operator-norm-182.md`

**Inherited objects checked against sources.**
- The chart \(r=(Y-D)/(1-D)\), \(b=D(1-Y)/(Y(1-D))\), its injectivity, \(r,b\notin\{0,1\}\) and the physical mask \(b\in Q\) match Round 171 (`ordinary-affine-line-energy-171.md` lines 14–17). The report's equivalent \(\chi(1-Y)=\chi(1-D)\) follows from \(b=(D/Y)u^{-1}\).
- "\(\mu(r,b)=g(Y)g(D)\) with the square mask and all interior exclusions of Round 171" is Round 178 line 3 verbatim.
- \(H_k\) carries \(1_{s\ne1}\): Round 169 line 11.
- The positive upper \(0\le H_\alpha\le F_\mu h_t\) with \(h_t(e)=g(t/e)\) is Round 178 line 57.
- \(\sum_\xi W_\xi=M_1^2\): Round 178 line 18.
- The Rudnev–Shkredov route: Round 178 lines 39–57.

| Item | Statement | Verdict | Notes |
|---|---|---|---|
| (a1) | \(S(t)=M_1^2G^2/p+\|\pi(\mu)h_t^\circ\|^2\) | CONFIRMED | \(F_\mu\mathbf 1=M_1\mathbf 1\) and \(F_\mu\) preserves \(\mathbf 1^\perp\); \(\sum_e h_t=G\) for \(t\ne0\). Audit check O5 verifies it for every \(t\) at four primes with \(g=|f|^2\). |
| (a2) | \(\operatorname{tr}((\pi\pi^*)^k)=pT_k-T_k^\times(m)\); \(k=1\) HS; \(k=2\) fibrewise variance | CONFIRMED | Re-derived: \(\operatorname{tr}U_h\) is \(p\), 1 or 0, and the slope is a homomorphism. The regular-representation decomposition (\(p-1\) characters and \(\pi\) with multiplicity \(p-1\)) gives the same formula. \(k=2\): \(p\sum\Delta^2-\sum_aC(a)^2=p\sum_{a,c}(\Delta-C/p)^2\). Audit check O2 compares singular values of \(\pi\) with group-convolution \(T_k\), which is independent of the report's trace computation (\(k=1,2,3\), four primes). |
| (a3) | Kernel geometry: fixed point \(D/Y\), fibre equation, \(K(1,x)=g(1/x)n(1/x)\), diagonal, conic determinant, entry/row/column bounds | CONFIRMED | Fibre equation and degeneracy re-derived by hand. Determinant \(-(x-y)(1-y)/4\) verified exactly (O6). The report's C5 brute force covers only \(x\ne0\); the determinant covers \(x=0\). |
| (a4) | Row-one lower bound; Corollary 4′ under (H_sat) | CONFIRMED-WITH-CORRECTION | The inequality is correct (O3 checks the row formula and the bound). The second display drops the factor \((1-1/p)^{-1}\); it stays valid because \(\|\pi\|^2\ge0\). **Label correction:** "b1′ is exact at exponent 3/4" and "every moment criterion is at its floor" are proved only under (H_sat) (\(\sum g^2\asymp\sqrt p\) and square-class balance). Neither is known for the actual \(g\). The summary's heading "(a)" should carry "under (H_sat)". |
| (a5) | Prop. 5: weighted sum \(\le2G^7/p+2\sigma_R^2G\sum g^2\); \(\sigma_3\le\sigma_R\le\sigma_1\); \(|\sigma_R-\|RK_{\rm irr}\||\le G\) | CONFIRMED | Interlacing via a 3-dimensional subspace and 2 linear conditions is correct. O4 checks all three numerically. |
| (a6) | \(\|\pi\|=O(p^{59/64})\), covariance \(118/64>115/64\); point–plane limit \(p^{1/8}M_1^{3/4}\); \(pT_3\ge M_1^6/(p-1)\); \(\operatorname{tr}_3=O(p^{177/32})\) | CONFIRMED | Arithmetic verified (O7). The Hölder step uses \(\sum_\xi W_\xi=M_1^2\) (R178). \(T_3=\sum_h\lambda(h)^2\ge M_1^6/(p(p-1))\) is correct. |
| (a7) | Optimal \(\mathcal E\) in the R178 Rudnev–Shkredov route gives \(S\ll p^{17/8}\), covariance \(p^{13/8}\) | CONFIRMED-WITH-CORRECTION | Arithmetic: \(|U|^{5/8}\mathcal E^{1/8}M_1^{1/2}=p^{17/16}\). This agrees with the accepted R180 statement. It is a comparison of two specific bounds (a method statement), not a theorem that no other \(k=2\) route exists. |
| (b1″), (b1‴), (b-k3) | Conditional criteria | Honest; implications CONFIRMED | (b1‴): \(2G^7/p+2\sigma_R^2G\sum g^2=O(p^{5/2})\) iff \(\sigma_R^2\sum g^2=O(p^2)\). Next-test threshold \(\eta<57/64\) verified. |
| (c) | Four 0/1 models, power iteration | Honest as evidence | Replay output is identical to the report's table, all 20 model rows. The models are not the actual optimiser, as the report says. |

Mission compliance: re-proves the R181 splitting and HS identity in full; states which energy each moment equals and what the one-dimensional representations remove; reports exponents exactly; lists the majorized weights. The refutation branch is answered correctly: the obstruction found is a saturation of b1′, not a refutation.

## 2. Report: `native-claude-ordinary-prime-shifted-level-energy-182.md` (checked with particular care)

### 2.1 The external theorem

Stevens–de Zeeuw, arXiv:1609.06284v4, Theorem 4 (Section 1.3), as printed in v4:
- **Hypotheses:** "Let A,B⊂F be sets with |A|=a, |B|=b, a≤b and ab²≤n³. Let L be a finite set of lines of size n. If F has positive characteristic p, assume an≪p²."
- **Conclusion:** "I(A×B,L)≪a^{3/4}b^{1/2}n^{3/4}+n."
- **Constants:** \(\ll\) means an absolute constant (§1.1). The proof removes vertical lines first, at cost at most \(ab\).

The report's quotation matches this statement. The numbering is right: the Cartesian-product theorem is Theorem 4, and the main \(m^{11/15}n^{11/15}\) theorem is Theorem 3.

### 2.2 Hypotheses for the sets of Lemma SE

- Points \(B\times VB\) with \(a=N\le b=|VB|=KN\). Since \(|VB|\ge|B|\), we have \(a\le b\).
- Lines \(\ell_{u,v}:Z=v(uX+1-u)\). They are non-vertical, and \((u,v)\mapsto\) (slope, intercept) is injective because slope + intercept \(=v\ne0\). So \(\mathcal L\) is a set of \(n=tN\) distinct lines.
- \(ab^2\le n^3\iff K^2\le t^3\). The case \(t<K^{2/3}\) is kept separately. Correct.
- \(an=N^2t\le N^4/h\le p^2/h\le c_0p^2\) once \(h\ge1/c_0\), using \(t\le N^2/h\) (from \(\sum_um(u)=N^2\)) and \(N\le\sqrt p\). Correct.
- Incidences: each row solution \((x,y)\) of \(u\) and each \(v\) gives the incidence \(((x,vy),\ell_{u,v})\), and these are injective. So \(I\ge hNt\). Correct.
- \(hNt\le C_1(K^{1/2}N^2t^{3/4}+tN)\Rightarrow t\le16C_1^4K^2N^4/h^4\) for \(h\ge2C_1\). Correct.
- Energy split at \(H=\max(H_0,K^{2/3}N^{2/3})\) gives \(\ll K^{2/3}N^{8/3}\). Re-derived term by term (audit Part 1).
- \(B\subset\mathbb F_p\setminus\{0,1\}\) ensures \(u\ne0\) and \(1-x\ne0\). Correct.

**Verdict on Lemma SE: CONFIRMED.** It improves Round 177's \(K^{16/13}N^{36/13}\) (`ordinary-shifted-energy-four-factor-diagonal-177.md` line 12–18). That lemma has the same hypotheses: \(B\subset\mathbb F_p^\times\setminus\{1\}\), \(N\le\sqrt p\), \(|B/B|=KN\), the same as Lemma SE with \(V=B^{-1}\). Both exponents are smaller: \(8/3<36/13\) and \(2/3<16/13\).

### 2.3 Exponent arithmetic of Proposition 3

- **BSG and price per point.** BSG gives \(|B_j|\gg m_jK_j^{-1/2}\) and \(|B_j/B_j|\ll K_j^4|B_j|\). Lemma SE with \(K=K_j^4\) then gives a price per point \(\ll K_j^{5/6}m_j^{-1/3}\ll Q_0^{5/6}m_j^{-7/6}\).
- **Phase 1:** \(p^{1/3}t^{-8/3}\). **Phase 2:** \(p^{1/3}t^{-5/3}p^{\delta/6}\). **Leftover:** \(p^{3/8-3\delta/4}\). **Light part:** \(p^{3/8-\varepsilon/4}\).
- At \(\varepsilon=1/46\), \(\delta=1/138\) the four norm exponents are 17/46, 289/828, 17/46 and 17/46. Hence \(E^\times(h)=O(p^{68/46})=O(p^{34/23})\).
- The audit's grid search over \((\varepsilon,\delta)\) finds no better value: the optimum is \(0.369625\ge17/46=0.369565\). So the chosen parameters are optimal for this bookkeeping.
- Lemma S1 (hereditary energy) is re-derived correctly and applies to \(M_j\subseteq S_t\subset Q\).
- \(m_j\le\lfloor\sqrt p\rfloor\) meets Lemma SE's \(N\le\sqrt p\).
- The triangle inequality for \(\mathcal N=E^{\times1/4}\) holds because it is the \(\ell^4\) norm of the Mellin transform. Layer cake is a finite sum. Correct.

### 2.4 Verdict table

| Item | Statement | Verdict | Notes |
|---|---|---|---|
| (a1) | Row-pair reformulation, vacuous masks, \(s=1\iff P=P'\), \(Y/D\) injective, \(\mathcal M_w\le\frac14(E_Q-\mathrm{diag})\le\frac14E^\times(h)\) | CONFIRMED | Re-derived. Audit Part 2 checks it exactly at \(p=53,61\) (primes the report did not use), with independent code and **no inversion symmetry**. This confirms (H3) is not needed. |
| (a2) | Multiplicative Fourier form; trivial frequency \(O(p^{45/46})\) | CONFIRMED | \(\bar\chi(s)=\bar\chi(A/C)\chi(Y/D)\) gives \(|F_\kappa|^2\). Parseval uses (iii). \(\sum_\kappa\sum_P\mu^2\le\Gamma_2^2\). \(1/2+34/23-1=45/46\). |
| (a3) | Lemma S1 | CONFIRMED | Jensen and orthogonality on \(\widehat Q\). This is the R163/R173 statement. |
| (a4) | Lemma S2, \(|\sum g(x)\chi(1-x)|\le\sqrt p\) | CONFIRMED | Nonnegative expansion of \(|f|^2\) and the lift \(1_Q\eta=\frac12(\psi_0+\psi_0\lambda)\); Jacobi sums have modulus 1 or \(\sqrt p\). Audit Part 4 is consistent (ratios 0.03–0.11). The remark that Young's inequality is at least as good is correct. |
| (a5) | Lemma SE \(E^\times(1-B)\ll K^{2/3}N^{8/3}\) | **CONFIRMED** | §2.1–2.2. |
| (a6) | Corollary SE (log-intervals; subsets of small cosets) | CONFIRMED | \(V P\subseteq\{\theta^j:|j|<N\}\) and \(VB\subseteq H\). Requires \(P\not\ni1\), which is stated. |
| (a7) | \(E^\times(h)=O(p^{34/23})\) | **CONFIRMED** | §2.3. Caveat carried from the report: the BSG form (\(|B|\gg mK^{-1/2}\), \(|B/B|\ll K^4|B|\), Schoen's theorem) is cited as the accepted input of Rounds 163/173/177 (R177 line 48 uses exactly this form). Neither the report nor this audit re-read the paper. Consequences: the squared \(r\)-row mass is \(O(p^{34/23})\). \(\mathcal M_w\) is **not** improved (34/23 > 11/8), and the report says so. The R178/179 downstream exponents that used \(3/2-3/418\) were not re-derived, and the report says so. |
| (a8) | Method cap \(E^\times(h)\gtrsim p^{4/3}\) for BSG + Young | CONFIRMED-WITH-CORRECTION | The formula \(\varepsilon=(3/8-\beta/8)/(2a+1/4)\) and the values 1/46 and 1/6 are verified. **Correction:** this is a statement about one parametrized scheme: pieces of size \(\le\sqrt p\), Phase-1 cost, and Young below a single cut \(\tau\). It is not a theorem about every BSG-based argument. The "Exact remaining gap" sentence "no argument that passes through BSG pieces and Young can go below \(p^{4/3}\)" should be narrowed accordingly. |
| (b1) | Per-level near-sharp energy for \(t\ge p^{-1/2}\) gives \(\mathcal M_w=O(p^{1+1/1280})\) | Honest; implication CONFIRMED | Young below \(p^{-1/2}\) gives \(p\); layer cake gives \(p^{\eta/4+1/4}\log p\). Downstream: R180 line 51, \(\mathcal D_0+\mathcal D_1\le4R_*\mathcal M_w\) with \(R_*=O(p^{1/2-1/1280})\) (line 42), and line 76, \(\mathcal D_J\le2G\mathcal M_w\). Both match. |
| (b2) | Fourier criterion | Honest | It is correctly marked as not viable. |
| (c1), (c2) | Log-interval, subgroup and random models | Honest as evidence | Replay identical. Minor: the "sub" rows use \(H\setminus\{1\}\) (\(N=d-1\)). |

Mission compliance: the row-pair reformulation is re-proved in full. Every external input is stated with its hypotheses and checked. The structural facts used about \(g\) are (H1), (H2) and (H4), each with its source. Proved, conditional and floating results are kept separate. The Round 181 Shkredov coset claim is correctly left unproved. "Supported for the secondary question (exponent below 36/13)" matches the mission's acceptance clause.

## 3. Report: `native-claude-cold-prime-signed-nonseed-price-182.md`

| Item | Statement | Verdict | Notes |
|---|---|---|---|
| (a1) | Frozen-base identity; Proposition 1 with (H1) class closure, (H2) corrections uniform over inputs, (H3) strict invariance | CONFIRMED | The identity \(U_{j+1}=R+LU_j+T(U_j)\) is checked. The induction uses one \(j\)-independent threshold \(p_1\). This implements both corrections of `native-claude-audit-181.md` lines 118–120. It is a criterion: no price is shown to satisfy it. Remark 2 (H1/H2 for \(P_{5000}\) inherited, not re-derived) is honest. |
| (a2) | \(\kappa^*\in[0.7741471,0.7741472]\) "exact rationals", plus brackets at \(p_0=10^{-3},10^{-6},10^{-12}\) | **ERROR (minor, numerical)** | The script's certified lower bound is \(0.7741470635\) (recomputed by calling its own `lower_kappa`). `fmt` prints it rounded to nearest as 0.7741471. The audit's independent 60-digit maximisation gives \(\sup=0.7741470636\), **below** the printed lower end. Likewise \(0.9383483650<0.9383484\) and \(0.9980706538<0.9980707\). **Correct statement:** \(\kappa^*(0.01272)=0.77414706\ldots\), \(\kappa^*(10^{-3})=0.93834837\ldots\), \(\kappa^*(10^{-6})=0.99807065\ldots\). Printed brackets must be rounded outward. Nothing downstream changes: all later uses round down to 0.77414 or 0.774147. The R181 fixed-ball statement (\(c=1.0043\): discriminant \(>0\) at 0.77394 and \(<0\) at 0.77395) is confirmed independently. |
| (a3) | Proposition 2 (Duhamel), Corollary 2.1 \(\lambda_{\max}(C)=1-C(1-\kappa^*)\), Corollary 2.2 | CONFIRMED-WITH-CORRECTION | The variation-of-constants identity and the table are verified (0.77415, 0.71768, 0.66122, 0.54829, 0.32244). **Correction to Cor. 2.2:** empty \(L_S\)-blocks have price \(\|I\|=1\), so the word bound needs \(C_S\ge1\). This holds for every row of the β-table. |
| (a4) | Remark 2.3: the criterion forces \(\Gamma_{k_n}\) bounded; the bound 1.066 gives \(\Gamma\ge n^{1/20}/1.066\) | CONFIRMED-WITH-CORRECTION | Uses the accepted R180 \(0<\liminf\|R_{602}\|_{2,n}\) (ineffective; `cold-growing-prefix-delocalization-180.md` line 26). "\(\exists u\iff4\sigma\Gamma c<1\)" treats \(c\) as constant. Necessity still holds with \(c\) replaced by \(c(M_0)\approx0.93\), since \(c(M_0+u)\ge c(M_0)\). \(1.066^{80}>2^7\) verified exactly. "Needs a power rate below one" is a paraphrase of "\(\Gamma_{k_n}\) bounded". By submultiplicativity the two are equivalent up to constants. |
| (a5) | Lemma 3.1 \(r'_++r'_-=4r-NZ\); rates 0.71006 / 0.53255; \(G_m\) upper bounds; power constants | CONFIRMED | Lemma 3.1 and \(G_1(\alpha)=\max(2+\alpha,(4+2\alpha)/(1+\alpha))\) were re-derived by hand (\(\pi_\alpha=r+\alpha Z/2\), \(Z\) = zero slots; the all-\(|w|=1\) ray gives \(2+\alpha\)). Audit Part 2 brute-forces the Round 80 rule over 2413 configurations (\(r\le4\), \(m\le3\)). No ratio exceeds the reported \(G_{\rm up}\). At \(m=2\) the maxima equal the report's \(G_{\rm lo}\) exactly (11, 9.478, 8.667). The β-table is reproduced; it is under (b1), as labelled. |
| (a6) | Crude costs \(2A/\sqrt N\), \(4A/\sqrt N\), Taylor majorant \(G(y)\) | CONFIRMED (as implications) | \(\sum_{l\ge1}(2l+2)c_lx^l=x(1-x)^{-3/2}+2(1-x)^{-1/2}-2\) was checked against the series. Values 0.50073, 1.00145, 0.10425, 0.64623 and total 1.96127 reproduced. \(A(h)\le1.9946\) is conditional (b2), as labelled. |
| (b1)–(b4) | Conditional | Honest | — |
| (c1)–(c3) | Floating stationary row; frozen decay | Honest as evidence, with one correction | Replay identical. **Correction to "What survives"** (§4 and "Exact remaining gap"): \(B\) as defined contains the *seed-only* higher Taylor terms. Their crude dimension cost 0.10425 (doubled to about 0.21 if \(\pi_1\) doubles as for the h-linear term) is not in "\(\rho A(h)<1.925\)". Charging it leaves an h-dependent budget of 0.137 (or 0.033), i.e. \(\rho A(h)<1.094\) (or 0.264). With \(A(h)\gtrsim0.55\) that needs \(\rho\lesssim2\), not \(\lesssim3.5\). This holds unless the seed-only part is moved into the seed multiplier (\(L_S=K\Phi'_t(S)\cdot\)) and re-priced. The report's next test 1 suggests exactly that move, and it should be made explicit. Also, "evidence rules out every plain-dimension version" assumes the crude product ratio \(\rho=2\) is best possible. A smaller provable \(\rho\) is not excluded, so "rules out" should read "is evidence against, at \(\rho=2\)". |

Mission compliance: Proposition 1 is restated and re-proved with both audit hypotheses. No new price is claimed, so no new p0, c or closure is owed. Exact and floating material are separated. Outcome "inconclusive" with "best certified κ0 = 1.066 and the blocking term = non-seed multiplier" matches the mission's inconclusive clause.

## 4. Blind overlap review

This section was written before opening any shared-obligation, draft or inflight file.

**Answer: no two reports reduce to a genuinely shared estimate at the same hypotheses and scale.**

**Reports 1 and 2.** They share the same underlying measure, through an exact identity verified in audit Part 5 at \(p=29,53\). Let \(\mu(r,b)=g(Y)g(D)\) be report 1's weight on the Round 171 chart, with mask \(b\in Q\) and \(Y\ne D\). Since \(\kappa=1-r\) and \(b_{171}=\kappa D/Y\) is report 2's \(b\):
\[
 \mathcal M_w=\sum_r\sum_{b\ne b'}\mu(r,b)\mu(r,b')\,w(b/b'),\qquad
 E_Q(h)=\sum_r m(r)^2=T_1^\times(m).
\]
So the direct first mass is a \(w\)-weighted **dilation** (intercept-ratio) correlation inside the slope fibres of report 1's \(\mu\). The squared \(r\)-row mass of report 2 is exactly the slope energy that report 1's Hilbert–Schmidt identity subtracts.

The estimates they need are different:
- Report 2 needs an **upper** bound on the multiplicative first moment of \(b/b'\) within slope fibres, or on \(E^\times(h)\), at scale \(p^{1+1/1280}\).
- Report 1 needs an **upper** bound on the row-deleted operator norm, equivalently on the additive **translation** discrepancy \(\sum_{a,c}(\Delta(a,c)-C(a)/p)^2\) of \(\mu\) at scale \(p^3\) (\(k=2\)) or \(p^{9/2}\) (\(k=3\)). There \(\sum m^2\) and \(T_k^\times(m)\) enter with a **minus** sign.

So report 2's new bound \(\sum_rm(r)^2=O(p^{34/23})\) gives report 1 nothing. As an upper bound it is useless in a subtracted term, and through \(W_\xi\le\sum m^2\) it is weaker than R180's \(\sup C=O(p^{11/8})\), which already feeds \(\mathcal E(\mu)=O(p^{43/16})\).

A weaker shared *input* exists: a bound \(\sum g^2=O(p^{1/2-\delta})\) would help both:
- report 1 through (b1‴), where any \(\delta>0\) relaxes the target;
- report 2 through (b2), which needs roughly \(\delta\ge1/4\) together with control of \(\hat w\), and is refuted in subgroup-mixture models.

The scales differ, so this is a shared hypothesis, not a shared estimate.

**Report 3 and reports 1/2.** Disjoint. Report 3 concerns the cold complex dynamics: prices of \(L^m\) for the frozen multiplier. The only common feature with report 1 is the tool of operator powers and moments (\(\Gamma_k\) vs. \(\operatorname{tr}((\pi\pi^*)^k)\)). Sharing a tool does not count.

## 5. Replay log

All commands were run from the repository root on 2026-11-20. "Matches" means the printed output equals the report's quoted output line for line.

| Script | Command | rc | Time / peak memory | Key output |
|---|---|---|---|---|
| shifted rowpair | `python3 -B research/paley-182-shifted-energy-rowpair-check.py` | 0 | 0.16 s / 9.6 MB | Matches; `ALL OK` (A at p=13–41, B at 31/61/101, C floating) |
| shifted exponents | `python3 -B research/paley-182-shifted-energy-exponents.py` | 0 | 0.02 s / 8.6 MB | Matches; `Lemma SE (8/3) + layer cake : a=5/6, eps=1/46, delta=1/138, E^x(h)=O(p^(34/23))` |
| shifted logint | `python3 -B research/paley-182-shifted-energy-logint.py 4000000` | 0 | 3.8 s / 229 MB | Matches; log-interval E/N² 2.775–2.998, subgroup 2.18–3.42 |
| opnorm identities | `python3 -B research/paley-182-opnorm-identities.py` | 0 | 0.14 s / 9.2 MB | Matches; `all exact checks passed` |
| opnorm models | `python3 -B research/paley-182-opnorm-models.py 20 26 36 40 54` | 0 | 256 s / **502 MB** | All 20 model rows match the report's table. The report's "~140 MB peak" understates memory by about 3.5×. |
| cold criterion | `python3 -B research/paley-182-cold-criterion-check.py` | 0 | 19.0 s / 9.5 MB | Matches; `p0=1e-02: kappa* in [0.7741471, 0.7741472]` (lower end mis-rounded, see §3 (a2)) |
| cold seed power | `python3 -B research/paley-182-cold-seed-power-check.py` | 0 | 7.1 s / 8.7 MB | Matches; `alpha=1: lam_hat=2.893613 (rate 0.51366), C=1.0749` |
| cold fixed point | `/usr/bin/python3 -B research/paley-182-cold-fixedpoint-diagnostic.py` | 0 | 1.4 s / 78 MB | Matches; `p=400009 ... sup|h|=0.5566 RMS(h)=0.1749`. Needs numpy; `/opt/homebrew/bin/python3` has none. |
| audit shifted | `python3 -B research/paley-182-audit-shifted-energy-check.py` | 0 | 0.5 s / 41 MB | `P1 Prop 3 four norm exponents ... ['17/46','289/828','17/46','17/46']`; `grid optimum 2957/8000 >= 17/46`; `P2 p=53/61: M_w(chart)==M_w(rows) exactly`; `P5 ... M_w == sum_r sum_(b!=b') mu mu' w(b/b')`; `ALL AUDIT CHECKS OK` |
| audit opnorm | `/usr/bin/python3 -B research/paley-182-audit-opnorm-check.py` | 0 | 7.9 s / 27 MB | `O2-O5 OK` at p=29,37,53,61; `O6 conic determinant ... OK`; `O7 exponents ... OK`. macOS Accelerate emits spurious matmul FP warnings; they are silenced and finiteness is asserted. |
| audit cold | `python3 -B research/paley-182-audit-cold-check.py` | 0 | 0.5 s / 9.2 MB | `p0=0.01272: sup = 0.7741470636 < printed lower end 0.7741471: True`; β-table reproduced; `Round 80 rule brute force: 2413 parent configurations ... 0 stopped early`; all maxima ≤ G_up |

No replay was killed. The largest footprint was the op-norm models at 502 MB.

## 6. Ranked next tests (auditor's recommendation)

1. **First mass as a fibre dilation correlation (ordinary; uses the §4 identity).**
   - \(\mathcal M_w=\sum_r\sum_{b\ne b'}\mu(r,b)\mu(r,b')w(b/b')\) keeps \(w\) and every amplitude. Compute it, and its restriction to the large spectrum of \(w\) (report 2's test 2), in subgroup-mixture and Fejér models.
   - Test whether a per-slope-fibre multiplicative energy, rather than the whole-level \(E^\times(1-S_t)\), already reaches \(p^{1+o(1)}\).
   - Outcome: a route to \(\mathcal M_w\) that avoids the BSG method cap of report 2's (a8), or a model with power growth that refutes positivity.
2. **Whole-level shifted energy, numerically (report 2's test 1).** This is a cheap falsification test of criterion (b1) on structured admissible families: rank-two progressions and Fejér level sets of \(g=|f|^2\).
3. **Re-price the cold seed multiplier as \(K\Phi_t'(S)\) (cold).**
   - Move the seed-only Taylor terms into \(L_S\), and compute its exact per-simple \(\pi_1\) growth with the audited Round 80 rule. The Part 2 brute force here can be extended.
   - Without this move, the h-linear allowance is \(\rho A(h)\lesssim1.09\), not 1.925 (§3 correction).
   - Combine with report 3's test 2: does \(c(M)\) survive in \(\pi_1\)?
4. **Row-deleted sixth moment by word type (report 1's test 1).** Compute \(\operatorname{tr}((R\pi\pi^*R)^3)\) exactly at \(p\le677\), split by six-word class. Then look for a point–conic incidence input with its hypotheses stated.
5. **Decide \(\sum g^2\) for the actual law (shared input of report 1 (b1‴) and report 2 (b2), at different scales).** \(\sum_\alpha\omega(\alpha)^2=2\sum g^2/(p-1)\) together with square-class balance.
6. **Bookkeeping hygiene.**
   - Fetch and quote Schoen's BSG statement before the next acceptance relies on \(|B|\gg mK^{-1/2}\), \(|B/B|\ll K^4|B|\) again.
   - Re-derive the R178/179 consequences of \(E^\times(h)=O(p^{34/23})\). The audit expects no exponent change, since R180's \(\sup C\) is stronger.
   - Use outward rounding when printing certified brackets.
