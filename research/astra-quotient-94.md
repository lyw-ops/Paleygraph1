# A forbidden pentagon and recurrent occupancy on a bounded family of critical cosets

Let $p\equiv1\pmod4$ be prime, $Q=\mathbb F_p^{\times2}$, $n=(p-1)/2$, and $B\le Q$ have odd order $b\ge1500$. If $\sqrt p/b\le18/25$, then for **each sign** the forbidden Cayley graph on $B$ contains a triangle or a five-cycle. In particular
\[
                  \Theta_\sigma(B)/b\le 1/\sqrt5.
\]
This includes every odd-order critical subgroup on the trapped physical branch of [round 93](astra-coset-93.md). It also applies to subgroups in the stated size range without assuming that their restricted theta nearly realizes the full theta. When $5\nmid b$ the upper is separated from $1/\sqrt5$ by an absolute positive constant at all sufficiently large orders. A separate restriction below bounds the number of possible critical cosets across *all* admitted physical pins at the same prime, once a positive shortfall mass is fixed.

## Five forbidden factors

Write $s(x)=\chi(1-x)$, $F=\{x\in B:s(x)=-\sigma\}$, $f=|F|$, $c=\chi(2)$, and $F^{1/2}=\{x\in B:x^2\in F\}$. The sets $F,F^{1/2}$ are disjoint in the absence of a forbidden triangle, since $1,x,x^2$ are distinct for nontrivial $x\in B$. Squaring is bijective, and $s(-x)=s(x)s(x^2)$ for $x\ne1$. Thus
\[
 \sigma\sum_Bs(x)=b-1-2f,\qquad \sum_Bs(-x)=b-1-4f+c.
\]
For any character $\psi$ of $B$ let $S_\psi,T_\psi$ be the corresponding sums of $s(x)\psi(x)$ and $s(-x)\psi(x)$. They are real by inversion. Extending $\psi$ in the two ways to $B\cup(-B)$ gives $S_\psi\pm T_\psi$. Completion by all multiplicative character extensions bounds their absolute values by $\sqrt p$ using the complete Jacobi bound. Hence $|S_\psi|+|T_\psi|\le\sqrt p$. At the trivial character this gives
\[
 f/b\ge [2-\sqrt p/b-(2-c)/b]/6\ge 213/1000=:d_0 .
\]
[Two-layer completion and odd-cycle theta bound](astra-coset-93.md)

