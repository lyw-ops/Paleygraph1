# Cross-floor certificates for the stationary smoothing path

For [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), two true stationary spectra at different floors give nonnegative coordinate contributions to each side of an exact parameter integral. The total of the two sides is explicit. This gives two options: certify one sign at a time, using different floors and caps, or compare the signs on a common cap. On a fine mesh the latter discards the **signed** contribution at large bulk coordinates at a uniform cost, even when the two unsigned contributions cannot be shown to be small. A second version uses a bulk pairing of the true two-floor inverse column. These are reductions to scalar cancellation through primes; none establishes that cancellation.

## Directed gains between two true stationary pairs

Use $K^2=P=I-J$, $n=(q-1)/2$, $c=1-1/n$, $w_0(t)=1$, $w_i(t)=t/n$ off the mark, and $W_t=1+ct$. Write $A_{s,i}(t)=\sqrt{w_i(t)}e^{s\gamma_i(t)}$, $s=\pm1$, for the positive stationary pair, and $m(t)=\gamma_0(t)$, $g(t)=n^{-1}\sum_{i\ne0}\gamma_i(t)$. The marker extends to $t=0$ with $m(0)=\log(\vartheta(\overline H_q)/\sqrt n)$, and the [leverage bound](marked-response.md#an-integral-for-the-conjectured-limit) gives $|m(a)-m(0)|\le\tfrac12\log W_a$. In this note $s=+$ is the theta side.

Normalize to mean one, $P_{s,i}(t)=\sqrt{n/W_t}\,A_{s,i}(t)$. By the [log optimization](marked-response.md#weighted-complementary-projections), the value of the weighted log objective on side $s$, after subtracting $\frac12\log n$, is

$$F_s(t)=\sum_i w_i(t)\log P_{s,i}(t)-\tfrac12\log n
=F_0(t)+s[m(t)+t g(t)],\qquad
F_0(t)=\tfrac{ct}2\log t-\tfrac{W_t}2\log W_t.$$

Each $F_s$ is convex as a maximum of affine functions in $t$. Its derivative is $n^{-1}\sum_{i\ne0}\log P_{s,i}(t)$, either by stationarity or by $m'=-t g'$ from the [mixed product](bulk-logarithm.md#exact-comparison-between-two-weights). In particular

$$t(F_+''+F_-'')=c/W_t,\qquad t(F_+''-F_-'')=2t g'(t)=-2m'(t). \tag{1}$$

For $a,b>0$ define the directed gain $G_s(a\leftarrow b)=F_s(a)-F_s(b)-(a-b)F_s'(b)$, and put $L_{s,i}=\log(P_{s,i}(b)/P_{s,i}(a))$, $\phi(x)=e^x-1-x$. The product of opposite mean-one spectra has sum $n$ even at different floors. Using $w_i(a)/P_{s,i}(a)=(W_a/n)P_{-s,i}(a)$, this says $\sum_i w_i(a)e^{L_{s,i}}=W_a$. Hence

$$G_s(a\leftarrow b)=\sum_i w_i(a)\phi(L_{s,i}). \tag{2}$$

Each term is nonnegative. The reverse direction uses $w_i(b)$ and $-L_{s,i}$. Formula (2) uses the exact stationarity product, not an identity for two unconverged trial diagonals.

For $a<b$, the contribution of this interval to the integral of $tF_s''$ is exactly

$$I_s[a,b]=\int_a^b tF_s''(t)\,dt
=\frac{bG_s(a\leftarrow b)+aG_s(b\leftarrow a)}{b-a}. \tag{3}$$

Indeed $G_s(a\leftarrow b)=\int_a^b(t-a)F_s''(t)\,dt$ and the reverse gain has kernel $b-t$. In particular

$$I_++I_-=\log(W_b/W_a),\qquad I_+-I_-=2[m(a)-m(b)]. \tag{4}$$

At finite order the interval contributions are additive. To give a lower certificate $C_s$ for $I_s[0,b]$, choose any disjoint intervals inside $(0,b]$, and sum lower bounds on (3), for instance retaining any subset of terms in each direction of (2). The two signs can use different intervals, grids, and coordinates. Integration down to zero is valid by (1), since each nonnegative density $tF_s''$ is bounded by $c/W_t$. The resulting theta bracket is

$$m(b)+C_+-\tfrac12\log W_b\ \le m(0)\ \le m(b)+\tfrac12\log W_b-C_-. \tag{5}$$

Take a large **fixed** $b$ with $m_q(b)\to0$ using the [large-floor argument](bulk-logarithm.md#an-integral-with-a-uniformly-integrable-integrand). Then $\liminf_{q\to\infty}C_s\ge\frac12\log(1+b)$ for just one sign suffices for its corresponding bound. The two proofs need no floor at which both signs are certified. More generally one can allow an additive deficit and send it to zero after the field limit. The lower certificate can omit any interval of small total $\int c/W_t\,dt$, including $(0,a)$ at cost at most $\log W_a$. A fixed coarse certificate may miss substantial unsigned gain; (2) gives a lower bound, not automatic convergence to half the budget.

## The signed cap costs only density and mesh

There is a stronger localization when the signs are compared on the *same* kept coordinates of a given interval. Let $I_{s,i}$ denote the summand of (3) given by (2), and set $d_i=\gamma_i(a)-\gamma_i(b)$. Off the mark $L_{s,i}=k-s d_i$ where $k=\tfrac12\log(bW_a/(aW_b))$. The coefficients of $\phi(L_{s,i})$ and $\phi(-L_{s,i})$ in (3) are both $ab/[n(b-a)]$. In particular the signed bulk summand simplifies exactly:

$$I_{+,i}-I_{-,i}=-\frac{2\sqrt{ab}}{n\sqrt{W_aW_b}}\sinh d_i,\qquad i\ne0. \tag{6}$$

Here $\phi(x)+\phi(-x)=2(\cosh x-1)$ and $\sinh k=(b-a)/(2\sqrt{ab W_aW_b})$. No small logarithmic increment is assumed sitewise.

The two exact mixed products imply

$$
\cosh d_0-1+\frac{\sqrt{ab}}n\sum_{i\ne0}(\cosh d_i-1)=\Delta_{ab},\qquad
\sinh d_0+\frac{\sqrt{ab}}n\sum_{i\ne0}\sinh d_i=0,
$$

$$\Delta_{ab}=\sqrt{W_aW_b}-1-c\sqrt{ab}\le\tfrac c2(\sqrt b-\sqrt a)^2. \tag{7}$$

For any omitted bulk set of density $r$ (cardinality divided by $n$), (6), $|\sinh x-x|\le\cosh x-1$, and $x^2\le2(\cosh x-1)$ bound its signed contribution in absolute value by

$$\frac{2}{\sqrt{W_aW_b}}\left(\sqrt{2r\sqrt{ab}\,\Delta_{ab}}+\Delta_{ab}\right). \tag{8}$$

One cap keeps the mark and sites where $\sqrt n\max(u_i(a),u_i(b))\le M$, where $u(t)=A_+(t)+A_-(t)$. On every interval up to a fixed $b_*$, the omitted density is at most $4\sqrt{W_{b_*}}/M$ by the mass identities. Sum (8) along any mesh of $[a_*,b_*]$, $0<a_*<b_*$, of maximal step $h$ in $\sqrt t$. The total error is $O_{b_*}(M^{-1/2}+h)$, uniformly in $a_*$ and in the field. This estimate is for the signed difference. The two unsigned omitted budgets can be as large as the squared increment budget at each step; bounding their sum by the same expression would require more input. Also the mark stays in the cap for (8). To avoid using a marked summand as part of the cancellation test, the next version uses only a bulk pairing.

## A bulk scalar of the true two-floor inverse

Set $v(t)=A_+(t)-A_-(t)$, $V(t)=v(t)/\sqrt t$, and $\kappa_t=u_0(t)/\sqrt t=2\cosh m(t)/\sqrt t$. The scaled solutions now have a common bulk weight $1/n$. For $a<b$ form $E_0=0$, $E_i=\tanh((\gamma_i(a)+\gamma_i(b))/2)$ on the bulk, with $M_E=(I-E^2)^{1/2}$. Put $X_E=(K-PEP)^{-1}P$ with the inverse on the mean-zero space, and $e=Pe_0$. The [true secant](stationary-secant.md#the-exact-inverse-column) is

$$V(a)-V(b)=(\kappa_a-\kappa_b)X_E e. \tag{9}$$

In fact the normalized difference of the two $u$ coordinates is $E_i$ times the normalized $v$ difference off the mark. At the mark the normalized $u$ difference is $\kappa_a-\kappa_b$. Write $R(t)=-2t m'(t)$ for the signed marked leverage, with $|R(t)|\le ct/W_t$. Differentiating gives $\kappa_t'/\kappa_t=-(1+R(t)\tanh m(t))/(2t)<0$. Thus there is no division by a zero secant denominator.

At a bulk site the half-difference of the logs satisfies $M_{E,i}(V_i(a)-V_i(b))=4\sinh(d_i/2)/\sqrt n$. For $f=\mathbf 1_{\mathrm{bulk}}/\sqrt n$, use (7) and $|\sinh x-2\sinh(x/2)|\le\cosh x-1$ to get

$$\left|m(a)-m(b)+\alpha_{ab}\langle f,M_E X_Ee\rangle\right|\le\Delta_{ab},\qquad
\alpha_{ab}=\tfrac12\sqrt{ab}(\kappa_a-\kappa_b)>0. \tag{10}$$

The [weighted inverse contraction](response-locality.md#contraction-and-response-derivative) gives $\|M_E X_E e\|_2\le1$: apply $M_E X_E M_E-E$ to the marked unit vector, since $E_0=0$. Thus in (10) one can replace $f$ by $f$ restricted to the bulk cap at cost $\alpha_{ab}\sqrt r$. This is a bound on the error from discarding sites in a particular pairing; it gives no absolute inverse spectral tail estimate. On $0<a_*\le a<b\le b_*$ with mesh ratios $b/a\le2$, the sum of $\alpha_{ab}$ is $O_{b_*}(1)$ uniformly as $a_*\downarrow0$. Indeed $|\kappa_t'|\ll_{b_*}t^{-3/2}$ by the displayed derivative and the uniform mark bound, and $\sqrt{ab}\le\sqrt2,t$ throughout each interval.

In particular, on a mesh of $[a_*,b_*]$ as above, put $\mathcal S=\sum_{[a,b]}\alpha_{ab}\langle f_{ab,M},M_E X_E e\rangle$, where $f_{ab,M}$ is $f$ restricted to the kept sites. Then

$$|m(0)-m(b_*)+\mathcal S|\le \tfrac12\log W_{a_*}+O_{b_*}(h+M^{-1/2}). \tag{11}$$

It would suffice to bound just the sum of the signed capped pairings, with $q\to\infty$ first at fixed mesh and cap, then $h\to0$, $M\to\infty$ and $a_*\downarrow0$. The two directions of (11) can use different meshes. This is a bulk test on true secant columns, with their actual weight $M_E$, instead of finite-time agreement for the true half-angle or convergence of its undamped marked spectral tail at each floor. Taking limits in a damped computation of $\mathcal S$ would still require control of its *signed* regularization error; the contraction bound alone does not give it. Equivalently one can test weighted signed increments of the logs on the kept sites. Neither time evolution nor an inverse is necessary to define that test.

There is also local compactness directly in the floor. With a uniformly sampled bulk coordinate, the log paths are tight in $C([a_*,b_*])$ for fixed $a_*>0$. Indeed (7), divided by the squared step and sent to the diagonal, gives $n^{-1}\sum_{i\ne0}|\gamma_i'(t)|^2\ll_{a_*,b_*}1$. The exponential first-moment bound of [bulk-logarithm](bulk-logarithm.md#an-integral-with-a-uniformly-integrable-integrand) bounds the squared log at $a_*$. An integrated squared derivative bound gives a $1/2$-Hölder modulus by Cauchy–Schwarz, so Markov's inequality and Arzelà–Ascoli give tightness. Log means and fixed log increments pass to these laws by uniform integrability. One may ask only for cancellation of the integrated signed mean in any such limiting law (or of its signed mesh functional), without tightness of the uncapped total spectrum. Compactness does not force the limit law to be symmetric. Nor does a normalized $\ell_2$ modulus for the diagonal by itself justify continuity of arbitrary inverse or higher-word tests.

## Fixed and decreasing floors; the square control

For comparison the *marked* secant $h_{ab}=\langle e,X_E e\rangle$ gives a different averaging law. If $[a,b_*]$ is partitioned, (9) telescopes to

$$\tanh m(a)=\frac{\kappa_{b_*}}{\kappa_a}\tanh m(b_*)+
\sum_{[l,r]}\frac{\kappa_l-\kappa_r}{\kappa_a}h_{lr}. \tag{12}$$

All weights are positive and their sum, including the endpoint, is one. In particular, in the [signed time representation](parallel-sign-4.md#exact-tail-and-certificates-for-cancellation) one can combine prefixes and signed tails for the true $E(l,r)$ using these weights. It is the weighted signed sum that matters for each direction; neither a common time cutoff nor a uniform bound on the absolute tail at every pair is imposed by (12). At $b_*=n$ the normalized solution at $b_*$ is constant, so the single secant is just the true half-angle. That choice alone gains no new cancellation.

If $0<a<b\to0$ jointly with the field, (12) must not be interpreted as the fixed-floor, field-first test. In fact $h_{ab}=\tanh m(0)+O(b)$ uniformly even as $b/a\downarrow1$. To see this, the derivative ratio for the normalized mark is

$$\frac{(V_0(t))'}{\kappa_t'}=\frac{\tanh m(t)+R(t)}{1+R(t)\tanh m(t)}.$$

Average the ratio with the positive measure $-d\kappa_t$ and use the leverage and marker bounds. If only $a\to0$ and $b$ is fixed positive, (9) instead gives $h_{ab}-\tanh m(0)\to0$ because $\kappa_a\asymp a^{-1/2}$, whereas $\kappa_b=O_b(1)$. Log path tightness on a positive compact interval gives no tightness of the logs at such moving floors. In the integral test the region $(0,a_*)$ costs $O(a_*)$ for either sign; it can be discarded without any estimate of the moving-floor inverse. Its small contribution does not mean $m(0)$ is small: the rest of the path is what sets that value.

For the [square fields](square-order-control.md#a-square-order-comparison), $q=r^2$ and $\vartheta(\overline H_q)=r-1$. At large fixed $b_*$ with the same large-floor parity input, $m_q(b_*)\to0$. Thus $I_+[0,b_*]-I_-[0,b_*]\to\log 2$. Even for $a_*>0$ fixed and small, the field liminf of the difference on $[a_*,b_*]$ is at least $\log 2-\log(1+a_*)$. This is a fixed-interval obstruction to a field-independent signed balance in (5) or (11). It survives taking a fine mesh and arbitrarily large caps. At small fixed floors the [square bulk witness](parallel-finite-time-6.md#square-order-test-of-the-order-of-limits) makes $n^{-1}\sum_{i\ne0}(1+\tanh\gamma_i(t))$ small in field limsup as $t$ is chosen small. Since each two-floor $E_i$ is between the two endpoint full-angle values, the first signed moment $\langle Ke,EKe\rangle$ is close to $-1$ for two sufficiently small fixed floors, using the Jacobi entry bound. By the fixed-depth parity input the two-floor trial diagonal obtained from the corresponding finite-depth logs has vanishing first moment: it is a bounded Lipschitz odd function of the two scaled bulk iterates at these fixed floors. This is a finite-time transfer obstruction, not a claim of failure of real inverse tightness at every fixed pair.

If both square floors decrease to zero, the [square witness estimate](parallel-coupling-2.md#exact-square-order-control-with-decreasing-floors) implies $\gamma_i(a),\gamma_i(b)\to-\infty$ in bulk probability. Consequently $E\to-1$ in normalized bulk $\ell_2$, while $h_{ab}\to1/3$ by the derivative ratio. If only $a\downarrow0$ and $b$ is fixed, the same bulk limit follows by tightness of the single-floor log at $b$, and the one-moving-endpoint estimate gives the same marked limit. In either case the bounded-time signed density for this stripped secant tends to $-e^{-s}$. To see this, use the [finite-word comparison](parallel-finite-time-6.md#from-capped-comparison-to-all-fixed-signed-moments) with reference diagonal $F=-1$ in the bulk and $F_0=0$. The reference words $(KF)^jKe$ are in the span of $e,Ke$ with bounded coefficients for each fixed $j$, so they are uniformly flat on the bulk. The zeroth reference moment tends to $-1$. Also $KFKe=-e+K_{00}Ke$ and $\|Fe\|=O(n^{-1/2})$, so the first moment and the norms of the words of degree $j\ge2$ tend to zero. The telescoping bound transfers the fixed moments to $E$, and the exponential series transfers the density on bounded intervals. Since the full signed integral tends to $1/3$, its tail at any fixed time $T$ tends to $4/3-e^{-T}$, just as for the decreasing-floor half-angle. Replacing it by zero before taking the field limit would give the wrong secant.

## Finite replay

Six pairs of floors from $0.01,0.025,0.05,0.2,1,8$ were checked at $q=101,9413,23^2,97^2$ with the existing FFT [stationary solver](../smoothing.py). The maximum fixed-point residual was $1.0\cdot10^{-11}$. Substituting the normalized difference into (9) gave a maximum column residual of $2.2\cdot10^{-11}$. The mixed inequality (10) held in all 24 comparisons; the directed gains matched the objective differences within $1.1\cdot10^{-10}$, and both equations in (4) within $4.4\cdot10^{-11}$. The per-coordinate formula (6) agreed within $3.5\cdot10^{-17}$; (8) held in 96 checks with $M=2,4,8,32$. For $[a,b]=[0.01,8]$ the two integral contributions were $(1.09246,1.09463)$ at $9413$ and $(1.42430,0.76279)$ at $97^2$. The cap $M=4$ retaining the mark at both endpoints gave lower certificates $(0.42950,0.43095)$ and $(0.66798,0.22992)$ respectively on this coarse interval. These are floating-point checks, not prime-field estimates.
