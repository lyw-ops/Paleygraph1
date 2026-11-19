# Negative-part Fourier certificates at zero bulk floor

The one-sided test in [the reciprocal extension](parallel-extension-7.md#opposite-sector-tests-with-the-same-weights) can be formulated without any stationary solve or positive bulk floor. The cost is the negative part of an exactly projected finite-time average. A linear program evaluates the worst pairing compatible with opposite Fourier support, and a translated witness gives a cheaper certified upper bound. The zero-floor fixed points are exactly pairs of theta optimizers. The field-first order of limits matters because the fixed-point problem for an individual field already returns theta.

## Feasible-sector trial and its opposite linear program

Use $n=(q-1)/2$, $K^2=I-J$ and $U_\sigma=\mathbb R\mathbf1\oplus\ker(I-\sigma K)$. With weights $w_0=1$, $w_i=\tau/n$ off the mark, allow $\tau=0$. Put $W=\sum_i w_i$ and $B\in\mathcal B_{-\sigma}$ when $B\ge0$, $B\in U_{-\sigma}$ and $\sum_i B_i=\sqrt{nW}$. Let $z_0=0$, $z_{t+1}=(z_t+K\Phi(z_t))/2$, and $\Phi_i(z)=\sqrt{z_i^2+4w_i}$. Use the trial

$$ H_{\sigma,T}=\frac{(I+\sigma K)\bar u_T}{2}\in U_\sigma,\qquad
 \bar u_T=T^{-1}\sum_{t<T}\Phi(z_t). $$

Set $b=H_{\sigma,T,0}$, $m_T=\sqrt{nW}\,\overline H_{\sigma,T}$ and $C_i=(H_{\sigma,T,i})_-$ off the mark, with $C_0=0$. The [norm identity](iteration-parity.md#a-criterion-involving-only-the-iterates) uses no strict positivity of the bulk floor and gives $m_T\le W$. Opposite sectors give $\langle H_{\sigma,T},B\rangle=m_T$ exactly. Thus

$$ b\sqrt{W/n}\,\theta_{-\sigma}\le m_T+D_T,
 \qquad D_T=\max_{B\in\mathcal B_{-\sigma}}\langle C,B\rangle. \tag{1} $$

Indeed take a maximizer of the mark, and retain its whole marked contribution and the lower bound $-\langle C,B\rangle$ off the mark. More generally the same estimate for $bB_0$ uses the actual $\langle C,B\rangle$ for any opposite $B$, including the stationary one at positive $\tau$. Equation (1) is stronger than requiring $H$ to be everywhere positive. Its elementary LP dual is

$$ D_T=\sqrt{nW}\min\{\overline G:G\in U_\sigma,\ G\ge C\}. \tag{2} $$

Here $G$ is necessarily nonnegative. The projected average $H+G$ is then a feasible theta row for $\sigma$ provided $b>0$, yielding the finite upper bound $\theta_{-\sigma}/\sqrt n\le\sqrt n\,\overline{H+G}/(H+G)_0$. This keeps any improvement from $G_0$. At positive floor, unlike (1), the actual pairing against the stationary opposite spectrum needs its mark-to-theta bracket.

## Exactly zero bulk floor

At $\tau=0$, (1) becomes $b\theta_{-\sigma}/\sqrt n\le1+D_T$. For each fixed $T$, the fixed-depth marked cancellation from [the trace argument](uniform-fixed-depth.md#applying-the-algebra-to-smoothing) transfers to $\tau=0$ by the elementary bound

$$ \|z_t^{(\tau)}-z_t^{(0)}\|_2\le t\sqrt\tau. $$

For a common input, the two update maps differ by at most $\sqrt\tau$ in norm, since the activations differ by at most $2\sqrt{\tau/n}$ in each bulk coordinate, coincide at the mark, and $K$ is a contraction. Each map is nonexpansive, giving the bound by induction. At positive floor, fixed-depth cancellation implies $b\to1$ at fixed $\tau$ using $H_{\sigma,T}=\tfrac12(\bar u_T+\sigma\bar z_T)+\sigma z_T/T$. The same conclusion holds at zero floor after letting the auxiliary $\tau$ decrease to zero in the comparison. This step only needs the established fixed-depth cancellation for the marked coordinate; it makes no claim about transferring the whole worst pairing uniformly as $T$ grows.

Consequently the sufficient bound is $\liminf_{T\to\infty}\limsup_{p\to\infty}D_T=0$ for each sign at **zero** bottom weight. The sides may use different depths. The upper bounds for both theta values and $\theta_+\theta_-=n$ imply the target. This formulation avoids proving an estimate for a family of positive floors.

The zero-floor fixed points also have a direct description. If $z=K\Phi(z)$, put $A_\pm=(\Phi(z)\pm z)/2$. Then $A_\pm$ are nonnegative, have coincident means, and belong to the complementary sectors. Their products are one at the mark and zero elsewhere. Orthogonality therefore forces the common mean to be $1/\sqrt n$. Their marked product is one, so $\sqrt n A_\pm$ attain the two theta optima. Conversely any two mean-one optimizers $P_\pm$ satisfy $\sum_i P_{+,i}P_{-,i}=n=P_{+,0}P_{-,0}$, hence their bulk products vanish. Then $z=(P_+-P_-)/\sqrt n$ is fixed and $\Phi(z)=(P_++P_-)/\sqrt n$. The possible nonuniqueness of a zero-floor fixed point does not affect (1) or the finite-time trial.

The square control retains a uniform obstruction even without stationary data. At $q=r^2$, use the explicit plus-optimal subfield row in (1) with a negative-sign trial. Since $\theta_+=r-1$ and $m_T\le1$, at every fixed $T$ one has $\liminf_r D_T\ge\sqrt 2-1$ from the fixed-depth marked law. The same lower bound applies to convex combinations of any fixed finite list of prefix trials, since each has the same limiting mark and the same mean bound. Time mixing by itself does not remove the square obstruction.

## The prime Fejér obstruction also holds at zero floor

The [Fejér perturbation](parallel-negative-8.md#prime-counterexample-to-a-norm-only-use-of-full-feasibility) rules out a proof based only on the endpoint norm, the two ports, the averaged reciprocal inequality and the support constraint. It can be placed at zero floor in the field-first order. In the notation of that argument put $m_t=\langle j,\Phi(z_t)\rangle/2$. At zero floor $z_1=Ke_0$. The Jacobi entry bound and $\|Ke_0\|_2^2=1-1/n$ give $\|z_1\|_1\ge(1-1/n)n/\sqrt q$. Therefore $m_1\ge (1-1/n)\sqrt n/(2\sqrt q)$, which is bounded below on large fields.

For $T\ge2$ the norm identity now gives $2T-\|z_T\|_2^2\ge 2m_1^2\gg1$. The slack in $\sqrt{2T}-\|z_T\|_2$ is at least a constant times $T^{-1/2}$. Also $m_0=1/\sqrt n$ gives $1-c_T\ge(1-m_0)^2/(2T)$, where $c_T=T^{-1}\sum_{t<T}m_t$. At fixed $T$, choose $L=T^4$ and take the arbitrarily large primes supporting the Fejér patterns. The perturbation uses only $O(T/\sqrt L)=O(T^{-1})$ of the endpoint slack and $O(L^{-1})$ of the mean slack. Its two unprojected positive averages stay nonnegative and continue to meet the reciprocal inequality with zero bulk products as lower bounds. The trial mark changes by $O(n^{-1/2})$, and its bulk negative norm is still at most $\sqrt{2/T}$. Yet the opposite feasible pairing retains the positive constant from (8) of that note. The same slack proof works at every fixed $0<\tau\le1$, since $z_1=(1-\sqrt{\tau/n})Ke_0$ and $\sqrt W-m_0\to \sqrt{1+\tau}-\sqrt\tau>0$. The modifications preserve the averaged identities used in the comparison. The time recurrence itself is the untested constraint in this counterexample.

## The true iteration against bounded-degree Fejér tests

Using the [fixed-expression Mellin approximation](iteration-parity.md#uniform-fixed-expression-trace-estimates) for the **true finite-time iterate**, there is a contrasting result for precisely this family of test spectra. Write $g=\sqrt n C$, $\mu=B/\sqrt{nW}$ and $f_\mu(x)=\sum_h\mu_h h(x)$ on $Q$. At each fixed $T$ and $\tau\ge0$, assume a family of probabilities has bounded $\sqrt n\|\mu\|_2$ and $\sum_{x\ne1}|f_\mu(x)|=o(\sqrt q)$. Then

$$ \sum_h\mu_h g_h-\overline g\longrightarrow0. \tag{4} $$

Indeed put $Y_t=\sqrt n z_t$. Off the mark $g$ is a Lipschitz function of $Y_0,\ldots,Y_T$, namely the negative part of $\frac1{2T}\sum_{t<T}(\sqrt{Y_t^2+4\tau}+\sigma Y_t)+\sigma Y_T/T$. The fixed-depth construction approximates the $Y_t$ by bounded, fixed-complexity Mellin fields in normalized $\ell_2$. The same holds at $\tau=0$ via $\|Y_t^{(\tau)}-Y_t^{(0)}\|_{2,n}\le t\sqrt\tau$ and the positive-floor approximants. Compose with the Lipschitz function and approximate on the approximants' bounded range by a fixed polynomial. Setting the mark of $g$ to zero costs at most the single bounded value of the polynomial there, divided by $\sqrt n$ in normalized $\ell_2$. Thus for each fixed accuracy there is an approximant $g_*$ with $\|g_*-g\|_{2,n}$ within that accuracy. The Mellin trace for each polynomial term has bounded rank and is lisse off $1$, so its normalized inverse Fourier coefficient there is $O(q^{-1/2})$ by purity. The bounded exceptions in the trace product add $O(q^{-1})$ uniformly. This uses the fixed-depth trace argument, with constants depending on the chosen accuracy, $T$ and $\tau$. Consequently

$$ \left|\sum_h\mu_h g_{*,h}-\overline{g_*}\right|
\ll_{g_*} q^{-1/2}\sum_{x\ne1}|f_\mu(x)|=o(1). $$

Cauchy–Schwarz controls the two approximation errors by $(1+\sqrt n\|\mu\|_2)\|g_*-g\|_{2,n}$. Send the approximation error to zero after the field limit to obtain (4).

For the Fejér example $\mu=F_L/n$, both $\sqrt n\|\mu\|_2=O(\sqrt L)$ and $\sum_{x\ne1}|f_\mu(x)|\le L$ are bounded when $L$ is fixed at each depth. This includes $L=T^4$ when $q$ goes to infinity first. Thus the true pairing, unlike the perturbation's, is bounded in field limsup by $\sqrt W\limsup_q\overline g\le W\sqrt{2/T}$. At positive floor the faster bound from [the joint endpoint and average cutoff](parallel-negative-8.md#locating-the-terms-that-can-contribute) applies. The argument also allows any fixed-depth family with these two Fourier bounds. It does not apply to the whole feasible cone, whose positional $\ell_1$ and scaled frequency $\ell_2$ can both grow with the field.

As a finite check, at zero floor and depth 128 the three pairs $(p,L)=(1000033,2),(1000081,3),(1088641,4)$ give $\sum_h (F_L(h)/n)g_h-\bar g$ equal to $2.3283\times10^{-5}$, $1.8557\times10^{-5}$ and $3.5193\times10^{-5}$. These use $d=4$ and the minus trial, and take the first prime at least one million in the respective progression $1\pmod{8\prod_{j=1}^{L-1}(4^j-1)}$. The arithmetic statement (4) uses the approximation argument rather than assuming a rate from these samples.

If one uses the [stronger uniform fixed-depth approximation draft](uniform-fixed-depth.md), then at each fixed $\tau>0$, (4) only needs $\sum_{x\ne1}|f_\mu(x)|=o(\sqrt q)$ for feasible probabilities. The polynomial approximation is uniform outside a bounded number of frequencies, and both true and approximate scaled costs are uniformly bounded at fixed depth after removing the mark. The exceptional cost pairs against at most $O(q^{-1/2})$ mass by the point cap. This removes the need for a scaled frequency $\ell_2$ bound at positive floor. The argument for bounded-degree Fejér tests at zero floor uses only the normalized $\ell_2$ approximation.

## An explicit majorant and a projected point-cap comparison

Let $P_\sigma=(I+\sigma K-J)/2$ be the orthogonal projection to the zero-mean part of $U_\sigma$. The pairing against $B\in\mathcal B_{-\sigma}$ is unchanged if $C$ is replaced by $C_\alpha=C-\alpha P_\sigma C$. The Jacobi bound gives $B_i\le (\sqrt q+1)\sqrt{W/n}$. Maximizing the pairing over just this point cap and the total mass is an upper bound computed by sorting. One can also fix $B_0$ to its actual value when comparing with the stationary pairing. The resulting conditional upper bound does not apply to arbitrary opposite spectra.

For an actual Fourier majorant take the nonnegative [elementary witness](iterate-majorants.md#repair-with-translated-witnesses) $L_\sigma\in U_\sigma$, of mean one and mark $h=L_{\sigma,0}$. For a threshold $t$, let

$$ G=\alpha P_\sigma C+t\mathbf1+h^{-1}L_\sigma*(C_\alpha-t)_+. \tag{3} $$

Translation preserves the sector, and the marked term of the convolution shows $G\ge C$. Its mean is $t+h^{-1}\sum_i(C_{\alpha,i}-t)_+$, minimized at the appropriate upper order statistic. Thus (3) is an explicit dual row for (2), using a point cap slightly tighter than the Jacobi cap because translations of $L_\sigma$ give $B_i\le\sqrt{nW}/h$. In the experiment, $\alpha$ ranges over $0,1/2,1,3/2,2$. Each candidate is valid at exact arithmetic. A smaller value from the exact LP isolates the benefit of imposing all opposite Fourier constraints.

For squares this repair can be exact. Write $H_0^\perp$ for the subfield annihilator in the frequency group, so the elementary negative witness vanishes on $H_0^\perp\setminus\{0\}$. Suppose for a negative-sign trial that every excess $(C_\alpha-t)_+$ is on $H_0^\perp$, that $C_\alpha\ge t$ on $H_0^\perp$, and that the trial is nonpositive on $H_0^\perp\setminus\{0\}$. Then $G=C$ on $H_0^\perp$ by (3). In particular $H+G$ is supported on the mark when restricted to that subgroup. Pairing it with the uniform plus optimum on $H_0^\perp$ attains complementary equality, so this explicit repair reaches the theta bound at that field. These are sufficient conditions for exactness, independent of convergence of the averaging iteration.

## Numerical comparison

[The replay](../negative_pairing.py) uses the existing averaged iteration and LP. At positive floor it also compares with the actual stationary opposite vector. At zero floor it omits the stationary solve and can certify the repaired row with interval arithmetic by rounding on the allowed Fourier support. See [positive-floor runs](../data/negative-pairing.csv), [zero-floor runs](../data/negative-pairing-zero.csv), and [million-order zero-floor runs](../data/negative-pairing-zero-large.csv). The [million-order positive-floor replay](../data/negative-pairing-large.csv) saves the pairing and cap columns only.

At $\tau=0.0005$, $T=512$, the smaller-mark side gives the following comparison. The LP is run only at small orders. The cap and LP columns are numerical upper estimates of the support function in (1), and the actual column uses the converged stationary spectrum of the opposite side.

| Order | Actual | LP | Projected cap |
|---:|---:|---:|---:|
| 1997 | 0.004958 | 0.005219 | 0.009139 |
| 1849 | 0.078126 | 0.078205 | 0.078213 |
| 9413 | 0.005075 | | 0.009997 |
| 9409 | 0.183309 | | 0.183490 |
| 153649 | 0.005155 | | 0.011697 |
| 151321 | 0.393452 | | 0.393860 |
| 1000033 | 0.005171 | | 0.012392 |
| 994009 | 0.407511 | | 0.407929 |

For the tested small primes, the LP optimum is close to the stationary cost on this side. Fixing the stationary mark reduces the point-cap bound modestly. At zero floor and depth 512, the repaired rows at $p=9413$ give two certified normalized upper bounds $1.005674$ and $1.005050$, rounded up. At $p=1000033$ the two bounds are numerically $1.008327$ and $1.006778$. The zero-floor square control at $997^2$ gives $1.412796$ as the upper bound for its plus theta, numerically equal to $(997-1)/\sqrt{(997^2-1)/2}$. Overall there are 48 interval-certified rows at orders up to 10000. The near-square field-order discrepancy survives both the stationary-free LP and the explicit majorant. The uniform prime estimate in (1) remains open.
