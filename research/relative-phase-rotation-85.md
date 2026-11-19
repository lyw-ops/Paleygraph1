# Rotating the relative phases at an actual cold Jacobian

At a physical solution on the cold forcing path, a spread of relative phases below \(\pi/2\) suffices for an invertible Jacobian even when individual activation derivatives have modulus above one. At first contact with that spread, a singular direction is supported on the two sets of extreme phases. A weighted cross compression provides a further test on these two sets. The unforced phase budget then excludes singularity at such a first contact on an explicit \(p^{-1/4}\) scale, within the stated enlarged sector. An ordinary holomorphic continuation theorem on a common two-dimensional neighborhood remains open.

## Exact rotation of the linear problem

Retain the physical \(K=K^*\), \(K^2=I-J\) and \(\Phi_i(U_i)=\sqrt{4t_i+U_i^2}\), where \(J\) is the constant projector, \(t_0=n\), and \(t_i=t\) on the bulk. Write
\[
 U_i=2\sqrt{t_i}\sinh z_i,\qquad
 \Phi_i(U_i)=2\sqrt{t_i}\cosh z_i,\qquad
 \phi_i=\Im z_i,\qquad D_i=\tanh z_i .
\]
All functions and lifts refer to the actual continuing branch. Work in \(|\phi_i|\le\alpha=\arctan(3/2)<\pi/2\), so the activation never vanishes. Suppose the \(\phi_i\)'s fit in \([c-\pi/4,c+\pi/4]\) with \(|c|<\pi/4\). Put \(\tau=\tan c\),
\[
 \widetilde D=(D-i\tau I)(I-i\tau D)^{-1}=\operatorname{diag}\tanh(z_i-ic),
 \qquad
 \widetilde K=(I-i\tau K)^{-1}(K-i\tau I)=K-i\tau J .
\]
The diagonal denominators are nonzero since
\(\cosh(z_i-ic)=\cos c\,\cosh z_i(1-i\tau D_i)\) and \(|\phi_i-c|\le\pi/4\). The last identity for \(\widetilde K\) follows by evaluating on the eigenvalues \(0,\pm1\) of \(K\). For \(u=(I-i\tau D)h\), direct multiplication gives
\[
 (I-KD)h=\frac{1}{1+\tau^2}(I-i\tau K)(I-\widetilde K\widetilde D)u .       \tag{1}
\]
Thus the rotation changes only the constant multiplier of \(K\). In particular \(\widetilde K^*\widetilde K=I-(1-\tau^2)J\). If the relative phases have spread strictly below \(\pi/2\), one can choose \(|c|<\pi/4\) so they lie strictly within the centered interval. Indeed the allowable centers are \((\max_i\phi_i-\pi/4,\min_i\phi_i+\pi/4)\), which intersects \((-\pi/4,\pi/4)\) inside the enlarged sector. Then \(\|\widetilde D\|<1\) and the physical Jacobian is invertible.

At spread exactly \(\pi/2\), put \(c=(\max\phi+\min\phi)/2\), so \(|\tau|\le1/5\). If the Jacobian is singular, equality of norms in the contracted equation from (1) forces \(u\) to be supported on
\[
 S=S_+\cup S_-,\qquad S_\pm=\{i:\phi_i=c\pm\pi/4\},
 \qquad J\widetilde D u=0.
\]
The equation on \(S\) therefore uses \(K_{SS}\) itself because the rotated constant term vanishes. Write \(v=\widetilde D u\). Then \(u=Kv\) and \(Ku=K^2v=v\). Consequently \(u+v\) and \(u-v\) are eigenvectors of the compression with respective eigenvalues \(+1\) and \(-1\). Neither can vanish because each active \(\widetilde D_i\) has nonzero imaginary part. More generally, if the Jacobian nullity is \(m\ge1\), the maps \(u\mapsto (I\pm\widetilde D)u\) are injective on the rotated kernel. Each eigenvalue has multiplicity at least \(m\) on this compression. The entry bound now gives \(2m\le \|K_{SS}\|_{\mathrm F}^2\le p|S|^2/n^2\). Thus \(|S|\ge\sqrt{2m}\,n/\sqrt p\). This support statement includes both extremes rather than all sites with \(|D_i|>1\).

## The weighted cross compression

