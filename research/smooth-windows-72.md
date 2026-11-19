# Smooth actual windows isolate the high-density part of a primary optimizer

On the actual undamped cold orbit, smoothly tapering the moving time windows gives both normalized \(L^1\) defect \(O(1/d)\) and normalized \(L^2\) defect \(O(d^{-1/2})\). The same windows retain the marked budget and small overlap of the raw positive rows. Consequently a true supercritical endpoint must place order-\(d\) collision energy on a joint cutoff where the opposite proposed row has a fixed negative deficit and the primary density exceeds a constant times \(d\). The older localized collision test did not require this density threshold.

Use the exact notation of [round 70](paired-windows-70.md) and the arithmetic marked horizon \(D(p)\). Let \(d\to\infty\), \(d=o(D)\), \(\eta=\sqrt{d/D}\), and let \(W_a=[a,a+d-1]\subset[1,D]\). Put
\[
  t_k=(k+1)(d-k),\qquad
  \omega_{a+k}=t_k^2/Z_d,\quad
  Z_d=\sum_{k=0}^{d-1}t_k^2,\qquad 0\le k<d.
\]
Extend the weights by zero. We use constants independent of \(p,D,d,a\), and both signs use the same weights. Call \(B_{s,\omega}=\sum_j\omega_j B_{s,j}\) the raw positive rows, \(Z_{s,\omega}=\sum_j\omega_j Z_{s,j}\) their sector projections, and \(G_\omega=\sum_j\omega_j g_j\) their scaled mean.

## Simultaneous choice of smooth windows

For selection only, pad the window energy by one site at each end, with the same weight \(w_*=\omega_a=\omega_{a+d-1}\):
\[
 H_a=\frac{\sum_j\omega_j g_j^2+w_*(g_{a-1}^2+g_{a+d}^2)}{1+2w_*}.
\]
The sum of these padded energies over the starts is at most \(\sum_{j=0}^{D+1}g_j^2\le D+2\), since the selection kernel still sums to one and is translated over the starts. There are at least \(\eta D\) windows with \(H_a\le1+4\eta\) for sufficiently large \(D\), by the same counting inequality as for the flat means in round 70. On all these windows \(G_\omega^2\le (1+2w_*)(1+4\eta)\) by Jensen.

The middle half of the \(t_k\)'s is bounded below by a positive constant times \(d^2\), so \(Z_d\asymp d^5\) and \(\max \omega_j\le C_0/d\). By positivity \(B_{s,\omega}\le C_0\bar B_{s,a}\) pointwise, where the bar denotes the flat-window average. Thus (2) in round 70 gives
\[
  \sum_a \mathbb E_{\mathrm{bulk}}[B_{+,\omega}B_{-,\omega}]
        \le C_0^2(d^2-1)/(6d).
\]
Discard the starts at most \(\lfloor\eta D/4\rfloor\) and the starts with overlap larger than \(C_0^2\eta\). At least \(\eta D/2\) windows remain. On each, the normalized mark factors \(m_s=Z_{s,\omega}(0)/\sqrt n\) satisfy \(1+o(\eta)\) by uniform marked cancellation. Taking \(\epsilon=8(\eta+w_*)\), define \(R_s=Z_{s,\omega}+[(1+\epsilon)m_s-G_\omega]b_s\). The mean direction is nonnegative on the bulk and the coefficient multiplying it is nonnegative.

## Both defect norms for the same profile

