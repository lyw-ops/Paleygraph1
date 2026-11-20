# The erased mixed cost in the calibrated regime

On the original square and at the original cutoff, the necessary anisotropic cost of [round 99](schur-newton-99.md) is impossible throughout its calibrated regime. At a putative first hit, for **every** legal deletion \(S\) containing that hit, the surviving counting cost would satisfy
\[
 {1\over\sqrt n}\sum_{j\notin S}\big(206|\Im b_j|+0.380|\Re b_j|\big)
       <1.84\cdot10^{-8}
       \qquad(n^{1/4}\bar r\le0.025).
\]
Here \(b=B/\sqrt t\) includes the same rotation at the mark, \(B\) is the actual nonlinear remainder from the physical height-100 predictor, and \(\bar r=0.169724(0.51358)^{100}\) is the **old**, unchanged envelope. Erasing just the hitting site suffices whenever it is legal. The bound follows already on the whole source, so erasing the largest paying terms in addition costs nothing. The round-99 lower is \(3.41\cdot10^{-5}\). The sharpened estimate also contradicts that lower throughout \(n^{1/4}\bar r\le1.076\), wherever the eventual round-99 estimates apply.

Independently of the threshold in those translated-matrix estimates, the selected comparison never reaches its first activation for any eligible prime with \(10^{30}\le n\le10^{296}\), on the full square. Thus its bulk products remain one and its counting excess is zero on every such ray. At height 600 a separate counting contraction extends the genuine holomorphic stationary section on the square through \(n\le10^{358}\), from the former ceiling \(10^{347}\), with the same lower restriction \(n\ge10^{30}\). This last range has a coordinate cap and does not carry the stronger height-510 angle conclusion beyond its stated size.

## The genuine physical segment products

