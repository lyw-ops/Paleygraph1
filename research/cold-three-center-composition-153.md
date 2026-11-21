# A direct two-height comparison outside the three-center square

Keep the original closed cold square, \(t_0=n\), both lifts, and the whole translated \(P_{5000}\) class. Let \(E_h=A_h-B_3\) for the two actual heights in [Round 152](cold-three-center-152.md). The exact difference is
\[
              A_{602}A_{601}-B_3^2=E_{602}A_{601}+B_3 E_{601}.
\]
Composing the retained weight comparisons before pricing gives the uniform eventual bound
\[
                 \|A_{602}A_{601}-B_3^2\|_{P_{5000}}<0.66381.
\]
This improves the product of the separate scalar upper bounds for the two terms. The needed direct difference is \(0.51961239\), using \(\|B_3^2\|<0.48038761\).

## Pricing both terms on the same input column

For \(B_3,E_{601},E_{602}\), reproduce the signed Jacobi and Legendre coefficient collection and exact \(W\) measure from Round 152. For \(A_{601}\) use the narrower inherited [Round 130](cold-combined-height-130.md) retained derivative comparison and its tilted leak. The comparison step for each retained folded row \(r_k\) on a base input weight \(j\ge1\) sends \((j-1)r_k\) to each positive weight \(k\), and \(r_k/2\) to each nonzero \(|j-k|\) and \(j+k\). Contributions to the same absolute weight are added. The zero count after the step is covered by the negative-packet rank identity, so the next vertex uses the same rule.

Let \(C_r(j)\) be that single-column cost in the inherited rational \(\pi\), and set \(C_r(0)=0\). If the inner comparison has row \(s\), the composed base cost is
\[
 (j-1)\sum_k s_k C_r(k)
      +\tfrac12\sum_k s_k\bigl(C_r(j+k)+C_r(|j-k|)\bigr).
\]
For a unit off-base first moment, the composed norm ratio is \(m_sm_r+(\sum_k s_k C_r(k)+m_s\nu_r)/5000\), where \(m\) denotes total mass and \(\nu_r=\sum_k r_k\pi(k)\). This uses the off-base rule of [Round 96](shifted-resolvent-96.md#the-two-estimates-for-one-physical-derivative-step): the inner step adds the \(s\) base row and leaves off-base moment \(m_s\). The two product costs are added at the same input weight and then maximized. Only finitely many columns precede the affine region; thereafter both summed cost and input price are affine, so the finite endpoint and limiting ratio suffice.

All loss estimates act on the positive weight comparison. They charge paths using a discarded weight or omitted word, without requiring a separate actual vector for an individual discarded weight. For example the lost terms for \(E_{602}A_{601}\) are bounded by the \(E_{602}\) loss rate times the complete \(A_{601}\) comparison rate, plus the \(A_{601}\) loss rate times the complete \(E_{602}\) comparison rate. The analogous terms for \(B_3 E_{601}\) give the rest of the tail. The checked complete comparison rates justify both uses. The inherited uniform \(O_{5000}(n^{-1/2})\) lift and physical marking repairs remain covered by the strict margins. [Outward replay](cold-three-center-composition-153-check.py) · [Saved record](cold-three-center-composition-153-checks.jsonl)

## A lower witness for the chosen positive comparison

Restrict the two products to weights \(1,\ldots,12\) at both vertices. Their sum maps the recorded positive integer vector componentwise above \(0.6174\) times itself in the same replay. A numerical eigensolver was used only to find that integer vector. Positivity implies that any coordinatewise monotone homogeneous gauge positive at the vector has rate greater than \(0.6174\) on this retained comparison. Thus changing the weight price alone cannot reach \(0.51961239\) for this comparison.

The actual operator keeps more sign information. The obstruction says nothing about its signed norm or a different packet accounting. The next essential test is an actual retained-center or Picard label that cancels across the two vertices, or a different way of containing the true derivative.
