# A projection model with an actual fixed gap and a long marked return tail

This is a finite-dimensional family outside the prime problem. It tests what follows from exact sector projections, pointwise complementarity and true primary and secondary optimization alone.

Let \(n=2m^2\), \(m\ge4\). Choose sets \(A_*,B_*\) of sizes \(m,2m\) in an \(n\)-point set with \(A_*\cap B_*=\{0\}\). Put \(q=2m\), \(r=m\), \(F=q 1_{A_*}\), \(R=r 1_{B_*}\). Both have mass \(n\), and their only overlap is \(F_0R_0=n\), so \(f=F-\mathbf1\) and \(R-\mathbf1\) are orthogonal. Write \(C_*=(A_*\cup B_*)^c\) and take \(V_+\) to be the direct sum of \(\mathbb R f\) and a subspace of dimension \(n/2-1\) of the mean-zero vectors supported on \(C_*\). This is possible because \(|C_*|=n-3m+1\ge n/2\). Let \(V_-=(\mathbb R\mathbf1+V_+)^\perp\), and \(K=P_{V_+}-P_{V_-}\). Thus \(K^2=I-\Pi\), \(K\mathbf1=0\), and the centered ranks differ by one. Orthogonality to the additional mean-zero directions gives \(R-\mathbf1\in V_-\).

For any nonnegative \(F'\in\mathbf1+V_+\), the opposite row gives \(\langle F',R\rangle=n\), so \(F'_0\le n/r=q\). Analogously \(R_0\) is optimal in the opposite sector. If \(F'_0=q\), write \(F'=\mathbf1+t f+w\) with \(w\) in the extra subspace. Then \(w_0=0\) and \(q>1\) force \(t=1\). On \(C_*\), \(F'=w\ge0\) and \(w\) is mean-zero, so \(w=0\). Hence \(F\) is the unique actual optimum and the least-bulk-energy one. The normalized gap is \(q/\sqrt n=\sqrt2\).

On \(S=A_*\setminus\{0\}\), the pure opposite projection compresses to
\[
 C=I_S-\frac{1}{m}\mathbf1_S\mathbf1_S^*.
\]
Indeed the compression of the constant projection plus the projection on \(f\) equals \(\bigl(1/n+(q-1)/n\bigr)\mathbf1_S\mathbf1_S^*\), since \(\|f\|_2^2=n(q-1)\). The other \(V_+\) directions vanish on \(S\). Here \(x=q\mathbf1_S\) is an eigenvector of \(C\) with eigenvalue \(1/m\). The exact [exterior return identity](ordinary-exterior-mark-return-161.md) gives
\[
 \sum_{j>L}\langle e_0,D^j e_0\rangle=(m-1)(1-1/m)^L.
\]
For every growing \(T=o(m)\) and fixed \(b>0\) this is asymptotic to \(m\) at \(L=\lfloor bT\rfloor\), larger than the needed \(o(T)\) upper. The model preserves true optimization, exact reciprocity, the projection algebra and a fixed gap even for arbitrarily slowly growing times. It does not impose the circulant physical Jacobi entries, the physical diagonal, or the actual Picard orbit. In particular \(K_{00}=2(q-1)/n-(1-1/n)\) here. It cannot settle any eligible-prime case.
