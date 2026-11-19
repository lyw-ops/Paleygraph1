# Separate sector costs in trimming the cold drift

Fix \(0<\varepsilon<1\) and \(\delta>0\). Write \(n=(p-1)/2\), \(P_\sigma=(I-J+\sigma K)/2\), and let \(q\) be any nonnegative probability in \(\mathbb R\mathbf1+\operatorname{ran}P_\sigma\) with \(\sqrt n\,q_0\ge1+\delta\). Allow any real comparison \(z\le q\) and any deletion \(A\) with \(|A|\le(1-\varepsilon)^2n/(1+\sqrt p)\). Define
\[
 \begin{split}
 x&=q-z,\qquad M_E=\sum_{i\notin A}x_i,\qquad Z_0=\sqrt n\,(-z_0)_+,\\
 U&=\sqrt n\|P_\sigma z\|_2,\qquad V=\sqrt n\|P_{-\sigma}z\|_2,\qquad
 H=\max(2,V+n^{1/4}M_E).
 \end{split}
\]
Here \(\|\cdot\|_2\) denotes the counting norm. For all sufficiently large eligible primes, uniformly in \(q,z,A\),
\[
             \log_2^*p-\log_2^* H
                  \le C_{\delta,\varepsilon}(1+U^2+Z_0).                 \tag{1}
\]
In particular, with a nonnegative comparison value at the mark, the same-sector energy costs \(U^2\) units of depth. The opposite-sector energy enters the iterated-logarithm bound on the exterior remainder. This permits comparisons with large opposite-sector norm and small same-sector norm. The bound applies to either sector and to deletion sets selected from the actual row.

## The trimmed remainder and the exact signed drift

