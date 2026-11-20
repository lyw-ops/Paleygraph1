# A uniform vertical-fiber saving and the full weighted affine energy

Use the actual near-critical probability \(\nu\) on \(\widehat Q\) with \(n\max\nu=O(\sqrt p)\) and \(g=|f|^2\) on \(Q\), zero off \(Q\). Keep the actual eligible primes, physical mark, \(G=\sum g=O(\sqrt p)\), and the \(b\)-square, nonzero-interior affine chart of [Round 171](ordinary-affine-line-energy-171.md). Put
\[
 \varepsilon_*=\frac1{1280},\qquad \delta_*=\frac1{640}=2\varepsilon_*,
 \qquad \tau=p^{-\varepsilon_*}.
\]
The same \(g\) weights are used at every threshold.

## Every heavy vertical fiber is smaller than the crude maximum

For any affine map \(T(x)=c x+d\) with \(cd\ne0\), let \(X\) be a set with \(g(x),g(Tx)\ge\tau\) for every \(x\in X\). The following bound is uniform in \(c,d\) and all sufficiently large eligible primes:
\[
 |X|=O(p^{1/2-\delta_*}).
\]
Indeed, suppose \(|X|\ge p^{1/2-\delta_*}\) and trim to at most \(\lfloor\sqrt p\rfloor\) elements if necessary, with that lower exponent intact. For any subset \(W\) of the actual level \(g\ge\tau\), the cap and complex-phase Jensen argument of [Round 163](ordinary-shifted-layer-energy-saving-163.md) give
\[
 E^\times(W)\gg \tau^2 |W|^4/\sqrt p .
\]
For completeness, choose unit phases so that the expectation under \(\nu\) of the character sum over \(W\) is at least \(\sqrt\tau |W|\); its fourth moment is at least \(\tau^2 |W|^4\), and at most \(n\max\nu\) times the uniform-anchor fourth moment. Orthogonality bounds the latter by counting multiplicative energy.

