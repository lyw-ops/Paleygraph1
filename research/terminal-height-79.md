# A finite paired window with one actual terminal row

The finite pairing in [round 79](astra-excess-79.md) extends to an arbitrary companion profile. Concentrating the companion weight at a single time gives a pointwise height requirement on one actual, unpinned projected terminal row. On a fixed fraction of the marked depth, one can discard a number of sites set by a growing iterated-exponential threshold, using only the finite true trajectory.

## Exact finite pairing

Let \(a,b\) be positive integer times, \(a\le b\), and let \(\nu\) be a probability on the interval. Define, on the same interval,
\[
 \theta=\frac1{1+2\sum_{j=a}^b(j-a)\nu_j},\qquad
 \omega_j=\theta\left(\nu_j+2\sum_{k>j}\nu_k\right).
\]
Both profiles are zero off the interval. Then \(\omega\) is a probability, decreasing inside the interval, and \(\omega\ge\theta\nu\). For any profile \(w\) write
\[
 A^w_j=(2w_j+w_{j-1}+w_{j+1})/4,\qquad
 B^w_j=(w_{j-1}-w_{j+1})/4.
\]
The bulk coefficients of the paired sum of projected rows satisfy
\[
 A^\omega_j-\theta B^\nu_j\ge0,\qquad
 \theta A^\nu_j-B^\omega_j=\frac{\theta}{2}
                      (\mathbf1_{j=a-1}+\mathbf1_{j=a}).       \tag{1}
\]
For the first inequality, \(A^\omega\ge\theta A^\nu\) and \(A^\nu-B^\nu=(\nu_j+\nu_{j+1})/2\ge0\). For the second, on all integer times, \(\theta(\nu_{j-1}+\nu_j)-(\omega_{j-1}-\omega_j)=2\theta\mathbf1_{j=a}\). Sum this identity at \(j,j+1\) and divide by four. The early jump has the helpful sign.

