# Threshold tests on the actual Picard repair, and a necessary floor–time budget

For every sufficiently large prime $p\equiv1\pmod4$, the true first
clipped reflection at floor $1/5$ and depth $1$ leaves **both** rows
negative on a positive fraction of the bulk, for **every nonnegative
clipping threshold**, even if chosen separately for each field and sign. The test is a signed integral against a nonnegative degree-12
Jacobi polynomial. At this floor the limiting normalized mark is less
than one, so the elementary product of the two marks does not give
this conclusion.

At depth two, the product of the two actual marks does rule out
**every** mark-preserving nonnegative paired completion at every fixed
$0<\tau\le1/10$. For general depth, the field-first limiting budget
improves from $1+\tau+1/T$ to $1+\tau$. The early deviations of the
true arithmetic Picard means impose a strictly positive lower bound
on $T\tau$ along any successful family with floors tending to zero.

These restrictions hold also on eligible square orders. They rule out
routes on all primes in their stated ranges and do not prove the
prime/square separation required for ordinary theta. In this note
$q=2n+1$, $K^2=I-J$, and all spatial averages $E$ use $1/n$.
The symbols $v_t,\phi_t,\mu_t,A_{\sigma,t},X_{\sigma,T}$ use the
[round-35 definitions](averaged-mark-35.md). A normalized row has mean
one, root $X_{\sigma,T}(0)/M_T$, and lies in $1+V_\sigma$.

## 1. Weighted budget with the terminal reserve

Let $g_t=\sqrt n\,\mu_t$, $E_t=\|v_t\|_2^2$ in counting norm, and
$W=1+(n-1)\tau/n$. Take decreasing weights
$\alpha_1\ge\cdots\ge\alpha_T\ge0$, of sum one. Set
$\alpha_{T+1}=0, \beta_t=\alpha_t-\alpha_{t+1}$, and
$G=\sum\alpha_t g_t$. Use the same weights on the one-step projected
rows. All claims about field limits in this section fix $T,\tau$
first. The estimates are uniform over the decreasing simplex at each
such $T$, permitting field-dependent weights. The energy telescope gives

\[
 \sum_t\alpha_t g_t^2
 = W+\tfrac14\left(\alpha_1E_1-\sum_{t=1}^T\beta_t E_{t+1}\right).
 \tag{1}
\]

For $i\ne0$ put $b_{t,i}=\sqrt{\tau+n v_t(i)^2/4}$ and let
$V_t=\operatorname{Var}_{i\ne0} b_{t,i}$, using probability
$1/(n-1)$. The within-bulk and between-group variance decomposition
of $\phi_t$ is exact:
\[
 E_{t+1}/4
 =\tfrac{n-1}{n} V_t
   +\tfrac{n-1}{4n}
       (\phi_t(0)-2E_{i\ne0}b_{t,i}/\sqrt n)^2.
\]
Here $\phi_t(0)=2+o(1)$ by fixed-depth marked cancellation.
The bulk mean is $O_{\tau,T}(1)$ by the energy bounds.
As $E_1/4=(1-\sqrt{\tau/n})^2(1-1/n)=1+o(1)$,
$E_{t+1}/4=1+(1-1/n)V_t+o(1)$. All $V_t=O_{\tau,T}(1)$.
Because $\sum\beta_t=\alpha_1$, (1) becomes
\[
 \sum\alpha_t g_t^2=1+\tau-\sum\beta_t V_t+o(1).
 \tag{2}
\]
In particular $\limsup G^2\le1+\tau$ at every fixed depth. For the
uniform prefix the reserve is precisely $V_T/T$. A one-sided
$E_{t+1}\ge4-o(1)$ follows already from $\phi_t(0)\ge2$ without
any arithmetic input.

