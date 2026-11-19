# An infinite geometric cold window forces high opposite height on the whole negative mask

For an actual selected window of effective length \(d\), every site where \(R_s<-u\) has \(R_{-s}>(2d+1)u\). This is a pointwise statement, including sites of arbitrarily large primary density. The right endpoint jump in the [finite geometric taper](relative-window-77.md#a-geometric-taper-giving-an-exponentially-small-low-height-mask) disappears if the taper continues on the actual cold trajectory. The early end of a one-sided decreasing geometric taper has the favorable sign. Energy controls the distant future for the mean and mark without assuming arithmetic cancellation there.

For a fixed supercritical gap, a fixed positive deficit price must then lie on the intersection of this high-height mask and the [Schur intermediate density band](astra-schur-77.md#a-cap-set-by-the-exterior-clipped-mass). On a shorter marked prefix even a growing set of the most expensive sites may be discarded, with an explicit stretched-exponential deletion budget. The argument gives a necessary geometry for a hypothetical supercritical true primary face. A prime-uniform upper on its surviving interaction remains open.

## The geometric coefficients

Use the zero-floor trajectory and genuine two-sector projections of [round 69](timed-pinning-69.md). Fix \(0<\alpha<1\), \(J=\lfloor D(p)/8\rfloor\), \(d=\lfloor J^\alpha\rfloor\), \(h=1/(d+1)\), \(b=1-h\). For a positive start \(a\), take \(\omega_{a+j}=h b^j\) for \(j\ge0\), and zero at earlier times. These are probabilities with mean delay \(d\). Use counting Euclidean norm for \(v\) and normalized Euclidean norm for \(Y=\sqrt n v\). The round-70 energy estimate gives \(\|Y_j\|_{2,n}\le2\sqrt j\), \(g_j^2\le j+1\). All the weighted rows converge absolutely in these norms, hence also at each coordinate for fixed field. The bulk formula of [round 77](relative-window-77.md#paired-rows-with-a-nonnegative-bulk-constant) passes to the limit by this bound. Its coefficients are
\[
 A_j=(2\omega_j+\omega_{j-1}+\omega_{j+1})/4,\qquad
 B_j=(\omega_{j-1}-\omega_{j+1})/4.
\]
At \(a-1,a\), \(B_j\le0\). At every later time \(B_j/A_j=(1-b)/(1+b)=:\theta=1/(2d+1)\). On every site, therefore, \(B_j\le\theta A_j\), including both early boundary times. Also \(c_\omega=h(G-g_{a-1})/2\), where \(G=\sum\omega_jg_j\).

### Selection and pinning

Write \(L=\lceil\sqrt{dJ}\rceil\), \(\eta=\sqrt{d/J}\). Consider \(1\le a\le J-L\) and use the padded energy
\[
 H_a=\frac{\sum_j\omega_j g_j^2+h g_{a-1}^2}{1+h}.
\]
For \(j\le J\) the weights of all starts sum to at most one after the padding is normalized. The prefix energy identity gives \(\sum_{j=0}^J g_j^2\le J+1\). For each start the remaining future contributes at most \(C(J+d+2)b^L\), since \(g_j^2\le j+1\) and the conditional tail is another shifted geometric variable. As \(b^L\le e^{-L/(d+1)}\) and \(d=\lfloor J^\alpha\rfloor\), this beats every fixed negative power of \(J\). Thus \(\sum_a H_a\le J+1+o(1)\), and at least \(4\eta J\) starts have \(H_a\le1+8\eta\) eventually. One may discard the starts \(a\le\eta J\) and simultaneously require raw bulk overlap \(O(\eta)\). Indeed the [lag budget](paired-windows-70.md#a-common-window-on-the-marked-trajectory) and positivity bound the sum of raw overlaps by
\[
 \sum_{\ell\ge1}\ell\sum_{j\ge0}h^2b^{2j+\ell}
 =\frac{b}{1-b^2}=O(d).
\]
Markov's inequality with a sufficiently large constant leaves at least \(\eta J\) starts.

The one-time mark \(Z_{s,j}(0)/\sqrt n\) is \(1+o(\eta)\) uniformly through \(J\) on these positive times by the inherited prime marked bound. At later times its absolute value is at most \(2\sqrt{j+1}\): projection contracts the counting norm of the raw row, which is at most \(2\sqrt{n(j+1)}\). The future mark tail is \(O(b^L\sqrt{J+d+2})\). The geometric projected marks \(m_s=Z_{s,\omega}(0)/\sqrt n=1+o(\eta)\) follow. On the selected starts \(G^2\le(1+h)H_a\) and \(|c_\omega|=O(\sqrt h)\). Take a common allowance \(\epsilon=C(\eta+\sqrt h)\) with \(C\) a sufficiently large absolute constant. The canonical bulk mean direction \(b_s(i)\) is at least \(1/2\) eventually. The pinned row \(R_s=Z_{s,\omega}+[(1+\epsilon)m_s-G]b_s\) has nonnegative pin increment and
\[
 c_s(i):=c_\omega+[(1+\epsilon)m_s-G]b_s(i)\ge0\qquad(i\ne0).
\]

Write \(u_{s,j}=(sY_j)_+\) on the bulk. There \(R_s=c_s+\sum_j(A_j u_{s,j}-B_j u_{-s,j})\). In \(R_s+\theta R_{-s}\) the two coefficients are \(A_j-\theta B_j\ge0\) and \(\theta A_j-B_j\ge0\). In particular,
\[
 R_s+\theta R_{-s}\ge0,\qquad
 r_s:=(R_s)_-\le\theta R_{-s}\quad\text{where }r_s>0.             \tag{1}
\]
The pointwise comparison has no remainder. Further, \(r_s\le\sum_j(B_j)_+u_{-s,j}\), and \(B_j=\theta A_j\) for \(j\ge a+1\), with \(A_j\ll\omega_j\) there. Thus \(\|r_s\|_{1,n}\ll d^{-1}\) by the bound on \(G\). The exact projection defect in [round 72](smooth-windows-72.md#both-defect-norms-for-the-same-profile) uses the first differences of \(\omega\); subtract \(Y_a\), since they sum to zero. Its normalized second norm is at most
\[
 \sum_{k\ge1}h^2b^{k-1}\sqrt{k}\le\sqrt h ,
\]
by the time-shift inequality and Jensen for a geometric variable with mean \(1/h\). Nonnegativity of the pin and raw row then gives \(\|r_s\|_{2,n}\ll d^{-1/2}\).

## Surviving high height and intermediate density

Let \(q\) be any true feasible probability in sector \(-s\) with \(\sqrt n q_0\ge1+\delta\), \(\delta>0\) fixed. This includes every optimizer on that primary face. Take \(B=o(d)\), \(B\ge0\), any set \(A\) with \(|A|\le c\sqrt n\) for sufficiently small absolute \(c>0\), and put \(M_E=\sum_{i\notin A}(q_i-B/n)_+\). The [Schur cap](astra-schur-77.md#a-cap-set-by-the-exterior-clipped-mass) controls the excess at every row, including members of \(A\):
\[
 n\sum_i(q_i-C_0 M_E/\sqrt n)_+^2\ll B .                        \tag{2}
\]
It follows that the contribution of all \(q_i>2C_0 M_E/\sqrt n\) to \(\sum_i q_i r_s(i)\) is \(O(\sqrt{B/d})\). Exact complementary orthogonality requires \(\sum_{i\ne0}q_ir_s(i)\ge m_s(\sqrt n q_0-1-\epsilon)\). The sites with \(r_s\le u=\delta/8\) pay at most \(u\); sites with \(nq_i\le c_\delta d\) pay at most \(c_\delta d\|r_s\|_{1,n}\le\delta/8\) for a suitable fixed \(c_\delta>0\). Therefore on each selected window the actual set
\[
 I=\{i\ne0:R_s(i)<-u,\ R_{-s}(i)>(2d+1)u,\
             c_\delta d<nq_i\le2C_0\sqrt n\,M_E\}
\]
satisfies \(\sum_I q_i r_s(i)\gg_\delta1\). In particular \(\sum_I q_iR_{-s}(i)\gg_\delta d\) and \(n\sum_I q_i^2\gg_\delta d\). These conclusions use the same pinned profiles, marks and density band, even if the global clipped collision grows faster than every power of \(D\).

### Removing the largest individual prices

Put \(N=\exp[J/(8(d+1))]\). The following stronger lower bounds hold uniformly after arbitrary deletions \(K\) of size \(\le N/M_E^2\):
\[
 \sum_{I\setminus K}q_i r_s(i)\gg_\delta 1,\qquad
 \sum_{I\setminus K}q_i R_{-s}(i)\gg_\delta d,\qquad
 n\sum_{I\setminus K}q_i^2\gg_\delta d .                        \tag{3}
\]
In particular \(I\) contains more than \(N/M_E^2\) sites. The deletion can be chosen after observing the exact mask, opposite height, primary density and individual prices. There is no claim of arithmetic cancellation on all surviving interactions.

For the proof, the [trimmed Mellin bound](trimmed-mellin-77.md#statement) implies \(n^{1/4}M_E/\sqrt N\to\infty\) under supercriticality. In fact \(\log_2^*\max(2,n^{1/4}M_E)\ge\log_2^*p-O_\delta(1+B)\), \(B=o(D)\), whereas \(\log_2^*N\le\log_2^*D+O(1)\), and \(D\asymp\log_2^*p\). Our absolute \(c\) may be taken below both the trimmed and the Schur thresholds. Consequently \(|K|\le\sqrt n\) eventually. Equation (2) gives \(n\sum_K q_i^2\ll B+M_E^2|K|\ll B+N\) and \(\sum_K q_i\ll n^{-1/4}\sqrt{B+N}\).

Use the [actual Mellin approximation argument](trimmed-mellin-77.md#the-cold-approximation-at-the-shorter-horizon) with per-step error \(e=(N+D)^{-4}\) through time \(2J+1\). For clarity, the resource base \(V_0=O((e^{-2}+1)^8)\) has iterated logarithm at most \(\log_2^*D+O(1)\). The dominating recursion \(V_{t+1}=2^{V_t}\) therefore has \(\log_2^*V_t\le\log_2^*p-3\) through \(2J+1\), since \(D=\log_2^*p-\log_2^*\log_2^*p-O(1)\) up to rounding and \(2J\le D/4\). In particular the actual marked coefficient at each step can be retained and the bounded approximants satisfy
\[
 \|\widetilde Y_t\|_\infty\le p^{1/8},\qquad
 \|\widetilde Y_t-Y_t\|_{2,n}\ll (2J+2)(e+p^{-3/8}).
\]
In the bulk formula for \(R_s\) replace \(u_{s,t}\) through \(2J\) by the corresponding parts of \(\widetilde Y_t\), retain the exact constant and pin, and drop the remaining times. The sum of moduli of all time coefficients is at most two. The dropped contribution has normalized second norm \(O(b^{J-1}\sqrt{2J+d+2})\), by \(a\le J\), \(\|Y_t\|_{2,n}\le2\sqrt t\) and the geometric tail. This error multiplied by \(\sqrt{B+N}\) tends to zero, by the choice of \(N\). Thus the bulk approximant has coordinate bound \(O(1+p^{1/8})\) and normalized second error \(o((B+N)^{-1/2})\). Pair its negative part with \(q\mathbf1_K\), then pay the error by Cauchy–Schwarz. This bounds the removed price \(\sum_{K\setminus\{0\}}q_i r_s(i)\) by
\[
 O((1+p^{1/8})n^{-1/4}\sqrt{B+N})+o(1)=o(1).
\]
Subtract from the lower price on \(I\), use (1), and apply the second norm bound for \(r_s\) to obtain (3).

For a signed-kernel diagnostic let \(y_i=(q_i-B/n)_+\mathbf1_{I\setminus K}(i)\). Then \(n\sum_i y_i^2\gg_\delta d\), since \(nq_i>c_\delta d\) there and \(B=o(d)\). Hence the [retained-diagonal identity](astra-schur-77.md#a-uniform-row-estimate) demands signed surviving price \((1/2+o(1))n\sum_i y_i^2\) even after imposing its allowed common-column eliminations. The row mask \(I\setminus K\) may exclude far more than \(\sqrt n\) potential priced pairs collectively. The projector formula's own conditions on its eliminated columns still apply.

## A longer geometric window at the first positive time

For \(a=1\) the same pointwise and sparse-deletion conclusions hold with \(d=\lfloor J/(16\log J)\rfloor\), where \(\log\) is natural. In this case \(N=\exp[J/(8(d+1))]\sim J^2\) and the common allowance can be \(4/(d+1)\). This version uses a prescribed start and makes no use of the separate raw-overlap estimate.

Indeed, writing \(E_j=\|v_j\|_2^2\), the exact energy telescope and decreasing weights give
\[
 G^2\le\sum_{j\ge1}\omega_j g_j^2
 =1+\tfrac14\left(hE_1+\sum_{j\ge2}(\omega_j-\omega_{j-1})E_j\right)
 \le1+h .
\]
Here \(E_1\le4\) and the terminal product vanishes by \(E_j\le4j\). Also \(g_j\ge g_0=1/\sqrt n\) for every \(j\), by the marked activation, so \(c_\omega\ge0\). Through \(J\) use the marked bound with any fixed power greater than one. Beyond \(J\) the weighted mark tail, including the missing mass of the baseline \(1\), is \(O(b^{J-1}\sqrt{J+d+2})=o(h)\). Thus \(m_s=1+o(h)\) and \(G\le1+h/2\), so the common allowance \(4h\) gives a positive pin increment for both signs. The norm bounds and density argument are unchanged. In the deletion estimate the same \(N\) still makes the geometric future \(o((B+N)^{-1/2})\), since \(J/(d+1)\sim16\log J\), and the Mellin resource bound applies with this polynomial \(N\).

The paired inequality also gives a signed linear objective on the whole bulk. For any such pinned window and complementary probability,
\[
           \sum_{i\ne0}q_i R_{-s}(i)
                   \ \ge\ (2d+1)m_s(\sqrt n\,q_0-1-\epsilon).
\]
Indeed multiply \(R_s+\theta R_{-s}\ge0\) by \(q\) on the bulk and use the exact marked complementary pairing for \(R_s\). The full bulk objective is fixed and linear in \(q\) once the window is fixed. The sharper intersection in (3) retains the density and deficit constraints.

## Four infinite-window enclosures

The [Arb512 checker](astra-height-78-check.py) uses certified complementary even endpoints at four primes. For each fixed start and \(d=4\) it encloses the entire infinite geometric row, retaining 140 time weights and bounding the remainder in counting norm by \(2\sqrt n\,b^{140}\sqrt{a+140+d+1}\). It transports Euclidean rounding errors on the exact nonlinear trajectory via nonexpansiveness. The fields and allowances below are finite diagnostics. Here the joint mask means \(R_s<-1/40, nq_i>1\); the theorem's asymptotic choice of constants is not asserted for these small fields.

| \(p\) | Start | Allowance | Negative / joint sites | Minimum opposite height on mask | Joint negative price |
|---:|---:|---:|---:|---:|---:|
| 101 | 1 | 0.020 | 17 / 17 | 1.75478 | 0.09816 |
| 257 | 2 | 0.050 | 20 / 20 | 0.88695 | 0.04886 |
| 409 | 3 | 0.040 | 24 / 20 | 1.20477 | 0.03366 |
| 769 | 11 | 0.010 | 40 / 36 | 1.17928 | 0.01391 |

The entries summarize the [outward intervals](astra-height-78-checks.jsonl). All mask comparisons and the positivity of both bulk constants are strict. The maximum ratio \(r_s/R_{-s}\) on these masks is below \(0.088\) in all four cases, versus the universal \(1/9\) at \(d=4\).

## Ranked next tests

1. On the true larger primary face choose one geometric start and bound the remaining linear height price after discarding its largest \(\lfloor N/M_E^2\rfloor\) deficit prices. An \(o(d)\) upper on \(\sum_{I\setminus K}q_iR_{-s}(i)\) for one actual optimizer suffices; the left boundary and all far-future entries are already accounted for.
2. If that price persists, test the signed Schur interaction on the surviving joint mask, retaining the full diagonal and using common-column elimination. A uniform fixed fractional deficit below half the surviving collision contradicts (3) and the signed identity.
