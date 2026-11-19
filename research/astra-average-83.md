# Paying terminal sites from the clipped exterior source

Fix \(0<\delta\le1\) and a true side-\(\sigma\) feasible probability \(q\) with \(\sqrt n\,q_0\ge1+\delta\) at an eligible prime. Use \(D=D(p)\), \(\Lambda=\log_2^*p\), \(J=\lfloor D/8\rfloor\), and any good terminal window of [round 79](terminal-height-79.md). Its length \(d\asymp D\), pinned primary deficit \(r\), companion projection \(Z\), and joint set \(I\) are taken at the same terminal time \(b\). Take the root alone as the initial deletion in that construction. On the bulk,
\[
 0\le r\le (2d-1)^{-1}\sum_{j=b-1}^{b+1}a_j |Y_j|,
 \qquad (a_{b-1},a_b,a_{b+1})=(1,2,1)/4.
\]
On \(I\) one has \(Z\ge(2d-1)r\). The deficit price \(\sum_I q_i r_i\) stays above a constant depending only on \(\delta\), also after any one admissible round-79 deletion. Unadorned second norms count sites, and \(\|\cdot\|_{2,n}\) uses normalized counting measure.

## Send the clipped exterior through the Jacobi operator

Choose \(B=o(D)\) and any positive exterior split \(q=x+z\) with \(x_0=0\) and \(0\le z_i\le B/n\) off zero. Thus \(z_0=q_0\). Put \(M=\sum x_i\), \(m=M^2/\sum x_i^2\). The hard clip is one choice and its exterior mass is at most \(M\). By the [trimmed lower bound](trimmed-mellin-77.md), \(n^{1/4}M\) exceeds every base-two tower of height at most \((1-\kappa)\Lambda\) eventually, for every fixed \(\kappa>0\). In particular \(M>0\) and \(B+1=o(\sqrt n M^2)\).

Use the same signed Jacobi field at every terminal time,
\[
 W(i)={\sigma n\over\sqrt p\, M}(Kx)_i,\qquad
 e_i=1+\sigma n(Kz)_i .
\]
The weights of this translated field are \(x/M\). The actual eigen-equation and \(K^2=I-J_{\rm const}\), with \(J_{\rm const}\) the mean projection, give
\[
 nq_i=\sqrt p\,M W(i)+e_i,\quad
 {\mathbb E}_n e^2=1+n\|z\|_2^2-(\sum z_i)^2=O(B+1),\quad
 {\mathbb E}_n W^2={n\over p}(m^{-1}-n^{-1}).                    \tag{1}
\]
Here \(q_0=O(n^{-1/2})\) and \(\sum_{i\ne0}z_i\le1\). Also \(m\gg\sqrt n\). Indeed \(|W|\le1\) by the Jacobi column bound. Multiply \(q_i\le \sqrt p\,M/n+|e_i|/n\) by \(x_i\) and sum, using \(x\le q\). The resulting \(\|x\|_2^2\le(\sqrt p/n)M^2+O(\sqrt{(B+1)/n})\|x\|_2\) proves the assertion by the lower bound on \(M\).

For \(\alpha>0\) write \(G_\alpha=\{i\ne0:\sqrt n q_i>\alpha M\}\) and \(T_\alpha=\{i\ne0:W(i)>\alpha\sqrt n/(2\sqrt p)\}\). Then
\[
 n\sum_{G_\alpha\setminus T_\alpha}q_i^2\le4{\mathbb E}_n e^2,\qquad
 \sum_{G_\alpha\setminus T_\alpha}q_i r_i
                         =O(\sqrt{(B+1)/d}).                       \tag{2}
\]
Indeed \(e_i>nq_i/2\) there, and \(\|r\|_{2,n}=O(d^{-1/2})\). The same fixed head thus retains every fixed positive high-density deficit at every good time. Its counting fraction is \(O(1/(\sqrt p\,\alpha^2))\) by (1). The [forward Schur interaction](astra-surviving-80.md) uses a field built from the paying sites separately at each time. Formula (2) uses the clipped exterior as its source and localizes the actual deficit itself.

## Collision required on the same head

