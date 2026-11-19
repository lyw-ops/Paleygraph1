# A half-angle inverse for the stationary vector

Use the Paley Fourier involution $K^2=P=I-J$, the mean-zero source $e=Pe_0$, and weights $w_0=1$, $w_i=\tau/n$ on the bulk, where $0<\tau\le1$. Write $\nu_i=\sqrt{w_i}$, $W=\sum_i w_i$, and let $v=Ku$ be the stationary solution with

$$v_i=2\nu_i\sinh\gamma_i,\qquad u_i=2\nu_i\cosh\gamma_i,\qquad D_i=\tanh\gamma_i.$$

For a strict diagonal $E$, write $H_E=K-PEP$ on the mean-zero space, $X_E=H_E^{-1}P$ for its inverse extension, and $m_E=(X_Ee)_0$. A stripped diagonal has entry zero at the mark.

## The exact inverse column

Let $B$ be the stripped diagonal with $B_i=\tanh(\gamma_i/2)$ on the bulk. Then

$$
\boxed{X_B e=\frac{v}{u_0-2\sqrt{\tau/n}},\qquad
m_B=\frac{v_0}{u_0-2\sqrt{\tau/n}}.} \tag{1}
$$

In fact $K v=Pu$ and $v_i\tanh(\gamma_i/2)=u_i-2\nu_i$. Therefore $H_Bv=P(2\nu)+(u_0-2)e=(u_0-2\sqrt{\tau/n})e$. All inverse columns here are well defined because $\|B\|<1$ and $K$ is an involution on the mean-zero space. In particular $m_B=D_0+O(\sqrt{\tau/n})$ uniformly, so either one-sided or two-sided marked cancellation for $B$ transfers to the stationary marker.

With $a=u_0-2\sqrt{\tau/n}$ the weighted bulk norm has the exact formula

$$
\sum_{i\ne0}(1-B_i^2)(X_B e)_i^2
=\frac{4\sqrt{\tau/n}}{a^2}\sum_{i\ne0}(u_i-2\sqrt{\tau/n})
\ll\sqrt\tau. \tag{2}
$$

Use $(1-\tanh^2(\gamma_i/2))v_i^2=4\nu_i(u_i-2\nu_i)$ and $\sum_i u_i=2\sqrt{nW}$.

There is a two-weight secant identity. Hold every bulk weight fixed and let $(v^{(j)},u^{(j)},\gamma^{(j)})$ be the stationary solutions for two positive marked weights, $j=1,2$. If $E_0=0$ and $E_i=\tanh((\gamma_i^{(1)}+\gamma_i^{(2)})/2)$ on the bulk, then

$$
v^{(1)}-v^{(2)}=(u_0^{(1)}-u_0^{(2)})X_E e.
$$

Indeed $u_i^{(1)}-u_i^{(2)}=E_i(v_i^{(1)}-v_i^{(2)})$ off the mark by the common bulk weights and the addition formulas. Equation (1) takes the second marked weight equal to the common bulk weight, so its stationary vector is zero.

## Uniform transfer along the hyperbolic path

