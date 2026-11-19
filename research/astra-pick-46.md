# What finite real Pick tests can detect on the physical marked curve

There is no uniform bound on the number of real interpolation nodes needed to detect a branch point, even in degree two with the exact sector bound and hot decay. The obstruction works against *all choices* of nodes up to any prescribed growing budget. On the actual square Paley family a different conclusion holds: one explicit linear combination of hot marks and one cold mark detects failure of the whole right-half-plane section with a fixed positive margin for every sufficiently large square. Both results below are ordinary proofs. No new field computation, interval certificate, or all-prime estimate is claimed.

## A common measure budget for two half-plane Pick functions

Write $W_n(t)=1+(1-1/n)t$ and $m(t)$ for the physical plus mark. On the whole right half-plane use $t=T\sqrt\xi$ with $T=2048$ and the principal square root. On a Cayley disk $|b|<h<1$, $b=(t-c)/(t+c)$, use instead
\[
 u=b/h,\qquad t(\xi)=c\frac{(1+h)\sqrt\xi+(1-h)}{(1-h)\sqrt\xi+(1+h)} .
\]
In both cases the upper half $t$-domain maps to the upper $\xi$-half-plane. Put $L_n(\xi)=\log W_n(t(\xi))$, $M(\xi)=m(t(\xi))$, and $K_x(s)=1/(1+s)-1/(x+s)$. Define the explicit positive measure $d\nu_n(s)=\pi^{-1}\arg W_n(t(-s+i0))\,ds$ for $s>0$. For the whole right half-plane its density is $\pi^{-1}\arctan((1-1/n)T\sqrt s)$.

A physical marked section exists on the proposed domain exactly when for every finite set $x_i>0$ and real $v_i$,
\[
 \left|\sum_i v_i[M(x_i)-M(1)]\right|
 \le \tfrac12\int_0^\infty \left|\sum_i v_i K_{x_i}(s)\right|\,d\nu_n(s). \tag{1}
\]
Here $M(x_i)$ only uses real stationary solutions. Real rational coefficients and a prescribed dense set of positive nodes suffice. The kernel differences are integrable even on the whole half-plane.

Indeed $H_\pm=L_n/2\pm M$ have nonnegative imaginary parts by the [physical sector theorem](parallel-cold-complex-36.md), and their sum is $L_n$. Both imaginary parts are bounded and vanish on the positive boundary. A bounded harmonic function on the half-plane is the Poisson integral of its bounded boundary values, by the disk Poisson formula and the conformal map. There is no singular boundary or linear term. The boundary values for $\Im M$ therefore have the form $\eta(s)\arg W_n(t(-s+i0))$, $|\eta|\le1/2$. The Poisson kernel is the imaginary part of $-1/(\xi+s)$ up to its factor $1/\pi$. Matching the real constant at 1 gives
\[
 M(\xi)-M(1)=\int K_\xi(s)\eta(s)\,d\nu_n(s),\qquad
 L_n(\xi)-L_n(1)=\int K_\xi(s)\,d\nu_n(s). \tag{2}
\]
Conversely (1) gives a well-defined functional of norm at most $1/2$ on the span of the $K_{x_i}$ in $L^1(\nu_n)$. Real Hahn–Banach and $L^1$ duality give $\eta$. Its integral (2) is holomorphic off the nonpositive axis and matches the real mark by density and continuity. Reflection and composition with $\xi(t)$ give the physical section. The analytic graph lifts to the normalized marked curve as in [round 45](astra-strip-45.md). This proves (1), with no tests on coordinatewise stationary jets.

### A field-first use with local disks

Fix finitely many physical Cayley disks covering the real path from $a$ to $T$, in a chain with open real overlaps and the last meeting the hot interval. Suppose for every disk and **each fixed rational test** (1) the limsup through eligible primes of left minus right is at most zero. Then $m_p(a)\to0$, even if the individual marked algebraic curves have ramification inside the disks. Indeed on a fixed compact positive interval the real marks are equicontinuous and bounded: $|d m/d\log t|\le1/2$ by real stationary leverage, and the mark is bounded at $T$ by the hot theorem. Exhaust the positive axis by compact intervals and extract a locally uniform subsequential real limit. The densities in (1) converge pointwise to those with $W=1+t$ and are dominated by $1/2$, so every limit satisfies (1). The preceding extension argument glues holomorphic limits along the real overlaps, and they vanish on the hot interval. The identity theorem forces their values at $a$ to be zero. This applies to every subsequence. Applying it at a sequence $a\downarrow0$ would give ETH26 by the stationary bracket. This implication does not produce the required prime estimates. It avoids the stronger requirement of a section on each individual field.

