# A supercritical row must lose weighted antipodal cancellation at almost every late time

A positive fraction of the endpoint-weighted absolute signal cancelling at a positive fraction of late times forces *exponential* growth of the terminal signed mean if the ordinary mark stays supercritical. This applies even if the matching is chosen afresh to maximize cancellation at each time. Consequently, at polynomial collision, a supercritical actual optimum must put asymptotically all of its absolute signal on **unshared endpoint weight** under every cheap round-49 whole-history matching, on average throughout a late window. No bound on the RMS density imbalance or assumption on its support is needed for this conclusion. The implication holds on both primes and eligible squares. The prime input needed to contradict it remains open.

## An exact multiplicative budget

Use the [actual undamped cold path](endpoint-direction-45.md), write $\rho_i=n\mu_i$ for a positive sector probability, $\alpha=\sqrt n\mu_0$, $\delta=\alpha-1$, and $r^2=E\rho^2$. Expectations without a plan are uniform on the cyclic indices. At each time define
\[
 w_{ti}=\rho_i\sigma Y_t(i),\quad m_t=Ew_t,\quad a_t=E|w_t|,
 \quad H_t=\sum_{u<t}(a_u-m_u).
\]
The [exact time identity](astra-critical-44.md) is
\[
 m_t=H_t+F_t,\qquad F_t=2\delta t-\alpha B_t+E_t/4+A_t,
 \qquad E_t=E Y_t^2\le4t .
\]
Here $B_t$ is the true cumulative marked loss and $A_t$ is the nonnegative squared-mean reserve.

For any uniform-marginal plan $P_t$, put $d_t=E_{P_t}|w_{ti}+w_{tj}|/(2a_t)$ when $a_t>0$. Thus $1-d_t$ is the fraction of absolute endpoint signal cancelled on paired indices. The plan may depend on the sign, endpoint, time and complete true trajectory. It need not be symmetric. On any integer interval $s\le t\le T$ take $c\le\min_{s\le t\le T}F_t$ with $L_s=c+H_s>0$. Then all $m_t\ge L_t=c+H_t>0$, $0<d_t\le1$, and
\[
 \boxed{\quad
 \sum_{t=s}^{T-1}-\log d_t
 \ \le\ \log\frac{c+H_T}{c+H_s}
 \ \le\ \log\frac{m_T}{c+H_s} .\quad}                            \tag{1}
\]
Indeed $d_t a_t\ge m_t$ by the two marginals and the triangle inequality. Hence
$H_{t+1}-H_t=a_t-m_t\ge(d_t^{-1}-1)m_t\ge(d_t^{-1}-1)L_t$.
Multiplication of $L_{t+1}\ge L_t/d_t$ proves (1). This retains the exact energy in $F_t$ when checking finite intervals. The weaker choice $c=2\delta s-\alpha B_T$ is valid for $\delta\ge0$.

Take $T=D$ in the proved marked window, $s=\lfloor D/2\rfloor$, and suppose $\delta\ge\delta_0>0$. Then $c+H_s\gg_{\delta_0} D$ and $m_T\le2r\sqrt D$. At most
\[
 \frac{\log(2r\sqrt D/(2\delta s-\alpha B_D))}{-\log(1-\eta)}
                                                                    \tag{2}
\]
of these times can have cancellation fraction at least $\eta$, for $0<\eta<1$. A fixed fraction of times with a fixed cancellation fraction therefore forces $m_D/D$ and $r/\sqrt D$ to grow exponentially in $D$. Under $\log^+(m_D/D)=o(D)$, the mean cancellation fraction tends to zero, uniformly over *all* choices of $P_t$, since $1-d_t\le-\log d_t$. A sufficient premise is $\log r=o(D)$. In particular at polynomial collision the exceptional-time count for fixed $\eta$ is $O_{\delta_0,\eta}(\log D)$. A family where (2) rules out cancellation at almost every time may still admit effective cancellation at selected times. The budget is conditional on a fixed supercritical mark, without requiring a subgroup or other description of a bad endpoint.

## Where a common low-cost plan loses its weight

For the same whole-history plan $P$ at all depths, set $u=Y_t(i)$, $v=Y_t(j)$, $b=\min(\rho_i,\rho_j)$ and define
\[
 C_t(P)=\frac{E_P[b(|u|+|v|)]}{2a_t},\qquad
 J_t(P)=\frac{E_P[b|u+v|]}{2a_t}.
\]
The first number is the fraction of absolute endpoint signal covered by density common to both indices. The second is the actual unsigned matching error on just this common weight. For every such plan,
\[
 0\le C_t-J_t\le1-d_t.
                                                                    \tag{3}
\]
Indeed the numerator of $a_t(1-d_t)$ is the expectation of $\min(\rho_i|u|,\rho_j|v|)\mathbf1_{uv<0}$. This dominates $E_P[b\min(|u|,|v|)\mathbf1_{uv<0}]=a_t(C_t-J_t)$. Dividing by $a_t$ proves the claim. Also $J_t\le\|b\|_{2,P}\epsilon(P)/(2a_t)$ for the [round-49 true-history RMS budget](astra-drift-49.md).

