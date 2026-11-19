# Two-floor control of the actual complex stationary row

For two genuine unforced factor pairs at distinct complex floors, the complementary sector equations give a signed secant identity. Only the marked term contains a change in explicit weights after the bulk floor is normalized to one. This gives a prime-uniform Lipschitz bound on the marked logarithm throughout the closed relative-phase chamber in the cold square. Comparison to the true real stationary pair gives a normalized exponential discrepancy estimate for the bulk at any available complex point in the enlarged absolute sector, including beyond first spread contact. Existence on a prime-uniform complex neighborhood remains open.

## The signed secant with the physical means retained

Write \(n=(p-1)/2\), \(c_n=(n-1)/n\), and \(W(t)=1+c_n t\). Use the genuine unforced factors \(A,B\), scaled so \(A_iB_i=t\) on the bulk and \(A_0B_0=n\). They belong to complementary real Fourier sectors plus constants, and on the positive mean sheet their common mean is \(\sqrt{W(t)}\). Put \(\mathcal A=A/\sqrt t\), \(\mathcal B=B/\sqrt t\), so their common mean is \(M(t)=\sqrt{c_n+1/t}\) with the root positive on the positive real axis. With continuous relative logs \(z_i=\rho_i+i\phi_i\), the normalized factors are \(e^{\pm z_i}\) on the bulk and \(\sqrt{n/t}\,e^{\pm z_0}\) at the mark. These formulas use the nonzero factors and remain meaningful without the activation chart. [Proper factor family](astra-phase-86.md)

For two genuine pairs at \(t_1,t_2\) on this mean sheet, put \(d_i=(z_i^{(1)}-z_i^{(2)})/2\), \(\Phi_i=\phi_i^{(1)}+\phi_i^{(2)}\), and
\[
 s_j=\sqrt n/\sqrt{t_j},\qquad s=(s_1+s_2)/2,\qquad e=(s_1-s_2)/2,\qquad r=|e/s|.
\]
The Hermitian product of the two factor differences in counting norm is \(n|M(t_1)-M(t_2)|^2\), since their nonconstant parts are in opposite sectors. Off the mark the individual product is \(-4e^{i\Phi_i}|\sinh d_i|^2\). At the mark the factor differences are \(2e^{(z_0^{(1)}+z_0^{(2)})/2}(s\sinh d_0+e\cosh d_0)\) and \(2e^{-(z_0^{(1)}+z_0^{(2)})/2}(-s\sinh d_0+e\cosh d_0)\). Let \(\beta\) be a real orientation, \(c_i=\cos(\Phi_i-\beta)\), and \(v_0=\sin(\Phi_0-\beta)\). The real rotated pairing is exactly
\[
\begin{split}
 \sum_{i\ne0}c_i|\sinh d_i|^2+c_0|s|^2|\sinh d_0|^2
       +\tfrac n4\cos\beta\,|M(t_1)-M(t_2)|^2
 &=c_0|e|^2|\cosh d_0|^2\\
 &\quad-2v_0\Im(s\overline e\,\sinh d_0\,\overline{\cosh d_0}) .
\end{split}                                                        \tag{1}
\]
The explicit weight-change source is entirely at the mark.

Suppose \(c_i\ge0\) on the bulk, \(c_0>0\) and \(\cos\beta\ge0\). Put \(\Gamma=(1+|v_0|)/c_0\). With \(X=|\sinh d_0|\), \(Y=|\cosh d_0|\), (1) gives \(X^2\le r^2Y^2+2r|v_0|XY/c_0\), hence \(X\le r\Gamma Y\). Since \(Y^2-X^2=\cos(2\Im d_0)\le1\), if \(r\Gamma<1\) then
\[
\begin{split}
 |\sinh d_0|&\le\frac{r\Gamma}{\sqrt{1-r^2\Gamma^2}},\\
 \sum_{i\ne0}c_i|\sinh d_i|^2+\tfrac n4\cos\beta\,|M(t_1)-M(t_2)|^2
      &\le \frac{c_0\Gamma^2}{1-r^2\Gamma^2}|e|^2 .
\end{split}                                                        \tag{2}
\]
The second line uses \(c_0+2|v_0|\Gamma=c_0\Gamma^2\). The mean term is also \(\cos\beta\,|e|^2\,4|s|^2/(n|M(t_1)+M(t_2)|^2)\) by subtracting \(M(t_j)^2=c_n+s_j^2/n\).

## Bounds on the available physical cold sector

