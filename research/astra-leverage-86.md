# Marked leverage on the original terminal mask

At one good time, the high-density alternative of [round 83](astra-split-83.md) forces a tower-scale loss of positive marked leverage on the original terminal mask even if the frozen Jacobi head is discarded. It also forces a signed interpolation loss on a specific exposed subface. Conversely a moderately large positive leverage forces the actual pin price on one genuine row to survive every deletion of nearly linear size, at optimized coordinates of density at most a power of an iterated logarithm. Neither conclusion supplies an all-prime upper on the surviving price.

## A price supported on the actual hinge source

Use the fixed larger-side gap, time, and notation of [round 83](astra-split-83.md). In particular $P=\{i\ne0:R_i<-u\}$, $h=Z1_P$, $M=1-a$, $\gamma=\sqrt n a=O(1)$, and $H$ is the specified half-height tower. Fix any genuine opposite optimizer $r^*$, with zero set $S$ on the exterior. Use the exact signed marked space of [round 85](astra-overflow-85.md), supported on $I=\{0\}\cup S$ with root weight $a^2$. Write its marked section as $x_0=1$, $y_i=\sqrt{w_i}x_i$. Every such signed $y$ has mass one and root $a$. Its nonnegative rows are exactly the genuine maximizing face $\mathcal Q_a$.

In the high-density alternative let $q^*$ be the squared-hinge minimizer, $v$ its normalized hinge, $F=\{v_i>0\}\subset S\cap P$, $m=1/\sum v_i^2$, and $\rho M=\sqrt n\langle v,q^*\rangle$. For any erased $A\subset F$ set $f_i=\sqrt n\,v_i1_{F\setminus A}(i)$ and $\beta_A=\min_{q\in\mathcal Q_a}\langle q,f\rangle$. The first variation at $q^*$ and the true point cap give
\[
 \beta_\varnothing=\rho M,\qquad
 \beta_A\ge\rho M-\gamma\sum_Av_i
         \ge\rho M-\gamma\sqrt{|A|/m}.                                      \tag{1}
\]
Only assume $w_i\le d/[n(1+h_i)]$ on $F\setminus A$. All other exterior weights can be arbitrary positive numbers. Since $h_i>(2d-1)u$ there, $D_f=\sum w_i f_i^2\ll_\delta m^{-1}$. Cauchy–Schwarz on the exterior of every genuine row yields
\[
 \ell_+\le {D_f\over D_f+\beta_A^2}\ll_\delta (\rho^2m)^{-1}
         \ll_\delta H^{-3/2}
 \quad\text{if}\quad |A|\le {\rho^2 M^2m\over4\gamma^2}.                    \tag{2}
\]
Here the last step uses the actual high-alternative lower $\rho^2m\gg_\delta H^{3/2}$. The first fraction assumes $D_f>0$, as holds under the displayed cardinality bound. In fact $n\sum_{F\setminus A}q_i^2\ge m\beta_A^2$ for every genuine optimizer, directly by (1). Thus the estimate survives freeing a constant multiple of $\rho^2m$ originally charged coordinates, deleting all head charges, and changing the entire uncharged metric. The conclusion uses the time at which the hinge was computed.

The constraint has a signed consequence on a support which can be selected from true data. Write $\mathcal F_A=\{q:\langle q,f\rangle=\beta_A,\ q\in\mathcal Q_a\}$ and let $I_A$ be the union of its supports. Every signed normalized row supported on $I_A$ has $\langle y,f\rangle=\beta_A$. Indeed a relative interior point of $\mathcal F_A$ is positive on $I_A$, so a sufficiently short segment from that point in either sign of any zero-root supported tangent is feasible. Minimality kills its $f$-derivative. Therefore the **ordinary** signed leverage restricted to $I_A$ satisfies the first upper in (2). For $A=\varnothing$, $I_A$ includes the support of the actual hinge minimizer.

