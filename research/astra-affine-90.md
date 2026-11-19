# Four equal-density pieces of the affine first price

On the actual affine matches of round 89, one can measure an exterior atom of either optimizing face by the change of the **real first price** between two pieces of the same size to leading order. The pieces can be taken as ordinary subsets. A displaced conditional measure supported on the plus optimizer affects the plus price alone, even when its characteristic function is tested at both charged endpoints. There is also a sharp threshold for canceling the signed first price on one of four pieces using real endpoint tests of Fourier norm one. Cancellation on the entire affine fiber with its prescribed third-coordinate coset remains open.

## The two endpoint phases

Take $p\equiv1\pmod4$ prime, $Q=\mathbb F_p^{\times2}$, $G=\widehat Q$, $n=|Q|$, and $D_\pm=\{x\in Q:\chi(1-x)=\pm1\}$. Write $q,r$ for genuine plus and minus optimal probabilities at zero, $a=q_0,b=r_0$, $F,R$ for their characteristic functions, and $q^e_i=(q_i+q_{-i})/2$, with the same convention for $r^e$. Thus $nab=1$ and $a,b\ll p^{-1/2}$. Each reflection preserves feasibility and the optimal mark. Therefore every pair of reflected or unreflected opposite optimizers has its aligned overlap exhausted at zero. In particular $q^e_i r^e_i=0$ for $i\ne0$. [Paired optimal faces](astra-matched-88.md#exact-overlap-behind-the-nonlinear-covariances)

As in [the affine test](astra-linear-89.md), take independent uniform rational primes $u,v\le (\log p)^A$, $A>6$, and $x=u^2 z\in D_+$, $y=v^2(z+1)\in D_-$, denoting these matches by $\mathcal M$. Optionally restrict $z+2$ to a coset of a fixed subgroup of index $d$ of $Q$. Write $\lambda=1/(2d)$ with this restriction and $\lambda=1$ without it. The coset may be chosen after the probes; the subgroup and all endpoint Fourier envelopes are chosen before. For a cyclic additive interval $I$ put $\alpha_I=|I|/p$ and
\[
 H_I(P,S)=\frac1{\sqrt p}\sum_{\substack{z\in\mathcal M\cap I\\ \text{third restriction}}}
     [\Re R(y)-\Re F(x)]P(x)S(y).
\]
If $P=\sum_h c_hh$, $S=\sum_h e_hh$, set $L_q(P)=\sum_h q^e_{-h}c_h$, and similarly for $L_r$. With $B=\|c\|_1\|e\|_1$ and $E_A=(1+\log p)(\log p)^{1/2-A/4}$ one has
\[
 \mathbb E_{u,v}\sup_{I,\,\mathrm{coset}}
 \left|H_I(P,S)-\alpha_I\lambda\frac{n}{4\sqrt p}
  [c_0 L_r(S)-e_0 L_q(P)]\right|\ll_A B E_A .                 \tag{1}
\]
Taking the supremum over endpoint coefficient phases with predetermined absolute envelopes is also valid, with the envelope norms defining $B$. For the full interval one can drop $1+\log p$. The underlying count divided by $p$, weighted by $P(x)S(y)$, is $\alpha_I\lambda c_0e_0/16+O(B(1+\log p)/\sqrt p)$ deterministically and simultaneously.

For (1), expand the third coset into its $d$ annihilating characters with coefficients of modulus $1/d$, imposing also the square requirement. Consider one character $h(x)$ and $k(y)$ and an additive twist $e_p(lz)$. In the plus marginal freeze $v$. Before the strict $x=1$ correction, its Fourier row at $z$ has coefficients $q^e_{i-h}$ times $i(u^2)$, since $h(x)\Re F(x)$ has this shifted row. The opposite multiplier is $k(y)1_{y\in D_-}$. Expand all characters on squares into the two lifts on $\mathbb F_p^\times$. For each fixed $i$ the centered complete column divided by $\sqrt p$ has absolute bound $O(1)$ by the same mixed Weil estimate as in [round 89](astra-linear-89.md#complete-twisted-columns-and-short-averaging). Its finite roots lie at $0,-1,v^{-2}-1$ and, when present, $-2$. Only $i=k=l=0$ and the trivial optional third character give a main term. The untwisted coefficient there is $n/(4\sqrt p)$ without the third restriction, or $n/(8\sqrt p)$ before the third coset coefficient. The external phase $k(v^2)$ has unit modulus and equals one when $k=0$. The capped short-prime bound over $u$ applies to the translated probability $q^e_{i-h}$; the exceptional $x=1$ costs at most $1/\sqrt p$. Interchanging endpoints gives the $r^e_{-k}$ term with $h=0$. Summing the three absolute Fourier envelopes and the usual interval envelope proves (1). For the raw count expand both strict sign indicators. The extra moving root $u^{-2}$ is distinct from the previous roots for large $p$, since the short probes satisfy $u^2v^2+v^2-u^2<p$ and $2u^2+1<p$. Every nonconstant column costs $O(\sqrt p)$ before division by $p$, yielding the stated count. The constants are independent of character orders and index.

## A displaced atom seen on its own sector

Let $j\ne0$ with $q_j>0$. For $t=-j$ put $\mu_i=nq_i r_{i+t}$ and $T(w)=\Re\sum_i\mu_i i(w)$. This is an actual conditional probability. It has $\mu_j=q_j/a$, and $\mu_0=0$ since $r_{-j}=0$. Thus $T$ is real, has zero constant coefficient, and its Fourier norm is one. The exact two endpoint responses are
\[
  L_r(T)=0,\qquad D_q:=L_q(T)=\sum_iq_i^e\mu_i
     \ge \frac{q_j^2}{2a}.                                      \tag{2}
\]
The first equality uses $\mu_i>0\Rightarrow q_i>0$ and opposite-face disjointness even after reflection. The bound uses $q^e_j\ge q_j/2$. With $r$ as parent one uses $\nu_i=nr_iq_{i-k}$ for $r_k>0$ and obtains $D_r\ge r_k^2/(2b)$ with $L_q(\Re\widehat\nu)=0$. Either statement uses the original probabilities in the conditioning even when they are noneven. [Displacement probabilities](astra-fibers-86.md#actual-conditional-law-at-each-positional-output)

More generally choose any real $T,U$ of Fourier norm at most one and zero constant coefficient. Write $D_q=L_q(T)$, $D_r=L_r(U)$. For $\epsilon,\delta\in\{+1,-1\}$ form the four nonnegative weights
\[
 w_{\epsilon\delta}(z)=\frac{1+\epsilon T(x)}2\,\frac{1+\delta U(y)}2 .
\]
They sum to one. Their individual signed prices have the main terms
\[
   \alpha_I\lambda\frac n{16\sqrt p}
       (b-a+\delta D_r-\epsilon D_q),                           \tag{3}
\]
with the common error in (1). Choosing $T=U$ from (2) makes the second sign immaterial to the main term. The two choices of the first sign differ by $\alpha_I\lambda n D_q/(8\sqrt p)$, uniformly detectable on all macroscopic intervals if $q_j/a$ stays above a fixed positive constant and $d$ stays bounded. The same comparison is possible with the additional nonnegative weight $1_{z+2\in Q}|\widehat\mu(g(z+2))|^2$ in place of the third coset, uniformly in $g\in Q$. Its third Fourier norm is one and its new $\lambda=\tfrac12\sum_i\mu_i^2\ge (q_j/a)^2/2$.

For character selectors the optimal amplitude in this class has a simple form. Put $m_q=\max_{i\ne0}q_i^e$ and $m_r=\max_{i\ne0}r_i^e$. The bounds $|D_q|\le m_q$, $|D_r|\le m_r$ follow by the Fourier norms. Each endpoint of these two intervals is attained using the appropriate $\pm\Re i(w)$ and every interior point by attenuation. Consequently the least possible absolute bracket in (3), over the specified real tests and cell signs, is exactly
\[
             (|b-a|-m_q-m_r)_+.                                  \tag{4}
\]
Under $|b-a|\le m_q+m_r$ there is a quarter of the matches, to leading order in count, with first price $o(1)$ on *every* additive interval on almost all draws. The conclusion also holds if the right side of (4) is $o(p^{-1/2})$. If $m_q+m_r=o(p^{-1/2})$, the entire class of norm-one probes has the original quarter-price main term, with a uniform bound on the expected error for every choice made before the draws. These assertions concern localized first prices. The three other pieces still carry their own charges.

## A single sharp partition for all intervals

The weighted four-way comparison above holds for ordinary disjoint subsets, using just two extra uniform elements $K,J\in\mathbb F_p$. Order the four outcomes, and, for each $z$, divide $[0,1)$ into four consecutive intervals with lengths $w_{\epsilon\delta}(z)$. Assign $z$ to the outcome containing $((Kz+J)\bmod p)/p$. Use the same partition for every additive interval and every choice of third coset. Conditional on the two primes, distinct $z$ have independent uniform labels, since their two linear forms in $K,J$ are independent. Each cell probability differs from its intended weight by at most $2/p$.

For one fixed third coset, write $d_z=[\Re R(y)-\Re F(x)]/\sqrt p$ on its strict matches and zero elsewhere. The indicators of a cell, centered by their actual probabilities, are pairwise orthogonal across $z$. The normalized total squared coefficient obeys
\[
 \sum_z |d_z|^2\le\frac2p\left(\sum_Q |F|^2+\sum_Q |R|^2\right)
 \le \frac{2n(a+b)}p=O(p^{-1/2}).
\]
Any interval splits into $O(1+\log p)$ dyadic blocks, including a possible wrap. Cauchy–Schwarz followed by summation over every block at each dyadic level bounds the expected maximum squared interval error by $O((1+\log p)^2\sum_z|d_z|^2)$. The $2/p$ bias costs $O(p^{-1/2})$ even by the unit endpoint caps. For simultaneous cosets, square the maximum over the cosets and bound by their sum of squares. Their supports are disjoint, so their squared-coefficient budgets sum to the same bound. With the additional collision weight, the same argument applies to each fixed dilation, without a simultaneous dilation claim for this rounding estimate. For counts use $|d_z|=1/p$ on the relevant sites. Consequently all four sharp cell prices obey (3) up to mean supremum error
\[
        O_A\big(E_A+(1+\log p)p^{-1/4}\big).
\]
Their counts divided by $p$ simultaneously equal $\alpha_I\lambda/64+O_{L^1}((1+\log p)/\sqrt p)$. This quarter-density conclusion compares against the original strict matched count $\alpha_I\lambda p/16$. Some additive seeds attain the stated errors up to an absolute factor after averaging over the prime draws; on almost all joint draws the errors vanish. The labels use only an affine function of the field coordinate and the prescribed endpoint scores.

If the assignment can inspect the charged endpoint values, one can instead choose a deterministic partition *for every* pair of primes, preserving the two marginal prices separately in every interval with rounding error $O(1/\sqrt p)$ and counts with error $O(1)$. In each third coset process its matched sites in increasing additive order. At a site $z$ assign each outcome probability $w_{\epsilon\delta}(z)$ and attach the vector $(1,\Re F(x),\Re R(y))$ to its chosen cell. After each new site, preserve all four three-vector totals of the processed fractional allocation, and preserve each site's probability sum. Freeze integral allocations permanently. In the remaining supports, the affine space respecting each site's sum has dimension $\sum_z (s_z-1)$, with $s_z$ the number of its positive outcomes. The four three-vectors impose at most nine additional independent linear equations since the sum across the cells is fixed. Whenever $\sum(s_z-1)>9$, move along a nonzero kernel direction until a positive coordinate reaches zero. After finitely many eliminations at most nine sites are fractional. At the end assign those sites any of their supported outcomes. For each earlier prefix all allocations integral at that time have stayed fixed. Its discrepancy from its prescribed totals comes from at most nine sites, each changing each real component by at most one. Taking differences of prefixes and allowing wrap gives the assertion, simultaneously for all cosets. This construction exchanges the two-seed arithmetic form for a sharper pointwise rounding bound.

## Subfield obstruction and finite checks

At field order $s^2$ for odd primes $s\to\infty$, the genuine plus row is uniform on the annihilator $C$ of $\mathbb F_s^\times$ in $\widehat Q$. It has $a=2/(s+1)$ and $b=1/(s-1)$. For every nonzero $j\in C$ the conditional law at $-j$ is exactly $\delta_j$: the aligned support of the opposite row on $C$ consists only of its mark. Thus $T=U=\Re j$ gives the largest possible parent response $D_q=a$ and $D_r=0$. Use the full field with no third restriction and fixed probes $u,v$. The unweighted and four weighted counts still have proportions $1/16$ and $1/64+O(1/s)$ of the field (with an $O(1/s)$ error for the former as well), by the distinct-root multiplicative Weil estimate over $\mathbb F_{s^2}$. But $F$ vanishes on every match: $F(x)\ne0$ would put $z$ and then $y$ in the subfield. There $y$ could not be in $D_-$. The actual $R(y)=2/(s+1)$ on all matches. Each of the four genuine signed prices therefore tends to $1/32$. The prime main term (3) for $\epsilon=+1$ would tend to $-3/32$. In this square control even a conditional atom of mass one gives equal quarter-prices. [Genuine subfield pair](parallel-witness-6.md#the-four-coordinates-have-independent-limiting-support)

The [384-bit replay](astra-affine-90-check.py) reconstructs both optimizing rows at $53,257,409$, using a feasible odd perturbation of the minus row at the last two primes. It checks the two own conditional responses, both zero opposite responses, convolution columns against the measured strict interval price in all four cells, and all $53^2$ additive seeds against their predicted first and second moments at $53$. At $409$ the responses $D_q,D_r$ are respectively in $(0.014426774,0.014426775)$ and $(0.018289244,0.018289245)$. Scaling both scores by a factor in $(0.230979244,0.230979245)$ cancels the predicted $+,-$ bracket. For probes $(2,3)$ the measured weighted price of that cell is still in $(0.002945407,0.002945408)$ on the checked interval and index-two coset. The checker enumerates the four actual weighted prices over $11^2,19^2,43^2$ as well. [Outward records](astra-affine-90-checks.jsonl)

## Remaining tests

1. On a fixed gap with a nonzero conditional atom, compare the true first prices of the two sharp pieces separated by its parent score on one macroscopic interval and one bounded-index third coset. Equality up to $o(1)$ on a positive proportion of joint draws would contradict (2)–(3) on that sequence. Cancellations obtained by tuning (4) on one piece alone do not imply that equality.
2. On a fixed gap with $m_q+m_r=o(p^{-1/2})$, seek a comparison on the entire affine coset or allow endpoint tests with increasing Fourier norm large enough to resolve the actual exterior rows. Formula (4) gives the exact loss for norm one. The arithmetic estimate (1) still applies at norm product $B$ with $B E_A=o(1)$.
