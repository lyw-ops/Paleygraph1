# Fixed-width seed projection: an exact distance and a mixture barrier

## Outcome and scope

There is a new obstruction to using actual reciprocal fixed-width rows as positive seeds: **their distance to the exact mark/mean/sector slice is macroscopic even after arbitrary positive mean slack**. This holds for every positive mixture of widths in a fixed compact subinterval of `(0,1)`, without identifying any bulk support. It strengthens a worst-case projection upper bound into a lower bound on the *best possible* affine projection of that positive source.

This is a barrier to this seed construction, not a proof that the resulting projected seed has macroscopic negative part or is far from a good repair. Those are different assertions. No analytic seed with the requested prime-uniform `n^(1/4)` defect or repair radius is obtained here. Signed extrapolation remains possible; below are exact feasibility and cancellation tests for it. The argument uses the established fixed-width scalar limit from [quadratic theta](quadratic-theta.md), not any new character-sum assertion.

## 1. The direct projection formula is the nearest affine row

Let `P=P_{-sigma}`, `F=P_sigma`, `ell=Pe_0`, `kappa=P_00>0`, and `M=1-ell/kappa`. Let

\[
\mathcal A_{a,\mu}=\{Y\in\operatorname{im}(J+P):Y_0=a\sqrt n,\ \overline Y=\mu\}.
\]

Take any real `Z` already having the prescribed root and mean; positivity is not needed for this assertion. Set `f=FZ`. Then

\[
\boxed{\quad \operatorname{dist}(Z,\mathcal A_{a,\mu})^2
 =\|f\|^2+\frac{f_0^2}{\kappa},\qquad
 \Pi_{\mathcal A}Z=Z-f+\frac{f_0}{\kappa}\ell.\quad} \tag{1}
\]

Indeed every correction has forbidden component `-f` and mean zero. Its allowed component `v` must have `v_0=f_0`. Since `v_0=<ell,v>`, its minimum norm is attained uniquely at `v=f_0 ell/kappa`. Orthogonality of the two sectors proves (1). This also proves that the projection construction in [one-sided-quadratic-22, (3)](one-sided-quadratic-22.md) is optimal in Euclidean distance to its particular positive source.

More specifically let `b>=0`, `b_0=1`, and `c_b=sum b/sqrt n`. If `a c_b<=mu`, the source

\[
Z=a\sqrt n\,b+(\mu-a c_b)M\ge0
\]

has the correct mean and root. Hence its nearest affine row satisfies

\[
\|Y_-\|\le \operatorname{dist}(Z,\mathcal A),\qquad
\frac{\operatorname{dist}(Z,\mathcal A)^2}{a^2 n}
 =\|Fb\|^2+\frac{((Fb)_0)^2}{\kappa}. \tag{2}
\]

The right side does **not** depend on the padding or on the size of the mean slack. Moreover `|(Fb)_0|<=sqrt(kappa_sigma)||Fb||`, where `kappa_sigma=F_00`. Thus

\[
\boxed{\quad \operatorname{dist}(Z,\mathcal A)
 \ge a\sqrt n\, |(Fb)_0|
 \sqrt{\kappa_\sigma^{-1}+\kappa^{-1}}.\quad} \tag{3}
\]

For Paley ranks the last square root tends to `2`. This lower bound concerns projection cost; it cannot be reversed into a negative-part lower bound.

## 2. The forbidden marked coordinate of an actual reciprocal row

Use the normalized reciprocal pair at width `0<r<1`:

\[
x_r=c_rj+u_r+rv_r,\qquad y_r=c_rj+ru_r+v_r,
\]

with `u_r in im F`, `v_r in im P`, `j=1/sqrt n`, and

\[
x_{r,0}y_{r,0}=1,\quad y_{r,0}^2=M_\sigma(r),\quad
c_r^2+r(\|u_r\|^2+\|v_r\|^2)=1.
\]

Normalize the **positive** target-side row by `b_r=y_r/y_{r,0}`. Eliminating `v_r` gives the exact scalar identity

\[
\boxed{\quad d_q(r):=(Fb_r)_0
 =\frac r{1-r^2}\left[
 \frac1{M_\sigma(r)}-r-
 \frac{(1-r)c_r}{\sqrt{nM_\sigma(r)}}\right].\quad} \tag{4}
\]

