# Jacobi endpoint concentration in critical frequency sets

Let $q\equiv1\pmod4$ be a finite field order, $Q$ its nonzero squares and $n=|Q|$. Let $S\subseteq\widehat Q$ have size $m$. With $s(a)=\chi(1-a)$ for the quadratic character $\chi$ and $\lambda=Fs$, define its mean Jacobi deficit and additive energy by

$$d(S)=\frac1{m^2}\sum_{i,j\in S}\left(1-\frac{|\lambda_{i-j}|^2}{q}\right),\qquad
E(S)=\sum_h r_S(h)^2,\quad r_S(h)=|\{(i,j)\in S^2:i-j=h\}|.$$

The [smallest-support argument](subgroup-modes.md#arbitrary-sets-at-the-smallest-possible-scale) gives $d(S)\to0$ if a real unit mean-zero approximate null vector of the stationary linearization is asymptotically concentrated on $S$ and $m\sim n/\sqrt q$. Here are additional restrictions on such a set and vector.

## Repeated differences are necessary

For $0<t\le1$, put $L_t=\{h:1-|\lambda_h|^2/q\le t\}$. If $\alpha$ is a lift of a nontrivial character $h$ of $Q$, inserting the square indicator gives $\lambda_h=(J(\alpha,\chi)+J(\alpha\chi,\chi))/2$. Inversion of the summation variable and $\chi(-1)=1$ give $J(\alpha\chi,\chi)=J(\bar\alpha,\chi)=\overline{J(\alpha,\chi)}$. Hence $\lambda_h/\sqrt q$ is the common real part of the two normalized sums. The phase condition defining $L_t$ consists of arcs of total length $O(\sqrt t)$ about $1$ and $-1$. Xi's uniform discrepancy bound for one fixed character gives

$$|L_t|\le C n(\sqrt t+q^{-1/4}).$$

The two excluded full characters only affect the marked mode and can be absorbed in the bound. This estimate is valid at prime and square orders. [Xi, *Equidistributions of Jacobi sums*, Theorem 1.1](https://arxiv.org/abs/1809.04286)

The deficit counts pairs with differences outside the cap: $\sum_{h\in L_t}r_S(h)\ge (1-d(S)/t)m^2$. By Cauchy–Schwarz this gives, for $t>d(S)$,

$$E(S)\ge \frac{(1-d(S)/t)^2m^4}{Cn(\sqrt t+q^{-1/4})}.$$

In particular, when $m\sim n/\sqrt q$, $d(S)\to0$ forces $E(S)/m^2\to\infty$. More quantitatively, for $d(S)\le1/2$ take $t=2d(S)$ to get $E(S)/m^2\gg(\sqrt{d(S)}+q^{-1/4})^{-1}$ at this scale. This excludes all families of frequency sets with energy at most a fixed multiple of $m^2$.

In fact nearly every pair in a hypothetical smallest-support mode has a difference with growing multiplicity. For any $M\ge1$,

$$\frac1{m^2}\sum_{h:r_S(h)\le M}r_S(h)
\le\frac{d(S)}t+\frac{CMn}{m^2}(\sqrt t+q^{-1/4}).$$

At the critical scale, take $q\to\infty$, then $t\downarrow0$, for any fixed $M$. A growing threshold $M$ is also allowed if $M\sqrt{d(S)}\to0$ and $Mq^{-1/4}\to0$, by choosing $t$ with $d(S)\ll t\ll M^{-2}$. Placing a fixed positive proportion of $S$ in a bounded-doubling set by a standard additive-energy argument would require a bound at the scale of $m^3$.

## One sign on the support

Let $y$ be a real unit mean-zero vector, $\|Hy\|_2\to0$, $\|P_{S^c}y\|_2\to0$ and $m\sim n/\sqrt q$. The compression proof gives $K_S=\sigma P_S y(P_S y)^{\mathsf T}+o_{\rm F}(1)$ for a sign $\sigma$, possibly depending on the field. Let $a_i\in\{\pm1\}$ be the signs of $y_i$ on $S$, choosing either sign at a zero. Flatness in magnitude gives $P_S y=m^{-1/2}a+o_{\ell_2}(1)$. Therefore

$$\frac1{m^2}\sum_{i,j\in S}\left|\frac{\lambda_{i-j}}{\sqrt q}-\sigma a_i a_j\right|^2\longrightarrow0.$$

Thus a candidate has a nearly rank-one sign pattern as well as the repeated-difference requirement. In particular, the product of the three signs on a uniformly sampled triangle in $S$ equals $\sigma$ for a proportion tending to one. Further, on $S$, $K_S P_S y=\sigma P_S y+o_{\ell_2}(1)$ and $P_S Ky=P_S Dy+o_{\ell_2}(1)$ by the near-null equation and its mean correction bound. Consequently

$$\frac1m\sum_{i\in S}|D_i-\sigma|^2\longrightarrow0.$$

At the true smoothing diagonal, $D_i=(A_i-B_i)/(A_i+B_i)$. Thus $A_i/B_i$ grows without bound on almost all of $S$ when $\sigma=+1$, with $B_i/A_i$ taking that role when $\sigma=-1$. For an exact eigenvector of $H$ with eigenvalue $\zeta\ne0$ tending to zero, the sign of $\zeta$ is also $\sigma$ for all sufficiently large orders along this configuration. Indeed $\|P_\perp Dy\|^2=1-2\zeta\langle Ky,y\rangle+\zeta^2\le1$ and $\langle Ky,y\rangle=\sigma+o(1)$.

## Translations that almost preserve a critical set

For a critical-scale near-null vector as above, let $r(h)=|S\cap(S+h)|/m$. Fix any $1/2<c<1$. Uniformly over the shifts with $r(h)>c$, we have $r(h)=1-o(1)$. Thus for large orders $G=\{h:r(h)>c\}$ is an exact subgroup, and $S$ differs from a union of $G$-cosets by $o(m)$ entries.

To prove the overlap restriction, normalize the truncation of $y$ to $S$ to get a unit vector $x$. Then $K_{SS}=\sigma xx^{\mathsf T}+o_{\rm F}(1)$ and $\|(K-\sigma I)x\|=o(1)$, while $|x|=m^{-1/2}\mathbf1_S+o_{\ell_2}(1)$. Write $z$ for the translate of $x$ by $h$, $T=S+h$, and $I=S\cap T$. Translation invariance gives the same properties for $z$ on $T$. Restricting the two rank-one compression formulas to $I$ shows $\|x_Ix_I^{\mathsf T}-z_Iz_I^{\mathsf T}\|_{\rm F}=o(1)$. Flatness gives $\|x_I\|^2=\|z_I\|^2+o(1)=r(h)+o(1)$, so $|\langle x_I,z_I\rangle|=r(h)+o(1)$. All these errors are uniform in $h$.

On $S\setminus T$, the component $K_{S\setminus T,I}z_I$ has norm $r(h)\sqrt{1-r(h)}+o(1)$ by the compression formula on $S$. Its cancellation partner $K_{S\setminus T,T\setminus S}z_{T\setminus S}$ has norm at most $(1-r(h))\sqrt{1-r(h)}+o(1)$ by the entrywise Jacobi bound. The two must sum to $o(1)$ since $z$ is an approximate eigenvector vanishing there. Thus $(2r(h)-1)\sqrt{1-r(h)}\le o(1)$, which gives $r(h)=1-o(1)$ uniformly on $G$.

The symmetric-difference triangle inequality gives $1-r(h+k)\le(1-r(h))+(1-r(k))$, so $G$ is closed under addition. It contains zero and is closed under inversion. Averaging $|S\triangle(S+h)|$ over $h\in G$ gives $2\sum_C |G|\rho_C(1-\rho_C)=o(m)$, where $\rho_C=|S\cap C|/|G|$ and $C$ ranges over its cosets. Rounding every $\rho_C$ to the nearest of $0,1$ changes at most that many entries, which proves the claim.

For the energy $E(S)=m^2\sum_h r(h)^2$, summing $r(h)^2\le r(h)$ on $G$ and $r(h)^2\le c r(h)$ off $G$ gives

$$\frac{E(S)}{m^3}\le c+(1-c)\frac{|G|}{m}.$$

If $E(S)\ge(1/2+\delta)m^3$ for a fixed $\delta>0$, taking $c\in(1/2,1/2+\delta)$ gives $|G|\gg_\delta m$. The union approximating $S$ then uses only boundedly many cosets. If $E(S)/m^3\to1$, the same inequality and $\sum_h r(h)=m$ give $|G|/m\to1$, and $S$ differs from a single coset by $o(m)$ entries. The available repeated-difference lower bound still permits much smaller energy.

## Numerical search over arbitrary supports

The [critical-set probe](../critical_sets.py) searches for small $d(S)$ at $m=\lceil n/\sqrt q\rceil$ using interval seeds, greedy growth from strong Jacobi differences, and single swaps. Uniform samples and subgroups of order $m$ serve as baselines. The search permits arbitrary supports and records the energy of each set and the norm of the signed compression. Reported scores are attained values from a heuristic search. The square-field subgroup gives the exact control values $d(S)=m^{-1}(1-1/q)$ and $E(S)=m^3$.

The table compares selected orders from the [full CSV](../data/critical-sets.csv). The maximum compression norm is taken over the same candidates, and can come from a different support than the minimum deficit. The norms and deficits in the CSV use floating point.

| Field order | $m$ | Lowest deficit found | $E(S)/m^2$ at that deficit | Highest norm found |
|---|---:|---:|---:|---:|
| $97^2$ | 49 | 0.020406 | 49 | 0.98958 |
| $9413$ | 49 | 0.304885 | 3.52728 | 0.24039 |
| $193^2$ | 97 | 0.010309 | 97 | 0.99479 |
| $37253$ | 97 | 0.349975 | 2.91476 | 0.16572 |
| $389^2$ | 195 | 0.005128 | 195 | 0.99742 |
| $151337$ | 195 | 0.381834 | 2.63934 | 0.14193 |
| $1000033$ | 501 | 0.420173 | 2.54854 | 0.08655 |

Greedy growth followed by swaps found the smallest deficit at each tested prime. At $p=1000033$, a contiguous interval has much stronger repetition, with $E(S)/m^2=334.00$ and a deficit of $0.486329$. The square controls combine higher repetition and smaller deficits than the prime candidates with the lowest deficits.

The [progression compression bound](progression-gap.md) excludes slow modes on intervals and their subsets at this scale, including many sets with energy of order $m^3$.