Apply the fixed-loss form of [Reiher–Schoen, Theorem 1.2](https://link.springer.com/article/10.1007/s00493-024-00092-5), in the multiplicative group. With energy parameter \(K_1\ll p^{2\varepsilon_*+\delta_*}\), it gives \(X_1\subseteq X\) of size \(l_1\gg p^{1/2-\varepsilon_*-3\delta_*/2}\) and
\[
 |X_1/X_1|\ll p^{8\varepsilon_*+4\delta_*}l_1 .
\]
Apply the same theorem to \(T(X_1)\) using its own hereditary bound, with energy parameter \(K_2\ll p^{3\varepsilon_*+3\delta_*/2}\). Obtain \(W_2\subseteq T(X_1)\) of size \(l_2\gg p^{1/2-5\varepsilon_*/2-9\delta_*/4}\) and \(|W_2/W_2|\ll p^{12\varepsilon_*+6\delta_*}l_2\). Its preimage \(X_2\subseteq X_1\) has
\[
 |X_2/X_2|\ll p^{8\varepsilon_*+4\delta_*}l_1
            \ll p^{(19/2)\varepsilon_*+(19/4)\delta_*}l_2 ,
\]
since \(l_1\ll \sqrt{K_2}l_2\). Both exponents are therefore bounded by \(12\varepsilon_*+6\delta_*\).

Apply [Zhelezov, Theorem 1](https://arxiv.org/abs/1507.05548) to \(cX_2\), its reciprocal set, and the reciprocal of \(cX_2+d\), with nonzero shift \(d\). These sets all have the common size \(l_2\le\sqrt p\), and the two product sizes in that theorem are the two quotient sizes just bounded. It would follow that \(l_2^{1/26}\ll p^{12\varepsilon_*+6\delta_*}\), impossible because
\[
 \frac1{52}-\Bigl(12+\frac5{52}\Bigr)\varepsilon_*
             -\Bigl(6+\frac9{104}\Bigr)\delta_*=\frac9{33280}>0.
\]
The constants are uniform since the cap and BSG loss are fixed and Zhelezov's estimate is uniform in nonzero shift.

Consequently a level line set \(\mathcal L_{a,d}\) with both thresholds at least \(\tau\) has vertical multiplicity \(m_{\mathcal L}=O(p^{1/2-\delta_*})\): at fixed \(r\), \(Y=r+(1-r)D\) has nonzero slope and shift because \(r\ne0,1\). The other occupancy bound \(M_{\mathcal L}\le2V\) stays as in Round 171. This vertical argument applies to the actual one-match affine chart. It does not automatically apply to the different vertical fibers of the inverted full diagonal.

## Weighted energy on all levels

Let \(\mu_0(r,b)=g(Y)g(D)\) on the genuine square-masked affine set, and zero elsewhere. The affine energy \(E_w(\mu_0)=\sum_h|\sum_j\mu_0(j)\mu_0(jh)|^2\) has fourth root a norm, up to the fixed normalization: it equals \(|\mathrm{Aff}(\mathbb F_p)|^{-1/4}\) times the Schatten \(4\)-norm of the regular convolution operator. This follows by expanding the trace of \((M_{\mu_0}^*M_{\mu_0})^2\) in the regular representation and using that each nonidentity translation has trace zero. The same identity defines the norm on complex coefficients with conjugates in the correlation. Hence layer cake permits an integral of \(E(\mathcal L_{a,d})^{1/4}\) to bound the actual \(E_w(\mu_0)^{1/4}\).

Use the primary affine-energy estimate with the all-level prime-field term \(m_{\mathcal L}|\mathcal L|^3/p\) verified in [Round 172](ordinary-full-diagonal-affine-172.md). Here \(N_{\mathcal L}\le UV\), \(U\le G/a,V\le G/d\). The first energy term after its fourth root is \(m_{\mathcal L}^{1/8}(UV)^{5/8}\). For \(a,d\ge\tau\), integrate it with the new uniform \(m_{\mathcal L}\) to get \(O(p^{11/16-\delta_*/8})\). For \(a<\tau\) or \(d<\tau\), use \(m_{\mathcal L}\le\sqrt{UV}\). Integrating \((UV)^{11/16}\) on that union gives \(O(G^{11/8}\tau^{5/16})\), which is smaller. The other two energy terms give \(O(G^{5/4}+p^{-1/4}G^{7/4})=O(p^{5/8})\) after fourth root and layer integration, using \(M\le2V,m\le V\) and the exact \(\int_0^1V(d)\,dd\le G\). Hence
\[
 E_w(\mu_0)=O\bigl(p^{11/4-\delta_*/2}\bigr).
\]
This is an all-level bound on the actual positive weight with both square and endpoint conditions. The sufficient target \(O(p^2)\) remains open.

## Consequent improvement of the full two-dimensional one-match estimate

The incidence argument of Round 172 can use the same vertical gain. On the heavy threshold region the first term \(E^{1/8}|\mathcal L|^{1/2}\) is bounded by
\(m_{\mathcal L}^{1/16}(UV)^{13/16}\) plus the unchanged other two terms. After integrating \(a,d\) and the input level of \(h_t(e)=g(t/e)\), this gives
\(O(p^{37/32-\delta_*/16})\) multiplying the square root of output set size. On the light threshold region the crude \(m_{\mathcal L}\le\sqrt{UV}\) gives \((UV)^{27/32}\), and integration gains \(\tau^{5/32}\), again enough since \(\delta_*=2\varepsilon_*\). The unchanged terms of Round 172 are strictly smaller. Rearrangement and the actual \(w(t)\) mass then give
\[
 \sum_{s\ne0,1,t}w(t)|H_\alpha(s,t)|^2
       =O\bigl(p^{45/16-\delta_*/8}(1+\log p)\bigr).
\]
The already priced endpoints cost \(O(p^{5/2})\). Thus in the original covariance the matching-number-one term is \(O(p^{29/16-1/5120}(1+\log p))\). Neither the necessary \(O(p^{3/2})\) matching bound nor zero match follows. This gain uses the actual probability cap and shifted high levels in addition to the general affine incidence theorem.
