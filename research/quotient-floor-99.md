# A vanishing trial root in the signed recurrent-prefix test

On the bounded trapped branch, the filtered candidate list and the original recurrent masks can be kept while weakening the root requirement on the *trial* in the signed flat-prefix test. A root mass of order \(1/J\) suffices if its constant is large enough and the signed flat charge is measured relative to that root. This gives a second sparse-deletion target for the true quotient data.

Fix the setting and recurrence parameters of [round 98](astra-quotient-98.md). In particular the original block \(L\) on the filtered list has size \(m\asymp\sqrt n\), \(|\lambda|\le\kappa_*<1\), and the true recurrent visits give the uniform lower \((1-\sigma\lambda)\sum_{j<J}\omega_j\mathbb E_L|Y_j|\ge c_0J\) for some \(c_0>0\). Here the fixed triangular weights are \(\omega_j=2(J-1-j)/(J(J-1))\). Retain the original independent per-time erasures in the two data rows \(U_\omega\), \(V_J\) of that proof. Let \(\varepsilon_p\) bound the maximum removed counting first mass divided by \(\sqrt n\) for either data row at every time. The [actual erasure budget](astra-recur-95.md) gives \(\varepsilon_p=o(1)\).

For any nonnegative quotient probability \(q\) in the allowed sector with root \(w=q(L)>0\), the exact signed Abel calculation of round 98 gives
\[
 \sigma\mathbb E_L K U_\omega+
 \frac{2}{J-1}\frac{\sigma\langle q,V_J\rangle}{w}
 \ \ge\
 c_0J-\frac4w-C\varepsilon_p\left(1+\frac1{w(J-1)}\right) .       \tag{1}
\]
Indeed it gives \(c_0J-4/w\) before erasures by the same energy bound \(2\sum_j\omega_j g_j\le4\), positivity of the marked term, and the nonnegative signed exterior reserve. For each erased row, the change of the transform is \(O(\varepsilon_p)\) by \(\|K\|_{\max}\le\sqrt p/n\). The change of the signed quotient pairing *before* dividing by \(w\) is \(O(\varepsilon_p)\), since \(\|q\|_\infty\le1/m\) for every coset-constant probability. These bounds hold independently of the root. This keeps (1) valid for shrinking \(w\).

In particular, for a fixed positive \(c_0\), take \(A=8/c_0\). If the true triangular term is \(o(J)\) from above, a signed trial with \(w\ge A/J\) and \(\sigma\langle q,V_J\rangle\le o(wJ^2)\) contradicts recurrence by (1). The original positive floor on the initial filtered list and its signed coefficient bound have their original role.

To use the [signed quotient head](astra-quotient-99.md#a-sparse-deletion-test-and-its-opposite-sector-obstruction), let \(\eta_J\ge A/J\) be a desired smaller root and set \(s_J=\eta_J J^2/\log J\). Its genuine hot set is \(S_{s_J}=\{R:v_R>s_J\}\), with \(v_R\) on the fixed original-eroded flat signed prefix as in that note. The relative size obeys
\[
 \frac{|S_{s_J}|}{|G/L|}
 \le \min\left\{\frac{\log J}{\eta_JJ^2},
                    \frac{2(\log J)^2}{\eta_J^2J^3}\right\}.
\]
If a legal law of root \(w\ge\eta_J\) vanishes on this set, then its charge is at most \(s_J(1-w)\le wJ^2/\log J\), regardless of any negative block prices. Thus fixed-floor retention in the earlier sufficient test can be replaced by retention of \(\eta_J\), at the cost of enlarging the head. For example \(\eta_J=J^{-1/2}\) asks for a projection or LP root of that order against at most a \(2(\log J)^2/J^2\) fraction of the original quotient. Taking \(\eta_J=A/J\) asks for a root \(A/J\) against at most a \((\log J)/(AJ)\) fraction. The proof is an ordinary inequality on the genuine orbit; neither capacity lower nor the triangular upper at unbounded primes is established here.

1. Seek a legal trial at root \(A/J\) or \(J^{-1/2}\) on the enlarged measured head by the [clique projection test](astra-quotient-99.md#an-explicit-trial-without-the-capacity-lp) or the exact opposite-sector dual.
2. Keep the one-sided identity-fiber triangular test on the same recurrent block. The relaxed trial root leaves that independent requirement unchanged.
