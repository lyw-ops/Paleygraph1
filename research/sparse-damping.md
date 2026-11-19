# Damping with finitely many marked frequencies

The [fixed-depth inertia argument](iteration-parity.md) extends to any bounded number of marked frequencies, with uniform error over their locations and masses. Its arithmetic input is the same tame-convolution closure used in the single-mark proof draft. The same cancellation holds at the exact fixed point of the damped equation for each fixed damping factor. Removing damping is the remaining step at this scale.

## Fixed-depth cancellation with arbitrary marks

Fix a positive floor mass $\tau$ and an upper bound $m$ on the number of marks. Take any nonnegative unit weight $w$ supported on $S$ with $|S|\le m$, let $w^\tau=w+\tau\mathbf1/n$, and fix $0<\alpha<1$. Start the recursion $v_0=0$ and $v_{t+1}=\alpha K\sqrt{v_t^2+4w^\tau}$. Put $V_t=\sqrt n\,v_t$ and $X_j=\sqrt n\,K e_j$. With $\phi(y)=\sqrt{y^2+4\tau}$, the exact update is

$$V_{t+1}=\alpha\left(K\phi(V_t)+\sum_{j\in S} b_{t,j}X_j\right),\qquad b_{t,j}=\sqrt{v_{t,j}^2+4w_j+4\tau/n}-\sqrt{v_{t,j}^2+4\tau/n}.$$

The functions $X_j$ are frequency translates of the initial Jacobi field. On the Mellin side, a frequency translate twists its underlying object by the multiplicative Kummer character lifting that frequency. This twist is tame and unramified at $1$, so it preserves negative type. The ranks, convolution dimensions and numbers of exceptional full characters in any fixed expression remain bounded uniformly over the twists. Thus the uniform fixed-expression estimate applies to each odd product in any fixed list of these fields and their iterated even feedbacks.

Consider the ideal recursion obtained by using $2\sqrt{w_j}$ in place of each $b_{t,j}$. At every fixed depth the ideal iterate is approximable in normalized $\ell_2$ by bounded linear combinations of negative fields. For the induction, approximate $\phi$ by an even polynomial on the bounded range of the preceding approximation and apply the even-product closure under $K$. The polynomial error and the linear combination bounds can be chosen uniformly in the locations and weights, because the number of source terms is at most $m$ and all their coefficients are bounded. Multiplying the even polynomial by any $X_i$ gives an odd combination, whose normalized mean tends to zero. The $\ell_{2,n}$ comparison to the ideal iterate is uniform because $\|X_i\|_{2,n}\le1$.

Now $|b_{t,j}-2\sqrt{w_j}|\le\sqrt{v_{t,j}^2+4\tau/n}$. If $\max_{j\in S}|v_{t,j}|=o(1)$ and $V_t$ is within $o(1)$ of the ideal iterate in normalized $\ell_2$, the next ideal-iterate comparison follows by Lipschitz continuity of $\phi$. To get the next marked bound, the exact update reads

$$v_{t+1,i}=\alpha\left(\frac1n\sum_k X_i(k)\phi(V_t(k))+\sum_{j\in S}K_{ij}b_{t,j}\right).$$

The first term tends to zero by the ideal comparison. The second is $O(m\sqrt q/n)$ by the entry bound on $K$ and $b_{t,j}\le2$. The induction starts at zero. This proves $\max_{i\in S}|v_{t,i}|=o(1)$ uniformly for each fixed $t$ through primes and quadratic extensions, with the same arithmetic input in both cases.

## Taking the fixed-damping limit

The update is an $\alpha$-contraction in ordinary $\ell_2$. The first step has norm at most $2\alpha\sqrt{1+\tau}$, so the error after $t$ steps is bounded by $2\sqrt{1+\tau}\,\alpha^{t+1}/(1-\alpha)$. Let the field order tend to infinity and then let $t\to\infty$. It follows that $\|v_{\alpha,S}\|_2=o(1)$ at the exact damped fixed point. In particular

$$\left|2\sum_i w_i\operatorname{arsinh}\frac{v_{\alpha,i}}{2\sqrt{w_i^\tau}}\right|\le\sum_{i\in S}\sqrt{w_i}|v_{\alpha,i}|\le\|v_{\alpha,S}\|_2=o(1).$$

