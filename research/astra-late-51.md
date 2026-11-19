# What the opposite endpoint can supply on an unshared cold history

Cover a site of the larger optimum by the **sum of both endpoint densities at its antipodal partner**. A fixed fraction of late signal covered in this way has a cost even if the opposite endpoint has arbitrarily high collision. On a supercritical subsequence with polynomial collision on the larger side, it forces a positive order-window signed mean of the opposite endpoint at a positive fraction of the following times. This also forces order-window directional collision on the smaller-theta side. At all odd prime squares of characteristic at least five the gain from adding the opposite density is at most order inverse square root of the field size, for every matching and even for arbitrarily chosen signal. This order is sharp over unrestricted matchings.

## An exact identity for the extra coverage

Use the actual cold history and the [round-50 notation](astra-coupling-50.md). Write $X,\bar X$ for the two least-norm positive endpoints normalized to sum $\sqrt n$, with larger sign $\sigma$, marks $\alpha\ge1$ and $\beta=1/\alpha$, and densities $\rho=\sqrt n X$, $\bar\rho=\sqrt n\bar X$. Set $r^2=E\rho^2$, $\bar r^2=E\bar\rho^2$. At $z_t=\sigma Y_t$ the signed means of the two rows are $m_t=E\rho z_t$ and $\bar m_t=-E\bar\rho z_t$; absolute means are $a_t=E\rho|z_t|$ and $\bar a_t=E\bar\rho|z_t|$. All unpaired expectations are uniform. With $b_t$ the true marked injection and $g_t=\langle j,\phi_t\rangle/2$, the exact sector equations give
\[
 m_{t+1}=a_t+\alpha b_t-2g_t,\qquad
 \bar m_{t+1}=\bar a_t+\beta b_t-2g_t.                    \tag{1}
\]
Indeed $\sigma KX=X-j$ and $-\sigma K\bar X=\bar X-j$. These identities apply to every step, including zero.

For a symmetric uniform-marginal plan $P$, let $C_t=E_P[\min(\rho_i,\rho_j)|z_t(i)|]/a_t$ as in round 50, assuming $a_t>0$. Let $U_t$ use $\min(\rho_i,\rho_j+\bar\rho_j)$ instead. Define
\[
 k_{ij}=\min((\rho_i-\rho_j)_+,\bar\rho_j),\qquad
 e_t=E_P k_{ij}|z_t(i)+z_t(j)|.
\]
The fresh coverage is $(U_t-C_t)a_t=E_P k_{ij}|z_t(i)|$. Put $R_t=E_P[(\bar\rho_j-k_{ij})|z_t(j)|]\ge0$ and $J_t=E_P k_{ij}(|z_t(j)|-|z_t(i)|)$. Then
\[
 \boxed{\quad\bar m_{t+1}=(U_t-C_t)a_t+R_t+J_t+\beta b_t-2g_t,
 \qquad |J_t|\le e_t\le r\epsilon(P).\quad}                    \tag{2}
\]
This is just the second marginal in (1). The last bound uses $k_{ij}\le\rho_i$ and the RMS cost of the full true histories. It requires **no bound on the collision of the opposite endpoint**. At unrestricted larger collision one can still retain the actual $e_t$ or signed $J_t$.

Take $s=\lfloor D/2\rfloor$, $L=D-s$. On a fixed supercritical subsequence $\alpha\ge1+\delta$ the full applicable lower bound on $a_t$ is
\[
 a_t\ge m_t=2t(\alpha-1)-\alpha B_t+E_t/4+A_t+H_t .
\]
Here $E_t=E Y_t^2$ and $A_t,H_t$ are the exact squared-mean and larger-side wrong-sign occupation reserves. Throughout the late half this is $\gg_\delta D$. At polynomial larger collision $r=O(D^k)$ choose the round-49 arithmetic budget with $r\epsilon(P)=o(1)$. Round 50 gives $L^{-1}\sum C_t=O_{\delta,k}(\log D/D)$ for every symmetric plan there. From (2),
\[
 \frac1L\sum_{s\le t<D} U_t
 \ll_{\delta,k} \frac{\log D}{D}
       +\frac{1}{DL}\sum_{s\le t<D}(\bar m_{t+1})_+ .             \tag{3}
\]
The norm telescope gives $\sum_{t<D}g_t^2=D-E_D/4\le D$, so the late mean of $2g_t$ is $O(1)$. At individual times $2g_t=O(\sqrt D)$. If the left side of (3) is at least $\eta>0$, a positive fraction of times have $U_t\ge\eta/2$ since $0\le U_t\le1$. Outside $O_{\eta,\delta,k}(\log D)$ exceptions these have $C_t\le\eta/4$, forcing $\bar m_{t+1}\gg_{\eta,\delta}D$ by (2). Each such time $u=t+1$ consequently has
\[
 \bar H_u+A_u+E_u/4=\bar m_u+2(1-\beta)u+\beta B_u .
\]
All signs and the terminal energy are exact. This charges the sum of the reserves; it need not force the wrong-sign occupation alone. At each of these times the opposite directional collision $[\bar m_u]_+^2/\|P_{-\sigma}v_u\|^2\gg D$ since $E_u\le4D$. Its upper bound is $\bar r^2-1$ by sector Cauchy–Schwarz.

