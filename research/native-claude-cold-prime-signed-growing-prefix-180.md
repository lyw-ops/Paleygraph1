# Signed growing prefix after height 602: exact form of the gap, a bounded-delocalization criterion and evidence

Candidate report for mission `coordination/missions/round-180/cold-prime-signed-growing-prefix.md`. It is an agent draft, not an acceptance. No repository file was changed. Scripts and outputs are in this scratchpad directory, `r180/`.

## Result summary

**Outcome: inconclusive.** The growing-prefix confinement is neither proved nor refuted. The mission's "tension" turns out to be a normalization artifact. I identify the exact uncontrolled signed sum and give a sharp conditional criterion with explicit constants. I also show that several natural routes cannot close the prefix.

1. **(a) The tension is not a contradiction.** The normalized increment at height 602 is small but stays positive: \(0<\liminf_p\inf_Q\|R_{602}\|_{2,n}\le\limsup_p\sup_Q\|R_{602}\|_{2,n}<9.1\cdot10^{-209}\). It is not of order one. Round 179's lower bound \(c\sqrt n\) applies only to the unnormalized counting norm. Coordinate confinement in radius \(\rho\) only requires a bounded sup-to-RMS ratio, called the *delocalization ratio* \(\Lambda\), and the allowed ratio is astronomically large (\(\Lambda\lesssim6.5\cdot10^{205}\) for \(\rho=0.025\)). It must, however, be **independent of \(n\)**.
2. **(a) Exact uncontrolled sum.** For every height \(h\) and coordinate \(i\),
 \(R_{h+1,i}=\tfrac{\sqrt n}{2}\,\mathbb E_n\big[(\tau_iS)\,\tilde D_hR_h\big]\).
 Here \(\tau_iS=2\sqrt nKe_i\) is the cyclically shifted seed, \(\tilde D_h\) is the actual secant multiplier, and \(\mathbb E_n\) is the normalized coordinate average. Confinement requires the maximum over all \(n\) shifts of these correlations to be within a bounded factor of their root mean square. The bounded factor may grow at most like \(\gamma^{k}\) with \(\gamma<1/q\).
3. **(b) Criterion D(\(\Lambda,\gamma\)).** Suppose the bound \(\|R_{602+k}\|_\infty\le\Lambda\gamma^k\|R_{602+k}\|_{2,n}\) holds along the confined prefix, with \(q\gamma<1\) and \(\Lambda\cdot9.1\cdot10^{-209}<(\rho-\eta)(1-q\gamma)\). Then the Round 173 prefix test holds for all sufficiently large eligible primes, uniformly on \(Q\) and both lifts, at \(t_0=n\).
4. **(a) Method obstructions.** Each of the following fails as \(p\to\infty\):
   - every norm-only estimate (Hölder combinations of the row-\(\ell^2\) contraction and the entrywise price), since each loses exactly \(\sqrt n\);
   - every bound with a ratio \(\Lambda_n\to\infty\), including a sub-Gaussian \(\sqrt{\log n}\);
   - every unsigned price rate \(\ge1\);
   - a moving Newton predictor, which only restates the same signed sum.
5. **(a; curve is floating point) A larger radius is allowed** up to about \(\rho\approx3.6\) with \(q(\rho)<1\), at cutoff \(k_n=\lceil c\log_2n\rceil\) with \(c>1/(2\log_2(1/q(\rho)))\). The radius \(3/8\) keeps \(c=4/7\). A larger radius only rescales the budget. It does not remove the requirement that \(\Lambda\) be independent of \(n\).
6. **(c) Evidence** comes from double precision at real \(t=a\) and at \(t=a+2^{-17}i\), for \(p\) from \(1009\) to \(10000121\), using the Jacobi-seed start. The increments are delocalized and Gaussian-like: the fourth-moment ratio is \(\approx3.00\) and sup/RMS \(\approx(0.9\text{–}1.0)\sqrt{2\ln n}\). The ratio does not grow with depth up to \(k=800\) in the linearized iteration, and the mark coordinate is not special. The lowest-complexity increment has an \(n\)-independent ratio of \(2.82\), which is compact-law saturation. The physical \(\ell^2\) rate is \(\approx0.240\), well below \(q\).

## Setup recalled

