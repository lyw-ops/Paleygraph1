# The two signed charges at an actual forced contact

At a first right-angle spread contact on the height-600 forcing line, the two signed charges of every real kernel direction are determined by the component of the actual residual perpendicular to any chosen affine line in the complex plane. This gives a prime-uniform estimate vanishing linearly with the imaginary floor, with explicit amplitude weights on the true active sites. A ramified physical branch at a positive remaining forcing parameter must have first fractional exponent exactly one half. In corank one it must be an ordinary square-root fold, and the sign-definite side of its real kernel direction must occupy strictly fewer active sites than the mixed side.

## The residual perpendicular to a line

Use the [actual cold forcing](astra-phase-86.md), on its closed square of half-width \(2^{-17}\) about \(2031/128\), for \(n=(p-1)/2\ge10^{30}\). Fix \(t\), put \(X=V_{600}(t)\), \(R=K\Phi_t(X)-X\) and \(q=1-\lambda\). Consider a first spread contact from the real forcing segment, within \(|\phi_i|\le\arctan(3/2)\), at \(q=q_*>0\). The marked site lies off the two extreme sets. Write \(s_i=\pm1\) on those sets, \(\phi_i=c+s_i\pi/4\), \(\rho_i=\Re z_i\) and \(v=i e^{2ic}\). Then \(|\tan c|\le1/5\).

Work in the even physical coordinates, using full counting sums so each inversion orbit has its actual multiplicity. For a log-null direction \(\nu\) the corresponding ordinary right and transposed left nulls are \(h_\nu=\Phi\nu\) and \(D h_\nu=U\nu\). The [contact real form](root-neutral-unfolding-86.md) uses real vectors \(a\) such that, after a common fixed phase normalization, the log direction equals \(a_i\) on the upper side and \(-i a_i\) on the lower. All complex nulls are complex linear combinations of these. For a real generator put
\[
 f_i=s_i e^{\rho_i}a_i,\qquad g_i=e^{-\rho_i}a_i,\qquad
 A_j=\sum_+a_i^j,\qquad B_j=\sum_-a_i^j .
\]
The rows \(f,g\) are real, have mean zero, and belong to the plus and minus sectors respectively. They vanish outside \(S=\operatorname{supp}a\). The factors \(A=\sqrt{t_i}e^{z_i}\), \(B=\sqrt{t_i}e^{-z_i}\) satisfy on that support
\[
 A\nu=\sqrt t\,e^{i(c+\pi/4)}f,\qquad
 B\nu=\sqrt t\,e^{-i(c+\pi/4)}g .
\]
Pair with the opposite completed factors \(B-qR/2\) and \(A+qR/2\) respectively. With \(F=\sum_S f_iR_i\), \(G=\sum_S g_iR_i\), ordinary complex bilinearity gives
\[
 F=\frac{2\sqrt t}{q}e^{-i(c+\pi/4)}(A_1-iB_1),
 \qquad G=-v F.                                                     \tag{1}
\]
The phase in the second equation is separated from the real axis. Fix any \(\theta,d\in\mathbb R\), put \(r_i=\Im(e^{-i\theta}R_i)-d\), and let \(Y=\sum_S f_i r_i\), \(Z=\sum_S g_i r_i\). Both sums are real. Mean zero removes \(d\). The real and imaginary parts of \(e^{-i\theta}F\) are \(-(Z+\Re(v)Y)/\Im(v)\) and \(Y\). In particular,
\[
 \frac{4|t|}{q^2}(A_1^2+B_1^2)
   =\frac{Y^2+Z^2+2\Re(v)YZ}{(\Im v)^2}
   \le\frac{13}{8}(Y^2+Z^2).                                       \tag{2}
\]
Here \(|\Re v|=|\sin 2c|\le5/13\). Equation (2) retains both actual signed sums, including their cross term. For example, it implies the two bounds
\[
 \sqrt{A_1^2+B_1^2}\le \frac{q}{2\sqrt{|t|}}\sqrt{13/8}\,
 \min\left\{
 \|r\|_{\infty,S}\sqrt{\|f\|_1^2+\|g\|_1^2},
 \ \|a\|_2\Big[\sum_S(e^{2\rho_i}+e^{-2\rho_i})r_i^2\Big]^{1/2}
 \right\}.                                                         \tag{3}
\]
All norms here are unnormalized except where explicitly indicated. The line can be chosen separately for each real direction. Collinearity of the residual values on its support forces both side sums of that direction to vanish exactly.

