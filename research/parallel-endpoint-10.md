# Flat endpoint spectra and a marked tangent test

For [Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), a spectrum with a large mark and squared norm close to its pointwise upper bound must either lose some of that flatness under a one-sided norm penalty, or produce a forbidden positional clique. The threshold at which the penalty leaves the minimum-norm endpoint is a linear program on its tangent cone. This gives a finite prime-field test on the endpoint itself. The test concerns near-saturation of the norm cap; it does not bound every diverging endpoint norm. On prime-square orders, a classification of pure Jacobi sums proves that **every** plus optimum has squared norm of order the square root of the field order.

## A translation test with the mark retained

Use the [Fourier convention](fourier.md) with field order $q$, $G=\widehat Q$, $n=|Q|$, $j=\mathbf1/\sqrt n$, and $U_\sigma=\mathbb Rj\oplus\operatorname{ran}P_\sigma$. Work on the full real frequency space, so translations are allowed even though the unique norm selections are even. Put

\[
 \mathcal F_\sigma=\{x\in U_\sigma:x\ge0,\ \langle j,x\rangle=1\},\qquad
 \alpha=\max_{x\in\mathcal F_\sigma} x_0=\theta_\sigma/\sqrt n .
\]

Let $X$ be the least-norm maximizer of the mark, the same endpoint selected by the [reciprocal quadratic path](parallel-quadratic-support-9.md#which-endpoint-does-damping-select). For this test use the separate, **one-sided** regularization

\[
 X_t=\arg\max_{x\in\mathcal F_\sigma}\{x_0-t\|x\|^2\},\qquad t>0.
\]

Write $x=X_t$, $a=x_0$, and $\tau=t\sqrt n$. The objective is strictly concave. Its first-order inequality implies for every $z\in\mathcal F_\sigma$

\[
 x_0-t\|x\|^2-(z_0-t\|z\|^2)\ \ge\ t\|z-x\|^2.
\]

Taking $z=T_hx$, with $T_h$ the translation for which $(T_hx)_0=x_h$, gives

\[
 \boxed{\quad t\|x-T_hx\|^2\le a-x_h \quad(h\in G).\quad}                    \tag{1}
\]

In particular the mark is a maximum. Define the dimensionless norm deficit

\[
 D=1-\frac{\|x\|^2}{a\sqrt n}=\frac{\sum_i x_i(a-x_i)}{a\sqrt n}.
\]

The deficit measures the distance from a spectrum whose coordinates are all either zero or at the mark height. It differs from a Jacobi endpoint deficit and makes no assumption on the size of $a$ relative to the Jacobi entry bound.

Fix $0<\eta\le1/2$ and let $S=\{h:x_h\ge(1-\eta)a\}$. Write $L=\sqrt n/a$ and

\[
 b=1-D/\eta,\qquad \omega=\left(2\sqrt{2D/\eta}+\sqrt{\eta/\tau}\right)^2.
\]

Off $S$ the sum of the coordinates is at most $(D/\eta)\sqrt n$. Since the mark is a maximum, $bL\le |S|\le L/(1-\eta)$. Also $\|x-a\mathbf1_S\|^2\le 2a\sqrt n D/\eta$: off $S$ use $x_i^2\le a x_i$; on $S$ use $(a-x_i)^2\le[\eta/(1-\eta)] x_i(a-x_i)$. Combining the approximation with (1) gives $|S\mathbin{\triangle}(S+h)|\le L\omega$ for every $h\in S$.

If $2\omega<b$, then $H=S-S$ is a subgroup. In fact for $h\in S-S$ the triangle inequality gives $|S\mathbin{\triangle}(S+h)|\le2L\omega$, and for $h,k\in S-S$ the translates at $h-k$ still overlap since $2L\omega<|S|$. Hence $h-k\in S-S$. As $0\in S$, the subgroup contains $S$; counting all ordered pairs in $S^2$ gives

\[
 |H|(|S|-L\omega)\le |S|^2,
 \qquad |H|\le\frac{\sqrt n/a}{(1-\eta)(1-\omega/b)},
 \qquad \sum_{i\in H}x_i/\sqrt n\ge b.                                  \tag{2}
\]

If $b>1/2$, each positional element $v\in B=H^\perp$ receives a contribution of at least $b$ with phase one from $H$ in the inverse Fourier transform of $x/\sqrt n$. The rest has modulus at most $1-b$. Thus every $v\in B\setminus\{1\}$ has $s(v)=\sigma$. For any pair of distinct elements of $B$ the difference has quadratic sign $\sigma$, since $B\subset Q$. On the plus side $B\cup\{0\}$ is a Paley clique. On the minus side scaling $B$ by any nonsquare makes it a Paley clique. By [Hanson–Petridis, Theorem 1.2](https://arxiv.org/pdf/1905.09134) a prime Paley clique of size $c$ has $c(c-1)\le n$. Consequently, at prime order the observable conditions $b>1/2$ and $2\omega<b$ force

\[
 \boxed{\quad a\sqrt n(1-\eta)(1-\omega/b)+\mathbf1_{\{\sigma=+1\}}
                   \le \frac{1+\sqrt{1+4n}}2.\quad}                       \tag{3}
\]

In particular, for each fixed $\delta>0$ there is $c_\delta>0$ such that for all sufficiently large primes and every $t>0$ with $a\ge1+\delta$,

\[
 D\ge c_\delta\min\{1,t\sqrt n\}.                                        \tag{4}
\]

Otherwise take a sequence where $D/\min\{1,\tau\}\to0$. Choose $\eta=o(\min\{1,\tau\})$ with $D=o(\eta)$, so that $b\to1$, $\omega\to0$, contradicting (3). Thus a norm arbitrarily close to the point cap at a fixed multiple of the $n^{-1/2}$ scale is excluded on the imbalanced side. Indeed, comparing to $X$ gives $a\ge\alpha-t\|X\|^2\ge \alpha(1-t\sqrt n)$, so a sufficiently small fixed multiple of that scale preserves any mark gap $\alpha\ge1+2\delta$. If $X$ itself nearly saturates the point cap, then at that penalty $X_t$ must have lost a positive fraction of its squared norm: $a\le\alpha$ and (4) bound $\|X_t\|^2$ away from $\alpha\sqrt n$ by that fraction. This does not force bounded norm of $X_t$.

## The finite test on the actual endpoint

For $X$ itself, if $X_h=\alpha$, then the translate is another optimum of equal norm. The midpoint and strict convexity force $T_hX=X$. Conversely a period gives $X_h=\alpha$. So the exact maximum set of the minimum-norm optimizer is its period subgroup. In particular an exactly flat optimum selection has the form $X=\alpha\mathbf1_H$ with $|H|=\sqrt n/\alpha$, and $H^\perp$ gives the corresponding clique. On the plus side this is impossible at a prime if $\alpha\ge1$: the clique would have size $\alpha\sqrt n+1$, larger than the prime bound. For the minus side the exact necessary bound drops the extra vertex.

The following linear program extends the test to nearly flat $X$. Its feasible directions are the full one-mark tangent cone

\[
 \mathcal K_X=\{d\in U_\sigma:\langle j,d\rangle=0,\ d_i\ge0\text{ if }X_i=0\}.
\]

Each such direction is feasible for a sufficiently small positive step, so $d_0\le0$. Define

\[
 t_* = \tfrac12\inf\{-d_0:d\in\mathcal K_X,\ \langle X,d\rangle=-1\},       \tag{5}
\]

with empty infimum $+\infty$. For $t>0$, $X_t=X$ if and only if $t\le t_*$. In fact the exact condition is $d_0-2t\langle X,d\rangle\le0$ on the whole cone. If the inner product is nonnegative this is automatic; otherwise one normalizes it to −1. Equivalently, $2t_*$ is the smallest ratio $(\alpha-v_0)/\langle X,X-v\rangle$ over vertices $v$ of $\mathcal F_\sigma$ with positive denominator. The cone is generated by $v-X$ over these and the other vertices, and testing the linear first-order inequality on each suffices. A vertex at the optimal mark cannot have positive denominator by the first-order condition for minimizing norm on the optimal face. Thus $t_*>0$ at each fixed order, including degenerate theta faces. Formula (5) uses the zeros of $X$, and can also be tested at a proposed $t$ by maximizing the linear functional $e_0-2tX$ over the original feasible polytope. No terminal support of the reciprocal path is needed.

On primes with $\alpha\ge1+\delta$, feed $X$ into (3) at any $0<t\le t_*$. In particular, with $D_*=1-\|X\|^2/(\alpha\sqrt n)$,

\[
 \boxed{\qquad D_*\ge c_\delta\min\{1,t_*\sqrt n\}.\qquad}                   \tag{6}
\]

Thus an imbalanced prime sequence of almost-flat minimum-norm endpoints must have $t_*\sqrt n\to0$. In that case (5) supplies a direction reducing squared norm to first order whose loss of mark per unit of squared norm reduction is $o(n^{-1/2})$. In the vertex version, the winning vertex has mark loss $o(1)$ since $\langle X,X-v\rangle\le\|X\|^2\le\alpha\sqrt n$ and $\alpha=O(1)$ by the entry bound on $K$ applied to $X=j+\sigma KX$. This gives an explicit obstruction to retaining a flat endpoint at the natural penalty scale. It does not preclude $t_*\sqrt n\to0$, or large norms with a norm deficit bounded away from zero.

## Prime-square comparison for the minimum, using pure Jacobi sums

Let $q=h^2$ with $h$ an odd prime, $B=\mathbb F_h^\times$, $H=B^\perp$, and $d=|H|=(h+1)/2$. On the plus side $\alpha=(h-1)/\sqrt n$, and $\alpha\mathbf1_H$ is an optimum of squared norm $h-1$. The [constant minus certificate](square-order-control.md#a-square-order-comparison) has, before the common normalization by $\sqrt n$, the spectrum $d$ at the mark and $(h-\lambda_i)/(h+1)$ off it, where $\lambda_i=\widehat s(i)$. Consequently every plus optimum is supported on

\[
 E=\{0\}\cup\{i\ne0:\lambda_i=h\}.
\]

For $i\ne0$, $\lambda_i$ is the real part of $J(\psi,\chi_q)$ for either full character lift $\psi$ of $i$, by the [two-lift formula](fourier.md#joint-distribution-on-the-even-modes). Since the Jacobi sum has modulus $h$, equality requires $J(\psi,\chi_q)=h$. Apply [Akiyama's classification and sign remark, pp. 97 and 100](https://matwbn.icm.edu.pl/ksiazki/aa/aa75/aa7521.pdf). In case 1 the order of $\psi$ divides $h+1$, so its restriction belongs to $H$. In case 2 its order $k$ satisfies $2(h-1)/k$ odd. Its exponent in the full cyclic character group is then $d$ times an odd integer: the factor $(q-1)/k=d[2(h-1)/k]$ is multiplied by a unit modulo $k$, and $k$ is even. Restriction reduces that exponent modulo $n=d(h-1)$, giving at most $(h-1)/2$ distinct possible frequencies. The two exceptional orders, 24 and 60, contribute at most $\varphi(24)+\varphi(60)=24$ more. Thus $|E|\le h+24$. Moreover, for $h\equiv1\pmod4$ the case 2 sign is negative, so $|E|\le d+24$.

By Cauchy–Schwarz and the known flat trial, the squared norm of the minimum on the plus side therefore satisfies

\[
 \frac{n}{h+24}\le \|X\|^2\le h-1,\qquad
 \|X\|^2\ge\frac{n}{(h+1)/2+24}=h-1-O(1)\quad(h\equiv1\!\pmod4).
\]

This improves the $O(n/\sqrt h)$ support bound from [phase equidistribution](rank-partitions.md#an-extensive-defect-at-a-single-mark-over-square-fields) and gives the $\sqrt q$ scale for the minimum itself. The exceptional orders need not be excluded individually for this estimate.

The opposite minimum is bounded and has an exact value. The constant minus witness is already the minimum-norm optimizer: in the positional normalization $f(1)=1$ every minus optimum has sum $d-1$ over $D_-$, so its squared norm there is at least $(d-1)^2/|D_-|$, with equality only for the constant row. Parseval in the mean-one normalization and $|D_-|=n/2$ give $\|Y\|^2=1+(d-1)^2/(n/2)=2h/(h+1)$. Thus the square contrast concerns the two true norm selections.

If $h\equiv1\pmod{120}$, for example, the exceptional congruences do not occur and $E=H$. Then every plus optimum is exactly $X=\alpha\mathbf1_H$: its positional inverse transform is constant on each $B$-coset and equals one at 1, and every other coset contains a negative position by the [exact coset sum −2](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy). The same flat spectrum is selected by the one-sided penalty for all sufficiently small $t>0$. To see this directly, let $Y$ be the normalized constant minus witness, so $Y_0=\alpha^{-1}$, it vanishes on $H\setminus\{0\}$, and $\gamma=\min_{i\notin H}Y_i>0$. For $z\in\mathcal F_+$, the pairing $\langle Y,z\rangle=1$ gives $\alpha-z_0\ge\alpha\gamma\sum_{i\notin H}z_i$. Meanwhile $\|X\|^2-\|z\|^2=2\alpha\sum_{i\notin H}z_i-\|X-z\|^2$. These inequalities show $X_t=X$ for $0<t\le\gamma/2$. This is a finite-field interval; the argument gives no uniform lower bound for its width at scale $n^{-1/2}$. The translation test still produces the subfield clique here, where the prime arithmetic exclusion does not apply.

## Checks and remaining scope

Sixty dense one-sided quadratic solves at ten primes from 13 through 257, both signs and $t\sqrt n\in\{0.02,0.10,0.25\}$, checked (1) at all 2,556 shifts with no observed negative slack. At five primes from 13 through 173, the tangent LP (5) for both signs gave zero linear support gain at $0.95t_*$ and strictly positive gain at $1.05t_*$, using independent maximization over the full mean-one even polytope. Checking even directions suffices for that linear test by inversion averaging. These are floating-point checks.

On twelve prime squares with $h$ from 3 through 61, exact remainders modulo the cyclotomic polynomial $\Phi_n$ tested $\lambda_i=h$ at every nonzero $i$ (5,704 comparisons). In cyclic position order, reduce the integer polynomial with coefficients $c_e=\sum_{j:ij\equiv e\bmod n}s(g^{2j})$; its remainder equals the constant $h$ exactly when the equality holds. For $h=7,11,17,19,41$ the respective counts of additional modes outside $H$ were $2,4,4,12,4$; the other sampled orders had none. The infinite-order support bound follows from the classification.

The prime test excludes near-cap flatness at a positive scaled tangent width and gives a measurable failure mode when the width vanishes. It leaves open diffuse high norms, the moderately nonflat critical-scale case, and the uniform endpoint bound required by the reciprocal-path argument. No conclusion about the asymptotic theta ratio follows from (6) alone.
