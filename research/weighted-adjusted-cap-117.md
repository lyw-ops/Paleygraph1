# Weighting the actual adjusted cap overshoot

Use the actual capped row and notation of [the direct opposite-sector completion](projected-cap-completion-108.md), with \(M=10\), a fixed \(0<t\le1\), and one sign \(\epsilon\). Thus \(z=a-\epsilon U\), \(T=T_\epsilon=z_-\) for all large fields, \(\mu=\mathbb E_n a\), \(d=z_0/\sqrt n\), \(\ell=(\epsilon(KT)_0)_+/\sqrt n\), and \(\nu=2\sqrt{1+t-t/n}\). Let
\[
             V=z_+-\epsilon KT,\qquad S=V_-.
\]
Here \(S\) is the coordinatewise adjusted overshoot, whose supremum is \(c_\epsilon\) in Round 108. Even when \(V\) is signed, its centered row is in the true \(-\epsilon\) sector and \(\mathbb E_n V=\mu+\mathbb E_n T\). The same cap budget gives, exactly,
\[
 V_0/\sqrt n\ge d-\ell,\qquad \mu+\mathbb E_n T\le\nu(1-\ell/2).
\]
Here \(d\to2\) at each fixed floor and \(d-\ell\) is bounded below by a positive constant for large primes.

## Test only the overshoot weighted by the true factor

For any positive or nonnegative favored-sector row \(F\) with mean \(m_F>0\), the exact opposite-sector orthogonality gives
\[
 (d-\ell)\frac{F_0}{m_F\sqrt n}
   \le \mu+\mathbb E_nT+\frac{\mathbb E_n(FS)}{m_F}.
\]
Indeed \(\mathbb E_n(FV)=m_F(\mu+\mathbb E_n T)\), whereas \(\mathbb E_n(FV_+)\ge F_0V_0/n\) by positivity. Consequently
\[
 \frac{F_0}{m_F\sqrt n}\le \frac\nu2+
       \frac{\mathbb E_n(FS)/m_F+(\nu/2)(2-d)}{d-\ell}.        \tag{1}
\]
In particular take a true ordinary favored Fourier-LP optimizer, normalized to have mean one. Its marked ratio is \(\theta_\epsilon/\sqrt n\) by the [Fourier LP](fourier.md). If there is a choice of true optimizer with \(\mathbb E_n(FS)=o(1)\) along all primes, (1) gives the sharp fixed-floor upper \(\limsup_p\theta_\epsilon/\sqrt n\le\sqrt{1+t}\). This only tests the overshoot where the optimizer puts mass.

There is a separate explicit test using the true reciprocal stationary factor \(F=f_\epsilon\), with mean \(\nu/2\) and mark \(\sqrt n e^{\epsilon\gamma}\). With that choice (1) gives
\[
 e^{\epsilon\gamma}\le \frac{\nu^2}{4}+
       \frac{\mathbb E_n(f_\epsilon S)+(\nu^2/4)(2-d)}{d-\ell}.      \tag{2}
\]
In particular \(\mathbb E_n(f_\epsilon S)=o(1)\) for both signs at each of a sequence of fixed floors tending to zero is sufficient for the original limit, by the true stationary complementary theta bracket. This criterion requires no cap-defect rate. It gives \(\limsup_p e^{\epsilon\gamma}\le 1+t\) at each floor where it holds, and the ordinary upper from the complementary stationary bracket is \((1+t)^{3/2}\) at that floor. The sharp fixed-floor \(\sqrt{1+t}\) assertion above concerns the optimizer test.

## What a persistent mark forces in the actual adjusted overshoot

At a fixed floor with \(\epsilon\gamma\ge\delta>0\) on a subsequence and \(t<e^\delta-1\), (2) forces \(\mathbb E_n(f_\epsilon S)\gtrsim1\), with no cap rate. The unadjusted spill \(T\) and this adjusted overshoot \(S\) are different rows. If one additionally has the critical bound \(\alpha=O(n^{-1/2})\), then
\[
  \|S\|_{2,n}^2\le\|KT\|_{2,n}^2
      =\|T\|_{2,n}^2-(\mathbb E_nT)^2\le\alpha,
  \qquad \|S\|_\infty=O(1).
\]
The first inequality follows from \(S\le(\epsilon KT)_+\), the last from the Jacobi entry bound. For fixed sufficiently small \(\eta>0\), the bulk subset \(f_\epsilon<\eta\sqrt n\) contributes \(O(\sqrt\eta)\) to the pairing by Cauchy–Schwarz, since its squared factor norm is at most \(\eta\sqrt n\,(\nu/2)\). The mark contributes zero as \(V_0>0\) eventually. On the actual high bulk \(f_\epsilon\ge\eta\sqrt n\), entries with \(S\le\eta'\) contribute at most \(\eta'\nu/2\). Taking also a small fixed \(\eta'>0\), the remaining pairing is still bounded below. Boundedness of \(S\) and \(f_\epsilon/\sqrt n\) and the factor's mean show that the set with both high \(f_\epsilon\) and fixed positive adjusted overshoot has order \(\sqrt n\) sites. Thus, under the extra cap rate, a fixed positive marked obstruction needs an actual weighted population of high overshoots. An isolated maximum need not obstruct (1) or (2).

Neither optimizer-weighted nor stationary-weighted vanishing of the adjusted overshoot is proved. The weighted criterion leaves a direct arithmetic target that permits large overshoots on sites carrying negligible true weight.

## Retaining both actual levels at the critical cap rate

Under the additional rate \(\alpha\le B/\sqrt n\), the high overshoot recipients just obtained can be tested against a fixed bounded source level of the actual \(T\). Indeed on \(T_i>0\) the cap defect at that site equals \(4t+2AT_i+T_i^2\). Consequently for fixed \(0<\lambda<L\),
\[
 \left\|K\left(T-1_{\{\lambda\le T\le L\}}T\right)\right\|_\infty
 \le\sqrt p\,\alpha\left(\frac\lambda{4t}+\frac1L\right).
\]
First choose small positive \(\lambda\) and large finite \(L\), depending on the fixed obstruction parameters, to make this at most half the retained fixed overshoot margin. On the same \(\asymp\sqrt n\) recipient sites with high favored factor, the bounded true source then has signed transport strictly above the actual local slack, by a fixed margin. The source level has \(O(\sqrt n)\) sites by the cap-defect count, and \(\gtrsim\sqrt n\) sites by the fixed transport lower and the entry bound. A prime arithmetic test can therefore keep the actual favored recipient level and local slack while restricting the true transport source to bounded positive amplitudes. The rate is used for the source and recipient geometry. The sufficient test (2) itself is independent of that rate.
