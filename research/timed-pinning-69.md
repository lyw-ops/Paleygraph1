# Pinning an arbitrary weighted average on the actual cold trajectory

The zero-floor projected proposals admit a single small-variable linear program for choosing their time weights and completing both marks by the canonical mean direction. The time weights can be placed anywhere in the proved marked window. The test retains the actual signed difference between the two ends of a delayed interval. Its dual either certifies that some time mixture passes or exhibits a finite collection of sites obstructing every such mixture at the stipulated allowance.

## An exact signed difference for arbitrary time weights

Use \(n=(p-1)/2\), \(K^2=I-J\) and \(P_s=(I-J+sK)/2\), with \(J\) the constant projector, \(s\in\{-1,1\}\), and \(p>5\). The actual cold trajectory is \(v_{j+1}=K\phi_j\), where the bulk activation is \(\phi_j(i)=|v_j(i)|\) and the marked activation is \(\phi_j(0)=\sqrt{4+v_j(0)^2}\). Write \(g_j=\sqrt n\,\overline{\phi_j}/2\), \(Y_j=\sqrt n v_j\), and define the scaled positive raw row and the exact projected row by
\[
 B_{s,j}=\frac{\sqrt n}{2}(\phi_j+s v_j),\qquad Z_{s,j}=(J+P_s)B_{s,j}.
\]
They have mean \(g_j\). The exact identity is
\[
 Z_{s,j}=B_{s,j}+\frac s2 P_{-s}(Y_{j+1}-Y_j).
 \tag{1}
\]
Indeed \(P_{-s}\phi_j=-sP_{-s}v_{j+1}\). Thus for a convex time weight \(\omega\) on any finite set of times \(\mathcal I\), its projection defect is \(sP_{-s}\sum_{j\in\mathcal I}\omega_j(Y_{j+1}-Y_j)/2\). For a flat average on \([a,b]\) of length \(d=b-a+1\), it is exactly \(sP_{-s}(Y_{b+1}-Y_a)/(2d)\). These formulas keep the signed difference at each site, including overlap of peak sets from the two endpoints. [Original projected averages](averaged-mark-35.md) · [Decreasing weights and their absolute bounds](astra-averaged-positive-36.md)

The mean of the delayed flat average satisfies
\[
 \overline g_{[a,b]}^2\le 1+\frac{E_a-E_{b+1}}{4d},\qquad E_j=\|v_j\|_2^2.
 \tag{2}
\]
This follows from Jensen and the exact energy telescope. In particular \(a=o(d)\) gives \(\overline g_{[a,b]}\le1+o(1)\) through primes since \(E_a\le4a\). One can therefore delay the start past any fixed early spike while keeping the leading mean budget, provided the endpoint stays in the marked window and the interval grows. For example set \(a=3,b=L\), so (1) compares \(Y_{L+1}\) to \(Y_3\). A vanishing allowance suffices if the negative part of the signed projection defect, after the accumulated positive raw row, is uniformly \(o(1)\) on the bulk. Equation (2) does not supply that signed bound. [Prime marked window and energy budget](vanishing-floor-38.md)

## Exact allowance and a sparse dual test

Let \(b_s=\mathbf1-P_s e_0/(P_s)_{00}\). It lies in \(\mathbb R\mathbf1+V_s\), has mean one, vanishes at the mark and equals \(1+O(p^{-1/2})\) uniformly off it, by the Jacobi bound. Work at sufficiently large primes so all its bulk values are positive. Put \(m_{s,j}=Z_{s,j}(0)/\sqrt n\). Let \(D=D(p)\) be the proved marked depth and \(L=\lceil D/2\rceil\). For positive times \(1\le j\le D\), the mark factors are \(1+o(1)\) uniformly by the single-time marked identities and cancellation through \(j+1\le D+1\). At time zero the exact mark is \((J+P_s)_{00}\), which is also positive. For a time set with positive marks and a target \(\epsilon\ge0\), set
\[
 A_{s,i,j}(\epsilon)=Z_{s,j}(i)/b_s(i)+(1+\epsilon)m_{s,j}-g_j
 \quad(i\ne0).
\]
Define
\[
 \mathcal B(\epsilon)=\max_{\omega\in\Delta(\mathcal I)}\min_{s,i\ne0}
                  \sum_{j\in\mathcal I}\omega_j A_{s,i,j}(\epsilon).
 \tag{3}
\]
It is a linear program in the time weights and one scalar. In (3), \(\mathcal B(\epsilon)\ge0\) is exactly feasibility for this mixture and the canonical mean directions at the mean limit imposed by the stipulated normalized marks. Indeed take \(Z_{s,\omega}=\sum_j\omega_j Z_{s,j}\), \(m_{s,\omega}=\sum_j\omega_jm_{s,j}\) and \(G=\sum_j\omega_jg_j\). The repaired row is
\[
 R_s=Z_{s,\omega}+\big[(1+\epsilon)m_{s,\omega}-G\big]b_s.
\]
It is nonnegative on the bulk precisely when every constraint of (3) for this \(s\) holds; its root is already positive. This formulation also permits lowering a mean if the resulting row remains nonnegative. Each row has normalized mark \(1/(1+\epsilon)\) after division by its mean. Conversely any repair in the same direction with mean at most \((1+\epsilon)m_{s,\omega}\) implies this particular repair is nonnegative, since \(b_s\ge0\). Complementary reciprocity gives the exact interval
\[
 (1+\epsilon)^{-1}\le \vartheta(\overline H_p)/\sqrt n\le 1+\epsilon.
 \tag{4}
\]
Thus a vanishing allowance solving (3) through all primes would establish the problem with the exact marks and means, without an auxiliary root or slope comparison.

