# A quadratic Jacobi test for the actual stationary mark

At real floor \(t=1\), the physical stationary marks satisfy

\[
\limsup_{p\to\infty}|m_p(1)|\le \log(22731/20000)<0.128
\]

through all primes \(p\equiv1\bmod4\). The same estimate holds through the eligible squares. The improvement uses an exact Fourier-sector equation for a quadratic Jacobi column. An explicit reciprocal model at \(m=\log(57/50)\) meets **all** affine moment constraints of [round 41](astra-branch-41.md), so that improvement cannot come from those constraints alone.

At square orders and every sequence of moving floors \(t_q\downarrow0\), the square-root Jacobi test also improves the upper bound on the normalized minus mark loss from \(0.11167\) to \(0.105\). The same moving-floor estimate through primes requires a sufficiently small logarithmic gap to the Jacobi trial. The argument concerns real positive floors and does not provide a common complex domain.

## An exact extra moment

Use the [round-41 normalization](astra-branch-41.md), with \(q=2n+1\), \(W=1+(1-1/n)t\), \(P_+,P_-\) the actual mean-one stationary spectra, and \(E=n^{-1}\sum_{i\ne0}\). Thus \(P_{+,i}P_{-,i}=t/W\) in the bulk, and \(E P_\sigma\to1\). Write \(k_i=\lambda_i/\sqrt q\), \(h_i=2k_i^2-1\), and \(y_i=(Kh)_i\). Put \(u_\sigma=h-\sigma y\).

Since \(K P_\sigma=\sigma(P_\sigma-\mathbf1)\) and \(K\) is symmetric, the exact full-field identity is

\[
\frac1n\sum_i u_{\sigma,i}P_{\sigma,i}=\frac1n\sum_i h_i.
\]

The bulk law of \((k_i,y_i)\) is \((X,Y)\), where \(X\) is arcsine on \([-1,1]\), and \(Y\) is independent of \(X\) and is the sum of two independent semicircles on \([-1,1]\). This is the first two coordinates of [the compact law](joint-law-32.md), rescaled by \(k=(\sqrt n/\sqrt q)x\), \(y=(2n/q)K(x^2)\). In particular \(|y_i|\le2+O(q^{-1/2})\) at every unmarked coordinate by the pointwise aliases in that law. In addition \(y_0=(\sqrt q/n)\sum_i k_i h_i=O(1)\), since \(X(2X^2-1)\) has mean zero and the polynomial mean error is \(O(q^{-1/2})\). The elementary Jacobi trial on the other side gives \(P_{\sigma,0}=O(\sqrt n)\) at every floor by the cross inner product and positivity. Finally \(E(2k^2-1)=O(q^{-1/2})\). Consequently

\[
E[u_\sigma P_\sigma]=O(q^{-1/2})
\]

uniformly over real positive floors. This step uses the exact sector, so it does not assume that a stationary row samples the joint bulk law according to counting measure.

For a fixed positive floor \(t\), set \(A=1/\sqrt{2(1+t)}\) and take any subsequential physical limit \(m\). By the exact first moments of [round 41](astra-branch-41.md), for \(f=1-aX+b(2X^2-1-Y)\) and \(g=1+cX+d(2X^2-1+Y)\) nonnegative on \([-1,1]\times[-2,2]\), we obtain

\[
(1-aAe^m)(1-cAe^{-m})\ \ge\
\frac{t}{1+t}\big(\mathbb E\sqrt{fg}\big)^2.                  \tag{1}
\]

Indeed use the actual columns \(f_i=1-ak_i+b\,u_{+,i}\) and \(g_i=1+ck_i+d\,u_{-,i}\) in bulk reciprocal Cauchy–Schwarz. Add \(q^{-1/4}\) to each finite column if needed to keep the bulk values nonnegative for all sufficiently large fields. The addition costs \(o(1)\) on the left since \(E P_\sigma\le1\). Their counting expectations of the square-root product converge by the joint compact law. The mark is excluded from both sides of this Cauchy–Schwarz estimate.

## The bound at floor one

Choose
\[
(a,c,b,d)=(19/20,\ 143/200,\ 1/20,\ 9/100).
\]

For \(f\), the lower envelope in \(Y\) is decreasing in \(X\) and is zero at \(X=1\). For \(g\), the lower envelope is increasing and is \(39/200\) at \(X=-1\). Also \(f+g\le2+|c-a|+b+d+2|d-b|<5/2\), and hence \(0\le fg\le(5/4)^2\).

The [exact rational checker](quadratic-mark-42-check.py) proves \(\mathbb E\sqrt{fg}>39713/50000\). At \(t=1\) the left side of (1) is \((1-ae^m/2)(1-ce^{-m}/2)\), strictly decreasing for \(m\ge0\), since \(a>c>0\). At \(e^m=22731/20000\) it is already smaller than \((39713/50000)^2/2\), so all such nonnegative limits are excluded. For negative \(m\) exchange the tests and apply \((X,Y)\mapsto(-X,-Y)\), which preserves the model and changes \(m\) to \(-m\). The strict margin at the threshold gives the claimed prime bound and its square counterpart. In particular, the lower bound for \(\exp(16/125)\) through its fourth Taylor term exceeds \(22731/20000\).

