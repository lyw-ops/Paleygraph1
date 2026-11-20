# Complete kernels for the favorable cross-ratio sector

Keep the actual near-critical short block, \(Q,n,\nu,f,\rho,v\) and physical correlation of [Round 154](ordinary-lift-and-gauss-kernel-154.md). The goal on this branch is a signed \(O(p)\) upper on its favorable Legendre off-diagonal. The [affine chart](ordinary-crossratio-affine-chart-155.md) used only physical \(x,y\in Q\). The favorable contribution can be extended to \(x,y\in\mathbb F_p\) at additive cost \(O(p)\). In the extension retain \(u\in Q\setminus\{1\}\), write \(t=r_u(y)/r_u(x)\), and require \(t\in Q\setminus\{1\}\), \(\chi(1-t)=\rho\). As before, include only nonzero factors of the four physical \(f\)'s in the term.

## Completing the selected sign at cost \(O(p)\)

For an arbitrary anchor \(a\in\widehat Q\), put
\[
 B_{u,a}(x)=f(1-vux)\overline{f(1-vx)}\,\overline{a(r_u(x))}
\]
on the contributing full field and zero elsewhere. Let \(B_{u,a}^{\rm sq}\) be the square part and \(B_{u,a}^{\rm ns}\) the nonsquare nonzero part. Their squared counting norms summed over \(u\in Q\setminus\{1\}\) satisfy
\[
 \sum_u\|B_{u,a}^{\rm sq}\|_2^2\ll p,\qquad
 \sum_u\|B_{u,a}^{\rm ns}\|_2^2\ll1 .
\]
For the first use the square row squared mass \(O(\sqrt p)\) from Round 153. For the second use its nonsquare row squared mass \(O(1)\). For either nonzero coset, multiplication by \(u\) is transitive as \(u\) ranges in \(Q\), so the sum is at most the square of its row squared mass. The zero coordinate is treated separately below.

On the contributing off-diagonal the denominator in the formula for \(1-t\) is square, so its favorable indicator is
\[
 \frac{1_{x\ne y}+\chi(u-1)\chi(y-x)}2.
\]
For the first half use the uniform-in-anchor \(O(p)\) full-versus-square correction of [Round 153](ordinary-affine-jacobi-factorization-153.md) to the unmasked squared correlation. Removing the physical diagonal adds at most \(O(p)\), including the \(n-1\) zero-zero terms of the full diagonal.

For the additive convolution half, temporarily restrict both rows to nonzero coordinates. The convolution by \(\chi\) on \(\mathbb F_p\) has norm \(\sqrt p\). The terms with at least one nonsquare nonzero input therefore have total absolute bound
\[
 O\!\left(\sqrt p\left(\sum_u\|B^{\rm sq}_{u,a}\|_2^2\right)^{1/2}
                     \left(\sum_u\|B_{u,a}^{\rm ns}\|_2^2\right)^{1/2}
          +\sqrt p\sum_u\|B_{u,a}^{\rm ns}\|_2^2\right)=O(p).
\]
To restore the cross terms with zero, the extra signed sum is twice the real part of
\[
 \sum_{u\in Q\setminus\{1\}}\chi(u-1)\sum_{x\ne0}
                                      \chi(x) B_{u,a}(x).
\]
The anchor can be absorbed into the full affine row \(h_a(x)=f(1-vx)\overline{a(1-vx)}\). On each nonzero \(Q\) coset, \(\chi(x)\) is constant, and the \(x\)-sum is a multiplicative correlation of that row. The unnormalized Fourier multiplier of \(u\mapsto\chi(u-1)\) on \(Q\) is \(O(\sqrt p)\) by the ordinary two-character Jacobi bound, including the trivial character. Multiplicative Parseval therefore bounds each coset contribution by \(O(\sqrt p)\) times its row squared mass. This gives \(O(p)\) for the square coset and \(O(\sqrt p)\) for the nonsquare coset. The zero-zero entry of the signed half vanishes. These bounds hold for every anchor, including the trivial anchor.

