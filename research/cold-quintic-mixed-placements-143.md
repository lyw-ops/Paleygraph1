# Six placements at the second higher Jacobi order

This Round 143 calculation concerns the selected symmetric block with one linear Legendre insertion on the unshifted \(C=C_1\). As in Round 142 use \(d_t(S)\) and \(\alpha Y d'_t(S)\) with \(S=s_nC\) and \(\beta=s_n^2/(8t)\). At the common bulk floor their relative scalar coefficients are, respectively, \(1-\beta C^2+(3/2)\beta^2 C^4\) and \(1-3\beta C^2+(15/2)\beta^2 C^4\). The actual \(t_0=n\) is restored by the same bounded marked and lift repairs as in the finite R142 block.

With global prefactor \(\alpha s_n/(4t)\), the coefficient of \(\beta^2\) in the two full orders is
\[
\begin{split}
Q_2={}&\tfrac32 K[C^5K(CY)+Y K(C^6)]\\
     &+3K[C^3 K(C^3Y)+C^2Y K(C^4)]\\
     &+\tfrac{15}{2}K[C K(C^5Y)+C^4Y K(C^2)] .
\end{split}
\]
The middle row places one first correction in each step. It is present along with both pairs of pure second corrections. All six words have the extra unshifted input \(C\).

Using \(K(CY)=W+O_{P_{5000}}(n^{-1/2})\), \(K(C^2)=Y/2+O_{P_{5000}}(n^{-1/2})\), and the R142 formula for \(K(C^4)\), one can isolate all explicit \(K(CW)\) and \(K(Y^2)\) occurrences from the Chebyshev decompositions in these six words. The \(K(CW)\) scalar is
\[
 \frac32\frac{10}{16}+3\frac9{16}+\frac{15}{2}\frac{10}{16}=\frac{117}{16}.
\]
Here \(C^5=(C_5+5C_3+10C)/16\) and \(C^3=(C_3+3C)/4\). The \(K(Y^2)\) scalar is
\[
 \frac32\frac{15}{32}+3\frac14+\frac{15}{2}\frac3{16}=\frac{183}{64}.
\]
The first term uses \(C^6=(C_6+6C_4+15C_2+10)/32\), the second the constant \(1/2\) in \(C^2\), and the third the constant \(3/8\) in \(C^4\). Relative to the leading pool \(K(CW)+K(Y^2)/2\), these explicit contributions multiply \(\beta^2\) by \(117/16\) and \(183/32\). These are subtotals of displayed Chebyshev occurrences. The remaining generic words must be checked for further returns before these become full coefficients.

The new word \(K[C_3 K(C_3Y)]\) has rank \(18\) or \(20\) on each simple fixed lift. Its inner active fiber is \((-5,-1,3,3,0,0)\), up to sign or exchange, and the other six weights are zero. The outer shifts by \(3\) and \(-3\) give absolute moments \((22,18)\) or \((18,18)\). The word \(K[C K(C_5Y)]\) has rank \(18\) on each simple fixed lift. The inner active fiber is \((-7,-3,5,5,0,0,0,0,0,0)\), and the other ten weights are zero. The outer shifts by \(1\) and \(-1\) give moments \((26,10)\). Simplicity follows in both words from repeated Jacobi convolution-line twists and ordinary generic transport. Thus these two words cannot add a named old rank-four or rank-eight label. The \(Y K(C_6)\) and other residual products still require a derived-label comparison.

The corrected expansions also repeat the exact word \(K[C K(C_3Y)]\) from the first higher block. The two displayed contributions give \(3\cdot(3/4)(1/4)+(15/2)(5/16)=93/32\) in \(Q_2\), with the first coming from \(C^3K(C^3Y)\) and the second from \(C K(C^5Y)\). Thus its visible joint coefficient is \(-3\beta/4+93\beta^2/32\). This is a repeated-word identity. It does not determine the complete arithmetic-label coefficient in the presence of residual products.
