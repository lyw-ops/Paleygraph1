# The critical floor against an actual concentrated witness

At square order and floor one, the signed mean of the actual scaled Picard endpoint on the subfield annihilator grows at least as fast as $2^{-1/6}T^{1/3}$ in the short marked window, in the liminf sense below. The strictly positive linear coefficient for lower floors vanishes at this endpoint. At floor one the minus row also requires a strictly positive extra scaled mean of order at least $1/T$ to retain its mark. The signed estimate applies to a general positive sector witness exactly at the corresponding mass threshold, including on primes when such a witness is given. It does not settle prime simultaneous completion or ETH Problem 26.

## A finite drift bound retaining the activation curvature

Use the [true zero-start undamped orbit](averaged-mark-35.md), $Y_t=\sqrt n v_t$, $W=1+(1-1/n)\tau$, $g_t=\sum_i\phi_t(i)/(2\sqrt n)$ and $E_t=\|v_t\|^2$. Let $\mu$ be any probability in $\mathbb R1+V_\sigma$, $\alpha=\sqrt n\mu_0$, $m_t=\sigma\sum_i\mu_iY_t(i)$ and $f(y)=\sqrt{y^2+4\tau}$. The [actual marked coefficient](parallel-depth-window-30.md) is $b_t=\sqrt{4+v_t(0)^2}-\sqrt{4\tau/n+v_t(0)^2}$. Write
$$R_t=\alpha\sum_{j<t}(2-b_j),\quad \gamma=\alpha-\sqrt W,\quad
F_t=2\sum_{j<t}(\sqrt W-g_j),\quad
H_t=\sum_{j<t}\left[\sum_i\mu_i f(Y_j(i))-m_j\right].$$
For $0<\tau\le1$, these three reserves are nonnegative and $H_t,R_t$ are nondecreasing. In fact
$$m_t+R_t=2\gamma t+F_t+H_t,\qquad
\sqrt W F_t= E_t/4+\sum_{j<t}(\sqrt W-g_j)^2. \tag{1}$$
The first identity follows from $K\mu=\sigma(\mu-1/n)$ and the exact split $\sqrt n\phi_t=f(Y_t)+\sqrt n b_t e_0$. The second is the energy telescope from zero. Jensen gives
$$H_{s+1}-H_s\ge\sqrt{m_s^2+4\tau}-m_s
\ge 2\tau/((m_s)_++\sqrt\tau). \tag{2}$$
This is where positivity of the same test across all times enters.

Let $V=m_T+R_T+2T(-\gamma)_+=2T\gamma_++F_T+H_T$. For every $s<T$, (1), monotonicity of $H$ and Cauchy–Schwarz on the prefix of $\sqrt W-g_j$ imply
$$m_s\le V+2\sqrt{s\sqrt W\,V}.$$
Summing (2) gives the fully explicit inequality
$$V(V+2\sqrt{T\sqrt W\,V}+\sqrt\tau)\ge2\tau T. \tag{3}$$
In particular at a fixed positive floor, along growing $T$ with $R_T+2T(-\gamma)_+=o(T^{1/3})$,
$$\liminf m_T/T^{1/3}\ge \tau^{2/3}(1+\tau)^{-1/6}.$$
To pass to the limit divide (3) by $T$ on any subsequence of bounded $V/T^{1/3}$. The other subsequences already satisfy the claim.

There is also a surplus above the linear drift. Put $U=F_T+H_T$. Since $g_s\ge0$, the first identity before inserting $\sqrt W$ shows $m_s\le2\alpha s+U$. For $\alpha>0$, summing (2) and integrating the decreasing lower envelope gives
$$U\ge (\tau/\alpha)\log(1+2\alpha T/(U+\sqrt\tau)). \tag{4}$$
At fixed $\tau>0$ and $\alpha\to a>0$, $\liminf U/\log T\ge\tau/a$, by taking subsequences on which the ratio is bounded. Thus a supercritical witness forces this additional logarithmic term in $m_T+R_T-2\gamma T$. These bounds use its Fourier sector and mass, without replacing it by a cap or dropping its entire bulk contribution.

## The square endpoint and the price of actual completion

For $q=r^2$, use the [exact plus probability](square-order-control.md) uniform on the subfield annihilator $I$, $|I|=(r+1)/2$. Then $\alpha^2=2(r-1)/(r+1)$. At $\tau=1$ the deficit $(-\gamma)_+$ is $O(1/r)$. In the [round-38 window](vanishing-floor-38.md) $T\le D(q)$, the inequality $0\le 2-b_j\le |v_j(0)|+2/\sqrt n$ gives $R_T=o(1)$ uniformly after taking the window exponent $B>2$. Hence for every growing $T$ in that window,
$$\liminf\frac{1}{T^{1/3}|I|}\sum_{i\in I}Y_T(i)\ge 2^{-1/6}.$$
Removing the mark costs $\alpha|v_T(0)|=o(1)$. The same lower bound applies to the average scaled bulk terminal excess $\sqrt n(\phi_T-\phi_0)$ on $I$ with the mark omitted (and denominator $|I|$), since off the mark $f(Y_T)-2\ge Y_T-2$. This is sublinear, so the result by itself gives no constant lower bound for this average divided by $T$.

Let $G=T^{-1}\sum_{t=1}^T g_t$ and $X_-(0)$ be the actual unscaled minus mark. Any nonnegative minus completion preserving that mark at scaled mean $G+s$ obeys $G+s\ge\alpha X_-(0)$ by pairing with $\mu$. Uniformly for $1\le T\le D(q)$, $X_-(0)\ge1-o(1/T)$ from the two mark identities in [round 35](averaged-mark-35.md) and the round-38 estimate. Indeed the sum of marks is at least two and their difference is $O(D^{-B})$. The telescope starting at time one reads
$$2\sqrt W T(\sqrt W-G)=(E_{T+1}-E_1)/4+\sum_{t=1}^T(g_t-\sqrt W)^2.$$
Here $E_{T+1}\ge4-o(1)$ from the single marked summand as in round 38, and $E_1\le4$. The Jacobi first-step law gives $g_1\to g=\mathbb E\sqrt{1+2\cos^2\Theta}<\sqrt2$ for uniform $\Theta$ on $[0,\pi]$, with strict inequality by Jensen. Since $T|\gamma|=o(1)$, every such square completion has
$$\liminf T s\ \ge (\sqrt2-g)^2/(2\sqrt2)>0.$$
Thus exact completion at this boundary floor already fails on all sufficiently large squares throughout the window, including fixed depths. An allowance tending to zero more slowly than $1/T$ is outside this obstruction. The cubic estimate and the price estimate concern distinct quantities.

The checker uses dense actual Arb orbits and exact subfield probabilities at $q=49,121$, at the critical mass threshold and at floor one. Run `.venv/bin/python -B research/astra-repair-41-check.py` to reproduce the finite checks. Neither the tests nor the square theorem provide a prime upper bound.
