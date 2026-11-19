# The centered quadratic remainder at the thirtieth seed predictor

Let \(p=2n+1\equiv1\pmod4\) be prime, \(a=2031/128\), \(D=\{|t-a|<1/4\}\), and \(I\) a closed real subinterval of \(D\) of positive length. Take the actual marked seed orbit \(V_0=S=2\sqrt n Ke_0\), \(V_{j+1}=K\Phi_t(V_j)\). At \(V=V_{30}\) let \(r=V_{31}-V\), \(D_V=\operatorname{diag}\Phi'_t(V)\), and define the exact Newton correction and the signed coordinatewise Taylor remainder by
\[
 h=(I-KD_V)^{-1}r,\qquad B=\Phi_t(V+h)-\Phi_t(V)-D_Vh .
\]
The activation has floor \(n\) at coordinate zero and floor \(t\) elsewhere. For every \(0<\eta<1\) there exists \(c=c(I,\eta)>0\) such that, for all sufficiently large eligible primes, on a set of measure at least \((1-\eta)|I|\),
\[
             \|KB\|_{2,\mathrm{count}}=\|(I-J)B\|_{2,\mathrm{count}}
                  \ge c\sqrt n.                                      \tag{1}
\]
Equivalently the actual nonlinear residual at the once-corrected row has this lower bound. Corrections real on \(I\) with uniform counting linear defect \(o(\sqrt n)\) give the same conclusion, after decreasing \(c\). The estimate uses no cap on \(V+h\) on the real axis. It excludes the [centered test of round 76](astra-predictor-76.md) on the entire disk for this predictor. The constant is non-effective, and the exceptional sets may depend on the prime. Estimate (1) does not decide the single center \(a\), the nine-center predictor, the stationary row, or ETH Problem 26.

## A square with positive variance at unbounded primes

Use \(E=n^{-1}\sum_i\), \(\|x\|_N^2=E|x|^2\), and \(Jx=Ex\) in every coordinate. Recall the real rows
\[
 L_1=K(S^2/2),\qquad L_{j+1}=K(SL_j).
\]
For each fixed \(1\le j\le31\),
\[
        \sup_p\|L_j\|_\infty<\infty,\qquad
        \liminf_p \operatorname{Var}_n(L_j^2)>0.                    \tag{2}
\]
Here is why connectedness supplies the additional information about the square. The fixed-expression Mellin calculus approximates \(L_j\) in \(\|\cdot\|_N\) with error \(O_j(p^{-1/2})\) by a bounded linear combination of negative trace fields. Start with the Jacobi line and its quadratic lift. For each successive product with \(S\), expand the independent lifts, take the even middle convolution, then apply the ordinary quadratic twist to its nonpunctual part. The product formula fails only on boundedly many full characters at each fixed operation, with bounded error there. \(K\) contracts \(\|\cdot\|_N\), and multiplication by \(S\) has bounded norm. This inductively gives the stated error with uniformly bounded ranks, dimensions, list size and coefficients at that depth. The compact-support traces themselves are bounded also at their bad characters. Since the counting error is \(O_j(1)\), the actual \(L_j\) is uniformly bounded coordinatewise. Each good lift uses the same function of the joint arithmetic Frobenius matrices, obtained by including both quadratic twists as summands. Uniform averaging on full characters therefore computes the square-subgroup mean. [Fixed-expression arithmetic and lift formulas](iteration-parity.md#uniform-fixed-expression-trace-estimates)

For each prime, take the arithmetic semisimplification of the pure weight-zero direct sum of these objects and their quadratic lifts. This preserves the Frobenius traces, tameness and singularity support. Its geometric tensor words with duals are tame and lisse off the point one in the torus, with punctual constituents supported only at one. This follows from the tame local convolution formula, including the support statement for punctual constituents. Subobjects inherit this condition, and inversion in the dual fixes one. The only simple geometric punctual object in the generated category is consequently \(\delta_1\). Katz's connectedness criterion shows the geometric convolution group is connected. Its compact form \(H_p\) is connected as well. The good base-field characters belong to a single arithmetic coset \(g_pH_p\), which can vary with the prime. [Katz, Corollary 6.7 and Lemma 7.1](https://web.math.princeton.edu/~nmk/mellin331.pdf) · [Rojas-León, §5](https://arxiv.org/pdf/1106.1398) · [Single-singularity argument in round 60](astra-rankeight-60.md#the-connected-group)

More explicitly, every subsequential law of \(L_j\) has connected support. Pass to a subsequence with constant list of block dimensions, and realize the compact groups block-unitarily in a fixed \(U(d)\). Pass further so that the bounded coefficients converge, \(g_p\to g\), and \(H_p\) converges in Hausdorff distance to a compact subgroup \(H\). Closedness under products and inverse passes to the limit, as does connectedness. Haar measures of \(H_p\) converge to Haar on \(H\): any weak limit is supported on \(H\), and for every \(u\in H\) choose \(u_p\in H_p\) converging to \(u\) to see left invariance. The real parts of the trace combinations converge uniformly on the ambient block group to a continuous function \(f\). For each fixed real polynomial test on that function the empirical mean differs from its coset Haar mean by \(o(1)\). Indeed expand the polynomial in traces and their dual traces. For every resulting fixed tensor word its geometrically trivial multiplicity contributes precisely the trace of \(g_p\) on geometric invariants, the coset Haar integral. Its nonpunctual middle-extension stalk contributes \(O(p^{-1/2})\); bounded ranks at fixed word length and boundedly many bad characters make this uniform. This argument retains arithmetic phases on every multiplicity space. Boundedness and polynomial approximation pass to continuous tests. Thus the limiting law is the image of Haar on \(gH\) under \(f\), with support the connected set \(f(gH)\). [Fieldwise coset integral and uniform fixed-word errors](uniform-fixed-depth.md#the-two-largest-coordinate-repair-costs-at-fixed-depth)

Exactly \(EL_j=0\) since \(K1=0\), and [round 77](astra-newton-77.md) proves \(\liminf_p E L_j^2>0\) through \(j=31\). A subsequence with vanishing variance of the square would have a limiting law supported on \(\{-b,b\}\) for some \(b>0\), by uniform boundedness. Its zero mean would give positive mass to both points, contradicting connected support. This proves (2) without computing individual fourth moments or identifying a common arithmetic group across primes.

## A scalar analytic test without a square root at the corrected coordinates

Put \(z=1/(2\sqrt t)\), \(G_z(x)=(\sqrt{1+z^2x^2}-1)/z\), and use the unmarked proxies \(U_0=S\), \(U_{j+1}=S+KG_z(U_j)\) from [round 77](astra-newton-77.md). Write \(W=U_{30}\), \(R=U_{31}-W\), and
\[
 A=\sqrt{1+z^2W^2},\qquad D_0=zW/A,\qquad H=(I-K\operatorname{diag} D_0)^{-1}R .
\]
Here \(D_0\) denotes a whole bulk derivative row. All subsequent products without \(K\) are coordinatewise. The round-77 analytic bridge contains the real segment \(0\le z\le\max z(I)\) in its interior. Shrink to a prime-independent open neighborhood of that segment with \(|z|<0.13\). On it \(\|U_j\|_\infty<5\) through height 30, so \(\|D_0\|_\infty\le0.65/\sqrt{1-0.65^2}<1\). Both \(R,H\) are holomorphic and bounded in normalized second norm by prime-independent constants, using the bound on \(G_z(W)\) and the Neumann series. No sup bound for \(H\) is required.

Define
\[
 P=(1-D_0^2)H^2,\qquad C=A+zD_0H,\qquad
 k=\frac{EP}{EC+\sqrt{(EC)^2+z^2EP}},\qquad g=L_{31}^2-E L_{31}^2.
\]
The scalars \(EP,EC\) are uniformly holomorphic and bounded there by the normalized second-norm bound, including for complex parameters (no conjugation in \(H^2\)). On the real segment \(EP\ge0\) and \(EC>0.9\). In detail, the real derivative on each segment joining consecutive inputs is at most \(0.65\), and \(\|U_1-S\|_N<2\) by rationalization, using \(\|S\|_\infty<3\). Thus \(\|H\|_N\le 2(0.65)^{30}/(1-0.65)<1\); also \(A\ge1\). By Cauchy estimates on a slightly smaller neighborhood, both \(EC\) and the discriminant have uniformly positive real part on a common open tube around the real segment. The positive square root therefore gives a bounded holomorphic \(k\) on that tube, satisfying \(EP=2k EC+z^2 k^2\).

The scalar witness
\[
                 f_p(z)=E(gP)-2k E(gC)
\]
is holomorphic and locally uniformly bounded there by (2). In the finite-dimensional Taylor expansion at zero, \(R=z^{31}L_{31}+O_p(z^{32})\), hence \(H=z^{31}L_{31}+O_p(z^{32})\). We have \(C=1+O_p(z^2)\), \(k=O_p(z^{62})\), and \(Eg=0\). It follows that
\[
          [z^{62}]f_p=E(gL_{31}^2)=\operatorname{Var}_n(L_{31}^2).
\]
The corresponding first centered coefficient of the proxy Taylor remainder is \((I-J)L_{31}^2/2\) at order 63. Here the squared equation avoids evaluating its bulk square root anywhere off the real axis. By (2) every subsequential locally uniform limit of \(f_p\) has a nonzero coefficient at order 62. The normal-family argument of round 77, removing neighborhoods of the finitely many zeros of the limit on \(z(I)\), gives \(|f_p(z(t))|\ge c_0(I,\eta)>0\) on a real subset of the asserted measure for each sufficiently large prime. The neighborhoods can be chosen in the \(t\)-interval by composition with \(z(t)\).

For real \(t\in I\) form the unmarked bulk remainder \(B'=G_z(W+H)-G_z(W)-D_0H\). It is nonnegative by convexity, with \(\|B'\|_N\le2\|H\|_N\). Squaring \(\sqrt{1+z^2(W+H)^2}=C+zB'\) gives the exact identity
\[
                     P=2CB'/z+(B')^2 .
\]
Let \(b=EB'/z\) and \(e=\|(I-J)B'\|_N\). Replacing \(B'\) by its mean in this identity incurs \(O_I(e)\) in normalized first norm, by Cauchy–Schwarz and the uniform second-norm bounds on \(C,B'\). Taking the mean yields \(EP=2bEC+z^2b^2+O_I(e)\). Since \(b,k\ge0\) and \(EC>0.9\), subtraction of the scalar equation for \(k\) gives \(|b-k|=O_I(e)\). Testing the same first-norm error against bounded \(g\), and using \(Eg=0\), gives \(|f_p|=O_I(e)\). Thus the centered unmarked remainder has a positive normalized lower bound on the selected set.

## Returning to the actual mark and linear correction

The rows \(H\), uniformly for real \(t\in I\), are approximable in \(\|\cdot\|_N\) to every fixed accuracy by rows of prime-independent bounded sup norm. To check this point, use bounded linear combinations of real negative Mellin fields as approximants. The seed is already such a field. If a row \(u\) has these approximants, so does the output \(K G_z(u)\). First approximate \(u\) in normalized second norm by a real negative combination with coordinate bound \(M\). The real map \(G_z\) is globally 1-Lipschitz. Approximate it on \([-M,M]\), uniformly for \(t\in I\), by even polynomials of fixed degree and bounded parameter-dependent coefficients (e.g. polynomial approximation on the product of compact intervals followed by symmetrization in the argument). Applying \(K\) to each even product gives negative fields with normalized second error \(O(p^{-1/2})\) as above. This proves the assertion for every \(U_j\) through 31 and their difference \(R\). Approximants can be made real by adjoining duals and taking real parts; bounded exceptional errors are allowed in the normalized comparison.

For a Neumann summand \(X\) with such approximants, the next summand is \(K(D_0X)\). First approximate \(X\) at the prescribed accuracy by a negative combination \(X'\) bounded by \(M'\), using \(|D_0|\le1\) on the real segment. Then approximate \(W\) by negative fields sufficiently accurately in \(\|\cdot\|_N\) compared with \(1/(1+M')\). The function \(x\mapsto zx/\sqrt{1+z^2x^2}\) is globally \(|z|\)-Lipschitz on the real axis; approximate it uniformly by an odd polynomial on the compact range of the approximant to \(W\). After multiplication by \(X'\) every monomial is even in negative fields, and the same transport rule applies. All choices may be made successively, with complexity depending on accuracy and the fixed number of summands only. The Neumann tail is uniformly small by \(\|D_0\|_\infty\le0.65\) and bounded \(R\). This proves the bounded approximability of \(H\).

Two consequences used below are \(|H_0|/\sqrt n=o_I(1)\) and \(\|dH\|_N=o_I(1)\) whenever the multipliers \(d\) are uniformly bounded with \(\|d\|_N=o_I(1)\). Indeed, replace \(H\) first by a uniformly bounded approximant at precision \(\epsilon\), let the prime increase, then let \(\epsilon\downarrow0\). This rules out concentration of the normalized square mass on the exceptional site or on changing small sets.

On the same real interval the true orbit and the proxy satisfy \(\|V_j-U_j\|_N=O_I(n^{-1/2})\) through 31 by the [marked forcing comparison](astra-newton-77.md). Off the mark, the true and proxy slopes consequently differ by \(O_I(n^{-1/2})\) in normalized second norm, by the global derivative Lipschitz estimate above. The contribution at the mark to this comparison is also \(O(n^{-1/2})\), since both slopes lie in \([-1,1]\). The actual inverse at \(V_{30}\) is bounded on \(I\) by its real coordinate cap 5 and the positive floor. Subtraction of the two Newton equations gives
\[
 (I-KD_V)(h-H)=(r-R)+K(D_V-\operatorname{diag}D_0)H .
\]
Both terms tend to zero in normalized second norm uniformly on \(I\), the last by bounded approximability. In particular \(\|h-H\|_N=o_I(1)\) and \(|h_0|/\sqrt n=o_I(1)\).

The bulk Taylor remainder is globally 2-Lipschitz in its correction on the real axis. Changing its base from \(W\) to \(V\), at the fixed correction \(H\), costs in normalized second norm at most \(2\|V-W\|_N+\|(G'_z(V)-G'_z(W))H\|_N=o_I(1)\). Finally a real remainder at either floor has modulus at most \(2|h_i|\); restoring the actual floor at zero costs at most \(4|h_0|/\sqrt n=o_I(1)\). This proves \(\|B-B'\|_N=o_I(1)\) and (1). For an approximate real correction the inverse bound first gives \(o_I(1)\) distance to \(h\) in normalized second norm. Lipschitz continuity of the remainder in the correction transfers the bound, and the normalized linear defect is negligible in the total corrected residual.

There is also a simultaneous lower bound for **every** real candidate correction \(u\) on the same selected set, without a small-defect hypothesis. Put \(d_u=r-(I-KD_V)u\), \(B_u=\Phi_t(V+u)-\Phi_t(V)-D_Vu\), and \(M=\sup_{p,t\in I}\|(I-KD_V)^{-1}\|_{2\to2}\) for sufficiently large primes. Then
\[
 c\sqrt n\le\|KB_u\|_{2,\mathrm{count}}+2M\|d_u\|_{2,\mathrm{count}}
 \le\|K\Phi_t(V+u)-(V+u)\|_{2,\mathrm{count}}+(1+2M)\|d_u\|_{2,\mathrm{count}} .
\]
Indeed \(h-u=(I-KD_V)^{-1}d_u\), and the coordinate remainders are globally 2-Lipschitz in the correction. Thus allowing a candidate to miss the linear equation can give a small actual corrected residual only at a linear cost of order \(\sqrt n\) on these floors.

The proof uses fixed-expression arithmetic, real stability, and ordinary complex analysis. It introduces no finite-prime extrapolation or new interval calculation.

1. To test the single floor \(a\), obtain a quantitative lower bound for the scalar witness at \(z=1/(2\sqrt a)\), or a different real witness there. The positive leading coefficient and connected support control the measure of exceptional floors but leave an isolated zero possible.
2. For \(V_{600}\), determine whether its actual initial signed predictor has a bounded analytic path to a reference parameter with a nonzero leading increment. The same connected-support and squared-equation argument applies once the leading row has zero mean, positive normalized variance, and fixed-word control.
