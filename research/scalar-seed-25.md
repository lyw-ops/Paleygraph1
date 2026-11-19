# A scalar Jacobi correction leaves a macroscopic defect

The [fixed-mark defect criterion](pinned-penalty-24.md) requires a repair in a prescribed Fourier sector. A single correction formed by applying a fixed continuous scalar function to the Jacobi eigenvalues and projecting it into that sector cannot remove the macroscopic negative part when $0<\mu<\sqrt2a$. This includes any fixed polynomial degree, finitely many hinge functions, and finite combinations of fixed absolute-value functions. It leaves open corrections depending jointly on several arithmetic fields or on a growing number of projected residuals.

Let $q\equiv1\pmod4$, $n=(q-1)/2$, $X_q=\widehat s/\sqrt q$, $P=P_{-\sigma}$, $\ell=Pe_0$, $\kappa=P_{00}$, and $L=P-\ell\ell^{\mathsf T}/\kappa$. For fixed $a,\mu>0$, start from $Y_q^0=\mu+(a\sqrt n-\mu)\ell/\kappa$. For a fixed continuous real function $g$ on $[-1,1]$ put

$$
Y_q(g)=Y_q^0+L g(X_q).
$$

This row has mean $\mu$, root $a\sqrt n$ and the required sector exactly. The two affine scalar functions have no effect on the correction, since $L\mathbf1=LX_q=0$.

## The limiting projected scalar field

Write the Chebyshev expansion with the arcsine probability measure $\omega$ as

$$
g(x)=c_0+c_1x+\sum_{m\ge2}c_mT_m(x),\qquad
\widetilde g=g-c_0-c_1x.
$$

