# Jacobi caps conditioned on genuine translation overlaps

Let $q\equiv1\pmod4$ be an odd finite field order, $Q=(\mathbb F_q^\times)^2$, $n=|Q|$, and $m_0=n/\sqrt q$. Write $G=\widehat Q$ additively, $s(x)=\chi(1-x)$ on $Q$, and $\lambda=Fs$ with the unnormalized Fourier transform. Put

$$\Delta(u)=1-\lambda_u^2/q,\qquad L_t=\{u:\Delta(u)\le t\},\qquad
r_S(h)=|S\cap(S-h)|,\qquad d(S)=|S|^{-2}\sum_{x,y\in S}\Delta(y-x).$$

For any fixed comparison range $m=|S|\asymp m_0$, there are constants $c,C>0$ such that, uniformly over all $S\subseteq G$ and all sufficiently large $q$ in this family,

$$\begin{aligned}
d(S)\le c q^{-1/3} &\quad\Longrightarrow\quad \max_{h\ne0} r_S(h)\ge C q^{3/8},\
d(S)\le c q^{-43/120} &\quad\Longrightarrow\quad \max_{h\ne0} r_S(h)\ge C q^{2/5}.
\end{aligned} \tag{1}$$

The maximizing range can omit any fixed bounded number of shifts, with constants allowed to depend on that bound. In particular the conclusion applies at the $O(q^{-1/2})$ deficit where the [three-point bound](parallel-arithmetic-2.md) gives $q^{7/24}$. The proof uses the anchors of actual translated copies of a subset of $S$. It also forces conditional repetition inside differences of a four-translate intersection. Prime and square orders obey the same estimates.

## Uniform intersections of endpoint sets

For any fixed $j$ and distinct shifts $b_1,\ldots,b_j\in G$,

$$\left|\bigcap_{i=1}^j(b_i+L_t)\right|
\ll_j q\big(t^{j/2}+q^{-j/(2(j+1))}\big)\qquad(0<t\le1/4). \tag{2}$$

