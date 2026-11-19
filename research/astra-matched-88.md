# Which joint moments can persist on the actual matched fibers?

Let $p\equiv1\pmod4$ be prime, $Q=\mathbb F_p^{\times2}$, $n=(p-1)/2$, $D_\pm=\{x\in Q:\chi(1-x)=\pm1\}$. Let $F,R$ be the characteristic functions of any true complementary optimal probabilities $q,r$ on $G=\widehat Q$, oriented plus and minus, with common mark at zero. Their exterior Fourier supports on $Q$ are disjoint. Write $a=q_0,b=r_0$, so $nab=1$, $\max q=a,\max r=b\ll p^{-1/2}$, and $nq_i r_i=1_{i=0}$. On the matched fiber $M_h=\{x\in D_+:hx\in D_-\}$ the price is
\[
 H(h)=p^{-1/2}\sum_{M_h}(\Re R(hx)-\Re F(x)).
\]
Throughout use $h=h_0\ell^2$ with $h_0\in Q$ arbitrary and $\ell$ uniform among the rational primes at most $L=(\log p)^A$, for fixed $A>2$. Put $\eta=(\log p)^{1/2-A/4}$. A fixed nonvanishing full marked price forces half that signed price on almost all these shifts. We give a simultaneous restriction at the unnormalized mixed-product scale, and a deterministic bound for many adaptive deletions on the same pairs. [Matched price theorem](astra-diffuse-87.md) · [Marked criterion for ordinary theta](astra-complement-84.md#a-fixed-cubic-test-at-the-marked-root)

## Linear covariance at a fixed gap

For $h\ne1$ choose $x$ uniformly in $M_h$ and write $N_h=|M_h|=n/4+O(\sqrt p)$. Let $X=\sqrt n\,\Re F(x)$, $Y=\sqrt n\,\Re R(hx)$. Then, uniformly on both true optimal faces and every short translate,
\[
 \mathbb E_\ell\Big(
 |\mathbb E_{M_h}X-2\sqrt n\,a|+
 |\mathbb E_{M_h}Y-2\sqrt n\,b|+
 |\mathbb E_{M_h}XY-4|+
 |\operatorname{Cov}_{M_h}(X,Y)|\Big)\ll_A\eta .                 \tag{1}
\]
Give empty-fiber means and covariance value zero. Thus a fixed signed price can persist with asymptotically *unequal* first moments, whose product tends to four, and vanishing signed covariance. The product moment in (1) is order one after multiplying each individual coefficient by $\sqrt n$. In particular an unnormalized formula for the cross term is needed. Independently conjugating either of $F,R$ gives the same complex covariance conclusion for the unscaled coefficient sums in (2).

## Exact overlap behind the nonlinear covariances

Allow any polynomial or absolutely convergent series $P(z)=\sum_{k+l\ge1}c_{kl}z^k\bar z^l$ with $c_{kl}\ge0,\sum c_{kl}=1$, and independently choose another such filter $S$. Their degrees and weights may depend on the prime. Put $U=P(F),V=S(R)$. These are characteristic functions of probabilities $u,v$, formed by taking the indicated convex combinations of convolution powers of the two rows and their respective reflections. Each has its original sector and point cap $\|u\|_\infty\le a,\|v\|_\infty\le b$. Define
\[
 \begin{split}
 G_{U,V}(h)&=\sum_{x\in M_h}U(x)\overline{V(hx)}
  -\frac{\big(\sum_{M_h}U(x)\big)\overline{\big(\sum_{M_h}V(hx)\big)}}{N_h},\\
 \mu_i&=nu_i v_i,\qquad
 T(h)=\sum_{i\ne0}\mu_i\overline{i(h)}.
 \end{split}
\]
Set $G_{U,V}=0$ on an empty fiber. The measure $\mu$ has total mass one. The covariance of the actual pair satisfies
\[
 \mathbb E_\ell |G_{U,V}(h)-T(h)|\ll_A\eta.                         \tag{2}
\]
This uses each law's true marked mass, including changes of that mass under the filters.

Indeed multiplicative-character orthogonality gives $\sum_{x\in Q} U(x)\overline{V(hx)}=\sum_i\mu_i\overline{i(h)}$. At $h=1$ the left side equals one by the disjoint exterior sectors. For $h\ne1$ this full cross product differs from the strict matched product by precisely $\overline{V(h)}+U(h^{-1})$. Both axis terms have short mean absolute $O_A(\eta)$ by the capped-law sampling inequality of round 87. For either matched marginal, round 87's strict disagreement selector and the bounded Jacobi transform give
\[
 \frac1{\sqrt n}\sum_{M_h} U(x)=\frac{\sqrt n\,u_0}{2}
                 +O_{L^1(\ell),A}(\eta),
 \qquad
 \frac1{\sqrt n}\sum_{M_h} V(hx)=\frac{\sqrt n\,v_0}{2}
                 +O_{L^1(\ell),A}(\eta).
\]
The same proof applies to complex sums before taking real parts. Both normalized sums are uniformly bounded *pointwise*: each equals its bounded centered first term plus a constant multiple of a translated Jacobi column tested on a probability, with bounded axis corrections. Their product divided by $N_h/n$ is therefore $nu_0v_0+O_{L^1(\ell),A}(\eta)$. The sole possible $h=1$ costs $O(1/|\mathcal P_L|)$. This proves (2). For $U=\Re F,V=\Re R$ the corresponding laws are the evenizations. Reflection preserves optimal feasibility and the mark. Each choice of a reflected or unreflected law still has overlap $1/n$, with $q_0r_0=1/n$ exhausting it. Consequently their evenizations also have $\mu=\delta_0$, proving (1). This argument allows negative and complex positional coefficients.

## Localization of any nonlinear covariance

There is a single set of small-prime exceptional characters independent of the endpoints and filters. For fixed $0<e<1$ put
\[
 B_e=\{i\in G:|m_i|>e\},\qquad m_i=\mathbb E_\ell i(\ell^2).
\]
Then $|B_e|\le p^{1/A+o_A(1)}$ for fixed $e$, and with $\mu^{\rm ext}=\mu|_{G\setminus\{0\}}$,
\[
 \sup_{h_0}\mathbb E_\ell |G_{U,V}(h_0\ell^2)|
 \le O_A(\eta)+
 \big(e+\sup_j\mu^{\rm ext}(j+B_e)\big)^{1/2}.                       \tag{3}
\]
In particular a short mean absolute covariance bounded below by $c>0$ forces mass at least $c^2/2$ of the **actual exterior convolution-law overlap** on one translate of $B_{c^2/4}$ for all sufficiently large primes after decreasing $c$ to at most one if necessary. The indicated translate has at most $p^{1/A+o(1)}$ sites. For a prescribed larger exponent $A$ the statement holds on its corresponding short family.

For the size estimate take $j=\lfloor\log(p/3)/\log L\rfloor$, $M=|\mathcal P_L|$. Unique factorization and character orthogonality give
$\sum_i|m_i|^{2j}\le n j!/M^j$ since products of $j$ primes are at most $p/3$ and their squares agree modulo $p$ only when the integer products agree. Chebyshev's lower bound $M\gg L/\log L$ gives $\log(n(j/(Me^2))^j)\le (1/A+o(1))\log p$. Expanding the squared modulus of $T(h_0\ell^2)$ bounds its mean by $\sum_{i,k}\mu_i^{\rm ext}\mu_k^{\rm ext}|m_{i-k}|$. Split the differences at $B_e$ and use $\|\mu^{\rm ext}\|_1\le1$. Cauchy–Schwarz and (2) give (3). In particular, degree growth alone costs nothing for these convex combinations. The expectation is taken after choosing the filters.

A sign restriction retaining the phases holds on the short family of ratios $h=\ell_1^2/\ell_2^2$ with independently chosen primes. Equation (2) still holds after conditioning on the denominator. The real averaged covariance satisfies
\[
 \mathbb E_{\ell_1,\ell_2}\Re G_{U,V}(h)
       =\sum_{i\ne0}nu_i v_i |m_i|^2+O_A(\eta)\ \ge -O_A(\eta).         \tag{4}
\]
A positive limiting average in (4) forces actual mass on $B_e$ itself for sufficiently small fixed $e$. The nonvanishing linear matched price from round 87 still persists on almost all these ratios by the same conditioning.

## A forced short rational ratio between the two intermediate spectra

Write $A_4=\sum_{Q}|F|^4$, $B_4=\sum_Q |R|^4$, and continue to use the short ratio family in (4). There is a uniform lower bound at the raw joint-product scale
\[
 \mathbb E_{\ell_1,\ell_2}\sum_{M_h}|F(x)R(hx)|^4
        \ \ge\ A_4B_4/n-O_A(\eta).                                   \tag{4a}
\]
In fact for $P(z)=S(z)=|z|^4$, orthogonality gives $u_0=A_4/n$, $v_0=B_4/n$. In the full cross product the ratio average of every Fourier character is $|m_i|^2$, so its contribution from the mark is $A_4B_4/n$ and every exterior contribution is nonnegative. The axis removal has short mean absolute $O_A(\eta)$ as in (2).

Suppose $A_4B_4/n\ge c>0$ along a prime sequence. This holds in particular if *both* endpoints have $\gg_\tau\sqrt p$ sites at some fixed modulus threshold $\tau>0$. Choose $t>0$ with $t^2\le c/4$. The round-86 fiber bound gives $\sum_{M_h}|FR|^2\le1$ at every $h\ne1$, where $FR$ here abbreviates $F(x)R(hx)$. On pairs where at least one end has modulus below $t$, their total fourth-product cost is at most $t^2$. The whole fourth-product cost on a fiber is at most one. Thus at least a $c/2$ fraction of the ordered prime ratios, eventually, have a matched pair with **both** endpoint moduli at least $t$. There are at most $t^{-4}$ such witnesses per ratio. Off the diagonal the ratios $\ell_1^2/\ell_2^2$ are all distinct for large $p$: equality forces the positive integer cross products, both at most $L^2<p/3$, to agree. Hence the intermediate head ratio set contains $\gg_c|\mathcal P_L|^2$ distinct explicit short rational squares. Along a fixed gap, all but $o(1)$ of this positive fraction also satisfy the mean and covariance limits in (1) and the half-price estimate. All their joint intermediate pairs together cost $o(1)$ in the normalized marked *linear* price, which the remaining pairs must then pay.

This ratio count is hereditary on the set of rational primes. For every subset $J\subset\mathcal P_L$ of size $M'$, the capped-law short bound for a uniform prime in $J$ is $O_A(\eta\sqrt{M/M'})$. In the round-87 proof the same moment order $j$ works and unique factorization bounds collisions by $j!(M')^j$. The earlier bound $(n\|u\|_\infty)^{1/(2j)}\sqrt{j/M}$ acquires exactly the displayed factor. Apply this to the two axes in (4a), conditioning on either denominator. Thus *every* $J$ with $M'\ge C_{A,c}\eta^2M$ contains at least a $c/2$ fraction of its ordered pairs witnessed by the two $t$-heads, for a sufficiently large constant and $t^2\le c/4$. Equivalently the undirected graph joining primes in the presence of such a ratio has independence number $O_{A,c}(\eta^2M)$. Inversion invariance of the modulus heads makes the two edge orientations equivalent. On subsets with $M'/(\eta^2M)\to\infty$ the half-price and covariance estimates also have vanishing errors, by the same replacement in the sampling bound.

There is a signed version. Take $P(z)=S(z)=z|z|^2$, and suppose the product of the relative signed marks $(u_0/a)(v_0/b)$ is at least $c>0$. Thus $u_0=n^{-1}\sum F|F|^2$ and $v_0=n^{-1}\sum R|R|^2$ are genuine nonnegative convolution masses, with the signs in the sums retained. The same axis argument gives a ratio-averaged lower bound $c-O_A(\eta)$ for
\[
    \sum_{M_h}\Re\{F(x)\overline{R(hx)}\}\,|F(x)R(hx)|^2 .
\]
On pairs with an end below $t$ the sum of absolute values is at most $t\sum |FR|^2\le t$, and the entire absolute sum is at most one. For $0<t\le c/4$ a positive fraction of short ratios therefore have a joint $t$-head witness with $\Re(F(x)\overline{R(hx)})>0$. This conclusion about phases allows both original rows to be noneven.

## Deterministic erasure on the surviving signed price

Let $T_0(x)=(1-2x)^2$ and let $S$ be any subset of a true fixed $\tau$-head in either row. An image here means $g(T_0(S)\cap Q)$, with any $g\in Q$, or its inversion. For $K$ such images, potentially chosen *after seeing* $h$, discard any collection of matched pairs whose first output $x$ or second output $(hx)^{-1}$ lies in their union. The total absolute charge removed, including both ends, satisfies
\[
  \frac1{\sqrt p}\sum_{\rm discarded}(|F(x)|+|R(hx)|)
          \ll_\tau K p^{-1/1056}                                     \tag{5}
\]
at **every** shift. Indeed each endpoint or partner of a touched pair lies, up to inversion, in some dilate of $T_0(S)\cap Q$. The modulus of a characteristic function is inversion invariant, and a quadratic-residue dilate $z(1-2x)^2$ is again the square of a nondegenerate affine function. Round 86's prime incidence bound on the whole image therefore applies to either row, uniformly in all dilations. Each site enters at most once per choice of touched end on a fixed fiber. Summing its four possible endpoint charges proves (5). [Uniform affine-square estimate (5)](astra-fibers-86.md#a-prime-field-incidence-bound-for-the-intermediate-spectra)

In particular the balanced images of round 86 can be deleted at a power-saving cost at every shift. The signed price still persists on almost every short shift after $K=o_\tau(p^{1/1056})$ such adaptive deletions, with no disjointness hypothesis. Exact cancellation of the two signed counts holds pair by pair. Equation (1) concerns the complete matched fiber: (5) has a $1/\sqrt p$ normalization and does not transfer the unnormalized covariance through the deletions.

There is a complementary estimate for a sharp amplitude cutoff which uses no prime averaging. The round-86 conditional-law Parseval bound gives $\sum_{M_h}|F(x)R(hx)|^2\le1$ for every $h\ne1$, also after conjugation. For $0<u\le1$, the absolute matched linear price on pairs with *both* moduli at least $u$ is at most $2/(\sqrt p\,u^3)$, since each modulus there is at most $u^{-3}|FR|^2$. On pairs with one specified end of modulus above $u$, the opposite modulus costs at most $O(p^{-1/4}u^{-2})$ after division by $\sqrt p$. In fact the large end has at most $O(\sqrt p/u^2)$ sites by the point cap and Parseval, and on that subset the sum of squares of the opposite modulus is at most $u^{-2}$. This bounds, simultaneously in all shifts and sharp thresholds, the partner loss when separate truncated marginal prices are replaced by whole-pair truncation. Both-head absolute price is negligible for $u p^{1/6}\to\infty$. The partner bound gives the corresponding conclusion for $u p^{1/8}\to\infty$.

## Finite check and next tests

The [Arb384 checker](astra-matched-88-check.py) reconstructs complementary optima at primes 53, 257 and 409. At the latter two it solves the forbidden sine equations and adds a strictly feasible odd displacement to the minus row, yielding genuinely complex coefficients. At every shift it checks the raw cross-product transform and its strict axis corrections, the fiber square-product budget, and the finite ratio transform using four rational primes. It also checks the absolute toll of two shift-dependent translated or inverted images against the four endpoint sums used in (5). At 409 the $F|F|^2,R^2$ test has exterior ratio transform in $(0.231703121,0.231703122)$ and measured real matched covariance in $(0.000299257,0.000299258)$. The difference includes the finite axes and measured marginal correction. For the signed-cubic test, all 12 off-diagonal ordered ratios there have a positive-phase joint witness at threshold $1/8$. The four diagonal ratios have empty strict fibers. [Outward intervals](astra-matched-88-checks.jsonl)

1. For one family and a fixed-gap sequence, compare the first marginal prices on the pairs surviving (5). At almost every short shift the leading covariance (1) vanishes even when the means differ, so a useful comparison must constrain the means themselves. The surviving first-price difference $o(1)$ on a positive proportion of shifts would suffice for ordinary theta.
2. For filters extracting the two intermediate signed prices, for example $P(z)=z|z|^{2j}$, test the actual overlap $nu_i v_i$ on translates of $B_e$. Bounding all such masses by $o(1)$ gives short-family nonlinear decorrelation by (3); linking decorrelation to equality of the linear means is a further step. No arithmetic upper on the full matched first-price difference is obtained here.
