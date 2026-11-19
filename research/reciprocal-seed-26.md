# Signed reciprocal mixtures with a certified finite-family cost

The [fixed-width positive-mixture obstruction](astra-seed-25.md) permits signed extrapolation. This experiment minimizes the **whole** forbidden-sector projection cost, retains positivity of the padded source at every coordinate, and controls the total variation of the signed coefficients. At the tested localized prime fields, signed mixtures improve substantially on positive ones. The fixed-width cost divided by $\sqrt n$ remains around $0.056$ through order one million. Shrinking the widths improves the cost further. These finite trials do not settle its asymptotic scale.

Six additional Arb certificates give upper and lower bounds for the optimum in the saved rationalized six-row families. They do not certify that the saved rows are the exact reciprocal minimizers. A separate [full-Paley example](parallel-extrapolation-26.md) shows that a general impossibility theorem for signed mixtures would be false: two actual reciprocal rows at fixed positive widths can cancel the entire forbidden sector in that different model.

## The finite convex program

Use $n=(q-1)/2$, $F=P_\sigma$, $P=P_{-\sigma}$, $\ell=Pe_0$, $\kappa=\ell_0$, and $M=\mathbf1-\ell/\kappa$. Take nonnegative real rows $b_j$ with $(b_j)_0=1$, and write $c_j=\sum_i(b_j)_i/\sqrt n$. Define

$$
f_j=Fb_j,\qquad d_j=(f_j)_0,\qquad
G_{ij}=\langle f_i,f_j\rangle+d_i d_j/\kappa,
\qquad C_{ij}=\sqrt n(b_j)_i-M_i c_j.
$$

For real coefficients $\alpha$ with $\sum_j\alpha_j=1$, the source

$$Z=\mu M+C\alpha$$

has mark $\sqrt n$ and mean $\mu$. Its positivity is the linear constraint $C\alpha+\mu M\ge0$ off the mark. The nearest exact-sector row is

$$Y=Z-FZ+(FZ)_0\ell/\kappa.$$

By the exact projection identity,

$$
\frac{\operatorname{dist}(Z,\mathcal A_{1,\mu})^2}{n}
=\alpha^{\mathsf T}G\alpha.
\tag{1}
$$

The program minimizes (1) under the source positivity, coefficient sum, and $\|\alpha\|_1\le T$ constraints. Positivity is checked over all coordinates after each small constraint-generation solve. Cancelling only $\sum\alpha_jd_j$ would miss the rest of the Gram cost. Negative entries in the unpadded combination $\sum\alpha_jb_j$ are permitted when the source $Z$ is nonnegative.

## A dual lower bound that does not depend on optimizer status

The matrix $G$ is positive semidefinite. For any real test vector $v$, any selected off-mark constraints, nonnegative multipliers $\lambda$, and a real $\eta$, set

$$r=2Gv-\eta\mathbf1-C_{\rm selected}^{\mathsf T}\lambda.$$

The supporting-plane inequality and the three constraints give

$$
\boxed{\quad
\alpha^{\mathsf T}G\alpha\ge
\eta-\mu\lambda^{\mathsf T}M_{\rm selected}
-T\|r\|_\infty-v^{\mathsf T}Gv.
\quad}
\tag{2}
$$

Indeed $\alpha^TG\alpha\ge2(Gv)^T\alpha-v^TGv$, while $\lambda^TC\alpha\ge-\mu\lambda^TM$. The remaining term is bounded below by $-\|\alpha\|_1\|r\|_\infty$. There is no requirement that the multipliers or $v$ be optimal. Using only a subset of the positivity constraints preserves the lower bound.

The certificate saves nonnegative integer numerators for each $b_j$, all with denominator $10^{10}$ and root numerator $10^{10}$. It also saves integer numerators for $v,\lambda,\eta$ and the selected indices. The replay validates these premises and uses Arb at 128 bits. With $\widehat b$ the unnormalized DFT, it computes

$$
\langle Fb_i,Fb_j\rangle=\frac1n\sum_{s_k=\sigma}
\widehat b_i(k)\overline{\widehat b_j(k)},\qquad
(Fb_j)_0=\frac1n\sum_{s_k=\sigma}\widehat b_j(k).
$$

It encloses $G,C$, the right side of (2), and the upper trial cost. The upper trial coefficients are moved slightly toward a positive single-width source before rounding; every source coordinate is then checked by interval arithmetic. All six recorded upper trials are feasible at the same requested mean $101/100$ and total-variation cap $10$. The standalone replay invokes no floating-point optimization.

