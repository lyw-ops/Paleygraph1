# The two-anchor reduction at the endpoint

For [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), the order-two branch of [Round 20, §4](parallel-rectangle-20.md#4-the-twisted-coset-becomes-a-pinned-cross-ratio-question) remains open here. The smooth cap does work at the endpoint: a bounded normalized strong `3/2` moment of the **anchor-averaged** off-identity correlations suffices. The averaging can use every anchor in the subgroup, and yields exactly the ratio-of-differences distribution of one reciprocal shifted subgroup. The special anchor `-1` has one full overlap, which can be omitted; a torsion-point estimate bounds every other individual overlap by $O(b^{2/3})$, but does not give the required moment.

## 1. Every anchor works, including the involution anchor

Let $p\equiv1\pmod4$ be prime, $Q$ the nonzero squares, $B\le Q$, $b=|B|\sim\sqrt p$, $d$ the nontrivial quadratic character of $B$, $\chi$ the field's quadratic character, and $\sigma\in\{\pm1\}$. The near-unit assumption is
$$
\chi(1-x)=\sigma d(x)\qquad(x\in B\setminus E),\qquad |E|=o(b).
\tag{1}
$$
Include $1$ in $E$. For **any** $a\in B\setminus\{1\}$, put $\phi_a(x)=(x-a)/(x-1)$ and $X_a=\phi_a(B\setminus\{1,a\})$. Outside $E\cup aE$, the character of $\phi_a(x)$ equals $d(a)$: the two factors have characters $\sigma d(x)$ and $\sigma d(x)d(a)$. Choose $c_a\ne0$ with $\chi(c_a)=d(a)$ and put $g_a=\mathbf1_{Q\cap c_aX_a}$. Uniformly in $a$, $\|g_a\|_2^2=b-o(b)$.

For the unscaled differences, the identity
$$
\phi_a(x)-\phi_a(y)=\frac{(a-1)(x-y)}{(x-1)(y-1)}
$$
and (1) show that $\chi(\phi_a(x)-\phi_a(y))=\sigma\chi(a-1)$ for all but $o(b^2)$ ordered pairs. Indeed $\chi(x-y)=\chi(1-x/y)=\sigma d(x)d(y)$ except for at most $b|E|$ pairs. The resulting sign for $g_a$ is $\rho_a=\sigma d(a)\chi(a-1)$, which equals $+1$ for $a\notin E$. If $\mathcal T_{xy}=p^{-1/2}\chi(x-y)$ is the additive Paley convolution, then uniformly in $a$,
$$
\langle g_a,(I-\rho_a\mathcal T)g_a\rangle=o(b).
\tag{2}
$$
In fact the signed Rayleigh quotient is $(1-o(1))|Q\cap c_aX_a|/\sqrt p$. Multiplication by $c_a$ leaves the unrestricted correlations
$$r_a(u)=|X_a\cap uX_a|$$
unchanged, so each correlation of $g_a$ is bounded by $r_a(u)$ for $u\in Q$. In particular there is no need to restrict $a$ to $\ker d$.

For $a=-1$, $X_{-1}$ is both negation and inversion invariant:
$$\phi_{-1}(1/x)=-\phi_{-1}(x),\qquad \phi_{-1}(-x)=1/\phi_{-1}(x).$$
Consequently $r_{-1}(-1)=b-2$ exactly. This term costs $O_M(p^{-1/2})$ after normalizing the cap pairing by $b$, by the off-identity entry bound of Round 20. It can be removed before estimating the tail. The exceptional anchor need not obey $\chi(1-a)=\sigma d(a)$ itself: (2) holds for it with its own sign.

There is also an exact simplification of its other ratios. For $u\ne1$, $h=(1+u)/(1-u)$ converts the ratio equation to $xy-1=h(x-y)$. If $u\ne -1$ as well, let $S=\{t:t^2\in B\}$, $D_0=B$, $D_1=S\setminus B$, and $\Delta(v)=v-v^{-1}$. Then
$$
r_{-1}(u)=\frac12\sum_{i=0}^1
\#\{(v,w)\in D_i^2:\Delta(w)=h\Delta(v),\ wv,w/v\notin\{1,-1\}\}.
\tag{3}
$$
Take $w^2=xy$ and $v=x/w$; $x=wv$, $y=w/v$ and $w,v$ are in the same coset of $B$ in $S$. Both choices of $w$ give the same pair $(x,y)$. Formula (3) replaces the cross ratio by a ratio of two Dickson polynomial values. The shifted-subgroup tail does not transfer directly: $\Delta(v)=(v^2-1)/v$ entails different dilations at different $v$, and dropping the denominators only controls a count lumped by multiplicative cosets.

## 2. Averaging is an exact ratio-of-differences problem

Write $D=\{(x-1)^{-1}:x\in B\setminus\{1\}\}$ and $t_a=(a-1)^{-1}$. Exactly $X_a=(1-a)(D-t_a)\setminus\{0\}$, where the expression means to scale and omit zero. For $u\ne0,1$,
$$
r_a(u)+1=|\ell_{a,u}\cap (D\times D)|,\qquad
\ell_{a,u}:\quad z=uw+(1-u)t_a.
\tag{4}
$$
The extra point is $(t_a,t_a)$; on this line, any equality of two of $z,w,t_a$ forces equality of all three. The lines are distinct as $(a,u)$ varies. Hence, averaging over $a\in B\setminus\{1\}$,
$$
\bar r(u)=\frac{1}{b-1}\#\{(t,z,w)\in D^3:\ t,z,w\text{ distinct},\ z-t=u(w-t)\}.
\tag{5}
$$
Averaging over a subset of a fixed positive fraction of the anchors is pointwise dominated by a constant times (5). In particular we can use $a\notin E$ to work with a single cap for sign $+1$. Since $r_a$ is nonnegative, it is enough to control a moment of the mean $\bar r$; a mean of the individual moments is a stronger requirement.

Equivalently the all-anchor numerator in (5), multiplied by $b$, is the number of ordered pairwise-distinct quadruples of $B$ with that cross ratio: divide the quadruple by its first anchor to set it to $1$. The $\ell^2$ count for (5) has another exact interpretation. If $T_*(D)$ counts ordered triples of distinct collinear grid points on lines of nonzero finite slope in $D^2$, then
$$\sum_{u\ne0,1}\bar r(u)^2=\frac{T_*(D)}{(b-1)^2}.$$
For a squared count at a given $u$, take one triple $(t,z,w)$ from each coordinate. This gives collinear points with no repeated first or second coordinate, and all such triples arise once. Thus an $O(b^4)$ estimate for this grid triple count would be sufficient already by Cauchy–Schwarz. The generic [prime-field grid triple bound](https://arxiv.org/pdf/1702.01003) is $O(|D|^6/p+|D|^{9/2})$, giving $O(b^{5/2})$ here after division. The stronger estimates for [grids of subgroups](https://arxiv.org/abs/2003.03493) do not apply directly to the reciprocal shifted set $D$. A bound on the number of distinct cross-ratio values would also not give this moment.

For comparison, the [Stevens–de Zeeuw grid incidence estimate](https://arxiv.org/abs/1609.06284), in the form $I(D^2,L)\ll b^{5/4}|L|^{3/4}+b^2+|L|$ for $b|L|\ll p^2$, gives
$$
\#\{(a,u):u\ne0,1,\ r_a(u)\ge t\}\ll \min(b^3/t, b^5/t^4).
\tag{6}
$$
The additive $b^2$ term covers $|L|<b$, where the incidence bound also follows from $I≤ b|L|$. The trivial counting term in (6) uses the total number of pairs in all $X_a$. It also verifies the size condition on $L$ since $b^4\asymp p^2$. For large enough constant $t$, absorb the $|L|$ term, and the $b^2/t$ rich-line term is bounded by $b^5/t^4$ for $t\le b$. Bounded $t$ follows from the trivial term. After dividing by $b-1$, (6) improves the trivial estimate for the number of rich ratios per anchor only for $t\gg b^{2/3}$. It does not control the fixed-$t$ ladder at which the cap operates.

## 3. The cap does work with a strong endpoint moment

Let $a_{M,\rho}$ be the multiplicative cap coefficients of [Round 20, §1](parallel-rectangle-20.md#1-a-smooth-jacobi-cap), with $P_{M,\rho}(v)=((1+\rho v)/2)^M$. On $Q\setminus\{1\}$ set $v_{M,\rho}(u)=\sqrt p\,|a_{M,\rho}(u)|$, with probability-normalized norms below using the measure $1/p$ per point. For fixed $M$ and $p$ sufficiently large depending on $M$, the bounds there give
$$
\|v_{M,\rho}\|_2\ll M^{-1/4},\qquad
\|v_{M,\rho}\|_\infty\ll\sqrt M .
\tag{7}
$$
The identity coefficient contributes $O(M^{-1/2}+p^{-1/4})$ to the cap mass divided by $b$. The rest is bounded by a constant times $p^{-1}\sum_u v_{M,\rho}(u)r_a(u)$. Formula (2) forces the normalized cap mass to tend to one for every *fixed* $M$, since $1-P_{M,\rho}(k)\le M(1-\rho k)/2$. This also holds for finite averages in $M$ and uniformly over the anchors in (2).

Suppose $r\ge0$ dominates one usable correlation or the anchor average of the usable correlations, and
$$
\frac1p\sum_{u\in Q\setminus\{1\}}r(u)^{3/2}\le C .
\tag{8}
$$
One can ignore any bounded number of ratios having multiplicity $O(b)$: they cost $O_M(p^{-1/2})$ each. Take $M_j=4^j$ and $V_K=\sum_{j=1}^K v_{M_j,\rho}$. For $2\le t\le C_0 2^K$, split at $j_0$ with $2^{j_0}\asymp c_0t$ for a sufficiently small constant $c_0$. The $L^\infty$ bound makes the sum below $j_0$ at most $t/2$ (use an empty sum near the lower endpoint). The rest has $L^2$ norm $\ll 2^{-j_0/2}\ll t^{-1/2}$ by summing the geometric sequence in (7). Chebyshev gives
$$
\frac1p|\{u:V_K(u)>t\}|\ll t^{-3}.
$$
By the $L^\infty$ bound $V_K\le C_0 2^K$, and integrating the distribution gives $\|V_K\|_3^3\ll K+1$. Therefore by Hölder the averaged off-identity cap contribution is $O(C^{2/3}K^{-2/3})$, and its averaged diagonal contribution is $O(K^{-1}+p^{-1/4})$. Choose a sufficiently large **fixed** $K$, then let $p\to\infty$. This contradicts (2). In particular, (8) for $\bar r$ from (5) would close the branch and, by the same sequence argument as in Round 20, give a fixed deficit in a fixed neighborhood of the critical size for exact twisted cosets. The argument works on either sign for a single anchor.

Here are two comparisons with the former strict tail threshold. A tail $\#\{r\ge t\}=o_t(p/t^{3/2})$ uniformly for large fields suffices even if (8) fails: split at $t=M$, use $p^{-1}\sum_{r\le M}r^2=o_M(M^{1/2})$ and $p^{-1}\sum_{r>M}r=o_M(M^{-1/2})$ in (7). On the other hand the bare weak bound $O(p/t^{3/2})$ gives only $O(1)$ this way. For an abstract distribution with measure $\asymp M^{-3/2}$ on $r\asymp M$ at geometric scales, kernels of height $\asymp\sqrt M$ on the corresponding layers meet (7) and can have order-one pairing at every scale. This explains a limitation of (7) plus a bare weak bound; it does not disprove a gap for the actual Jacobi coefficients.

## 4. Uniform individual saving and the square-order check

For $u\ne0,1$, let $h_{a,u}=\phi_a^{-1}\circ (z\mapsto uz)\circ\phi_a$. Then
$$
|B\cap h_{a,u}(B)|=r_a(u)+2
$$
as a projective intersection; the two extra points are the fixed anchors $1,a$. Here and in the incidence argument any values at $\infty$ are omitted from the grid. The strongest pointwise comparison here follows directly from [Corvaja–Zannier, Theorem 2](https://ems.press/content/serial-article-files/31918):
$$r_a(u)\ll b^{2/3}+b^2/p\ll b^{2/3}\qquad ((a,u)\ne(-1,-1)).\tag{9}$$
Apply it on the projective line with the rational functions $x^b,h_{a,u}(x)^b$. Both have degree $b$ and nonzero differentials, as $p\nmid b$. Their zeros and poles occupy at most four places. They are multiplicatively independent modulo constants unless the two sets of zeros and poles coincide, since otherwise some place occurs in only one divisor. Coincidence means $h_{a,u}$ is a dilation or a scaled inversion. A dilation fixing 1 is the identity, excluded; a scaled inversion fixing 1 has scale 1, and its other fixed point is $-1$. In the $\phi_{-1}$ coordinate that inversion acts by $u=-1$. Every point of $B$ mapped back into $B$ contributes one to the gcd count.

For comparison, a direct use of subgroup Möbius incidences gives the weaker $O(b^{9/10})$. Let $h$ be a Möbius map with all four matrix entries nonzero. Its left and right $B$-dilation orbit $\mathcal H=\{D_\beta hD_\alpha:\alpha,\beta\in B\}$, where $D_\alpha(x)=\alpha x$, has $b^2$ distinct maps. Every map has the same number $N$ of grid incidences on $B\times B$. A quotient of two maps has the form $D_{\beta_1}hD_r h^{-1}D_{\beta_2}^{-1}$, where $r=\alpha_1/\alpha_2$. Write $A,F,G,D$ for the four entries of $h$ (with the symbol $D$ here an entry). The two products $P=AD$ and $S=FG$ satisfy $PS\ne0$ and $P\ne S$. Up to scalar the middle matrix is
$$
\begin{pmatrix}Pr-S&AF(1-r)\\GD(r-1)&P-Sr\end{pmatrix}.
$$
For $r\ne1$, its off-diagonal entries are nonzero. The double-dilation invariant, diagonal product divided by off-diagonal product, is $1-(P-S)^2r/[PS(r-1)^2]$; any given invariant allows at most two $r$. If at least one diagonal entry is nonzero, all other parameters are fixed by the output matrix and $r$: comparing its two off-diagonal entries against a nonzero diagonal entry determines $\beta_1,\beta_2$. There are $b$ choices of $(\alpha_1,\alpha_2)$ for that $r$. Both diagonals can vanish only for $r=-1$ with $P=-S$, giving inversion followed by a dilation. For $r=1$ the quotient is a dilation. Each of these exceptional sectors has $b^3$ ordered pairs of orbit maps and multiplicity at most $b^2$ in its outputs. These observations bound the quotient energy by $O(b^5)$ (combine the sectors by Cauchy–Schwarz). [Warren–Wheeler, Theorem 4](https://arxiv.org/pdf/2107.12286) now gives $b^2N\ll b^{29/10}+b^{5/2}$. If $b>\sqrt p$, split the second coordinate into $O(1)$ parts of size at most $\sqrt p$ and use the same orbit and energy for every part. This is the dilation-orbit argument from [the Möbius transform note](mobius.md#a-power-saving-for-subgroup-indicator-overlaps-at-prime-order) with the arbitrary four-entry invariant.

If exactly one matrix entry vanishes, invert the input or output or both as needed to put the zero in the bottom left. Inversion preserves $B$, and the resulting affine map has nonzero translation and slope. One application of the [Mit'kin line estimate](https://arxiv.org/pdf/1701.06192) bounds $N$ by $O(b^{2/3})$. The remaining matrices represent dilations or scaled inversions, disposed of above. Both power savings bound the largest nonexceptional correlation; even (9) does not bound the moment in (8).

At odd square order $q=\ell^2$, there is an **exact twisted comparison**. Take $B=\{x:x^{\ell+1}=1\}\le Q$ and $d(x)=x^{(\ell+1)/2}$ interpreted as a sign. For $x\ne1$ in $B$,
$$
(1-x)^{\ell-1}=-1/x,qquad
\chi_q(1-x)=(-1)^{(\ell+1)/2}d(x).
$$
The signed coset mean tends to one. For every $a\ne1$ in $B$, $\phi_a(x)^\ell=\phi_a(x)/a$ on its finite nonzero image. Hence $X_a=v_a\mathbb F_\ell^\times$ for any $v_a\in X_a$ (the two sets have the same size $\ell-1$). Every $u\in\mathbb F_\ell^\times$ gives full overlap $\ell-1$, all other $u$ give zero. This holds after removing the special involution ratio, and even for the anchor mean. The normalized strong $3/2$ moment grows as $\ell^{1/2}$. The $b^2/p$ term in Corvaja–Zannier uses the characteristic $p=\ell$, not the field order $q$, so (9) does not contradict this example. Thus the missing tail estimate is genuinely a prime-field question.

## 5. An alternative cell count: two powers are free, another half power is needed

For a map with four nonzero entries, normalize the bottom right entry to one and write
$$h(x)=\frac{\lambda\alpha\beta x+\beta}{\alpha x+1},\qquad \lambda\ne0,1.$$
For $h_{a,u}$ the product of its fixed points is $-\beta/\alpha=a$, so $\beta/\alpha\in B$ (as $-1\in B$). Set $C=\alpha B=\beta B$. Dilating the input and output independently by elements of $B$ preserves the cell $(\lambda,C)$. The cell count is
$$
N_C(\lambda)=\#\{(X,Y)\in C\times C^{-1}:XY+Y=\lambda X+1\}.
$$
Every map in the cell has $N_C(\lambda)$ intersections with $B$. Exactly $N_C(\lambda)$ maps in the cell fix 1: the point $(X,Y)=(\alpha,1/\beta)$ must be on the displayed curve. Not all of these maps need have a second fixed point in $B$. If they do, they specify a unique pair $(a,u)$ since the map is nonidentity. Therefore there are at most $N_C(\lambda)$ pairs $(a,u)$ per cell, each with $r_a(u)=N_C(\lambda)-2$.

The cells have the unconditional estimate
$$
\sum_{\lambda\ne0,1}\sum_{C} N_C(\lambda)^2\le b^3+2b(p-1).
\tag{10}
$$
Indeed, set $s=XY\in B$ and write $\lambda X^2=(s-1)X+s$. To count a second solution in the same cell put $X'=rX$ with $r\in B$ and $s'=X'Y'\in B$. Equate the two formulas for $\lambda X^2$:
$$ (s-1)X+s=(s'-1)X/r+s'/r^2.$$
For each $(r,s,s')$ there is at most one $X$ unless both coefficients agree. The identity cases are $r=1,s=s'$ and $r\ne1,s=-1/r,s'=-r$, altogether at most $2b$ triples. In those cases there are at most $p-1$ nonzero choices for $X$. This proves (10).

If the left side of (10) with exponent $5/2$ were $O(b^3)$, summing $r_a(u)^{3/2}$ over all anchors and ratios with four nonzero entries would cost $O(b^3)$, sufficient for (8) by averaging and convexity. For each $a$ the other maps occur only at $u=a$ or $u=1/a$: this follows from the diagonal entries $u-a,1-ua$ in an unnormalized matrix whose off-diagonals are $a(1-u),u-1$. Their cap contribution tends to zero for each fixed $M$, uniformly in $a$, by the bounded number of terms. The elementary second moment (10) only pays for the total pair mass, which is already controlled. A useful next step is an estimate for the extra half power, or a direct bound for the smaller moment of the mean in (5).

## 6. Exact finite comparisons

Run [the standard-library check](parallel-crossratio-21-check.py) with Python 3. It compares the two ratio histograms in (4) for every selected anchor, checks (3) at every nonidentity ratio for the involution anchor, and compares the Möbius grid count with $r_a(u)+2$ at all ratios for $p=97$ and at sampled ratios otherwise. For the first three primes it enumerates the full set of cells in (10) and compares sampled Möbius grid counts with the corresponding cell counts. All counts were exact integers. Only the displayed moments and normalizations are rounded.

| $p$ | $b$ | Anchors | Largest individual overlap excluding $(-1,-1)$ | Mean's normalized $3/2$ moment | Mean's normalized second moment | Cell second moment divided by $b^3$ |
|---:|---:|---:|---:|---:|---:|---:|
| 97 | 12 | 11 | 6 | 1.152 | 1.502 | 1.870 |
| 1153 | 32 | 31 | 8 | 0.726 | 0.735 | 3.058 |
| 4177 | 72 | 71 | 12 | 1.291 | 1.474 | 2.530 |
| 10193 | 98 | 97 | 10 | 0.872 | 0.865 | — |
| 40801 | 200 | 41 | 12 | 0.962 | 0.987 | — |
| 252001 | 500 | 41 | 18 | 0.995 | 1.022 | — |

The table uses every nonzero, nonidentity ratio, including both square classes and the $-1$ ratio. The last two prime rows average 41 deterministic sampled anchors including $-1$; other rows average all $b-1$ anchors. For the square comparison the script enumerates the exact twist and full overlap profile for every anchor at $\ell=7,11,13,31$, obtaining normalized $3/2$ moments $1.500,2.352,2.706,4.959$ respectively. The prime rows are compatible with (8), but do not establish a uniform bound.
