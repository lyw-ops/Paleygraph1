# A critical subgroup for a shortfall walk that stays at the mark

At a fixed prime gap, a sharp cubic carrying a fixed amount of primary mass has two alternatives. A bounded convolution power can escape the almost-maximal marks of the actual quartic minimizer, forcing the [round-91 excess payment](astra-discount-91.md) when efficiency tends to one. Otherwise almost all shortfall lies on one subgroup coset of order comparable to the inverse mark. The same optimizer nearly attains its cap on average on the entire subgroup and coset, and pays fixed physical deficit and order-window-length height on the coset. Its annihilator has a bounded forbidden clique number. These statements allow arbitrary factorization of the cyclic order.

## The finite escape test

Take a true growing delayed pin from [round 88](astra-persistent-88.md) on the primary larger side, with $n=(p-1)/2$, $a$ its maximum mark, and $1+\delta\le\gamma=\sqrt n a=O(1)$. Write $P$ for the physical exterior mask, $r$ for its restricted deficit and $h$ for the positive companion, so $h\ge(2d-1)r$ and $r>v=\delta/8$ on $P$. Let $q$ be any actual masked quartic minimizer and put
\[
 u=q/a,\quad S=\sum_Pu_i^3,\quad \alpha=aS,\quad
 \mu_i=1_P(i)u_i^3/S,\quad \eta=\sum_i\mu_i u_i,\quad T_*=\eta S .
\]
Assume $S>0$. Reflection preserves the physical mask and optimizing face. Strict convexity in the masked variables makes $\mu$ even also for a non-even minimizing row. The inequalities $q_i\ge\alpha\mu_i$, $\alpha\le1$, and $\|\mu\|_\infty\le1/S$ hold pointwise or by summation. For $t$ sampled from $\mu^{*j}$ write $x_i^j=\mathbb E q_{i+t}$ and $f_j=1-x^j_0/a$. Then $f_0=0$ and $f_1=1-\eta$.

