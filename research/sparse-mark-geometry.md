# Sparse mark geometry and concentration

This note addresses the sparse part of the [rank expansion](random-weight-ranks.md). At growing sample counts the signed log optimum concentrates around its mean, with a bound independent of field order. At two marks, one linear program gives sharp bounds on the first rank term. These are distinct tests of the remaining expected signed contribution.

## Dimension-free fluctuation bound

Let $F=F_+-F_-$ as in the [rank expansion](random-weight-ranks.md), let $a_k=\mathbb EF(W^{(k)})$, and write $\mathsf H(w)=-\sum_iw_i\log w_i$. The value at every simplex vertex is the same $a_1$. For any normalized weights $u,v$ and $w=(1-b)u+bv$, the two Jensen gaps

$$J_\sigma=(1-b)F_\sigma(u)+bF_\sigma(v)-F_\sigma(w)$$

are nonnegative. Their sum is $\mathsf H(w)-(1-b)\mathsf H(u)-b\mathsf H(v)$, which is the mutual information of the mixture label and the sampled frequency. In particular the sum is at most the binary entropy $h(b)$. Thus

$$|F(w)-(1-b)F(u)-bF(v)|\le h(b).$$

By the same Jensen argument applied to a mixture of simplex vertices, $|F(u)-a_1|\le\mathsf H(u)$. In both comparisons the signed difference is bounded by the sum of two nonnegative gaps.

Generate $W^{(k)}$ by $k$ independent pairs of a uniform frequency label and an exponential mass. Replace one pair by a fresh independent pair. Let $u$ be the normalized weight from the other $k-1$ pairs and $b,b'$ the old and new fractions of mass at the replaced pair. Since the value of a single mark is always $a_1$, the change of the signed log optimum obeys

$$|F(W^{(k)})-F(W^{(k)\prime})|\le |b-b'|\log(k-1)+h(b)+h(b').$$

Both $b,b'$ have the $\operatorname{Beta}(1,k-1)$ marginal, including when the new frequency label repeats another. Since $\mathbb E b^2=2/[k(k+1)]$ and $h(b)\le b(1-\log b)$, the expected squared change is $O(\log^2(k+1)/k^2)$. For the logarithm term, split at $b=1/k$ and use the boundedness of $x^2(\log x)^2$ on $(0,1]$. The Efron–Stein inequality gives

$$\operatorname{Var} F(W^{(k)})=O(\log^2(k+1)/k),$$

with an absolute constant. At $k=1$ the variance is zero. At any growing sparse scale, $F(W^{(k)})-a_k\to0$ in mean square, uniformly in the field order. Thus a persistent expected discrepancy at a growing sample count would also appear in typical samples. Bounding the mean $a_k$ itself still requires a comparison of the two signs.