In particular, if $\bar r=o(\sqrt D)$, or just the last term of (3) tends to zero, every cheap symmetric plan has vanishing average $U_t$. Choose a uniform late time and then a pair with law $\rho_i|Y_t(i)|P(i,j)/a_t$. The probability that the partner has $\rho_j+\bar\rho_j\ge\lambda\rho_i$ tends to zero for every fixed $\lambda>0$, by Markov's inequality applied to the coverage fraction. This describes the **relative density** missing from the partners and remains meaningful on faces having no common bulk zero.

## A square obstruction of sharp order

At $q=h^2$, $n=(h^2-1)/2$ for an odd prime $h\ge5$, use the [actual least-norm pair](square-endpoint-uniqueness.md). The larger density is $\rho=(h-1)\mathbf1_H$ on the subfield annihilator. The opposite density equals $1+(h-1)(P_-e_0)_j$. As $(P_-e_0)_j=(-1/n-K_{j0})/2$ at $j\ne0$, the Jacobi bound $|K_{j0}|\le h/n$ gives $\bar\rho_j\le 2h/(h+1)$ off the mark. Fresh coverage vanishes for $j\in H$ because $\rho_j$ is already maximal there. Thus at every active source $k_{ij}/\rho_i\le 2h/(h^2-1)$, independently of $P$. **Every symmetric plan** and every test signal with $a_t>0$ satisfy
\[
 0\le U_t-C_t\le\frac{2h}{h^2-1}.                              \tag{4}
\]
For the independent uniform plan, $k_{ij}=\bar\rho_j$ when $i\in H$, $j\notin H$. Opposite mass in $H$ is entirely at zero by complementarity; $\bar\rho_0/n=1/(h-1)$. Hence $U_t-C_t=(h-2)/(h-1)^2$ exactly, for any signal of positive denominator. This establishes the order of the unrestricted envelope. The independent plan need not meet the arithmetic cost budget. The square larger collision lies outside the polynomial-window regime, while (4) itself has no collision premise.

There is a corresponding finite prime rejection test independent of the cost. Let $M=\max_{j\ne0}\bar\rho_j$. Since translations preserve feasibility, $\rho_i\le\rho_0$ and $k_{i0}=0$. Thus
\[
 U_t-C_t\le \frac{E[\min(\rho_i,M)|Y_t(i)|]}{a_t}.              \tag{5}
\]
If the signal sits above the bulk scale of the opposite row, (5) limits every plan simultaneously. The sharp square order follows from precisely this density separation. A prime-uniform bound on the distribution in (5) is open.

## A complementary test at arbitrarily high collision

Let $Q$ be any coupling of the endpoint probabilities $\rho/n$ and $\bar\rho/n$; its marginals here differ from those of $P$. Set $W_t(Q)=E_Q|z_t(i)+z_t(j)|$. Subtracting the equations (1) and using the two marginals gives, for each $t$,
\[
 b_t(\alpha-\beta)\le W_{t+1}(Q)+W_t(Q).
\]
More generally one can take the two separate minima independently, since the two scalar mean differences are bounded using only their respective marginals. Each minimum is the one-dimensional Wasserstein distance between the law of $z_t$ under the larger endpoint and the law of $-z_t$ under its complement. Matching their increasing quantiles attains it. This constraint on *absolute* error persists at every adjacent pair of late times if $\alpha$ has fixed excess, even when larger-side same-density matching sees negligible signal. At marked times $b_t=2-o(1)$ uniformly by the round-38 marked loss. A small relative error on an order-$D$ signal does not prove the requisite absolute estimate.

The [320-bit replay](astra-late-51-check.py) checks (1), the exact opposite reserve identity, and the fresh-coverage lower bound with its measured matching error for the existing depth-eight true-history assignment. It also encloses the two marginal Wasserstein distances using the integral of the absolute CDF difference on rounded dyadic sites, adding the two mean site-rounding errors. All 24 late pairs strictly exceed the lower bound. At the squares it additionally checks the universal cap and the independent-plan value. Means over times 2–7, rounded to five places, follow.

| Order | Same-side coverage $C$ | Two-endpoint coverage $U$ | Next opposite signed mean |
|---:|---:|---:|---:|
| 101 | 0.00081 | 0.69276 | 1.33236 |
| 173 | 0.00856 | 0.68482 | 2.21794 |
| 121 (square) | 0.00000 | 0.16996 | 1.03670 |
| 961 (square) | 0.00000 | 0.06296 | 1.25232 |

These are fixed-field comparisons. Replay the [four records](astra-late-51-checks.jsonl) with `.venv/bin/python -B research/astra-late-51-check.py`.

1. At polynomial larger collision, maximize late average $U$ on cheap symmetric plans and test whether the opposite positive means at the following times average $o(D)$. A fixed positive maximum together with that mean bound rules out fixed mark excess. If the plan-independent cap (5) and the optimized $C$ both vanish on an unbounded prime subsequence, the proposed positive union-coverage estimate fails.
2. On unrestricted endpoint collisions, minimize the cross-endpoint scalar Wasserstein distances independently at each time. One adjacent late pair with summed minimum $o(1)$ on every prime suffices. A subsequence with a common positive lower bound for every adjacent late pair refutes this transfer estimate. A single fixed-depth success or failure does not decide either limit.
