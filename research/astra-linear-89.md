# The original signed price on additive intervals of affine matches

Let $p\equiv1\pmod4$ be prime, $Q=\mathbb F_p^{\times2}$, $n=(p-1)/2$, and $D_\pm=\{x\in Q:\chi(1-x)=\pm1\}$. Take any genuine plus and minus optimal probabilities $q,r$ on $G=\widehat Q$, with characteristic functions $F,R$, common mark $a=q_0,b=r_0$, point caps $a,b\ll p^{-1/2}$, and $nab=1$. Write
\[
 C_*={n(b-a)\over\sqrt p},\qquad C=C_*-p^{-1/2}.
\]
The full marked cubic is $C$, since the exterior positional sector counts differ by $-1$. Ordinary theta has the conjectured limit exactly when $C_*\to0$. [Marked cubic identity](astra-complement-84.md#a-fixed-cubic-test-at-the-marked-root)

Fix $A>2$, let $u,v$ be independent uniform rational primes at most $L=(\log p)^A$, and put $\eta=(\log p)^{1/2-A/4}$. Match
\[
 x=u^2z\in D_+,\qquad y=v^2(z+1)\in D_-,\qquad z\in\mathbb F_p.
\]
For a cyclic additive interval $I\subset\mathbb F_p$, define $H_I=p^{-1/2}\sum_{z\in I,\,\mathrm{matched}}[\Re R(y)-\Re F(x)]$. Both endpoint maps are injective and the two signed counting terms cancel on every individual pair. Then
\[
 \mathbb E_{u,v}|H_{\mathbb F_p}- C_*/4|\ll_A\eta,\qquad
 \mathbb E_{u,v}\sup_I\left|H_I-{|I|\over p}{C_*\over4}\right|
 \ll_A (1+\log p)\eta .                                                   \tag{1}
\]
In particular $A>6$ gives vanishing simultaneous discrepancy for every interval, including intervals chosen after seeing the rows and primes. Along a fixed gap, every interval of length at least $\delta_p p$ has the sign of the original gap on almost all prime pairs if $\delta_p/[(1+\log p)\eta]\to\infty$. The affine correspondence $y=(v/u)^2x+v^2$ has nonzero additive offset on every pair of primes. The entire matched set has $p/16+O(\sqrt p)$ points for every such pair at sufficiently large $p$. Indeed the four linear factors at $0,-1,u^{-2},v^{-2}-1$ have distinct roots. Equality of the two moving roots would imply $v^2-u^2+u^2v^2=0\pmod p$, impossible since this positive integer is less than $p$ eventually. The other coincidences are excluded by $u^2,v^2>1$ and $L^2+1<p$. Expanding the four strict sign and square indicators gives the count by Weil with bounded endpoint corrections.

## A genuine shifted atom on the same matches

For every displacement $t\in G$, the actual conditional measure $\mu_t(i)=nq_i r_{i+t}$ has mass one. This follows by positional orthogonality since $F,R$ have disjoint exterior sectors. Its characteristic function is $M_w(t)=\sum_i\mu_t(i)i(w)$ on $Q$. Fix an atom index $j\in G$. Multiply the summand of $H_I$ by
\[
 1_{z+2\in Q}\;\overline{j(g(z+2))}\, M_{g(z+2)}(t),\qquad g\in Q,
\]
and denote the result by $H_{I,t,j,g}$, extending this weight by zero off its domain. Uniformly in both genuine optima, the displacement and atom,
\[
 \mathbb E_{u,v}\sup_{g\in Q,\,I}
 \left|H_{I,t,j,g}-{|I|\over p}{\mu_t(j) C_*\over8}\right|
 \ll_A (1+\log p)\eta .                                                     \tag{2}
\]
For the full interval the bound is $O_A(\eta)$, still with the supremum in $g$. The choice of $t,j$ may depend on the prime and the optimal face, and precedes the draw of $u,v$. The choice of the third-coordinate dilation $g$ can follow that draw. The test is complex even though the two charged first coefficients are real. At $t=0,j=0$ its third-coordinate factor reduces to the square indicator. For a genuinely displaced test, any $j\ne0$ with $q_j/a\ge c>0$ gives $\mu_{-j}(j)\ge c$. Likewise any $t\ne0$ with $r_t/b\ge c$ gives $\mu_t(0)\ge c$. Thus the local first price of such an actual conditional law retains a fixed fraction of any gap. [Conditional displacement and its positional decomposition](astra-fibers-86.md#actual-conditional-law-at-each-positional-output)

More generally take any fixed coefficients $c_h$ on $G$ with sum of absolute values $B$, and use the third factor $1_{z+2\in Q}\sum_h c_h h(g(z+2))$. Formula (2) holds with main coefficient $c_0$ and error multiplied by $B$. The same proof allows phase changes on each exterior coefficient after the draw, with a prescribed absolute envelope and fixed $c_0$. For a subgroup of $Q$ of index $d$, its coset indicators have envelope $1/d$ on the $d$ annihilating characters. Hence (2) gives the main term $|I|C_*/(8pd)$ simultaneously on every coset of this subgroup in the third coordinate, at the same absolute error regardless of $d$. The conditional test also permits the nonnegative observable $|M_{g(z+2)}(t)|^2$, with $c_0=\sum_i\mu_t(i)^2$ and $B=1$.

## Complete twisted columns and short averaging

Write $e_p(kz)=\exp(2\pi i kz/p)$ and extend a character on $Q$ by zero on its complement. For the first endpoint, freeze $v$. With third-coordinate character $h$, the complete column against an endpoint character $i$ is
\[
 K_{v,k}(i,h)={1\over\sqrt p}\sum_{z\in Q,\,z+2\in Q}
      i(z) h(z+2)1_{v^2(z+1)\in D_-}\,e_p(kz).
\]
It satisfies
\[
 \left|K_{v,k}(i,h)-{n\over8\sqrt p}1_{k=0,\,i=h=0}\right|\ll1 .           \tag{3}
\]
Without the third character and its square restriction, the main term is $n1_{k=i=0}/(4\sqrt p)$. For the second endpoint use $w=z+1\in Q$, the multiplier $1_{u^2(w-1)\in D_+}$, and $h(w+1)1_{w+1\in Q}$, with additive twist $e_p(k(w-1))$. The estimates have identical constants up to an absolute factor.

For (3), extend each character on squares by the half-sum of its two lifts to $\mathbb F_p^\times$. Expand the strict sector indicator by the square test at $z+1$ and the quadratic test at $v^{-2}-1$, correcting at most two individual points. The possible finite roots $0,-2,-1,v^{-2}-1$ are distinct for all sufficiently large $p$, uniformly over the probes. For the second endpoint the corresponding roots in $w$ are $0,-1,1,1+u^{-2}$, again distinct. For $k=0$ a nontrivial local character at any root gives a bounded multiple of $\sqrt p$ by the multiplicative Weil bound, using distinct roots in the primitive-character representation. For $k\ne0$ the additive twist has a simple pole at infinity, so the mixed Weil bound costs only $O(\sqrt p)$ uniformly in the orders of both lifts. The only constant term has $k=i=h=0$, coefficient $1/16$ on the full field. Replacing $p/16$ by $n/8$ changes the raw term by $O(1)$. Without the third restriction the coefficient is $1/8$. [Mixed Weil bound, Theorem 5](https://escholarship.org/content/qt3qb1v3vw/qt3qb1v3vw.pdf)

Use the evenizations of $q,r$ for the two charged real parts. Their masses and caps at zero remain $a,b$. The conditional test still uses the original, possibly noneven, optima. Before imposing the first endpoint's strict sign, its complete weighted price at frequency $k$ equals
\[
 \sum_i q^{\rm ev}_i i(u^2) K_{v,k}(i,h).
\]
The only correction is at $x=1$, since all other coefficients vanish on the wrong sector. Its modulus is at most $p^{-1/2}$. Freeze $v,h,k$, subtract the constant column in (3), and apply the capped-law short-prime bound to the remaining bounded coefficients. This gives mean absolute $O_A(\eta)$ over $u$, uniformly in $v,h,k$. Reverse the order of conditioning for the second marginal. Subtracting the two bounds gives the complete signed frequency sum $S_k(h)$ with
\[
 \mathbb E_{u,v}|S_k(h)-1_{k=0,\,h=0}C_*/8|\ll_A\eta .
\]
The unrestricted third coordinate similarly gives $C_*/4$ at $k=0$. This argument needs the cap only on the distinguished endpoint averaged at that step. [Short-prime moment inequality (2)](astra-diffuse-87.md#unique-factorization-in-the-short-family)

For every cyclic interval $I$ and every representative $0<|k|\le(p-1)/2$, the normalized additive Fourier coefficient satisfies $|\widehat{1_I}(k)|\le1/(2|k|)$ by the geometric sum. Its constant term is $|I|/p$. Expand $1_I$, majorize the supremum by the sum of the frequency errors with this common envelope, and take expectations. For (2) do the same first with the envelope $|c_h|$ in the third coordinate. This proves both estimates, including their adaptive suprema. For a slowly growing number of disjoint intervals the errors can also be summed.

There is a spatially localized version with vanishing error for every $A>2$. Fix $1\le H\le p/2$, allowed to depend on $p$, and put $\Lambda_H(z)=H^{-1}(1_{[0,H-1]}*1_{[-H+1,0]})(z)$, with counting convolution on the additive field. This triangular weight is supported on $|z|<H$. Its normalized Fourier coefficients are nonnegative, sum to $\Lambda_H(0)=1$, and have constant term $H/p$. Replacing the interval by $\Lambda_H(z-c)$ permits the simultaneous supremum over all centers $c$, all exterior phases with the prescribed third-coordinate coefficient envelope, and all third dilations, at error $O_A(B\eta)$. The main terms are $HC_*/(4p)$ without the third coordinate and $Hc_0 C_*/(8p)$ with it. Along a fixed gap the unweighted window therefore has the original sign at **every** center on almost all draws whenever $H/(p\eta)\to\infty$. If its width is also chosen after the draw with $H\ge\delta p$, the cost is $O_A(B\eta[1+\log(1/\delta)])$. Indeed the Fourier envelope at nonzero $|k|\le p/2$ is $\min(1/(2|k|),1/(4\delta k^2))$, using the geometric sum twice and the bound by $H$ once. Summation gives the claimed price. For the unrestricted third coordinate use $B=1$ throughout.

## What a gap would still have to pay

Write $m=\max_{i\ne0}\{q_i/a,r_i/b\}$. If $m\to0$, every displaced law has $\max_i\mu_t(i)\le m$ for $t\ne0$, since at least one member of the product lies off its mark. In this case one can impose a uniformly vanishing amplitude cutoff on **both** charged endpoints, with an additive error in (1). In fact $\sum_Q|F|^2\le n(a^2+ma)$ by Parseval, and the analogous estimate holds for $R$. Erasing all pairs with either modulus above $\tau=(m+p^{-1/2})^{1/3}$ removes absolute normalized charge $O(\tau)$ at every pair of primes, uniformly over intervals and all weights of modulus at most one. The pre-normalization charge per removed pair is at most two, and each large site removes at most one pair. Thus the full and interval bounds after erasure cost $O_A(\eta+\tau)$ and $O_A((1+\log p)\eta+\tau)$, respectively. Consequently a hypothetical gap either has a subsequence with the genuinely displaced positive atom in (2), or the full affine interval price persists on an array whose surviving entries tend uniformly to zero. This dichotomy gives no arithmetic upper on either surviving signed sum.

At orders $s^2$ with $s$ an odd prime tending to infinity, the genuine square family has $F=1_{\mathbb F_s^\times}$ and $R=2/(s+1)$ on $D_-$, with $R(1)=1$. All short rational primes belong to the subfield. A nonzero first coefficient forces $z,x,y\in\mathbb F_s$, so $y\in D_-$ is impossible. The distinct-root count at order $s^2$ gives $s^2/16+O(s)$ strict pairs, since $L^4=o(s)$. Thus $H_{\mathbb F_{s^2}}=1/8+O(1/s)$ on every probe, while $C_*/4=-1/8+O(1/s)$. This checks the prime distinction on the original signed charge. [Square complementary probabilities](parallel-witness-6.md#the-four-coordinates-have-independent-limiting-support)

## Finite checks

The [384-bit replay](astra-linear-89-check.py) reconstructs genuine complementary pairs at $53,257,409$, including a certified odd perturbation on the minus row at the latter two. For every ordered pair of the finite probe primes, it checks the two complete marginal transforms with the strict identity corrections at additive frequencies $0,1,5$. It replays a sharp interval and a triangular window by independent additive Fourier inversion for the unrestricted test, a translated displaced atom, its conditional collision observable, and a nontrivial index-two coset. At $409$ the atom $\mu_{173}(31)$ is in $(0.308294402,0.308294403)$. For probes $(2,3)$ the affine fiber has 22 sites, and the displaced-atom interval sum has imaginary part in $(-0.000083614,-0.000083613)$. The checker also enumerates the square examples at $11^2,19^2,43^2$ using the quadratic norm to the subfield. These finite computations test the identities independently of the asymptotic error estimates. [Outward interval records](astra-linear-89-checks.jsonl)

## Ranked remaining tests

1. Fix $A>6$. For one bounded-index third-coordinate coset, compare the two true first prices on a macroscopic additive interval on a positive fraction of draws. Either the coset or the interval can be selected after seeing the draw. A difference $o(1)$ there would exclude a fixed gap by (2).
2. On a sequence with $m\ge c>0$, seek the same cancellation for a nonzero displacement with the guaranteed atom above, allowing an adaptive third-coordinate dilation. On a sequence with $m\to0$, compare the two first prices on the affine matches surviving the displayed deterministic amplitude cutoff. The interval and conditional equidistribution formulas determine the size of these tests under a gap and leave their cancellation open.
