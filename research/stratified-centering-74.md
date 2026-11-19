# The truncated opposite autocorrelation budget through primes

Let \(q\) be any actual feasible probability in one sign sector, and fix \(\delta>0\). Suppose \(A\subset G\) is a nonempty set with \(\sqrt n\,q_i\ge1+\delta\) for every \(i\in A\). In the opposite autocorrelation comparison the high-density part of \(q\) pays a budget of order its squared mass, with an explicit prime-uniform error. This estimate uses the clipping identity on forbidden positions and the number of admissible opposite sign runs. Keeping the squared mass can distinguish a small high-density part of the optimizer from a general probability of unit mass. An optional partition of \(A\) accounts separately for differences within each block.

## A masked second moment with no within-block differences

Write \(a=|A|\), partition \(A=\bigsqcup_{j=1}^k A_j\) into nonempty blocks, and let \(b_j=|A_j|\). Independently choose \(H_j\) uniformly from \(A_j\), and take the random probability
\[
 \mu=\sum_{j=1}^k(b_j/a)\delta_{H_j}.
\]
Define \(v=q*\widetilde\mu\), with the indexing \(v_i=\sum_h\mu_hq_{i+h}\). Each realization is feasible with \(\sqrt n\,v_0\ge1+\delta\). If the original row is primary optimal and all members of \(A\) are at its cap, each realization is on the same true primary face. Put \(x_i=(q_i-B/n)_+\) for any density cutoff \(B>0\). For any mask \(S\subset G\), Jensen gives the exact upper bound
\[
\begin{split}
 \mathbb E\frac1n\sum_{i\in S}(nv_i-B)_+^2
 \le{}& \frac{n}{a^2}\sum_{i\in S}\left[
   \sum_j b_j\sum_{h\in A_j} x_{i+h}^2
    +\sum_{j\ne\ell}\sum_{h\in A_j,\,k\in A_\ell}x_{i+h}x_{i+k}
 \right].                                                       \tag{1}
\end{split}
\]
Indeed \((v_i-B/n)_+\le\sum_h\mu_h x_{i+h}\). The diagonal expectation uses \((b_j/a)^2/b_j\) for each \(h\in A_j\). For an ordered pair in two different blocks the corresponding expectation is \(1/a^2\), by independence. Distinct members of the same block never occur in the sampled measure together. Formula (1) retains the actual mask, which may be computed from a true projected cold window.

Define the ordered cross-block difference numbers
\[
 R_\times(t)=\#\{(h,k)\in A^2:k-h=t,\ h,k\text{ in different blocks}\}.
\]
Extending (1) to all sites bounds its right side by
\[
 \frac n{a^2}\left[L_x\sum_j b_j^2+
                 \sum_{t\ne0} C_x(t)R_\times(t)\right],            \tag{2}
\]
where \(L_x=\sum_i x_i^2\) and \(C_x(t)=\sum_i x_i x_{i+t}\). In particular there is no claim about how many within-block differences collide. One can keep the mask in (1), or use the following global pricing estimate.

