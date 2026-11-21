# Complete named pools through the second higher mixed Jacobi order

Use the original marked cold square, the actual \(t_0=n\), the unshifted input \(C=C_1\), and the symmetric two-step action of \(d_t(S)\) and \(\alpha Yd'_t(S)\), with \(S=s_nC\) and \(\beta=s_n^2/(8t)\). Keep the six terms of the coefficient \(Q_2\) of \(\beta^2\) from [Round 143](cold-quintic-mixed-placements-143.md), after the prefactor \(\alpha s_n/(4t)\). Every formula below refers to the generic main terms, with finite mark and lift corrections of physical price \(O_{P_{5000}}(n^{-1/2})\) for the entire selected block. Use the whole \(K\) in each occurrence. Write \(W\) for the rank-three center, \(V=U+U'\) for the sum of the fourth-Jacobi centers, and \(\mathcal R_{10}=K[C K(C_3Y)]\).

The complete harmonic expansion is
\[
\begin{split}
Q_2={}&K\left[\tfrac{117}{16}CW+\tfrac{183}{64}Y^2\right]
         +\tfrac{93}{32}\mathcal R_{10}\\
&+K\left[\tfrac{3}{32}C_5W+\tfrac{33}{32}C_3W+
\tfrac{3}{64}Y K(C_6)+\tfrac{15}{64}YV+
\tfrac{3}{16}C_3 K(C_3Y)+\tfrac{15}{32} C K(C_5Y)
+\tfrac{3}{32} C_2YV+\tfrac{21}{8} C_2Y^2+\tfrac{15}{32} C_4Y^2\right].
\end{split}                                                     \tag{1}
\]
This follows by substituting the three Chebyshev identities for \(C^3,C^5,C^6\) in Round 143 and \(C^2=(C_2+1)/2\), \(C^4=(C_4+4C_2+3)/8\). The feedbacks used are \(K(C^2)=Y/2+O_P(n^{-1/2})\), \(K(C^4)=V/16+Y/2+O_P(n^{-1/2})\), \(K(C_4)=V/2+O_P(n^{-1/2})\), \(K(C_2)=Y+O_P(n^{-1/2})\) and \(K(CY)=W+O_P(n^{-1/2})\). For example \(3C^2Y K(C^4)\) contributes \(3C_2YV/32+3YV/32+3C_2Y^2/4+3Y^2/4\) before the outer \(K\).

## Separation from the three named pools

Each last-bracket term of (1) is separated from the named labels of \(K(CW)\), \(K(Y^2)\), and \(\mathcal R_{10}\).

- In \(C_j W\) for \(j=3,5\), each fixed lift is a simple Jacobi shift of a rank-three constituent. It cannot match \(CW\) before the last \(K\), since the rank-three derived types have the independent Jacobi torus and the shifts \(\pm j\) differ from \(\pm1\). Its derived group also differs from those of \(Y^2\). The two lists for a \(W\)-lift are \((-3,1,1)\) and \((1,0,0)\), up to sign and exchange, obtained by transporting the \(\pm1\) Jacobi line times a fixed Legendre lift. With the extra shifts \((j,-j)\) or \((-j,j)\), the pooled absolute moments give ranks \(8,10\) for \(j=3\) and \(14,16\) for \(j=5\). The rank-ten case of \(C_3W\) has folded weight-one count zero. Every lift of \(\mathcal R_{10}\) has folded count four by the two lists in [Round 142](cold-cubic-mixed-pooling-142.md). They cannot be equal.
- The Chebyshev feedback theorem for \(m=2,4,6\) gives fixed-lift factors with convolution groups \(Sp_2,Sp_4,Sp_6\). The two lifts of each even mode are included. Across these three ranks the Lie types are distinct, so the joint geometric group of one Legendre lift and one fourth- or sixth-mode lift is the product. Each tensor of their standards, with or without one Jacobi line, is simple. The finite marked discrepancy in \(K(C_6)\) is a bounded multiple of \(Ke_0\) by the exact even Chebyshev formula. Thus these products exhaust the generic contributions of \(Y K(C_6),YV,C_2YV\), without assuming a new higher-word monodromy theorem. Before the last \(K\), the two fibers of the \(m\)-lift have weights \((-m,m,0^{m-2})\) and \(0^m\). In the two phase cases \(Y K(C_6)\) has outer ranks \(20,24\), and \(YV\) has ranks \(12,16\). The \(\pm2\) shifted \(YV\) has rank \(20\) in all phase cases. These follow by adding the Legendre weights and then the opposite Jacobi shifts in the two fibers, and taking the averaged absolute moment. All exceed ten. [Even Chebyshev groups and mark](parallel-graph-shapes-23.md#a-fixed-number-of-path-columns-gives-no-leading-gain)
- The last \(K\)-images of \(C_3 K(C_3Y)\) and \(C K(C_5Y)\) have simple fixed lifts of ranks \(18,20\) and \(18\), respectively, by the two-stage transport calculation of Round 143.
- For \(C_jY^2\) with \(j=2,4\), first split \(Y^2\) into its unit, the two individual Legendre symmetric squares, and the mixed standard product. The dimensions of these simple sectors are \(1,3,4\). The symmetric-square fiber lists are \((-4,0,4)\) and \(0^3\), while both mixed lists are \((-2,-2,2,2)\). After the opposite shifts \(\pm j\), the transported ranks in the three sectors are \((2,8,8)\) for \(j=2\) and \((4,12,16)\) for \(j=4\). Thus none is rank ten. The old \(Y^2\) sectors have zero Jacobi shift and cannot match their shifted versions. The unit times the line is a pure Jacobi label and has no old derived type. All other shifted Legendre-derived factors are distinct from \(CW\) before the final transport. The unshifted unit is punctual and killed by \(K\).

All pre-transport label comparisons apply after \(K\) because the ordinary rank-one generic twist is invertible. For the other terms the explicit post-transport ranks and folded weight counts are generic invariants. Physical repairs, including at the true marked diagonal, retain the same finite-word bound as in R143. This argument does not require pairwise separation of the nine last-bracket terms from each other.

The coefficients on the three named pools of the selected block through order \(\beta^2\), after the common prefactor, are therefore
\[
 \begin{array}{c|c}
 K(CW)&1-3\beta+\frac{117}{16}\beta^2\\[2pt]
 \frac12K(Y^2)&1-\frac52\beta+\frac{183}{32}\beta^2\\[2pt]
 \mathcal R_{10}&-\frac34\beta+\frac{93}{32}\beta^2 .
 \end{array}
\]
In the first higher block the other \(C_3W,YV,C_2Y^2\) terms are separated from \(\mathcal R_{10}\) by the same comparisons just given. Thus the third row is complete at this truncation, not just a repeated-word subtotal. The result concerns the named generic labels on this one actual source. It leaves all further Taylor orders, the price of the remaining sectors, and the full marked analytic derivative open.
