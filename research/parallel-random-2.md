# Random restriction at the second update and a one-cost test of the optimum

Let $w$ be a deterministic mass profile $(m_j)_{j=1}^k$, $\sum_j m_j=1$, placed at a uniform ordered injection $(I_j)_{j=1}^k$ in the frequency group. Write $S=\{I_j\}$, $r_2=\sum_j m_j^2$, and use the normalization $F=F_+-F_-$ from the [rank expansion](random-weight-ranks.md). Two results separate a sparse cancellation that can be proved directly from a test of the actual optimum:

- At every fixed positive floor, the **second Picard update** has expected signed log test $O_\tau(\sqrt{k/n}+\sqrt{r_2})$. For the [harmonic profile](parallel-sparse.md), this is $O_\tau(n^{-1/8})$ at $k=\lfloor n^{3/4}\rfloor$. The proof uses the random locations, without a finite-field character moment theorem.
- At the **undamped optimum**, one prescribed linear cost per sign bounds the signed log value, even at zero floor. This gives a rationally checked example $-0.133<B_2<-0.113$ at $p=101$ for the harmonic masses. It gives a sufficient test for $B_k\to0$ at growing sparse orders; that test is unproved asymptotically.

## Leave one mark out of the second update

Assume a real symmetric $K$ satisfies $K\mathbf 1=0$, $K^2=I-J$, where $J=\mathbf1\mathbf1^{\mathsf T}/n$, and $\max_{il}|K_{il}|\le M/\sqrt n$. These hold with a common $M$ at prime and square orders by the Jacobi bound. Use ordinary Euclidean norms and put

$$w^\tau=w+\tau\mathbf1/n,\qquad v_0=0,\qquad v_{t+1}=\alpha K\sqrt{v_t^2+4w^\tau},\qquad L_t=2\sum_i w_i\operatorname{arsinh}\frac{v_{t,i}}{2\sqrt{w_i^\tau}}.$$

For $1\le k\le n/2$, $\tau>0$, $0\le\alpha\le1$, and constants depending only on $M,\tau$, we have

$$\mathbb E\|v_{1,S}\|_2^2\le C_M k/n,\qquad
\mathbb E\|v_{2,S}\|_2^2+|\mathbb E L_2|\le C_{M,\tau}\big(\sqrt{k/n}+\sqrt{r_2}\big).\tag{1}$$

Thus $\mathbb E|L_2|\le C_{M,\tau}[(k/n)^{1/4}+r_2^{1/4}]$. For harmonic masses $r_2\le 2/k$: Jensen bounds the sum of the squared expected exponential order statistics by the expected sum of the squared order statistics, namely $2k$. The same order holds for any profile with $\max m_j=O(1/k)$.

Set $x_j=\sqrt{m_j+\tau/n}-\sqrt{\tau/n}$ and $d_j=2\alpha x_j$. Then $v_1=\sum_j d_j K e_{I_j}$, $\sum_j d_j^2\le4$, and $\sum_j |d_j|^3\le8\sqrt{r_2}$. For a label $j$, let $v^- = v_1-d_j K e_{I_j}$. Conditional on all the other slots, $v^-$ is fixed with norm at most two and $i=I_j$ is uniform on the unused coordinates. Hence $\mathbb E |v^-_i|^2\le4/(n-k+1)$. The self term adds at most $|d_j|M/\sqrt n$ in absolute value. Summing squared bounds gives the first estimate of (1).

Write $\phi(s)=\sqrt{s^2+4\tau/n}$. At marked $i=I_j$, the extra activation from mass $m_j$ has value $2x_j$ at $v_{1,i}=0$, and its difference from that value is at most $|v_{1,i}|$. Indeed the extra activation is the difference of two square roots and its derivative lies in $[-1,1]$. Thus $v_2=v_1+\alpha K\phi(v_1)+\alpha K e$ with $e$ supported on $S$ and $\|e\|_2\le\|v_{1,S}\|_2$. By $\|K\|\le1$, the first and third terms contribute $O(k/n)$ to the expected squared marked norm, and $O(\sqrt{k/n})$ to the absolute expected linear log test.

For the middle term, Taylor expansion at the deleted input gives, at $i=I_j$,

$$ (K\phi(v_1))_i=Y_j+d_j A_i+R_i,\qquad Y_j=(K\phi(v^-))_i,\qquad A_i=\sum_l K_{il}^2\phi'(v^-_l).$$

Here $\mathbb E Y_j^2\le4/(n-k+1)$ by the same held-out sampling bound, since $K\mathbf1=0$ and $\phi$ is 1-Lipschitz. Also $|R_i|\le C_{M,\tau} d_j^2$: use $\|\phi''\|_\infty\le\sqrt n/(2\sqrt\tau)$ and $\sum_l |K_{il}|^3\le M/\sqrt n$. It remains to control $A_i$, which tests the odd derivative $\phi'$ against squared entries of a row.

