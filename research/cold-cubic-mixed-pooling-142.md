# First higher Jacobi coefficients pooled in the actual mixed transport

Use \(C=C_1\), \(S=s_n C\) and the actual Legendre center \(Y\), with its fixed cold coefficient \(\alpha\), on the original marked square. On the Jacobi input \(C\), take the leading mixed pair and all four placements of exactly one next Taylor term. All multipliers below have their actual marked denominator at \(t_0=n\). The two relevant scalar series begin
\[
 d_t(S)=\frac{S}{2\sqrt t}-\frac{S^3}{16t^{3/2}}+\cdots,\qquad
 d'_t(S)\alpha Y=\frac{\alpha Y}{2\sqrt t}
                   -\frac{3\alpha S^2Y}{16t^{3/2}}+\cdots.
\]

Put \(\beta=s_n^2/(8t)\). With the common bulk denominator for the intermediate calculation, the combined output on \(C\) is \(\alpha s_n/(4t)\) times
\[
 K(CK(CY)+Y K(C^2))
 -\beta\, K\left[
 C^3K(CY)+Y K(C^4)+3C K(C^3Y)+3C^2Y K(C^2)
 \right].                                                        \tag{1}
\]
Restoring the physical marks in the finite block changes the output by \(O_{P_{5000}}(n^{-1/2})\) uniformly on the square. A single changed multiplier contributes another bounded multiple of \(Ke_0\) after \(K\), and each adjacent fixed word has bounded price. Thus this correction preserves the actual entry and both boundary pairs, as in [the leading mixed column](cold-mixed-seed-column-141.md).

Use \(K(CY)=W+C/p\), \(K(C^2)=Y/2-C/\sqrt p\), and \(C^3=(C_3+3C)/4\). The identity \(C^4=(C_4+4C_2+3)/8\) and the [fourth-mode feedback](astra-joint-65.md#exact-finite-field-feedback) give \(K(C^4)=(U+U')/16+Y/2+O_{P_{5000}}(n^{-1/2})\). Then (1) equals, up to the same physical error,
\[
\begin{split}
 &(1-3\beta)F_4
    +\left(1-\frac52\beta\right)\left(\frac{D+D^\vee}{8}+\frac R4\right)\\
 &\quad-\beta K\left[
 \frac14 C_3 W+\frac1{16}Y(U+U')+\frac34 C K(C_3Y)+\frac34 C_2Y^2
 \right].                                                       \tag{2}
\end{split}
\]
Indeed the first higher bracket contributes \(3K(CW)\) and \((5/4)K(Y^2)\) before the remaining terms, compared with \(K(CW)\) and \(K(Y^2)/2\) at leading order. The exact \(K(CW)\) and \(K(Y^2)\) feedbacks give (2), including the known small exceptional terms.

## Separation of the remaining terms from the named old labels

The operation by \(K\) on a pre-transport even convolution object twists its generic local system by \(s\), with inverse the same twist on the generic local system. Thus equality of nonpunctual arithmetic labels after twisting forces equality before twisting. For the terms other than \(C K(C_3Y)\) in the last bracket, separation can be checked before the final \(K\).

- \(C_3W\) has the same rank-three derived types as \(CW\), with Jacobi shifts \(\pm3\) in place of \(\pm1\). Within one derived standard or dual the differing shifts cannot agree, since the Jacobi line has infinite order. The rank-three types are distinct from the Legendre types in \(Y^2\).
- \(Y(U+U')\) has a nontrivial component on one of the two independent new symplectic factors, absent from both \(CW\) and \(Y^2\).
- The terms in \(C_2Y^2\) have shifts \(\pm2\) on the same derived types as \(Y^2\). The two Legendre standards have trivial determinant, so the unshifted \(Y^2\) sectors gain no Jacobi shift. These are also distinct from the rank-three derived types in \(CW\). The unit of \(Y^2\) here yields a shifted Jacobi line, not one of the named rank-four or rank-eight output fields.

For the remaining term, take one lift \(L^{\star3}\) or \(L^{\star(-3)}\) from \(C_3\) and one of the two Legendre lifts. At the two base twists before the inner \(K\) the combined nonzero weights have total rank moment six, since the Legendre weights are \((-2,2)\) on one fiber and zero on the other and the Jacobi shifts are \(\pm3\). After the inner \(K\) the resulting dimension is six. Up to sign reversal and exchanging the fibers, its nonzero weights at the active fiber are \((-5,-1,3,3)\) and the other fiber is zero. Thus the actual active fiber also has two zero weights. Adding one of the two opposite \(\pm1\) Jacobi shifts in the outer \(C\) multiplication gives absolute moment fourteen at the active fiber and six at the other, irrespective of the relative sign. The final \(K\) therefore has rank ten on each such constituent. Each factor before twisting is a Jacobi convolution-line twist of a simple object, and the ordinary rank-one twist preserves simplicity at each \(K\). These rank-ten fields cannot equal any of the old rank-four or rank-eight fields.

This proves exact signed pooling of the displayed old arithmetic labels through this finite higher-order block. On the original square the two relative coefficient magnitudes are eventually \(<0.812\) and \(<0.844\), respectively. These follow by applying \(|1-c/t|=|t-c|/|t|\) with the actual \(s_n^2=8+4/n\) and the halfwidth \(2^{-17}\). The \(O_{P_{5000}}(n^{-1/2})\) physical term repairs the actual mark and exceptional lifts. It is separate from the analytic Taylor orders beyond this block. The new labels in the final bracket still cost physical price, and there is no claimed full all-order contraction.
