# Translation constraints on the smoothed spectra

Let $A=(\Phi(v^*)+v^*)/2$ and $B=(\Phi(v^*)-v^*)/2$ be the positive, even spectra of the [smoothing equation](smoothing.md), indexed by $\widehat Q$. Use $c=\tau/n\le1$, $w_0=1$, $w_i=c$ for $i\ne0$, and $W=1+(n-1)c$. Then $A_iB_i=w_i$ and $\sum_i A_i=\sum_i B_i=\sqrt{nW}$.

## An exact deficit for each translate

The inverse Fourier supports of $A$ and $B$ intersect only at the identity of $Q$. Therefore every cross-correlation is constant:

$$\sum_i A_i B_{i+h}=W\qquad(h\in\widehat Q).$$

For $h\ne0$ set $t_h=A_h/A_0$, so $B_h/B_0=c/t_h$. In the cross-correlation, the two terms at $i=0,-h$ sum to $t_h+c/t_h$, using evenness. On the remaining indices the summand is $cA_i/A_{i+h}$. The involution $i\mapsto-i-h$ inverts the ratio. Hence

$$c\sum_{i\notin\{0,-h\}}\big(\cosh(\log(A_i/A_{i+h}))-1\big)
=1+c-t_h-c/t_h=(1-t_h)(1-c/t_h).$$

In particular $c\le t_h\le1$. Both exact spectra reach their maximum at the marked frequency. This bound is sharper than the elementary estimate on individual entries from the Jacobi kernel.

Let $U_i=\log(A_i/\sqrt c)$ for $i\ne0$ and $U_0=0$. Write $D_h=(1-t_h)(1-c/t_h)$. By $\cosh(x)-1\ge x^2/2$,

$$d(h)^2:=\frac1n\sum_i |U_i-U_{i+h}|^2\le\frac{2D_h}{\tau}+O_\tau\big((\log n)^2/n\big).$$

The error is from the two entries incident to the mark, where $U_h=O_\tau(\log n)$ by $c\le t_h\le1$ and the elementary boundedness of $A_0,B_0$. The function $d$ is a translation-invariant pseudometric since translation is an isometry on $\ell_2$. With normalized Fourier coefficients $\widehat U(a)=n^{-1}\sum_i U_i\overline{i(a)}$ on $Q$, its exact square is $\sum_a |1-h(a)|^2|\widehat U(a)|^2$. Thus ratios $A_h/A_0\to1$ or $B_h/B_0\to1$ imply $d(h)\to0$ at fixed $\tau$. This only constrains peaks near the mark scale. The identity allows concentration on many entries of smaller amplitude.

## A prime-field exclusion for subgroup cosets

For any nonnegative spectrum $L$ on the plus support with mean $1$, let $\mu(i)=L_i/n$. Suppose $\mu$ gives more than half its mass to a coset $C$ of a subgroup $S\le\widehat Q$. Its annihilator $S^\perp$ in $Q$ has size $n/|S|$. For $a\in S^\perp$ the coset characters all have the same value at $a$. The inverse Fourier coefficient of $L$ there has absolute value at least $2\mu(C)-1>0$. Thus $s(a)=+1$ for $a\in S^\perp\setminus\{1\}$. For distinct $a,b\in S^\perp$, multiplicativity gives $\chi(a-b)=s(a/b)=+1$. Adding $0$ produces a Paley clique of size $|S^\perp|+1$.

