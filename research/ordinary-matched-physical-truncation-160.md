# Stable physical truncation for the actual matched anchor moment

Use the true weighted phase arc and selected ordinary-prime short block of [Round 157](ordinary-marked-frequency-localization-157.md). On the physical square input \(x\in Q\) put \(F(x)=f(1-vx)\), zero if \(1-vx\notin Q\). The following estimate holds for any two rows \(G,H\) supported on \(\{x\in Q:1-vx\in Q\}\). They can be selected from the actual orbit before choosing the anchor. Define
\[
 C_{G,H;a}(u)=\sum_{x\in Q}G(ux)\overline{H(x)}\,
                     \overline{a((1-vux)/(1-vx))},\qquad u\in Q\setminus\{1\}.
\]
Only terms with both physical arguments in \(Q\) are included. For \(u\ne1\) the indicated ratio is injective in \(x\). Exact unweighted anchor orthogonality therefore gives
\[
 \frac1n\sum_a\sum_{u\in Q\setminus\{1\}}|C_{G,H;a}(u)|^2
    =\|G\|_2^2\|H\|_2^2-\sum_x|G(x)H(x)|^2 .
\]
Here \(a\) varies in \(\widehat Q\), and the right side uses counting norms. In particular, for any nonnegative anchor weight \(\mu\) with \(\mu_a\le\nu_a\),
\[
 \|C_{G,H}\|_{\ell^2(\mu,u)}
          \le\sqrt{n\max_a\nu_a}\,\|G\|_2\|H\|_2 .
\]
No approximation of the true law is used in this upper.

Let \(E=F-G\) and suppose \(\|G\|_2\le\|F\|_2\), as for a hard physical cut. Expand the difference as \(C_{F,E}+C_{E,G}\) and apply the last estimate. The true cap \(\max\nu_a=O(p^{-1/2})\) and \(\|F\|_2^2=O(\sqrt p)\) give
\[
 \big|\|C_{F,F}\|_{\ell^2(\mu,u)}-\|C_{G,G}\|_{\ell^2(\mu,u)}\big|
                 \ll \sqrt p\,\|E\|_2.
\]
The \(\ell^2\) norm on the left is the square root of the corresponding actual weighted moment. Take \(\mu=\nu 1_{I_{\rm arc}}\) to use the original phase arc; in particular there is no hard cut on the true anchor law beyond that arc.

This gives two precise cuts. First, if a physical deleted part has counting squared mass \(O(1)\), then a uniform \(O(p)\) upper for the original arc moment is equivalent to the same upper for the truncated moment, by the displayed inequality. In particular all sites with \(|F(x)|\le C/\sqrt p\) may be deleted. Second, let \(D=(e+p^{-1/2})^{-1/2}/\log(2/(e+p^{-1/2}))\) on the hypothetical critical sequence. The conditional lower of Round 157 is \(\|C_{F,F}\|_{\ell^2(\mu,u)}^2\gg pD\). Deleting a part of squared mass \(o(D)\) preserves that lower up to a fixed constant, including removal of a growing lower-amplitude threshold \(o(\sqrt{D/p})\). The bound holds also for a sparse set of \(o(D)\) arbitrary physical sites, since \(|F|\le1\). These are cuts among the original four physical factors. They impose no bound on cutting the slope weight \(f_{\rm arc}\) itself.

## An absolute bound when each of the two pairs has a small factor

In the actual favorable sum, replace either of the original two physical factors at each of the \(x\) and \(y\) vertices by a real or complex row with counting norm \(O(1)\), supported on its original physical layer. Keep the other two factors bounded by \(|F|\) in modulus. This entire term costs \(O(p)\) in absolute value, retaining its slope weight and favorable sign. For the unsigned half of the favorable mask use Cauchy–Schwarz in \((a,u)\) with the weighted cross-correlation bound above, once for each pair. Each has \(\ell^2(\nu,u)\) norm \(O(\sqrt p)\).

For the signed half use
\[
   1_{\chi(1-t)=\rho}
       =\tfrac12(1+\chi(u-1)\chi(y-x))
\]
on \(x\ne y\). Let \(A_{u,a}\) and \(B_{u,a}\) be the modulated products on the two pairs, including their respective physical cuts. The additive convolution bound is \(\sqrt p\). Both \(\sum_u\|A_{u,a}\|_2^2\) and \(\sum_u\|B_{u,a}\|_2^2\) are \(O(\sqrt p)\), by the counting norms of the four factors and the bijection \((u,x)\leftrightarrow(ux,x)\) on each pair. The total signed half is therefore \(O(p)\). The removed diagonal has the same bound by Cauchy–Schwarz or better. The same proof works with the true phase-arc anchor measure and with any extra slope multiplier of bounded Mellin coefficient sum, by convolving this anchor measure with the multiplier coefficients and using their absolute values. This covers all quadratically small physical cuts in distinct pairs, including the matching signed geometry.

## The moderate high-pair conditions impose more signs

Suppose the squared amplitudes at \(1-vx,1-vy\) both exceed a fixed \(a\), and those at \(1-vux,1-vuy\) both exceed a fixed \(b\), with \(a+b>1\). The two-threshold character argument of [Round 159](ordinary-quantitative-near-unit-slope-159.md) makes every nonzero cross difference between these two levels have sign \(\rho\), before reflecting. Thus \(\chi(u-1)=1\), and at nonzero differences also
\(\chi(r-u)=\chi(1-ur)=1\) with \(r=y/x\), by the crossed pairs. At least one of the two squared thresholds exceeds \(1/2\); using that layer on both \(x\) and \(y\) gives \(\chi(y-x)=1\) for \(x\ne y\). The favorable sign is automatic on this slice. These exact extra restrictions concern the pair geometry. They do not supply a sufficiently strong second moment for this fixed middle or high layer.
