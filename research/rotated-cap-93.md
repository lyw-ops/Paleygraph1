# Translated phase caps and the two signed corrections

A symmetric cap centered at a nonzero admissible relative angle also has genuine clipped stationary pairs. Their two signed corrections are canonical. Moving the cap center decreases the upper-minus-lower correction, at a rate controlled by the total product on the actively corrected sites. Opening the cap decreases the total correction with the same lower rate, twice the general coefficient from round 92 in the angular coordinate. These conclusions use the anisotropic factor pairing directly. A common cap-free section through unbounded primes remains open.

## A genuine rotated clipped problem

Normalize the bulk products to one and write \(u+iv=n/t\), \(u>0\). Let \(0<\theta<\pi/4\), \(a=\tan\theta\), \(b\) be the phase center, and \(\rho=|v|/u\). For existence use
\[
       \rho\le 1/100,\qquad |b|<\theta,\qquad \theta-|b|>10\rho .
\]
Seek complementary complex factors \(A,B\) with equal mean \(M\), marked product \(u+iv\), and bulk products \(q=1+e\ge1\). Set \(A'=e^{-ib}A,\ B'=e^{ib}B\), and require positive real parts, \(|\arg A_i'|\le\theta\) on the bulk, and \(e_i>0\) only at an endpoint. At the mark require both rotated absolute angles to be at most \(\theta\). They will be strictly smaller. The two opposite bulk phases are \(\pm(\phi_i-b)\), with \(\phi_i=\arg A_i\) in the resulting unrotated lift. The two signs refer to the upper and lower endpoints of the relative bulk interval.

Here is an existence construction. Given positive real weights \(w\), take their [positive real stationary pair](marked-response.md#weighted-complementary-projections) of equal mean \(\sqrt{W/n}\), where \(W=\sum_i w_i\). Write \(\nu=\sqrt w\), \(J_w\) for the difference of the two orthogonal weighted sector projections, and \(c_i=(J_w)_{i0}\). Determine \(\omega\in(-\pi/2+|b|,\pi/2-|b|)\) by
\[
 \frac{\tan(\omega-b)+\tan(\omega+b)}2=\frac{v}{2W},\qquad
 \zeta=\frac{\tan(\omega-b)-\tan(\omega+b)}2 .
\]
The left side is strictly increasing onto \(\mathbb R\) with derivative at least one. Set \(P_i=0\) off the mark, \(P_0=v/(2w_0)\), and prescribe the phase-tangent difference by
\[
        D_i=\zeta+\frac{v c_i}{2\nu_0\nu_i}.
\]
Then \(\nu(P-v/(2W))\) is perpendicular to \(\nu\), and \(J_w[\nu(P-v/(2W))]=\nu(D-\zeta)\). Consequently the two real stationary factors multiplied by \(1+i(P+D)\) and \(1+i(P-D)\) belong to the complexified complementary sectors. Their mean angles are respectively \(\omega-b\) and \(\omega+b\). An inverse pair of positive real scale factors makes their mean moduli equal without changing any product. Rotating back gives equal mean \(M\).

To solve the pointwise products by Brouwer, restrict \(w_0\) to \([u/3,2u]\). Then \(|\omega|\le 3\rho/2\), so \(|\zeta|\le z_*=\tan(|b|+3\rho/2)<a\). Put \(v_i=v c_i/(2\nu_0)\) on the bulk and, with the current \(v_i,\zeta\) held fixed, set the new \(\nu_i\) to the least \(s\ge0\) such that
\[
 |v_i+\zeta s|\le as,\qquad s^2+(v_i+\zeta s)^2\ge1 .
\]
The first inequality defines a half-line. On it the second left side is strictly increasing for \(s>0\), since its derivative is at least \(2s(1-a|\zeta|)\). This update is continuous, gives \(q_i\ge1\), and the first constraint is tight whenever the second is strict. The new real bulk weights lie in \([1/(1+a^2),\,\max(1,3v^2/(4u(a-z_*)^2))]\). For the mark use the positive root of
\[
 (1+\zeta^2)(w'_0)^2-(u-v\zeta c_0)w'_0-v^2(1-c_0^2)/4=0.
\]
It is in \([u/3,2u]\), since \(u-v\zeta c_0\in[u-|v|,u+|v|]\), \(1\le1+\zeta^2<2\), and \(\rho\le1/100\). At a fixed point this is the real part of the desired marked product and \(2w_0P_0=v\) is the imaginary part. At the mark the tangent bound is \(|P_0|+|D_0|\le z_*+3\rho<a\). Brouwer gives the pair on this box, including in the even subspace.

Conversely, for any genuine rotated clipped pair in the closed marked cone, real positive parts give the real stationary pair after inverse real scaling. The imaginary mean relations and the weighted sector equations give the same formulas for \(\omega,\zeta,D\). At the mark \(u=w_0(1-P_0^2+D_0^2)\) and the two tangent bounds first give \(w_0\ge u/(1+a^2)>u/2\). Now \(|P_0|\le\rho\) gives \(w_0\le u/(1-\rho^2)<2u\). The formulas above then put this pair in the same compact positive-weight bounds with strict marked angles.

## Rigidity for the rotated factors

Let \(U=A'-B'\), \(S=A'+B'\), and let \(P_1\) denote the orthogonal projection onto constants. The mean relation is exact:
\[
                   U=(K-i\tan b\,P_1)S.
\]
On the real and imaginary row coordinates use the squared norm \(a^2|\Re z|^2+|\Im z|^2\). The nonconstant component of \(K-i\tan b P_1\) is an isometry, and its constant multiplier has operator norm \(|\tan b|/a<1\) in this metric. The [round-90 scalar cap](clipped-signs-90.md) is nonexpansive in this same norm. The marked secant is strict since both rotated relative phases are below \(\theta\). Comparing any two roots therefore fixes the mean of \(S\) and the mark of \(U\). With equal means their differences use only \(K\), and the same signed eigenrow and quadratic pairing argument of round 90 makes both total corrections \(E_\pm=\sum_\pm e_i\) canonical. Here \(\pm\) denotes the cap sign in the rotated factors.

The true pairs on compact parameter subsets of the stated existence range have compact graphs in the positive real-part chart by the weight bounds. For fixed \(p\), the factors are bounded in real part by their real-part sums and below on each charged coordinate by the product divided by the opposite upper bound. Signs and weights vary continuously, with no signed price at an uncharged tie. Thus \(E_\pm\) are continuous. The cap equations are semialgebraic in \(a,\tan b\) and the original factor coordinates: rotate by \(1-i\tan b\) at \(A\) and by its conjugate at \(B\) before comparing real and imaginary parts. Piecewise differentiable selections follow as in [round 92](cap-sweep-92.md). A change at fixed \(\theta\) or at fixed \(b\) has finitely many such pieces on compact intervals. In two parameters the selections are differentiable on a finite union of open cells with complement of smaller dimension.

## The angular work inequality

At a differentiable genuine clipped pair freeze the rotation at the base value \(b\) when taking the factor derivatives. Their product variation \(dq\) is real on the bulk and zero at the mark. Off the positively corrected set \(dq_i=0\), by \(q_i\ge1\). There the local complex activation differential of \(S\) in \(U\) is nonexpansive in the anisotropic norm. This includes uncharged ties and the mark. On an active site write
\[
 A'_i=\sqrt{q_i}\,e^{g_i+i(\phi_i-b)},\qquad
 B'_i=\sqrt{q_i}\,e^{-g_i-i(\phi_i-b)},\qquad
 \phi_i-b=\sigma_i\theta,\quad \sigma_i\in\{1,-1\}.
\]
For the derivative with the base rotation fixed put \(F=d\phi_i\) and \(V=dq_i/(2q_i)\). Direct multiplication gives
\[
 \begin{split}
 a^2\Re(dA'_i)\Re(dB'_i)+\Im(dA'_i)\Im(dB'_i)
  &=
 q_i\left[a^2(cV-sF)^2-(sV+cF)^2
           -(a^2c^2-s^2)(dg_i)^2\right]\\
  &= -q_i(1-a^2)F^2-\sigma_i a\,dq_i F ,
 \end{split}
\]
where \(c=\cos\theta\) and \(s=\sigma_i\sin\theta\). The loss \(\|dU\|_a^2-\|dS\|_a^2\) is minus four times the sum of these cross pairings. With the base rotation held fixed, complementary tangents satisfy \(dU=(K-i\tan b\,P_1)dS\), even when their unrotated cap center is changing. Therefore the summed loss is nonpositive. Putting \(U_* = b+\theta,\ L_* = b-\theta\), \(N_\pm\) equal to their positively corrected counts, and \(\kappa=(1-a^2)/a\), we obtain
\[
 \boxed{\quad
 -dU_*\,dE_+ +dL_*\,dE_-
 \ \ge\ \kappa\left[(N_++E_+)(dU_*)^2+
                    (N_-+E_-)(dL_*)^2\right].\quad}                  \tag{1}
\]
The derivatives of active angles are exactly \(dU_*\) or \(dL_*\). The inequality also holds when opposite uncharged sites are tied, since their product derivative is zero.

Write \(E=E_++E_-\), \(I=E_+-E_-\). In particular, at fixed \(b\) or fixed \(\theta\) respectively,
\[
             -\partial_\theta E\ \ge\ \kappa(N_++N_-+E),
 \qquad      -\partial_b I\ \ge\ \kappa(N_++N_-+E).                    \tag{2}
\]
The first inequality sharpens the centered sweep in counting normalization: \(-\partial_a E\ge(1-a^2)/(a(1+a^2))(N_++N_-+E)\), with the previous one-sign coefficient now valid for arbitrary signs. At center zero the proof only needs the strict marked relative angle from round 92, so the improved coefficient holds on the full centered range there, including outside the small-ratio existence construction above. Holding one boundary fixed and opening the other decreases the correction on the moving side by (1).

There is an exact cross relation wherever two derivatives exist from one chosen smooth family. For tangent directions \(V,W\) write \(X_V=d_V\log A\), \(Y_V=d_V\log B\), with \(X_V+Y_V=d_Vq/q\), using the fixed marked product in that equation. Complementary pairing gives \(\sum q X_VY_W=n\,d_VM\,d_WM\). Interchange \(V,W\) and take imaginary parts after using the product equations:
\[
       \sum_i d_W q_i\,d_V\phi_i=\sum_i d_V q_i\,d_W\phi_i .
\]
Use \(V=\partial_b,\ W=\partial_\theta\) and the active constraints to obtain
\(\partial_\theta E=\partial_b I\). Equivalently \(\partial_{L_*}E_+=\partial_{U_*}E_-\) in boundary coordinates. This leaves the off-diagonal work terms skew. No estimate of their absolute signs is required for (1).

## Consequences for the actual cold floor

Each one-parameter inequality integrates across the finite differentiability partition by continuity. If the correction stays positive while moving the center by length \(h\) in the direction of the initial imbalance \(I(0)\), the imbalance must either reach zero, or the integral of \(N_++N_-+E\) over that motion is at most \(|I(0)|/\kappa\). While the imbalance keeps its initial sign, \(-d|I|/dh\ge\kappa(1+|I|)\) because \(E\ge|I|\) and at least one site is active. Thus a shift of length at least \(\log(1+|I(0)|)/\kappa\), when admissible, reaches either a zero-correction row or an exactly balanced positive pair of signed corrections. This bound uses the unaveraged imbalance. A sparse actual set at unbounded orders can evade it over every available shift.

If two admissible centers admit zero-correction pairs, they give the same unrotated pair. Their mean is fixed by the same total product. The [Hermitian phase secant](astra-phase-86.md#separate-signed-sources-on-the-two-true-extreme-sets) has, on the two pairs, summed phases in a common interval of width \(4\theta<\pi\), including the mark. Rotation by the sum of the two centers makes every coefficient strictly coercive. Thus the zero set in center space, when nonempty, is precisely the admissible part of the closed interval of centers whose bounds contain every bulk phase of this pair and whose marked cones contain both marked angles. In particular shifting the caps tests the actual phase spread before requesting an absolute phase bound about zero.

At the genuine prime-173 small-floor ray considered in round 92, the checker below verifies the local angular inequalities by an outward solution and differentiates both the center and the half width at the symmetric cap. The two slopes lie in \((-15.424,-15.423)\). The correction is approximately \(0.097804\) at \(b=-1/250\), approximately \(0.035786\) at \(b=0\), and zero at \(b=1/250\). The local differential proof requires only the valid pair, strict marked relative phase and \(|\tan b|<a\), conditions checked separately at these finite parameters. Both rotated absolute marked angles also satisfy the cap in the checker. The global existence argument used above has a smaller imaginary-to-real ratio. [Checker](rotated-cap-93-check.py) · [Outward records](rotated-cap-93-checks.jsonl)

1. At the nominated floor apply the center sweep to the actual two signed cap sets. A count or weighted-price lower over a center interval would either give a cap-free row or force a balanced positive pair where the signed return tests can be applied.
2. Seek a common through-primes estimate on the actual phase spread using the rotated interval, or use the exact center-width relation to control the loss on one of the two interacting extremes. The standing total correction bounds remain averaged.