For any $\alpha\in[1/2,1]$ put $B_{\alpha,0}=0$, $B_{\alpha,i}=\tanh(\alpha\gamma_i)$ on the bulk. The energy in the [sitewise attenuation estimate](stationary-attenuation.md#transfer-in-weighted-squared-energy) simplifies exactly:

$$
Q_{B_\alpha}=\sum_{i\ne0}\frac{u_i^2(D_i-B_{\alpha,i})^2}{1-B_{\alpha,i}^2}
=4\sum_{i\ne0}w_i\sinh^2((1-\alpha)\gamma_i)
\le 2 W^{1-\alpha}\tau^\alpha . \tag{3}
$$

The equality uses the difference of two hyperbolic tangents. For the bound, let $c=2(1-\alpha)\in[0,1]$. Convexity of $\log\cosh$ gives $\cosh(c\gamma_i)\le\cosh(\gamma_i)^c$. Apply concavity of the $c$-th power, since $n^{-1}\sum_{i\ne0}\cosh\gamma_i\le\sqrt{W/\tau}$ by the total mass identity. The $c=0$ case has $Q_{B_\alpha}=0$. As $|B_{\alpha,i}|\le|D_i|$ on the bulk,

$$|m_{B_\alpha}-D_0|\ll\tau+\tau^\alpha$$

with no norm assumption on $v$. Equation (1) is sharper at $\alpha=1/2$.

The change of variables also changes the size of sets on which the diagonal approaches the endpoints. If $0<\delta\le 1/2$, then

$$
|\{i\ne0:1-|B_{\alpha,i}|\le\delta\}|
\ll \frac{n}{\sqrt\tau}\,\delta^{1/(2\alpha)} . \tag{4}
$$

Indeed $\cosh\gamma_i\ge\frac12 (2/\delta-1)^{1/(2\alpha)}$ on that set. The half-angle case has the power $\delta$ rather than $\sqrt\delta$. The Paley entry bound gives $u_i\ll1$ uniformly, so $1-\|B\|_\infty\gg\sqrt{\tau/n}$ using $1-|\tanh(\gamma_i/2)|=2/(1+\exp|\gamma_i|)$ and $\exp|\gamma_i|\le u_i/\nu_i$. All singular values of $H_B$ are at least $1-\|B\|_\infty$.

For a unit vector $y$ in the window $|H_B|\le\eta\le1$, the inequality $\|PB y\|\ge1-\eta$ gives $\sum_i(1-B_i^2)y_i^2\le2\eta$. For any fixed $A>2$, all but $2/A$ of the squared norm lies on the set where $1-|B_i|\le A\eta$. At $\eta=O(n^{-1/2})$ and fixed positive $\tau$, that set has size $O_{A,\tau}(\sqrt n)$ by (4). If $\mu$ denotes the spectral measure of $H_B$ at $e$, (1) gives

$$\int_{|\lambda|\le\eta}|\lambda|^{-1}\,d\mu
\le \eta\int\lambda^{-2}\,d\mu
=\eta\lVert v\rVert_2^2/a^2.$$

These statements put the smallest-window contribution on the critical-size scale. They give no control on the signed contributions of larger windows, and the size constant in (4) does not give the asymptotically sharp critical size needed for the [arithmetic overlap exclusion](parallel-overlap-3.md).

## An exact residual certificate with a midpoint diagonal

Let $z$ be a real mean-zero trial vector at the same weights, $u^z_i=\sqrt{z_i^2+4w_i}$, $\eta_i=\operatorname{arsinh}(z_i/(2\nu_i))$ and $r=z-Ku^z$. Use the full midpoint diagonal $C_i=\tanh((\gamma_i+\eta_i)/2)$ and multiplier $M_i=\sqrt{1-C_i^2}$. The secant formula gives

$$H_C(v-z)=-Kr,\qquad
M(v-z)=-(I+R(C)C)M^{-1}r,$$

where $R(C)=MX_C M-C$ is the [response contraction](response-locality.md#contraction-and-response-derivative). For the second identity use $X_CKr=r+X_CCr$ on mean-zero $r$ and $M^2+C^2=I$. Consequently

$$
\lVert M(v-z)\rVert_2\le2\lVert M^{-1}r\rVert_2,\qquad
|v_0-z_0|\le 2M_0^{-1}\lVert M^{-1}r\rVert_2. \tag{5}
$$

The weight in the norm of the difference is the hyperbolic discrepancy exactly:

$$\lVert M(v-z)\rVert_2^2=8\sum_i w_i\big(\cosh(\gamma_i-\eta_i)-1\big).$$

The residual bound involves both the trial and the true stationary solution. It admits a sufficient linear-program certificate using only the trial. On the bulk,

$$M_i^{-2}=\tfrac12(1+\cosh(\gamma_i+\eta_i))
\le\tfrac12(1+e^{|\eta_i|}\cosh\gamma_i).$$

Let $c_0=0$, $c_i=n e^{|\eta_i|}r_i^2$ on the bulk. With $\mu_\sigma=(u+\sigma v)/(2\sqrt{nW})$ the normalized stationary probability of sign $\sigma$, one has

$$\sum_{i\ne0} M_i^{-2}r_i^2
\le\tfrac12\lVert r_{\rm bulk}\rVert_2^2+
\tfrac14\sqrt{W/\tau}\, \langle c,\mu_++\mu_-\rangle . \tag{6}
$$

Each pairing is at most the support function of the corresponding nonnegative Fourier probability cone, so (6) can be checked by the [same full-spectrum linear programs](signed-drift.md#a-linear-program-test-independent-of-the-stationary-solve) as for the signed iterate drift. The new cost is the squared residual with a trial-dependent weight. At fixed positive $\tau$ along a sequence tending to zero, trial vectors with bounded marked hyperbolic coordinates, $z_0=o(1)$, $r_0=o(1)$, $\|r\|_2=o(1)$ and the two linear-program costs $o(1)$ would give the theta limit by (5) and the theta bracket. Iterated limits can use fixed-depth parity for the two marked terms. The averaged residual bound in $\ell_2$ alone does not give the weighted costs in (6).

## Square-order failure under stronger hyperbolic attenuation

Take $q=r^2$ with $r$ an odd prime, and $\tau=1/n$. For any fixed $0<\alpha<1/6$ the true square stationary diagonal satisfies

$$
m_{B_\alpha}\longrightarrow-1,\qquad m_{B_{1/2}}\longrightarrow\frac13. \tag{7}
$$

The second limit follows from (1) and the [exact square theta and marker](parallel-coupling-2.md#exact-square-order-control-with-decreasing-floors). For the first, let $\ell$ be the explicit mean-one minus spectrum from the same square certificate. On the bulk $\ell_i=(r-\lambda_i)/(r+1)$, where $\lambda_i=n K_{i0}$. The complementary product and the exact optimum at the mark give $\sum_{i\ne0} A_{+,i}\ell_i\ll\sqrt n\,\tau$, as in the [square-order bulk estimate](parallel-coupling-2.md#exact-square-order-control-with-decreasing-floors). Thus

$$
\frac1n\sum_{i\ne0} e^{\gamma_i}\ell_i\ll\sqrt\tau,\qquad
\frac1n\sum_{i\ne0}e^{\gamma_i}\ll\tau^{-1/2}.
$$

The [single Jacobi cap bound](parallel-arithmetic-2.md#two-widths-in-the-triangle-count) gives

$$\frac1n|\{i\ne0:\ell_i<c\}|\ll\sqrt c+n^{-1/4}.$$

Indeed $\ell_i<c$ requires $1-\lambda_i^2/q=O(c)$ for $c>0$ small. Fix $0<\rho<1$, put $\theta=\operatorname{arctanh}\rho$, and set $S=\{i\ne0:\alpha\gamma_i>-\theta\}$. On $S$ one has $e^{2\alpha\gamma_i}\ll_{\alpha,\rho}e^{\gamma_i}$ because $e^{\gamma_i}\ge e^{-\theta/\alpha}$ and $2\alpha<1$. The contribution to $n^{-1}\sum_{i\in S}e^{2\alpha\gamma_i}$ from $\ell_i\ge c$ is $O_{\alpha,\rho}(\sqrt\tau/c)$. On $\ell_i<c$ use Hölder to bound the same average by $O((\sqrt c+n^{-1/4})^{1-2\alpha}\tau^{-\alpha})$. Choose $c=\tau^\beta$ with $\beta<1/2$ and $(\beta/2)(1-2\alpha)>\alpha$, possible exactly in the stated range for $\alpha$. Since $\tau=1/n$, both contributions tend to zero.

Compare with the diagonal equal to $-\rho$ on the bulk and zero at the mark. Its mark is $-\rho+O_\rho(n^{-1})$ and its bulk response column is pointwise $O_\rho(n^{-1/2})$, by the constant-diagonal inverse $(K-\rho P)/(1-\rho^2)$ followed by a rank-one change at the mark. The [pointwise bound](response-locality.md#a-pointwise-one-sided-bound) estimates the increase to $B_\alpha$ by $O_\rho(n^{-1}\sum_{i\in S}e^{2\alpha\gamma_i})=o(1)$. Hence $\limsup m_{B_\alpha}\le-\rho$ for every $0<\rho<1$. The general bound $|m_{B_\alpha}|\le1$ proves (7). This leaves the interval $1/6\le\alpha<1/2$ undecided by the comparison.

In the [signed time integral](parallel-sign-4.md#exact-tail-and-certificates-for-cancellation), take $F=B_{1/2}$. Its tail uses the true stationary vector in place of a new undamped solve:

$$J_T(B_{1/2})=a^{-1}\langle y(2T),|B_{1/2}|^{1/2}v\rangle .$$

At square order $\tau=1/n$, the normalized bulk of $B_\alpha$ tends to $-1$ for every fixed $\alpha>0$ by the known bulk limit for $D$ and continuity of the hyperbolic rescaling on $[-1,1]$. Therefore the bounded-time proof for the signed density applies to all these $B_\alpha$ and gives $j_\alpha(s)\to-e^{-s}$ uniformly on bounded intervals. By (7), the signed tails at every fixed $T$ have limits $4/3-e^{-T}$ for $\alpha=1/2$ and $-e^{-T}$ for $\alpha<1/6$. Thus the two attenuations have the same finite-time limits in this comparison, with a difference of $4/3$ in the limiting tails.

## Numerical comparison

The [probe](../stationary_secant.py) records the half-angle column and the trial residuals over [64 comparisons](../data/stationary-secant.csv) on four pairs of prime and square orders. These use two floors and four averaged iteration depths. The maximum half-angle source and midpoint source errors are both below $1.0\cdot10^{-10}$, and the half-angle inverse column agrees in Euclidean norm with (1) to within $6.4\cdot10^{-10}$. Independent dense checks at four small orders verify the response-contraction formula for 128 random trial vectors and the two-weight secant for 32 pairs of stationary weights. Their maximum errors are $2.1\cdot10^{-12}$ and $1.4\cdot10^{-11}$.

The largest matched pair at $\tau=0.01$ and depth $256$ gives

| Order | $1-\lVert D\rVert_{\infty,\mathrm{bulk}}$ | $1-\lVert B\rVert_\infty$ | $\lVert r\rVert_2$ | $\lVert M^{-1}r\rVert_2$ | Marked error |
| ---: | ---: | ---: | ---: | ---: | ---: |
| $389^2$ | $1.37\cdot10^{-7}$ | 0.000523 | 0.03906 | 38.70995 | 0.58261 |
| $153649$ | 0.000340 | 0.025758 | 0.000164 | 0.001934 | $1.48\cdot10^{-6}$ |

The weighted residual can be large on the square stationary tail even when the unweighted residual is small. At orders at most 500 the CSV also records both linear-program costs from (6). These are finite-order floating-point diagnostics.

In a separate square sweep at $\tau=1/n$, the marked responses were

| $r$ | $m_{B_{1/12}}$ | $m_{B_{1/6}}$ | $m_{B_{1/4}}$ | $m_{B_{1/2}}$ |
| ---: | ---: | ---: | ---: | ---: |
| 47 | -0.17908 | -0.16541 | 0.04327 | 0.31417 |
| 97 | -0.25431 | -0.26407 | 0.02102 | 0.32411 |
| 193 | -0.32011 | -0.35565 | 0.00398 | 0.32871 |
| 389 | -0.38146 | -0.44429 | -0.00939 | 0.33104 |

The sweep uses the same stationary solver and marked inverse as the probe, evaluating $\tanh(\alpha\gamma)$ for the listed exponents and zero at the mark. The largest stationary and inverse residuals are below $8\cdot10^{-11}$ and $9\cdot10^{-11}$, respectively. Only $\alpha<1/6$ and $\alpha=1/2$ are covered by (7).

For the half-angle signed time evolution at $\tau=0.01$, use the [Poisson-series replay](parallel-sign-4.md#finite-order-replay) with $F=B_{1/2}$ and the exact inverse column (1). At $T=32$, the signed tail is $-7.56\cdot10^{-7}$ at $153649$ and $0.69435$ at $389^2$. The two prefix integrals are respectively $(0.53658,0.53781)$ and $(0.31242,0.68001)$. At these two orders and the pair $9413,97^2$, the prefix difference plus the tail reproduces $m_B+1/n$ within $3.0\cdot10^{-12}$.