If both rows admit nonnegative completions with their prescribed marks
and means, their cross inner product is $n$. Both unnormalized marks
tend to one, so $G\ge1-o(1)$. Substitute (2) into the exact identity
$2(1-G)=\sum\alpha_t(1-g_t)^2+1-\sum\alpha_t g_t^2$ to obtain the
necessary inequality along any completable field sequence
\[
 \sum_t\alpha_t(1-g_t)^2+\sum_t\beta_t V_t\le\tau+o(1).       \tag{3}
\]
The initial arithmetic mean tends to
$m(\tau)=\pi^{-1}\int_0^\pi\sqrt{\tau+2\cos^2 u}\,du$, by the Jacobi
arcsine law. As $\alpha_1\ge1/T$, any schedule with
$T\tau<(1-m(\tau))^2$ admits no such joint completion on any
sufficiently large eligible field. In particular for any successful
field-first family $\tau_j\downarrow0$, $T_j$ chosen after $\tau_j$,
\[
 \liminf_j T_j\tau_j\ge(1-2\sqrt2/\pi)^2.
\]
The statement does not interchange the limits in $q$ and $T$.

At square orders the maximum feasible minus-sector root is
$(\sqrt q+1)/2$. The prescribed normalized minus root divided by
$\sqrt n$ has lower limit at least $1/\sqrt{1+\tau}$, by (2).
Every fixed $0<\tau<1$ therefore rules out that completion on all
sufficiently large squares, **for every fixed depth**. This includes
the old $\tau+1/T<1$ obstruction and the previously uncovered
shallow depths.

## 2. Actual one-step scatter tested against Jacobi incidence

Write $x_q=\widehat s/\sqrt q$ with values in $[-1,1]$, $X=\cos\theta$
for uniform $\theta\in[0,\pi]$, and
$Y_j=(\operatorname{tr}U_j+\operatorname{tr}V_j)/2$ for independent
pairs of Haar compact symplectic matrices of dimension
$2\lfloor j/2\rfloor$, independently over $j\ge2$ and of $X$.
We use the [proved finite joint path laws](parallel-graph-shapes-23.md)
and the [normalized $L^2$ completion](scalar-seed-25.md), especially
$E Y_j^2=1/2$. These fieldwise inputs hold along every prime and
eligible square sequence. They do not identify the distribution of
$K$ applied to a new jointly thresholded field.

Put $f(x)=2\sqrt{\tau+2x^2}$, $g=Ef(X)/2=m(\tau)$, write
$f=2g+\sum_{j\ge2}c_j T_j$ with odd coefficients zero, and put
$S=\sum_{j\ge2} c_jY_j$. The series converges in $L^2$.
The actual scaled first state satisfies
$\sqrt n v_1=2(1-\sqrt{\tau/n})\sqrt{q/n}\, x_q$. To reach the
second state, the excess of the marked activation over the bulk
formula gives a forcing $2\sqrt2 X+o_{L^2}(1)$ in the finite-word
approximation, and $K$ applied to the bulk activation gives $S$.
Specifically,
\[
 \sqrt n v_2=\big[\phi_1(0)-n^{-1/2}f_q(x_q(0))\big]\sqrt{q/n}\, x_q+
                K f_q(x_q),
\]
where $f_q(x)=2\sqrt{\tau+(1-\sqrt{\tau/n})^2(q/n)x^2}$ converges
uniformly to $f$. The bracket tends to 2. Truncating $f$ in the
arcsine $L^2$ norm costs at most that error in the limiting normalized
counting $L^2$ after $K$, by contraction and fixed-polynomial
sampling. The bulk variables can thus be tested jointly with finitely
many $x_q,KT_j(x_q)$ against Lipschitz functions, with the associated
second-moment control. Root contributions have to be removed separately
when the projected normalized row, whose root is large, is tested.

The limiting normalized $T=1$ **bulk** row has law
\[
 B_\sigma=A_\sigma(X)+\frac{\sigma S}{4g},\qquad
 A_\sigma(x)=\frac12+\frac{f(x)}{4g}+\frac{\sigma\sqrt2}{g}x.
 \tag{4}
\]
For example this follows by adding/subtracting the two one-step row
identities in [round 35, (5)](averaged-mark-35.md). The mark of size
$O(\sqrt n)$ contributes $o(1)$ to a bounded test's first moment.
Set $D_\sigma=(\delta-B_\sigma)_+$; this is the limit of the genuine
bulk clipping deficit, with zero at the mark. Its approximation is
controlled by the same $L^2$ error as the input row because the
positive part is 1-Lipschitz.

