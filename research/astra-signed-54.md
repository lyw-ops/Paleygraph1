# Collecting the two Legendre characters inside the full Picard activation

The actual common marked section for sufficiently large eligible primes and prime squares extends to
\[
 513/32<\Re t<1057/64,\qquad |\Im t|<1/1024,
\]
with \(|m_q(t)|\le3/\sqrt n\). This overlaps the [previous common rectangle](marked-domain-53.md). The same signed expansion with the distinguished coefficient used in both upper certificates still has a rigorous escape barrier at \(t=127/8\). This obstruction concerns a specified majorant and gives no singularity of the marked germ.

## An arithmetic character expansion

Write \(S=2\sqrt nKe_0\), \(s=2\sqrt{q/n}\), and let \(Y=\mathcal A(N)\) be the average of the two full Legendre Mellin traces, where \(N=\mathrm{TwLeg}(1)[1]\) and the other object is \(N'=N\otimes\mathcal L_\chi\). The [exact Legendre formula](parallel-graph-shapes-23.md#a-fixed-number-of-path-columns-gives-no-leading-gain) gives \(KT_2(S/s)= Y-2\lambda/q\), with the small term a scalar Jacobi field of representation cost \(O(n^{-1/2})\). Equivalently the [marked-only exception rule](marked-domain-53.md) gives this error from the bad pair of lifts. Katz's arithmetic \(SL_2\) groups for the two Legendre objects give determinant one, including over the square base fields. On the good characters write \(Y=(\operatorname{tr}A+\operatorname{tr}B)/2\) with \(A,B\) their Frobenius conjugacy classes. For \(h\ge0\) decompose \(Y^h\) with coefficients \(m_{hab}\) on \(\operatorname{tr}\operatorname{Sym}^a A\operatorname{tr}\operatorname{Sym}^b B\). The initial coefficient is \(m_{000}=1\). Multiplication by \(Y\) sends each coefficient with half its weight to each valid neighbor \((a\pm1,b),(a,b\pm1)\). This is an equality of arithmetic tensor characters. It can be used for all finite fields in the eligible families without an equidistribution limit. [Geometric and arithmetic groups and boundary blocks](parallel-graph-shapes-23.md#a-fixed-number-of-path-columns-gives-no-leading-gain)

Put \(V=S+\alpha Y+Z\) and expand the update for \(Z\). If \(c_{jk}\) are the signed Jacobi Laurent coefficients of \(H_t(S+R)\), the coefficients **before taking moduli** are
\[
 d_{jkab}=\sum_{h\ge0}\binom{j+h}{j}\alpha^h c_{j+h,k}m_{hab}
     -\alpha\mathbf1_{(j,k,a,b)=(0,2,0,0)} .
\]
The subtraction represents \(-\alpha Y\) after taking \(K\), up to the small Jacobi correction. For each \(j\) form a symmetric positive kernel \(P_j\). Each \((k,a,b)\) adds \(|d_{jkab}|\) times the convolution of \(C_k=(\delta_k+\delta_{-k})/2\) with
\[
 (b+1)\sum_{i=0}^a\delta_{-2a+4i}.
\]
Indeed at full twist 1 the fiber weights of \(N\) are \(-2,2\), while those of \(N'\) are \(0,0\), by the two rank-two boundary blocks. At full twist \(\chi\) the factors are interchanged. The displayed kernel already includes the pooled answer after summing the symmetric coefficients in \((a,b)\). The two Jacobi powers are averaged independently, and the other factors in \(Z^j\) have independent lift choices. With \(L\) the [packet projection](astra-histogram-53.md), the upper update is therefore \(\sum_j L(P_j*\mu^{*j})\).

The summands of the symmetric powers are direct summands of convolution powers and preserve the two-character category. Their parity at the interior point follows from being summands of the corresponding even or odd products. At the exceptional cyclic coordinate the actual products and the represented products differ by at most twice their dimension bounds before applying \(K\). One can charge errors before or after collecting characters, using absolute coefficients in the former case. Both sums converge on the stated caps by the absolute Taylor bound. The [exact Picard argument](marked-domain-53.md) therefore adds only \(O(n^{-1/2})\) in the first packet, uniformly on this compact rectangle. It includes the correction from the distinguished seed and the true marked activation.

## Complex upper certificate

Choose the holomorphic \(\alpha=c_{02}^{[28]}(t)\), using the actual finite-field scale in the degree-28 polynomial. The matching subtracted term cancels algebraically at that degree before interval evaluation. On each closed floor slab of width \(1/64\), the [checker](astra-signed-54-check.py) collects all the signed irreducible coefficients up to degree 28 on the whole complex rectangle. It then takes componentwise maxima of the resulting positive kernels over the slabs. The all-core convolution and mixed remainder estimates of the previous packet proof apply unchanged, regarding each symmetric kernel as a positive sum of \(C_k\). The omitted Taylor part is bounded before splitting \(R=\alpha Y+Z\), charging its mass and second moment as \(2|\alpha|+b,4|\alpha|+c\). The constant mode is killed by \(K\). All 24 positive packet components and both residual budgets map below \(0.9999\) of their caps. The full coordinate bound is \(4.6\).

Initialize at \(S+\alpha Y\), so \(Z=0\); the true updates from this seed are holomorphic. The coordinate bound gives a Euclidean contraction on successive differences by \(4.6/\sqrt{4|t|-4.6^2}<3/4\), with a smaller marked bound for sufficiently large fields. The limit is the unique positive pair on the real interval; its overlap with the earlier holomorphic section agrees by the identity theorem. The marked bound follows by the same scaled inverse hyperbolic sine as in round 53.

## Freezing the zero weight

The lower part of the rectangle uses an invariant for the same full positive kernel with a different way of enclosing its distribution. Fix \(u=530953/10^6\) as a bound for the input mass at zero. For the nonzero weights use a symmetric 32-packet table \(H\) with **only its nonzero atoms**, and permit any positive symmetric excess \(E\) with \(\|E\|_\eta=\sum_w\cosh(\eta w)E(w)\le e\), where \(\eta=1/5\), \(e=34/10^5\). An admissible pooled measure is dominated by \(u\delta_0+H+E\) with \(E(0)=0\). Put \(M=u\delta_0+H\). The hyperbolic cosine norm multiplies under convolution of symmetric positive measures by the addition formula.

Evaluate the finite kernels on \(M\) by convolution. For the nonzero part of the output, charge only the positive excess over the individual atoms of \(H\) to the residual norm. Every mixed term with at least one old error has pre-projection norm bounded in total by
\[
 e\sum_{j\ge1}j\|P_j\|_\eta(\|M\|_\eta+e)^{j-1}.
\]
Projection preserves all its nonzero atoms. For the tail after Taylor order 14 use the ordinary binomial bound with ratio
\[
 r=(s\cosh\eta+|\alpha|(1+\cosh(2\eta))+\|M\|_\eta+e)^2/(4|t|).
\]
Indeed independent seed cosine powers have exactly the random-walk moment \((\cosh\eta)^p\) under their absolute cosine expansion, and the Legendre seed has pooled norm \(1+\cosh(2\eta)\). Thus the whole new off-zero excess has norm strictly less than \(e\). Its induced zero atom is at most the core contribution \(\sum_{a\ge1}(a-1)2H(a)\) plus \(e/\eta\), because \(a-1\le\cosh(\eta a)/\eta\). This total is strictly less than \(u\). The new measure is consequently in the same invariant, with slack for the small exact marked-column corrections. The last interval replay covers \([513/32,1041/64]\), overlapping the first certificate. Its ordinary input mass cap is \(u+\sum_{w\ne0}H(w)+e\); together with both distinguished seeds this again gives the full bound \(4.6\).

## Lower escape with the full irreducible-character collection

At \(t=127/8\) use the same distinguished coefficient \(\alpha=c_{02}^{[28]}\). A second check covers all real \( |\alpha-487/2000|\le10^{-6}\). In the limiting scale, and uniformly in the stated seed enclosure, the exact positive kernels have rigorous lower bounds. For Taylor orders beyond degree 28, the sum of the absolute coefficient errors in all the \(P_j\), weighted by \(2^j\) and counting the full input dimension, is at most
\[
 2\sqrt t\,\big|\tbinom{1/2}{15}\big|\,r^{15}/(1-r),\qquad
 r=(s+2|\alpha|+2)^2/(4t).
\]
Clebsch–Gordan decomposition of a monomial has nonnegative multiplicities, and their dimension sum at fixed \(h\) is \(2^h\). Thus the same tail divided by \(2^j\) bounds the change of each weight coefficient of the absolute kernel. The checker subtracts this error and retains only arities \(j\le8\), shifts of magnitude at most 14, and output packets through 24. Starting from zero the total packet mass of this lower recursion exceeds 21 at height 353 for the natural coefficient, and at height 382 uniformly on the second coefficient interval. The surviving shift-zero atom of \(P_2\) exceeds \(1/20\). Jensen conditionally on one packet draw gives \(\mathbb E|X+X'|\ge1\) for a normalized packet measure. Thus the next full mass is greater than the square of the old mass divided by 20. There is no positive finite-mass invariant for the full irreducible-character map with either of these prescriptions at this floor. Other choices of the distinguished coefficient have separate kernels.

## Ranked tests

1. Extract a second feedback field from \(KT_1(S/s)Y\) by identifying its arithmetic summands, boundary weights and genuine arithmetic unit contractions, then repeat the signed collection. A retained lower iteration above the reciprocal of a proved self-quadratic kernel coefficient rejects its absolute remainder invariant.
2. Optimize the holomorphic distinguished coefficient in a neighborhood of \(127/8\), including the scalar subtracted \(T_2\) mode. A lower escape uniform over an interval of coefficients excludes that entire interval; the displayed calculations cover the natural coefficient and the stated short interval.