- **Parameters.** \(p\equiv1\pmod4\) prime, \(n=(p-1)/2\), \(a=2031/128\), \(Q\) the closed square of half-width \(2^{-17}\) about \(a\), \(N=4(a-2^{-17})\).
- **Map.** \(V_{h+1}=K\Phi_t(V_h)\), with \(\Phi_{t,i}(z)=\sqrt{4t+z^2}\) on the bulk and \(\sqrt{4n+z^2}\) at the physical mark \(i=0\) (so \(t_0=n\)).
- **Operator \(K\).** \(K\) is the real symmetric circulant on \(\mathbb Z/n\) with multiplier \(\chi(1-g^{2k})\in\{\pm1\}\) and \(0\) at \(k=0\) (`theta.paley_sign`, `smoothing.kernel_action`). So \(K^2=I-J\) and \(\|K\|_{2\to2}\le1\).
- **Seed and rows.** The seed is \(S=2\sqrt nKe_0\), with \(\|S\|_\infty<2.828428\). Rows start from the genuine nine-center row. The two quadratic lifts enter through the trace representations of the physical vectors and are inherited as in the cited rounds.
- **Norms and increments.** \(R_h=V_{h+1}-V_h\) and \(\|x\|_{2,n}^2=n^{-1}\sum|x_i|^2\).
- **Polydisk.** \(\mathcal P_\rho=\prod_i\{|z-V_{602,i}|\le\rho\}\). On it the scalar derivative is below \(q_\rho\): \(q_{0.025}=0.525\) (Round 173), \(q_{0.05}=0.535\) (Round 174), \(q_{3/8}=0.545\) (Round 177). For the 3/8 disk this is the seed-centred bound with \(|z-S_i|\le B=2.338\).
- **Lipschitz property.** The map is \(q_\rho\)-Lipschitz in normalized \(\ell^2\) on \(\mathcal P_\rho\), by convexity and \(\|K\|\le1\).
- **Round 173 test.** \(V_{602},\dots,V_{m_n}\in\mathcal P_\rho\), \(m_n=602+k_n\), \(k_n=\lceil(4/7)\log_2n\rceil\), with terminal sup clearance \(\eta\). Then \(\sqrt n\,q^{k_n}=o(1)\) closes the tail.
- **Known fixed prefix.** \(P_{5000}(R_{602})<0.01272\) (Round 174). The packet displacement bounds through \(V_{612}\) stay inside radius \(3/8\), the last being \(0.35998\) (Round 177). The packet rate is \(\|KD_{602}\|_{P_{5000}}<1.066\) (Round 162).

## Argument with full details

### 1. Size of the normalized increment (label a, inherits ineffective compact transfer)

Round 80 bounds the complex normalized residual at row 600 on \(Q\): \(\limsup_p\sup_Q\|R_{600}\|_{2,n}\le4(0.449922)^{600}\). Exact decimal arithmetic gives \(3.0507\cdot10^{-208}\). This bound uses the nine-center caps \(|U_j-S|\le1.94\) through height 600, fixed-height compact transfer on the closed square, and vanishing marked corrections.

The segments \([V_{600},V_{601}]\) and \([V_{601},V_{602}]\) satisfy \(|z-S_i|\le1.94+0.011+0.012=1.963<2.338\) (Rounds 126, 162, 177). Each lies in the convex seed-centred region where the scalar derivative is below \(0.545\) (Round 177). The mark derivative is \(O(n^{-1/2})\). Hence \(\|R_{h+1}\|_{2,n}\le0.545\|R_h\|_{2,n}\) for \(h=600,601\), and
\[
 \limsup_{p}\sup_{t\in Q}\|R_{602}\|_{2,n}\le 0.545^2\cdot3.0507\cdot10^{-208}<9.07\cdot10^{-209}=:\varepsilon^* .
\]
The lower bound follows from Round 179, \(\liminf\inf_Q\|R_{611}\|_{2,n}>0\), together with the upper contraction \(\|R_{611}\|_{2,n}\le0.545^9\|R_{602}\|_{2,n}\) inside the 3/8 disks. Those disks contain the fixed prefix through \(V_{612}\) by Round 177. So \(\liminf_p\inf_Q\|R_{602}\|_{2,n}>0\). Both thresholds are ineffective.

### 2. The tension, stated exactly (label a)

