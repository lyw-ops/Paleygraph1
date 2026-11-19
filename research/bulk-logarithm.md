# The bulk logarithmic mean along the smoothing path

For the exact complementary smoothing pair, let $A_i(\tau)=\sqrt{w_i(\tau)}e^{\gamma_i(\tau)}$ and $B_i(\tau)=\sqrt{w_i(\tau)}e^{-\gamma_i(\tau)}$. The weights are $w_0=1$ and $w_i=\tau/n$ off the mark. Put $c=1-1/n$, $W_\tau=1+c\tau$, and

$$m_p(\tau)=\gamma_0(\tau),\qquad g_p(\tau)=\frac1n\sum_{i\ne0}\gamma_i(\tau).$$

The stationary estimate required here concerns only the signed mean $g_p(\tau)$. Once it tends to zero at fixed positive weights, an integration over the weight gives the theta limit. The mean has uniform logarithmic tail bounds from the exact mass of the two spectra.

## Exact comparison between two weights

Each spectrum is in its [complementary Fourier space](marked-response.md#weighted-complementary-projections) and has sum $\sqrt{nW_\tau}$. Their mean-zero parts at different weights are still orthogonal across signs. For every $\tau,\sigma>0$ this gives

$$\sum_i A_i(\tau) B_i(\sigma)=\sqrt{W_\tau W_\sigma}.$$

Write $d_i=\gamma_i(\tau)-\gamma_i(\sigma)$. Reversing the weights gives the identity with $d_i$ negated. Taking the sum and difference yields

$$\begin{aligned}
\cosh d_0-1+\frac{\sqrt{\tau\sigma}}n\sum_{i\ne0}(\cosh d_i-1)&=\Delta,\\
\sinh d_0+\frac{\sqrt{\tau\sigma}}n\sum_{i\ne0}\sinh d_i&=0,\\
\Delta&=\frac{c(\sqrt\tau-\sqrt\sigma)^2}{\sqrt{W_\tau W_\sigma}+1+c\sqrt{\tau\sigma}}.
\end{aligned}$$

For any real $x$, $|\sinh x-x|\le\cosh x-1$. For $x\ge0$ the inequality is $e^{-x}-1+x\ge0$, and absolute values give the other half. Thus

$$|m_p(\tau)-m_p(\sigma)+\sqrt{\tau\sigma}\,[g_p(\tau)-g_p(\sigma)]|\le\Delta.$$

Also $\cosh x-1\ge x^2/2$ gives $|g_p(\tau)-g_p(\sigma)|^2\le 2c\Delta/\sqrt{\tau\sigma}$. This is a uniform modulus of continuity on every compact subinterval of $(0,\infty)$.

## An integral with a uniformly integrable integrand

The spectra depend smoothly on the positive weights by strict concavity and the [first-order equations](marked-response.md#weighted-complementary-projections). Letting $\sigma\to\tau$ in the bound above gives $m_p'(\tau)=-\tau g_p'(\tau)$. Equivalently, differentiating the mixed product in its first argument at $\sigma=\tau$ gives $\sum_i w_i\gamma_i'=0$.

The mass of $A$ and $B$ bounds

$$\frac1n\sum_{i\ne0}e^{|\gamma_i(\tau)|}\le 2\sqrt{W_\tau/\tau}.$$

In particular $|g_p(\tau)|\le 2\sqrt{(1+\tau)/\tau}$, enough to integrate at zero uniformly in $p$ and to have $\tau g_p(\tau)\to0$ there. The [theta bracket](smoothing.md#fixed-point-and-a-sufficient-residual-estimate) gives $m_p(\tau)\to\log(\vartheta(\overline H_p)/\sqrt n)$ at the same endpoint. Integrating by parts, for every $T>0$,

$$\log\frac{\vartheta(\overline H_p)}{\sqrt n}=m_p(T)+Tg_p(T)-\int_0^T g_p(\tau)\,d\tau.$$

For $T=n$ the weights are all equal and both boundary terms vanish. More generally, for every fixed $T\ge1024$ the boundary terms tend to zero as $p\to\infty$ by the [large-weight invariant ball](large-smoothing.md#applying-the-bound-to-the-full-iteration) and fixed-depth parity. In detail, for $n\ge T$ the exact and iterative scaled fields have sup norm at most $6$. For all these points and the line segments between them, the activation derivative off the mark has absolute value at most $6/\sqrt{36+4T}$, and at the mark the bound is $6/\sqrt{36+4n}$. The Picard map is therefore contractive with a factor separated from one uniformly in $p$. Since the fixed point has unscaled $\ell_2$ norm at most $6$, the iterate converges in that norm uniformly in $p$ at fixed $T$. The bulk test $y\mapsto\operatorname{arsinh}(y/(2\sqrt T))$ on the scaled fields is odd and Lipschitz. Its normalized mean vanishes at fixed depth in the field-first limit and transfers to the stationary field by the uniform contraction. The invariant ball already gives $m_p(T)=O(n^{-1/2})$.

Consequently, under the arithmetic input from the fixed-depth and large-weight arguments, it suffices to prove $g_p(\tau)\to0$ through primes on a dense subset of $(0,1024)$. The two-weight modulus extends convergence to the full interval, and the integrable bound permits the field limit under the integral. Without using the large-weight ball, convergence on a dense subset of $(0,\infty)$ still suffices. Use the [elementary bound](marked-response.md#an-integral-for-the-conjectured-limit) $|m_p(T)|=O(T^{-1/2})$ for $T\le n$, first take $p\to\infty$ at fixed $T$, then send $T$ to infinity.

There is also a sharper uniform bound near zero. The two marked leverage scores are nonnegative with sum $1-1/W_\tau$, so $|m_p'(\tau)|\le c/(2W_\tau)$. Hence $|g_p'(\tau)|\le c/(2\tau W_\tau)$. Integrating this from $\tau$ to $n$, where $g_p(n)=0$ and $W_n=n$, shows

$$|g_p(\tau)|\le \frac c2\log(W_\tau/\tau)\qquad(0<\tau\le n).$$

The portion of the integral below $\epsilon\le n$ is bounded in absolute value by $\big((1+\epsilon)\log(1+\epsilon)-\epsilon\log\epsilon\big)/2$. In particular, if the normalized theta has a limit point different from $1$, then along a subsequence there must be a compact interval inside $(0,1024)$ on which the bulk mean has a fixed sign and stays bounded away from zero. To see this, discard small endpoint intervals using the integral bound at zero, the uniform bound near $1024$, and the vanishing boundary terms. The remaining integral has magnitude bounded away from zero. Choose a weight where the mean has the corresponding sign and magnitude bounded below, pass to a limit of those weights, and use the uniform modulus to keep the sign and a positive lower magnitude on an interval.

## What fixed-depth parity needs to transfer

Let $D_i(\tau)=\tanh\gamma_i(\tau)$. For each fixed $G>0$, the function

$$d\longmapsto\max(-G,\min(G,\operatorname{arctanh}d))$$

extends to a bounded Lipschitz odd function on $[-1,1]$. Its bulk average goes to zero at fixed iteration depth by [inertia parity](iteration-parity.md#application-to-the-picard-iterates). If its average at the exact stationary diagonal goes to zero for each fixed $G$, then the exact log mean does too, since

$$\frac1n\sum_{i\ne0}(|\gamma_i|-G)_+\le 2e^{-G}\sqrt{W_\tau/\tau}.$$

For example, the [normalized diagonal approximation](bulk-caps.md#fixed-depth-cancellation-and-transfer) transfers this test. It would suffice to transfer the bounded odd means themselves. The total-spectrum feedback and the excess mass of either spectrum need no further estimates once this signed scalar cancellation holds. This uses the identity over a weight interval. A test at a single fixed weight does not by itself give the theta limit.

One can alternatively use the [capped signed means](bulk-caps.md) $I_L$, taking the same definition at every $L>0$. For $a,b>0$,

$$\int_0^\infty\left(\min(a,L)-\min(b,L)\right)\frac{dL}{L^2}=\log(a/b).$$

Split the integral at $\min(a,b)$ and $\max(a,b)$ to obtain this identity. Here $a_i b_i=\tau$, so $g_p(\tau)=\tfrac12\int_0^\infty I_L(\tau)L^{-2}\,dL$. At fixed $\tau$, the portion above $M$ is bounded in absolute value by $2\sqrt{W_\tau}/M$. For $M>\sqrt\tau$, the portion below $\tau/M$ contributes in absolute value at most the average of $\log(\max(a_i,b_i)/M)_+$. This is also at most $2\sqrt{W_\tau}/M$. Indeed the low-$L$ integrand is zero unless the smaller spectrum is below $\tau/M$, and then its absolute integral is bounded by $\log((\tau/M)/\min(a_i,b_i))$. Cancellation of $I_L$ at each fixed $L>0$ is therefore a second form of the sufficient condition. Neither version of the stationary signed cancellation has been established through all primes.

## Numerical verification

The [weight-path probe](../log_means.py) records $m_p,g_p$ and checks both mixed-product equations and the finite-difference bound at adjacent weights. The same identities apply at square order, where the exact theta limit differs. The square controls test how a persistent bulk signed log mean can account for that difference.

The [198 recorded rows](../data/log-means.csv) use 33 geometrically spaced weights from $0.05$ to $8$ at each order. The largest fixed-point residual is below $10^{-10}$ and the largest error in either mixed-product equality is $4.3\times10^{-11}$. All 192 adjacent pairs satisfy the finite-difference bound. Integrating the cubic spline of $\tau g_p(\tau)$ in $\log\tau$ and adding the boundary terms reconstructs $m_p(0.05)$ with absolute error less than $4\times10^{-7}$ in each row of the table.

An independent check differentiated the fixed-point equation and solved the dense mean-zero linearization at six weights for each of $41,101,11^2,23^2$. The absolute discrepancies in $m_p'+\tau g_p'$ were below $2\times10^{-13}$. Coordinatewise central differences agreed with the derivatives to within $4.5\times10^{-8}$.

| Field order | $g_p(0.05)$ | $\int_{0.05}^{8} g_p(\tau)\,d\tau$ | $m_p(0.05)$ |
| ---: | ---: | ---: | ---: |
| $9413$ | $0.005468$ | $0.000325$ | $0.000405$ |
| $37253$ | $-0.000321$ | $0.000922$ | $-0.000356$ |
| $151337$ | $0.004145$ | $0.001097$ | $-0.000988$ |
| $97^2$ | $-1.115105$ | $-0.256499$ | $0.312410$ |
| $193^2$ | $-1.142692$ | $-0.260465$ | $0.317269$ |
| $389^2$ | $-1.157035$ | $-0.261983$ | $0.319743$ |

These are floating-point comparisons. The exact identity for the whole theta value uses the interval starting at zero and its stated boundary terms.