Indeed `Fy_r=ru_r` and
`(1-r^2)u_{r,0}=x_{r,0}-r y_{r,0}-(1-r)c_r/sqrt n`.
Because `0<=c_r<=1` and `M_sigma(r)->1` locally uniformly at positive widths,

\[
\sup_{r\in I}\left|d_q(r)-\frac r{1+r}\right|\longrightarrow0
\quad\text{for every }I=[r_-,r_+]\subset(0,1). \tag{5}
\]

This holds through primes and squares. It requires no assertion about a zero set or distribution of the bulk. Also `c_{b_r}=c_r/sqrt(M_sigma(r))<=1+o(1)` uniformly on `I`. Thus with `a=1` **every fixed positive mean slack** `mu=1+epsilon` makes these positive padded sources feasible eventually.

Combining (3) and (5), a single fixed width has

\[
\liminf_q\frac{\operatorname{dist}(Z_r,\mathcal A_{1,1+\epsilon})}{\sqrt n}
 \ge \frac{2r}{1+r}>0. \tag{6}
\]

In particular, adding mean slack does not turn this direct projection cost into `O(n^(1/4))`.

## 3. Arbitrarily many positive widths do not cancel the obstruction

Allow the number of widths and their weights to depend on the field, and put

\[
b=\sum_{j=1}^{k_q}\alpha_jb_{r_j},\qquad
\alpha_j\ge0,\quad\sum_j\alpha_j=1,\quad r_j\in I.
\]

This is nonnegative and anchored. Uniformity in (5) proves

\[
(Fb)_0=\sum_j\alpha_j\frac{r_j}{1+r_j}+o(1)
 \ge \frac{r_-}{1+r_-}+o(1). \tag{7}
\]

Its padded source is feasible for every `mu=1+epsilon` eventually, and its **minimum** projection cost is at least
`(2r_-/(1+r_-)+o(1))sqrt n`. This rules out positive multi-width averaging and any continuation procedure whose final positive source remains such a mixture. It does not rule out nonlinear continuation with new supports or widths tending to zero.

There is a useful conditional quantitative version for moving widths. Suppose all used widths satisfy `0<r_j<=r_+<1` and

\[
\sup_j|M_\sigma(r_j)-1|=o(1).
\]

Equation (4), now divided by `r_j`, proves uniformly
`d_q(r_j)=(r_j/(1+r_j))(1+o(1))`, including arbitrarily small positive `r_j`. Consequently an `O(n^(1/4))` projection cost requires

\[
\boxed{\quad \sum_j\alpha_j\frac{r_j}{1+r_j}=O(n^{-1/4}).\quad} \tag{8}
\]

In particular the total weight at widths at least any fixed `s>0` must be `O(n^(-1/4))`. For a single row, `r=O(n^(-1/4))` is necessary by this marked-coordinate test. This is weaker than the usual sufficient energy scale `r=O(n^(-1/2))`; the gap is real information still missing from the bulk norm. The scalar hypothesis at moving widths is explicit and is **not** supplied by the fixed-width theorem.

## 4. Signed extrapolation: cancellation, conditioning, and positivity

Now permit real coefficients `alpha_j` with sum one, still at widths in `I`, and write `N=sum_j(-alpha_j)_+`. Its total variation is `1+2N`. For bounded total variation, (5) implies

\[
(Fb)_0=\sum_j\alpha_j h(r_j)+o(1),\qquad h(r)=r/(1+r).
\]

An `O(n^(1/4))` projection cost requires this marked coordinate to be `O(n^(-1/4))`. If `r_-<r_+`, it follows that

\[
\boxed{\quad \liminf_q N\ge
 \frac{h(r_-)}{h(r_+)-h(r_-)}
 =\frac{r_-(1+r_+)}{r_+-r_-}.\quad} \tag{9}
\]

Proof: the positive coefficients have mass `1+N` and the negative ones have mass `N`; therefore the limiting marked sum is bounded below by `(1+N)h(r_-)-Nh(r_+)`. The bound is sharp for cancellation of this **one scalar**, using the two endpoint widths. Closely spaced widths require large negative coefficients. If total variation grows, the fixed-width asymptotic error is multiplied by that variation and no unqualified limiting cancellation argument is valid.

There is an exact finite-field version with no asymptotics: if all `d_q(r_j)` lie in `[d_min,d_max]` with `d_min>0`, then

