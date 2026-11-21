# A masked reciprocal lower at fixed ordinary repair depth

Use the actual positive reciprocal factors \(g,g_-\) normalized by \(\sqrt n\) as in [Round 120](reflected-offmark-cubic-120.md). Put \(\mu=\mathbb E_n g=\mathbb E_n g_-\). Consider an actual nonnegative source \(q\) satisfying \(q(0)=0\), \(\|q\|_{2,n}\le C n^{-1/4}\), \(\mathbb E_n(qg)\ge c n^{-1/2}\), and define \(\eta_q=n^{1/4}\|q-\epsilon Kq\|_{2,n}\). The constants \(C,c\) are fixed. Neither a bounded supremum nor a critical upper on the mean \(m=\mathbb E_n q\) is imposed here. Write \(u=\epsilon Kq\), \(w=qg/(n\mathbb E_n(qg))\), and let \(\mathcal L=\sum_{x,y}\omega^-_x w_y k(x-y)^2\). The full-input masked-output distinct expansion obeys
\[
             n M_q^{\rm dist,\circ\mathrm{out}}
       = p\mu\mathbb E_n(qg)\,\mathcal L+O(\eta_q+n^{-1/4}).                \tag{1}
\]

For the full masked moment substitute \((Kg)(Kg_-)=\mu(g+g_-)-\mu^2-t/n\) off zero, replace \(u\) by \(q\) in the terms with the factors, and use \(q(0)=0\). The replacement error before scaling is \(O(\eta_q/n)\) since the normalized factor norms are \(O(n^{-1/4})\). Opposite-sector projection gives \(\mathbb E_n(qg_-)=O(n^{-3/4}+\eta_q n^{-1/2})\), because \(m=O(n^{-1/4})\) and \(2\Pi_- q=q-u-m\mathbf1\). The constant terms cost \(O(n^{-5/4})\) using \(\|u\|_{2,n}=O(n^{-1/4})\). Consequently the full masked moment is \(\mu\mathbb E_n(qg)+O(n^{-5/4}+\eta_q/n)\).

Book collisions in the original rows, with prefactor \(\epsilon p^{3/2}\) over the three normalized counting expectations. The exactly-two-equal pattern pairing the repair and opposite inputs costs \(O((p/n)\mu\mathbb E_n(qg_-))\) by the \(O(p^{-1/2})\) pointwise Katz bound, unchanged at that order by deleting the output. Pairing the two true factors costs \(O((p/n)m\mathbb E_n(gg_-))=O(n^{-5/4})\). The all-equal term is bounded by \(p^{3/2}n^{-2}\mathbb E_n(qgg_-)=O(n^{-3/2}m)\) from the exact reciprocal product and absence of the repair input mark. The remaining equal repair/favored pair has the exact full-output value from [Round 116](paired-legendre-cubic-116.md):
\[
 -\frac pn\mu\mathbb E_y\left[q_y g_y\left(\sum_x\omega^-_x k(x-y)^2-\frac{n-1}{p}\right)\right].
\]
Its single deleted output costs \(O(n^{-3/2})\) since \(\mu\mathbb E_n(qg)=O(n^{-1})\). Subtracting that collision cancels the constant baseline up to the smaller term \(\mu\mathbb E_n(qg)/n\), proving (1). All estimates keep the opposite input singleton as part of the full true factor.

## Uniform paired spreading with a second moment of the density

The density of \(w\) relative to the true favored law \(\omega\) is \(r(y)=\mu q_y/\mathbb E_n(qg)\). It satisfies
\[
 \mathbb E_\omega r^2=\frac{\mu\mathbb E_n(q^2g)}{(\mathbb E_n(qg))^2}=O(1)
\]
by the bounded normalized factor \(g\) and the squared norm of \(q\). Under the original positive pair \(\omega\otimes\omega^-\), the difference law is exactly uniform. The new difference density is the conditional expectation of \(r\) under that pair given the difference. Conditional Jensen therefore gives an \(O(1)\) second norm under the uniform difference law. By Cauchy–Schwarz and the unweighted Jacobi arcsine law, a sufficiently small fixed \(|k|\)-window about zero carries at most half of this new difference mass. Consequently \(\mathcal L\ge c_1>0\) uniformly, with \(c_1\) depending on the fixed input bounds. This replaces pointwise domination by a bounded second moment of the density.

## Application to the genuine ordinary orbit

Under the fixed-floor critical cap-rate marked obstruction of [Round 109](persistent-repair-deficit-109.md), the actual ordinary negative rows \(q=h_j\) meet the input hypotheses for every \(j\le2c_*\sqrt n\) on its persistent window. This uses the already proved true favored pairing lower, the ordinary negative norm bound by the initial spill, and positivity of the actual mark. The displacement bound from the nonexpansive ordinary update gives \(\eta_q=O((j+1)^{-1/2})\), uniformly in that window, since \(q-u=2Pq-\mathbb E_n q\,\mathbf1\). The paired-square lower and the prefactor lower in (1) are independent of \(j\). Thus one may choose a sufficiently large **fixed** ordinary repair depth \(j_0\), depending on the obstruction parameters, and deduce \(M_{h_j}^{\rm dist,\circ\mathrm{out}}\ge c_2/n\) for every \(j_0\le j\le2c_*\sqrt n\) and all sufficiently large primes in the obstruction. The same holds for the actual dyadic-block average of [the old-slack note](ordinary-slack-dissipation-121.md), which lies entirely after \(j_0\); the required norms, marked input and true pairing are inherited by averaging.

An independent arithmetic upper at any such fixed genuine depth would now exclude the critical-rate marked obstruction without a growing-depth masked estimate. This statement still uses the actual capped fixed point as input to the finite repair depth. Approximating that input by a finite Picard prefix with enough normalized power saving, or controlling the arithmetic of the actual source directly, remains open. This does not prove the cap rate or the rate-free weighted route.
