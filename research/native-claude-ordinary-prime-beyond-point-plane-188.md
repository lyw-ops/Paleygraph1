# Round 188 native Claude draft: one-match estimates beyond the point–plane floor

- **call_id:** `ordinary-prime-beyond-point-plane`
- **Author:** Claude subagent started by the Round 188 coordinator (session/r188-beyond-pp). This is an agent assessment. It is not an audit, not human acceptance and not a mathematical certification.
- **Mission:** `coordination/missions/round-188/ordinary-prime-beyond-point-plane.md`, exported from `coordination/round-187.json` (SHA-256 `36fbe33d8dedca6cd2fdccc3abd6a034b9ae45c034d2ebc17e11a1237fc384b3`, matches the export).
- **Inputs read.** All nine SHA-256 values listed in the mission match:
  - `research/round-186-acceptance.json` (`9f1a0ccb…626ee`), `research/round-187-acceptance.json` (`edc1d3eb…1d9`)
  - `research/native-claude-audit-187.md` (`714513ca…657ff`); §2 and §5 read in full, the rest skimmed
  - `research/native-claude-ordinary-prime-level-pair-energy-187.md` (`52686317…b7`); setup, Theorem 2, §§6–7, remaining gap
  - `research/ordinary-weighted-slope-product-incidence-178.md` (`9e4589c6…1d71`), `research/ordinary-mixed-row-autocorrelation-180.md` (`357f5058…85aa`), `research/ordinary-weighted-affine-vertical-saving-173.md` (`61e959f2…3a2023`): in full
  - `research/native-claude-ordinary-prime-near-critical-slope-row-mass-184.md` (`85702949…02ec`): lines 1–200
  - `research/native-claude-ordinary-prime-row-deleted-one-match-183.md` (`9af6768f…7f7`): in full

  Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-187.md`. For the chart and the operator criteria: `research/ordinary-one-match-positive-form-168.md`, `research/ordinary-one-match-twisted-physical-169.md`, `research/ordinary-affine-line-energy-171.md`, `research/native-claude-ordinary-prime-one-match-operator-norm-182.md` (Propositions 5–6 and the (a)/(b) lists), and §3 of `research/native-claude-ordinary-prime-near-critical-support-energy-184.md`.
- **Scripts (all new):**
  - `research/paley-188-bpp-exponents.py`: exact `Fraction` arithmetic for every exponent in this report.
  - `research/paley-188-bpp-models.py`: `--check` runs exact integer checks of the identities at p = 13, 17, 29, 37, and floating checks of the character identities at p = 29, 37, 53. With prime arguments it runs floating-point models.
- **Nothing was committed.** No coordination file, acceptance record or other agent's file was touched.

## Result summary

**Verdict: inconclusive** in the mission's sense. I found no unconditional one-match exponent below 7/4. The accepted 43/24 is unchanged. Three findings change what the remaining obligation is.

1. **A twisted second-norm estimate without affine energy (Theorem A; proved).** Take the actual g = |f|² (ν ≥ 0, so its multiplicative Fourier law satisfies ω ≥ 0), with the chart, mask and positive completion of Rounds 171–178. Then for **every** t ∈ F_p^×:
   \[
   \sum_{s}|F_\mu h_t(s)|^2\;=\;\frac{M_1^2G^2}{p}+\|\pi(\mu)\varphi_t\|^2,\qquad
   \|\pi(\mu)\varphi_t\|^2\;\le\;p\,T_0\;\le\;p\,X,
   \]
   where \(T_0=\sum_\lambda g(\lambda)\Delta(h_{0,\lambda})\) and \(X=\sum_r m(r)^2\) is the slope-row second moment. The t-average obeys \(\sum_t\|\pi(\mu)\varphi_t\|^2\le p\,\mathcal T\) with \(\mathcal T=\sum_\lambda c_g(\lambda)\Delta(h_{0,\lambda})\le\Gamma_{\rm tot}X\). Hence
   \[
   \text{one-match covariance}\;\ll\;p^{3/2}+\min\bigl(W,\ \Gamma_{\rm tot}/4\bigr)\,X ,\qquad W=\textstyle\sum_tw(t)\le G .
   \]
   - **No affine energy, no point–plane, no six-word input.** The proof uses three identities:
     - (i) the horizontal (intercept) masses equal the slope-row masses in law: \(m'(b)=c_h(b)\) on \(Q\setminus\{1\}\), so \(\sum_bm'(b)^2=X\) exactly;
     - (ii) \(\|F_\mu\chi\|^2=p\,S_0(\chi)-|\hat m(\chi)|^2\) for every nontrivial multiplicative character χ, by a Gauss sum;
     - (iii) orthogonality of the t-dilations.
   - **The method floor is \(p^{3/2}\), not \(p^{7/4}\).** \(X\) has floor ≍ p, attained up to constants in every model, and \(\Gamma_{\rm tot}\ll\sqrt p\).
   - **Unconditionally**, with Round 187 Corollary 4 (\(X\ll p^{4/3}(\log p)^{32/3}\)), this gives \(p^{11/6+o(1)}\). That is **worse** than 43/24 by \(p^{1/24}\). So the accepted exponent does not move.
   - **Conditionally**, \(X=O(p^{1+\varepsilon})\) gives covariance \(O(p^{3/2+\varepsilon})\):
     - below 7/4 iff ε < 1/4;
     - below 43/24 iff ε < 7/24;
     - better than Round 184 Proposition 1(ii) (7/4 + ε/8) iff ε < 2/7;
     - the target O(p^{3/2}) when \(X=O(p)\), or more generally when \(\Gamma_{\rm tot}X=O(p^{3/2})\).
2. **Correction to the recorded obligation.** The accepted wording says that "reaching O(p^{3/2}) needs an input that is not an affine-energy bound and the generic six-word class below p^{9/2}". That holds only for the operator-norm route (b1″).
   - By Theorem A, the optimal-order slope-row estimate \(X=O(p)\) implies the one-match target with no six-word input and no affine energy.
   - So the one-match obligation is now the **X form of `cand:slope-row-mass-x`**, the same shared estimate as the first mass. The scales differ: the one-match target needs X = O(p), while the first-mass target X = O(p^{1+1/1280}) gives one-match O(p^{3/2+1/1280}).
   - The generic six-word class is no longer necessary. It stays a separate, alternative route (§4).
3. **Not every route through E(μ) floors at 7/4 (Proposition 1, method statements; Proposition B, proved).**
   - The 7/4 floor belongs to **point–plane pricing of E(μ)**: both terms \(\sum W^{3/2}\ge M_1^3/\sqrt{p-1}\) and \(G\log p\,M_1^2\) are \(\asymp p^{5/2}\).
   - The Rudnev–Shkredov second-norm route floors at \(p^{13/8}\) for every E, because \(E(\mu)\ge M_1^4/(p(p-1))\).
   - The Plancherel/operator route gives covariance \(\ll p^{3/2}+\Gamma_{\rm tot}E(\mu)^{1/2}\). It reaches the target when \(E(\mu)=O(p^2)\) (Round 182 (a7)).
   - New: \(E(\mu)\le cX+\sum_{\lambda\ne1}C(\lambda)D(\lambda)\le c\,M_1^2\). Here \(D(\lambda)=\max_\beta\Delta(\lambda,\beta)\) and \(c=\sum\mu^2\le\Gamma_2^2\). Consequences:
     - The translation fibre of the affine energy is already harmless: \(E_1\le cX\ll p^{7/3+o(1)}\) contributes \(p^{5/3}\). The binding part of E(μ) is the dilation fibres \(E_{\ne1}\).
     - A support-energy criterion. With \(\Gamma_{\rm tot}=p^\gamma\) the covariance is \(\ll p^{\min(1+2\gamma,\ \gamma+4/3,\ 43/24)+o(1)}\). So γ ≤ 1/4 gives the target, γ < 5/12 gives an exponent below 7/4, and γ < 11/24 an exponent below 43/24. This improves Round 184 Corollary Y (7/4 + γ/8 for γ < 3/8).
4. **What a new route must control (exact).**
   - Through Theorem A: the quantity \(T_0-c=\sum_{\lambda\ne1}g(\lambda)\Delta(h_{0,\lambda})\), or its t-average \(\mathcal T\), currently bounded by \(X\ll p^{4/3}\).
     - Below 7/4 needs \(X\le p^{5/4-\delta}\), or a direct bound on \(T_0\).
     - X at the point–line floor \(p^{4/3}\) is the binding term. Lowering it needs both a height-1 pair-energy bound below \(N^{5/2}\) at \(N\asymp\sqrt p\), and a light-level input that moves the Young barrier from \(p^{-1/6}\) to below \(p^{-1/4}\).
   - Through the operator route: the dilation-fibre energy \(E_{\ne1}(\mu)\) must fall below \(p^{5/2}\) when \(\Gamma_{\rm tot}\asymp\sqrt p\). A pointwise bound \(\sup_{\lambda\ne1}D(\lambda)\le p^{1/2-\delta}\) suffices.
5. **Evidence (floating, models only).** Flat laws \(g=|f|^2\) and a sector-concentrated control, \(p\le2003\):
   - \(\Lambda_0/X=1\) to machine precision.
   - The weighted fluctuation \(\sum_tw\|\pi\varphi_t\|^2\) is 0.15–25% of the mean term, which is the target scale. It is largest in the interval model, about 16% at p ≥ 401, and 0.6–3% in the sector model.
   - Theorem A's averaged bound is within factors 5–100 of the true weighted fluctuation.
   - The uniform bound is fairly tight per t: \(\max_t\|\pi\varphi_t\|^2/(pT_0)\) ranges over 0.04–0.64.
   - \(T_0/c\) ranges over 1.2–7.4. In the sector model it falls from 2.1 to 1.17 as p grows from 101 to 2003.
   - In the sector model (\(M_1\approx p\)): \(E(\mu)/p^2\approx1.0\)–1.4, \(X/p\approx1.9\)–2.3, \(\max D\approx6\)–9.

**No new bound on X, \(\mathcal M_w\) or Γ₂ is proved here** (stated separately, as the mission asks). Theorem A uses X as an input. It changes the use of `cand:slope-row-mass-x`, not its status.

## Setup and hypotheses

Notation and normalisations are those of Rounds 168–187, with counting norms.

- **Field and law.** p ≡ 1 (mod 4) is prime, n = (p−1)/2, Q is the set of squares, and χ₂ is the Legendre symbol. ν ≥ 0 is a probability on \(\widehat Q\), \(f=\sum_\eta\nu_\eta\eta\) on Q (zero elsewhere), and \(g=|f|^2\).
  - On \(\mathbb F_p^\times\), \(g=\sum_\alpha\omega(\alpha)\alpha\) with \(\omega\ge0\), \(\sum_\alpha\omega(\alpha)=g(1)=1\) and \(\omega(\bar\alpha)=\omega(\alpha)\). Each lift carries half of \(\lambda_\nu=\nu*\check\nu\ge0\) (Rounds 166/169).
  - **(H3), inversion symmetry:** \(g(1/x)=g(x)\). It holds because ν is real: \(f(1/x)=\overline{f(x)}\).
  - The cap (H2) gives \(G=\sum g\le C_{\rm cap}\sqrt p\), and \(\kappa=\max\omega\le C/\sqrt p\).
  - \(\Gamma_{\rm tot}=\sum_{x}g(x)^2=(p-1)\sum_\alpha\omega(\alpha)^2=n\,\mathcal E(\nu)\) and \(\Gamma_2=\Gamma_{\rm tot}-1\) (Round 183 Prop. 1.1).
  - \(w=g(1-g)\le\min(g,\tfrac14)\) and \(W=\sum_tw(t)=G-\Gamma_{\rm tot}\).
- **Chart (Round 171).** \(\mu(r,b)=g(Y)g(D)\) on \(Y\ne D\in\mathbb F_p\setminus\{0,1\}\), with \(r=(Y-D)/(1-D)\), \(b=D(1-Y)/(Y(1-D))\) and the mask \(b\in Q\). The map is \(j_{r,b}(e)=re+b\), with fixed point D/Y.
  - Masses: \(M_1=\sum\mu\le G^2\) and \(c=\sum\mu^2\le\Gamma_2^2\). Slope rows are \(m(r)=\sum_b\mu(r,b)\) and horizontal (intercept) rows are \(m'(b)=\sum_r\mu(r,b)\).
  - \(X=\sum_rm(r)^2\) and \(\Lambda_0=\sum_bm'(b)^2\).
- **Affine autocorrelation.** For \(h=(\lambda,\beta):x\mapsto\lambda x+\beta\), \(\Delta(\lambda,\beta)=\sum_{r,b}\mu(r,b)\mu(\lambda r,b+r\beta)\). Then \(\mathcal E(\mu)=\sum\Delta^2\) and \(C(\lambda)=\sum_rm(r)m(\lambda r)\). The dilation about 0 by λ is \(h_{0,\lambda}=(\lambda,0)\), and \(D(\lambda)=\max_\beta\Delta(\lambda,\beta)\).
- **Shifted and multiplicative correlations.** \(h(z)=g(1-z)\), \(c_h(\kappa)=\sum_zh(z)h(\kappa z)\) and \(c_g(\lambda)=\sum_xg(x)g(\lambda x)\le\Gamma_{\rm tot}\). Round 183 Prop. A gives \(m(r)=c_h(1-r)\) when \(1-r\in Q\setminus\{1\}\) and 0 otherwise. So \(X=E_Q(h)\le E^\times(h)\).
- **Physical kernel (Rounds 169, 173, 178, 182).** \(h_t(e)=g(t/e)\) for e ≠ 0 and \(h_t(0)=0\). Then \(F_\mu v(s)=\sum_{r,b}\mu(r,b)\,v((s-b)/r)\), \(\varphi_t=h_t-G/p\), and \(\pi(\mu)=F_\mu|_{\mathbf 1^\perp}\).
  - The accepted positive upper is \(0\le H_\alpha(s,t)\le F_\mu h_t(s)\) for \(s\notin\{0,1\}\), with the endpoint terms already priced at \(O(p^{5/2})\).
  - The matching-number-one covariance is \(O(p^{-1}\sum_{s\ne0,1,t}w(t)|H_\alpha(s,t)|^2+p^{3/2})\) (Rounds 169/173).
- **No near-critical (NC) input is used** except where a statement is marked (NC).

**Accepted inputs, each with its source.**

| input | statement | source |
|---|---|---|
| R182-P5 | \(\sum_{s\ne0,1,t}w|F_\mu h_t|^2\le 2G^7/p+2\sigma_R^2G\Gamma_{\rm tot}\); splitting \(\sum_s|F_\mu h_t|^2=M_1^2G^2/p+\|\pi\varphi_t\|^2\) | Round 182 Prop. 5 and (a1); confirmed by the Round 182 audit |
| R182-a2 | \(\operatorname{tr}((\pi\pi^*)^2)=p\,\mathcal E(\mu)-E^\times(m)\), so \(\|\pi\|^4\le p\,\mathcal E(\mu)\) | Round 182 (a2); also Round 183 Prop. 2.4 proof |
| R178 | Rudnev–Shkredov second norm and the point–plane bound \(\mathcal E(\mu)\ll\sum_\xi(W_\xi^2/p+W_\xi^{3/2}+G\log p\,W_\xi)\) | Round 178 |
| R183-A | \(m(r)=c_h(1-r)\) on \(1-r\in Q\setminus\{1\}\) | Round 183, Proposition A (quoted in Round 184 setup) |
| R187-T2 | \(X\le E^\times(h)\ll p^{4/3}(\log p)^{32/3}\); \(\mathcal E(\mu)\ll p^{8/3}(\log p)^{16/3}\); covariance \(O(p^{43/24}(\log p)^{4/3})\) | Round 187 Theorem 2, Corollaries 3–4 (agent-accepted; the audit advises a human read of Lemma M′) |
| R184-Y | \(X\le\Gamma_2M_1\) | Round 184 Lemma Y |

**No new external theorem is used.** The only facts used beyond accepted project inputs are orthogonality of characters and the Gauss-sum modulus \(|\sum_x\chi(x)e_p(\xi x)|=\sqrt p\) for nontrivial χ and ξ ≠ 0.

## 1. Where the 7/4 floor lives (Proposition 1; method statements)

Write exponents with \(G\asymp\sqrt p\), \(M_1\asymp p\), \(\Gamma_{\rm tot}=p^\gamma\), \(\mathcal E(\mu)=p^{e_E}\) and \(X=p^{e_X}\). Every covariance exponent is the maximum of 3/2 and the route value below. All of them are checked in `paley-188-bpp-exponents.py`.

| route | covariance | value at Round 187 inputs | floor of the route |
|---|---|---|---|
| RS: Rudnev–Shkredov second norm (R178) | \(p^{9/8}\mathcal E^{1/4}\) | \(e_E=8/3\): **43/24** | \(\mathcal E\ge M_1^4/(p(p-1))\): **13/8** for every E |
| OP: operator / Plancherel (R182-P5, R182-a2) | \(\Gamma_{\rm tot}\mathcal E^{1/2}\) | γ = 1/2: 11/6 | \(\mathcal E\asymp p^2\): **3/2** |
| point–plane pricing of E, in either route | \(\mathcal E\gg\sum W^{3/2}+GM_1^2\ge p^{5/2}\) | n/a | **7/4** (RS and OP, γ = 1/2) |
| CH: Theorem A (this report) | \(\min(W,\Gamma_{\rm tot}/4)X\) | \(e_X=4/3\): 11/6 | \(X\ge(2-o(1))p\) on (NC): **3/2** |

**Proposition 1.**
- (a) The RS route cannot give a covariance below \(p^{13/8}\) when \(M_1\asymp p\), whatever E is. This repeats Round 182 (a7), stated as a floor.
- (b) Point–plane pricing of \(\mathcal E(\mu)\) cannot go below \(p^{5/2}\). This is Round 182 Prop. 6 and Round 183 (2.5b). It caps both the RS and OP routes at 7/4.
- (c) The OP route reaches \(p^{3/2}\) iff \(\Gamma_{\rm tot}^2\mathcal E(\mu)=O(p^3)\). The actual \(\mathcal E(\mu)\) has no known lower bound above \(\asymp p^2\).

*Proof.*
- (a) \(\mathcal E\ge c^2+(M_1^2-c)^2/(p(p-1)-1)\) by Cauchy–Schwarz over the non-identity elements, and \(c\le\Gamma_2^2\ll p\). Insert this into \(p^{9/8}\mathcal E^{1/4}\).
- (b) This is Hölder over the \(p-1\) values of ξ, plus the collinearity term.
- (c) Use R182-P5 with \(\sigma_R^2\le\|\pi\|^2\le(p\mathcal E-E^\times(m))^{1/2}\) and \(\sum w\le G\). ∎

**Answer to the mission's second question.** Not every route through \(\mathcal E(\mu)\) floors at 7/4. The 7/4 floor belongs to the point–plane bound for \(\mathcal E(\mu)\). The RS second-norm route has the lower floor 13/8, and it cannot reach the target even with an optimal energy. The OP route reaches the target with an optimal-order energy \(\mathcal E(\mu)=O(p^2)\).
- Models put \(\mathcal E(\mu)/p^2\) at 0.05–16, with no visible growth in p in any family (§5; Round 183 tables give 2.6–3.4 for sector 0/1 models).
- So the checkpoint phrase "\(\mathcal E(\mu)\ge p^{5/2}\)" should read "the point–plane bound for \(\mathcal E(\mu)\) is \(\ge p^{5/2}\)". It is not a lower bound for \(\mathcal E(\mu)\).

## 2. Fibre decomposition of the affine energy (Proposition B; proved)

**Proposition B.** For any nonnegative μ on the affine group:
- (i) \(\sum_\beta\Delta(\lambda,\beta)=C(\lambda)\) for every λ;
- (ii) \(\Delta(h)\le\Delta(\mathrm{id})=c\) for every h;
- (iii) \(\mathcal E(\mu)\le\sum_\lambda C(\lambda)D(\lambda)=cX+\sum_{\lambda\ne1}C(\lambda)D(\lambda)\le c\,M_1^2\).

In particular the translation fibre \(E_1=\sum_\beta\Delta(1,\beta)^2\) is at most cX. The fibre-variance energy of Round 182 satisfies \(\mathcal E-E^\times(m)/p\le\sum_\lambda C(\lambda)(D(\lambda)-C(\lambda)/p)\).

*Proof.*
- (i) For fixed (r, b), as β varies, \(b+r\beta\) runs over \(\mathbb F_p\) because r ≠ 0. So \(\sum_\beta\mu(\lambda r,b+r\beta)=m(\lambda r)\).
- (ii) Cauchy–Schwarz, since \(j\mapsto jh\) is a bijection.
- (iii) Bound each fibre: \(\sum_\beta\Delta(\lambda,\beta)^2\le D(\lambda)\,C(\lambda)\). Then \(D(1)=c\) by (ii), and \(\sum_\lambda C(\lambda)=M_1^2\). ∎

Exact integer checks at p = 13, 17, 29, 37 (two random inversion-symmetric integer weights each) confirm (i), (ii), (iii) and the trace identity \(p\,\mathcal E=\operatorname{tr}((KK^T)^2)-M_1^4+E^\times(m)\) (`--check`).

**Corollary B1 (operator route; proved).** Under (H1)/(H2) with the cap, the covariance is \(\ll p^{3/2}+\Gamma_{\rm tot}\Gamma_2\,p\). Combined with Round 187 and Theorem A, it is \(\ll p^{\min(1+2\gamma,\ \gamma+4/3,\ 43/24)+o(1)}\) for \(\Gamma_{\rm tot}=p^\gamma\).
- Thresholds: γ ≤ 1/4 gives the target; γ < 5/12 gives an exponent below 7/4; γ < 11/24 an exponent below 43/24.
- Round 184 Corollary Y gave \(7/4+\gamma/8\), and only for γ < 3/8. At γ = 1/3 the new value is 5/3 against 43/24.

*Proof.* Use OP with \(\mathcal E\le cM_1^2\le\Gamma_2^2M_1^2\), \(G\le C\sqrt p\) and \(M_1\le G^2\): \(p^{-1}G\,\Gamma_{\rm tot}(p\,cM_1^2)^{1/2}\ll\Gamma_{\rm tot}\Gamma_2p\). The γ + 4/3 branch is OP with Round 187's \(\mathcal E\), or Theorem A with Round 187's X. ∎

Equivalently (Round 183 Prop. 1.1), \(\Gamma_{\rm tot}=n\,\mathcal E(\nu)\). The one-match target therefore follows from \(\mathcal E(\nu)=O(p^{1/4}/n)\), an additive-energy bound for the law ν. For a flat law on S, \(|S|\asymp\sqrt p\), this is \(\mathcal E(S)=O(|S|^{5/2})\). On (NC), Round 183 Prop. 1.4 gives only \(\Gamma_2\le(\frac12+o(1))\sqrt p\). This criterion is **conditional** and does not settle the Γ₂ question.

**Reading for the operator route.**
- \(E_1\le cX\ll p\cdot p^{4/3+o(1)}\) (Round 187 Cor. 4) contributes \(\Gamma_{\rm tot}E_1^{1/2}\ll p^{5/3+o(1)}\). So the slope-row bounds already settle the translation fibre below 7/4.
- What remains is the dilation-fibre energy \(E_{\ne1}=\sum_{\lambda\ne1,\beta}\Delta(\lambda,\beta)^2\):
  - \(E_{\ne1}\le p^{5/2-\delta}\) gives covariance \(p^{7/4-\delta/2}\) when \(\Gamma_{\rm tot}\asymp\sqrt p\);
  - \(E_{\ne1}=O(p^2)\) gives the target;
  - \(\sup_{\lambda\ne1}D(\lambda)\le p^{1/2-\delta}\) suffices for the first, through (iii).
- In models the dilation fibre carries 80–98% of \(\mathcal E\) (§5). A pointwise bound for D is a two-equation, four-variable count on sets of size √p. I see no incidence theorem that saves anything on it: point–line bounds save nothing when the number of curves equals the set size.

## 3. Theorem A: the character route

### Lemma A1 (horizontal masses; proved, uses (H3))
For \(b\in Q\setminus\{1\}\), \(m'(b)=c_h(b)\), and \(m'(b)=0\) otherwise. Hence \(\Lambda_0=\sum_bm'(b)^2=E_Q(h)=X\).

*Proof.* Put \(u_x=(1-x)/x\), so \(x=1/(1+u_x)\) and \(b=u_Y/u_D\). The chart conditions are:
- \(Y,D\in\mathbb F_p\setminus\{0,1\}\), which is \(u\ne0\) together with \(g(0)=0\);
- \(Y\ne D\), which is \(b\ne1\);
- the mask \(b\in Q\).

Hence \(m'(b)=\sum_{v\ne0}k(v)k(bv)\) with \(k(v)=g(1/(1+v))\). By (H3), \(k(v)=g(1+v)=h(-v)\), so \(m'(b)=c_h(b)\). The slope rows are \(m(r)=c_h(1-r)\) on \(1-r\in Q\setminus\{1\}\) (R183-A). Both sums of squares therefore equal \(\sum_{\kappa\in Q\setminus\{1\}}c_h(\kappa)^2\). Without (H3), replace h by \(\tilde h(z)=g(1/(1-z))\). ∎

Exact checks of \(m'=c_h\), \(m=c_h(1-\cdot)\) and \(\Lambda_0=X\) pass at p = 13, 17, 29, 37. In every model \(\Lambda_0/X=1.000000\).

### Lemma A2 (π on multiplicative characters; proved, any μ ≥ 0)
Let χ be a nontrivial multiplicative character, extended by χ(0) = 0. Then
\[
\|F_\mu\chi\|^2=p\,S_0(\chi)-|\hat m(\chi)|^2,\qquad S_0(\chi)=\sum_b\Bigl|\sum_r\mu(r,b)\bar\chi(r)\Bigr|^2=\sum_\lambda\chi(\lambda)\Delta(\lambda,0)\ \le\ \Lambda_0,
\]
where \(\hat m(\chi)=\sum_rm(r)\bar\chi(r)\).

*Proof.*
- \(F_\mu\chi(s)=\sum_bA_b\,\chi(s-b)\) with \(A_b=\sum_r\mu(r,b)\bar\chi(r)\). This uses \(\chi((s-b)/r)=\chi(s-b)\bar\chi(r)\), and both sides vanish at s = b.
- Additive Parseval gives \(\|A*\chi\|^2=p^{-1}\sum_\xi|\hat A(\xi)|^2|\hat\chi(\xi)|^2\). Here \(\hat\chi(0)=0\) and \(|\hat\chi(\xi)|^2=p\) for ξ ≠ 0 (Gauss sum). Hence the sum is \(\sum_{\xi\ne0}|\hat A(\xi)|^2=p\sum_b|A_b|^2-|\sum_bA_b|^2\), and \(\sum_bA_b=\hat m(\chi)\).
- Expanding \(|A_b|^2\) and putting \(r'=\lambda r\) gives \(\sum_\lambda\chi(\lambda)\Delta(\lambda,0)\).
- Finally \(|A_b|\le m'(b)\). ∎

Floating check: the identity holds to relative error ≤ 7·10⁻¹⁷ for every χ at p = 29, 37, 53.

**Reading.** The operator norm \(\|\pi(\mu)\|^2\) can be as large as \(p\Gamma_2\asymp p^{3/2}\): the s = 1 row (Round 182 Prop. 4, Round 183 Cor. 1.3). On a normalised multiplicative character, by contrast, π has squared norm \(\le\frac p{p-1}\Lambda_0=\frac p{p-1}X\). That is \(\asymp p\) when X sits at its floor. The vectors \(h_t\) are built from characters.

### Theorem A (proved)
Assume ν ≥ 0 (so ω ≥ 0) and (H3). Let μ, \(F_\mu\), \(h_t\), \(\varphi_t\), \(T_0=\sum_\lambda g(\lambda)\Delta(\lambda,0)\) and \(\mathcal T=\sum_\lambda c_g(\lambda)\Delta(\lambda,0)\) be as above. Then:
- (i) **(uniform in t)** \(\|\pi(\mu)\varphi_t\|^2\le p\,T_0\le p\,X\) for every \(t\in\mathbb F_p^\times\);
- (ii) **(t-average)** \(\sum_{t\in\mathbb F_p^\times}\|\pi(\mu)\varphi_t\|^2\le p\,\mathcal T-G^2X\le p\,\Gamma_{\rm tot}X\).

Consequently
\[
\sum_{s\ne0,1,\,t}w(t)\,|H_\alpha(s,t)|^2\ \le\ \frac{W M_1^2G^2}p+p\,\min\Bigl(W\,T_0,\ \tfrac14\mathcal T\Bigr)+O(p^{5/2}),
\]
and with the cap \(G\le C_{\rm cap}\sqrt p\) the one-match covariance is
\[
O\Bigl(p^{3/2}+\min\bigl(W\,T_0,\ \tfrac14\mathcal T\bigr)\Bigr)=O\bigl(p^{3/2}+\min(W,\Gamma_{\rm tot}/4)\,X\bigr).
\]

*Proof.*
1. **Character expansion.** For e ≠ 0, \(h_t(e)=g(t/e)=\sum_\alpha\omega(\alpha)\alpha(t)\bar\alpha(e)\), and \(h_t(0)=0\). Subtract the mean. For α ≠ 1, \(\bar\alpha\) already has mean zero. The trivial character \(\mathbf 1_{\mathbb F_p^\times}\) has mean (p−1)/p, and \(G=(p-1)\omega(1)\). So
   \[\varphi_t=\sum_\alpha\omega(\alpha)\alpha(t)\,\bar\alpha^\circ,\qquad \bar\alpha^\circ=\bar\alpha\ (\alpha\ne1),\quad \mathbf 1^\circ=\mathbf 1_{\mathbb F_p^\times}-\tfrac{p-1}p=-(\delta_0-\tfrac1p).\]
2. **Size of each image.**
   - For α ≠ 1, Lemma A2 gives \(\|\pi\bar\alpha^\circ\|^2\le pS_0(\bar\alpha)\).
   - For α = 1, \(F_\mu\delta_0(s)=m'(s)\), so \(\|\pi(\delta_0-\tfrac1p)\|^2\le\|F_\mu\delta_0\|^2=\sum_bm'(b)^2=\Lambda_0=S_0(\mathbf 1)\le pS_0(\mathbf 1)\).
   - Hence \(\|\pi\bar\alpha^\circ\|^2\le pS_0(\bar\alpha)\) for every α.
3. **Part (i).** The weights ω(α) ≥ 0 sum to 1. Cauchy–Schwarz then gives \(\|\pi\varphi_t\|^2\le\sum_\alpha\omega(\alpha)\|\pi\bar\alpha^\circ\|^2\le p\sum_\alpha\omega(\alpha)S_0(\bar\alpha)\). By Lemma A2, \(\sum_\alpha\omega(\alpha)S_0(\bar\alpha)=\sum_\lambda\Delta(\lambda,0)\sum_\alpha\omega(\alpha)\bar\alpha(\lambda)=\sum_\lambda g(1/\lambda)\Delta(\lambda,0)=T_0\), using (H3). Finally \(T_0\le\sum_\lambda\Delta(\lambda,0)=\Lambda_0=X\) since g ≤ 1, using Lemma A2's \(S_0(\mathbf 1)=\Lambda_0\) and Lemma A1.
4. **Part (ii).** Orthogonality \(\sum_t\alpha(t)\bar\alpha'(t)=(p-1)[\alpha=\alpha']\) gives \(\sum_t\|\pi\varphi_t\|^2=(p-1)\sum_\alpha\omega(\alpha)^2\|\pi\bar\alpha^\circ\|^2\).
   - This is at most \(p(p-1)\sum_{\alpha\ne1}\omega(\alpha)^2S_0(\bar\alpha)+(p-1)\omega(1)^2\Lambda_0\).
   - Since \(c_g(\lambda)=(p-1)\sum_\alpha\omega(\alpha)^2\bar\alpha(\lambda)\), we have \((p-1)\sum_\alpha\omega(\alpha)^2S_0(\bar\alpha)=\mathcal T\). The α = 1 term of that sum is \(G^2\Lambda_0/(p-1)\), so the total is \(\le p\mathcal T-G^2\Lambda_0\).
   - Also \(\mathcal T\le\Gamma_{\rm tot}\Lambda_0\), because \(c_g\le c_g(1)=\Gamma_{\rm tot}\).
5. **Consequence.** Use the splitting of R182-P5, \(0\le H_\alpha\le F_\mu h_t\) off s ∈ {0, 1}, and the priced endpoints. For the uniform branch, multiply (i) by w(t) and sum. For the averaged branch, use \(w\le\frac14\) and (ii). The mean term is \(WM_1^2G^2/p\le G^7/p\ll p^{5/2}\). Divide by p. ∎

Checks (`--check`, floating, p = 29, 37, 53, random laws):
- ω is real and ≥ 0 up to 10⁻¹⁸.
- The t-sum identity in step 4 holds to relative error ≤ 7·10⁻¹⁶.
- The two expressions for \(\mathcal T\) agree.
- \(\max_t\|K\varphi_t\|^2/(pT_0)\le0.08\), and \(\sum_t\|K\varphi_t\|^2/(p\mathcal T)\approx0.78\)–0.82.
- The physical form of \(T_0\) below was checked by direct summation at p = 29, 37, 53.

**Physical form of the binding term.** In the \((Y,b)\) chart, \(r=(1-b)Y\). So two maps with the same intercept have slope ratio \(Y'/Y\), and
\[
T_0-c=\sum_{Y\ne Y'}g(Y)g(Y')g(Y'/Y)\sum_{b\in Q}g(D_b(Y))g(D_b(Y'))\ \le\ \sum_{Y\ne Y'}g(Y)g(Y')\,g(Y'/Y)\,c_h\!\Bigl(\tfrac{\phi(Y)}{\phi(Y')}\Bigr),
\]
with \(\phi(Y)=Y/(1-Y)\) and \(D_b(Y)\) defined by \(D/(1-D)=b\,\phi(Y)\).
- It couples a multiplicative triangle of g, namely \((Y,Y',Y'/Y)\), with the shifted correlation \(c_h\).
- In a random-like regime one expects \(T_0-c\approx(G/p)X\ll c\). The trivial step \(g(Y'/Y)\le1\) gives \(T_0\le X\), and that step loses everything.

### Corollary A (exponents; exact, `paley-188-bpp-exponents.py`)
- **Unconditional**, with Round 187 Cor. 4: covariance \(\ll p^{3/2}+G\,p^{4/3}(\log p)^{32/3}=p^{11/6+o(1)}\). This does **not** improve 43/24 (11/6 − 43/24 = 1/24). The uniform second norm is \(\|H_\alpha(\cdot,t)\|_2\ll p^{7/6+o(1)}\), against Round 187's RS value \(p^{55/48+o(1)}\).
- **Conditional on X = O(p^{1+ε})** (any g with the cap): covariance \(O(p^{3/2+\varepsilon})\). The thresholds against 7/4, 43/24 and Round 184 Prop. 1(ii) are ε = 1/4, 7/24 and 2/7.
- **X = O(p), or more generally \(\Gamma_{\rm tot}X=O(p^{3/2})\), or \(T_0=O(p^{3/2}/W)\), gives the one-match target O(p^{3/2}).** No six-word, affine-energy or near-critical input is needed.
- At the first-mass target \(X=O(p^{1+1/1280})\) the covariance is \(O(p^{3/2+1/1280})\).

### Consistency
- **Floors.** On (NC), \(X\ge(2-o(1))p\) (Round 184 Prop. 2) and \(\Gamma_{\rm tot}\le(\frac12+o(1))\sqrt p\) (Round 183). The Theorem A bound never drops below its own floor \(\asymp p^{3/2}\), so there is no conflict with any accepted lower bound.
- **Square control** (Round 184 Prop. 5, \(\mathbb F_{r^2}\)). Theorem A is field-general: Lemmas A1–A2 use only Gauss sums and orthogonality. All primality enters through X. In the subfield configuration \(X\ge(1-o(1))q^{3/2}\), and Theorem A then gives nothing below \(q^{2}\). This agrees with Round 184's statement that any power saving must come from a prime-only input, here the one in X (Round 187 Lemma C's characteristic term).
- **b1′ saturation** (Round 182 Prop. 4, Round 183 Cor. 1.3). Theorem A does not bound \(\|\pi\|\). It bounds π on the cone spanned by the \(\bar\alpha^\circ\) with weights ω ≥ 0. That cone avoids the s = 1 row direction in the sense of Lemma A2. No conflict.

## 4. What a new route must control (exact terms)

| route | quantity | needed for < 7/4 (\(\Gamma_{\rm tot}\asymp\sqrt p\)) | needed for the target | proved now | models (§5) |
|---|---|---|---|---|---|
| Theorem A, uniform | \(T_0=c+\sum_{\lambda\ne1}g(\lambda)\Delta(h_{0,\lambda})\) | \(T_0\le p^{5/4-\delta}\) | \(T_0=O(p)\) | \(T_0\le X\ll p^{4/3+o(1)}\) | \(T_0/c\approx1.2\)–7.4 (sector 2.1 → 1.17); \(T_0/X\approx0.06\)–0.76 |
| Theorem A, averaged | \(\mathcal T=\sum_\lambda c_g(\lambda)\Delta(h_{0,\lambda})\) | \(\mathcal T\le p^{7/4-\delta}\) | \(\mathcal T=O(p^{3/2})\) | \(\mathcal T\le\Gamma_{\rm tot}X\ll p^{11/6+o(1)}\) | \(\mathcal T/p^{3/2}\le4\) |
| through X | \(X=E_Q(h)\) (`cand:slope-row-mass-x`) | \(X\le p^{5/4-\delta}\) | \(X=O(p)\) | \(p^{4/3+o(1)}\) (point–line floor) | \(X/p\approx0.3\)–8 |
| operator | dilation-fibre energy \(E_{\ne1}(\mu)\) | \(<p^{5/2}\) | \(O(p^2)\) | \(\le\mathcal E\ll p^{8/3+o(1)}\) | \(E_{\ne1}/p^2\le16\) |
| operator, pointwise | \(\sup_{\lambda\ne1}D(\lambda)\) | \(\le p^{1/2-\delta}\) | O(1) | \(\le c\ll p\) | 1–43 |

**The binding term is X**, at the point–line floor \(p^{4/3}\) of Round 187.
- Reaching the 7/4 threshold through X needs \(X\le p^{5/4-\delta}\).
- Inside the Round 187 pricing, both of its binding places must move:
  - **Light levels.** The Young term \(\tau_0G^3\) must be \(\le p^{5/4}\), so the light/heavy split must sit at \(\tau_0\le p^{-1/4-\delta}\). Round 187 Prop. P′ prices heavy pairs only down to heights \(p^{-1/6}\); at e = 1/5 whole level sets already give T3 excess +1/120 (audit §2.3).
  - **Height 1.** The pair energy of level sets of size \(N\asymp\sqrt p\) must be below \(N^{5/2}\). Lemma M′ gives \(N^{8/3}\). The MPRRS-type \(N^{5/2}\) is known only for structured products (Round 186 §6.3) and would land exactly on 7/4, not below.
- Alternatively, a direct bound on \(T_0\) or \(\mathcal T\) could use the extra weight \(g(Y'/Y)\), which the reduction to X discards.

**The generic six-word class.** It is no longer necessary for the one-match target: X = O(p) suffices by Theorem A. It remains open as the operator-norm route b1″ (\(\|R\pi(\Delta_G)R\|=O(p^{3/2})\), Round 183). Nothing here bounds it. The mission asked to keep it separate.

## 5. Evidence (floating point; models only; not certificates)

`paley-188-bpp-models.py P …` builds:
- flat laws ν = 1_S/|S| on \(S\subset\mathbb Z/n\), \(|S|\approx n/\sqrt p\), with S random (`rand`), a random half of an interval of length 2|S| (`halfint`), A + A for a random A (`sumset`) or an interval (`interval`);
- a control `sector`, g = 1/2 on a random inversion-closed subset of the sector \(T_+\) of size ≈ √p. It is not of the form |f|², but it has \(M_1\approx p\) as on (NC). Theorem A (ii) and Lemmas A1–A2 hold for it; (i) uses ω ≥ 0, which this control need not satisfy.

The flat laws are far from (NC) (\(M_1\approx p/2\)), as Round 184 found for every flat-law model. The ratios below come from the runs at p ∈ {101, 197, 401, 601, 809} (full affine-autocorrelation table) and p ∈ {1009, 1201, 1601, 2003} (no table). Run time is under a minute per prime list.

| model, p | \(\Gamma_{\rm tot}/\sqrt p\) | \(M_1/p\) | \(X/p\) | \(\mathcal E/p^2\) | \(E_{\ne1}/\mathcal E\) | max D | weighted fluct / mean | Thm A (pT/4) / fluct | OP bound / fluct |
|---|---|---|---|---|---|---|---|---|---|
| sector, 401 | 0.54 | 0.92 | 1.86 | 0.99 | 0.94 | 7.6 | 0.017 | 10.9 | 13.2 |
| sector, 809 | 0.53 | 0.95 | 1.96 | 1.12 | 0.95 | 7.3 | 0.008 | 17.3 | 27.2 |
| sector, 1601 | 0.53 | 0.99 | 2.13 | 1.28 | — | — | 0.006 | 21.8 | 41.0 |
| interval, 809 | 0.68 | 0.48 | 0.68 | 0.19 | 0.74 | 15.3 | 0.16 | 6.7 | 3.1 |
| interval, 1601 | 0.67 | 0.48 | 0.64 | 0.17 | — | — | 0.16 | 6.5 | 3.0 |
| sumset, 601 | 0.96 | 1.97 | 8.0 | 15.9 | 0.98 | 42.7 | 0.011 | 4.9 | 3.5 |
| rand, 1601 | 0.12 | 0.47 | 0.45 | 0.05 | — | — | 0.002 | 20.0 | 5.1 |

Reading (models only):
- \(\Lambda_0/X=1.000000\) in every run (Lemma A1).
- The weighted fluctuation is far below the mean term \(WM_1^2G^2/p\), which is the target scale \(p^{5/2}\). In `sector` it falls from 3% to 0.6% of the mean as p grows from 101 to 1601. No model shows a power excess.
- \(\mathcal E(\mu)/p^2\) is bounded in `sector` (1.0–1.4) and `interval`. It grows in `sumset`, where \(G/\sqrt p\) itself grows to 2 (the model's cap constant drifts). This tracks X, as Round 183 found for coset models.
- The dilation fibre carries most of the affine energy (74–98%), as §2 predicts. max D is bounded in `sector` (6–9) and grows slowly in `interval` (6 → 15) and `sumset`.
- The Theorem A and OP bounds are both within constant factors of the truth here. Theorem A's averaged bound is the better of the two in `sector`.
- The uniform bound (i) holds in every run, with \(\max_t\|\pi\varphi_t\|^2/(pT_0)\) between 0.04 (`rand`) and 0.64 (`sector`). So it is within a factor of about 2 of the worst t in the sector control.
- \(T_0/c\) lies in 1.2–7.4. In `sector` it falls from 2.1 to 1.17 between p = 101 and 2003, and \(T_0/X\approx0.16\)–0.26 there. This fits the random-like heuristic \(T_0-c\approx(G/p)X\ll c\). The trivial step \(T_0\le X\) loses a factor of 4–17 in the models.
- These are not the actual near-critical g. Small p cannot test an exponent.

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved.** Hypotheses: the actual chart and positive completion of Rounds 171–178; ν ≥ 0 a probability (so ω ≥ 0); (H3) g(1/x) = g(x); the cap only where stated.
- (a1) Proposition 1, the route floors (method statements): RS ≥ \(p^{13/8}\); point–plane pricing ≥ \(p^{5/2}\), i.e. 7/4; OP reaches \(p^{3/2}\) iff \(\Gamma_{\rm tot}^2\mathcal E=O(p^3)\).
- (a2) Proposition B: \(\sum_\beta\Delta(\lambda,\beta)=C(\lambda)\); \(\Delta\le c\); \(\mathcal E(\mu)\le cX+\sum_{\lambda\ne1}C(\lambda)D(\lambda)\le cM_1^2\). Any μ ≥ 0.
- (a3) Corollary B1: covariance \(\ll p^{3/2}+\Gamma_{\rm tot}\Gamma_2p\) (cap), and \(\ll p^{\min(1+2\gamma,\gamma+4/3,43/24)+o(1)}\) with Round 187.
- (a4) Lemma A1: \(m'(b)=c_h(b)\) on \(Q\setminus\{1\}\), so \(\Lambda_0=X\). Uses (H3).
- (a5) Lemma A2: \(\|F_\mu\chi\|^2=pS_0(\chi)-|\hat m(\chi)|^2\) and \(S_0(\chi)=\sum_\lambda\chi(\lambda)\Delta(\lambda,0)\le\Lambda_0\). Any μ ≥ 0.
- (a6) Theorem A: \(\|\pi\varphi_t\|^2\le pT_0\le pX\) uniformly in t (ω ≥ 0); \(\sum_t\|\pi\varphi_t\|^2\le p\mathcal T-G^2X\le p\Gamma_{\rm tot}X\). One-match covariance \(O(p^{3/2}+\min(W,\Gamma_{\rm tot}/4)X)\) (cap for the mean term).
- (a7) Corollary A: unconditional \(p^{11/6+o(1)}\), not an improvement. Every exponent is exact in `paley-188-bpp-exponents.py` (`ALL OK`).

**(b) Conditional.**
- (b1) \(X=O(p^{1+\varepsilon})\) gives covariance \(O(p^{3/2+\varepsilon})\). At ε = 0, or with \(\Gamma_{\rm tot}X=O(p^{3/2})\), this is the one-match target, with no six-word and no affine-energy input. At \(\varepsilon=1/1280\) (the first-mass target) it is \(O(p^{3/2+1/1280})\).
- (b2) \(\Gamma_{\rm tot}=O(p^{1/4})\), i.e. \(\mathcal E(\nu)=O(p^{1/4}/n)\), gives the target. \(\Gamma_{\rm tot}=O(p^\gamma)\) with γ < 5/12 gives an exponent below 7/4.
- (b3) \(E_{\ne1}(\mu)\le p^{5/2-\delta}\) gives \(p^{7/4-\delta/2}\) through OP when \(\Gamma_{\rm tot}\asymp\sqrt p\); \(\sup_{\lambda\ne1}D\le p^{1/2-\delta}\) suffices for this.
- (b4) \(T_0-c=O(p)\) (uniform branch) or \(\mathcal T=O(p^{3/2})\) (averaged branch) gives the target.

**(c) Evidence.** Exact integer identities at p ≤ 37; floating character identities at p ≤ 53; floating models at p ≤ 2003 (§5).

## Remaining gap

1. **One-match.** Accepted \(O(p^{43/24+o(1)})\), unchanged. The cheapest sufficient statements are now:
   - **X ≤ p^{5/4−δ}** for an exponent below 7/4 (Theorem A). The Round 187 point–line pricing sits at \(p^{4/3}\), a gap of \(p^{1/12}\). It needs a height-1 pair energy below \(N^{5/2}\) together with light-level pricing below \(p^{-1/4}\).
   - **X = O(p)**, or \(\Gamma_{\rm tot}X=O(p^{3/2})\), for the target.
   - A direct bound on \(T_0\) that uses the multiplicative-triangle weight \(g(Y'/Y)\).
   - The operator route (dilation-fibre energy, or b1″ with the six-word class) remains an alternative.
2. **First mass.** Unchanged: X, \(\mathcal M_w\) at \(p^{4/3+o(1)}\) against \(p^{1+1/1280}\). It now shares its estimate with the one-match target.
3. **Support energy.** Γ₂ is unchanged. The useful one-match threshold improves from γ < 3/8 to γ < 5/12 (for 7/4), and γ ≤ 1/4 gives the target.
4. **Unchanged:** the zero-match estimate, the generic J sum \(O(p^{9/4})\), the cold route, the Round 176/180 fixed-a generic squared mass, and the original theta-limit target. **Nothing here proves or refutes the original target.**

## Shared estimates (for the coordinator)

- **`cand:slope-row-mass-x` (X form)** becomes the one-match quantity through Theorem A.
  - Before this report, its one-match use was capped at 43/24 → 7/4 (point–plane).
  - After it, the one-match covariance is \(O(p^{3/2}+\sqrt p\,X)\) with no 7/4 floor.
  - Scale for the one-match target: X = O(p). Scale for the first mass: \(X=O(p^{1+1/1280})\).
  - This report proves no new bound on X.
- **Γ₂ / support energy.** The threshold γ ≤ 1/4 gives the one-match target (Corollary B1). No Γ₂ bound is proved.
- No new shared candidate ID is proposed. The touch is on the existing `cand:slope-row-mass-x`.

## What would change the proof plan

- **If an audit accepts Theorem A:** the one-match and first-mass obligations merge into X near its floor. The six-word class becomes optional. The deferred `ordinary-prime-height-one-structured-energy` call gains value: its payoff was capped at 43/24 → 7/4, but through Theorem A every saving in X now moves the one-match exponent one-for-one (3/2 + ε). It needs ε < 7/24 to beat 43/24.
- **If a direct bound \(T_0=O(p^{1+o(1)})\) were found**, it would give the one-match target without settling the first mass. A natural test is whether \(g(Y'/Y)\) gives a power saving over \(X\) in \(T_0-c\). In models \(T_0/c\in[1.2,7.4]\) and \(T_0/X\in[0.06,0.76]\), with no growth in p.
- **If the audit finds an error in Lemma A1 or A2,** the operator-route results (Proposition B, Corollary B1) stand on their own.

## Ranked next tests

1. **Price \(T_0-c=\sum_{Y\ne Y'}g(Y)g(Y')g(Y'/Y)\,[\ldots]\) directly.** It is a five-weight, three-variable sum whose expected size is \(\ll\sqrt p\). Combine Round 187's level extraction with the multiplicative triangle \(g(Y)g(Y')g(Y'/Y)\). A saving of \(p^{1/12}\) over X gives an exponent below 7/4 for the one-match covariance (uniform branch, with \(W\le G\)).
2. **X below the point–line floor:** the deferred height-1 structured-energy call, now with the larger payoff above. Below 7/4 needs height-1 pair energy \(<N^{5/2}\) and light levels down to \(p^{-1/4}\).
3. **Γ_tot = O(p^{1/4})** for the near-critical law: an additive-energy power saving \(\mathcal E(S)\ll|S|^{5/2}\) for the flat support. This is the support-energy call at a sharper, now sufficient, scale.

## Replay

```
.venv/bin/python -B research/paley-188-bpp-exponents.py           # exact; prints ALL OK
.venv/bin/python -B research/paley-188-bpp-models.py --check      # exact + floating identities; ALL CHECKS OK (~2 s)
.venv/bin/python -B research/paley-188-bpp-models.py 101 197 401 601 809       # models with the Delta table (~1 min)
.venv/bin/python -B research/paley-188-bpp-models.py --nodelta 1009 1201 1601 2003   # models, no table (~2 min)
```
numpy 2.3.5. The model seeds are deterministic in (p, model).

## Verdict

**Inconclusive** in the mission's sense.
- **Best unconditional exponent:** 43/24 (Round 187), unchanged. The new affine-energy-free route gives 11/6 now. It has method floor 3/2.
- **Answer to the question:**
  - Yes, there is a twisted second-norm estimate that avoids the affine energy and uses the slope-row bounds: \(\|H_\alpha(\cdot,t)\|_2^2\le M_1^2G^2/p+pX\) uniformly in t (Theorem A).
  - It goes below 7/4 exactly when \(X<p^{5/4}\), which the current slope-row bound \(p^{4/3}\) does not reach.
  - Not every route through \(\mathcal E(\mu)\) floors at 7/4. Only point–plane pricing of \(\mathcal E\) does. RS floors at 13/8; OP reaches 3/2 at the optimal energy.
- **Binding term:** X (equivalently \(T_0\le X\)) at the point–line floor \(p^{4/3}\). A new route must bring it below \(p^{5/4}\). For the operator route, the dilation-fibre energy \(E_{\ne1}(\mu)\) must fall below \(p^{5/2}\).
