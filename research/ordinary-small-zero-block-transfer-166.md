# Quantitative elimination of a small zero-coefficient block

Use the precise centered physical compression \(G_0\), source \(c_0\), and actual complementary coefficients \(w\) of [Round 165](ordinary-complementary-weighted-laplacian-165.md). Write \(A=\{w>0\}\), \(B=U'\setminus A\), \(b=|B|\), and let \(Q_A,d_A\) be the actual Schur matrix and source. The norms below are counting. Fix \(0<\eta<1\) and assume
\[
 b\le (1-\eta)n/\sqrt p .
\]
This condition is on the actual selected basis. No estimate forcing this cardinality on every true fixed-gap sequence is assumed.

The exact physical formula gives, uniformly on the actual columns,
\[
 (G_0)_{ii}=\tfrac12+O(1/n),\qquad
 |(G_0)_{ij}|\le\sqrt p/(2n)+O(1/n)\quad(i\ne j),\qquad
 |(c_0)_i|=O(n^{-1/2}).
\]
Indeed \(G_0\) removes the constant projection and the one actual pure-sector marked vector, whose entries are \(O(n^{-1/2})\) away from the mark. All columns in \(U'\) are unmarked. Gershgorin therefore bounds \(G_{0,BB}\ge(\eta/4)I_B\) for all sufficiently large primes under the displayed size condition. For empty \(B\) all these debits are zero. The genuine inverse cost on this block obeys
\[
 D_B=\langle c_{0,B},G_{0,BB}^{-1}c_{0,B}\rangle
       =O_\eta(b/n)=O_\eta(n^{-1/2}).
\]

## Retaining the actual Schur source

Write \(q_A=c_{0,A}-d_A=G_{0,AB}G_{0,BB}^{-1}c_{0,B}\). Since \(0\le G_0\le I\), its squared \(B\)-block gives
\[
 G_{0,BA}G_{0,AB}\le G_{0,BB}-G_{0,BB}^2.
\]
It follows directly that
\[
 \|q_A\|_2^2\le D_B-\|c_{0,B}\|_2^2\le D_B,
 \qquad \|q_A\|_\infty=O_\eta(b/n).
\]
The latter follows by pairing each off-diagonal block row of second norm \(O(\sqrt{b/n})\) with \(G_{0,BB}^{-1}c_{0,B}\). Both \(q_A\) and \(c_{0,A}\) annihilate \(w|_A\), since \(G_{0,BA}w|_A=0\). Consequently the correction's inverse cost on the positive spectral part of \(Q_A\) above any cutoff \(s>0\) is at most \(D_B/s\). This controls the transfer at those scales, for example by \(o(T)\) at \(s=T^{-1/2}\) in an admissible growing window with \(T\to\infty\). No inference for arbitrarily small positive eigenvalues follows.

## Effect on the actual high-weight signed form

Let \(A_H=\{i\in A:w_i\ge H\}\). The actual mass sum \(\sum w_i=n-r\) gives \(|A_H|\le n/H\). For every vector \(\xi\) supported in \(A_H\), the Schur quadratic debit obeys
\[
 \langle \xi,G_{0,AB}G_{0,BB}^{-1}G_{0,BA}\xi\rangle
 \le O_\eta(b/H)\|\xi\|_2^2 .
\]
Use \(\|G_{0,BA_H}\|_{\rm HS}^2\ll b|A_H|/n\) and the established inverse bound. Thus if \(z\) is supported on \(A_H\), one may apply the exact signed Jacobi squared-difference formula of Round 165 to \(\xi=\operatorname{diag}(w)z\) with total relative quadratic error \(O_\eta((1+b)/H)\) for the rank corrections and Schur elimination together. The full actual coefficient vector \(w\) remains in the difference form, including edges to low weights. A signed lower bound there, a passage to the required test source, and the small spectrum below the transfer cutoff remain open.

The same argument applies to the combined elimination set \(C=B\cup\{i:0<w_i<H\}\) if \(|C|\le(1-\eta)n/\sqrt p\) and \(A_H\ne\varnothing\). Eliminate this block jointly. Its inverse debit is exactly the sum of the separate zero and low-weight debits from successive Schur elimination, by solving those block equations. All error bounds then hold with \(|C|\) in place of \(b\), retaining only the true high-weight Schur block. An applicable bound on \(|C|\) across fixed-gap sequences is also open.