There are explicit prime-uniform prices for the choice \(\theta=d=0\). On the concentric half-size square, the actual height-600 residual satisfies
\[
 \|\Im R(t)\|_\infty\le2872\,|\Im t|,\qquad
 \limsup_{p\to\infty}\sup_{t:\Im t\ne0}
   \frac{\|\Im R(t)\|_{2,n}}{|\Im t|}<7.99\,10^{-203}.             \tag{4}
\]
The second norm is normalized. Each coordinate is real on the real axis. Apply the Cauchy derivative estimate on disks of radius approaching \(2^{-18}\) about every point of the vertical integration segment. The [height-600 outgoing interval](astra-adjoint-82-checks.jsonl) puts the sup norm below \(0.010954497\) on the full square. The [round-80 field-first estimate](astra-dissipation-80.md) bounds the uniform limsup of the normalized second norm by \(4(0.44992117)^{600}\), using the recorded [interval for the rate](astra-dissipation-80-checks.jsonl). Vector-valued Cauchy gives the same derivative estimate in that norm. This proves (4), also uniformly as the imaginary part tends to zero. In (3) the first choice therefore gives a coefficient less than \(460q|\Im t|\) multiplying \((\|f\|_1^2+\|g\|_1^2)^{1/2}\). The amplitude and support factors can grow through primes.

## The first fractional order on the incoming branch

For an arbitrary complex log null \(\nu\), the same two ordinary completed-factor pairings give
\[
 q_*(U\nu)^{\mathsf T}R=4t\sum_i\nu_i .                            \tag{5}
\]
The real form is invariant under \(\nu\mapsto s\bar\nu\). Moreover \(\sum\nu^2=0\) and \(\sum_+|\nu|^2=\sum_-|\nu|^2\). In particular if every left null annihilates the true forcing, then (5) gives \(A_1-iB_1=0\) for every real generator. Both real side sums vanish. They then vanish separately for every complex log null as well.

