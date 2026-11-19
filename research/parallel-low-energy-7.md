# A prime support bound for the affine Paley cone

For [Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), a feasible spectrum at prime order needs at least $(1-o(1))\sqrt n$ nonzero frequencies, where $n=(p-1)/2$. This includes the affine cone that allows a nonzero positional value at the identity. The bound is larger by a factor tending to $\sqrt2$ than the critical scale $m_0=n/\sqrt p$. It applies to arbitrary supports, including the low additive energy sets left by [the reflected energy test](parallel-extreme-6.md) and the [six-anchor test](parallel-five-4.md). No coset cover or finite phase classification is needed. For the true stationary pair it excludes a near-minimum high set when the floor is sufficiently small as a function of $p$. The quantitative bound below does not reach polynomially small floors.

## A missing interval and an affine rank bound

Let $p\equiv1\pmod4$ be prime, $Q=(\mathbb F_p^\times)^2$, $s(x)=\chi(1-x)$, and $D_\sigma=\{x\in Q:s(x)=\sigma\}$. Identify $G=\widehat Q$ with $\mathbb Z/n\mathbb Z$ using a generator $\beta$ of $Q$. Denote a primitive complex $n$th root by $\zeta$. For $u\in\mathbb C^G$ define $f_u(\beta^j)=\sum_i u_i\zeta^{ij}$. Here the affine condition of sign $\sigma$ means $f_u=0$ on $D_{-\sigma}$; $f_u(1)=\sum_i u_i$ need not vanish. A feasible probability is a nonnegative mass-one vector satisfying this condition.

Let $I$ have size $m$ and miss an interval of length $L\ge1$ in a generator direction of $G$. The dimension of the space of vectors supported on $I$ satisfying the affine condition is bounded by

$$\boxed{\dim\{u:\operatorname{supp}u\subseteq I,\ f_u|_{D_{-\sigma}}=0\}\le (m-L+1)_+.} \tag{1}$$

