# The genuine repair reweighting in the Legendre trace

Use the actual late repair and [one-repair reciprocal cubic](paired-legendre-cubic-116.md). The positional Fourier transform of a probability law is taken without further normalization. Let \(\Pi_-\) project onto the centered \(-\epsilon\) eigenspace of \(K\). The late estimate gives \(\|\Pi_- h\|_{2,n}=O(n^{-1/2})\). Consequently \(\|\widehat\pi\,1_{\{s=-\epsilon\}}\|_{2,\mathrm{count}}=\|\Pi_-h\|_{2,n}/m=O(1)\), whereas \(\|\widehat{\omega^-}\|_{2,\mathrm{count}}=O(n^{1/4})\). The same positional expansion as in (3) and Hasse now give
\[
 \mathbb E_{\pi\otimes\omega^-} k(x-y)^2=(n-1)/p+O(n^{-1/4}).
\]
So without the actual favored-factor reweighting the second moment is asymptotically its uniform value, even without the trimmed residual branch.

The near-eigen error can also be removed *after* reweighting. Let \(h_*=h-\Pi_-h\) and \(w_*=h_*g/(n\mathbb E_n(hg))\), retaining the original denominator. The centered positional transforms of both \(h_*\) and \(g\) lie in the true favored sector. Although \(w_*\) can be signed, its total mass is exactly one because \(\mathbb E_n(g\Pi_-h)=0\). Its negative mass is \(O(n^{-1/4})\) by Cauchy–Schwarz against \(g\). Parseval and bounded \(g\) give
\[
 \|\widehat w-\widehat w_*\|_{2,\mathrm{count}}
 =\frac{\|g\Pi_-h\|_{2,n}}{\mathbb E_n(hg)}=O(1).
\]
Thus replacing \(w\) by this signed row in the actual restricted trace \(p^{-1}\sum_{s(v)=-\epsilon} a_p(v)\widehat{\omega^-}(v)\overline{\widehat w(v)}\) changes it by \(O(n^{-1/4})\). The main term has one genuine opposite coefficient and the positional product of two genuinely favored spectra, with constants retained. This preliminary reduction does not estimate their correlated trilinear Legendre sum. No prime-uniform bound eliminating the real obstruction follows from it alone.

## The two true favored inputs in positional variables

Put \(\pi_*=h_* /(nm)\). At \(s(v)=-\epsilon\), multiplication on the frequency side and Fourier inversion give
\[
 \widehat w_*(v)=\frac{m\mu}{\mathbb E_n(hg)}
       \sum_{ab=v\,;\ s(a)=s(b)=\epsilon}
            \widehat{\pi_*}(a)\widehat\omega(b).
\]
The coefficient is \(\asymp n^{-1/2}\). The constant index of either favored factor gives zero here because the other factor would be outside its exact favored support. It follows that the trace statistic at the critical scale is the actual opposite coefficient against a two-favored trilinear sum, with a controlled replacement error \(O(n^{-1/4})\).

An exact unweighted baseline in that sum comes from the reciprocal product. For every \(a\in Q\) with \(s(a)=\epsilon\), inversion symmetry of the true even factors gives
\[
 \sum_{b\,;\ s(b)=\epsilon,\,s(ab)=-\epsilon}
          \widehat\omega(b)\widehat{\omega^-}(ab)
       =\frac{1-t/n}{n\mu^2}-\widehat\omega(a^{-1}).
\]
Before support restriction, the convolution of the two counting-normalized positional rows equals \(n\) times the transform of the pointwise product \(\omega\omega^-\). At nonidentity \(a\), the constant bulk part of \(gg_-\) drops out and the actual marked correction gives the first term. The excluded \(ab=1\) contributes \(\widehat\omega(a^{-1})\); the excluded \(b=1\) contributes zero by the genuine opposite support. This computes the sum with a constant twist. Replacing that constant by the Legendre trace \(a_p(ab)\) is precisely the remaining signed arithmetic step. The baseline identity does not imply that the trace is independent of the two actual factors.
