# A source Krylov certificate for the half-angle signed tail

For [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), a 32-dimensional Krylov space generated from the propagated marked source gives small signed-tail intervals on three prime fields. Separate lower bounds show that both unsigned tails are larger than the entire signed interval. The same calculation gives a large positive tail at the matched square orders. The certificate uses a squared, site-weighted residual of one source solve. It does not require a Lyapunov inequality on the ambient space.

## The signed residual identity

Keep the notation of the [signed time integral](parallel-sign-4.md). Use the half-angle diagonal $F_i=\tanh(\gamma_i/2)=v_i/(u_i+2\sqrt{w_i})$ off the mark and $F_0=0$, as in the [half-angle inverse](stationary-secant.md). Set $V=|F|^{1/2}$, $S=\operatorname{sgn}F$ with sign $+1$ at zeros, $B=SVKV$, $A=I-B$, $z=Ke$, and $b=SVz$. The orbit is $y(s)=e^{-sA/2}b$, and $d=y(T)$. The quantity to enclose is

$$
J_T=d^{\mathsf T}SA^{-1}d
    =J_T^+-J_T^-,\qquad
J_T^\pm=\int_T^\infty \|P_\pm y(s)\|^2\,ds ,
$$

where $P_\pm$ are the coordinate projections for the two signs of $S$. Write $D=I-|F|$ for the **gap diagonal in this note** and $\delta=\min_i D_{ii}>0$. Then

$$
L=\tfrac12(A+A^{\mathsf T})=(I_+-N_{++})\oplus(I_-+N_{--}),
\qquad L\succeq D,
$$

where $N=VKV$. The block inequality follows from $\|K\|\le1$ on each sign block after multiplication on both sides by $V$.

For **any** trial vector $x$, put $r=d-Ax$. Since $SA$ and $SA^{-1}$ are symmetric, expansion gives

$$
\boxed{\quad J_T=x^{\mathsf T}S(d+r)+r^{\mathsf T}SA^{-1}r,\qquad
|r^{\mathsf T}SA^{-1}r|\le \|D^{-1/2}r\|^2 .\quad} \tag{1}
$$

Indeed, for $h=A^{-1}r$,
$\|D^{1/2}h\|^2\le h^{\mathsf T}Lh=h^{\mathsf T}r
\le\|D^{1/2}h\|\|D^{-1/2}r\|$.
Use this once more in $r^{\mathsf T}Sh$, since $S$ commutes with $D$. The same proof gives the bound with $L^{-1}$ in place of $D^{-1}$, since $L$ also commutes with $S$. Using $D$ gives a directly computable sum; only those coordinates on which the *source residual* lands pay a penalty for saturation. The correction $x^{\mathsf T}Sr$ is essential to make the remainder quadratic without imposing a Galerkin orthogonality condition.

Choose $x$ in $\mathcal K_m(B,d)=\operatorname{span}\{d,Bd,\ldots,B^{m-1}d\}$ to minimize the radius in (1). With an Arnoldi basis $U$, this is a weighted least-squares problem with $m$ columns, $D^{-1/2}AU$, and right-hand side $D^{-1/2}d$. Neither invariance of this finite Krylov space nor a bound on its omitted eigenvalues is needed. Equivalently $x=p(B)d$ and $r=h(B)d$, where $h(t)=1-(1-t)p(t)$. The best squared radius is the minimum of

$$
\sum_{j,k=0}^m h_j h_k\,\langle B^j d,D^{-1}B^k d\rangle
\quad\text{over } \deg h\le m,\ h(1)=1. \tag{2}
$$

This is a positive Gram form on the actual marked trajectory. At $m=0$, (1) only gives $\|D^{-1/2}d\|^2$. No choice of test channels from the full coupling matrix is involved.

## Propagation and checks of the two signs

If $\tilde d$ is the Poisson series through degree $M$, then
$\|d-\tilde d\|\le\epsilon_T=\|b\|\Pr\{\operatorname{Pois}(T/2)>M\}$.
For a trial built from $\tilde d$, let $\tilde r=\tilde d-Ax$. An interval for $J_T$ has center $C=x^{\mathsf T}S(\tilde d+\tilde r)$ and radius

