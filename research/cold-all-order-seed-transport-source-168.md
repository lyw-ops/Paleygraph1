# All even seed units and the surviving seed moments

Keep \(R=V_{601}-V_{600}\), \(V_s=V_{600}+sR\), the two actual lifts, the original square, and physical \(t_0=n=(p-1)/2\). Use \(B=KD_{602}\), \(\varepsilon=0.011\), \(M=4.811\), \(N=4(2031/128-2^{-17})\), \(x=M^2/N\) and the bulk Taylor expansion of [Round 165](cold-paired-Taylor-source-saving-165.md). Write \(s_n=2\sqrt{p/n}\), \(c_l=4^{-l}\binom{2l}{l}\), \(b_l=(2l+1)c_l\). On good coordinates, the true common seed has the Laurent expression \(S=s_n(z+z^{-1})/2\) as in [Round 167](cold-common-seed-Taylor-unit-167.md).

For each order \(l\), the pure seed branch of \(V_s^{2l}\) has unit coefficient \(s_n^{2l}c_l\). Integration is independent of \(s\) for these branches. They collect with the same actual \(R^2\) source into
\[
 \Xi(t)\frac{R^2}{2\sqrt{4t}},\qquad
 \Xi(t)=\sum_{l\ge0}(-1)^l(2l+1)c_l^2
             \left(\frac{s_n^2}{4t}\right)^l .
\]
In particular the first coefficients in \(y=s_n^2/(4t)\) are \(1,-3/4,45/64,-175/256\). The series and the first-moment majorants converge uniformly on the original square for all sufficiently large eligible primes. The bad coordinate and the physical marked replacement carry the separate existing \(O(n^{-1/2}\varepsilon^2)\) charge after \(K\), using the convergent uncompensated budget. The scalar attaches to the same true \(R^2\) packet under every outer \(B^jK\); the identity gives no extra \(j\)-decay.

## Exact seed charges before estimating the norm

Round 165's paired bound includes the pure seed terms with rank majorant \(\varepsilon^2(2+l)s_n^{2l}\), since each pair of independent unit signs has expected absolute sum one. On the pure seed part use the total exponent \(W\) of all \(2l\) signs before taking the absolute first moment. Each sign word has mass \(2^{-2l}s_n^{2l}\). Then \(\Pr(W=0)=c_l\) and \(\mathbb E|W|=2l c_l\). The latter follows by telescoping \((k-l)\binom{2l}{k}=l\bigl(\binom{2l-1}{k-1}-\binom{2l-1}{k}\bigr)\) for \(k>l\). The pure nonunit branch retains rank majorant \(\varepsilon^2s_n^{2l}[2(1-c_l)+2l c_l]\). The 2 charges the two actual increments; the \(2lc_l\) charges the surviving total Laurent exponents. Thus the order-\(l\) bundled comparison permits debit
\[
 \varepsilon^2s_n^{2l}d_l,\qquad d_l=l+2(1-l)c_l,\quad l\ge1,
\]
prior to taking any source norm. It is positive for all \(l\), since \(c_l\le1/2\). Mixed words retain the former paired bound \(2d_1d_2-s_n^2\) on each factor pair. After the pure debit the remaining bound is monotone in the original non-increment dimension budget, since the original bound was monotone and the removed pure term is independent of the nonseed masses. Replacing the non-increment budget by \(M\) and \(s_n^2\) in the debit by its lower bound \(8\) is therefore valid. The factor 2 in the \(K\) price cancels the half from integration.

For a uniform rational upper, put \(t_c=2031/128\), \(a=2^{-17}\), \(d=2^{-16}\), \(Y_0=8/(4t_c)\), \(Y_1=(8000001/1000000)/(4t_c)\), and \(\Delta=(8000001/1000000)d/(4t_c(t_c-a))\). Eventually \(s_n^2\le8000001/1000000\). We have \(Y_1+\Delta<\rho=127/1000\). With \(a_l=(2l+1)c_l^2\), an upper on \(|\Xi|\) is the rational
\[
 U=1-a_1Y_0+a_2Y_1^2-a_3Y_0^3+a_4Y_1^4+
       \Delta\,\frac{3+\rho}{(1-\rho)^3}.
\]
The real-center alternating series has positive sum and decreasing terms because \(a_{l+1}/a_l=(2l+1)(2l+3)/(4(l+1)^2)<1\). The last term bounds the complex displacement by differentiating the majorant with coefficients \(2l+1\) on the disk of radius \(\rho\).

Use only the first four positive debits for a simple rational comparison. The leading post-\(K\) price is at most
\[
 \frac{\varepsilon^2}{\sqrt N}\left[
     (2+x-12/N)(1-x)^{-5/2}-2+2U-
     \sum_{l=1}^4 b_l d_l(8/N)^l \right]<0.00009657 .
\]
For example, lower-bound the two square roots by \(7966725769249/10^{12}\) and \(797070143291/10^{12}\) respectively, check both squares, and compare the remaining rationals. Including the vanishing actual repairs still gives eventual price below \(0.00009657\), and below \(0.00010295\) after one actual outer \(B\) at translated rate \(1.066\). This is an ordinary analytic bound with rational constant comparison, on the original square. The full distributed translated inverse and a sufficient nonlinear common-domain bridge remain open.
