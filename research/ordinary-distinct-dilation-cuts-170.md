# Degeneracies in the physical and Jacobi forms of the different-ratio collision

Retain the actual \(g,w=g(1-g)\), physical mark, and square mask from [Round 169](ordinary-one-match-twisted-physical-169.md). Put \(G=\sum g=O(\sqrt p)\), \(m=p-1\), and \(L_z=\sum_Y g(Y)g(zY)\), so \(L_z\le G\), \(\sum_z L_z=G^2\). The required single-kernel squared scale is \(O(p^2)\) over the auxiliary slope for each \(t\), or \(O(p^{5/2})\) after the actual \(w(t)\) sum. All deletions estimated below are at the latter target scale. The \(4+4\) zero-match term is a separate problem.

## Selected-argument and within-copy collisions

At nonidentity slope \(s\), set \(E=A/s=CY/D\). From the exact displaced reciprocal dilation,
\[
 CY=DE,\qquad C+Y=D+sE+(1-s)DE .
\]
The latter identity follows by substituting \(A=sE\) in \((1-C)(1-Y)=(1-D)(1-A)\). The nonzero weight is \(g(C)g(Y)g(D)g(tE)\). Keep the true square mask and omit the already paid zero endpoints so that \(D,Y\ne 1\), \(s\ne1\). Each tuple determines at most one \(s\), since the coefficient \(E(1-D)\) is nonzero. It determines at most one original \(u,x,y\), by the physical formulas of Round 169.

At fixed \(s,D,E\), there are at most two ordered pairs \((C,Y)\), given by the roots with the displayed sum and product. At fixed \(s,Y,D\), the equation for \(C\) is
\[
 C\left(1-\frac{Y}{D}(s+(1-s)D)\right)=D-Y.
\]
If the coefficient and right side both vanish, \(Y=D\) implies \((1-s)(1-D)=0\), excluded here. Hence there is at most one \(C\), and the same argument at fixed \(s,C,D\) gives at most one \(Y\).