In the forbidden projector \(P=P_{-\sigma}\) write \(\lambda=P_{ii}\) and use the off-diagonal bound \(\mu=(1+\sqrt p)/(2n)\). Since \(Px=-Pz\), the diagonal estimate in [round 76](astra-masked-76.md#removing-arbitrary-exceptional-coordinates) gives
\[
 (\sqrt{\lambda+\mu}-\sqrt{|A|\mu})\sqrt n\,\|x\|_2
 \le V+\sqrt{n\mu}\,M_E.
\]
It uses \(|\langle x,(P-\lambda I)x\rangle|\le\mu(\|x\|_1^2-\|x\|_2^2)\) and \(\|x\|_1=\sum_i x_i\). No positivity of \(z\) is needed. The coefficient is at least \(\varepsilon\sqrt{\lambda+\mu}\), so
\[
     \sqrt n\,\|x\|_2\le C_\varepsilon H,\qquad
     \sum_i x_i\le M_E+\sqrt{|A|}\|x\|_2\le C_\varepsilon n^{-1/4}H.       \tag{2}
\]
The upper bound \(\sqrt n\,q_0=O(1)\) follows from \(q_0=1/n+(P_\sigma q)_0\), the off-diagonal bound for \(P_\sigma\), and \(1-(P_\sigma)_{00}=1/2+O(1/n)\).

Put \(Y_t=\sqrt n\,v_t\) for the true cold orbit started at zero, with \(\phi_t(i)=|v_t(i)|\) off the mark and \(\phi_t(0)=\sqrt{4+v_t(0)^2}\). Thus \(Y_{t+1}=K(|Y_t|+\sqrt n\,\beta_t e_0)\), where \(\beta_t=\phi_t(0)-|v_t(0)|\in[0,2]\). Write \(g_t=\sqrt n\,\overline{\phi_t}/2\) and \(\gamma=\sqrt n\,q_0\). The identity \(\sigma Kq=q-\mathbf1/n\) and \(q\ge0\) give
\[
 \sigma\langle q,Y_{t+1}\rangle
 =\langle q,|Y_t|\rangle+\beta_t\gamma-2g_t
 \ge \sigma\langle q,Y_t\rangle+\beta_t\gamma-2g_t.
\]
The energy telescope \(\|v_{t+1}\|_2^2-\|v_t\|_2^2=4-4g_t^2\) yields \(\sum_{t<T}g_t^2\le T\) and \(\sum_{t<T}g_t\le T\). By the [actual mark bound](vanishing-floor-38.md#1-uniformity-of-the-marked-arithmetic-as-the-floor-vanishes), \(\beta_t=2+o(1)\) uniformly through the proved marked depth. Consequently at each \(1\le T\le D(p)\) for all sufficiently large primes,
\[
               \sigma\langle q,P_\sigma Y_T\rangle
               =\sigma\langle q,Y_T\rangle\ge c_\delta T.                 \tag{3}
\]
The equality uses the zero mean of \(Y_T\).

## Approximating the projection with its exact marked source

Suppose (1) fails along a sequence with \(g=\log_2^*p-\log_2^*H\) and \(g/(1+U^2+Z_0)\to\infty\). Use \(T=\lfloor g/8\rfloor\) and the [round-77 shortened-horizon approximation](trimmed-mellin-77.md#the-cold-approximation-at-the-shorter-horizon) with this \(H\). That construction needs only \(g\to\infty\) and \(H\ge2\). In particular \(H\le\log_2\log_2p\) eventually. The bulk-linear combination
\[
 F_T=\tfrac12(\sigma Y_T+|Y_{T-1}|)-g_{T-1}\mathbf1
\]
has an approximant \(\widetilde F_T\) of sup norm \(O(p^{1/8}+\sqrt T)\) and error \(o(1/H)\) in \(\|\cdot\|_{2,n}=\|\cdot\|_2/\sqrt n\). Indeed use the approximants to \(Y_T,Y_{T-1}\), retain the scalar \(g_{T-1}\le\sqrt T\) exactly, and use the Lipschitz continuity of absolute value. This holds on the whole space. The marked source is kept separately via the identity
\[
           \sigma P_\sigma Y_T=F_T+\tfrac12\sqrt n\,\beta_{T-1}e_0.
\]
It follows from \(KY_T=\sqrt n\,(\phi_{T-1}-\overline{\phi_{T-1}}\mathbf1)\). Hence
\[
 \begin{split}
 \sigma\langle z,P_\sigma Y_T\rangle&\le U\|Y_T\|_{2,n}\le 2U\sqrt T,\\
 \langle x,F_T\rangle&\le \|\widetilde F_T\|_\infty\sum_i x_i
             +\sqrt n\,\|x\|_2\|F_T-\widetilde F_T\|_{2,n}=o(1),\\
 \tfrac12\sqrt n\,\beta_{T-1}x_0&\le\sqrt n\,q_0+Z_0=O(1)+Z_0 .
 \end{split}
\]
In the second line, \(p^{1/8}n^{-1/4}H=o(1)\) by the bound on \(H\). In the first line, the cold energy again gives \(\|Y_T\|_{2,n}\le2\sqrt T\). Summing the three lines gives an \(o(T)\) upper bound for the left side of (3), because \(U^2+Z_0=o(T)\). This contradiction proves (1).

For \(z_i=\min(q_i,B/n)\), one has \(U^2,V^2\le n\|z\|_2^2\le B\) and \(Z_0=0\). Thus (1) also gives the cutoff estimate of round 77 up to the constant: adding \(\sqrt B\) inside \(H\) increases its iterated logarithm by \(O(1+B)\). With a signed comparison, a large negative mark must be charged or handled by a separate argument. Treating the entire projected drift as a bounded Mellin approximation would omit its marked source.

## Ranked next tests

1. On the true larger primary face and a fixed deletion \(A\), minimize the same-sector cost subject to \(z\le q\), \(z_0\ge0\), and a budget on \(V+n^{1/4}M_E\). This is a convex problem in the actual face and the comparison row. Compare to the scalar cutoff at the same exterior budget.
2. If the convex comparison fails, retain the signed directional objective \(\sigma\langle z,P_\sigma Y_T\rangle\) in place of its Cauchy–Schwarz upper bound. The proof only needs this objective to be \(o(T)\) along a suitable growing prefix and the separate exterior and mark bounds. Verify any saving on actual prime faces before using it asymptotically.
