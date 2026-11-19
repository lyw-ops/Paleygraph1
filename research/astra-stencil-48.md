# Signed cold tests on actual Paley stationary rows

Every eligible prime passes a three-node limiting measure test at every cold floor from zero to one half, with uniform margin greater than .049. The same test passes on squares. Different explicit signed real tests fail at primes 113 and 173 and at square 121. Each failing test includes hot floors 28 and 32. A static concave trial problem gives a sufficient prime estimate for the asymptotic square-separating stencil of round 47 and an explicit opposite square gap. The all-prime trial estimate and ETH26 remain open.

## A continuous family of passing tests

Use the [whole-half-plane budget](astra-pick-46.md) with anchor $T=28$. The functional is
\[
 m_q(a)-\tfrac75m_q(3)+\tfrac25m_q(28),\qquad 0<a\le1/2 .
\]
For $K_x(s)=(1+s)^{-1}-(x+s)^{-1}$, $x=(a/T)^2$, $y=(3/T)^2$, the combined kernel $K_x-7K_y/5$ is negative at zero and positive near infinity by its value at zero and its leading coefficient at infinity. The limiting absolute marked value is at most $E(a)+7E(3)/5$, where
\[
 E(a)=\log\frac{\sqrt2[1+(1-8/\pi^2)a]}{\sqrt{1+a}} .
\]
This uses the [reciprocal trial](astra-branch-41.md) and the [hot theorem](seed-majorant-47.md). The finite first-order identity gives $l_{\sigma,0}/P_{\sigma,0}\le1+t[c-(E_b\sqrt{l_\sigma})^2]$, where $E_b$ divides the bulk sum by $n$ and $c=1-1/n$. The Jacobi trial, its root asymptotic and its bulk square-root mean are independent of $t$. The bound is uniform on the compact cold range, including arbitrary moving floors tending to zero.

Pair the combined kernel with $(s-r)/(s+r)$ for $r=(4/T)^2$. For an individual floor $v$, write $z=(v/T)^2$ and
\[
 F(v)=\frac{z+r}{z-r}\log\frac{1+v}{1+T}
       -\frac{2r(z-1)}{(z-r)(r-1)}\log\frac5{1+T}.
\]
Partial fractions give the lower bound $|F(a)-7F(3)/5|/2$ for the limiting budget. Its finite version replaces $1+v$, $1+T$, and $5$ by $W_v,W_T,W_4$, where $W_v=1+cv$. Convergence is uniform here. Interval evaluation on 512 rational subintervals proves the margin. These tests reach the cold endpoint without forcing zero theta bias.

## Explicit real tests failing on specified primes

For $(q,a,k)=(113,1/5,48),(173,1/20,47),(121,3/4,48)$ let $h=2^{-3300}$, $t(b)=a(1+b)/(1-b)$ and set
\[
 D_{k,h}f=\frac1{k!h^k}\sum_{j=0}^k(-1)^{k-j}{k\choose j}f(jh),\qquad
 S_q=D_{k,h}(m_q\circ t)+m_q(28)-m_q(32).
\]
Each test is field independent once its center and degree are chosen. At the indicated field its absolute value exceeds the whole-half-plane budget by more than 1998.

At the real center write $u_i=\sqrt{v_i^2+4w_i}$ and $v=Ku$. Here $n\le86$, $w_i\ge1/1720$, and $\max u_i\le\sum u_i=2\sqrt{nW_a}<26$. The equation $u^2-(Ku)^2=4w$ has derivative $J=2\operatorname{diag}(u)(I-\operatorname{diag}(v/u)K)$ with complex Euclidean inverse norm below $2^{25}$ since $1-|v_i/u_i|\ge2w_i/u_i^2>2^{-20}$ and $1/\min u_i<21$. On $|b|\le\rho=2^{-62}$ we have $\|4(w(t(b))-w(a))\|_2\le16|b|$. The quadratic remainder $z^2-(Kz)^2$ has norm at most $2\|z\|_2^2$ and Lipschitz constant $4d$ on a ball of radius $d=2^{-30}$. Inverting the fixed real $J$ gives a strict holomorphic contraction of this closed ball into itself for the increment from $u$. Its real solution agrees locally with the positive stationary row. The mark $A_0=(u_0+v_0)/2$ is at least $1/26$ since its reciprocal is at most 26. Its displacement is at most $d$, hence $|m_q(t(b))-m_q(a)|<1$ throughout. Its Taylor coefficients at orders $l\ge1$ are bounded by $\rho^{-l}$.