This differs from the [homogeneous rank test](rank-partitions.md#exact-localization-through-prime-orders) by the extra allowed value at $1$. The correction comes from taking differences between consecutive missing coefficients. Translation of $I$ multiplies each positional row by a nonzero scalar. Dilation of $I$ by a unit acts on the evaluation matrix by a cyclotomic Galois automorphism, which preserves rank. We can therefore put the gap at $0,\ldots,L-1$ with step one.

Reduce the forbidden-position evaluation matrix over $\mathbb F_p$ by $\zeta\mapsto\beta$. Reduction cannot increase rank, since a minor nonzero after reduction is nonzero before reduction. For a vector in the reduced kernel, put $F(X)=\sum_{i\in I}u_i X^i$ over $\mathbb F_p$. Euler's criterion at the roots of $X^n-1$ gives

$$((1-X)^n-\sigma)F(X)\equiv-\frac{\sigma F(1)}n(1+X+\cdots+X^{n-1})\pmod{X^n-1}. \tag{2}$$

Indeed the left side vanishes at every square other than $1$: either $s(x)=\sigma$ or $F(x)=0$. At $1$ its value is $-\sigma F(1)$, as on the right. All $n$ roots are distinct. At a gap index $j$, the coefficient on the left is $\sum_{i\in I}(-1)^{i-j}\binom n{i-j}u_i$, since $i>j$, reducing the product uses exponent $n+j$, and $n$ is even. It is constant in $j$ by (2). Subtract the coefficient at $j+1$ and use Pascal's identity to obtain

$$\sum_{i\in I}(-1)^i\binom{n+1}{i-j}u_i=0,\qquad 0\le j\le L-2. \tag{3}$$

Write $a=\min(m,L-1)$ and $N=n+1$. For $a\ge1$, take the first $a$ rows in (3) and any $a$ columns. Divide column $i$ by $(-1)^i\binom Ni$ and multiply by $\prod_{h=1}^{a-1}(N-i+h)$. All scalars are nonzero modulo $p$: $N<p$, and the factors are positive and less than $p$. The rows now evaluate the degree-at-most-$a-1$ polynomials

$$T_j(t)=t(t-1)\cdots(t-j+1)\prod_{h=j+1}^{a-1}(N-t+h),\qquad 0\le j<a.$$

Their evaluations at $0,\ldots,a-1$ are triangular with nonzero diagonal. In particular the positive factors on the diagonal are bounded by $N+a-1<p$, since $a\le n-1$. They form a basis and evaluation at the distinct selected column indices is invertible. This proves (1), including the trivial case $a=0$.

The $m$ cyclic gaps of a nonempty set contain $n-m$ outside points. If $n>m(m+1)$, one gap has length at least $m+1$. Thus **every nonzero affine spectrum of either sign** at prime order has support size satisfying $m(m+1)\ge n$. This also bounds the support of every zero-floor optimizer; positivity, evenness, and optimality were not used in the rank argument. The conclusion is about exact support and does not follow from the homogeneous rank bound, which requires $F(1)=0$.

## Quantitative exterior mass and the true stationary high set

Let $W_\sigma$ denote the unnormalized evaluation matrix with rows $j$ such that $\beta^j\in D_{-\sigma}$ and all frequency columns. The projector onto this positional sector in frequency coordinates is

$$P_{-\sigma}=n^{-1}W_\sigma^*W_\sigma=(I-\sigma K-J)/2,$$

where $J=\mathbf1\mathbf1^{\mathsf T}/n$ and $K$ is the Jacobi multiplier. Write $d=[\mathbb Q(\zeta+\zeta^{-1}):\mathbb Q]=\varphi(n)/2$ for $n>2$. Suppose $I$ has a gap of length at least $m+1$. Then (1) makes $P_{-\sigma,II}$ positive definite. The entries of $nP_{-\sigma,II}$ are algebraic integers in the real cyclotomic field: the forbidden set is inversion invariant. Under each Galois conjugation the principal block is that for a unit dilation of $I$, so all the conjugated eigenvalues of $P_{-\sigma,II}$ are in $[0,1]$. The nonzero integer norm of $\det(nP_{-\sigma,II})$ has modulus at least one. Each of the other $d-1$ factors is at most $n^m$. It follows that

$$\lambda_{\min}(P_{-\sigma,II})\ \ge\ \det P_{-\sigma,II}\ \ge\ n^{-md}. \tag{4}$$

For every affine spectrum $u$, projection of $u_I$ cancels that of $u_{I^c}$. Applying (4) and the projector contraction gives

$$\|u_{I^c}\|_2^2\ge n^{-md}\|u_I\|_2^2. \tag{5}$$

There is also a signed deficit test for a flat mask, even if it is not feasible. With $d_\sigma(I)=m^{-2}\sum_{i,j\in I}(1-\sigma k(j-i))$ and $k=m_0 K_{0,\cdot}$, testing (4) on $\mathbf1_I/\sqrt m$ gives $1-(m/m_0)(1-d_\sigma(I))\ge m/n+2n^{-md}$. The term $m/n$ is present over square fields too; (4) quantifies the additional strictness at primes.

For the [true stationary pair](parallel-half-arithmetic-5.md#notation-and-identities-for-the-actual-pair), use weights $w_0=1$, $w_i=\tau/n$ for $i\ne0$, $W=\sum_i w_i$ and $\mu_\sigma=A_\sigma/\sqrt{nW}$. Fix $0\le\rho<1$ and let $I$ be the stripped half-angle set $\{i\ne0:\sigma B_i>\rho\}$ together with the mark. Put $R=(1+\rho)/(1-\rho)$. Off $I$ one has $A_{\sigma,i}\le R\sqrt{\tau/n}$. Hence

$$\|\mu_{\sigma,I^c}\|_2^2\le\frac{R^2\tau}{nW},\qquad \mu_\sigma(I)\ge1-R\sqrt{\tau/W}.$$

If $I$ misses an interval of length $m+1$, (5) and Cauchy–Schwarz imply

$$\frac{R^2\tau}{nW}\ge \frac{n^{-md}}{m}\big(1-R\sqrt{\tau/W}\big)_+^2. \tag{6}$$

In particular for any integer $M\ge1$ with $M(M+1)<n$, both signs have at least $M$ **bulk** high coordinates whenever

$$0<\tau<\min\left\{\frac1{4R^2},\ \frac{n}{4R^2M}\,n^{-Md}\right\}.$$

Otherwise $m\le M$, the gap exists by averaging and (6) contradicts the floor bound. Taking $M$ maximal gives $M\sim\sqrt n\sim\sqrt2m_0$. For example, $\tau_p=\exp(-p^2)$ meets this condition eventually at every fixed $\rho$. This excludes the low-energy near-minimum *true* high set in this floor regime, without an assumption about the mass of its discarded part beyond the actual threshold cap. It also proves an order-by-order exclusion for all sufficiently small floors. The cyclotomic norm does not yield a useful lower bound on the tail at fixed or polynomially small floors: it allows a spectrum to spread over many more frequencies than the high set with weights too small for the other tests to see. The result consequently does not remove the near-minimum scenario in those regimes or bound the limiting theta ratio.

## Square control and exact arithmetic checks

Over $q=r^2$, the annihilator $H=(\mathbb F_r^\times)^\perp$ has size $b=(r+1)/2\sim m_0$. The spectrum $\mathbf1_H/b$ is feasible for the plus sign because its positional profile is $\mathbf1_{\mathbb F_r^\times}$. In cyclic frequency order the spacing is $r-1$, so it misses a gap of length $r-2\ge b+1$ for $r\ge7$. This violates (1) and (5) if those statements are carried over to squares. In (3), $n+1$ now exceeds the characteristic. The divisions by $\binom{n+1}{i}$ and the polynomial basis proof are no longer justified. The shifted support $H-1$ gives the following checks, with the rank of the first $b$ Pascal rows computed over $\mathbb F_r$:

| $r$ | $n$ | $b$ | Gap | Extra modes $h\notin H$ with $\lambda_h=r$ | Pascal rank |
|---:|---:|---:|---:|---:|---:|
| 7 | 24 | 4 | 5 | 2 | 3 |
| 11 | 60 | 6 | 9 | 4 | 5 |
| 13 | 84 | 7 | 11 | 0 | 6 |
| 29 | 420 | 15 | 27 | 0 | 14 |
| 37 | 684 | 19 | 35 | 0 | 18 |

The last three rows also give exact comparisons for the **true** stationary high set. The [square minus witness](square-order-control.md#a-square-order-comparison) in mean-one frequency normalization has $L_-(0)=b$, zeros on $H\setminus\{0\}$, and $L_-(h)=(r-\lambda_h)/(r+1)$ otherwise. The cyclotomic check gives $\delta=\min_{h\notin H} L_-(h)>0$ in those rows. Complementary supports yield $\langle L_-,\mu_+\rangle=1$ and $\sum_{h\in H}A_{-,h}=b\sqrt{W/n}$, using $\mathbf1_H/b$ for the second identity. Since $A_{+,0}A_{-,0}=1$, these give $1/(bW)\le\mu_+(0)\le1/b$, and then

$$\mu_+(H^c)\le\frac{W-1}{W\delta},\qquad
\sum_{h\in H\setminus\{0\}}A_{-,h}\le\frac{b(W-1)}{\sqrt{nW}}.$$

At each of these fixed square orders, $A_+$ is $O_r(\tau)$ off $H$ and $A_-$ is $O_r(\tau)$ on $H\setminus\{0\}$. The same bulk reciprocal relation gives $B_i\to1$ on $H\setminus\{0\}$ and $B_i\to-1$ off $H$. The true plus high set including the mark is therefore exactly $H$ for sufficiently small positive floors. This check uses integer arithmetic and the stationary identities, and makes no assertion that the minus witness is strictly positive off $H$ at every square order. The infinite family of exact feasible subfield spectra needs no such strictness.

To replay the saturation column, compute the remainder of $\sum_j s_j X^{hj\bmod n}$ modulo $\Phi_n(X)$; the Fourier value equals $r$ exactly when this remainder is the constant $r$. The following uses the existing square sign generator.

~~~python
from flint import fmpz_poly
from square_control import square_field_sign

for r in (7, 11, 13, 29, 37):
    s = list(map(int, square_field_sign(r)))
    n = len(s)
    phi = fmpz_poly.cyclotomic(n)
    hits = set()
    for h in range(1, n):
        coeff = [0] * n
        for j, v in enumerate(s):
            coeff[h*j % n] += v
        if fmpz_poly(coeff) % phi == r:
            hits.add(h)
    H = set(range(r-1, n, r-1))
    assert H <= hits
    print(r, len(hits-H))
~~~

As a separate prime check, exact elimination verified the Pascal matrix rank in (3) and the evaluation-matrix rank bound for both signs on 4,920 gap/support pairs: exhaustive up to size $\lfloor\sqrt n\rfloor+2$ in gaps $L\ge2$ at $p=13,17,29$, and 100 samples (seed 2607) at each of $41,73,101,173,257,401,521$. Of the full-column-rank cases with $m\ge3$, 430 had $E(I)\le m^3/2$. These checks exercise gap endpoints and low-energy masks. The mathematical obstruction is the paired coefficient identity (3) and the nonvanishing of the indicated minors in prime characteristic.
