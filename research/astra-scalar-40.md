# An arithmetic integral bound on the physical mark and its exact cold germ

Put $n=(q-1)/2$, $c=1-1/n$, $W=1+ct$. Let $P_\sigma(t)$ be the actual positive **mean-one** stationary row of sign $\sigma$ with weights $w_0=1,w_i=t/n$ off zero. Write $m_q(t)=\log(\sqrt{W/n}\,P_{+,0}(t))$. Reciprocity gives $\sigma m_q(t)=\log(\sqrt{W/n}\,P_{\sigma,0}(t))$. Extend to $t=0$ by $m_q(0)=\log(\theta_+/\sqrt n)$. The following bound controls the real scalar itself on every prime limit path, at every positive floor in an integral. It also determines the initial derivative of every square limit path. A different, finite-field derivative detects the sizes of the two optimal supports. These results leave the all-prime ordinary theta limit open.

## A bulk logarithmic cost bounds the entire positive marked deficit

For **any** positive mean-one feasible trial row $v$ on the same side, define $B(v)=n^{-1}\sum_{i\ne0}\log v_i$. Then the exact finite-field inequality is

\[
 \int_0^\infty \left[\log\frac{v_0}{P_{\sigma,0}(t)}\right]_+
                  \frac{dt}{t^2}
 \ \le\ c\log(1/c)-B(v).                                           \tag{1}
\]

To prove it, write $G(t)=\max_u\{\log(u_0/v_0)+t B(u)\}$ over that same feasible polytope. The strict logarithmic optimum gives $G'=B(P_\sigma(t))$ at every $t>0$. The two optimality inequalities at ordered floors show that $B(P_\sigma(t))$ is nondecreasing and that the optimized marked coordinate is nonincreasing. Equivalently this follows from convexity of $G$ and the identity
\[
 (G(t)/t)'=t^{-2}\log(v_0/P_{\sigma,0}(t)).
\]
The integrand is positive on a terminal interval, possibly empty. On the whole positive axis $G(t)/t\ge B(v)$ by the trial. Its limsup at infinity is at most $c\log(1/c)$ by Jensen on the $n-1$ bulk sites, $\sum u_i=n$, and $u_0\le n$. Integrate the derivative over the terminal interval, taking limits at its endpoints. These facts explain why the positive part in (1) is allowed even for suboptimal trial marks.

