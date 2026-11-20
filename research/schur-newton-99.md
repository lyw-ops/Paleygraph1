# Erasing actual Newton sources at a first comparison activation

At the true near-flat first activation on the nominated square, every block of at most \(\lfloor\sqrt n/2000\rfloor\) coordinates containing the hit can be eliminated together with its nonlinear Newton sources. The compensated surviving sites must still give an oriented imaginary response above \(3.41\cdot10^{-5}\). This holds eventually through eligible primes. The erased block can include the mark and the largest nonlinear sources.

## Exact nonlinear Schur identity

Use \(W,R,r,D,H,Z,U,\Delta,B\) from the [same-floor Newton comparison](newton-boundary-98.md#the-nonlinear-remainder-after-the-newton-step), at the actual first comparison activation with the original cutoff \(10^{-8}\). Write \(W_i=2\sqrt{t_i}\sinh g_i\) and \(U_i=2\sqrt{t_i}\sinh z_i\) on the physical phase lifts, with \(t_0=n\) and \(t_i=t\) on the bulk. The exact secant identity gives
\[
 E_i=\tanh((z_i+g_i)/2)-\tanh g_i,\qquad B_i=E_i\Delta_i.
\]
Use the common rotation for every site's row, including the mark:
\[
  h_*=H/\sqrt t,\qquad d=\Delta/\sqrt t,\qquad b=B/\sqrt t.
\]
Then \(d=h_*+Zb\) and \(b=Ed\), writing \(E=\operatorname{diag}(E_i)\). On any set \(S\) containing a hitting site \(i\), and \(O=S^c\), put
\[
 A=Z_{SS}E_S,\qquad M=(I-A)^{-1},\qquad
 \widetilde Z_{iO}=(M Z_{SO})_{iO}.
\]
Whenever \(M\) exists, the true rotated imaginary row satisfies
\[
 \operatorname{sgn}(\Im(U_i/\sqrt t))\,\Im(\widetilde Z_{iO} b_O)
 \ge
 \frac{2\cdot10^{-4}}{\sqrt3}-7.1\cdot10^{-5}
          -\left|\Im((M-I)h_{*,S})_i\right|.                         \tag{1}
\]
Indeed \(d_S=M(h_{*,S}+Z_{SO}b_O)\). At the hit \(\big|\Im(U_i/\sqrt t)\big|\ge 2\cdot10^{-4}/\sqrt3\), while the nominal row satisfies \(\big|\Im((W+H)_i/\sqrt t)\big|<7.1\cdot10^{-5}\) by the [nominal full-square contour](newton-boundary-98.md#control-the-newton-correction-on-the-full-square). This identity absorbs all sources inside \(S\), including the source at the hitting site.

## Erasure margins

On the whole nominated square, eventually through eligible primes, \(\max|Z_{ij}|\le178/\sqrt n\) and \(\|Z\|_{2\to2}<2.057\). In addition \(|E_i|\le1.514\), since the true exact secant has modulus less than one and \(|D_i|<0.514\). For \(|S|\le\sqrt n/c\) put \(\theta=178(1.514)/c\). The matrix \(A\) then has operator norms at most \(\theta\) in counting supremum and second norms, the latter by the row and column tests. If \(\theta<1\), its inverse satisfies \(\|M\|\le(1-\theta)^{-1}\) in both norms. Independently of any imaginary bound on \(Z\), \(\|h_*\|_\infty<0.019\), so (1) gains more than \(4.39\cdot10^{-5}\) for every \(S\) with \(|S|\le\lfloor\sqrt n/10^7\rfloor\).

For a larger erasure, retain the matrix imaginary part. On the bulk \(|\Im z_j|\le\arcsin(10^{-4}/\sqrt3)\) at the actual first comparison hit, and at the mark the phase is at most \(|\arg t|/2\) by the [exact marked phase identity](real-phase-projection-89.md#the-exact-column-and-the-real-weight-equations). For the nominal predictor, \(\|\partial_t W\|_\infty<21\) and the reality at \(T=\Re t\) give
\[
 |\sin\Im g_j|\le \tfrac12|\Im(W_j/\sqrt t)|
 \le \tfrac12|\Im t|\left(21/\sqrt L+4.768/(2L^{3/2})\right)
 \quad(j\ne0).
\]
At the mark the same inequality follows from \(|\Im W_0|\le21|\Im t|\) and the denominator \(2\sqrt n\). It follows that \(|\Im g_j|<2.03\cdot10^{-5}\) at every site. The elementary inequality \(|\Im\tanh(x+iy)|\le\tan|y|\) for \(|y|<\pi/4\) gives \(|\Im E_i|<6.1\cdot10^{-5}\). The [contour estimate for \(H\)](newton-boundary-98.md#control-the-newton-correction-on-the-full-square) and the real values at \(T\) give
\[
 \|\Im h_*\|_\infty
 \le |\Im t|\left(15.811/\sqrt L+0.075/(2L^{3/2})\right)
 <3.04\cdot10^{-5}.
\]
If \(\sqrt n\max_{i,j}|\Im Z_{ij}|\le \zeta\), then
\[
 \|\Im A\|_\infty\le (1.514\zeta+178(6.1\cdot10^{-5}))/c.
\]
The exact resolvent difference \(M-\overline M=M(A-\overline A)\overline M\) consequently gives
\[
 |\Im((M-I)h_{*,S})_i|
 \ \le\
       \frac{\theta}{1-\theta}\,3.04\cdot10^{-5}
       +\frac{1.514\zeta+178(6.1\cdot10^{-5})}{c(1-\theta)^2}\,0.019.   \tag{2}
\]
The [translated contour](astra-rotate-99.md) gives \(\zeta=0.283\) on the full square. With \(c=2000\), the right side of (2) is below \(1.031\cdot10^{-5}\), so (1) is greater than \(3.41\cdot10^{-5}\) for every such erasure.

## Compare with the original row on the survivors

For every such block, the exact compensated row obeys
\[
 \|\widetilde Z_{iO}\|_\infty\le \frac{178}{(1-\theta)\sqrt n},\qquad
 \|\widetilde Z_{iO}-Z_{iO}\|_2\le
 \frac{178(1.514)(2.057)\sqrt{|S|}}{(1-\theta)\sqrt n}.              \tag{3}
\]
The first follows by taking the row sum of \(M\). For the second, write \(M-I=A M\); the counting second norm of row \(A_{iS}\) is at most \(178(1.514)\sqrt{|S|}/\sqrt n\), and \(\|Z_{SO}\|_{2\to2}\le\|Z\|_{2\to2}\). Also
\[
 \|\widetilde Z_{iO}-Z_{iO}\|_\infty
      \le \frac{\theta}{1-\theta}\frac{178}{\sqrt n}.                \tag{4}
\]
The first inequality in (3) makes the surviving counting first mass of \(b_O\) greater than \(1.65\cdot10^{-7}\sqrt n\). More precisely write \(L_A=(1.514\zeta+178(6.1\cdot10^{-5}))/[c(1-\theta)^2]\). The imaginary entries of the change in the exterior row satisfy
\[
\sqrt n\max_j|\Im(\widetilde Z_{ij}-Z_{ij})|
     \le\zeta\,\frac{\theta}{1-\theta}+178L_A<0.097 .
\]
This is obtained by expanding \((M-I)Z_{SO}\) into its real and imaginary parts, with \(\|\Im M\|_\infty\le L_A\). Meanwhile the real entry change is bounded by (4), less than \(27.72/\sqrt n\). This gives a test directly on the original row:
\[
 \operatorname{sgn}(\Im(U_i/\sqrt t))\,\Im(Z_{iO} b_O)
  +\frac{27.72\|\Im b_O\|_1+0.097\|\Re b_O\|_1}{\sqrt n}
    >3.41\cdot10^{-5}.                                               \tag{5}
\]
With the matrix imaginary entry bound \(0.283/\sqrt n\) on the original row, we also have the necessary anisotropic counting inequality
\[
          206\|\Im b_O\|_1+0.380\|\Re b_O\|_1
                         >3.41\cdot10^{-5}\sqrt n .                   \tag{6}
\]
Every term remains in the common rotated \(b=B/\sqrt t\) units. A deletion can target the largest contributions to (6) or the largest oriented terms of the ordinary row in (5). If \(S\) includes the \(k\) largest sources by modulus, possibly in addition to the hitting site and mark, then \(\|b_O\|_2\le\|b\|_1/(2\sqrt k)\): writing \(v=\|b_O\|_\infty\), the sum of squares on \(O\) is at most \(v(\|b\|_1-kv)\). If \(S\) instead includes the \(k\) largest anisotropic weights \(a_j=206|\Im b_j|+0.380|\Re b_j|\) in (6), the same calculation gives \(\|a_O\|_2\le\|a\|_1/(2\sqrt k)\).

The [rotated quadratic bounds](astra-rotate-99.md) give \(\|b\|_{1,n}\le0.04919 r^2\) and \(\|\Im b\|_{1,n}\le0.000055 r^2+0.09834 r r_I\), where \(r_I=\|\Im R\|_{2,n}\) and \(R\) is still in the original physical units. They also bound \(r\le\bar r=0.169724(0.51358)^{100}\) and \(r_I\le0.00624\bar r\). Inserting these in (5), whenever \(n^{1/4}\bar r\le0.025\), the ordinary oriented exterior alone is greater than \(1.94\cdot10^{-5}\) after every allowed deletion. In the same regime the real mixed sum satisfies
\[
 2\,\operatorname{sgn}(\Im(U_i/\sqrt t))
   \sum_{j\in O}(\Re Z_{ij})\,w_j\ell_j(\Re\Delta_j)(\Im\Delta_j)
     >10^{-5}.
\]
Here \(w_j,\ell_j\) are as in the [exact quadratic square](astra-rotate-99.md#exact-physical-square-and-its-phase). The absolute error in its replacement (3) also bounds this restricted sum, since the absolute error estimate sums a nonnegative majorant over the sources. This costs at most \(0.015\sqrt n r^2\le0.015(0.025)^2\). The mixed test survives erasing its own largest paying terms. [Arb arithmetic checker](schur-newton-99-check.py) · [Replay](schur-newton-99-checks.jsonl)

1. Test the oriented original row after a data-dependent deletion using (5). Both the real and imaginary mass of the surviving physical remainder appear with explicit coefficients.
2. Estimate the smallest anisotropic counting mass in (6) after deleting its largest contributors. A prime-uniform upper of \(3.41\cdot10^{-5}\sqrt n\) for one legal erasure at every candidate hit suffices. The current fixed-depth normalized quadratic source estimate still allows (6) at unbounded sizes.