Parametrize the incoming ray by \(r=q-q_*>0\). The locally finite, bounded factor fibers at \(q_*>0\) give convergent Puiseux expansions at the contact. Assume the physical germ has a first noninteger term of exponent \(\alpha\), and write \(\omega\ne0\) for its incoming log coefficient. The [two-conjugate argument](root-neutral-unfolding-86.md#a-sufficient-forced-contact-bound-with-both-extreme-sets) proves that \(\omega\) is a contact null and that
\[
         \max_{i\in S_+'}\Im\omega_i\le\min_{j\in S_-'}\Im\omega_j,
 \qquad S_s'=\{i:s_i=s,\ \omega_i\ne0\}.                          \tag{6}
\]
This uses only the incoming chamber and the actual forced equations. Both active sets are nonempty. Their individual side sums cannot both vanish for \(\omega\): (6) would force every active imaginary part to vanish, contradicting \(\sum\omega^2=0\).

If \(\alpha>1/2\), the displacement in \(U\) is \(O(r^{\min(1,\alpha)})\). Expand \(U-K\Phi(U)+qR=0\), project against any \(U\nu\), and divide by \(r\). The linear displacement vanishes under projection and the nonlinear remainder is \(o(r)\). This forces \((U\nu)^{\mathsf T}R=0\) for every null, contradicting (6) by (5).

If \(\alpha<1/2\), the leading displacement is \(r^\alpha\Phi\omega\). At order \(r^{2\alpha}\) the forcing disappears. Since \((U\nu)^{\mathsf T}K=(\Phi\nu)^{\mathsf T}\) and \(\Phi_i''=4t_i/\Phi_i^3\), the projected equation gives \(\sum\nu\omega^2=0\) for every log null. Taking \(\nu=s\bar\omega\) yields \(\sum_+\omega|\omega|^2=\sum_-\omega|\omega|^2\). The equal quadratic masses on the two sides and (6) force all active imaginary parts to be one value \(u\). Take \(\nu=\omega\). The imaginary part of \(\sum\omega^3=0\) is \(3u\sum(\Re\omega)^2-mu^3=0\), where \(m=|S_+'|+|S_-'|\). Since \(\sum\omega^2=0\) gives \(\sum(\Re\omega)^2=mu^2\), one has \(u=0\) and then \(\omega=0\), again impossible.

Only \(\alpha=1/2\) remains. The same quadratic projection now includes \((U\nu)^{\mathsf T}R\). Combining it with (5) gives the inhomogeneous identities
\[
         \boxed{\quad \sum_i\nu_i(\omega_i^2-2/q_*)=0
                    \quad\text{for every log null }\nu.\quad}        \tag{7}
\]
In particular some real generator must have nonzero charges in (2). Thus if every real generator in a spanning family has collinear actual residual values on its support, the first contact admits a holomorphic continuation irrespective of kernel dimension. At general corank the exponent calculation leaves higher Puiseux terms open after a square-root leading term.

## A counting-size independent test for the true active support

Assume the incoming branch is ramified. Write \(m_s=|S_s'|\), \(m=m_++m_-\), \(\delta=|m_+-m_-|/m\), \(C=2/q_*\), and take \(u\) between the two extrema in (6). Put \(y_i=\Im\omega_i\), \(w_i=|\omega_i|^2+C\). Taking \(\nu=s\bar\omega\) in (7) gives \(\sum_+w_i y_i=\sum_-w_i y_i\). Since the quadratic masses on the two signs agree, the incoming order gives the exact absolute-deviation identity
\[
      \sum_{S_+'\cup S_-'}w_i|y_i-u|=C(m_+-m_-)u.                 \tag{8}
\]
In particular \(u\ne0\), since otherwise every active imaginary part vanishes. On the smaller side all \(y_i\) have the sign of \(u\) and \(|y_i|\ge|u|\). For equal cardinalities every active \(y_i=u\), and either side may be chosen.

Let \(H=\sum y_i^2=\sum(\Re\omega_i)^2\). The imaginary part of (7) with \(\nu=\omega\) gives \(\sum [3(\Re\omega)^2-y^2-C]y=0\). Subtract \(u\) from the last factor and use \(|3(\Re\omega_i)^2-y_i^2-C|\le3w_i\) in (8). This gives \(|2H-Cm|\le3C\delta m\). Also \(|y_i|\le w_i/(2\sqrt C)\), so on any subset \(I\) of the active support
\[
    \left|\sum_I(y_i^2-u^2)\right|
                \le \delta m (u^2+\sqrt C|u|/2).                    \tag{9}
\]
If \(\delta<1/3\), let \(h_\delta>0\) be the positive root of
\[
       (1+\delta)h_\delta^2+(\delta/2)h_\delta=(1-3\delta)/2 .
\]
Applying (9) on the whole support shows that \(|u|/\sqrt C\ge h_\delta\).

Choose the real component of the contact kernel whose entries on the smaller side are \(y_i\) or \(-y_i\): take the imaginary part of its coefficient vector in the contact real form for a smaller upper side and the real part for a smaller lower side. For the resulting real vector \(a\), the relevant side sum has modulus at least \(m(1-\delta)|u|/2\). The equality of side quadratic masses for this real direction and (9) on the smaller side imply
\[
      \|a\|_2^2=2\sum_{\rm smaller}y_i^2
                \le m u^2(1+\delta+\delta/h_\delta).
\]
Its support is contained in \(S'=S_+'\cup S_-'\). Applying (3) gives the following necessary condition, with full counts on \(S'\), for every affine residual line:
\[
 q_*\!\left[\frac1m\sum_{S'}(e^{2\rho_i}+e^{-2\rho_i})
       (\Im(e^{-i\theta}R_i)-d)^2\right]^{1/2}
 \ \ge\ \sqrt{\frac{8|t|}{13}}\,
        \frac{1-\delta}{\sqrt{1+\delta+\delta/h_\delta}} .           \tag{10}
\]
The smaller eigenvalue of the true two-by-two residual covariance is the minimum of the bracket over all lines. Explicitly, center the two real coordinates of \(R\) at their weighted mean with weights \(e^{2\rho_i}+e^{-2\rho_i}\), sum the weighted outer products, and divide by \(m\). Thus comparison against the covariance tests (10) without choosing an orientation.

The right side exceeds \(1.89\) throughout the square whenever the active cardinalities differ by a factor at most \(3/2\). Indeed \(\delta\le1/5\) implies \(h_\delta>0.368\) by substitution. For equal active cardinalities (8) and the cubic give \(u^2=1/q_*\), and (10) exceeds \(3.12\). These bounds do not deteriorate with the cardinality of either side. On the half-size square (4) shows, for example, that a ramified contact with cardinality ratio at most \(3/2\) requires
\[
   \left[\frac1m\sum_{S'}(e^{2\rho_i}+e^{-2\rho_i})\right]^{1/2}
             >\frac{1.89}{2872\,q_*|\Im t|}\qquad(\Im t\ne0).
\]
There is also an explicit exclusion after deleting two outlying inversion orbits on the full square. The actual even residual is constant on each orbit. Fit a line through the residual values on any two active orbits, using any line through the common point if they coincide. The other distances are bounded by the residual diameter, strictly below \(0.02191\). If at most two orbits are active the required transverse RMS is impossible. Otherwise delete the two largest-amplitude orbits, ordered by \(e^{2\rho_i}+e^{-2\rho_i}\), and denote the rest by \(T\). For cardinality ratio at most \(3/2\), (10) forces
\[
       \frac1m\sum_{i\in T}(e^{2\rho_i}+e^{-2\rho_i})
                 >\frac{7441}{q_*^2}.
\]
In particular the third largest weight exceeds \((1.89/(0.02191q_*))^2\). At least three distinct active inversion orbits have \(|U_i|>343/q_*\), because \(|U_i|^2=|t|(e^{2\rho_i}+e^{-2\rho_i}-2+4\sin^2\phi_i)\) and \(0<q_*\le1\). At equal active counts the corresponding threshold is \(|U_i|>567/q_*\) on at least three orbits. These exclusions use the actual physical amplitudes and residual on the would-be singular support.

## The sign-definite side of a simple fold is smaller

At even corank one choose the real generator above. Then \(\omega=k\nu\) for a nonzero complex \(k\) and (7) gives
\[
      k^2=\frac{2}{q_*}\frac{A_1-iB_1}{A_3+iB_3}.                  \tag{11}
\]
For a ramified contact the numerator is nonzero by (5) and (6), and (7) forces the denominator to be nonzero. Conversely these two nonzero quantities make the scalar analytic reduction an ordinary fold at this solution: the forcing derivative is nonzero by (5), and the second derivative along the kernel is \(-4t(A_3+iB_3)\). The first derivative along the kernel is zero. The range equation can be eliminated by the implicit function theorem and its curvature correction is killed by the left null. Thus the reduced curve has a simple critical point of its projection onto the forcing parameter. For this to be a physical first contact it must also obey the incoming order.

If both active signs of the real generator contain both positive and negative entries, (6) requires \(\Im k=0\) on the upper side and \(\Re k=0\) on the lower side, a contradiction. If both sides have constant sign, either \(g\) or \(f\) has constant sign, contradicting its zero mean. Thus precisely one side is sign-definite. We can put it on the upper side: to exchange the sides take the negative incoming coefficient in (6), whose new upper and lower values are \((ik)b_i\) and \(-i(ik)(-a_i)\) for the old lower and upper real entries respectively. Equation (7) is invariant under this change. Normalize the real generator so that all its active upper entries are positive. Write \(b_i\) for its mixed lower entries in this orientation. The order requires \(\Im k<0\), and \(\Re k\ne0\), since (11) cannot be negative real when \(A_1,A_3>0\). Write \(b_i'=\operatorname{sign}(\Re k)b_i\) and \(B_j'=\sum_-(b_i')^j\). Then
\[
 T=\frac{\max_- b_i'}{\min_+ a_i}>0,\qquad
 r_0=\frac{|\Im k|}{|\Re k|}\ge T,\qquad
 2\arctan r_0=\arctan(B_1'/A_1)+\arctan(B_3'/A_3).
\]
The last formula follows by taking the arguments in (11), conjugating if \(\Re k<0\). Each denominator of an arctangent is positive, so both sides use the same principal argument. The equal quadratic masses and the mixed sign give \(B_3'<(\max b_i')\sum_-b_i^2\) and \(A_3\ge(\min a_i)\sum_+a_i^2\). Therefore \(B_3'/A_3<T\) and
\[
                       B_1'>T A_1 .                                 \tag{12}
\]
In particular \(m_-\max b_i'\ge B_1'>T A_1\ge m_+\max b_i'\). Equal active cardinalities exclude a corank-one ramified contact, regardless of the size of the actual residual or the variation of real amplitudes. Using the original eigenrows in (2), whose squared combined side charge is invariant under the sign exchange, gives the strict necessary lower bound \(q_*\sqrt{13/8}\sqrt{Y^2+Z^2}>2\sqrt{|t|}A_1\sqrt{1+T^2}\), for every line orientation on this true support.

The estimates above are ordinary analytic implications for the genuine branch. The [rational checker](astra-forced-87-check.py) reads the two earlier outward-rounded predictor records and verifies the constants in (4) and (10). The [replay](astra-forced-87-checks.jsonl) uses exact rational arithmetic. Existence of a fold on the cold square is open. The two amplitude norms in (3), relative to the signed side masses in (12), have no known uniform upper bound. A common two-dimensional cold section and the ordinary-theta limit remain open.

1. Compare the smaller eigenvalue of the true amplitude-weighted residual covariance with (10), beginning with balanced supports. At wider imbalances, bound the *transverse* residual correlations \(Y,Z\) in (2) on the smaller sign-definite set and its mixed partner. Project out the best affine residual line on their actual union, and compare the result with (12).
2. Beyond the factor-of-two range, impose (7) on every real generator together with (6). In particular \(\nu=s\bar\omega\) gives \(\sum_+\Im\omega (|\omega|^2+2/q_*)=\sum_-\Im\omega (|\omega|^2+2/q_*)\). Test this weighted order using the remaining Fourier rows on the active support.
