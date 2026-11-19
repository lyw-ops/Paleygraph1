# A compression gap on square-root-scale progressions

Let $q\equiv1\pmod4$ be a finite field order, $Q=(\mathbb F_q^\times)^2$, $n=|Q|$, and $m_0=n/\sqrt q$. The quadratic character is $\chi$, the sign on $Q$ is $s(a)=\chi(1-a)$, and the frequency operator is $K_{ij}=\lambda_{i-j}/n$ with $\lambda=Fs$. The Jacobi bound is $|\lambda_h|\le\sqrt q$.

Fix $B\ge1$. Consider frequency progressions

$$I=\{h_0+jd:0\le j<M\},\qquad M\le Bm_0,$$

where the order $\ell$ of $d$ in $\widehat Q$ satisfies $\ell\ge64 B m_0$. Then $\limsup_q\|P_I K P_I\|<1$ as $q\to\infty$. In particular the [small-support argument](subgroup-modes.md#arbitrary-sets-at-the-smallest-possible-scale) excludes stationary slow modes concentrated on these progressions or on subsets of them. The upper bound on $M$ permits any fixed multiple of the smallest possible support scale.

## The sign averaged on the fibers of the step

Write $g=n/\ell$ and $R=\ell/m_0=\sqrt q/g$. For $t\in\mathbb Z/\ell\mathbb Z$, let $f(t)$ be the average of $s(a)$ over the $g$ elements $a\in Q$ with $d(a)=\exp(2\pi i t/\ell)$. Then $|f|\le1$ and its unnormalized discrete Fourier coefficients have absolute value at most $R$, since they are $\lambda_{hd}/g$ up to the sign convention for $h$.

These two bounds give a signed sum estimate on any interval $J$ of length $H$ with $R\le H\le\ell/2$,

$$\left|\sum_{t\in J}f(t)\right|\ll R(1+\log(H/R)).$$

To see this, set $r=\lfloor R\rfloor$ and smooth $\mathbf1_J$ by convolution with the uniform probability on $\{0,\dots,r-1\}$. The change in the sum is at most $2r$. The Fourier magnitudes of the two factors at cyclic distance $k>0$ from zero are at most $\min(H,\ell/(2k))$ and $\min(1,\ell/(2rk))$. Split their product sum at $\ell/H$ and $\ell/r$ and divide by $\ell$ to obtain $O(1+\log(H/r))$. Multiply by the bound $R$ for the Fourier coefficients of $f$. This is the interval smoothing argument of [Fouvry et al., Theorem 1.1](https://aif.centre-mersenne.org/item/AIF_2017__67_1_423_0/) with the two magnitude bounds kept separate.

## A large Rayleigh quotient forces a long sign bias

Suppose the compression norm tends to $1$ on a subsequence. Choose a unit vector $y$ on $I$ with Rayleigh quotient tending to $\sigma\in\{1,-1\}$, passing to a further subsequence to fix the sign. Translate the progression to start at zero and use coordinates $y_j$ on its terms. Put

$$Y(\theta)=\sum_{j=0}^{M-1}y_j e^{2\pi i j\theta},\qquad r_y(h)=\sum_j\overline{y_j}y_{j+h},$$

with zero extension for the correlation. Since $|K_{ij}|\le1/m_0$, the Rayleigh quotient gives $\sum_h|r_y(h)|\ge(1-o(1))m_0$. There are at most $2M-1$ terms. Cauchy–Schwarz and Parseval on the circle give

$$\|Y\|_\infty^2\ge\int_0^1|Y|^4\,d\theta=\sum_h|r_y(h)|^2\gg_B m_0,$$

using $\int_0^1|Y|^2\,d\theta=1$. Choose $\theta_q$ attaining the supremum and rescale

$$F_q(z)=m_0^{-1/2}Y(\theta_q+z/m_0).$$

These entire functions satisfy $|F_q(z)|\le\sqrt B\exp(2\pi B|\operatorname{Im}z|)$ by Cauchy–Schwarz. By compactness on compact sets, pass to a subsequence with a locally uniform entire limit $F$. The preceding lower bound gives $|F(0)|>0$.

The frequency compression is the quadratic form of positional multiplication by $s$. In the progression coordinates it satisfies the exact identity

$$1-\sigma\langle y,Ky\rangle
=\frac1\ell\sum_t(1-\sigma f(t))|Y(t/\ell)|^2.$$

The identity uses discrete Parseval and $M\le\ell$. On the cyclic interval $J_T$ defined by $|t-\ell\theta_q|\le TR$, use consecutive integer representatives near $\ell\theta_q$. Its summands take the form $R^{-1}(1-\sigma f(t))|F_q((t-\ell\theta_q)/R)|^2$.

First suppose $R\to\infty$ on the subsequence. For every fixed $T>1$, the nonzero entire $F$ has only finitely many real zeros in $[-T,T]$. Outside arbitrarily small neighborhoods of the zeros, $|F_q|$ is bounded below uniformly by local uniform convergence. The summands are nonnegative and their total tends to zero. The grid in the argument of $F_q$ has spacing $1/R\to0$, so the omitted neighborhoods have a proportion that can be made arbitrarily small. It follows that

$$\sum_{t\in J_T} f(t)=\sigma |J_T|+o_T(R),\qquad |J_T|=(2T+o(1))R.$$

Taking $T$ fixed and large enough contradicts the bound $O(R(1+\log(2T)))$ from Fourier smoothing.

For a bounded subsequence, pass to limits $R\to R_*\ge64B$ and $\ell\theta_q-\lfloor\ell\theta_q\rfloor\to\beta\in[0,1]$. The grid in $[-T,T]$ then converges to the portion of $(\mathbb Z-\beta)/R_*$ in that interval. Take $T$ away from the two grid boundaries. At each limiting point where $F\ne0$, the corresponding value of $\sigma f$ tends to $1$. The number $N(T)$ of zeros of $F$ in the disk of radius $T$, counted with multiplicity, satisfies Jensen's bound

$$N(T)\log 2\le 4\pi BT+\log(\sqrt B/|F(0)|),$$

by applying Jensen's formula at radius $2T$ and using the exponential-type bound. Thus

$$\liminf_q R^{-1}\sigma\sum_{t\in J_T} f(t)\ge 2T-\frac{1+2N(T)}{R_*}\ge T-O_{B,F}(1).$$

Here $2N(T)$ allows the worst value $-1$ at every sampled zero. This again contradicts the logarithmic sum bound for sufficiently large fixed $T$ and proves the gap in both cases.

The square-order annihilator of the subfield clique has $\ell=|I|\sim m_0$ and norm tending to $1$. In the [critical-set experiments](../data/critical-sets.csv), generator-step intervals have compression norms $0.14193$ at $p=151337$ and $0.08655$ at $p=1000033$. The square-order subgroup at $q=389^2$ has compression norm $387/388$. The proof yields a qualitative gap for the progression family, and the numerical values come from finite floating-point compressions.

## A bounded number of separated intervals

The gap also holds for any subset of the union of at most $r$ progressions of lengths at most $Bm_0$ in a common coset of $\langle d\rangle$, with $B,r$ fixed and $\ell/m_0\to\infty$. The translates of the progressions within that coset can be arbitrary. The proof keeps track of their relative phases when evaluating the Fourier polynomial on the positional interval.

Write the progression starts as $a_j\in\mathbb Z/\ell\mathbb Z$. Suppose a unit compression vector $y$ has Rayleigh quotient tending to $\sigma=\pm1$. In the common coset, identify $y$ with a vector on $\mathbb Z/\ell\mathbb Z$, and write $Y(t)=\sum_i y_i\exp(2\pi i it/\ell)$. Its cyclic autocorrelation has at most $O_{B,r}(m_0)$ possible nonzero differences, since each pair of component progressions contributes an interval of at most $2Bm_0$ differences. The Jacobi entry bound gives $\sum_h|r_y(h)|\ge(1-o(1))m_0$. Cauchy–Schwarz and cyclic Parseval give $\ell^{-1}\sum_t |Y(t)|^4\gg_{B,r}m_0$. As $\ell^{-1}\sum_t|Y(t)|^2=1$, there is a grid point $t_0$ with $|Y(t_0)|\gg_{B,r}\sqrt{m_0}$.

Assign each coordinate of $y$ to one of its progressions, using zero coefficients for overlaps already assigned. At $u=t/R$, $R=\ell/m_0$, the rescaled polynomial has the form

$$m_0^{-1/2}Y(t_0+t)=\sum_{j=1}^r F_{j,q}(u)\exp(2\pi i a_j t/\ell).$$

The envelopes $F_{j,q}$ have frequencies in $[0,B]$ in the $u$ variable, with the phase at $t_0$ incorporated in the coefficients. Cauchy–Schwarz bounds them by $\sqrt B\exp(2\pi B|\operatorname{Im}u|)$, so pass to locally uniform entire limits $F_j$. The large grid peak gives $\sum_j F_j(0)\ne0$.

For $k\in\mathbb Z^r$, let $\beta_q(k)$ be the centered representative modulo one of $k\cdot a/\ell$. By a diagonal subsequence, each $R\beta_q(k)$ has a limit in the extended real line. The finite-limit indices form a subgroup $\Lambda$ of $\mathbb Z^r$, and their limits form an additive functional on $\Lambda$, since $R\to\infty$. Choose a real vector $b$ extending that functional by $k\mapsto k\cdot b$. The recentered phases are

$$z_{q,t}=a t/\ell-b(t/R)\pmod{\mathbb Z^r}.$$

On every fixed interval $|t|\le TR$, the empirical measure of $(t/R,z_{q,t})$, with weight $1/R$ per grid point, converges to Lebesgue measure on $[-T,T]$ times Haar probability on $L=\Lambda^\perp\subset\mathbb T^r$. Indeed, for $k\in\Lambda$, the character of the recentered phase tends to one uniformly. For other $k$, the distance of $k\cdot a/\ell-k\cdot b/R$ from the integers, times $R$, tends to infinity. The geometric-sum bound gives vanishing normalized character sums on subintervals. Approximation of continuous test functions by intervals in the first coordinate and trigonometric polynomials in the second gives the asserted convergence.

The limiting rescaled polynomial is

$$F(u,z)=\sum_j F_j(u)\exp(2\pi i(b_j u+z_j)).$$

It is nonzero at $(0,0)$. On the identity component $L^\circ$, $F(0,z)$ is a trigonometric polynomial with a zero set of Haar measure zero, by successive one-variable integration. For almost every such $z$, the function $u\mapsto F(u,z)$ is nonzero entire, so its real zeros have measure zero. Let $w(z)$ be the squared absolute value of the average of the characters of any set of representatives of $\Lambda^{\rm sat}/\Lambda$, where $\Lambda^{\rm sat}=\operatorname{span}_{\mathbb Q}(\Lambda)\cap\mathbb Z^r$. This nonnegative trigonometric polynomial equals the indicator of $L^\circ$ on $L$. Indeed the finite quotient of the lattices is the dual of $L/L^\circ$, as seen by putting $\Lambda$ in Smith normal form. The sum of the absolute Fourier coefficients of $w$ is at most one.

The Rayleigh deficit gives $R^{-1}\sum_{|t|\le TR}(1-\sigma f(t_0+t))|m_0^{-1/2}Y(t_0+t)|^2\to0$. On the part where $|F(u,z_{q,t})|$ exceeds any fixed positive threshold, the same limit holds with $w(z_{q,t})$ in place of the squared polynomial. On the remaining part, use $0\le1-\sigma f\le2$, the empirical limit, and then send the threshold to zero. The limiting product of $w$ with the zero-set indicator vanishes by the preceding argument. Therefore

$$R^{-1}\sigma\sum_{|t|\le TR} f(t_0+t)w(z_{q,t})\longrightarrow \frac{2T}{[L:L^\circ]}.$$

For the opposite estimate, each Fourier term of $w(z_{q,t})$ modulates $f$ by a single frequency in $t$. Approximate this frequency by a multiple of $1/\ell$ at cost $O_T(R^2/\ell)=o_T(R)$ in the interval sum. An exact cyclic modulation keeps the two Fourier magnitude bounds used in the interval smoothing estimate. The weighted sum is consequently $O(R(1+\log(2T)))+o_T(R)$, since the Fourier coefficients of $w$ have absolute sum at most one. The component index is finite and fixed on the subsequence. Taking $T$ fixed and sufficiently large contradicts the displayed linear limit and proves the gap.

For example, two identical packets spaced $\ell/2$ apart give the phase factor $1+(-1)^t$. Its zeros fill every odd grid point. The component indicator selects the even points, giving the nonzero limiting interval average used in the proof. In a finite compression test at $p=151337$, splitting $195$ consecutive frequencies into two lengths differing by one and starting the pieces at $0$ and $n/2$ gives norm $0.13307$, compared with $0.14193$ for one interval. At $389^2$, the same two-interval construction gives $0.12198$ and the annihilator of the subfield has norm $0.99742$. These norms are from dense eigensolves on the specified supports.
