# Compression gaps on higher-rank frequency progressions

Let $q\equiv1\pmod4$ be an odd field order, $n=(q-1)/2$, $m_0=n/\sqrt q$, and let $K$ be the [Paley convolution operator](progression-gap.md) on the frequency group $\widehat Q$. Write $\lambda=Fs$, so $K_{ij}=\lambda_{i-j}/n$ and $|\lambda_h|\le\sqrt q$. Consider boxes of fixed rank $d$,

$$I=a+\left\{\sum_{j=1}^d k_j d_j:0\le k_j<M_j\right\},\qquad M=\prod_j M_j\le Bm_0.$$

Assume the displayed parameterization is injective, all $M_j\to\infty$, and $\ell/M\ge(128d)^d$, where $\ell=|\langle d_1,\ldots,d_d\rangle|$. Then $\limsup_{q\to\infty}\|K_{II}\|<1$. It follows that the same gap holds on every subset of $I$. The condition on the subgroup order permits short relations among the steps. It also permits boxes with a growing number of separated intervals and volumes a fixed factor above the critical size.

## A peak and its rescaled relation lattice

Suppose along a subsequence there is a unit vector $y$ on $I$ with Rayleigh quotient tending to $\sigma\in\{1,-1\}$. Remove the translate $a$. Put $r_y(h)=\sum_i\overline{y_i}y_{i+h}$, extending $y$ by zero. The entry bound gives

$$\sum_h |r_y(h)|\ge(1-o(1))m_0,\qquad
\sum_h |r_y(h)|^2\gg_{B,d}m_0,$$

since $I-I$ has at most $2^d M$ elements. Define

$$Y(\theta)=\sum_{\mathbf k}y_{\mathbf k}e^{2\pi i\mathbf k\cdot\theta},\qquad
e^{2\pi i\Theta_j(x)}=d_j(x)\quad (x\in Q).$$

Finite Fourier orthogonality gives $n^{-1}\sum_x|Y(\Theta(x))|^2=1$ and $n^{-1}\sum_x|Y(\Theta(x))|^4=\sum_h|r_y(h)|^2$. There is consequently an $x_0\in Q$ with $|Y(\Theta(x_0))|\gg_{B,d}\sqrt M$. The rescaled polynomials

$$F_q(z)=M^{-1/2}Y\left(\Theta(x_0)+(z_j/M_j)_j\right)$$

are uniformly bounded on compact subsets of $\mathbb C^d$: Cauchy–Schwarz gives $|F_q(z)|\le\exp(2\pi\sum_j|\operatorname{Im}z_j|)$. Pass to a locally uniform entire limit $F$ with $F(0)\ne0$.

Let

$$\Lambda_q=\{(k_j/M_j)_j:\mathbf k\in\mathbb Z^d,\ \sum_j k_j d_j=0\}.$$

The lattice has covolume $\ell/M$. Injectivity of the box implies that distinct lattice points have $\ell_\infty$ distance at least one. Pass to a subsequence on which the lattices converge locally to a discrete subgroup $\Lambda\subset\mathbb R^d$. This can be done by local compactness and separation on each bounded region followed by a diagonal subsequence. Limits of sums and differences remain in the limit set. The separation also gives uniform polynomial counting bounds, so sums of Schwartz functions over the lattices converge. If $\Lambda$ has full rank, approximate its basis by vectors of $\Lambda_q$. For large orders, the resulting independent vectors have determinant at least $\ell/M$. Thus $\operatorname{covol}(\Lambda)\ge(128d)^d$. In particular, when $\ell/M\to\infty$ the rank must be less than $d$.

## The local sampling measure and the sign bias

Place weight $M/n$ at each rescaled positional point $(M_j(\Theta_j(x)-\Theta_j(x_0)))_j$, allowing period translates by the $M_j$ in each coordinate. Call the resulting locally finite measure $\mu_q$. For $g\in C_c^\infty(\mathbb R^d)$, periodize $g((M_j u_j)_j)$ on the torus. Its coefficient at $\mathbf k$ is $M^{-1}\widehat g((k_j/M_j)_j)$. Averaging over $Q$ kills every coefficient except the relations, so

$$\int g\,d\mu_q=\sum_{\xi\in\Lambda_q}\widehat g(\xi)\ \longrightarrow\
\sum_{\xi\in\Lambda}\widehat g(\xi).$$

Let $W=\operatorname{span}_{\mathbb R}\Lambda$, $V=W^\perp$, and $\Lambda^\#\subset W$ be the dual lattice inside $W$. Poisson summation on $W$ identifies the limiting measure as

