# Positive quadratic completion and descent on the full terminal face

Use the genuine larger-side probability face \(\mathcal Q_a\) with root \(a\), and put \(M=1-a,\ \gamma=\sqrt n a\). Fix any opposite optimizer \(r^*\) at zero. Write \(S=\{i\ne0:r_i^*=0\}\) and \(b(U)=\overline U-aU_0\). Every law in the maximizing primary face has exterior support in \(S\). A nonnegative exterior row \(y\) supported there completes to such a law exactly when
\[
                 \sum_S y_i U_i=b(U)\qquad(U\in V_{-\sigma}),
\]
where \(V_{-\sigma}\) is the real opposite sector with its constants. The constant equation takes care of the total mass. These facts follow from complementary optimality \(nar_0^*=1\) and the disjoint nonconstant Fourier sectors. Additional forced zeros can be left in \(S\).

## A one-sided root trace and the cost of real terminal heights

Fix the actual window and notation of [round 83](astra-split-83.md). In its common-head alternative freeze the same \(T\). One may also take \(T=\varnothing\) to test height alone. Choose any good time \(b\) in the same prefix, with its own length \(d\), deficit mask \(P\), primary pin \(R\) in the opposite sector and terminal companion \(Z\) in the tested sector. Put \(h=Z1_P\) and \(g=1_T+h/d\). Use the stated capacities \(c_i=Ae_i/n\) off \(P\), and their minimum with \(d/[n(1+h_i)]\) on \(P\). Thus \(c_i>0\). Write \(C=\{i\in S:g_i>0\}\). The weighted second norm has the following prime-uniform bound.
\[
  \sum_C c_i g_i^2\le 2c(T)+\frac2d\frac1n\sum_P h_i
               =O_\delta(d^{-1}).                                      \tag{1}
\]
Indeed \(c(T)\) is exponentially small on the frozen common head by the actual energy estimate of round 83. On \(P\), use \(h_i^2/(1+h_i)\le h_i\). The normalized bulk first norm of the actual \(Z\) is bounded by its three adjacent absolute-value rows and the bounded constant in the [exact bulk expansion](relative-window-77.md). Each of the three neighboring \(g_j\)'s is at most four and bounds half the bulk first norm of its corresponding \(Y_j\). All the times use the true root and the same frozen head.

For real opposite \(U\) such that \(U_i\le0\) on \(S\setminus C\), define
\[
 \Xi=\sup_U
 \frac{\big[b(U)-\sum_C c_i(U_i)_+\big]_+}
      {\big(\sum_C c_i(U_i)_+^2\big)^{1/2}}.
                                                                    \tag{2}
\]
A zero denominator contributes zero. Such a field has nonpositive \(b(U)\) by any genuine completion. Then
\[
 \Xi^2=\min_{q\in\mathcal Q_a}\sum_C\frac{(q_i-c_i)_+^2}{c_i},\qquad
 \Delta_g(c)\le \big(\sum_C c_i g_i^2\big)^{1/2}\Xi
                    \ll_\delta \Xi/\sqrt d .                      \tag{3}
\]
In particular one genuine minimizing row pays both the head and the height within this upper bound. The squared-excess minimum enforces positivity directly.

For any genuine \(q\), the numerator before taking its positive part is at most \(\sum_C(q_i-c_i)_+(U_i)_+\); this proves one direction by Cauchy–Schwarz. For the other take a minimizer on the compact face, set \(z_i=(q_i-c_i)_+/c_i\) on \(C\) and zero on \(S\setminus C\). First variation of the squared objective shows that \(q\) minimizes the linear \(z\)-cost on the same face. The finite dual of its displayed moment equations has an attaining \(U_i\le z_i\) on \(S\) with equality wherever \(q_i>0\). Consequently \((U_i)_+=z_i\) on \(C\), \(U_i\le0\) on \(S\setminus C\), and the numerator in (2) is precisely \(\sum_C c_i z_i^2\). The second part of (3) is Cauchy–Schwarz on this attaining primal row. If a global potential is desired, subtract a sufficiently large multiple of \(r^*\) to make \(U\) nonpositive also on the rest of the exterior and at the root. This preserves its restriction to \(S\) and \(b(U)\). For any \(\kappa\ge\max(0,\max_S U_i)\), \(\kappa-U\) is then a globally nonnegative opposite field.

