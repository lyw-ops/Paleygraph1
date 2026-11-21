# Corrected support and leakage test for the unmarked distance

Use the true least-bulk-energy optimizer \(F=q e_0+E_S x\), its complementary optimizer \(R\), the set \(U=(S\cup\{0\})^c\) of genuine zero coordinates, and \(J=I-P\) from [Round 161](ordinary-exterior-mark-return-161.md). Let \(H=E_U^*J E_U\), \(u=\mathbf1_U\), and \(W=U\cup\{0\}\). Norms are counting unless stated otherwise.

## Exact witness space and the exterior-only restriction

Orthogonality to \(\operatorname{Ran}(JE_U)\) inside \(\operatorname{Ran}J\) means vanishing on \(U\). Thus the correct space is
\[
 \mathcal V=\operatorname{Ran}(J)\cap\{y:y_U=0\},
 \qquad \operatorname{supp}y\subseteq S\cup\{0\}\quad (y\in\mathcal V).
\]
This is the marked interior, while the exterior \(W\) is the support of the complementary row. Interchanging them in a trial-vector bound can even remove the true witness \(F\).

For every \(y\in\mathcal V\), true complementarity gives
\(\langle\mathbf1,y\rangle=\langle JR,y\rangle=R_0y_0\).
If also \(y_0=0\), then \(F\pm t y\) stay in the pinned nonnegative face for sufficiently small \(|t|\), since \(F>0\) at every point of \(S\cup\{0\}\). Least energy and fixed mark imply \(\langle F,y\rangle=0\). Therefore
\[
 \operatorname{proj}_{\mathcal V}\mathbf1
    =\frac{n}{\|F\|_2^2}F,
 \qquad
 \operatorname{proj}_{\mathcal V}J e_0
    =\frac{q}{\|F\|_2^2}F .
\]
In fact restricting coefficients to \(W\) produces only this one witness direction. If \(z=E_W z_W\) and \((Jz)_U=0\), then \(Jz\in\mathcal V\) is orthogonal to all elements of \(\mathcal V\) of mark zero, since \(\langle Jz,y\rangle=z_0 y_0\) on that space. Thus \(Jz\) is proportional to \(F\). Taking \(z=e_0-E_U H^\dagger E_U^*J e_0\) produces the nonzero multiple displayed above. An exterior-only exact trial is algebraically possible, but searching for a different direction there gives no new test.

## A signed transfer from a near mask

For arbitrary real \(y\in\operatorname{Ran}J\) let \(\ell=E_U^*y\). Then \(\ell\in\operatorname{Ran}H\). The unique orthogonal projection from \(y\) onto \(\mathcal V\) removes \(JE_U H^\dagger\ell\), of squared norm \(\langle\ell,H^\dagger\ell\rangle\). Hence with \(d_U=\operatorname{dist}(\mathbf1,\operatorname{Ran}(J E_U))\),
\[
 d_U\,\|y\|_2
 \ge\left|\langle\mathbf1,y\rangle-\langle u,H^\dagger\ell\rangle\right|.
\]
This is the signed mean that must survive the correction; an ordinary small overlap on the wrong support alone does not measure it. In particular \(\langle u,H^\dagger u\rangle\le n\) and Cauchy give the sufficient requirements
\[
 \langle\mathbf1,y\rangle\ge c n,qquad
 \|y\|_2^2=o(nT),\qquad
 \langle\ell,H^\dagger\ell\rangle=o(n)
]
for one admissible growing \(T\) on each fixed-gap sign and floor. The last requirement may instead be replaced by an estimate retaining a fixed fraction of the mean in the signed formula. For a split at \(\kappa>0\), the part of the leakage cost with eigenvalues above \(\kappa\) is bounded by \(\|\ell\|_2^2/\kappa\). The part below \(\kappa\) needs a weighted estimate or a representation \(\ell=Hb+e\) with controlled signed mean \(\langle u,b\rangle\) and controlled remaining \(H^\dagger\) cost. These give exact transfer conditions for a candidate produced on a genuine near mask. No such candidate with the required prime-uniform leakage is established here.

The coordinate block \(E_U^*J E_W\) contains \(\tfrac12 E_U^*E_W\) since \(U\subset W\). It is not a wholly off-diagonal block; the fixed diagonal and the pointwise Jacobi bound alone do not give a full correction estimate.

## A Fourier-minor test specific to the genuine Jacobi sector

Choose a maximal linearly independent subset \(U'\subseteq U\) of the actual columns \(JE_U\) and let \(k=|U'|\), \(H'=E_{U'}^*J E_{U'}\). Then \(H'\) is invertible if \(k>0\), and projection onto these columns gives the same distance as using \(U\). The matrix determinant lemma gives the exact ratio
\[
 \frac{d_U^2}{n}=\frac{\det(H'-\mathbf1_{U'}\mathbf1_{U'}^*/n)}
                           {\det H'}.
\]
For \(k=0\) the ratio is one with the empty determinant convention. In the actual unitary Fourier coordinates on the cyclic group indexed by \(Q\), write \(J=M^*1_{\Omega_\epsilon}M\), where the sector \(\Omega_\epsilon\) consists of \(1\) and the physical \(a\in Q\) with \(\chi(1-a)=\epsilon\), using the Fourier convention of [the smoothing note](smoothing.md). The removed constant projector is the contribution of the row indexed by \(1\). By Cauchy–Binet the numerator and denominator are sums of \(|\det M_{I,U'}|^2\) over \(k\)-subsets \(I\) of \(\Omega_\epsilon\setminus\{1\}\) and of \(\Omega_\epsilon\), respectively. This uses the exact actual adaptive set \(U'\). It is a ratio of weighted sums, so the existence or count of a nonzero minor by itself gives no lower bound.

Multiplying the row index set \(I\) by a fixed element of \(Q\) multiplies columns of the Fourier minor by unit scalars. Thus the modulus is constant on each translation orbit of row sets in the full character parameter space. Grouping the sums by these orbits, the ratio is a weighted average of the fraction of eligible sector translates avoiding the constant row, with the denominator weights equal to the number of eligible translates times the squared minor. A prime-uniform lower bound of size \(\omega(1/T)\) for this weighted fraction would be sufficient. No such bound is established for the actual ranks.