### The two-row estimate

Condition instead on $I_j=i$. For two distinct rows $l,b$, the vector $(\sqrt n v^-_l,\sqrt n v^-_b)$ is a deterministically weighted sample without replacement from the population

$$Z(y)=\sqrt n(K_{ly},K_{by}),\qquad y\ne i,$$

with coefficients $d_a$ for $a\ne j$. Its population mean is $O_M(n^{-1})$ and its covariance is $I_2+O_M(n^{-1})$ in operator norm. Indeed the full-population mean is zero; the full covariance is the corresponding principal minor of $I-J$, and exclusion removes a single uniformly bounded vector. The same statements hold for a single row.

Here is the finite-population comparison used for this test. Center a bounded population of size $N=n-1$ and couple iid draws $J_a$ to ordered draws $T_a$ without replacement. At step $a$, take $T_a=J_a$ if the latter is unused; otherwise draw uniformly from the unused population. Each $T_a$ is uniform on the unused population given the past. The conditional mean of $Z(T_a)-Z(J_a)$ is $-\sum_{h<a} Z(T_h)/(N-a+1)$ and its conditional second moment is $O_M(a/N)$. For weights of squared sum at most four, the weighted martingale differences therefore have squared norm in expectation $O_M(k/n)$. The weighted sum of the conditional means has $L^2$ norm $O_M(k/n)$: the centered sample sum of $a-1$ draws has $L^2$ norm $O_M(\sqrt{a-1})$ by the finite-population covariance formula, and Cauchy–Schwarz applies to $\sum_a |d_a|\sqrt{a-1}$. The resulting weighted-sum comparison costs $O_M(\sqrt{k/n})$ in expectation against any fixed Lipschitz test in one or two dimensions.

For the iid draws, replace each centered weighted summand by an independent centered Gaussian with matching covariance. Taylor expansion through degree two against a test with bounded third derivatives costs $O_M(\sum_{a\ne j}|d_a|^3)$ times the derivative bound; the first two orders agree and both third absolute moments are bounded times $|d_a|^3$. The factor $I+O_M(1/n)$ in the final covariance can be replaced by identity at cost $O_M(1/n)$ for a Lipschitz test, using the same Gaussian in both models. The omitted mean costs $O_M(\sqrt k/n)$. This argument also covers zero total variance by taking a degenerate Gaussian.

Let $\psi(s)=s/\sqrt{s^2+4\tau}$, so $\phi'(v^-_l)=\psi(\sqrt n v^-_l)$. The tests $\psi(s)$ and $\psi(s)\psi(t)$ are smooth with bounded derivatives through order three at fixed $\tau$. Their Gaussian comparison has expectation zero by oddness in a centered Gaussian coordinate and independence of the two coordinates in the product test. Consequently each conditional mean $\mathbb E[\phi'(v^-_l)\mid I_j=i]$ and each off-diagonal expectation $\mathbb E[\phi'(v^-_l)\phi'(v^-_b)\mid I_j=i]$ is bounded in absolute value by

$$ E_{n,k}=C_{M,\tau}\big(\sqrt{k/n}+\sqrt{r_2}\big).$$

The bound is uniform in $i,j,l,b$. Since $\sum_l K_{il}^2\le1$ and $\sum_l K_{il}^4\le M^2/n$, it gives $|\mathbb E A_i|\le E_{n,k}$ and $\mathbb E A_i^2\le E_{n,k}+M^2/n$ under the same conditioning. This proves the squared norm bound in (1) on summing the Taylor terms, using $\sum_j d_j^4\le16r_2$.

To get the sharper signed rate, replace $L_2$ by $\sum_{i\in S}(w_i/\sqrt{w_i^\tau})v_{2,i}$. The error in expectation is $O(\mathbb E\|v_{2,S}\|_2^2)$ by $|\operatorname{arsinh}x-x|\le C x^2$. The coefficient at $i=I_j$ is at most $\sqrt{m_j}$. The terms $Y_j$ then cost $O(\sqrt{k/n})$, and the linear terms $d_j A_i$ cost $O(E_{n,k})$ since $\sum_j\sqrt{m_j}|d_j|\le2$. The remainders cost $O_{M,\tau}(\sum_j m_j^{3/2})=O_{M,\tau}(\sqrt{r_2})$. This proves (1).

### What still needs an exterior estimate

