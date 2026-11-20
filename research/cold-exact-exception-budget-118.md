# Excluding exceptional coordinates with the exact outer inverse

Use the actual physical predictor and complex square of [the corrected derivative transfer](cold-newton-mark-transfer-115.md), at a supplied moving starter. Keep \(Z,C,H,R,P\) from that argument. Assume \(\|KD\|_{2\to2}\le q_*<1\), \(\|C\|_\infty=O(1)\), \(\|Z\|_{\max}\le B n^{-\beta}\) and \(r=\sup_Q\|R\|_{2,n}=o(n^{-(1-\beta)/2})\), with \(0<\beta\le1/2\). Fix an inner square \(Q'\Subset Q\). For each output coordinate and floor let \(F\) be the set of actual summation coordinates to omit from the arithmetic estimate. No packet bound is assumed at those coordinates.

Write \(L_j=\sum_{i<j}(KD)^iK\), \(H_k=\sum_{i<k}(KD)^iR\). The following estimate leaves **only the truncated good-coordinate sum** for arithmetic:
\[
 \left|(ZCH)_a-\big[L_j 1_{F^c} C H_k\big]_a\right|
  \ll \sqrt n\,q_*^j r+n^{1-\beta}q_*^k r+n^{1/2-\beta}\sqrt{|F|}\,r.             \tag{1}
\]
Insert the diagonal restriction before truncating, so the three errors are respectively
\[
 \big[(Z-L_j)1_{F^c} C H_k\big]_a,
 \quad \big[Z1_{F^c} C(H-H_k)\big]_a,
 \quad \big[Z1_F C H\big]_a.
\]
The first uses the counting second norm, the second the maximum entry of the **exact** outer inverse and the counting first norm, and the third the same entry maximum and the first norm restricted to at most \(|F|\) coordinates. The latter is bounded by \(\sqrt{|F|n}\|H\|_{2,n}\). The counting contraction bounds each needed inner tail or full normalized second norm by the corresponding geometric bound times \(r\). The cutoffs from Round 115 make the first two terms \(o(1)\). At those cutoffs the last one in (1) is also \(o(1)\) for \(|F|=O(n^\beta)\), irrespective of any growth of packet values on the omitted set. This uses the exact inverse entry bound already required for this version of the starter. It gives a different sufficient budget from that of the [returned truncated-inverse estimate](api-astra-overflow-118.txt). Either may be tighter, depending on the available entries and actual set size.

The physical mark can be removed even without spending one ordinary bad coordinate. In fact \(C_0=\Phi''_{t,0}(V_0)P_0=O(n^{-1/2})\) when \(P\) and the marked predictor are uniformly bounded, by the exceptional radicand \(4n+V_0^2\). The first correction is bounded at the mark by the starter. Moreover \(Z_{a0}=P_a/f=O(n^{-1/2})\) from the actual marked susceptibility with \(|f|\asymp\sqrt n\). Hence the exact mark summand \(Z_{a0} C_0 H_0\) is \(O(n^{-1})\) on the stated disks. One may always include it in \(F\) when (1) is used instead.

For a common set \(F\), the good summation term on the right of (1) can be represented by arithmetic words and their genuine signed punctual contributions as in the returned proposal. Deleting additional good coordinates must be charged when proving or using a complement mean estimate for a word. The bound on the **actual** lost sum in (1) is separate from that arithmetic requirement. In particular removing up to square-root many coordinates at \(\beta=1/2\) does not prove that the complement words have the necessary mass, parity, or cancellation. Only if the resulting combined bound for \(P_a+[L_j1_{F^c}CH_k]_a\) has a fixed angular margin does the earlier derivative transfer give a gap on the fixed inner square. An actual starter and its good-coordinate representation remain unproved; no cold prime domain is added here.

## Parity of the whole finite word on the physical prefix

There is a structural choice of representation for the full finite word whenever the actual physical prefix stays on the common bulk square-root sheet and its initial nine-center row is written in its supplied negative packets. Use the negative packet and boundary closure of [the shifted-column calculation](shifted-resolvent-96.md#boundary-weights-for-a-translated-column). The unshifted packet class has only the two base full characters \(1,\chi\) as possible boundary exceptions. An inverse row with output shift \(a\) also allows the two full lifts of \(a\) (or their inverses according to the column convention). The following classification concerns finite representations at each prime and floor. It supplies no uniform bound on their ranks or coefficients.

At a fixed prime and floor, a bulk activation value on the prefix is a scalar function of \(V_x^2\), by the common square-root choice. Finite interpolation in the distinct values of \(V_x^2\) gives an even polynomial that agrees at every bulk coordinate. Similarly the unmarked derivative is an odd polynomial on that row, by interpolating its factor \((4t+V_x^2)^{-1/2}\); curvature is an even polynomial from \(4t(4t+V_x^2)^{-3/2}\). The interpolation coefficients are allowed to depend on the entire finite row. Exceptional physical derivative or activation values at zero are represented separately before the next application of \(K\). The output of a point correction there is a scalar multiple of the actual negative column \(Ke_0\).

Induct along the exact prefix. Transport of an even polynomial in negative fields gives negative fields, and the errors in product identification occur only on the common base pair, so after transport they are again marked-column corrections. Thus every physical prefix row and its consecutive difference \(R\) has an unshifted negative representation. In \(KD\) applied to any negative input, the bulk odd derivative times that input gives an even product before transport. The exact marked derivative and any boundary repair simply give the same columns allowed by the common fiber union. In particular \(H_k\) and \(P=fZe_0\) have unshifted negative representations; for \(P\), the finite-field inverse lies in the span of the finite orbit of \(Ke_0\) under \(KD\) by the convergent Neumann series and finite-dimensional closure. The row of \(L_j\) is a translated-column Neumann sum because \((KD)^iK=K(DK)^i\) is transpose symmetric. It stays negative, with the base and translated pairs as its boundary union.

In the good-coordinate product \((L_j)_{ax}\Phi''_{t,x}(V_x)P_x(H_k)_x\), the bulk curvature has even parity, and the three rows have negative parity. After expanding into their constituent fields, every nonzero word therefore has an odd number of negative factors. By [the odd-product inertia test](iteration-parity.md#uniform-fixed-expression-trace-estimates), no word has a geometric punctual summand at the identity. The curvature's even representation may contain constants and punctual terms; this does not change the count of negative factors. The actual bounded mark term is handled separately as above. All full-character exceptions are contained in the base and translated pairs by the boundary rule before any **additional** good-coordinate deletion. They project to at most two actual summation coordinates.

This choice resolves the punctual term for a structural class that contains the finite physical word under the stated sheet and initial-packet hypotheses. It leaves the decisive growing-depth bound on the absolute coefficient times rank/dimension cost. Finite polynomial interpolation, or the finite-dimensional representation of the exact susceptibility, supplies no such cost bound. The distinction is material: a representation of the correct parity can still have a useless absolute price as the field and Picard depth grow.

## A third finite cutoff for the susceptibility inside the word

Set \(P_m=fL_m e_0\) with \(m\) an inverse cutoff independent of the Picard height, and \(C_m=\operatorname{diag}(\Phi_t''(V)P_m)\). Counting contraction and \(|f|=O(\sqrt n)\) give \(\|P-P_m\|_{2,n}=O(q_*^m)\). Also \(\|H-H_k\|_\infty\ll\sqrt n q_*^k r=o(1)\) at the original cutoff since \(\beta\le1/2\), so the bounded first correction on the supplied starter gives \(\|H_k\|_\infty=O(1)\).

Split \(L_j=Z-(Z-L_j)\) in the additional good-coordinate error. The exact entry bound and normalized Cauchy–Schwarz for \((P-P_m)H_k\) give the first term below; the counting second norm of the outer tail and the supremum bound on \(H_k\) give the second:
\[
 \left|[L_j1_{F^c}(C-C_m)H_k]_a\right|
       \ll n^{1-\beta}q_*^m r+\sqrt n\,q_*^{j+m}.
\]
Thus \(m=k+\lceil\log\log n\rceil\) for large \(n\) makes the error vanish at the original residual scale. This gives three logarithmically truncated factors at the same actual predictor. The separate summand \(P_a\) in the combined derivative remains exact and may need a longer cutoff for its independent estimate. The three cutoffs do not bound the degree, rank or coefficient price needed for the arithmetic sum.
