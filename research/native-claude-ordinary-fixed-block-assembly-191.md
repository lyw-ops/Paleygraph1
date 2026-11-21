# Round 191 native Claude draft: assembling fixed moderate blocks (obligation (A))

- **Author:** Claude subagent started by the Round 191 coordinator (session/r191-assembly). Call id `ordinary-fixed-block-assembly`.
- **Status:** agent draft, written while the user was asleep. It is not an acceptance record, a human review or a mathematical certification. No new incidence estimate is proved. Every composition of accepted statements is marked **bookkeeping (unaudited)**.
- **Mission:** `coordination/missions/round-191/ordinary-fixed-block-assembly.md`, exported from `coordination/round-190.json` (SHA-256 `b8f6e40f…84c05cc`, matches).
- **Sources checked (SHA-256 all match the mission):** `research/round-189-acceptance.json` (`ad4e0b5a…6506`), `research/round-190-acceptance.json` (`11c42c0a…409b`), `research/native-claude-audit-190.md` (`6237bffb…7b80`), `research/native-claude-ordinary-obligation-map-stocktake-190.md` (`bced35fc…442c8a`).
- **Also read:** `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-190.md`; `proof_scope` and `failed_paths_and_open_bounds` of acceptance records 152–166 and 182–190; the route notes of the reduction in full: R152 `ordinary-affine-correlations-152.md`, R153 `ordinary-affine-jacobi-factorization-153.md`, R154 `ordinary-lift-and-gauss-kernel-154.md`, R155 `ordinary-crossratio-affine-chart-155.md`, R156 `ordinary-sign-selective-completion-156.md`, R157 `ordinary-marked-frequency-localization-157.md` and `ordinary-five-root-trivial-slices-157.md`, R158 `ordinary-prime-near-unit-slope-spread-158.md`, R159 `ordinary-quantitative-near-unit-slope-159.md` and `ordinary-single-lift-ratio-law-159.md`, R160 `ordinary-matched-physical-truncation-160.md` and `ordinary-rank-two-slope-orthogonality-160.md`, R162 `ordinary-physical-slope-fiber-count-162.md`, R163 `ordinary-shifted-layer-energy-saving-163.md`, R164 `ordinary-physical-pair-slope-pinning-164.md`, R165 `ordinary-physical-collision-two-copy-165.md`, R166 `ordinary-regular-character-collisions-166.md`; R172 `ordinary-full-diagonal-affine-172.md`:1–10; R180 `ordinary-paired-J-cross-ratio-180.md`:40–80; R183 `native-claude-ordinary-prime-first-mass-fibre-dilation-183.md`:1–80.
- **Scripts (new):**
  - `research/paley-191-assembly-exponents.py` (exact Fractions). Part A checks every loss exponent below. Part B checks the identity of Proposition 2 exactly at \(p=13,17,29,37,41\) for arbitrary rational weights. Run `python3 research/paley-191-assembly-exponents.py` (prints `ALL OK`).
  - `research/paley-191-assembly-models.py` (floating, **evidence only**; needs numpy). Run `.venv/bin/python -B research/paley-191-assembly-models.py` (about 5 s).

Citations: "R*n* file:line" for route notes, "R*n* acc:line" for `research/round-n-acceptance.json`. Exponents are powers of \(p\). Notation as in the Round 190 stocktake: \(g=|f|^2\), \(w=g(1-g)\), \(G=\sum g\), \(F(x)=f(1-vx)\) on physical \(x\in Q\) with \(1-vx\in Q\), vertex values \(A_x=1-vx\), \(C_x=1-vux\), slope \(t=C_yA_x/(C_xA_y)\), \(P_t\) the completed nonnegative majorant of R166 `ordinary-regular-character-collisions-166.md`:7–11. \(D=E^{-1/2}/\log(2/E)\), \(E=e+p^{-1/2}\), is the slowly diverging factor of the conditional lower bound (R157:39–41, R160:27).

---

## 0. Answer in brief

1. **No.** \(O(p)\) for every fixed moderate block, together with every cut already paid, implies neither the \(O(p)\) favorable off-diagonal nor the contradiction on the critical branch. This holds for every closing form of the blocks (\(\mathcal M_w\), \(X\), \(\mathcal D\)). The R157/R160 device pays only **vertex** cuts of squared mass \(o(D)\); it does not apply to slope cuts (R160 `ordinary-matched-physical-truncation-160.md`:27, last two sentences).
2. **Assembly inequality (Proposition 1, bookkeeping).** For every vertex level \(a\in(0,1]\), with \(F_{\ge a}=F\,\mathbf 1\{g(1-vx)\ge a\}\) and \(m_{<a}=\|F-F_{\ge a}\|_2^2\),
\[
c_1\,pD\ \le\ \mathcal M_\nu(F)\ \le\ 2\|F\|_2^4+2\sum_{t\ne1}|f(t)|\,P^\natural_t(\ge a)+O(p\,m_{<a}),
\qquad P^\natural_t(\ge a)\le a^{-2}P_t^{(\ge a)} .
\]
   It needs no favorable/wrong-sign split and no slope cut.
3. **The slope part of (A) is closed by \(X=O(p)\), not by \(\mathcal M_w=O(p)\)** (Proposition 2, bookkeeping, checked exactly). \(\sum_{t\ne1}P_t=X_c-\mathrm{diag}\), where \(X_c=X+O(p)\). So \(X=O(p)\) pays every slope \(t\ne1\) at a fixed vertex level, including the bands \(p^{-(1-4/445)}<g<s_0\) and the near-unit slopes, at cost \(a^{-2}X\). Under \(\mathcal M_w=O(p)\) the same pieces lose:
   - \(p^{\sigma/2}\) on a slope band \(g\asymp p^{-\sigma}\); the worst case is \(441/890\), or \(441/1780\) after combining with R163;
   - a factor \(1/(1-g(t))\) near unit slopes, which no accepted statement bounds; combined with R159 and R162 the loss is \(3/7\), and up to \(1/2-o(1)\) when \(E\) is large.
