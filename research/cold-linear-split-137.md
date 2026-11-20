# Separate translated prices for the center and Picard parts

Take the original closed square of halfwidth \(2^{-17}\) centered at \(2031/128\), the two actual rows \(h=601,602\), and the marked floor \(t_0=n\), \(t_i=t\) away from zero. Write \(V_h=\mathcal C+Y_h\), where \(\mathcal C\) is the nine-center row fixed in the Picard envelope and contains the Jacobi seed \(S\). The linear remainder is the sum of the two physical multipliers
\[
 E_h^{(1)}=E_{\rm cen}+E_{{\rm res},h},\qquad
 E_{\rm cen}=\operatorname{diag}(d_{t_i}'(S_i)(\mathcal C_i-S_i)),\qquad
 E_{{\rm res},h}=\operatorname{diag}(d_{t_i}'(S_i)Y_{h,i}).
\]

For sufficiently large eligible primes, uniformly on this square, the translated price bounds are
\[
 \|K E_{\rm cen}\|_{P_{5000}}<0.267,
 \qquad \|K E_{{\rm res},h}\|_{P_{5000}}<0.260.
\]
In particular an actual signed center price below \(0.070\), with uniform strict slack, suffices for the \(0.472\) remainder target when retaining the \(0.260\) residual upper and the [\(0.142\) nonlinear upper](cold-resummed-136.md). An estimate below \(0.330\) for the **whole linear term** also suffices. The center price alone needs its own smaller budget when the residual is charged separately. Either budget concerns fixed rows and leaves the invariant-ball and half-step margins open.

## Outward calculation

The [same-Laurent-exponent collection](cold-resummed-136.md) at nonseed degree one gives a common positive folded weight row \(\gamma_1\) after taking absolute values. Convolve it separately with the eight retained center weights and the retained physical \(Y_h\) envelope. The residual includes the existing excess-zero charge. The actual height-601 envelope is carried from the [verified prefix](cold-combined-height-130.md), and the actual height-602 envelope uses the verified extra step in the Round 136 replay. Both convolutions have full finite weight support inside the cut of Round 136.

The translated column test of Round 136 applies separately to each convolution. Only the residual has discarded off-zero weight mass. Its tilted cost is bounded by \(10\varepsilon\|\gamma_1\|_{\rm tilt}\) with \(\varepsilon=5\cdot10^{-7}\). Each piece can charge the entire \(0.0000407\) analytic tail of [Round 135](cold-remainder-135.md) independently, since before absolute binomial and word charges its terms form a subset of the mixed words in that tail. The full analytic radius bound for the actual marked rows applies to both subsets. The uniform exceptional-lift and physical marked-floor repair remains \(O_{5000}(n^{-1/2})\) separately, because both unresummed absolute coefficient-dimension series are dominated by the original convergent series. The finite outward comparisons are strict and absorb this eventual repair.

The [checker](cold-linear-split-137-check.py) reuses the Round 136 arithmetic and tests two additional outward bounds in 192-bit Arb with python-flint 0.9.0. The [saved records](cold-linear-split-137-checks.jsonl) are eventual physical uppers from a positive comparison. A higher positive rate, or failure to improve either part in this comparison, would give no signed lower for the actual sum. The earlier jointly priced bound \(0.527\) for the linear sum remains sharper than adding the two decimal ceilings here.
