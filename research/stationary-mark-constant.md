# The marked and constant sources in each signed block

Let $K=K^{\mathsf T}$ be the Paley frequency operator, $K^2=I-J$, and $j=\mathbf1/\sqrt n$, $J=jj^{\mathsf T}$. Use the stationary pair $A_{\pm}=(u\pm v)/2$, $v=Ku$, $w_0=1$, $w_i=\tau/n$ for $i\ne0$, and $W=\sum_i w_i$. Write $a_\sigma=A_{\sigma,0}$ for $\sigma\in\{1,-1\}$, so $a_+a_-=1$. Fix $\alpha\in[1/2,1]$ and use the stripped diagonal $F_i=\tanh(\alpha\gamma_i)$ on the bulk, where $A_{\pm,i}=\sqrt{w_i}e^{\pm\gamma_i}$. This includes the half-angle and the full stripped diagonal.

For a given sign put $I_\sigma=\{i:\sigma F_i>0\}$. Define $V$ diagonally as $\sqrt{|F_i|}$ on $I_\sigma$ and zero elsewhere. Put

$$
Q=I-\sigma K,\qquad L=I-\sigma VKV=I-V^2+V Q V,\qquad
b=\sigma VKe_0,\qquad d=Vj .
$$

Here $Q$ has eigenvalues in $\{0,1,2\}$ and $L$ is positive definite. Both $b,d$ are supported on $I_\sigma$. The first is the marked source of the corresponding one-sign block. The other tests the constant vector. Define the two one-sign responses and their defects by

$$
U_\sigma=b^{\mathsf T}L^{-1}b,\quad M_\sigma=d^{\mathsf T}L^{-1}d,\qquad
D_\sigma=1+\sigma/n-U_\sigma,\quad C_\sigma=1-M_\sigma .
$$

The resolvent update at the zero diagonal gives $U_\sigma=\sigma(m_{F\mathbf1_{I_\sigma}}-m_{\varnothing})$, where $m_{\varnothing}=K_{00}=-1/n$. Equivalently $D_\sigma=1-\sigma m_{F\mathbf1_{I_\sigma}}$.

## A two-dimensional defect relation

Uniformly for $0<\tau\le1$ and $\alpha\in[1/2,1]$,

$$
\boxed{\displaystyle
\left|\sqrt{W C_\sigma}-a_\sigma\sqrt{D_\sigma}\right|
\ll\tau^{\alpha/2}.} \tag{1}
$$

The defects are nonnegative. There is also a joint inequality for the cross entry. Define $q_0=Q^{1/2}e_0$ and

$$G=I-Q^{1/2}V L^{-1}VQ^{1/2},\qquad E_\sigma=j^{\mathsf T}G q_0.$$

The exact variational formula

$$
f^{\mathsf T}G f
=\min_{y\in\mathbb R^n}
\left(\|Q^{1/2}V y-f\|_2^2+\|(I-V^2)^{1/2}y\|_2^2\right) \tag{2}
$$

follows by the normal equation $L y=V Q^{1/2}f$. Thus $0\preceq G\preceq I$. Since $Q^{1/2}j=j$ and $VQ e_0=-b$, we have

$$j^{\mathsf T}G j=C_\sigma,\qquad
q_0^{\mathsf T}G q_0=D_\sigma,\qquad
E_\sigma=n^{-1/2}+d^{\mathsf T}L^{-1}b.$$

In particular the signs in the last expression come from the negative mark source $VQe_0=-b$.

For $f_\sigma=\sqrt W j-a_\sigma q_0$, one has $f_\sigma=Q^{1/2}(A_\sigma-a_\sigma e_0)$ by the exact stationary Fourier support. Use the trial $V_i y_i=|v_i|$ on $I_\sigma$ and zero elsewhere in (2). The difference $r=A_\sigma-a_\sigma e_0-Vy$ has $0\le r_i\le\sqrt{\tau/n}$ on the bulk. On the same sign $r_i=A_{-\sigma,i}$. On the other sign $r_i=A_{\sigma,i}$. Therefore $\|Q^{1/2}r\|^2\le2\tau$. For the remaining term, set $t=|\gamma_i|$ on $I_\sigma$ and $\nu=\sqrt{\tau/n}$. Pointwise,

