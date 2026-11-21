# Signed first-spill dual and its clipped cost

Fix the actual marked first reflection of [Round 150](ordinary-prime-repair-source-150.md#restricting-both-coordinates-of-the-first-spill), with both physical roots excluded. Keep \(T,T+1\) in the simultaneous marked window and \(u=T^{-1/3}\). Use normalized expectation and define
\[
 d_{\rm mid}=d\,1_{\{n^{-1/4}T^{1/12}<d\le\sqrt n\,T^{-5/6}\}},\qquad
 S=\{i\in I:b_i^{(0)}\ge b_*\},
\]
where \(I\) is the true common complementary zero set on the bulk and \(b_*>0\) is fixed. Write \(K^\circ\) for the kernel with diagonal deleted, and put \(w=-\sigma1_S K^\circ d_{\rm mid}\). This is the signed cost, with \(w_0=0\). The cutoff \(H\) on the optimizer can be set to zero.

For each true opposite optimum \(F\), complementarity makes \(F\) vanish on the bulk outside \(I\). On \(S\) one has \(-\sigma Kd\ge b^{(0)}+u/2\). Thus \(\mathbb E(F1_S(-\sigma Kd))\ge g-b_*\), where \(g=qz_0/n-1\) and \(\mathbb E(Fb^{(0)})\ge g\) by the actual affine pairing. The low and high tails cost \(O_\tau(T^{-1/12})\) and \(O_\tau(T^{-1/6})\), respectively, by applying the Round 150 norm and entry estimates to their actual supports. The diagonal costs \(O_\tau(n^{-1/2}T^{-2/3})\). These estimates are uniform over all true \(F\). In particular a fixed gap forces \(\mathbb E(Fw)\ge g-b_*-o(1)\) for every such \(F\).

There is also an absolute comparison on the same exact receiver. Since \(-\sigma Kd\) is positive on \(S\),
\[
 0\le w_+-w\le1_S\bigl(|Kd_{\rm low}|+|Kd_{\rm high}|+|K_{ii}|d_{\rm mid}\bigr).
\]
The bounds just used apply to \(\mathbb E(F\,\cdot)\) of each nonnegative summand. For low inputs use Cauchy–Schwarz with \(\|F1_S\|_2\le\sqrt q\), and for high inputs use \(\mathbb EF=1\) with the pointwise estimate. Thus \(\sup_F\mathbb E(F(w_+-w))=O_\tau(T^{-1/12}+T^{-1/6}+n^{-1/2}T^{-2/3})\).

The [face dual](ordinary-terminal-face-dual-143.md) applies to either cost, including signed \(w\). Both of the exact maxima
\[
 \max\{\mathbb E Z-qZ_0/n:Z\in U_\sigma,\ Z\le w\text{ on }I\},
 \qquad
 \max\{\mathbb E Z-qZ_0/n:Z\in U_\sigma,\ Z\le w_+\text{ on }I\}
\]
are attained and differ by \(o(1)\), by the uniform comparison on their two primal minima. An \(o(1)\) upper on either maximum at one admissible growing marked time and fixed \(b_*\) smaller than the gap lower would exclude that gap. The proof uses the full high receiver and gives no lower on an arbitrary subset of it. It relates the two actual cost formulations without supplying the needed ordinary-prime upper.
