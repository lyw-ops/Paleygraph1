# Review of the physical secant response

The [returned draft](api-astra-overflow-122.txt) gives the exact adjacent secant identity on a common analytic sheet. Its counting-norm estimate (D) is valid with separate bounds at the two actual depths. One can retain the factor \(1/2\) by integrating the linear Taylor bound in the secant parameter. With \(\rho_j=\|K\Phi_t'(V_j)\|_{2\to2}\) and \(a_j=\|R_j\|_\infty\), this gives
\[
\|R_{m+2}\|_{2,n}
\le \prod_{j=m}^{m+1}(\rho_j+\kappa_j a_j/2)\,\|R_m\|_{2,n}.
\]
The curvature estimate is conditional on the two genuine segments remaining on their designated analytic sheets.

At height 600 the first actual segment can be controlled for every eligible \(n\ge10^{30}\). The existing [physical prefix bounds](astra-source-88.md) give \(\rho_{600}<0.51358\) and \(\|V_{600}\|_\infty<4.768\) on \(Q\). The [outgoing residual bound](phase-action-84.md) gives \(\|R_{600}\|_\infty<0.011\). On the first segment \(|z|<4.779\), so the bulk radicand has real part at least \(4L-4.779^2>40.62\), where \(L=2031/128-2^{-17}\). The bulk curvature is bounded by \(4\sup_Q|t|/(4L-4.779^2)^{3/2}<0.246\). At the mark the same bound \(0.246\) follows from \(4n/(4n-4.779^2)^{3/2}\). The sharpened secant norm is then at most \(0.51358+0.246(0.011)/2<0.515\). This deduction uses a fixed-height outward input on the original square and holds without an upper cutoff on \(n\). It bounds \(R_{601}\) in normalized second norm. The second segment requires its own coordinate control.

With the input numbers in (E), the unsharpened expression is below one when \(\kappa_{600}<44.3633\ldots\). The corrected expression with the factor \(1/2\) permits \(\kappa_{600}<88.7266\ldots\). The raw threshold \(86.3\) does not follow from (E). The repeated height-600 factor in (G) requires control of \(\rho_{601}\) and \(a_{601}\) too. Curvature on both segments alone does not supply the repeated values. The marked curvature has magnitude \(4n/|4n+W_0^2|^{3/2}\). Its asserted \(O(n^{-1/2})\) bound requires a lower bound of order \(n\) on the marked radicand. The square of the quoted fixed-depth absolute packet price is just an accounting comparison. No upper on the signed actual two-step product or lower on its norm follows from that square.

The independent [frozen orbit estimate](cold-frozen-orbit-transfer-122.md) uses shifted signed resolvents to propagate the full nonlinear Picard trajectory. The same note transfers corrected predictors with only the older endpoint's entry estimate. Both are conditional and leave the moving starter and prime-uniform arithmetic bounds open. The [completion receipt](api-astra-122-receipt.json) records the gateway's matching model label and token usage.
