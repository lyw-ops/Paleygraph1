# Stationary existence from a translated Newton bound

A translated entry bound for the transported inverse can be used to construct the physical complex stationary branch directly. With a controlled first Newton step, the sufficient residual scale is \(n^{1/4}r=o(1)\) when the translated entries have size \(O(n^{-1/2})\). The proof does not assume that a true stationary continuation has already reached a first comparison activation.

## The mixed norm estimate

Use the normalization of [the original complex square](astra-resolvent-102.md). Let \(V\) be continuous on closed \(Q\), holomorphic inside and real on the real diameter. Use the physical activation \(\Phi_t\), whose specified scalar sheets have the corresponding continuity on the closed moving disks and are jointly holomorphic in the interior. Write
\[
 D=\Phi_t'(V),\quad A=I-KD,\quad Z=A^{-1}K,\quad
 R=K\Phi_t(V)-V,\quad H=A^{-1}R,\quad
 r=\sup_Q\|R\|_{2,n}.
\]
All quantities below are bounded uniformly on \(Q\). Suppose \(\|A^{-1}\|_{2\to2}\le a\), \(\|Z\|_{2\to2}\le z\), and \(\max_{i,j}|Z_{ij}|\le b n^{-\beta}\) with constants \(a,z,b\) independent of the field. Here \(0<\beta\le1/2\). Assume the scalar physical branches admit a common complex disk of radius \(d\) about each \(V_i(t)\), with curvature upper \(C\) on the disks and real-positive roots on the real diameter. The first Newton step is assumed to satisfy \(\sup_Q\|H\|_\infty\le h<d\), with \(zCh<1\).

Put
\[
 E_\infty=2bCa^2 n^{1-\beta}r^2 .
\]
If \(h+E_\infty<d\) and \(zC(h+E_\infty)<1\), there is a holomorphic stationary row \(Y\) in the interior with
\[
 \sup_Q\|Y-V-H\|_\infty\le E_\infty,\qquad
 \sup_Q\|Y-V-H\|_{2,n}\le ar .                                      \tag{1}
\]
In particular \(n^{(1-\beta)/2}r\to0\) suffices for the two strict inequalities given a fixed gap in the other hypotheses.

To prove (1), write \(Y=V+H+e\). With
\(B(u)=\Phi_t(V+u)-\Phi_t(V)-D u\), the exact stationary equation is \(e=ZB(H+e)\). On the closed ball with both bounds in (1), \(\|H+e\|_{2,n}\le2ar\) and \(\|H+e\|_\infty\le h+E_\infty\). Scalar Taylor's formula gives
\[
 \|B(H+e)\|_{1,n}\le 2Ca^2r^2,\qquad
 \|B(H+e)\|_{2,n}\le C(h+E_\infty)ar .
\]
The first gives the sup bound on \(ZB\) by the translated entry estimate, and the second gives the normalized second norm bound. The sup bound depends on the **square** of the normalized residual. The Lipschitz factor on this ball in normalized second norm is at most \(zC(h+E_\infty)<1\), by integrating the scalar derivative of \(B\) on each line segment. The finite-dimensional intersection of the two closed balls is complete in normalized second norm. Iteration from \(e=0\) stays in the ball and converges uniformly in the floor at fixed \(n\), so its limit is continuous on the closed square and holomorphic in the interior. At real floors it stays real on the prescribed sheets. Positive complementary factors at the real limit identify the physical solution by uniqueness.

## Angular implication and scope

If the nominal predictor \((V+H)/\sqrt t\) has a fixed strict imaginary gap below the [original cutoff's hitting coordinate](astra-marked-101.md#compare-with-the-true-derivative-before-integrating-the-angle) on \(Q\), (1) transfers the gap for all sufficiently large primes with \(n^{(1-\beta)/2}r\to0\). At real floors the row agrees with the physical solution. To exclude an actual first activation on the closed square, use the usual physical midpoint-secant uniqueness on the common sheets. The disk and cap must be chosen within that uniqueness sector. For example, phases of the two inverse hyperbolic sine lifts bounded by \(0.4\) and \(0.001\) give midpoint phase below \(\pi/4\), which makes every finite-field secant strictly contractive. A fixed strict margin can be checked at the same boundary floors. In the absence of the angular gap, (1) still gives the unforced stationary section under its own hypotheses.

The [shifted-column estimates](shifted-resolvent-96.md) give \(\beta=1/2\) at heights 100 and 250 and \(\beta=0.467\) at height 600. These are fixed-height results. Their recorded normalized residual caps do not tend to zero with \(n\) at the required scaled speed. The original problem still requires a compatible family of actual predictors, or a new signed control of the nonlinear tail. The [earlier quadratic first-hit comparison](newton-boundary-98.md) also used a translated entry bound and squared residual, but evaluated its remainder on a hypothesized true first-hit row. The present ball constructs a stationary branch using only predictor quantities.

1. Establish a compatible translated exponent, bounded first Newton step, and residual decay \(n^{(1-\beta)/2}r\to0\) on a genuine growing-depth family.
2. Test the nominal corrected angle at the same growing depths. A coordinate bound on \(H\) for existence can be much weaker than the rotated imaginary margin needed for no activation.
