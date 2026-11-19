# A fourth-moment Newton test and 600 actual marked returns

Let \(a=2031/128\), \(D=\{|t-a|<1/4\}\), \(Q=\{|\Re t-a|,|\Im t|<2^{-17}\}\), and \(n=(q-1)/2\). For eligible primes and prime squares with \(10^{30}\le n\le 10^{307}\), the **physical** stationary row is holomorphic throughout \(Q\) and its mark satisfies \(|m_q|\le 3/\sqrt n\). On the real interval of \(Q\), for unbounded sizes,
\[
 \limsup_{q\to\infty}\ \sup_{|t-a|<2^{-17},\ t\in\mathbb R}|m_q(t)|<4\cdot10^{-170}.
\]
The size ceiling and the positive limiting tolerance are different conclusions. A common complex crossing for unbounded primes, decay of the mark at this floor, and the ordinary-theta limit remain open. The earlier wide disks retain their original size ranges. [Round 75](astra-fourth-75.md)

## A signed linear solve on the wider disk

Use counting norms, \(T_t(W)=K\Phi_t(W)\), \(F_t(x)=\sqrt{4t+x^2}\), and \(F_n\) at the actual mark. All roots use the branch positive on the real axis. Let \(W,h\) be real-on-real holomorphic rows on \(D\), and suppose uniformly
\[
 \|W\|_\infty\le5,\quad \|\Im W\|_\infty\le 2.2,\quad
 \|h\|_4\le1,\quad
 \|r-(I-KD_W)h\|_2\le1/32,
 \qquad r=T_t(W)-W,\quad D_W=\operatorname{diag}\Phi_t'(W).
\]
For every sufficiently large field these hypotheses certify the actual stationary branch on the whole disk. In particular the exact correction \(h=(I-KD_W)^{-1}r\) is a well-defined holomorphic row before making the fourth-moment test. The bulk derivative is bounded by \(3/5\) on the predictor region and the marked derivative is smaller, so the inverse has counting operator norm at most \(5/2\).

Indeed, write \(L=a-1/4\), \(U=a+1/4\). On the coordinate segments \(W+sh\), \(0\le s\le1\), the imaginary part has modulus at most 3.2. The bulk second derivative is \(4t/(4t+x^2)^{3/2}\), giving the Taylor bound
\[
 \|T_t(W+h)-T_t(W)-KD_Wh\|_2
 \le \frac{2U}{(4L-3.2^2)^{3/2}}\,\|h\|_4^2
 <\frac9{100}\|h\|_4^2.
\]
Here \(K\) contracts the counting norm. At the mark the corresponding constant is \(2n/(4n-3.2^2)^{3/2}\), smaller for large \(n\). The residual at \(W+h\) is below \(1/8\). On its closed counting ball of radius \(1/2\) the modulus is at most 6.5 and the imaginary part at most 3.7. With modulus cap \(M\) and imaginary cap \(b\), the derivative bound \(M/(4L-2b^2+M^2)^{1/2}\) follows from \(\Re(4t+x^2)\ge4L+|x|^2-2b^2\). Here it is below \(3/4\). The ball maps strictly inside itself, and Picard convergence gives the holomorphic fixed row. The positive complementary factors at real \(t\) identify the physical solution. Its marked log is \(\operatorname{arsinh}(V_0/(2\sqrt n))\), with modulus less than \(3.3/\sqrt n\) eventually. [Positive identification and counting contraction](marked-domain-53.md)

A sharper signed test is available if a few large fourth-moment contributions dominate. With \(p_i=t\) on the bulk and \(p_0=n\), put
\[
 B_i=\frac{(1-D_{W,i}^2)h_i^2}
 {F_{p_i}(W_i+h_i)+F_{p_i}(W_i)+D_{W,i}h_i}.
\]
This is the exact quadratic remainder by a difference of squares, interpreted by analytic continuation at removable cases. Since \(K^*K=I-J\) with \(J\) the projection onto constants, \(\|KB\|_2=\|(I-J)B\|_2\) also for complex rows. One may replace the fourth-moment hypothesis by the two conditions that \(W+h\) satisfies the preceding caps 6 and 3.2, and \(\|(I-J)B\|_2+\|r-(I-KD_W)h\|_2<1/8\). The coordinatewise segment stays inside the same root region. The exact polynomial numerator uses \(h_i^2\), including its phase.

