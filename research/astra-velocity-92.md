# A real marked-column integral forced by first contact

Let $t=x+iy$ be on a true real-start vertical ray in the nominated square about $2031/128$. Up to and including a first bulk angle tie, the complex incoming velocity integral of [round 91, (4a)](astra-contact-91.md) forces a signed integral on a **real** marked-weight interval. The bulk profile on the real interval is constant and can be chosen within $10^{-8}$ of one at every site. At a first tie the signed, averaged column somewhere on that interval then exceeds $956/\sqrt n$ in the direction fixed by the tie data. A separate choice makes every bulk weight exactly one and gives unconditional third- and fourth-moment comparisons with that ordinary real stationary branch. The comparisons cover multiple and tangent ties.

## Simultaneous changes to the real weights

Use full counting multiplicities, $s=u+iv=n/t$, $a=1/\sqrt2$, and the two genuine nonnegative endpoint pairs $P^\pm,Q^\pm$ of [the two-mark reduction](real-two-marks-91.md). Their common bulk product is $k$, their respective marked products are $h\pm d$, $d=v/a$, $h\ge u>|d|$. At an unforced floor before or at contact put $z_i=\sin\phi_i$, $\nu_i=\cos\phi_i>0$ in the bulk, so $z_i$ is exactly the coordinate obtained by integrating the incoming velocity from its zero real value. Then
\[
 k_i=1-3z_i^2,\qquad \sigma_i=\operatorname{sgn}(z_i),\qquad
 F_i=(\nu_i+|z_i|/a)^2.
\]
In particular $k_i=0$ precisely at ties and $F_i=8/3$ there. On a positive sign the favorable endpoint product is $P_i^+Q_i^-=F_i$, and on a negative sign it is $Q_i^+P_i^-=F_i$. This follows by writing the real parts of the original two factors as $e^{\pm\gamma_i}\nu_i$ and their imaginary parts as $\pm e^{\pm\gamma_i}z_i$.