$$
\rho=\left(\|D^{-1/2}\tilde r\|+\epsilon_T/\sqrt{\delta}\right)^2
              +2\epsilon_T\|x\| . \tag{3}
$$

This follows by applying (1) with the exact $d$ and bounding both occurrences of the propagation error. This is the only use of the minimum gap in (3); the residual itself is weighted site by site.

For a separate test for cancellation, choose $U_*>T$, and let $\bar y=\int_T^{U_*} y(s)\,ds$. Cauchy–Schwarz in time gives $J_T^\pm\ge\|P_\pm\bar y\|^2/(U_*-T)$. Integrate the Poisson coefficients exactly up to $M$: the coefficient of $B^k b$ is $2[\mathsf P(k+1,U_*/2)-\mathsf P(k+1,T/2)]$, with $\mathsf P$ the regularized lower incomplete gamma function. For the resulting $\widetilde{\bar y}$, a lower bound is

$$
\ell_\pm=\frac{(\|P_\pm\widetilde{\bar y}\|-(U_*-T)\epsilon_{U_*})_+^2}{U_*-T}. \tag{4}
$$

Thus $|C|+\rho\ll\min(\ell_+,\ell_-)$ distinguishes cancellation from decay of both unsigned tails. Equation (4) uses only a finite time interval and no information from the fitted Krylov solve.

For an independent signed reference, put $a=u_0-2\sqrt{\tau/n}$, $x_b=SVv/a$. For exact stationarity $Ax_b=b$, and $J_T=y(2T)^{\mathsf T}Sx_b$. Even for a stationary *trial* $v$ used to build $F$, the identity

$$
b-Ax_b=(SV/a)(Ku-v)
$$

holds: $Fv=u-2\sqrt{\tau/n}\,\mathbf1-a e_0$ and $K\mathbf1=0$. The error in the reference $\tilde y(2T)^{\mathsf T}Sx_b$, for that supplied $F$, is bounded by

$$
\epsilon_{2T}\|x_b\|+
\big(\|D^{-1/2}\tilde y(2T)\|+\epsilon_{2T}/\sqrt\delta\big)
       \|D^{-1/2}(b-Ax_b)\|. \tag{5}
$$

This follows from the weighted inverse estimate used in (1). The fit takes the diagonal as input and does not use the reference column.

For a rigorous transfer from a trial diagonal $\widetilde F$ to $F$, one can add

$$
\|e\|^2\|F-\widetilde F\|_\infty
\left[\frac{1}{\delta_F\delta_{\widetilde F}}+T+\tfrac12 T^2\right]
$$

to the radius, with $\delta_E=\min_i(1-|E_i|)$. In fact $J_T=m_F-m_0-\int_0^T j(s)\,ds$. Use the resolvent identity for the marked scalar and $j(s)=z^{\mathsf T}F e^{-s(I-KF)}z$ for the prefix; Duhamel and the two contraction estimates bound the difference of the densities by $(1+s)\|z\|^2\|F-\widetilde F\|_\infty$. This transfer is crude and needs an independent input bound. For instance, if a radius $R$ around $\tilde v$ satisfies $\|\tilde v-K\tilde u\|\le R(1-c_R)$, where $c_R=\max_i (|\tilde v_i|+R)/\sqrt{(|\tilde v_i|+R)^2+4w_i}$, then the stationary map contracts the ball into itself. This gives $\|F-\widetilde F\|_\infty\le R/(4\sqrt{\tau/n})$ by the derivative bound on the half-angle map. These input bounds were not used in the replay.

## True Paley orders

At $\tau=0.01$ the following runs used $m=32$, $M=95$, and $U_*=T+8$. The reference in the last column uses the half-angle column in (5). All rows use the actual Paley prime or prime-square character and a numerical stationary solve. The measured stationary residual is below $10^{-10}$ in all runs; the reference error estimate (5) is below $10^{-9}$ in the table and $5\cdot10^{-9}$ in the lower-floor run below. All displayed numbers are rounded floating-point diagnostics, without directed rounding or certification of the nonlinear stationary solve. Formulas (1)–(5) are exact bounds for the supplied diagonal if evaluated with rigorous arithmetic; (5) controls the reference for that diagonal, not its distance from the tail of the unknown exact stationary diagonal.