For a fixed polynomial $h=h_0+h_1x+\sum_{j\ge2} h_jT_j(x)$, let
$h_q=h(x_q)$. Moving the symmetric pinned projection to the test
computes the signed integral of the actual repair $y=z+2L_\sigma d$:
\[
 \lim_q E[h_q y]=E[h(X) B_\sigma]
 + E\left[D_\sigma\left(h(X)-h_0-h_1X+
                      \sigma\sum_{j\ge2}h_jY_j\right)\right].    \tag{5}
\]
Indeed $L_\sigma$ kills $1,x_q$, and for each fixed $j\ge2$ the
round-25 pointwise bulk alias of $2L_\sigma T_j$ is
$T_j+\sigma KT_j+o(1)$. The exact value at the mark is zero.
Cauchy–Schwarz passes the polynomial cutoff approximations. Formula
(5) never approximates the clipped deficit in a norm stable under a
second pointwise evaluation of $K$.

Use $\tau=1/5,\delta=1/500$ and
$h(\sigma x)=(1-\sigma x)^{12}/E(1-X)^{12}$, where below $h$
denotes the plus-sign test. Joint symmetry lets us use $X'=\sigma X$
and $Y'_j=\sigma Y_j$ in (4)–(5). The odd-degree test coefficients
acquire a factor $\sigma^j$, and their expectations against $D$
are zero by independence since $S$ uses only even $j$. The
remaining expressions coincide for the two signs.

Put $A=A_+(X),\ b=c_2/(4g),\ D_2=(\delta-A-bY_2)_+$.
Dropping the higher independent paths in the deficit and then using
Cauchy–Schwarz bounds (5) above by
\[
 \begin{split}
 I_2 + \frac{\sqrt{4(1+\tau)-4g^2-c_2^2/2}}{4g}
                 \sqrt{\sum_{j\ge2}h_j^2},\quad
 I_2= E[Ah +D_2(h-1-h_1X+h_2Y_2)] .                        \tag{6}
 \end{split}
\]
In fact the first square root is the $L^2$ norm of the omitted
paths, and the other is the exact norm of the centered pinned test,
adding the two independent variances $\sum h_j^2/2$. The retained
integral computes the correlation between the clipping decision and
the same $Y_2$ in the signed scatter. Dropping that correlation
would invalidate the calculation.

The [128-bit checker](astra-prime-repair-38.py) encloses (6) by
$-0.01965400\ldots$ from above. It gives $1.03608<g<1.03609$,
so both limiting roots divided by $\sqrt n$ are $1/g<1$.
For details, $Y_2=u+v$ with independent $u,v$ of semicircular
density $2\sqrt{1-u^2}/\pi$. The code uses their exact CDF to
enclose the mass of every mesh cell and convolves the two mass lists.
It integrates $Ah+D_2(h-1-h_1X+h_2Y_2)$ using the first three
truncated moments of this discrete sum. The midpoint value lies
between $-.079560$ and $-.079559$; the geometric integration
error is below .017867, and the omitted-path error below .042040.
The derivative bounds in the checker hold across the hinge by the
Lipschitz product inequality. The normalizations use
$h_j=2(-1)^j {24\choose12-j}/{24\choose12}$ for $j\ge1$.
The arithmetic in the record bounds a limiting compact integral,
not a finite FFT trajectory.

Both signs thus have $E[h_q y]<-.019$ for all sufficiently large
fields. In particular the minimum is below $-.018$ eventually
because $E h_q\to1$. There is also positive density: $\|h_q\|_\infty<7$;
the normalized $L^2$ norm of $z$ is at most
$\sqrt{1+(E_1+4W)/(n\mu_1^2)}<\sqrt{10}$ eventually by projection.
Consequently $\|y\|_{2,n}\le3\|z\|_{2,n}+2\delta<10$.
If $F=\{y<-.009\}$, then
$E[h_q y]\ge-.009Eh_q-70\sqrt{|F|/n}$, forcing a positive
liminf fraction. The positive mark is outside $F$.

### Every nonnegative clipping threshold fails

