# A deficit quantile for signed exterior minors at a first cold tie

At a first bulk tie in the closed square of half-width `2^-17` about \(2031/128\), more than **1.28% of the actual clipping-deficit mass** must occur on sites where the **individual oriented interval average** of the near-flat real marked column exceeds \(947.03/\sqrt n\). On the same sites the two exterior Fourier signs must agree with their respective orientations together, with an integrated common cap exceeding \(946.43/\sqrt n\). The interval and the near-flat weight profile are shared by all the sites. The particular marks at which they exceed these values may differ. An exact square controls the comparison even when a factor at the tie is zero. This strengthens the [single averaged test](astra-minors-93.md) in a different direction. It gives a condition on the distribution of the real column over the actual deficits, without an all-profile column upper.

## The two endpoint comparison, including zero factors

Use full counting on the cyclic group of order \(n=(p-1)/2\). At or before the tie let \(z_i=\sin\phi_i\), \(v_i=\cos\phi_i>0\), \(a=1/\sqrt2\), and \(k_i=1-3z_i^2\) on the bulk. In the notation of the [two real endpoints](real-two-marks-91.md), for some real bulk log-amplitudes \(g_i\) the old plus factors at the two endpoints are \(e^{g_i}(v_i\pm z_i/a)\), and the old minus factors are \(e^{-g_i}(v_i\mp z_i/a)\). The two weights at zero are \(r_\pm^2=h\pm d>0\). Compare to the corresponding positive stationary pairs at these same two marks and **any single fixed positive bulk profile** \(k'_i\). Write \(g'_{i,\pm}\) for their half log-ratios, \(q_i=\sqrt{k'_i}\), and
\[
 G_i=g'_{i,+}-g'_{i,-}=q_i^{-1}\int_{r_-}^{r_+} J(r^2,k')_{i0}\,dr,\qquad
 L_i^\pm=\sqrt{v_i\pm z_i/a}\ e^{\mp G_i/4}.
\]
The signed square obeys
\[
 \boxed{\quad \sum_{i\ne0}q_i(L_i^+-L_i^-)^2
          \ \le\ \sum_{i\ne0}(q_i-\sqrt{k_i})^2.\quad}                 \tag{1}
\]
Indeed for each pair \((P,Q)\) and its comparison \((P',Q')\) at the same marked weight, the sum of \((\sqrt{P'Q}-\sqrt{PQ'})^2\) is the sum of \((\sqrt{w'}-\sqrt w)^2\) minus \(n(m'-m)^2\), by the two complementary cross pairings. Take half the sum of these equalities over the two endpoints. On the bulk its left summand is exactly
\[
 q_i(L_i^+-L_i^-)^2+
 q_i[(L_i^+)^2+(L_i^-)^2]\,
 \left[\cosh\!\left((g'_{i,+}+g'_{i,-})/2-g_i\right)-1\right].
\]
Thus (1) drops only this nonnegative midpoint-amplitude term, the two marked square losses and the two squared mean changes, each of the latter four with its half weight. The equality of products at an old tie causes no division by a zero factor. [Endpoint energy identity](astra-velocity-92.md#simultaneous-changes-to-the-real-weights)

There is also a signed reconstruction of the actual bulk phase from this one real integral. Put \(T_i=\tanh(G_i/2)\) and \(\widehat z_i=aT_i/\sqrt{1+a^2T_i^2}\). With \(\theta_i=z_i/(a v_i)\), the left summand of (1) is at least \(q_i v_i\cosh(G_i/2)(\theta_i-T_i)^2\). Indeed after taking out \(q_i v_i\cosh(G_i/2)\) the remaining square is the squared difference of \(\sqrt{(1+\theta_i)(1-T_i)}\) and \(\sqrt{(1-\theta_i)(1+T_i)}\). Their sum is at most two by Cauchy–Schwarz. Their squares differ by \(2(\theta_i-T_i)\). The map \(T\mapsto aT/\sqrt{1+a^2T^2}\) is \(a\)-Lipschitz. In particular, for \(k'_i=\max(k_i,e)\), \(\delta=1-e\) and \(\widehat k'_i=1-\min(3\widehat z_i^2,\delta)\),
\[
 \sum_{i\ne0}\cosh(G_i/2)(z_i-\widehat z_i)^2
 \le {a^2\over\sqrt{2e/3}}\sum_{i\ne0}(q_i-\sqrt{k_i})^2,\qquad
 \sum_{i\ne0}(k'_i-\widehat k'_i)^2
 \le {12\delta a^2\over\sqrt{2e/3}}\sum_{i\ne0}(q_i-\sqrt{k_i})^2.       \tag{2}
\]
The second bound uses the global \(2\sqrt{3\delta}\)-Lipschitz constant of the truncated quadratic. All sums are unnormalized. Only the sites with \(k_i<e\) supply the right side, even though the reconstructed profile is tested everywhere.

## How much actual deficit must see a large signed column

Take \(e=1-10^{-8}\), \(\delta=1-e\), \(q=\sqrt e\), \(b_i=(e-k_i)_+\), and \(\lambda_i=b_i/\sum b\) on the bulk. At least one true tie makes the denominator positive. Write \(\sigma_i=\operatorname{sgn}z_i\). Define
\[
 g_* = \operatorname{arctanh}\!\left(0.99\sqrt{2\delta/(3-\delta)}\right),
 \qquad A=\{i:b_i>0,\ \sigma_iG_i>2g_*\}.
\]
Then the following inequality retains the actual weights on the paying sites:
\[
 {13\over1000}\big(1-\lambda(A)\big)
 \le\sum_{i\in A}\lambda_i{q-\sqrt{k_i}\over q+\sqrt{k_i}}
 \le\lambda(A).
                                                                    \tag{3}
\]
In particular \(\lambda(A)\ge13/1013>0.0128\). This is a fraction of deficit, not a lower bound on the number of distinct sites. A site with a tiny deficit can pay only a small fraction of its own \(\lambda\)-mass on the right of (3).

For the proof subtract each site's budget in (1) from its square loss. This net term is nonnegative off the selected set. On a selected site put \(r=\sqrt{1-k_i}\), so that \(v_i=\sqrt{1-r^2/3}\), \(|z_i|/a=\sqrt{2/3}\,r\), and \(b_i=r^2-\delta\). As a function of \(g=\sigma_iG_i/2\) its net term is exactly
\[
 D_i(g)=2q[v_i\cosh g-\sqrt{2/3}\,r\sinh g]-e-k_i .
\]
Its value is at least \(-(q-\sqrt{k_i})^2\) on every site with \(b_i>0\). On \(A^c\) it is at least \(D_i(g_*)\), since \(\tanh g_*<\sqrt{2/3}\,r/v_i\), including at \(r=1\). We show \(D_i(g_*)\ge0.013 b_i\) uniformly.

* If \(r\le c=1/100\), put \(\rho=0.99\). The squared-difference bound used in (2), evaluated at \(g_*\), gives a square loss at least \(2q\sqrt{1-c^2/3}(r-\rho\sqrt\delta)^2/(3-\delta)\). Here \(\sqrt{2/3}\,r/v_i\ge r\sqrt{2/(3-\delta)}\). Also \((r-\rho\sqrt\delta)^2\ge(1-\rho^2)(r^2-\delta)\), by completing the square. The budget divided by \(b_i\) is at most \(c^2/(q+\sqrt{1-c^2})^2\). The resulting lower bound on \(D_i(g_*)/b_i\) exceeds \(0.01324\).
* If \(c\le r\le1\), concavity gives \(v_i\ge1-(1-\sqrt{2/3})r^2\). Use \(\cosh g_*\ge1\) and \(r\le r^2/c\). Then \(D_i(g_*)/r^2\) is at least \(1-2q(1-\sqrt{2/3})-2q\sqrt{2/3}\sinh(g_*)/c-(1-q)^2/c^2>0.619\). Since \(b_i\le r^2\), this proves the required bound here too.

The sum of the net terms is at most zero. Combining the two bounds gives (3). In the nominated square, put \(\ell=|r_+-r_-|\), \(\eta=\operatorname{sgn}(d)\) and let \(I\) be the unoriented interval between the two marks in square-root coordinates. For each \(i\in A\), the [real marked interval length](astra-velocity-92.md#quantitative-arithmetic-tests) gives
\[
 \frac{\sqrt n}{\ell}\int_I\eta\sigma_i J(r^2,k')_{i0}\,dr
 >2q g_*\,\frac{\sqrt n}{\ell}>947.03 .                              \tag{4}
\]
The lower constants are uniform in the prime and the ray. Both the signs and the measure in (3) can be recovered from the real midpoint reflection \(c_i=J_{w,i0}\): on the selected bulk, \(\eta\sigma_i=\operatorname{sgn}(c_i)\) and \(b_i=(3Bc_i^2-\delta)_+\), with \(B=v^2/(4w_0)\) for \(u+iv=n/t\). [Exact midpoint column](real-phase-projection-89.md#the-exact-column-and-the-real-weight-equations)

## The two signs in the same exterior test

At each \(r\in I\) use the exterior inverse Gram entries \(d_{si}\) and caps \(U_{si}\) from [the two-row deletion formula](astra-minors-93.md#a-signed-test-after-deleting-two-rows), with tilts from the real stationary pair for \((r^2,k')\). Define
\[
 M_i(r)=\mathbf1_{\eta\sigma_i d_{+i}>0>\eta\sigma_i d_{-i}}\min(U_{+i},U_{-i}).
\]
For large eligible primes the two exterior Grams are invertible. On each selected site \(j=J(r^2,k')_{i0}\) and \(m=rq/W\) satisfy \(2\Pi_{+i0}=j-m\) and \(2\Pi_{-i0}=-j-m\). Whenever \(\eta\sigma_i j>m\), both required signs hold together and \(\min(U_{+i},U_{-i})\ge |j|-m\). Otherwise \(\eta\sigma_i j\le m\). In all cases \(\eta\sigma_i j\le m+M_i(r)\), with \(\sqrt n m<0.6\) by the bound on \(W\). Thus the **same** set carrying at least \(13/1013\) of the deficit satisfies
\[
                {\sqrt n\over\ell}\int_I M_i(r)\,dr>946.43
                \qquad \text{for every }i\in A.                      \tag{5}
\]
The qualifier in (5) is a joint sign and size test along the actual interval. A bound on the deficit fraction satisfying (5) below \(13/1013\) would therefore exclude a first tie. R93's single-mark bound of 955.4 still applies at its own common mark.

At \(p=173,\ t=2031/128+i/131072\) the certified real-start ray stays strictly below contact. Taking \(e=1-2\cdot10^{-14}\) makes twelve full sites contribute deficit. All twelve pass the sitewise \(0.99\) log threshold for this \(e\). At both genuine comparison marks the four contributions in (1) recover the budget \(8.31066447045\ldots\cdot10^{-30}\); the signed-square part is \(1.31336285199\ldots\cdot10^{-43}\). The test uses the smaller deficit threshold to exercise the comparison at this finite prime.

On the same prime at real part \(1/50\), an independent replay follows the [true first contact at the singleton 43](astra-contact-91.md). With \(e=1-10^{-8}\), all 85 bulk sites carry deficit and 83 pass the signed log threshold. The two sites in inversion orbit 9 have the **wrong sign** of the real log difference. The passing sites carry more than 99.95% of the deficit. At the tied site \(G_{43}\in(1.9598,1.9600)\), and the total square loss lies in \((0.864,0.866)\) against a budget in \((2.5022,2.5024)\). Thus a requirement of individual sign agreement at *every* selected site already fails on a genuine first tie at a different floor. [Arb replay](astra-minors-94-check.py) · [Outward records](astra-minors-94-checks.jsonl)

1. Bound the deficit-weighted quantile of the joint signed integral (5) directly, using the midpoint column to generate both the real profile and the labels. The stronger cost in (3) discounts small deficits even on sites with large real integrals.
2. Use (2) to compare the entire clamped profile against the one recovered from its real endpoint integrals. A perturbation argument based only on independent small bulk changes lacks this signed constraint. The fixed-floor arbitrary-profile upper and the absence of a cold first tie through all primes remain open.
