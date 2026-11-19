# A reciprocal cap for the one-sided extension

For [Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), the full stripped activation turns the signed extension in [stationary-mark-constant.md, (4a)](stationary-mark-constant.md#a-scalar-criterion-and-its-denominator) into a weighted cost on trial spectra in a single Fourier sector. The weight is determined by the **actual opposite stationary spectrum**. A Fourier projection of the averaged finite-time iterate supplies a specific signed trial. Its mean only needs an upper bound if we test the sign with the smaller stationary mark. The remaining leakage estimate through all primes is an assumption. The target here is the marked-minus-constant source of a stationary sign block; the [reference extension](parallel-reference-4.md#exact-extension-for-a-strict-diagonal) instead interpolates the inverse column restricted to an exceptional set of a reference diagonal.

## A pointwise cap with explicit cost

Work at exponent $\alpha=1$. Let $e_0$ be the marked unit vector, $j=\mathbf1/\sqrt n$, $J=jj^{\mathsf T}$ and $K^2=I-J$. For a sign $\sigma$ write $Q=I-\sigma K$, $q_0=Q^{1/2}e_0$, $E_\sigma=\ker Q$ and $U_\sigma=\mathbb Rj\oplus E_\sigma$. Set $A=A_\sigma$, $B=A_{-\sigma}$, $a=A_0$, $a'=B_0$ and $\nu=\sqrt{\tau/n}$. Then $A_iB_i=\nu^2$ off the mark, $aa'=1$, and $\langle j,A\rangle=\langle j,B\rangle=\sqrt W$, with $W=1+(n-1)\nu^2$. In particular $A\in U_\sigma$ and $B\in U_{-\sigma}$.

On the bulk let $m_i=\min(1,B_i/\nu)=\min(1,\nu/A_i)$ and put $m_0=1$. The active set is $I_\sigma=\{i\ne0:A_i>\nu\}$. For the diagonal $V$ and the defect $G$ of the [one-sign block](stationary-mark-constant.md#a-two-dimensional-defect-relation), we have
\[
 V_i^2=\frac{1-m_i^2}{1+m_i^2},\qquad
 \mathcal R_i:=\frac{V_i^2}{1-V_i^2}=\frac{m_i^{-2}-1}{2}.
\]
Both formulas include the inactive entries and the mark. For a real, possibly signed trial $H\in U_\sigma$ define the bulk leakage
\[
 \mathcal L_\sigma(H)=\sum_{i\ne0}m_i^2 H_i^2 .
\]
If $\langle j,H\rangle=c$ and $H_0=b$, put
\[
 g_i=(1-m_i^2)H_i.
\]
This is a signed trial on the actual one-sided support. Since $Q^{1/2}H=cj$, the first cost at source $cj-bq_0$ is
\[
 \|Q^{1/2}g-(cj-bq_0)\|^2
 \le 2\sum_{i\ne0}m_i^4 H_i^2 .
\]
The activation penalty is exactly $\sum_i 2m_i^2(1-m_i^2)H_i^2$, with zero terms off $I_\sigma$. Therefore
\[
 \|G^{1/2}(cj-bq_0)\|^2\le 2\mathcal L_\sigma(H).
 \tag{1}
\]
In particular, $H=A$ pays at most $(n-1)\nu^2\le\tau$ before the factor 2, regardless of its norm or peak heights.

There is also a converse within a factor of two. For general ports $c,b$, put
\[
 F_\sigma(c,b)=\inf_{H\in U_\sigma,\,\langle j,H\rangle=c}
                  \big[(H_0-b)^2+\mathcal L_\sigma(H)\big].
\]
Then
\[
 F_\sigma(c,b)\le \|G^{1/2}(cj-bq_0)\|^2\le 2F_\sigma(c,b).
 \tag{2}
\]
Indeed $Q$ lies between the orthogonal projection onto $E_\sigma^\perp$ and twice that projection. In the extension minimum, replace the first cost by $\inf_H\|g-H+be_0\|^2$, or twice this quantity, for the lower or upper bound. This infimum has exactly the constraint $\langle j,H\rangle=c$ in (2). At an active site with penalty $\mathcal R_i^{-1}g_i^2$, minimization in $g_i$ yields the weight $1/(1+\mathcal R_i)=2m_i^2/(1+m_i^2)\ge m_i^2$ for the lower bound. For the upper bound the minimizer is $g_i=(1-m_i^2)H_i$ and the weight is $2m_i^2$. At inactive sites $g_i=0$, and the weights are 1 and 2. This proves (2), in particular for $c=b=1$ in (4a).

## A finite-depth trial on the smaller-mark side

Use the actual stationary pair only for the weights $m_i$. To make $H$, start the averaged iteration at $z_0=0$, set $u_t=\Phi(z_t)$ and $z_{t+1}=(z_t+Ku_t)/2$, and write $\bar u_T=T^{-1}\sum_{t<T}u_t$ and $\bar z_T=T^{-1}\sum_{t<T}z_t$. Define
\[
 H_{\sigma,T}=\tfrac12(\bar u_T+\sigma K\bar u_T)
             =\tfrac12(\bar u_T+\sigma\bar z_T)+\sigma z_T/T.
 \tag{3}
\]
The second identity is the iteration telescope. The first gives exact membership in $U_\sigma$ without a projection error in the leakage. The mean $c_T=\langle j,\bar u_T\rangle/2$ is independent of sign. The [averaged norm identity](iteration-parity.md#a-criterion-involving-only-the-iterates) gives $0<c_T\le\sqrt W$. The mark $b_{\sigma,T}=H_{\sigma,T,0}$ tends to 1 for each fixed $\tau,T$ in the field-first limit: each of the finitely many $z_{t,0}$, including $z_{T,0}$, tends to zero by the existing [fixed-depth estimate](uniform-fixed-depth.md#applying-the-algebra-to-smoothing). For a moving schedule the argument below uses the actual $b_{\sigma,T}$; fixed-depth estimates give no uniform convergence rate in $T$ or $\tau$.

Let $D_\sigma=\|G^{1/2}q_0\|^2$. Combining (1) for $H=H_{\sigma,T}$ and $H=A$ gives
\[
 |\sqrt W b_{\sigma,T}-a c_T|\sqrt{D_\sigma}
 \le \sqrt{2W\,\mathcal L_\sigma(H_{\sigma,T})}+c_T\sqrt{2\tau}.
 \tag{4}
\]
This follows by taking $\sqrt W(c_Tj-b_{\sigma,T}q_0)-c_T(\sqrt Wj-aq_0)$. Choose $\sigma$ with $a_\sigma\le1$ (ties arbitrary). Since $a\ge0$ and $c_T\le\sqrt W$, (4) implies
\[
 1-a\le |1-b_{\sigma,T}|+
             2\sqrt{\frac{\mathcal L_\sigma(H_{\sigma,T})+\tau}{D_\sigma}} .
 \tag{5}
\]
Consequently, at decreasing floors through primes, it suffices that $b_{\sigma,T}=1+o(1)$ and $\mathcal L_\sigma(H_{\sigma,T})+\tau=o(D_\sigma)$ on the smaller-mark side. The mark product and the [stationary theta bracket](smoothing.md#fixed-point-and-a-sufficient-residual-estimate) then yield the conjectured limit. One may test both signs to avoid choosing a sign in advance. These conditions also imply $c_T\to1$ by (4). Using $\|G^{1/2}j\|\le (a\sqrt{D_\sigma}+\sqrt{2\tau})/\sqrt W$ from (1) for $A$, the trial at ports $(c_T,b_{\sigma,T})$ then gives $N_\sigma=o(D_\sigma)$ at ports $(1,1)$ by the triangle inequality in the $G$ norm.

An alternative order of limits is to find a sequence of fixed pairs $(\tau_k,T_k)$, $\tau_k\downarrow0$, for which the prime limsup of $(\mathcal L_\sigma+\tau_k)/D_\sigma$ tends to zero as $k\to\infty$. At each pair the premise on the trial mark follows from fixed-depth cancellation, even if the smaller-mark side varies with the prime. This formulation needs no uniform rate for that cancellation. It still needs a new overlap estimate.

The extra input can be formulated as a scalar capped overlap. For $X_i=\sqrt n|H_{\sigma,T,i}|$ and $Y_i=\sqrt n A_i$ on the bulk it is
\[
 \mathcal L_\sigma(H_{\sigma,T})
 =\frac1n\sum_{i\ne0}X_i^2\min(1,\tau/Y_i^2).
\]
For cutoffs $M,s>0$ an upper bound is
\[
 \frac1n\sum_{X_i>M}X_i^2+
 \frac1n\sum_{X_i\le M,\,Y_i<s}X_i^2+
 \frac{\tau}{s^2 n}\sum_{X_i\le M,\,Y_i\ge s}X_i^2 .
 \tag{6}
\]
For example, if $\|B\|_2$ and $\|H_{\sigma,T}\|_2$ are bounded, the denominator is separated from zero by (7) below. One may take $s\gg\sqrt\tau$ and prove that the first two terms of (6) vanish for a choice of $M$. Only the trial's squared mass at low **same-sign** stationary heights is counted in the second term; small density of large true heights gives no such estimate. This differs from [capping the hyperbolic discrepancy](parallel-finite-time-6.md#capping-the-discrepancy-before-taking-the-time-average), which seeks diagonal convergence. The leakage allows the true spectrum to be much larger than the trial. It uses neither cancellation between signed time tails nor a bounded stationary norm for the finite inequality (5).

## Opposite-sector tests with the same weights

On $U_{-\sigma}=\operatorname{ran}Q$, the dual energy in [the marked lower bound](stationary-mark-constant.md#a-scalar-criterion-and-its-denominator) simplifies to
\[
 \|Q^{-1/2}\ell\|^2+\sum_i\mathcal R_i\ell_i^2
 =\tfrac12\left(|\langle j,\ell\rangle|^2+
                         \sum_i m_i^{-2}\ell_i^2\right).
\]
The dual formula for $D_\sigma$ is the supremum of $\ell_0^2$ divided by this energy over nonzero $\ell\in U_{-\sigma}$. Taking $\ell=B$ now gives the explicit bound
\[
 D_\sigma\ge
 \frac{2(a')^2}{W+(a')^2+\sum_{i\ne0}\max(B_i^2,\nu^2)}.
 \tag{7}
\]
On the active set $B_i/m_i=\nu$ even when the same-sign activation is arbitrarily close to one. Thus (5) has a solve-free sufficient version: $b_{\sigma,T}\to1$ and $(1+\|B\|^2)(\mathcal L_\sigma(H_{\sigma,T})+\tau)\to0$ on the smaller-mark side, where $a'\ge1$. The actual $D_\sigma$ can give a better denominator.

For a one-sided theta bound alone there is a different test, also with no inverse solve. Fourier orthogonality gives $\langle H_{\sigma,T},B\rangle=c_T\sqrt W$. Hence
\[
 b_{\sigma,T} a'\le W+
     \sum_{i\ne0} B_i(H_{\sigma,T,i})_- .
 \tag{8}
\]
The sum tests only the *negative entries after projection*, since the unprojected average $\bar A_{\sigma,T}=(\bar u_T+\sigma\bar z_T)/2$ in (3) is positive. Explicitly the negative part is $(-\sigma z_{T,i}/T-\bar A_{\sigma,T,i})_+$. This uses the same projected iterate as [the Fourier majorant repair](iterate-majorants.md#a-feasible-theta-row-obtained-from-the-same-repair), with the remaining negative part paired against the actual opposite spectrum. The sum is at most
$\sqrt{\mathcal L_\sigma((H_{\sigma,T})_-)}
 (\sum_{i\ne0}\max(B_i^2,\nu^2))^{1/2}$.
Here $\mathcal L_\sigma$ means the same bulk quadratic sum, with no sector restriction needed for the bound. Vanishing of the sum in (8) and $b_{\sigma,T}\to1$ give the same limit when applied to the smaller-mark side, even if the positive leakage is large. The sum can also be capped on the true opposite spectrum: the part on $\sqrt n B_i\le M$ is at most $M\|(H_{\sigma,T})_-\|_2\le M\sqrt{2W/T}$, by (3) and the averaged norm bound. Thus for $T\to\infty$ it is enough to choose $M=o(\sqrt T)$ and bound the negative pairing on the uncapped opposite peaks. This estimate is separate from the signed drift, which pairs the whole time endpoint against $B$.

## Square obstruction and finite checks

In the [exact square-order limit](stationary-mark-constant.md#exact-square-field-limits) with decreasing floors, $a_-\to1/\sqrt2$. On any such schedule with $b_{-,T}\to1$, (4)–(5) give
\[
 \liminf \frac{\mathcal L_-(H_{-,T})+\tau}{D_-}
 \ge \tfrac14(1-1/\sqrt2)^2 .
\]
This uses the known stationary square limit and does not presume a rate for $D_-\to0$. Similarly (8) forces the negative-entry pairing to have liminf at least $\sqrt2-1$ on such a schedule. Small absolute leakage is therefore insufficient, and taking the depth large enough to follow the square stationary mark can instead invalidate the premise on $b_{-,T}$.

I checked (1), (4) and (7) at $\tau=0.0005$ on both signs at $q=9413,37253,97^2,193^2$, at depths 128 and 512. The replay uses [weighted_iterate](../poisson_weights.py) for the stationary pair, then $u_t=\operatorname{hypot}(z_t,2\sqrt w)$ and [kernel_action](../smoothing.py) for (3). For stability the smaller stationary entry at each site is computed from its reciprocal product. The full one-sign defect uses CG as in [stationary_mark_constant.py](../stationary_mark_constant.py), at exponent 1. The largest stationary and CG residuals were $1.0\cdot10^{-10}$ and $9.8\cdot10^{-13}$; the sector identity in (3) and complementary pairing in (8) agreed to $2.0\cdot10^{-15}$ and $1.6\cdot10^{-12}$. The following rows are for the smaller-mark side:

| Order | Sign | Depth | Trial mark $b_{\sigma,T}$ | $D_\sigma$ | Leakage $\mathcal L_\sigma(H_{\sigma,T})$ | $(\mathcal L_\sigma+\tau)/D_\sigma$ |
|---:|:---:|---:|---:|---:|---:|---:|
| $9413$ | $-$ | 128 | 0.999370 | 0.427917 | 0.001445 | 0.004545 |
| $9413$ | $-$ | 512 | 0.999511 | 0.427917 | 0.000376 | 0.002047 |
| $37253$ | $+$ | 128 | 0.999640 | 0.426593 | 0.001276 | 0.004162 |
| $37253$ | $+$ | 512 | 0.999599 | 0.426593 | 0.000347 | 0.001986 |
| $97^2$ | $-$ | 128 | 0.947678 | 0.045601 | 0.002006 | 0.054953 |
| $97^2$ | $-$ | 512 | 0.808834 | 0.045601 | 0.000736 | 0.027110 |
| $193^2$ | $-$ | 128 | 0.976115 | 0.026019 | 0.001287 | 0.068687 |
| $193^2$ | $-$ | 512 | 0.895210 | 0.026019 | 0.000969 | 0.056466 |

An independent dense check of (2) at $q=13,41,73$ used 48 prescribed cap and source pairs. The ratio of the $G$ form to $F_\sigma$ ranged from 1.05724 to 1.99982. These checks are floating-point diagnostics. The cap, dual energy and finite inequalities are proved for the exact stationary pair. No estimate here makes the required leakage ratio or the negative-entry pairing vanish through all primes. Bounded opposite norm in the example after (6) is also a hypothesis.