For $\alpha=1$ let $v_*$ be the stationary solution at floor $\tau/n$, $u_s=\sqrt{v_s^2+4w^\tau}$ and $\gamma_s=\operatorname{arsinh}(v_s/(2\sqrt{w^\tau}))$, including $s=*$. As in [the damped comparison](poisson-smoothing.md#comparing-damped-and-undamped-fixed-points), the exact nonnegative discrepancy is

$$D=4\sum_i w_i^\tau (\cosh(\gamma_{*,i}-\gamma_{2,i})-1)
=n\overline u_*\overline u_2-4(1+\tau)+\langle v_3-v_2,v_*\rangle.$$

This uses $\langle\Pi u_*,\Pi u_2\rangle=\langle v_*,v_3\rangle$ for $\Pi=I-J$. In particular the floor error and Cauchy–Schwarz give

$$|\mathbb E F(w)|\le \log(1+\tau)+|\mathbb E L_2|+\sqrt{2\mathbb E D}.$$

The leave-one-out bound does not bound $D$. Even allowing arbitrary fixed depth is not enough at square order: the [bounded-mark damping result](sparse-damping.md) and the exact square theta give a discrepancy at one mark. A transfer at $k=\lfloor n^{3/4}\rfloor$ or another growing sparse scale needs control of the stationary residual pairing or a separate feasible witness.

For a floating-point check of the finite-depth behavior, 96 uniform injections at each listed order used the harmonic masses, $k=\operatorname{round}(n^{3/4})$, $\tau=0.1$, $\alpha=1$, and RNG seed 2617 (orders $9413,9409,37253,37249,151337,151321$ in that order). The marked score is from two FFT updates, with no stationary solve.

| Field order | $k$ | Sample mean $\|v_{2,S}\|_2^2$ | Sample mean $L_2$ | Sample mean $\lvert L_2\rvert$ |
|---:|---:|---:|---:|---:|
| 9413 | 568 | 0.37675 | $-0.00093$ | 0.02292 |
| $97^2$ | 568 | 0.38039 | $-0.00042$ | 0.02026 |
| 37253 | 1594 | 0.29121 | 0.00191 | 0.01189 |
| $193^2$ | 1594 | 0.29288 | 0.00016 | 0.01162 |
| 151337 | 4562 | 0.22114 | 0.00003 | 0.00689 |
| $389^2$ | 4562 | 0.22149 | $-0.00045$ | 0.00693 |

## A square-root cost for the exact signed optimum

For $\mathcal P_\sigma$ the mean-one feasible spectrum polytope and $h_\sigma(c)=\max_{P\in\mathcal P_\sigma}c\cdot P$, define

$$R_\sigma(w)=h_\sigma(\sqrt w)/\sqrt n.$$

There is a pointwise enclosure, also for zero weights:

$$-2\log R_-(w)\ \le\ F(w)\ \le\ 2\log R_+(w).\tag{2}$$

For each sign, Jensen bounds $\sum_i w_i\log(P_i/\sqrt{w_i})$ on the positive support by $\log\sum_i \sqrt{w_i}P_i$. Thus $F_\sigma(w)\le \frac12[\log n+\sum_i w_i\log w_i]+\log R_\sigma(w)$. Subtract the exact complementary entropy identity to obtain (2). Equivalently, the gap of the two log bounds is $2\log(R_+R_-)\ge0$. There is no optimization over the cost direction in this test.

After averaging (2), $\mathbb E R_\sigma\le1+o(1)$ for **both** signs suffices for $\mathbb E F=o(1)$ by $\log x\le x-1$. One can instead seek upper bounds $o(1)$ on both averaged log ratios directly, or certify that both their difference and the nonnegative log-product slack tend to zero. These are linear support tests with maxima over the *full* spectra, including constraints away from the marks. The test is only sufficient: cancellation of $F$ by itself does not bound the separate losses in the Jensen step.

### Two fixed masses: prime certificate and square check

For $k=2$, the harmonic masses are $(1/4,3/4)$. By translation and reversal the average in (2) only needs $h=1,\ldots,n/2$, with multiplicity two except at $n/2$. The following are floating-point comparisons against the independent [projected log intervals](poisson-smoothing.md#an-interval-for-arbitrary-marked-weights) with floor $10^{-4}$. Every individual shift interval intersected its projected log interval in this sweep, and the largest stationary residual was below $10^{-9}$.

| Field order | Averaged square-root cost enclosure | Averaged projected log enclosure |
|---:|---:|---:|
| 41 | $[-0.08020,0.05201]$ | $[-0.01924,-0.01906]$ |
| $7^2$ | $[0.05996,0.26888]$ | $[0.12466,0.12485]$ |
| 101 | $[-0.13276,-0.11398]$ | $[-0.12169,-0.12150]$ |
| $13^2$ | $[0.04821,0.31721]$ | $[0.10724,0.10744]$ |
| 401 | $[-0.03237,-0.02590]$ | $[-0.02908,-0.02888]$ |
| $19^2$ | $[0.12903,0.35009]$ | $[0.17530,0.17550]$ |

The result $-0.133<B_2<-0.113$ at $p=101$ has a rational check below. It does not use a positive floor or a rounded decision about any active constraint. For a real sine and cosine basis $A$ of $V_\sigma$, write $P=\mathbf1+Ax$. Each coefficient satisfies $|x_j|\le2$ because $P\ge0$ and $\overline P=1$. For any nonnegative vector $y$, feasibility $-Ax\le\mathbf1$ gives the exact upper bound

$$h_\sigma(c)\le\mathbf1^{\mathsf T}(c+y)+2\|A^{\mathsf T}(c+y)\|_1.$$

Use upward rational bounds for the two entries of $\sqrt w$, a rounded nonnegative dual candidate for $y$, and rational cosine intervals from [the theta verifier](../theta.py). This gives a rational upper bound $U_h$ on $h_\sigma(\sqrt w)$. An upper bound on $2\log R_\sigma$ is then obtained from the series for $\log(U_h^2/n)$ with rational remainder. The LP only proposes $y$; any values of $y\ge0$ passing the rational checks suffice.

~~~python
from fractions import Fraction
from math import lcm
from scipy.optimize import linprog
from face_ranks import spectrum_basis
from theta import cosine_intervals, paley_sign

sign = paley_sign(101)
n, s = len(sign), 10**9
t = lcm(n, 4)
c1, c2 = s // 2, 866025404
assert (2*c2)**2 > 3*s*s
lo, hi = cosine_intervals(t, s)

def coeff(j, d, i):
    a = (d-i*j*(t//n)) % t
    a = min(a, t-a)
    return lo[a], hi[a]

def log_upper(x):
    z = (x-1)/(x+1)
    return (2*sum(z**(2*i+1)/(2*i+1) for i in range(8))
            + 2*abs(z)**17/(17*(1-z*z)))

for side, target in [(1, Fraction(-113, 1000)), (-1, Fraction(133, 1000))]:
    basis = spectrum_basis(sign, side)
    columns = [(j, d) for j in range(1, n//2+1) if sign[j] == side
               for d in ((0,) if 2*j == n else (0, t//4))]
    total = Fraction(0)
    for h in range(1, n//2+1):
        cost = (c1*basis[0] + c2*basis[h])/s
        lp = linprog(-cost, A_ub=-basis, b_ub=[1]*n,
                     bounds=(-2, 2), method="highs")
        assert lp.success
        z = [max(0, round(-s*float(x))) for x in lp.ineqlin.marginals]
        z[0] += c1
        z[h] += c2
        num = sum(z)*s
        for j, d in columns:
            pair = [coeff(j, d, i) for i in range(n)]
            low, high = [sum(x*y[b] for x, y in zip(z, pair)) for b in (0, 1)]
            num += 2*max(-low, high)
        upper = Fraction(num, s*s)
        total += (1 if 2*h == n else 2)*log_upper(upper*upper/n)
    result = total/(n-1)
    assert result < target
    print(side, float(result))
~~~

For comparison with an asymptotic obstruction, the exact square single-mark value is $a_1=\log(2(r-1)/(r+1))$ at $q=r^2$. The mixture entropy bound $|F(w)-a_1|\le\mathsf H(w)$ gives $B_2\ge a_1-h(1/4)$, where $h$ is binary entropy. Moreover a fraction $((r+1)/2-1)/(n-1)$ of the nonzero shifts lie in the subfield annihilator, where $F(w)=a_1+h(1/4)$ by [the exact coset formula](sparse-mark-geometry.md#exact-coset-shifts-over-square-fields). Adding this correction gives the finite-order bound

$$B_2\ge a_1-h(1/4)+2h(1/4)\frac{(r+1)/2-1}{n-1},\qquad \liminf_{r\to\infty}B_2\ge\log 2-h(1/4)>0.1308.$$

In particular the upper square-root cost in (2) cannot have vanishing logarithmic mean there. This is a uniform-injection control on the actual optimum. For growing $k$, the [prescribed square-grid profiles](parallel-sparse.md#what-the-square-control-excludes) also have positive limiting $F$ with vanishing $K_{S,S}$ compression. Neither example yields a nonzero *growing* injection mean over squares. To prove a prime asymptotic, the remaining step is to exploit the random marks in the linear support test or the stationary pairing; the finite prime interval and the second-step estimate do not resolve that step.
