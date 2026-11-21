# Affine chart for the actual cross-ratio

Let \(u\in Q\setminus\{1\}\), \(X=(1-vx)^{-1}\), \(Y=(1-vy)^{-1}\), and \(r_u(x)=(1-vux)/(1-vx)\). Observe
\[
 r_u(x)=u+(1-u)X,\qquad
 L(ux)=\frac{X}{u+(1-u)X}.
\]
Consequently \(r_u(y)/r_u(x)=t\) if and only if
\[
 Y=tX+\frac{u(t-1)}{1-u}.
\]
The maps on \(x,y\) therefore all fix the point \(1/v\), and the same chart conjugates the entire two-parameter family into the affine group. For \(t\ne1\), the slope \(t\) and intercept \(b=u(t-1)/(1-u)\) recover \(u=b/(b+t-1)\), so these parameters have no multiplicity. Impose \(u,t\in Q\setminus\{1\}\), \(\chi(1-t)=\rho\) for the favorable sector, and preserve the original domain of the five functions. In the \(X\)-chart the four physical arguments of \(f\) are
\[
  X^{-1},\quad Y^{-1},\quad uX^{-1}+1-u,\quad uY^{-1}+1-u.
\]
Thus \(f(t)\) multiplies a four-function correlation on the affine \(X,Y\) graph whose two transported factors depend on the same \(u=b/(b+t-1)\). The original physical square restrictions are \(\chi(1-X^{-1})=\chi(1-Y^{-1})=\rho\) (with \(X,Y\ne1\)), and all four physical \(f\)-arguments must be in \(Q\).

This derivation gives two checks on possible incidence arguments. First, uniform mixing over a genuinely three-parameter projective family would not directly apply to this shared-fixed-point family. Second, a graph incidence estimate with independent input weights in \(X,Y\) misses the \(u\)-dependent factors on both vertices. This chart leaves the favorable-sign upper open.

## Removing slope families with bounded fiber weight

For fixed \(u\ne1\) and \(t\ne0\), the relation \(r_u(y)=t\,r_u(x)\) gives an injective partial permutation \(x\mapsto y\) on the contributing physical set. With \(A_u(x)=F_0(ux)\overline{F_0(x)}\), Cauchy–Schwarz bounds the absolute subtotal at \(u,t\) by \(|f(t)|\|A_u\|_2^2\). If a family of slopes \(E_u\) satisfies \(\sup_u\sum_{t\in E_u}|f(t)|=O(1)\), then its absolute contribution is \(O(\sum_u\|A_u\|_2^2)=O(p)\) on the actual critical branch. The families may depend on \(p\) and on the actual row. In particular one may remove any fixed finite number of bounded-degree slope graphs in \(u\) with uniformly bounded fibers. This also gives a bound for the portion of the favorable sector selected by such a family. The remaining upper requires control across growing weighted families.
