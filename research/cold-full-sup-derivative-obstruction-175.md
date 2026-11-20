# The full coordinate-supremum derivative grows at the true cold center

Use the actual physical height \(602\), both lifts, \(t_0=n\), and the original complex square of [Round 174](cold-first-prefix-step-174.md). The full \(\ell^\infty\to\ell^\infty\) estimate proposed in the gateway draft fails for the actual matrix, already at the disk center \(V_{602}\). In fact
\[
 \|K D_{602}\|_{\infty\to\infty}\asymp\sqrt n
\]
uniformly on the original square for sufficiently large eligible primes. This assertion concerns the full coordinate space and leaves the behavior on the true signed residuals open.

The genuine rows satisfy \(V_{602}=K a\), \(a_i=\sqrt{4t_i+V_{601,i}^2}\), with the physical sheets. Both \(V_{601}\) and \(V_{602}\) are uniformly bounded. At the mark \(a_0=2\sqrt n+O(n^{-1/2})\), while all other \(a_i=O(1)\), so their common coordinate mean \(\bar a=n^{-1}\sum_i a_i\) is \(O(1)\). By symmetry and \(K^2=I-P_1\) from [Round 96](shifted-resolvent-96.md),
\[
 \sum_i |V_{602,i}|^2=\sum_i |a_i-\bar a|^2
 \ge |a_0-\bar a|^2\ge4n-C_0\sqrt n.
\]
The bounded marked coordinate of \(V_{602}\) can be discarded in this lower bound. On all remaining coordinates,
\[
 |D_{602,i}|=\frac{|V_{602,i}|}{|\sqrt{4t+V_{602,i}^2}|}
 \ge C^{-1}|V_{602,i}|
\]
for a uniform upper bound \(C\) on those bulk radical moduli. Thus \(\sum_i|D_{602,i}|^2\gg n\).

Each column of \(K\) has squared Euclidean norm \(1-1/n\). Consequently the squared Frobenius norm of \(KD_{602}\) equals \((1-1/n)\sum_i|D_{602,i}|^2\gg n\), so at least one row has squared Euclidean norm bounded below. The genuine Jacobi entry bound \(|K_{ij}|\le\sqrt p/n\) and the bounded scalar derivative make its largest entry \(O(n^{-1/2})\). Its absolute row sum is therefore \(\gg\sqrt n\). The opposite bound follows from the counting second-norm contraction and Cauchy–Schwarz. Matrix row sums give the induced infinity norm, allowing arbitrary complex input phases in that norm.

The same order holds when the input is restricted to mean zero. Put \(B=KD_{602}\) and \(P=I-P_1\). Then \(\|BP\|_{\mathrm F}^2=\|B\|_{\mathrm F}^2-\|BP_1\|_{\mathrm F}^2\gg n\), since \(BP_1\) has rank at most one and bounded second-norm operator norm. The entries of \(BP\) are still \(O(n^{-1/2})\), as each is an entry of \(B\) minus its row mean. Apply the same row argument to \(BP\) and use \(\|P\|_{\infty\to\infty}\le2\).

Thus contraction in the full coordinate norm cannot follow from this true derivative. A rate on an invariant price class dominating the coordinate norm would be different. Starting with only \(a_*=0.01272\) and radius \(0.05\), the geometric-series test for one-step uniform rate \(q_*\) needs \(a_* /(1-q_*)<0.05\), equivalently \(q_*<0.7456\). A proof with larger \(q_*<1\) would also need a further bound, for example a smaller genuine outgoing price or a signed prefix sum with clearance.