$$\mu=\frac{1}{\operatorname{covol}_W(\Lambda)}
\sum_{w\in\Lambda^\#}\operatorname{Leb}_{V+w}.$$

For $\Lambda=\{0\}$ this is ordinary Lebesgue measure. When the rank is less than $d$, the limit has a continuous direction even though it may be concentrated on affine planes. At full rank it is a lattice sampling measure. Local limits for continuous compactly supported tests follow by smooth approximation and the local mass bound from a nonnegative smooth majorant.

Let $\omega_q$ be the signed measure formed by multiplying each point of $\mu_q$ arising from $x$ by $s(x)$. The Rayleigh deficit is

$$\frac1n\sum_{x\in Q}(1-\sigma s(x))|Y(\Theta(x))|^2=o(1).$$

On each fixed compact rescaled region, the contribution from the periodic lifts is at most a bounded multiple of this deficit. Thus $\int |F_q|^2\,d(\mu_q-\sigma\omega_q)$ tends to zero locally. For any nonnegative smooth test $g$, separate the region with $|F|>\epsilon$. Uniform convergence and the Rayleigh deficit control that region. Bound the remaining region by $2\mu_q$ and pass to the limit using a continuous amplitude cutoff. Sending $\epsilon\downarrow0$ gives

$$\liminf_q\sigma\int g\,d\omega_q\ \ge\ \int g\,d\mu-2\int_{\{F=0\}}g\,d\mu.$$

When $\dim V>0$, the restriction of $F$ to $V$ is real analytic and nonzero at the origin, so its zero set there has Lebesgue measure zero. For a test supported in a tube around $V$ that misses the other planes this gives

$$\int g\,d\omega_q\ \longrightarrow\ \sigma\int g\,d\mu.$$

## The contradiction from a long tube

Choose orthonormal coordinates on $V$ and $W$. On $V$ let $g_T$ be the product of $\dim V$ copies of $h_T=\mathbf1_{[-T,T]}*\zeta$, where $\zeta$ is a fixed nonnegative smooth probability supported on $[-1,1]$. In the transverse directions multiply by a fixed smooth bump with values in $[0,1]$, equal to one at zero and supported close enough to miss the other planes. This gives a nonnegative smooth compact test on $\mathbb R^d$. Then

$$\int g_T\,d\mu=\frac{(2T)^{\dim V}}{\operatorname{covol}_W(\Lambda)}.$$

The Fourier bound on $s$ gives, for fixed $T$,

$$\left|\int g_T\,d\omega_q\right|
\le\frac{\sqrt q}{n}\sum_{\mathbf k\in\mathbb Z^d}
\left|\widehat g_T((k_j/M_j)_j)\right|.$$

All $M_j$ tend to infinity, so the sum divided by $M$ converges to $\|\widehat g_T\|_1$ by Riemann sums for a Schwartz function. Rotation preserves that integral. The one-dimensional bound $|\widehat h_T(\xi)|\le\min(2T,1/(\pi|\xi|))|\widehat\zeta(\xi)|$ gives $\|\widehat h_T\|_1=O(1+\log T)$. Hence the last display has limit superior at most a constant times $(1+\log T)^{\dim V}$, where the constant depends only on $B$, the fixed transverse bump and $\zeta$. Its limit in absolute value is a positive constant times $T^{\dim V}$. Taking $T$ arbitrarily large yields the contradiction.

### Full rank with a fine sampling direction

When $\Lambda$ has full rank, the dual lattice $\Lambda^\#$ has covolume at most $(128d)^{-d}$. It contains a nonzero vector of length at most $2\sqrt d\,\operatorname{covol}(\Lambda^\#)^{1/d}$. A cube of side $2\operatorname{covol}(\Lambda^\#)^{1/d}$ has volume greater than the covolume, so two of its points are congruent modulo the lattice. Take a shortest vector $w$, which is primitive and satisfies $\|w\|\le1/(64\sqrt d)$. The line $\mathbb Rw$ meets the lattice exactly at the integer multiples of $w$. The orthogonal projections of all other lattice points to $w^\perp$ have positive distance from zero uniformly, since a primitive vector extends to a lattice basis and the projected remaining basis is independent.

Use the same tube test with $h_T$ along the unit direction $w/\|w\|$ and a transverse bump missing every other lattice line. Its mass on $\mu$ is at least $(2(T-1)/\|w\|-1)/\operatorname{covol}(\Lambda)$ since $h_T=1$ on $[-T+1,T-1]$. The entire restriction $F(z w/\|w\|)$ has bound $\exp(2\pi\sqrt d\,|\operatorname{Im}z|)$ and is nonzero at zero. Jensen's formula at radius $2(T+1)$ gives at most $4\pi\sqrt d\,(T+1)/\log 2+O_F(1)$ zeros in the disk of radius $T+1$. As $0\le g_T\le1$, the contribution lost to zeros in the sign lower bound is at most twice this count divided by $\operatorname{covol}(\Lambda)$. The upper bound on $\|w\|$ leaves a positive linear term in $T$. The Fourier estimate for this tube is $O(1+\log T)$, again a contradiction.

## Consequences for critical stationary supports

The [signed stationary comparison](signed-coset-bands.md#transfer-from-one-sign-of-the-diagonal) now excludes a near-zero band whenever the high set of its sign is contained in these boxes and its one-sided exterior bound is fixed. Rank two includes separated packets with additive energy of order $4M^3/9$ when the differences are injectively parameterized, which is below the previous $M^3/2$ overlap threshold. This argument applies to prime and extension fields. The [square subfield support](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy) has $\ell/M=1$. Its unit lattice spacing permits the concentration that the fine sampling hypothesis excludes.

The hypothesis is a cover of the relevant set. An energy bound may produce a structured subset while leaving the larger support and its Rayleigh quotient unaccounted for. Establishing a suitable cover for the actual high sets remains open.

The [coset-progression extension](coset-progression-gap.md) treats progression covers with subgroup fibers and bounded side lengths. For density-one primes it excludes every critical-size support with bounded doubling.

## Numerical comparison

The [box probe](../progression_boxes.py) compares an interval with two rank-two boxes whose first step generates the full cyclic group. The second steps are $\lfloor n/(M_2+1)\rfloor$ for the folded box and $\lfloor n/(\sqrt 2(M_2+1))\rfloor$ for the other box. It also records the square subfield compression. At $p=1000033$, the $23$ by $22$ box with the second step $15372$ has energy $0.445324\,M^3$ and compression norm $0.0850002$. The folded box at the same size has a scaled relation of length $23/22$ and norm $0.0867171$. At $997^2$ the two box norms are $0.0961346$ and $0.0982525$, and the subfield norm is $0.998996$. These are the compression values for the specified supports, from the [28 recorded rows](../data/progression-boxes.csv).

A Gaussian periodization check at the same eight field orders compared the direct positional average with the sum over the scaled relation lattice, with maximum absolute discrepancy below $3\cdot10^{-16}$.