For a price on the unrestricted signed row let $U$ be an attaining opposite LP minorant $U_i\le f_i$ on $S$, $\overline U-aU_0=\beta_A$. This follows from the exact complementary moment system in [round 84](astra-capacity-84.md). Its slack $s_i=f_i-U_i\ge0$ vanishes throughout $I_A\setminus\{0\}$. For every signed normalized marked row,
\[
 \sum_S(y_i)_-s_i
 \ \ge\ \beta_A-\langle f,y\rangle
 \ \ge\ \beta_A-\sqrt{D_f}\,(\|x\|^2-1)^{1/2}.                              \tag{3}
\]
In particular the canonical signed row of leverage $\ell$ pays $(1-o(1))\beta_A$ on negative coordinates outside $I_A$ whenever $\ell\rho^2 m\to\infty$ under (2). Equivalently, with $L$ the full signed projector, $e$ the root vector and exterior vectors extended by zero there, $L(\beta_A e+Ws)=LWf$. The physical pin multiplier from round 85 still applies to the very same $y$ with its original bound when the height caps are retained on all of $S\cap P$. Once some caps are freed, (1)–(3) continue to hold, and the pin error must use the newly chosen weights. If the initial signed leverage is large, restricting a feasible-elimination path entirely down to $I_A$ retains a fraction at most $O_\delta(1/(\ell\rho^2m))$ of its initial leverage, even though this subface contains genuine rows.

## Deleting nearly a linear number of sites under a masked collision bound

