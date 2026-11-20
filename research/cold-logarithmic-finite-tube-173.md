# A finite-tube criterion for convergence after the true height 602

Keep the physical \(t_0=n=(p-1)/2\), the original closed complex square, the actual \(K\Phi_t\) and both lifts. This criterion concerns the actual moving Picard rows. It gives a sufficient finite confinement test for holomorphy on the original square's interior and does not assert that the growing finite test passes.

## A uniform disk for the exact fixed-height row

By [Rounds 126 and 162](cold-height-602-frozen-kernel-162.md), the genuine height \(602\) row has \(\sup|V_{602,i}|<4.791\) and \(\sup_i|\Phi'_{t,i}(V_{602,i})|<0.518\) eventually. Let \(d=0.025\) and center a coordinate disk of radius \(d\) at each exact \(V_{602,i}(t)\). Put \(t_c=2031/128\), \(N=4(t_c-2^{-17})\). Off the physical mark, all points of the disks have \(|z|\le4.816\) and the real part of \(4t+z^2\) is at least \(N-4.816^2>0\). The scalar curvature formula and the rational comparison
\[
 16\bigl[4(t_c+2^{-16})\bigr]^2<(N-4.816^2)^3
\]
give \(|\Phi''_{t,i}(z)|<1/4\). At the mark the curvature is \(O(n^{-1/2})<1/4\) eventually because the radicand is \(4n+z^2\). The sheets are analytic on the coordinate disks. It follows that the scalar derivative is uniformly less than \(0.518+0.025/4<q=0.525\) throughout. By integrating along the coordinate segments and using \(\|K\|_{2\to2}\le1\), the true map is \(q\)-Lipschitz in counting or normalized second norm whenever both endpoints are in this polydisk.

## Finish the tail once one finite prefix is known

Put \(k_n=\lceil(4/7)\log_2 n\rceil\), and \(m_n=602+k_n\). Suppose the actual Picard rows \(V_{602},\ldots,V_{m_n}\) stay in the coordinate disks uniformly on the original square and both lifts, and the last one has distance at least a fixed \(\eta>0\) from their boundaries in coordinate supremum norm. The initial increment \(R_{602}=V_{603}-V_{602}\) has normalized second norm \(O(1)\) by the fixed actual neighboring secant of Round 126. Along the tested prefix, including the increment out of the last point, the contraction therefore gives
\[
 \|R_{m_n}\|_{2,n}\le q^{k_n}\|R_{602}\|_{2,n}.
\]
Here \(R_{m_n}=K\Phi_t(V_{m_n})-V_{m_n}\) is evaluable inside the disks and does not require analyticity of a future iterate's radicand yet. The exact rational \(q^8<2^{-7}\) makes \(\sqrt n\,q^{k_n}=o(1)\).

From \(V_{m_n}\), a tentative first exit would have coordinate displacement at most
\[
 \frac{\sqrt n\,\|R_{m_n}\|_{2,n}}{1-q}=o(1)
\]
by summing contracted increments until that exit and using the finite-dimensional norm conversion. The bound is smaller than \(\eta\) for sufficiently large \(n\), which excludes the exit. The remaining actual orbit converges uniformly on the original square to a stationary holomorphic row on its interior. This last assertion uses uniform convergence of analytic iterates on every compact subset of the interior; the positive radicand margin and the known analytic starting row justify the sheets throughout.

Thus a proof of the single finite-prefix confinement test would suffice for this common continuation without a moving-height translated or shifted-resolvent estimate. This does not verify the prefix, and it does not establish derivative transfer estimates that require a translated inverse. The existing fixed-height source upper bounds alone do not show the required prefix. The raw secant constant \(0.51358+0.248(0.011+0.012/2)\) is \(0.517796\). The actual secant comparison is a fixed-height input and does not control an entire moving tube.
