# High-rank whole-row translations in the actual Jacobi sector

Use the genuine Fourier-minor ratio of [Round 162](ordinary-zero-set-leakage-162.md). Write \(Q=(\mathbb F_p^{\times})^2\), \(n=|Q|\), and
\[
 \Omega_\epsilon=\{1\}\cup\{x\in Q:\chi(1-x)=\epsilon\}.
\]
The actual column set \(U'\) is held fixed. Let \(k=|U'|\), and translate row-index sets by multiplication in \(Q\).

## Exact two-sector overlap

For \(h\in Q\setminus\{1\}\) set
\[
 E_h=\sum_{x\in\mathbb F_p}\chi\bigl(x(1-x)(1-hx)\bigr).
\]
Expanding the two indicator factors on \(Q\) gives
\[
 |\Omega_\epsilon\cap h^{-1}\Omega_\epsilon|
   =\frac n4+\frac{1-2\epsilon+2\epsilon\chi(1-h)}4+\frac{E_h}{8}.
\]
Indeed the indicator is \((1+\epsilon\chi(1-x)+1_{x=1})/2\), the one-sign sums on \(Q\) are \(-1\), and the product of the signs sums to \(-1+E_h/2\). The last sum follows by opening the square mask, evaluating the distinct-root quadratic sum as \(-1\), and excluding \(x=0\), which contributes 1 to that quadratic sum. The two extra marked terms give \(2+2\epsilon\chi(1-h)\), since \(h\) is square and \(p\equiv1\pmod4\). The cubic has distinct roots, so the standard elliptic curve point-count bound gives \(|E_h|\le2\sqrt p\). In particular the overlap is at most \(n/4+\sqrt p/4+5/4\), uniformly over both signs and all such \(h\).

Consequently, if \(k>n/4+\sqrt p/4+5/4\), each \(k\)-element row set in the sector is the only eligible set in its full translation orbit. Having a new eligible translate would put the original row set in a two-sector overlap exceeding that bound. In this high-rank regime a minor containing the constant row cannot be moved off it by translating its whole row set. No rank bound on the actual zero set places it below this threshold. This observation does not force any of those orbit weights to be large.

## What a one-row exchange would have to show

For a \((k-1)\)-element \(I\subseteq\Omega_\epsilon\setminus\{1\}\), put \(w(I,a)=|\det M_{I\cup\{a\},U'}|^2\) for \(a\notin I\), including \(a=1\). Denote by \(N\) the total weight omitting the constant row, and by \(B\) the total containing it. Then exact double counting gives
\[
 B=\sum_I w(I,1),\qquad
 kN=\sum_I\sum_{a\in\Omega_\epsilon\setminus(I\cup\{1\})}w(I,a).
\]
A useful exchange estimate at ranks comparable to \(n\) must therefore transfer aggregate replacement weight well above \((k/T)B\) to force \(N/(N+B)=\omega(1/T)\). The size and pair overlap of the actual sector alone cannot compare these non-translate determinant weights. No such aggregate estimate is claimed.

## The actual macroscopic Gram compression cannot be near-scalar

Write \(r=|\Omega_\epsilon|\), and let \(H'=E_{U'}^*J E_{U'}\) as in Round 162. The diagonal of \(H'\) is \(r/n=1/2+(1-\epsilon)/(2n)\). The entrywise square \(C=K\circ K\) of the actual real symmetric Jacobi operator satisfies
\[
 \|C-(1-1/n)\Pi\|_{2\to2}\le (1+\sqrt p)/n .
\]
This is the [squared-kernel mixing formula](astra-paired-96.md#mixing-of-the-actual-paired-matrix), from the same quadratic and cubic autocorrelation sums as above. In particular, on any set of \(k\) actual coordinates, with indicator \(b\),
\[
 \sum_{i,j\in U'} K_{ij}^2
   =\langle b,Cb\rangle
   =(1-1/n)k^2/n+O(k/\sqrt n).
\]
Subtracting the diagonal costs \(k/n^2\). In the off-diagonal of \(H'\), replace \(\epsilon K_{ij}/2\) by \((\epsilon K_{ij}+1/n)/2\). The cross term in its squared Hilbert–Schmidt norm costs \(O(k/n)\), since the sum of the \(K_{ij}\) over the block is \(\langle b,Kb\rangle=O(k)\). The square of the constant costs \(O(k^2/n^2)\). Thus
\[
 \frac1k\left\|H'-\frac rn I\right\|_{\rm HS}^2
  =\frac{k}{4n}+O(n^{-1/2}).
\]
This estimate holds for arbitrary adapted \(U'\), whether or not its columns are independent. In particular, at any macroscopic \(k/n\) the operator norm differs from the scalar matrix by at least \(\tfrac12\sqrt{k/n}-O(n^{-1/2})\). If \(k/n\ge1/4+c\) with fixed \(c>0\), this exceeds \((r-k)/n\) for sufficiently large primes, since \(r/n=1/2+O(1/n)\). Therefore the proposed sufficient bound based on simultaneous scalar operator control and rank deficit cannot work in that regime. A directional estimate for the constant-row leverage or a comparison of actual exchange weights remains possible.

## Actual signed cofactor mass for one-row replacement

For each \((k-1)\)-set \(I\subseteq\Omega_\epsilon\setminus\{1\}\), take the cofactor vector \(v_I\) for adding a last row to \(M_{I,U'}\). Then with \(g_I=M E_{U'}v_I\), \(w(I,a)=|g_I(a)|^2\), including \(g_I(a)=0\) for \(a\in I\). Rank-deficient \(I\) simply has zero cofactor vector. Expanding the actual Jacobi sector mask gives
\[
 \sum_{a\in\Omega_\epsilon\setminus(I\cup\{1\})}w(I,a)
 =\tfrac12\big(\|v_I\|_2^2+
                 \epsilon\langle E_{U'}v_I,K E_{U'}v_I\rangle
                 -|g_I(1)|^2\big).
\]
The middle term is real. The constant-row contribution is subtracted only with coefficient one half because the sector indicator already includes its half correction. This is an explicit signed quadratic sum in the actual cofactor Fourier polynomial on the genuine columns.

If \(G=H'-\mathbf1_{U'}\mathbf1_{U'}^*/n\), then \(\sum_I v_I v_I^*=\operatorname{adj}(G)\). For an arbitrary complex row \(z\), the quadratic form of that sum at \(z\) is the increase \(\det(G+z^*z)-\det G\) by Cauchy–Binet. This proves the identity and shows that summing without an additional cofactor estimate simply recovers the original inverse. At the actual columns \(G\) is positive definite because \(H'\) is and \(d_U^2>0\). A useful next estimate must quantify the signed replacement mass for the actual cofactor family, rather than only the volume of the spectral sector.
