# Opposite autocorrelation budgets on the visible part of a clipped row

The weighted opposite run mixtures can be applied after removing parts of a clipped feasible row which rarely reach the actual negative masks. The removed mass is charged by its exact squared overlap with the masks. The remaining part may have new forbidden Fourier coefficients. Their contribution to the run budget is controlled by the counting energy of that part, with a prime-uniform factor from the distribution of run powers. This permits a squared-mass budget based on visible tail mass, including when the full clipped mass is large.

## Visibility of the genuine marked masks

Let \(q\) be a true feasible probability on the cyclic frequency group \(G\) of order \(n=(p-1)/2\). Fix \(\delta>0\) and a nonempty set \(A\) on which \(\sqrt n\,q_h\ge1+\delta\). Partition \(A=\bigsqcup_j A_j\), with \(a=|A|\) and \(b_j=|A_j|\). Let \(\boldsymbol\mu\) be the random probability of [round 74](stratified-centering-74.md#a-masked-second-moment-with-no-within-block-differences), choosing one independent uniform member of each block with weight \(b_j/a\). Then \(\mathbb E\boldsymbol\mu=\mu_A\), the uniform probability on \(A\). Each \(v=q*\widetilde{\boldsymbol\mu}\), in the convention \(v_i=\sum_h\boldsymbol\mu_hq_{i+h}\), remains feasible and retains a supercritical mark. Exact cap sites of a true primary optimizer retain primary optimality as well.

Take any probability distribution over the selected smooth windows of [round 72](smooth-windows-72.md#a-joint-threshold-for-the-remaining-obstruction), independently of the drawing of the centers. Write \(S\) for the actual opposite negative mask at the fixed threshold \(u=\delta/8\) for the chosen window. The expectation over windows is denoted by \(\mathbb E_S\). The visibility of an original site \(j\) is
\[
 w_j=\mathbb E_S\sum_h\mu_A(h)\,\mathbf1_S(j-h).
\]
It is a number in \([0,1]\), and its mean over original sites is \(\mathbb E_S(|S|/n)\). The analysis also allows a single selected window.

Put \(x_i=(q_i-B/n)_+\) and take any split \(x=y+z\) into nonnegative vectors. Define \(M_y=\sum_i y_i\), \(L_y=\sum_i y_i^2\), and \(E_z=n\sum_i w_i z_i^2\). Jensen for the clipping map and then the triangle inequality in the joint \(L^2\) space give
\[
\begin{split}
 \left(\mathbb E_{S,\boldsymbol\mu}n
 \sum_{i\in S}(v_i-B/n)_+^2\right)^{1/2}
  &\le
    \left(\mathbb E_{S,\boldsymbol\mu}n
       \sum_{i\in S}(y*\widetilde{\boldsymbol\mu})(i)^2\right)^{1/2}
       +\sqrt{E_z}.                                             \tag{1}
\end{split}
\]
To see the second term, \((\sum_h\boldsymbol\mu_h z_{i+h})^2\le\sum_h\boldsymbol\mu_h z_{i+h}^2\) by probability normalization. Summing on \(S\) and taking the expectation gives precisely \(E_z\) for the last expression. A sharp but optional split is \(y_i=x_i\mathbf1_{w_i>\tau}\), giving \(E_z\le\tau n\sum_i z_i^2\). At \(\tau=0\) this term vanishes. A split for which some visible coordinates of \(z\) have small height can use the exact \(E_z\).

## The run budget without assuming Fourier zeros for the visible part

Let \(L\) be the run length and \(\Omega\) a circular-tent phase weight as in [round 75](bohr-pricing-75.md#one-weight-for-a-set-of-prescribed-shifts), with mean \(\mu_\Omega\) and with its stated counting premise. Let \(\mathcal C\) be the convex mixture of opposite feasible autocorrelations constructed there, and \(W(h)\) its price weight with \(\mathcal C(h)\ge cW(h)/n\) for \(h\ne0\).

Even with no inherited Fourier zeros for \(y\), positivity gives \(0\le y*\widetilde r\le q*\widetilde r=\mathbf1/n\) for any actual opposite feasible \(r\). Averaged over \(r\) from the mixture, this bounds the total convolution budget by \(M_y\). For the refinement, the weighted run count gives \(T_\Omega\gg n2^{-L}\mu_\Omega\). The fiber bound for \(t^{\pm j}=u\) is at most \(j\) points, each of weight at most one. Hence the expected contributions of the nonconstant coefficients in the Fejér transform are bounded by
\[
  C\frac{2^L L^2}{n\mu_\Omega}
     \sum_{\substack{u\ne1\\u\ \mathrm{opposite}}} |\widehat y(u)|^2
  \le C\frac{2^L L^2}{\mu_\Omega} L_y,                            \tag{2}
\]
where the Fourier transform is unnormalized. Indeed the powers of each admissible run are distinct and the Fejér coefficients have modulus at most one. Use Parseval for the final inequality. For the unconditioned run mixture the same bound has \(\mu_\Omega=1\). Uniform rows contribute only the constant Fourier coefficient, whose square is exactly \(M_y^2\). Thus the exact off-diagonal budget on \(y\) satisfies
\[
 \begin{split}
 \beta_y&=n\sum_{h\ne0} C_y(h)\mathcal C(h)\\
 &\le F_y-nL_y\mathcal C(0),\\
 F_y&=\min\{M_y,\ M_y^2+C 2^L L^2 L_y/\mu_\Omega\}.
 \end{split}                                                     \tag{3}
\]
One can retain the opposite Fourier energy in the first line of (2). If \(M=\sum_i x_i\) and \(L_z=\sum_i z_i^2\), the identity \(\widehat y=-\widehat{(q-x)}-\widehat z\) on opposite positions also bounds that energy by \(\big(\sqrt{B(1-M)}+\sqrt{nL_z}\big)^2\). This follows from Parseval and the triangle inequality. It recovers the low-density bound of rounds 74–75 when \(z=0\), and can be useful when the removed part and retained part have very different global energies. With no condition on the removed part, \(L_y\le (C/\sqrt n)M_y\) already gives a small error for the visibility cut used below.

Write \(R_\times(h)\) for the ordered difference count across distinct blocks in \(A\), and \(U=\max_{h\ne0} R_\times(h)/W(h)\). Applying the round-74 second moment to \(y\), and using (3) for the off-diagonal comparison, bounds the first squared term in (1) by
\[
 \frac{nL_y}{a^2}\sum_j b_j^2
 +\frac{nU}{c a^2}\big(F_y-nL_y\mathcal C(0)\big).                \tag{4}
\]
The diagonal in (4) can also be kept exactly on the actual masks as
\[
 \frac{n}{a^2}\mathbb E_S\sum_{i\in S}\sum_j b_j
                 \sum_{h\in A_j}y_{i+h}^2 .
\]
For the proof of (4), the expected pair coefficients are diagonal \(b_j/a^2\) for \(h\in A_j\), \(1/a^2\) for any ordered pair in distinct blocks, and zero for distinct sites in the same block. Extending just the off-diagonal sum to all sites gives \(n a^{-2}\sum_{h\ne0}R_\times(h)C_y(h)\), which is bounded by (3). If using a residual \(e=(R_\times/a^2-\lambda\mathcal C)_+\) rather than a uniform comparison \(U\), the additional cost is at most \(n\min\{L_y\|e\|_1,(M_y^2-L_y)\|e\|_\infty\}\).

## Consequence at marked depth and separation of cap sites

For \(d\to\infty\), \(d=o(D(p))\), and \(B=o(d)\), the left squared quantity in (1) is at least \(c_\delta d\), by the genuine marked-window comparison. This lower bound holds for each eligible mask and each sampled feasible row, so there is no independence hypothesis on the original optimizer versus the windows. In particular along any prime subsequence on which \(q\) is supercritical on \(A\), the sum of \(E_z\) and (4) is bounded below by \(c_\delta d/2\), after a harmless choice of the constant \(c_\delta\). If these two quantities are both \(o(d)\) on a given family of actual masked profiles, that family cannot have a fixed supercritical gap. Here the time windows are chosen first, and \(w,y,z\) depend on those windows; the contradiction only uses the displayed scale for those windows.

For one use of the scales, suppose \(a\asymp\sqrt n\), block sizes are bounded, \(U=O(D^2)\), and \(\mu_\Omega\ge p^{-1/8}\). If at one suitable selected window \(M_y=O(D^{-1})\) for the part visible from at least one center, take \(y=x\mathbf1_{w>0}\), so \(E_z=0\). For \(L\le(\log_2 p)/4\), the error in (3) times the comparison coefficient is \(o(1)\) since \(L_y=O(M_y/\sqrt n)\) and \(D\) is of log-star order. The term paid at \(M_y^2\) is \(O(1)\), as is the diagonal. This excludes the specified combination with a fixed supercritical gap for \(d\to\infty\), \(B=o(d)\). It allows full clipped mass of order one outside the visible set. The existence of such a window or small visible mass on actual primary faces is open.

There is a second separation for deterministic uniform centering, directly at the prescribed mask. Let \(x_A=x\mathbf1_A\), and \(x_{\rm out}=x-x_A\). Then
\[
 \Big(n\sum_{i\in S}(v_i-B/n)_+^2\Big)^{1/2}
 \le
 \frac{\sqrt n\max_{j\in A}x_j}{a}
       \left(\sum_{i\in S}R_A(i)^2\right)^{1/2}
  +\Big(n\sum_{i\in S}(x_{\rm out}*\widetilde\mu_A)(i)^2\Big)^{1/2}.
                                                                    \tag{5}
\]
The contribution of \(x_A\) is bounded by \(R_A(i)\max_A x/a\) at each site. For exact cap sites \(x_A=(q_0-B/n)_+\mathbf1_A\), so this bound for the core is an equality. The outside term can use the visibility estimate (1)–(4) with singleton blocks and with \(x_{\rm out}\) split into visible and rarely visible parts. In particular, if \(A\) is an exact period subgroup, the first squared bound in (5) is \(n(q_0-B/n)_+^2|S\cap A|\). This retains actual mask hits inside the period subgroup instead of paying the repeated differences from all its members. For a single marked center it vanishes since \(0\notin S\); the outside term still contains the full masked diagonal of the clipped row and generally needs a separate estimate. The formula itself makes no bound on the number of hits or on the outside mass.

## Optimizing the split on an actual window

The simplest paid version of (4) uses \(M_y^2+C2^L L^2 L_y/\mu_\Omega\) and omits the diagonal debit. This gives a convex optimization for a fixed row, masks, and partition. Set \(\lambda=nU/(c a^2)\), \(\alpha_i=nw_i\), and
\[
 \kappa_i=\frac{n}{a^2}\mathbb E_S\sum_j b_j
                 \sum_{h\in A_j}\mathbf1_S(i-h)
              + \lambda C2^L L^2/\mu_\Omega .
\]
Twice the minimum of
\[
 \sum_i\alpha_i(x_i-y_i)^2+\sum_i\kappa_i y_i^2
                  +\lambda\Big(\sum_i y_i\Big)^2,\qquad 0\le y_i\le x_i ,
                                                                    \tag{6}
\]
is an upper bound for the squared left side of (1). The minimizer with \(y_i=0\) at coordinates with \(\alpha_i+\kappa_i=0\) can be found from
\[
 y_i=\frac{(\alpha_i x_i-\lambda m)_+}{\alpha_i+\kappa_i},
 \qquad m=\sum_i y_i .
\]
Indeed the first-order residual is zero wherever the displayed numerator is positive, and nonnegative at the lower endpoint elsewhere. The upper bound \(x_i\) is automatic. The right side of the equation for \(m\) is continuous and decreasing in \(m\) in the weak sense, so there is a unique solution for that choice of the zero-coefficient coordinates. Equation (6) gives the optimal such squared upper bound up to the factor two from (1). At a singleton center the two weights are both \(nw_i\), \(U=0\), and (6) recovers the original masked collision after the factor two. A smaller singleton bound requires information beyond this split.

The split can also be optimized jointly with the choice of optimizer on an actual primary face. Allow nonnegative \(y,z\) with \(q_i-B/n\le y_i+z_i\le q_i\), impose the true primary mark and full Fourier feasibility on \(q\), and specify the center conditions \(\sqrt n\,q_h\ge1+\delta\) on \(A\). These are linear constraints. Minimize the quadratic analogue of (6), using \(n\sum_i w_i z_i^2\) as its first term. One can use the exact total budget \(\lambda n\,\mathbb E_r\|y*\widetilde r\|_2^2\) in place of the mass-squared term and the Fourier-error part of \(\kappa_i\). This is a nonnegative quadratic form, and by positivity of the rows it is nondecreasing in each coordinate of a nonnegative \(y\). Every feasible \(y+z\) dominates the actual \((q-B/n)_+\), and any excess can be removed without increasing the objective. Hence the program is a joint convex upper certificate at the fixed centers and windows, even when the primary optimizer is not unique. An \(o(d)\) bound on its attainable value through primes remains open.

## Ranked next tests

1. Measure the clipped mass on \(S+A\), including its actual opposite Fourier energy and its cost on the retained diagonal. Use (6) to optimize the split on each actual matched window, then test whether the objective is \(o(d)\) through primes in a class of primary faces.
2. For true period subgroups use (5) to estimate the actual hits in the marked coset and the outside tail separately. For the singleton case keep the exact opposite positivity and find a weighted upper for the nonroot masked diagonal; global difference pricing alone supplies no such bound.
