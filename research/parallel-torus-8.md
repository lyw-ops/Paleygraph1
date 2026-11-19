# Squaring the two cyclic Paley kernels

This follows the two torus models in [additive-neighbor-compression.md](additive-neighbor-compression.md) for [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/). Squaring the cyclic kernel gives an exact transfer to squared, twisted two-point correlations of its symbol. It gives uniform bounds for frequency-restricted vectors and for the mean gain over translated vectors. The positive square-order control shows exactly where these bounds stop: its coherent vector has critical size in both torus coordinates, even though the symbol obeys the same complete character-sum estimates, with the same constants. A uniform prime-field gap remains open.

## Notation and endpoint bookkeeping

Use the split group $G_+=((\mathbb F_q^\times)^2,\cdot)$ of even order $(q-1)/2$ and the nonsplit group $G_-=\{t^2:t^{q+1}=1\}$ of odd order $(q+1)/2$, for $q\equiv1\bmod4$. Use $s=s_\sigma$ from the earlier note. In cyclic additive coordinates $G_\sigma=\mathbb Z/m\mathbb Z$, put $e(x)=\exp(2\pi i x/m)$ and

$$ K_{x,y}=\frac{s(x-y)s(x+y)}{2\sqrt q}. $$

Here $s$ is real and even, $s(0)=0$, and $s^2=1$ away from zero. Write $P$ for deletion of the inversion-fixed endpoints (both $0,m/2$ for the split group; just $0$ for the nonsplit group). Then $PKP$ on inversion-even functions is the signed additive compression $B_\sigma=\sigma T_{C_\sigma,C_\sigma}$, with all other directions having eigenvalue zero if the deleted coordinates are retained. We use the full $K$ for the transfer. It is a contraction: on its even subspace, it is the signed additive compression to the image of $z\mapsto(z+z^{-1}+2)/4$, multiplied on both sides by the diagonal weights $\sqrt{\#\text{fiber}/2}$. On the odd subspace it is zero. This follows by pulling back normalized fiber indicators, and the additive operator is a contraction by its quadratic-character correlation. The difference $K-PKP$ has rank at most $2\operatorname{rank}(I-P)\le4$. For any fixed power its normalized trace effect is $O(m^{-1})$, by telescoping, bounding the trace norm of the difference by its rank times its operator norm. Endpoint deletion is not a small-norm approximation.

## A uniform bound for twisted translate correlations

For either symbol, any $j\ge1$, any distinct shifts $a_1,\ldots,a_j$ in its torus, and any character $h$ of the torus,

$$ \left|\sum_{z\in G_\sigma} h(z)\prod_{i=1}^j s_\sigma(a_i z)\right|\le j\sqrt q. \tag{1} $$

In the split case, extend $h$ to $\mathbb F_q^\times$ and use the projector $(1+\chi)/2$. The sum is half the sum of two rank-one character sums with the two extensions of $h$. Work on the projective line with $0,\infty$ and the $j$ distinct roots $a_i^{-1}$ removed. The local system is tame, and quadratic inertia at each of these $j$ roots makes it geometrically nontrivial; the extension of $h$ has no ramification there. Thus $H_c^0=H_c^2=0$, the tame Euler characteristic gives $\dim H_c^1=j$, and the weight bound gives $j\sqrt q$ for each of the two sums.

In the nonsplit case, average over the two preimages $t$ of $z=t^2$ in the full norm-one torus. If $b_i^2=a_i$, then

$$ s_-(a_i t^2)=\chi\!\left(\frac{b_i t-(b_i t)^{-1}}{\sqrt d}\right). $$

The choice of square root does not affect the character since $\chi(-1)=1$. The function in the character is defined over $\mathbb F_q$: conjugation in $\mathbb F_{q^2}/\mathbb F_q$ inverts the norm-one coordinate and changes the sign of $\sqrt d$. On the geometric projective line it has two simple zeros $t=\pm b_i^{-1}$, and poles only at the two boundary points of the torus, denoted $0,\infty$ in a split coordinate. The zero pairs are disjoint for distinct $a_i$. The twist $h(t^2)$ has a rank-one Lang local system, tame at the two boundary points (geometrically the Lang cover has degree $q+1$) and lisse on the torus. The product is tame on the line minus $2+2j$ points and geometrically nontrivial by its local inertia at a simple zero. Thus $\dim H_c^1=2j$ and the complete sum is at most $2j\sqrt q$ before dividing by two. At a removed zero the original summand is zero in both proofs. The inputs here are the [Lang character construction and Euler characteristic formula, §§1.2–1.3](https://www.math.uchicago.edu/~ngo/PCMI.pdf), and [Deligne's weight bound](https://numdam.org/articles/10.1007/BF02684780/). In particular (1) holds with no prime-field hypothesis and with explicit dependence on $j$, including when $j$ grows with $q$.

## Exact transfer for the square and fourth moment

For a cyclic offset $a$, set $g_a(u)=s(u+a)s(u)$ and use the unnormalized Mellin sum $G_a(c)=\sum_u g_a(u)e(-cu)$. Expanding over the intermediate vertex and using evenness gives

$$
4q(K^2)_{x+a,x}
=\sum_y g_a(x-y)g_a(x+y)
=(g_a*g_a)(2x),
$$

where convolution uses counting measure. This works even when doubling is not injective. Define the Fourier transform of a diagonal of $K^2$ by $W(a,b)=\sum_x (K^2)_{x+a,x}e(-bx)$. Fourier inversion of the convolution yields

$$ W(a,b)=\frac1{4q}\sum_{2c=b}G_a(c)^2. \tag{2} $$

The nonsplit group has one term. In the split group, odd $b$ gives zero and $b=2c$ gives two terms, from $c$ and $c+m/2$. Since $g_a(-a-u)=g_a(u)$, $G_a(c)^2=e(ac)|G_a(c)|^2$. Thus after the common phase is removed the two terms add for even $a$ and subtract for odd $a$. In particular, (1) gives $|W(a,b)|\le 1$ for every $a\ne0$ in the nonsplit case, and $\le 2$ in the split case (also $\le1$ for odd $a$). The exceptional diagonal uses $G_0(c)=m\mathbf1_{c=0}-1$. Directly, $(K^2)_{x,x}=(m-2+\mathbf1_{2x=0})/(4q)$: among the intermediate vertices, only $y=x,-x$ are excluded.

By Parseval, the exact fourth moment is

$$ \operatorname{tr}K^4=\frac1m\sum_{a,b}|W(a,b)|^2
=\frac1{16q^2m}\sum_{a,b}\left|\sum_{2c=b}G_a(c)^2\right|^2. \tag{3} $$

In the nonsplit case the last sum is simply $\sum_{a,c}|G_a(c)|^4$. The split case needs the mixed term between the two lifts; single-character fourth moments alone do not recover it.

The higher moments also have a cyclic transfer. Let $D_{a,b}f(x+a)=e(bx)f(x)$. These matrices are orthogonal in the Hilbert–Schmidt inner product, each has squared norm $m$, and $K^2=\sum_{a,b}w(a,b)D_{a,b}$ with $w=W/m$. Multiplying two basis elements uses $D_{a,b}D_{u,v}=e(bu)D_{a+u,b+v}$. Hence $\operatorname{tr}K^{2j}=m(w^{\star j})(0,0)$, where $\star$ sums over offsets that add to the target, with the displayed phase. The bound on each $W(a,b)$ does not control this repeated sum: it leaves products over many offsets and their phases. This is where a high-moment argument would need new cancellation.

## Two uniform bounds on restricted tests

Write $S(h)=\sum_x s(x)e(-hx)$. Then $|S(h)|\le\sqrt q$ by (1), and $\sum_h |S(h)|^2=m(m-1)$. In the unitary cyclic Fourier basis the formula from the earlier note reads

$$ (FKF^*)_{\ell h}=\frac1{2m\sqrt q}\sum_{2b=\ell-h}S(b+h)S(b). $$

Consequently the absolute entry bound is $1/(2\sqrt q)$ in the nonsplit case and $1/\sqrt q$ in the split case. For a unit vector supported on $L$ Fourier coordinates, this bounds the absolute Rayleigh quotient by $L/(2\sqrt q)$ or $L/\sqrt q$, respectively. In the split case $L$ can be replaced by the maximum number of selected coordinates in either parity, since the matrix has no entries between opposite parities. In positional coordinates the bound is $L/(2\sqrt q)$ for both signs. This gives a uniform gap for all vectors in any support smaller than the corresponding critical size by a fixed factor. The estimate also excludes near-edge unit vectors with $1-o(1)$ of their squared norm on such a support, by projecting onto the support and using $\|K\|\le1$ to bound the Rayleigh error by $o(1)$. The bounds apply to the actual compression when its vectors are embedded with their endpoint values zero.

There is a different bound even for dense vectors if one averages over the torus translates. For the unit Fourier vector $v_h$, summing the squares of its output coefficients gives

$$ \|K v_h\|^2\le \begin{cases}
(m-1)/(4m),&\sigma=-,\\
(m-1)/(2m),&\sigma=+.
\end{cases} \tag{4} $$

Indeed, sum $|S(b+h)S(b)|^2/(4m^2q)$ over $b$, using the cap on $S(b+h)$. In the split case Cauchy–Schwarz across up to two terms costs a factor of two. For $\tau_a f(x)=f(x-a)$, averaging $\|K\tau_a f\|^2$ over $a$ cancels cross terms between distinct Fourier coordinates. Thus (4) also bounds this mean divided by $\|f\|^2$. Likewise averaging over modulations $f(x)\mapsto e(bx)f(x)$ leaves only the positional diagonal of $K^2$, with upper bound $(m-1)/(4q)$. These averages control the proportion of translates or modulations with large gain. They do not control the gain of the original vector at the prescribed anchor.

## The coherent square-order packet in both bases

Take $q=r^2$, $r\ge5$ odd, in the split group, and let $H_1=\mathbb F_r^\times$ and $H_2=\{z\in\mathbb F_{r^2}^\times:z^{r+1}=1\}$. Both lie in $G_+$, their intersection is $\{1,-1\}$, and they generate $G_+$. In multiplicative coordinates the exact set over the subfield is

$$ x(z)\in\mathbb F_r \quad\Longleftrightarrow\quad z^r\in\{z,z^{-1}\}\quad\Longleftrightarrow\quad z\in H_1\cup H_2. $$

The first equivalence follows from the two roots of $X^2-(4x(z)-2)X+1$. The kernel equals $1/(2r)$ on this union except for pairs $z=w^{\pm1}$, where it is zero. This is also visible at the level of the symbol: $s=1$ on $H_1\setminus\{1\}$, while on $H_2\setminus\{1\}$,

$$ s(z)=(-z^{-1})^{(r+1)/2}, $$

a constant times the quadratic character of $H_2$. For pairs across the two subgroups, Frobenius sends $z/w$ to $zw$ when $z\in H_1$ and $w\in H_2$, so the two symbol factors agree. Within each subgroup the factors multiply to $+1$ unless one vanishes.

Three consequences make the obstruction quantitative.

- The unit indicator $f$ of $(H_1\cup H_2)\setminus\{1,-1\}$ has $2r-4$ positional coordinates, and $2r-6$ positive entries in each row on this support. Thus $\langle f,Kf\rangle=(r-3)/r$ in the actual punctured compression. This nearly saturates the positional bound.
- For the unpunctured transfer let $u=\mathbf1_{H_1}+\mathbf1_{H_2}$. Its Fourier support is contained in $A=H_1^\perp\cup H_2^\perp$, of size $r-1$, all of the same parity. Its Rayleigh quotient is $(r-1)/(r+2)$: $\|u\|^2=2r+4$, $\sum_z u(z)=2r$, and the deleted diagonal/inverse pairs have total weight $4r$. This nearly saturates the split Fourier bound. Moreover, the punctured indicator equals $u-2\mathbf1_{\{1,-1\}}$, before normalizing. Its Fourier mass outside $A$ is exactly $4(r-3)/((r-2)(r+1))$: the transform of $\mathbf1_{\{1,-1\}}$ has squared entry $4/m$ on every even frequency, and there are $m/2-(r-1)$ such frequencies outside $A$. Thus the actual witness concentrates on the critical scale in both bases.
- The symbol satisfies (1) for all distinct shift families, including families of logarithmic size, and all twists, at these same square orders. Therefore bounds based only on this field-uniform square-root cancellation and the transfer identities, with the same hypotheses on the group and endpoints, cannot prove a uniform split gap. The mixed phases or an additional prime-field input must exclude coherent packets. This argument does not construct a near-one vector in the nonsplit case.

## A log-depth moment target

Let $\rho=\sqrt3/2$, the predicted rescaled bulk edge from [Kunisky's degree-two conjecture](https://arxiv.org/html/2303.16475#S1.SS4). The earlier note explains how the conjectured least adjacency eigenvalue, together with control of the constant direction, would imply a signed gap. A different sufficient target is to prove, through primes, a bound

$$ \operatorname{tr}\left[T_k(B_\sigma/\rho)^2\right]\le C p,\qquad
k=\lceil c\log p\rceil,\qquad c>1/\log 3, \tag{5} $$

with $T_k$ the Chebyshev polynomial of the first kind and $C$ independent of $p$. A bound of the same form for the full $K$ also suffices, by compression. This is a two-sided sufficient condition, and does not assume that the actual signed edge is already known. For $\beta_\sigma>\rho$, its individual positive contribution is at least $\frac14\exp(2k\,\operatorname{arcosh}(\beta_\sigma/\rho))$. Thus (5) would give

$$ \limsup_{p\to\infty}\beta_\sigma\le
\rho\cosh(1/(2c))<1,\qquad \operatorname{arcosh}(1/\rho)=\log\sqrt3. $$

The same square-order positive witness forces the trace in (5) with $q$ in place of $p$ to be at least $q^{c\log 3-o(1)}/4$, so (5) fails on that family at the needed depth. Fixed normalized moments cannot rule out a single outlier, and a bound $O(p)$ for a Chebyshev square at depth $o(\log p)$ has the same limitation. The exact transfer (2)–(3) identifies what can be computed at low degree. For the log-depth target the remaining issue is cancellation across different offsets in the twisted products, with enough arithmetic information to distinguish primes from the square control. Even such a gap would only feed the bounds on concentrated near-endpoint profiles in the earlier note; it would leave the diffuse case of Problem 26.

## Checks

An in-memory check used both tori at $p=13,17,41,101,257$ and the positive torus at $q=5^2,7^2,11^2,17^2,23^2$. The positional factorization at the primes, the convolution identity on every cyclic diagonal, and the square packet's entry pattern were checked in exact integer arithmetic. The cyclic Fourier and fourth-moment formulas, the column bounds, and both square-order Rayleigh quotients and the Fourier leakage were also checked numerically (maximum normalized transform discrepancy below $1.4\cdot10^{-16}$). The twisted power trace was checked through $K^8$ on one even and one odd cyclic order. These checks verify identities and normalizations; they give no spectral upper bound from samples.
