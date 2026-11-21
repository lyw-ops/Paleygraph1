# Quadratic total correction from translating a phase cap

On the nominated square about $2031/128$, the unaveraged canonical price on **each** side of the centered cap is at most $1.4\cdot10^9 n(r')^2$, where $r'=\|R_{600}/\sqrt t\|_{2,n}$ is the normalized physical residual. The same conclusion holds on an open rectangle of tilted caps. This improves the first-power estimate for the total price, and prices the *full products*, including their squared marked-column mass on the cap. The proof compares the angular action at different boundaries with a single, cap-independent predictor. A separate real two-sector test applies when the center sweep balances positive corrections. Such a balanced row occurs at the explicit prime 173.

## The same predictor for a rectangle of phase boundaries

Use $s=u+iv=n/t$, $n=(p-1)/2\ge10^{30}$ and the closed physical cold square of half-width $2^{-17}$. Put $\theta_0=\arctan(1/\sqrt2)$, and first allow $|b|,|\theta-\theta_0|\le0.01$. Write $U=b+\theta, L=b-\theta$ for the upper and lower angles, $a=\tan\theta\in(0.69,0.73)$. The [rotated cap construction and work inequality](rotated-cap-93.md) apply globally here, with strict marked angles. Write $A,B$ for any genuine unrotated factors, $q_i=1+e_i$ on the bulk, $M$ their common mean and $E_\pm$ the counting corrections. All their unrotated arguments are in $(-0.64,0.64)$. Define $w^0=(s,1,\ldots,1)$.

For the [height-600 physical predictor](astra-source-88.md), let $Z=V_{600}/\sqrt t$, $S_Z=\sqrt{4w^0+Z^2}$ on its positive branches and $R'=KS_Z-Z$. The predictor factors $A_Z=(S_Z+Z)/2,B_Z=(S_Z-Z)/2$ have the exact products $w^0$. Their completed versions $A_Z+R'/2,B_Z-R'/2$ are in the genuine complementary sectors and have equal means. Both $Z$ and $R'$ have mean zero. Use the primes on $A'=e^{-ib}A,B'=e^{ib}B$ for the rotation, writing $D'=A'-B', S'=A'+B'$, and analogously for the predictor. In the Hilbert norm $|x+iy|_a^2=a^2x^2+y^2$ the linear map $T_b=K-i\tan b\,P_1$ is a contraction, where $P_1$ averages. Direct use of $K^2=I-P_1$ gives the filtered predictor error
\[
   D'=T_b S',\qquad T_b S'_Z-D'_Z=R_b=\cos b\,R'+i\sin b\,KR'.
\]
The true last preimage $H=\Phi_t(V_{600})-\Phi_t(V_{599})$ has sup norm below 0.005377, so $KR'=(I-P_1)H/\sqrt t$. The [centered predictor bounds](astra-column-90.md) now give
\[
 |Z|<1.20,\quad |\Im Z|<0.504,\quad
 \|R_b\|_\infty<0.00283,\qquad \|R_b\|_{2,n}\le1.01r'.
\]
The large marked value of $S_Z$ stays in the rotated predictor and does not enter this residual.

Set $d_i=|D'_i-D'_{Z,i}|_a$. On the bulk the scalar activation from $D'$ to $S'$ is globally nonexpansive. It has norm of the derivative below $0.90$ on every $a$-metric ball of radius $0.10$ about $D'_{Z,i}$. In fact $D'_Z=\cos b\,Z-i\sin b\,S_Z$ gives throughout each such ball $|\Im z|<0.63, |\Re z|<1.38$. Write $z=2\sinh(g+i\phi)$. Then $|\sin\phi|\le0.315, |\sinh g|<0.73$, the ball lies strictly inside the cap, and the determinant of $I-F'^*F'$ in the anisotropic metric exceeds
\[
 \frac{(1-2(0.315)^2)^2-(1/0.69-0.69)^2(0.63)^2/4}{(1+0.73^2)^2}>0.24 .
\]
The contraction criterion and determinant formula are those of [round 90](astra-column-90.md). The predictor itself is the genuine scalar activation on this ball: its unrotated bulk phase has $|\sin\phi_Z|\le0.252$, so the rotated predictor phase lies strictly inside the cap. The initial strictly contractive portion of the segment to the true row gives loss $d_i^2-|S'_i-S'_{Z,i}|_a^2\ge0.10d_i\min(d_i,0.10)$.

The marked secant has norm below $0.95$ on this entire rectangle. Indeed, with $\phi_i=(\arg A_i-\arg B_i)/2$, Hermitian complementary pairing gives
\[
 \sum_B q_i\sin^2\phi_i+|s|\sin^2\phi_0
   =(\sum_B q_i+|s|-|\sum_B q_i+s|)/2\le(|s|-u)/2.
\]
In particular $|\phi_0|\le|\arg s|/2$. On the corrected sites $|\phi_i|>0.59$, so the identity bounds their sum of products by $(|s|-u)/(2\sin^2(0.59))$, giving $|M|<1.1$ from its squared value. From $A-B=K(A+B)$, the Jacobi entry bound and the positive real parts give $|(A_0-B_0)/\sqrt s|\le2\sqrt{p|t|/n}\sec(0.64)\Re M<16$. Thus the marked relative amplitude $g_0=\log|A_0/B_0|/2$ has modulus below 3. The predictor marked log has modulus below $10^{-12}$ since $|Z_0|<1.2$. The rotated marked secant is multiplication by $\tanh(G+iF)$ where $|G|<1.51, |F|<0.011$, from the half-sum of these relative logs after subtracting $ib$. Its norm is at most $|\Re\tanh(G+iF)|+|\Im\tanh(G+iF)|/a<0.95$. These bounds use only the genuine and predictor marked endpoints.

Let $\mathcal S,\mathcal T$ be the bulk sets $d_i\le0.10, d_i>0.10$. Squaring $D'-D'_Z=T_b(S'-S'_Z)+R_b$, summing and using the contraction bounds just obtained gives
\[
    \sum_{\mathcal S} d_i^2+\sum_{\mathcal T}d_i+d_0^2
                    \le6000n(r')^2.                                      \tag{1}
\]
For details, the sitewise losses sum to at most $2\sum_i d_i|R_{b,i}|$. Absorb the cross terms on $\mathcal S$ and at the mark by Young with quadratic prices $0.05$ and $0.045$ respectively. On $\mathcal T$ their price is below $0.00566d_i$. The remaining coefficients exceed $0.0043$ everywhere and the residual-square price is at most $23(1.01)^2 n(r')^2$. In particular the mark enjoys a genuine quadratic estimate even when its counting displacement exceeds one.

## Oscillation of the angular action and the separate boundary prices

At a genuine pair put
\[
 P=\tfrac12\Im\sum_i w_i^0\log(A_i/B_i),
\]
using the individual positive-real-part logs. All differentiable selections at fixed floor satisfy $dP=-E_+\,dU-E_-\,dL$: the full product-weighted log variation vanishes by $\sum B\,dA=\sum A\,dB=nM\,dM$, and at a positive correction the bulk half log-ratio has imaginary part exactly the active endpoint. On a fixed cap all genuine roots are joined by the line of clipped fixed points from the same-sign secant equality, including after rotation. The differential therefore makes $P$ constant along that line. Compactness and the finite semialgebraic pieces justify integration in either endpoint as in [round 93](rotated-cap-93.md). The variable-floor action identity and its marked-log consequence are described in [the curvature note](cap-curvature-94.md).

There is one real number $P_*(t)$ **independent of both cap endpoints** such that
\[
                        |P-P_*|\le 7\cdot10^6 n(r')^2.                 \tag{2}
\]
To verify this, subtract the action of the unrotated predictor. For each log use its linear term at that predictor. In the two terms of the difference they combine, before the factor $1/2$ and imaginary part, to
\[
  \sum_i(B_{Z,i}A_i-A_{Z,i}B_i)=\tfrac12\sum_i R'_i(A_i+B_i).
\]
This is exact because cross-pairing both genuine factors with the opposite completed predictor gives the same result. Use $P_*=P_Z+\tfrac14\Im\sum R'S_Z$. Its remaining linear term costs less than $300n(r')^2$ even before the factor $1/4$: each unrotated factor displacement is at most $d_i/a$ by the secants. Apply Cauchy–Schwarz with (1) on $\mathcal S$ and the mark, and use $\|R'\|_\infty<0.0028$ on $\mathcal T$.

For the bulk log remainders, on $\mathcal S$ the predictor real parts are greater than $0.36$, since $\Re S_Z\ge\sqrt{4-(0.504)^2}$, and each displacement is at most $0.10/0.69$. Taylor's integral remainder along each straight factor segment bounds their sum by $60d_i^2$. On $\mathcal T$ their imaginary parts together cost at most $2\pi+|B_Z\Delta A|+|A_Z\Delta B|<70d_i$ using the positive charts, the predictor cap and $d_i>0.10$. At the mark both genuine and predictor real parts exceed $0.039\sqrt{|s|}$, since $|g_0|<3$. The same Taylor bound on both straight segments, now multiplied by $|s|$, is below $2000d_0^2$. Equation (1) proves (2) including $r'=0$. The linear cancellation at a common predictor is needed for this quadratic oscillation.

At fixed width (2) directly bounds the center integral of the full correction, including across switching parameters. At fixed center it bounds the signed width integral:
\[
 0\le\int_{b_1}^{b_2}(E_++E_-)\,db\le1.4\cdot10^7n(r')^2,\qquad
 \left|\int_{\theta_1}^{\theta_2}(E_+-E_-)\,d\theta\right|
 \le1.4\cdot10^7n(r')^2 .
\]
Both are for arbitrary ordered endpoints in the comparison rectangle. Also \(P_*\) is harmonic in the physical floor on the square's interior, by the holomorphic predictor, positive factor charts and the unconjugated bilinear residual term.

For $|b|,|\theta-\theta_0|\le0.004$ one can move $U$ down by $h=0.01$ with $L$ fixed inside the larger rectangle, or $L$ up by $h$ with $U$ fixed. The first move makes $E_+$ nondecreasing, the second makes $E_-$ nondecreasing, by [the one-boundary work inequality](rotated-cap-93.md). The absolute action difference along each segment is at least $h$ times its initial corresponding price. Consequently
\[
   \boxed{\quad E_+/n,\ E_-/n\le1.4\cdot10^9(r')^2,\qquad
        (E_++E_-)/n<1.8\cdot10^8\|R_{600}\|_{2,n}^2\quad}            \tag{3}
\]
in the last bound for nonzero residual. This yields total average below $2.8\cdot10^{-341}$ throughout the finite-prime cold range, and field-first limsup below $1.7\cdot10^{-407}$. On the centered cap $|H|/n\le3400(r')^2$ already holds for *all* saturated sites including ties, so $\sum_{H}q_i/n\le(2.8\cdot10^9+3400)(r')^2$. With the centered column identity $q_i=3B c_i^2$ on $H$, this bounds the true squared column tail by that same quantity times $n/(3B)$ for $v\ne0$. The normalized counting price still permits individual saturated sites at unbounded orders.

## Actual balance and a two-sector real test

Fix the floor and width on any compact interval of admissible centers. The canonical $I=E_+-E_-$ is continuous and nonincreasing by the center work inequality. Wherever $E_++E_->0$ it is strictly decreasing, with $-I_b\ge(1-a^2)/a$. In particular, if a cap-free center exists and the left and right endpoints of the center interval are outside its zero set, their imbalances are strictly positive and strictly negative. These strict signs persist in an open neighborhood of this floor by compactness and continuity in the floor as well as the center. At each nearby floor either a cap-free center exists, or an interior center has $E_+=E_->0$. In the latter case it is the unique balanced center. This applies on the far side of any first loss of a cap-free center for which the zero interval is strictly inside the admissible interval. At any individual floor with no cap-free center, absence of balance instead forces positive outward-side correction at the right endpoint if $I>0$ throughout, or at the left endpoint if $I<0$ throughout.

A balanced positive pair supplies two nonempty sign sets at the **same** true tilted row. The following constraint already applies when there are merely ties of both signs. Put $P^\pm=\Re A'\pm\Im A'/a, Q^\pm=\Re B'\pm\Im B'/a$, rescaling $P^\pm,Q^\pm$ reciprocally by $c_\pm,c_\pm^{-1}>0$ so each pair has equal mean. Their nonnegative products coincide on the bulk, say $k$, and their marked products are $\tau_\pm=h\pm v/a>0$, since rotations and reciprocal rescalings preserve the complex product. At a tie of sign $\sigma$, the favorable crossed product $P^+Q^-$ on the upper side and $Q^+P^-$ on the lower side is
\[
             F_i=Cq_i(c_+/c_-)^{\sigma},\qquad C=4\cos^2\theta .
\]
Choose any probabilities $\lambda^+,\lambda^-$ on respective nonempty sets of tied sites, disregarding their zero atoms, and any $z>0$. Repair their old zero weights to $z\lambda_i$, keep all positive old weights, and lift every other zero to $\epsilon>0$. Let $J(r)$ be the marked reflection of the resulting **one fixed positive bulk profile** with real mark $r^2$. Write $\ell=|\sqrt{\tau_+}-\sqrt{\tau_-}|$, $f_i=\sigma_i\sqrt{\lambda_i}$ on the selected support and zero elsewhere. Both probabilities have mass one, so $f\perp\sqrt w$ at every mark. For sufficiently small $\epsilon$,
\[
 \int_{\sqrt{\tau_-}}^{\sqrt{\tau_+}}\!\langle f,J(r)e_0\rangle\,dr
 \ \ge\ \sqrt z\sum_{\sigma,i}\lambda_i^\sigma
             \log\!\frac{Cq_i}{z\lambda_i^\sigma}
            -\ell\sqrt{n\epsilon/z}.                                    \tag{4}
\]
If all ties are selected the debit is zero. Indeed, apply [the real Hellinger inequality (2)](astra-velocity-92.md) at both endpoints, choosing the favorable factors at each repaired site. Their new crossed product equals its new bulk weight times the exponential of its signed real log-ratio change. The [physical real derivative](marked-response.md) integrates that change as $\int J_{i0}\,dr/\sqrt{w_i}$. The two mean rescalings cancel after averaging with the opposite equal masses. On omitted zero sites select the favorable old factors and take $\epsilon\le\min F_i$ there, giving nonnegative log terms. Their omitted signed integral costs at most $\ell\sqrt{n\epsilon/z}$ by $\|J(r)e_0\|_2\le1$. No limiting degenerate projector is needed. In particular the permitted $\epsilon$ can also be made small enough to incur any assigned positive debit.

If $M_\sigma=\sum_{i\in S_\sigma}q_i$ on the chosen sign sets, take $\lambda_i=q_i/M_\sigma$, $z=C\sqrt{M_+M_-}/\exp(2)$. The principal lower bound in (4) becomes $4\sqrt z$; this follows also by optimizing (4) first over both probabilities and then over $z$. The real orientation is $\eta=\operatorname{sign}(v)$ when $\ell>0$. At a single real mark on this interval both sector projectors obey
\[
 2\eta\langle f,\Pi_+ e_0\rangle=-2\eta\langle f,\Pi_- e_0\rangle
 \ \ge\ 4\sqrt z/\ell-\sqrt{n\epsilon/z}.
\]
The identity uses $f_0=0$ as well as $f\perp\sqrt w$. In particular one gets a signed real test on any designated upper/lower pair without a mean-mode debit from either Fourier sector. Taking just one site per sign and $z=1$ gives principal lower bound $2\log C+\log(q_iq_j)$ on the oriented column-difference integral. The selected real profile need not be nearly flat.

The [Arb256 checker](astra-center-94-check.py) solves the rotated equations **and** zero imbalance as one square interval system. At $p=173, t=1/50+17i/1000, a=1/\sqrt2$, it encloses $b=0.140094856451317\ldots$ and $E_+=E_-=0.415012360160602\ldots$. The upper orbit is fixed site $43$; the lower orbit is $\{29,57\}$. Their respective repair weights $1,1/2,1/2$ preserve evenness. Independent positive real stationary solves at the two resulting marks verify (4) with integral $4.32878920366525\ldots$ above lower bound $3.19050117734670\ldots$, without a regularizing debit. At the same floor a separate enclosure of the unit-bulk equations gives phase spread \(1.28748281929179\ldots>2\theta=1.23095941734077\ldots\), with both extremes in the bulk. In fact **no tilted center at this width admits a zero-correction pair** on the positive mean sheet with both rotated marked angles inside its cap. Otherwise its coordinatewise sums of relative phases with the enclosed unit-bulk pair lie on an interval of width at most \(1.28749+2\theta<\pi\), including the mark. Their means coincide, so the rotated [Hermitian secant identity](astra-phase-86.md) forces equality at every coordinate, contrary to the lower on the bulk spread. This prime and floor lie away from the nominated square. [Outward records](astra-center-94-checks.jsonl)

1. Test the signed two-sector integral (4) on like-cost upper/lower subsets of any balanced survivor at the nominated floor. The exact contrast cancels the common marked mean; individual projector upper bounds lose that cancellation.
2. Use the cap-independent action comparison around the true predictor to bound the *oscillation* of its quadratic residual remainder on a one-boundary segment in counting units. A bound below the one-site integrated work threshold would give an actual cap-free wider row. At present (3) controls the counting average.
