# Positive repair within the reference mass reserve

At width \(s=1/16\), the sorted-defect repair costs \(0.24172\) on the plus side of \(p=153649\), with \(1-c=0.15042\). A repair using repeated projections onto the opposite Fourier sector costs \(0.11439\). At the nearby square \(389^2\), the **minimum** positive repair costs \(0.47868\), with \(1-c=0.15402\). The square optimum is attained by translates of the elementary witness at the subfield annihilator. The fixed-width obstruction holds asymptotically at every \(s<\sqrt2-1\), with an explicit excess over the reserve.

The reference is the actual reciprocal optimizer from [Round 15](parallel-transport-15.md). The finite-order comparison tests both signs at fixed width and at \(s=q^{-1/4}\). The [ETH problem](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/) requires a prime-aspect estimate.

## 1. The positive and signed repair problems

Put \(n=(q-1)/2\), \(j=\mathbf1/\sqrt n\), and \(U_\sigma=\mathbb Rj+V_\sigma\), where \(P_\sigma\) projects onto \(V_\sigma\). With \(x=A_\sigma(s)\), \(y=A_{-\sigma}(s)\), and \(c=\langle j,y\rangle\), let

$$H=H_0=(J+P_{-\sigma})y,\qquad a=\langle e_0,H\rangle>0.$$

Write \(C_i=-H_i\) off the mark, \(C_0=0\), and \(d=C_+\). For \(F=d\) or \(C\) define

$$
\Gamma(F)=\min_{G\in U_{-\sigma},\ G\ge F}\langle j,G\rangle .
\tag{1}
$$

The choice \(F=d\) gives a positive repair. With \(F=C\), \(G\) can spend positive slack of \(H\) at bulk coordinates. In both cases \(H+G\ge0\) and its mark is \(a+G_0\ge a\). If \(m_0=\sqrt{M_\sigma(0)}=\sqrt n/\theta_\sigma\), then

$$
m_0\ge \frac{a+G_0}{c+\langle j,G\rangle}.
\tag{2}
$$

Indeed the normalized elementary endpoint pairing with an anchored optimal \(b_0\in U_\sigma\) gives \(\langle b_0,H+G\rangle=m_0(c+\langle j,G\rangle)\ge a+G_0\). The positive budget \(\langle j,G\rangle\le1-c+\epsilon\) yields \(m_0\ge a/(1+\epsilon)\). At fixed \(s\) the more stringent budget \(a-c\) suffices for \(m_0\ge1\).

The finite-dimensional LP dual in (1) is

$$
\Gamma(F)=\max\{\langle B,F\rangle : B\in U_\sigma,\ B\ge0,\ \langle j,B\rangle=1\}.
\tag{3}
$$

The primal is feasible by a constant shift and the dual is compact and nonempty. The signed optimum is exactly

$$
\Gamma(C)=a/m_0-c .
\tag{4}
$$

For the upper bound take \(Y\in U_{-\sigma}\) to be a nonnegative optimal endpoint spectrum of mark \(a\). Its mean coordinate is \(a\sqrt{M_{-\sigma}(0)}=a/m_0\) by theta reciprocity. Then \(G=Y-H\) is feasible in (1) with \(G_0=0\). The reverse inequality follows from (2). As a result, using the unrestricted signed LP by itself evaluates the endpoint. A constructive upper bound on that LP can instead use only \(H\) and the known Fourier set. The positive optimum always dominates (4) and can be strictly larger. The dense example \(p=401,\sigma=+,s=1/16\) gives \(0.08837\) for \(\Gamma(d)\) and \(0.07550\) for \(\Gamma(C)\).

## 2. Project before paying for the upper tail

