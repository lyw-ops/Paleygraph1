# Independent audit of Round 183 (session/r183-audit)

- **Auditor:** Claude Opus 5.5 side session started by the Round 183 coordinator (`session/r183-audit`). This is an agent audit, not human acceptance and not a mathematical certification. The auditor wrote none of the three reports and is not the coordinator.
- **Status of this file:** written incrementally. The "Blind overlap review" section below was saved before any file under `coordination/shared-obligations/`, `coordination/drafts/` or any `coordination/round-*-inflight.json` was opened.
- **Read:** `AGENTS.md`, `docs/WORKFLOW.md`, `docs/ROUND_REVIEW.md`, `coordination/checkpoints/round-182.md`, `research/round-182-acceptance.json`, `research/native-claude-audit-182.md`, the three missions in `coordination/missions/round-183/`, the three reports, and the sources a check needed:
  - `anchored-repair-20.md` lines 66–78 (gap theorem); `ordinary-prime-coset-spread-151.md` lines 24–45 and `round-151-acceptance.json` proof scope; `ordinary-weighted-slope-product-incidence-178.md` line 29; proof scopes of `round-178/180-acceptance.json`;
  - `native-claude-ordinary-prime-shifted-level-energy-182.md` (Lemma S1, lines 100–106);
  - `cold-height-602-frozen-kernel-162.md` lines 30–46, `cold-first-prefix-step-174.md` lines 1–30, `native-claude-cold-prime-signed-nonseed-price-182.md` (hypothesis (b1), lines 210, 265, 289–293).
- **External sources**, read through a fetch subagent (arXiv HTML renderings):
  - Shkredov, arXiv:1504.04522**v1** (only version), Theorem 6 and §2 definitions;
  - Reiher–Schoen, arXiv:2308.10245**v2** (Combinatorica 44 (2024) 691–698), abstract, Theorems 1.1 and 1.2.
  - Schoen, Combinatorica 35 (2015) 695–701, is not on arXiv. Its full text was **not** read; its statement is known here only as Reiher–Schoen restate it.
- **Files written:** this file; `research/paley-183-audit-fibre-check.py`, `research/paley-183-audit-rowdel-check.py`, `research/paley-183-audit-cold-check.py`. Nothing else in the repository was changed. Nothing was committed.

Verdict key (per claim the report labels as proved):
- **ACCEPTED:** correct as written, for the stated hypotheses.
- **ACCEPTED WITH CORRECTION:** true after the stated correction, which does not change the report's main conclusion.
- **CONDITIONAL:** correct given a named input that is not proved or not checked.
- **REJECTED:** false as written, or not supported.

## Summary

| Report | Main verdict | Corrections / conditions |
|---|---|---|
| F. First mass as fibre dilation | (a1), (a3), (a5), (a7) ACCEPTED; (a2) ACCEPTED WITH CORRECTION; (a4), (a6) CONDITIONAL on Shkredov Thm 6 (statement now quoted from the source and matching; proof not checked). "Inconclusive" is honest. **Proposition C (w worth exactly 3/4) is ACCEPTED** and re-checked exactly at seven new primes. **Corollary C2 is CONDITIONAL only on Shkredov's Theorem 6, whose hypotheses it meets.** | (a2): the "rich-fibre criterion" (RF) is equivalent to \(E_Q(h)=X=O(p^{1+1/1280})\), which was already a sufficient condition via Round 182 Prop. 1(iv); it is not a weaker new criterion. C1 is a statement about arguments that use only (H1), (H2), (H4); under (NC) the family \(g_H\) is not admissible (§2.3). |
| C. Cold seed multiplier power rate | (a1)–(a3), (a5) ACCEPTED (compact model, per simple, under the inherited (b4)/(b-Jk)); (a4) CONDITIONAL on (b1*), (b3); (a6) ACCEPTED as an implication. **Proposition 3 exact suprema: ACCEPTED**; an independent float LP and an exact extremal family agree to \(\le2\cdot10^{-6}\) from below, never above. "Inconclusive" is honest. | **The π₁ allowance 1.912 is CONDITIONAL on reading (b1) for the source price, which the report's own Lemma 4 does not support in π₁.** Under the report's re-derived constants (b1*), the π₁ allowance is 1.128, only slightly above the Round 182 audit's 1.094; the restoration holds for the dimension price A (allowance 1.542), not for π₁. Printed allowances \(X\) are rounded the wrong way ("\(X\le1.9122\)"; the certified statement is \(X\ge1.9120\)). |
| R. Row-deleted one-match | (a1), (a2), (a4)–(a9) ACCEPTED (with (a2), (a4) on (NC)); (a3) ACCEPTED WITH CORRECTION. **IXX verified at \(O(p^{150/32})\): ACCEPTED** (arithmetic and every inequality re-derived; the cubic split checked exactly at p=29–53). **"(H_sat) square-class balance false": ACCEPTED on the near-critical branch (NC)**, from an intermediate step of the accepted Round 151 proof. "Inconclusive" is honest. | (a3): "b1′ saturated iff \(\sum g^2\gg\sqrt p\)" must read "the \(s=1\) row forces saturation iff …"; small \(\sum g^2\) does not by itself make \(\|\pi\|=o(p^{3/4})\). (SL) is sufficient but stronger than R needs: R's route needs only \(\max_\xi W_\xi=O(p^{1+\varepsilon})\). Mission normalization correction (factor 2) confirmed. |

**Citation finding (affects accepted Rounds 163/173/177/182, not a Round 183 claim).** The BSG form used for \(E^\times(h)=O(p^{34/23})\), \(|B|\gg mK^{-1/2}\), \(|B/B|\ll K^4|B|\), is **Reiher–Schoen 2024, Theorem 1.2** (\(|A'|\ge(1-\varepsilon)K^{-1/2}|A|\), \(|A'-A'|\le2^{33}\varepsilon^{-9}K^4|A'|\), any abelian group). It is not Schoen 2015: Reiher–Schoen state the earlier best result as \(|A'|\ge\Omega(|A|/K)\), \(|A'-A'|\le O(K^4|A'|)\) (their Theorem 1.1, attributed to Schoen [4]). The exponents used by the project are therefore correct for a published theorem, but the citation should be corrected. No Round 183 claim depends on BSG: R's equivalence (Prop. 2.2(3)) also follows from the trivial \(X\le GM_1\).

## 1. Blind overlap review