Use the positive test $P_M$ of the [three-point argument](parallel-arithmetic-2.md#two-widths-in-the-triangle-count). In the product of $j$ tests, a nonconstant monomial is a product of powers of normalized Jacobi sums at distinct shifts. If $\beta_i$ lifts $b_i$, the $2j$ Gauss twists $\bar\beta_i,\chi\bar\beta_i$ are all distinct. Away from the exceptional characters, a nonzero Jacobi exponent gives two opposite exponents on that pair of Gauss phases. Thus a nonconstant test monomial gives a nontrivial Gauss phase monomial, with total degree $O_j(M)$. Averaging over full characters and removing or restoring the at most $2j$ exceptional lifts costs $O_j(1/q)$, since all assigned phases have modulus one. The product descends to $G$, so its mean is $M^{-j}+O_j(M/\sqrt q+1/q)$. The bound on the Gauss monomial is [Katz, Theorem 9.6](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf).

Take $M\asymp_j\min(t^{-1/2},q^{1/(2(j+1))})$, with a sufficiently small constant for majorization and rounding to at least one. Each test is bounded below by an absolute positive constant on its own translated cap. This proves (2). Write $\beta(j)=1/(2(j+1))$. For $t\ll q^{-1/(j+1)}$ the count in (2) is $O_j(q^{1/2+\beta(j)})$.

## Counting from actual anchors

Discard at most half of $S$ to obtain $U$ of size $M_0\asymp m_0$ such that every $x\in U$ has $\sum_{y\in U}\Delta(y-x)\le2md(S)$. This follows by averaging the nonnegative row sums on $S$. Fix $t=A d(S)$ with, for example, $A=256$. The diagonal ensures $d(S)>0$. Each $x\in U$ then has at most $4M_0/A$ bad neighbors in $U$, where a bad pair has difference outside $L_t$. All anchoring below takes place in this same $U$.

For a set $B$ of $j$ distinct shifts let $I_B=\bigcap_{b\in B}(U-b)$ and $a=|I_B|$. For each $x\in I_B$ and $y\in U$ put $u=y-x$. For all but $4j/A$ of these pairs in proportion, $u\in\bigcap_{b\in B}(b+L_t)$. Assume $t\ll q^{-1/3}$ and $2\le j\le5$, so (2) bounds the number of good differences by $O_j(q^{1/2+\beta(j)})$. Since $0\notin L_t$, every good $u$ is outside $B$. The multiplicity of $u$ is $|I_B\cap(U-u)|$. Counting the pairs first and then counting pairs of pairs gives

$$\begin{aligned}
\max_{u\notin B}|I_{B\cup\{u\}}|&\gg_j a q^{-\beta(j)},\\
\sum_g r_{I_B}(g)r_U(g)&\gg_j a^2q^{1/2-\beta(j)}.
\end{aligned} \tag{3}$$

For the second estimate, apply Cauchy–Schwarz on the good differences. The sum of squared multiplicities of all differences equals the displayed sum, since two pairs with the same difference differ by a common translation $g$. An excluded shift contributes at most $aM_0$ to this sum. Hence for any set $F$ of bounded size, if $a\ge C_{j,|F|}q^{\beta(j)}$ for a sufficiently large constant, then

$$\sum_{g\notin F}r_{I_B}(g)r_U(g)\gg_j a^2q^{1/2-\beta(j)},\qquad
\max_{g\notin F}r_U(g)\gg_j q^{1/2-\beta(j)}. \tag{4}$$

The maximum bound uses $\sum_g r_{I_B}(g)=a^2$. This is a lower bound on the average multiplicity in $U$ of a difference sampled from the anchor intersection, with the omitted shifts assigned multiplicity zero. If the maximum off $F$ is $O(q^{1/2-\beta(j)})$, then a positive proportion of the $a^2$ pairs in $I_B$ have difference off $F$ with $r_U(g)\gg_j q^{1/2-\beta(j)}$. There are $\gg a$ distinct such differences since $r_{I_B}(g)\le a$.

### Energy identities at a fixed translation

For $I_h=I_{\{0,h\}}$ and $h\ne0$, count ordered triples $(x,y,z)\in I_h\times U^2$ by $(u,v)=(y-x,z-x)$, with multiplicity $b_h(u,v)$. Requiring all edges among $x,x+h,y,z$ except the anchor edge $(x,x+h)$ to be good leaves a positive fraction of the triples, by the row bound and the union bound. First $u,u-h\in L_t$, then $v,v-h,v-u\in L_t$. The latter three shifts are distinct, since $u\ne0,h$. The pattern count is $O(q^{2/3+5/8})=O(q^{31/24})$. The exact collision identity gives

$$\sum_{u,v}b_h(u,v)^2=\sum_g r_{I_h}(g)r_U(g)^2
\gg |I_h|^2 q^{17/24}. \tag{5}$$

The identity counts a common translation for the anchor and both other vertices. After deleting a bounded set of shifts, (5) still holds with a changed constant if $|I_h|\ge C q^{7/24}$ for a sufficiently large $C$, since each deleted term is at most $|I_h|M_0^2$.

Summing the conditional estimates uses the exact identity $\sum_h r_{I_h}(g)=r_U(g)^2$. For a fixed $g$, the two choices are ordered points in $U\cap(U-g)$, and their difference is $h$. In particular, if $T_b=\{h\ne0:r_U(h)\ge b\}$, equations (4) and (5) with the deletion $F=\{0\}$ give, for sufficiently large fixed $C_1,C_2$,

$$\begin{aligned}
\sum_{g\ne0}r_U(g)^3 &\gg q^{1/3}\sum_{h\in T_{C_1q^{1/6}}} r_U(h)^2,\\
\sum_{g\ne0}r_U(g)^4 &\gg q^{17/24}\sum_{h\in T_{C_2q^{7/24}}} r_U(h)^2 .
\end{aligned} \tag{6}$$

At $d(S)=O(q^{-1/2})$, the [one-point energy bound](critical-sets.md#repeated-differences-are-necessary) applied to $U$ gives $E(U)\gg q^{5/4}$, since $d(U)\le4d(S)$. The excluded small overlaps in the first line of (6) have energy at most $C_1q^{1/6}M_0^2=O(q^{7/6})$, and the zero shift costs $M_0^2$. Thus the first line lower bounds the off-zero cubic sum by a constant times $q^{1/3}E(U)$ in this range.

## From two anchors to four

At $d(S)=O(q^{-1/2})$, the [three-point result](parallel-arithmetic-2.md#translation-multiplicities-and-a-compression-gap) gives a seed $|I_h|\gg q^{7/24}$ on $U$ itself. For the wider hypothesis in (1), the good pairs in $U^2$ have differences in $L_t$. Since $0\notin L_t$, the single-cap case of (2) gives

$$\max_{h\ne0} r_U(h)\gg (\sqrt{A d(S)}+q^{-1/4})^{-1}.$$

Choosing $c$ in (1) sufficiently small gives a seed above the constant threshold $C_{2,|F|}q^{1/6}$ in (4). The following steps use either seed.

1. Apply (4) with $B=\{0,h\}$ and omit zero. It produces a nonzero shift of overlap $\gg q^{1/3}$. Use this new shift to form a new two-anchor intersection. By the first line of (3), a third distinct shift leaves an intersection of size $\gg q^{1/3-1/6}=q^{1/6}$. This exceeds the threshold $q^{\beta(3)}=q^{1/8}$ by a power, so (4) gives a shift $h$ with $r_U(h)\gg q^{3/8}$, proving the first line of (1). At this step also omit the unique possible nonzero element of order two, so $h\ne-h$.
2. Take $I=I_h$ of size $a\gg q^{3/8}$. Every $x,y\in I$ has both endpoints and their $h$-translates in $U$. Use the wider cap width $t'=32md(S)/a$. Among the $a^2$ pairs, a positive fraction have all of $u=y-x,u-h,u+h$ in $L_{t'}$. For each of the three constraints, the total deficit of the relevant ordered pairs is at most $2md(S)a$ by the row bound, so the number of failures is at most $a^2/16$. Since $0,h,-h$ are distinct, (2) bounds the number of such $u$ by $O(q(t')^{3/2}+q^{5/8})$. Such $u$ automatically avoid $0,h,-h$. At $d(S)=O(q^{-1/2})$ we have $t'\ll q^{-1/4}$, so some such $u$ has $r_I(u)\gg a^2 q^{-5/8}\gg q^{1/8}$. Under the second deficit hypothesis in (1), $t'\ll c q^{-7/30}$, and the count is $O(c^{3/2}q^{13/20}+q^{5/8})$. Since $a^2\gg q^{3/4}$, choosing $c$ small enough makes $r_I(u)\ge C_{4,|F|}q^{1/10}$ for some such $u$ at large $q$.
3. The identity

   $$r_I(u)=|I_{\{0,h,u,h+u\}}|$$

   supplies four distinct anchors. Their common intersection meets the threshold in (4) for $\beta(4)=1/10$. Applying (4) again, with zero and any prescribed bounded set of shifts omitted, proves $\max r_U(g)\gg q^{2/5}$. Since $U\subseteq S$, this proves the second line of (1).

In particular, (4) on the four-translate intersection forces its differences to detect repeats in $U$ at scale $q^{2/5}$. One can repeat step 2 with the new shift of size $\gg q^{2/5}$, omitting the involution in step 3. Now $t'\ll q^{-31/120}\ll q^{-1/4}$ even at the wider deficit of the second line of (1). It gives an intersection with $a_4\gg q^{7/40}$. If the maximum overlap off zero is $O(q^{2/5})$, the positive-proportion consequence of (4) shows that $\gg q^{7/40}$ distinct nonzero shifts have overlap $\gg q^{2/5}$.

## Transfer and the square control

The entry bound and Frobenius norm give $\|K_{SS}\|\le (m/m_0)\sqrt{1-d(S)}$ for arbitrary supports and arbitrary compression vectors. For either exponent pair $(\delta,\gamma)=(1/3,3/8),(43/120,2/5)$ in (1), if $\max_{h\ne0}r_S(h)=o(q^\gamma)$ then $d(S)>c q^{-\delta}$ for large $q$. With $m\le m_0+o(q^{1/2-\delta})$ this implies $\|K_{SS}\|\le1-c' q^{-\delta}$.

For the actual one-sided stationary high set $S_\sigma=\{i:\sigma D_i>\rho\}$, with fixed $0\le\rho<1$ and sufficiently small positive floor parameter $\tau$ as in the [stationary quadratic-form estimate](parallel-arithmetic-2.md#exact-stationarity-and-the-square-control), the lower bound is $\lambda_{\max}(\sigma K_{S_\sigma S_\sigma})\ge1-O_\rho(q^{-1/2})$. The entry bound first gives $|S_\sigma|\ge m_0-O_\rho(1)$. Then the Frobenius inequality gives $d(S_\sigma)=o(q^{-\delta})$ if $|S_\sigma|\le m_0+o(q^{1/2-\delta})$. Thus the $q^{3/8}$ overlap holds at slack $o(q^{1/6})$, and the $q^{2/5}$ overlap holds at slack $o(q^{17/120})$, which includes $O(1)$ slack. A near-null direction known only to have $d(S)=o(1)$ needs a quantitative deficit estimate to use this transfer.

There is also a consequence for a feasible probability $\mu$ of either sign with $m_0\|\mu\|_2^2\ge1-O(q^{-1/2})$. The [one-cone bounds](parallel-arithmetic-2.md#exact-stationarity-and-the-square-control) give a point cap $L=(1+\sqrt q)/n$ and weighted deficit $d_\mu=O(q^{-1/2})$. Since $\sum_i\mu_i(1-\mu_i/L)=1-\|\mu\|_2^2/L=O(q^{-1/2})$, the set $S=\{i:\mu_i\ge L/2\}$ carries mass $1-O(q^{-1/2})$, and $\sum_{i\in S}(L-\mu_i)=O(q^{-1/2})$. Hence $|S|=m_0+O(1)$ and $d(S)\le 4d_\mu/(L|S|)^2$. On every shift, the probability overlap obeys $r_\mu(h)\ge (L/2)^2r_S(h)$. Equation (1) yields $\max_{h\ne0}r_\mu(h)\gg q^{-3/5}$.

For $q=r^2$, take $S=(\mathbb F_r^\times)^\perp$. It has $m=(r+1)/2$, $\lambda_h=r$ on $S\setminus\{0\}$ and $\lambda_0=-1$. Thus $d(S)=(1-1/q)/m$, $r_S(h)=m$ on $S$, and $E(S)=m^3$. All distinct choices of anchors in $S$ retain the whole set. The uniform probability on $S$ is feasible by the [subfield formula](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy).

## First missing estimate

The [next anchor count](parallel-five-4.md) crosses the fifth-anchor threshold below using triples in an actual two-translate intersection. It amplifies the overlap further via six anchors.

At the lower-bound scale $r_U(h)\asymp q^{2/5}$, the three-cap count in step 2 guarantees $a_4\gg q^{7/40}$. Adding a fifth distinct shift by (3) gives only $a_5\gg q^{7/40-1/10}=q^{3/40}$. To remove the zero-shift term and then force overlaps at $q^{5/12}$ by (4), this route needs $a_5\ge C q^{1/12}$. The exponent falls short by $1/120$. Equivalently, for the four-anchor strategy with one more vertex the missing scale is $a_4\ge C q^{1/10+1/12}=C q^{11/60}$. A power-saving three-cap estimate of size $O(q^{37/60-\eta})$ for the differences actually realized by the good pairs in $I_h^2$, for some $\eta>0$, would suffice at this step. The uniform bound used here is $O(q^{5/8})$. The same discrepancy occurs if one goes directly to a mixed triangle based at a four-anchor intersection: the two stages use four and five distinct shifts, with total pattern count $O(q^{1+1/10+1/12})$. This can exceed $a_4 M_0^2$, leaving the zero-shift term alone compatible with the collision lower bound.

There is also an obstruction to obtaining a fixed positive overlap fraction or a bounded-coset cover solely from the cardinality bounds (2) and the resulting energy inequalities. In an abstract cyclic group of order $2m^2$ with $m$ a power of two, choose a subgroup $H$ of order $m\ell$, where $\ell$ is a power of two comparable to $\log m$. There are size-$m$ subsets $S\subset H$ with $r_S(h)=O(m/\ell)$ for every $h\ne0$. For existence, select points with independent probability $2/\ell$, then thin to size $m$. The initial size is at least $m$ with probability tending to one by Chebyshev. For fixed $h\in H\setminus\{0\}$ the directed edges $x\mapsto x+h$ split into at most three matchings by coloring each cycle, with the two edges of a two-cycle in different classes. The counts in each class are sums of independent Bernoulli variables of mean at most $4m/\ell$. An exponential Markov bound gives probability $\exp(-\Omega(m/\ell))$ of exceeding $16m/\ell$ in any given class. A union bound over $h$ suffices. Thinning preserves the overlap bound, while Cauchy–Schwarz and support in $H$ give $E(S)\asymp m^3/\ell$. Every such $S$ has all its nonzero overlap ratios tending to zero. A union of boundedly many cosets differing from $S$ by $o(m)$ points would have a common subgroup of order $\gg m$ and hence a nonzero shift with overlap ratio $1-o(1)$.

In this model set the formal scale $q=4m^2+1$ and the artificial deficit to zero on $H\setminus\{0\}$ and one elsewhere. It has $d(S)=1/m$, and every intersection of fixed finitely many translated caps has size at most $m\ell=o(q^{1/2+\beta(j)})$ for fixed $j$. This verifies compatibility with the cap cardinality tests at every fixed order, including the conditional tests above. Actual Gauss phases, $K^2=I-\mathbf1\mathbf1^{\mathsf T}/n$, and stationarity supply further constraints in the Paley problem. Intermediate overlaps above the new lower bound, including $o(m)$ overlaps, remain open there. The [prime coset exclusions](critical-coset-phases.md) concern covers obtained by other means.

## Checks

Exact integer enumeration of 728 cyclic subsets and samples checked 7,146 conditional pair identities, 7,146 mixed triple identities, 110,740 four-anchor identities and degeneracy checks, and 7,874 summed-shift identities. Rational arithmetic checked every exponent in the amplification and the $1/120$ shortfall. Direct finite-field enumeration for $r=3,5,7,11,17,31,47$ gave positional sign sums $r-2$ on $\mathbb F_r^\times$ and $-2$ on each other coset in $Q$, reproducing the square-control endpoint formula by Fourier orthogonality.
