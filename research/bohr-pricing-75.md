# Opposite sign runs with prescribed simultaneous phases

For the actual prime Paley sign masks, one can require a logarithmic opposite sign run and prescribed small phases in several chosen directions at the same time. The weighted run average prices all bounded integer combinations of those directions, including shifts of full order. The same average retains the clipped tail budget from round 74, with an explicit cost for the phase restrictions.

## Counting sign runs with a Fourier weight

Use \(Q=(\mathbb F_p^\times)^2\) of order \(n=(p-1)/2\), \(G=\widehat Q\), and let \(\mathcal T\) be the generators of length-\(L\) runs for the sign opposite to a tested feasible row \(q\). Thus \(t\in\mathcal T\) if \(\operatorname{ord}(t)>2L\) and all \(t^j\), \(1\le j\le L\), have the opposite sign under \(u\mapsto\chi(1-u)\). Work uniformly for \(1\le L\le\lfloor(\log_2 p)/4\rfloor\). A generator here is a base of a run, which can have any order exceeding \(2L\).

For every character \(\eta\in G\), the character-sum argument of [round 73](opposite-autocorrelation-73.md#a-single-mixed-budget-for-all-low-order-differences) gives
\[
 \sum_{t\in\mathcal T}\eta(t)
     =2^{-L}n\,\mathbf1_{\eta=1}+O(L^2\sqrt p).                    \tag{1}
\]
For each nonempty subset of the sign factors, extend the character twist from \(Q\) to the full multiplicative group and expand the indicator of \(Q\). The factor with largest exponent \(j\) has a simple primitive \(j\)-th root absent from every smaller factor. Its multiplicity in the polynomial after lifting all characters to a single primitive character is \((p-1)/2\). The monomial twist only changes the root at zero. The distinct-root form of the Weil bound costs \(O(L^2\sqrt p)\) uniformly in the twist. The coefficients of the sign expansion have total absolute sum one, and removing elements of order at most \(2L\) costs \(O(L^2)\). The empty subset contributes exactly the displayed main term before that removal. [Weil's character-sum bound](https://www.pnas.org/doi/10.1073/pnas.34.5.204)

For any \(\Omega:Q\to[0,1]\) with Fourier coefficient absolute sum at most one, put
\[
 \mu_\Omega=n^{-1}\sum_{t\in Q}\Omega(t),\qquad
 T_\Omega=\sum_{t\in\mathcal T}\Omega(t),\qquad
 \epsilon_L=2^L L^2\sqrt p/n .
\]
Summing (1) against its Fourier coefficients gives
\[
 2^L T_\Omega/n=\mu_\Omega+O(\epsilon_L).                           \tag{2}
\]
The error is uniform even when the weight is chosen from the observed differences of \(q\). The same estimate applies to \(\Omega(t)\eta(t)\) with main term \(n^{-1}\sum_t\Omega(t)\eta(t)\), since multiplying by a character only permutes the coefficients.

## One weight for a set of prescribed shifts

Fix \(h_1,\ldots,h_k\in G\) and an integer \(R\ge1\). Write \(h=\sum_j v_jh_j\) additively and let
\[
 \Lambda_R=\Big\{\sum_jv_jh_j:\ v_j\in\mathbb Z,\ \sum_j|v_j|\le R\Big\},
 \qquad a=\frac1{8R(L+1)}.
\]
On the circle \(\mathbb R/\mathbb Z\) use the tent \(\omega_a(x)=(1-\|x\|_{\mathbb R/\mathbb Z}/a)_+\). It has nonnegative Fourier coefficients, constant coefficient \(a\), and absolute coefficient sum one. Indeed it is the circular convolution of two centered interval indicators of length \(a\), divided by \(a\). Its coefficients are the squares of the interval coefficients divided by \(a\), and their sum is the value at zero. Define
\[
 \Omega(t)=\prod_{j=1}^k\omega_a\!\left(\frac{\arg\eta_{h_j}(t)}{2\pi}\right).
\]
Its finite Fourier coefficients on \(Q\) are nonnegative and sum to one, since the product expansion has those properties before equal characters are grouped. In particular \(\mu_\Omega\ge a^k\). Whenever \(\Omega(t)>0\), all \(h\in\Lambda_R\) satisfy \(|\arg\eta_h(t)|\le 2\pi aR<1/(L+1)\). This uses circular distance and so also covers dependent directions and characters of low order.

Assume \(\epsilon_L\le c_0\mu_\Omega\) for a sufficiently small absolute constant \(c_0\). It is sufficient to impose this with \(a^k\) in place of \(\mu_\Omega\). Equation (2) gives \(T_\Omega\ge n2^{-L}\mu_\Omega/2\). The weighted Fejér autocorrelation profile
\[
 C_\Omega(h)=\tfrac12 C_{\mathrm{unif}}(h)
  +\frac1{2T_\Omega}\sum_{t\in\mathcal T}\Omega(t) C_{r_t^F}(h)
\]
is a convex mixture of autocorrelations of actual opposite feasible probabilities. For each \(t\) used in the average, the Fejér row from [round 73](opposite-autocorrelation-73.md#a-uniformly-available-prime-weight-on-a-character-arc) obeys \(C_{r_t^F}(h)\ge cL/n\) on \(\Lambda_R\), by the cosine lower bound for powers up to \(L\). The autocorrelations are nonnegative everywhere. Mix \(C_\Omega\) equally with the all-run profile of round 73 to obtain \(\mathcal C\). Then
\[
 \mathcal C(h)\ge \frac c n W(h),\qquad
 W(h)=1+\frac{L}{\operatorname{ord}(h)}+L\,\mathbf1_{\Lambda_R}(h)
 \qquad(h\ne0).                                                   \tag{3}
\]
For example, at \(L=\lfloor(\log_2 p)/4\rfloor\) the sufficient counting condition holds uniformly if \([8R(L+1)]^k\le p^{1/8}\), for all sufficiently large \(p\). This allows several prescribed high-order differences to be specified before choosing a run. The R73 single-arc comparison can price those differences only for a run already known to fit that arc.

For a general positive-definite weight \(\Omega\) as above there is also a coefficient version. Let \(a_\Omega(h)=n^{-1}\sum_t\Omega(t)\overline{\eta_h(t)}\), so \(a_\Omega\ge0\), and \(\Omega\) real gives \(a_\Omega(-h)=a_\Omega(h)\). The nonconstant Fejér coefficients in the covariance are \((1-j/(L+1))^2\) at \(t^{\pm j}\). By the twisted form of (2), after division by \(T_\Omega\) the expected cosine equals \(a_\Omega(jh)/\mu_\Omega+O(\epsilon_L/\mu_\Omega)\). Here \(a_\Omega(jh)\le\mu_\Omega\) by \(\Omega\ge0\). If \(L\epsilon_L\le c_1\mu_\Omega\) with \(c_1\) sufficiently small, the uniform part absorbs the summed signed errors, giving
\[
 C_\Omega(h)\ge \frac c n\left(
 1+\frac1{\mu_\Omega}\sum_{j=1}^L
    (1-j/(L+1))^2 a_\Omega(jh)\right).
\]
In particular \(\Omega(t)=|\widehat\nu(t)|^2\) for a probability \(\nu\) prices the multiples of a difference by their measured autocorrelation. This choice has \(\mu_\Omega=\sum_i\nu_i^2\) and \(a_\Omega=C_\nu\).

## The same weighted runs keep a small clipped budget

At any cutoff \(B>0\) put \(x_i=(q_i-B/n)_+\), \(M=\sum_i x_i\), \(z=q-x\), and \(L_x=\sum_i x_i^2\). Opposite positions have \(\widehat x=-\widehat z\) and their Fourier energy is at most \(B(1-M)\), as in [round 74](stratified-centering-74.md#a-smaller-budget-for-the-clipped-true-row). Each \(t^{\pm j}=u\) has at most \(j\) preimages in \(Q\), and each weight is at most one. Consequently the average nonconstant Fejér contribution to \(n\|x*\widetilde r\|_2^2\) is at most \(C\,2^L L^2 B(1-M)/(n\mu_\Omega)\), by Parseval with counting norm. The unweighted part of \(\mathcal C\) already has the corresponding bound with \(\mu_\Omega=1\). Since \(0\le x*\widetilde r\le1/n\), the exact off-diagonal budget therefore obeys
\[
 \begin{split}
 n\sum_{h\ne0}C_x(h)\mathcal C(h)
  &\le F-nL_x\mathcal C(0),\\
 F&=\min\left\{M,\ M^2+
                C\frac{2^L L^2}{n\mu_\Omega}B(1-M)\right\}.        \tag{4}
 \end{split}
\]
The bound also holds with a smaller Fourier sum for a specified weight: replace the error in (4) by the actual weighted sum
\[
 \frac1{T_\Omega}\sum_{t\in\mathcal T}\Omega(t)
 \sum_{j=1}^L\left(1-\frac{j}{L+1}\right)^2
 \big(|\widehat z(t^j)|^2+|\widehat z(t^{-j})|^2\big)
\]
for the weighted run portion of the mixture, together with the analogous contribution from the unweighted portion. The displayed budget removes the actual diagonal before spending it on differences.

## A prime-uniform restriction on true supercritical sites

Let \(A\subset G\) be a nonempty set of size \(m\) where \(\sqrt n\,q_i\ge1+\delta\) for fixed \(\delta>0\), and partition \(A\) into blocks of sizes \(b_j\). Let \(R_\times(h)\) count ordered pairs with difference \(h\) in different blocks. With \(W\) from (3), put \(U=\max_{h\ne0} R_\times(h)/W(h)\). The [round-74 masked comparison](stratified-centering-74.md#a-masked-second-moment-with-no-within-block-differences) and (3)–(4) give the necessary condition
\[
 B + \frac{\sqrt n\,M}{m^2}\sum_j b_j^2
      + \frac{nU}{m^2}F \ \ge\ c_\delta D(p).                     \tag{5}
\]
The constants are uniform in the field, cutoff and geometry under the counting premise above. To verify the limit order, if the left side were \(o(D)\) along a choice of all parameters and eligible primes, choose \(d\) as the integer part of the geometric mean of \(D\) and the maximum of the left side and one. Then \(d\to\infty\), \(d=o(D)\), \(B=o(d)\). The diagonal uses \(nL_x\le C\sqrt n\,M\). In the off-diagonal bound one can take a comparison coefficient \(nU/(cm^2)\) with no residual and apply (4). On the other hand every sampled translate combination in the masked comparison has mark at least \(1+\delta\), and every selected opposite smooth marked window has hinge at least \(c'_\delta d\) at the fixed deficit cutoff \(\delta/8\). This contradicts the \(o(d)\) upper bound. Any failure of the stated uniform constant would give such a sequence. The argument also applies to exact cap centers on a true primary face.

## Comparison at a shorter run length

Suppose \(m\asymp n^{1/3}\), block sizes are bounded, and the full actual tail satisfies \(M=O(m/\sqrt n)\) at \(B=o(D)\). Use \(L=\lfloor(\log_2 p)/12\rfloor\) and a single generator \(h_1\) of the cyclic group \(G\), with \(R\asymp m\). Then \(\Lambda_R=\{jh_1:|j|\le R\}\). Its tent has \(\mu_\Omega\asymp1/(mL)\), since \(\eta_{h_1}(t)\) enumerates the \(n\)-th roots of unity and the central half of its support contains \(\asymp n/(mL)\) of them. The upper bound follows by counting the entire support. The relative counting error \(\epsilon_L/\mu_\Omega\) tends to zero. If cross-block repetitions outside \(\Lambda_R\) remain bounded and those inside are \(O(L)\), then \(U=O(1)\). The error contribution in (5) is \(O(2^L L^3 B/m)=o(D)\). The other terms are \(B+O(1)\), so this geometry and clipped mass cannot occur together with the supercritical mark.

The comparison can gain when repetition counts comparable to \(L\) occur on at least a constant times \(m\) shifts in this interval. This is a comparison of upper bounds on a prescribed profile. It requires the stated hypotheses and makes no claim that such a profile occurs on a primary face. For the uniform or the unconditioned all-run comparison from rounds 73–74, those shifts are all priced at \(O(1/n)\): for \(h=jh_1\) there with \(j\ne0\), \(\operatorname{ord}(h)\ge n/R\), larger than every available run length. In the unconditioned covariance every character at \(t^{\pm j'}\) with \(1\le j'\le L'\) then has zero full-group average. For any available length \(L'\), (1) bounds its average over the runs by \(O(\epsilon_{L'})\). The resulting covariance is \((1+O(L'\epsilon_{L'}))/n\).

For these hypotheses, \(M\asymp m/\sqrt n\) and \(nL_x\asymp m\) by the values on \(A\) and the point cap. If the unconditioned price coefficient \(\lambda\) is at least a sufficiently small constant times \(nL/m^2\), the paid term in (3) of round 74 is \(\gg L\), since the uniform part gives an off-diagonal budget \(\gg M^2-L_x\). Below that coefficient the residual is \(\gg L/m^2\) on \(\gg m\) shifts. Both unlocalized residual bounds in round 74 are then \(\gg L\). This allows a separation in the bounds with the same specified profile and partition, because \(D=o(L)\). An alternative partition, a localized residual or a separately selected run can supply other comparisons.

The small actual \(M\) hypothesis in this example is still needed. With a singleton as the only center, the diagonal of (5) can dominate, and the hinge on the actual marked negative set still needs its own estimate.

## Ranked next tests

1. On the genuine optimizer minimize the combined cost in (5) over the cutoff, run length and weighted run conditions. Keep the exact diagonal and signed Fourier contribution where available. Test frequent high-order differences lying in a small number of directions before applying the unweighted residual bound.
2. On isolated caps use the actual marked mask and direct opposite-face complementarity. Control the diagonal hinge there, or show that a near-optimal feasible replacement can spread its mark across enough centers to use (5).