Let $F$ denote the forbidden positional sign in the square group $Q$ and set $\kappa=\max_{z\in F}|\widehat\mu(z)|$, $b=\sqrt{(1+\kappa)/2}$ and $c_p=\lfloor(1+\sqrt{1+4n})/2\rfloor$. For all $k\ge1$,
\[
  1-f_k\le \frac{c_p}{na}+\frac{b^{k-1}}{\sqrt\alpha},\qquad
  \kappa\le\min(1,(1-\alpha)/\alpha).                                      \tag{1}
\]
Indeed the positional phase vectors $(\sqrt{\mu_i}\,i(z))_i$ for $|\widehat\mu(z)|>b$ each have squared projection $>b^2$ onto the root line. Every pair has inner-product modulus $>2b^2-1=\kappa$ by Cauchy–Schwarz on the perpendicular components. Their nontrivial quotients avoid $F$. Since the elements of $Q$ are squares, their nonzero additive differences have one quadratic sign. Scaling for the negative sign gives a Paley clique, of size at most $c_p$. For $b=1$ the high set is empty. Invert $x^k_0$ on $Q$, bound each high term by one, and apply Cauchy–Schwarz to the other terms after taking out $b^{k-1}$. Parseval gives $\sum|\widehat q|^2\le na$ and $\sum|\widehat\mu|^2\le n/S$. Finally $q-\alpha\mu$ is nonnegative of mass $1-\alpha$ and $\widehat q=0$ on $F$. This proves the last inequality. [Hanson–Petridis, Corollary 1.5](https://arxiv.org/abs/1905.09134) · [Earlier phase-vector estimate](astra-quadratic-10.md#weighted-phase-vectors-and-a-scalar-moment-consequence)

Thus $\alpha\ge\zeta>0$ and $\kappa\le1-c$ give $f_k\gg_\delta1$ for a fixed $k=k(\delta,\zeta,c)$ on every sufficiently large prime. In particular $\alpha\ge1/2+c$ suffices, with no large-prime-factor hypothesis. If $\eta\to1$, any fixed-power escape gives a subsequence and a fixed $1\le j<k$ for which $f_j\to0$ and $f_{j+1}\to e>0$. For a positive fraction of $t\sim\mu^{*j}$ the next-step cubic loss exceeds $e/3$, and one can simultaneously take $q_t/a\to1$. Such a mark is strictly submaximal by quartic first variation. With $A=m(\gamma-1-v)-v\gg_\delta1$, $m=R_0/\sqrt n=1+o(1)$, and $E=(r-(A/\eta)\mu/a)_+$, the same translate pays $q^t(E)\gg_{\delta,e}1$ by the bounded-coefficient physical inequality. Its height and deletion conclusions at the round-88 selected length follow from the same pointwise pin. [Translate on the actual pin](astra-discount-91.md#a-bounded-coefficient-at-the-physical-pin)

## The alternative when every fixed power stays near the maximum

Suppose along a sequence $\alpha\ge\zeta>0$ and $f_j\to0$ for every fixed $j$. There are a subgroup $K\le G=\widehat Q$, a coset $C$ of $K$ with $C=-C$, and growing even integers $r_p$ such that
\[
 \begin{split}
 &\|\mu^{*r_p}-{\rm Unif}(K)\|_{\rm TV}
  +\|\mu^{*(r_p+1)}-{\rm Unif}(C)\|_{\rm TV}=o(1),\qquad \mu(C)=1-o(1),\\
 &q(K)=(1-o(1))a|K|,\qquad q(C)=(1-o(1))a|K|.                       \tag{2}
 \end{split}
\]
Here $K$ and $C$ can vary with the prime. For the prime conclusion below, the single-step concentration and both near-saturated means are simultaneous for the same minimizer and pin.

Choose $k_p\to\infty$ slowly so that $\max_{1\le j\le k_p}f_j=o(1)$. For $A_s=\{z:|\widehat\mu(z)|\ge1-s\}$,
\[
    (1-o(1))na\le |A_{k_p^{-1/2}}|,\qquad
    |A_{k_p^{-1/4}}|\le(1+o(1))n/S.
\]
For the first bound use the same inversion and Cauchy–Schwarz as in (1) at $j=k_p$, cutting at $1-k_p^{-1/2}$. The second is Parseval. Partition $[k_p^{-1/2},k_p^{-1/4}]$ into $\lfloor\sqrt{\log k_p}\rfloor$ intervals with common ratio. There is a pair of consecutive endpoints $l<L$ with $L/l\to\infty$ and $|A_L\setminus A_l|=o(na)$, since the entire size change is $O_\zeta(na)$.

The set $A_l$ is symmetric and contains the identity. The phase-vector inequality gives $A_l A_l^{-1}\subseteq A_{4l}$ since $2(1-l)^2-1\ge1-4l$. Thus $|A_l A_l^{-1}|=(1+o(1))|A_l|$. In fact $H=A_l A_l^{-1}$ is a subgroup. For $z=x/y\in H$, $xA_l,yA_l\subset H$ intersect in at least $2|A_l|-|H|>|A_l|/2$ places. Thus $|A_l\cap zA_l|>|A_l|/2$. For any $z,w\in H$ the sets $A_l\cap zA_l$ and $A_l\cap w^{-1}A_l$ intersect, implying $zw\in H$.

Set $K=H^\perp$. Now $|H|\in[(1-o(1))na,(1+o(1))n/S]$ and $A_l\subseteq H\subseteq A_{4l}\subseteq A_L$. Averaging $|\widehat\mu|^2$ over $H$ gives $\sum_{C'}\mu(C')^2\ge(1-4l)^2$, where the sum runs over $K$-cosets. One coset $C$ therefore has mass $1-O(l)$, and evenness forces $C=-C$. Choose $r_p$ as the nearest even integer to $(lL)^{-1/2}$, so $r_p l\to0$, $r_p L\to\infty$ and $r_p+1\le k_p$. On $H$, $\widehat\mu^{r_p}=1+o(1)$ uniformly by reality and evenness of the exponent. On $A_L\setminus H$ the squared Fourier error against $1_H$ sums to $o(na)$. On $Q\setminus A_L$ its sum is at most $(1-L)^{2r_p-2}n/S=o(na)$. By Parseval $\|\mu^{*r_p}-{\rm Unif}(K)\|_2^2=o(a)$. Its mass on $K$ is $1-o(1)$ by averaging the real even powers on $H$. Cauchy–Schwarz on $K$ now proves the first total variation statement because $|K|=O(1/a)$. One further step gives the second, since ${\rm Unif}(K)*\mu$ places $1-O(l)$ uniformly on $C$. Evaluating $u\in[0,1]$ against the two walks proves the last line of (2).

## Prime divisor, quotient and physical tests at that coset

Let $j(H)$ be the largest size of a subset of $H$ whose nontrivial pairwise quotients all belong to $F$. For every feasible primary row the mass of each $K$-coset is at most $1/j(H)$, by testing the resulting orthogonal phase vectors against the rank-one contribution of that coset. Here $|H|\ge(1-o(1))na>c_p$, so the prime clique theorem guarantees $j(H)\ge2$. The point cap for $\mu$ and (2) give
\[
 (1-o(1))\alpha\le a|K|\le\frac{1+o(1)}{j(H)}\le\frac{1+o(1)}2.       \tag{3}
\]
Thus slow propagation requires an actual divisor in this interval and a positional subgroup with forbidden clique number at most $(1+o(1))/\alpha$. In the cyclic group, for each admissible divisor there are at most two candidate cosets, the subgroup itself and its order-two translate in the quotient if it exists. This excludes slow propagation whenever no such divisor exists with a fixed margin, even if the order has no prime divisor comparable to $n$. [Coset Gram test](astra-dual-90.md#exactly-efficient-shortfalls)

Since $\mu$ is supported on $P$ and $q\ge\alpha\mu$, one has on this specific coset
\[
 |C\cap P|\ge(1-o(1))S,\qquad
 q(r1_C)\ge(1-o(1))v\alpha,\qquad
 q(h1_{C\cap P})\ge(1-o(1))(2d-1)v\alpha.                           \tag{4}
\]
In particular the *unweighted* average of $h$ on $C$ is $\gg_{\delta,\zeta}d$. An $o(d)$ bound there for every at most order-two candidate from (3) therefore forces finite escape. The height and deficit lower bounds survive deleting $o(1/a)$ source sites, since the lost $\mu$-mass is $o(1)$ by its cap. The first-moment height estimate over the full group does not by itself test these specific critical cosets.

There is also a restriction involving the actual opposite optimum $v^*$, of mark $\beta=1/(na)$. Averaging the translated opposite equality over $K$ gives
\[
   \sum_{B\in G/K} q(B)v^*(B)=|K|/n .                                \tag{5}
\]
The term $B=K$ alone pays $(1-o(1))|K|/n$ because $q(K)=(1-o(1))a|K|$ and $v^*(K)\ge\beta$. Thus $v^*(K)=(1+o(1))\beta$ and, if $C\ne K$, $v^*(C)=o(\beta)$. In particular every opposite optimizer can place only $o(\beta)$ off the root within $K$, uniformly over the opposite face. The same coset supports the leading primary average, even when it carries $\gg\sqrt n$ sites. The primary optimum in the cyclic quotient with the sign restricted to $H$ lies between the projected value $q(K)$ and $a|K|$, since a uniform lift of any feasible quotient law is feasible in the original sector. This identifies a near-optimal marked quotient that can be tested directly from the positional sign.

The alternatives are subsequential. For a fixed gap with $\eta\to1$ and $\inf\alpha>0$, pass to a subsequence on which each $f_j$ converges. A positive limit at any finite time gives the displaced excess payer. If all limits vanish, (2)–(5) hold. The argument leaves open the case $aT_*\to0$, the upper on the escaped translate's price, and the occurrence of the critical cosets in (3)–(4).

## Finite checks and next tests

At prime $97$, terminal time $11$, the length-two quartic minimizer has $\alpha=0.025346767\ldots$ and $\kappa=0.833540609\ldots$. The strict high spectrum in the proof of (1) contains only the identity. Using its actual cardinality gives the step-128 upper $0.169131533$ on the normalized root, whose actual value is $0.143920929\ldots$. On the length-eight minimizer the two equally weighted shortfalls, at $8$ and $40$ in $\mathbb Z/48$, approach uniformity on $\{0,16,32\}$ at even times and $\{8,24,40\}$ at odd times. The step-20 and step-21 total variation distances are exactly $1/1572864$ and $1/3145728$. The corresponding limiting normalized roots are $1/3$ and $0.238799297\ldots$, respectively. Thus confinement to a coset alone can still allow substantial escape from maximal marks. The finite graph does not instantiate the asymptotic fixed-gap and efficiency assumptions.

Over the square field of order $31^2$ the genuine subfield row and length-eight physical mask have $\alpha=15/16$, $\eta=1$, and every walk has normalized root one. The charged height on the order-16 subgroup is $16.283557995\ldots$. Its annihilator has order 30 and no forbidden character, demonstrating exactly where the prime conclusion (3) fails. [Arb384 and exact-count replay](astra-height-92-check.py) · [Outward intervals](astra-height-92-checks.jsonl)

1. For each critical divisor use the actual restricted positional sign to compute the quotient maximum mark and a forbidden clique in its annihilator. Among the surviving at most two cosets, bound the mean of the same early companion or the size of the physical mask intersection in (4).
2. In the bounded-time escape case test the actual excess on the near-maximal translates. To see what their opposite laws permit, for every true opposite optimizer $v^*$ one has $n\sum_{i\ne0}v_i^*q_{i+t}=1-u_t$. Hence the part of $q^t(E)$ on $nv_i^*\ge\lambda E_i$, $i\ne0$, is at most $(1-u_t)/\lambda$. Choosing $\lambda\downarrow0$ more slowly than the mark loss leaves a fixed price on sites with $n v_i^*=o(E_i)$ for any specified opposite optimizer, including after the physical size deletions when the retained price is positive.
