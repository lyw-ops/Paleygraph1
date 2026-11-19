# Selecting common time windows and localizing the remaining deficit

The actual cold trajectory admits a moving window with two quantitative controls at once. Its projected negative parts have vanishing normalized RMS, and its raw positive parts have vanishing bulk overlap. A true supercritical primary face must have large collision energy on one explicitly chosen defect set of vanishing counting density. This conclusion holds through all eligible primes. The inverse estimate on that set is open.

## A common window on the marked trajectory

Use the notation of [round 69](timed-pinning-69.md). Set \(v_0=0\), \(E_j=\|v_j\|_2^2\) in counting norm, and \(g_j=\sqrt n\,\overline{\phi_j}/2\). The bulk part of the raw row is \(B_{s,j}(i)=(sY_j(i))_+\) for \(i\ne0\). Write \(\mathbb E_{\mathrm{bulk}}=n^{-1}\sum_{i\ne0}\). On the available marked interval \(1,\ldots,D\), take an integer \(d\to\infty\) with \(d=o(D)\) and put
\[
 \eta=\sqrt{d/D},\qquad W_a=[a,a+d-1],\quad 1\le a\le D-d+1.
\]
Bars with subscript \(a\) are uniform averages on \(W_a\). Write \(U_a=\mathbb E_{\mathrm{bulk}}[\bar B_{+,a}\bar B_{-,a}]\).

