# A joint support obstruction to completion in the seven principal directions

The seven arithmetic projections from [round 60](signed-compact-60.md) cannot by themselves complete a cold averaged proposal. For either sign, any row built from the exact affine representative of the proposed mean and mark and an arbitrary linear combination of the seven pinned projections has a bulk value asymptotically at most the mean minus \(\sqrt2\) times its scaled mark. The bound worsens by at least one quarter of the coefficient \(\ell^1\) norm in the limiting support. The coefficients may depend on the field and depth, and may be unbounded. The result follows from an explicit joint compact support calculation at one Jacobi endpoint.

## Rows and bound

Write \(x=\sqrt n K e_0\), \(P_\sigma=(I-J_{\rm av}+\sigma K)/2\), \(\ell_\sigma=P_\sigma e_0\), and \(s_\sigma=(\ell_\sigma)_0\). Let
\[
 L_\sigma=P_\sigma-\ell_\sigma\ell_\sigma^{\mathsf T}/s_\sigma.
\]
Use the seven field versions of the sources
\[
 h=(x^2-1,xy,xz,xw,C_4,H_2,H_\times),\qquad
 Kh=(y,z,w,u_5,Q,D,E)
\]
from [round 60](signed-compact-60.md#source-projections-and-arithmetic-moments). In particular the last two sources are the arithmetic symmetric-square average and the cross product of the two Legendre lifts, with the exact prescribed finite normalization. Constant choices in \(h\) vanish under \(L_\sigma\).

For scaled mean \(G\), scaled mark \(a\ge0\), and \(c\in\mathbb R^7\), consider the row
\[
 R_{\sigma,q}=G\mathbf1+
       \frac{a\sqrt n-G}{s_\sigma}\ell_\sigma+
       \sum_{j=1}^7 c_j L_\sigma h_j.
 \tag{1}
\]
Its affine sector, mean and normalized mark \(R_{\sigma,q}(0)/\sqrt n=a\) are exact. For every \(0<\epsilon<1/4\) and \(B>0\), there are \(\eta>0\) and a field threshold such that on at least \(\eta n\) off-mark coordinates
\[
 R_{\sigma,q}(i)
 \,\le\, G-(\sqrt2-\epsilon)a
        -(1/4-\epsilon)\|c\|_1+\epsilon .
 \tag{2}
\]
This holds through eligible primes and prime squares, for both signs, all \(0\le a\le B\), \(|G|\le B\), and all \(c\) simultaneously in the sense that the witnessing set can depend on the sign pattern of \(c\). Thus if the gap \(\sqrt2 a-G\) is bounded below by a fixed positive number, the scaled rows have a uniform negative bulk margin on a positive fraction of the coordinates. In particular their normalized bulk \(L^2\) negativity does not tend to zero.

## Compact support in a prescribed cube

Let \(J\) be the positive circle coordinate, so \(X=(J+J^{-1})/\sqrt2\). In the compact model let \(H\) denote the centered source vector and \(T\) its seven outputs, as in round 60. At \(J=1\) the positive rank-three and rank-four coordinates and the arithmetic dual rank-four pair have determinant one. For \(U_5\) keep the perverse matrices on their prescribed determinant cosets. The Legendre factors, the two symplectic rank-four factors, the arithmetic dual rank-four pair and the symplectic rank-eight factor vary independently given \(J\). [Rank-three and rank-four normalization](rank-four-arithmetic-56.md) · [Higher fields](weighted-arithmetic-57.md) · [Positive and perverse determinants](astra-ranknext-58.md) · [New rank-four and rank-eight groups](two-node-groups-59.md) · [Cross Legendre group](astra-rankeight-60.md)

At this fiber the support of the vector \((H-T)/2\) contains the entire cube \([-1/4,1/4]^7\). To prescribe its coordinates \(d_j\), choose successively
\[
\begin{aligned}
 Y&=1-2d_1, & Z&=\sqrt2Y-2d_2, &
 W&=\sqrt2 Z-2d_3, & U_5&=\sqrt2 W-2d_4,\\
 Q&=1-2d_5, &
 D&=Y^2-1-2d_6, &
 E&=Y^2-2d_7 .
\end{aligned}
\tag{3}
\]
For the first choice set both Legendre traces \(A=B=Y\), possible in \(SU(2)\) since \(1/2\le Y\le3/2\). Then \(H_2=Y^2-1\) and \(H_\times=Y^2\). The two rank-three real traces may each be \(Z/\sqrt2\), because \(0\le Z\le 3\sqrt2/2+1/2\) and the real trace range of \(SU(3)\) includes \([-1,3]\). The four rank-four real traces may each be \(W/2\), since \(|W|\le 3+\sqrt2/2+1/2<8\) and \(SU(4)\) realizes every real trace in \([-4,4]\). These ranges follow from conjugate pairs \((e^{i\vartheta},e^{-i\vartheta})\), with a final 1 in odd dimension.

For \(U_5\) take each of the eight perverse real traces equal to \(-U_5/(2\sqrt2)\), as their sum has multiplier \(-1/(2\sqrt2)\). Here \(|U_5|\le (7/2)\sqrt2+3/2<6\sqrt2\). At dimension \(d\ge5\), the real trace range on any fixed unitary determinant coset contains \([-3,3]\). There are scalar matrices in the coset with phases within \(\pi/d\) of \(1\) and \(-1\), and the connected coset interpolates between their real traces. In particular the perverse determinant signs at positive \(J=1\) cause no restriction on this choice. The selected \(Q,D,E\) lie in \([-4,4],[-4,4],[-8,8]\), respectively. Their groups realize these intervals by conjugate pairs. The Jacobi terms in \(H\) both equal 1 at \(J=1\), completing (3).

For the other sign, the joint law is invariant under simultaneous sign reversal of \((X,T,A,B)\). All these variables are limits of negative Mellin fields, and all fixed odd words have vanishing mean. Compact support makes the polynomial moments determine their joint law. The source vector \(H\) is invariant under the reversal. It follows that at \(X=-\sqrt2\), the support of \((H+T)/2\) contains the same cube. The two conclusions can be written as a support cube for \((H+\sigma T)/2\) at \(\sigma X=-\sqrt2\).

## Transfer to the exact finite rows

For all bulk coordinates the canonical part of (1) is \(G+\sigma a x+O_B(n^{-1/2})\). This follows by substituting \(K_{00}=-1/n\) and \((\ell_\sigma)_i=(-1/n+\sigma K_{i0})/2\) off the mark. The seven inputs and their \(K\) outputs are uniformly bounded at their fixed ranks, allowing bounded exceptional errors and vanishing normalized \(L^2\) errors in the joint law. Therefore
\[
 (L_\sigma h_j)(i)
   =\tfrac12(h_j(i)+\sigma Kh_j(i)) + o(1)
\]
in normalized bulk \(L^2\). Indeed the limiting means of the centered inputs vanish, and the pinning subtraction at bulk coordinates equals \((\ell_\sigma)_i (P_\sigma h_j)_0/s_\sigma\), with \((P_\sigma h_j)_0=O(1)\) and \((\ell_\sigma)_i=O(n^{-1/2})\). The good-character equidistribution and the normalization checks used in the earlier joint moment laws give convergence of the empirical distribution of \((x,L_\sigma h)\) to the indicated compact coordinates. A bounded number of exceptional coordinates can be discarded.

For each sign pattern of \(c\), use the compact point with \(\sigma X=-\sqrt2\) and \(d_j=-\operatorname{sgn}(c_j)/4\), choosing an arbitrary sign when a coefficient is zero. Each fixed open neighborhood of this point has positive compact measure, because Haar measure on the full joint compact group has full support. There are at most \(2^7\) patterns per sector. Take a minimum over their neighborhood measures. For each pattern, weak convergence gives a fixed positive fraction of off-mark frequencies with \(\sigma x< -\sqrt2+\epsilon\) and every projected coordinate within \(\epsilon\) of its selected value. The uniform canonical error is less than \(\epsilon\) for all sufficiently large fields. This proves (2) without bounding the size of \(c\).

The same patches give an exact finite-field linear test independent of \(c\) or the averaging depth. Average \((L_\sigma h_j)_{j=1}^7\) over each of the \(2^7\) patches. The convex hull of the resulting seven-vectors contains the cube of radius \(1/4-\epsilon\), since its support function in direction \(c\) is at least \((1/4-\epsilon)\|c\|_1\). Take a convex combination giving zero and let \(\nu\) be the corresponding mixture of uniform probabilities on the patches. Then \(\nu\) annihilates all seven columns exactly, is supported on the off-mark arc \(\sigma x< -\sqrt2+\epsilon\), and has point masses at most \(1/(\eta n)\). If a positive row is written as (1) plus a further correction \(r\), then
\[
 \sum_i\nu_i r_i\ge(\sqrt2-\epsilon)a-G-\epsilon .
\]
For a fixed positive right-hand side the further correction must carry a positive normalized \(L^1\) mass. The bound also tests a proposed new direction on this same arc.

For the actual average, take \(G=\sqrt n M_T\) and \(a=X_{\sigma,T}(0)\) in (1). In the growing marked window the true budget and root cancellation give \(a=1+o(1)\) and \(G\le\sqrt{1+\tau}+o(1)\) at every fixed \(0\le\tau<1\). Thus an exact completion of the true mean and mark by this specified seven-source family is impossible for all sufficiently large primes, uniformly in eligible increasing depths in the window. This also excludes a vanishing extra scaled mean or a vanishing loss in the scaled mark within this family. The obstruction applies to either sign and follows directly from their common compact law.

The true projected average \(Z_{\sigma,T}=\sqrt n X_{\sigma,T}\) is the sum of a nonnegative raw average and an endpoint difference of normalized \(L^2\) norm at most \((\|v_{T+1}\|+\|v_1\|)/(2T)=O(T^{-1/2})\), by the energy bound. In particular its negative part has the same upper bound. The negative-part map is 1-Lipschitz, so (2) separates the true average in normalized \(L^2\) by a fixed positive amount from the entire seven-direction family. For the linear patch test above, the actual difference \(r=Z_{\sigma,T}-R_{\sigma,q}\) already obeys \(\sum_i\nu_i r_i\ge(\sqrt2-\epsilon)a-G-\epsilon-O(\eta^{-1/2}T^{-1/2})\), since \(n\nu_i\le1/\eta\). This quantifies how much the true history supplies outside the seven directions. [Actual endpoint identity and energy bound](astra-positive-39.md#1-a-positive-completion-with-an-explicit-price-at-each-time)

The next completion test should start from the actual depth-dependent average and bound the largest negative entry after a pinned exact-sector repair with \(o(1)\) extra scaled mean. The patch test checks that proposed approximations preserve the bulk contribution outside the seven directions before a pointwise certificate is attempted.