Averaging against \(\nu_a\) proves the claimed \(O(p)\) comparison. More generally, insert a slope multiplier \(\psi(t)\) on \(Q\) with Mellin Fourier coefficient sum at most \(K\). The coefficients of \(f(t)\psi(t)\) have absolute sum at most \(K\). The same pointwise-in-anchor comparison gives cost \(O(Kp)\), with no nonnegativity required of the new coefficients.

## A separated two-kernel expansion at fixed slope

For the exact full-field sum just obtained, fix \(t\ne0,1\) and take \(z=(1-u)/(u(1-vx))\), \(z'=t(z+1)-1\). The four nonzero arguments are
\[
 a_x=\frac{1-u}{u z},\quad c_x=\frac{(1-u)(z+1)}{z},\qquad
 a_y=\frac{1-u}{u z'},\quad c_y=\frac{(1-u)(z'+1)}{z'}.
\]
Conversely these arguments correspond to the unique \(x,y\) for this \(u,z,t\). In particular \(z,z',z+1\) are nonzero and the deleted points are \(0,-1,(1-t)/t\).

Use the true full lift law \(w\) of Round 153 to expand
\(f(c_x)\overline{f(a_x)}\,\overline{f(c_y)}f(a_y)\) in \(U,V,U',V'\). Set \(D=(U/V)/(U'/V')\). At fixed slope the sum of the four \(f\) factors over \(u,x,y\) with this relation is
\[
 \sum_{U,V,U',V'}w_Uw_Vw_{U'}w_{V'}
 \frac{J(V/V',D)+J(\chi V/V',D)}2\,
 \overline{U'(t)}
 \sum_{z\in\mathbb F_p}
 (U/U')(z+1)(V/U)(z)(U'/V')(t(z+1)-1).
\]
As always even a trivial character is zero at zero. Expanding each argument gives the \(u\)-factor \((V/V')(u)D(1-u)\) independent of \(z,t\), and leaves the displayed \(z\)-factor after expanding \(z'+1=t(z+1)\). Summing with the original \(f(t)\) over \(\chi(1-t)=\rho\) gives the full favorable contribution. Slope completion now involves this three-root kernel with its true four lifted weights and one more factor \(f(t)\). A pointwise estimate for the isolated \(z\)-sum still does not bound the required weighted sum over growing slopes.

## The actual convolution norm is large

Let \(h_\rho=1_{\{t\ne1,\ \chi(1-t)=\rho\}}f\) on \(Q\). Its convolution price \(\max_a|\widehat h_\rho(a)|\) uses the unnormalized multiplicative Fourier transform. For \(a\ne1\), the pin expansion \(f=c+e\) on the wrong sector gives
\[
 \widehat h_\rho(a)=n\nu_a-1-c\,\widehat{1_{\{\chi(1-t)=-\rho\}}}(a)
                         -\widehat{1_{\{\chi(1-t)=-\rho\}}e}(a).
\]
The mask coefficient is \(O(\sqrt p)\) for \(a\ne1\) by Jacobi. Since \(c=O(p^{-1/2})\) and \(\|e\|_2=o(1)\), the last two terms are \(O(1)+o(\sqrt p)\) uniformly. Choose a maximizer of \(\nu_a\), necessarily nontrivial by the actual zero mark. It has \(\nu_a\ge\sum_b\nu_b^2\sim\sqrt p/n\). Thus the maximum is at least \((1-o(1))\sqrt p\). It is \(O(\sqrt p)\) on every coordinate by the Jacobi bound and \(\max\nu_a=O(p^{-1/2})\). The \(O(1)\) uniform convolution bound fails on the hypothetical genuine critical sequence itself. This rules out a per-\(u\) uniform norm shortcut and leaves room for bounds coupling the actual translated data across \(u\).

## A weighted slope filter

Keep the quantitative pin of Round 154 and let \(\psi\) have normalized Mellin Fourier coefficient sum at most \(K\). The wrong sector with \(f\psi\) still costs \(O(Kp)\): its residual uses \(\|\psi\|_\infty\le K\) and the previous Mellin second moment, while its constant part uses each Mellin character separately in the exact negative sign mask. For each such character the unsigned term is bounded by \(M_a=O(p^{3/2})\) from Round 154, and the signed term again uses the additive convolution norm \(\sqrt p\) with \(\sum_u\|A_u\|_2^2=O(p)\). The unmasked diagonal costs \(O(Kp)\).

Write \(\mu_a\) for the normalized inverse-character coefficients of \(f\psi\), so that \(f(t)\psi(t)=\sum_a\mu_a a(t)\). The unmasked true sum is \(\sum_a\mu_a M_a\). The uniform-anchor second moment of Round 152 gives \(\sum_a M_a=O(np)\), with \(M_a\ge0\). Thus the absolute favorable filtered sum is
\[
 O\!\left(p(K+n\|\mu\|_\infty)\right).
\]
In particular, for a slope coset of \(H\le Q\) of size \(h\), the mask satisfies \(K=1\) by character orthogonality. One has \(\|\mu\|_\infty\le(h/n)\max_C\nu(C)\) with \(C\) ranging over dual cosets of \(H^\perp\). Its favorable contribution is therefore \(O(p(1+h\max_C\nu(C)))\). This gives an \(O(p)\) criterion for growing slope cosets with smooth actual dual mass, regardless of their total \(|f|\) mass. There is no assertion that such smoothing holds for the whole favorable sector.

## Separating the two nonzero additive frequency signs

In the physical square problem push \(A_u(x)\) forward by \(r_u\) to a row \(B_u(z)\), extended by zero off \(Q\). With the plus additive transform, the correlation at slope \(t\) is
\[
 \sum_z B_u(z)\overline{B_u(tz)}
      =p^{-1}\sum_{\xi\in\mathbb F_p}\widehat B_u(t\xi)\overline{\widehat B_u(\xi)} .
\]
For \(\xi=0\), summing with \(f(t)1_{\rm favorable}(t)\) costs \(O(p)\). Indeed \(\sum_{\rm favorable} f=O(\sqrt p)\) by the zero anchor weight, \(f(1)=1\), and the wrong-sector pin. Also \(\sum_u|\widehat B_u(0)|^2=M_{\rm triv}=O(p^{3/2})\).

Insert the extra multiplier \(\chi(\xi)\) in the frequency sum. The quadratic Gauss value gives the position kernel \(p^{-1/2}\chi(tz-w)\). In the sum over all \(t\in Q\) weighted by \(f(t)\), write \(t=(w/z)s\) for each contributing pair \(z,w\in Q\). Then \(\chi(tz-w)=\chi(1-s)\). The quadratic Jacobi coefficient in the \(a\)-term of \(f\) is \(\sqrt p k(a)\), so the resulting expression is exactly \(\sum_a\nu_a k(a)M_a\).

The wrong-sector subtraction here again costs \(O(p)\). In its constant component, the normalized Mellin coefficients of the wrong indicator are \(O(p^{-1/2})\) at nontrivial anchors and at most one at the trivial slot. Multiply by \(c=O(p^{-1/2})\), and use \(\sum_a M_a=O(np)\), \(M_{\rm triv}=O(p^{3/2})\), \(|k(a)|\le1\). The residual uses Cauchy–Schwarz with the Mellin array \(k(a)M_a\), whose second norm is no larger than that of \(M_a\). The \(t=1\) term is \(O(p)\) by Parseval with \(\sum_u\|B_u\|_2^2=O(p)\). Consequently the two favorable forms on nonzero \(\xi\) of signs \(\pm1\) are
\[
           \tfrac12\sum_a\nu_a(1\pm k(a))M_a+O(p).
\]
This retains the original weights and separates the frequency signs at the desired additive error scale. Bounding either favorable form still requires information about the coupled law \(\nu_a M_a\).
