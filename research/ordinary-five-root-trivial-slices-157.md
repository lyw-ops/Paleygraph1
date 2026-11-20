# Trivial finite-root factors in the completed favorable kernel

Use the true five lifted weights \(w_Tw_Uw_Vw_{U'}w_{V'}\) from [Round 156](ordinary-sign-selective-completion-156.md), with \(\kappa=\max w=O(p^{-1/2})\). Write \(\beta=V/U\), \(C=U'/V'\), \(\alpha=U/U'\), \(\delta=T/U'\) and \(L=(U/V)/(U'/V')\). Fourier variable names below are multiplicative characters of the full field, with all characters extended by zero at zero.

In the fixed-slope formula of Round 156 change \(y=t(z+1)-1\) and expand the slope factor \(f(t)=\sum_Tw_TT(t)\). For \(t\ne0,1\) use the half-sums of \(1,\chi(t)\) and \(1,\rho\chi(1-t)\), and \(\chi(1-t)=\chi(z-y)\chi(z+1)\). With \(q\) indicating the slope lift and \(s\) indicating the last sign factor, the \(z,y\) kernel is
\[
 \sum_{z,y}\beta(z)(\alpha\bar\delta\chi^{q+s})(z+1)\,
       C(y)(\delta\chi^q)(y+1)\,\chi(z-y)^s .
\]
Here \(s=0\) omits the last factor entirely. The \(s=0\) diagonal \(t=1\) is reinstated in this formula and removed at \(O(p)\) after assembling the true weights, using the physical diagonal estimate. For \(s=1\) it vanishes. The \(u\)-factor in each case is \(J((V/V')\chi^i,L)\), \(i=0,1\). For \(s=0\) the two-variable kernel is the product of two Jacobi sums with prefactor \(\beta(-1) C(-1)\).

Now set \(s=1\), \(D=\delta\chi^q\), \(A=\alpha\bar\delta\chi^{q+1}\), so \(AD\chi=\alpha\), and denote its kernel by \(\mathscr K\). All four slices on which one of \(\beta,A,C,D\) is trivial can be removed at total absolute cost \(O(p)\) for each choice of \(q,i\). This cost refers to the sum over the true five weights, including the outer \(u\)-factor.

For example if \(\beta=1\), complete the inner \(z\)-sum by translating \(z+1\) and subtracting \(z=0\). With \(y+1\ne0\) on its effective support, this gives exactly
\[
 \mathscr K
 =J(A,\chi)\,C(-1)J(C,\alpha)-(C\chi)(-1)J(C\chi,D).
\]
The exceptional \(p\)-size second Jacobi factor in the product requires \(C=\alpha=1\), which together with \(\beta=1\) means \(U=U'=V=V'\). Its weight is \(O(\kappa^3)\), and the kernel is at most \(O(p^{3/2})\) on this event. An exceptional outer Jacobi factor similarly forces \(V/V'=\chi^i\) and \(L=1\). Together with \(\beta=1\), these have weight \(O(\kappa^3)\). Even after multiplying by the worst \(O(p)\) outer factor, the combined exceptional weight costs \(O(p)\). On the rest of this slice the kernel is \(O(p)\), the outer factor at most \(\sqrt p\), and the slice has weight \(O(\kappa)\), again costing \(O(p)\).

The \(C=1\) case swaps \(z,y\) and the two pairs of root characters. For \(A=1\), simultaneously reflect \(z\mapsto -1-z\), \(y\mapsto -1-y\) so it is the root-zero trivial character in the first pair. This introduces only unit scalars, since \(\chi(-1)=1\). The possible \(p\)-size second Jacobi factor now requires \(D=1\) and \(\beta C\chi=1\); together they force \(T=U\chi^{q+1}\), \(U'=U\chi\) and \(V'=V\), again three constraints. The outer exceptional event together with \(A=1\) likewise fixes three of the independent lifted variables after conditioning on the others. The case \(D=1\) uses both symmetries. These bounds use absolute contributions and so hold even after partitioning overlap between the four slices.

The two trivial-at-infinity slices are also removable. Invert \(z,y\) simultaneously; they are both nonzero in the kernel. This replaces \(\beta,C\) by \((\beta A)^{-1}\chi,(CD)^{-1}\chi\), keeps \(A,D\), and preserves the quadratic diagonal factor. The new first and third factors are trivial when \(T=V\chi^q\) and \(T=V'\chi^{q+1}\), respectively. If both are trivial and \(\alpha=1\), there are again three independent constraints. The outer principal event together with either displayed condition likewise fixes three variables. The preceding \(O(p)\) bounds therefore apply to the two infinity slices.

This removes only these six exact trivial-root contributions. On the actual short block the assembled \(\chi(1-t)\)-twisted complete sum differs from \(\rho\) times the assembled untwisted sum by \(O(p)\), because their difference uses only the wrong sector and that sector has the pin bound of [Round 154](ordinary-lift-and-gauss-kernel-154.md). The genuinely coupled regular sum still needs a prime-specific signed estimate.
