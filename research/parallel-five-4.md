# Paired anchors cross the five-point threshold

For the arithmetic reduction of [Randomstrasse101, Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), the critical support overlap improves from $q^{2/5}$ to $q^{3/7}$. The first step counts triples in one actual two-translate intersection. It replaces the earlier four-anchor lower bound $q^{7/40}$ by $q^{113/560}$, so a fifth anchor retains $q^{57/560}$ points, above the $q^{1/12}$ threshold. The second step appends two anchors at once, with the same separation as the original two. It reaches six anchors and gives the $q^{3/7}$ bound. Both steps use the existing Jacobi cap estimate.

Let $q\equiv1\pmod4$ be an odd prime power, $Q=(\mathbb F_q^\times)^2$, $n=|Q|$, and $m_0=n/\sqrt q$. Use additive notation for $G=\widehat Q$. Write $\lambda$ for the unnormalized Fourier transform of $s(x)=\chi(1-x)$ on $Q$, and put

$$
\Delta(u)=1-\lambda_u^2/q,\qquad L_t=\{u:\Delta(u)\le t\},\qquad
r_X(h)=|X\cap(X-h)|,\qquad
d(S)=|S|^{-2}\sum_{x,y\in S}\Delta(y-x).
$$

Fix a comparison range $0<b_-\le |S|/m_0\le b_+<\infty$ and a bound $f$ on the number of omitted shifts. There are constants $c,c_*>0$ and $q_0$ depending only on this data such that for every $q\ge q_0$, every such $S\subseteq G$, and every $F_0\subset G$ with $|F_0|\le f$,

$$
d(S)\le c q^{-43/120}
\quad\Longrightarrow\quad
\max_{g\notin F_0\cup\{0\}}r_S(g)\ge c_* q^{3/7}.
\tag{1}
$$

In particular this covers $d(S)=O(q^{-1/2})$ with any fixed implied constant. It gives a necessary translation constraint even for supports of compressions tested with arbitrary signed vectors.

## Cap and collision inputs