In particular, for \(\nu=\mathbf1_{j=b}\), put \(d=b-a+1\). Then \(\theta=(2d-1)^{-1}\), \(\omega_j=2\theta\) for \(a\le j<b\), and \(\omega_b=\theta\). The companion projection is just \(Z_{-s,b}\). For the primary window let \(R_s^\omega\) be the exact pinned row of [round 69](timed-pinning-69.md#exact-allowance-and-a-sparse-dual-test), with allowance fixed below. The companion needs no pin.

## Good terminal times through the proved arithmetic window

Fix \(0<\delta\le1\), set \(J=\lfloor D(p)/8\rfloor\), and take \(1\le a\le\max(1,\lfloor\delta J/400\rfloor)\). Use any \(b\in[\lceil J/2\rceil,J-2]\) with \(\max(g_{b-1},g_b,g_{b+1})\le4\). There are at least \(J/4\) such times eventually: \(\sum_{j=0}^{J}g_j^2\le J+1\), so failures charge at most \(3(J+1)/16\) terminal times. In particular \(d\asymp D(p)\).

The decreasing-weight telescope gives \((G^\omega)^2\le1+\omega_a E_a/4\le1+2\theta a\), using \(E_a\le4a\). The inherited marked estimate gives \(m_s^\omega=Z^\omega_s(0)/\sqrt n=1+o(1)\) for both signs. Pin \(R_s^\omega\) with allowance \(\epsilon=\delta/8\). The increment \((1+\epsilon)m_s^\omega-G^\omega\) is bounded below by a fixed positive multiple of \(\delta\). In the exact bulk formula the unpinned constant \(c_\omega=\tfrac12\sum_j(\omega_j-\omega_{j+1})g_j\) is bounded below by \(-\omega_a g_{a-1}/2\ge-Cd^{-1/2}\). For the terminal profile \(c_\nu=(g_b-g_{b-1})/2\) has modulus at most \(2\), so the positive pin also absorbs \(\theta c_\nu\). The bulk pin direction is at least \(1/2\) for large fields. Thus (1) gives
\[
                     R_s^\omega(i)+\theta Z_{-s,b}(i)\ge0\qquad(i\ne0).
                                                                    \tag{2}
\]
This holds pointwise, including zero sites of the actual primary row.

For the negative defect \(r_s=(R_s^\omega)_-\) on the bulk, put \(r_s(0)=0\). Nonnegativity of the pinned constant and (1) give the finite envelope
\[
        r_s(i)\le \theta\sum_{j=b-1}^{b+1} A^\nu_j(-sY_j(i))_+ .
                                                                    \tag{3}
\]
Each bulk normalized first norm of \((-sY_j)_+\) is at most \(2g_j\); the normalized second norm is at most \(2\sqrt j\). Consequently \(\|r_s\|_{1,n}\ll d^{-1}\) and \(\|r_s\|_{2,n}\ll d^{-1/2}\), uniformly over the selected terminal times.

## A tower-scale deletion on the terminal height

Let \(q\) be any genuine probability in the opposite sector, with \(\sqrt n q_0\ge1+\delta\). Let \(B=o(d)\), \(B\ge0\), \(A\) have at most \(c\sqrt n\) sites for a sufficiently small absolute \(c\), and \(M_E=\sum_{i\notin A}(q_i-B/n)_+\). For \(u=\delta/8\), define
\[
 I=\{i\ne0:r_s(i)>u,\quad Z_{-s,b}(i)>(2d-1)u,\quad
                         k_\delta d<nq_i\le2C_0\sqrt n M_E\},
\]
with small \(k_\delta>0\) and the absolute \(C_0\) of the Schur cap. The exact opposite-sector pairing requires \(\sum_i q_i r_s(i)\ge m_s^\omega(\sqrt n q_0-1-\epsilon)\). The \(r_s\le u\) terms and \(nq_i\le k_\delta d\) terms cost at most \(\delta/8\) each, and the \(nq_i>2C_0\sqrt n M_E\) terms cost \(O(\sqrt{B/d})\) by the [Schur cap](astra-schur-77.md#a-cap-set-by-the-exterior-clipped-mass) and the second norm bound. Equation (2) proves the height condition on every remaining site. Thus \(\sum_I q_i r_s(i)\gg_\delta1\).

Write \(\Lambda=\log_2^*p\). Fix \(0<\xi<7/8\) and allow any \(H\ge2\) with \(\log_2^*H\le(7/8-\xi)\Lambda\). For every deletion \(L\) of size at most \(H^2/M_E^2\), uniformly in all the above choices,
\[
       \sum_{I\setminus L}q_i r_s(i)\gg_\delta1,\qquad
       \sum_{I\setminus L}q_i Z_{-s,b}(i)\gg_\delta d,\qquad
                      n\sum_{I\setminus L}q_i^2\gg_\delta d .             \tag{4}
\]
To prove this, [round 77](trimmed-mellin-77.md) gives \(n^{1/4}M_E/H\to\infty\): a bounded subsequence of the ratio would force \(\log_2^*\max(2,n^{1/4}M_E)\le(7/8-\xi)\Lambda+O(1)\) despite the uniform lower bound \(\Lambda-O_\delta(1+B)=\Lambda-o(\Lambda)\). Hence \(|L|\le\sqrt n\) eventually. The Schur cap and Cauchy--Schwarz give
\[
 \sqrt n\|q\mathbf1_L\|_2\ll H+\sqrt B,\qquad
                \|q\mathbf1_L\|_1\ll n^{-1/4}(H+\sqrt B).
\]
Apply the actual Mellin tower construction through \(J\) with per-step error \((H+D)^{-4}\). The initial tower height is at most \(\max(\log_2^*H,\log_2^*D)+O(1)\); adding \(J+2\le\Lambda/8+O(1)\) leaves a gap at least \(\xi\Lambda-O(1)\) below \(\Lambda\). Thus the approximants have sup norm at most \(p^{1/8}\) and normalized second error \(o((H+\sqrt D)^{-1})\), including all three terms in (3). Also \(H\le\log_2\log_2 p\) eventually. Pair (3) with \(q\mathbf1_L\), bounding the approximants by their sup norm and the error by the counting norm of \(q\mathbf1_L\). The result is \(o(1)\) with no future-tail expense. This proves the first assertion in (4), and (2) and the second norm of \(r_s\) give the other two.

## A fixed linear objective at each terminal time

In the [linear test](full-depth-height-79.md#a-linear-test-on-a-genuine-primary-face), replace \(R_{-s}\) in the objective by \(Z_{-s,b}\) and use the negative mask of \(R_s^\omega\). For an exterior cap \(M\) fixed before the optimization, allow any fixed \(L\) of size \(|L|\le H^2/M^2\). The objective charges every supercritical feasible row at least a positive constant times \(d\) and is linear in \(q\) on the full true face with the linear lift of the exterior cap. The active density band in the proof can vary with \(q\). An attainable \(o(d)\) upper in one such LP per larger true face would exclude a fixed gap uniformly. This reduction leaves open the prime-specific height upper bound.

1. Use a fixed later projection rather than a second time average and estimate its true price after discarding the prescribed large sites. Compare spread across the \(J/4\) admissible terminal times for one actual primary optimizer.
2. Focus on the nonconstant Fourier contributions to the surviving price. The finite envelope and large deletion budget account for isolated sites but alone give no cancellation on the retained mask.