4. **The vertex part of (A) is untouched by every first-mass form.** Under \(X=O(p)\), (A) is exactly the vertex-layer increment estimate
\[
\text{(A}_V)\qquad \sqrt{\mathcal M_\nu(F)}-\sqrt{\mathcal M_\nu(F_{\ge a})}=o(\sqrt{pD})\quad\text{for one fixed }a\in(0,\tfrac12],
\]
   with all slopes and signs kept. Its only accepted price is R160's \(2\sqrt{n\max\nu}\,\|F\|_2\,m_{<a}^{1/2}\asymp(p\,m_{<a})^{1/2}\). So (A\(_V\)) holds under **vertex tightness**: (V) \(m_{<a}=o(D)\), robustly \(O(1)\), for one fixed \(a\).
   - (V) implies \(\sum g^2\gg\sqrt p\), the high-energy alternative that R183 acc:270 records as open.
   - R183 acc:264 (Prop. 1.4) forces \(a\le\frac12+o(1)\).
   - Flat and \(D_\theta\) model laws (R190 acc:295, Theorem 4, evidence only) violate (V): \(m_{<0.05}\approx0.28\)–\(0.50\sqrt p\).
   - The loss of the R160 device on the layers \(C^2/p<|F|^2<a\) is \(p^{1/2}\) against \(O(p)\), and between \(p^{1/4}\) and \(p^{1/2-o(1)}\) against \(o(pD)\).
5. **Correction to the mission's range.** R160:27 deletes \(|F|\le C/\sqrt p\), that is \(|F|^2\le C^2/p\). So the unpaid vertex layers are \(C^2/p<|F|^2<a\), not \(C/\sqrt p<|F|^2<a\). The layer \(|F|^2\asymp p^{-1/2}\) is unpaid; it carries all the vertex mass of flat laws.
6. **Answers to the three sub-questions.**
   - \(\mathcal M_w=O(p)\): implies neither part of (A).
   - \(X=O(p)\): implies the slope part completely, but not (A\(_V\)).
   - The weighted first mass with the true vertex and slope amplitudes kept, \(\mathfrak M^\natural:=\sum_{t\ne1}|f(t)|P^\natural_t=O(p)\): implies the contradiction directly, with no assembly (bookkeeping). But it is strictly stronger than the target on admissible laws. It is \(\asymp p^{7/4}\) in flat and \(D_\theta\) laws, where \(X\approx1.4p\) and \(\mathcal M_\nu\approx0.4p\) (evidence). So neither \(X=O(p)\) nor \(\mathcal M_w=O(p)\) implies it, and no accepted estimate approaches it.

**Verdict: no** (§10). Record (A) as a separate ordinary obligation with the exact form (A\(_{\rm unif}\)) of §6. With \(X\) (or \(\mathcal M_{\sqrt g}\)) as the fixed-block target, (A) reduces to the vertex statement (A\(_V\)).

---

## 1. The accepted reduction, traced

**Top level.**
- **R152** `ordinary-affine-correlations-152.md`:3–13: the cap inequality \(L^2(1+D_g)\log(\cdots)\gg\min(\eta_g^{-1/2},p^{1/4})\).
- R152:58–63: averaging in the true anchor law \(\nu\) turns \(\mathcal M_\nu(F):=\mathbb E_\nu\sum_{u\ne1}|C_a(u)|^2\) into the five-factor sum
\[
\mathcal M_\nu(F)=\sum_{u\ne1}\sum_{x,y}F(ux)\overline{F(x)F(uy)}F(y)\,f(t).
\]
- R152:65–69: \(\mathcal M_\nu(F)/p\to\infty\) on the critical branch.
- **R153** `ordinary-affine-jacobi-factorization-153.md`:5–11: the cap \(\max\nu=O(p^{-1/2})\).
- **R154** `ordinary-lift-and-gauss-kernel-154.md`:79–93: the diagonal and the wrong sign cost \(O(p)\). "The actual remaining test is an \(O(p)\) signed upper on the favorable off-diagonal" (line 93).

**Conditional lower bound.**
- **R157** `ordinary-marked-frequency-localization-157.md`:7–17: the phase arc \(I_{\rm arc}\). An \(O(p)\) upper on \(\sum_{a\in I_{\rm arc}}\nu_aM_a\) or on \(S^{\rm add}_\rho\) would exclude the branch.
- R157:21–43: \(D_{g_a}\gg E^{-1/2}/\log(2/E)\), hence \(\sum_{I_{\rm arc}}\nu_aM_a\gg pD\). Since \(M_a\ge0\), \(\mathcal M_\nu(F)\ge\sum_{I_{\rm arc}}\nu_aM_a\gg pD\).

**Cuts and blocks.**
- **R160** `ordinary-matched-physical-truncation-160.md`:3–27, the **device**.
  - For \(\mu\le\nu\), \(\|C_{G,H}\|_{\ell^2(\mu,u)}\le\sqrt{n\max\nu}\,\|G\|\|H\|\).
  - Hence \(|\|C_{F,F}\|-\|C_{G,G}\|\|\ll\sqrt p\,\|F-G\|\) for a hard cut.
  - Physical squared mass \(O(1)\) can be deleted at the \(O(p)\) target. Mass \(o(D)\) keeps the lower bound \(\gg pD\).
  - "These are cuts among the original four physical factors. They impose no bound on cutting the slope weight \(f_{\rm arc}\) itself."