## Why all affine tests leave a larger mark

Take \(u=57/50\), let \(X\) have the arcsine law, and set

\[
v=(u+u^{-1})X+\tfrac{59}{100}(2X^2-1)+\tfrac25(4X^3-3X),\quad
w_0=\sqrt{\tfrac12+v^2/4}.
\]

Put \(a_0=1-\mathbb E w_0\), \(c_0=(u-u^{-1})/2-2\mathbb E[Xw_0]\). The two other bounds in the checker for this model give \(a_0>9/10000\) and \(|c_0|<1/5000\). Thus \(w=w_0+a_0+c_0X\ge w_0\). The pair \(p=w+v/2,\ q=w-v/2\) is positive, has means one, has first moments \(u/2,-u^{-1}/2\), and satisfies \(pq\ge1/2\).

To obtain exact reciprocity, let \(\varepsilon\) be an independent fair sign and put \(P=p(1+\varepsilon\sqrt{1-1/(2pq)})\), \(Q=1/(2P)\). Their conditional means given \(X\) are \(p,q\). This realizes the full affine constraints at \(m=\log u>\log(22731/20000)\), even with pointwise reciprocity. It does not obey the added quadratic Fourier condition and is not a field stationary row.

## Moving cold floors

For \(q\) square let \(L_-=\theta_-=(\sqrt q+1)/2\), the exact Jacobi trial mark. Let \(t_q\downarrow0\) at any rate and put \(w_i=1+(41/50)k_i+(11/100)u_{-,i}\). Its bulk compact lower bound is at least \(7/100\) because the lower envelope in \(Y\) is increasing in \(X\). Hence the finite bulk weights are eventually positive. As in [round 41](astra-branch-41.md), stationarity against the same-side Jacobi trial \(l_-\) gives

\[
\frac{L_-/P_{-,0}-1}{t_q}=1-1/n-E[l_-/P_-].
\]

In particular \(P_{-,0}/L_-\to1\). The exact first and quadratic moments then give \(E[wP_-]\to1-(41/50)/2\), since \(E[kP_-]\to-1/2\). By Cauchy–Schwarz

\[
E[l_-/P_-]\ \ge\ (E\sqrt{l_-w})^2/E[wP_-].
\]

In the limit the numerator square is \((\mathbb E\sqrt{(1-X)(1+\frac{41}{50}X+\frac{11}{100}(2X^2-1+Y))})^2\). Under the substitution \(X=2z^2-1\) with \(0\le z\le1\), the measure multiplied by \(\sqrt{1-X}\) is \(2\sqrt2/\pi\) times Lebesgue measure \(dz\). The checker proves that the latter probability integral, with the independent \(Y\), exceeds \(80747/100000\). Using \(\pi<22/7\) and \(\log x\le x-1\) yields

\[
\limsup_{q\to\infty}\frac{\log(\theta_-/P_{-,0}(t_q))}{t_q}
\le 1-\frac{8(80747/100000)^2}{(22/7)^2(1-(41/50)/2)}
<0.105.                                                       \tag{2}
\]

The same proof on either prime sign applies when \(\log(\theta_\sigma/L_\sigma)=o(t_q)\), with \((k,y)\mapsto(-k,-y)\) for the other sign. That assumption is used only to pass from the Jacobi trial mark to the true cold optimum. The pointwise bound (1) requires no such assumption.

The entire normalized test family (1) leaves every compact subinterval of the elementary cold range \((-\tfrac12\log2,\tfrac12\log2)\) admissible at all sufficiently small \(t\). In fact nonnegativity forces \(|a|,|c|\le1\), by taking \(X=\pm1,Y=1\) for \(f\), and \(X=\pm1,Y=-1\) for \(g\). Thus for \(|m|\le M<\tfrac12\log2\), the left side of (1) is at least \((1-e^M/\sqrt2)^2\). Since the two test means are one, Cauchy–Schwarz bounds its right side by \(t/(1+t)\), uniformly over the coefficients. This explains why improving the fixed-floor numerical bound alone with these columns cannot force cold cancellation.

## Arithmetic of the checks

For \(0\le z\le R^2\) put \(r=1-z/R^2\). The binomial expansion is \(\sqrt z=R(1-\sum_{j\ge1}c_j r^j)\), \(c_1=1/2\), \(c_{j+1}/c_j=(2j-1)/(2j+2)\). Truncation at degree \(D\) gives an upper bound; subtracting \(R(1-\sum_{j\le D}c_j)r^D\) gives a lower bound. Use the exact arcsine moments \({2h\choose h}/4^h\) and semicircle moments \({2h\choose h}/(4^h(h+1))\), zero at odd powers, and binomial convolution for the sum of the two semicircles. The third check uses the exact moments of \(2z^2-1\) for uniform \(z\in[0,1]\). The [three records](quadratic-mark-42-checks.jsonl) use rational polynomial expectation and comparison throughout.

These are constraints on actual stationary values at real floors. A common cold complex continuation domain through primes, control of higher signed jets, and the ordinary-theta limit remain open.