Let \(R\in U_{-\sigma}\) be the [nonnegative Jacobi row](parallel-transport-15.md#deflate-the-expensive-part-of-the-dual) with \(R_0=1\) and \(\sum_i R_i=n/h_R\), where \(h_R=1+2|D_{-\sigma}|/(\sqrt q+1)\). For **any** \(A\in U_{-\sigma}\) and real threshold \(t\), the explicit row

$$
G=A+t\mathbf1+R*(F-A-t)_+
\tag{5}
$$

dominates \(F\), since the zero shift in the convolution gives \((F-A-t)_+\) and all other terms are nonnegative. The repair uses signed entries in \(A\) even when the finished \(G\) is positive. By choosing \(t\) at an upper order statistic one gets

$$
\langle j,G\rangle
=\langle j,A\rangle+\frac{\sqrt n}{h_R}T_{h_R}(F-A),
\tag{6}
$$

where \(T_h\) sums the largest \(h\) entries, with a fractional last entry. Here \(T_h\) acts on signed residuals and \(t\) can be negative. The identity follows by minimizing \(\sqrt n\,t+(\sqrt n/h_R)\sum_i(F_i-A_i-t)_+\). Choosing \(A=0\) recovers the sorted-defect bound. Choosing \(A=\alpha P_{-\sigma}d\) gives a one-projection bound as in [negative pairing](negative-pairing.md#an-explicit-majorant-and-a-projected-point-cap-comparison).

Use a proposed normalized mean \(b\) and project onto the affine space \(L_b=bj+V_{-\sigma}\) and the orthant \(B_F=\{G:G\ge F\}\). The Douglas–Rachford update and its affine projection are

$$
A_\nu=bj+P_{-\sigma}w_\nu,\qquad
w_{\nu+1}=w_\nu+\max(2A_\nu-w_\nu,F)-A_\nu .
\tag{7}
$$

Every \(A_\nu\) gives a certificate (5)–(6), including at infeasible proposed means. If \(L_b\cap B_F\) contains \(W\), then for any integer \(N\ge1\) the least repaired mass over the first \(N\) projections satisfies

$$
\min_{\nu<N}\langle j,G_\nu\rangle
\le b+\sqrt{\frac n{h_R}}\frac{\|w_0-W\|_2}{\sqrt N}.
\tag{8}
$$

To prove this, the update is the average of the identity and the composition of the two reflections in the convex sets, each nonexpansive. Both fix \(W\). The parallelogram identity gives
\(\|w_{\nu+1}-W\|^2+\|w_{\nu+1}-w_\nu\|^2\le\|w_\nu-W\|^2\).
Every coordinate violating \(A_\nu\ge F\) has a positive step at least as large as its violation. Thus \(\|(F-A_\nu)_+\|_2\le\|w_{\nu+1}-w_\nu\|_2\) and \(T_{h_R}(F-A_\nu)\le\sqrt{h_R}\|(F-A_\nu)_+\|_2\). This proves (8). Taking \(b\) down to the optimum and enough iterations approaches \(\Gamma(F)\) at any individual field order. Formula (8) alone has a factor of order \(n^{1/4}\). The actual upper-tail price in (6) is the quantity measured in the replay.

## 3. A sharp square obstruction at fixed width

For \(q=\ell^2\), take \(\sigma=+\) and the subfield annihilator \(I=(\mathbb F_\ell^\times)^\perp\), of size \(k=(\ell+1)/2\). The [square endpoint](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy) has \(m_0=k/\sqrt n\) and \(b_0=\mathbf1_I\). In particular

$$
\Gamma(d)\ge\frac{\sqrt n}{k}\sum_{i\in I}d_i
\ge\frac{a}{m_0}-c.
\tag{9}
$$

The second inequality uses \(\sum_I H_i=m_0c\). For \(R=R_-\) the Jacobi height is \(h_R=k\). The convolution \(R*\mathbf1_I\) is identically one, by complementary support and the two means. Since \(R_0=1\) and \(R\ge0\), it follows that \(R=0\) on \(I\setminus\{0\}\). Define

$$
G_I=R*(d\mathbf1_I).
\tag{10}
$$

This equals \(d\) on \(I\), has mark zero, and its normalized mean is the first lower bound in (9). **If \(G_I\ge d\) off \(I\), it attains \(\Gamma(d)\).** If also \(H_i\le0\) on \(I\setminus\{0\}\), the two inequalities in (9) are equalities, \(G_I\) attains the signed optimum, and \(H+G_I\) attains the endpoint in (2). The comparison checks both hypotheses directly at the tested square orders.

For each fixed \(0<s<1\), the [fixed-width theorem](parallel-fixed-width-13.md) gives \(x_0,y_0\to1\). From the exact reciprocal pair,

$$
a=y_0-s(P_\sigma x)_0
=\frac{y_0-sx_0}{1-s^2}+\frac{s c}{(1+s)\sqrt n}
\ \longrightarrow\ \frac1{1+s}.
$$

Combining this with (4) gives the **exact asymptotic signed excess** on squares,

$$
\Gamma(C)-(1-c)\longrightarrow\frac{\sqrt2}{1+s}-1 .
\tag{11}
$$

It is strictly positive for \(s<\sqrt2-1\). The same expression is a lower bound on the liminf for positive repair. The signed threshold is sharp by (4), since an optimal mark-preserving signed repair exists at every finite field order. Along slow moving paths \(s_q\to0\) with \(s_q\log_2^*q\to\infty\), [the marked bound](parallel-complexity-14.md) gives the same excess with limit \(\sqrt2-1\). The finite comparisons at \(s=q^{-1/4}\) use directly computed reference spectra.

## 4. What fixed-depth norm control transfers to the repair

The normalized \(\ell_2\) control of the scaled iterates in the [fixed-width proof](parallel-fixed-width-13.md#3-direct-passage-through-absolute-value-with-the-marked-input-separated) is ordinary \(\ell_2\) control in the normalization here. The [uniform fixed-depth result](uniform-fixed-depth.md) also bounds each fixed iterate in scaled sup norm. Transferring a fixed-depth bulk tail to the stationary \(H\) still requires sparse-scale control. In fact an \(o(1)\) ordinary \(\ell_2\) error in \(U_{-\sigma}\) can give an order-one error in \(T_{h_R}\) even when its mean and mark vanish, **also over primes**.

Let \(L\) project orthogonally onto \(V_{-\sigma}\cap e_0^\perp\) and \(m=n-1\). Choose a uniformly random \(k'\)-subset \(S\) of the bulk, where \(k'=\lfloor h_R\rfloor\). Since \(L\mathbf1=Le_0=0\), summing the diagonal and off-diagonal expectations gives

$$
\mathbb E\|L\mathbf1_S\|_2^2
=\frac{k'(m-k')}{m(m-1)}\operatorname{rank}(L)
=(1/2+o(1))k'.
$$

For a maximizing \(S\), \(E=-L\mathbf1_S/k'\) has zero mean and mark and \(\|E\|_2\le1/\sqrt{k'}\). Its bulk satisfies \(T_{k'}((-E)_+)\ge-\sum_{i\in S}E_i=(\|L\mathbf1_S\|_2^2/k')\ge1/2-o(1)\). This attains the order of the generic \(\sqrt{k'}\|E\|_2\) bound under exact Fourier and mark constraints. Transferring a smaller tail bound to the stationary row requires additional control on the actual orbit error.

## 5. Reproducible comparison

The [replay](parallel-defect-16.py) fits at \(b=a-c\) and at an intermediate proposed mean for the positive repair. It compares both fits with the raw cap, a single-projection cap, and the independent dense LP where available. The signed trial fits at \(b=a-c\). Every candidate is completed by (5). The endpoint on the larger ordinary-theta side is the smaller of the two \(m_0\)'s, so both signs are retained in the [32 numerical rows](parallel-defect-16.csv).

| Order, plus side, \(s=1/16\) | \(1-c\) | Raw cap | One projection | Positive repair | Signed repair | Signed lower bound on \(m_0\) |
|---|---:|---:|---:|---:|---:|---:|
| \(9413\) | 0.14857 | 0.21417 | 0.19510 | 0.11185 | 0.09409 | 0.99511 |
| \(97^2\) | 0.16099 | 0.47001 | 0.46450 | 0.46450 | 0.46450 | 0.71443 |
| \(153649\) | 0.15042 | 0.24172 | 0.22183 | 0.11439 | 0.09562 | 0.99710 |
| \(389^2\) | 0.15402 | 0.48062 | 0.47868 | 0.47868 | 0.47868 | 0.70893 |

The positive repair fits the reserve on all 16 prime rows and on the square minus rows. The square plus repair exceeds the reserve in all eight rows, with equality in (9) verified numerically by (10). For \(s=q^{-1/4}\) the largest prime pair of sign trials gives \(m_0\) lower bounds \(0.99772\) and \(0.99427\). The maximum reported Picard residual is below \(10^{-11}\).

The [32-row interval replay](parallel-defect-16-certified.jsonl) treats each supplied width as its exact binary rational. It rounds a trial Picard vector and encloses its distance to the exact stationary vector by its Arb residual divided by \(1-(1-s)/(1+s)\). The map to \(y\) and the Fourier projection into \(H\) are contractions. The repair is rounded in the allowed Fourier support and a rational constant bump covers any remaining entrywise defect including the reference error. For the square plus rows, the interval check of (10) uses \(R*\mathbf1_I=1\) to bound the error in the entire translated repair by the reference error. The interval slack is reported in unscaled coordinates. Across both widths, the interval results give at least \(0.02638\) of spare reserve on all 16 prime rows. On all eight square plus rows, they give an excess of at least \(0.07312\) over the reserve and certify the hypotheses for equality in (9). The table reports rounded diagnostics.

~~~sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  .venv/bin/python -B research/parallel-defect-16.py \
  > research/parallel-defect-16.csv
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 \
  .venv/bin/python -B research/parallel-defect-16.py --certificate \
  > research/parallel-defect-16-certified.jsonl
~~~

For primes, it suffices to prove that the positive part of \(\Gamma(d)-(1-c)\) tends to zero on both signs in the field-first small-width limit, or along a slow moving reference path with balanced marks. The projected residual estimate (6) reduces this to upper-tail control for a sequence of explicit affine projections at the available mean. That uniform prime estimate remains open.
