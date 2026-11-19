# Dual majorants for the square-root cost

For [Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), the [one-cost test](parallel-random-2.md#a-square-root-cost-for-the-exact-signed-optimum) uses the full Fourier LP with cost $\sqrt w$. Its dual is a pointwise majorant in the complementary Fourier space. An optimal primal and dual pair identifies the test with a signed-log optimization over reweightings penalized by relative entropy. On an explicit square-field placement of the harmonic masses with $k\sim n^{3/4}$, the signed-log value tends to zero and the exact LP enclosure has width tending to infinity. For uniform injections at that scale, a projected-cost majorant gives an $O(\sqrt{\log n})$ bound, and no rescaling of that projection followed by a constant repair gives a bounded majorant value with high probability. The true LP can use all complementary Fourier directions.

## Exact dual and the reweighting it selects

Write $U_\sigma=\mathbb R\mathbf1\oplus V_\sigma$ for the real Fourier space of sign $\sigma=\pm1$, with $V_+\oplus V_-=\mathbf1^\perp$. Let $\mathcal P_\sigma=\{P\in U_\sigma:P\ge0,\ \bar P=1\}$. Fix normalized weights $w$, put $S=\{i:w_i>0\}$ and $c_i=\sqrt{w_i}$, and use the [signed optimum and entropy identity](random-weight-ranks.md#curvature-at-weights-with-zeros). The full support function and the normalized LP value are

$$h_\sigma(c)=\max_{P\in\mathcal P_\sigma}c\cdot P
  =\min_{\substack{Y\in U_{-\sigma}\\Y\ge c}}\sum_i Y_i,\qquad
R_\sigma(w)=h_\sigma(c)/\sqrt n.\tag{1}$$

Indeed, write $P=\mathbf1+Ax$ for a real basis $A$ of $V_\sigma$ and free coefficients $x$. Dualizing $-Ax\le\mathbf1$ gives a nonnegative multiplier $z$ with $A^{\mathsf T}(c+z)=0$ and objective $\sum_i(c_i+z_i)$. Thus $Y=c+z$. Both optima are attained by LP duality. For checking a proposed $Y$, projection onto $U_{-\sigma}$ followed by addition of the positive part of the largest coordinate deficit gives a feasible certificate in exact arithmetic. Every exterior inequality $Y_i\ge0$ for $i\notin S$ is part of (1).

For any such certificate $Y$, put $a=\sum_iY_i$. The spectrum $nY/a$ is feasible on the opposite side. Evaluating its log objective and using the entropy identity gives the upper bound

$$\sigma F(w)\le 2\log(a/\sqrt n)
   -2\sum_{i\in S}w_i\log\frac{Y_i}{c_i}.\tag{2}$$

The second term uses the actual slack of the same certificate on the marks. Omitting it gives the one-cost enclosure. The difference between the right side of (2) and $\sigma F(w)$ is exactly twice the opposite log-optimality gap of $nY/a$.

The underlying reweighting formula is

$$2\log R_\sigma(w)
  =\max_{u\in\Delta(S)}\{\sigma F(u)-D(u\|w)\},
  \qquad D(u\|w)=\sum_{i:u_i>0}u_i\log(u_i/w_i).\tag{3}$$

To see it, expand $\log(c\cdot P)$ as the maximum over $u\in\Delta(S)$ of $\sum_i u_i\log(c_iP_i/u_i)$, with zero summands omitted and value $-\infty$ if $u$ charges a zero of $P$. Take the maximum over $P$, then use $2F_\sigma(u)=\log n+\sum_i u_i\log u_i+\sigma F(u)$. There is also an explicit maximizing $u$. If $(P,Y)$ attains (1), set $u_i=c_iP_i/h_\sigma(c)$. Complementary slackness gives $P_i(Y_i-c_i)=0$ everywhere. The feasible spectra $P$ and $nY/h_\sigma(c)$ therefore have product $nu$ coordinatewise. On the support of $u$ their log objectives sum to the full complementary entropy value, so each is optimal for $u$.

In particular the excess over $\sigma F(w)$ in (3) is the largest signed increment available to an adaptive reweighting after paying $D(u\|w)$. The sum of those two nonnegative excesses is the width $2\log(R_+R_-)$ of the LP enclosure. Small $F(w)$ at the sampled profile gives no estimate on that width by (3) alone.

## A certificate and its limitation under uniform injection

Let $K$ be the real Fourier multiplier with eigenvalues $\pm1$ on $V_\pm$ and zero on constants. Use the [Jacobi entry bound](fourier.md#joint-distribution-on-the-even-modes) $|K_{ij}|\le M/\sqrt n$, with $M=\sqrt{(2n+1)/n}$ for either prime or prime-square Paley orders. For each $\lambda\in\mathbb R$ the following is a feasible majorant in (1):

$$Y_{\sigma,\lambda}
  =\lambda(I-\sigma K)c+t_{\sigma,\lambda}\mathbf1,\qquad
t_{\sigma,\lambda}=\max_i\{(1-\lambda)c_i+\lambda\sigma(Kc)_i\}.\tag{4}$$

In particular, taking $\lambda=1$ gives

$$R_\sigma(w)\le \frac{\|c\|_1}{\sqrt n}+\sqrt n\max_i\sigma(Kc)_i.\tag{5}$$

On a uniform ordered injection of any deterministic mass profile $(m_j)$ of sum one, sort the input lengths $d_j=\sqrt{m_j}$ in decreasing order. This merely relabels the random slots. For a fixed row $i$, reveal the locations in this order and use the Doob martingale for $(Kc)_i=\sum_jd_jK_{i,I_j}$. At reveal $j<n$ its increment is

$$\left(d_j-\frac{\sum_{a>j}d_a}{n-j}\right)(K_{i,I_j}-\bar K_{i,\mathrm{unused}}),$$

where the mean is over the coordinates still unused just before reveal $j$. The coefficient lies in $[0,d_j]$. Thus the conditional range length is at most $2Md_j/\sqrt n$. Hoeffding's exponential-moment bound and $\sum_jd_j^2=1$ give $\mathbb E\exp(t\sqrt n\,\sigma(Kc)_i)\le\exp(t^2M^2/2)$, since each row has mean zero. Taking the maximum over $n$ rows gives, for either sign and $1\le k<n$,

$$\mathbb E R_\sigma(w)\le \sqrt{k/n}+M\sqrt{2\log n},\qquad
\mathbb P\!\left\{R_\sigma(w)>\sqrt{k/n}+M\sqrt{2\log(n/\delta)}\right\}\le\delta
\quad(0<\delta<1).\tag{6}$$

This uses only a single matrix-vector product. At $k=\lfloor n^{3/4}\rfloor$ it improves the $O(\sqrt k)$ bound obtained by summing one-mark caps. The expectation bound in (6) grows with $n$ and gives no vanishing signed estimate.

For the harmonic profile at this same scale, even the minimum normalized mass among the certificates in (4) tends to infinity in probability, for either sign. For any two distinct rows $i,\ell$, the vectors $\sqrt n(K_{iy},K_{\ell y})$ over uniform $y$ have mean zero, bounded entries and covariance $I_2+O(1/n)$ since $K^2=I-J$. The same holds in one row. Apply the [weighted sampling and Gaussian comparison](parallel-random-2.md#the-two-row-estimate) with no held-out slot or omitted coordinate. For every fixed smooth bounded test with bounded derivatives through order three, the errors are uniform over rows and $O(\sqrt{k/n}+\sum_jd_j^3+1/n)=o(1)$. Here $\sum_jd_j^3\le(\sum_jm_j^2)^{1/2}\le\sqrt{2/k}$.

Fix $T>0$ and a smooth test $0\le f\le1$ that vanishes on $(-\infty,T]$ and has strictly positive standard Gaussian mean. The empirical average of $f(\sigma\sqrt n(Kc)_i)$ tends to that mean in probability. The one-row test gives the limiting expectation, and the two-row test $f(x)f(y)$ gives variance $o(1)$ because its Gaussian coordinates are independent. Removing the $k=o(n)$ marks changes the average by at most $k/n$. Hence $L=\sqrt n\max_{i\notin S}\sigma(Kc)_i\to\infty$ in probability.

The normalized mass of (4) is $\lambda\|c\|_1/\sqrt n+\sqrt n t_{\sigma,\lambda}$. For $\lambda\ge1/2$, the exterior constraints give a lower bound $L/2$ on the event $L>0$. For $\lambda\le1/2$, choose a mark with $c_i\ge1/\sqrt k$. Its constraint gives the affine lower bound

$$\sqrt n c_i+\lambda\left(\|c\|_1/\sqrt n+\sqrt n[\sigma(Kc)_i-c_i]\right).$$

The slope is negative with probability tending to one. The same exponential-moment estimate gives $\sqrt n\|Kc\|_\infty=O_{\mathbb P}(\sqrt{\log n})$, while $\sqrt{n/k}\asymp n^{1/8}$ and $\|c\|_1/\sqrt n\le\sqrt{k/n}$. Evaluating the affine bound at $\lambda=1/2$ now gives the uniform lower bound $\tfrac12\sqrt{n/k}-\tfrac12\sqrt n\|Kc\|_\infty$ throughout $\lambda\le1/2$. Both lower bounds diverge in probability. This proves an obstruction for the particular family (4) at prime and square orders. The unrestricted dual in (1) has additional directions, so (4) supplies no asymptotic lower bound for its optimum.

## Exact separation on a growing square-field rectangle

Take $q=r^2$ with $r\equiv1\pmod4$ prime, put $b=r-1$, $m=(r+1)/2$ and $n=bm$. In the [subfield and norm-one coset grid](sparse-mark-geometry.md#exact-coset-shifts-over-square-fields), there are $b$ rows and $m$ columns. The translated subgroup spectra $b\mathbf1_{\{\mathrm{row}\}}$ and $m\mathbf1_{\{\mathrm{column}\}}$ are feasible plus and minus spectra, respectively. In particular, a vector constant within each row is in $U_+$, and one constant within each column is in $U_-$.

Use $A$ rows and $B$ columns with $k=AB$. Assign the increasing [harmonic profile](parallel-sparse.md) $w_{ad}=x_{(a-1)B+d,k}/k$ for $1\le a\le A$, $1\le d\le B$, zero elsewhere, where $x_{j,k}=H_k-H_{k-j}$. On the plus side choose the single last row spectrum. As a dual majorant, extend the last row cost to be constant on each column, including zero for unused columns. This majorizes every entry since the costs are increasing down columns, and its mass equals the row spectrum's objective. On the minus side the last column and the rowwise extension of its cost give the reverse pair. Thus the exact values are

$$
\begin{aligned}
R_+(w)&=\sqrt{\frac{b}{m}\frac BA}\,\frac1B\sum_{d=1}^B\sqrt{H_k-H_{B-d}},\\
R_-(w)&=\sqrt{\frac{m}{b}\frac AB}\,\frac1A\sum_{a=1}^A\sqrt{x_{aB,k}}.
\end{aligned}\tag{7}
$$

Let $D_k=k^{-1}\sum_j x_{j,k}\log x_{j,k}$, with $D_k\to D=1-\gamma$ by the [entropy comparison for deterministic masses](parallel-sparse.md#deterministic-masses-and-a-bounded-finite-palette). Write $D_{\rm row}=A^{-1}\sum_a \mu_a\log\mu_a$ for the corresponding moment of the row means $\mu_a=B^{-1}\sum_d x_{(a-1)B+d,k}$. Then $0\le\Delta=D_k-D_{\rm row}\le H_k/A$. In fact the Jensen gap of $x\log x$ in a block of mean $\mu$ is at most $\operatorname{Var}(x)/\mu$, which is at most the range of that block by $x^2\le(\max x)x$. The sum of the ranges of the consecutive blocks is at most $H_k$.

The plus spectrum that mixes the selected rows according to the row masses scores $\log b-\log A+D_{\rm row}$. The minus spectrum that mixes the selected columns uniformly scores $\log m-\log B$. Their scores sum to the entropy optimum minus $\Delta$. Since the two log-optimality gaps are nonnegative, their difference has absolute value at most $\Delta$. This gives

$$\left|F(w)-\left[\log(b/m)-\log(A/B)+D_k\right]\right|\le 2\Delta.\tag{8}$$

Choose $\alpha=2e^D$, $B=\lfloor n^{3/8}/\sqrt\alpha\rfloor$, $A=\lfloor\alpha B\rfloor$. These rectangles fit for all sufficiently large $r$. They have $k\sim n^{3/4}$, and (8) yields $F(w)\to0$. In the first sum in (7), the minimum squared summand is $H_k-H_{B-1}\sim\log A$ and the mean of the squared summands is $H_k-H_B+1\sim\log A$. This sandwiches the mean of the square roots after Jensen. For the second sum in (7), the difference from the mean of all $k$ square roots is at most $\sqrt{H_k}/A$ by monotonicity and summing the block ranges. The latter mean tends to $\mathbb E\sqrt X=\sqrt\pi/2$ for $X\sim\operatorname{Exp}(1)$. On compact subintervals of $0<j/k<1$ the harmonic profile converges to the exponential quantile $-\log(1-j/k)$, and the contribution from any fraction $\epsilon$ of the indices is at most $\sqrt{\epsilon}$ by Cauchy–Schwarz and $k^{-1}\sum_j x_{j,k}=1$. Consequently

$$
\frac{R_+(w)}{\sqrt{\log A}}\ \longrightarrow\ e^{-D/2},\qquad
R_-(w)\ \longrightarrow\ e^{D/2}\frac{\sqrt\pi}{2},\qquad
2\log(R_+R_-)=\log\log A+\log(\pi/4)+o(1).\tag{9}
$$

This is a primal and dual separation on the actual Paley Fourier LP, for the same harmonic profile and a growing sparse scale. It uses prescribed locations over square fields. For uniform injections over primes or squares, these placements give no lower bound on the mean width of the true LP enclosure.

## Full LP checks on uniform injections

For each order below, 24 uniform ordered injections used the harmonic masses at $k=\lfloor n^{3/4}\rfloor$. Each sign was solved in the full real sine and cosine basis with every frequency inequality. The width is averaged across the 24 pointwise enclosures. The last column averages the independently projected log intervals at floor mass $10^{-4}$. All comparisons here use floating point.

| $q$ | $k$ | Mean $R_+$ | Mean $R_-$ | Mean one-cost width | Mean width with (2) | Mean signed-log interval |
|---:|---:|---:|---:|---:|---:|---:|
| 41 | 9 | 1.17452 | 1.20223 | 0.65464 | 0.35011 | $[-0.03380,-0.03369]$ |
| 101 | 18 | 1.14418 | 1.18394 | 0.59208 | 0.36186 | $[-0.02154,-0.02142]$ |
| $13^2$ | 27 | 1.18931 | 1.17485 | 0.65971 | 0.39942 | $[-0.01000,-0.00987]$ |
| 401 | 53 | 1.12129 | 1.19630 | 0.58316 | 0.38785 | $[-0.06710,-0.06695]$ |
| $29^2$ | 92 | 1.15280 | 1.14160 | 0.54403 | 0.38056 | $[-0.00471,-0.00455]$ |
| 1009 | 106 | 1.14355 | 1.13216 | 0.51485 | 0.35591 | $[0.01348,0.01364]$ |

The repaired primal and dual values divided by $\sqrt n$ differed by less than $5.0\times10^{-9}$. Each slack-adjusted interval intersected the corresponding projected log interval. The largest stationary residual was below $10^{-9}$. With the same LPs the $(A,B)=(9,3)$ rectangle at $13^2$ gives $(R_+,R_-)=(1.31520,1.28600)$ and the $(15,5)$ rectangle at $29^2$ gives $(1.49300,1.20839)$, agreeing with (7) to less than $10^{-7}$. The sample table quantifies the slack at these inputs. It gives no asymptotic trend or sampling error bound for the expectation.

The following replay runs from the repository root.

~~~python
from math import exp, sqrt
import numpy as np
from scipy.optimize import linprog

from face_ranks import spectrum_basis
from poisson_weights import log_bounds
from square_control import square_field_sign
from theta import paley_sign

def harmonic(k):
    return np.cumsum(1 / np.arange(k, 0, -1)) / k

def lp_pair(sign, basis, side, cost):
    n = len(cost)
    result = linprog(-(cost @ basis), A_ub=-basis, b_ub=np.ones(n),
                     bounds=(None, None), method="highs")
    assert result.success, result.message
    primal = 1 + basis @ result.x
    repair = max(0., -primal.min()) + 1e-12
    primal = (primal + repair) / (1 + repair)
    transform = np.fft.rfft(cost - result.ineqlin.marginals)
    transform[1:] *= sign[1:len(transform)] == -side
    dual = np.fft.irfft(transform, n)
    dual += max(0., np.max(cost - dual)) + 1e-12
    return cost @ primal / sqrt(n), dual.sum() / sqrt(n), dual

def check(sign, bases, w):
    cost = np.sqrt(w)
    marks = w > 0
    ratios, endpoints, adjusted = [], [], []
    for side, basis in zip((1, -1), bases):
        lower, upper, dual = lp_pair(sign, basis, side, cost)
        assert -1e-10 <= upper - lower < 5e-9
        ratios.append(upper)
        endpoints.append(2 * np.log(upper))
        adjusted.append(endpoints[-1] - 2 * (w[marks] @ np.log(dual[marks] / cost[marks])))
    lower, upper, residual = log_bounds(sign, w, 1e-4)
    assert residual < 1e-9
    assert max(lower, -adjusted[1]) <= min(upper, adjusted[0]) + 1e-8
    return [*ratios, sum(endpoints), sum(adjusted), lower, upper]

for q in (41, 101, 169, 401, 841, 1009):
    r = int(sqrt(q))
    square = r*r == q
    sign = square_field_sign(r) if square else paley_sign(q)
    n = len(sign)
    bases = [spectrum_basis(sign, side) for side in (1, -1)]
    rng = np.random.default_rng(2603 + q)
    k = int(n**.75)
    samples = []
    for _ in range(24):
        w = np.zeros(n)
        w[rng.choice(n, k, replace=False)] = harmonic(k)
        samples.append(check(sign, bases, w))
    print(q, k, np.round(np.mean(samples, axis=0), 8))
    if square:
        b, m = r-1, (r+1)//2
        alpha = 2*exp(1-0.5772156649015329)
        cols = int(n**.375 / sqrt(alpha))
        rows = int(alpha*cols)
        mass = harmonic(rows*cols).reshape(rows, cols)
        sites = (np.arange(rows)[:, None]*m + np.arange(cols)[None, :]*b) % n
        w = np.zeros(n)
        w[sites] = mass
        ratios = np.asarray(check(sign, bases, w)[:2])
        exact = [b*np.sqrt(mass[-1, :]).sum()/sqrt(n),
                 m*np.sqrt(mass[:, -1]).sum()/sqrt(n)]
        assert np.max(np.abs(ratios - exact)) < 1e-7
        print("rectangle", q, rows, cols, ratios)
~~~

At prime order the signed estimate for growing uniform injections still needs control of the true adaptive reweightings in (3), a majorant in (1) beyond (4), or a direct signed estimate. Even a vanishing signed mean at this scale would control only the remainder in the [rank expansion](random-weight-ranks.md#an-integral-identity-for-finitely-many-labels).