Written after reading the three reports and their missions (`coordination/missions/round-183/*.md`), `AGENTS.md`, `docs/WORKFLOW.md`, `docs/ROUND_REVIEW.md`, `coordination/checkpoints/round-182.md`, `research/round-182-acceptance.json` and `research/native-claude-audit-182.md`. No shared-obligation, draft or inflight file had been opened.

Reports, abbreviated:
- **F** = `native-claude-ordinary-prime-first-mass-fibre-dilation-183.md` (first mass \(\mathcal M_w\) as a fibre dilation correlation);
- **C** = `native-claude-cold-prime-seed-multiplier-power-rate-183.md` (cold seed multiplier power rate);
- **R** = `native-claude-ordinary-prime-row-deleted-one-match-183.md` (row-deleted one-match criterion).

| Pair | Classification | Reason |
|---|---|---|
| F – C | **independent** | C concerns prices of powers of the frozen cold multiplier at \(V_{602}\). No object, lemma or estimate of F appears in it. |
| R – C | **independent** | Same reason. The only common feature is the use of operator powers (\(\Gamma_k\) vs \(\operatorname{tr}A^k\)), a shared tool, not a shared estimate. |
| F – R | **shared-input** (one shared candidate estimate, at different scales; not duplicated) | See below. |

**F – R in detail.**

1. **The shared estimate is the slope-row mass \(X=\sum_r m(r)^2=E_Q(h)=\sum_{\kappa\in Q\setminus\{1\}}c_h(\kappa)^2\)**, with the actual \(\mu\), \(h(z)=g(1-z)\), counting norms, and the hypotheses (H1), (H2), (H4) of Round 182.
   - R names it explicitly as candidate shared lemma (SL): \(X=O(p^{1+\varepsilon})\). In R it enters as an **upper** bound for \(W_\xi\le X\) inside the Round 178 point–plane bound for \(\mathcal E(\mu)\). Any \(\varepsilon<3/16\) improves the one-match exponent, and \(\varepsilon=o(1)\) brings the dominant IXX class to \(p^{9/2+o(1)}\).
   - F's rich-fibre criterion (RF), \(\sum_{c_h(\kappa)>\tau}c_h(\kappa)^2=O(p^{1+1/1280})\) at \(\tau=p^{1/1280}\), is **equivalent** to \(X=O(p^{1+1/1280})\), although F does not say so. The fibres with \(c_h\le\tau\) contribute at most \(\tau M_1\le\tau(G-1)^2=O(p^{1+1/1280})\) (F's own Proposition B). So (RF) is (SL) at \(\varepsilon=1/1280\).
   - In F's admissible coset family \(g_H\), Proposition C gives \(\mathcal M_w(g_H)=\tfrac34\cdot\tfrac14(E_Q(h)-\mathrm{diag})\). For arguments that use only (H1), (H2), (H4), a bound on \(X\) is therefore also **necessary** at F's scale in that family, not only sufficient.
2. **Scales differ.** F needs \(\varepsilon\le1/1280\); R gains from any \(\varepsilon<3/16\). A proof of F's version implies R's. A proof of R's version at, say, \(\varepsilon=1/8\) gives F nothing at target scale (it gives \(\mathcal M_w\le X/4=O(p^{9/8})\), which does improve the accepted \(\mathcal M_w=O(p^{11/8})\)). So R's version is a strictly easier intermediate that still matters to both calls.
3. **Shared accepted input.** Both use the accepted Round 182 bound \(X\le E^\times(h)=O(p^{34/23})\) as their current verified value (F: "verified bound"; R: Proposition 2.2(1)). Both inherit its BSG/Schoen dependence.
4. **Shared hypothesis, not estimate: \(\sum g^2\).** F's (G2) \(\Gamma_2=O(p^{1/4+1/2560})\) and R's Part 1 concern the same quantity. R's Proposition 1.4 (if accepted) bounds it above by \((\tfrac12+o(1))\sqrt p\) on (NC) and shows that F's (G2) is equivalent to \(\mathcal E(S)/|S|^3=O(p^{-1/4+1/1280})\) for the flat support. This is as the Round 182 audit described: one shared hypothesis, at different scales.
5. **A cross-report interaction F does not see.** R's Proposition 1.2 (sector concentration on (NC): \(G_{-\rho}=O(1)\)) is a structural constraint on the actual \(g\) that is **not** among F's (H1), (H2), (H4). F's family \(g_H\) is admissible for (H1)–(H4) but is generally not sector-concentrated and has a two-level, non-flat law \(\nu\). If R's Proposition 1.2 is accepted, F's necessity statement (Corollary C1) stays true as written (it is about arguments using only (H1), (H2), (H4)), but it stops being an obstruction for arguments that also use (NC). The open "coset subclass" of F's Corollary C3 is then not known to contain any (NC)-admissible \(g\).
6. **Not duplicated.** Neither report proves (SL) or (RF). F's Proposition A re-derives the Round 182 audit identity, as its mission required. R cites the same identity (via \(X=E_Q(h)\)) and does not re-prove it. No lemma is proved twice.

**Would this have changed dispatch?** Probably not the choice of calls. It should have produced one `cand:` entry for \(X=E_Q(h)=O(p^{1+\varepsilon})\) with both call IDs, with the two scales stated. F's closeout note ("the one shared hypothesis is \(\sum g^2\)") understates the overlap: it misses that (RF) is the same estimate as R's (SL).

### After unblinding

Opened afterwards: `coordination/round-183-inflight.json`, `coordination/shared-obligations/round-183-before.json` and `coordination/drafts/round-183-dependency-assessment.json`.

- The coordinator's pre-dispatch comparison (`comparison_status: assessed`, `known_shared: []`) found that the two ordinary calls share the object \(\mu\) but no estimate. It named \(\sum g^2\) as the only possible shared input and recorded no `needs:` edge.
- **My classification is unchanged.** F – R is **shared-input**: the estimate \(X=\sum_rm(r)^2=E_Q(h)=O(p^{1+\varepsilon})\) is a sufficient condition in both reports, at different scales (F: \(\varepsilon\le1/1280\), and necessary within the \(g_H\) family for (H1)/(H2)/(H4)-only arguments; R: \(\varepsilon<3/16\)). The coordinator could not have seen this before dispatch, because the identification of F's (RF) with \(X\) and R's use of \(X\) as an upper bound for \(W_\xi\) are both Round 183 outputs.
- Refinement after checking R in detail (§4): R needs only \(\max_\xi W_\xi=O(p^{1+\varepsilon})\), where \(W_\xi=\sum_rm(r)m(\xi/r)\le X\). The common strong form is \(X=O(p^{1+\varepsilon})\). A `cand:` entry should record both forms.
- Dispatch: knowing this would not have changed the Round 183 calls. It should change Round 184 (§6).

