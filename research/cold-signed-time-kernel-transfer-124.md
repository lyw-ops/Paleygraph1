# Signed transfer for the actual varying cold derivative kernels

Use the physical square \(Q\) of [Round 122](cold-frozen-orbit-transfer-122.md). Fix \(t\in Q\) and a genuine reference derivative \(D=\operatorname{diag}\Phi_t'(V)\), and put \(B=KD\). Let \(D_i\) be the actual derivatives at subsequent physical predictors, or the actual adjacent secant diagonals on segments in the common physical sheets. Use \(B_i=KD_i\) and \(E_i=D_i-D\). All bounds below are uniform on \(Q\). Suppose the reference and every segment or endpoint used satisfy \(\|B\|_{2\to2},\|B_i\|_{2\to2}\le q<1\). Write \(\rho_E=\sup_i\|(E_{i,xx})_x\|_{2,n}\) for the normalized second-norm bound of the diagonal displacement.

Define the frozen coefficients \(A_\ell=B^\ell K\) for \(\ell\ge0\), and the actual kernels
\[
 P_{b,a}=B_{b-1}\cdots B_a K,\qquad P_{a,a}=K.
\]
The rightmost \(K\) delivers a source in the physical coordinates. An empty product has counting \(2\to2\) norm at most one, and \(\|P_{b,a}\|_{2\to2}\le q^{b-a}\).

## One signed insertion and a quadratic remainder

Telescoping the actual product against the frozen product, first with all frozen factors to the left of the change and then with all frozen factors to the right of the change, gives
\[
\begin{aligned}
P_{b,a}={}& A_{b-a}+\mathcal L_{b,a}+\mathcal R_{b,a},\\
\mathcal L_{b,a}={}&\sum_{i=a}^{b-1} A_{b-1-i}E_i A_{i-a},\\
\mathcal R_{b,a}={}&\sum_{a\le h<i<b}
 A_{b-1-i}E_i P_{i,h+1} E_h A_{h-a}.
\end{aligned}                                                       \tag{1}
\]
Indeed the first telescoping leaves \(A_{b-1-i}E_iP_{i,a}\). In that term use \(P_{i,a}=A_{i-a}+\sum_{h=a}^{i-1} P_{i,h+1}E_h A_{h-a}\). The ordered sums in (1) hold without any commutation between different diagonals.

Assume \(\sum_{\ell\ge0}\|A_\ell\|_{\max}\le\Delta\). At each quadratic summand of (1) the counting second norms of its left row and right column are at most \(\|A_{b-1-i}\|_{\max}\sqrt n\,\rho_E\) and \(\|A_{h-a}\|_{\max}\sqrt n\,\rho_E\). The inner kernel costs at most \(q^{i-h-1}\). Summing as a convolution of these three bounds gives
\[
 \sup_a\sum_{b\ge a}\|\mathcal R_{b,a}\|_{\max}
     \le \frac{n\rho_E^2\Delta^2}{1-q},\qquad
 \sup_b\sum_{a\le b}\|\mathcal R_{b,a}\|_{\max}
     \le \frac{n\rho_E^2\Delta^2}{1-q}.                               \tag{2}
\]
For the first bound the indices \(b-1-i,i-h-1,h-a\) range independently over their nonnegative values when the whole sum over \(b\) is taken, with the same statement after summing over \(a\) for fixed \(b\). Truncating to a supplied finite time window only removes nonnegative summands of the majorant.

Thus if \(\Delta=O(n^{-\beta})\), \(n^{1-\beta}\rho_E^2=O(1)\), and the signed \(\mathcal L_{b,a}\) has summed entry price \(O(n^{-\beta})\) in one of these directions, the actual family \(P_{b,a}\) has the same summed bound in that direction. The signed input is one insertion tested with frozen factors only. The genuinely changing intermediate family in (2) needs only its counting contraction. If the \(D_i\) are all equal to a new frozen diagonal, both statements give the shifted-tail transfer at the new diagonal with the same exponent. This extends the zero-shift consequence of [Round 105](frozen-entry-transfer-105.md) to all shifts and to nonconstant sequences without multiplying the quadratic error by a time cutoff.

For example, the bound with fixed \(b\) gives a direct Duhamel estimate for any forcing \(G_i\) in the recurrence \(u_{i+1}=B_i u_i+K G_i\), \(u_a=0\). If its full actual summed price is \(O(n^{-\beta})\), then
\[
 \|u_b\|_\infty\le \sum_{i=a}^{b-1}\|P_{b,i+1}G_i\|_\infty
      \ll n^{1-\beta}\sup_{a\le i<b}\|G_i\|_{1,n}.
\]
This applies to actual secant products if the stated resources hold for those secants. On common curvature disks for the rooted physical orbit, a whole segment of second-norm contraction starting with residual \(r\) gives \(\rho_E\ll r/(1-q)\) by integrating the derivative. It still requires the signed first-insertion price at that reference and a compatible residual scale.

## Current fixed-height input and the arithmetic test

At the verified fixed height \(600\), [Round 96](shifted-resolvent-96.md) gives \(\|A_\ell\|_{\max}\ll n^{-1/2}1.048^\ell\) and also \(\|A_\ell\|_{2\to2}\le0.514^\ell\). Summing the first bound up to \(\lfloor\log n/(2\log(1.048/0.514))\rfloor\) and the counting bound thereafter gives \(\Delta=O(n^{-0.467})\). At fixed heights \(100,250\), the strict absolute column contraction instead gives \(\Delta=O(n^{-1/2})\). These deductions concern the fixed reference and do not give \(\rho_E=o(n^{-(1-\beta)/2})\) at height 600.

The linear test allows a separate summation-coordinate exception budget. If \(E_i^{\rm exc}\) is supported on a field- and time-dependent set of size \(O(n^\beta)\), with uniformly bounded entries, then its entire contribution to each of the two summed linear prices is \(O(n^{-\beta})\). In fact each insertion costs at most \(O(n^\beta)\|A_{b-1-i}\|_{\max}\|A_{i-a}\|_{\max}\), and summing gives \(O(n^\beta\Delta^2)\). The remaining signed sum uses the actual \(E_i-E_i^{\rm exc}\). This budget covers the mark and other specified exceptions while leaving their potentially nonzero signs in the physical kernel and in the counting contraction.

The two frozen powers in the linear test can each be cut at
\[
 J=\left\lceil\frac{\beta\log n}{2|\log q|}\right\rceil .
\]
In fact for \(v\ge J\),
\(\|A_u E_i A_v\|_{\max}\le \|A_u\|_{\max}\sqrt n\,\rho_E q^v\), by the counting second norm of a row of \(A_u E_i\). The transposed estimate applies for \(u\ge J\). Summing over \(u,v\) gives a bound \(2\Delta\sqrt n\,\rho_E q^J/(1-q)\) for the total price of all terms removed, with either endpoint fixed. This is \(o(n^{-\beta})\) when the reference has \(\Delta=O(n^{-\beta})\) and \(n^{(1-\beta)/2}\rho_E\to0\). The cutoff restricts two frozen factors in each insertion. It places no upper bound on actual times \(a,b\) over the supplied admissible sequence.

The transfer provides a concrete signed test for the actual variable products. A growing starter with the needed residual and an arithmetic estimate for the true interior insertion remain open. The actual stationary mark and a common cold domain do not follow from the fixed-height prices.
