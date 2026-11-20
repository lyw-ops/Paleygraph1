# The actual cold quadratic insertion and a sharper height-601 rate

Use \(Q,V=V_{600},R=V_{601}-V_{600},D=D_{600}\) from [Round 126](cold-actual-first-insertion-126.md). Put \(D'=D_{601}\), \(E=D'-D\), \(A_u=(KD)^uK\), and \(A'_v=(KD')^vK\). Throughout, \(\varepsilon=0.011\) exceeds the actual packet price of \(R\), \(M=4.811\) bounds the dimension-cost representations of \(V\) and \(V+R\), \(N=4(2031/128-2^{-17})\), and \(x=M^2/N<1\). The argument uses the same physical sheets and is uniform on \(Q\) for sufficiently large eligible primes.

## First-moment price of the actual derivative difference

On unmarked coordinates use the telescoping series of Round 126 for \(E\). For each word use the pooled base-character weight measure after expanding the two lift choices independently, scaled by the absolute coefficient. Let \(m_0,m_1\) denote bounds for the total mass and the first absolute moment of the resulting positive measure. They include all terms of the analytic series. For a word of arity \(2\ell+1\), one factor is \(R\), and the remaining \(2\ell\) are taken from \(V\) or \(V+R\). The dimension mass in this arity is at most \(\varepsilon(2\ell+1)M^{2\ell}\) before the binomial coefficient. Each negative term has first absolute moment equal to dimension when pooled over the base pair. This would give a factor \(2\ell+1\) to estimate the first absolute moment by the triangle inequality.

There is a uniform saving in each pair of the \(2\ell\) non-residual factors. Use their actual decompositions with the common real Jacobi seed \(S=2\sqrt n\,Ke_0\), whose rank-one field has dimension mass \(s_n=2\sqrt{p/n}\ge\sqrt8\). This seed is a designated summand in the [physical prefix price](astra-predictor-76.md) and adding \(R\) leaves it a designated summand of the expanded \(V+R\). Its pooled normalized weights are equiprobable \(-1,+1\). On the seed-seed part of a paired factor, the mean absolute sum is \(1\), whereas the separate moments sum to \(2\). Thus for each pair the triangle bound improves by \(s_n^2\) times the mass of the other factors. This uses independent lift choices. It is a saving in an upper weight comparison, without subtracting an unsigned quantity from a physical signed trace. Concretely, if the paired factor masses are \(c_1,c_2\), the pair costs at most \(2c_1c_2-s_n^2\). This is nonnegative and increasing in both masses on \(c_i\ge s_n\), so after the saving all the individual mass upper bounds can be replaced by \(M\).

Pair the \(2\ell\) non-residual factors and then apply the first-moment triangle bound across pairs and the residual. Summation using \(c_\ell=\binom{2\ell}{\ell}/4^\ell\) gives
\[
\begin{aligned}
 m_0&\le \frac{\varepsilon}{\sqrt N}(1-x)^{-3/2}<0.002727,\\
 m_1&\le \frac{\varepsilon}{\sqrt N}
           \bigl(1+2x-12/N\bigr)(1-x)^{-5/2}<0.006611 .
\end{aligned}                                                      \tag{1}
\]
Indeed the full first moment before pairing uses \((2\ell+1)^2\), whose generating function with \(c_\ell\) is \((1+2x)(1-x)^{-5/2}\). The \(\ell\) pair savings sum to \(s_n^2 M^{-2}\sum_\ell c_\ell (2\ell+1)\ell x^\ell\), with \(s_n^2\ge8\) and the latter series equal to \((3/2)x(1-x)^{-5/2}\). The estimates and the series are for the actual subtractive difference of the two derivatives.