| Field order | $T$ | $\ell_+$ | $\ell_-$ | Center $C$ | Radius $\rho$ | Half-angle reference |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $9413$ | 8 | 0.007601 | 0.007735 | $-2.01\cdot10^{-4}$ | $4.03\cdot10^{-7}$ | $-2.00875\cdot10^{-4}$ |
| $97^2$ | 8 | 0.2272 | 0.005473 | 0.693215 | $8.09\cdot10^{-12}$ | 0.693215 |
| $37253$ | 8 | 0.007868 | 0.007742 | $3.88\cdot10^{-5}$ | $6.89\cdot10^{-7}$ | $3.88294\cdot10^{-5}$ |
| $193^2$ | 8 | 0.1500 | 0.004104 | 0.839284 | $2.43\cdot10^{-11}$ | 0.839284 |
| $153649$ | 8 | 0.007648 | 0.007696 | $-1.40\cdot10^{-5}$ | $5.96\cdot10^{-7}$ | $-1.40242\cdot10^{-5}$ |
| $389^2$ | 8 | 0.08516 | 0.004233 | 0.922460 | $1.16\cdot10^{-10}$ | 0.922460 |
| $9413$ | 32 | $5.01\cdot10^{-5}$ | $5.73\cdot10^{-5}$ | $-7.88\cdot10^{-6}$ | $4.02\cdot10^{-10}$ | $-7.88308\cdot10^{-6}$ |
| $97^2$ | 32 | 0.07109 | 0.001254 | 0.214457 | $3.28\cdot10^{-16}$ | 0.214457 |
| $37253$ | 32 | $7.35\cdot10^{-5}$ | $6.63\cdot10^{-5}$ | $1.08\cdot10^{-5}$ | $8.08\cdot10^{-10}$ | $1.08369\cdot10^{-5}$ |
| $193^2$ | 32 | 0.08450 | 0.000709 | 0.468626 | $8.14\cdot10^{-16}$ | 0.468626 |
| $153649$ | 32 | $6.48\cdot10^{-5}$ | $6.53\cdot10^{-5}$ | $-7.56\cdot10^{-7}$ | $7.01\cdot10^{-10}$ | $-7.55958\cdot10^{-7}$ |
| $389^2$ | 32 | 0.06460 | 0.000290 | 0.694350 | $3.51\cdot10^{-15}$ | 0.694350 |