Keep the same good time with $d\asymp D(p)$ and $B=0$ in the [round-79 terminal band](terminal-height-79.md). Write $r_i=(-R_i)_+$ on the exterior, with $r_0=0$, and $I(q)$ for its joint density, deficit and height band. Let $K\ge2$ satisfy $\log_2^*K\le(7/8-\xi)\log_2^*p$ for fixed $\xi>0$. Take $U_p$ to dominate $K,D$ and the supremum budget of the three finite cold approximants below. One may use $U_p=\max(2,\log_2\log_2 p)$, any fixed further iterated logarithm eventually, or the smaller actual resource bound. The same growing-depth arithmetic approximation used in round 79 gives a **single nonnegative** majorant up to an error on the exterior,
\[
        r\le (C/d)(U_p+E),\qquad E\ge0,\qquad \|E\|_{2,n}=o(1/K).             \tag{4}
\]
To see this, use round 79 (3) with its three neighboring true $Y_j$. Bound their approximants by their supremum and take $E$ to be the sum of the three absolute approximation errors. The per-step error $(K+D)^{-4}$ gives the claimed second norm by [the shortened tower construction](trimmed-mellin-77.md#the-cold-approximation-at-the-shorter-horizon). The resource tower has iterated logarithm at most $\max(\log_2^*K,\log_2^*D)+D/8+O(1)$ with $D\le\log_2^*p+O(1)$ as used in round 79. The growing margin $\xi\log_2^*p-O(1)$ places it below any fixed further iterated logarithm eventually. All site choices below may depend on the true row and terminal time. This is the same physical approximation principle as [round 83’s high/low deletion](astra-average-83.md#nearly-linear-deletion-on-the-other-part). Here the admissible precision is set by the observed local collision or ordinary signed interpolation energy.

For any genuine $q$ and any $L\subseteq P$ with local collision $n\sum_Lq_i^2\le K^2$, (4) implies
\[
 q(r1_L)\ \le\ (C/d)\left(U_p K\sqrt{|L|/n}+o(1)\right).                     \tag{5}
\]
In particular, on *every* subset of $P$ of size at most $n/U_p^6$ carrying a fixed positive fraction of the pin deficit, the local collision must exceed $K^2$ for all sufficiently large primes. The same local estimate can be applied regardless of collision away from $L$.

Suppose now that $n\sum_P q_i^2\le K^2$. The high-density tail $D_q=\{i\in P:nq_i>U_p^4\}$ has $q(D_q)\le K^2/U_p^4$. By (4) its deficit costs at most $(C/d)(U_pK^2/U_p^4+o(1))=o(1)$. For every deletion $L$ with $|L|\le n/U_p^6$, apply (5) on $L\cap P$ and excise $D_q$ as well. For $J=I(q)\setminus(L\cup D_q)$ the original terminal theorem and pairing now give
\[
       q(r1_J)\gg_\delta1,\qquad q(Z1_J)\gg_\delta d,\qquad
       n\sum_J q_i^2\gg_\delta d,\qquad k_\delta d<nq_i\le U_p^4\ (i\in J).
                                                                            \tag{6}
\]
For the collision lower use $\|r\|_{2,n}\ll_\delta d^{-1/2}$. Also $q(J)\gg_\delta d/U_p$ by (4), whence $|J|\gg_\delta n d^2/(U_p^2K^2)$ by Cauchy–Schwarz. These conclusions apply to one and the same genuine row against all deletions.

To obtain a test solely in terms of leverage, keep height caps on all $S\cap P$ and take the positive minimizing row. Its masked collision is at most $C_\delta(1/\ell_+-1)$ since $nw_i\ll_\delta1$ on $P$. Consequently (6) holds on this row if $1/\ell_+\ll_\delta K^2$, after enlarging the approximation parameter by a fixed factor. In particular a lower $\ell_+\gg_\delta H^{-1}$ for the terminal-only metric at one good time would exclude the high-density branch by (2) and localize the surviving terminal charge according to (6), with $K\asymp_\delta \sqrt H$. This threshold suffices for the branch selection. An upper $o(d)$ on the price remaining in (6) would still be needed to exclude the fixed gap this way.

## Amplification on the high-paying part of the selecting row

In fact the source in (1) forces a much stronger all-face loss than the half-height tower estimate in (2). In the high-density branch, $G=I(q^*)\cap\{q_i^*>2t\}$ pays fixed deficit, where $t=H^{-1/4}M/\sqrt n$. Thus $|G|\le1/(2t)=O(\sqrt n H^{1/4})$ by mass. For every precision tower $K$ admitted above, (4) and $K,U_p,H\le\max(2,\log_2\log_2 p)$ (choosing that admissible $U_p$) give
\[
 \|r1_G\|_{2,n}\le (C/d)(U_p\sqrt{|G|/n}+o(1/K))=o(1/(dK)).
\]
Cauchy–Schwarz forces $n\sum_G(q_i^*)^2/(d^2K^2)\to\infty$. Since the actual hinge $z_i=(q_i^*-t)_+1_P$ exceeds $q_i^*/2$ on $G$, and $\langle v,q^*\rangle\ge\sum z_i^2/\sum z_i$, this gives
\[
  {\rho^2m\over d^2K^2}\ \ge\ {n\sum_i z_i^2\over M^2d^2K^2}\longrightarrow\infty,
  \qquad \ell_+=o_\delta\big(1/(d^2K^2)\big).                              \tag{8}
\]
The leverage bound applies with the same erasures and all outside-weight freedom of (2), and also to the signed leverage restricted to $I_A$. Formula (1) now transfers a diverging multiple of $d^2K^2$ in unweighted collision to **every** genuine optimizer on $F\setminus A$, although $G$ was defined using only the selecting row. In particular every deletion of at most $d^2K^2$ source coordinates is permitted eventually. These limits hold along any fixed-gap, high-branch sequence. They place no empirical assumption on actual prime faces.

For a selected time one can use the actual cost $b+2$ of approximating through its three physical iterates instead of the longest prefix. The proof of (4) works whenever $\max(\log_2^*K,\log_2^*D)+b\le(1-\xi)\log_2^*p$ for fixed $\xi>0$. A good time with $b\le D/13+O(1)$ is available in the original round-79 interval: take $B'=\lceil 8J_0/13\rceil+5$ with $J_0=\lfloor D/8\rfloor$. The [prefix energy identity](astra-height-78.md#selection-and-pinning) bounds the number of bad terminals up to $B'$ by $3(B'+2)/16$, since each $g_j>4$ spoils at most three times. There are more candidates than this in $[\lceil J_0/2\rceil,B']$, and $B'\le J_0-2$ eventually. At such an admissible time (4)–(8) allow tower heights up to $(12/13-\xi)\log_2^*p$ for $K$, for fixed positive $\xi<12/13$. Formula (8) at every good time has the original $7/8-\xi$ range. In particular on a high-branch subsequence
\[
 \liminf\frac{\log_2^*(1/\ell_+)}{\log_2^*p}\ge7/8,
 \qquad\text{and the lower bound is }12/13\text{ if }b\le D/13+O(1).
\]
This follows by taking $K$ a tower of any fixed smaller relative height and letting that height increase to the stated value.

## A signed pin test at the weaker interpolation scale

The same density reduction needs only the ordinary projector if both signs of its output are retained. Keep the actual height caps on $S\cap P$. For **any** signed normalized row $y$ with $n\sum_P y_i^2\le K^2$, set
\[
 A_-(y)=\sum_S(y_i)_-(R_i+u)_+,\qquad
 A_{\rm credit}(y)=\sum_S\big[(y_i)_+(R_i+u)_++(y_i)_-(R_i+u)_-\big].
\]
For $|L|\le n/U_p^6$ and $k>0$ let $J_y=\{i\in P\setminus L:kd<ny_i\le U_p^4\}$. At the fixed gap $B_*=aR_0-\overline R-u(1-a)\gg_\delta1$. Uniformly over such $L,y$,
\[
 B_*+A_{\rm credit}(y)
 \le A_-(y)+\sum_{J_y}(y_i)_+(R_i+u)_-+O(k)+o(1).                       \tag{7}
\]
Indeed exact opposite pairing gives equality before dropping any terms of $\sum_P (y_i)_+(R_i+u)_-$. The range $ny_i\le kd$ there costs at most $kd\|r\|_{1,n}=O(k)$. For the deletion and upper-density tail apply (4)–(5) to $(y_i)_+1_P$, whose masked collision is bounded; the tail first norm is at most $K^2/U_p^4$ by its defining density. Neither estimate uses the total mass or the signs off $P$.

For the canonical signed row the collision hypothesis follows from $1/\ell\ll_\delta K^2$, with a fixed rescaling of $K$ as above. Thus if its negative pin price stays below $B_*/2$, for small $k=k_\delta$ its positive sites in $J_y$ pay a fixed deficit and order-$d$ height, after every allowed deletion; the collision and cardinality conclusions in (6) follow on these sites as well. This extends the actual signed price test from $1/\ell=o(d)$ to the larger interpolation-energy regime by accounting for the observable remaining height explicitly. If the hinge-source caps are retained as well, (3) constrains the negative sites of the very same signed row.

## Replay on an actual degenerate optimal face

At $p=97$, time four, use the physical hinge of [round 83](astra-split-83.md), omit the frozen head, and assign weight $4a$ outside the retained terminal mask. On it use the same finite capacity scale $1/5$ and true height cap. The source is positive on the pair $5,43$. Freeing this pair assigns it $4a$ as well, and replaces $f$ by its restriction to the other sites, with the original hinge normalization.

| Freed sites | Exact $\beta_A$ | Ordinary $\ell$ | Positive $\ell_+$ | Source upper in (2) | Negative slack charge in (3) |
|---|---:|---:|---:|---:|---:|
| None | 0.465056922 | 0.776652231 | 0.401277337 | 0.412042379 | 0.401473038 |
| $5,43$ | 0.267562898 | 0.803609545 | 0.512184553 | 0.533332841 | 0.223210659 |

The [Arb384 checker](astra-leverage-86-check.py) reconstructs the cyclotomic complementary supports, true mask and source. Both exact source gradients are strictly positive in the two nonnegative even anchor parameters; the same is true of both weighted norm gradients at their origin. Reflection averaging preserves the source cost and reduces the squared norm. Thus the computed minima hold on the full face. The source-exposed signed root minimizer is also even and lies at the origin of those parameters, giving signed leverage on $I_A$ equal to the displayed positive leverage. In the erased case the point-cap floor from (1) alone is 0.085194407, substantially weaker than the exact 0.267562898. The interpolated slack is supported only on the reflected anchors 10 and 21, each negative in the full signed row. These finite cutoffs do not realize the asymptotic gap hypotheses. [Outward intervals](astra-leverage-86-checks.jsonl)

1. On the actual larger face, test whether the terminal-only inverse positive leverage is $O_\delta(K^2)$ for one of the precision towers in (8) at the chosen admissible time. Such a bound forces the diffuse alternative (6). The same holds for $\ell_+\gg_\delta (dK)^{-2}$ by (8) and by using $dK$ in (6), reducing the fixed tower margin if needed. The source inequality (3) locates exactly where any inexpensive signed row must leave the exposed minimizing support in the high-density branch.
2. In the moderate-collision regime test the actual terminal price on $k_\delta d<nq_i\le U_p^4$ after discarding up to $n/U_p^6$ sites. The exceptional sites can be selected after the row. Against a fixed gap every such deletion must retain order-$d$ companion price.