The change of scale is attained on actual Paley operators. On the established warm rectangles inside \(D\), let \(V^*\) be their physical row, with modulus \(<4.654\) and imaginary cap \(<1.84\), by subtracting the real Jacobi seed from the packet bound. In cyclic order set \(e_j=(1/4)n^{-1/4}\cos(2\pi j/n)\) and take \(W=V^*+e\). It is even and mean zero. Here \(\|e\|_4\le1/4\) and \(\|e\|_2=n^{1/4}/(4\sqrt2)\) for \(n>2\). The original counting residual is at least \((1-3/5)\|e\|_2\), by the contraction on the segment. Taylor expansion from \(W\) to \(W-e\) shows that the exact linear correction differs from \(-e\) in counting second norm by at most \((5/2)(9/100)\|e\|_4^2\). Hence its counting fourth norm is \(<1\) for every such field. This example uses the existing warm solution to distinguish the two tests. The unknown cold predictor is a separate problem. [Warm physical row](astra-fourth-75.md)

## A finite comparison for the complete nine-center predictor

Start \(V_0\) at the [round-65 nine-center row](astra-joint-65.md), then use the **exact** map \(V_{j+1}=T_t(V_j)\) at every coordinate. The distinguished center coefficients depend on \(t\) as in that construction. Its degree-28 arithmetic kernels include the root subtractions, both fourth-mode symplectic traces, and the exceptional fourth column with coefficient \(2(1-8/q+7/q^2)\) per paired amplitude. The seven center amplitudes all have modulus below one on the closed square. The following interval argument bounds \(V_j\) through height 600 without a steady packet cap.

Use the round-64 symmetric weight measure of the residual, with \(\eta=1/5\), and write \(h_k\) for its stored off-zero packet caps \(1\le k\le50\). A further off-zero residual has cosh-weighted mass at most \(\epsilon=5\cdot10^{-7}\). Packet \(k\) creates \(k-1\) units of zero weight per off-zero unit. Thus put
\[
 z_0=\sum_{k=1}^{50}(k-1)h_k+2.8\epsilon+10^{-8},\qquad
 C=z_0\delta_0+\sum_{k=1}^{50}\tfrac12 h_k(\delta_k+\delta_{-k}).
\]
The inequality \(k-1\le2.8\cosh(k/5)\) bounds the zero cost of the excess. The true full signed residual is dominated in the representation calculus. Begin at \(h=0\). At each step take the full degree-28 upper measures \(U_j\), \(0\le j\le28\), evaluated once on the whole closed square. The complete tilted norm of their core and residual descendants is bounded by
\[
 P=\sum_j \|U_j\|_\eta(\|C\|_\eta+\epsilon)^j.
\]
The tilted norm is multiplicative on symmetric positive convolutions. Truncate each power \(C^{*j}\) to \([-80,80]\) after **each** multiplication, start from \(\delta_0\), and also restrict each \(U_j\) to \([-80,80]\). Let \(d_k\), \(0\le k\le50\), be the one-sided coefficients of the sum of these restricted convolutions. All coefficients in these numerical upper polynomials are nonnegative. Thus \(d_0+2\sum_{k=1}^{50}d_k\cosh(k/5)\) prices a subset of the positive comparison calculation. Subtracting it from \(P\) charges every discarded path, including paths which leave the strip and return. This subtraction uses the *same positive upper polynomials* on both sides. It requires no lower bound on a physical coefficient. Add the unexpanded binomial orders from degree 30 using \(2\sqrt{|t|}|\binom{1/2}{15}|r^{15}/(1-r)\), with \(r\) the full tilted input norm squared divided by \(4\inf\Re t\). This is the inherited weighted-tail estimate. The resulting excess at every step is below \(394\cdot10^{-9}<\epsilon\). Use \(h'_k=2d_k\) with outward rounding and insert the true exceptional allowance \(10^{-12}\) into \(h'_1\). [Weighted packet calculation](astra-joint-64.md)