## 2. Report F: `native-claude-ordinary-prime-first-mass-fibre-dilation-183.md`

### 2.1 External input: Shkredov, Theorem 6

Source: arXiv:1504.04522, which exists in v1 only (17 Apr 2015), read in its HTML rendering. Theorem 6, as quoted by the fetch subagent from the source:

> "Let p be a prime number, Γ, Π be multiplicative subgroups of F_p^*. Suppose that |Γ||Π| < p. Then for any x, y ≠ 0 one has E^×(Γ+x, Π+y) ≪ |Γ||Π| log(min{|Γ|, |Π|}) + |Γ|^2 + |Π|^2."

Further details from the source:
- §2 defines \(E^\times(A,B)=|\{a_1b_1=a_2b_2\}|\) with no exclusion of 0.
- \(\ll\) is Vinogradov's symbol; logarithms are base 2.
- The abstract states the special case \(E^\times(G+x)\ll|G|^2\log|G|\) for \(|G|<p^{1/2}\).

F's transcription matches this statement exactly. F's remark that deleting 0 from \(\Gamma+x\) only lowers the count is correct for this definition. Neither F nor this audit re-checked the proof (Proposition 3 and Remark 4 of the paper). Claims using Theorem 6 are therefore marked **CONDITIONAL on Shkredov's Theorem 6**, with the hypotheses verified.

### 2.2 Verdicts

