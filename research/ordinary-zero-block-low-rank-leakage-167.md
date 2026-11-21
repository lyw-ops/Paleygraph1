# Low-rank elimination and a basis-independent positive-support split

Use the true centered marked compression \(G_0\), source \(c_0\), positive complementary support \(A=\{w>0\}\), and actual independent extension \(U'=A\cup B\) of [Round 165](ordinary-complementary-weighted-laplacian-165.md). All norms are counting. Let \(G_B=G_{0,BB}\), positive definite for nonempty \(B\), \(b=|B|\), and \(P_s=\mathbf1_{(0,s]}(G_B)\) with \(0<s<1/2\).

## Actual low-spectrum dimension and elimination

The physical squared-Jacobi mixing bound of [Round 96](astra-paired-96.md#mixing-of-the-actual-paired-matrix) applies on these actual adaptive columns:
\[
 \|K_{BB}\|_{\rm HS}^2=(1-1/n)b^2/n+O(b/\sqrt n).
\]
Also \(G_B-\tfrac12 I_B=\tfrac\epsilon2K_{BB}-\Pi_{BB}/2-b_{0,B}b_{0,B}^*/d\) with the genuine marked vector \(b_0\) of Round 165 and fixed \(d\asymp1\). The two latter terms have combined Hilbert–Schmidt norm \(O(b/n)\), by actual entry estimates. Using \(\|K_{BB}\|_{\rm HS}=O(b/\sqrt n)\), the squared norm is consequently
\[
 \|G_B-\tfrac12 I_B\|_{\rm HS}^2=\frac{b^2}{4n}+O(b/\sqrt n).
\]
Thus uniformly on all actual basis extensions,
\[
 \operatorname{rank}P_s\le
 \frac{b^2/(4n)+O(b/\sqrt n)}{(1/2-s)^2}.
\]
In particular at \(s=T^{-1/2}\) on a growing window the rank is
\((1+O(T^{-1/2}))b^2/n+O(b/\sqrt n)\) as an upper. This does not bound the overlap of the true source \(c_{0,B}\) with its low eigenspace.

Set \(X=G_{0,AB}\), \(Z=XG_B^{-1/2}\). Since \(0\le G_0\le I\), its squared \(B\)-block gives \(Z^*Z\le I_B-G_B\). Hence the exact Schur self-energy decomposes into two positive terms
\[
 XG_B^{-1}X^*=ZP_sZ^*+Z(I_B-P_s)Z^* .
\]
The first is a contraction of rank at most the above dimension. On \(A_H=\{w\ge H\}\), the second has quadratic bound \(O(b/(Hs))\) times the squared counting norm, since \(|A_H|\le n/H\) and \(\|G_{0,BA_H}\|_{\rm HS}^2=O(b|A_H|/n)\). These are bounds on different parts of the actual transfer. They replace a bound involving the smallest eigenvalue of the entire \(B\)-block by the specifically identified low-rank debit and a high-spectrum bound. The low-rank term can still carry the full source, and the \(b/(Hs)\) bound only gives a gain in the stated parameter range.

For the actual Schur source correction, its low part
\[
 ZP_sG_B^{-1/2}c_{0,B}
\]
has squared counting norm at most the actual directional inverse cost of \(G_B\) on \((0,s]\), by \(\|Z\|\le1\). The high part can be bounded by the same argument with the high inverse cost. A small Euclidean norm is still insufficient to drop this vector in the inverse of \(Q_A\) near zero.

## Eliminating the positive support first

Let \(P_0=P_\epsilon-P_\epsilon e_0e_0^*P_\epsilon/d\) be the genuine mark-zero sector projector and write \(a_i=P_0 e_i\). Let \(\mathcal A=\operatorname{span}\{a_i:i\in A\}\). Its Gram matrix \(G_{0,AA}\) has just the kernel vector \(w|_A\), by the full nullspace identity and \(w_B=0\). In the real ambient image space let \(h\) be the minimal norm vector satisfying \(\langle a_i,h\rangle=c_{0,i}\) on \(U'\). Its squared norm is the centered inverse cost. The unique minimal solution of just the constraints on \(A\) is \(h_A=P_{\mathcal A}h\) and has squared norm \(c_{0,A}^*G_{0,AA}^\dagger c_{0,A}\). The remaining constraints have columns
\[
 r_i=(I-P_{\mathcal A})a_i,\qquad
 c_i'=c_{0,i}-\langle a_i,h_A\rangle\quad(i\in B).
\]
For a full-span extension these residual columns are independent. Their Gram is \(G_B-G_{0,BA}G_{0,AA}^\dagger G_{0,AB}\), positive definite when nonempty. Consequently
\[
 c_0^*G_0^\dagger c_0
 =c_{0,A}^*G_{0,AA}^\dagger c_{0,A}
   +(c'_B)^*\bigl(G_B-G_{0,BA}G_{0,AA}^\dagger G_{0,AB}\bigr)^{-1}c'_B.
\]
The two debits in this order are individually independent of the chosen true extension \(B\) while \(A\) is fixed. The second is \(\|h-h_A\|_2^2\), on the quotient of the full actual span by \(\mathcal A\). To verify extension invariance, any genuine column in \(U\) is a linear combination in a full-span basis of the \(JE_i\). Centering gives the same linear combination for \(a_i\). The coefficient relation for \(c_{0,i}\) is also preserved, since \(c_{0,i}\) is evaluation of \(JE_i\) against \((\mathbf1+(q-1)P_\epsilon e_0/d)/\sqrt n\) in the range of \(J\). The full centered Gram span is therefore fixed for actual full-span extensions and so is the representer \(h\).

A different basis can redistribute the zero-first debits, but this quotient debit cannot be removed by choosing a different basis on the same true \(A\). The original target still requires source-weighted control on at least these actual components, or a different argument excluding fixed gaps.