Use \(a=2031/128\), \(h=2^{-17}\), \(Q=\{ |\Re t-a|,|\Im t|\le h\}\), \(L=a-h\), \(n=(p-1)/2\), \(t_0=n\), and \(t_j=t\) otherwise. Let \(V_k\) be the [actual nine-center iteration](astra-predictor-76.md), \(R_k=V_{k+1}-V_k\), and use the counting mean for \(\|\cdot\|_{2,n}\). The positive envelopes of the nine-center returns increase coordinatewise. For the incoming segment \([V_{k-1},V_k]\), subtract the real Jacobi seed of representation mass \(m_S\) from the full upper mass \(m_k\) at the right endpoint. Its coordinates lie in disks of radius \(B_k=m_k-\inf m_S\) about the real seed, whose absolute value is at most \(s=2.828428\). Exactly the [seed-disk maximization](astra-source-88.md#the-seed-centered-disks-on-the-complex-square) bounds the physical scalar derivative on this segment by
\[
 d_k={s+B_k\over\sqrt{4L+(s+B_k)^2}}.
\]
The checker verifies \(2s(4L-2B_k^2)>4B_k(s+B_k)^2\) separately at every height, which gives the required monotonicity towards the real extremum of the disk. The marked derivative obeys the same bound. Define \(\rho_k=0.169724\prod_{j=1}^k d_j\). Since \(K\) contracts the second norm and the initial physical increment has norm below \(0.169724\), \(\|R_k\|_{2,n}\le\rho_k\). In particular,
\[
 \rho_{100}<2.4870\cdot10^{-32},\qquad
 \rho_{100}/\bar r<0.012739,\qquad
 \rho_{510}<2.651\cdot10^{-154},\qquad
 \rho_{600}<1.140\cdot10^{-180}.
\]
Every factor refers to its own physical segment. The last two products use the same finite-prime enclosure as the first, valid at \(n\ge10^{30}\).

For the imaginary part at height 100, the [round-99 differentiated-secant argument](astra-rotate-99.md#the-signed-mixed-term-on-the-actual-hitting-row) gives
\[
 \|R_k'\|_{2,n}\le d_k\|R_{k-1}'\|_{2,n}
     +D_*\|R_{k-1}\|_{2,n},\quad
 D_*={4(a+2h)21+2(4.768)\over(4L-4)^{3/2}} .
\]
Its original bounds \(\|V_j'\|_\infty<21\) through height 100 and \(\|R_0'\|_{2,n}\le42\) apply eventually through eligible primes. Every comparison factor \(d_j>0.4\). Divide by \(\rho_k\), sum the recurrence, and integrate vertically from the real diameter. Thus \(r_I=\|\Im R_{100}\|_{2,n}\le\beta\rho_{100}\), with \(\beta=h(42/0.169724+100D_*/0.4)<0.007472\). This is an upper relative to an envelope, without a lower bound on the actual residual.

Use the [round-99 physical square](astra-rotate-99.md) at the candidate hit, with \(r=\|R_{100}\|_{2,n}\). The true normalized first norms of \(b\) and \(\Im b\) are bounded by \(0.04919r^2\) and \(0.000055r^2+0.09834rr_I\), respectively. Therefore the claimed counting cost divided by \(\sqrt n\) is at most
\[
 \big[206(0.000055+0.09834\beta)+0.380(0.04919)\big]
 (\rho_{100}/\bar r)^2(n^{1/4}\bar r)^2.
\]
The [outward replay](astra-mixed-100-checks.jsonl) uses the unrounded factors for both cutoffs. This step needs the round-99 square and lower bound with their original eventual qualifiers. The next argument gives a separate explicit interval of primes, which includes both calibrated ranges above \(10^{30}\).

## A marked-only angular source and an explicit no-hit interval

Write \(P_k=\partial_t(V_k/\sqrt t)\) at **all** sites, \(D_k=\operatorname{diag}\Phi'_t(V_k)\), and \(\Phi_t(v)_i=\sqrt{4t_i+v_i^2}\). Direct differentiation of \(V_{k+1}=K\Phi_t(V_k)\) gives
\[
 P_{k+1}=K D_k P_k-
 {2n\over t\sqrt t\,\Phi_t(V_k)_0}K e_0.                         \tag{1}
\]
Indeed \(\Phi_i-D_{k,i}V_{k,i}=4t_i/\Phi_i\). The explicit time derivative of \(\Phi_i\) cancels this contribution off the mark; at the mark \(t_0=n\) is constant. The [physical marked-column price](astra-adjoint-82.md#physical-packet-prices-for-the-actual-derivative) is \(\sqrt p/n\) in packet 1. Since \(\|V_k\|_\infty<4.8\), the source in (1) costs at most
\[
 f={\sqrt{2+10^{-30}}\over L^{3/2}\sqrt{1-4.8^2/(4\cdot10^{30})}}<0.02238
\]
for \(n\ge10^{30}\). For \(P_0\) use Cauchy on disks centered in \(Q\) of limiting radius \(1/125-h\). On the [larger round-98 square](newton-boundary-98.md#control-the-newton-correction-on-the-full-square) the initial center has represented mass below \(4.8\), hence price at most \(2(4.8)\) by \(\pi(k)\le2k\). Dividing also by \(\sqrt{a-1/125}\) and the radius bounds this initial derivative price.

Here are the details for evaluating the direction in (1). Keep a length-50 vector of positive nonzero packet caps \(u_k\) for the propagated sources and an additional scalar price \(e\) for everything else, initially the Cauchy bound and \(u=0\). The positive weight measure of a packet is \(Q_k=(\delta_{-k}+\delta_k)/2+(k-1)\delta_0\). On each step form the retained multiplier measure \(\mu\) from the derivative of the arity-collected kernels at that step's current envelope, as in round 82. Convolve \(\mu\) with \(\sum u_k Q_k\), keep the paired nonzero masses at indices 1 through 50 as the next \(u\), and add \(f\) in packet 1. The geometric transport retains the nonzero weights and fills their packet zeros. The surviving finite convolution beyond 50 is charged its actual price to \(e\). The omitted tilted multiplier mass \(\delta\) costs at most \(10\delta\sum\pi(k)u_k\), and the finite-prime derivative repairs at most \(10^{-12}\sum\pi(k)u_k\), by the round-82 one-step bound. Transport the old scalar \(e\) at the full round-82 rate for that height. These are positive comparisons, valid without assuming a sign for the vector in (1). Their coordinate bound is \(e+\sum k u_k\). The [checker](astra-mixed-100-check.py) obtains
\[
             \|P_{510}\|_\infty<14.835
\]
on the full square. Reality at \(\Re t\) bounds \(\|\Im(V_{510}/\sqrt t)\|_\infty\) by \(14.835h\).

For \(10^{30}\le n\le10^{296}\) the **unnormalized** second norm of \(R_{510}\) is at most \(c=10^{148}\rho_{510}\). On a counting second-norm ball of radius \(3c<8\cdot10^{-6}\) about \(V_{510}\), the actual map is Lipschitz with factor below \(2/3\). Indeed this ball is inside the radius-\(1/2\) disk enlargement of the prefix, whose modulus and imaginary caps \(5.268,2.44\) give that bound by the physical scalar estimate of round 88. Center displacement is at most \(c\), so the ball maps into itself. Its holomorphic fixed point \(Y\), real and stationary on the real diameter, satisfies
\[
 \|\Im(Y/\sqrt t)\|_\infty
      \le14.835h+3c/\sqrt L<0.00011518<2\cdot10^{-4}/\sqrt3 .         \tag{2}
\]
At any first comparison activation its unit-product row \(U\) must coincide with \(Y\). To see this at that floor write \(Y_i=2\sqrt{t_i}\sinh y_i\) on the positive-real branch. The above coordinate disks give \(|\Im y_i|<0.4\) using \(|\sin\Im y_i|\le|\Im(Y_i/(2\sqrt{t_i}))|\). The [first-hit phases](same-floor-97.md#the-actual-first-boundary-lag-is-residual-scale) of \(U_i=2\sqrt{t_i}\sinh z_i\) have \(|\Im z_i|<0.001\), including the mark. Thus \(|\tanh((y_i+z_i)/2)|<1\) at each site. Subtracting the two stationary equations and taking the counting second norm gives equality of the rows, since the field is finite and \(K\) contracts. At a hitting bulk site \(|\Im(U_i/\sqrt t)|\ge2\cdot10^{-4}/\sqrt3\), contradicting (2). Continuity from the real diameter in the [selected comparison](astra-count-96.md#stop-at-the-first-boundary-of-the-selected-real-profile) then gives zero excess throughout each ray.

Finally \(\sqrt n\rho_{600}<1/8\) for \(n\le10^{358}\). The radius-\(1/2\) counting contraction about \(V_{600}\) from [round 88](astra-source-88.md#the-seed-centered-disks-on-the-complex-square) applies literally with this improved product. This proves existence of the genuine stationary branch there, with \(|m_p|<3/\sqrt n\). The positive angular comparison at 510 and the residual contraction at 600 are finite-depth results. At unbounded order this calculation supplies neither a uniform exterior upper nor a growing physical sequence with a common phase margin.

1. Propagate the signed derivative of the *increment* in (1), retaining the common marked-column source in two consecutive iterates before pricing. A growing-depth upper below \(2\cdot10^{-4}/(\sqrt3 h)\) with a vanishing counting residual would exclude the first hit on the corresponding sizes.
2. Outside the calibrated regime, estimate the signed or anisotropic exterior of the actual height-100 remainder after deleting its largest paying sources. The full-mass upper still grows like \(\sqrt n\) at fixed height.