At $T=8$, $|C|+\rho$ is at most $2.7\%$ of either unsigned lower bound at all three primes, and just $0.2\%$ at $153649$. The zero-trial radii at those primes are $0.096$–$0.098$. At $T=32$ the lower bounds themselves shrink, but $|C|+\rho$ is still under $17\%$ of either at all three primes. The largest pair reproduces the signed $T=32$ comparison in [the half-angle note](stationary-secant.md#numerical-comparison). At the squares the fitted boundary value remains positive and large: the same procedure does not erase the known imbalance. In particular, at $389^2$, $T=8$, the radius falls from $2.5\cdot10^{-5}$ at $m=16$ to $1.2\cdot10^{-10}$ at $m=32$, while the center stays near $0.92246$.

At the lower fixed floor $\tau=0.0005$ for the largest pair, $T=8$, the prime interval has $C\approx5.90\cdot10^{-5}$, $\rho\approx9.88\cdot10^{-4}$ and $\min(\ell_+,\ell_-)\approx0.0155$. It still detects cancellation, but the radius is now about 17 times the center. The square gives $C\approx1.11241$ and $\rho\approx2.49\cdot10^{-8}$. These runs give no uniform degree bound as the floor tends to zero.

## What would make this asymptotic?

For the true half-angle weights and a residual supported off the mark there is the exact cost identity

$$
\|D^{-1/2}r\|^2
=\tfrac12\|r\|^2+\sum_{i\ne0}\frac{u_i+|v_i|}{4\sqrt{\tau/n}}\,r_i^2 .
\tag{6}
$$

Indeed $(u_i+2\nu_i)^2-v_i^2=4\nu_i(u_i+2\nu_i)$, with $\nu_i=\sqrt{\tau/n}$. This identifies the needed arithmetic estimate: the chosen polynomial defect $h(B)d$ must be small in the squared residual cost seen by the stationary bulk mass. For example, a sufficient bound on the second term in (6) is $\sqrt{W/\tau}\,n\|r\|_\infty^2$, using $\sum u_i=2\sqrt{nW}$, $W=\sum w_i$. The norm bound is sufficient only; (6) permits concentration where the stationary mass is small.

The [marked contraction defect](stationary-defect-tail.md#the-defect-bounds-the-marked-orbit) further confines the residual estimate to small-gap sites. Since $V^2\preceq I-e_0e_0^{\mathsf T}$, $bb^{\mathsf T}\preceq I-BB^{\mathsf T}$; telescoping its conjugates by $B^k$ gives $\|\sum a_k B^k b\|\le\|a\|_{\ell_2}$. The coefficients for $r=h(B)d$ are the convolution of the coefficients of $h$ with the Poisson probabilities of mean $T/2$. Hence $\|r\|\ll\|h\|_{\ell_1}(1+T)^{-1/4}$, where $\|h\|_{\ell_1}$ is its coefficient norm. For any $0<\eta<1$,

$$
\|D^{-1/2}r\|^2
\ll \frac{\|h\|_{\ell_1}^2}{\eta\sqrt{1+T}}
      +\sum_{D_{ii}<\eta}\frac{r_i^2}{D_{ii}} . \tag{7}
$$

The first term follows by dropping the weight on sites with $D_{ii}\ge\eta$ at cost $1/\eta$. For $\eta=T^{-1/4}$ and bounded coefficient norm this term tends to zero uniformly in the order. It leaves a specific source residual to estimate on the near-saturated sites.

If the signed moments $b^{\mathsf T}SB^k b$ tend to zero for every fixed $k$ on the **true** prime half-angle diagonals, then the center of (1) tends to zero for any fixed $T$ and fixed-degree polynomials $p$ with uniformly bounded coefficients. In fact the center equals
$b^{\mathsf T}Se^{-TA}[2p(B)-(I-B)p(B)^2]b$.
The exponential series is uniformly summable because $\|B\|\le1$. For any desired tail tolerance, it would suffice to choose $T$ and a degree independently of the prime, and such bounded-coefficient trials with the limsup of (6) below the tolerance. This, together with fixed-time cancellation, would control the undamped marker using the half-angle identity and the [theta bracket](smoothing.md) in the fixed-floor then vanishing-floor limits. The prior [fixed-depth parity argument](diagonal-damping.md#what-parity-proves-at-fixed-damping) does not establish those moment or residual bounds for true stationarity. Numerical least squares also does not guarantee uniform bounds on the monomial coefficients.

There is an analytic obstruction to such a fixed-degree residual estimate at the square orders with $\tau_q\to0$. The [square stationary limits](parallel-coupling-2.md#exact-square-order-control-with-decreasing-floors) give the marked limit $1/3$ by the exact half-angle inverse, and $F_i\to-1$ in bulk density by continuity of the half-angle map on $[-1,1]$. The [bounded-time square calculation](parallel-sign-4.md#true-square-order-obstruction) then applies to $F$: $J_T\to4/3-e^{-T}$, $\|Bb\|\to0$, $\|b\|\to1$, $b^{\mathsf T}Sb\to-1$, and $D_{ii}\to0$ in bulk density.

If $h$ has fixed degree and bounded coefficients, $r=h(B)d=e^{-T/2}h(0)b+o_{\ell_2}(1)$. For every fixed $\eta>0$ the part of $r$ on $\{D_{ii}>\eta\}$ has norm tending to zero, since $\|b\|_\infty=O(n^{-1/2})$. If the radius in (1) stays bounded along a subsequence, the remaining squared norm is at most $\eta$ times the radius. Sending $\eta$ to zero gives $h(0)\to0$ on that subsequence. Now $p(0)=1-h(0)\to1$, so $x^{\mathsf T}S(d+r)\to-e^{-T}$. Equation (1) forces the liminf of the radius to be at least $4/3$ (also true if it diverges). A small finite-order square radius does not imply a uniform bounded-coefficient approximation as the floor decreases.

## Replay

Run from the repository root. The extra two runs use the lower fixed floor. The code prints $m=0,16,24,32$ radii and checks the compressed intervals against the independent reference using (5), with a floating-point allowance. The largest Poisson omission probability used here is $5.94\cdot10^{-20}$.

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python - <<'PY'
import numpy as np
from scipy.special import gammainc
from scipy.stats import poisson

from poisson_weights import weighted_iterate
from smoothing import kernel_action
from square_control import square_field_sign
from theta import paley_sign


def replay(q, p, tau):
    sign = paley_sign(q) if q == p else square_field_sign(p)
    n = len(sign)
    w = np.full(n, tau / n)
    w[0] = 1
    v, u, stat_res = weighted_iterate(sign, w, tolerance=1e-10)
    assert stat_res <= 1e-10
    F = v / (u + 2 * np.sqrt(w))
    F[0] = 0
    V, S = np.sqrt(abs(F)), np.where(F < 0, -1., 1.)
    D = 1 - abs(F)
    delta = D.min()
    root = np.sqrt(D)

    def B(x):
        return S * V * kernel_action(sign, V * x)

    z = np.fft.irfft(sign[:n // 2 + 1], n)
    b = S * V * z
    a = u[0] - 2 * np.sqrt(w[1])
    xb = S * V * v / a
    rb = S * V * (kernel_action(sign, u) - v) / a
    k = np.arange(96)

    def eps(s):
        return np.linalg.norm(b) * poisson.sf(95, s / 2)

    for T in (8, 32):
        coeff = np.array([poisson.pmf(k, T / 2), poisson.pmf(k, T),
                          2 * (gammainc(k + 1, (T + 8) / 2)
                               - gammainc(k + 1, T / 2))])
        accum = np.zeros((3, n))
        power = b
        for i, col in enumerate(coeff.T):
            accum += col[:, None] * power
            if i + 1 < len(k):
                power = B(power)
        d, d2, integrated = accum
        lower = [max(np.linalg.norm(integrated[S == s]) - 8 * eps(T + 8), 0)**2 / 8
                 for s in (1, -1)]
        ref = (S * xb) @ d2
        ref_err = (eps(2 * T) * np.linalg.norm(xb)
                   + (np.linalg.norm(d2 / root) + eps(2 * T) / np.sqrt(delta))
                   * np.linalg.norm(rb / root))
        Q = np.empty((n, 32), order="F")
        AQ = np.empty_like(Q)
        Q[:, 0] = d / np.linalg.norm(d)
        for j in range(32):
            nxt = B(Q[:, j])
            AQ[:, j] = Q[:, j] - nxt
            if j + 1 < 32:
                for _ in range(2):
                    nxt -= Q[:, :j+1] @ (Q[:, :j+1].T @ nxt)
                Q[:, j+1] = nxt / np.linalg.norm(nxt)

        print(f"{q=} {tau=} {T=} {stat_res=:.3g} {delta=:.3g}"
              f" lower={lower[0]:.9g},{lower[1]:.9g}"
              f" ref={ref:.12g} {ref_err=:.3g}"
              f" rho0={(np.linalg.norm(d / root) + eps(T) / np.sqrt(delta))**2:.6g}")
        for m in (16, 24, 32):
            c = np.linalg.lstsq(AQ[:, :m] / root[:, None], d / root, rcond=None)[0]
            x = Q[:, :m] @ c
            r = d - x + B(x)
            center = (S * x) @ (d + r)
            radius = ((np.linalg.norm(r / root) + eps(T) / np.sqrt(delta))**2
                      + 2 * eps(T) * np.linalg.norm(x))
            print(f"  {m=} C={center:.12g} rho={radius:.6g}")
            assert abs(center - ref) <= radius + ref_err + 5e-13
            if m == 32 and q == p:
                ratio = (abs(center) + radius) / min(lower)
                limit = (0.027 if T == 8 else 0.17) if tau == 0.01 else 0.1
                print(f"  signed bound / unsigned lower bound = {ratio:.6g}")
                assert ratio < limit
            if m == 32 and q != p:
                assert center - radius > 0.2


for q, p in ((9413, 9413), (97**2, 97), (37253, 37253), (193**2, 193),
             (153649, 153649), (389**2, 389)):
    replay(q, p, 0.01)
for q, p in ((153649, 153649), (389**2, 389)):
    replay(q, p, 0.0005)
PY
```
