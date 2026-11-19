# True high-height masks at a fixed fraction of the marked depth

The infinite geometric windows can run at effective length \(d\asymp_\delta D(p)\) when testing a fixed supercritical gap \(\delta>0\). The constant fraction may depend on the gap. This uses the weighted energy budget of the future marks and pays only the negative part of the geometric projection defect when deleting expensive sites. It strengthens the \(D/\log D\) prescribed-start test and permits a family of order-\(D\) starts.

Use the notation of [round 78](astra-height-78.md) with \(0<\delta\le1\) and \(J=\lfloor D(p)/8\rfloor\). There is a constant \(c_\delta>0\) such that the following holds for \(d\to\infty,\ d\le c_\delta J\), all integer starts \(1\le a\le\max(1,\lfloor\delta d/100\rfloor)\), and all sufficiently large eligible primes. Use \(h=1/(d+1)\), \(b=1-h\), weights \(\omega_{a+j}=hb^j\), and pin both rows with allowance \(\epsilon=\delta/8\). For any true complementary probability \(q\) in sector \(-s\) with \(\sqrt n q_0\ge1+\delta\), any \(B=o(d)\), \(B\ge0\), and any common deletion \(A\) of size at most \(c\sqrt n\) for a sufficiently small absolute \(c\), write
\[
 M_E=\sum_{i\notin A}(q_i-B/n)_+,\qquad
 N=d\exp[J/(8(d+1))].
\]
There are constants \(k_\delta>0,C_0>0\), the latter absolute, for which
\[
 I=\{i\ne0:R_s(i)<-\delta/8,\ R_{-s}(i)>(2d+1)\delta/8,\
                      k_\delta d<nq_i\le2C_0\sqrt n M_E\}
\]
satisfies, for every \(L\) of size at most \(N/M_E^2\),
\[
 \sum_{I\setminus L}q_i(R_s(i))_-\gg_\delta 1,\qquad
 \sum_{I\setminus L}q_iR_{-s}(i)\gg_\delta d,\qquad
 n\sum_{I\setminus L}q_i^2\gg_\delta d.                         \tag{1}
\]
When \(d=\lfloor c_\delta J\rfloor\), the scale in the last two inequalities is \(D(p)\). The number of starts is \(\asymp_\delta D(p)\). This is a necessary condition on actual probabilities at a fixed gap, including optimizers on the actual larger side.

## The future marks have a weighted energy bound

For any \(m\ge0\), the time weights \(hb^j\) give
\[
 h\sum_{j\ge0}b^j g_{m+j}^2\le1+hE_m/4\le1+hm,
 \qquad E_m=\|v_m\|_2^2 .                                      \tag{2}
\]
Indeed \(4(g_t^2-1)=E_t-E_{t+1}\), the decreasing weight differences at all times after \(m\) have nonpositive sign, and the boundary at infinity vanishes since \(E_t\le4t\). Thus \(G=\sum\omega_jg_j\le\sqrt{1+ha}\).

The signed projected marks can be bounded through time, even after the arithmetic window. For \(j\ge1\), write the exact formula for \(Z_{s,j}=(J_{\mathrm{const}}+P_s)B_{s,j}\), where \(J_{\mathrm{const}}\) denotes the constant projector. At the root it gives
\[
 4m_{s,j}=\phi_j(0)+\phi_{j-1}(0)+s v_{j+1}(0)+s v_j(0)
                       +\overline{\phi_j}-\overline{\phi_{j-1}},
 \qquad m_{s,j}=Z_{s,j}(0)/\sqrt n .
\]
This is the identity \(Kv_j=\phi_{j-1}-\overline{\phi_{j-1}}\mathbf1\). Since \(\max_i|K_{0i}|\le\sqrt p/n\) and \(\phi_{j-1}\ge0\), \(|v_j(0)|\le 2\sqrt{p/n}\,g_{j-1}\) for \(j\ge1\). Also \(\phi_j(0)\le2+|v_j(0)|\). Hence for \(j\ge2\),
\[
                   |m_{s,j}-1|\le C(g_{j-2}+g_{j-1}+g_j).
\]
On the marked times \(1,\ldots,D\), use instead the inherited estimate \(m_{s,j}=1+o(1)\) uniformly. In the future, the weighted mean of each displayed \(g\) is at most its weighted second norm conditional on \(j>D\). By (2) this bounds the full average mark error by
\[
              |m_s-1|\le o(1)+C b^{D+1-a}\sqrt{1+h(D+1)} .       \tag{3}
\]
The geometric rate may be made arbitrarily small uniformly by \(d\le c_\delta J\), since \(h(D+1-a)\ge 8/c_\delta-O(1)\) asymptotically at the largest \(d\), and \(ha\) stays bounded. Choose \(c_\delta\) so that \(|m_s-1|\le\delta/100\) eventually for both signs. Now \(G\le1+\delta/100\) eventually by (2), so \((1+\epsilon)m_s-G\) is bounded below by a fixed positive multiple of \(\delta\). The constant \(c_\omega=h(G-g_{a-1})/2\) has absolute value \(O(\sqrt h)\), since \(g_{a-1}^2\le a\). The pin direction has bulk entries at least \(1/2\), so its increment absorbs \(c_\omega\).

