# Reflecting the rooted Jacobi endpoint

For Problem 26, the rooted Jacobi condition has a second consequence after the positional change of variable $x\mapsto 1-cx$. A nearly saturated feasible spectrum forces the reflected profile to have large **multiplicative energy**. Over a prime field this rules out a signed near-minimum support covered by a bounded number of frequency cosets, at relative size slack $o((\log p)^{-2})$. Even without assuming a cover, in that size range the actual stationary high set has additive energy at most $(1/2+o(1))|S|^3$. The argument does not exclude low-energy supports, or all supports with the qualitative slack $o(1)$.

## The additive operator sees the root

Let $p\equiv1\pmod4$ be prime, $Q=(\mathbb F_p^\times)^2$, $G=\widehat Q$, $n=|Q|$, and $m_0=n/\sqrt p$. Use $s(x)=\chi(1-x)$ on $Q$ and $k(h)=p^{-1/2}\sum_{x\in Q}s(x)h(x)$ as in [the half-angle note](parallel-half-arithmetic-5.md). On all of $\mathbb F_p$ set

$$
 (Tf)(x)=p^{-1/2}\sum_y\chi(x-y)f(y).
$$

The elementary quadratic character correlation gives $T=T^*$ and $T^2=I-p^{-1}\mathbf1\mathbf1^*$, so $I\pm T$ are positive semidefinite with norm at most two. On $Q$, the compression of $T$ is diagonal in the *multiplicative* Fourier basis, with eigenvalues $k(h)$. Indeed, in its action on $h(x)$ one substitutes $y=xu$ and uses $\chi(x)=1$. Consequently, if $f(x)=\sum_h w_h h(x)$ on $Q$, extended by zero, then

$$
 \langle f,(I-\sigma T)f\rangle=n\sum_h |w_h|^2(1-\sigma k(h)).       \tag{1}
$$

For the actual stationary probability $\mu=\mu_\sigma$, let $w=\mu$ and put $\delta_0=\sum_h\mu_h(1-\sigma k(h))$. The rooted stationary identity is

$$\delta_0=1+p^{-1/2}-m_0\mu_0.$$

The point cap $\mu_h\le L=(1+\sqrt p)/n$ then gives $\langle f,(I-\sigma T)f\rangle\le nL\delta_0$. Along a near-minimum stationary sequence from the half-angle note, $\|f\|_2^2=n\|\mu\|_2^2\asymp\sqrt p$ and $\delta_0=o(1)$, so this is a small relative error. The same implication holds for any feasible probability with $\|\mu\|_2^2\asymp m_0^{-1}$ and small rooted defect.

Choose $c\ne0$ with $\chi(c)=\sigma$, and set $Rf(x)=f(1-cx)$ and $g=\mathbf1_Q Rf$. The permutation $R$ satisfies $TR=\sigma RT$ by changing variables in the additive kernel. For feasible $f$, the condition $f(y)=0$ when $y\in Q\setminus\{1\}$ and $s(y)\ne\sigma$ gives **exactly** $Rf-g=\mathbf1_{\{0\}}$. Thus the triangle inequality in the seminorm for $I-T$ gives

$$
 \frac{\langle g,(I-T)g\rangle}{\|g\|_2^2}\ll\delta_0+p^{-1/2},\qquad
 \|g\|_2^2=\|f\|_2^2-1.                                          \tag{2}
$$

The output sign in (2) is positive for both input signs, because of the nonsquare dilation in the negative case. This distinction is needed: the reflection by itself does not send a negative feasible profile into $Q$.

## The reflected fourth moment

For a function $g$ on $Q$ define its multiplicative energy by

$$
 \mathcal E_\times(g)=\sum_{a\in Q}\left|\sum_{x\in Q}g(x)\overline{g(ax)}\right|^2
 =n\sum_{h\in G}|\widehat g(h)|^4,                               \tag{3}
$$