Finite minimax gives the exact dual
\[
 \mathcal B(\epsilon)=\min_{\nu\in\Delta(\{(s,i):i\ne0\})}
                         \max_{j\in\mathcal I}\sum_{s,i}\nu_{s,i} A_{s,i,j}(\epsilon).
 \tag{5}
\]
There is a minimizing \(\nu\) supported on at most \(|\mathcal I|\) signed sites. Take an optimal vertex of the dual epigraph, using a finite slack interval for the epigraph variable with endpoints strictly outside all matrix entries. If the support has size \(r\), the coordinates on it and the epigraph variable have \(r+1\) variables. The sum equation and the at most \(|\mathcal I|\) time inequalities must span them at a vertex, so \(r\le |\mathcal I|\). The slack endpoints are inactive at an optimum. This proves that a fixed short list of signed sites suffices to obstruct every time mixture, including when the obstruction is not an actual Fourier-feasible optimizer.

The same proof applies to any \(k\) preassigned weight profiles on the whole time window. Replace the time columns by their \(k\) weighted averages and test convex mixtures of the profiles. Feasibility for every selection of at most \(k\) signed sites, with the mixture allowed to depend on that selection, now implies one mixture feasible at all sites. For two profiles, write their two entries at each signed site as \(B_i,C_i\), with \(i\) here indexing signed sites. A mixture with coefficient \(u\) on the second profile needs \(u\ge-B_i/(C_i-B_i)\) when \(B_i<0\le C_i\), and \(u\le B_i/(B_i-C_i)\) when \(C_i<0\le B_i\). It fails precisely if a site has both entries negative or two sites give incompatible lower and upper endpoints. This tests two peak sites at a time even though each column uses a growing number of actual iterates.

For a known probability \(q\) on the opposite sector \(-s\), the weights \(\nu_{s,i}=q_i b_s(i)\) on that single sign are a dual probability because \(q\) is orthogonal to \(P_s e_0\). At each time its payoff is exactly
\[
 \sum_{i\ne0}\nu_{s,i}A_{s,i,j}(\epsilon)
  =m_{s,j}(1+\epsilon-\sqrt n\,q_0).
 \tag{6}
\]
In fact \(\sum_iq_iZ_{s,j}(i)=g_j\) by opposite-sector orthogonality. Thus a supercritical true optimum obstructs (3) for every time mixture below its gap \(\sqrt n q_0-1\). In the square control the explicit plus probability already rejects every allowance below \(\sqrt{2(r-1)/(r+1)}-1\), at order \(r^2\) with positive mark factors. The dual also permits signed-site tests without the Fourier equations, so a prime failure of (3) alone would reject this completion rule. [Square control](square-order-control.md)

## Two finite prime comparisons

At depth \(128\), use the same exact weights \(\omega_j\propto j^6(129-j)\) on both signs. On the actual zero-floor trajectory at \(p=9413\) and \(p=153649\), Arb128 certifies both repaired rows at \(\epsilon=1/200\). Over both signs the respective bulk minima exceed \(0.00149837\) and \(0.0000324843\). Flat weights on times 1 through 128 fail even at \(\epsilon=1/100\) on both primes. One strictly negative bulk entry is enough for the failure, since the fixed-direction repair increases pointwise with \(\epsilon\). Formula (4) gives the finite theta interval \([200/201,201/200]\) at each prime. This check uses a fixed weight formula selected after floating exploration, and asserts no optimality of that formula.

For replay, put \(w_0=w_{129}=0\) and \(W_w=\sum_j w_j\) for the integer weights. The exact scaled row used in the checker is
\[
 Z_{s,\omega}=\frac{\sqrt n}{4W_w}
 \left[(I+sK)\sum_{j=0}^{128}(w_j+w_{j+1})\phi_j
            +\sum_{j=0}^{128}(w_j-w_{j+1})\overline{\phi_j}\,\mathbf1\right].
\]
The interval computation uses the same Euclidean shadowing of the unrounded trajectory as round 63, enclosing the local defect at each rational center. The \(I+sK\) term costs at most twice the accumulated source norm error, while the constant part uses the sharper mean bound from Cauchy--Schwarz. Both checker runs produced identical records. [Checker](timed-pinning-69-check.py) · [Interval records](timed-pinning-69-checks.jsonl) · [Original shadowing](true-spill-63.md#norm-shadowing-of-the-unrounded-input)

## Ranked tests

1. In the actual late prime window establish \(\mathcal B(\epsilon_p)\ge0\) for some \(\epsilon_p\to0\). For delayed flat weights, test the signed projected difference in (1) against the raw positive average at each site and retain the precise energy term in (2). A prime-uniform feasible bound proves (4).
2. On the measured early peak patches test the dual against all eligible time columns at matching marked depth. A negative dual margin at fixed positive \(\epsilon\) along unbounded primes rejects this canonical repair for every time mixture tested. A fixed early peak that disappears from the joint inequality does not reject the rule.