For \(x\in\mathbb C^n\), \(\|x\|_{2,n}\le\|x\|_\infty\le\sqrt n\|x\|_{2,n}\), and both inequalities are sharp. The constant vector \(\varepsilon\mathbf 1\) attains the left one, with unnormalized norm \(\varepsilon\sqrt n\).

Round 179's statement "unnormalized \(\ge c\sqrt n\)" is therefore compatible with a coordinate supremum of the same order as \(\varepsilon\). As long as the prefix stays in \(\mathcal P_\rho\), \(\|V_{602+k}-V_{602}\|_{2,n}\le\|R_{602}\|_{2,n}/(1-q)<2\cdot10^{-208}\) eventually. That is 206 orders of magnitude below \(\rho\).

Coordinate displacement can therefore be small exactly when the increments are *delocalized*: each coordinate is comparable to the RMS rather than to \(\sqrt n\) times it. Nothing in the second-norm data forbids this. Nothing in the existing sup-norm data proves it.

### 3. The uncontrolled signed sum (label a)

\(K\) is real symmetric and circulant, so \(K_{ik}=(Ke_i)_k=(\tau_iS)_k/(2\sqrt n)\). The exact secant identity \(R_{h+1}=K\tilde D_hR_h\), with \(\tilde D_h=\int_0^1\Phi_t'(V_h+sR_h)\,ds\) coordinatewise, gives
\[
 R_{h+1,i}=\frac{1}{2\sqrt n}\sum_{k\in\mathbb Z/n}S_{k-i}\,\tilde D_{h,k}\,R_{h,k}
 =\frac{\sqrt n}{2}\,c_i(h),\qquad c_i(h)=\mathbb E_n\big[(\tau_iS)\tilde D_hR_h\big].
\]
By Parseval, \(\big(n^{-1}\sum_i|c_i(h)|^2\big)^{1/2}=2\|R_{h+1}\|_{2,n}/\sqrt n\).

The quantity that is not controlled is
\[
 \max_{i}|c_i(h)|\ \text{ versus }\ \operatorname{RMS}_i\,c_i(h),\qquad 602\le h<602+k_n .
\]
These are \(n\) Jacobi-twisted correlations of the actual secant-weighted increment. The controlled parts are:

- the RMS, by Parseval and the \(\ell^2\) contraction;
- each summand, by \(|S_{k-i}\tilde D_{h,k}R_{h,k}|\le2.83\cdot0.545\,|R_{h,k}|\);
- the steps \(h\le611\), by Deligne-type packet prices.

The mark is \(i=0\), where \(R_{h+1,0}=\frac{\sqrt n}2\mathbb E_n[S\tilde D_hR_h]\). It is not singled out by the identity, and the numerics do not single it out either.

### 4. Norm-only estimates lose exactly \(\sqrt n\) (label a)

Put \(M=(K\tilde D)^jK\). The available estimates are a row-\(\ell^2\) bound \(\le q^j\) and an entrywise bound \(\|M\|_{\max}\ll n^{-1/2}(1.066)^j\) (Round 162). Hölder pairs a row's \(\ell^{r'}\) norm with an input's \(\ell^r\) norm, \(1/r+1/r'=1\), \(r\le2\). The row's \(\ell^{r'}\) norm is bounded by interpolating the \(\ell^2\) and \(\ell^\infty\) bounds. The input's \(\ell^r\) norm is bounded by \(n^{1/r}\) times its normalized norm.

