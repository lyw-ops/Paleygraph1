# Actual physical incidence with a small or sparse slope layer

Use the original physical square sum and the true favorable sign of [Round 156](ordinary-sign-selective-completion-156.md). On a selected block require \(A_x,A_y\in\mathcal A\) and \(C_x,C_y\in\mathcal B\), where
\[
 A_x=1-vx,\qquad C_x=1-vux=1-u+uA_x
\]
and similarly for \(y\). Retain \(x,y\in Q\), \(u\in Q\setminus\{1\}\), \(x\ne y\), four nonzero \(f\) factors, and the true slope \(t=C_yA_x/(C_xA_y)\in Q\setminus\{1\}\) on its favorable sign. Here \(v\ne0\), and \(1\) cannot occur among these four vertex arguments since \(x,y,u\ne0\). Count only genuine contributing triples. Arbitrary additional fixed entry restrictions decrease their number.

For each fixed \(t\), the fiber count \(N_t\) satisfies
\[
 N_t\le\min\{|\mathcal A|^2,|\mathcal B|^2\}.
\]
For fixed distinct \(A_x,A_y\) the equation for \(u\) is
\[
 t A_y(1-u+uA_x)=A_x(1-u+uA_y).
\]
Its two coefficients cannot both vanish, since all arguments are nonzero and this would force \(A_x=A_y\). Thus it admits at most one \(u\), then \(x,y\) are fixed. Conversely fix distinct \(C_x,C_y\) and use the inverse map with \(u^{-1}\) and \(t^{-1}\). Without fixing \(t\), assigning \((A_x,A_y,C_x)\) determines \(u\) because \(A_x\ne1\), and reversing gives the symmetric bound
\[
 \sum_t N_t\le |\mathcal A|\,|\mathcal B|\min\{|\mathcal A|,|\mathcal B|\}.
\]
These are counts in the exact original physical variables, with no Fourier clean-locus claim.

For any slope subset \(D\), let \(m_D=\sup_{t\in D}|f(t)|\). The absolute value of the actual restricted sum is at most
\[
 \min\!\left\{
  \min(|\mathcal A|^2,|\mathcal B|^2)\sum_{t\in D}|f(t)|, 
  |\mathcal A|\,|\mathcal B|\min(|\mathcal A|,|\mathcal B|)\,m_D
 \right\}.
\]
This uses the true five factors and the bound \(|f|\le1\) only on the other four. In particular fixed positive squared thresholds at all four vertices give both cardinalities \(O(\sqrt p)\) by Parseval. On this specific block, either \(m_D=O(p^{-1/2})\) or bounded counting first mass of \(f|_D\) suffices for \(O(p)\). More generally on a dyadic slope band with \(|f|^2\le p^{-\sigma}\) this yields \(O(p^{(3-\sigma)/2})\) on the two fixed high vertex layers. This adds a cut with a single low-amplitude slope on this block, which is not covered by the multi-factor flattening cutoff of [Round 160](ordinary-rank-two-slope-orthogonality-160.md). The moderate slope band with growing first mass and \(\sigma<1\) remains open. When the two fixed squared thresholds sum to more than one, the sign is already forced by the four true pair signs of [Round 160](ordinary-matched-physical-truncation-160.md), so this particular mask itself gives no further oscillation.

## The remaining off-diagonal shifted-layer energy

Let \(X=\{x\in Q:1-vx\in\mathcal A\}\), \(Y=\{x\in Q:1-vx\in\mathcal B\}\), and \(h(u)=|X\cap u^{-1}Y|\). Before imposing the slope mask, the off-diagonal count for the four physical levels is exactly \(\sum_{u\in Q\setminus\{1\}}h(u)(h(u)-1)\). The two-threshold sign information permits retention of the actual sign restriction on \(u\) when it is forced. For a slope band with \(|f(t)|^2\le p^{-\sigma}\), an \(O(p^{1+\sigma/2})\) upper on this off-diagonal count suffices for the \(O(p)\) block, even after arbitrary slope restrictions and while retaining all weights.

With the unnormalized Mellin transform on \(Q\), the total \(\sum_u h(u)^2\) is
\[
 \frac1n\sum_\eta |\widehat{1_X}(\eta)|^2\,|\widehat{1_Y}(\eta)|^2.
\]
This follows by multiplicative correlation and Parseval. The constant term is \(O(p)\) at the fixed high thresholds, so a sufficient new bound concerns the excess nontrivial spectrum of the actual two shifted layers. An estimate on unshifted layer sizes or the fixed favorable sign alone does not supply it.