Apply (1) to the arithmetic trial $v=(1-\alpha)\mathbf1+\alpha l_\sigma$, $0<\alpha<1$, where the position row of $l_\sigma$ is $\delta_1+2\mathbf1_{D_\sigma}/(\sqrt q+1)$. Its bulk spectral values are $(\sqrt q+\sigma\lambda_i)/(\sqrt q+1)$ and its mark is $1+(n-1-\sigma)/(\sqrt q+1)$ by the [Jacobi Fourier formulas](fourier.md). In particular $v_0/\sqrt n\to \alpha/\sqrt2$. The inherited [arcsine law](smoothing.md#first-two-iteration-markers) gives
\[
 B(v)\longrightarrow \int_0^{2\pi}\log(1+\sigma\alpha\cos x)\frac{dx}{2\pi}
             =\log\frac{1+\sqrt{1-\alpha^2}}2 .
\]
For the evaluation, factor the integrand's argument as $A|1+rz|^2$ on the circle with $A=(1+\sqrt{1-\alpha^2})/2$, $r=\sigma\alpha/(2A)$, and integrate the convergent logarithm series. First keep $\alpha<1$, so the test is bounded and continuous.

Let $m$ be any locally uniform subsequential limit of the real physical marks through eligible primes, or through prime squares. Such subsequences exist on compact intervals containing zero, by the [real leverage bound](marked-response.md#an-integral-for-the-conjectured-limit) $|m_q'(t)|\le c/(2W)$ and the two elementary Jacobi theta brackets at zero. Fatou in (1) gives, for each sign,
\[
 \boxed{\displaystyle
 \int_0^\infty
 \left[\log\!\left(\alpha\sqrt{(1+t)/2}\right)-\sigma m(t)\right]_+
                 \frac{dt}{t^2}
 \ \le -\log\frac{1+\sqrt{1-\alpha^2}}2 ,\qquad 0<\alpha\le1.}       \tag{2}
\]
Increasing $\alpha$ to one gives the endpoint by monotone convergence after taking the field limit. No uniform control on negative logarithms of individual Jacobi eigenvalue gaps is assumed. The arithmetic input is the actual one-column Jacobi witness and its empirical bulk law. The variational bound applies to the true stationary optimum. This gives a bound through all primes even when neither benchmark is asymptotically optimal.

For a square limit take $\sigma=-1$, $\alpha=1$. Since $\theta_-/\sqrt n\to1/\sqrt2$, the expression inside the positive part is already nonnegative. It equals the limit $d(t)$ of $\log(\theta_-/P_{-,0}(t))$, a nondecreasing function. We obtain
\[
 \int_0^\infty d(t)\,dt/t^2\le\log 2,\qquad
 m(t)=\tfrac12\log 2-\tfrac12\log(1+t)+o(t)\quad(t\downarrow0).     \tag{3}
\]
Indeed $d(t)/(2t)\le\int_t^{2t}d(s)\,ds/s^2\to0$. This proves the right derivative $-1/2$ for **each actual square limit path**, with the field limit first. More generally if a prime subsequence attains the elementary extremum $\theta_\sigma/\sqrt n\to1/\sqrt2$, every limit path on it satisfies $\sigma m(t)=-\tfrac12\log2+\tfrac12\log(1+t)+o(t)$ by the identical proof. The latter is conditional on that extremal asymptotic. The error in (3) is for an individual limiting path. It does not give a joint rate for arbitrary $t=t_q\downarrow0$.

## The face chart at the exact cold endpoint

At fixed finite $q$, let $I$ be the maximal unmarked positive support of the sign-$\sigma$ optimal face, and $J$ its unmarked complement. There is a strictly complementary opposite optimum with positive support $\{0\}\cup J$ by [the exterior partition](rank-partitions.md#complementarity-gives-the-partition), applied to the single mark. All sizes count full coordinates, including multiplicities of distinct indices in an even orbit. Write $\theta=\theta_\sigma$, $b=|J|/n$. The true marked germ is real analytic through zero, and its derivatives are
\[
 (\sigma m_q)'(0)=\frac c2-b=\frac{|I|-|J|}{2n},\qquad
 (\sigma m_q)''(0)= b^2-\frac{c^2}2-\frac2n\sum_{i\in I}\frac{k_i^*}{u_i^*}. \tag{4}
\]
Here $u^*$ is the analytic center of the optimal face for the objective $\sum_{i\in I}\log u_i$. The transversal $k^*$ can be computed even when the optimal face has positive dimension.

For details let $V$ be the sign's mean-zero tangent space, $T=\{h\in V:h_J=0\}$. Its elements have $h_0=0$, since both signs of a small change at a relative interior optimizer are feasible, and its mark is optimal. Thus $T$ is the optimal-face tangent. Put $N=V\ominus T$ and parametrize $u=u^*+h+t k$ with $h\in T,k\in N$. The affine coordinates span the entire mean-one sector for $t\ne0$. After subtracting $\log\theta+b t\log t$ from the objective and dividing by $t>0$, it is
\[
 \frac{\log(1+t k_0/\theta)}t+
 \frac1n\sum_{I}\log(u_i^*+h_i+t k_i)+\frac1n\sum_J\log k_j.        \tag{5}
\]
The first term extends analytically to $t=0$. There (5) splits. Its $h$ maximizer is zero. Its $k$ maximizer $k^*$ maximizes $k_0/\theta+n^{-1}\sum_J\log k_j$ with $k_J>0$. This domain is nonempty by projecting $\mathbf1-u^*$ onto $N$. For a strictly complementary opposite mean-one row $v^*$, $v_0^*=n/\theta$ and orthogonality gives $k_0/\theta=-n^{-1}\sum_J v_j^*k_j$. Since each $v_j^*>0$ and restriction from $N$ to $J$ is injective, the functional goes to minus infinity at infinity and at every finite boundary point. Empty zero-dimensional factors can be omitted. The Hessians on $T,N$ are negative definite separately and the mixed Hessian is zero. The analytic implicit function theorem gives the germ $(h(t),k(t))$ from $t=0$. The corresponding rows are positive for small $t>0$, so strict concavity identifies the actual physical solution. This argument tolerates redundant Fourier constraints and nonvertex optimum faces.

Stationarity in the scaling direction $k$ itself gives exactly
\[
 \frac{k_0}{\theta+t k_0}+\frac t n\sum_I\frac{k_i}{u_i^*+h_i+t k_i}+b=0 .
\]
At zero this gives $k_0^*/\theta=-b$. Its first derivative gives $k_0'(0)/\theta=b^2-n^{-1}\sum_I k_i^*/u_i^*$. Inserting these in $\sigma m_q=\log(\theta+t k_0(t))+\tfrac12\log(W/n)$ proves (4). One may use any representative modulo $T$ of the maximizing transversal in (4), since the face center annihilates $\sum_I h_i/u_i^*$. The complementary row also shows $k_j^*=1/v_j^{\rm cen}$ on $J$, where $v^{\rm cen}$ is its own face analytic center. The exact bulk product is $t/W$, and the opposite chart proves convergence to that center.

For primes let $M=\lceil(\sqrt{1+4n}-1)/2\rceil$. The [prime affine support theorem](parallel-low-energy-7.md#a-missing-interval-and-an-affine-rank-bound) gives $1+|I|,1+|J|\ge M$. Hence
\[
 \sqrt n\left(\tfrac12-|m_p'(0)|\right)\ge (M-1/2)/\sqrt n=1+O(n^{-1/2}).                     \tag{6}
\]
At $q=r^2$ for odd primes $r$, the [uniqueness of the subfield plus optimum](square-endpoint-uniqueness.md) gives $1+|I|=(r+1)/2$ on the plus side. Consequently $m_{r^2}'(0)=-1/2+r/(2n)$ and the left side of (6) tends to $1/\sqrt2$. This separates primes from squares in a signed stationary derivative at the $n^{-1/2}$ correction scale. It does not exclude the unscaled extremal derivative $-1/2$ as a prime limit. The field-first conclusion (3) was proved without commuting derivatives with limits. No field-uniform radius for (5) follows from the implicit function theorem.

## Exact checks

The [checker](astra-scalar-40-check.py) differentiates the independent prime-13 cubic at its physical endpoint and the square-25 quintic at its specified face center. At 13 the plus face is the single spectrum $1+\cos(\pi i/3)$. The transversal is $-\cos(\pi i/3)/3$. At 25 use the symmetry and the variables of [round 34](complex-branches-34.md#2-the-actual-square-25-minus-curve). In its notation the minus optimal face in the invariant space has $t=r$, $0\le r\le1$, and mark $3$. With $h=1/(1+r)$ its variable bulk log sum is $6\log(1-h)+2\log h+\log(2h-1)$. Its center is $h=(7+\sqrt{13})/18$. The opposite plus center equals $4\mathbf1_{\{0,4,8\}}$. Thus a representative of the minus transversal has values $1/4$ at 4 and 8 and is $-[\cos(\pi i/6)+\cos(5\pi i/6)]/4$. Symmetry of the optimum at all positive floors allows this reduced calculation. The [two exact records](astra-scalar-40-checks.jsonl) verify both derivatives in (4). The second derivatives for the stated signs are $-101/216$ and $-343/864-5\sqrt{13}/216$.

~~~sh
uv run --no-project --with sympy==1.14.0 python -B research/astra-scalar-40-check.py
~~~

Neither the integral bound nor the cold face slopes give the required cancellation across intermediate prime floors. The explicit arithmetic benchmark in (2) also exists on squares, where the marked path is nonzero at the cold endpoint.
