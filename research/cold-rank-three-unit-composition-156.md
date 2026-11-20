# A signed rank-three unit merge on the translated comparison

Keep the original complex square, original physical mark \(t_0=n\), both lifts and both actual heights from [Round 153](cold-three-center-composition-153.md). Put \(A_h-B_3=E_h\). In \(E_h\) take the same finite analytic prefix as Round 153 and expand in the non-Legendre displacement about \(S+\alpha Y\). Let \(b,c\) be the zero Jacobi exponent and trivial Legendre coefficients of arities one and three of this prefix. In the displayed selected slots the terms
\[
   \delta b\,G,\qquad 3\beta^2\delta c\,W^2G
\]
are actual multiplier terms of \(E_h\) before the left \(K\). The factor \(3\) counts the positions of \(G\). Both terms belong to the omission since \(\delta G\) is absent from \(B_3\).

The [rank-three decomposition](astra-rankthree-55.md#collecting-signed-rank-three-characters) gives a true arithmetic unit of weight \(1/4\) in \(W^2\), from the four ordered dual pairs. After retaining that part of the second term, the common field \(G\) has the exact merged coefficient
\[
              \delta b+\tfrac34\beta^2\delta c .
\]
This is an identity of arithmetic summands at the multiplier vertex. It is preserved after multiplication by any inner row, so applies to the actual translated boundary classes and survives in the positive comparison of the large-input affine limit. The rest of \(W^2G\), other coefficients and true Picard residual remain in the original envelopes. Both bad-lift corrections and the physical denominator restoration retain the original \(O_{5000}(n^{-1/2})\) estimate.

To reprice Round 153, take its retained folded comparison rows for \(E_{601}\) and \(E_{602}\). Their weight-zero Jacobi and trivial Legendre slots priced the two selected coefficients separately at
\[
 |\delta|_{\rm cap}
    \left(|b|_{\rm up}+\tfrac34|\beta|_{\rm cap}^2|c|_{\rm up}\right)
\]
times the symmetric measure of \(G\). The unit portion lies inside the retained weight cutoff: the support of the folded \(G\) measure is \(0,\ldots,5\). Replace this charge by the outward modulus of the merged coefficient. The exact signed saving itself exceeds \(5\cdot10^{-8}\) on the square, before any extra cap savings. The [outward replay](cold-rank-three-unit-composition-156-check.py) subtracts a rounded-down saving from each of the two retained rows and verifies nonnegativity. It composes them with the unchanged \(A_{601}\) and \(B_3\) comparisons. All lost-path, tail and physical corrections are charged using the old complete upper rates, so the strict output is
\[
            \|A_{602}A_{601}-B_3^2\|_{P_{5000}}<0.66379866
\]
uniformly eventually on the original square. [Saved record](cold-rank-three-unit-composition-156-checks.jsonl)

The reduction applies on the whole translated comparison. Its magnitude leaves the \(0.51961239\) target open. A fuller signed collection would pair the unit at more Jacobi and Legendre labels and with the remaining actual centers, and seek additional independent arithmetic coincidences.