Write $\beta_j=1/(2(j+1))$. The [uniform translated cap bound](parallel-overlap-3.md#uniform-intersections-of-endpoint-sets) for distinct $b_1,\ldots,b_j$ is

$$
\left|\bigcap_{i=1}^j(b_i+L_t)\right|
\ll_j q\bigl(t^{j/2}+q^{-j/(2(j+1))}\bigr),\qquad 0<t\le1/4.
\tag{2}
$$

In particular it is $O_j(q^{1/2+\beta_j})$ for $t\ll q^{-1/(j+1)}$. This includes $j=6$: the two Gauss twists for each Jacobi quotient are disjoint from the twists for every other shift, because those shifts are distinct modulo the quadratic character. The mean of each nonconstant monomial in the product of the squared-phase tests is $O_j(M/\sqrt q+1/q)$ for test length $M$, by [Katz, Theorem 9.6](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf) and the cost of at most $2j$ exceptional lifts. The product has constant coefficient $M^{-j}$ and coefficient sum one. Taking $M\asymp_j\min(t^{-1/2},q^{\beta_j})$ with a small fixed comparison constant gives (2), just as for $j\le5$. The estimate is uniform in the shifts and the field order.

Let $m=|S|$. Keep a set $U\subseteq S$ of size $N\ge m/2$ for which every $x\in U$ has row sum at most $D=2md(S)$ over $U$. This follows by discarding rows with original sum greater than $D$. Also $d(U)\le4d(S)$. Apply the [earlier $q^{2/5}$ result](parallel-overlap-3.md#from-two-anchors-to-four) to $U$, taking $c$ small enough in (1), with zero and the possible nonzero involution omitted. Thus $r_U(h)\gg q^{2/5}$ for some $h\ne-h$.

For a set of shifts $B$, put $I_B=\bigcap_{b\in B}(U-b)$. We will extend anchors and amplify overlaps using a narrow width $t_0=128D/N=O(d(S))$. It is positive because $\Delta(0)=1-1/q>0$. If $|B|=j\in\{4,5,6\}$ and $|I_B|=b>0$, a positive fraction of pairs $(x,y)\in I_B\times U$ obey $y-x\in\bigcap_{v\in B}(v+L_{t_0})$. Indeed each row based at $x+v\in U$ rules out at most $D/t_0=N/128$ choices of $y$. There are $O_j(q^{1/2+\beta_j})$ such differences by (2). They avoid $B$ since $0\notin L_{t_0}$. The multiplicity of a difference $u$ is $|I_B\cap(U-u)|$. Pigeonholing, and then separately squaring and summing these multiplicities via Cauchy–Schwarz, give

$$
\begin{aligned}
\max_{u\notin B}|I_{B\cup\{u\}}|&\gg_j b q^{-\beta_j},\\
\sum_g r_{I_B}(g)r_U(g)&\gg_j b^2 q^{1/2-\beta_j}.
\end{aligned}
\tag{3}
$$

The collision identity in the second line counts two pairs with the same difference by their common translation $g$. Each deleted term costs at most $bN$, including the term at $g=0$. If $b/q^{\beta_j}\to\infty$ by a fixed power, the same lower bound holds with any bounded set of shifts deleted, uniformly in that set. As $\sum_g r_{I_B}(g)=b^2$, some remaining shift has $r_U(g)\gg_j q^{1/2-\beta_j}$.

## A triple inside one overlap gives four anchors

Fix $h\ne-h$ with $a=|I_{\{0,h\}}|\gg q^{2/5}$ and put $I=I_{\{0,h\}}$. Use the wider width

$$
t_1=128D/a\ll q^{1/2-43/120-2/5}=q^{-31/120}.
$$

Put $J_h=\{-h,0,h\}$, $H_h=J_h-J_h=\{0,\pm h,\pm2h\}$. The first set has three distinct elements; the second has at most five, with no requirement that $h$ have large order. Count ordered triples $(x,y,z)\in I^3$ with differences $u=y-x$, $v=z-x$, $v-u=z-y$. Keep those for which each of these three differences $d$ lies in $\bigcap_{e\in J_h}(e+L_{t_1})$ and avoids $H_h$. For each of the nine deficit tests, the two vertices being compared are in $U$, since their underlying vertices and their $h$-translates are in $U$. At a fixed first vertex, summing over the appropriate $a$ choices of the second costs at most $D$ by the row bound. Each test therefore deletes at most $a^3/128$ triples. The exclusions from $H_h$ cost at most $3|H_h|a^2$. A positive fraction of the $a^3$ triples remain.

There are $O(q^{5/8})$ choices of $u$ by the three-cap bound. At fixed $u$ the shift sets for the constraints on $v$ are $J_h$ and $u+J_h$. They are disjoint exactly when $u\notin H_h$, so the six-cap bound gives $O(q^{4/7})$ choices of $v$. Thus the number of good patterns $(u,v)$ is $O(q^{67/56})$. Counting collisions of triples with the same $(u,v)$ gives

$$
\sum_g r_I(g)^3\gg a^6 q^{-67/56}.
\tag{4}
$$

In fact for the unrestricted pattern multiplicities $b_I(u,v)$ one has $\sum_{u,v}b_I(u,v)^2=\sum_g r_I(g)^3$: equal patterns mean that all three vertices have the same translation, and at fixed $g$ each of the three starting vertices lies independently in $I\cap(I-g)$. Apply Cauchy–Schwarz to the good triples and use the unrestricted sum as an upper bound for those collisions.

The terms at $g\in H_h$ together cost at most $5a^3$. They are negligible since at the starting scale

$$
3(2/5)-67/56=1/280>0.
$$

Now bound the remaining sum by $(\max_{g\notin H_h}r_I(g))^2\sum_g r_I(g)$ and use $\sum_g r_I(g)=a^2$. This yields a $g\notin H_h$ for which

$$
B_4=\{0,h,g,g+h\},\qquad
b_4=|I_{B_4}|=r_I(g)\gg a^2 q^{-67/112}.
\tag{5}
$$

All four anchors are distinct. At $a\gg q^{2/5}$ this is $b_4\gg q^{113/560}$. The first line of (3) with $j=4$ now gives a genuine five-anchor intersection of size $\gg q^{57/560}$, and $57/560>1/12$. Applying the second line with $j=5$ gives $r_U(h')\gg q^{5/12}$ outside any bounded exclusions, including zero and the involution. This crosses the $3/40$ versus $1/12$ gap of the earlier pair argument without improving the three-cap bound alone.

## Add an entire second pair to the rectangle

Run the triple argument again with a shift $h$ of overlap $a\gg q^{5/12}$, choosing it with $h\ne-h$ as above. The result (5) now has $b_4\gg q^{79/336}$. For $x\in I_{B_4}$ and $y\in I$, both $y$ and $y+h$ are available. Require all differences from the four vertices $x+B_4$ to these two vertices to lie in $L_{t_1}$. At fixed $x$, each test excludes at most $D/t_1=a/128$ choices of $y$. The difference $u=y-x$ is then in the intersection of caps shifted by

$$
B_4-\{0,h\}=J_h\ \cup\ (g+J_h),
$$

which consists of six distinct shifts because $g\notin H_h$. We may further exclude $u\in H_h\cup(g+H_h)$, losing at most $10b_4$ pairs. Hence $\gg b_4a$ pairs survive, on at most $O(q^{4/7})$ differences. Some surviving difference $u$ has multiplicity $\gg b_4a q^{-4/7}$. Its exact multiplicity among all pairs is the size of

$$
I_{B_6},\qquad B_6=\{0,h,g,g+h,u,u+h\}.
$$

Indeed $x$ must lie in $I_{B_4}$, and $x+u\in I$ supplies the two new vertices. The exclusions on $u$ ensure the six anchors are distinct. In particular

$$
b_6=|I_{B_6}|\gg q^{79/336+5/12-4/7}=q^{9/112},
\qquad 9/112-1/14=1/112>0.
$$

Now (3) with $j=6$ gives $r_U(g')\gg q^{1/2-1/14}=q^{3/7}$ outside the prescribed bounded set and zero. Since $U\subseteq S$, this proves (1).

One more pass starting from a $q^{3/7}$ overlap gives $b_4\gg q^{29/112}$ and $b_6\gg q^{13/112}$. If $\max_{g\ne0}r_S(g)=O(q^{3/7})$, then a fixed positive fraction of the ordered pairs in this $I_{B_6}^2$ have difference outside the bounded exclusions and detect overlap $r_U(g)\gg q^{3/7}$: otherwise the off-exclusion sum in (3) would be too small. Each difference has multiplicity at most $b_6$, so there are $\gg q^{13/112}$ such shifts. Appending a singleton from this six-anchor lower bound gives only $b_7\gg q^{5/112}$, below the $q^{1/16}$ needed to amplify with seven caps. This is a limitation of that direct extension, not a barrier for other configurations.

## Critical compressions, feasible spectra, and square orders

The [Frobenius inequality](parallel-overlap-3.md#transfer-and-the-square-control) is $\|K_{SS}\|\le(m/m_0)\sqrt{1-d(S)}$. For $m\asymp m_0$ with $m\le m_0+o(q^{17/120})$, an overlap bound $\max_{g\ne0}r_S(g)=o(q^{3/7})$ forces $d(S)>c q^{-43/120}$ by (1), hence $\|K_{SS}\|\le1-c' q^{-43/120}$. For the actual stationary one-sided high set at a fixed threshold $0\le\rho<1$ and sufficiently small positive floor parameter, the [stationary form bound](parallel-arithmetic-2.md#exact-stationarity-and-the-square-control) gives signed top eigenvalue at least $1-O_\rho(q^{-1/2})$ in this size range. This implies $m\ge m_0-O_\rho(1)$, and the Frobenius inequality gives $d(S)=o(q^{-43/120})$. The high set therefore satisfies (1) with slack $o(q^{17/120})$, including bounded slack. A qualitative $d(S)=o(1)$ does not suffice for this transfer.

For a feasible probability $\mu$ of either sign with $m_0\|\mu\|_2^2\ge1-O(q^{-1/2})$, the [one-cone bounds](parallel-arithmetic-2.md#exact-stationarity-and-the-square-control) give $\mu_i\le L=(1+\sqrt q)/n$ and $d_\mu=O(q^{-1/2})$. Let $S=\{i:\mu_i\ge L/2\}$. The quantity $\sum_i\mu_i(1-\mu_i/L)=O(q^{-1/2})$ bounds both half the exterior mass and half the total unused capacity on $S$. Thus $L|S|=1+O(q^{-1/2})$, $|S|=m_0+O(1)$, and $d(S)\le 4d_\mu/(L|S|)^2$. Since $r_\mu(g)=\sum_i\mu_i\mu_{i+g}\ge (L/2)^2r_S(g)$, we obtain $r_\mu(g)\gg q^{-4/7}$ for some nonzero shift outside any fixed bounded exclusions.

At a square order $q=r^2$, take the actual Paley support $S=(\mathbb F_r^\times)^\perp$, of size $(r+1)/2$. On the positional subgroup $\mathbb F_r^\times$ the sign sum is $r-2$. On every other coset $a\mathbb F_r^\times$ in $Q$ it is $-2$: the quadratic norm polynomial $N(1-at)$ has nonzero discriminant and square leading coefficient, giving quadratic character sum $-1$ over $\mathbb F_r$, with the extra term at $t=0$ then removed. Fourier transformation on the quotient gives $\lambda_0=-1$ and $\lambda_h=r$ on $S\setminus\{0\}$. Consequently $d(S)=(1-1/q)/|S|$, and each nonzero shift in $S$ has full overlap $|S|$. Anchors selected within this subgroup retain the entire support, and all nondegenerate pattern differences in $S$ are exact endpoints. The uniform probability on $S$ is an exact feasible plus spectrum, since its positional transform is $\mathbf1_{\mathbb F_r^\times}$. The square example meets the hypotheses and is consistent with the strengthened necessary constraint.

The result leaves intermediate overlaps of order at least $q^{3/7}$ but still $o(m_0)$ open. The [prime finite-phase exclusions](critical-coset-phases.md) still require a coset cover obtained by other means. In particular, this does not establish the theta asymptotic in Problem 26.

## Checks

Exact enumeration on all subsets of cyclic groups of orders 5 through 9, and on seeded samples at orders 10 through 31, gave 8,682 checks of the cubic collision identity, 109,268 checks of the six-cap distinctness test, 68,684 checks of the four-anchor identity, and 545,912 checks of the six-anchor extension identity. Exact rational arithmetic verified the width and amplification exponents, including the $1/280$ margin for deleting the small shifts in (4) and the $1/112$ margin at six anchors. Direct norm enumeration for $r=3,5,7,11,17,31,47,97$ verified the positional coset sums in the actual square fields. The cyclic enumeration checks combinatorial identities; the cap bounds in the proof come from the Jacobi sums.