The series converges in $L^2(\omega)$ and $\sum c_m^2<\infty$. By the [joint Mellin group calculation](parallel-graph-shapes-23.md#a-fixed-number-of-path-columns-gives-no-leading-gain), for every fixed finite list the all-mode variables $(X_q,(KT_m(X_q))_{m\ge2})$ converge jointly to

$$
X\sim\omega,\qquad Y_m=\tfrac12(\operatorname{tr}U_m+\operatorname{tr}V_m),
$$

where all compact symplectic matrices $U_m,V_m$ are independent, of size $d_m=2\lfloor m/2\rfloor$, and independent of $X$. Each $Y_m$ is centered, symmetric, of variance $1/2$, and has full support $[-d_m,d_m]$. This is the same proof before the square pushforward used for the opposite-point feature. The consistent finite product measures define the entire sequence.

For each fixed $m\ge2$, $(PT_m(X_q))_0=O_m(1)$ and $\overline{T_m(X_q)}=o(1)$. The first estimate follows from the bounded Mellin trace for $KT_m$ at the root. Since $\ell_i=O(n^{-1/2})$ off the mark, the off-mark field $LT_m(X_q)$ differs uniformly by $o(1)$ from $(T_m(X_q)-\sigma KT_m(X_q))/2$. The canonical bulk tends to $\mu-a\sqrt2\sigma X$. Therefore

$$
\boxed{\quad
\lim_q\frac{\|(Y_q(g))_-\|_2}{\sqrt n}
=\left\|\left(\mu-a\sqrt2\sigma X+
\tfrac12[\widetilde g(X)-\sigma S_g]\right)_-\right\|_{L^2},
\qquad S_g=\sum_{m\ge2}c_mY_m.
\quad}
\tag{1}
$$

The sum defining $S_g$ converges in $L^2$. To justify (1), first take a finite polynomial. The finite joint limit and uniform off-mark bounds give convergence of the squared negative part. For general continuous $g$, polynomial approximations and the contraction of $L$ give

$$
\|L(g-g_N)(X_q)\|_2/\sqrt n
\le\|(g-g_N)(X_q)\|_2/\sqrt n
\longrightarrow\|g-g_N\|_{L^2(\omega)}.
$$

Fixed-degree empirical convergence applies because $(g-g_N)^2$ is continuous. The negative part is 1-Lipschitz, so taking $N\to\infty$ proves (1). The positive root is omitted when asserting a bulk second-moment limit. It never contributes to the negative part. This argument does not permit evaluating an arbitrary representative of an $L^2(\omega)$ function on the discrete eigenvalues.

The same reasoning gives the correction's limiting squared norm:

$$
\lim_q\|L g(X_q)\|_2^2/n=\tfrac14\sum_{m\ge2}c_m^2.
\tag{2}
$$

Indeed the deterministic Chebyshev part and independent noise each have variance $\sum c_m^2/2$ before division by four.

## Positive residual for every fixed continuous scalar function

Assume $\mu<a\sqrt2$. If $\sum d_m|c_m|$ diverges, $S_g$ has unbounded support in both directions. For any $B>0$, choose $N$ with $\sum_{m\le N}d_m|c_m|>B+1$ and tail variance $\frac12\sum_{m>N}c_m^2<1/2$. The finite block has positive probability of exceeding $B+1$, and its independent tail lies in $[-1,1]$ with probability at least one half. Symmetry gives the other tail. Since $g$ is bounded and $X$ is independent of this noise, the limiting row in (1) is strictly negative on an event of positive probability.

If $\sum d_m|c_m|<\infty$, the scalar Chebyshev series converges uniformly. The support of $S_g$ has both endpoints $\pm\sum d_m|c_m|$, by choosing finite blocks near their endpoints and using an independent tail of small variance. At $X=\sigma$, and with $\sigma S_g$ near its positive endpoint, the limiting row is at most

$$
\mu-a\sqrt2-\tfrac12\sum_{m\ge2}(d_m-1)|c_m|<0.
$$

Continuity in $X$ and the product support make this a positive-probability event. If all $c_m=0$, the canonical row itself has negative part of positive measure. Thus the limit in (1) is strictly positive for every fixed continuous $g$.

The conclusion also holds uniformly when arbitrary field-dependent coefficients are allowed in a fixed finite family $g_1,\dots,g_k$, independent modulo affine functions. Namely,

$$
\boxed{\quad
\liminf_q\inf_{b\in\mathbb R^k}
\frac{\|(Y_q^0+L\sum_j b_jg_j(X_q))_-\|_2}{\sqrt n}>0.
\quad}
\tag{3}
$$

If a contradicting coefficient sequence were bounded, a convergent subsequence and (1) would contradict the preceding positive residual. If its norm diverged, divide by that norm and pass to a coefficient direction on the unit sphere. Uniform $L^2$ bounds for the fixed family make changes in the coefficients harmless. The canonical bulk disappears under this rescaling. Formula (2) gives a nonzero limiting correction of mean zero. Such a variable has a nonzero negative part, contradicting the vanishing rescaled residual. This proves boundedness and (3). Exact affine dependencies can be removed before this argument.

For a polynomial family one also has an explicit coefficient coercivity argument. At $X=\sigma$, take $Y_m=\sigma d_m\operatorname{sgn}(c_m)$. The limiting row is at most $-\delta-\sum|c_m|/2$, with $\delta=a\sqrt2-\mu$. Each of the finitely many coefficient-sign corners has a neighborhood of uniformly positive limiting mass on which the error is at most $\delta/2+\sum|c_m|/4$. This gives a positive lower bound proportional to $\delta+\sum|c_m|$, without a choice of bounded coefficients.

## A common positive floor as the scalar degree increases

The compact-group limit has a stronger conclusion. There is a number $\Delta(a,\mu)>0$ such that the right side of (1) is at least $\Delta(a,\mu)$ for every scalar correction in this model when $0<\mu<a\sqrt2$. Thus even taking the scalar degree to infinity after the field limit leaves a positive macroscopic defect.

To prove the necessary coercivity on the infinite coefficient space, let $C=\|c\|_{\ell_2}$ and $h_c(X)=\sum_{m\ge2}c_mT_m(X)$. Both $h_c$ and $S_c$ have mean zero and variance $C^2/2$. A standard compact symplectic trace has second moment one and fourth moment three in dimension at least four, by the exact moment formula. In dimension two the Haar $SU(2)$ density $(2/\pi)\sin^2\theta\,d\theta$ gives second moment one and fourth moment two. Consequently $\mathbb EY_m^4\le3/4$. Independence then gives $\mathbb ES_c^4\le3C^4/4$, first for finite sums and then for their $L^4$ limits. [Stolz, Theorem 3.17](https://www.ruhr-uni-bochum.de/imperia/md/content/stochastik/veroeffentlichungen/stolzdsm.pdf)

For $C>0$, Cantelli's inequality gives $\Pr(h_c\le C/2)\ge1/3$. Applying Paley–Zygmund to $S_c^2$ and using symmetry gives $\Pr(\sigma S_c\ge3C/5)\ge49/3750$. These events are independent. Their intersection implies $(h_c-\sigma S_c)/2\le-C/20$, and hence

$$
\left\|\left(\tfrac12(h_c-\sigma S_c)\right)_-\right\|_2
\ge \frac7{1500\sqrt2}\|c\|_{\ell_2}.
$$

The objective $J(c)$ on the right of (1) therefore obeys

$$
J(c)\ge \frac7{1500\sqrt2}\|c\|_{\ell_2}-\sqrt{\mu^2+a^2}.
$$

It is a continuous convex function of $c$ because it is the norm of the negative part of a bounded affine map into the common product $L^2$ space. It is weakly lower semicontinuous and coercive, so it attains its minimum on $\ell_2$. That minimum cannot be zero. The preceding support proof works for all coefficient sequences in $\ell_2$: an unbounded noise support is independent of a scalar field finite almost surely, while finite weighted absolute sum makes the scalar field continuous and gives the same corner contradiction. Thus the minimum is $\Delta(a,\mu)>0$.

Finite sequences are dense in $\ell_2$ and $J$ is Lipschitz on that space. Each finite-degree arithmetic optimization converges to the corresponding compact-group optimization by its finite joint limit and the coefficient coercivity argument. Consequently

$$
\boxed{\quad
\lim_{M\to\infty}\lim_{q\to\infty}
\inf_{\deg g\le M}\frac{\|(Y_q^0+Lg(X_q))_-\|_2}{\sqrt n}
=\Delta(a,\mu)>0.
\quad}
\tag{4}
$$

The order of limits in this formula is part of the assertion. A degree that grows with the field requires arithmetic estimates beyond the fixed-word limits. Corrections depending jointly on new projected fields also fall outside this scalar space.

There is a growing-degree version for controlled scalar functions. For every compact set $\mathcal K\subset C([-1,1])$, the actual-field lower bound is uniform over $g\in\mathcal K$. Cover $\mathcal K$ by a finite uniform-norm net and use the contraction of $L$ and the Lipschitz negative part to transfer the finite set of limits (1). Each limiting value is at least $\Delta(a,\mu)$. Thus the actual defect is eventually at least $\Delta(a,\mu)/2$ uniformly on the compact set. In particular this holds for scalar polynomials of arbitrarily growing degree satisfying

$$
\sum_{m\ge2}m|c_{q,m}|\le C
$$

for a fixed $C$. After discarding the affine terms, the tails above degree $M$ have uniform supremum at most $C/(M+1)$, so this family is precompact in the uniform norm. Any scalar polynomial construction with vanishing bulk defect must therefore have an unbounded weighted coefficient sum along its successful sequence.

## A sharper lower bound on the canonical correction distance

The same projected scalar law sharpens the [canonical radius bound](pinned-penalty-24.md#a-barrier-to-small-corrections-from-the-simplest-exact-mark-row). Suppose arbitrary root-preserving corrections $h_q\in\operatorname{im}L$ obey $\|(Y_q^0+h_q)_-\|_2=o(\sqrt n)$. For every fixed nonnegative continuous $u$, Cauchy–Schwarz gives

$$
\liminf_q\frac{\|h_q\|_2}{\sqrt n}
\ge \frac{a\sqrt2\mathbb E[Xu(X)]-\mu\mathbb E[u(X)]}
{\sqrt{\frac12\operatorname{Var}(u)-(\mathbb E[Xu])^2}}.
\tag{5}
$$

Use a positive numerator and the reflected $u(\sigma X)$ as needed. The denominator is the norm of the projected test, by (2). The contribution of the assumed negative part tends to zero at each fixed test.

Taking the supremum in (5) is a two-moment scalar projection problem. Put $T=\mu-a\sqrt2 X$ and

$$
\mathcal Z=\{Z\ge0:\mathbb EZ=\mu,\ \mathbb EXZ=-a/\sqrt2\}.
$$

The norm of $T$ is fixed by these two moments, so minimizing $\|Z-T\|_2^2$ over this set equals minimizing $\mathbb E Z^2-\mu^2-a^2$. Hilbert-space projection duality gives the supremum in (5) as $\sqrt2\operatorname{dist}(T,\mathcal Z)$. In the range $a/\sqrt2<\mu<a\sqrt2$, its unique minimizer is $Z=\beta(t-X)_+$, where $t\in(-1,1)$ is fixed by

$$
\frac{-\mathbb E[X(t-X)_+]}{\mathbb E[(t-X)_+]}=\frac{a}{\sqrt2\mu},
\qquad \beta=\frac{\mu}{\mathbb E[(t-X)_+]}.
$$

The multiplier condition follows by completing the square and projecting onto the nonnegative cone. The ratio is strictly decreasing with $t$ and ranges from one to one half on this interval, giving the unique solution. If $a=\mu=1$, it gives $t=0.3220002851\ldots$ and the radius lower bound $0.3872561930\sqrt n$. Formula (5) with the rational threshold $t=161/500$ directly certifies this lower bound by the elementary arcsine integrals. The simpler threshold $1/3$ gives $0.3871958592\sqrt n$. These are lower bounds for arbitrary corrections achieving the stated vanishing bulk residual. Attainment in the full Fourier sector remains open.

## Replay

The [script](scalar-seed-25.py) compares the finite polynomial subfamilies of degree 2, 4, and 8 on actual Paley fields and on the compact-group limit. Its coefficient optimization minimizes the bulk squared negative part. It reports floating-point feasible trials and gradients. The finite-field run is deterministic. The compact-group run samples independent Haar compact symplectic matrices and has sampling error.

The Haar sampler successively takes a standard complex Gaussian vector in the complement of the already selected quaternionic pairs, normalizes it, and adds its symplectic partner. Unitary symplectic invariance of the Gaussian law gives the Haar law. Separate second- and fourth-moment comparisons at dimensions 2, 4 and 8 agreed with the exact trace moments within sampling variability.

The [30 finite-field records](scalar-seed-25-fields.jsonl) and [three limit samples](scalar-seed-25-limit.jsonl) give the following negative-part RMS values. Scalar finite-field records omit the positive root and divide by $\sqrt{n-1}$; this differs from the theoretical normalization by the factor $\sqrt{n/(n-1)}$. The limit samples use 160,000 independent tuples. All table entries are rounded.

| Field and sign | Degree 2 | Degree 4 | Degree 8 |
|---|---:|---:|---:|
| $1000033,+$ | 0.10477 | 0.09942 | 0.09871 |
| $1000033,-$ | 0.10420 | 0.09896 | 0.09825 |
| Compact-group sample | 0.10508 | 0.09969 | 0.09898 |

The [deeper 60,000-tuple sample](scalar-seed-25-limit-deeper.jsonl) gives degree-8 and degree-16 values about $0.09952$ and $0.09947$. Those values estimate trial performance in the limit model and do not certify the value of $\Delta$.

The [projected-descent comparison](scalar-seed-25-descent.jsonl) uses the full residual direction at every step and gives negative-part norms divided by $\sqrt n$ after 256 steps of about $0.001310$ and $0.000663$ at the million-order prime. On square plus $389^2$ the corresponding value is $0.020898$, close to the known exact square defect. The [mean-relaxed comparison](scalar-seed-25-relaxed.jsonl) at $\mu=1.003$ has degree-8 scalar residuals about $0.097$ on both signs and full projected-descent residuals about $0.000217$ and $0.0000127$. The direction in full descent depends on the earlier projected fields and can escape the scalar-function restriction. These finite computations leave its prime-uniform convergence estimate open.

The [two interval distance bounds](scalar-seed-25-distance.jsonl) evaluate the arcsine integrals in (5) at exact rational thresholds with Arb. The finite-field and fixed-seed limit outputs replayed byte-for-byte.

```sh
export VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1
.venv/bin/python -B research/scalar-seed-25.py 9413 153649 1000033 --square-roots 97 389
.venv/bin/python -B research/scalar-seed-25.py --samples 160000
.venv/bin/python -B research/scalar-seed-25.py --samples 60000 --degrees 2 4 8 16
.venv/bin/python -B research/scalar-seed-25.py --radius-bound
.venv/bin/python -B research/scalar-seed-25.py 153649 1000033 --square-roots 389 \
  --degrees 8 --repair-steps 256
.venv/bin/python -B research/scalar-seed-25.py 1000033 --degrees 8 --mean 1.003 --repair-steps 256
```
