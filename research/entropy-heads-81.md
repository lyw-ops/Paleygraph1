# Entropic cost of the actual signed Schur interaction

The translated Jacobi moment comparison also bounds an exponential test with a parameter growing with the prime. On the true terminal mask this gives a choice between more deletions on the low-density side and large relative entropy of the actual exterior clipped row. The entropy estimate tests the whole signed interaction before restricting to the Jacobi-bias heads.

## An exponential comparison for weighted translates

Use \(G=\widehat Q\), \(n=(p-1)/2\) and the normalized real Jacobi kernel \(k\) from [round 80](astra-surviving-80.md#weighted-translated-jacobi-moments). For any probability \(v\) on \(G\) and sign \(\sigma\) set \(W(j)=\sigma\sum_i v_i k(j-i)\), \(m=(\sum_i v_i^2)^{-1}\). Write \(E\) for uniform counting expectation. For real \(t\),
\[
                  E e^{tW}\le e^{t^2/(2m)}
                            +\frac{C|t| e^{|t|}}{\sqrt p}.             \tag{1}
\]
To verify it, take \(\widetilde W=\sigma\sum_i v_i\cos\theta_i\) with independent uniform angles. The monomial argument of round 80 applies to both odd and even powers. At order \(a\ge1\), each product uses at most \(a\) distinct centers with disjoint pairs of full-character quadratic lifts. Its exponential expansion has absolute coefficient mass at most one and total Gauss exponent at most \(2a\). Constant terms match the independent angles. The Katz moment bound and at most \(2a\) exceptional full characters give \(|EW^a-\mathbb E\widetilde W^a|\le Ca/\sqrt p\); the trivial bound covers \(a\ge\sqrt p\). Averaging weighted products over their centers preserves the bound. The absolutely convergent exponential series, since \(|W|,|\widetilde W|\le1\), now gives (1) by \(\sum_{a\ge1}a|t|^a/a!=|t|e^{|t|}\). The bounded-variable exponential bound for the independent angles gives the first term. The uniformity covers centers and weights selected after computing the true primary row.

## A lower bound on the exterior clipped entropy

Take any of the sets \(S\) and exterior clipped rows \(x\mathbf1_E\) in the [retained-diagonal comparison](astra-surviving-80.md#where-a-large-collision-gets-its-signed-price). In particular \(x=(q-B/n)_+\), \(E=A^c\), \(M=\sum_E x_i>0\), \(L=n\sum_S q_i^2\), \(M_S=\sum_S q_i\), \(v=q\mathbf1_S/M_S\) and
\[
             \rho=\frac{L}{\sqrt n M_S M},
                  \qquad \rho^2m=\frac{L}{M^2}.
\]
Assume \(L\to\infty\), \(B=o(L)\) and \((1+|A|)/\sqrt n=o(\rho)\), under the common-column size bound there. The signed Schur identity gives \(E_\mu W=(\sqrt{n/p}+o(1))\rho\), where \(\mu=x\mathbf1_E/M\) is the actual exterior clipped probability. This uses the **total signed price** and the error \(o(L)\), including the separated diagonal and the low part. In particular \(E_\mu W\ge\rho/2\) eventually and \(\rho\le2\). Its relative entropy to uniform obeys
\[
             \sum_i\mu_i\log(n\mu_i)
                \ \ge\ c\,\min\{L/M^2,\rho\log p\}-o(1).              \tag{2}
\]
Indeed for \(t\ge0\), Jensen's inequality, or nonnegativity of relative entropy to the Gibbs probability, gives \(\sum\mu_i\log(n\mu_i)\ge tE_\mu W-\log E e^{tW}\). Take \(t=\min(\rho m/4,(\log p)/8)\). The error in (1) is \(O((\log p)p^{-3/8})=o(1)\), and the leading exponential there is at least one. Thus the logarithm is at most \(t^2/(2m)+o(1)\le t\rho/8+o(1)\), proving (2). Logs in (1)–(2) are natural. Taking the logarithm of \(n\sum\mu_i^2\) gives an upper bound on the entropy by Jensen, so the same test forces
\[
               n\sum_E x_i^2
                \ge M^2\exp\!\bigl(c\min\{L/M^2,\rho\log p\}-o(1)\bigr).
                                                                        \tag{3}
\]
These bounds use the probability on the whole retained exterior. The restriction of \(\mu\) to the bias heads can have very small mass. In particular (2) does not follow merely by assuming that the clipped law is supported on those heads.

For comparison, the same raw moment bound gives a counting estimate with a growing moment order. If \(J=L/M^2\) and \(u=\min\{J,\log p/\log(C_0/\rho)\}\) tends to infinity for a sufficiently large absolute \(C_0\), then the head set \(T=\{j\in E:W(j)>\rho/8\}\) satisfies
\[
                         |T|/n\le C e^{-c u}+O(p^{-1/4}).              \tag{4}
\]
Use an integer \(\ell=\lfloor c_0u\rfloor\ge1\) in the moment bound of round 80. A small absolute \(c_0\) makes the independent term at most \(2^{-\ell}\) and keeps \((8/\rho)^{2\ell}\le p^{1/8}\); the extra factor \(\ell\ll\log p\) is absorbed into \(p^{-1/4}\). This grows the moment without interchanging fixed-center and large-field limits. It still allows clipped mass on a sparse head set.

## A common alternative at one true terminal time

Fix a supercritical gap \(\delta>0\) and use a genuine larger-side primary probability \(q\) with \(\sqrt n q_0\ge1+\delta\). For any one of the [finite terminal windows of round 79](terminal-height-79.md) let \(r\) be its actual deficit, \(Z\) its companion projection, \(d\asymp D(p)\) and \(I\) its density/height set. Take \(A=\{0\}\), \(B=o(d)\), and any allowed tower parameter \(H\). Define \(\alpha_p=D(p)/\log p\). For all sufficiently large eligible primes there is the following alternative, with the same \(q\) and window.

* The part of \(I\) with \(q_i\le M\alpha_p/\sqrt n\) pays a fixed positive deficit price and \(\gg_\delta d\) terminal height even after deleting any \(H^2/(M^2\alpha_p^2)\) sites.
* The remaining higher-density part retains \(\gg_\delta d\) collision after every original deletion of at most \(H^2/M^2\) sites. The genuine exterior law \(x\mathbf1_E/M\) then has entropy at least \(c_\delta D(p)\), and \(n\sum_E x_i^2/M^2\ge \exp(c_\delta D(p))\).

For the first claim, if the low part has an initial fixed price, the deficit price removed there by a set \(F\) of the enlarged size is \(o(1)\). In fact \(\sqrt n\|q\mathbf1_F\|_2\le H\) and \(\|q\mathbf1_F\|_1\le H^2/(M\alpha_p\sqrt n)\), counting just low sites. The bounded actual Mellin approximants for the terminal envelope have sup bound \(O(1+\log\log p)\) and normalized second error \(o(1/H)\) by the tower slack in [round 79](terminal-height-79.md#a-tower-scale-deletion-on-the-terminal-height). The resulting product of the sup bound and the mass is \(o(1)\) by \(n^{1/4}M/H\to\infty\), \(H\le\log_2\log_2p\), and \(\alpha_p^{-1}\le\log p\). The companion comparison gives the height bound after every deletion. If the initial low price is below half the uniform surviving price of round 79, the higher part after any original deletion still pays a fixed deficit price, giving \(L\gg_\delta d\) by Cauchy--Schwarz. For this row set \(\rho\ge\alpha_p\), since \(\rho\) is the \(q\)-weighted mean of \(\sqrt n q_i/M\) on the set. Thus \(L/M^2\gg_\delta D(p)\) and \(\rho\log p\ge D(p)\). The common-column error hypothesis follows from \(A=\{0\}\) and \(\rho\ge\alpha_p\). Now (2) and (3) prove the second alternative.

The latter condition tests the **shape of the clipped exterior**, even when the scalar mass \(M\) is far above the trimmed-Mellin threshold. This result does not show an entropy upper bound on genuine larger-side optimizers. It also leaves the height upper after the enlarged deletion unresolved.

1. See whether the exact optimal face contains a probability with exterior clipped entropy \(o(D(p))\) at a growing cutoff \(B=o(D)\). With \(A\) containing the root this would exclude the high branch at the stated setting. The same row still needs a surviving low-height upper.
2. On high row sets whose effective moment window tends to infinity, use (4) to formulate a fixed exposed-support head upper bound for the signed interaction. A counting estimate alone leaves (2) compatible with substantial concentration.