For a negative input in the translated packet class of [Round 96](shifted-resolvent-96.md), let \(P_\Lambda=A_{\rm base}+\Lambda b\), with \(\Lambda=5000\) and \(b\) its off-base first moment. In the pricing formula of [Round 82](astra-adjoint-82-check.py), \(w\mapsto\pi(|w|)\) is \(2\)-Lipschitz, including the affine extension. Comparing the base cost of a convolved input weight \(w\) with \(\pi(|w+z|)\le\pi(|w|)+2|z|\) yields
\[
 A_{\rm base}'\le m_0 A_{\rm base}+2d\,m_1,
\]
where \(d\) is the input dimension. The price includes the post-\(K\) twist: it permutes the matching positive weights within each character pair and leaves negative weights in that pair. The multiplier has zero weights off the base pair, so \(b'\le m_0 b\). Since \(d\le P_\Lambda\), the geometric price of \(KE\) is at most \((m_0+2m_1)P_\Lambda\). The corrections at bad characters and the marked-only derivative difference are supported on the base and input translated pair before applying \(K\), and cost \(O_\Lambda(\varepsilon n^{-1/2})P_\Lambda\) after \(K\), as in Round 126. In particular,
\[
 \|KD'\|_{\rm translated\ price}
 \le 1.046434(1+2/5000)+0.002727+2(0.006611)+O_\Lambda(n^{-1/2})
 <1.063
 \tag{2}
\]
eventually. This estimate keeps the boundary pair for an input source unchanged.

## Counting rate using the actual seed-centered disk

By [Round 88](astra-source-88.md) and \(\|R\|_\infty<0.011\), the actual \(V_{601}\) stays within \(B=1.951\) of the real seed \(S\), with \(\|S\|_\infty\le s=2.828428\) for the stated primes. At an ordinate of imaginary part \(y\), set \(u=\sqrt{1-y^2/B^2}\). For \(v=V_{601,i}\),
\[
 |v|^2\le F(u)=s^2+B^2+2sBu,\qquad
 \Re(4t_i+v^2)\ge |v|^2+C(u),\qquad
 C(u)=N-2B^2(1-u^2)>0 .
\]
Here \(t_i=t\) off the mark and \(t_0=n\). The derivative square is at most \(F/(F+C)\), increasing in \(u\) because \(2sB(N-2B^2)>4B^2(s+B)^2\). At the endpoint \(u=1\) this gives
\[
 \|KD'\|_{2\to2}\le \frac{s+B}{\sqrt{N+(s+B)^2}}<0.5145.
 \tag{3}
\]
The inequalities in (1)–(3) reduce to rational comparisons by squaring the positive expressions.

## Sum of the actual signed quadratic insertions

Fix a physical source \(a\). Before pairing with the other column, represent
\[
 H=A'_v E A_u e_a=(KD')^v K E A_u e_a .
\]
Round 96 bounds the price of the input \(A_u e_a\) by \(O(n^{-1/2}(1.048)^u)\). The just-proved price of \(KE\) is \(O(\varepsilon)\), and the new power rate is below \(1.063\). Therefore \(H\) has a genuine negative representation of price \(O(\varepsilon n^{-1/2}(1.048)^u(1.063)^v)\) on the base pair and the original \(a\)-pair. This step does not introduce a new translated fiber for each summation coordinate. Pair \(H\) against \(E A_w e_b\). The arithmetic word now uses only the base, \(a\)- and \(b\)-pairs. The odd-arity trace estimate and the summable word costs of Round 126, plus the direct marked correction, yield
\[
 \|A_w E A'_v E A_u\|_{\max}
 \ll \varepsilon^2 \min\!\left\{
       n^{-1/2}(1.048)^{u+w}(1.063)^v,\
       (0.514)^{u+w}(0.5145)^v
                      \right\}.                                   \tag{4}
\]
As in the first insertion, the \(n^{-1/2}\) bound arises after multiplying the normalized trace mean by \(n\) to form a physical matrix entry. The second bound in (4) uses counting second norms and \(\|E\|_\infty=O(\varepsilon)\), with no prime decay assumed for \(\|R\|_{2,n}\).

Let \(\beta=0.4579\). Bounding the minimum by the geometric mean with weight \(2\beta\) on its first argument produces an overall \(n^{-\beta}\) and three convergent geometric sums. The exact rational comparisons are
\[
 (1.048)^{4579}(0.514)^{421}<1,\qquad
 (1.063)^{4579}(0.5145)^{421}<1 .
\]
It follows that the entire actual sum of the quadratic insertion maximum entries is \(O(\varepsilon^2 n^{-0.4579})\). In the exact constant-diagonal identity by total power from [Round 124](cold-signed-time-kernel-transfer-124.md), the old kernel and the signed linear insertion already cost \(O(n^{-0.467})\). Thus \(\sum_j\|A'_j\|_{\max}=O(n^{-0.4579})\) on \(Q\). In particular the same estimate holds at every frozen shift of the genuine height-601 transported resolvent. An independent packet/counting split using (2)–(3) also gives this endpoint exponent.

The weaker direction in (4) is the long middle power. At counting rate \(0.5145\), this geometric summation method can retain \(0.467\) only if its middle price rate is less than \(0.5145^{-(1-0.934)/0.934}\), about \(1.04808\). The upper rate (2) cannot justify that condition. The result concerns the actual fixed transition and does not produce a compatible residual or confinement at growing height.