Let \(D_s=Z_{s,\omega}-B_{s,\omega}\). The [actual projection identity](timed-pinning-69.md#an-exact-signed-difference-for-arbitrary-time-weights) gives
\[
 D_s=\frac{s}{2}\sum_{j=a}^{a+d}(\omega_{j-1}-\omega_j)P_{-s}Y_j .
 \tag{1}
\]
The coefficients have sum zero. The weights are unimodal, so the sum of their absolute first differences is at most \(2C_0/d\). Subtract \(Y_a\) in (1) and apply the same nonexpansive time-shift bound as in round 70, \(\|Y_j-Y_a\|_{2,n}\le2\sqrt{j-a}\). This proves \(\|D_s\|_{2,n}\le C/\sqrt d\).

For the first norm, \(JY_j=0\), \(K Y_j=\sqrt n(\phi_{j-1}-\overline{\phi_{j-1}})\) for \(j\ge1\), \(\|Y_j\|_{1,n}\le2g_j\), and \(\|K Y_j\|_{1,n}\le4g_{j-1}\). Hence \(\|P_{-s}Y_j\|_{1,n}\le g_j+2g_{j-1}\). Since consecutive positive \(t_k\) have ratio in \([1/2,2]\) and \(|t_k-t_{k-1}|\le d\), the normalized consecutive weight differences obey
\[
   |\omega_{j-1}-\omega_j|
    \le C d^{-3/2}\min(\sqrt{\omega_j},\sqrt{\omega_{j-1}})
         \quad (a+1\le j\le a+d-1).
\]
Therefore the interior terms of (1) have \(L^1\) norm at most
\[
 C d^{-3/2}\left(\sum_{j=a+1}^{a+d-1}\sqrt{\omega_j}\,g_j+
                \sum_{j=a+1}^{a+d-1}\sqrt{\omega_{j-1}}\,g_{j-1}\right)
 \le C \sqrt{H_a}/d .
\]
At the two edges the coefficient magnitudes are \(w_*=d^2/Z_d=O(d^{-3})\). All four boundary mean terms appearing at these edges have weight \(w_*\) in the padded energy, so their contribution is \(O(\sqrt{w_*H_a})=O(d^{-3/2})\). Since the raw row and the pinned mean shift are nonnegative on the bulk, we have proved, on the very same windows and both signs,
\[
 \| (R_s)_-\|_{1,n}\le C_1/d,\qquad
 \| (R_s)_-\|_{2,n}\le C_2/\sqrt d .
 \tag{2}
\]
The root of \(R_s\) is positive, so including it in these norms contributes zero.

## A joint threshold for the remaining obstruction

Take any feasible opposite probability \(q\), and write \(\gamma=\sqrt n\,q_0\). Orthogonality and the exact mean and mark give
\(\sum_{i\ne0}q_iR_s(i)=m_s(1+\epsilon-\gamma)\).
For \(u,B>0\) define the joint tail
\[
 T_{s,u,B}(q)=\{i\ne0:R_s(i)<-u,\ nq_i>B\}.
\]
The contribution of the negative part on \(nq_i\le B\) is at most \(C_1 B/d\) by the first bound of (2). The contribution on \((R_s)_-\le u\) is at most \(u\) since \(q\) has mass one. Apply Cauchy--Schwarz to the remaining joint tail to get
\[
 m_s(\gamma-1-\epsilon)
   \le u+C_1B/d+
       C_2\,d^{-1/2}\left(n\sum_{i\in T_{s,u,B}(q)}q_i^2\right)^{1/2}.
 \tag{3}
\]
In particular, for a fixed \(\delta>0\), take \(u=\delta/8\) and \(B=\delta d/(8C_1)\). A true mark \(\gamma\ge1+\delta\) forces order-\(\delta^2d\) collision on that joint tail of every selected smooth window for every optimizer on that side. The density cutoff \(nq_i>B\) itself has at most \(n/B=O_\delta(n/d)\) sites. Low-density bulk never needs a translated squared cover in this test. Averaging over the selected windows preserves (3) and the squared lower bound, holding \(q\) fixed, or one can choose a single selected window for an upper certificate.

For example an upper \(o(d)\) on \(n\sum_{T_{s,u,B}(q)}q_i^2\) for some actual optimizer on each side, with \(B=o(d)\) and each fixed \(u>0\), would give the ordinary theta limit by (3) and reciprocity. One may also bound the actual magnitude-weighted sum on the joint tail instead of its collision. The inequalities (1)–(3) use the genuine nonlinear windows and apply through primes, but by themselves do not rule out concentration above the density cutoff.

The joint-tail test admits an equivalent vanishing target at this scale using a convex objective on the true face. Put \(S_{s,u}=\{i\ne0:R_s(i)<-u\}\) and
\[
 C_{s,u,B}(q)=\frac1n\sum_{i\in S_{s,u}}(nq_i-B)_+^2.
\]
The hard collision restricted to \(T_{s,u,2B}\) is at most \(4C_{s,u,B}\), and \(C_{s,u,B}\) is at most the hard collision on \(T_{s,u,B}\). Thus (3) with \(2B\) also gives
\[
 m_s(\gamma-1-\epsilon)
 \le u+2C_1B/d+2C_2 \sqrt{C_{s,u,B}(q)/d}.
\]
The squared positive part is convex and, on an inversion-even profile, averaging an optimizer and its reflection does not increase it. The latter conclusion need not hold for the hard cutoff. With an actual feasible \(v\) on the tested face, set \(\psi_i=\mathbf1_{S_{s,u}}(i)(nv_i-B)_+\). The value \(C(v)\) is an upper certificate, and the supporting tangent gives the lower certificate \(C(v)+2\min_{q\in \mathcal F}\sum_i\psi_i(q_i-v_i)\), where the minimum is over the same true face. This directly tests the high-density part without replacing the minimized quadratic by a worst-optimizer linear chord.

## Ranked tests

1. Minimize the convex squared positive-part objective on the actual primary face for each fixed deficit threshold and growing \(B=o(d)\). A uniform \(o(d)\) upper certificate at one selected profile on each side suffices. A feasible tangent lower bound of order \(d\) at every selected window along a prime subsequence would reject this sufficient test at the chosen thresholds.
2. Use the finite face parameterization to compare the direct quadratic minimum with a thresholded version of the signed cap bound. The two can be close or far according to the genuine intervals on the selected sites. Any extrapolation must control the high-density region for the actual marked time window through primes.