## One explicit extrapolation inequality for the actual square control

In the whole right half-plane put $d=(a/T)^2$, $0<a<1$. Choose any $J\ge1$ distinct hot nodes $d<x_i<1$ with $T\sqrt{x_i}>1024$. There are explicit real coefficients $c_i$ satisfying, under (1),
\[
 \left|M(d)-M(1)-\sum_{i=1}^J c_i(M(x_i)-M(1))\right|
 \le \frac{L_n(1)-L_n(d)}{2\,T_J((1+d)/(1-d))}
 \le [L_n(1)-L_n(d)]\left(\frac{T-a}{T+a}\right)^J . \tag{3}
\]
Here $T_J$ is the Chebyshev polynomial. Thus the conclusion uses just values, including when the hot points coalesce extremely closely but stay distinct.

For the coefficients set $z=1/(1+s)$, $z_*=1/(1-d)$, $D(z)=\prod_i(1-(1-x_i)z)$ and
\[
 R(z)=\frac{T_J(2z-1)D(z_*)}{T_J(2z_*-1)D(z)}.
\]
For $0\le z\le1$, $0<D(z_*)\le D(z)$. Also $R(z_*)=1$. The kernel $K_d=(d-1)z^2/(1-(1-d)z)$ times $1-R$ is therefore $z^2$ times a rational function with denominator $D$ and numerator of degree at most $J-1$. Its unique partial-fraction expansion is $\sum c_iK_{x_i}$, since $K_{x_i}=(x_i-1)z^2/(1-(1-x_i)z)$. The residual is $K_dR$ and has absolute value at most $|K_d|/T_J(2z_*-1)$. Its integral bound in (3) follows from (2), or directly from (1), because $K_d$ has one sign. Finally $T_J((1+d)/(1-d))=(r^{-J}+r^J)/2$, $r=(1-\sqrt d)/(1+\sqrt d)$. For example the nodes $x_i=1-i/[4(J+1)]$ are rational and all hot.

Set $a=1/2$, $J=12000$, and use those nodes. For every sufficiently large square order, the left side of (3) exceeds its first upper bound by more than $0.04$. The [actual square bracket](astra-complex-39.md) gives $m_q(1/2)>\tfrac14\log(4/3)>0.07$ eventually. All hot marks tend uniformly to zero, and these finitely many coefficients are fixed. The right side of (3) is at most $8(4095/4097)^{12000}<0.024$, using $\log W_n(T)<8$. This is one predetermined real functional on the actual stationary solutions. An initial segment of the square sequence is not specified. The large, potentially ill-conditioned coefficients make this a theoretical square control, not a recommendation for floating evaluation. The whole-half-plane test alone does not exclude a narrower tube.

## Every test through any prescribed rank can miss an actual branch

Fix $a\in(0,1)$, $T=2048$, $c=\sqrt{aT}$, $s=(T-c)/(T+c)$, and any $s<h<1$. This single Cayley disk contains both real endpoints. Let $N_n$ be **any** prescribed sequence of positive integers. The following algebraic comparison has all the following properties simultaneously.

* Its scalar mark satisfies the physical phase bound on the entire normalized right-half-plane cover, and tends uniformly to zero there. In particular all real cold marks and the hot supremum tend to zero.
* The degree-two marked cover ramifies at $b=\pm i e^{-n}$ inside the chosen disk, and its physical lifted cold-to-hot distance is $2\log n+O_a(1)$.
* On this same disk every ordinary real Pick test and both upper-half-disk Loewner tests from [round 45](astra-strip-45.md) pass at every selection of at most $N_n$ distinct real nodes. The two Loewner tests include the actual first derivatives. More general Hermite interpolation works for any prescribed finite total multiplicity after increasing the derivative budget.