Let \(C_*\) be a convex mixture of opposite feasible autocorrelations, and let \(\beta_*=1-nL_q C_*(0)\). For \(\lambda\ge0\) put \(e(t)=(R_\times(t)/a^2-\lambda C_*(t))_+\) on \(t\ne0\). The opposite budget of [round 73](opposite-autocorrelation-73.md#the-shared-autocorrelation-budget) bounds (2) by
\[
 \frac{nL_x}{a^2}\sum_j b_j^2+\lambda\beta_*
 +n\min\{L_x\|e\|_1,[(\textstyle\sum_i x_i)^2-L_x]\|e\|_\infty\}. \tag{3}
\]
Use \(C_x\le C_q\) for the budget term, \(C_x(t)\le L_x\) for the first residual bound, and the exact off-diagonal sum of \(C_x\) for the second. In particular the mass at zero has been removed before pricing cross-block differences.

The global partition estimate also follows using the uniform center measure of round 73. Place its within-block autocorrelation in the \(\ell^1\) residual of that estimate. The residual then pays at most \(nL_x\sum_j b_j(b_j-1)/a^2\), which together with the uniform diagonal is the displayed diagonal term. On a fixed mask the uniform center measure is the mean of the sampled center measures, and its actual convex cost is at most the expected cost in (1).

## A smaller budget for the clipped true row

Write \(M=\sum_i x_i\) and \(z=q-x\). For any opposite feasible probability \(r\), positivity and exact orthogonality give \(0\le x*\widetilde r\le q*\widetilde r=\mathbf1/n\). In particular the budget in (3) can use the exact nonnegative quantity
\[
 \beta_x(r)=n\|x*\widetilde r\|_2^2-nL_xL_r
    \le M-nL_xL_r,
\]
where the norm on the right-hand side of the equality is a counting norm. The same formulas hold by mixture, with \(L_r\) replaced by \(C_*(0)\) and the squared norm replaced by the weighted average of squared norms. This refinement follows by summing \(C_x(t)C_r(t)\) only over \(t\ne0\).

In the **specific prime mixture of round 73**, there is a squared-mass bound with a small additive error. Use the unnormalized transform \(\widehat x(u)=\sum_i x_i\overline{\eta_i(u)}\) at \(u\in Q\). At every opposite nonidentity position, \(\widehat x(u)=-\widehat z(u)\) because \(q\) has its actual Fourier zeros there. The low-density part satisfies \(z_i\le B/n\). Parseval therefore gives
\[
 \sum_{u\text{ opposite},\,u\ne1}|\widehat x(u)|^2
      \le n\sum_i z_i^2\le B(1-M).
\]
For a run generator \(t\in\mathcal T\), the nonconstant Fourier support of \(r_t^F\) is on \(t^{\pm j}\), \(1\le j\le L\), with coefficients bounded by one. For any nonidentity position \(u\) the equations \(t^j=u\) and \(t^{-j}=u\) have at most \(j\) solutions each in \(Q\). Using the untwisted run count \(|\mathcal T|\gg n/2^L\), the average of the contributions from all these Fourier coefficients is at most
\[
 \frac{2\sum_{j=1}^L j}{|\mathcal T|}\sum_{u\text{ opposite},\,u\ne1}|\widehat x(u)|^2
 \ll \frac{2^L L^2}{n} B(1-M).
\]
The constant Fourier coefficient contributes exactly \(M^2\) to \(n\|x*\widetilde r\|_2^2\), and the uniform member of the mixture has only this coefficient. Thus, with an absolute constant \(C\), the same mixture that prices all low-order differences satisfies
\[
 \beta_x^*\le
 \min\{M,M^2+C2^L L^2 B(1-M)/n\}-nL_x C_*(0).                 \tag{3a}
\]
The count of run generators and the forbidden Fourier equations suffice. This retains the original exact residual and masked diagonal estimates for the remaining terms in (3). The same derivation is uniform over all choices \(1\le L\le\lfloor(\log_2 p)/4\rfloor\). In the order-weight construction the relative error in the run count with a twist of order at most \(L\) is \(O(2^L L^3/\sqrt p)\) over this whole range. Shorter runs reduce the error in (3a) at the cost of weaker prices on torsion differences.

## A prime-uniform exclusion for clusters

Take \(S=S_{s,\delta/8}\) on any selected actual smooth window in the opposite sign from [round 72](smooth-windows-72.md#a-joint-threshold-for-the-remaining-obstruction), with \(d\to\infty\), \(d=o(D(p))\) and \(B=\sqrt d\). The hinge on the left of (1) is at least \(c_\delta d\) for **every** realization, uniformly once the window is long and its normalized mark and excess converge as in round 72. Use the order-weighted prime mixture of [round 73](opposite-autocorrelation-73.md#a-single-mixed-budget-for-all-low-order-differences) in (3), with \(L=\lfloor(\log_2 p)/4\rfloor\). The ambient cap \(q_i\le C/\sqrt n\) gives \(nL_x\le C\sqrt n\). The mixture has \(C_*(t)\ge c[1+L/\operatorname{ord}(t)]/n\) off zero, so choosing \(e=0\) and using \(0\le\beta_*\le1\) yields the necessary condition
\[
 \frac{\sqrt n}{a^2}\sum_j b_j^2
 +\frac n{a^2}\max_{t\ne0}\frac{R_\times(t)}{1+L/\operatorname{ord}(t)}
 \ \ge\ c_\delta' D(p) .                                          \tag{4}
\]
This holds for every such partition and all sufficiently large eligible primes. For the quantifiers, if there were a subsequence with the left side \(U=o(D)\), take \(d=\lfloor\sqrt{D\max(1,U)}\rfloor\). Then \(d\to\infty\), \(d=o(D)\) and \(U=o(d)\), so (3) contradicts the hinge lower bound. If a uniform constant and eventual threshold did not exist, one could choose such a subsequence. The same proof allows the arc-specific weight of round 73 or any other legitimate prime-uniform autocorrelation cover.

Keeping \(M\) changes the conclusion at smaller scales. Define the order-weighted count \(R=\max_{t\ne0}R_\times(t)/(1+L/\operatorname{ord}(t))\). For every \(B>0\) the same method gives the uniform necessary condition
\[
 B+\frac{\sqrt n\,M}{a^2}\sum_j b_j^2
  +\frac{nR}{a^2}\min\left\{M,M^2+C\frac{2^L L^2}{n}B(1-M)\right\}
   \ \ge\ c_\delta''D(p).                                      \tag{5}
\]
Here use \(nL_x\le C\sqrt n M\), (3a), and allow both \(B\) and \(L\) to vary with the prime. If the left side were \(o(D)\), take the same geometric mean for \(d\) with that entire left side as \(U\). In particular \(B=o(d)\), which is exactly the cutoff condition in the hinge lower bound. For example, with bounded block sizes and bounded \(R\), the condition excludes supercritical sets of size \(a\asymp n^{1/3}\) when \(M=O(a/\sqrt n)\) at some \(B=o(D)\). The diagonal and the squared-mass cost are bounded, and \(2^L L^2 B/a^2=o(D)\). This example requires an estimate of the actual clipped mass of the full feasible row. In the bounded *unweighted* multiplicity case a uniform opposite comparison already gives the squared-mass budget. Formula (3a) retains it up to a small error while using the stronger order-weighted prices.

For (4), if \(a\asymp\sqrt n\) and the mean block size seen by a uniform member of \(A\), \(a^{-1}\sum_j b_j^2\), is \(o(D)\), then some nonzero shift has \(R_\times(t)\gg_\delta D[1+L/\operatorname{ord}(t)]\). Thus a partition with small member-weighted block size and only bounded cross-block repeat counts cannot carry a supercritical plateau.

For an illustration of the partition cost, let \(U\subset\mathbb Z/n\) be a Sidon set of size comparable to \(\sqrt n\) with all neighbors separated by at least two. Set \(A=U\cup(U+1)\) with blocks \(\{u,u+1\}\). Such \(U\) exist for every sufficiently large \(n\): take a prime \(r\asymp\sqrt n\) with \(2r^2<n/2\), and use the integers \(2rj+(j^2\bmod r)\) for \(0\le j<r\). Equal integer nonzero differences force the same \(j-k\), since the difference between the two low-part deviations is strictly less than \(2r\). Reducing modulo \(r\) then fixes \(j+k\), since \(j-k\) is nonzero modulo \(r\). All signed differences lie in an interval of length less than \(n\), and all cyclic gaps are at least two. Then \(R_A(1)\ge|U|\), with shift 1 of order \(n\), while \(R_\times(t)\le4\) since cross-block differences use one Sidon difference plus one of \(-1,0,1\), with multiplicities \(1,2,1\). Formula (4) excludes this geometry. The round-73 zero-residual bound evaluated on all of \(A\) gives a left side of order at least \(\sqrt n\), while its general residual bound on \(A\) or its subset bound on \(U\) also excludes the geometry. This example illustrates the partition calculation; the improvement to the underlying budget is (3a).

## Ranked next tests

1. Measure the tail mass of one actual optimizer on each side at cutoffs \(B=o(D)\). Use (3a) inside the order-weighted comparison at the same cutoff, or bound its retained exact off-diagonal budget more strongly from the low-density Fourier energy. Combine with (1) where the actual mask supplies a diagonal improvement.
2. For a singleton root or a single large period class, the diagonal or cross-block cost can still be too high. A prime-uniform bound for the true convex hinge or a support constraint that limits such period classes remains necessary for this route.