For each lag \(\ell\ge1\) the nonexpansive map and the absolute-value activation give
\[
 \sum_{j\ge0}\mathbb E_{\mathrm{bulk}}(-Y_jY_{j+\ell})_+
 \le E_\ell/4 \le \ell.
 \tag{1}
\]
In fact \( \|v_{j+\ell}-v_j\|_2^2-\|v_{j+\ell+1}-v_{j+1}\|_2^2\) dominates \(4\sum_{i\ne0}(-v_j(i)v_{j+\ell}(i))_+\). The coordinate identity for \(|\cdot|\) gives the bulk loss, the marked activation is 1-Lipschitz, and \(K\) is a contraction. Telescoping yields (1). This is the lag estimate from [round 8](astra-iterate-8.md#2-every-lag-has-a-finite-loss-budget).

In the product defining \(U_a\) the simultaneous positive and negative copies at a fixed time have zero bulk product. A pair with lag \(\ell\) occurs in at most \(d-\ell\) windows, with the two orientations summing to \((-Y_jY_{j+\ell})_+\). It follows that
\[
 \sum_a U_a\le d^{-2}\sum_{\ell=1}^{d-1}(d-\ell)\ell
       =\frac{d^2-1}{6d}.
 \tag{2}
\]
The exact energy identity gives \(\sum_{j=1}^{D}g_j^2=D+(E_1-E_{D+1})/4\le D+1\). Each \(g_j\ge0\) occurs in at most \(d\) windows, so \(\sum_a\bar g_a\le\sum_{j=1}^D g_j\le D+1\). There are at least \(\eta D\) windows with \(\bar g_a\le1+4\eta\) for all sufficiently large \(D\). Indeed the number above that threshold is at most \((D+1)/(1+4\eta)\), with \(d/D=\eta^2\) and \(\eta D\to\infty\). Drop the starts \(a\le\lfloor\eta D/4\rfloor\) and the at most \(d/(6\eta)=\eta D/6\) windows with \(U_a>\eta\) by (2). This leaves a family \(\mathcal A\) of at least \(\eta D/2\) windows such that
\[
 \bar g_a\le1+4\eta,\qquad U_a=O(\eta).
 \tag{3}
\]
Both statements hold in each selected window for both signs. The starts tend to infinity and exclude any fixed set of early iterates.

The projection defect on \(W_a\) has normalized RMS at most \(1/\sqrt d\), jointly with (3). To see this, round 69 gives the exact defect \(sP_{-s}(Y_{a+d}-Y_a)/(2d)\). Iterating the nonexpansive map from \(v_d\) and \(v_0\) gives \(\|v_{a+d}-v_a\|_2\le\|v_d\|_2\le2\sqrt d\). The normalization is \(\|Y\|_{2,n}=n^{-1/2}\|Y\|_2\). Thus the RMS estimate is independent of the delay.

The selection also works within a prescribed tail \(L,\ldots,D\), \(L=\lceil D/2\rceil\). With \(R=D-L+1\) and \(\eta=\sqrt{d/R}\), replace \(1\) in the mean bound (3) by \(\sqrt{1+(E_L-E_{D+1})_+/(4R)}\), with an \(O(\eta)\) error. This follows by using \(\sum_{j=L}^D g_j^2=R+(E_L-E_{D+1})/4\). The tilted baseline is bounded by an absolute constant since \(E_L\le4L\). The absolute overlap bound (2) is unchanged after restricting the starts. In particular the tail version has a vanishing mean excess if the downward energy difference is \(o(D)\).

## An explicit small set must hold the obstruction

For the selected window let \(\bar Z_{s,a}\) and \(m_{s,a}=\bar Z_{s,a}(0)/\sqrt n\) be the exact projected average and normalized unscaled mark. The inherited uniform marked bound implies \(m_{s,a}=1+O(D^{-1}+\sqrt{D/n})\), taking the marked theorem with exponent \(1\). In the full-prefix selection use \(\epsilon=8\eta\) and form the pinned row
\[
 R_s=\bar Z_{s,a}+\big[(1+\epsilon)m_{s,a}-\bar g_a\big] b_s.
\]
For large fields the coefficient is nonnegative by (3) and the mark error is \(o(\eta)\). The row has exactly the intended mean \((1+\epsilon)m_{s,a}\), mark \(m_{s,a}\sqrt n\), and Fourier sector. Its bulk negative part has normalized RMS at most \(1/\sqrt d\) by the projection-defect estimate and nonnegativity of the raw row and of the pinned mean direction.

Fix a constant \(u>0\) and set \(S_{s,u}=\{i\ne0:R_s(i)<-u\}\). For each sign,
\[
 |S_{s,u}|\le n/(du^2).
 \tag{4}
\]
Let \(q\) be any feasible probability in the opposite sector with mark \(\gamma=\sqrt n\,q_0\). Orthogonality gives \(\sum_{i\ne0}q_i R_s(i)=m_{s,a}(1+\epsilon-\gamma)\). The contribution of the negative part outside \(S_{s,u}\) is at most \(u\). Cauchy--Schwarz on \(S_{s,u}\) therefore proves
\[
 m_{s,a}(\gamma-1-\epsilon)\le
       u +d^{-1/2}\Big(n\sum_{i\in S_{s,u}}q_i^2\Big)^{1/2}.
 \tag{5}
\]
In particular if a true larger normalized mark is at least \(1+\delta\) for fixed \(\delta>0\), then every primary optimizer on that side has \(n\sum_{i\in S_{s,\delta/4}}q_i^2\ge (\delta^2/16)d\) on the single defect set of the opposite proposal, for all sufficiently large primes in the sequence. One can take \(d=\lfloor D/\log D\rfloor\). The sets then have size \(O(n\log D/D)\), with the same range of selected mean and the separate overlap control (3).

One can also average the defect sets over \(\mathcal A\). Let \(F_{s,u}(i)\) be the fraction of the selected windows in which site \(i\) belongs to \(S_{s,u}\). Then \(\mathbb E_{\mathrm{bulk}}F_{s,u}\le1/(du^2)\), while \(n\sum_{i\ne0}q_i^2 F_{s,\delta/4}(i)\ge(\delta^2/16)d\) for every one of the same true supercritical optimizers. Here \(q\) is held fixed across all profiles. This distinguishes collision on the repeatedly measured cold defects from global collision of the optimizer.

An all-prime upper \(o(d)\) for the localized collision in (5) or its window average, for one actual optimizer on each sign and every fixed \(u>0\), would prove the conjecture upon sending \(u\) to zero. The bounds above locate the collision required of a supercritical face. They do not establish the necessary sparsity estimate for its optimizer on these adaptive sets. Nor is the small raw overlap a positivity assertion.

## Two delayed windows with a strictly useful mixture

At \(p=9413\) use flat weights separately on \([44,76]\) and \([84,124]\) of the actual zero-floor orbit, with \(\epsilon=1/200\). The rational interval check gives a strict feasible mixing interval containing \([0.668,0.968]\) for the coefficient of the second window, and contained in \((0.667,0.969)\). Thus the common mixture passes although each individual delayed window fails at the same requested normalized mark. The two outside witnesses are at bulk sites 1295 and 1720 of the minus row. Their slopes have opposite signs. Each inequality is affine in the mixing coefficient, so outward checks at the two inner endpoints imply simultaneous positivity on the entire closed interval, and the two witnesses exclude both outside rays.

The windows were selected via floating exploration, then frozen. The verification uses the unrounded orbit with the [Euclidean shadowing method](true-spill-63.md#norm-shadowing-of-the-unrounded-input), as in round 69. The example is finite and uses depths beyond the size of the proved arithmetic window at this field. It makes no claim about positive mixtures at asymptotic marked depth. [Checker](paired-windows-70-check.py) · [Interval record](paired-windows-70-checks.jsonl)

## Ranked next tests

1. On the selected windows estimate the actual larger-face collision \(n\sum_{i\in S_{s,u}}q_i^2\), with \(S_{s,u}\) computed on the unrounded orbit, and seek \(o(d)\) for each fixed \(u>0\). A fixed positive lower bound on the true normalized mark above 1 would force order-\(d\) localized collision by (5). A counting estimate of the defect set or a small RMS estimate alone cannot pass.
2. In the proved growing-depth window select two delayed profiles and compare the true signed mixing thresholds on the localized deficit sets. A compatible interval at \(\epsilon_p\to0\) would give the desired theta bounds, while a certified separation along unbounded primes would reject those profiles.