The forward difference multiplies the $l$th coefficient by $h^{l-k}S(l,k)$ for $l\ge k$ and kills lower orders, where $S(l,k)$ is a Stirling number of the second kind. Counting surjections gives $S(l,k)\le k^l/k!$. Hence the error against $c_k$ is bounded by
\[
 \rho^{-k}\frac{k^k}{k!}\frac{kh/\rho}{1-kh/\rho}<2^{-100}.
\]
The [actual jet enclosures](astra-cold-37-certified.jsonl) imply $|c_k|>2000$ in all three cases. Real leverage bounds the true hot difference by $\frac12\log(W_{32}/W_{28})<.07$.

For every density $|\eta|\le1/2$ the associated [measure representation](astra-pick-46.md) has $|\Im m|\le\pi/4$ on the whole right half-plane. The sine coefficient integral bounds all its cold Cayley Taylor coefficients of positive order by one. Its hot difference is bounded by the same .07 using the single-sign kernel. Supremizing over the densities thus bounds the exact budget by $1+2^{-100}+.07$. This proves the finite excess.

The kernel itself changes sign. In anchor-$a$ units its cold kernel at $t(b)$ is $4b/[(1+s)^2(1+2u b+b^2)]$, $u=(1-s)/(1+s)$. Its coefficient at order $k$ is $4(-1)^{k-1}U_{k-1}(u)/(1+s)^2$. At $s=1/(4k^2)$ and $4/k^2$ the two rational values have opposite signs and absolute value above five. On $|b|=1/2$ the rational kernel has modulus at most eight because the quadratic factors have unit-modulus roots. The same difference bound with radius $1/2$ and numerator eight gives error below one. The hot kernel difference has magnitude below one at both points. In comparison all three stencils pass at 13, 17 and 25 by the established whole-half-plane sections and sector bound. These fixed-field failures leave the asymptotic prime tests open.

## A static trial criterion for the square-separating node

Let $B$ be the exact limiting measure budget of the [128-hot-node stencil](seed-majorant-47.md) at $a=1/2$. For prime sufficiency use $B$ itself. Its upper bound .074 suffices for the square comparison. Let $R=e^{-B}\sqrt{n/W_a}$. For each sign maximize
\[
 Z_\sigma=\max_{l\in\mathcal P_\sigma}
    \left\{\frac{l_0}{R}+a(E_b\sqrt l)^2\right\}
\]
over nonnegative mean-one Fourier-sector rows of that sign. This uses the sign mask and prescribed parameters only. It rewards both a large trial mark and spread of its bulk. Its second-order cone representation replaces the square-root term by a variable $g\ge0$ with $y_i\ge0$, $y_i^2\le l_i g$, $E_b y\ge g$ on the bulk. Choose $y_i=\sqrt{l_i g}$ for the converse.

For the physical $P=P_\sigma(a)$ stationarity gives $l_0/P_0+aE_b(l/P)=W_a$ for every trial, including boundary rows. Cauchy–Schwarz bounds $E_b(l/P)\ge(E_b\sqrt l)^2$ since $E_bP\le1$. Also $(E_b\sqrt l)^2\le c$ by the bulk count. If $P_0/R=\kappa\le1$, then
\[
 Z_\sigma\le\kappa W_a+(1-\kappa)ac=W_a-(1-\kappa).
\]
Thus $\liminf_p(Z_\sigma-W_a)\ge0$ for both signs gives $\limsup_p|m_p(a)|\le B$ by physical reciprocity. Every fixed hot coefficient contributes $o(1)$, giving the proposed limiting inequality under the static trial hypothesis. On squares the minus-side mark has $\limsup P_{-,0}/R\le\exp(B-\frac12\log(4/3))$. Its cone program therefore has limiting deficit at least $1-\exp(.074-\frac12\log(4/3))>.067$. A failed trial hypothesis need not violate the physical bound.

1. Construct prime-mask rows on each sign whose explicit scores reach $W_a-o(1)$, starting at $a=1/2$. A fixed positive SOCP upper deficit along an unbounded prime subsequence refutes the sufficient trial target on that sign. Any smaller floor requires its own budget and target.
2. Test the displayed short-interval cold difference plus the hot pair in the prime limit. Positive limsup of its exact budget excess excludes whole-half-plane field-first control. Excess at a finite prime does not decide this.

The [checker](astra-stencil-48-check.py) certifies continuum constants, rational kernel signs, difference errors and conversions of inherited jets. Its [four records](astra-stencil-48-checks.jsonl) do not independently recompute stationary jets or evaluate the ill-conditioned real sums.
