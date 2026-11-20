# The rotated Newton square at a physical comparison hit

At the first bulk activation of the selected near-flat comparison, let \(R=K\Phi_t(W)-W\) be the physical height-100 residual. Write \(r=\|R\|_{2,n}\), \(r_I=\|\Im R\|_{2,n}\), with averaging over all individual sites. On the whole nominated square, for every sufficiently large eligible prime, a hit forces
\[
   \sqrt n\,r^2>5.07\cdot10^{-6},\qquad
   \sqrt n\,(0.024 r^2+17.51 r r_I)>4.4470\cdot10^{-5}.                  \tag{1}
\]
The imaginary part of *every* translated predictor resolvent entry has absolute value below \(0.283/\sqrt n\). This leaves a real signed correlation between the two components of the lag as the main unknown in the original rotated test. At the fixed height \(\bar r=0.169724(0.51358)^{100}\), \(r_I<0.00624\bar r\) and a hit forces \(\sqrt n\bar r^2>0.000333\). These necessary conditions retain a size factor at unbounded order.

## Exact physical square and its phase

Take \(a=2031/128, h=2^{-17}, L=a-h\), \(|\Re t-a|,|\Im t|\le h\), and \(n=(p-1)/2\). At the [first activation](same-floor-97.md#the-actual-first-boundary-lag-is-residual-scale) with cutoff \(\max_{j\ne0}X_j^2=10^{-8}\), the reconstructed row has unit bulk products. Put \(t_j=t\) off the mark and \(t_0=n\). In original physical units let \(U_j=2\sqrt{t_j}\sinh z_j\) denote its true stationary coordinate, \(W_j=2\sqrt{t_j}\sinh g_j\) for the predictor, and \(\Delta=U-W\). With \(s_j=(z_j+g_j)/2\), the secant is \(S_j=\tanh s_j\) and \(\ell_j=1-|S_j|^2=\cos(\Im z_j+\Im g_j)/|\cosh s_j|^2>0\). These formulas extend to coinciding coordinates. The [Newton residual](newton-boundary-98.md) is \(B_j=\Phi_t(U)_j-\Phi_t(W)_j-(\tanh g_j)\Delta_j\). Hyperbolic addition gives the exact identities
\[
 B_j=4\sqrt{t_j}\,\operatorname{sech}g_j\,\sinh^2((z_j-g_j)/2),\qquad
 B_j/\sqrt t=w_j\ell_j e^{i\kappa_j}\Delta_j^2 ,
\]
where
\[
 w_j=(4\sqrt{|t_j||t|}\,|\cosh g_j|\cos(\Im z_j+\Im g_j))^{-1},\quad
 \kappa_j=-\tfrac12\arg(t_jt)-\arg\cosh g_j-2\arg\cosh s_j .
\]
Indeed \(\Delta_j=4\sqrt{t_j}\cosh s_j\sinh((z_j-g_j)/2)\). The bulk first-hit phases obey \(|\sin\Im z_j|\le10^{-4}/\sqrt3\); the two marked factors' phases have the same weak sign, so \(|\Im z_0|\le |\arg t|/2\). From \(\|\partial_t W\|_\infty<21,\ \|W\|_\infty<4.768\), integrate vertically from the real floor to bound \(|\sin\Im g_j|\le |\Im(W_j/(2\sqrt{t_j}))|\). This gives \(|\Im g_j|<2.1\cdot10^{-5}\) also at the mark, where the denominator is constant. Consequently \(|\Im z_j+\Im g_j|<8\cdot10^{-5}=:\tau\), and \(|\kappa_j|<0.000106\), since \(|\arg\cosh(x+iy)|\le|y|\) in this strip. Below use \(w_j\le w_*=[4L\cos(2.1\cdot10^{-5})\cos\tau]^{-1}\).

## A sharper energy inequality and its imaginary component

Let \(E=\mathbb E\ell|\Delta|^2\), with counting mean \(\mathbb E\). Write \(c=\cos\tau, G=\sqrt{1+0.6^2}, A=G/\sqrt c, C=(G+0.6)/(4\sqrt L\,c)\). The predictor has \(|\sinh g_j|<0.6\) and \(|\cosh g_j|\le G\). With \(u=(z_j-g_j)/2\), \(|\cosh s_j|\le G+(G+0.6)|\sinh u|\) by the addition formula and \(|\cosh u|\le1+|\sinh u|\). Substitution of \(|\sinh u|=\sqrt{\ell_j}|\Delta_j|/(4\sqrt{|t_j|\cos(\Im z_j+\Im g_j)})\) gives the pointwise inequality
\[
                         1\le A\sqrt{\ell_j}+C\ell_j|\Delta_j| .
\]
Since \(\Delta-R=K(S\Delta)\) and \(K\) contracts the second norm, \(E\le2\Re\mathbb E\overline R\Delta-r^2\). Cauchy–Schwarz applied to the preceding pointwise bound yields
\[
 f E\le 2A r\sqrt E-r^2,\qquad f=1-2C(0.001180)>0 .
\]
Here \(\|R\|_\infty<0.001180\) is the height-100 packet bound. Therefore \(\sqrt E\le Mr\) with \(M=(A+\sqrt{A^2-f})/f\), \(M^2<3.122\). In particular the original physical source satisfies \(\|B\|_{1,n}\le M^2r^2/(4\sqrt L\cos(2.1\cdot10^{-5})c)<0.197r^2\) when \(r>0\), and vanishes when \(r=0\).

Write \(\Delta=u+iv, S=d+ie\) with real components (here \(u\) denotes the physical real lag). The exact sector identity \(e/\ell=\tfrac12\tan(\Im z+\Im g)\) bounds \(|e|\le\sigma\ell\), \(\sigma=\tfrac12\tan\tau\). Let \(x^2=\mathbb E\ell v^2\). Using the real operator \(K\) in \(v-\Im R=K(dv+eu)\), expanding the squares and \(1-d^2\ge\ell\) gives
\[
 x^2\le 2\sigma x\sqrt E+\sigma^2 E+2\mathbb E(v\Im R)-r_I^2 .
\]
Multiply the pointwise inequality by \(|v\Im R|\); its terms sum to at most \(A r_I x+C\|R\|_\infty x\sqrt E\). Set \(k=\sigma+C(0.001180), b=\sqrt{A^2-1}\), and \(k_2=k+\max(Ak/b,\sqrt{k^2+\sigma^2})\). Solving the quadratic and bounding its discriminant by the square of \(b r_I+(k_2-k)\sqrt E\) gives
\[
                          x\le (A+b)r_I+k_2\sqrt E .                  \tag{2}
\]

For the rotated and rescaled source \(b^{\rm rot}=B/\sqrt t\) the same square gives
\[
  \|b^{\rm rot}\|_{1,n}\le0.04919r^2,\qquad
  \|\Im b^{\rm rot}\|_{1,n}\le0.000055r^2+0.09834r r_I .
\]
The latter uses \(w_*[\max|\kappa| E+2x\sqrt E]\) and (2), with all sites included.

## Imaginary entries of the physical translated resolvent

Let \(Z=(I-K\operatorname{diag}(\tanh g))^{-1}K\). At the predictor, all entries are holomorphic on a neighborhood of the square of half-width \(0.006\), by the established [larger-square physical cap](newton-boundary-98.md#control-the-newton-correction-on-the-full-square) and the second-norm Neumann series. Divide each edge of the smaller contour (half-width \(0.006\)) into eight equal segments. The [checker](astra-rotate-99-check.py) repeats the height-100 monotone forward packet and absolute derivative price computation there, with the rational prices and omitted-weight and exceptional budgets of the [round-98 contour](newton-contour-98-check.py). These boxes lie inside its wider square; the dimensional bounds for exceptional terms used there follow from the same cap 4.8, lower real floor and upper modulus. The largest segment rate is below \(0.990737\). For each segment \(I\) the [translated-column estimate](shifted-resolvent-96.md#consequences-for-the-full-linearized-inverse) gives the uniform limsup bound \(P_I=\sqrt2(2/(1-q_I)-1)\) on \(\sqrt n\max_{ij}|Z_{ij}|\). It uses the same branch and absolute derivative packet rate \(q_I\), including the terms supported at the two exceptional sites. The estimates are uniform within each fixed box, and there are finitely many boxes.

Apply Cauchy's formula for the derivative to each entry. Along every vertical segment in the nominated square its scaled derivative has limsup at most \(\sum_I |I|P_I/(2\pi\operatorname{dist}(I,Q)^2)\). Conjugacy handles the bottom edge. Multiplying by \(h\) gives less than \(0.282628\); the entries are real on the real diameter. Hence eventually, uniformly through eligible primes,
\[
            \sqrt n\max_{ij}|\Im Z_{ij}|<0.283,\qquad
            \sqrt n\max_{ij}|Z_{ij}|<178 .
\]
The latter is the original round-96 small-square bound.

## The signed mixed term on the actual hitting row

At any hitting site \(i\), put \(\epsilon_i=\operatorname{sgn}\Im(U_i/\sqrt t)\). The [full-square nominal correction](newton-boundary-98.md#control-the-newton-correction-on-the-full-square) gives \(\epsilon_i\Im((ZB)_i/\sqrt t)>2\cdot10^{-4}/\sqrt3-7.1\cdot10^{-5}>4.4470\cdot10^{-5}\). The exact square gives, for every row,
\[
 \left|\Im((ZB)_i/\sqrt t)-2\sum_j (\Re Z_{ij}) w_j\ell_j u_jv_j\right|
 \le w_*(0.283+178\max|\kappa_j|)\sqrt n E<0.015\sqrt n\,r^2
                                                                    \tag{3}
\]
when \(r>0\). This uses \(|e^{i\kappa}-1|\le|\kappa|\) on the part multiplied by \(\Re Z\), and \(|\Delta^2|=|\Delta|^2\) on the part multiplied by \(\Im Z\). The mixed sum has modulus at most \(356 w_*\sqrt n\,x\sqrt E\). Equations (2) and (3), using the unrounded constants in both terms, give the second condition in (1). Directly taking modulus in the square bounds the output by \(178w_*M^2\sqrt n\,r^2\), giving the first condition. For instance, if \(\sqrt n\,r^2\le10^{-4}\), a hit requires the actual signed quantity \(2\epsilon_i\sum_j(\Re Z_{ij})w_j\ell_j u_jv_j>4.297\cdot10^{-5}\).

There is a prefix-only upper on \(r_I\) throughout the square. The [round-97 time-source recurrence](same-floor-97.md#transporting-the-nominal-real-reflection) bounds \(\|\partial_t V_j\|_\infty\le 9q^j+0.36(1-q^j)/(1-q)<21\) for \(0\le j\le100\), \(q=0.984138\). Finite-prime rates and sources have strict margins in those two quoted caps. On any segment between consecutive rows the physical scalar multiplier \(D(v)=v/\sqrt{4t_j+v^2}\) has modulus below \(d_*=0.51358\), by the [seed-disk estimate](astra-source-88.md#the-seed-centered-disks-on-the-complex-square). Its total time derivative has modulus bounded by \(D_*=(4(a+2h)21+2(4.768))/(4L-4)^{3/2}\), using \(|\Im v|<2\); at the mark use \(4n\,21/(4n-4)^{3/2}<D_*\). Write \(R_j=V_{j+1}-V_j\). Differentiating \(R_j=K\int_0^1 D(V_{j-1}+sR_{j-1})R_{j-1}\,ds\) in counting second norm gives
\[
  \|R'_{100}\|_{2,n}\le42d_*^{100}+100 D_*(0.169724)d_*^{99} .
\]
The starting derivative uses the two bounded prefix derivatives and \(\|R_0\|_{2,n}<0.169724\). Integrating from the real diameter yields \(r_I\le h[42/0.169724+100D_*/d_*]\bar r<0.00624\bar r\), and \(r\le\bar r\) by the prefix increment bound. Combined with (1) this gives the stated necessary size. The saved numbers are outward scalar and packet arithmetic. No physical first hit or ordinary theta limit is asserted. [Two Arb192 records](astra-rotate-99-checks.jsonl)

1. On the genuine hit and in the regime \(\sqrt n\,r^2\le10^{-4}\), bound the real signed mixed sum in (3), including \(2\epsilon_i\), by \(4.297\cdot10^{-5}\); retain the two lag components and common-site weight.
2. For a growing prefix certify its own versions of the entry, angular and energy bounds and \(\sqrt n(0.024r^2+17.51r r_I)\le4.4470\cdot10^{-5}\) with the same nominal margin. The current height-100 rate and contour are fixed-height estimates.
