# A complementary interpolant for the actual cofactor row exchange

Use the actual optimizer \(F=q e_0+E_Sx\), its true bulk zero set \(U\), and the sector \(J\) of [Round 162](ordinary-zero-set-leakage-162.md). Let \(\Gamma=\Omega_\epsilon\setminus\{1\}\). Counting norms are used. In the real full-coordinate face, the ordinary optima have their true values by reflection averaging, as in [Round 137](ordinary-bulk-spectrum-137.md).

## Joint choice of independent columns and a nonnegative complementary row

Let \(R\) be a complementary optimum minimizing the number of positive bulk coordinates among the real complementary optima. Its physical mark is \(r=n/q\), it satisfies \(JR=\mathbf1\), and its bulk support is in \(U\) by complementarity. The columns \(JE_i\) at its positive bulk coordinates are independent. Otherwise there is a nonzero real vector \(h\) on that support with \(Jh=0\). Since \(J\mathbf1=\mathbf1\), its coordinate sum is zero and it has both signs. Move along this direction until a first positive coordinate vanishes. The mark, mean, sector equation and nonnegativity persist, contradicting minimal support. The chosen representative may be noneven on the full real face.

Extend those independent columns to the actual independent set \(U'\) spanning \(JE_U\). With \(L=M_{\Gamma,U'}\) and \(w=R|_{U'}\ge0\), the exact opposite-sector identity gives
\[
 Lw=-\frac r{\sqrt n}\mathbf1_\Gamma,\qquad
 \mathbf1_{U'}^*w=n-r.
\]
This identifies the nonconstant-row interpolation space \(\mathcal E=\operatorname{Ran}L\) as containing \(\mathbf1_\Gamma\) through an actual nonnegative coefficient vector up to the common negative scalar. These are restrictions from true complementary optimization. The determinant ratio is unchanged by this choice of independent basis. In fact the identity \(\mathbf1_\Gamma\in\mathcal E\) holds for any independent basis of the columns, with possibly signed coefficients.

## The constant part of the exchange weight is bounded

Let \(G=L^*L\), which is positive definite on the actual independent set when \(k=|U'|>0\), and \(\mathsf N=\det G\). For each cofactor of [Round 163](ordinary-fourier-minor-orbit-isolation-163.md), write \(g_I|_\Gamma=L v_I\). Its covariance on \(\Gamma\) is exactly
\[
 \sum_I (L v_I)(L v_I)^*=\mathsf N P_{\mathcal E}.
\]
Put \(\varphi=(MF)/\sqrt n\). Then \(\varphi(1)=1\), \(\varphi\) is supported on \(\Omega_\epsilon\), and \(\sum_{a\in\Gamma}\varphi(a)=q-1\), by inversion at the physical mark. Since each \(v_I\) lives on true zero columns, orthogonality to \(F\) gives \(g_I(1)=-\langle\varphi_\Gamma,Lv_I\rangle\), with the inner product linear in its second argument. Thus the aggregate marked cofactor weight satisfies
\[
 \frac{\mathsf B}{\mathsf N}
   =\|P_{\mathcal E}\varphi_\Gamma\|_2^2
   =\frac{(q-1)^2}{|\Gamma|}
      +\left\|P_{\mathcal E\cap\mathbf1_\Gamma^\perp}
              \left(\varphi_\Gamma-\frac{q-1}{|\Gamma|}\mathbf1_\Gamma\right)
       \right\|_2^2
\]
for \(|\Gamma|>0\). This uses the exact complementary interpolant. The first term is \(O(1)\) since \(q\ll\sqrt n\) and \(|\Gamma|\asymp n\) for large primes. Thus along a hypothetical fixed gap the order-\(T\) obstruction resides in the centered projection on the genuine independent columns. If one can bound this centered term by \(o(T)\) at an admissible growing time on every fixed-gap sequence, the original fixed-gap criterion follows.

The centered part still involves the actual Fourier profile of the true optimum. The exact identity does not supply its needed upper; summing the signed cofactor estimate by the adjugate without an extra inequality only returns the old exchange mass. The representation with nonnegative complementary coefficients may provide additional arithmetic constraints on the centered direction.

In fact \(\varphi_\Gamma\) belongs to \(\mathcal E\). The true distance representer in Round 162 is \((n/\|F\|_2^2)F\), so it is \(\mathbf1-JE_U z\) for some \(z\), and its Fourier restriction to \(\Gamma\) is in \(\operatorname{Ran}M_{\Gamma,U'}\). Thus the centered term is exactly \(\|F\|_2^2/n-1-(q-1)^2/|\Gamma|\). It is equivalent to the prior energy obstruction up to bounded terms. Any improvement must use an extra estimate from the true nonnegative interpolation coefficients or an arithmetic directional Gram bound.
