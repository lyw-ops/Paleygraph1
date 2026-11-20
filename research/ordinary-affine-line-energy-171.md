# A prime power saving for the full weighted one-match physical criterion

Use the true \(g=|f|^2\) on \(Q\), extended by zero, with \(G=\sum g=O(\sqrt p)\), \(w=g(1-g)\), and the marked completed physical geometry of [Round 169](ordinary-one-match-twisted-physical-169.md). Counting norms are used. The following bound applies on the whole \(t\) range with the actual weight:
\[
 \sum_{s\ne1,t} w(t)\,|H_\alpha(s,t)|^2 = O(p^{23/8}).
\]
This improves the former \(O(p^3)\) bound. It falls short of \(O(p^{5/2})\); the separate zero-match term is unchanged.

## Affine action of the actual two unconstrained arguments

Use \(E=CY/D\) as in [Round 170](ordinary-distinct-dilation-cuts-170.md). Remove \(x=0,y=0\) at the prior target-scale cost in weighted squared norm. Then \(Y,D\) are nonzero and different from \(1\), and \(Y\ne D\) since \(u\ne1\). The exact sum/product identity gives
\[
 s=b+r e,\qquad e=1/E,\qquad
 r=\frac{Y-D}{1-D},\quad b=\frac{D(1-Y)}{Y(1-D)},\quad
 C=E\frac D Y .
\]
In particular \(r\ne0,1\), \(b\ne0,1\). The map \((Y,D)\mapsto(r,b)\) is injective, since \(Y=r+(1-r)D\) and \(D=br/((1-r)(1-b))\). Each pair \((Y,D)\) defines one affine permutation of the full prime field. In addition, the true physical square restriction is just \(b\in Q\) on the line parameters. Indeed \(b=D(1-Y)/(Y(1-D))=(D/Y)u^{-1}\), where \(u=(1-D)/(1-Y)\), and nonzero weights force \(D,Y\in Q\). The deleted \(u=1\) is equivalent to \(Y=D\).

For arbitrary thresholds \(a,d>0\), take the affine transformations from \(Y\) with \(g(Y)>a\) and \(D\) with \(g(D)>d\), keeping the preceding exclusions and the condition \(b\in Q\). If these two coordinate sets have sizes \(U,V\), the resulting set \(\mathcal L\) has size at most \(UV\). A vertical line in the parameter plane \((r,b)\) contains at most \(\min(U,V)\) members, since \(Y=r+(1-r)D\). A nonvertical line \(b=\xi r+\eta\) contains at most \(2V\) members: for fixed \(D\) its equation becomes
\[
 \xi Y^2+\bigl(\eta(1-D)-\xi D+D\bigr)Y-D=0 ,
\]
a nonzero polynomial of degree at most two. Thus with \(m_{\mathcal L}\) the vertical bound and \(M_{\mathcal L}\) the arbitrary line bound, \(m_{\mathcal L}\le\min(U,V)\) and \(M_{\mathcal L}\le 2V\).

## Weighted action bound using affine energy