The power of \(n\) is \(1/r-\tfrac12(1-2/r')=\tfrac12\) for every \(r\). Conversely, the data are attained up to constants. Take a flat row \(m\) (entries of modulus about \(\|m\|_2/\sqrt n\)) and \(y_k=\varepsilon\,\overline{m_k}/|m_k|\). Then \(|(My)_i|=\varepsilon\|m\|_1\asymp\sqrt n\,\varepsilon\|m\|_2\).

So no estimate built only from these operator norms can beat \(\sqrt n\). The improvement must come from the sign correlation between the rows of \((K\tilde D)^j\) and \(R_{602}\).

### 5. Criterion D(\(\Lambda,\gamma\)) (label b, proof of the implication is a)

**Hypotheses.**

- Fix \(\rho\in\{0.025,0.05,3/8\}\), \(q=q_\rho\), \(0<\eta<\rho\), \(\Lambda\ge1\), \(\gamma\ge1\) with \(q\gamma<1\) and \(\Lambda\varepsilon^*<(\rho-\eta)(1-q\gamma)\).
- Hypothesis D: there is \(p_0\) such that for every eligible \(p\ge p_0\), every \(t\in Q\), both lifts, and every \(0\le k<k_n\) with \(V_{602},\dots,V_{602+k}\in\mathcal P_\rho\),
\[
 \|R_{602+k}\|_\infty\le\Lambda\gamma^k\|R_{602+k}\|_{2,n}.
\]

**Conclusion.** For all sufficiently large eligible \(p\), \(V_{602},\dots,V_{m_n}\in\mathcal P_{\rho-\eta}\) uniformly on \(Q\). The Round 173 tail then gives the common stationary continuation on the interior of \(Q\) (radii \(0.05\) and \(3/8\) as in Rounds 174 and 177).

**Proof.** By §1 choose \(p_1\ge p_0\) with \(\|R_{602}\|_{2,n}\le\varepsilon'\), where \(\Lambda\varepsilon'<(\rho-\eta)(1-q\gamma)\), for \(p\ge p_1\). Induct on \(k\).

- If \(V_{602},\dots,V_{602+k}\in\mathcal P_\rho\), each segment \([V_{602+i-1},V_{602+i}]\) lies in the convex polydisk. Hence \(\|R_{602+i}\|_{2,n}\le q^i\varepsilon'\) for \(i\le k\).
- By D, \(\|V_{602+k+1}-V_{602}\|_\infty\le\sum_{i\le k}\Lambda(q\gamma)^i\varepsilon'<\rho-\eta\).
- The induction runs to \(k=k_n-1\), giving the terminal clearance \(\eta\).

**Numerical room** (\(\gamma=1\), \(\eta=\rho/2\)): \(\Lambda<6.5\cdot10^{205}\) for \(\rho=0.025\), \(1.3\cdot10^{206}\) for \(0.05\), and \(9.4\cdot10^{206}\) for \(3/8\) (`consts.py`).

### 6. What cannot close the criterion (label a, as statements about the method)

(i) **Unbounded ratio.** If \(\Lambda=\Lambda_n\to\infty\), including \(C\sqrt{\log n}\) or \(n^\delta\), the bound \(\Lambda_n\|R_{602}\|_{2,n}/(1-q\gamma)\) tends to infinity, because \(\liminf\|R_{602}\|_{2,n}>0\) (§1).

Starting at a later fixed height \(H\) does not help. Under confinement through \(H\), fixed-height compact transfer and Round 179's lower secant (\(.029/\sqrt5\) per step on the 3/8 cap) give \(\liminf\|R_H\|_{2,n}>0\) again.

From any fixed height, the \(\sqrt n\) conversion needs \(k\ge\log(\sqrt n\,\|R_H\|_{2,n}/\eta)/\log(1/q)\to\infty\) further steps. This is a dead zone of \(\tfrac12\log_{1/q}n-O_H(1)\) heights. A fixed-order moment bound \(\|x\|_\infty\le n^{1/2m}\|x\|_{2m,n}\) has the same defect.

(ii) **Unsigned price.** With a sup-dominating price whose secant rate is \(B\ge1\), the summed bound over \(k_n\) steps is at least \(k_nP(R_{602})\to\infty\). The Round 83 obstruction records show this happens at the cold floor for single-vertex collection (strict expansion \(>1.0000173\)).

A price route closes iff it supplies a secant rate \(\kappa\) with \(0.01272/(1-\kappa)<\rho-\eta\). That means \(\kappa<0.966\) for \(\rho=3/8\) and \(\kappa<0.49\) for \(\rho=0.025\) (as \(\eta\to0\)). A price bound is pointwise Deligne-type, so it is automatically uniform in \(n\).

(iii) **Moving predictor.** The frozen Newton correction is \(\sum_kL^kR_{602}\) with \(L=K\operatorname{diag}\Phi'(V_{602})\). Its coordinate supremum is, up to the nonlinear remainder, the same signed prefix sum as in §3. The available entrywise resolvent bound (Round 162) gives only \(O(n^{0.545})\|R_{602}\|_{2,n}\), which is worse than \(\sqrt n\). A genuine moving predictor therefore faces the identical \(n\)-uniform sup requirement. It is not an independent route.

### 7. Larger radius in place of 0.025 (label a for 0.025, 0.05, 3/8 by inherited rational checks; floating-point curve otherwise)

Use the Round 177 seed-centred bound with \(B=1.963+\rho\). Then \(q(\rho)=\max_{u\in[0,1]}\sqrt{A(u)/(A(u)+C(u))}\), maximized numerically (`qcurve.py`). The monotonicity shortcut of Round 177 fails for \(\rho\ge0.75\), so the maximum is taken over a grid of 200001 points.

| \(\rho\) | 0.025 | 0.05 | 3/8 | 0.5 | 1 | 2 | 3 | 3.5 |
|---|---|---|---|---|---|---|---|---|
| \(q(\rho)\) | 0.517 | 0.519 | 0.5441 | 0.553 | 0.589 | 0.684 | 0.841 | 0.954 |
| minimal \(c\) | 0.526 | 0.529 | 0.569 | 0.586 | 0.654 | 0.914 | 2.00 | 7.35 |

Analyticity requires \(N-2B^2>0\), that is \(\rho<3.67\). Any such radius gives contraction \(q<1\) and a valid tail with \(k_n=\lceil c\log_2n\rceil\) for \(c\) above the minimum. The value \(c=4/7\) works up to \(\rho\approx0.39\) (\(q<2^{-7/8}=0.54525\)). Note that the exact maximum at \(\rho=0.025\) is below the Round 173 value \(0.525\), which used a cruder curvature bound.

A larger \(\rho\) enlarges the budget linearly and the packet range of Round 177. It changes neither §6(i) nor the need for an \(n\)-independent \(\Lambda\).

## Proved vs conditional vs evidence

- **(a) Proved for all sufficiently large eligible primes**, with ineffective thresholds inherited from fixed-height compact transfer:
  - §1 bounds: \(0<\liminf\le\limsup<9.07\cdot10^{-209}\) for \(\|R_{602}\|_{2,n}\) on \(Q\);
  - the exact identity of §3;
  - the \(\sqrt n\)-invariance of norm-only estimates in §4;
  - the implication in §5;
  - the method obstructions in §6.
- **(b) Conditional.**
  - Hypothesis D(\(\Lambda,\gamma\)) implies the Round 173 prefix test and the common continuation on the interior of \(Q\).
  - A sup-dominating secant price rate \(\kappa<0.966\) on \(\mathcal P_{3/8}\) also implies them.
  - Neither condition is established.
- **(c) Finite/numerical evidence.**
  - Settings: double-precision NumPy FFT, not outward-rounded. Jacobi-seed start \(V_0=0\), not the nine-center row. Heights 2–40, plus a linearized power iteration at the converged real row up to \(k=800\). Real \(t=a\), and \(t=a+2^{-17}i\) for \(p=10009,100049\). One physical multiplier; the two lifts were not separated.
  - Primes: 1009, 10009, 100049, 1000033, 4000037, 10000121.
  - The table below lists sup/RMS of the increments (fourth-moment ratio \(m_4\) in parentheses). In the linearized iteration, \(m_4\approx3.00\) for all \(p\ge10^5\) at all depths up to 120 or 800. There is no depth trend, and \(|R_{h,0}|/\mathrm{RMS}\in[0.03,2.6]\).

  | \(n\) | \(\sqrt{2\ln n}\) | \(j=2\) | \(j\approx5\) | \(j\approx10\) | lin. \(k=120\) or 100 |
  |---|---|---|---|---|---|
  | 5004 | 4.13 | 2.75 | 3.44 | 3.69 | 3.80 |
  | 50024 | 4.65 | 2.78 (2.52) | 4.28 (3.01) | 4.12 | 4.22 |
  | 500016 | 5.12 | — | 5.08 | — | 4.78 |
  | 2000018 | 5.39 | 2.818 (2.50) | 4.98 (2.99) | 4.85 | 5.35 |
  | 5000060 | 5.55 | 2.819 (2.50) | 5.15 (3.01) | 5.39 | 4.79 |

  - The physical \(\ell^2\) rate is \(0.2400\)–\(0.2402\) for \(n\ge5\cdot10^4\), near the seed-only heuristic \(\sqrt{\mathbb ES^2}/(2\sqrt a)=1/\sqrt a\approx0.251\) (from \(\mathbb ES^2=4\) and Round 80's conditional covariance identity (4)). The fixed real row has \(\|V^*\|_\infty\) rising slowly: 3.27, 3.33, 3.35, 3.40.
  - Reading: increments are delocalized, with Gaussian coordinate laws, so the ratio grows like \(\sqrt{2\ln n}\) for moderate \(n\), consistent with \(\gamma=1\). The low-complexity increment saturates at an \(n\)-independent ratio, as a compact law with bounded support would.
  - These are floating-point diagnostics only. They say nothing about height 602 itself, which is machine-converged.

## Exact remaining gap

Prove, uniformly in \(n\), \(t\in Q\) and both lifts, for \(602\le h<602+k_n\) while the prefix is confined:
\[
 \max_{i\in\mathbb Z/n}\Big|\sum_{k}S_{k-i}\tilde D_{h,k}R_{h,k}\Big|
 \le \Lambda\gamma^{h-602}\Big(\sum_i\Big|\sum_kS_{k-i}\tilde D_{h,k}R_{h,k}\Big|^2\Big/n\Big)^{1/2},
\]
with \(q\gamma<1\) and \(\Lambda\) independent of \(n\), at most about \(10^{205}\). Equivalently, prove any other summable \(n\)-uniform sup decay of the increments with total below \(\rho-\eta\).

The evidence says the natural probabilistic bound is \(\Lambda\sim\sqrt{2\ln n}\). That bound is enough for every \(n<\exp(10^{411})\) but not for all large primes. An asymptotic proof must therefore use a saturation mechanism: a bounded compact coset supremum of the increment fields at each height, transferred to heights \(602+O(\log n)\). Alternatively it must use a signed Deligne-type price with secant rate \(<0.966\) on \(\mathcal P_{3/8}\).

The existing fixed-height compact transfer, the \(\ell^2\) contraction \(q\), the entrywise frozen resolvent, and the unsigned packet rates (\(1.048\), \(1.066\)) do not supply either one. Derivative transfer and the uniform stationary domain remain separate obligations.

## Two ranked next tests

1. **Signed cross-vertex price rate of the secant operator on \(\mathcal P_{3/8}\) about \(V_{602}\).**
   - Collect identical geometric simples across vertices and histories before taking absolute values, as in the Round 83 next test. Bound \(\sup_h\|K\tilde D_h\|_{P}\) in a norm \(P\ge\|\cdot\|_\infty\) with \(P(R_{602})\le0.01272\).
   - Success with \(\kappa<0.966\) (strict, outward-rounded) proves the growing prefix for all large primes, since price bounds are pointwise.
   - Heuristic motivation: the seed-only multiplier \(K(S/(2\sqrt t)\,\cdot)\) has rate at most \(s_p/\sqrt t\approx0.710\) by Round 80's \(D_{j+1}\le2s_pD_j\). The excess up to 1.066 comes from the nine-center part \(V_{602}-S\) (dimension budget 1.963), which is where signed collection can act.
   - Failure (an expanding signed-collected rule) closes the price route.
2. **Compact coset supremum of the increment fields at fixed heights.**
   - Establish fixed-height sup transfer: physical \(\max_i|R_{h,i}|\to\sup_{\text{coset}}|U_{h+1}-U_h|\) as \(p\to\infty\). The lower direction follows from equidistribution and continuity. The upper direction needs uniform absolute convergence on the fieldwise groups.
   - Then bound \(\sigma_h=\sup_{\text{coset}}|U_{h+1}-U_h|\) for \(602\le h\le612\) and test for geometric decay.
   - A compact displacement \(\sup|U_{602+K}-U_{602}|>\rho\) at a fixed \(K\) would refute the criterion for all large primes, which is the mission's refutation mode.
   - Uniform geometric decay of \(\sigma_h\) gives the saturation input needed for D. A growing-height transfer is still required afterwards.

Files (scratchpad, `r180/`): `rows.py` (physical map), `exp1.py`–`exp4.py` (diagnostics; `exp4.out` holds the large-prime run), `consts.py` (exact decimal and rational constants), `qcurve.py` (radius curve).