- R160:29–38: quadratically small pair cuts cost \(O(p)\).
- R160 `ordinary-rank-two-slope-orthogonality-160.md`:57–61: the five-factor flattening \(\sqrt{p-4}\prod_j\|h_j\|\). It pays the case of three amplitudes \(\le p^{-1/2}\). The general condition is \(\sum_j(\alpha_j-\frac14)_+\ge\frac34\).
- **R155** `ordinary-crossratio-affine-chart-155.md`:20–22: slope families with \(\sup_u\sum_{t\in E_u}|f(t)|=O(1)\) cost \(O(p)\).
- **R156** `ordinary-sign-selective-completion-156.md`:37, 68–76: slope multipliers with Mellin coefficient sum \(K\) cost \(O(Kp)\). The filtered favorable sum is \(O(p(K+n\|\mu\|_\infty))\).
- **R158**:3–5, 43 and **R159** `ordinary-quantitative-near-unit-slope-159.md`:8–12, 59–63: near-unit counts, \(|W_\epsilon|/\sqrt p\ll(E+\epsilon)^{1/6}\log^{1/3}(2/(E+\epsilon))\).
- R159:96–100: the \(|f|^{2k}\) filter gives only \(o(p^{3/2})\). "This does not control \(S_{\rho,1}\) at the required \(O(p)\) scale."
- **R162** `ordinary-physical-slope-fiber-count-162.md`:3–30, the **block**.
  - Four vertex levels \(\mathcal A=\{g\ge a\}\) (for \(A_x,A_y\)) and \(\mathcal B=\{g\ge b\}\) (for \(C_x,C_y\)).
  - \(N_t\le\min(|\mathcal A|^2,|\mathcal B|^2)\), and \(|\text{block}|\le\sum_{t\in D}|f(t)|N_t\).
  - Line 30: "The moderate slope band with growing first mass and \(\sigma<1\) remains open."
- **R163** `ordinary-shifted-layer-energy-saving-163.md`:58–65: slope cuts with \(g(t)\le p^{-\sigma}\) cost \(O_{a,b}(p)\) for \(\sigma\ge1-4/445\) (any \(a,b>0\)), and for better floors when the thresholds exceed \(1/2\). Line 80 gives \(\sigma\ge26/27\) when both exceed \(1/2\). Line 66: "It leaves fixed moderate slopes and the uncut ordinary target open."
- **R164** `ordinary-physical-pair-slope-pinning-164.md`:20–25: \(\gamma=1/54\) or \(1/211\), for one threshold above \(1/2\). Line 43: \(N_t\ll p^{1-\gamma}\). Lines 47–54: \(\sigma\ge1-2\gamma\). R164 acc:206: "The full O(p) moderate band remains open."
- **R165** `ordinary-physical-collision-two-copy-165.md`:43: rows with \(h(u)\le H\) cost \(O(Hp)\) at fixed thresholds.
- **R166**:7–11: \(N_t\le(a^2b^2)^{-1}P_t\). R166:42–44: \(w\ge s_0(1-s_1)\) on the band.