In fact the same test at the same floor proves
\[
 \limsup_q\sup_{\delta\ge0} E[h(\sigma x_q)y_{\sigma,q}(\delta)]
 \ \le\ -0.0106627,\qquad \sigma=\pm1.                         \tag{6a}
\]
Here $y_{\sigma,q}(\delta)=z_{\sigma,q}+2L_\sigma d_\delta$ and
$d_{\delta,i}=(\delta-z_{\sigma,q,i})_+$ off the mark, $d_{\delta,0}=0$.
This uses the [threshold convolution checker](astra-prime-repair-38-thresholds.py)
and [its separate interval record](astra-prime-repair-38-thresholds.jsonl).

The path truncation error in (6) is independent of $\delta$. For the
retained compact integral, it suffices to check $0\le\delta\le4$.
Indeed $A+bY_2<4$, so beyond 4 the positive part is affine and its
coefficient has mean $E(h-1-h_1X+h_2Y_2)=0$. With $W_h=h-1-h_1X$,
quantize $X$ and $Y_2$ as in the point test, but using $524288$
angular midpoints and $16384$ semicircle bins. Snap $A$ and $bY_2$
separately to the nearest multiple of $1/16384$. The signed mass
at their snapped sum, with weight $W_h+h_2Y_2$, is the sum of two
ordinary one-dimensional convolutions. The first convolves the
$W_h$-weighted law of the first variable with the plain law of the
second. The other convolves the plain first law with the
$h_2Y_2$-weighted second law. Adding $(\delta-s)_+$ times each signed
mass at $s$ to the unrounded base $E[Ah]$ on the angular grid gives
a piecewise affine function of $\delta$. Its maximum on $[0,4]$ is
attained at one of the mesh knots. A prefix sum of masses gives the
slope at each knot. All knots including the endpoints are tested.

The snapped function's largest value is less than $-.05676783$.
The snapping error is bounded by $14(1.000002)/16384$ since the
weight has absolute value less than 14. For the original compact
quadrature the integrand is Lipschitz in $X$ and $Y_2$ with constants
420 and 16, uniformly on this threshold range: $|A'|<2.2$,
$|A|<3$, $|h'|<42$, $(\delta-A-bY_2)_+<5.4$, and
$|W_h+h_2Y_2|<14$. The integral error is below .003212, and the
previous tail error remains .042040. The checker uses the unrounded
bounds and certifies the right side of (6a) for fixed $\delta$.

For compact threshold intervals (5) converges uniformly by
equicontinuity, since the clipped input is 1-Lipschitz in $\delta$
and $\|2L_\sigma h_q\|_{2,n}$ is bounded. To deal with any sequence
$\delta_q\to\infty$, use on the bulk
\[
 d_\delta=\delta-z+(z-\delta)_+ .
\]
The pinned projector kills the constant bulk indicator. The omitted
positive part has mean at most $E z^2/\delta$, uniformly in the
field. The off-mark test $2L_\sigma h_q$ has a uniform sup bound by
its **fixed polynomial** path expansion and its bounded finite-rank
Mellin traces. Therefore the difference from the limiting-in-threshold
pairing is $O(1/\delta)$ uniformly in $q$. Comparing first to a large
fixed cutoff and then sending that cutoff to infinity proves (6a).
This step does not assert a sup bound for the transformed deficit.

Uniformly over $\delta\ge0$ we also have $\|y\|_{2,n}\le3\|z\|_{2,n}$:
subtract $\delta$ times the bulk indicator inside $L$ and use
$|d_\delta-\delta|\le|z|$ there. Thus the preceding positive-density
argument applies simultaneously to all thresholds, for example with
$F=\{i:y_i<-.004\}$ and the eventual expectation upper bound $-.010$.
The previously displayed stronger estimate at the particular
threshold $1/500$ remains valid.

## 3. At depth two, the true marks cannot both be retained at small floors

