# Actual least-norm endpoints and a late cold secant

A late secant of the true zero-floor Picard path gives a sufficient prime test allowing endpoint collision excess of order \(T\). The additional requirement is that the actual path travel \(o(\sqrt T)\) between two times a positive fraction of \(T\) apart. The exact signed secant may be smaller still. This is a conditional reduction, and the finite score certificates below do not prove either asymptotic input.

The replay certifies the actual least-norm larger-theta endpoints before measuring their marked atom and signed orbit directions. It includes generic and degenerate optimal faces and the exact square controls.

## Keeping an interval of the actual time identity

Use the [round-44](astra-critical-44.md) notation at zero floor. Let \(X\ge0\) be any feasible row of sign \(\sigma\) and sum \(\sqrt n\), let \(\alpha=X_0\), \(d=X-j\), and set \(u_t=\sigma P_\sigma v_t\). Put \(E_t=\|v_t\|^2\). The true \(B_t,A_t,H_t\) are, respectively, the marked loss, the sum of squared mean losses, and the wrong-sign occupation of \(X\). Subtract the exact paired identities at \(0\le s<t\):

\[
\begin{split}
\langle d,u_t-u_s\rangle
+\alpha(B_t-B_s)-\tfrac14(E_t-E_s)
&=2(t-s)(\alpha-1)\\
&\quad +(A_t-A_s)+(H_t-H_s).
\end{split}                                                       \tag{1}
\]

The two reserves on the right are nonnegative on each interval even if \(E_t-E_s\) is negative. In the proved short marked window, \((B_t-B_s)/(t-s)=o(1)\) uniformly in both endpoints. Thus on the actual larger-theta sign, one can prove ordinary theta by showing the **upper** normalized signed secant

\[
\frac{\langle \sigma d-(v_t+v_s)/4,\ v_t-v_s\rangle}{t-s}\le o(1)          \tag{2}
\]

on a choice of intervals through all eligible primes. Here the energy difference from (1) is included before taking the upper bound. The difference vector is the true cold increment; a comparison of two independent orbit approximants requires an enclosure for their difference.

In particular take \(t=T\), \(s=\lfloor T/2\rfloor\), \(T\to\infty\) inside the arithmetic window, and \(X\) the least-norm larger-theta optimum. The two estimates

\[
\|X-j\|^2=O(T),\qquad \|v_T-v_{\lfloor T/2\rfloor}\|=o(\sqrt T)              \tag{3}
\]

would imply the conjecture without the smaller \(o(T)\) full collision assumption. Indeed \(\|v_s+v_T\|\le4\sqrt T\) by the true energy bound \(E_t\le4t\). Cauchy–Schwarz bounds the numerator in (2) by \((\|d\|+\sqrt T)\|v_T-v_s\|=o(T)\). Equivalently, a fixed supercritical mark with \(\|d\|=O(\sqrt T)\) forces order-\(\sqrt T\) movement on every such late half-prefix. The same argument works for varying intervals of length comparable to the larger time. It gives no prime upper bound on that movement. The square endpoint has \(\|d\|^2=r-2\) at order \(r^2\), outside the collision regime in (3).

## Certifying the actual endpoint

The floating Fourier LP proposes active even coordinates for both signs. For a pair of disjoint bulk supports covering all inverse orbits, the checker solves the two anchored Fourier systems by Arb. Invertibility and strict positivity verify actual feasible vectors. The exact opposite-sector pairing and their disjoint bulk supports imply that their normalized marks are reciprocals, and certify that each is optimal. Every even optimizer is confined to its own support by pairing with the opposite certificate. Invertibility at anchor one then forces uniqueness among even optimizers. Averaging under inversion preserves optimality and does not increase the Euclidean norm, so this also identifies the least-norm optimum over the full cone.

The square-system shortcut fails at primes 29 and 97, as the proposed supports have common zeros. The replay records that failure and uses exact elimination in \(\mathbb Q[Z]/(\Phi_n)\) instead. First it solves both anchored systems on the proposed supports and verifies positivity and exact complementary mass. It then tests the least norm on the entire allowed face of the larger sign. At 29 the anchored restriction on that face has full column rank. At 97 the two inactive allowed coordinates may increase, and the exact derivative of the squared norm is positive in each such coordinate direction while holding the other fixed. Every feasible difference then has nonnegative pairing with the selected endpoint, which certifies the minimum by convexity. These arguments reuse the exact support methods of [round 10](endpoint-norm.md) and [round 12](parallel-sampling-12.md).

At the prime squares the [subfield theorem](square-endpoint-uniqueness.md) identifies the unique plus optimum. For all selected least-norm endpoints the marked atom is measured by

\[
\omega=\frac{\alpha^2}{\|X\|^2},
\]

which avoids numerical rank thresholds entirely once the endpoint certificate is established.

On the actual bulk support \(I=\operatorname{supp}(X)\setminus\{0\}\), write \(b=X_I/\alpha\) and \(\ell=\sqrt n/\alpha-1\). The mass constraint gives the exact split

\[
\omega^{-1}=1+\frac{\ell^2}{|I|}+\left\|b-\frac{\ell}{|I|}\mathbf 1_I\right\|^2.
\]

The last two terms at prime 9413 are approximately \(1.94042\) and \(0.83533\), from the certified support size, atom, and mark. At square order 961 they are exactly \(15\) and \(0\), by the flat subfield support of size 16 including the mark. Both terms are nonnegative, so to obtain \(D(p)\omega_p\to\infty\) one needs each term to be \(o(D(p))\) on the least-norm larger-side endpoint. The split locates a possible loss in the density or the weights on the actual support.

## True orbit check and a finite warning

The [checker](endpoint-direction-45-check.py) applies the exact Paley multiplier by outward DFT arithmetic to dyadic centers. Nonexpansiveness propagates their global counting-\(L^2\) radii. It checks the accumulated (1) at consecutive reported times with both reserves enclosed, and reports the R44 directional energy

\[
L_t^{\rm dir}=\frac{\langle d,u_t\rangle_+^2}{\|u_t\|^2}
\]

together with \(B_t/t\), the raw secant, and the corrected secant of (1). This is a reproduction of the unrounded orbit from zero with explicit errors, not a fixed point substituted into its place.

For example, at \(p=101\) from time 16 to 64 the raw signed secant divided by time elapsed is about \(-0.0004105\), while the corrected value is about \(0.250565\). The certified normalized optimal mark is \(1.12413037\), so \(2(\alpha-1)\) is about \(0.248261\). The small raw late drift at this fixed field cannot be read as a prime-uniform limit: the exact marked loss repairs the inequality in (1). The same issue is visible in the small square controls. At prime 4001 the marked atom is about \(0.270896\) and the depth-64 directional energy divided by depth is about \(0.042086\). At square order 961 those values are \(0.0625\) and \(0.453073\), respectively. These are finite interval comparisons. The asymptotic criterion must retain the arithmetic window and an actual prime estimate on (2).
