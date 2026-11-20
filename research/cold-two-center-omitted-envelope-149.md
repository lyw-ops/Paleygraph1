# Removing all pure two-center words from the actual cold comparison

Keep the original closed cold square, physical mark \(t_0=n\), both boundary lifts, and \(P_{5000}\) norm. Fix the true heights \(h=601,602\) and use
\[
 A_h=K\,\operatorname{diag}(d_{t_i}(V_{h,i})),\qquad
 B_2=K\,\operatorname{diag}(d_{t_i}(S_i+\alpha Y_i))
\]
from the [whole two-center estimate](cold-higher-legendre-step-148.md). Then at both heights, uniformly for sufficiently large eligible primes,
\[
 \|A_h-B_2\|_{P_{5000}}<0.542 .
\]
The part linear in the total nonseed factors costs less than \(0.408\), and the part of total nonseed degree at least two costs less than \(0.134\).

## Exact word selection and positive bound

Write \(V_h=S+\alpha Y+H_h\), where \(H_h=\mathcal C_{\rm oth}+Y_h\) is the other actual fixed centers plus the actual height-\(h\) residual. Work first at good full Mellin characters. Expand the retained odd derivative polynomial through degree 27 in the seed and nonseed factors. The terms containing only \(S\) and \(\alpha Y\) cancel exactly in the difference. For each remaining word of total nonseed degree \(j\), use the signed seed-Laurent coefficient collection of [Round 136](cold-resummed-136.md). The same Laurent coefficient multiplies every fixed ordered \(j\)-word, so this selection commutes with the signed seed collection.

Use convolution of symmetric weight measures. Let \(a\) be the Round 136 amplitude upper and \(\mathfrak a=a(\delta_0+(\delta_{-2}+\delta_2)/2)\) the envelope of the fixed Legendre field. Construct \(\mathfrak h_h\) from the other fixed centers and retained residual at height \(h\), keeping the excess-zero charge. Thus \(\mathfrak a+\mathfrak h_h\) is the original retained nonseed envelope \(\beta_h\). A majorant for the selected words uses the positive recurrence
\[
 J_0=0,\qquad J_j=\beta_h*J_{j-1}+\mathfrak h_h*\mathfrak a^{*(j-1)} .
\]
The first term selects words with a previously chosen other factor and the second selects those with their first such factor in the new position. The retained row is \(\sum_{j=1}^{27}\gamma_j*J_j\), with \(\gamma_j\) the modulus of the already collected signed seed coefficients. Every convolution uses the exact integer weight before the common cutoff.

The neglected tilted residual at each height still contributes at most
\[
 j\varepsilon\|\gamma_j\|_{\rm tilt}(\|\beta_h\|_{\rm tilt}+\varepsilon)^{j-1}
\]
at degree \(j\), by the same subset bound as in Round 136. This accounts for every word using an unretained residual object. The absolute analytic tail \(0.0000407\) bounds the selected subset of all mixed words of analytic order at least 14. The exceptional and marked contribution is \(O_{5000}(n^{-1/2})\) relative price by the inherited lift and marked comparison, using an absolute summation over the selected subcollection of the original mixed words. The tail and repair treatment retains the actual \(t_0=n\).

## Translated price and remaining gap

The [outward replay](cold-two-center-omitted-envelope-149-check.py) forms the above positive recurrence and keeps \(|w|\le150\). It checks each translated base column, the affine limit, and the off-base first-moment price, using the Round 136 implementation. It charges the tilted overflow and residual by ten times their tilted mass. A strict finite comparison at 192-bit precision leaves room for the eventual marked and exceptional repairs. [Saved records](cold-two-center-omitted-envelope-149-checks.jsonl)

The direct positive bound improves the \(0.5592\) triangle bound from the two separately priced differences with the old linear baseline. On its first 12 weights the new retained comparison maps a fixed positive integer trial vector to more than \(0.4607\) times itself componentwise at both heights. The audit found the trial vector by midpoint iteration, and the checker verifies it outward with fixed integer inputs. This excludes reaching \(0.356\) by a coordinatewise monotone homogeneous reprice of this comparison. The actual signed derivative may cancel across the retained packets. Using \(\|A_{601}\|<1.048\) and \(\|B_2\|<0.644\), the paired triangle upper is \(0.542(1.048+0.644)=0.917064\), above the needed \(0.585\). A signed bound for the omission or the paired difference remains open, as do nonlinear confinement and the physical half-step.