\[
|(Fb)_0|\le\delta\quad\Longrightarrow\quad
 N\ge\frac{(d_{\min}-\delta)_+}{d_{\max}-d_{\min}} \tag{10}
\]

when the denominator is positive; if it is zero and `delta<d_min`, cancellation is impossible. This can be certified directly from reciprocal scalar and mass enclosures in (4).

Cancellation at the root does not imply cancellation in the sector. For an actual list of rows define

\[
G_{ij}=\langle Fb_{r_i},Fb_{r_j}\rangle+
 \frac{d_q(r_i)d_q(r_j)}\kappa.
\]

The **exact** projection cost is `a sqrt(n alpha^T G alpha)`. An extrapolated candidate succeeds as a direct positive-source construction only after checking all three conditions

\[
b=\sum_j\alpha_j b_{r_j}\ge0,\qquad
 a\sum_j\alpha_j c_{b_{r_j}}\le\mu,\qquad
 \alpha^T G\alpha=O(n^{-1/2}). \tag{11}
\]

These are convenient sufficient checks by (1)-(2), with the specified cost bound. They are not necessary for positivity of the *padded* source: mean slack can rescue some negative entries of `b`. The exact positivity test, allowing that rescue and even allowing negative padding, is

\[
\boxed{\quad \mu\ge a c_b+
 \max_{i\ne0}\frac{-a\sqrt n\,b_i}{M_i}.\quad} \tag{11a}
\]

Here all off-mark `M_i` are positive, as in the pinned geometry. Together with `alpha^T G alpha=O(n^(-1/2))`, (11a) is necessary and sufficient for this padded-source construction to have positivity and the desired projection cost. The maximum is not replaced by its positive part: a strictly positive bulk may permit negative padding. Checking only scalar root cancellation omits both the bulk Gram matrix and (11a).

## 5. Exact square control and the remaining distinction

At square plus the subfield witness `1_I`, with `h=(sqrt q+1)/2`, gives for **every** affine seed at mark `sqrt n` and mean `mu`

\[
\|Y_-\|\ge\frac{(\sqrt n-\mu h)_+}{\sqrt{h-1}},\qquad
\liminf\frac{\|Y_-\|}{n^{1/4}}
 \ge 2^{1/4}(1-\mu/\sqrt2)_+. \tag{12}
\]

This follows by summing `Y` on `I` and Cauchy--Schwarz, independently of how the seed was made. With `mu=1+epsilon<sqrt2`, vanishing normalized defect is impossible on squares; bounded normalized defect is entirely compatible with this lower bound.

Thus the square obstruction does not disprove an `O(n^(1/4))` seed theorem. Conversely, an `O(n^(1/4))` negative-part bound alone does not place the seed within `O(n^(1/4))` of an unrestricted defect minimizer or of a nonnegative feasible row. Formula (1) is a distance **from a positive source to the affine slice**, not distance within that slice to the positive cone. A further repair theorem must retain the nonstationarity cost from [astra-dynamics-24](astra-dynamics-24.md).

The new rigorous conclusion is therefore specific: positive mixtures of actual fixed-width reciprocal rows cannot supply the desired small-cost projection seed, even with arbitrary fixed positive mean slack. To escape, one needs a shrinking-width scalar/bulk estimate, a signed mixture satisfying the full Gram and positivity tests (11), or a different nonlinear seed construction. None is established here for all primes.

## Verification

`astra-seed-25-check.py` checks (1), (4), the Gram formula, and the finite signed-cancellation bound on actual prime and square Fourier sectors. It also computes signed two-width cancellation and records whether positivity survives. These are floating-point finite-order algebra checks, not interval certificates or asymptotic evidence. Only files with prefix `research/astra-seed-25` are written; no shared edits, commits, or pushes.


The replay passed 12 field/sign cases (primes 29, 61, 97 and squares 25, 49, 121), with three widths per case. The largest reciprocal scalar-identity discrepancy was below `1.84e-9`; the independent affine least-squares comparisons were below `1e-10`. Two-width signed cancellation at widths `.2,.7` removed the forbidden marked coordinate in every case, but left nonzero forbidden norm in every case, and produced negative entries in six cases. These observations are diagnostics only; negative entries before padding do not alone violate (11a).

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-seed-25-check.py > research/astra-seed-25-check.json
```