Use the [degree-two neck](astra-surface-38.md) $w^2=b^2+\epsilon^2$, $z=b+w$, $y=\epsilon^2/z=w-b$, $\epsilon=e^{-n}$, physical $w>0$ on the real diameter. For each $n$ choose $\kappa_n>0$ small and set $F=1+\kappa_n y$, $m=\log F$. The coordinate $F$ generates the same quadratic function field since $w=b+(F-1)/\kappa_n$. Neither normalization nor monodromy changes upon rescaling. The round-38 calculation, $|y|<3$, $|\Im y|\le2|\Im b|$ and $|\sin\arg W_n|\ge c|\Im b|/[4(1+c)]$ on the cover, gives the exact sector bound for sufficiently small $\kappa_n$ independent of $n$. Taking also $\kappa_n\le1/(10n)$ makes $|\log F|=O(1/n)$ everywhere. The annulus distance established there is $2\log\log(1/\epsilon)+O_a(1)$, giving the assertion. The cover is algebraic in its exponentiated mark, as for the physical stationary problem.

For the uniform interpolation assertion use $u=b/h$ on the real closed diameter $[-1,1]$. Let $\ell_n(u)=\log W_n(t(u))$. In the upper half disk,
\[
 \Im \ell_n(u)\ge \frac{\Im W_n(t(u))}{|W_n(t(u))|}
 \ge C\Im u,\qquad
 C=\frac{ch}{(1+h)^2[1+c(1+h)/(1-h)]}>0 .
\]
This uses $1-1/n\ge1/2$. For each fixed $n$ the branch on the closed real diameter is smooth and $m\to0$ in every fixed $C^k$ norm there as $\kappa_n\downarrow0$. Put $k=2N_n-1$. We can consequently choose the positive $\kappa_n$ so that
\[
 \max_{0\le j\le k}\frac{\|m^{(j)}\|_{[-1,1]}}{j!}
 <\frac{C}{4(1+\sum_{j=1}^k j2^{j-1})}.
\]
Derivatives here are in $u$. At any choice of up to $N_n$ nodes use their doubles in the Newton–Hermite interpolant $P$. Each order-$j$ divided difference is bounded by $\|m^{(j)}\|/j!$ by real Rolle interpolation, including confluent nodes. For $|u|<1$ every Newton product's derivative has modulus at most $j2^{j-1}$. Hence $\sup|P'|<C/4$. Its coefficients are real and integration vertically gives $|\Im P(u)|\le(C/4)\Im u$ on the upper half disk. Thus $\ell_n/2\pm P$ are Pick after the half-disk coordinate change, with the exact marked values and derivatives at all selected nodes. Their Loewner matrices are positive semidefinite. The same angular bound and reflection make $\tanh(\pi P/(2\phi))$ a disk self-map for the actual sector width $\phi$ of this Cayley disk, hence the ordinary Pick matrices are positive semidefinite as well. The interpolating polynomial may depend on the nodes. There is no physical section over this disk, since a nonzero affine function of $w$ has nontrivial ramification there.

This is a strict obstruction to recovering geometric access from a truncated real Pick hierarchy, even if all its node positions can be chosen adaptively, all real cold marks are small, and the degree is known. The example is not a Paley stationary family. It leaves the actual prime geometry and ETH26 open.

The [exact-rational checker](astra-pick-46-check.py) verifies the partial-fraction identities at orders 1, 2, 5 and 10 after clearing denominators and checks the constants for the order-12000 inequality. Run `.venv/bin/python -B research/astra-pick-46-check.py` to reproduce [five arithmetic records](astra-pick-46-checks.jsonl). These records contain no sampled Paley marks.

## Ranked next tests

1. On a fixed chain of small disks, bound the signed real tests (1) for every fixed rational stencil in the prime limit. The explicit measure budget is independent of unobserved complex roots and has a known limit. A fixed stencil with strictly positive limiting excess along a prime subsequence refutes this condition on that disk. A finite-field obstruction with excess tending to zero does not.
2. If finite-field geometric access is pursued, derive an arithmetic lower bound on the detectable amplitude of a reachable prime branch from the complementary Fourier stationary equations. A bound on the number of nodes or on the degree alone cannot do this. A prime subsequence with accessible ramification and uniformly vanishing excess in all stencils up to the proposed quantitative budget would refute a positive-margin detection theorem for that budget.
