# An all-height physical predictor on a colder open rectangle

For every eligible prime \(p=2n+1\) with \(n\ge10^{30}\), the actual nine-center Picard iterates are holomorphic at **every height** on
\[
  16640237<2^{20}\Re t<16640262,\qquad 2^{20}|\Im t|<1.                 \tag{1}
\]
Writing \(\|v\|_{2,n}^2=n^{-1}\sum_i|v_i|^2\), their physical residuals satisfy
\[
 \|K\Phi_t(V_h)-V_h\|_{2,n}\le9.308(0.526)^h,\qquad
 \sup_{i,h}|V_{h,i}|<4.654 .
\]
Here \(\Phi_t(x)_i=\sqrt{4t_i+x_i^2}\), with \(t_0=n\) and \(t_i=t\) in the bulk. The lower endpoint advances \(23/2^{20}\) below the previously proved unforced interval. The open overlap has \(16640260<2^{20}\Re t<16640262\). The nominated square about \(2^{20}t=16637952\) remains colder. [Previous unforced rectangle](astra-imaginary-84.md) · [Height-600 physical predictor](astra-source-88.md)

## Eight further signed rank-three labels

Use the old degree-28 arithmetic polynomial and its actual parameters. At free arity \(r\le8\), keep the same inner rank-three prefix \(l\le4,\ k\le9,\ u+v\le5\). Its indices are the number \(l\) of rank-three inputs, the absolute Jacobi mode \(k\), and the two Legendre labels \(u,v\). For a nontrivial \(\mathrm{GL}_3^2\) label \(a=(a_1,b_1,a_2,b_2)\) and determinant-corrected Jacobi exponent \(e\), let \(C_{r,a,u,v,e}\) be the old signed coefficient. It sums
\[
 \binom{r+l}{r}(\beta/4)^l\,d_{r+l,k,u,v}\,M_l(a,m)/|E_k|
 \quad\text{over } e=m+s,\quad s\in E_k=\{-k,k\}.
\]
Here \(M_l(a,m)\) is the integer multiplicity in \((4W)^l\) and \(E_0=\{0\}\). The \(d\)'s include the original root amendments and the factor \(1/500\) on \((r,l,k,u,v)=(0,1,1,0,0)\) left after forming the rank-four center. Each such signed coefficient is separately charged before multiplication by rank-four factors in the original upper bound. [Inner prefix and rank-four arithmetic](astra-rankfour-57.md) · [Nine-center amendments](astra-joint-65.md)

Take the four standard or dual labels of the two rank-three groups, their separate adjoints, and the product of the two standards and its dual. The last four labels in these coordinates are \((1,1,0,0),(0,0,1,1),(1,0,1,0),(0,1,0,1)\). For each label and \(j\le6\), at the same \(u,v,e\), combine
\[
       X=C_{j,a,u,v,e},\qquad
       Y=\binom{j+2}{2}\gamma^2 C_{j+2,a,u,v,e}/8 .
\]
The second term is the arithmetic unit in the square of the rank-four input \(F\). Its multiplicity eight in \((8F)^2\) gives \(8/64=1/8\), and its Jacobi shift is zero. Both summands have zero inputs from all later centers. The additional round-84 pools use the trivial rank-three label, and the partial rank-five root subtraction uses an older scalar with one rank-four child. Neither uses these two charges.

Subtract a lower bound for the triangle saving
\[
 |X|+|Y|-|X+Y|
 =\frac{2(|X||Y|-\Re(X\bar Y))}{|X|+|Y|+|X+Y|},
\]
taking zero when the denominator enclosure meets zero. For weight \(w\) of the actual rank-three pair fiber, the boundary sites \(w+b-e\), \(b=-2u,-2u+4,\ldots,2u\), occur with multiplicity \((v+1)\operatorname{mult}(w)\). The eight labels are closed under interchanging the two factors and taking duals. The full \((u,v,e)\) ranges are also preserved by the inherited twist involution, so pooling on the displayed fiber gives the reflected saving on the other lift. Debit the smaller certified saving on the two reflected sites from each side of the positive majorant. All unselected powers, labels and exceptional finite-field corrections keep their upper bounds.

## Field-first decay and harmonic action

In units \(2^{-20}\), the three real intervals have endpoints \((16640237,16640247),(16640245,16640254),(16640250,16640262)\). Use respectively five, five and six real subdivisions, imaginary half-width one, and the genuine forcing parameter one everywhere. The inherited symmetric 58-packet update, including binomial orders 15 through 22 and the remaining geometric tail, preserves the three frozen bounds with tilted excess \(<1.85\,10^{-10}\) against budget \(2\,10^{-10}\). This includes \(10^{-12}\) for the actual exceptional first packet. The maximum coordinate cap is below \(4.653015\). The same coldest frozen cap without the eight new pools overruns its first packet by more than \(1.43\,10^{-7}\). This last comparison concerns that particular cap. All certificates use outward-rounded Arb at 192 bits. [Checker](astra-depth-95-check.py) · [Frozen rational caps](astra-depth-95-caps.json) · [Four replay records](astra-depth-95-checks.jsonl)

The real Jacobi seed accounts for at least \(2.8284\) of the coordinate majorant. On every segment between successive iterates, \(|\Im V|\le M-2.8284\), where \(M\) is the complete cap for that rectangle. At left floor \(L\), the modulus of the activation derivative is bounded by
\[
 \frac{M}{\sqrt{4L+M^2-2(M-2.8284)^2}}<0.526 .
\]
This follows from \(\Re(4t_i+x^2)\ge4L+|x|^2-2(\Im x)^2\) and monotonicity in \(|x|\). The physical marked floor satisfies the same inequality. Apply the second-norm contraction of \(K\) to every successive difference, using \(\|V_1-V_0\|_{2,n}\le2M\). Consequently \(\lim_{h\to\infty}\limsup_{p\to\infty}\sup_{(1)}\|R_h/\sqrt t\|_{2,n}=0\) along the entire eligible prime sequence.

On the bulk \(|\Im(V_{h,i}/\sqrt t)|<0.46\) by the same bound and \(|\arg t|<10^{-7}\). The physical relation \(V_{h,i}/\sqrt t=2\sinh g_{h,i}\) gives \(|\Im g_{h,i}|<\arcsin(0.23)\) on the positive chart. At the mark use \(V_{h,0}/\sqrt n\) instead. Uniform convergence in normalized second norm at each fixed field gives a holomorphic stationary row with those strict margins. Its real positive factors identify the physical branch on the overlap. Its marked log satisfies \(|\operatorname{arsinh}(V_{\infty,0}/(2\sqrt n))|<3/\sqrt n\). This row itself is uncorrected at the centered cap \(a=1/\sqrt2\). Hence the canonical action is harmonic on the reciprocal image of (1) at each of these primes. On each closed real subinterval of (1) one can shrink the imaginary width to accommodate the finitely many smaller primes by positive stationary invertibility and compactness, as in round 84. [Physical marked potential](cap-curvature-94.md)

1. Address the remaining gap of \(2277/2^{20}\) between the lower endpoint and the right edge of the nominated square by collecting two successive physical derivative kernels. The single-vertex method at its central floor already has a divergence certificate even with full arithmetic collection. [Single-vertex obstruction](astra-direction-83.md)
2. For an intermediate advance, combine the same inner labels with the arithmetic unit of \(G^2\) from the rank-five center, whose coefficient is \(1/16\), at fixed outer arity and determinant exponent. The current majorant charges that scalar pair separately. [Rank-five arithmetic return](astra-ranknext-58.md)
