# Simultaneous endpoint tests from projected reference rows

The [ordered-defect bound](parallel-transport-15.md#a-direct-certificate-from-the-ordered-bulk-defect) uses a single projected reference row to lower-bound the ordinary theta endpoint. Several rows at different widths can be tested against the same possible rooted spectrum. The resulting minimax problem also accepts selected Fourier constraints on that spectrum. A positive margin gives an interval-certifiable endpoint bound from one combined Fourier row.

## Test a prescribed endpoint root

Let $m_0=\sqrt{M_\sigma(0)}=\sqrt n/\theta_\sigma$ and let $N=P_{-\sigma}$. An anchored endpoint minimizer $b^*$ satisfies $Nb^*=0$, $0\le b^*\le1$, and $j^Tb^*=m_0$, where $j=\mathbf1/\sqrt n$. The cap follows by translating a largest coordinate to the mark and renormalizing. For a proposed root $t\ge1/\sqrt n$ define the compact box with a mass constraint

$$
\mathcal B_t=\{b:b_0=1,\ 0\le b_i\le1,\ \textstyle\sum_{i\ne0}b_i\le t\sqrt n-1\}.
$$

For $H\in \mathbb Rj+\operatorname{ran}N$ with $c_H=j^TH\ge0$, put

$$\Delta_t(H)=\min_{b\in\mathcal B_t}\big(\langle H,b\rangle-tc_H\big).\tag{1}$$

If $m_0\le t$, the actual endpoint spectrum belongs to $\mathcal B_t$ and has $\langle H,b^*\rangle=c_H m_0$. This proves $\Delta_t(H)\le0$. Thus any $\Delta_t(H)>0$ certifies $m_0>t$. For any threshold $\tau\ge0$, the fractional box constraint gives

$$
\Delta_t(H)\ge H_0-tc_H-\tau(t\sqrt n-1)-\sum_{i\ne0}(-H_i-\tau)_+ .\tag{2}
$$

The best threshold gives equality by sorting the negative bulk entries. To verify a computed row, round it to an exact rational array and reproject it with Arb onto $\mathbb Rj+\operatorname{ran}N$. Evaluate (2) outward at any chosen nonnegative binary-rational threshold. Interval evaluation uses the resulting exact Fourier support and a positive lower bound on $c_H$ whenever required. It does not use numerical signs of the endpoint LP.

## A common test spectrum for several references

Use reference rows $H_j=(J+N)A_{-\sigma}(s_j)$, or project any nonnegative reference trials to obtain such rows. Put $f_j(b)=\langle H_j,b\rangle-tc_{H_j}$. Choose signed correction directions $G_i\in\operatorname{ran}N$, and allow coefficients $|\eta_i|\le D$ with $D>0$. Bilinear minimax on compact convex sets gives

$$
\max_{\lambda\in\Delta,\ |\eta_i|\le D}
\Delta_t\left(\sum_j\lambda_j H_j+\sum_i\eta_iG_i\right)
=\min_{b\in\mathcal B_t}\left[\max_j f_j(b)+D\sum_i|\langle G_i,b\rangle|\right].\tag{3}
$$

Here $\Delta$ is the simplex of reference weights. The right side is a linear program with one variable bounding the maximum and one per absolute value. Its row multipliers give the coefficients of the combined row. With $L$ reference rows and $K$ correction directions, there is an optimal bulk vector with at most $L+K+1$ fractional coordinates. Indeed, fix the epigraph variables at an optimal vertex. A perturbation on the fractional coordinates that preserves the mass, reference and correction linear forms would preserve every inequality in both directions. There are at most $L+K+1$ such linear forms. This gives a common, almost integral bulk test for the whole menu of reference widths.

Two choices of new directions start from an optimal test $b$ in (3). A coordinate direction is $N(e_k+e_{-k})/2$ where the untested coordinate of $Nb$ is largest in magnitude. A residual direction takes the projection of $Nb$ orthogonal to the span of the directions already used, then normalizes it. The latter is the unit vector most violated among unused orthogonal directions. Both constructions are valid because the true endpoint has zero inner product with every vector in $\operatorname{ran}N$. Each finite certificate can be checked by (2) after combining the reference rows and corrections. In particular an inaccurate LP result cannot give an incorrect positive interval margin.

Allowing arbitrary $G\in\operatorname{ran}N$ with $\|G\|\le D$ instead of a finite list replaces the last term on the right of (3) by $D\|Nb\|$. This identifies a uniform target for this approach. The common test spectra that withstand all the projected references would have to retain a forbidden projection large enough to give a positive minimum. Bounding that quantity from below through primes requires more than detecting violations on a finite sample.

## A necessary condition on narrower-width trials

Let $x_r=A_\sigma(r)$ be the normalized optimizer at a narrower width, with $a_r=x_{r,0}$ and $m_r=j^Tx_r/a_r$. If $m_r\le t$, then $b=x_r/a_r$ belongs to $\mathcal B_t$. Also $\|Nb\|\le\sqrt r/a_r$ by the quadratic energy normalization. For exact references at $s_j\ge r$, $\|NH_j\|\le1/\sqrt{s_j}$. Testing every mixture with $b$ proves

$$
\sup_{\lambda\in\Delta,\ G\in\operatorname{ran}N,\ \|G\|\le D}
\Delta_t\left(\sum_j\lambda_j H_j+G\right)
\le \max_j\left[(m_r-t)c_{H_j}+\frac{\sqrt r}{a_r\sqrt{s_j}}\right]
+D\frac{\sqrt r}{a_r}.\tag{4}
$$

Thus even unrestricted correction directions of bounded total norm fail if a narrower reference has $m_r\le t-\epsilon$, $r/\min_j s_j\to0$, and the reference masses are bounded below. The [two-row bound](astra-cuts-15.md#a-common-mass-floor-from-the-two-signed-jacobi-rows) supplies this last hypothesis when the reference widths lie in $(0,1-\delta]$ for fixed $\delta>0$ and the field order grows. The current experiment limits each direction coefficient separately. For $K$ orthonormal directions with coefficient bound $D$, the total norm in (4) is at most $D\sqrt K$. This shows precisely how a low anchored mass at a smaller width could obstruct every bounded-dimensional direction test at wider references.

For the plus sign of a square field, the subfield spectrum $b^*=\mathbf1_I$ has $m_0=(\sqrt q+1)/(2\sqrt n)\to1/\sqrt2$. It certifies $\Delta_t(H)\le(m_0-t)c_H<0$ for $t>m_0$ and $c_H>0$ for every row in (3), including all the selected correction directions.

## Interval replay

The default menu combines $0.5,0.3,0.2,0.1$ with $q^{-1/6},q^{-1/4},q^{-1/3}$. The [replay](../endpoint_mixture.py) tests the exact binary rational passed as `0.97` and uses $D=1$. The comparisons concern the information contained in the reference rows and selected constraints. Existing full endpoint LPs give tighter values on individual primes.

The [default-menu data](../data/endpoint-mixture.csv) contain 205 Arb lower bounds on the margin. Six primes and four squares were tested on both signs. At most 36 coordinate directions yielded four positive margins, and at most 36 residual directions yielded nine. Optimizing reference weights alone improved the best individual margin in four of the twenty cases. With 80 residual directions all eight extended prime rows were positive, with the smaller margin at $p=9413$ exceeding $0.00593$. The square plus margins stayed negative as required by the subfield spectrum.

The [54 fixed-menu bounds](../data/endpoint-mixture-fixed.csv) keep only reference widths $0.5,0.3,0.2,0.1$. They give both signs at $p=401$ lower endpoints above the prescribed value with 36 residual directions, and at $p=1997$ with 80 directions. At $p=9413$ the two margins remain below $-0.01299$ even with 80 directions. Adding the three smaller widths in the default menu makes the two margins positive at the same budget. The sample leaves open whether any bounded number of slow-width references and residual directions can suffice through primes.

| Order and sign | 36 coordinate directions | 36 residual directions | 80 residual directions |
|---|---:|---:|---:|
| $401,-$ | $-0.00016$ | $0.00243$ | |
| $4001,+$ | $-0.06223$ | $-0.00406$ | $0.00750$ |
| $9413,+$ | $-0.05073$ | $-0.00163$ | $0.00593$ |
| $9413,-$ | $-0.05180$ | $-0.00002$ | $0.00664$ |
| $97^2,+$ | $-0.23154$ | $-0.20367$ | |

Tabulated margins are rounded downward. The `next_projection_residual` column uses the maximum untested coordinate for the coordinate method and the norm perpendicular to the previous directions for the residual method.

~~~sh
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python endpoint_mixture.py 61 401 1009 1997 4001 9413 --square-characteristics 19 43 61 97 --certify-max-order 9413 --budget 36
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python endpoint_mixture.py 61 401 1009 1997 4001 9413 --square-characteristics 19 43 61 97 --certify-max-order 9413 --budget 36 --gauge residual
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python endpoint_mixture.py 1009 1997 4001 9413 --certify-max-order 9413 --budget 80 --gauge residual
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python endpoint_mixture.py 401 1997 9413 --square-characteristics 43 97 --certify-max-order 9413 --budget 36 --gauge residual --widths .5 .3 .2 .1
VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python endpoint_mixture.py 1997 9413 --certify-max-order 9413 --budget 80 --gauge residual --widths .5 .3 .2 .1
~~~