The variance step uses the [Efron–Stein replacement inequality](https://statistics.stanford.edu/technical-reports/jackknife-estimate-variance).

## Two-mark diagonal geometry

For a support $S$ let $C_\sigma(S)$ be the downward closure of the projection of $\mathcal P_\sigma/\theta_\sigma$ onto the marks, in the nonnegative orthant. Here $\theta_+=\vartheta(\overline H)$ and $\theta_-=\vartheta(H)$, so $\theta_+\theta_-=n$. The two projected bodies are antipolars:

$$C_-(S)=\{y\ge0:\sup_{x\in C_+(S)}x\cdot y\le1\}.$$

One inclusion follows from complementary orthogonality, since the full spectra have dot product $n$. For the reverse, extend $\theta_-y$ by zero off $S$ to a cost $c$. The defining inequality says $\max_{P\in\mathcal P_+}P\cdot c\le n$. The dual Fourier LP minimizes $\sum Q_i$ over $Q\in U_-$ with $Q\ge c$. A minimizer of mean at most one can be raised by a constant to mean one, producing the required negative-side spectrum. The positive log optimization has the same value on the downward closure by coordinate monotonicity.

Take $S=\{0,h\}$ with $h\ne0$. Each body is invariant under exchange of coordinates, by reflecting frequencies about $h/2$. Define $g_\sigma(h)=\max\{t:(t,t)\in C_\sigma(S)\}$. Each body contains the two unit axis points and lies in $[0,1]^2$, so $g_\sigma\in[1/2,1]$. Its support function at $(1,1)$ equals $2g_\sigma$, by averaging a maximizer with its coordinate exchange. Thus $g_+(h)g_-(h)=1/2$ exactly.

Let $D(h)=\tfrac12\int_0^1[r_+(t,1-t)-r_-(t,1-t)]\,dt$, the contribution of this pair to $d_2/2$. Given only $g=g_+(h)$, we have the sharp bounds

$$\frac1g-\frac32\le D(h)\le\frac32-2g.$$

Indeed the plus body lies between the quadrilateral with vertices $(0,0),(1,0),(g,g),(0,1)$ and the unit square clipped by $x+y\le2g$. These have the same axis maxima, so their integrated rank is ordered in reverse of their log optima. To see the ordering, for the log optimum $L(t)$ on any of these symmetric polygons use $r(t)=t(1-t)L''(t)$ almost everywhere and integrate by parts. The integral of the rank is $L(0)+L(1)-2\int_0^1L(t)\,dt$. The clipped square's single positive-normal edge contributes rank one for weight interval length $1/g-1$. The inner quadrilateral has two such edges and each contributes length $1-g$. The two ranks sum to one for almost every pair weight, so subtracting $1/2$ gives the stated bounds. The polygons attain the two endpoints, with the limiting square and simplex cases included.

Thus the exact averaged first rank term lies between the shift averages of these bounds with factor $1-1/n$, accounting for coincident labels. At $g=1/\sqrt2$, the interval for an individual pair is $[\sqrt2-3/2,3/2-\sqrt2]$. The diagonal value alone can leave an ambiguity of this size. At $g\to1/2$ both bounds tend to $1/2$. In particular, an averaged rank term tending to its maximum $1/2$ is equivalent to the plus diagonal heights tending to $1/2$ in mean over uniform nonzero shifts. The upper bound implies necessity, and the lower bound implies sufficiency.

There is also a uniform weight-profile comparison near the simplex endpoint. For $w=(t,1-t)$, the unit simplex and the relaxed bound $x+y\le2g$ give

$$0\le F_+(w)-[\log\theta_+-\mathsf H(w)]\le\log(2g).$$

Hence if $g_+(h)\to1/2$ in mean over shifts, the whole signed pair-weight curve is close in mean, uniformly in $t$, to $a_1-\mathsf H(t,1-t)$.

## Comparing fixed supports by linear costs

More support directions can resolve the ambiguity of a single diagonal test. Let $C=C_\sigma(S)$ with $|S|=k$, and let $Q$ be the intersection of the unit cube with the supporting halfspaces tested on an $\ell_1$ $\delta$-net of the nonnegative simplex of cost vectors. The support function at any nonnegative normalized cost $c$ satisfies $h_Q(c)\le h_C(c)+2\delta$. Indeed, compare $c$ to a tested direction and use the unit cube to bound the changes in both support functions. Since the axis points belong to $C$, $h_C(c)\ge1/k$. Downward closure then gives the inclusion

$$\frac{Q}{1+2k\delta}\subseteq C\subseteq Q.$$

To verify the first inclusion it is enough to test nonnegative separating costs. For a nonnegative point separated by a cost with negative components, clip those components to zero. Downward closure preserves the support value under this clipping, and the separating point's value can only increase. The multiplicative inclusion changes the log optimum by at most $\log(1+2k\delta)$, uniformly in the distribution of the mark weights. Thus fixed sparse log geometry can be compared to arbitrary accuracy using linear Fourier LPs. For example, in two dimensions a uniform comparison of the normalized positive support function to $\|c\|_2$ would give the Euclidean positive quarter-disk log optimum $\log\theta_+-\tfrac12\mathsf H(w)$ up to the corresponding multiplicative error, and hence a small conditional rank difference. Establishing such a support-function comparison for typical prime-field shifts remains open.

## Exact coset shifts over square fields

At $q=r^2$ let $B=\mathbb F_r^\times$, $b=r-1$, $A=B^\perp$, and $m=(r+1)/2$. The [subfield witness](square-order-control.md) gives $\theta_+=b$ and $\theta_-=m$. Translated copies of $b\mathbf1_A$ reach the plus maximum at every frequency in one coset of $A$. On any mark support in that coset the normalized plus body is the full cube; the antipolar minus body is the simplex. For any weights on such marks, $F(w)=a_1+\mathsf H(w)$. In particular $g_+(h)=1$ for $h\in A\setminus\{0\}$.

If $r\equiv1\pmod4$, let $B'$ be the subgroup of order $m$ in the norm-one torus. For $x\in B'\setminus\{1\}$, $x^r=x^{-1}$ and $(1-x)^{r-1}=-1/x$, so $s(x)=(-1/x)^m=-1$. Hence $m\mathbf1_{(B')^\perp}$ is a feasible minus spectrum of mean one attaining the minus maximum across its coset. On any mark support in one such coset the roles reverse, giving $F(w)=a_1-\mathsf H(w)$ and $g_+(h)=1/2$ on its nonzero shifts. The two types of exact coset shifts occupy proportions $O(1/r)$ among all shifts. The behavior of typical shifts therefore requires information beyond these exact cases.

## Weighted removal of exceptional pairs

The separate ChatGPT exploration suggested excluding every sampled pair in a subfield coset by a union bound, which works for $k=o(q^{1/4})$. An expectation comparison extends the useful range. Keep the exponential masses and replace only the frequency labels. The binary-mixture inequality above gives

$$|\Delta F|\le 2h(\eta_j)$$

when label $j$ is moved, where $\eta_j$ is its normalized mass. The unmoved weights and the mass on the moved label are the same before and after, and every simplex vertex has the same value. Independence of masses and labels is essential here. For Dirichlet weights $\mathbb E h(\eta_j)=H_{k-1}/k$, where $H_j=1+1/2+\cdots+1/j$ is a harmonic number and $H_0=0$. This follows by differentiating the two beta moments $\mathbb E\eta_j^a$ and $\mathbb E(1-\eta_j)^a$ at $a=1$.

Let $E$ be a symmetric set of forbidden differences, including zero, and suppose $(k-1)|E|<n$. Build a new list by using each independent uniform proposed label if it avoids all forbidden differences to already accepted labels. On rejection draw a uniform acceptable label. At step $j$ at most $(j-1)|E|$ labels are excluded, so the probability of a change is at most $(j-1)|E|/n$. Summing the expected change in the log optimum under this coupling gives

$$|\mathbb EF(\widetilde W^{(k)})-a_k|\le (k-1)H_{k-1}|E|/n.$$

This sample law is the sequential uniform law on acceptable choices. For a single subgroup $E=A$, the number of acceptable labels is the same for all admissible prefixes of a fixed length, so the new list is exactly the iid list conditioned on distinct $A$-cosets. When $q=r^2$ and $r\equiv1\pmod4$, the two frequency subgroups $A$ and $(B')^\perp$ have coprime orders $m,b$ and give a product grid. For $E=A\cup(B')^\perp$, after $j-1$ accepted labels there are $(b-j+1)(m-j+1)$ cells with both a new row and a new column. The sequential law is again the corresponding conditional iid law. In these cases the comparison error is $O(k\log(k+1)/r)$. Thus excluding every such pair has vanishing effect on the mean for $k=o(r/\log r)$, even at scales where the admissible event has vanishing probability.

A variant removes bounded short relations. To avoid every nonzero translation-invariant integer relation on at most $d$ distinct labels with coefficients of absolute value at most $L$, exclude choices creating such a relation whose last index is the current one. For each set of earlier indices and coefficients the congruence in the new label has at most $L$ solutions. The excluded set has size $O_d((j-1)^{d-1}L^{d+1})$ at step $j$. Whenever the maximum of these bounds is smaller than $n$, the same weighted coupling changes the expected log optimum by at most $O_d(k^{d-1}L^{d+1}\log(k+1)/n)$. Here the admissible law is sequential. This supplies an input restriction for arithmetic comparisons on growing sparse samples, provided the restriction alone leads to control of the logarithmic optima.

### Removing repeated cosets at cost $O(k/b)$

For a partition into $b$ equal cells there is a sharper comparison. Index the frequency set by $(C,Y)$, where $C$ is the cell and $Y$ is the offset within its cell. Start with $k\le b$ independent uniform cell labels, a separate exchangeable list of $k$ offsets, and normalized masses $(w_j)_{j=1}^k$ independent of both. Replacing the cell labels by a uniformly random injective list, independently of the offsets and masses, changes the expected signed value by at most $(k-1)/b$ for Dirichlet masses. In particular the offsets can already be sampled without replacement when they represent the second coordinate of a product grid.

For the coupling, condition on the partition of indices into groups $G$ of equal old cells and on the masses. Put $W_G=\sum_{j\in G}w_j$, $p_j=w_j/W_G$, and ignore groups of zero mass. Sample an injective uniform list of $k$ new cells $C'_i$ and a separate list of exchangeable offsets $(Y'_j)$. In each group index its members cyclically and set $Y_{ij}=Y'_{i+j}$ with the sum taken in that group's index set. Under the old law, choose a shared row $I$ in each group with probabilities $p_i$. Place all that group's masses $w_j$ at $(C'_I,Y_{Ij})$. Under the new law, choose a shared column $J$ with probabilities $p_j$. Place the masses $w_i$ at $(C'_i,Y_{iJ})$. The old group's chosen cells form a uniformly injective list across groups, so they have the correct conditional distribution given the original equality partition. In either law the offsets in each group are a permutation of its input offsets, so by exchangeability the full list has its original law independently of the cells and weights.

Conditional on the two sampled lists and the partition and masses, both weight vectors have the same barycenter, with mass $W_Gp_ip_j$ on $(C'_i,Y_{ij})$ for each group, before aggregation. Write $A=\sum_G W_G\mathsf H(p_G)$ and $B=\sum_G W_G\sum_{i\in G}p_i\mathsf H(\nu_i)$, where $\nu_i=\sum_{j\in G}p_j\delta_{Y_{ij}}$. The entropy of the barycenter is $\mathsf H((W_G)_G)+A+B$. The old and new expected entropies conditional on the sampled lists are respectively $\mathsf H((W_G)_G)+B$ and $\mathsf H((W_G)_G)+A$. Thus conditional Jensen bounds compare their signed expectations with error at most $A+B\le2A$. For Dirichlet weights, size-biasing the original cell counts gives $\mathbb E A=\mathbb E H_{1+\operatorname{Bin}(k-1,1/b)}-1\le(k-1)/(2b)$. When cells are individual frequencies, $B=0$ and the resulting bound is $(k-1)/(2n)$.

On the square grid for $r\equiv1\pmod4$, apply this first to the $b$ row labels with independent column offsets. Apply it next to the $m$ column labels, using the now-injective row list as the exchangeable offsets. Conditioning on distinct rows and distinct columns therefore changes the expected signed optimum by at most $(k-1)(1/b+1/m)$ for $k\le\min(b,m)$. In particular the comparison has vanishing error throughout $k=o(r)$, even if a sample typically contains some collisions.

The coupling was independently enumerated with three labels, four cells, three offsets, and unequal fixed masses. For both iid and injective offsets it gave exactly the two required label distributions and equal barycenters, including the case of repeated offsets within a cell.

### Replacing the exponential masses by a fixed profile

Once the locations are an exchangeable injective list, their law is unchanged if the Dirichlet masses are sorted in decreasing order before assignment. The same holds for the list conditioned on distinct rows and columns. Let $V_j$ be the $j$-th largest mass and $q_j=\mathbb E V_j$. At every fixed list of locations, the signed Jensen bound gives a comparison error at most

$$\mathsf H(q)-\mathbb E\mathsf H(V)=\mathbb E D_{\mathrm{KL}}(V\|q)\le\sum_{j=1}^k\frac{\operatorname{Var}(V_j)}{q_j}.$$

The inequality uses $\log x\le x-1$. The increasing order statistics of $k$ independent unit exponentials have independent spacings with respective rates $k,k-1,\ldots,1$. In descending order the unnormalized $j$-th statistic is thus $\sum_{\ell=j}^k E_\ell/\ell$ with independent unit exponentials $E_\ell$. The sum of all the statistics is $\sum_\ell E_\ell$, so their normalization writes $V_j=\sum_{\ell=j}^k B_\ell/\ell$ for a Dirichlet vector $B$. With $s_j=\sum_{\ell=j}^k1/\ell$ and $c_j=\sum_{\ell=j}^k1/\ell^2$, the moment formulas give

$$q_j=\frac{s_j}{k},\qquad \frac{\operatorname{Var}(V_j)}{q_j}=\frac{1}{k+1}\left(\frac{c_j}{s_j}-\frac{s_j}{k}\right).$$

For $j>k/2$, $c_j/s_j\le 1/j\le2/k$. For $j\le k/2$, it is at most $2/[j\log(k/j)]$. Grouping the latter terms into intervals $(k/2^{d+1},k/2^d]$ bounds their sum by $O(1+\log\log(k+2))$. Thus replacing the random ordered masses by the deterministic decreasing profile $q_j=(H_k-H_{j-1})/k$ costs $O((1+\log\log(k+2))/k)$ in the expected signed optimum, uniformly in the field and in the exchangeable injective sampling law. Only the locations remain random in this comparison.

## The entropy carried by exact coset collisions

For the square-order plus subgroup $A$, let $C$ be the coset of a frequency drawn with weight $w$, so $\mathsf H(w\mid C)=\sum_C w(C)\mathsf H(w(\cdot\mid C))$. Each within-coset log problem has signed value $a_1+\mathsf H(w(\cdot\mid C))$. The full value equals $a_1+\mathsf H(w\mid C)$ plus the difference of the two Jensen gaps for mixing distinct cosets. The sum of those gaps is $\mathsf H(C)$. For the norm-one subgroup when $r\equiv1\pmod4$, the within-coset term has the opposite sign.

For any partition of the $n$ frequencies into $b$ equal cosets, independent uniform labels with Dirichlet masses give the exact expectation

$$\mathbb E\mathsf H(W^{(k)}\mid C)=\mathbb E H_{1+\operatorname{Bin}(k-1,1/b)}-\mathbb E H_{1+\operatorname{Bin}(k-1,1/n)}\le (k-1)/b.$$

Conditional on the $k$ labels, a class containing $j$ sampled labels has mean total mass $j/k$, and its normalized sampled masses have expected entropy $H_j-1$. Size-biasing the counts by a uniformly chosen index gives the binomial formula at the coset and frequency levels. Their difference is the conditional entropy. In particular the expected *frequency* entropy is $H_k-\mathbb E H_{1+\operatorname{Bin}(k-1,1/n)}$. ChatGPT's formula $H_k-1$ applies to the individual labelled masses and needs this collision correction for the aggregated frequency weights. The known within-coset contribution vanishes for $k=o(r)$ on square fields. The between-coset Jensen gaps can still account for a nonzero signed contribution, as the two-mark experiments indicate.

The two subgroup partitions also give exact values on sparse product weights. For $r\equiv1\pmod4$, identify the frequency grid with its subfield-coset row $R$ and norm-one-coset column $C$. If $w$ has row marginal $u$ and column marginal $v$, constant-on-row and constant-on-column spectra give

$$F_+(w)\ge\log b-\mathsf H(u),\qquad F_-(w)\ge\log m-\mathsf H(v).$$

Indeed each such spectrum is a mixture of the corresponding translates of the subgroup witness, and the best mixture weights are its target marginals. The two excesses above these lower bounds sum to the mutual information $I(R;C)=\mathsf H(u)+\mathsf H(v)-\mathsf H(w)$, by the entropy identity. Consequently

$$\left|F(w)-[a_1-\mathsf H(u)+\mathsf H(v)]\right|\le I(R;C).$$

For product weights this is an equality of the two signed expressions. For example, uniform weights on a $j\times j$ rectangle have $F(w)=a_1$ for every $j\le m$. Taking $j\to\infty$ with $j=o(r)$ gives growing sparse supports with persistent signed value on square fields. The iid assumption of the dense-tail theorem and of the sparse expected-value problem is thus consequential.

## Comparisons

The [two-mark LP probe](../two_mark_geometry.py) imposes reflection about the midpoint of the marks, solves for the common maximum on both signs, and applies the two sharp bounds. Even displacements use an integer center and odd displacements use a half-integer center, with the corresponding cosine bases. Both signs are optimized independently, so the product $g_+g_-=1/2$ checks the comparison. The [data](../data/two-mark-geometry.csv) have separate rows for the exact subgroup shifts, and either enumerate all nonzero shifts up to inversion or sample shifts uniformly for larger fields.

| Field order | Sample mean $g_+$ on nonzero shifts | Mean lower bound on $D$ | Mean upper bound on $D$ |
|---:|---:|---:|---:|
| $31^2$ | $0.5390$ | $0.3918$ | $0.4219$ |
| $1009$ | $0.7067$ | $-0.0827$ | $0.0867$ |
| $43^2$ | $0.5227$ | $0.4169$ | $0.4546$ |
| $1997$ | $0.7116$ | $-0.0927$ | $0.0768$ |

Each table row uses 24 random shifts. The two bounds bracket the true conditional pair term separately at each computed shift. The displayed averages describe those samples. They have sampling error for the mean over all nonzero shifts, in addition to the small floating-point LP error.

The 230 rows cover six prime and six square orders. The largest diagonal product error was $1.3\times10^{-10}$. The two-mark heights and rank bounds were also checked against complete vertex enumeration at 76 shifts from eight smaller orders, with numerical deviations below $1.6\times10^{-11}$. Both exact square subgroup heights were checked independently for $r=5,13,17,29,37$. Fifteen sparse product-weight profiles on three of those square grids agreed with their exact entropy formulas within $7\times10^{-9}$.

The [off-diagonal follow-up](two-mark-support.md) integrates the first rank term over support normals and compares both bounds on the same shifts.