| Item | Statement | Verdict | Notes |
|---|---|---|---|
| (a1) | Prop. A: fibre form and four-variable form of \(\mathcal M_w\), \(w\) kept | **ACCEPTED** | Re-derived by hand: \(1-r=\kappa\), \(b=\kappa D/Y\), mask \(b\in Q\iff\kappa\in Q\), \(D=b(1-\kappa)/(\kappa(1-b))\), \(s=AD/(CY)\). The audit script F1 checks fibre form = four-variable form and \(m(r)=c_h(1-r)\) exactly at \(p=61,97,137\), with independent code. |
| (a2) | Prop. B and Corollary B ((RF), (MF), (G2)) | **ACCEPTED WITH CORRECTION** | All inequalities are correct (F2 checks them exactly). **Correction:** at \(\tau=p^{1/1280}\) the light fibres contribute at most \(\tau M_1\le\tau(G-1)^2=O(p^{1+1/1280})\). So (RF) is *equivalent* to \(X=E_Q(h)=O(p^{1+1/1280})\). Round 182 Prop. 1(iv) already gave \(\mathcal M_w\le(E_Q(h)-\mathrm{diag})/4\), so (RF) is the existing sufficient condition restated by fibre size, not a weaker one. It is weaker than (MF) and Round 182's (b1), as F says. The sentence "every fibre class of bounded mass is closed" is correct but contentless beyond this equivalence. |
| (a3) | **Prop. C**: \(g_H=|f|^2\) admissible; \(\mathcal M_w(g_H)=\tfrac3{4096}E_{\rm off}(H)=\tfrac34\cdot\tfrac14(E_Q-\mathrm{diag})\); Cor. C1 | **ACCEPTED** | Re-derived: \(f=\tfrac121_H+\tfrac12\delta_1\), \(g_H=\delta_1+\tfrac141_{H\setminus\{1\}}\), \(\max\nu=(|H|+1)/(2n)\), \(G=(|H|+3)/4\); every supported label lies in \(H\setminus\{1\}\), so \(s\in H\setminus\{1\}\) off the diagonal and \(w(s)=3/16\), with \(\mu\mu'=4^{-4}\). F3 recomputes \(\mathcal M_w\) from the fibre form, not the closed formula, for **every** subgroup \(|H|\ge3\) at \(p=137,149,157,173,181,193,197\). **Scope of C1:** it is a statement about arguments using only (H1), (H2), (H4) with cap \(C_{\rm cap}\). The family \(g_H\) is **not** on the near-critical branch: its law is two-level with flat part \(H^\perp\) of size \(n/|H|\), and \(m_{\rm eff}\approx4n/|H|\). Near-criticality needs a flat support of size \((1+o(1))m_0\) with \(m_{\rm eff}\sim m_0\). Round 151 (accepted, item 3) also proves a fixed Fourier mass outside every bounded union of cosets of size \(\asymp\sqrt p\), and R's Prop. 1.2 gives sector concentration. So C1 says that (H1)/(H2)/(H4) alone cannot reach the target. It does not show the first mass needs more than the near-critical structure. |
| (a4) | Cor. C2: coset supports with \(|H_i|^2<p\) give \(\mathcal M_w\ll k^4\max|H_i|^2\log p\) | **CONDITIONAL** on Shkredov Thm 6 (hypotheses met) | Proof checked: \(h\le\sum_i1_{1-\xi_iH_i}\); \(\mathcal N=E^{\times1/4}\) is a monotone norm, giving \(k^4\); the dilation \(z\mapsto-\xi^{-1}z\) maps \(1-\xi H\) to \(H-\xi^{-1}\); \(x=-\xi^{-1}\ne0\); \(|H|^2<p\). F5 is a sanity check only: \(E^\times(H-x_0)/(|H|^2\log_2|H|)\) lies in 0.29–0.45 for \(20\le|H|\le400\). Note that on (NC), Round 151 already excludes \(g\) supported on such unions when \(|H_i|\asymp\sqrt p\). C2 is useful as a structured-piece lemma, not as a statement about the actual law. |
| (a5) | Cor. C3: \(E_{\rm off}(H)\ll p^{4/3}\) for \(|H|\le2C_{\rm cap}\sqrt p\) | **ACCEPTED** | The hypotheses of Lemma SE (Round 182, accepted) hold: \(B_i\subseteq H\setminus\{1\}\subset\mathbb F_p\setminus\{0,1\}\), \(N_i\le\sqrt p\), \(V_i\subseteq H\), \(K_i\le|H|/N_i=O_{C_{\rm cap}}(1)\). Constants depend on \(C_{\rm cap}\). |
| (a6) | Prop. D: \(|S_t\cap(1+\xi\Gamma)|^4\ll C_{\rm cap}\sqrt p|\Gamma|^2\log|\Gamma|/t^2\) for \(|\Gamma|^2<p\) | **CONDITIONAL** on Shkredov Thm 6 | Lemma S1 is quoted correctly (Round 182 lines 100–106, accepted). \(W\subseteq S_t\subset Q\). Monotonicity and dilation by \(\xi^{-1}\) are correct. The "forced energy \(t^4|\Gamma|^3=O(p^{3/4}\log^{3/2}p)\)" paragraph is a statement about one mechanism, as F says. |
| (a7) | Props. E, F (spectral restriction; per-fibre Hölder) | **ACCEPTED as method statements** | \(\hat w(\chi)=\tfrac3{16}(|H|1[\chi|_H=1]-1)\); \(\Phi(\chi)=E_Q(h)\) on \(H^\perp\) (F3/F4 check \(Y/D\in H\) on the support); \(\sum_P\mu(P)^2\ge((|H|-1)^2/2-(|H|-1))/256\) (F4); Hölder with \((\nu\star\tilde\nu)(1)=\|\nu\|_2^2\); \(q\ge640\) arithmetic. These are statements about two methods in the family \(g_H\), not lower bounds for the actual \(\mathcal M_w\). |
| (b1), (b2) | (RF)/(MF)/(G2) ⇒ target; \(C_{\rm cap}<1/2\) ⇒ coset family closed | Honest | (G2) is not "false" for the actual law. R's Prop. 1.4 shows it is equivalent to \(\mathcal E(S)/|S|^3=O(p^{-1/4+1/1280})\), which is open. F says "false in every model", which is accurate. |
| (c) | Models; exact subgroup counts | Honest as evidence | The replays match (§5). |

Mission compliance:
- The identity is re-derived before use.
- \(w\) is stated as kept or majorized in each step.
- External inputs are stated with hypotheses.
- Models compare \(\mathcal M_w\) with its spectral restriction.
- The inconclusive return names the fibre class.

**Overlap note:** F's closeout says the only shared item is \(\sum g^2\). That is incomplete (§1).

## 3. Report C: `native-claude-cold-prime-seed-multiplier-power-rate-183.md`

| Item | Statement | Verdict | Notes |
|---|---|---|---|
| (a1) | Lemma 1: \(\Phi_t'(S)=(s/2\sqrt t)\sum_{k\ \rm odd}\hat g_k(\beta)J^k\), uniform \(\gamma_k\) | **ACCEPTED** | Series re-derived from \((1+y)^{-1/2}\) and \(\cos^{2l+1}\). The δ-term \(\tfrac12(1-b)^{-3/2}\delta\) is the derivative majorant summed over \(k\), since the binomial weights sum to at most 1. \(\beta_0=2/a=256/2031\), \(\delta\approx2.1\cdot10^{-7}\) and \(\varpi=s_{\rm up}/\sqrt N\) were rechecked. Audit C1 (float FFT, \(2^{16}\) points) puts \(\hat g_1,\dots,\hat g_9\) inside the printed brackets, and \(\sum|\hat g_k|=0.970544197765\). |
| (a2) | Lemma 2: the \(J^k\) child is valid; \(r(|k|-1)\le r'\le r(|k|+1)\); zero refill on the destination fibre under \(J^{\pm1}\) | **ACCEPTED** (compact model, given (b4)/(b-Jk)) | Proof re-derived: \(nz_{A'}+\tau=2r\) and \(r'=2r-\tau\) (accepted Round 182 Lemma 3.1); \(\#(|w|\ge2)\le\sum_{|w|\ge2}(|w|-1)=\#\text{zeros}\); for \(|k|\ge3\), \(r'\ge2r\). The brute-force replay matches. |
| (a3) | **Prop. 3: exact suprema \(G_m(\alpha)\)**, power forms; Round 182 \(G_{\rm up}\) are exact suprema | **ACCEPTED** (compact model, per simple, path-summed ratio) | Independent audit C2 uses my own slot-count linearisation of the \(J^k\) rule and a Charnes–Cooper LP in float64, for \(m\le3\) and \(\alpha\in\{0,\tfrac12,1\}\). With parent values \(|v|\le60\) plus columns at \(|v|=10^4,10^6\), the LP reaches the report's value to within \(2\cdot10^{-6}\) **from below**, and never exceeds it. The exact family \(A=(-K,0^{K/2-1})\), \(B=(0^{K/2})\) at \(K=20000\) is within \(2\cdot10^{-4}\) below, also never above. The case \(\alpha=1,m=1\) is attained at bounded \(|v|\), as the report says. The upper side rests on the report's exact dual certificate, which the audit replayed (identical output) but did not re-implement. The objects are per-simple path-summed ratios, an upper bound for \(\|L_S^m\|_{\pi_\alpha}\), as the report states. **Minor:** the \(|k|\ge7\) tail is not "τ ≈ 10⁻⁵". With the uniform \(\delta\)-term it adds about \(2.4\cdot10^{-4}\) to \(\lambda_S\) (0.53220 → 0.53244). This is conservative, and the report's \(\lambda_S\) values already include it. |
| (a4) | Lemma 4: \(c_\alpha=\tfrac{1+\alpha}2c(M)\); \(p_{0,\alpha}\le(1+\alpha)A(R_{602})\); \(\kappa^*_\alpha\) brackets | **CONDITIONAL** on (b1*) and (b3) | The factor bookkeeping agrees with the Round 162 text (lines 37–38: "price at most twice that rank. The integral of 1−s cancels this factor two") and Round 174 (line 13: "the factor 2 from the price and 1/2 from Taylor integration"). So \(c\) survives verbatim in π₁ and halves in \(A\); this answers the mission's question. Reading Round 174 line 3 ("dominates … the dimension budget") as \(A\le P_{5000}\) on the unshifted class is plausible but is a reading. The report correctly flags it as (b1*). Audit C3 (float) reproduces every \(\kappa^*\) inside its bracket: 0.7741470636, 0.8379025145, 0.7973781432, 0.7568537718, 0.6758050291. **The brackets are rounded outward** (lower end `dn`, upper end `up`; `kappa_bracket` uses \(c_{\rm up}\) for the lower and \(c_{\rm lo}\) for the upper bound). |
| (a5) | Lemma 5: \(\sum_k|\hat b_k|=1\) at real \(\beta\); \(\rho_0\le2.17565\); the majorant \(H\) | **ACCEPTED** | The sign-alternation proof is correct (C1: \(\sum|\hat b_k|=1.000000000000\), \(\rho_0(\beta_0)=2.175644\)). The rank rule gives \(\tfrac12(2d\cdot r+2|k|\cdot dr+2r\cdot d)=(|k|+2)dr\), an implication of (b5). \(H(0.55),H(1),H(1.994573)\) are reproduced (C4). |
| (a6) | Prop. 6 and the budget table; full rate ≤ 1.646 at \(A(h)\le1.9946\) | **ACCEPTED as an implication** of (b1*)/(b1), (b2)–(b5) | Audit C4 recomputes \(\beta_{\max}\) and \(A_{\max}\) from the printed \(\lambda_S,C_S\) and gets the same \(A_{\max}\) (0.6179, 0.2462, 0.4029, 0.4007). The \(\beta_{\max}\) differ by \(\le3\cdot10^{-5}\) because the printed \(\lambda_S,C_S\) are rounded up. **Rounding-direction error (minor):** section 5 prints the allowance as "\(X\le\) up(\(x_0\)+10⁻⁶)". The certified statement is a lower bound, \(X\ge\beta_{\max}\sqrt N\), so the printed values are 1–3·10⁻⁴ too large and carry the wrong sign. Corrected: \(X\ge1.5422\) (A, b1*); \(\ge1.9120\) (π₁, b1, m0=3); \(\ge1.1284\) (π₁, b1*). The "Exact remaining gap" constant "1.5424" should read 1.5422. |
| Summary item 2 | **"h-linear allowance in π₁ restored to 1.912"** | **CONDITIONAL; misleading as a headline** | The 1.912 uses (b1): \(p_0=0.01272\) and \(c(M)\) carried over verbatim to π₁. Lemma 4 supports the \(c\) part in π₁. It gives only \(\pi_1(R_{602})\le2A(R_{602})<0.02544\) for \(p_0\), not \(<0.01272\). No source shows \(\pi_1\le P_{5000}\). Under the report's own re-derived constants (b1*), the π₁ allowance is **≈1.128** (h-higher not charged). That is barely above the Round 182 audit's 1.094. **The genuine restoration is in the dimension price \(A\):** allowance ≥ 1.542, requirement \(A(h)<0.6179\), conditional on (b1*). The report says this itself ("the best price is the plain dimension price"), but the summary's π₁ sentence should carry the condition. |
| (b1*)–(b5) | Inherited/conditional inputs | Honest | (b3) (H1)/(H2) for π_α and (b1*) are the two cheapest things to check. |
| (c1)–(c3) | Picard diagnostic, FFT cross-checks | Honest as evidence | The replay is identical. "Any proof that prices h₁ and h − h₁ separately ends at ≈0.68" uses \(A(h-h_1)\ge\sup|h-h_1|\approx0.19\) (floating) and \(A(h_1)=0.4946\) (model value at \(t=a\), not on all of \(Q\)), so it is evidence. |

Mission compliance:
- \(L_S\) is re-priced with the seed-only Taylor terms included, and its exact \(m\)-step growth is computed.
- The h-linear term is priced with an explicit \(\rho_0\) and \(A(h)\).
- It is stated whether \(c(M)\) survives in π₁: yes, verbatim.
- The new price's \(p_0\), \(c\) and sup domination are given as implications. (H1)/(H2) are left as hypotheses, which the mission asked to be proved; this is honestly flagged.
- Exact and floating material are kept separate.
- Brackets are outward everywhere except the \(X\) allowance printout.

## 4. Report R: `native-claude-ordinary-prime-row-deleted-one-match-183.md`

| Item | Statement | Verdict | Notes |
|---|---|---|---|
| (a1) | Prop. 1.1: \(\sum g^2=(p-1)\sum\omega^2=n\mathcal E(\nu)\), \(G=n\sum\nu^2\); the mission's factor 2 is wrong | **ACCEPTED** | With the Round 166 lift convention (each square character has two lifts, each with weight \(\lambda_d/2\)): \(\sum_\alpha\omega^2=\tfrac12\sum\lambda_d^2\) and \(\sum g^2=n\sum\lambda_d^2\). Audit R5 (float) checks \(\sum g^2=n\mathcal E(\nu)\) and \(G=n\sum\nu^2\) at p=101, 197 for random laws. |
| (a2) | Prop. 1.2: on (NC), \(G_{-\rho}=O(1)\), \(G=(1+o(1))\sqrt p\), \(M_1=(1+o(1))p\); **the balance part of (H_sat) is false**; Lemma S2 is tight at χ | **ACCEPTED on (NC)** | The input is `ordinary-prime-coset-spread-151.md` line 41: the quadratic-form ratio is \(O(L/\sqrt p)\) and "is the relative integral of \((1-\rho\chi(1-x))|f(x)|^2\) on \(Q\)". This is an intermediate step in the proof of Round 151's accepted item 3, under exactly R's hypotheses (\(b\ge0\), \(b_0=0\), \(\|L_\sigma b\|\le Cr\), \(L\le p^{1/12}\)), with the same \(f=\sum b_jj/\sum b_j\). The integrand is \(2g\) on \(T_{-\rho}\), \(0\) on \(T_\rho\) and \(1\) at \(x=1\). On (NC), \(L\to1\) and \(G=n/m_{\rm eff}\sim\sqrt p\). The \(M_1\) bounds follow from the mask. **Label:** "false for the actual law" means false on the near-critical branch (NC), the standing hypothetical sequence of the ordinary route. It is not an unconditional statement. |
| (a3) | Cor. 1.3: \(\|\pi\|^2\ge(1-o(1))p(\sum g^2-C_2-2)\); "b1′ saturated iff \(\sum g^2\gg\sqrt p\)" | **ACCEPTED WITH CORRECTION** | The lower bound follows from accepted Round 182 Prop. 4 restricted to \(T_\rho\), with an additive \(-o(p)\) that is harmless. **Correction:** only the forward direction is proved. If \(\sum g^2=o(\sqrt p)\), the \(s=1\) row contributes \(\le G^2\sum g^2=o(p^{3/2})\), but that does not show \(\|\pi\|=o(p^{3/4})\). Read: "the \(s=1\) row forces \(\|\pi\|\gg p^{3/4}\) iff \(\sum g^2\gg\sqrt p\)". |
| (a4) | Prop. 1.4: \(\sum g^2/\sqrt p=\mathcal E(S)/|S|^3+o(1)\le\tfrac12+o(1)\) on (NC) | **ACCEPTED on (NC)** | The Round 20 gap theorem (`anchored-repair-20.md` lines 66–72) was checked: if \(m_{\rm eff}\le(1+\xi)m_0\) and \(\mathcal E(S_\tau)\ge(\tfrac12+\Delta)|S_\tau|^3\) then \(\|LE\|\ge\epsilon\|E\|\) on either sign, with \(S_\tau\) defined exactly as R uses it. The flattening \(e=m_0^{-1/2}1_S+o_{\ell^2}(1)\), \(|S|\sim m_0\) is proved inside the same Round 20 argument (line 76), as well as cited from Round 151. Checked: the norm \(N(\eta)=n^{-1/4}\|\hat\eta\|_4\), \(\mathcal E(\eta)\le\|\eta\|_2^2\|\eta\|_1^2\), the \(\ell^1\) cost of \(S\triangle S_\tau\), and the triangle inequality for \(N\). Status of \(\sum g^2\): open in \([O(1),(\tfrac12+o(1))\sqrt p]\), as R says. |
| (a5) | Prop. 2.1: exact I/S/P/G split of every trace | **ACCEPTED** | The replay passes (`--check`). The audit's independent code (R1) splits Δ by pair type and verifies the cubic class decomposition of the row-deleted trace exactly at p=29, 37, 41, 53. |
| (a6) | Prop. 2.2: \(\|\pi(\Delta_I+\Delta_S)\|\le X\); \(\max L_z^2\le\|\pi(\Delta_I+\Delta_P)\|\le\sum L_z^2\le GM_1\); **b1″ ⟺ \(\|R\pi(\Delta_G)R\|=O(p^{3/2})\)** | **ACCEPTED** | Re-derived: \(\pi(\mu_r)e_\eta=\hat\mu_r(\eta/r)e_{\eta/r}\); \(v_z=\mathbf 1-p\delta_z\) is fixed by maps fixing \(z\); \(L_z\le G\). Audit R4 (float) checks diagonality, the sandwich and the difference bound at p=29–53. **Note:** the equivalence needs only \(X\le GM_1=O(p^{3/2})\), not the BSG-based \(O(p^{34/23})\). |
| (a7) | Prop. 2.3: III \(p^4\), IIX \(p^{139/32}\), **IXX \(p^{150/32}\)**, XXX \(p^{177/32}\) | **ACCEPTED** | \(A=cRPR+Z\) because \(\pi(\Delta_I)=cP\). The cyclic expansion is exact (R1, exactly). \(0\le RPR\le I\). \(\operatorname{tr}Z^2\le\|\pi(\Delta-c\delta_{\rm id})\|_{HS}^2=p(\mathcal E-c^2)-\sum_a(\cdot)^2\) (R1 checks \(\operatorname{tr}Z^2\le p(\mathcal E-c^2)\) and \(0\le\)IXX\(\le3cp(\mathcal E-c^2)\) exactly). With \(c\le M_1\le G^2=O(p)\) and the accepted \(\mathcal E(\mu)=O(p^{43/16})\) (Round 180), the exponents are: IXX \(2+43/16=150/32\); IIX \(5/2+59/32=139/32\); XXX \(|\operatorname{tr}Z^3|\le\|Z\|\|Z\|_{HS}^2\), \(59/32+118/32=177/32\); III \(4\). Needed: \(144/32\). |
| (a8) | Prop. 2.4: six-word criterion ⇒ \(\mathcal E(\mu)=O(p^{5/2})\) when \(\bar a\gg p\) | **ACCEPTED** | The scalar inequality \(z(z^2-c_0z+2c_0^2)\ge0\), the variance step, \(\bar a\le2c\), and rows 0, 1 (\(\|F\|\le M_1\), the accepted Round 182 row bound) were re-derived. The k=2 trace identity is re-checked exactly (R3). The final inequality is checked exactly (R2). The error terms \(G^7/p\) and \(E^\times(m)/p\le M_1^2X/p\) are \(O(p^{5/2})\). The reading "(b-k3) is stronger than an unproved statement that already improves 115/64" is correct: \(\|\pi\|^4\le p\mathcal E\). |
| (a9) | Prop. 2.5: \(\mathcal E(\mu)\ll XM_1^2/p+X^{1/2}M_1^2+G\log p\,M_1^2\); point–plane floor \(p^{5/2}\) | **ACCEPTED** | The Round 178 inequality is quoted correctly (`ordinary-weighted-slope-product-incidence-178.md` line 29). \(\sum W^2\le XM_1^2\) and \(\sum W^{3/2}\le X^{1/2}M_1^2\). The floor follows from Hölder and \(M_1\asymp p\) on (NC). \(\varepsilon<3/16\iff7/4+\varepsilon/4<115/64\). **Sharpening:** the proof uses only \(\max_\xi W_\xi\), and \(W_\xi\le X\) by Cauchy–Schwarz. So the weakest sufficient input for the one-match improvement is \(\max_\xi W_\xi=O(p^{1+\varepsilon})\), \(\varepsilon<3/16\). The accepted analogue is Round 180's row-autocorrelation bound \(\sup_\lambda C(\lambda)=O(p^{11/8})\), which gives \(\sum_\xi W_\xi^{3/2}=O(p^{43/16})\). |
| (SL) | Candidate shared lemma \(X=O(p^{1+\varepsilon})\) | Agrees with the blind review | See §1 and the (a9) sharpening. R's remark that this "corrects" the Round 182 audit §4 is fair. Round 182's audit was about the then-current exponent 34/23, which does not help. A bound with \(\varepsilon<3/8\) would improve \(\mathcal E(\mu)\), and one with \(\varepsilon<3/16\) the covariance. |
| (c) | Exact model traces \(p\le677\) | Honest as evidence | The replay of p=101, 197, 293, 677 matches the report's tables line for line. IGG leads in every 0/1 sector model. The audit's random integer-weight checks at p=29–53 also show IXX at 65–70 % of \(\operatorname{tr}A^3\). |

Mission compliance:
- Part 1 decides the normalization and bounds \(\sum g^2\), citing Rounds 20/151 with line references.
- Part 2 computes exact traces by type at \(p\le677\).
- No point–conic theorem with valid hypotheses was found, and the report says so explicitly.
- The inconclusive return names the type (IGG in IXX) and its verified bound (150/32).

## 5. Replay log

Run from the repository root on 2026-11-21 with `.venv/bin/python` (numpy and scipy present; mpmath absent). "Matches" means the printed output equals the report's quoted output or table line for line.

| Script | Command | rc | Time / peak memory | Result |
|---|---|---|---|---|
| fibre identity | `.venv/bin/python -B research/paley-183-fibre-identity-check.py` | 0 | 1.1 s | Matches; `ALL OK` |
| fibre subgroups | `… paley-183-fibre-subgroup-energy.py 4100000` | 0 | 0.4 s / 690 MB | All 14 table rows match §6.2 |
| fibre models | `… paley-183-fibre-models.py 2000,20000` (quick subset; full run not repeated) | 0 | 13 s / 1.44 GB | All rows at p≈2000 and 20021 match §6.1 |
| cold power | `… paley-183-cold-seed-taylor-power.py` | 0 | 12.4 s | Matches (all 211 non-timing lines); `ALL EXACT CHECKS OK` |
| cold brute force | `… paley-183-cold-seed-taylor-bruteforce.py` | 0 | 22 s | Matches; `BRUTE FORCE CHECKS OK` |
| cold Picard | `… paley-183-cold-h-picard-diagnostic.py` | 0 | 0.7 s | Matches |
| rowdel check | `… paley-183-rowdel-trace.py --check` | 0 | 2.6 s | Matches; `all exact checks passed` |
| rowdel models | `… paley-183-rowdel-trace.py 101 197 293 677` (subset of the report's seven primes) | 0 | 183 s / 453 MB | Matches the quoted rows (e.g. `rand +1`, p=677: 0.15285, IGG +0.0947) |
| audit fibre | `.venv/bin/python -B research/paley-183-audit-fibre-check.py` | 0 | 1.4 s | `ALL FIBRE AUDIT CHECKS OK` |
| audit rowdel | `.venv/bin/python -B research/paley-183-audit-rowdel-check.py` | 0 | 0.5 s | `ALL ROWDEL AUDIT CHECKS OK` |
| audit cold | `.venv/bin/python -B research/paley-183-audit-cold-check.py` | 0 | 1.1 s | `ALL COLD AUDIT CHECKS DONE` (float replay; certifies nothing) |

Script hashes for the report scripts equal those quoted in the cold and rowdel reports (`803ac0dd…`, `70b99edc…`, `609fb8c8…`, `cfccf71b…`).

**Not checked:**
- the full fibre-model run at p=5000–80000;
- the rowdel models at p=401, 509, 577;
- the proofs of Shkredov's Theorem 6 and Reiher–Schoen Theorem 1.2;
- the text of Schoen 2015;
- (H1)/(H2) for any new price;
- the O(n^{-1/2}) corrections of Lemma 4(ii);
- the Round 57/80 weight calculus behind (b4)/(b-Jk);
- the upper side of Prop. 3 by an independent exact dual.

## 6. Ranked closeout

### 6.1 What Round 183 changes, obligation by obligation

| Obligation | Before (Round 182 acceptance) | After Round 183 (as audited) | Effect |
|---|---|---|---|
| One-match covariance, target \(O(p^{3/2})\) | \(O(p^{115/64})\). Criterion b1″ \(\|R\pi(\mu)\|=O(p^{3/4})\), via k=3: verified \(p^{177/32}\), need \(p^{144/32}\). b1′ saturated under (H_sat). | Exponent unchanged at 115/64. **b1″ ⟺ \(\|R\pi(\Delta_G)R\|=O(p^{3/2})\)** (generic class only; S/P classes cost \(O(p^{3/2})\)). The six-word criterion splits into (i) a necessary four-word part, \(\mathcal E(\mu)=O(p^{5/2})\) (verified \(p^{43/16}\), gap \(p^{3/16}\); IXX verified \(p^{150/32}\)), and (ii) GGG at \(p^{177/32}\). **New conditional:** \(\max_\xi W_\xi\le X=O(p^{1+\varepsilon})\) ⇒ covariance \(O(p^{7/4+\varepsilon/4}\log^{1/2}p)\), which improves 115/64 iff \(\varepsilon<3/16\). On (NC): (H_sat) balance is false but not needed; \(M_1=(1+o(1))p\); \(\sum g^2\in[O(1),(\tfrac12+o(1))\sqrt p]\), equivalent to \(\mathcal E(S)/|S|^3\). | reformulated |
| First mass \(\mathcal M_w\), target \(O(p^{1+1/1280})\) | \(O(p^{11/8})\); BSG + Young scheme capped at \(E^\times(h)=O(p^{4/3})\). | Exponent unchanged at 11/8. Keeping \(w\) gains exactly 3/4 in an (H1)/(H2)/(H4)-admissible coset family, so arguments using only those hypotheses must bound \(X=E_Q(h)\) itself at \(p^{1+1/1280}\). Coset supports with \(|H_i|^2<p\) closed (conditional on Shkredov Thm 6, now quoted). Spectral restriction and per-fibre Hölder are capped in that family. **The near-critical structure (Round 151 coset-mass exclusion, R's sector concentration) is not yet used and is the remaining lever.** | reformulated (new obstruction for (H1)/(H2)/(H4)-only methods) |
| Cold growing-prefix confinement | No price with \(\kappa_0<0.774\); frozen rate 1.066 (\(P_{5000}\)). Seed-only Taylor charge cut the π₁ allowance to ≈1.094. | Seed multiplier priced exactly with its Taylor terms: \(\lambda_S\le0.53244\), \(C_S\le1.3146\) (A, \(m_0=8\)). Under (b1*): \(\kappa^*_A=0.83790251\ldots\), allowance ≥ 1.542 in A, **requirement \(A(h)<0.6179\)** with \(\rho_0=2.17565\). π₁: allowance ≈1.128 (b1*); 1.912 only under the unsupported (b1) source transfer. Proved-type \(A(h)\le1.9946\) (b2) gives a full rate ≤ 1.646. Evidence: \(A(h)\gtrsim0.68\) for any separate-Picard pricing. | weakened (sharper criterion), conditional |
| Generic J sum \(O(p^{9/4})\); zero-match; cold complex stationary domain; derivative transfer; ETH target | open | unchanged | unchanged |
| BSG citation for \(E^\times(h)=O(p^{34/23})\) (Rounds 163/173/177/182) | "Schoen" form \(K^{-1/2}\), \(K^4\), not re-read | The form is Reiher–Schoen 2024 Thm 1.2 (constants depending on fixed ε), not Schoen 2015 (which has \(|A'|\gg|A|/K\)). The exponents stand; the citation needs correcting. | evidence / bookkeeping |

### 6.2 Precise remaining obligations

1. **Ordinary, shared:** \(X=\sum_rm(r)^2=E_Q(h)=O(p^{1+\varepsilon})\) for the actual near-critical \(g\). It needs \(\varepsilon\le1/1280\) for the first mass, and gives a power improvement of the one-match covariance for any \(\varepsilon<3/16\). The one-match use needs only the weaker \(\max_\xi W_\xi=O(p^{1+\varepsilon})\). Verified: \(X=O(p^{34/23})\) (BSG); Round 180 controls \(\sum_\xi W_\xi^{3/2}=O(p^{43/16})\) through the row autocorrelation \(\sup_\lambda C(\lambda)=O(p^{11/8})\).
2. **One-match, generic six-word class:** \(\|R\pi(\Delta_G)R\|=O(p^{3/2})\), equivalently GGG/XXX below \(p^{9/2}\) (verified \(p^{177/32}\)), together with \(\mathcal E(\mu)=O(p^{5/2})\).
3. **Near-critical support energy:** decide \(\mathcal E(S)/|S|^3\to0\) on (NC). This is equivalent to \(\sum g^2=o(\sqrt p)\) and would relax every operator target.
4. **Cold:**
   - \(A(h)<0.6179\) uniformly on \(Q\), both lifts, for \(h=V_{602}-S\), or a sharper product rule than \(\rho_0=2.17565\) for the actual non-seed simples (decisive: the transported fields \(K(J^{2i})\) of \(h_1\));
   - plus (b1*): \(A\le P_{5000}\) on the unshifted class, and the O(n^{-1/2}) corrections in \(A\);
   - plus (H1)/(H2) for \(A\).
5. Unchanged: generic J sum \(O(p^{9/4})\), zero-match estimate, cold uniform complex stationary domain and derivative transfer. The original target remains open.

### 6.3 Recommended Round 184 calls (most valuable first)

**1. `ordinary-prime-near-critical-slope-row-mass` (shared candidate; suggest `cand:slope-row-mass-X`).**
- **Question:** For the actual near-critical \(g\) on (NC), is \(\max_\xi W_\xi=O(p^{1+\varepsilon})\) for some \(\varepsilon<3/16\), where \(W_\xi=\sum_rm(r)m(\xi/r)\)? And is \(X=E_Q(h)=O(p^{1+1/1280})\)? The proof should use the near-critical structure that the (H1)/(H2)/(H4)-only arguments ignore: sector concentration (R Prop. 1.2), the flat law on \(|S|\sim m_0\), and Round 151's fixed Fourier mass outside coset unions.
- **Why now:** both ordinary calls of Round 183 reduced to this one estimate. F shows that (H1)/(H2)/(H4) alone force a bound on \(X\) itself, because \(w\) is worth only 3/4 in the \(g_H\) family, which is not near-critical. R shows that \(\varepsilon<3/16\) already moves the headline one-match exponent.
- **Scope:**
  - actual \(\mu\), \(h(z)=g(1-z)\), counting norms;
  - state each (NC) input with its round and line;
  - keep the max-convolution and the \(X\) versions separate;
  - models must be near-critical (flat law with \(m_{\rm eff}\sim m_0\), sector-concentrated), not \(g_H\).
- **If yes:** \(\varepsilon<3/16\) gives one-match covariance \(O(p^{7/4+\varepsilon/4+o(1)})<115/64\). \(\varepsilon\le1/1280\) for \(X\) closes the first mass and \(\mathcal D_0+\mathcal D_1=O(p^{3/2})\).
- **If no:** a near-critical admissible family with \(X\ge p^{1+\delta}\) shows that the shared route needs signed cancellation from \(w\) (first mass) and a non-point–plane input (one-match).
- **If inconclusive:** return the best exponent for \(\max W\) and for \(X\) from (NC) structure, and the exact level-set configuration that blocks.

**2. `cold-prime-h1-product-rule` (cold).**
- **Question:** In the two-fibre calculus, what is the exact per-simple \(A\)-price ratio of \(F\mapsto K(\Phi_t''(S)h_1F)\)? Here \(h_1=2\sqrt t\sum b'_kK(J^k)\) is the first Picard piece. Does it leave room under \(\beta_{\max}=0.19359\) for \(h-h_1\)? In the same call, check (b1*), \(A\le P_{5000}\) on the unshifted class, and the O(n^{-1/2}) corrections of Lemma 4(ii) in \(A\).
- **Why now:** Round 183 made the seed part exact and moved the whole budget to the non-seed h-linear term in the dimension price, with a sharp requirement \(A(h)<0.6179\) at \(\rho_0=2.17565\). The h₁ simples have exactly known weights, and the generic word rule is the only crude step left.
- **Scope:**
  - compact model with the Round 57/80/126 weight calculus for tensor products of two-fibre simples, stated as a hypothesis where not proved;
  - exact LP as in Prop. 3;
  - outward rounding, including allowances printed as lower bounds;
  - (H1)/(H2) for \(A\) stated or proved.
- **If yes:** a certified ratio leaving \(A(h-h_1)\lesssim0.19\) feasible makes the A-price route alive, with the remaining input a certified \(A(h-h_1)\).
- **If no:** a ratio \(\ge2-o(1)\) on the h₁ simples retires the per-simple A route, and the cold route goes back to Criterion D or sup transfer.
- **If inconclusive:** return the exact ratio for the \(K(J^{\pm2})\) part and the remaining budget.

**3. `ordinary-prime-near-critical-support-energy` (ordinary, structural).**
- **Question:** On (NC), does the flat support \(S\) satisfy \(\mathcal E(S)=o(|S|^3)\), or is there a near-critical configuration with \(\mathcal E(S)\asymp|S|^3\) (necessarily \(\le\tfrac12|S|^3\))? Equivalently: is \(\sum g^2=o(\sqrt p)\)?
- **Why now:** R reduced \(\sum g^2\) exactly to this energy and capped it at \(\tfrac12\) through Round 20. It is the gate for (b1‴) and for relaxing the IXX requirement by \(p^{2\delta}\). It is an old regime: "the broad-support and low-energy prime regimes" have been unresolved since Round 20. Rank it below call 1, because neither ordinary headline moves without call 1.
- **Scope:**
  - near-critical branch only;
  - Round 20 gap and Round 151 coset-mass exclusion as accepted inputs;
  - say explicitly which energy range \((\delta|S|^3,\tfrac12|S|^3)\) is excluded.
- **If yes:** every operator target relaxes by \(p^{\delta/2}\) when \(\mathcal E(S)=O(|S|^3p^{-\delta})\); the \(s=1\) row becomes negligible.
- **If no:** b1′ is exactly critical, and the one-match route must go through the generic six-word class.
- **If inconclusive:** return the largest excluded energy constant below \(\tfrac12\).

Not recommended now:
- the generic GGG six-word incidence count. No input with valid hypotheses is known, and call 1 would already move the headline exponent.
- the open exact coset subclass \(\sqrt p\le|H|\le2C_{\rm cap}\sqrt p\) of F. It is not near-critical.