Let \(T_0=1,T_{k+1}=2^{T_k}\). Take \(H=T_{\lfloor\Lambda/8\rfloor}\), \(N=T_{\lfloor\Lambda/2\rfloor}\), and \(e=(H+D)^{-12}\) as the scalar approximation tolerance in this section. The [finite cold approximation](trimmed-mellin-77.md#the-cold-approximation-at-the-shorter-horizon) gives common bounds through \(J\)
\[
 \|\widetilde Y_j\|_\infty\le U,\qquad
 \|Y_j-\widetilde Y_j\|_{2,n}\le C D(e+p^{-3/8})\le H^{-11}
                                                                    \tag{3}
\]
eventually, where \(\log_2^* U\le\Lambda/4+O(1)\). The base resources have iterated logarithm at most \(\Lambda/8+O(1)\) and each of the \(J+2\le\Lambda/8+O(1)\) stages costs one tower level. In particular \(U^2 H^C=o(N)\) for every fixed \(C\). For any set \(F\), apply (3) to the three-term envelope to obtain
\[
 \|r\mathbf1_F\|_{2,n}
      \le {C\over d}\big(U\sqrt{|F|/n}+H^{-11}\big).              \tag{4}
\]

Uniformly for \(p^{-1/4}N\le\alpha\le1\), (1) gives \(|T_\alpha|/n\le C/N^2\). Each true \(Y_j\) therefore has normalized squared norm at most \(C H^{-22}\) on the same head. If \(S\subseteq I\cap G_\alpha\) has deficit price at least a fixed \(\epsilon_0>0\), (2)–(4) and Cauchy–Schwarz give
\[
 n\sum_{S\cap T_\alpha}q_i^2\gg_{\epsilon_0} d^2 H^{22},\qquad
 \sum_{S\cap T_\alpha}q_i Z_i\gg_{\epsilon_0}d.                    \tag{5}
\]
The collision is required on the actual coordinates paying the retained height. The exponent 22 can be increased by increasing the fixed precision exponent in (3), with the same tower heights. At \(\alpha=H^{-1/4}\), the [signed entropy inequality](entropy-filter-82.md) applied to this retained set also yields
\[
 1+\mathcal D_{x/M}\gg_{\epsilon_0}
        \min\{d^2 H^{22}/M^2,\ H^{-1/4}\log p\}.
\]
Its hypotheses hold since \(L\gg B+1\) and the retained set has its own \(\rho>\alpha\). This proves an entropy requirement even before making further deletions, whenever the high sites carry a fixed deficit.

## Nearly linear deletion on the other part

The absolute density split \(A_N=\{i\ne0:nq_i>N\}\) satisfies \(|A_N|\le n/N\), independently of \(M\). Let \(\widetilde I\) be \(I\) after any one round-79 admissible deletion. At each good terminal time at least one of the following holds, uniformly:

* On \(\widetilde I\cap A_N\) the deficit price is \(\gg_\delta1\), the companion height price is \(\gg_\delta d\), and the collision of those sites is \(\gg_\delta d^2H^{22}\).
* On \(\widetilde I\setminus A_N\), those first two price bounds and collision \(\gg_\delta d\) survive every further deletion of up to \(\lfloor nH^2/N^2\rfloor=n^{1-o(1)}\) sites.

Split the fixed deficit price and retain a part that pays at least half. In the high case apply (4) with \(|F|/n\le1/N\). In the low case any allowed removed subset \(F\) in that density range has \(n\sum_F q_i^2\le H^2\) and \(\sum_F q_i\le H^2/N\). The bounded approximants and their errors in the three-term envelope give removed price at most \(C d^{-1}(UH^2/N+H^{-10})=o(1)\). The bound on \(Z\) over \(I\) and \(\|r\|_{2,n}=O(d^{-1/2})\) give the remaining height and collision. The claimed cardinality follows from \(N=p^{o(1)}\). The alternative may vary with \(b\).

The last absolute high set need not lie in the relative head of (5). Its role is to permit a nearly linear deletion for any exterior mass on the low side. The result supplies a sufficient test for the original conjecture. On each hypothetical sequence with a fixed gap, find one good terminal time and one true larger-side optimizer with both \(o(d^2H^{22})\) collision on the indicated absolute high joint mask and \(o(d)\) companion height after one allowed deletion on the absolute low mask. The needed upper estimates on actual optimizers remain open. No cancellation beyond the inherited growing marked window is used.

## Finite replay and ranked tests

The [Arb384 checker](astra-average-83-check.py) uses the certified endpoint pair, true zero-floor trajectory and finite pin of round 80. With \(B=1,\alpha=1/4\) and deficit cutoff \(0.01\), the reverse head retains \(5/13,10/22,14/38,14/52\) of the high paying sites at primes \(101,257,409,769\), respectively. Its retained deficit is strictly positive in all four cases. The checker verifies the equalities in (1) and the error-site collision in (2), including the full marked remainder. The finite times are \(4,5,6,7\); their pins use the minimum nonnegative mean increment from zero allowance, as in round 80. [Interval records](astra-average-83-checks.jsonl)

1. At a true larger optimum, test the collision in the deficit band on the reverse head, and the low companion height left after dropping its most expensive allowed sites. A fixed positive high deficit is excluded if its retained collision grows more slowly than (5). The absolute split gives a test below the useful relative thresholds.
2. On the capped round-79 band \(q_i\ll M/\sqrt n\), a normalized counting energy \(o(d^2/(M\sqrt p))\) for the three true fields on the reverse head forces \(o(1)\) high deficit there by weighted Cauchy–Schwarz. Test the true approximation error on this head at that scale. The \(H^{-22}\) bound is insufficient for it in general.