For a function \(\mu\) on the affine group let \(M_\mu=\sum_g\mu(g)U_g\), where \((U_g h)(s)=h(g^{-1}s)\). The permutation representation on counting mean-zero complex functions is irreducible of dimension \(p-1\): additive translations give distinct frequency lines, and dilations act transitively on the nontrivial additive frequencies. Finite-group Plancherel applied to \(M_\mu^*M_\mu\) therefore gives
\[
 \|M_\mu\|_{\mathbf1^\perp\to\mathbf1^\perp}
 \le \left(p \sum_h\left|\sum_g\overline{\mu(g)}\mu(gh)\right|^2\right)^{1/4}.
\]
The factor \(p\) is the ratio of group order to this dimension. If the coefficient modulus is at most the indicator of \(\mathcal L\), the sum inside the fourth root is bounded by its affine energy \(E(\mathcal L)=\#\{(g,h,g',h'):g^{-1}h=g'^{-1}h'\}\), before the factor \(p\).

Use the affine energy bound
\[
 E(\mathcal L)\ll m_{\mathcal L}^{1/2}|\mathcal L|^{5/2}
                    +M_{\mathcal L}|\mathcal L|^2
 \quad\text{provided }m_{\mathcal L}|\mathcal L|\le p^2 .
\]
This is Theorem 2.1 of [Petridis, Roche-Newton, Rudnev and Warren, An Energy Bound in the Affine Group](https://arxiv.org/abs/1911.03401). The two maximum multiplicities refer exactly to the affine parameter plane, with the first coordinate the multiplicative slope.

Set \(\tau=p^{-1/8}\). For \(g(Y),g(D)>\tau\), write the two weights by layer cake on \((0,1)\), with thresholds \(\max(a,\tau),\max(d,\tau)\). The size bounds \(U,V\le G/\tau=O(p^{5/8})\) give \(m_{\mathcal L}|\mathcal L|=O(p^{15/8})<p^2\) eventually. Use also \(U\le G/a,V\le G/d\). Since \(m_{\mathcal L}\le\sqrt{UV}\), the fourth root of the first energy term is at most \((UV)^{11/16}\). The fourth root of the second is at most \(2^{1/4}U^{1/2}V^{3/4}\). Both bounds are integrable over \(a,d\in(0,1)\), since each exponent of \(1/a,1/d\) is less than one. Consequently any such weighted affine action with coefficients \(\mu(r,b)=g(Y)g(D)1_{g(Y),g(D)>\tau}\xi_{Y,D}\), \(|\xi_{Y,D}|\le1\), has
\[
 \|M_\mu\|_{\mathbf1^\perp\to\mathbf1^\perp}
   \ll p^{1/4}\bigl(G^{11/8}+G^{5/4}\bigr)=O(p^{15/16}).
\]
Its action on constants has norm at most \(G^2\). The bounds apply to coefficients with any phases, with no estimate on individual field slopes assumed.

## Restoring the fourth true factor

For the heavy \(Y,D\) pairs, retain \(b\in Q\) and complete the \(x=0\) boundary and the auxiliary slopes \(0,1\) positively. This is an upper on the actual nonnegative kernel. For \(s\ne0,1\), recovering \(u=(1-D)/(1-Y)\), \(A=sE\), and then \(x,y\) gives the original completed input, except for the named \(x=0\) boundary. In particular the affine equation ensures the reconstructed \(C\) equals \(1-u+uA\). Extend \(h_t(e)=g(t/e)\) by zero at \(e=0\). Since the true mass satisfies \(g(x)=\sum_\alpha\omega(\alpha)\alpha(x)\) on nonzero \(x\), \(\sum_\alpha\omega(\alpha)=1\), the factor \(g(C)=g(E D/Y)\) gives the exact identity for the completed heavy kernel
\[
 H_{\mathrm{heavy,comp}}(\cdot,t)
   =\sum_\alpha\omega(\alpha)M_{\mu_\alpha}h_{t,\alpha},\qquad
 h_{t,\alpha}(e)=h_t(e)\alpha(e^{-1}),\quad
 \mu_\alpha(r,b)=g(Y)g(D)\alpha(D/Y)
\]
on the heavy pairs, with \(h_{t,\alpha}(0)=0\). The input second norm is at most \(\sqrt G\), and its constant projection has second norm at most \(G/\sqrt p\), by the true \(g\) mass. The mean-zero part contributes \(O(p^{15/16}\sqrt G)=O(p^{19/16})\), uniformly in \(t\), while the constant part is \(O(G^3/\sqrt p)=O(p)\). The squared sum of the heavy kernel over \(s\), after weighting by the actual \(w(t)\), therefore costs \(O(p^{19/8}\sqrt p)=O(p^{23/8})\). Only the initial completion was positive; the Fourier expansion is an exact complex identity inside the completed kernel.

For the omitted light pairs, \(H_{\mathrm{light}}(s,t)\ll\tau G^2\) pointwise on the true slopes \(s\ne0,1\). If \(g(Y)\le\tau\), fix \(s,C,D\), which determine at most one \(Y\) by Round 170. If \(g(D)\le\tau\), fix \(s,C,Y\), and the equation for \(D\) is
\[
 D^2+\bigl((1-s)CY-C-Y\bigr)D+sCY=0 .
\]
It has at most two roots. These pin bounds retain the uncut two weights. The true total mass over \(s\) is \(O(G^3)\) for each \(t\), so the light part costs \(O(\tau G^5)\) in squared slope norm and \(O(\tau G^6)=O(p^{23/8})\) after \(w\). Applying the triangle inequality across these terms and the already priced endpoint terms proves the displayed bound.

With the normalization of Rounds 168–169 this yields \(\mathcal P_1=O(p^{-1/8})\), hence \(O(p^{15/8})\) for the matching-number-one covariance contribution including its old \(O(p^{3/2})\) error. The target needs \(\mathcal P_1=O(p^{-1/2})\). For example, an \(O(p^2)\)-scale affine-energy bound with summably weighted level constants, covering levels down to a point where the remaining light terms fit the target, would give the target through this fourth-moment method. With the present pointwise light estimate that point would be \(\tau\le p^{-1/2}\), or one needs a stronger light estimate. The actual weighted action or the square-constrained physical correlation may allow a different improvement.

## The diagonal and a separate test for the full completed majorant

The full completed majorant \(P_s\) of [Round 166](ordinary-regular-character-collisions-166.md) equals the physical twisted kernel on \(t=s\), with endpoint repairs as above. Indeed the selected twisted factor is then \(g(sE)=g(A)\). In interior affine coordinates, for \(s\ne0,1\) the contribution of a pair \((Y,D)\) of square arguments is
\[
 g(Y)g(D)\,
 g\left(\frac{rD}{Y(s-b)}\right)
 g\left(\frac{rs}{s-b}\right)
\]
when \(b\in Q\), \(s\ne b\), and \(rs/(s-b)\ne1\). This comes from \(E=r/(s-b)\) and \(Y,D\ne1\), \(Y\ne D\). Completing the last restriction adds only the already priced \(x=0\) boundary. For the resulting positive majorant the two restored factors have exact joint Fourier phase
\[
 \sum_{\alpha,\beta}\omega(\alpha)\omega(\beta)
    (\alpha\beta)(r)\,\beta(D/Y)\,\alpha(s)\,
    \overline{\alpha\beta}(s-b),
\]
using \(\alpha\) for the factor at \(rs/(s-b)\). At \(s=b\) the last character is extended by zero, so this formula omits the pole for every pair of characters, including the trivial ones. The terms with \(\alpha=1\) or \(\beta=1\) have probability \(O(\kappa)\), as do terms with \(\alpha\beta\) belonging to any fixed bounded set of characters, by independence and \(\kappa=\|\omega\|_\infty\). Each such block is therefore \(O(\kappa G^2)=O(\sqrt p)\) pointwise, enough for \(O(p^{3/2})\) after squaring and applying \(w(s)\). This is a different expansion from the one-match Jacobi calculation. The remaining two-character average over \(r,b\) is open. The two-dimensional \(H_\alpha(s,t)\) energy proved above does not give the necessary diagonal estimate.