The [first four certificates](reciprocal-seed-26-certified.jsonl) and [two larger-field certificates](reciprocal-seed-26-larger-certified.jsonl) enclose the minimum projection cost divided by $n^{1/4}$ as follows. The decimals below are widened outwards from the interval endpoints.

| Order | Forbidden sign | Lower | Upper |
|---|---:|---:|---:|
| $97^2$ | $+$ | 0.5819823 | 0.5819854 |
| $97^2$ | $-$ | 0.3970860 | 0.3970968 |
| $9413$ | $+$ | 0.4612466 | 0.4612798 |
| $9413$ | $-$ | 0.4635373 | 0.4635433 |
| $153649$ | $+$ | 0.9353915 | 0.9353948 |
| $153649$ | $-$ | 0.9418595 | 0.9418642 |

These are finite-family bounds for the exact saved rational rows. The residuals for the original reciprocal solves are floating point; no interval closeness theorem transfers these lower bounds to the exact reciprocal optimizers. Projection cost bounds distance from a positive source to the affine slice. A lower bound on it is not a lower bound on the projected row's negative part or on the unrestricted repair optimum.

## Fixed versus shrinking widths

The [fixed-width sweep](reciprocal-seed-26-fixed.jsonl) uses the menu $\{.08,.12,.2,.32,.5,.7\}$ and tests 2, 4, or 6 selected widths with $T=1,3,10$. The [shrinking-width sweep](reciprocal-seed-26-shrinking.jsonl) uses $n^{-1/4}\{.5,.8,1.3,2,3,4\}$. Both have mean $1.01$, primes $9413,153649,1000033$, square orders $97^2,389^2,997^2$, and both signs. Each sweep records 108 floating-point feasible trials.

For the six-width menu and $T=10$, the projection costs divided by $n^{1/4}$ are:

| Prime | Fixed widths, $+$ | Fixed widths, $-$ | Shrinking widths, $+$ | Shrinking widths, $-$ |
|---|---:|---:|---:|---:|
| $9413$ | 0.4613 | 0.4635 | 0.3734 | 0.3688 |
| $153649$ | 0.9354 | 0.9419 | 0.6380 | 0.6518 |
| $1000033$ | 1.5142 | 1.5063 | 0.8081 | 0.8013 |

At the million-order prime, positive mixtures give fixed-width costs about $4.1650$ and $4.1538$ in this normalization. Signed mixtures improve these to $1.5142$ and $1.5063$. The shrinking menu further reduces them to $0.8081$ and $0.8013$. Its projected negative-part norms divided by $n^{1/4}$ are about $0.1299$ and $0.1198$, below its projection-cost bounds. These are candidate values, not certified global optima at that field.

The observed increase with field size does not disprove a bounded asymptotic cost for the shrinking menu. It provides no evidence of a vanishing cost either. A prime-uniform shrinking-width Gram and positivity estimate remains necessary. The [anchored-finish lemma](parallel-extrapolation-26.md#a-quantitative-source-cost-to-finish-statement) also shows why an $O(n^{1/4})$ source projection cost gives only bounded added mean under the simple translated repair. A vanishing added mean requires a smaller cost or more cancellation in that finish.

## Reproduction

```sh
export VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1
.venv/bin/python -B research/reciprocal-seed-26.py 9413 153649 1000033 \
  --square-roots 97 389 997 --variation 1 3 10 --sizes 2 4 6
.venv/bin/python -B research/reciprocal-seed-26.py 9413 153649 1000033 \
  --square-roots 97 389 997 --width-scale n14 --widths .5 .8 1.3 2 3 4 \
  --variation 1 3 10 --sizes 2 4 6
.venv/bin/python -B research/reciprocal-seed-26.py 9413 --square-roots 97 \
  --sizes 6 --variation 10 --certify
.venv/bin/python -B research/reciprocal-seed-26.py 153649 \
  --sizes 6 --variation 10 --certify
.venv/bin/python -B research/reciprocal-seed-26.py \
  --replay-input research/reciprocal-seed-26-q9413-side1-k6-tv10-input.json
```

The [optimizer-free replay results](reciprocal-seed-26-replayed.jsonl) reproduce the saved certificate outputs exactly. An independent mathematical audit checked (2), the Fourier normalizations, and the saved-input premises. These results leave ordinary theta convergence in Problem 26 open.