There is an explicit direction that tests the necessary scale in (2). Suppose \(\gamma\ge1+\delta\). Write \(u=\epsilon=\delta/8\), \(\theta=1/(2d-1)\) and \(m=R_0/\sqrt n\), so \(\overline R=(1+\epsilon)m\). Take
\[
 U^{\rm ht}=(-R-u)/(d\theta).
\]
Off \(P\) its exterior entries are nonpositive. On \(P\), the [pointwise terminal pairing](terminal-height-79.md) gives \(U^{\rm ht}\le h/d\). Its exact root residual is \(b(U^{\rm ht})=[m(\gamma-1-\epsilon)-uM]/(d\theta)\). In particular the mismatch on every optimizer is at least
\[
 L_b=\frac{m(\gamma-1-\epsilon)-uM}{d\theta}
                    - \frac{|P|}{n}
        +\big(\inf_{q'\in\mathcal Q_a}q'(T)-c(T)\big)_+ .            \tag{4}
\]
For the first two terms use \(\sum c_i h_i/d\le |P|/n\). The head has its own additive hinge payment even when it intersects \(P\). This also gives \(\Xi\gg_\delta\sqrt d\) via this particular opposite field in (2), since \(|P|/n=O_\delta(1/d)\) and its squared denominator is \(O(1/d)\) by (1). In the common-head case the primal side of (3) implies the stronger \(\Xi\ge[\inf q'(T)-c(T)]_+/\sqrt{c(T)}\) by Cauchy–Schwarz on \(T\cap S\). Thus the joint trace can have a much more demanding head direction under the hypothesized gap. No prime-uniform \(o(\sqrt d)\) bound on (2) is established.

## Signed root prices on the support of the actual complementary law

Let \(J_* = \{i\ne0:r_i^*>0\}\) and normalize any direction in (2) by \(H=U-(U_0/r_0^*)r^*\). Thus \(H_0=0\), \(H|_S=U|_S\) and \(b(U)=\overline H\). Write \(N(U)=(\sum_C c_i(U_i)_+^2)^{1/2}\). For the growing asymptotic capacities let \(A\ge2\). Uniformly for every such direction,
\[
\begin{split}
 0\le b(U)-\sum_C c_i(U_i)_+ -
 \left[\frac1n\sum_{J_*}H_i-\frac1n\sum_S(U_i)_-
                       -\sum_C(c_i-1/n)_+(U_i)_+\right]
 \ll d^{-1/2} N(U).                                             \tag{7}
\end{split}
\]
The difference is exactly \(\sum_C(1/n-c_i)_+(U_i)_+\). The capacity can fall below \(1/n\) only on \(P\), where it must then equal \(d/[n(1+h_i)]\). Consequently the squared dual norm of this difference is at most \((nd)^{-1}\sum_P(1+h_i)=O(1/d)\). The complementary sum equals \((1-r_0^*)/n\) times the average of \(U_i/r_i^*-U_0/r_0^*\) under the normalized exterior of \(r^*\). In particular every direction whose exterior average ratio lies below its root ratio contributes at most \(O(d^{-1/2})\) to (2).

There is a stronger restriction using the true primary projector \(P_\sigma=(I-J_{\rm const}+\sigma K)/2\). For every direction,
\[
 b(U)-\sum_C c_i(U_i)_+
 \le \frac1n\left[\sum_{i\in J_*}H_i-
      \sqrt n\,\max_{j\in J_*\cup\{0\}}
           |(P_\sigma(H1_{J_*}))_j|\right]
                  +O(d^{-1/2})N(U).                              \tag{8}
\]
Indeed for each such center \(j\), put \(t_i=\sqrt n(P_\sigma)_{ij}\). All sites of \(S\) are off diagonal, so \(|t_i|\le(1+\sqrt p)/(2\sqrt n)<1\) eventually. For either sign the normalized signed primary row \(w_i=(1\pm t_i)/n\) has \(0\le w_i\le2/n\) everywhere on \(S\). Orthogonality and \(H_0=0\) give \(b(U)=\sum_{J_*}w_iH_i+\sum_S w_i U_i\), regardless of the sign of the weight at the center. The excess over \(\sum_C c_i(U_i)_+\) on \(S\) is at most \(\sum_C(w_i-c_i)_+(U_i)_+\). Here \(c_i<2/n\) again implies the true height cap on \(P\), so \(\sum_C(w_i-c_i)_+^2/c_i\le4(nd)^{-1}\sum_P(1+h_i)\). Minimize the exterior sum over the two signs and over centers and use symmetry of the projector to obtain (8).

To force \(\Xi\gg_\delta\sqrt d\), the signed mean of a root-neutral direction on the **positive** support of the opposite optimizer must therefore exceed every displayed amplified Jacobi response there or at the root by \(\gg_\delta n\sqrt d\,N(U)\). To give a sufficient upper in (3) it is enough to show that the positive excess in these brackets is \(o(n\sqrt d)N(U)\) uniformly in \(U\) at one good time. Bounds (7) and (8) have different credits and can be used together. The projector test uses only one signed column at a time. The actual height and the true support enter its error through the same capacities as in (3).

## A sharp directional upper on the joint mismatch

The upper below takes a step from any specified genuine row, including a capacity-minimizing row with zeros, and permits coordinates to enter the support. It applies to any nonnegative demand and any strictly positive metric weights \(w_i\) on \(S\). The numerical check uses \(w_i=c_i\). Set \(F(q)=\sum_S g_i(q_i-c_i)_+\). Associate a slope \(f_i\) to each coordinate. Set it to zero for \(q_i<c_i\), to \(g_i\) for \(q_i>c_i\), and allow \(f_i\in[0,g_i]\) at equality. Minimize the following one-sided least-squares quantity over this box and real opposite fields \(H\):
\[
 \mathcal R=\min_{f,H}\left[
 \sum_{q_i>0} w_i(H_i-f_i)^2+
 \sum_{i\in S:q_i=0} w_i(H_i-f_i)_+^2\right].                       \tag{5}
\]
All sums in (5) are restricted to \(S\). Attainment follows by writing the sum as a weighted squared distance from a polyhedron. On the zero coordinates one may subtract an arbitrary nonpositive residual before squaring, and the relevant linear image of the slope box, opposite subspace and orthant is a closed polyhedron.

Use a minimizing pair and take \(v_i=w_i(H_i-f_i)\) where \(q_i>0\), \(v_i=w_i(H_i-f_i)_+\) where \(q_i=0\), and zero elsewhere, including the root. Differentiation in \(H\) proves \(\sum_i v_i U_i=0\) for all opposite \(U\). Minimization in the slope box makes \(f\) maximize \(\sum_i f_i v_i\) there. In the norm \(\|v\|_w^2=\sum v_i^2/w_i\), this gives
\[
       F'(q;v)=-\mathcal R,\qquad \|v\|_w^2=\mathcal R.
\]
In fact \(\sqrt{\mathcal R}\) is the largest decrease per unit norm in the full feasible tangent cone when directions of norm at most one are allowed. For any tangent \(z\), \(z_i\ge0\) at the zero sites and \(\sum H_i z_i=0\). Therefore \(F'(q;z)\ge\sum(f_i-H_i)z_i\ge-\sqrt{\mathcal R}\|z\|_w\). The direction just constructed attains the slope if \(\mathcal R>0\). If it vanishes, convexity certifies the global minimum. On the true metric \(w=c\), (1) gives \(\mathcal R\le O_\delta(1/d)\) by setting \(H=0\) in (5).

For \(v\ne0\) put \(t_+=\min_{v_i<0}q_i/(-v_i)\), which is finite since the constant equation gives \(\sum v_i=0\). For \(0\le t\le t_+\) the row \(q+tv\) is a genuine optimizer with the same root. The exact price on the line gives the upper
\[
 \Delta_g(c)\le F(q+tv)=F(q)-t\mathcal R+
 \sum_{(q_i-c_i)v_i<0}g_i\big(t|v_i|-|q_i-c_i|\big)_+ .                \tag{6}
\]
A hinge at an initial tie has the exact slope already used in \(F'(q;v)\). All further changes of slope are the indicated crossings. In particular with \(B=\sum_{(q_i-c_i)v_i<0}g_iv_i^2/|q_i-c_i|\) the improvement is at least \(\frac12\mathcal R\min(t_+,2\mathcal R/B)\), treating the second argument as infinite for \(B=0\). This uses \((x-y)_+\le x^2/(4y)\) for \(y>0\). Against a hypothetical gap this improvement, or the larger exact gain in (6), cannot exceed \(F(q)-L_b\). The quantities in (5)–(6) involve the observed row, the opposite restricted functions, capacities and actual terminal height.

If the good time is free one can use any probability \(\pi_b\) on good times with a common frozen head and the same input row. Apply (5) to the slope box of \(\sum_b\pi_bF_b\), the weighted sum of the individual boxes, with one fixed positive metric. Formula (6) then holds for the averaged cost with the crossing losses averaged over \(b\). At least one of those times costs no more than the averaged upper on the single constructed endpoint. The separate lower bounds (4) also average on that endpoint. Positivity prices and mask prices in this argument use the same actual coordinates.

## Finite directional obstruction from locking zeros

At prime 97, terminal time four, use the round-83 true energy envelope, frozen twenty-site head, marked terminal mask and finite pin conventions. For the reference scale \(1/5\) start from the exact least-energy-envelope-scale optimizer. Its joint mismatch is in \((0.595819142,0.595819143)\). In the physical metric \(w=c\), the first full-cone descent direction reopens coordinates 19 and 29 and reaches the boundary where 10 and 38 vanish. The second reaches the global joint optimum in \((0.507225779,0.507225780)\). Neither step crosses a positive-price hinge. If 19 and 29 are held at zero throughout, the best possible value on that restricted face is in \((0.521544066,0.521544067)\). The price of permanently keeping those zeros exceeds 0.014318286. At scale \(3/20\) the first step crosses charged coordinates 21 and 27, paying between 0.001232526 and 0.001232527 in the correction in (6).

The checker reconstructs the complementary cyclotomic faces, the true four-step pin and head. In the two even anchored coordinates a positive definite Gram matrix computes the least-squares descent. At the first step its unconstrained solution is strictly feasible at the zero pair. At the second, a strictly positive multiplier certifies the binding anchor. Both terminal slopes are strictly negative, so each endpoint minimizes the cost on its entire feasible segment. Reflection preserves all functions and the input row, and averaging a direction preserves feasibility and cannot increase its norm or directional cost, so the even result gives the full-cone slopes. For the locked minimum, on the even line with coordinate 19 fixed at zero, the other anchor starts at zero with strictly positive right derivative. Convexity and reflection give the claimed whole-face bound when both 19 and 29 are locked.

At scale \(1/5\) the attained quadratic trace squared in (2) is in \((0.703013692,0.703013693)\). The checker interpolates its opposite certificate and verifies strict negativity on both free pairs. The (3) upper is in \((0.665887511,0.665887512)\) on this finite profile. For the attaining opposite direction, the external mean in (7) lies in \((1.073401257,1.073401258)\). The maximizing column in (8) is the root and reduces it by more than 0.378130068. The checker retains the actual below-cap norm, less than 0.250409339, since this finite scale is below two. These finite times and cutoffs do not instantiate the asymptotic gap assumptions. [Arb384 checker](astra-capacity-84-check.py) · [Outward records](astra-capacity-84-checks.jsonl)

1. Bound the positive signed excess in (8) for one admissible time, keeping the root-neutral direction on the actual positive support of the opposite optimizer. Use the negative-mass and excess-capacity credits in (7) when the amplified Jacobi response is small. The physical pin specifies the scale a supercritical gap would force.
2. Measure the full-cone slope, first zero and charged crossings in (6) from one genuine comparison row, allowing initially zero coordinates to re-enter. A uniform gain greater than \(F(q)-L_b\) at one good time would preclude the fixed gap.
