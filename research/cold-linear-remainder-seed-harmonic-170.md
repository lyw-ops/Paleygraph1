# The shared first seed harmonic with one genuine nonseed factor

Keep the actual \(R=V_{601}-V_{600}\), \(V_s=V_{600}+sR\), \(0\le s\le1\), both lifts, the original square, and the physical \(t_0=n=(p-1)/2\). Use the exact bulk Taylor source and the notation \(\varepsilon,M,N,x,s_n,c_l,b_l\) of [Round 168](cold-all-order-seed-transport-source-168.md). In the actual common representation write \(V_s=S+W_s\), where \(S=s_n(z+z^{-1})/2\) on good characters is the designated Jacobi seed. The remaining field \(W_s\) has dimension budget at most \(M-s_n\) and uses the original base pair, by [Round 126](cold-actual-first-insertion-126.md). This is the actual remainder, including its \(sR\) term. Its products need not be small in any other norm.

## Reassembly before the outer frozen powers

In \((S+W_s)^{2l}\), select the \(2l\) terms with exactly one \(W_s\) and the other \(2l-1\) factors equal to \(S\). The two Laurent coefficients at exponents \(\pm1\) in \(S^{2l-1}\) are each \(c_l s_n^{2l-1}\), since
\(\binom{2l-1}{l-1} / 2^{2l-1}=c_l\). Their sum as a Laurent polynomial equals \(2c_l s_n^{2l-2}S\). Thus, without moving any multiplier through \(K\), all these terms multiply the same bulk vector \(R^2 S\int_0^1(1-s)W_s\,ds\). Relative to its full coefficient \(-3(4t)^{-3/2}\) at \(l=1\), the scalar is
\[
 \Xi_1(t)=\sum_{k\ge0}(-1)^k f_k y^k,\qquad
 f_k=\frac{4(k+1)}3 a_{k+1},\quad
 a_l=(2l+1)c_l^2,\quad y=\frac{s_n^2}{4t}.
\]
This has \(f_0=1\); for instance \(f_1=15/8\). It collects the actual first surviving modes with one nonseed factor across all even Taylor orders. The pure seed unit and all other mixed terms are separate branches. The identity applies under any actual frozen power \((KD_{602})^jK\) to the same bulk vector. The vanishing bad-character and marked replacements at the source are handled as in Round 168, with convergence of the uncompensated dimension sums. No claim about the full transport of these replacements follows from their first post-\(K\) prices.

Use \(Y_0,Y_1,\Delta,\rho\) of Round 168. The following rational bounds the scalar modulus uniformly on the original square for all sufficiently large eligible primes:
\[
 U_1=1-f_1Y_0+f_2Y_1^2-f_3Y_0^3+f_4Y_1^4+
       \Delta\,\frac{8}{3(1-\rho)^3}<0.802 .
\]
At the real center the terms of the alternating series decrease, since \(a_l\) decreases and \(f_{k+1}/f_k\le(k+2)/(k+1)\le2\), with \(Y_1<0.127\). Its sum is positive. The derivative bound on the complex displacement follows from \(f_k\le (4/3)(k+1)\). Thus the signed scalar compression retains a strict source-side improvement.

## Comparison with the full old source price

For words with one \(W_s\), the paired comparison of Round 165 charges 3 first moments for the two \(R\)'s and the \(W_s\), plus the seed first moments. In any particular sign word of total seed exponent \(+1\) or \(-1\), the sum of the pairwise absolute exponents, including the one unpaired seed sitting with \(W_s\), is at least 1. The selected two exponents therefore contribute at least the following explicitly designated branch of the old positive first-moment budget at order \(l\), writing \(D_s\) for the actual remaining dimension budget:
\[
 \varepsilon^2\,4(2l)(2c_l)s_n^{2l-1}D_s .
\]
Removing these contributions precedes taking the unsigned price. In the complementary comparison, each coefficient of the polynomial in \(D_s\) still bounds a sum of nonnegative sign-word charges, so one may substitute \(D_s=M-s_n\). The pure-seed debits of Round 168 are independent of \(D_s\). The reassembled common vector in the first display has base post-\(K\) price after integration at most \(4\varepsilon^2 s_n(M-s_n)\) before multiplying by \(-3(4t)^{-3/2}\Xi_1(t)\), using one first moment for \(S\) and three for the remaining factors. The post-\(K\) factor \(2\) cancels the integral mass \(1/2\).

For exact comparisons set
\[
 s_-=\frac{282842712}{10^8},\quad s_+=\frac{282842731}{10^8},\quad
 s_-\le s_n\le s_+
\]
eventually, checked by squaring. Using only the first four mixed debits as well as the first four pure debits gives the leading post-\(K\) bound
\[
\frac{\varepsilon^2}{\sqrt N}
\left[
 (2+x-12/N)(1-x)^{-5/2}-2+2U
 -\sum_{l=1}^4 b_l d_l(8/N)^l
 +\frac{12s_+(M-s_-)U_1}{N}
 -\sum_{l=1}^4
 \frac{b_l\,4(2l)(2c_l)s_-8^{l-1}(M-s_+)}{N^l}
\right]<0.00008874,
\]
where \(U,d_l\) are the pure quantities from Round 168. To check the inequality, use its same rational lower bounds on the square roots of \(N\) and \(1-x\). The rational expression then gives an upper below \(0.00008873856\) before the vanishing repairs. At the real translation rate \(1.066\), the genuine first \(KD_{602}\) step gives eventual price below \(0.00009460\) on the same square. This is an ordinary analytic source bound and one fixed transported step. The uniform full distributed response and sufficient nonlinear common-domain bridge remain open.
