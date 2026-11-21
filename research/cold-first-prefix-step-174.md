# An actual outgoing increment and a larger verified disk

Retain the true height-602 predictor, both lifts, the physical \(t_0=n\), and the original cold square \(Q\). Use the genuine base-pair packet price \(P_{5000}\) of [Rounds 126, 130 and 162](cold-height-602-frozen-kernel-162.md). It dominates the coordinate supremum and the dimension budget on these unshifted packets. The fixed estimates we need are
\[
 P_{5000}(E)<0.012,\qquad E=V_{602}-V_{601},\qquad
 \|KD_{601}\|_{P_{5000}}<1.048,\qquad
 \|KD_{602}\|_{P_{5000}}<1.066.
\]
The true \(V_{601}+sE\), and hence \(V_{602}\), have dimension bound \(4.823\).

## Nonlinear packet bound at the actual next two bases

For a true base row \(V\) and a direction \(U\) in the unshifted packet class with \(P_{5000}(U)\le A\), put
\[
 \mathcal T_V(U)=K\bigl(\Phi_t(V+U)-\Phi_t(V)-D_V U\bigr).
\]
When all \(V+sU\) have dimension bound \(M\), the even Taylor argument of Round 162 gives
\[
 P_{5000}(\mathcal T_V(U))
 \le \frac{2 A^2}{\sqrt N}(1+x/2)(1-x)^{-5/2}
       +O(n^{-1/2}A^2),\qquad
 N=4(2031/128-2^{-17}),\quad x=M^2/N.
\]
In the bulk, expand the curvature in powers of \((V+sU)^2/(4t)\), charge the \(2l+2\) factors in the boundary first moment at order \(l\), and use the factor 2 from the price and \(1/2\) from Taylor integration. The bad-character and physical-mark replacements use the same \(O(n^{-1/2}A^2)\) estimate with the actual marked radicand \(4n+z^2\). The bound is valid for arbitrarily close to optimal admissible representations. In the uses below, all dimension bounds are separated from \(\sqrt N\), and there is uniform strict slack in the numerical comparisons.

First use \(V=V_{601},U=E,M=4.823,A=0.012\). The main bound for \(P_{5000}(\mathcal T_{V_{601}}(E))\) is less than \(0.000140\), including the eventual vanishing error. Hence the actual outgoing increment \(R_{602}=V_{603}-V_{602}\) satisfies
\[
 P_{5000}(R_{602})<1.048(0.012)+0.000140<0.01272 .
\]
In particular the first outgoing step stays within the radius \(0.025\) of Round 173 with uniform slack.

Next use the frozen base \(V=V_{602}\) and \(P_{5000}(U)\le0.05\). Then \(M=4.873\) suffices, and the displayed scalar coefficient of \(A^2\), excluding its vanishing term, is strictly below one. The exact rational comparisons can be made by squaring both positive sides. Therefore the actual displacement \(U_j=V_{602+j}-V_{602}\) obeys
\[
 P_{5000}(U_{j+1})
 \le P_{5000}(R_{602})+1.066 P_{5000}(U_j)+P_{5000}(U_j)^2
\]
while the right-side input price is at most \(0.05\), for the fixed steps considered here. In particular the first, second and third actual displacements have prices less than \(0.01272,\ 0.02645,\ 0.04162\), respectively. The latter two fit the enlarged disk below. The inequality is a finite unsigned upper, not a growing-depth convergence estimate.

## Enlarged physical tube with the same logarithmic cutoff

At the fixed center \(V_{602}\) take coordinate disks of radius \(0.05\), instead of \(0.025\). The actual bulk coordinate modulus is then at most \(4.841\). The comparison
\[
 [4(t_c+2^{-16})]^2 < (0.255)^2(N-4.841^2)^3,\qquad t_c=2031/128,
\]
bounds the curvature by \(0.255\) on these disks. At the mark the curvature again tends to zero. The scalar derivative is therefore below \(0.518+0.05(0.255)<q=0.535\), so counting norm is contractive on the full polydisk. The exact inequality \(q^8<2^{-7}\) preserves the cutoff \(602+\lceil(4/7)\log_2 n\rceil\) and the conditional tail argument of Round 173, now with radius \(0.05\). The first three displacements have been proved inside these disks. Proving the remaining growing prefix with terminal clearance is still required. No uniform continuation or derivative-transfer estimate is inferred here.