**What the chain needs.** Every accepted *upper* bound on the favorable sum is stated at **fixed** vertex thresholds \(a,b>0\), with constants \(O_{a,b}\); the exceptions are the universal devices (R155, R156, the R159 filter, and R160's cut, pair cut and rank-two flattening). Examples are the R162 counts (both cardinalities \(O(\sqrt p)\) "by Parseval" at fixed thresholds, line 30), the R163/R164 incidence savings and the R166 majorant. The "fixed moderate block \(O_{a,b,s_0,s_1}(p)\)" of R190 acc:294 (B1, audited) inherits this.

---

## 2. What fixed-block bounds give, and the only free assembly

**Fact (bookkeeping).** Suppose \(|\text{block}(a,b,s_0,s_1)|\le C(a,b,s_0,s_1)\,p\) for every fixed block. Since \(D\to\infty\) along the branch, a diagonal choice of slowly moving thresholds \(a_p,b_p,s_{0,p}\to0\), \(s_{1,p}\to1\) gives
\[
|\text{block}(a_p,b_p,s_{0,p},s_{1,p})|=o(pD).
\]
Fixed-block constants therefore cost nothing: the lower bound has no rate, so any finite constant is absorbed. This is the only assembly that comes free.

**What it leaves.** The complement at the moving thresholds:
- the slopes \(g(t)<s_{0,p}\) and \(g(t)>s_{1,p}\), \(t\ne1\);
- every term with a vertex below \(a_p\) or \(b_p\).

Each needs an \(o(pD)\) bound. No accepted statement gives one:
- **Low slopes.** R163 needs \(g(t)\le p^{-(1-4/445)}\) (and R164 \(p^{-(1-2\gamma)}\)), a power, not \(s_{0,p}\to0\) slowly.
- **Near-unit slopes.** R159 bounds only their number.
- **Low vertices.** The only accepted price is R160's \(p\cdot m_{<a}\) (§5).

So fixed blocks plus paid cuts leave exactly the three families named in the audit (R190 acc:294; audit §3.5). The answer to the first question is **no**. The rest of this note gives the exact form of what is missing.

---

## 3. Proposition 1: the assembly inequality (bookkeeping, unaudited)

**Statement.** On the R157 critical branch (R157:3, hypotheses of R160:3), for every \(a\in(0,1]\):
\[
c_1\,pD\ \le\ \mathcal M_\nu(F)\ \le\ \Big(\big(\|F_{\ge a}\|_2^4+\mathfrak M^\natural(\ge a)\big)^{1/2}+2\sqrt{n\max\nu}\,\|F\|_2\,m_{<a}^{1/2}\Big)^2,
\]
where
\[
\mathfrak M^\natural(\ge a)=\sum_{u\ne1}\sum_{x\ne y}|F_{\ge a}(ux)F_{\ge a}(x)F_{\ge a}(uy)F_{\ge a}(y)|\,|f(t)|\ \le\ \sum_{t\ne1}|f(t)|P^\natural_t(\ge a)\ \le\ a^{-2}\big(X_c^{(\ge a)}-\mathrm{diag}\big).
\]
Here \(P^\natural_t(\ge a)\) sums \(\sqrt{g(A_x)g(C_x)g(A_y)g(C_y)}\) over completed triples at slope \(t\) with all four vertex values \(\ge a\). \(X_c^{(\ge a)}\le X_c\) is the level-restricted slope-row moment.

Since \(n\max\nu=O(\sqrt p)\) (R153:5–11) and \(\|F\|_2^2\le G=O(\sqrt p)\) (R160:20), the statement implies
\[
D\ \ll\ 1+\frac{\mathfrak M^\natural(\ge a)}{p}+m_{<a}\ \le\ 1+\frac{X_c}{a^2p}+m_{<a}.
\]

**Proof.**
1. **Lower bound.** \(\mathcal M_\nu(F)=\|C_{F,F}\|^2_{\ell^2(\nu,u)}\ge\|C_{F,F}\|^2_{\ell^2(\nu1_{I_{\rm arc}},u)}\gg pD\), by \(M_a\ge0\), R157:39–41 and R160:25–27.
2. **Cut.** \(F_{\ge a}\) is a hard physical cut of all four vertex rows, so \(\|F_{\ge a}\|\le\|F\|\). By R160:13–23 with \(\mu=\nu\) (allowed, \(\mu_a\le\nu_a\)):
\[
\sqrt{\mathcal M_\nu(F)}\le\sqrt{\mathcal M_\nu(F_{\ge a})}+\|C_{F,E}\|+\|C_{E,F_{\ge a}}\|,\qquad E=F-F_{\ge a}.
\]
   Each cross term is at most \(\sqrt{n\max\nu}\,\|F\|\|E\|\).
3. **Kept part.** The R152:58–63 expansion is linear algebra in the rows, so it holds for \(F_{\ge a}\):
\[
\mathcal M_\nu(F_{\ge a})=\sum_{u\ne1}\sum_{x,y}F_{\ge a}(ux)\overline{F_{\ge a}(x)F_{\ge a}(uy)}F_{\ge a}(y)f(t).
\]
   - The diagonal \(x=y\) has \(t=1\), \(f(1)=1\) (R154:77), and is at most \(\|F_{\ge a}\|^4\).
   - Off the diagonal use \(|f(t)|\le1\) only on the sign, keeping \(|f(t)|\) as a weight. The vertex product equals \(\sqrt{g\,g\,g\,g}\le a^{-2}g\,g\,g\,g\) because every factor is \(\ge a\).
   - Completing the physical square masks positively, as in R166:9–11, enlarges the sum to \(\sum_{t\ne1}|f(t)|P^\natural_t(\ge a)\le a^{-2}\sum_{t\ne1}P^{(\ge a)}_t\).
   - Proposition 2 below identifies the last sum with \(X_c^{(\ge a)}-\mathrm{diag}\).

**Remarks.**
- Proposition 1 bypasses the favorable/wrong split of R154. It uses absolute values on every off-diagonal term, so it does not need R154's quantitative pin.
- It is an inequality about the actual moment, for every \(a\). Its content is the trade-off between the positive majorant above level \(a\) and the R160 price below it.
- The models confirm both displayed inequalities numerically at \(a=0.1\) (§8, column "R160 ok", "Prop1 ok"). This is evidence only.

---

## 4. Proposition 2: \(X\) is slope-complete; \(\mathcal M_w\) is not

**Proposition 2 (bookkeeping; exact check).** With \(c(u)=\sum_{x\in\mathbb F_p}g(A_x)g(C_x)\), \(X_c=\sum_{u\in Q\setminus\{1\}}c(u)^2\) and \(\mathrm{diag}=\sum_u\sum_xg(A_x)^2g(C_x)^2\):
\[
\sum_{t\ne1}P_t=X_c-\mathrm{diag},\qquad P_1=\mathrm{diag}.
\]
The same holds with \(g\) replaced by \(g\mathbf 1_{\{g\ge a\}}\).

**Proof.**
- Expand \(c(u)^2\) as a sum over \((x,y)\) and group by slope.
- Because \(r_u\) is injective (R152:50), \(t=1\) exactly when \(x=y\) (R154:77).
- Substituting \(z=vx\) gives \(c(u)=c_h(u)+g(1)^2\cdot[\text{the }x=0\text{ term}]\), with \(c_h\) as defined in R183 `native-claude-ordinary-prime-first-mass-fibre-dilation-183.md`:47–49. So \(X_c=X+2\sum_uc_h(u)+O(n)=X+O(p)\), since \(\sum_uc_h(u)\le G^2\). The \(x=0\) term is the physical zero that R166:11 completes positively.

This refines R182 acc:260 (\(\mathcal M_w\le(E_Q(h)-\mathrm{diag})/4\)), which uses only \(w\le\frac14\). Part B of the exponent script checks both identities exactly for random rational \(g\) at five primes and two marks \(v\).

**Consequence (bookkeeping).** At every fixed vertex level \(a\), \(\sum_{t\ne1}|f(t)|P_t^\natural(\ge a)\le a^{-2}(X_c-\mathrm{diag})\). So \(X=O(p)\) pays **all** slopes \(t\ne1\) at once, at cost \(O_a(p)\). This covers:
- the bands \(p^{-(1-2\gamma)}<g<s_0\) (and \(p^{-(1-4/445)}<g<s_0\));
- the near-unit slopes;
- the slopes with \(g(t)=0\), which cost nothing in \(\mathcal M_\nu\).

**The slope-sharp weakening.** Since \(|f(t)|=\sqrt{g(t)}\),
\[
\mathcal M_w\ \le\ \mathcal M_{\sqrt g}:=\sum_{t\ne1}\sqrt{g(t)}\,P_t\ \le\ X_c-\mathrm{diag}.
\]
The middle form is the weakest first mass that is slope-complete, because its slope weight equals the true slope amplitude. The models give \(\mathcal M_{\sqrt g}/p\approx0.25\)–\(0.76\), \(\mathcal M_w/p\approx0.05\)–\(0.14\) and \((X_c-\mathrm{diag})/p\approx1.1\)–\(1.5\) (§8, evidence).

**Why \(\mathcal M_w\) is not slope-complete.** The ratio of true slope weight to \(w\) is \(|f|/w=1/(\sqrt g(1-g))\), unbounded at both ends. Exact losses at a fixed vertex level \(a\le\frac12\) (script Part A):

| piece | \(\mathcal M_w=O(p)\) alone | best accepted combination | loss exponent |
|---|---|---|---|
| band \(g(t)\asymp p^{-\sigma}\), \(0<\sigma<1-\frac4{445}\) (R163:61) | \(p^{1+\sigma/2}\) | \(\min(p^{1+\sigma/2},p^{3/2-2/445-\sigma/2})\) with R163:51–56 | alone up to \(441/890\); combined \(441/1780\), at \(\sigma=\frac12-\frac2{445}\) |
| same, one threshold \(>\frac12\) (R164:20–25, 47–54) | \(p^{1+\sigma/2}\), \(\sigma<1-\frac2{211}\) | \(\min(\cdot,p^{3/2-\gamma-\sigma/2})\) | \(209/422\); combined \(209/844\) |
| same, both thresholds \(>\frac12\) | \(\sigma<\frac{26}{27}\) | \(\gamma=\frac1{54}\) | \(13/27\); combined \(13/54\) |
| near-unit, \(1-g(t)\in[\epsilon,2\epsilon)\), \(t\ne1\) | \(p/\epsilon\), unbounded (no accepted lower bound on \(1-g(t)\); R158:3–5 allows \(o(\sqrt p)\) such slopes) | \(\min\big(p/\epsilon,\ p^{3/2-\gamma}(E+\epsilon)^{1/6}\log^{1/3}\big)\) with R159:59–63 and R162:9–11 (\(\gamma=0\)) or R164:43 | \((3-6\gamma)/7\) if \(E\le p^{-(6/7)(1/2-\gamma)}\): \(3/7\), \(627/1477\), \(26/63\). Otherwise \(\frac12-\gamma+\frac16\log_pE\), up to \(\frac12-\gamma-o(1)\) since \(E\) has no rate. So the loss is never below \((3-6\gamma)/7\). |
| all slopes under \(X=O(p)\) | — | \(a^{-2}X\) | **0** |

The rows with thresholds above \(\frac12\) apply to sub-blocks only. A single assembly cut needs \(a\le\frac12+o(1)\) (§5.3).

**Remark on the weight \(w\) and the queued sector call.** Wherever \(w/|f|\to0\), that is at \(g\to0\) and at \(g\to1\), a bound on \(\mathcal M_w\) leaves those slopes to be paid separately inside (A). R190's queued call `ordinary-first-mass-sector-obstruction` asks whether \(w\), small where \(g\approx1\), removes the sector pieces from \(\mathcal M_w\). If it does, the removed pieces are near-unit slopes, so they reappear in the slope part of (A). There they are paid only by an unweighted mass such as \(X\) or \(\mathcal M_{\sqrt g}\), which the R189 sector obstruction reaches. This is a structural observation, not a proof about the sector laws.

---

## 5. The vertex part: what remains under \(X=O(p)\)

### 5.1 Exact form

Assume \(X=O(p)\). Then \(\mathcal M_\nu(F_{\ge a})=O_a(p)\) by Proposition 1's kept part. So the contradiction holds along a sequence if and only if, for some fixed \(a\in(0,1]\),
\[
\text{(A}_V)\qquad\sqrt{\mathcal M_\nu(F)}-\sqrt{\mathcal M_\nu(F_{\ge a})}=o(\sqrt{pD})\qquad(\text{robust form: }O(\sqrt p)).
\]
(A\(_V\)) is one estimate covering every vertex layer below \(a\), with all slopes, both signs and the actual \(f(t)\) kept. It is signed, since it is a difference of norms. By R160:20–23 its accepted price is \(2\sqrt{n\max\nu}\,\|F\|\,m_{<a}^{1/2}\), so

**(V) vertex tightness:** \(m_{<a}=o(D)\) for one fixed \(a\); robustly, \(m_{<a}=O(1)\). Then (V) implies (A\(_V\)) (bookkeeping).

Since \(m_{<a}\) increases with \(a\), "\(O(1)\) for one fixed \(a_0\)" is equivalent to "\(O_a(1)\) for every \(a\le a_0\)". This is precisely what the R157/R160 device asks of the vertex layers: deleted squared mass \(o(D)\) (R160:27).

### 5.2 Loss of every accepted device on the layers \(C^2/p<g<a\)

- **R160 cut / pair cut.** The price is \(p\,m_{<a}\). The two-pair version R160:29–38 is homogeneous of degree one in each cut factor's norm, so by bookkeeping it gives the same \(p\,\eta_1\eta_2\le p\,m_{<a}\).
  - \(m_{<a}\) is at most \(G^{\rm vert}\le(1+o(1))\sqrt p\), and can equal \((1-o(1))\sqrt p\) (§5.3).
  - Loss against the robust \(O(p)\): **\(p^{1/2}\)**.
  - Loss against \(o(pD)\): \(m_{<a}/D\ge p^{1/4}\cdot\tfrac12\log p\), because \(D\le p^{1/4}/\log(2p^{1/2})\) as \(E\ge p^{-1/2}\). It reaches \(p^{1/2-o(1)}\) when \(D\) grows slowly. Exponent between **1/4** and **1/2**.
- **Positive majorant below the cut.** At a vertex level \(\alpha\) the cost is \(\alpha^{-2}X\) with true amplitudes, or \((\alpha^2\beta^2)^{-1}\) with R166:9's amplitudes bounded by one. At \(\alpha=C/p\) the losses are **\(p^2\)** and **\(p^4\)**.
- **Rank-two flattening** (R160 rank-two:57–61). The exponent is \(\frac74-\sum_j(\alpha_j-\frac14)_+\), a loss of \(\frac34-\sum_j(\alpha_j-\frac14)_+\). This is **3/4** whenever all five amplitudes are \(\ge p^{-1/4}\), i.e. \(g\ge p^{-1/2}\).
- **Floor for any absolute-value pricing (evidence).** In flat admissible laws the absolute off-diagonal is \(\mathfrak M^\natural\asymp p^{7/4}\), while \(\mathcal M_\nu\approx0.3p\), \(X_c\approx1.4p\) and \(\mathcal M_w\approx0.05p\) (§8). An argument that prices the low layers through absolute values and uses only (H1), (H2), (H4) therefore loses at least **\(p^{3/4}\)**. This is a method statement on the admissible class, in the style of R183 acc:262 (Proposition C), not a statement about the actual law.

### 5.3 Status of (V)

- **(V) implies the open high-energy alternative (bookkeeping).** On (NC), \(G^{\rm vert}=G-G_{-\rho}\ge(1-o(1))\sqrt p\) (R183 acc:264, Prop. 1.2; R190 acc:295, Theorem 1). So (V) gives \(\sum g^2\ge a\,(G^{\rm vert}-m_{<a})\ge(a-o(1))\sqrt p\). R183 acc:270 records \(\sum g^2\) as open in \([O(1),(\frac12+o(1))\sqrt p]\), "equivalent to the normalized additive energy \(E(S)/|S|^3\) of the flat near-critical support, the low-energy regime unresolved since Round 20".
  - On the low-energy sub-branch \(E(S)=o(|S|^3)\), Chebyshev gives \(\sum_{g\ge a}g\le\sum g^2/a=o(\sqrt p)\) for every fixed \(a\). So \((1-o(1))\) of the vertex mass lies below every fixed level.
  - There the fixed-block programme addresses a vanishing share of the mass, and (A) is the whole problem.
- **\(a\le\frac12\).** R183 acc:264 (Prop. 1.4) gives \(\sum g^2\le(\frac12+o(1))\sqrt p\). Tightness at a fixed \(a>\frac12\) would force \(\sum g^2\ge(a-o(1))\sqrt p\). So a single assembly cut must sit at \(a\le\frac12+o(1)\), and the better slope floors of R164 (\(\gamma=1/54,1/211\)) are unavailable for the whole kept part. The kept part needs the general fixed-threshold version, R163's \(1-4/445\), or \(X\).
- **Not implied by the sector-free (NC) consequences (evidence).** R190 acc:295 (Theorem 4): the \(D_\theta\) laws satisfy every sector-free accepted (NC) consequence. In the models, \(m_{<0.05}\approx0.28\)–\(0.39\sqrt p\) for \(D_{1/4}\), against \(G^{\rm vert}\approx0.5\sqrt p\) since these laws split the sectors evenly. A heuristic reason: by Parseval, the "noise" part \(\frac1m\sum_{j\in J'}(\mathbf 1_S-\theta)e(jk/n)\) has squared mass exactly \(n(1-\theta)/m=(1-\theta)\sqrt p\) for every \(S\), and for random \(S\) it sits at pointwise level \(O(p^{-1/2}\log p)\). So (V) would need the sector condition (NC2) or more, consistent with R190's finding that (NC)-based routes must use (NC2).
- **Holds in the square-field control.** In R157:45–54 (\(f=1\) on \(H\), \(-2/(s-1)\) elsewhere), \(m_{<a}\approx2=O(1)\). This field-general control also has \(X\asymp P^{3/2}\) (R184 acc:271, Prop. 5). So (V) alone gives nothing either; Proposition 1 needs both inputs.

---

## 6. The single uniform estimate, and which first mass implies it

**(A\(_{\rm unif}\)), the weakest sufficient form found (bookkeeping, from Proposition 1):**
\[
\inf_{0<a\le1/2}\Big(\sum_{t\ne1}|f(t)|\,P^\natural_t(\ge a)\ +\ p\,m_{<a}\Big)=o(pD).
\]
Its robust form: for one fixed \(a\in(0,\frac12]\),
\[
\text{(S}_a)\ \sum_{t\ne1}|f(t)|P^\natural_t(\ge a)=O(p)\qquad\text{and}\qquad\text{(V}_a)\ m_{<a}=O(1).
\]
- (S\(_a\)) is the slope part. It covers the bands \(p^{-(1-2\gamma)}<g<s_0\) and the near-unit slopes at one stroke.
- (V\(_a\)) is the vertex part. It covers the layers \(C^2/p<|F|^2<a\).
- The case \(a\to0\) of the infimum is \(\mathfrak M^\natural=o(pD)\), with no cut.
- The tautological signed form, necessary and sufficient, is (A\(_V\)) given (S\(_a\)).

**The three candidate first masses.**

| hypothesis | (S\(_a\)) slope part | (V\(_a\)) / (A\(_V\)) vertex part | target |
|---|---|---|---|
| \(\mathcal M_w=O(p)\) (log-free) | **no**: losses in the §4 table (\(441/890\) alone, \(441/1780\) combined; near-unit unbounded, \(3/7\) to \(\frac12-o(1)\) combined) | **no** | no |
| \(\mathcal M_{\sqrt g}=O(p)\) | **yes** (\(a^{-2}\)) | no | no |
| \(X=O(p)\) (log-free; floor \(2p\), R184 acc:271) | **yes** (\(a^{-2}\); Proposition 2) | **no**: models have \(X_c\approx1.4p\) and \(m_{<a}\asymp\sqrt p\) | yes **together with (V\(_a\))** (Proposition 1) |
| \(\mathfrak M^\natural=\sum_{t\ne1}|f(t)|P^\natural_t=O(p)\) (true vertex and slope amplitudes, all levels) | yes | yes (no cut needed) | **yes**, directly; but \(\asymp p^{7/4}\) in flat and \(D_\theta\) laws where the target holds; implied by neither \(X\) nor \(\mathcal M_w\) |

Current values: \(\mathcal M_w,X\ll p^{4/3+o(1)}\) (R187 acc:272, Corollary 4), so \(\mathcal M_{\sqrt g}\le X_c\ll p^{4/3+o(1)}\) too (bookkeeping). There is no accepted bound on \(\mathfrak M^\natural\), and no accepted bound on \(m_{<a}\) beyond \(m_{<a}\le G\).

---

## 7. Unassembled pieces with exact loss exponents (consolidated)

Losses are against the robust target \(O(p)\). Against \(o(pD)\) they shrink by at most \(D\le p^{1/4}/\log p\).

| piece | range | best accepted price | loss |
|---|---|---|---|
| slope bands, fixed vertex level \(a\le\frac12\) | \(p^{-(1-4/445)}<g(t)<s_0\) | \(\mathcal M_w\): \(p^{1+\sigma/2}\); with R163: \(\min(p^{1+\sigma/2},p^{3/2-2/445-\sigma/2})\) | \(441/890\); \(441/1780\) combined; **0 under \(X\)** |
| near-unit slopes | \(t\ne1\), \(g(t)>s_1\) | \(\mathcal M_w\): \(p/(1-s_1)\); with R159 and R162: \(\min(p/\epsilon,p^{3/2}(E+\epsilon)^{1/6}\log^{1/3})\) | unbounded alone; \(3/7\) if \(E\le p^{-3/7}\), else up to \(\frac12-o(1)\); **0 under \(X\)** |
| vertex layers, all slopes | \(C^2/p<|F|^2<a\) | R160: \(p\,m_{<a}\); majorant \(a^{-2}X\) at the cut level | \(1/2\) (R160, \(m_{<a}\asymp\sqrt p\)); up to \(2\) (majorant at \(\alpha=C/p\)); rank-two \(3/4\) at \(g\ge p^{-1/2}\) |
| vertex layers, absolute pricing (evidence) | flat/\(D_\theta\) laws | \(\mathfrak M^\natural\asymp p^{7/4}\) | \(\ge3/4\) for admissible-only absolute arguments |

---

## 8. Model evidence (floating; not the actual law; not on the critical branch)

`paley-191-assembly-models.py` (seeded). It uses three laws with \(m=\mathrm{round}(n/\sqrt p)\): flat random, \(D_{1/4}\) (R190 NC note line 199), and interval. It sets \(v=1\), \(\rho=+1\). None of these laws is near-critical (their sectors split evenly), so \(\mathcal M_\nu/p\) stays bounded, as expected.

**Part A** (\(p=10009,40009,160001\)), as fractions of \(\sqrt p\):

| law | \(G^{\rm vert}\) | \(\sum g^2\) | \(m_{<0.2}\) | \(m_{<0.05}\) | \(m_{<0.01}\) | \(X/p\) |
|---|---|---|---|---|---|---|
| flat | 0.49–0.50 | 0.049 → 0.012 | 0.49–0.50 | 0.35 → 0.50 | 0.04 → 0.30 | 0.48–0.50 |
| \(D_{1/4}\) | 0.50–0.52 | 0.17–0.19 | 0.39–0.42 | 0.28 → 0.39 | 0.06 → 0.28 | 0.49–0.51 |
| interval | 0.49–0.56 | 0.667 | 0.07–0.08 | ≈0.053 | ≈0.020 | 0.69–0.72 |

In every law the vertex mass below a fixed level is a fixed fraction of \(\sqrt p\), so (V) fails. In the interval law the fraction scales roughly like \(\sqrt a\) (Fejér side lobes). \(X/p\) stays bounded throughout.

**Part B** (\(p=401,797,1601,3209\); cut \(a=0.1\)):

| law | \(\mathcal M_\nu/p\) | \(\mathfrak M^\natural/p\) | \(\mathfrak M^\natural/p^{7/4}\) | \((X_c-\mathrm{diag})/p\) | \(\mathcal M_w/p\) | \(\mathcal M_{\sqrt g}/p\) | \(\mathcal M_\nu(F_{\ge a})/p\) | \(m_{<a}\) |
|---|---|---|---|---|---|---|---|---|
| flat | 0.27–0.40 | 1.5 → 8.7 | 0.016–0.026 | 1.27 → 1.48 | 0.10 → 0.05 | 0.36 → 0.25 | 0.12 → 0.009 | 3.4 → 20.9 |
| \(D_{1/4}\) | 0.34–0.50 | 2.0 → 6.8 | 0.016–0.022 | 1.31 → 1.46 | 0.11 → 0.05 | 0.39 → 0.27 | 0.30 → 0.04 | 2.2 → 17.6 |
| interval | 0.32–0.51 | 0.28–0.58 | ≤0.003 | 1.12 → 1.41 | 0.11–0.14 | 0.58 → 0.76 | 0.24–0.41 | 1.0 → 2.8 |

The R160 and Proposition 1 inequalities held in all twelve runs. In flat and \(D_\theta\) laws:
- the part above a fixed vertex level carries a vanishing share of \(\mathcal M_\nu\);
- the deleted mass grows like \(\sqrt p\);
- the absolute majorant grows like \(p^{7/4}\), while the signed moment is \(O(p)\).

These are finite floating-point diagnostics at small \(p\). They illustrate the method statements of §5.2–§5.3 and prove nothing asymptotic.

---

## 9. Hypotheses, bookkeeping to audit, remaining gap

**Hypotheses** (as in R157:3 and R160:3):
- the genuine selected short block on the hypothetical critical branch;
- the cap \(n\max\nu=O(\sqrt p)\) (R153:5–11);
- \(\|F\|_2^2=O(\sqrt p)\) (R160:20);
- \(|f|\le1\), \(f(1)=1\);
- (NC) facts only where cited (R183 acc:264, R190 acc:295).

No inversion symmetry and no incidence theorem are used.

**Bookkeeping items (unaudited compositions):**
- **C1. Proposition 1.** R152:58–63 expansion for cut rows, R157:39–41, R160:13–27 with \(\mu=\nu\), and R166:9–11 completion.
- **C2. Proposition 2.** \(\sum_{t\ne1}P_t=X_c-\mathrm{diag}\) and \(X_c=X+O(p)\) (exact script check for random rational \(g\)). Its consequence: \(X=O(p)\) closes every slope at a fixed vertex level.
- **C3.** The \(\mathcal M_w\) loss table of §4, including the two crossover optima \(441/1780\) and \((3-6\gamma)/7\).
- **C4.** The R160 pair cut costs \(p\eta_1\eta_2\), by homogeneity of the R160:29–38 proof.
- **C5.** (V) implies \(\sum g^2\ge(a-o(1))\sqrt p\), and \(a\le\frac12+o(1)\), from R183 acc:264.
- **C6.** The diagonal absorption of fixed-block constants (§2).

**Remaining gap.** (A) as named in R190 acc:294 is confirmed. It is refined into two parts:
- **(A-slope),** discharged by \(X=O(p)\) or \(\mathcal M_{\sqrt g}=O(p)\), but not by \(\mathcal M_w=O(p)\);
- **(A-vertex) = (A\(_V\)),** open. Its only accepted price is R160's \(p\,m_{<a}\). It closes under vertex tightness (V), which is at least as strong as the open high-energy alternative of R183 acc:270, and which fails in the \(D_\theta\) laws that satisfy every sector-free (NC) consequence (evidence). Otherwise it needs a genuinely signed estimate on the low vertex layers. No accepted tool gives one: the fixed-threshold machinery of R162–R166 depends on \(|\{g\ge a\}|=O_a(\sqrt p)\) and on quotient-set bounds at fixed levels.

**Consequence for the plan** (for the coordinator to judge).
- Fixed-block estimate rounds are insufficient in principle until (A-vertex) is addressed.
- If fixed-block work continues, the target should be \(X=O(p)\) (or \(\mathcal M_{\sqrt g}=O(p)\)) rather than \(\mathcal M_w=O(p)\): \(X\) also discharges (A-slope), and both are at \(p^{4/3+o(1)}\).
- The cheapest decisive next question is whether (NC2) forces (V), or forces at least \(\sum g^2\gg\sqrt p\). That is the Round 20 low-energy question, recorded at R183 acc:270.

---

## 10. Verdict

**No.** \(O(p)\) for every fixed moderate block, together with every paid cut, does not imply the \(O(p)\) favorable off-diagonal or the contradiction on the critical branch.
- The R157/R160 device pays vertex cuts of mass \(o(D)\) only, and slope cuts not at all.
- The missing statement has the exact uniform form (A\(_{\rm unif}\)) of §6.
- \(\mathcal M_w=O(p)\) does not imply it.
- \(X=O(p)\) implies its slope part (losses \(441/890\) or \(441/1780\) on bands, and \(1/(1-s_1)\) near unit slopes, become 0) but not its vertex part (loss \(p^{1/2}\) under R160, at least \(p^{3/4}\) for admissible absolute pricing).
- The true-amplitude first mass \(\mathfrak M^\natural=O(p)\) would imply the target outright, but it is strictly stronger than the target on admissible laws.

Record (A) as a separate ordinary obligation in the refined form (A-slope) + (A-vertex).

---

## Files

Written by this call only (nothing committed):

- `research/native-claude-ordinary-fixed-block-assembly-191.md` (this note)
- `research/paley-191-assembly-exponents.py`: SHA-256 `2df3ce44250517d649fafe6bf6b53a664e3af81a079b9341486a1e24fd70b32f`; exact; prints `ALL OK`
- `research/paley-191-assembly-models.py`: SHA-256 `b79357628d79eca96c6385f10ca2752f79d635ccc956b875f4633259c72d615d`; floating evidence; seeded; about 5 s with `.venv/bin/python -B`
