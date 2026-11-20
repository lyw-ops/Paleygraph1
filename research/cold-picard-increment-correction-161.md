# Exact transport of the true cold Picard increment

Use the genuine heights \(600,601,602\) on the original complex square, with the physical mark \(t_0=n\) and each lift separately. Let \(V_h\) be the true orbit, \(D_h=\operatorname{diag}\Phi_t'(V_h)\), \(A_h=I-KD_h\), and \(Z_h=A_h^{-1}K\) wherever the indicated inverse exists. Write \(\delta_h=V_{h+1}-V_h\). Set
\[
 U=\Phi_t(V_{601})-\Phi_t(V_{600}),\qquad U=D_{600}\delta_{600}+r.
\]
On any coordinate disks containing the segments on the chosen sheets with curvature bound \(C_{\rm curv}\), Taylor's formula gives \(|r_i|\le(C_{\rm curv}/2)|\delta_{600,i}|^2\). The exact orbit equations give \(J_{602}-J_{601}=\delta_{601}=KU\).

The correct resolvent difference and neighboring \(K\) cancellation are
\[
 Z_{602}-Z_{601}=Z_{602}(D_{602}-D_{601})Z_{601},
 \qquad
 Z_h K = (I+Z_hD_h)(I-\Pi).
\]
The first comes from \(A_{601}-A_{602}=K(D_{602}-D_{601})\). The second uses \(A_h^{-1}=I+Z_hD_h\) and \(K^2=I-\Pi\). These are identities of the actual operators. They put the adjacent \(K\)'s together without moving \(K\) through a multiplier. In particular
\[
 Z_h\delta_{601}=U-\overline U+Z_hD_h(U-\overline U)
\]
with \(\overline U\) the constant vector with value \(\mathbb E U\).

## The coordinatewise quadratic term cannot be charged as a smoothed one

The Taylor error is \(Kr\) before the outer transport and
\[
 Z_hKr=(r-\overline r)+Z_hD_h(r-\overline r)
\]
after it. With \(r_* =\|\delta_{600}\|_{2,n}\), \(M_Z=\max_{i,j}|(Z_h)_{ij}|\) and \(M_D=\|D_h\|_\infty\), the scalar bound gives
\[
 \|(Z_hKr)-r\|_\infty
 \le \frac{C_{\rm curv}}2(1+2nM_Z M_D)r_*^2 .
\]
Indeed \(|\overline r|\le\|r\|_{1,n}\le(C_{\rm curv}/2)r_*^2\) and the centered input costs at most twice that in normalized first norm. The separate term \(r\) retains its quadratic coordinate cost \((C_{\rm curv}/2)\|\delta_{600}\|_\infty^2\). In particular the coordinatewise bound is not implied by treating \(K\) as a first-norm contraction. At height 601 the available max-entry bound is \(O(n^{-0.467})\) from [Round 130](cold-combined-height-130.md). Applying that scale at height 602 requires a justified transfer or separate bound. The estimate just displayed is in coordinate supremum and does not itself bound the translated \(P_{5000}\) norm.

This correction separates the direct Taylor term, the signed remainder smoothed by the true frozen resolvent, and the height insertion with its actual multiplier. It leaves open the required uniform estimates for both lifts and a quantitative nonlinear transfer on the whole square. The previous \(0.66348896\) translated bound and \(0.51961239\) budget of [Round 159](cold-actual-H-scalar-units-159.md) are the relevant figures.
