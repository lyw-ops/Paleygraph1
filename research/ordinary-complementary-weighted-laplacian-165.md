# The actual centered Gram with a positive kernel vector

Use the true complementary interpolant of [Round 164](ordinary-cofactor-complementary-interpolant-164.md), including its nonnegative coefficients \(w\) on the chosen actual independent zero columns \(U'\). Counting norms are used. Write \(L=M_{\Gamma,U'}\), \(G=L^*L\), \(c=\mathbf1_{U'}/\sqrt n\), \(r=n/q\), and \(s=\mathbf1_\Gamma/\sqrt{|\Gamma|}\). Set
\[
 b=L^*s,\quad m_*=r\sqrt{|\Gamma|/n},\quad
 G_0=L^*(I-ss^*)L=G-bb^*,\quad
 c_0=c+\frac{\langle w,c\rangle}{m_*}b.
\]
All vectors in these formulas can be taken real on the column space, since the sector is inversion invariant. The row formulas in complex coordinates give the same result with the indicated Hermitian transposes. For sufficiently large primes \(|\Gamma|>0\). Since \(Lw=-m_*s\) and \(L\) is injective, \(\ker G_0=\mathbb R w\) on real coefficients, and \(c_0\perp w\).

## Exact centered inverse cost and the physical mark

The minimum of \(\|h\|^2\) subject to \(L^*h=c\) is \(\langle c,G^{-1}c\rangle\). Such a vector must have \(\langle s,h\rangle=-\langle w,c\rangle/m_*\), by the equation on \(w\). Subtracting this constant row leaves the centered equation with source \(c_0\). Thus
\[
 \langle c,G^{-1}c\rangle
 =\frac{(q-1)^2}{|\Gamma|}+\langle c_0,G_0^\dagger c_0\rangle.
\]
This is the same centered energy as the actual identity of Round 164, with new coordinate structure in the centered operator. In particular it is sufficient to control the last cost by \(o(T)\) on every fixed-gap sequence in the admissible growing marked window.

Put \(P_\epsilon=(I+\epsilon K-\Pi)/2\), the pure physical sector projection, \(b_0=E_{U'}^*P_\epsilon e_0\), and \(d=(P_\epsilon)_{00}=|\Gamma|/n\). Then
\[
 G_0=E_{U'}^*\left(P_\epsilon-\frac{P_\epsilon e_0e_0^*P_\epsilon}{d}\right)E_{U'},
 \qquad
 c_0=\frac1{\sqrt n}\left(\mathbf1_{U'}+\frac{q-1}{d}b_0\right).
\]
The operator in parentheses is the projection onto the pure sector with physical mark zero. The true entry cap gives \(b_{0,i}=O(n^{-1/2})\), so \(c_{0,i}=O(n^{-1/2})\). Thus the centered source is a definite combination of the uniform column source and the actual marked Jacobi column, and annihilates the positive complementary coefficients.

## Elimination and a true signed quadratic form

If \(A=\{i:w_i>0\}\) and \(B=U'\setminus A\), the \(B\)-block \(G_{0,BB}\) is positive definite when nonempty. Otherwise a nonzero kernel vector could be supported on \(B\), contradicting the exact kernel. Eliminate it by the Schur complement
\[
 Q_A=G_{0,AA}-G_{0,AB}G_{0,BB}^{-1}G_{0,BA},\qquad
 d_A=c_{0,A}-G_{0,AB}G_{0,BB}^{-1}c_{0,B}.
\]
The exact cost is
\[
 \langle c_0,G_0^\dagger c_0\rangle
 =\langle c_{0,B},G_{0,BB}^{-1}c_{0,B}\rangle+
   \langle d_A,Q_A^\dagger d_A\rangle .
\]
The formula follows by solving the two rows and pairing with the source, which annihilates the kernel. The empty block requires no debit. The kernel of \(Q_A\) is exactly the span of \(w|_A>0\). In particular conjugation by \(\operatorname{diag}(w|_A)\) gives a real symmetric matrix of zero row sums with the ordinary squared-difference quadratic form, retaining the signed off-diagonal coefficients. Neither the elimination cost nor the centered signed form has an available prime-uniform lower coercivity estimate.

Before elimination a useful local comparison follows directly from the physical entries. Write \(D_w=\operatorname{diag}(w)\). For real \(z\),
\[
 z^*D_wG_0D_wz
 =-\sum_{i<j}(G_0)_{ij}w_iw_j(z_i-z_j)^2.
\]
For \(i\ne j\) one has \((G_0)_{ij}=\epsilon K_{ij}/2+O(1/n)\). If \(z\) is supported where \(w_i\ge H>0\), replacing the off-diagonal coefficient by \(\epsilon K_{ij}/2\) in this expression costs \(O(H^{-1}\|D_wz\|_2^2)\). In fact \(\sum_{i<j}w_iw_j(z_i-z_j)^2\le (\sum_iw_i)\sum_iw_i z_i^2\), and \(\sum_iw_i=n-r\). This controls the two rank corrections on high complementary weights with their actual support. A lower estimate for the signed Jacobi differences and a transfer through low weights and zero coefficients remain open.

## A relaxed control retaining a positive complementary interpolant

The exact positive kernel structure also has a limitation without physical entries. Use the real circulant construction of [Round 164](ordinary-gram-directional-control-164.md) with \(a=k/n\) in a compact subinterval of \((0,1/2)\), and let \(G\) have eigenvalue \(\delta=o(1)\) on \(e=\mathbf1_k/\sqrt k\). Let \(z\) be a normalized real Fourier cosine in the larger-eigenvalue subspace, so \(z\perp e\), \(\|z\|_\infty\le\sqrt{2/k}\), and \(Gz=\lambda_+z\) with \(\lambda_+=1/2+\sqrt a/2+o(1)>a\). Fix \(\alpha>1\), set \(q=\alpha\sqrt n\), \(r=n/q\), and take \(m=|\Gamma|=n/2+O(1)\). Define
\[
 w=\frac{n-r}{k}\mathbf1_k+\tau z,\qquad
 \tau^2=\frac{r^2m/n-\delta(n-r)^2/k}{\lambda_+}.
\]
It has mean sum \(n-r\) and \(w^*G w=r^2m/n\). For sufficiently large \(n\), \(\tau^2>0\) and \(w>0\): it suffices that \(2\tau^2<(n-r)^2/k\), which holds from \(\alpha^2\lambda_+>a\). Its coordinates are bounded independently of \(n\), below the true normalized scale \(r\) eventually.

Choose an isometric embedding into \(\mathbb R^m\) mapping \(G^{1/2}w/\|G^{1/2}w\|\) to \(-\mathbf1_m/\sqrt m\), and let \(L\) be this embedding composed with \(G^{1/2}\). Then \(L^*L=G\) and \(Lw=-r\mathbf1_m/\sqrt n\) exactly, with a strictly positive interpolant and the correct source and mark scaling. The diagonal and squared Gram fluctuation from Round 164 are also unchanged. Nevertheless \(\langle c,G^{-1}c\rangle=a/\delta\), so the centered part of the splitting diverges at an arbitrarily prescribed rate. This model does not realize the Jacobi Fourier entries or the adaptive true support. It isolates the need for an arithmetic bound on the centered signed operator beyond the interpolant alone.