For a comparison at either endpoint let $w=(h\pm d,k)$ and let $w'>0$ have the same marked entry. Take its positive real stationary pair $P',Q'$. At every site choose either factor of the original pair as $X_j>0$ and the corresponding factor of the new pair as $X_j'$. At a zero weight choose the positive original factor, which exists at the endpoint ties considered here. Put $R_j=X'_j/X_j$. Writing $m,m'$ for the respective means, cross-pairing of the two native Fourier sectors gives the exact identity
\[
 \sum_j\left(\sqrt{w'_j/R_j}-\sqrt{w_j R_j}\right)^2
 =\sum_j(\sqrt{w'_j}-\sqrt{w_j})^2-n(m'-m)^2.                        \tag{1}
\]
Indeed the two cross products at a site are $w'_j/R_j$ and $w_jR_j$ in either order. The full sum of either cross pairing is $nmm'$, and $\sum w_j=nm^2$. The summand on the left is convex in $\log R_j$, with slope $w_j-w'_j$ at zero. Subtract its tangent in (1) to obtain
\[
              \sum_j(w'_j-w_j)\log R_j\ \ge\ n(m'-m)^2.                \tag{2}
\]
The choices of factor can differ at every site and at the two endpoints, including when some old factors vanish.

Fix $0<e\le1$. In the bulk set
\[
 k'_i=\max(k_i,e),\quad b_i=(e-k_i)_+,\quad
 \lambda_i=b_i/\sum_{j\ne0} b_j .
\]
Use this test if the denominator is positive, automatically the case at any first tie. It can also be used strictly before the first tie if some $k_i<e$. Write $J(r^2,k')$ for the actual weighted reflection of the positive real pair at marked weight $r^2$ and bulk weights $k'$. Set $r_\pm=\sqrt{h\pm d}$; integrals from $r_-$ to $r_+$ are oriented. At fixed bulk weights the [marked-response differential](marked-response.md#weighted-complementary-projections) gives
\[
 \partial_r\left(\tfrac12\log(P_i/Q_i)\right)=J(r^2,k')_{i0}/\sqrt{k'_i}.
\]
Use (2) at both ends, selecting the two original favorable factors on each site in the support of $b$. Since the new bulk product there is $e$, the product of the two corresponding new factors is $e\exp(\sigma_i\int J_{i0}\,dr/\sqrt e)$. Adding the two inequalities proves
\[
 \boxed{\quad \int_{r_-}^{r_+}\sum_i\lambda_i\sigma_i J(r^2,k')_{i0}\,dr
 \ \ge\ \sqrt e\sum_i\lambda_i\log(F_i/e) .\quad}                       \tag{3}
\]
The discarded nonnegative gain is $\sqrt e\,n[(m'_+-m_+)^2+(m'_--m_-)^2]/\sum b_i$. The path in (3) consists throughout of actual unconstrained positive real stationary pairs. Its fixed profile and labels are determined from the true complex endpoint. The original complex velocity may change sign along its ray.

## Quantitative arithmetic tests

On $k_i<e<1$, the favorable factor increases with $|z_i|$ up to $1/\sqrt3$. At $k_i=e$, one has $F_i/e=(1+q)/(1-q)$ with $q=\sqrt{(1-e)/(1+e/2)}$. Thus the right side of (3) is at least
\[
              L(e)=2\sqrt e\,\operatorname{arctanh}\sqrt{(1-e)/(1+e/2)}.
\]
The interval length obeys $\ell=|r_+-r_-|\le |d|/\sqrt{u-|d|}$. For $X=2031/128-2^{-17}$, $Y=2^{-17}$, this gives
\[
 \sqrt n/\ell\ \ge\ a X^{3/2}\sqrt{1-Y/(aX)}/|y| .
\]
Indeed $\sqrt{n(u-|d|)}/|d|=a|t|\sqrt{x-|y|/a}/|y|$. With $\eta=\operatorname{sgn}(d)$, some $r$ between the two endpoints therefore satisfies
\[
 \eta\sqrt n\sum_i\lambda_i\sigma_i J(r^2,k')_{i0}
 \ \ge\ a X^{3/2}\sqrt{1-Y/(aX)}\,L(e)/|y| .                            \tag{4}
\]
For $e=1/4$ the right side exceeds $51.22/|y|$, hence $6.71\cdot10^6$. For $e=1-10^{-8}$ it exceeds $0.007298/|y|$, hence $956$. The latter bulk profile lies in $[1-10^{-8},1]$ on the entire bulk. Equation (3) retains an oriented interval test on one fixed bulk profile.

There is an arithmetic version at that same real mark. Let $H_\pm$ be the two native mean-zero Paley Fourier sectors on the full cyclic group. Given the actual real amplitudes $g_i=\frac12\log(P_i/Q_i)$, take the projection determinantal distribution for the columns of a Fourier basis of $H_+$ scaled on its rows by $e^{-g_i}$, or of $H_-$ scaled by $e^{g_i}$. Equivalently sample a full-rank row-index set with probability proportional to its squared basis minor in these scaled Fourier matrices. Its projection kernel is $\Pi_\pm$. By Cauchy–Binet, one-point probabilities are its diagonal and two-point probabilities are the corresponding principal minors. This follows by expanding $\det(U^*\operatorname{diag}(1+t_j)U)$ in the $t_j$ for an orthonormal column basis $U$. Thus for inclusion indicators $I_j$, $\operatorname{Cov}_\pm(I_i,I_0)=-|(\Pi_\pm)_{i0}|^2$ off the mark.

At the mark selected by (4), $2\Pi_\pm=I-\sqrt w\sqrt w^{\mathsf T}/W\pm J$, $w=(r^2,k')$, $W=\sum w_j$. On the selected bulk sites the scaled rank-one entry is $\sqrt{ne}\,r/W\le\sqrt{ne/(u-|d|)}<4$ on the cold square. Weighted Cauchy–Schwarz in (4) proves, for **both** determinantal distributions at this same real mark,
\[
      -n\sum_i\lambda_i\operatorname{Cov}_\pm(I_i,I_0)
      \ \ge\ \tfrac14\big(\sqrt n L(e)/\ell-4\big)_+^2 .                 \tag{5}
\]
For $e=1-10^{-8}$ the left side exceeds $226{,}000$ on the square at any first tie. The raw unscaled Fourier sector has $2|(\Pi^{\rm native}_\pm)_{i0}|\le(1+\sqrt p)/n$ by the Jacobi entry bound. The real amplitude scaling in (5), including the extensive marked weight, matters even when the bulk products are nearly flat.

## Ordinary unit bulk and a real degeneracy

Set $e=1$. Now $k'\equiv1$ on the bulk at all marks, and $\lambda_i=z_i^2/\sum_j z_j^2$. The concave function $2\log(\sqrt{1-z^2}+\sqrt2 z)$ lies above the chord between $0$ and $1/\sqrt3$. Thus (3) and Hölder give, in full counting norms,
\[
 \sqrt3\log(8/3)\,\|z_B\|_3
 \ \le\ \int_{\min r_\pm}^{\max r_\pm}\|J(r^2,\mathbf1)_{B0}\|_3\,dr .   \tag{6}
\]
Indeed before Hölder the left side is the stated constant times $\sum|z_i|^3$ and the right integrand is oriented and signed with coefficients $z_i|z_i|$. The case $z_B=0$ is automatic. This estimate uses the physical ordinary positive real stationary branch with bulk product exactly one. Its marked interval can also be overapproximated without knowing the phase data, using $u\le h\le u+2c d^2/u$, $c=(1+a^2)/4$, from the two-mark bracket. A normalized third moment can still miss an individual contact through unbounded $n$.

In fact the flat real branch controls a fourth moment, with an additional cubic estimate on coordinates where its own incoming integral is too small. Write
\[
 G_i=\int_{r_-}^{r_+}J(r^2,\mathbf1)_{i0}\,dr,\qquad
 V_i=\max\{(\nu_i+z_i/a)^2e^{-G_i},\,(\nu_i-z_i/a)^2e^{G_i}\}.
\]
At each site in (2) choose the plus factor at one endpoint and the minus factor at the other in the orientation **maximizing** $V_i$, which can depend on $G_i$. The joint factor ratio is $1/V_i$, the weight increase is $3z_i^2$, and the mean terms are nonnegative. Hence
\[
                              \sum_B z_i^2\log V_i\le0 .                 \tag{7}
\]
At a tie the log is exactly $\log(8/3)-\sigma_iG_i$. Elsewhere it is $\log k_i+|G_i-2\operatorname{arctanh}(z_i/(a\nu_i))|$. Thus negative contributions arise only on sites where the **signed** flat-profile integral matches that phase parameter within $-\log k_i$.

Put $v_i=|z_i|$. The same chord bound gives $\log V_i\ge(3/2)v_i-|G_i|$. On $\log V_i<0$ one has $v_i<(2/3)|G_i|$. If $v_i\le1/\sqrt6$, then $V_i\ge k_i\ge1/2$ by the geometric mean, so $-\log V_i\le6v_i^2$. For $v_i>1/\sqrt6$ one has $|G_i|>1/2$ and $-\log V_i\le|G_i|$. Both cases give $v_i^2(\log V_i)_-\le(4/3)|G_i|^4$. Wherever $v_i\ge4|G_i|/3$, the positive lower bound is $\log V_i\ge3v_i/4$. Combining with (7) and then using $v_i\le1/\sqrt3$ gives
\[
 \sum_{v_i\ge4|G_i|/3}v_i^3\le\tfrac{16}{9}\sum_B|G_i|^4,\qquad
 \|z_B\|_4\le
 \left[(4/3)^4+\tfrac{16}{9\sqrt3}\right]^{1/4}\|G_B\|_4
 <1.44\|G_B\|_4                                                       \tag{8}
\]
for nonzero $G_B$, with the zero bound otherwise. For the true tie set $C$, retaining just its own positive summands in (7) gives the flat-profile test
\[
 \sum_{i\in C}\big(\log(8/3)-\sigma_i G_i\big)_+
      \le 4\sum_{i:\log V_i<0}|G_i|^4.                                  \tag{9}
\]
In particular, a tied site whose signed integral is below $\frac12\log(8/3)$ requires a fourth-power sum exceeding $\frac18\log(8/3)$ on the actual paying sites. All integrals in (6)–(9) use ordinary unit-bulk real Paley stationary rows. Counting norms can grow through primes even when each real column has its natural pointwise scale.

For each tied $i$ there is also a marked weight between $h-d$ and $h+d$ at which **both** real factors vanish at $i$ for the original common profile $k$. To see this without any uniqueness assumption, the full set of nonnegative stationary pairs at each marked weight is compact. All positively charged factors are fixed by strict concavity. On each zero site every possible plus row has zero product with every possible minus row. This follows by cross-pairing them, subtracting the fixed sum on charged sites and using nonnegativity. Hence the fiber is a product of convex sets and is connected. Its graph above the compact interval is compact by the mean bounds and closed equations. If the graph were disconnected the two disjoint compact pieces would project to disjoint closed sets covering the interval, since the fibers are connected. This is impossible. The continuous function $P_i-Q_i$ has opposite signs at the two switched endpoints. It must take zero, where $P_iQ_i=k_i=0$ forces the joint zero. Different tied sites may have different intermediate marks.

## Finite replay and next tests

At $p=173$, the real-start ray to $t=2031/128+i/131072$ stays inside the cap. With $e=1-2\cdot10^{-14}$, the six selected inversion orbits have twelve sites. At 256-bit Arb precision the integral in (3) is $2.41314076196\ldots\cdot10^{-7}$, above the signed phase-data lower bound $2.41314074356\ldots\cdot10^{-7}$. Direct differentiation of the real physical equation encloses the scaled oriented column average in $(1.413,1.415)$ throughout the real interval and agrees with the independent endpoint log-ratio integral. At the same physical floor, an independent solve with exactly unit bulk gives all 85 bulk sites negative summands in (7), with signed sum $-4.71953441779\ldots\cdot10^{-27}$. The fourth-power sums of $z$ and $G$ lie respectively in $(1.573,1.574)\cdot10^{-27}$ and $(1.006,1.007)\cdot10^{-25}$. A contraction enclosure connects the complex point to its real start. This prime checks the identity in the nominated square and has $n=86$. The actual small-floor first tie is separately certified in round 91. [Checker](astra-velocity-92-check.py) · [Outward records](astra-velocity-92-checks.jsonl)

1. On the real marked interval, bound the squared Fourier minors in (5) for the single nearly flat bulk profile $k'=\max(k,1-10^{-8})$ selected by the first tie. A uniform average below $226{,}000/n$ for either sector at every mark of this interval precludes that tie. A bound valid for every even profile in this narrow weight box would suffice without identifying the selected one.
2. On the ordinary unit-bulk real branch, use (9) to bound the fourth-power charge on sites satisfying the signed match in (7), against the shortfall on the tie set. This retains the original real bulk of exactly one and confines the negative contributions to a data-defined set. Neither the required real-column estimate nor the ordinary-theta limit is established here.