$$
(1-|F_i|)y_i^2
=4\nu^2\sinh^2(t)\frac{1-\tanh(\alpha t)}{\tanh(\alpha t)}
\ll \nu^2\cosh(t)^{2-2\alpha}.
$$

For $t\le1$ use $\tanh(\alpha t)\gg t$ and $\sinh t\ll t$. For $t\ge1$ use $1-\tanh(\alpha t)\le2e^{-2\alpha t}$. Since $2-2\alpha\in[0,1]$, concavity and $n^{-1}\sum_{i\ne0}\cosh\gamma_i\le\sqrt{W/\tau}$ bound the sum by $O(W^{1-\alpha}\tau^\alpha)$. This proves

$$
W C_\sigma-2\sqrt W a_\sigma E_\sigma+a_\sigma^2 D_\sigma
=\|G^{1/2}f_\sigma\|^2\ll \tau^\alpha . \tag{3}
$$

The reverse triangle inequality gives (1). Pairing $G^{1/2}f_\sigma$ against $G^{1/2}q_0$ and $G^{1/2}j$ also gives

$$
|\sqrt W E_\sigma-a_\sigma D_\sigma|\ll\tau^{\alpha/2}\sqrt{D_\sigma},
\qquad
|\sqrt W C_\sigma-a_\sigma E_\sigma|\ll\tau^{\alpha/2}\sqrt{C_\sigma}.
$$

The defects of these two inputs are nearly parallel in the $G$ inner product. The comparison uses two positive definite one-sign solves and no bound on the stationary norm $\|v\|_2$.

## A scalar criterion and its denominator

Along any sequence of primes with $\tau\downarrow0$, choose a sign $\sigma$ and $\alpha\in[1/2,1]$ at each order. If

$$
\tau^\alpha=o(D_\sigma),\qquad C_\sigma-D_\sigma=o(D_\sigma), \tag{4}
$$

