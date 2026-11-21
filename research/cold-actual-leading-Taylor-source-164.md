# The first genuine quadratic Taylor coefficient and the isolated marked source

Use the original cold square, both lifts, \(R=V_{601}-V_{600}\), and the true remainder \(r\) from [Round 162](cold-height-602-frozen-kernel-162.md). Write \(D=D_{602}\), \(B=KD\) and \(Z=(I-B)^{-1}K\). All assertions below are at the verified fixed heights.

For the actual coordinate sheets, the leading Taylor coefficient is
\[
 r^{(0)}_i=\frac{R_i^2}{2\sqrt{4t_i}},\qquad t_0=n,\quad t_i=t\ (i\ne0).
\]
The factor one half is the integral of \(1-s\). Let \(N=4(2031/128-2^{-17})\) and \(\varepsilon=0.011\), the true price bound for \(R\). Two negative factors have convolution generic rank at most twice the product dimension by the [boundary word estimate](cold-actual-first-insertion-126.md). The twist \(K\) kills the unit and prices the remaining negative word by at most twice its rank. Hence
\[
 \|K r^{(0)}\|_{P_{5000}}\le 2\varepsilon^2/\sqrt N+O(n^{-1/2})<0.000031
\]
eventually. This includes both lifts, the bad base characters and correction from bulk \(t\) to actual \(t_0\), since a bounded change at zero has price \(O(n^{-1/2})\) after \(K\). The strict scalar inequality follows by a rational square comparison. The earlier \(0.000115\) bound concerns the whole analytic remainder.

Also let \(r^{\mathrm b}\) be the whole Taylor remainder using the bulk scalar formula at every site, evaluated on the same actual pair of rows. Then \(r-r^{\mathrm b}=\delta e_0\), with \(|\delta|=O(\varepsilon^2)\), whereas \(|r_0|=O(n^{-1/2}|R_0|^2)\) for the true marked radicand. Consequently the physical atom costs
\[
 \sum_{j\ge0}\|B^jK(r-r^{\mathrm b})\|_\infty
     =O(\varepsilon^2 n^{-0.455})
\]
by the established max-entry sum. This costs only the marked-column kernel and has no ambient normalization factor. For the different transport \(ZK(r-r^{\mathrm b})\), retain its direct atom \(\delta(e_0-\mathbf1/n)\). Its remaining part
\(\delta ZD(e_0-\mathbf1/n)\) is \(O(\varepsilon^2 n^{-0.455})\) in supremum norm, by applying the max-entry bound to one marked column and to the constant correction of counting first norm one. The direct atom has no such claimed decay. These bounds do not control the full bulk frozen translated response or an actual nonlinear confinement.