For \(i\in S\) put \(w_i=|\Im(\widetilde D_i^{-1})|>0\), and use \(W_\pm=\operatorname{diag}(w_i:i\in S_\pm)\). The inverse \(\tanh\) values here have modulus one and imaginary signs opposite to the indicated phase sign. More explicitly \(w_i=1/\cosh(2\Re z_i)\) at either relative extreme. Singularity at the contact requires
\[
 \big\| W_+^{-1/2}K_{S_+S_-}W_-^{-1/2}\big\|_{2\to2}\ \ge1 .           \tag{2}
\]
Indeed \(v=\widetilde D u\) solves \((\widetilde D^{-1}-K_{SS})v=0\). With \(y_\pm=W_\pm^{1/2}v_\pm\), each rescaled diagonal block has Hermitian real part and imaginary part \(\mp I\). Its inverse has norm at most one. The two equations read \(A_+ y_+=C y_-\) and \(A_- y_-=C^*y_+\), with \(C=W_+^{-1/2}K_{S_+S_-}W_-^{-1/2}\). Both components must be nonzero. Combining the norm bounds proves (2). The imaginary parts also give \(\|y_+\|_2=\|y_-\|_2\) and
\[
 |\Im\langle C y_-,y_+\rangle|=\|y_+\|_2^2 .
\]
Thus the obstruction involves a signed cross return, even in cases where the whole compression has norm one. A sufficient magnitude bound for (2) to fail is
\[
 \frac{\sqrt p}{n}
 \left(\sum_{S_+} w_i^{-1}\sum_{S_-} w_i^{-1}\right)^{1/2}<1
\]
by the Jacobi entry bound. Large real amplitudes remain in the weights.

## Consequence at an unforced first contact

At \(\lambda=1\), the actual scaled factors \(A_i=\sqrt{t_i}e^{z_i}\), \(B_i=\sqrt{t_i}e^{-z_i}\) lie in opposite Fourier sectors plus constants. Their means agree, and their product is \(t_i\). Write \(\kappa=(n-1)/n\). Ordinary and Hermitian orthogonality therefore give
\[
 E(A B)=1+\kappa t,\qquad E(\overline A B)=|1+\kappa t|,
\]
where \(E\) is normalized counting. In particular, for \(t=x+iy\) with \(x>0\),
\[
 E|t_i|\sin^2\phi_i
 =\frac{1+\kappa |t|-|1+\kappa t|}{2}
 \le \frac{\kappa y^2}{4x(1+\kappa x)}.                            \tag{3}
\]
For the inequality rationalize the numerator first by the sum of the two moduli, then use \(|t|-x=y^2/(|t|+x)\). This includes the exceptional site with \(t_0=n\).

At spread exactly \(\pi/2\) within \(|\phi_i|\le\alpha\), every site in \(S\) satisfies \(\sin^2\phi_i\ge\cos^2\alpha=4/13\). For \(n\ge x\), if this contact is singular then (1) gives \(|S|/n\ge\sqrt{2m}/\sqrt p\), and (3) implies
\[
 |y|\ \ge\ (2m)^{1/4}\,4x\sqrt{\frac{1+\kappa x}{13\kappa\sqrt p}} .            \tag{4}
\]
Consequently an unforced branch in the enlarged sector cannot have a singularity at its first spread contact below that explicit width. At \(x=2031/128\) the right side is greater than \(85.7p^{-1/4}\). The result is local at the contact. A trajectory can pass through a nonsingular contact and later leave the sector or become singular.