The [pointwise paired inequality](astra-height-78.md#the-geometric-coefficients) therefore applies with no endpoint error. On the bulk \(R_s+\theta R_{-s}\ge0\), with \(\theta=(2d+1)^{-1}\). Write \(r_s=(R_s)_-\) on the bulk and zero at the root. The first-difference bounds from the same proof give \(\|r_s\|_{1,n}\le C/d,\ \|r_s\|_{2,n}\le C/\sqrt d\) with absolute \(C\). They also give the pointwise *upper* envelope
\[
                       r_s(i)\le C h\sum_{j\ge a}\omega_j(-sY_j(i))_+.     \tag{4}
\]
Here the left boundary terms in the formula for \(R_s\) have \(B_j\le0\), and later \((B_j)_+\le C h\omega_j\).

## Keeping only the future defect in the deletion cost

By the exact complementary pairing, \(\sum_i q_i r_s(i)\ge m_s(\sqrt n q_0-1-\epsilon)\). Discarding \(r_s\le\delta/8\) costs at most \(\delta/8\), and discarding \(nq_i\le k_\delta d\) costs at most \(\delta/8\) by the first norm bound. The [retained-diagonal Schur cap](astra-schur-77.md#a-cap-set-by-the-exterior-clipped-mass) gives \(n\sum_i(q_i-C_0M_E/\sqrt n)_+^2\le C B\). Therefore discarding \(nq_i>2C_0\sqrt n M_E\) costs \(O(\sqrt{B/d})\). Together with the pointwise height condition these leave \(\sum_{I}q_ir_s(i)\ge\delta/2\) eventually.

Now take \(|L|\le N/M_E^2\). As in [round 78](astra-height-78.md#removing-the-largest-individual-prices), the much larger exterior scale forced by [round 77](trimmed-mellin-77.md) implies \(n^{1/4}M_E/\sqrt N\to\infty\), since \(\log_2^*N\le\log_2^*D+O(1)\) and \(B=o(D)\). In detail, a bounded subsequence of this ratio would contradict \(\log_2^*\max(2,n^{1/4}M_E)\ge\log_2^*p-O_\delta(1+B)\). Thus \(|L|\le\sqrt n\) eventually. The same Schur cap and Cauchy--Schwarz yield
\[
 n\sum_{i\in L}q_i^2\le C(B+N),\qquad
                \sum_{i\in L}q_i\le C n^{-1/4}\sqrt{B+N}.
\]
Use the true Mellin approximants through time \(J\), with tolerance \((N+D)^{-4}\) as in round 78. They have coordinate bound \(p^{1/8}\) and normalized second error \(O(J[(N+D)^{-4}+p^{-3/8}])=o((B+N)^{-1/2})\). The portion of (4) through \(J\), paired against \(q\mathbf1_L\), is \(o(1)\) by these two estimates and \(N\le D e^{O(D)}\).

For \(j>J\) keep the actual upper envelope in (4), which includes the extra factor \(h\). Its normalized second norm is at most \(C h b^{J+1-a}\sqrt{J+d+2}\), by \(\|Y_j\|_{2,n}\le2\sqrt j\) and geometric Jensen. The remaining price on \(L\) is consequently bounded by
\[
 C h\sqrt{B+N}\, b^{J+1-a}\sqrt{J+d+2}
 \le C\sqrt{1+J/(d+1)}\exp[-15J/(16(d+1))].
\]
The constant absorbs the bounded factor \(\exp(ha)\). Decrease \(c_\delta\) so that this bound is less than \(\delta/8\) throughout \(d\le c_\delta J\) eventually. The deleted price is at most \(\delta/8+o(1)\). Subtract it to prove the first inequality in (1), then apply the paired height inequality and the normalized second bound to prove the other two. All \(L\) are allowed, including lists selected from the actual prices. The argument bounds the deleted price using a nonnegative envelope, which avoids approximating the full projected profile at the far end.

## A linear test on a genuine primary face

Fix a window, \(A\), a scalar exterior budget \(M>0\), and a deletion \(L\) with \(|L|\le N/M^2\). On either true primary face, impose \(M_E\le M\) by variables \(x_i\ge0,\ x_i\ge q_i-B/n\) for \(i\notin A\) and \(\sum_{i\notin A}x_i\le M\). Define the fixed cost array
\[
      f_i=R_{-s}(i)\mathbf1_{\{i\ne0,\ r_s(i)>\delta/8,\ i\notin L\}}.
\]
The paired bound gives \(f_i\ge0\). Minimize \(\sum_i f_i q_i\) with the genuine primary mark and sector equations, nonnegativity, normalization and the exterior budget. This is an LP with a fixed mask. Every feasible point at a supercritical mark is charged \(\gg_\delta D(p)\) for \(d=\lfloor c_\delta J\rfloor\) by (1). An \(o(D(p))\) attainable upper bound on such an LP through primes, at one choice of window and parameters per larger-side face, would exclude this gap. The q-dependent band need not appear in the LP.

## Ranked next tests

1. Compare the minimized fixed-mask price with a certified genuine-row price on the narrower density band. Use the exterior budget jointly with the actual optimal-face equations and test a growing \(d\) rather than holding it fixed.
2. Seek a prime-specific bound for the price on the surviving intersection across the common windows of linear depth. A repeated loss in a bounded-expression approximation can be charged to (4), so the remaining arithmetic issue is the signed interaction of the true probability with this set.