where $\widehat g$ is the unitary multiplicative Fourier transform. Let $\eta$ be an upper bound, sufficiently small, on $\langle g,(I-T)g\rangle/\|g\|_2^2$. By (1), at least $3/4$ of the squared Fourier norm lies on $\{h:1-k(h)\le4\eta\}$. Its size is $O(p(\sqrt\eta+p^{-1/4}))$ by the [one-cap bound](critical-sets.md#repeated-differences-are-necessary) from [Xi, Theorem 1.1](https://arxiv.org/abs/1809.04286), using $1-k^2\le2(1-k)$ on this cap. Cauchy–Schwarz in (3) now yields

$$
 \mathcal E_\times(g)\gg \frac{\|g\|_2^4}{\sqrt\eta+p^{-1/4}}.       \tag{4}
$$

In particular an arbitrary actual near-minimum stationary spectrum, without any frequency cover hypothesis, must satisfy $\mathcal E_\times(g)\gg p/(\sqrt{\delta_0}+p^{-1/4})$. The energy is of the complex profile itself, so replacing it by the energy of its absolute value only weakens the necessary condition. This is a constraint on the reflected positional profile, rather than a lower bound on the number of large original positional phases.

## A prime gap for bounded coset covers

There is a version of (4) that uses only the *within-set* signed endpoint, and therefore avoids a floor loss. For a nonempty set $U\subseteq G$ of size $m\asymp m_0$, write

$$
 d_\sigma(U)=m^{-2}\sum_{i,j\in U}(1-\sigma k(j-i)),\qquad
 \epsilon_U=d_\sigma(U)+|m/m_0-1|+p^{-1/2}.
$$

Choose an anchor $i_0\in U$ whose average signed deficit is at most $d_\sigma(U)$ and use $f(x)=m^{-1}\sum_{j\in U}(j-i_0)(x)$ on $Q$, zero elsewhere. Translating the mask to this anchor does not change its positional modulus. Now $\|f\|_2^2=n/m$ and (1) bounds the additive form by $d_\sigma(U)\|f\|_2^2$. The other defect, for positional multiplication by $s$, is exactly

$$
 v=1-\frac{\sum_{x\in Q}\sigma s(x)|f(x)|^2}{\|f\|_2^2}
   =1-\frac m{m_0}(1-d_\sigma(U))\ge0.                            \tag{5}
$$

With the same $R$ and $g$ as before, $f(1)=1$ gives $\|Rf-g\|_2^2=(v\|f\|_2^2+1)/2$: the discarded mass consists of the identity and the wrong sign. Thus $\|g\|_2^2\asymp\sqrt p$ for small $\epsilon_U$, and $\langle g,(I-T)g\rangle/\|g\|_2^2\ll\epsilon_U$. No exact feasibility of the mask is needed.

Suppose $U$ is a union of at most $r$ cosets of a common frequency subgroup $H$, with $r$ fixed. Then $f$ is supported on $B=H^\perp$ and $|f|\le1$. Its reflected profile is supported inside $c^{-1}(1-B)\setminus\{0\}$, with the additional restriction to $Q$. Expanding (3) with absolute values bounds it by the unweighted multiplicative energy of $(1-B)\setminus\{0\}$ in $\mathbb F_p^\times$. Here $|B|\asymp_r\sqrt p$. [Macourt–Shkredov–Shparlinski, Corollary 4.1](https://doi.org/10.4153/CJM-2017-044-2) bounds the shifted-subgroup energy by $O(|B|^4/p+|B|^2\log |B|)=O_r(p\log p)$ in this size range. Removing zero does not increase the count of product equalities. Combining with (4) proves, for all sufficiently large primes,

$$\boxed{\quad d_\sigma(U)+|m/m_0-1|+p^{-1/2}\gg_r(\log p)^{-2}.\quad} \tag{6}
$$

The implicit constant may also depend on the comparison bounds on $m/m_0$. Large $\epsilon_U$ already satisfies (6); in the small case the proof gives $\sqrt{\epsilon_U}+p^{-1/4}\gg_r(\log p)^{-1}$. The energy bound here is the prime-field input. The derivation does not use an exclusion for each finite phase rank or the order of a displacement in $G/H$. On signed flat supports it gives a wider size window than the one furnished by the explicit lower bound on $\Delta_p$ in the [bounded-deficit coset argument](signed-coset-bands.md#a-union-of-frequency-cosets). The fixed-rank mass gaps in [the finite-phase note](critical-coset-phases.md) still reach qualitative slack for the ranks tested there.

In particular, if $m=m_0+o(m_0/(\log p)^2)$, the signed Rayleigh quotient of the **uniform** unit vector on $U$ is at most $1-c_r/(\log p)^2$ for a constant $c_r>0$, by (5)–(6). This is a test of that vector, not a bound on the full compression norm.

The common subgroup hypothesis can be relaxed for a disjoint union $U=\bigsqcup_{j=1}^r U_j$ of cosets, provided each $|U_j|\asymp m_0$ uniformly and $r$ stays bounded. Indeed the anchored flat profile is the sum of the profiles from the individual cosets. Each summand is supported on the annihilator of its own frequency subgroup and has pointwise modulus at most $|U_j|/m\le1$. After reflection and clipping, the shifted-subgroup estimate applies to each summand $g_j$. The fourth-moment identity (3) and the triangle inequality in $\ell_4$ give $\mathcal E_\times(\sum_j g_j)^{1/4}\le \sum_j\mathcal E_\times(g_j)^{1/4}\ll_r (p\log p)^{1/4}$. This proves the same (6) for that type of cover. The size assumption on the individual cosets keeps each positional annihilator of order at most a constant times $\sqrt p$.

Equation (6) also holds, with an additional error $O(|S\triangle U|/|S|)$ on its left, for a set $S$ compared to such a union $U$: uniform probabilities change in $\ell_1$ by at most $2|S\triangle U|/|S|$, and the kernel deficit is bounded by two. Alternatively, for feasible probabilities with $\|\mu\|_2^2\asymp m_0^{-1}$, (2)–(4) rule out $\delta_0=o((\log p)^{-2})$ if $\mu$ is $o(1)$ in $\ell_1$ from a uniform critical coset union. Indeed, point caps on both spectra turn this into $o(\sqrt p)$ squared positional error, preserved or decreased by reflection and clipping. The mask's clipped profile must then carry a positive fraction of $\sqrt p$ on the same Fourier cap as $g$, which contradicts the shifted-subgroup bound by (3). This last version does not require a logarithmic rate for the mass approximation; it pays the rate in the rooted defect instead.

## Consequence for the actual high set

Fix a half-angle threshold $0\le\rho<1$ and let $S=S_\sigma$ be the bulk high set of the exact stationary pair. Suppose its stationary mass stays bounded below (in particular, take $\tau\to0$). If

$$ |S|\le m_0+o\big(m_0/(\log p)^2\big),                         \tag{7} $$

the [signed quadratic form and flatness estimates (8)–(9)](parallel-half-arithmetic-5.md#which-jacobi-endpoint-information-survives-at-each-size) give $m=|S|\ge m_0-O_\rho(1)$ and $d_\sigma(S)=o((\log p)^{-2})$. Hence (6) excludes a bounded coset cover even with $o(m_0/(\log p)^2)$ errors. The same conclusion about energy needs no cover assumption:

$$ E(S)=\sum_h |S\cap(S+h)|^2\le(1/2+o(1))m^3.                  \tag{8} $$

For the rounding step, write $d=d_\sigma(S)$, $\delta=1-(m/m_0)(1-d)\ge0$, and $r_h=|S\cap(S+h)|/m$. The uniform unit vector $u$ on $S+h$ satisfies $\|Ku-\sigma u\|_2\le\sqrt{2\delta}$. Sum $\sigma Ku$ over $S\setminus(S+h)$. In the unnormalized sum of $\sigma k(j-i)$, the columns in the overlap contribute at least $r_h(1-r_h)m^2-m^2d$, by the within-$S$ deficit. The other columns contribute at least $-(1-r_h)^2m^2$. Divide by $m_0\sqrt m$ and use the Cauchy–Schwarz upper bound on the sum of $\sigma Ku$ to get

$$ (m/m_0)\big((2r_h-1)(1-r_h)-d\big)\le\sqrt{2\delta(1-r_h)}. $$

For each fixed $a>1/2$, this shows $1-r_h=O_a(d+\delta)$ when $r_h>a$. As in [translation rounding](signed-coset-bands.md#turning-overlap-into-a-coset-cover-at-the-required-precision), those shifts form a subgroup for sufficiently large $p$, and rounding the coset densities changes $O_a(m(d+\delta))=o(m/(\log p)^2)$ entries. The energy bound $E(S)/m^3\le a+(1-a)|H|/m$ for this subgroup $H$ follows by summing $r_h^2\le a r_h$ off $H$ and $r_h^2\le r_h$ on $H$. If the energy ratio exceeded $1/2$ by a fixed amount, choose $a$ closer to $1/2$; then $|H|\gg m$, so the rounded union would contain only a bounded number of cosets. This contradicts (6) and proves (8).

## Checks and remaining gap

At square order $q=r_0^2$, the uniform spectrum on the subfield annihilator has $f=\mathbf1_{\mathbb F_{r_0}^\times}$ and rooted defect $2/r_0$. The positive reflection with $c=1$ gives $g=\mathbf1_{\mathbb F_{r_0}^\times\setminus\{1\}}$. With $b=r_0-1$, its energy is $(b-1)^2+(b-1)(b-2)^2\asymp b^3$: for nonidentity ratios one deletes two distinct points of the subgroup. This satisfies (4) and shows why the shifted-subgroup estimate cannot be used in this square control.

Direct dense calculations at twelve primes from 13 through 257 checked 130 signed coset masks. The additive diagonal form, the affine intertwining identity, the clipping cost, (5), and the Fourier fourth moment agreed with their direct sums within $1.9\cdot10^{-12}$ in absolute error. Exact cyclic counts also checked the square energy formula at 98 subgroup sizes. These checks test normalizations and signs; the bounds use the cited arithmetic estimates.

The size window (7) is much wider than the one in [the six-anchor estimate](parallel-five-4.md), but the upper energy bound (8) is compatible with its lower overlap bound even in their common range. Neither result forces a phase clique for a general low-energy support. In particular this does not rule out the limit $\sigma m_B\to1/3$ for an unrestricted near-minimum stationary sequence and does not settle the theta asymptotic.