For a fixed lower real floor \(L>0\), write \(D=|t_1-t_2|\). The principal square roots give
\[
 r=\frac D{|\sqrt{t_1}+\sqrt{t_2}|^2}\le \frac D{4L},\qquad
 \frac{|e|}{\sqrt n}
 =\frac{D}{2|\sqrt{t_1}\sqrt{t_2}|\,|\sqrt{t_1}+\sqrt{t_2}|}
 \le \frac D{4L^{3/2}}.                                           \tag{3}
\]
In the cold square let both true rows have \(|\phi_i^{(j)}|\le\arctan(3/2)\) and phase spread at most \(\pi/2\). Their summed phases have spread at most \(\pi\). Use its midpoint for \(\beta\), so \(c_i\ge0\). The marked sector inequality on the physical sheet gives \(|\Phi_0|<10^{-6}\) there. Since \(\Phi_0\) lies between the two summed extremes, both \(|\beta|\) and \(|\Phi_0-\beta|\) are at most \(\arctan(3/2)+|\Phi_0|/2<\pi/3\). Thus \(c_0,\cos\beta>1/2\), and \(\Gamma<4\). Equation (2) bounds the marked log difference by \(O(D/L)\) and the normalized angularly weighted bulk discrepancy by \(O(D^2/L^3)\), uniformly over fields and through exact chamber contact. Here \(|z_0^{(1)}-z_0^{(2)}|\le\pi|\sinh d_0|\) by \(|\Im d_0|\le\pi/2\) and the sine bound on that interval. The comparison does not require a path inside a common domain. [Marked sector](parallel-cold-complex-36.md#1-the-exceptional-coordinate-forces-a-complex-sector)

There is also a coercive comparison beyond spread contact. Given a true physical unforced row at \(t=x+iy\) in the cold square, use the strictly positive stationary pair at \(t_2=x\) and take \(\beta=0\). Then \(\Phi_i=\phi_i(t)\). Throughout the enlarged absolute sector all \(c_i\ge2/\sqrt{13}>1/2\), and (2) gives
\[
 |z_0(t)-z_0(x)|=O(|y|/x),\qquad
 \frac1n\sum_{i\ne0}\left|\sinh\frac{z_i(t)-z_i(x)}2\right|^2
       =O(|y|^2/x^3).                                             \tag{4}
\]
The constants in (4) are absolute on the square. In particular the normalized bulk average of \(\cosh(\Re(z_i(t)-z_i(x)))-1\) has the same bound, since \(|\sinh((u+iv)/2)|^2=(\cosh u-\cos v)/2\). The marked estimate holds further up to the first absolute right angle \(|\phi_i|\le\pi/2\), with the bulk estimate then weighted by \(\cos\phi_i\). At any fixed threshold of relative discrepancy the enlarged-sector estimate gives a quadratic counting bound, through primes. A bound on the absolute amplitudes of the true real row is unnecessary for this comparison.

At small real floors the common mean in (1) improves the scale. Suppose \(x>0\) tends to zero, \(|y|\le x\), and a genuine pair at \(t=x+iy\) on the physical mean and mark sheets has \(|\phi_i|\le\pi/2\). Compare it again to the true real pair at \(x\). Use \(\beta=0\) and denote the ratio of the mean term to \(|e|^2\) by \(\Lambda=4|s|^2/(n|M(t)+M(x)|^2)\). It satisfies \(\Lambda=1+O(x)\) uniformly in \(n\). Indeed \(M(t_j)=(1/\sqrt{t_j})\sqrt{1+c_nt_j}\), the last factor differs from one by \(O(x)\), and the two reciprocal square roots lie in a common angle interval of length at most \(\pi/8\). The true marked sector gives \(v_0=O(|y|)\), \(c_0=1+O(y^2)\). Since \(r\le1/4\), the nonnegative bulk terms in (1) then give
\[
 (1-r^2)X^2\le O(r^2 x)+O(|y|)rX(1+X).
\]
For sufficiently small \(x\), absorb the last quadratic term and apply the inequality \(2ab\le a^2+b^2\) to the linear term. This gives \(X=O(r\sqrt x)\). Substituting into (1) after retaining its mean term shows that the angularly weighted bulk sum is \(O(|e|^2x)\). Accordingly the available complex branch satisfies
\[
 |z_0(x+iy)-z_0(x)|=O(|y|/\sqrt x),\qquad
 \frac1n\sum_{i\ne0}\cos\phi_i(t)
       \left|\sinh\frac{z_i(t)-z_i(x)}2\right|^2=O(|y|^2/x^2).        \tag{6}
\]
The constants here are independent of the field and small floor. The case \(y=0\) in the phase regime follows directly from (1).

## Infinitesimal balance up to and past spread contact

For a differentiable true unforced germ, use the derivative with respect to the log of the marked weight \(s_0\) while keeping the bulk weight \(t\) fixed, at \(s_0=n\). Write \(g_i\) for the derivative of \(z_i\); scaling all weights identifies \(g_i=-t\,z_i'(t)\) on the actual floor branch. The homogeneous rescaling defines this derivative whenever the specified floor germ is holomorphic, including at a singular Jacobian. Here use the original factors \(A,B\) of common mean \(\sqrt W\). Their derivatives are \(A_i(g_i+\tfrac12 1_{i=0})\) and \(B_i(-g_i+\tfrac12 1_{i=0})\) and have common mean \(1/(2\sqrt W)\). With \(\tau_i=|t|\) on the bulk and \(\tau_0=n\), the Hermitian pairing gives, for any real \(b\) with \(c_0=\cos(2\phi_0-b)>0\),
\[
\begin{split}
 \frac1n\sum_{i\ne0}\tau_i\cos(2\phi_i-b)|g_i|^2
 &+c_0(\Re g_0)^2
  +c_0\left(\Im g_0+\frac{\tan(2\phi_0-b)}{2}\right)^2\\
 &=\frac1{4c_0}-\frac{\cos b}{4|W|}.                              \tag{5}
\end{split}
\]
Indeed the marked product before rotation contributes \(ne^{2i\phi_0}(1/4-|g_0|^2+i\Im g_0)\). On the closed chamber with enlarged absolute phases take \(b=\max_i\phi_i+\min_i\phi_i\). Then all bulk cosines are nonnegative, and \(c_0,\cos b>1/2\). The disk in (5) gives a uniform bound \(|g_0|\le 1+\sqrt3/2<2\), including an analytic first-contact germ by continuity. Beyond the chamber the same identity keeps the negative angular action as a separate term at the actual bulk sites.

## Comparison along the true height-600 forcing line

For \(n\ge10^{30}\) on the concentric half-square let \(t=x+iy\) and take the physical row on the height-600 forcing line at \(q=1-\lambda\in[0,1]\), within the enlarged absolute sector. Compare it to the true unforced real factors at \(x\). Write \(R'(t)=R(t)/\sqrt t\), let \(F,G\) be the differences of the normalized \(A,B\) factors, and let \(M^c(t,q)\) be the common normalized mean of the completed factors. Use normalized counting \(E\). Their exact Hermitian sector pairing is
\[
 \Re E(F\overline G)
  =|M^c(t,q)-M(x)|^2+\frac q2\Re E(R'(t)\overline{F-G})
                         +\frac{q^2}{4}E|R'(t)|^2 .                    \tag{7}
\]
Indeed the completed difference factors are \(F+qR'/2,G-qR'/2\), with common mean difference \(M^c-M(x)\). Use \(r_t=\|R(t)\|_{2,n}\), \(r_x=\|R(x)\|_{2,n}\). The actual residual pairing on the right of (7) has absolute value \(O(r_t^2+r_x^2+r_t|y|)\) before multiplication by \(q/2\). For the physical row split \(U(t,q)-X(t)\) at modulus one as in the genuine secant bound. Cauchy–Schwarz below one and the uniform \(\|R\|_\infty\) cap above one bound its pairing by \(O(r_t^2)\). The same split for the real stationary row minus \(X(x)\) costs \(O(r_t r_x+r_x^2)\) against \(R(t)\). The remaining difference \(X(t)/\sqrt t-X(x)/\sqrt x\) has sup norm \(O(|y|)\) by bounded holomorphy of the actual predictor on the full square and Cauchy on the half-square. The constants are absolute on the fixed square. [True predictor secant](astra-imaginary-84.md#large-derivatives-at-height-600-beyond-unit-phase)

Set \(\beta=0\) in the factor expansion of (1). With (7), its left side has the same bulk and marked terms, and the mean term is \(n|M^c-M(x)|^2/4\). The additional error is at most \(O(nq(r_t^2+r_x^2+r_t|y|))\), since the \(q^2\) term is favorable. The real reference has zero phases, so every \(c_i>1/2\). The marked weight ratio \(r\) in (3) is uniformly small. With \(Y\le1+X\), absorb the terms \(|e|^2 X^2\) and \(2|se|X(1+X)\) into the marked quadratic term, using Young's inequality for the linear term. Since \(|s|^2\asymp n\) on the fixed square, this gives
\[
 \left|z_0(t,q)-z_0(x,0)\right|^2+
   \frac1n\sum_{i\ne0}\left|\sinh\frac{z_i(t,q)-z_i(x,0)}2\right|^2
       =O\!\left(|y|^2+q(r_t^2+r_x^2)\right).                         \tag{8}
\]
This uses the actual forced mark in the enlarged sector and the same positive real reference at each \(x\). The normalized bound retains an explicit positive floor-dependent error; it permits sparse high relative discrepancies and does not bound the absolute real amplitude of the reference row.

The [Arb128 replay](physical-two-floor-88-check.py) uses the actual \(p=173\) real-start ray above \(x=1/50\). It checks (1), (2) and (5) at \(y=0.02161\), just beyond first spread contact inside the enlarged absolute sector, and at \(y=0.022\), outside the enlarged sector with all absolute phases still below \(\pi/2\). In both cases the orientation \(\beta=0\) keeps the finite-difference bulk term nonnegative, while the corresponding local tangent includes a negative raw cosine. These finite checks concern the two stated points. [Interval records](physical-two-floor-88-checks.jsonl)

1. Use the relative estimate (4) against the true real row to bound the amplitude-weighted large-phase sites seen by the signed residual or Jacobi return. This requires control of their overlap with the actual real amplitude tail.
2. Beyond first contact, compare the signed bulk term in (5) with genuine complementary tangent constraints. A marked bound along the continued segment may be possible without controlling the full-row inverse.