At prime order the [Hanson–Petridis bound](https://arxiv.org/abs/1905.09134) is $(1+\sqrt{2p-1})/2$, so $|S^\perp|\le(\sqrt{4n+1}-1)/2<\sqrt n$. It follows that **no coset of a subgroup of size at most $\sqrt n$ can carry more than half the mass** of a plus spectrum, including the smoothed $A$. This excludes the specific majority-mass coset observed in the square-order control. It applies to every feasible plus spectrum. The argument leaves general subsets of the dual group and collections of cosets open.

## Testing a high plateau with a feasible spectrum

The same cross-correlation reasoning gives a test that uses the reciprocal weights. Take a nonnegative plus spectrum $L$ of mean $1$, a set $I\subseteq\widehat Q\setminus\{0\}$, and $\eta\ge0$ such that $L_i\le\eta$ outside $I\cup\{0\}$. If $\sqrt n A_i\ge M$ for all $i\in I$, then $B_i=c/A_i\le\tau/(M\sqrt n)$ there, so

$$\sqrt W=\frac1{\sqrt n}\sum_i L_i B_i
\le\frac{L_0B_0}{\sqrt n}+\frac\tau M+\eta\sqrt W.$$

The first equality uses complementary supports. An analogous test exchanges $A$ and $B$ and uses a minus spectrum. The marked term is necessary. For example, the subfield indicator spectrum over a square field has its marked value at the $\sqrt n$ scale.

As one application, consider [the Fejér example](square-order-control.md#a-sector-estimate-that-fails-even-at-prime-order). Let the plus support contain $4^j$ for $1\le |j|\le J$ and take the order of $4$ to exceed $2J$. The degree-$J$ Fejér spectrum and any of its translates then have mean $1$, height at most $J+1$, and values bounded by $[(J+1)\sin^2(\delta/2)]^{-1}$ outside their phase arc of radius $\delta$. For $J=o(\sqrt n)$ and $J\sin^2(\delta/2)\to\infty$, the test shows that each such arc has at least one unmarked coordinate with scaled spectrum at most $\tau/\sqrt{1+\tau}+o(1)$. In particular, on primes with plus support on a run of length $J\gg L^2$, the degree-$L$ Fejér kernel cannot be dominated on all bulk coordinates by a fixed multiple of $\sqrt n A$. An arc of radius of order $1/L$ about its maximum has Fejér values of order $L$ throughout. This tests plateaus aligned with feasible Fourier kernels. Controlling irregular high sets remains necessary for a general norm estimate.

## Mass and energy outside a coset

Normalize the stationary spectra to probabilities $\mu=A/\sqrt{nW}$ and $\nu=B/\sqrt{nW}$. Their cross-correlation is uniform. For any two frequency sets $I,J$,

$$\mu(I)\nu(J)\le |J-I|/n.$$

This follows by summing the uniform cross-correlation over $J-I$, which includes every pair in $I\times J$. Also, if $A_i\ge a$ on $I$ and $B_i\ge d$ on $J$, then $|\{i\in I:i+h\in J\}|\le W/(ad)$ for every $h$, by keeping only those terms at that shift. In particular, any two cosets of the same frequency subgroup of size $m$ have a product of opposite-sign masses at most $m/n$. If one coset carries at least $\epsilon$ of either spectrum's mass, the opposite spectrum places at most $m/(n\epsilon)$ on each individual coset of that subgroup.

Let $T$ contain the mark, and write $D=(A-B)/(A+B)$ for the true stationary diagonal. From $\mu(T)+\nu(T)\le1+\mu(T)\nu(T)$ we get

$$\frac1n\sum_{i\notin T}\frac{1}{\sqrt{1-D_i^2}}
=\frac12\sqrt{W/\tau}\big(\mu(T^c)+\nu(T^c)\big)
\ge\frac12\sqrt{W/\tau}\left(1-\frac{|T-T|}{n}\right).$$

Here $A_i+B_i=2\sqrt{\tau/n}/\sqrt{1-D_i^2}$ off the mark. If $T$ is contained in a union of at most a fixed number of cosets of the same subgroup of size $O(\sqrt n)$, then $|T-T|/n=O(n^{-1/2})$. Consequently $\sup_{i\notin T}|D_i|$ tends to one as $\tau\to0$. A clipping bound independent of $\tau$ cannot hold outside a fixed number of critical cosets in that limit, over either prime or square fields. The bound still allows a different reference for each fixed $\tau$.

There is also a quadratic cost from each forbidden positional coefficient. Let $L=A$ or $B$ with sign $\sigma=+1$ or $-1$ respectively, let $M=L/\sqrt{nW}$, and let $I$ be a coset of a frequency subgroup $G$. Put $k_\sigma=|\{x\in G^\perp:s(x)=-\sigma\}|$. At every such $x$, the inverse unitary Fourier coefficient of $L$ is zero. The contribution from $I$ has absolute value $\sum_{i\in I}L_i/\sqrt n$, since all characters in $I$ have the same phase at $x$. Thus the contribution from $I^c$ has the same magnitude there, and Parseval gives

$$\|\mathbf1_{I^c}L\|_2^2\ge k_\sigma W M(I)^2.$$

This holds for any feasible positive spectrum with the stated support and normalization. It rules out positive mass on a single coset with bounded exterior energy whenever the corresponding forbidden count grows. The [unshifted marked-response calculation](unshifted-cosets.md) also reduces its prescribed-support obstruction to bounded sign defects, through a different use of the same positional coset averages.

## Comparison with the square-order control

[Seven numerical runs](../data/translation-diagnostics.csv) at $\tau=0.05$ check the shift budget and the constant cross-correlation, with maximum errors below $10^{-7}$. At $q=389^2$, the largest unmarked peak is about $95.1\%$ of its spectrum's marked peak. Its shift has $D_h\simeq0.0492$, and the plus spectrum places $90.6\%$ of its mass on the size-$195$ annihilator of the subfield clique. At the nearby prime $151337$, the peak ratio is $2.70\%$ and the largest mass among subgroup cosets of size at most $\sqrt n$ is $0.365\%$. At $p=1000033$ the peak ratio is $1.04\%$. These sample values describe floating-point iterates with the recorded residuals.
