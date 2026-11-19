# Relative defect moments on the actual paired cold windows

A smoother time taper bounds the negative defect relative to the opposite projected row at the *same coordinate*. For every fixed integer \(k\ge2\), the normalized \(k\)-th moment of the defect divided by the \((k-1)\)-st power of that positive opposite row is \(O_k(d^{-k})\). The estimate applies to true cold windows with growing length \(d=o(D(p))\), including the genuine mark and the mean allowance. It gives a more restrictive negative-set geometry when the opposite row has moderate height, and a weighted \(L^{k/(k-1)}\) test on the true primary face.

## Paired rows with a nonnegative bulk constant

Use the notation of [round 69](timed-pinning-69.md#an-exact-signed-difference-for-arbitrary-time-weights) and [round 72](smooth-windows-72.md#simultaneous-choice-of-smooth-windows). In particular \(Y_j=\sqrt n v_j\), \(g_j=\sqrt n\,\overline{\phi_j}/2\), and off the mark \(\sqrt n\phi_j=|Y_j|\). Here \(D=D(p)\) is the inherited marked horizon, \(d\to\infty\), \(d=o(D)\), and \(\eta=\sqrt{d/D}\). Fix \(k\ge2\) and an integer \(m\ge2k\), both independently of the field. On a window \([a,a+d-1]\) put
\[
 \omega_{a+j}=\frac{[(j+1)(d-j)]^m}{\sum_{\ell=0}^{d-1}[(\ell+1)(d-\ell)]^m}
                  \qquad(0\le j<d),
\]
and set the other weights to zero. Denote its common endpoint weight by \(w_*\), and use \(\pi_j=\omega_j\) in the window and \(\pi_{a-1}=\pi_{a+d}=w_*\) for the two extra sites.

The energy-window selection applies with this taper. Indeed \(\max\omega_j\le C_m/d\). The sum over starts of \(\sum_j \pi_j g_j^2/(1+2w_*)\) is bounded by \(\sum_{j=0}^{D+1}g_j^2\le D+2\), since the padded selection kernel is a probability. There are at least \(\eta D\) good starts with padded energy at most \(1+4\eta\) eventually, by the same count as in round 72. The counting bounds for raw overlap also apply, since each raw tapered positive row is pointwise at most \(C_m\) times the flat positive row. Discard the early and high-overlap starts with the same argument, using the new constant \(C_m\). The marked normalization \(m_s=Z_{s,\omega}(0)/\sqrt n\) is \(1+o(\eta)\) on the retained starts by the same uniform marked cancellation, and \(G_\omega=\sum_j\omega_j g_j\) satisfies \(G_\omega^2\le (1+2w_*)(1+4\eta)\). We only need these premises on the retained windows.

For \(s=\pm1\) and \(i\ne0\) put \(u_{s,j}(i)=(sY_j(i))_+\). Define two time coefficients
\[
 A_j=\tfrac14(2\omega_j+\omega_{j-1}+\omega_{j+1}),\qquad
 B_j=\tfrac14(\omega_{j-1}-\omega_{j+1})
\]
and let \(c_\omega=\frac12\sum_j(\omega_j-\omega_{j+1})g_j\). Then the **exact** two-row formula on the bulk is
\[
 Z_{s,\omega}(i)=c_\omega+\sum_j A_j u_{s,j}(i)
                      -\sum_j B_j u_{-s,j}(i).                  \tag{1}
\]
To verify it use \(P_{-s}=(I-J-sK)/2\), \(JY_j=0\) and \(KY_j=\sqrt n\phi_{j-1}-2g_{j-1}\) in the weighted projection identity. Collect terms using \(sY_j=u_{s,j}-u_{-s,j}\) and \(|Y_{j-1}|=u_{s,j-1}+u_{-s,j-1}\). The indices of \(KY_j\) there begin at \(j=a\ge1\), so the recurrence identity applies also at the edge. In particular \(A_j\ge |B_j|\). The coefficient \(c_\omega\) is the same for both signs.

Write \(\ell_j=\min(j-a+1,a+d-j)\) on the interior, and \(\ell_{a-1}=\ell_{a+d}=1\). On this extended support one has
\[
 \pi_j\asymp_m \ell_j^m/d^{m+1},\quad A_j\asymp_m\pi_j,\quad
 |B_j|+|\omega_j-\omega_{j+1}|\le C_m\pi_j/\ell_j .
                                                                    \tag{2}
\]
These bounds use the degree-two bump, the sum of its \(m\)-th powers \(\asymp_m d^{2m+1}\), and the bounded ratios of consecutive positive bump values. At the two extra sites, the nonzero neighboring weight is \(w_*\), so the same estimates hold with \(\ell_j=1\). By Cauchy–Schwarz and the padded energy bound,
\[
 |c_\omega|\le C_m\Big(\sum_j\pi_j/\ell_j^2\Big)^{1/2}
                       \Big(\sum_j\pi_j g_j^2\Big)^{1/2}
                \le C'_m/d.                                     \tag{3}
\]

Pin the rows as in round 72 using \(\epsilon=8(\eta+w_*)+C''_m/d\), with \(C''_m\) large enough. The original allowance \(8(\eta+w_*)\) already gives nonnegative mean addition on both signs. The extra allowance dominates the constant in (3) since \(m_s\) and the canonical bulk mean directions \(b_s(i)\) are bounded below by \(1/2\) eventually. Thus the actual pinned rows satisfy
\[
 R_s(i)=U_s(i)-F_s(i)+c_s(i),\quad
 U_s=\sum_j A_j u_{s,j},\quad F_s=\sum_j B_j u_{-s,j},\quad
 c_s(i)\ge0
 \qquad(i\ne0).                                                  \tag{4}
\]
They retain the true sector, the mark \(m_s\sqrt n\) and the mean \((1+\epsilon)m_s\). In particular \(R_s(i)+R_{-s}(i)\ge0\) on the bulk since \(F_s\le U_{-s}\). Their negative sets are disjoint for this common allowance.

## The relative defect estimate

Let \(r_s(i)=(R_s(i))_-\). If this is positive, set \(V=U_{-s}(i)\), \(f=F_s(i)\), and \(U=U_s(i)\). By (4), \(0<r_s\le f-U\), \(f\le V\), and \(R_{-s}(i)\ge V-U\ge V-f+r_s\ge r_s\). Define the nonnegative field
\[
 H_{s,k}(i)=\sum_j\frac{|B_j|^k}{A_j^{k-1}}\,u_{-s,j}(i)
\]
on the bulk, with zero summands if \(A_j=0\). Hölder gives \(f^k/V^{k-1}\le H_{s,k}(i)\) whenever \(f>0\); this follows by first bounding \(f\le\sum |B_j|u_{-s,j}\) and weighting by the positive numbers \(A_j u_{-s,j}\).

\(V\ge f>U\) at such a site. Hence \(r_s/R_{-s}\le(f-U)/(V-U)\le f/V\). Combining this with \(r_s\le f\) gives, with the ratio defined as zero on \(r_s=0\),
\[
 \frac{r_s(i)^k}{R_{-s}(i)^{k-1}}\le H_{s,k}(i).                \tag{5}
\]
There is no division by a nonpositive value on the support of \(r_s\).

By (2), the coefficient \(\theta_j=|B_j|^k/A_j^{k-1}\) satisfies \(\theta_j\le C_{m,k}\pi_j/\ell_j^k\). In particular
\[
 \sum_j\frac{\theta_j^2}{\pi_j}
 \le C_{m,k}d^{-(m+1)}\sum_{\ell=1}^d\ell^{m-2k}
 \le C'_{m,k}d^{-2k}.
\]
Since \(n^{-1}\sum_{i\ne0}u_{-s,j}(i)\le2g_j\), Cauchy–Schwarz with the padded energy gives \(n^{-1}\sum_{i\ne0}H_{s,k}(i)\le C_{m,k}d^{-k}\). It follows that on every such selected window, on both signs,
\[
 \frac1n\sum_{i\ne0}\frac{r_s(i)^k}{R_{-s}(i)^{k-1}}
       \le \frac{C_{m,k}}{d^k}.                                  \tag{6}
\]
The same coefficient estimate with exponent one and \(r_s\le \sum_j |B_j|u_{-s,j}\) gives the ordinary negative \(L^1\) bound \(C_m/d\), with the same weights and allowance.
The unweighted negative \(L^2\) bound \(O_m(d^{-1/2})\) also holds with this taper. Apply the projection identity to \(Y_j-Y_a\), use the time-shift bound \(2\sqrt{j-a}\) in normalized norm, and use total coefficient variation \(2\max_j\omega_j=O_m(1/d)\).

## A simultaneous mask and height test

Let \(S=\{i\ne0:R_s(i)<-u\}\) for a fixed \(u>0\). For any \(H>0\) the low-height part of this **actual** mask obeys
\[
 \frac{|\{i\in S:R_{-s}(i)\le H\}|}{n}
     \le \frac{C_{m,k}H^{k-1}}{u^k d^k}.                        \tag{7}
\]
In particular a fixed height cap gives density \(O(d^{-k})\) for any fixed \(k\), using the corresponding taper. The very high opposite rows are uncontrolled by this count.

For any true feasible \(q\) in the sector \(-s\), write \(x_i=(q_i-B/n)_+\), \(\gamma=\sqrt n\,q_0\), and \(\rho=k/(k-1)\). Orthogonality, the mark and the mean give the signed identity \(\sum_{i\ne0}q_iR_s(i)=m_s(1+\epsilon-\gamma)\). Pay at most \(u\) on \(r_s\le u\), and at most \(C_m B/d\) on the low-density remainder within \(S\). Hölder with (6) on the rest gives
\[
 m_s(\gamma-1-\epsilon)
 \le u+\frac{C_m B}{d}
      +\frac{C_{m,k}}d
        \left(\frac1n\sum_{i\in S}(n x_i)^\rho R_{-s}(i)\right)^{1/\rho}.
                                                                    \tag{8}
\]
For fixed \(\delta>0\), whenever \(\gamma\ge1+\delta\), \(u=\delta/8\), and \(B=o(d)\), the last weighted moment is \(\gg_{\delta,m,k} d^\rho\) on each of the same selected windows. Its weights are positive on \(S\), so it is a convex objective on the true primary face. An \(o(d^\rho)\) upper for one appropriate window and one genuine larger-face representative would rule out the fixed gap. A proof needs to handle the high opposite heights along with the large \(q_i\); (7) is a counting estimate for their complement.

For \(k=2\), if \(R_{-s}\le H=o(d)\) on the clipped negative support, the original masked collision must be at least a constant times \(d^2/H\). This is stronger than an order-\(d\) lower bound in that regime. Without such a cap, both the round-72 unweighted test and (8) are available. The relative estimate and marked window proof do not isolate prime-only arithmetic from the square controls, and do not settle either limiting question.

## A geometric taper giving an exponentially small low-height mask

There is a separate pointwise version for a different taper. Let \(0<\tau\le1/2\), \(\tau\to0\), and \(\tau d\to\infty\). Use \(\omega_{a+j}\) proportional to \(\exp[-\tau|j-(d-1)/2|]\), and set \(w_*=\omega_a=\omega_{a+d-1}\). The padded energy count, the mark bound, and the removal of early starts apply as before. If also keeping the raw-overlap condition, for any common taper the sum of raw overlaps over all starts is at most
\(\sum_{\ell\ge1}\ell\sum_j\omega_j\omega_{j+\ell}\le d/2\), by the round-70 lag budget. Thus the same \(O(\eta)\) overlap selection is available without bounding the peak of the geometric taper by \(O(1/d)\). Mark and mean are imposed by pinning with allowance \(8(\eta+w_*)+C(\tau+\sqrt{w_*})\). Away from the two endpoint jumps \(|\omega_j-\omega_{j+1}|\le C\tau\omega_j\), so the absolute constant in (1) is \(O(\tau+\sqrt{w_*})\) by the padded energy bound. As in (4), the added pin makes \(c_s(i)\ge0\).

Write \(J_{\mathrm{edge}}=\{a-1,a,a+d-1,a+d\}\), \(\theta=\tanh\tau\), and
\[
 E_s(i)=\sum_{j\in J_{\mathrm{edge}}}|B_j|u_{-s,j}(i).
\]
At each interior time \(j\notin J_{\mathrm{edge}}\), the two neighboring weights have ratio between \(e^{-2\tau}\) and \(e^{2\tau}\), so \(|B_j|\le\theta A_j\). On the edge \(|B_j|\le C w_*\) because the nearest nonzero adjacent weights have ratio at most \(e^\tau\). It follows that
\[
 F_s(i)\le\theta U_{-s}(i)+E_s(i),\qquad
 \frac1n\sum_{i\ne0}E_s(i)\le C\sqrt{w_*}.
\]
The second estimate uses the padded energy at the four edge times, each of weight at least \(w_*\). If \(r=r_s(i)>0\), \(V=U_{-s}(i)\), and \(f=F_s(i)\), then \(r\le f\) and
\[
 R_{-s}(i)\ge V-f+r\ge(1-\theta)V-E_s(i)+r.
\]
Eliminating \(V\) from \(r\le\theta V+E_s(i)\) yields the pointwise comparison
\[
                 r_s(i)\ \le\ \theta R_{-s}(i)+E_s(i)
                 \qquad(r_s(i)>0).                              \tag{9}
\]
In particular for \(H\theta\le u/2\) a site with \(R_s<-u\) and \(R_{-s}\le H\) must have \(E_s>u/2\). The central weight shows \(w_*\le\exp[-\tau(d-2)/2]\), since the distance between an endpoint and a closest central time is at least \((d-2)/2\). Thus
\[
 \frac{|\{i\ne0:R_s(i)<-u,\ R_{-s}(i)\le H\}|}{n}
          \le (C/u)\exp[-\tau(d-2)/4].                            \tag{10}
\]
For example \(\tau=d^{-\beta}\), \(0<\beta<1\), gives an exponentially small counting fraction in \(d^{1-\beta}\) at \(H\le u d^\beta/2\). The mean allowance still tends to zero. The assertion concerns counting measure, including all physical frequencies except the mark. It alone does not exclude a large value of \(q\) on a sparse set.

The exact orthogonality test with (9) gives
\[
 m_s(\gamma-1-\epsilon)\le u+C B(\tau+\sqrt{w_*})
    +\theta\sum_{i\in S}x_i R_{-s}(i)+\sum_{i\in S}x_i E_s(i).    \tag{11}
\]
Here the ordinary \(L^1\) bound \(C(\tau+\sqrt{w_*})\) follows from \(r_s\le \sum |B_j|u_{-s,j}\), interior \(|B_j|\le C\tau\omega_j\), and the edge estimate. Thus if a true row is supercritical and \(u=\delta/8\), \(B(\tau+\sqrt{w_*})=o(1)\), it must pay a fixed amount by the two weighted sums in (11). For \(d\) comparable to a fixed positive power of \(D\) strictly below one and \(\tau=d^{-\beta}\), the last sum is \(o(1)\) whenever the unweighted clipped collision on \(S\) is at most a fixed power of \(D\). In fact \(\|E_s\|_{2,n}\le Cw_*\sqrt D\) by the true energy on the four edge times, and Cauchy–Schwarz prices this sum by \(\|E_s\|_{2,n}\sqrt{n\sum_{S}x_i^2}\). The needed collision control for actual optimizers is open. This version leaves a linear weighted height test if the edge price can be certified.

## Ranked next tests

1. On the true negative supports bound the overlap between high opposite height \(R_{-s}\) and superthreshold primary density \(nq_i\). Keep the low-height density savings (7) or (10) and use signed Schur or actual-row visibility on the high-height intersection. Measure the true edge term in (11) before using its linear height test.
2. For \(k=2\), directly optimize the positive-weighted convex collision in (8) over the true primary face. Compare it to the unweighted collision on the same selected windows and record which sites carry a possible order-\(d^2\) cost.