For the undamped solution $v_*$, the difference between its signed log test and $F(w)$ is bounded by $\log(1+\tau)$ by the [entropy gap](poisson-smoothing.md#an-interval-for-arbitrary-marked-weights). The [mixed-product identity](poisson-smoothing.md#comparing-damped-and-undamped-fixed-points), with $u_\beta=\sqrt{v_\beta^2+4w^\tau}$, gives

$$4\sum_i w_i^\tau\left(\cosh(\gamma_{\alpha,i}-\gamma_{*,i})-1\right)\le (1-\alpha)\langle (I-J)u_\alpha,(I-J)u_*\rangle.$$

For example, uniform boundedness of $\mathbb E\|u_*\|_2$ for the marked weight model at each fixed $\tau$ would give cancellation at bounded label counts after $\tau\downarrow0$. Indeed $(1-\alpha^2)\|(I-J)u_\alpha\|_2^2\le4(1+\tau)$, so the expected right side tends to zero as $\alpha\uparrow1$. Then Cauchy–Schwarz and $\cosh x-1\ge x^2/2$ transfer the signed log test. An expectation bound on the mixed pairing itself would also suffice.

For the square-order single mark, $F(w)\to\log 2$. Any fixed $0<\tau<1$ gives a strict gap between $\log(1+\tau)$ and that limit. The same argument along subsequences therefore forces $\|u_*\|_2\to\infty$ there. The fixed-damping result cannot distinguish the two field families on its own.

This gives a fixed-relative-floor version of the [sparse Poisson moment obstruction](parallel-audit.md#counterexamples-what-cannot-pass-to-sparse-intensity), using the inertia argument above. At intensity $c=1/n$ and floor $\epsilon=\delta c$ for fixed $0<\delta<1$, condition on exactly one jump overall with size $X\in[1,2]$. The conditional size law and the probability of this event are independent of $n$. Translation and scaling of weights reduce the exact spectrum to $\sqrt X$ times the single-mark spectrum with floor mass $\tau=\delta/X$. At each fixed $X$ its ordinary squared norm diverges through square orders. Fatou's lemma on this event shows that $c^{-1}\mathbb E\|u_*\|_{2,n}^2\to\infty$ even at this fixed relative floor.

## The bulk contribution in a marked inverse

At a fixed point, let $T=S^c$, $P=I-J$, and $D_T$ be the diagonal equal to $v_i/u_i$ on $T$ and zero on $S$. On the mean-zero space define $B=(K-\alpha P D_T P)^{-1}P$. The inverse exists for $0<\alpha\le1$ at positive floor since $\|D_T\|<1$ and $K^2=P$. Applying $K$ to $v=\alpha K u$ yields the exact decomposition

$$v_S=\alpha B_{SS}u_S+\alpha B_{ST}(4w_T^\tau/u_T).$$

Here division is coordinatewise and the second source has norm at most $2\sqrt\tau$. The elementary estimate $\|K_{SS}\|\le |S|\sqrt q/n$ controls the first block at zero bulk diagonal. At the true diagonal the inverse also involves repeated passages through $T$. This form isolates the two quantities needed for a direct marked estimate: the compression of the bulk inverse to $S$, and how the floor source on $T$ reaches $S$.

## Numerical checks

At floor mass $\tau=0.05$ the one-mark signed log tests from the FFT recursion were as follows. The $\alpha=1$ checks use the safeguarded Newton solve in [the weighted solver](../poisson_weights.py), with residuals below $10^{-9}$.

| Field order | $\alpha=0.9$ | $\alpha=0.99$ | $\alpha=1$ | $\|u_*\|_2$ |
|---:|---:|---:|---:|---:|
| $9413$ | $0.00208$ | $0.00100$ | $0.00081$ | $3.08$ |
| $97^2$ | $0.02482$ | $0.27925$ | $0.62482$ | $9.35$ |
| $37253$ | $-0.00043$ | $-0.00070$ | $-0.00071$ | $3.08$ |
| $193^2$ | $0.00824$ | $0.15340$ | $0.63454$ | $13.04$ |

The corresponding four-label checks use eight samples per order and hold the sample weights fixed across damping factors. At the larger prime and square orders, the mean absolute signed tests were respectively $0.0208$ and $0.0125$ at $\alpha=0.9$, and $0.0239$ and $0.0345$ at $\alpha=1$. The measured means of $\|u_*\|_2$ were $3.14$ and $3.92$. At small orders $41,49,101$, a separate dense inverse check with four labels agreed with the marked decomposition to $1.6\times10^{-10}$.
