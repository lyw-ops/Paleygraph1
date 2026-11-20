# Directional inverse cost with the exact diagonal and squared Gram fluctuation

This is a relaxed matrix control for the signed cofactor strategy. Use \(n\) even and a sequence \(k\equiv1\pmod4\) with \(a=k/n\) in a fixed compact subinterval of \((0,1/2)\). Write \(e=\mathbf1_k/\sqrt k\), \(c=\sqrt a\,e\), \(d_*=(1/2)+(1-\epsilon)/(2n)\). Choose any \(0<\delta=o(1)\). On the real cyclic space of length \(k\), choose two Fourier-invariant real subspaces of equal dimension \((k-1)/2\) orthogonal to \(e\), using disjoint symmetric sets of nonzero Fourier frequencies. Define a real symmetric circulant \(H\) with eigenvalues
\[
 a+\delta\quad\text{on } e,\qquad
 d+\sqrt a/2\text{ and }d-\sqrt a/2
 \quad\text{on the other two subspaces},\qquad
 d=\frac{kd_*-a-\delta}{k-1}.
\]
Then both \(H\) and \(G=H-cc^*\) are positive definite contractions for large \(n\). The diagonal of \(H\) is exactly \(d_*\) because it is circulant and its trace is \(kd_*\). Furthermore
\[
 \frac1k\|H-d_* I\|_{\rm HS}^2
   =\frac a4+O(1/k).
\]
This follows by summing the squared deviations of the displayed eigenvalues. For \(K'=\epsilon(2H-I-cc^*)\), one has the exact physical diagonal value \(K'_{ii}=-1/n\) and the local counting bound \(\|K'\|_{2\to2}\le1\). Indeed the marked-direction eigenvalue of \(\epsilon K'\) is \(a+2\delta-1\) and the others are \(2d-1\pm\sqrt a\). The determinant ratio is \(\delta/(a+\delta)\), which can tend to zero at any chosen rate even with the actual macroscopic squared fluctuation and diagonal constraints.

The matrices do not impose the physical Jacobi entries, the ambient projection or the actual optimizer support. The control only eliminates a directional bound inferred from these summary constraints. On the true independent columns one can use the directional spectral measure
\[
 \vartheta(B)=\|1_B(G)c\|_2^2,\qquad c=\mathbf1_{U'}/\sqrt n .
\]
The true ratio is \((1+\int\lambda^{-1}d\vartheta)^{-1}\). At \(\lambda>T^{-1/2}\), the inverse cost is at most \((k/n)\sqrt T=o(T)\) automatically. A sufficient actual-prime bound at small scales is, for some fixed \(\eta,\alpha>0\),
\[
 \vartheta((0,s])\ll s^{1+\eta} T^{1+\eta/2-\alpha}
 \qquad(0<s\le T^{-1/2}).
\]
Indeed the dyadic inverse sum over \(s=2^{-j}T^{-1/2}\) is bounded by a constant times \(T^{1-\alpha}\sum_j 2^{-j\eta}\). This is a source-specific criterion on the unmarked pure Gram, using the constant Fourier row. It does not give a prime bound on that measure.
