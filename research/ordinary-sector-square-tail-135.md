# The ordinary sector tail and its second-moment requirement

Let \(Y,b,\nu,F_\pm,S\) be the actual ordinary complementary quantities in [Round 134](ordinary-seed-window-134.md). Restrict all expectations below to the bulk by the factor \(1_{\{i\ne0\}}\). For each cutoff \(L\ge0\) the proposed positive sector tail has the exact value
\[
 H_{p,L}=\mathbb E_n\!\left[1_{\{i\ne0\}}
   \big(F_+(Y-L)_++F_-(-Y-L)_+\big)\right]
        =\frac{2}{\nu}\,\mathbb E_n[1_{\{i\ne0\}} b(b-L)_+].
\]
This follows from \(b=|Y|\) and the complementary support, so the only nonzero ordinary factor is \(2b/\nu\) at a bulk point with \(b>0\). The ordinary mean \(\nu\) stays bounded above and away from zero by the ordinary product identity and the entry bound, with the marked activation \(2\sqrt n+O_M(n^{-1/2})\).

For every nonnegative scalar \(b\),
\[
 \frac12 b^2 1_{\{b>2L\}}\le b(b-L)_+\le b^2 1_{\{b>L\}} .
\]
It follows that \(\lim_{L\to\infty}\limsup_p H_{p,L}=0\) is precisely uniform integrability of the bulk squares in the stated prime-first order. This is stronger than merely a uniform bound on the ordinary normalized second moment. It is also stronger than the signed seed-tail condition needed for the window comparison. For \(L>0\), on the actual support the signed tail satisfies the exact useful upper
\[
 \left|\mathbb E_n[1_{\{i\ne0\}}(b-L)_+S]\right|
 \le \frac{\nu\|S\|_\infty}{2L}\,H_{p,L}.
\]
This implication does not reverse, because the signed tail can cancel. Even a uniform bulk second-moment bound would suffice for the signed seed tail directly, since \((b-L)_+\le b^2/(4L)\) for \(L>0\). For bounded-window parity, the approximant must be even in the fixed family of negative trace fields. The actual ordinary support estimate and the clipped-window parity remain open through primes.
