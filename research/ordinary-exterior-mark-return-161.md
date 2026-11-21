# The marked exterior projection and its long return tail

Use the true least-bulk-energy optimum \(F=q e_0+E_S x\) of [Round 137](ordinary-bulk-spectrum-137.md), with sign \(\epsilon\) and actual positive bulk support \(S\). All inner products are counting. Let \(W=S^c\), including the physical mark, and let \(\Pi\) be the constant projection. The exact pure opposite-sector projection and its blocks are
\[
 P=\tfrac12(I-\epsilon K-\Pi)
   =\begin{pmatrix}C&B\\B^*&D\end{pmatrix}_{S,W}.
\]
Here \(K\) is real self-adjoint, \(K\mathbf1=0\) and \(K^2=I-\Pi\). In particular \(PF=0\). Write \(e_0\) also for the unit coordinate in \(W\).

## Exact exterior spectral measure at the physical mark

The two block equations are \(Cx=-qBe_0\) and \(B^*x=-qDe_0\). The actual complementary optimum \(R\) is zero on \(S\) and obeys \(PR=R-\mathbf1\). In particular \(B R|_W=-\mathbf1_S\). Since \(BB^*=C(I-C)\), the range of \(B\) is orthogonal to \(\ker C\). Thus \(\mathbf1_S\perp\ker C\), so \(A=2C+\mathbf1_S\mathbf1_S^*/n\) has the same kernel as \(C\). Least bulk energy now gives \(x\perp\ker C\) by Round 137. Also \(x\) is orthogonal to the \(1\)-eigenspace of \(C\), because \(B^*\) kills it and \(Cx=-qBe_0\). Similarly \(B\) kills the \(1\)-eigenspace of \(D\), and \(B^*x=-qDe_0\) gives \(e_0\perp\ker(I-D)\).

For \(0<\lambda<1\), \(B^*/\sqrt{\lambda(1-\lambda)}\) is a unitary identification from the \(\lambda\)-eigenspace of \(C\) onto the \((1-\lambda)\)-eigenspace of \(D\). The identities are \(BB^*=C(I-C)\), \(B^*B=D(I-D)\) and \(CB+BD=B\), and give both directions. Let \(\omega\) be the probability spectral measure of \(D\) at \(e_0\). On each interior eigenvalue,
\[
 \frac{\|\mathbf1_{\{\lambda\}}(C)x\|_2^2}{q^2}
    =\frac{1-\lambda}{\lambda}\,\omega(\{1-\lambda\}).
\]
The endpoint analysis above gives \(\omega(\{1\})=0\) and allows \(\delta=0\) to be included with zero weight. Thus
\[
 \frac{\|x\|_2^2}{q^2}
 =\int_{[0,1)}\frac{\delta}{1-\delta}\,d\omega(\delta)
 =\langle e_0,(I_W-D)^\dagger e_0\rangle-1,
 \qquad
 \frac{\langle x,Cx\rangle}{q^2}
 =D_{00}=\tfrac12+\frac{\epsilon-1}{2n}.
\]
The last equality uses the actual \(K_{00}=-1/n\). In the complementary compression the positive optimum also gives \((I_W-D)R|_W=\mathbf1_W\). These formulas hold at a fixed prime without approximation. In contrast to the affine forcing for \(A\), the exterior forcing for \(I_W-D\) is exactly the fixed coordinate \(e_0\) and its inverse occurs to the first power.

## An exact long-depth test for every fixed gap

For any integer \(L\ge0\),
\[
 \sum_{j>L}\langle e_0,D^j e_0\rangle
 =\int_{[0,1)}\frac{\delta^{L+1}}{1-\delta}\,d\omega(\delta)
 =\frac{\langle x,(I_S-C)^L x\rangle}{q^2}.
\]
Every return term is nonnegative since \(0\le D\le I\). The series at a fixed prime converges by \(\omega(\{1\})=0\). It is a sum for the actual adaptive exterior \(W\) with the original mark.

On a hypothetical fixed-gap sequence, [Round 160](ordinary-gap-marked-spectral-window-160.md) gives \(\|x\|_2^2\ge c nT\) at an admissible growing \(T\). By the exact energy identity and \(q^2=O(n)\), the part of \(\|x\|_2^2\) on \(\lambda>A_0/T\) for \(C\) is at most \(q^2 D_{00}T/A_0\). Choose fixed \(A_0\) large enough so the other part has size at least \(c nT/2\). For any fixed \(b>0\), take \(L=\lfloor bT\rfloor\). On \(0<\lambda\le A_0/T\), \((1-\lambda)^L\ge e^{-2bA_0}\) for large \(T\). Since \(q^2=O(n)\), the displayed tail is then \(\gg_b T\), with fixed-gap constants. In fact the contribution to the exterior inverse lever from \(1-A_0/T\le\delta<1\) alone is \(\gg T\).

A prime-uniform \(o(T)\) upper for this tail, for one admissible growing \(T\) and one fixed \(b>0\) on each hypothetical fixed-gap sign and floor, would rule out the ordinary fixed gaps. It suffices to bound the mark's inverse-weighted measure near \(1\) on its own adaptive exterior, not the full trace of the compression. Removing the constant projection does not assert that the individual spectral bands for \(C\) coincide with those for \(A\). No prime-uniform return upper follows from the exact energies or from convergence at each fixed prime.

## The capacity after deleting the marked coordinate

Let \(U=W\setminus\{0\}\), \(J=I-P\), \(H=E_U^*J E_U\), \(a=1-D_{00}\), and \(d=D_{U0}\). Thus \(I_W-D\) has blocks \(\bigl(\begin{smallmatrix} a&-d^*\\-d&H\end{smallmatrix}\bigr)\) with the mark first. Its positive Schur complement is
\[
 s=a-d^*H^\dagger d=\frac{1}{1+\|x\|_2^2/q^2}.
\]
Positivity gives \(d\in\operatorname{Ran}H\), and \(e_0\in\operatorname{Ran}(I_W-D)\) gives \(s>0\) and the reciprocal diagonal inverse formula even if \(H\) is singular. Write \(u=\mathbf1_U\) and \(r=R_0=n/q\). Since \(J\mathbf1=\mathbf1\), \(u\in\operatorname{Ran}H\) as well. Solving the \(U\) rows of \((I_W-D)R|_W=\mathbf1_W\) gives \(R|_U=H^\dagger(u+dr)\) up to a vector in \(\ker H\). The mark row becomes \(rs=1+d^*H^\dagger u\). Using \(\sum R=n\) now gives
\[
 n-\langle u,H^\dagger u\rangle=r^2s
 =\operatorname{dist}\bigl(\mathbf1,\operatorname{Ran}(J E_U)\bigr)^2.
\]
The distance identity uses \((J E_U)^*\mathbf1=u\) and \((J E_U)^*(J E_U)=H\). A lower bound \(n-\langle u,H^\dagger u\rangle\gg L_p n/T\) with \(L_p\to\infty\), for each hypothetical fixed gap and one admissible \(T\), would also exclude the gap, since \(r^2\asymp n\). This poses an unmarked subspace approximation question on the actual zero coordinates. The distance formula alone gives no such lower bound.