For this last allowance, the dimensional coefficient sum of the raw activation before transport is below 17 using the full input bound \(4.8\) and \(2\sqrt{|t|}(2-\sqrt{1-4.8^2/(4\inf\Re t)})\). All bad-lift corrections from it cost at most \(34\sqrt q/n\). The marked replacement \(F_n(V_{j,0})-2\sqrt n-F_t(V_{j,0})\) contributes at most \(11\sqrt q/n\). The seven named center identities contribute in total at most \(16\sqrt q/n\). Indeed \(K C_2\) and \(K(C_1Y)\) have column coefficients of modulus at most 2 and 1, the rank-four and rank-five corrections below 2 each, \(K(AB)\) has zero correction, and the dual-square and fourth-mode pairs have coefficients of modulus below 3 each. For the rank-five correction use \(n(s_A+s_B+q)/(4q^{5/2})\). Each of the four compact boundary eigenvalues at the specified lift has magnitude at most \(q^{-1/2}\), since no weight is zero, whence \(|s_A|,|s_B|\le4q^{3/2}\) after the \(q^2\) normalization. All amplitudes have modulus \(<1\). The sum fits in \(10^{-12}\) for \(n\ge10^{30}\), whose actual Jacobi scales lie in the seed enclosure. This pays the correction anew at each of the 600 updates. [Rank-five normalization](weighted-arithmetic-57.md) · [Nonzero boundary weights](rank-four-arithmetic-56.md) · [Uniform lift and marked correction](marked-domain-53.md)

The full coordinate bound, including the center and at most \(4\epsilon\) for residual coordinates outside the stored packets, is below 4.768 at each height. Subtracting the real Jacobi seed's representation mass gives an imaginary cap of 2. On the segments between consecutive iterates the bulk and marked derivatives are less than \(0.55\), and on real parameters less than \(0.52\). Thus
\[
 n^{-1/2}\|V_{600}-V_{599}\|_2
 \le9.6(0.55)^{599},\qquad
 n^{-1/2}\|V_{600}-V_{599}\|_2\le9.6(0.52)^{599}<10^{-169}\quad(t\text{ real}).
\]
For \(n\le10^{307}\) the complex unnormalized increment is below \(1/4\). On the radius-\(1/2\) counting ball at \(V_{600}\), use coordinate caps 5.3 and 2.5 for the modulus and imaginary part. This gives Lipschitz constant \(<2/3\), also on the preceding segment. The terminal residual is \(<1/6\). The resulting physical fixed row has \(|m_q|\le3/\sqrt n\).

For the real conclusion at unbounded size use the strictly positive trial factors \((\Phi_t(V_{599})\pm V_{600})/(2\sqrt n)\). The marked product is \(1+O(1/n)\), the trial marked log is \(O(1/\sqrt n)\), and the bulk products multiplied by \(n\) are \(t+(V_{599,i}^2-V_{600,i}^2)/4\). After normalizing by the marked product, the counting distance of the bulk square-root weights from their target is at most \(0.4\cdot 9.6(0.52)^{599}+O(1/n)\), by the difference-of-squares estimate with cap 4.8. The [marked square-root stability bound](marked-response.md) gives the stated uniform positive tolerance.

The fourth-moment criterion uses ordinary analytic inequalities, with its constants checked by rational arithmetic. The 600-step bound uses outward-rounded Arb192 numbers. There is no finite-field enumeration or floating fit in the certificate. [Replay](astra-predictor-76-check.py) · [Two records](astra-predictor-76-checks.jsonl)

1. On the width-\(2^{-17}\) square, apply the exact signed linear correction at \(V_{600}\). Bound its counting fourth norm by one or compute the centered norm of its exact squared remainder under the stated coordinate caps. Either bound closes the indicated test for unbounded sizes.
2. On \(D\), attempt the same correction at the round-75 30-step row. Certify the whole marked linear defect below \(1/32\) when truncating a signed solve. A normalized counting second moment alone leaves the growth of the fourth norm unresolved.