On a supercritical subsequence $a_t\ge m_t\gg_{\delta_0}D$ throughout the late half. Therefore at polynomial collision $r=O(D^k)$, choose the marked window constant so that the round-49 arithmetic plan has cost $O(D^{-k-2})$. For **every** plan at that budget, $J_t=o(1)$ uniformly, since $\|b\|_{2,P}\le r$. Equations (1) and (3) now give
\[
 \frac1{D-s}\sum_{t=s}^{D-1} C_t(P)
 \ll_{\delta_0,k}\frac{\log D}{D}.                                  \tag{4}
\]
In particular the conclusion addresses how *the weighted absolute signal*, rather than just the squared density, is distributed across the very same pairs. Unweighted whole-history matching may be excellent while the density common to the pair sees virtually none of the endpoint signal. At unrestricted collision one may use (1) and (3) with the measured terminal $m_D$ and $J_t$, even if the Cauchy bound on $J_t$ is large. One fully quantitative test is $m_D\exp[-\sum_{t=s}^{D-1}(C_t-J_t)]=o(D)$: it excludes any fixed supercritical mark since $c+H_s\gg D$ and (1) bounds this sum by $\log(m_D/(c+H_s))$. Apply that test on putative supercritical subsequences, on which all denominators are positive.

## Sharp one-time transport checks at actual endpoints

If $w_{(1)}\le\dots\le w_{(n)}$ are the sorted weighted signed samples, the minimum defect over all uniform-marginal plans is
\[
 d_t^{\min}=\frac1{2na_t}\sum_{k=1}^n|w_{(k)}+w_{(n+1-k)}|.
\]
For $a\le b$, $c\le d$, convexity of absolute value gives $|a+c|+|b+d|\ge |a+d|+|b+c|$. Ordering a minimizing permutation reversely therefore attains the minimum, and the assignment LP has a permutation minimizer. Separate minima at each time can be inserted together in (1), even when no single plan attains them all.

The [320-bit checker](astra-coupling-50-check.py) certifies actual least-norm prime endpoints by the round-45 complementary active equations, and uses the [exact square plus endpoints](square-endpoint-uniqueness.md). It checks all six times $2,\ldots,7$ on each depth-eight trajectory. On all 24 field-time pairs every antitone paired sum is certified nonnegative, so $d_t^{\min}=m_t/a_t$ exactly. An unrestricted plan can absorb all available wrong-sign signal in these examples. At prime 101, at each of these times even unrestricted plans cancel less than 0.25 percent of the endpoint signal. At prime 173, at time two some plan cancels over 3.26 percent, while the exhibited common history plan cancels less than 0.33 percent. At square 121 every weighted sample has the endpoint sign throughout these times (zeros allowed), so no plan cancels any positive weight there. These are fixed-field checks, separate from the marked-window limits.

| Field order | Product of inverse minimum defects, times 2–7 | Upper bound from the occupation ratio in (1) |
|---:|---:|---:|
| 101 | 1.00827 | 1.00879 |
| 173 | 1.11646 | 1.12176 |
| 121 (square) | 1 | 1 |
| 961 (square) | 1.00112 | 1.00162 |

The middle numerical column is rounded to the nearest displayed digit, and the last column is rounded upward. The common plan is a permutation proposed by rounded whole-history costs. Optimization is unnecessary for its verified costs. Only the separate sorted formula is claimed to be the exact one-time optimum. Replay the four [records](astra-coupling-50-checks.jsonl) with `.venv/bin/python -B research/astra-coupling-50-check.py`.

1. At polynomial collision, maximize the *late mean common signal* $\sum C_t(P)/(D-s)$ on the true larger-side optimum over uniform-marginal plans at the prescribed whole-history budget. This is a finite linear program (use the squared cost constraint). A uniform fixed positive lower bound through those primes rules out supercriticality by (4). A subsequence on which the maximum tends to zero falsifies that proposed positive-overlap estimate, even if the marks there tend to one.
2. Without a collision bound, use the exact sorted $d_t^{\min}$ and retain $m_D$ on the true endpoint. The quantity $m_D\prod_{s\le t<D}d_t^{\min}/D=o(1)$ whenever $m_t>0$ throughout the late half would exclude fixed excess. A subsequence with these positive means and a fixed positive lower bound for the quantity refutes this sufficient test at that window. An isolated positive prefix or a failed common assignment does not refute it.