If there is also no five-cycle, the five-fold product $F^5$ misses the identity, since a closed odd walk of length five contains an odd cycle of length at most five. Let $J$ stabilize $F^5$. In $B/J\cong\mathbb Z/m$ let $A$ be the image of $F$ and $k=|A|$. The five-fold sum $5A$ is aperiodic and misses zero. Kneser's theorem gives $5k-4\le |5A|\le m-1$. This follows also by iterating the two-set theorem since the stabilizer of each intermediate sum is contained in the final stabilizer. The capacity of the occupied cosets gives $k/m\ge d_0$. The inverse symmetry of $A$, the absence of zero, and odd $m$ make $k$ even. Therefore
\[
                          5k-3\le m\le k/d_0,\qquad k\in\{2,4,6,8\}.
\]
The entire quotient classification is small. For each possible $m$, run over the $k/2$-element subsets of $\{1,\dots,(m-1)/2\}$, adjoin their negatives, form five sums, and retain only the sets whose five-fold sum misses zero and has trivial stabilizer. Reduce by multiplication by all units. The second column of the table gives *all* resulting possibilities, with their negatives understood. The [integer classification and interval certificate](astra-quotient-94-check.py) implements these loops. [Kneser's theorem](https://arxiv.org/abs/1303.3539)

For $j=(m-1)/2$ inflate $\psi(x)=e^{2\pi i j x/m}$ from the normalized quotient coordinates. Let $h=2^{-1}j\bmod m$, the exponent of its unique square-root character $\xi$. Both are nontrivial. The nontrivial analogues of the two sums give
\[
 \sigma S_\psi=-1-2\sum_F\psi,\qquad
 T_\psi=c-1-2\sum_F(\psi+\xi).
\]
For each listed positive residue $z$ put $u_z=|F\cap(\pm z+J)|/b$, using the union of both cosets, and let $v_z=-4\cos(2\pi jz/m)-2\cos(2\pi hz/m)$. Inversion gives $\sqrt p/b\ge\sum_z u_z v_z-3/b$. Each $u_z\le2/m$, and $\sum_z u_z\ge d_0$. All $v_z$ are positive. The last column rounds down the bound $(2/m)\sum_z v_z-(k/m-d_0)\max_z v_z$ for their weighted sum.

| $m$ | Positive representatives | $j$ | $h$ | Lower bound |
| ---: | --- | ---: | ---: | ---: |
| 7 | 1 | 3 | 5 | 0.862419 |
| 9 | 1 | 4 | 2 | 0.726643 |
| 17 | 1, 3 | 8 | 4 | 0.817337 |
| 27 | 1, 3, 5 | 13 | 20 | 0.807938 |
| 37 | 1, 3, 5, 7 | 18 | 9 | 0.805593 |

Every lower bound exceeds $18/25+3/1500$, a contradiction. Testing a forbidden triangle gives $\Theta_\sigma(B)/b\le1/3$, and a forbidden five-cycle gives $\cos(\pi/5)/(1+\cos(\pi/5))=1/\sqrt5$. On the trapped larger-side branch $b\ge(2-o(1))na$ with $a\sqrt n\ge1+\delta$, so $\limsup\sqrt p/b\le1/[\sqrt2(1+\delta)]<18/25$. Together with the even-order theorem of round 93, every trapped primary cubic satisfies
\[
 \alpha \le \frac{1}{t\sqrt5}\frac{|P\cap C|}{|K|}+o(1).
\]
For even $b$ and the plus sign one retains $1/(3t)$. The index $t=[K\cup C:K]$ distinguishes the order-two translate.

## A simultaneous physical restriction at all admitted lengths

Fix one full primary optimizer $x$ of mark $a$ and a cutoff $0<s<1$. Let $\mathcal C_s(x)$ consist of every self-inverse coset $C$ of a subgroup of $G=\widehat Q$ with $x(C)\ge s$ and $|C|\le2/a$. This list uses one primary optimizer, chosen before any terminal time, length or tested quartic minimizer. There is a bound independent of the factorization of $n$,
\[
            |\mathcal C_s(x)|\le N_s:=2\lceil2/s^2\rceil\lfloor4/s^2\rfloor^2 .       \tag{1}
\]
Indeed take a maximal subfamily of $M$ cosets whose distinct pairs intersect in fewer than $s^2/(2a)$ points. For $V$ drawn with law $x$, the number $Y$ of these cosets containing $V$ satisfies
\[
 (Ms)^2\le (\mathbb EY)^2\le\mathbb EY^2\le M+M(M-1)s^2/2
\]
by the common point cap $x_i\le a$. Thus $M\le2/s^2$. Every coset outside the subfamily intersects one selected coset in at least $s^2/(2a)$ sites. This intersection is a coset of the intersection subgroup $I$, so the index of $I$ in *each* of the two subgroups is at most $4/s^2$. The new order is the selected order multiplied by a ratio of two integers of that size. In a cyclic group each order fixes the subgroup and admits at most two self-inverse cosets. The selected cosets themselves are covered using the ratio one. This proves (1).

For each $C\in\mathcal C_s(x)$ let $K$ be its subgroup, $L=K\cup C$, $t=[L:K]$, $B=L^\perp$ and $c_C=\Theta_\sigma(B)/(t|B|)$. Take any finite nonempty family of admitted physical pins $j$ with true masks $P_j$, and any probability weights $\pi_j$ on them. Write
\[
 H(i)=\sum_j\pi_j1_{P_j}(i),\qquad U_j=\max_{C\in\mathcal C_s(x)}
                                  c_C\frac{|P_j\cap C|}{|C|},
\]
taking every maximum over an empty coset family, including the last maximum in (2), to be zero. A single physical pin in the support of $\pi$ satisfies
\[
 \min_{j:\pi_j>0} U_j
 \le \sum_j\pi_j U_j
 \le \sum_{C\in\mathcal C_s(x)}c_C\mathbb E_C H
 \le N_s\left(\lambda+\max_{C\in\mathcal C_s(x)}
                         \Pr_C\{H\ge\lambda\}\right)                     \tag{2}
\]
for $0<\lambda<1$, where $\mathbb E_C,\Pr_C$ use the uniform law on $C$. The middle sum retains each *actual restricted theta*. One proves it by replacing the maximum by the sum and interchanging finite averages. The last step uses $0\le c_C,H\le1$. At a common terminal time and growing dyadic lengths one can use only the [simultaneously admissible lengths](astra-persistent-88.md) with the original sparse counting and inverse-leverage conclusions. Formula (2) also applies to the [many good terminal times](terminal-height-79.md) with start one and lengths comparable to the full marked depth.

To connect the finite selector to the trapped branch, fix a target mass $\zeta>0$ and choose $s=\zeta/2$. If the pin minimizing $U_j$ is trapped with $\alpha\ge\zeta$, then its critical $C$ belongs to this same list eventually. Indeed the [universal primary contact](astra-coset-93.md) gives $x(P_j\cap C)=(1-o(1))a|P_j\cap C|=\alpha+o(1)$. Its order is at most $(1+o(1))/a$ by the cap saturation of the minimizing row. The joint formula gives $U_j\ge\alpha-o(1)$. All asymptotic uses here concern only the *one selected sequence* of pins, so no uniform error assumption across an increasing number of quartic solutions is needed.

In particular, if this selected pin is trapped at mass $\zeta$, then eventually one fixed candidate $C$ at each prime has both $c_C\ge\zeta/(2N_s)$ and $\mathbb E_C H\ge\zeta/(2N_s)$, by the middle bound in (2). A fraction at least $\zeta/(4N_s)$ of its sites belong to masks of total time weight at least $\zeta/(4N_s)$. For the uniform family of good terminal times $T\asymp D(p)$, those same sites have true exterior companion height $\ge(2T-1)\delta/8\gg_\delta D(p)$ at a positive fraction of the times, using the common start one. The sites and coset can depend on the prime. A vanishing upper for the recurrent-site fraction at each fixed positive time fraction on this bounded list would therefore remove the trapped branch at one admitted pin. A single-time global counting bound gives no such upper on a critical coset of order comparable to $\sqrt n$.

## Stability under deleting generators and a strict gap in the absence of fifth roots

Let $b\ge3000$ and $\sqrt p/b\le18/25$. Delete any inversion-symmetric set of $e\le b/10000$ generators from $F$, obtaining $F'$. Then the surviving Cayley graph still has a triangle or a pentagon. Indeed if there is neither, define $s'$ on $B$ by its new forbidden indicator, leaving the value at 1 zero. Define the other layer by $t'(x)=s'(x)s'(x^2)$ off the identity and $t'(1)=c$. The original character sums change by at most $2e$ and $4e$, since squaring is bijective. Their new sum of absolute values is at most $\sqrt p+6e$. All the algebra used above now applies to $F',s',t'$. Its density is at least $(2-18/25-6/10000-3/3000)/6>213/1000$. The least last-column value minus $3/3000$ still exceeds $18/25+6/10000$. This proves the assertion for the true sign graph after the stated deletion.

There is consequently an absolute $c_*>0$ such that the original graph has at least $c_*b^4$ distinct simple oriented pentagons rooted at 1 for all sufficiently large eligible orders, including graphs with triangles. Otherwise the ordered solutions of $x_1\cdots x_5=1$ with $x_i\in F$ would be $o(b^4)$ along a subsequence. The nonsimple walks cost $O(b^3)$ because a repeated vertex forces a proper consecutive block to have product one, independently of the full product equation. The arithmetic removal lemma for one equation then removes $o(b)$ elements from each copy of $F$ to destroy all solutions. Removing the union and its inverse deletes a symmetric $o(b)$ generators. A surviving pentagon gives a solution, and a surviving triangle also gives one by appending an inverse pair, contradicting resilience. [Král’, Serra and Vena, removal lemma for groups](https://arxiv.org/abs/0804.4847)

The following theta restriction uses only the explicit deletion result. Let $c_5=\cos(\pi/5)$, $w=\Theta_\sigma(B)/b$, and $v$ be any optimizing probability on $\widehat B$ rooted at the trivial character. For triangle-free forbidden graphs put
\[
 {\cal M}=\{\psi\ne1:5\mid{\rm ord}(\psi),\ {\rm ord}(\psi)\le10^6\}.
\]
There is an absolute $\Delta>0$ such that
\[
 v\bigl(\widehat B\setminus(\{1\}\cup{\cal M})\bigr)
 \le \frac{20}{\Delta}\,[c_5-(1+c_5)w].                                  \tag{3}
\]
In particular any sequence approaching $w=1/\sqrt5$ carries all but $o(1)$ of its nonroot mass on bounded-order characters divisible in order by five. On $5\nmid b$ the left side equals $1-w$, giving an absolute strict gap. If a triangle is present the stronger direct bound $1/3$ applies.

To prove (3), iteratively choose a simple pentagon rooted at 1 and delete all of its step generators and their inverses, at most ten generators per choice. As long as at most $b/10000$ have been deleted, resilience gives another pentagon since triangle-freeness is preserved. This supplies at least $b/100000$ pentagons whose first-step generators are distinct. Let $A_5$ be the adjacency matrix of a five-cycle. On a rooted ordered pentagon with vertices $x_0=1,x_1,\ldots,x_4$ put $z_j=\psi(x_j)$. Then $z^*A_5 z+10c_5\ge0$ on the unit torus. Equality requires $z$ in the least eigenspace, hence $z_j=u e^{4\pi\mathrm i j/5}+v' e^{-4\pi\mathrm i j/5}$. Constancy of $|z_j|^2$ kills its nonconstant discrete Fourier coefficient $u\overline{v'}$, and $z_0=1$ makes $z$ one of the two pure windings. In particular the phase of $z_1$, in turns, is $\pm2/5$.

Fix the angular radius $\rho=10^{-8}$ in turns. Define $\Delta$ as the minimum of $z^*A_5z+10c_5$ over vectors with $|z_j|=1$, $z_0=1$, and first-step phase at distance at least $\rho$ from both windings in $\mathbb R/\mathbb Z$. Compactness and the equality characterization give $\Delta>0$. For each chosen pentagon the average of $z^*A_5 z$ against $v$ is zero by the forbidden moment at every edge. The trivial character contributes $10w$. Thus the unnormalized nonroot expectation of $z^*A_5z+10c_5$ equals $10[c_5-(1+c_5)w]$.

For a character of order $m>10^6$, at most $b(4\rho+2/m)<b/200000$ generators in all of $B$ lie in the two first-step arcs, by counting equally spaced phases. For $m\le10^6$ with $5\nmid m$ even the nearest phase is at least $1/(5m)>\rho$ away. Therefore every nonroot character outside $\mathcal M$ costs at least $\Delta$ on at least half the packed pentagons. Averaging the preceding expectation proves (3). The constant defined here yields a structural separation. The proof does not estimate a useful numerical gap.

## Physical replay and next estimates

At $p=97$ take the genuine plus optimizer at the two zero anchors, $s=7/50$, the terminal time eleven, and the three physical masks at lengths two, four and eight. Nine self-inverse cosets meet the finite order and mass tests. The largest actual joint score on the whole list is precisely $1/4$ at length two. At both longer lengths it lies between $0.097630$ and $0.097632$. Sites eight and forty belong to all three masks. The finite replay uses repaired rational certificates on each restricted graph and Arb384 for the physical mask and primary face. These values illustrate the selector at a fixed field. [Checker](astra-quotient-94-check.py) · [Two records](astra-quotient-94-checks.jsonl)

1. On the many good terminal times with start one, bound the proportion on each of the $O_\zeta(1)$ candidate cosets where the genuine exterior companion exceeds a fixed multiple of $D(p)$ for positive time density. Even an upper tending to zero at each fixed time-density threshold suffices in (2), even for arbitrarily high exceptional sites.
2. On the surviving odd-order triangle-free subgroups, use the actual five-cycles in the restricted theta LP. By (3) it suffices near equality to test the finitely many bounded-order characters divisible in order by five. Show that even these are incompatible with the actual pentagons when $5\mid b$, or exploit the resulting bounded-character support of the quotient optimizer. Smaller positive mass, finite-power escape, and the all-prime ordinary theta limit remain open.
