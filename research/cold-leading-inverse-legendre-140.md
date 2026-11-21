# The marked leading pure Jacobi inverse line is a Legendre trace

Use \(G=\mathbb F_p^{\times2}\), \(n=|G|\), the position sign \(s(x)=\chi(1-x)\), and the actual Jacobi seed \(S=2\sqrt n\,Ke_0\). On the original cold square take the first Taylor monomial of the pure derivative, with the physical mark retained:
\[
 D^{\rm lin}_{ii}=S_i/(2\sqrt{t_i}),\qquad t_0=n,\quad t_i=t\ (i\ne0).
\]
Use the same square-root branch and inverse Fourier normalization as in the [actual position kernel](cold-position-kernel-139.md). Put \(a=1/\sqrt{tn}\) and \(b=(a-1/n)/n\). The convolution row of \(D^{\rm lin}\) is \(a s(x)+b\) at every position. Since \(S_0=-2/\sqrt n\), the change in the marked derivative from the bulk prescription is \(a-1/n\), whose inverse Fourier row is the constant \(b\).

Define the extended Legendre trace by
\[
 A_p(\lambda)=-\sum_{u\in\mathbb F_p}\chi\bigl(u(u-1)(u-\lambda)\bigr).
\]
For \(\lambda\ne0,1\) this is the elliptic curve Frobenius trace, and \(A_p(1)=1\). Let \(\ell^{\rm lin}(x)\) be the \((x,x^{-1})\) entry of \((KD^{\rm lin})^2\). For \(x\in G\setminus\{1\}\), the exact formula is
\[
 \boxed{\displaystyle
 \ell^{\rm lin}(x)=-a^2\bigl(A_p(-1/x)+s(x)\bigr)
         -2ab\,s(x)\bigl(1+A_p(x)/2\bigr)-b^2s(x).}                 \tag{1}
\]
The row with \(x=1\) is zero. In particular at \(x=-1\) the first term of (1) is \(-a^2(1+\chi(2))\). This value can vanish even though its family has a local singularity.

To prove the formula, the term of degree \(a^2\), after removing the outer \(s(x)\), is the sum over \(z\in G\) of \(\chi(f_x(z))\), where \(f_x(z)=(z-1)(z-x)(z-x^{-1})\). The product of roots is one and the root set is invariant under inversion. Thus \(f_x(1/z)=-f_x(z)/z^3\), so the two full nonzero sums obtained by inserting the square indicator are equal. As \(\chi(f_x(0))=1\), the sum over \(G\) is the full cubic character sum minus one. The affine change \(z=1+(x-1)u\) gives the Legendre parameter \(-1/x\) and introduces the scalar \(s(x)\). Multiplication by the outer \(s(x)\) gives the first term. For each term linear in \(b\) use \(\sum_{z\in G}s(z)s(x/z)=-1-A_p(x)/2\). Inversion of \(z\) gives the same value for \(\sum_z s(z)s(zx)\). The constant term uses \(\sum_z s(z)=-1\). These calculations apply at \(x=-1\) with the extended character trace at the singular parameter. [The quadratic sign convolution](paired-legendre-cubic-116.md#conversion-to-a-restricted-legendre-family)

The rank-two Legendre local system pulled back by \(x\mapsto-1/x\) has nontrivial unipotent inertia at \(x=-1\), because the map is étale there and sends that point to the single unipotent Jordan block at \(\lambda=1\). The remaining functions in (1) are lisse near \(x=-1\) in their displayed trace realizations. Thus the leading pure-seed term has a genuine nearby local-system contribution there even with its exact mark. Modifying only the value at \(x=-1\) cannot make this realization lisse. Restricting to squares by a degree-two étale pullback does not remove the singularity. [Katz, Legendre local monodromy](https://web.math.princeton.edu/~nmk/mellin324book.pdf)

This identifies the collision for the degree-two pure-seed comparator. Its contribution is subtracted in the actual square difference. The formula gives neither its survival in the mixed nonseed words nor a physical lower on the full difference. In the actual inverse-line cohomological estimate, \(H_c^2=0\) still follows from the fixed nontrivial inertia at \(z=1\) when \(x=-1\). The collision at \(z=-1\) concerns variation in the parameter \(x\) and does not undo that vanishing.

For two general spatial rows \(d_1,d_2\), the coordinate \(u=x/z\) rewrites the actual inverse-line kernel as \(s(x)\sum_{u\in G}s(x/u)d_1(u)d_2(x^2/u)\). At the collision \((x,u)=(-1,1)\), both Kummer prefactors are lisse with special trace \(\chi(2)\), and \(x\mapsto x^2\) is étale there. Thus the local calculation to test next is the multiplicative convolution collision at \(u=1\) with parameter \(x^2\), with the displayed Kummer prefactors retained in the global sum.
