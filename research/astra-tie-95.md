# A real comparison profile determined by the floor alone

At every point of the closed square of half-width \(2^{-17}\) about \(2031/128\) there is a unique self-consistent real comparison profile for each lower cutoff \(0<e<1\). It uses only the Paley sectors, the floor \(t\) and the cutoff. For \(e=1-10^{-8}\) the iteration constructing it is a contraction with constant below \(0.000123\) in full counting second norm. At a true first tie, more than **1.256% of the actual deficit mass** must see the signed interval average above \(947.03/\sqrt n\) on this one real profile. At \(e=0.27\), an individual interval average on the corresponding floor-determined profile must exceed **\(6.72\cdot10^6/\sqrt n\)** in absolute value. If \(m\) sites tie, the reconstructed square-root product excess of the near-flat profile must have counting second norm above \(0.08128\sqrt m\). The smaller cutoff allows a wider range of bulk weights. These are necessary conditions, with no through-primes upper for the selected columns.

## Construction from real positive optimizers

Put \(a=1/\sqrt2, u+iv=n/t, d=v/a, q_f=\sqrt e, \delta=1-e\). For a bulk vector \(q\in[q_f,1]^{n-1}\), solve for the marked midpoint \(h=h(q^2)\) by the strictly increasing scalar equation [R91, (1)](real-two-marks-91.md#eliminate-the-two-marked-floors). At marked weights \(h\pm d\) and common bulk weights \(q^2\), take the real positive optimizers \(P^\pm,Q^\pm\). Define
\[
 G_i(q)=\tfrac12\log(P_i^+/Q_i^+)-\tfrac12\log(P_i^-/Q_i^-),\qquad
 F_i(q)=\max\left(q_f,\,[1+(1+a^2)\sinh^2(G_i(q)/2)]^{-1/2}\right).
 \tag{1}
\]
All norms below use unnormalized individual-site counting. Set
\[
 D=3|d|/(u-|d|)<2.05\cdot10^{-6}.
\]
For any two input profiles, the change in **each** square-root mark is at most \(D\|q-q'\|_2\). Indeed [R91, (3)](real-two-marks-91.md#eliminate-the-two-marked-floors) bounds the midpoint change by \(6|d|\|q-q'\|_2/\sqrt{u-|d|}\). The same bound applies to nonnegative inputs including genuine ties. With the mark held fixed, the [real differential](marked-response.md#weighted-complementary-projections) bounds the bulk log change by \(\|q-q'\|_2/q_f\). Holding the bulk fixed, its analogous bound is the square-root mark change divided by \(q_f\). Thus
\[
 \|G(q)-G(q')\|_2\le 2(1+D)\|q-q'\|_2/q_f.
\]
Write \(z(G)=a\tanh(G/2)/\sqrt{1+a^2\tanh^2(G/2)}\). The outer function in (1) is \(\sqrt{1-\min(3z(G)^2,\delta)}\). Its Lipschitz constant is at most \(L=a\sqrt{3\delta}/(2q_f)\), since \(z\) is \(a/2\)-Lipschitz. At \(\delta=10^{-8}\) this proves the stated global contraction with constant \(K=2(1+D)L/q_f<0.000123\). Iteration from the all-ones vector therefore gives the unique fixed point \(q_*\); a trial in the box has counting second-norm error at most \(\|q-F(q)\|_2/(1-K)\).

For any \(0<e<1\), continuity and the compact box already give a fixed point. To prove uniqueness at wider cutoffs, reconstruct the complex factors at a fixed point by
\[
 A=(P^++P^-)/2+ia(P^+-P^-)/2,\qquad
 B=(Q^++Q^-)/2+ia(Q^+-Q^-)/2 .
\]
They lie in the complementary sectors with equal means and mark \(AB=s=n/t\). On the bulk their phases are opposite, with plus phase \(\psi_i=\arctan(a\tanh(G_i/2))\) and product
\[
 Q_i^*=q_{*,i}^2[1+(1+a^2)\sinh^2(G_i/2)]\ge1.                    \tag{2}
\]
In particular \(Q_i^*>1\) exactly where the unclamped value of (1) is below \(q_f\). The symbol \(Q_i^*\) here denotes the reconstructed product.

For these rows the scalar map from \(U=A-B=x+iy\) to \(S=A+B\) on the bulk is strictly contractive on every compact line segment in the metric \(a^2dx^2+dy^2\). To see this, put \(\sin^2\psi_e=\delta/3\). In the domain \(y^2\le4\sin^2\psi_e+x^2\tan^2\psi_e\) take \(S=\sqrt{4+U^2}\) on the positive sheet. The derivative obeys the strict metric contraction test of [R90, (2)](astra-column-90.md#a-scalar-extension-and-fixed-point-rigidity), since every relative phase there has magnitude at most \(\psi_e<\arctan a\). Outside, prescribe
\[
           \Re S\pm\Im S/a=\sqrt{(x\pm y/a)^2+4e}.
\]
These are precisely the endpoint sums at common product \(e\). The two linear coordinates \(x\pm y/a\) diagonalize the metric up to a constant factor, and each real square-root map has derivative of magnitude strictly below one. The maps agree on the two boundary curves. For completeness, at fixed \(x\) the endpoint-product-\(e\) branch has product \(Q=e/(1-3\sin^2\psi)\) and \(y^2=4Q\sin^2\psi+x^2\tan^2\psi\), strictly increasing in \(|\psi|<\arctan a\). Hence it is the stated exterior branch whenever \(Q>1\). Integrating the derivative on the finite pieces of a compact segment gives the claim.

At the mark the exact equal-product secant multiplier between two rows is \(\tanh((g_0+g'_0)/2)\) for the complex half log ratios with positive-chart lifts. Their relative phases have magnitude at most \(|\arg s|/2<\arctan a\): the [midpoint real-column identity](real-phase-projection-89.md#the-exact-column-and-the-real-weight-equations) gives marked factor tangents \(v(1\pm J_{00})/(2w_0)\) of common weak sign, also for positive nonunit real bulk products by the same imaginary-row pairing. The multiplier is strictly contractive in the same metric. Now \(U-U'=K_{\rm Paley}(S-S')\) is nonexpansive, while any differing coordinate would give a strict loss in the reverse direction. All differences vanish. Recovering \(q_*\) from the endpoint products proves uniqueness for every cutoff. This argument supplies no uniform iteration rate outside the near-flat contraction range.

## The actual signed deficit on the single selected profile

Suppose an unforced real-start ray reaches a first tie at this floor. Write \(z_i=\sin\phi_i, k_i=1-3z_i^2, q_i^0=\sqrt{\max(k_i,e)}\), \(B_0=\|q^0-\sqrt k\|_2^2\), and \(h_0=h(k)\). For this paragraph take \(\delta=10^{-8}\). At fixed midpoint \(h_0\), let \(G^0\) compare the two real rows with bulk \((q^0)^2\). The [signed square of R94, (2)](astra-minors-94.md#the-two-endpoint-comparison-including-zero-factors) gives
\[
 \|z-z(G^0)\|_2\le a(q_f\sqrt{2/3})^{-1/2}\sqrt{B_0}.
\]
The cutoff square root is \(\sqrt{3\delta}/q_f\)-Lipschitz as a function of \(z\). Updating the midpoint from \(h_0\) to \(h((q^0)^2)\) changes the two endpoint logs in difference by at most \(2D\sqrt{B_0}/q_f\) in second norm. Applying the contraction residual bound to \(q^0\) therefore proves
\[
 \|q_*-q^0\|_2\le C\sqrt{B_0},\quad
 C=\frac{(\sqrt{3\delta}/q_f)a(q_f\sqrt{2/3})^{-1/2}+2LD/q_f}{1-K}
 <0.000136.                                                        \tag{3}
\]

Use the R94 square with the old endpoints at \(h_0\pm d\) and the new ones at \(h(q_*^2)\pm d\). The proof by the two complementary cross pairings permits different old and new marked weights: their square-root differences squared simply enter the budget, with weight one half at each endpoint. Discarding the nonnegative marked losses, mean changes and midpoint amplitude errors gives the bulk square bound with right side at most \((1+D^2)\|q_*-\sqrt k\|_2^2\le(1+\epsilon)B_0\), where \(\epsilon=(1+D^2)(1+C)^2-1<0.000273\). The two bulk factors inside the R94 square use the actual signed phases and the single new log difference \(G(q_*)\). Restrict to \(b_i=(e-k_i)_+>0\), replacing their prefactor \(q_{*,i}\ge q_f\) by \(q_f\).

Put \(g_*=\operatorname{arctanh}(0.99\sqrt{2\delta/(3-\delta)})\), \(A=\{b_i>0:\operatorname{sgn}(z_i)G_i(q_*)>2g_*\}\), and \(\lambda_i=b_i/\sum b\). Subtracting the original budget shows that the sum of the R94 net terms on the deficit sites is at most \(\epsilon B_0\). On \(A^c\) the sitewise lower is \(0.013 b_i\); on \(A\) it is \(-(q_f-\sqrt{k_i})^2\), by the two ranges in [R94, (3)](astra-minors-94.md#how-much-actual-deficit-must-see-a-large-signed-column). Hence
\[
 .013(1-\lambda(A))\le
 \sum_{i\in A}\lambda_i\frac{q_f-\sqrt{k_i}}{q_f+\sqrt{k_i}}
 +\epsilon B_0/\sum b .
\]
As \(B_0\le\sum b\), this gives \(\lambda(A)\ge(.013-\epsilon)/1.013>0.01256\). Let \(I_*\) join the two marks \(\sqrt{h(q_*^2)\pm d}\) in increasing order and put \(\eta=\operatorname{sgn}d\). Then every \(i\in A\) satisfies
\[
 \frac{\sqrt n}{|I_*|}\int_{I_*}\eta\operatorname{sgn}(z_i)
               J(r^2,q_*^2)_{i0}\,dr>947.03 .
\]
Indeed the oriented integral is \(q_{*,i}G_i(q_*)\) and the [R92 length bound](astra-velocity-92.md#quantitative-arithmetic-tests) uses only \(h\ge u\). Both signed exterior caps must also have joint oriented integral above \(946.43\) in the same scaling for sufficiently large eligible primes. In applying [R94's two-sign test](astra-minors-94.md#the-two-signs-in-the-same-exterior-test), the rank-one background is now \(rq_{*,i}/W\); its scaled value is bounded by \(\sqrt{n/(n-1)}/(2q_f)<0.6\) for large \(n\). Only the deficit probabilities and their signs still refer to the true tie.

## A test with no input from the unknown tie

If all reconstructed bulk products in (2) equal one, the reconstructed row is an exact unforced pair with every bulk phase strictly inside the cap. It cannot coexist with a true tie. Indeed for two such unit-bulk, equal-mark rows with phases in the closed cap, the same-product secant at each site has multiplier \(\tanh((g_i+g_i')/2)\) of ordinary complex modulus strictly below one, since the half-sum relative angle has magnitude at most \(\arctan a<\pi/4\). The \(K_{\rm Paley}\) contraction forces coincidence. Thus some site of the fixed profile must have \(Q_i^*>1\), hence \(q_{*,i}=q_f\). There
\[
 \left|\int_{I_*}J(r^2,q_*^2)_{i0}\,dr\right|
 >2\sqrt e\,\operatorname{arctanh}\sqrt{(1-e)/(1+e/2)} .
\]
After multiplying by \(\sqrt n/|I_*|\), the bound exceeds \(956.59\) at \(e=1-10^{-8}\) and \(6.72\cdot10^6\) at \(e=0.27\). The site and interval may change with the cutoff.

The reconstructed excess also prices a shortfall on any collection \(T\) of actual tied sites. Set \(r_i=\sqrt{Q_i^*}\), \(X_i=r_i\sin\psi_i-\sin\phi_i, Y_i=r_i\cos\psi_i-\cos\phi_i\) on the bulk. Complementary Hermitian pairing gives \(\sum\Re[(A'-A)\overline{(B'-B)}]=n|M'-M|^2\ge0\). At the equal-product mark the summand is nonpositive by the ordinary secant above. At each bulk site it is at most \(Y_i^2-X_i^2\): the two cross terms sum to \(2r_i\cos(\phi_i+\psi_i)\cosh(\Re(g_i'-g_i))\) before subtraction. Thus \(\|X\|_2\le\|Y\|_2\). With \(m_i=(\phi_i+\psi_i)/2\), \(Y_i\cos m_i+X_i\sin m_i=(r_i-1)\cos((\phi_i-\psi_i)/2)\). It follows that
\[
 \sum_{i\in T}\left(1/\sqrt3-\operatorname{sgn}(z_i)r_i\sin\psi_i\right)_+^2
 \le \frac{1+a^2}{(1-a)^2}\sum_{Q_i^*>1}(\sqrt{Q_i^*}-1)^2 .       \tag{4}
\]
In particular let $E=\|\sqrt{Q^*}-1\|_2$ and $m=|T|>0$. The identity $q_{*,i}^2=Q_i^*-3r_i^2\sin^2\psi_i\ge e$ bounds $\sqrt3\,|r_i\sin\psi_i|\le\sqrt{r_i^2-e}$. Average on the tied sites, use Cauchy–Schwarz in (4), and apply Jensen to the concave increasing function $r\mapsto\sqrt{r^2-e}$ on $r\ge1$. Since the average of $r_i$ over $T$ is at most $1+E/\sqrt m$, this gives $1\le\sqrt{(1+E/\sqrt m)^2-e}+k_a E/\sqrt m$, with $k_a=\sqrt{3(1+a^2)}/(1-a)$. The right side increases, and solving at equality gives the test
\[
 \frac{\|\sqrt{Q^*}-1\|_2}{\sqrt m}\ \ge\
 c_e=\frac{e}{k_a+1+\sqrt{(k_a+1)^2-(k_a^2-1)e}}\,.              \tag{5}
\]
At $e=1-10^{-8}$ the lower bound exceeds $0.08128$ per square root of the tie count, while at $e=0.27$ it exceeds $0.01731$. The left numerator is entirely floor-determined. An upper below $c_e$ on this counting norm excludes even a single tie without its location, sign or deficit distribution. A vanishing normalized average alone permits a singleton.

At \(p=173, t=2031/128+i/131072\), an outward real-only computation with the smaller \(\delta=2\cdot10^{-14}\) encloses the unique fixed profile within \(1.51\cdot10^{-41}\) in counting second norm. Precisely twelve sites in inversion orbits \(5,16,24,34,35,36\) have reconstructed product above one. The counting second norm of their square-root excess is between \(2.8828\cdot10^{-15}\) and \(2.8829\cdot10^{-15}\). The physical ray is strictly below true contact there by [R92's separate continuation](astra-velocity-92.md#finite-replay-and-next-tests). Thus the converse of the active-site necessity fails at this cutoff.

On the separate prime-173 ray at real part $1/50$, [the R91 first-contact certificate](astra-contact-91.md#first-tie-at-a-genuine-prime) places a genuine single tie at site 43 in $0.01294720<\Im t<0.01294721$. For every floor in that entire closed bracket the real comparison with $e=1-10^{-8}$ has $q_{*,i}=\sqrt e$ and $Q_i^*>1$ on all 85 bulk sites. Its counting square-root excess is between 1.50 and 1.54, above the lower from (5). Here $u>|d|$ and the marked relative angles are inside the cap, as required for the uniqueness and secant arguments. The small-ratio numerical contraction constant of the nominated square is not needed. [Outward checker](astra-tie-95-check.py) · [Three replay records](astra-tie-95-checks.jsonl)

1. Bound the high signed column or the counting excess in (5) on the floor-determined real profile, using its exact coordinate equation (1) at the two endpoint marks. Freely prescribed near-flat perturbations need not satisfy this equation.
2. At the near-flat cutoff, approximate that profile by contraction from unit bulk and test the exterior minor signs on the resulting profiles. The counting error after each iteration contracts; a passage from normalized residual estimates to a single exceptional site still needs arithmetic control.