There is an additional compatibility at an unforced first contact on the cold square, even without the shrinking-width restriction (4). The marked contribution to (3) is \(\sin^2\phi_0\), which is less than \(4/13\) throughout that square. Thus every linear kernel vector \(h\) vanishes at the mark, since (1) locates its support in \(S\). For the original unforced equation \(F(U,t)=U-K\Phi_t(U)=0\), the left null vectors of \(I-KD\) are exactly \(Dh\) as \(h\) ranges over its right kernel. This uses transpose over \(\mathbb C\), not adjoint: \((I-DK)Dh=0\), the map \(h\mapsto Dh\) is injective on the kernel by \(h=KDh\), and left and right nullities agree. Euler's scalar identity \(\Phi_i-D_i U_i=4t_i/\Phi_i\) gives
\[
 (I-KD)U=K(4t_i/\Phi_i),\qquad
              \sum_i t_i h_i/\Phi_i=0 .
\]
Here pairing with \(Dh\) uses \((Dh)^{\mathsf T}K=h^{\mathsf T}\). Since \(h_0=0\), every such left null vector annihilates the actual floor forcing:
\[
             (Dh)^{\mathsf T}\partial_t F
                        =-2\sum_{i\ne0}h_i/\Phi_i=0 .            \tag{6}
\]
In particular ordinary transverse fold ramification in the floor variable is excluded at this first contact. Zeroth-order singularity and higher-order obstruction are still possible. For the two-parameter equation \(F(U,t,\lambda)=U-K\Phi_t(U)+(1-\lambda)R(t)=0\) at any singular point with \(h_0=0\), the same calculation gives the exact projection
\[
 (Dh)^{\mathsf T}\partial_t F
       =(1-\lambda)(Dh)^{\mathsf T}\bigl(R'(t)-R(t)/(2t)\bigr).
\]
This is a signed estimate for the parameter source on the actual obstruction space.

The null direction also has a balanced factor form at an unforced contact. With \(\omega_i=h_i/\Phi_i\), the variations \(\delta A_i=A_i\omega_i\), \(\delta B_i=-B_i\omega_i\) are in the complementary Fourier sectors with common mean. Indeed \(\delta A-\delta B=h=KDh=K(\delta A+\delta B)\). The pointwise zero variation of their product forces that common mean to vanish, because each original mean is nonzero. Pairing the two variations in both the ordinary and Hermitian ways now gives
\[
 \sum_{i\in S}\omega_i^2=0,\qquad
             \sum_{i\in S_+}|\omega_i|^2
               =\sum_{i\in S_-}|\omega_i|^2 .
\]
Here all contact sites are bulk. The second identity uses \(e^{-2i\phi_i}=\mp i\,e^{-2ic}\) on the two sides. The projected second variation of \(F\) on this direction is \(-4t\sum_{i\in S}\omega_i^3\) after pairing against the same left null vector \(Dh\). The two balance identities do not identify this cubic or exclude higher-order ramification.

## Rotated action along the height-600 path

Take the true forcing path starting at \(X=V_{600}(t)\) with \(R=K\Phi_t(X)-X\), so \(U-K\Phi_t(U)=(\lambda-1)R\). Let \(E\) and the second norm be normalized. For any linear perturbation \(h\), set \(g=Dh\), \(b=h-Kg\). The norm identity and the reality of \(E(Kg)\bar g\) give
\[
 \begin{split}
 E(1-|D|^2)|h|^2+|Eg|^2&=2\Re E b\overline h-\|b\|_2^2,\\
 E(\Im D)|h|^2&=-\Im E b\overline g .
 \end{split}
\]
Use \(h=\partial_\lambda U\), \(b=R\), and a fixed orientation \(\beta=2c\in(-\pi/2,\pi/2)\). Multiply the two identities by \(\cos\beta\) and \(2\sin\beta\), respectively. The resulting loss is exactly
\[
 E\,4|t_i|\cos(2\phi_i-\beta)|\partial_\lambda z_i|^2
      +\cos\beta\,|E g|^2 .
\]
The two signed cross terms integrate to \(2\Re E R[\cos\beta\,\overline{\Delta U}+i\sin\beta\,\overline{\Delta\Phi}]\). Here \(\Delta U=U-X\), \(\Delta\Phi=\Phi_t(U)-\Phi_t(X)\) at the end of the segment. The [height-600 enlarged-sector secant estimate](astra-imaginary-84.md#large-derivatives-at-height-600-beyond-unit-phase) gives \(|\Delta\Phi_i|\le|\Delta U_i|\), the sup bound \(0.011\) on \(R\), and \(E\min(|\Delta U|^2,|\Delta U|)\le870 v^2\|R\|_2^2\) through time \(v\le1\). Split at unit displacement to get
\[
 E|R\Delta U|\le(\sqrt{870}+0.011\cdot870\,v)\,v\|R\|_2^2 .
\]
Thus if the available segment in the enlarged sector lies in one rotated interval \(|\phi-c|\le\pi/4\), one has the nonnegative integrated estimate
\[
 E\int_0^v 4|t_i|\cos(2\phi_i-\beta)|\partial_\lambda z_i|^2\,d\lambda
                  \le112\,v\|R\|_2^2.                          \tag{5}
\]
The numerical inequality only uses \(2\sqrt2(\sqrt{870}+9.57)<112\). This extends the phase action to asymmetric angular intervals, preserving the signed forcing and the weighted marked coordinate. At any fixed field the enlarged-sector secant estimate already prevents a coordinate from escaping to infinity on the available path.

1. On the actual branch estimate the signed weighted cross compression (2) on the two phase extremes, and project the second floor variation using (6) if this compression can have unit norm. Equation (4) identifies the regime where a first-contact singularity is already excluded.
2. Use the exact oriented action preceding (5) to control excursions in an angular interval selected by the actual phases. It remains necessary to prevent later escape from the enlarged sector or loss of invertibility beyond its first spread contact.