then $a_\sigma\to1$ by (1). The product $a_+a_-=1$ and the [stationary theta bracket](smoothing.md#fixed-point-and-a-sufficient-residual-estimate) then give the conjectured limit. A sufficient special case is a defect $D_\sigma$ separated from zero and $U_\sigma-M_\sigma=o(1)$. Proving that comparison through all primes remains open.

There is also a positive quadratic test with no subtraction of inverse responses. Let

$$
N_\sigma=(j-q_0)^{\mathsf T}G(j-q_0)
=\min_{\operatorname{supp}g\subseteq I_\sigma}
\left\{\|Q^{1/2}(g-j+e_0)\|^2+\sum_{i\in I_\sigma}\frac{1-V_i^2}{V_i^2}g_i^2\right\}. \tag{4a}
$$

The minimum follows from (2) by $g=Vy$ and $Q^{1/2}j=j$. The trial $g$ may have either sign on $I_\sigma$. Subtract $\sqrt W(j-q_0)$ from $f_\sigma$ in (3) to obtain

$$
|a_\sigma-\sqrt W|\sqrt{D_\sigma}
\le \sqrt{W N_\sigma}+O(\tau^{\alpha/2}).
$$

Hence $N_\sigma+\tau^\alpha=o(D_\sigma)$ is another sufficient condition at one sign. It asks for a weighted interpolation on the actual one-sided support, with prescribed mark and constant inputs.

There is a lower bound on $D_\sigma$ using any vector $\ell$ in the constants plus the opposite Fourier sector. Indeed the Woodbury identity gives $G=(I+Q^{1/2}\mathcal R Q^{1/2})^{-1}$, $\mathcal R=V^2(I-V^2)^{-1}$. Test the dual quadratic form at $Q^{-1/2}\ell$ on $\operatorname{ran}Q$:

$$
D_\sigma\ge\frac{\ell_0^2}{\|Q^{-1/2}\ell\|^2+\sum_i\mathcal R_i\ell_i^2}. \tag{5}
$$

At $\alpha=1/2$, the [constant Fourier witness](fourier.md#feasible-parameters-and-objective) of the opposite sign, with spectrum divided by $\sqrt n$, has mark bounded below, bulk sup norm $O(n^{-1/2})$ and bounded norm. Here $\mathcal R_i=(A_{\sigma,i}/\nu-1)/2$ on $I_\sigma$, zero elsewhere, where $\nu=\sqrt{\tau/n}$. Thus $\sum_i\mathcal R_i\ll n/\sqrt\tau$ and $D_\sigma\gg\sqrt\tau$ uniformly. This is the same scale as the worst error in (3) for the half-angle and by itself does not give (4).

For that witness one may use its exact complementary pairing. Its mean is $1/\sqrt n$, hence $\langle A_\sigma,\ell\rangle=\sqrt W$. Since $\ell\ge0$ and $\ell_i\ll n^{-1/2}$ off the mark,

$$
\sum_i\mathcal R_i\ell_i^2\ll\frac{\sqrt W-a_\sigma\ell_0}{\sqrt\tau}. \tag{6}
$$

This gives a defect bounded away from zero if the elementary opposite witness pairs almost entirely at the mark, with bulk pairing $O(\sqrt\tau)$. In particular, on any hypothetical sequence with $\theta_\sigma/\sqrt n\to\sqrt2$, floors can be chosen tending to zero slowly enough for this assumption: the theta bracket changes $a_\sigma$ from $\theta_\sigma/\sqrt n$ by $O(\tau)$ and $\ell_0=1/\sqrt2+O(n^{-1/2})$. Under this hypothesis, an absolute marked/constant balance at this sign would already rule out the extreme limit.

### What an extreme marked value forces

At the half-angle this same opposite witness also compares the two *responses*. Write $r=\sqrt q$, $k_i=nK_{i0}/r$. The elementary opposite witness has $\ell_i=r(1-\sigma k_i)/((r+1)\sqrt n)$ on the bulk. In particular $1-\sigma k_i$ is nonnegative. The two input vectors satisfy

$$
b-\sqrt{q/n}\,d=-\frac r n V(1-\sigma k).
$$

Since $L\succeq I-V^2$, the reverse triangle inequality and $|k_i|\le1$ give

$$
\begin{aligned}
\left|\sqrt{U_\sigma}-\sqrt{q/n}\sqrt{M_\sigma}\right|^2
&\le \frac{q}{n^2}\sum_i\mathcal R_i(1-\sigma k_i)^2\\
&\ll\frac{\sqrt W-a_\sigma\ell_0}{\sqrt\tau}. \tag{7}
\end{aligned}
$$

For the second line use $\mathcal R_i\le A_{\sigma,i}/(2\nu)$ on $I_\sigma$, $(1-\sigma k_i)^2\le2(1-\sigma k_i)$, and the complementary pairing with $\ell$ above. Thus if $\theta_\sigma/\sqrt n\to\sqrt2$ through any field orders, one may choose floors tending to zero so slowly that $\sqrt W-a_\sigma\ell_0=o(\sqrt\tau)$. Along those floors, $U_\sigma=2M_\sigma+o(1)$ by (7). At the same time (1) gives $C_\sigma=2D_\sigma+o(1)$. Solving the two scalar relations using $D_\sigma=1-U_\sigma+o(1)$ and $C_\sigma=1-M_\sigma$ shows

$$
(U_\sigma,M_\sigma,D_\sigma,C_\sigma)\longrightarrow(2/3,1/3,1/3,2/3). \tag{8}
$$

This is an additional necessary condition for an extreme theta deviation. It gives a target for either of the two positive definite one-sign solves, without requiring the full marked resolvent.

One can also use $\ell=A_{-\sigma}$ with $\alpha\le1$. On $I_\sigma$, $\mathcal R_i\ell_i^2\le \nu^2/2$ by reciprocity and $\mathcal R_i=(e^{2\alpha|\gamma_i|}-1)/2$. Hence $D_\sigma\gg (1+\|A_{-\sigma}\|_2^2)^{-1}$. This bound is uniform when the opposite spectrum has bounded norm. Equation (4) still requires the equality of marked and constant defects at that sign.

## Exact square-field limits

Take $q=r^2$ with $r$ an odd prime and any floors $\tau_q\downarrow0$. The square [constant opposite witness](square-order-control.md#square-order-comparison) has $\ell_0=\sqrt n/(r-1)$. The exact square theta value and the stationary bracket give $a_+\ell_0\ge1/\sqrt W$. Hence $\sqrt W-a_+\ell_0=O(\tau)$ at any such floors, and (7)–(8) apply on the positive side. In particular the two defects tend to $1/3$ and $2/3$.

On the other side $D_-\to0$. The negative part of the half-angle diagonal converges to $-1$ in normalized bulk $\ell_2$ by the [true square bulk limit](parallel-coupling-2.md#exact-square-order-control-with-decreasing-floors). At any fixed linear damping $t<1$, the same constant-background inverse comparison from that limit gives the negative-only mark tending to $-t$. Coordinate monotonicity for the undamped mark and the absolute bound by one imply that its mark tends to $-1$, so $D_-=o(1)$.

Also $C_-\to0$ by (1), so both negative-side responses tend to one.

The positive limits from (8) hold without a rate assumption on the floors. For comparison, a subfield-only monotonicity argument sees the same positive mark when $\tau=o(n^{-2})$. In that case the [stationary subfield estimate](parallel-exterior-3.md#a-true-square-stationary-counterexample-with-retained-same-sign-highs) gives $\exp(-\gamma_i)=O(\sqrt{n\tau})=o(1/r)$ on the nonzero subfield-annihilator frequencies, so their half-angle activation is $1-o(1/r)$ and the [response of the saturated subgroup](response-locality.md#square-order-test-of-the-formula) is $2/3+o(1)$.

At prime order, the [reflection estimate](parallel-extreme-6.md) excludes a different aspect of the extreme configuration, the possibility of a near-minimum stationary high set approximated by a bounded coset cover at logarithmic resolution. Either excluding the port limits (8) or ruling out the associated stationary concentration would obstruct the extreme theta deviation.

## Numerical comparison

The [FFT positive-definite probe](../stationary_mark_constant.py) records [54 comparisons](../data/stationary-mark-constant.csv). The first 48 use three pairs of Paley orders, two floors, both signs and the two exponents $1/2,1$. The last six use the larger primes $1008001$ and $1000033$ at the smaller floor. The probe checks the directional defect against the trial cost in (2) and the marked defect against the elementary witness in (5). The largest stationary and block-solve residuals are $1.0\cdot10^{-10}$ and $9.8\cdot10^{-13}$. Independently, 64 dense prescribed sign blocks checked the Woodbury, mixed-entry and sign-only marked identities within $1.7\cdot10^{-15}$.

At $\tau=0.0005$, the largest matched pair gives

| Order | Exponent | Sign | Marked defect $D_\sigma$ | Constant defect $C_\sigma$ | $N_\sigma$ from (4a) |
| ---: | ---: | :---: | ---: | ---: | ---: |
| $389^2$ | $1/2$ | $+$ | 0.345408 | 0.672700 | 0.085088 |
| $389^2$ | 1 | $+$ | 0.335626 | 0.667809 | 0.056581 |
| $153649$ | $1/2$ | $+$ | 0.449809 | 0.454493 | 0.043991 |
| $153649$ | $1/2$ | $-$ | 0.449131 | 0.455924 | 0.043898 |
| $153649$ | 1 | $+$ | 0.424232 | 0.423637 | 0.000482 |
| $153649$ | 1 | $-$ | 0.423528 | 0.425059 | 0.000482 |
| $1008001$ | 1 | $+$ | 0.422185 | 0.423196 | 0.000482 |
| $1008001$ | 1 | $-$ | 0.423308 | 0.423213 | 0.000482 |
| $1000033$ | 1 | $+$ | 0.422434 | 0.423588 | 0.000482 |
| $1000033$ | 1 | $-$ | 0.423378 | 0.423139 | 0.000482 |

These comparisons use numerical stationary inputs and floating-point linear solves. They do not show equality of the defects through all primes.