The previous joint law gives the actual first two limiting means:
\[
 g_1\to m(\tau),\qquad
 g_2\to E\sqrt{\tau+(\sqrt2 X+S/2)^2}.
\]
The single marked activation contributes $O(n^{-1/2})$ to either
mean. All variables in the expectation have the compact-product law
of section 2. Retaining $Y_2$, then applying conditional Jensen
to the concave square root, proves
\[
 \lim g_2\le E\sqrt{\tau+v(\tau)+(\sqrt2 X+c_2(\tau)Y_2/2)^2},
 \quad v(\tau)=1+\tau-m(\tau)^2-c_2(\tau)^2/8.               \tag{7}
\]
Here $v(\tau)=\sum_{j\ge4}c_j(\tau)^2/8$ is the variance of the
omitted paths in $S/2$.

For every $j=2k\ge2$, $|c_j(\tau)|$ decreases as $\tau$
increases. Indeed insert
$\sqrt y=(2\sqrt\pi)^{-1}\int_0^\infty(1-e^{-sy})s^{-3/2}ds$
into the cosine coefficient of $2\sqrt{1+\tau+\cos(2\theta)}$.
Apart from a fixed positive factor and sign $(-1)^{k+1}$, it is
\[
 \int_0^\infty e^{-(1+\tau)s}I_k(s)s^{-3/2}\,ds,
\]
where $I_k(s)=\sum_{m\ge0}(s/2)^{2m+k}/(m!(m+k)!)>0$ from
the two exponential series. Fubini applies directly to $1-e^{-sy}$
by its $O(\min(s,1))$ uniform bound. This includes $\tau=0$.
In particular $v$ decreases and $c_2>0$.
For fixed offset and $X$, the expectation of
$\sqrt{a+(\sqrt2 X+bY_2)^2}$ is an even convex function of $b$,
hence increases for $b\ge0$. On a floor interval $[l,r]$, (7)
therefore holds with floor $r$ and with $v,c_2$ evaluated at
$l$. For $m(\tau)$ take $m(r)$.

| Floor interval | Upper bound on limiting $(g_1+g_2)/2$ |
|---|---:|
| $[0,.05]$ | .969017 |
| $[.05,.08]$ | .985504 |
| $[.08,.10]$ | .997235 |

These [interval records](astra-prime-repair-38-certified.jsonl) use
$1024$ midpoint angles for $X$ and $512$ bins for each
semicircle coordinate. The error on the second mean is at most
$\sqrt2\pi/(2\cdot1024)+c_2(l)/512$ by the 1-Lipschitz property of
$u\mapsto\sqrt{a+u^2}$. At zero, $m(0)=2\sqrt2/\pi$ and
$c_2(0)=4m(0)/3$. The three displayed bounds apply to each fixed
positive floor throughout the indicated closed intervals.

By the inherited fixed-depth marked limit, both prescribed normalized
roots divided by $\sqrt n$ tend to $2/\lim(g_1+g_2)>1/.998$.
Their product divided by $n$ exceeds unity. Hence no nonnegative
paired completion preserving both marks exists on any sufficiently
large prime for these parameters, however many signed reflections are
allowed. The same argument applies on squares. If the two time steps
are given decreasing weights, the obstruction still holds: $\lim g_2
\ge m(\tau)=\lim g_1$ by Jensen on the independent centered $S$
and convexity of the square-root quadratic. The decreasing mixture
therefore has mean at most that of the uniform prefix in the limit.

## 4. Scope and replay

The weighted energy bound precludes all completions in one range of
floors and depths. The signed incidence computation tests the actual
clipped vector and identifies failure in each sign separately where
the product of the prescribed marks permits both. Its finite
low-degree arithmetic inputs also hold on squares. Higher $T$ can
introduce new nested fields inside the threshold, and moving the
projection back to a polynomial test no longer identifies those
joint expectations from the current path-group law. A second actual
reflection introduces $K D$ inside a new threshold, also outside
(5). No independence for these quantities is assumed. The prime
positivity problem at fixed floors and suitably large selected $T$
and the original ETH26 limit remain open.

Replay the five compact integral records with

    .venv/bin/python -B research/astra-prime-repair-38.py
    .venv/bin/python -B research/astra-prime-repair-38-thresholds.py

The recorded decimal values include the stated quadrature and path
bounds where applicable. No stationary-solver output is an input.
