# Smoothing independent frequency weights

The [size-biased Poisson identity](rank-partitions.md#independent-input-for-the-remainder) expresses the remainder of the rank expansion in terms of independent inputs $Z_i$. At fixed positive intensity, matrix universality gives sign cancellation for the damped nonlinear fixed point. Gaussian concentration of the exact logarithmic spectra removes the damping. This proves that the entire rank expansion from $k\ge cn$ tends to zero for every fixed $c>0$, through both prime and prime-square orders.

## An interval for arbitrary marked weights

For nonnegative normalized $w$, put $E(w)=\sum_{i:w_i>0}w_i\log(n w_i)$. If $P\in\mathcal P_+$ and $Q\in\mathcal P_-$ are positive on this support, set $L_+=\sum w_i\log P_i$ and $L_-=\sum w_i\log Q_i$. The complementary entropy identity gives

$$2L_+-E(w)\le F(w)\le E(w)-2L_-.$$

For the exact positive smoothing solution at $w^\varepsilon=w+\varepsilon\mathbf1/n$, the interval has width

$$2\left[\log(1+\varepsilon)+\sum_{i:w_i>0}w_i\log\frac{w_i}{w_i^\varepsilon}\right]\le2\log(1+\varepsilon).$$

The exact positive solution is convenient for computing a narrow interval, while the inequality only uses feasibility. From any numerical iterate $v$, form $u_i=\sqrt{v_i^2+4w_i^\varepsilon}$ and the two nonnegative trial spectra $(u\pm v)/2$. Project each onto its allowed Fourier space, add a constant to ensure positivity, and normalize its mean to one. The resulting spectra are feasible in exact arithmetic. The [FFT probe](../poisson_weights.py) uses this projection, with a matrix-free Newton solve for the trial vector. Its reported intervals use floating-point FFTs, and its standard errors estimate sampling variability separately.

## Fixed-depth cancellation from independent inputs

Write $J=\mathbf1\mathbf1^{\mathsf T}/n$ and $\Pi=I-J$. Since $K\mathbf1=0$ and $K^2=\Pi$, the matrix $H_0=K+J$ is a real symmetric orthogonal matrix. Its entries are $O(n^{-1/2})$ by the Jacobi bound. Thus $\Pi H_0\Pi=K$ has the traffic distribution of a punctured Haar reflection, by [Gorini, Jones, Kunisky and Pesenti, Theorem 1.6](https://arxiv.org/html/2604.11729v1). This argument also applies to $-K$.

For independent, identically distributed side data $Z_i$ of a fixed law with all moments, the comparison extends to expected empirical tests of fixed polynomial iterations in $K$ and the data. Expand each empirical polynomial into labelled graphs with a power of $Z$ at each vertex. For each equality partition of the labels, expectation over the $Z_i$ gives a product of fixed moments and the remaining sum is an injective traffic moment on the quotient graph. The injective and unrestricted traffic polynomials are related by partition inversion. This also bounds all fixed moments of each such vector network evaluated at a uniform coordinate. In particular any such test odd under replacing $K$ by $-K$ has a vanishing expected empirical limit.

To use the genuine activation, fix an independent nonnegative input law $Z$ of positive finite mean, a floor $\epsilon>0$, and set $w_i=Z_i+\epsilon$. For $0<\alpha\le1$, write

$$v_0=0,\qquad v_{t+1}=\alpha K\sqrt{v_t^2+4w}.$$

At fixed depth, the annealed law of $(Z_i,v_{t,i})$ at a uniform coordinate tends to that of $(Z,s_t g)$ with $g$ standard normal independent of $Z$. Here $s_0=0$ and

$$s_{t+1}^2=\alpha^2\operatorname{Var}\big(\sqrt{s_t^2g^2+4(Z+\epsilon)}\big).$$

First consider bounded side data and replace the activations by fixed polynomials $f_t(x,z)$ even in $x$. For the Haar reference, take an unpunctured reflection $H$ with an equal number of both signs. The polynomial recurrence with $H$ and centered inputs $\alpha(f_t-\mathbb E f_t)$ has a Gaussian asymptotic law, as follows from [Fan, Theorem 4.3](https://arxiv.org/abs/2008.11892). In the AMP version the limiting derivative coefficients vanish because the polynomial is even in the centered Gaussian last iterate, independently of the side data. The first free cumulant is zero and the second is one. With the derivative matrix zero the covariance recursion is the second-moment matrix of the centered polynomial inputs. The nondegeneracy condition can be ensured when choosing the approximating polynomials, by taking a nonconstant first input and inserting an arbitrarily small nonzero even term of higher degree in each last iterate. Given the earlier Gaussian iterates and the side data, this term cannot be a linear combination of the previous inputs and Gaussian coordinates. For constant side data the genuine Picard iteration is identically zero.

Here is how to pass from that AMP statement to the punctured polynomial recurrence without a sup-norm estimate on polynomial iterates. On the Haar model, the AMP output has vanishing empirical mean and each empirical input mean converges to its deterministic center. The empirical Onsager coefficients tend to zero. Thus replacing the centered $H$ update by $\Pi H\Pi$ changes each AMP update by a finite sum of vector networks times scalars tending to zero in probability. The vectors are the constant vector, $H\mathbf1$, and previous polynomial inputs. Expanding the recursions at fixed depth, every term in the difference has one such small factor. Every fixed polynomial network in $H$ and the independent data has bounded normalized moments, from the Haar traffic distribution and the same equality-partition argument. Products of scalar empirical averages are tight by their moment bounds. Hence the difference goes to zero in every fixed normalized $\ell_p$ norm in probability. This expansion also supplies higher-moment bounds for the plain punctured network, so its empirical moments converge in expectation. The traffic comparison transfers its joint expected moments with $Z$ to the Paley matrix. Gaussian moments with bounded independent side data determine the joint law.

Now choose the polynomial approximations sequentially. At each preceding polynomial stage the limiting law of the last iterate with $Z$ has a product of a Gaussian and a bounded distribution. Polynomials even in the Gaussian variable are dense in the corresponding even $L^2$ functions. At that stage the squared error of approximating $\sqrt{x^2+4(z+\epsilon)}$ by the chosen polynomial converges in empirical expectation by the joint law and the available higher moments. The genuine activation is 1-Lipschitz in $x$, and $\|K\|\le1$, so errors propagate in normalized $\ell_2$ with at most the sum of the stage errors. Gaussian variances of the polynomial stages converge to the displayed recursion as the approximation errors go to zero. Indeed, standard deviation is the $L^2$ distance to constants, and changing $s g$ to $s' g$ changes the true activation by at most $|s-s'|\,|g|$. For unbounded $Z$ truncate it first. The change in activation at fixed $v$ is bounded by $2|\sqrt{Z+\epsilon}-\sqrt{(Z\wedge L)+\epsilon}|$, which goes to zero in $L^2$ as $L\to\infty$. The same normalized $\ell_2$ comparison removes this truncation at fixed depth.

In particular the expected signed log test tends to zero at every fixed depth:

$$\frac2n\mathbb E\sum_i Z_i\operatorname{arsinh}\frac{v_{t,i}}{2\sqrt{Z_i+\epsilon}}\longrightarrow0.$$

For bounded $Z$ the test is Lipschitz in the iterate. For unbounded $Z$, on $Z>L$ use the bound $|2Z\operatorname{arsinh}(v/(2\sqrt{Z+\epsilon}))|\le\sqrt Z|v|$ and Cauchy–Schwarz with the bounded normalized second moment at fixed depth. On the other coordinates, comparing exact and truncated iterations costs at most the product of the normalized $\ell_2$ difference and the normalized $\ell_2$ norm of $\sqrt Z$.

## Comparing damped and undamped fixed points

For every fixed $0<\alpha<1$ the nonlinear map is a contraction, with a depth truncation bound uniform in expected normalized $\ell_2$. The signed cancellation above therefore holds for its exact fixed point $v_\alpha$. The limiting second moment is bounded uniformly in $\alpha<1$. Indeed $\mathbb E\sqrt{s_t^2g^2+4w}\ge s_t\sqrt{2/\pi}$, so the reference recursion gives $s_{t+1}^2\le(1-2/\pi)s_t^2+4\mathbb Ew$. Thus $\limsup_n\mathbb E\|v_\alpha\|_{2,n}^2\le2\pi\mathbb Ew$ for each fixed $\alpha<1$.

Let $u_\alpha=\sqrt{v_\alpha^2+4w}$, $\gamma_{\alpha,i}=\operatorname{arsinh}(v_{\alpha,i}/(2\sqrt{w_i}))$, and write $*$ for the undamped solution. With $W=\sum_i w_i$, the fixed-point equations give

$$n\overline u_\alpha^{\,2}+(1-\alpha^2)\|\Pi u_\alpha\|_2^2=4W,\qquad n\overline u_*^{\,2}=4W.$$

The pointwise identity $u_{\alpha,i}u_{*,i}-v_{\alpha,i}v_{*,i}=4w_i\cosh(\gamma_{\alpha,i}-\gamma_{*,i})$ and $\langle v_\alpha,v_*\rangle=\alpha\langle\Pi u_\alpha,\Pi u_*\rangle$ imply

$$4\sum_i w_i\big(\cosh(\gamma_{\alpha,i}-\gamma_{*,i})-1\big)
\le (1-\alpha)\langle\Pi u_\alpha,\Pi u_*\rangle.$$

Consequently removal of nonlinear damping in the signed log test follows from

$$\lim_{\alpha\uparrow1}(1-\alpha)\limsup_n\frac1n\mathbb E\langle\Pi u_\alpha,\Pi u_*\rangle=0.$$

## Gaussian concentration at a fixed Poisson intensity

Fix $c>0$ and $\epsilon>0$. Let $Z$ have the compound Poisson law of intensity $c$ with mean-one exponential jumps. The law of $\nu=\sqrt{Z+\epsilon}$ is a Lipschitz image of a standard Gaussian, with constant depending on $c,\epsilon$. To see this, write its underlying compound Poisson density on $z>0$ as

$$f_c(z)=e^{-c-z}\sum_{m\ge1}\frac{c^m z^{m-1}}{m!(m-1)!}.$$

Write the sum as $h(z)$. Under the probability weights of its terms, indexed by $j=m-1$, the identity $\mathbb E[j(j+1)]=cz$ follows by shifting the index. Therefore $0\le h'(z)/h(z)=\mathbb E j/z\le\sqrt{c/z}$. For $z\ge4c$ the derivative of $\log f_c$ lies in $[-1,-1/2]$. Its survival function $\overline F_c$ thus satisfies $f_c(z)\le\overline F_c(z)\le2 f_c(z)$ in that range. Also $f_c(z)\ge c e^{-c-z}$.

Couple $z$ with the standard normal coordinate $g$ by the increasing quantile map. Below the atom threshold for $Z=0$ the map for $\nu$ is constant. On the continuous part its derivative is $\phi(g)/(2\sqrt{z+\epsilon}\,f_c(z))$, where $\phi$ is the normal density. This is bounded on compact $z$ intervals, including the limit as $z\downarrow0$. For large $z$, the Gaussian Mills bound and the survival ratio above give a derivative at most $C(1+g)/\sqrt{z+\epsilon}$. Moreover $c e^{-c-z}\le\overline F_c(z)=\overline\Phi(g)\le e^{-g^2/2}$ for $g\ge0$. Thus the derivative is bounded at large $z$ as well. The quantile map is continuous at the atom threshold and has a finite global Lipschitz constant $L_{c,\epsilon}$.

For the undamped smoothing solution, $u_{*,i}=2\nu_i\cosh\gamma_{*,i}$. The [weighted response identity](marked-response.md#weighted-complementary-projections) gives $d\gamma_{*,i}=(R\,d\nu)_i/\nu_i$, with $R=\Pi_+-\Pi_-$ and $\|R\|\le1$. Therefore

$$\big\|\nabla_\nu\log u_{*,i}\big\|_2\le 2/\nu_i\le2/\sqrt\epsilon.$$

Since $\nu_i\ge\sqrt\epsilon$, this gives a global Lipschitz bound on the positive-floor domain. Compose with the independent Gaussian quantile representations. The resulting function $\log u_{*,i}$ has Euclidean Lipschitz constant $B=2L_{c,\epsilon}/\sqrt\epsilon$, uniformly in $n$. The Gaussian concentration moment bound and Jensen's inequality give

$$\mathbb E u_{*,i}^2\le e^{2B^2}\big(\mathbb E u_{*,i}\big)^2.$$

The finite-field problem is translation invariant in frequency and the input law is iid, so the expectation on the right is independent of $i$. The exact total mass implies $\mathbb E u_{*,i}=2\mathbb E\sqrt{W/n}\le2\sqrt{c+\epsilon}$. This proves a uniform expected normalized squared norm bound for the undamped spectrum. [Gaussian concentration moment bound](https://www.numdam.org/item/SPS_1999__33__120_0.pdf)

Together with the damped norm bound, this controls the pairing by Cauchy–Schwarz and proves the damping removal condition. Since $Z_i\le w_i$, Cauchy–Schwarz and $\cosh x-1\ge x^2/2$ transfer the weighted signed log test at positive floor. The entropy identity bounds the absolute difference between $F(Z)$ and $2\sum_i Z_i\gamma_{*,i}$ by $n\epsilon$. For $W_Z=\sum Z_i>0$, the sum of the two optimality gaps is $W_Z\log((W_Z+n\epsilon)/W_Z)+\sum_{i:Z_i>0}Z_i\log(Z_i/(Z_i+\epsilon))\le n\epsilon$. At $W_Z=0$ both expressions vanish. Sending $\epsilon\downarrow0$ proves $G_n(cn)\to0$. The same argument with intensity $c$ and the dimension-free Poisson comparison at integer $\lfloor cn\rfloor$, or the bound on $G_n'$ to bridge the unit difference, gives $a_{\lfloor cn\rfloor}\to0$ for every $c>0$.

In fact $\sup_{k\ge cn}|a_k|\to0$ at each fixed $c>0$. On compact positive ranges of $k/n$, the harmonic bound $|a_{m+1}-a_m|\le1/(m+1)$ supplies a uniform modulus from a finite grid of ratios. At larger ratios use $|a_k|\le 2(n-1)/(k+1)$. Thus the dense scale's full signed contribution vanishes in the rank expansion. This holds for prime and square orders. The concentration and universality bounds used here depend on the fixed intensity, so the regime $k/n\to0$ remains open.

For $c\ge\log2$, the [localized dimension estimate](rank-partitions.md#the-densely-sampled-regime) further implies that the signed exterior counts themselves have vanishing weighted sum on this scale:

$$\sum_{k\ge\lceil cn\rceil}\frac{\mathbb E[|I_+|-|I_-|]}{k(k-1)}\longrightarrow0.$$

This follows by subtracting the dimension correction and the constant $-1$ in the exterior partition formula from the rank expansion tail.

## Prime and square comparisons

The [fixed-count runs](../data/multiweights-fixed.csv) measure $a_k$, and the [size-biased Poisson runs](../data/multiweights-poisson.csv) measure $G_n(t)$. The floor mass is $0.001$. Each multi-label row uses 32 draws with the same seed across orders. The table shows interval midpoints followed by Monte Carlo standard errors.

| Field order | $a_1$ | $a_2$ | $a_4$ | $G_n(1)$ | $G_n(4)$ |
|---:|---:|---:|---:|---:|---:|
| $97^2$ | $0.6715$ | $0.2205\pm0.0419$ | $0.0108\pm0.0093$ | $0.3712\pm0.0533$ | $0.0607\pm0.0342$ |
| $9413$ | $0.0009$ | $0.0132\pm0.0053$ | $0.0027\pm0.0061$ | $0.0043\pm0.0052$ | $-0.0019\pm0.0061$ |
| $193^2$ | $0.6818$ | $0.1888\pm0.0284$ | $0.0218\pm0.0087$ | $0.3844\pm0.0525$ | $0.0469\pm0.0270$ |
| $37253$ | $-0.0008$ | $-0.0023\pm0.0031$ | $0.0019\pm0.0038$ | $-0.0003\pm0.0020$ | $0.0018\pm0.0027$ |

At $q=193^2$ the inferred first rank term $a_1-a_2$ is approximately $0.493$, close to its upper bound $(1-1/n)/2$. At the matched prime its estimate is $0.0015$ with sampling standard error about $0.0031$. The square samples localize most of the observed discrepancy to the first few draws. The larger sample counts and the finite field sizes still need asymptotic control.

All 35 small-case FFT log intervals contained the independently computed log difference from the dense positive log solver, up to $10^{-7}$, and all 140 damped pairing inequalities held in the small-case checks. A finite-difference check of the gradient of $\log u_{*,i}$ gave maximum discrepancy $2\times10^{-8}$ over 924 coordinate tests. In a separate check at the four table orders, the variance recursion was evaluated by Gaussian and gamma quadrature for Poisson intensities $0.5$ and $2$, floor $0.15$, and damping $0.9$. Across 16 draws per setting at depths $1,2,4,8,16$, the maximum error of a sample mean variance from its reference was $0.011$, and the largest absolute sample mean signed log test was $0.0066$.

The [independent audit](parallel-audit.md) checks the polynomial traffic transfer, the exact projection and the log concentration. It also gives a lower bound on the deterioration of the sub-Gaussian constant as the intensity goes to zero, and a positive sparse Poisson signed objective at square orders. The [bounded-mark damping argument](sparse-damping.md) uses a separate arithmetic input at the other end of the sample range.