Write \(H_j(s,t;a)\) for the nonnegative raw physical sum restricted to argument \(j=a\), with \(j\in\{C,Y,D,E\}\). In each of the four restrictions one can sum one remaining variable with its own weight and use the preceding multiplicity bound, so \(H_j(s,t;a)\le 2G\). The bound also holds for the transformed factor \(g(tE)\) because \(t\ne0\). The total raw sum over \(s\) is at most \(G^3\) for each \(t\): \(C,Y,D\) determine \(E,s\), and \(g(tE)\le1\). Consequently
\[
 \sum_{s,a} H_j(s,t;a)^2\le 2G^4 .
\]
For two possibly different argument roles \(j,j'\), Cauchy bounds \(\sum_{s,a}H_j(s,t;a)H_{j'}(s,t;a)\) by the same upper. Thus all cross-copy collisions between the four argument lists, including across roles, can be removed at target scale, whether or not \(z=z'\). The same proof covers literal equalities involving the twisted argument \(tE\) in either copy, since multiplication by the fixed nonzero \(t\) permutes the argument labels in the Cauchy sum.

Under the retained restrictions \(D\ne Y,C\), \(E\ne Y,C\) follows from \(CY=DE\); the first pair of inequalities follows from \(Y=D\) forcing \(y=0\) or \(u=1\), and \(C=D\) forcing \(s=1\). The only possible within-copy repetitions are \(C=Y\) and \(D=E\). For either, two nonzero weighted variables determine the entire tuple and \(s\) (take \(C,D\) or \(D,Y\), respectively), giving total mass at most \(G^2\) over \(s\). As the total pointwise kernel is at most \(2G^2\) by the sum over \(D,E\), products of these repeated tuples with any other copy also cost at most \(O(G^4)\) at fixed \(t\).

## Exact two-linear Jacobi expansion

For a distinct variant, use the positive completion of the \(A=1\) boundary already paid in Round 169. For \(z\in Q\setminus\{1\}\), define two nonnegative functions \(A_{t,z},B_z\) on the displaced reciprocal variables \(y,d\in\mathbb F_p^\times\), with zero at \(-1\), by
\[
 A_{t,z}(y)=g((1+y)^{-1})g(tz(1+y)^{-1}),\qquad
 B_z(d)=g((1+d)^{-1})g(z(1+d)^{-1}).
\]
Their first norms are at most \(L_{tz},L_z\), and their squared second norms satisfy the same bounds. The reciprocal row is
\[
 C_{t,z}(u)=\sum_y A_{t,z}(y) B_z(y/u),\qquad
 u=U_z(s)=\frac{1-sz}{1-z}.
\]
Write \(\widehat A(\rho)=\sum_y A(y)\overline{\rho(y)}\), and likewise for \(B\). The masked row on the common slope is exactly
\[
 K_{t,z}(s)=\sum_\rho a_{t,z}(\rho)\rho(U_z(s)),\qquad
 a_{t,z}(\rho)=\frac{\widehat A_{t,z}(\rho)\widehat B_z(\bar\rho)
                +\widehat A_{t,z}(\rho\chi)\widehat B_z(\bar\rho\chi)}{2m}.
\]
Indeed \(u=y/d\) in the row Fourier transform, and the mask is \((1+\chi(u))/2\) off zero. Every character vanishes at zero, including the trivial character. The row on that excluded slope is zero. Completing \(s\) temporarily to all of \(\mathbb F_p\) adds at most \(2G^4\) to the fixed-\(t\) full positive squared mass, since the two added slopes \(0,1\) each have row sum at most \(\sum_z L_z=G^2\).

For \(z\ne z'\), write \(b=1/z\), \(b'=1/z'\). With \(x=(s-b)/(b'-b)\), the first row argument is \(c x\), where \(c=-(b'-b)/(b-1)\), and the second is \(c'(1-x)\), where \(c'=(b'-b)/(b'-1)\). Thus the completed \(s\)-sum in the two row expansion with characters \(\rho,\eta\) equals
\[
 \rho(c)\eta(c')J(\rho,\eta),\qquad
 J(\rho,\eta)=\sum_x\rho(x)\eta(1-x).
\]
There is no conjugation in the row product since the physical rows are real; conjugating a whole row would correspond to relabeling its Fourier character. By Parseval and Cauchy,
\[
 \sum_\rho |a_{t,z}(\rho)|\le\sqrt{L_{tz}L_z},
 \qquad
 \sum_{z,\rho}|a_{t,z}(\rho)|\le G^2.
\]
The trivial-trivial term has \(J(1,1)=p-2\); also
\(0\le a_{t,z}(1)\le L_{tz}L_z/m\), since it is the mean of the positive masked correlation. Its total absolute contribution over the distinct rows is at most \(p(G^3/m)^2=O(p^2)\). Every term with exactly one trivial character or with \(\rho\eta=1\) and both characters nontrivial has Jacobi size at most 1, costing at most \(G^4=O(p^2)\) in total. Thus the distinct-ratio squared criterion reduces to the sign-sensitive average of the remaining regular Jacobi terms under these exact row coefficients. The separate positive physical cuts above concern the physical expansion and must not be subtracted again from the Jacobi expansion.

As another sufficient partial cut, the collection where \(L_z\le H\), for fixed \(H>0\), has norm at most \(\sqrt H\,G^2\) over \(s\) at each \(t\) by Young and the slope parametrization. Use \(\|K_{t,z}\|_2\le L_{tz}\sqrt{L_z}\) and sum \(L_{tz}\). The same holds for \(L_{tz}\le H\) by the opposite Young bound. Thus these collections can be removed by norm comparison. This does not bound separately all cross-products touching those rows. The generic pointwise Jacobi bound on the regular frequencies gives only \(O(p^{5/2})\) at fixed \(t\), which remains too large by \(p^{1/2}\). Neither the regular average nor the mixed energy of the larger-overlap rows has been bounded here.

## The row-norm-only shortcut fails under the cap and autocorrelation alone

The gateway's proposed sufficient bound
\[
 \sum_t w(t)\left(\sum_z L_{tz}\sqrt{L_z}\right)^2=O(p^{5/2})
\]
cannot follow from the cap, \(g=|f|^2\), and the normalization alone. This control uses an auxiliary probability, not the actual optimizer. In \(Q=\langle b\rangle\) of order \(n\), let \(\nu\) be uniform on the \(2L\) characters of exponents \(\pm1,\ldots,\pm L\), with \(L=\lfloor n/(2\sqrt p)\rfloor\). It is even, vanishes at the trivial character, and \(n\max\nu=n\sum\nu^2=n/(2L)\sim\sqrt p\). With \(x=Lk/n\), the exact characteristic row is \(L^{-1}\sum_{j=1}^L\cos(2\pi xj/L)\). It converges uniformly on \(0\le x\le3/10\) to \(\sin(2\pi x)/(2\pi x)\) by the Riemann sum error bound for a uniformly Lipschitz integrand. The limit uses its continuous value at zero. Thus \(w(b^k)\) is bounded below by a fixed positive constant for \(1/5\le Lk/n\le1/4\), and \(g\) is bounded below for \(0\le Lk/n\le3/10\). The full lift of \(\nu*\check\nu\) has cap \(O(p^{-1/2})\).

Choose \(z=b^j\) and the summation variable \(Y=b^i\) with \(1\le i,j\le \lfloor n/(40L)\rfloor\). For the above choices of \(t\), all the exponents at \(Y,zY,tzY\) stay in the latter compact interval, with no wrap. Consequently \(L_z,L_{tz}\gg n/L\) on \(\gg n/L\) such \(z\)'s, for \(\gg n/L\) choices of \(t\). The displayed row-norm expression is \(\gg(n/L)^6\asymp p^3\). This rules out that sufficient bound with just those hypotheses, while leaving both the true distinct-ratio estimate and any property specific to the actual optimizer open.
