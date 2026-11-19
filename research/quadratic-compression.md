# The mean and centered mark costs on the current quadratic support

The total allowed energy of the reciprocal quadratic optimizers splits exactly into two positive costs on either actual support. One is the minimum energy of a signed mean-one trial on that support. The other is a signed interpolation cost for the marked coordinate, with the constant component removed. The formulas apply at the measured width, without requiring any persistence of the support.

## Exact decomposition

Fix a sign $\sigma$, width $0<r<1$ and the actual unit-energy pair $x=A_\sigma(r)$, $y=Q_\sigma(r)x=A_{-\sigma}(r)$ from the [quadratic path](quadratic-theta.md). Write $a=x_0$, $c=\langle j,x\rangle=\langle j,y\rangle$, $j=\mathbf1/\sqrt n$, and $S=\{i:x_i>0\}$. Let $E_S$ extend by zero and let $C=E_S^*P_{-\sigma}E_S$. Below, $j$ and $e=e_0$ denote their restrictions to $S$. Put

$$
B=r^2 I+(1-r^2)C,\quad H=j^*B^{-1}j,\quad
\ell=r^2H,\quad \eta_* = \frac{j^*B^{-1}e}{H},\quad
T=\min_{\eta\in\mathbb R}(e-\eta j)^*B^{-1}(e-\eta j).
$$

Write $\mathcal E_\tau=\|P_\tau A_\tau(r)\|^2$ for the allowed energy of sign $\tau$ in this note. Then

$$\boxed{\displaystyle
\mathcal E_++\mathcal E_-+c^2=\frac{c^2}{\ell}+\frac{T}{a^2}.}\tag{1}$$

Indeed, the optimality equations on $S$ give

$$x_S=\frac r a B^{-1}(e-\mu j),\qquad \mu=(1-r)ac.$$

The relation $P_{-\sigma}x=r P_{-\sigma}y$ gives

$$\mathcal E_++\mathcal E_-+c^2=\|x\|^2+(r^{-2}-1)\|P_{-\sigma}x\|^2
=r^{-2}x_S^*Bx_S=a^{-2}\|B^{-1/2}(e-\mu j)\|^2.$$

The minimizing $\eta_*$ makes $e-\eta_*j$ orthogonal to $j$ in the $B^{-1}$ metric. The mean equation says $c=(r/a)(\eta_* -\mu)H$. Thus the squared norm in the last formula separates into $T$ and $(\eta_* -\mu)^2H$, which proves (1). In particular $c^2/\ell+T/a^2=c^2+(1-c^2)/r$. The result applies on either actual support, with the same left side and potentially different contributions.

In spectral terms, for $\mu_j$ the spectral measure of the restricted constant for $C$,

$$
\ell=\int_{[0,1]}\frac{r^2}{r^2+(1-r^2)\lambda}\,d\mu_j(\lambda),\quad
T=\int_{[0,1]}\frac{d\mu_{e-\eta_*j}(\lambda)}{r^2+(1-r^2)\lambda}.
$$

In particular $0<\ell\le |S|/n$. The factor $c^2$ in (1) is essential when $c$ varies. Along any sequence $r\to0$, bounded total allowed energy is equivalent to $\ell$ bounded below and $T$ bounded above. In one direction use $c\le1$ and the uniform bounds on $a,a^{-1}$. In the other use $c^2=1-r(\mathcal E_++\mathcal E_-)$ as well.

## Two signed trial problems

The two costs have separate geometric tests that require no rank cutoff:

$$\begin{aligned}
\ell^{-1}&=\min_{j^*v=1}\left[\|v\|^2+(r^{-2}-1)\|P_{-\sigma} E_Sv\|^2\right],\
T&=\min_{\eta,v,w}
\left\{\|v\|^2+\|w\|^2:
e-\eta j=r v+\sqrt{1-r^2}\,E_S^*P_{-\sigma} w\right\}.
\end{aligned}\tag{2}$$

The first is the minimum of the squared $B/r^2$ norm under a mean constraint. For the second, the operator on $(v,w)$ in the constraint has Gram matrix $B$ and is onto, since $r>0$. Its least squared-norm preimage of a fixed right-hand side has cost given by $B^{-1}$. Minimizing over $\eta$ proves the claim. Equivalently, one needs a bounded mean-one trial with $O(r)$ opposite leakage and a bounded opposite-sector interpolator whose restricted error after a constant correction is $O(r)$. The two trials can be constructed independently. Positivity is only used to identify the true $S$ leading to (1). The signed trials in (2) need no positivity.

At $r_p=o(n^{-1/4})$, estimates in (2) on *either* actual sign support would bound both allowed energies, and hence complete the [one-width comparison](quadratic-fourth.md#a-one-sided-single-width-criterion) using the [fixed positive width limit](parallel-fixed-width-13.md). The [one-sided compression test](astra-energy-13.md) directly treats a single allowed energy using the centered bulk part of the actual primal vector. It permits a large opposite energy. The test in (2) instead isolates the constant and the marked linear functional in two quadratic minimizations. An unweighted minimum positive eigenvalue does not certify either test.

## Finite comparisons and certification

[The replay](../quadratic_compression.py) takes candidate supports from the existing damped iteration. It reconstructs the optimizer by solving with $B$ in orthonormal even orbit coordinates and applying the rank-one formula for $Q_{\sigma,SS}^{-1}$. For interval certification it uses the exact binary-rational width in the CSV, forms $B$ from Fourier projector coefficients enclosed by Arb, checks every active coordinate positive, and applies the full $Q_\sigma$ by a Fourier ball transform to check all inactive multipliers positive. The zero equations on the support hold by construction. KKT then proves the identity of the reconstructed optimizer. The [64 rows](../data/quadratic-compression.csv) include 40 interval-certified comparisons. At the exact width $r=1/4$ for $p=5$, the mean cost, mark cost and total allowed energy are $(4/5,4/5,4/5)$ on the plus support and $(8/5,0,4/5)$ on the minus support, also checked by the certificate.

Selected values at $r\sqrt q=1/4$ are rounded below:

| Order | Support sign | $\ell$ | $c^2/\ell$ | $T/a^2$ | Total allowed energy |
|---:|:---:|---:|---:|---:|---:|
| 97 | + | 0.311152 | 2.8945 | 1.9207 | 3.9146 |
| $11^2$ | + | 0.101187 | 8.0348 | 1.0055 | 8.2273 |
| $11^2$ | − | 0.539710 | 1.5064 | 7.5339 | 8.2273 |
| $19^2$ | + | 0.056695 | 14.2314 | 1.2548 | 14.6793 |
| $19^2$ | − | 0.489339 | 1.6489 | 13.8373 | 14.6793 |
| 1997 | + | 0.279463 | 3.4746 | 2.6784 | 5.1819 |
| $97^2$ | + | 0.010456 | 76.6116 | 1.3800 | 77.1905 |
| $97^2$ | − | 0.473358 | 1.6923 | 76.2993 | 77.1905 |
| 9413 | + | 0.264456 | 3.7275 | 2.7844 | 5.5261 |

The entries above 401 are numerical reconstructions. In these square examples the rapid growth comes from the mean cost on the plus support and the centered mark cost on the minus support. The plus support at $97^2$ still contains 1339 coordinates out of 4704, so its density is much larger than its filtered mean weight. A bound on just the support density would miss that divergence. Both terms stay bounded in the displayed prime cases. Their uniform bounds through primes remain open.
