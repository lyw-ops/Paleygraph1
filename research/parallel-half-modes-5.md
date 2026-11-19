# Localizing the marked slow response of the true half-angle diagonal

For Randomstrasse101 Problem 26, the [half-angle source](stationary-secant.md) makes the signed inverse contribution of a small spectral window a linear pairing with the stationary vector. The part of this pairing outside a measured saturation set has an explicit bound in terms of the weighted stationary energy. There is a time version for a smooth average of the [signed tail](parallel-sign-4.md): the marked time source is bounded in the dual of the dissipation norm. This gives a localization error at scale $1/T$, even though the evolution is not self-adjoint. Neither calculation assumes a global bound on $\|v\|_2$. The true square stationary solution has a signed contribution tending to $4/3$ even in some shrinking windows and after some growing times.

## Setup

Work on the $n=(q-1)/2$ Paley frequencies with $K^2=P=I-J$, $K=K^{\mathsf T}$, $KJ=0$, $K_{00}=-1/n$, and $\max_{ij}|K_{ij}|\le \sqrt q/n$. Write $e=Pe_0$, $z=Ke$, $\nu=\sqrt{\tau/n}$, $w_0=1$, $w_i=\nu^2$ for $i\ne0$, and $W=\sum_i w_i$, with $0<\tau\le1$. Take the **true** stationary pair $v=Ku$, $u_i=\sqrt{v_i^2+4w_i}$. Set
$$
B_0=0,\qquad B_i=\frac{v_i}{u_i+2\nu}=\tanh(\gamma_i/2)\quad(i\ne0),\qquad
H=K-PBP\ \text{on }P\mathbb R^n,\quad a=u_0-2\nu .
$$
Then $B_i v_i=u_i-2\nu$ in the bulk, $Hv=ae$, and $m_B=(H^{-1}e)_0=v_0/a$. Here $a$ is bounded away from zero uniformly; $\sum_i u_i=2\sqrt{nW}$ and the entry bound give $\|u\|_\infty=O(1)$. In particular $m_B=D_0+O(\nu)$, where $D_0=v_0/u_0$. Put $d_i=1-|B_i|$, $M^2=I-B^2$, and define
$$
S_\delta=\{i\ne0:d_i\le\delta\},\qquad
p_\delta=\frac1{\sqrt n}\sum_{i\in S_\delta}(u_i-2\nu).
$$
For $0<\delta\le1/2$, the half-angle identities give
$$
|S_\delta|\ll n\delta/\sqrt\tau,\qquad
\sum_{i\ne0} M_i^2 v_i^2=4\nu\sum_{i\ne0}(u_i-2\nu)\ll\sqrt\tau,\qquad
\sum_{S_\delta} v_i^2\ll\sqrt n\,p_\delta .
$$
The first inequality follows from $u_i=2\nu(1+B_i^2)/(1-B_i^2)\ge\nu/\delta$ on $S_\delta$; the last uses $v_i^2=(u_i+2\nu)(u_i-2\nu)$.

## A hard signed window

Let $Q_\eta=\mathbf1_{\{|H|\le\eta\}}$ on $P\mathbb R^n$, $\mu_\eta=\|Q_\eta e\|^2$, and $W_\eta=\langle e,H^{-1}Q_\eta e\rangle$. Thus $W_\eta$ counts negative eigenvalues with a minus sign. Set $f=Q_\eta e$ and $\beta=2\eta-\eta^2$ for $0<\eta\le1$. Then
$$
\boxed{\begin{aligned}
W_\eta &= m_B\mu_\eta+\frac1a\sum_{i\in S_\delta}v_i f_i+R,\\
|R|&\le \frac{\sqrt{\beta\mu_\eta-\mu_\eta^2}}{a}
          \left(\sum_{i\ne0,\ i\notin S_\delta}\frac{v_i^2}{1-B_i^2}\right)^{1/2}
     \ll \frac{\eta}{\delta}\tau^{1/4}.
\end{aligned}} \tag{1}
$$
In fact $W_\eta=a^{-1}\langle v,f\rangle$ by the exact source. For every $y\in\operatorname{ran}Q_\eta$, $Ky=Hy+PBy$ and $\|Ky\|=\|y\|$, so $\|PBy\|\ge(1-\eta)\|y\|$. Hence
$$
\|My\|^2+\|JBy\|^2=\|y\|^2-\|PBy\|^2\le\beta\|y\|^2.
$$
Since $f_0=\mu_\eta$ and $M_0=1$, this gives $\mu_\eta\le\beta$ and $\|Mf\|_{\mathrm{bulk}}^2\le\beta\mu_\eta-\mu_\eta^2\le\eta^2$. This last bulk estimate is what buys a factor $\eta$, rather than $\sqrt\eta$, in (1). Apply weighted Cauchy–Schwarz on the omitted sites, using $1-B_i^2\ge d_i>\delta$ there. The same proof holds for either sign window alone with its own projector and marked mass. In an eigenbasis the full window is $a^{-2}\sum_{|\lambda_j|\le\eta}\lambda_j|\langle v,y_j\rangle|^2$; the single pairing in (1) keeps the cancellation in this sum.

In particular,
$$
|W_\eta|\ll \eta+\sqrt{\eta\sqrt n\,p_\delta}
                      +(\eta/\delta)\tau^{1/4}. \tag{2}
$$
At fixed floor and $\eta=c/\sqrt n$, choose $\delta=L\eta$: the omitted contribution is $O(\tau^{1/4}/L)$. Small **signed** overlap on this set suffices, even if $p_\delta$ is large. Vanishing $p_\delta$ at each fixed $L$ is a stronger, unsigned sufficient test. At decreasing floors the error tends to zero even at fixed $L$, though the set can grow. For $\eta\sqrt n\to0$ one can just take $\delta=1/2$, since $p_\delta=O(1)$. None of these statements supplies the signed overlap at critical or wider widths through all primes.

There are only boundedly many modes in the critical window at fixed $\tau,c,L$. For example, if $\eta\le1/128$ and $\delta\ge128\eta$, write any unit $y\in\operatorname{ran}Q_\eta$ as $y_S+y_{S^c}$ with $S=S_\delta$. The defect estimate gives $\|y_{S^c}\|\le\sqrt{2\eta/\delta}$ and $\|JBy\|\le\sqrt{2\eta}$. Using $Ky=Hy+By-JBy$ on the exterior and then $\|K\|\le1$ gives
$$
\|K_{SS}y_S\|\ge 1-\eta-2\sqrt{2\eta/\delta}-\sqrt{2\eta}>\tfrac12.
$$
Restriction to $S$ is injective on the window, and every vector in its image has $\|K_{SS}y_S\|\ge\frac12\|y_S\|$. By min–max for $K_{SS}^2$, $\operatorname{rank}Q_\eta\le4\|K_{SS}\|_{\mathrm F}^2\le4q|S|^2/n^2$. This test uses the true set, with its constant factor in the size bound. It does not give the sharp size hypothesis for the arithmetic coset exclusions, or a bounded rank uniformly as $\tau\downarrow0$. Also, a small marked form at a fixed-depth reference does not estimate (1); the normalized defects in the [reference comparison](parallel-reference-4.md) include an independent constant-direction overlap.

## A time average with an explicit error at scale $1/T$

To avoid overloading $B$, write $V=|B|^{1/2}$, $\Sigma=\operatorname{sgn}B$ (take $+1$ at zeros), $U=\Sigma V K V$, $A=I-U$, and $b=\Sigma Vz$. Let $L=(A+A^{\mathsf T})/2$. The two sign blocks of $L$ are $d_\sigma+V_\sigma(I-\sigma K)V_\sigma$, interpreting the latter as a form on the sign block extended by zero. Thus $L\succeq\operatorname{diag}(d)\succ0$. The [exact time tail](parallel-sign-4.md#exact-tail-and-certificates-for-cancellation) is $J_s=a^{-1}\langle e^{-sA}b,Vv\rangle$.

The marked source has the uniform dual bound $bb^{\mathsf T}\preceq 2L$. Indeed on each sign block the pairing with $b_\sigma$ is $-\langle e_0,(I-\sigma K)V f_\sigma\rangle$, because $V_0=0$. Apply Cauchy–Schwarz for the two positive forms $I-\sigma K$; the sum of the two marked forms at $e_0$ is $2$. The rest of the bound is the quadratic form of $L$. For any real $g\in L^2(0,\infty)$, this implies
$$
\left\|\int_0^\infty g(s)e^{-sA}b\,ds\right\|\le\|g\|_{L^2}.
$$
To see it, test against $h$ and use $ |\langle b,e^{-sA^{\mathsf T}}h\rangle|\le\sqrt2\|L^{1/2}e^{-sA^{\mathsf T}}h\|$. The integral of the latter squared norm without the factor $2$ is $\|h\|^2/2$, by differentiating the squared norm of the adjoint orbit and using decay. This argument does not bound the unsigned slow responses separately.

For a nonnegative averaging density $\phi\in H^1(0,\infty)$ with $\phi(0)=0$ and $\int\phi=1$, define $g_T(s)=T^{-1}\phi(s/T)$, $Y_T=\int g_T(s)e^{-sA}b\,ds$, and $\bar J_T=\int g_T(s)J_s\,ds$. Integration by parts gives $AY_T=\int g'_T(s)e^{-sA}b\,ds$. Therefore
$$
\|Y_T\|\le \frac{\|\phi\|_2}{\sqrt T},\qquad
\|L^{1/2}Y_T\|\le\frac{\sqrt{\|\phi\|_2\|\phi'\|_2}}{T}.
$$
The second estimate tests both the coordinate defect $d$ and the opposite Fourier-sector defects in $L$. With $C_\phi=\sqrt{\|\phi\|_2\|\phi'\|_2}$, the tail certificate is
$$
\boxed{\left|\bar J_T-\frac1a\sum_{i\in S_\delta}Y_{T,i} V_i v_i\right|
\le \frac{C_\phi}{aT}
   \left(\sum_{i\notin S_\delta}\frac{|B_i|v_i^2}{d_i}\right)^{1/2}
\ll_\phi \frac{\tau^{1/4}}{T\delta}.} \tag{3}
$$
The mark contributes zero. The second bound uses $d_i v_i^2\le M_i^2v_i^2$ and $d_i>\delta$ on the omitted bulk. The localized term is bounded by $O_\phi(\sqrt{\sqrt n\,p_\delta/T})$, but can instead be evaluated with its sign. At $T\asymp\sqrt n$ and fixed floor, taking $\delta=L_*/T$ for a fixed large $L_*$ gives a set of order at most $\sqrt n$ and an error $O_\phi(\tau^{1/4}/L_*)$. For $T/\sqrt n\to\infty$ one gets $\bar J_T=o(1)$ uniformly in the floors by taking $\delta=1/2$. These are statements about the average, not pointwise decay of $J_T$ on the same scale.

One useful choice is $\phi(x)=xe^{-x}$, for which both norms are $1/2$ and $Y_T=T^{-2}(A+T^{-1})^{-2}b$. Equivalently, for $\epsilon=1/T,\ t=(1+\epsilon)^{-1}$ and $H_{tB}=K-tPBP$ on the mean-zero space,
$$
\bar J_T=m_B-m_{tB}-\epsilon t^2\,\frac{d}{dt}m_{tB},\qquad
\frac{d}{dt}m_{tB}=\sum_i B_i (H_{tB}^{-1}e)_i^2. \tag{4}
$$
The weight on the signed density $j(s)$ is $1-e^{-\epsilon s}(1+\epsilon s)$, the cumulative distribution of $g_T$; the damped time identity gives (4). One can also take a smooth $\phi$ supported in $[1,2]$ to use only cutoffs between $T$ and $2T$.

If the true diagonals have fixed-damping cancellation through primes, the signed density tends to zero at each bounded time by the moment argument in [parallel-sign-4](parallel-sign-4.md#finite-time-versus-the-arithmetic-limit). For each fixed $T$, the integrated part $m_B-m_0-\bar J_T$ tends to zero (also for the exponential kernel, by dominated convergence with the exponentially decaying weight). In this order of limits a signed bound tending to zero on the local term in (3), with $T$ and then $L_*$ large, would therefore suffice. The bound at $T/\sqrt n\to\infty$ by itself does not allow that interchange of limits. Fixed-depth parity has not established fixed-damping cancellation for the true $B$ here.

## True square obstruction, including moving cutoffs

Let $q=r^2$, $r$ odd prime, $\tau=\tau_q\to0$. The [exact square theta and stationary bracket](parallel-coupling-2.md#exact-square-order-control-with-decreasing-floors) give $m_B\to1/3$. Put $\sigma_q^2=n^{-1}\sum_{i\ne0}(1+B_i)^2$. There is a rate sufficient for moving cutoffs:
$$
\sigma_q^2\ll \tau^{1/6}+n^{-1/4}. \tag{5}
$$
Indeed with $A_+=(u+v)/2$ and the explicit square minus witness $\ell_i=(r-nK_{i0})/(r+1)$ in the bulk, the same square bracket gives $\sum_{i\ne0}A_{+,i}\ell_i\ll\sqrt n\,\tau$. Since $1+B_i=2x_i/(1+x_i)$ for $x_i=A_{+,i}/\nu$, $(1+B_i)^2\le x_i$. Where $\ell_i\ge c$, the contribution to $\sigma_q^2$ is $O(\sqrt\tau/c)$; elsewhere the [single Jacobi cap count](parallel-arithmetic-2.md#two-widths-in-the-triangle-count) gives $O(\sqrt c+n^{-1/4})$ for small $c$. Use $c=\tau^{1/3}$.

For the hard window, take the reference $H^0=K+P-ee^{\mathsf T}$, corresponding to bulk $-1$ and stripped mark. It need not be invertible on all of $P\mathbb R^n$. On $\operatorname{span}(e,z)$ it has $H^0e=z+e/n$, $H^0z=z+(1+1/n)e$, so $x^0=z-e$ solves $H^0 x^0=e$ there and $\langle e,x^0\rangle=-1$ exactly. The two reference eigenvalues on this span approach $(1\pm\sqrt5)/2$. Each unit vector on the span has bulk sup norm $O(n^{-1/2})$, hence $\|(H-H^0)w\|\ll\sigma_q$ there. Testing the two reference eigenvectors against $Q_\eta$ shows $\|Q_\eta x^0\|\ll\sigma_q$ uniformly for $0<\eta\le1/2$ at large $q$: on the window their reference eigenvalues are separated from the true spectrum. Also $\|H^{-1}(I-Q_\eta)e\|\ll\eta^{-1/2}$, by summing $\mu_\xi\le2\xi$ over dyadic bands above $\eta$ (for $\xi>1$ the bound holds by total mass). Insert $e=Hx^0+(H^0-H)x^0$ in the retained signed response. This proves
$$
W_\eta=m_B+1+O(\sigma_q/\sqrt\eta)\qquad (0<\eta\le1/2). \tag{6}
$$
In particular the true signed window tends to $4/3$ whenever $(\tau^{1/6}+n^{-1/4})/\eta\to0$. This includes $\tau=1/n,\ \eta=n^{-1/7}$.

For time, $\|Ub\|\le\|(B+I)z\|+\|Ve\|\ll \sigma_q+n^{-1/2}$, and $b^{\mathsf T}\Sigma b=z^{\mathsf T}Bz=-1+O(\sigma_q+n^{-1})$. Using $\|U\|\le1$ in the exponential series gives $\|e^{-sA/2}b-e^{-s/2}b\|\le(1-e^{-s/2})\|Ub\|$. Expand the signed square and integrate the error from $j(s)=-e^{-s}$ up to $T$: the linear term has the factor $e^{-s/2}$, while the quadratic term is $O(\sigma_q^2+n^{-1})$ at all times. Thus
$$
J_T=m_B+1-e^{-T}
         +O\big(\sigma_q+n^{-1/2}+T(\sigma_q^2+n^{-1})\big).
$$
For the gamma average in (4), replace $e^{-T}$ by $(1+T)^{-2}$ with the same error order, since the mean cutoff is $2T$. At $\tau=1/n,\ T=n^{1/7}$, both tails tend to $4/3$. These bounds do not locate the entire discrepancy at $\eta=C/\sqrt n$ or $T=C\sqrt n$; the range in (5) matters.

## Finite-order checks at narrower widths and longer times

The inputs were stationary solves from [weighted_iterate](../poisson_weights.py) with the actual prime and square sign kernels. Dense diagonalization on $P\mathbb R^n$ checked (1) at $\tau=1/n,\ \eta=4/\sqrt n,\ \delta=2\eta$:

| $q$ | Modes $(+,-)$ in the window | $W_\eta$ | Bulk local term in (1) |
| ---: | ---: | ---: | ---: |
| $29^2$ | $1,127$ | 0.842653 | 0.800718 |
| 853 | $11,12$ | -0.003232 | -0.003235 |
| $47^2$ | $1,315$ | 0.964736 | 0.931479 |
| 2221 | $19,18$ | 0.002961 | 0.002961 |

Across 288 checks at three prime and three square orders, including the positive and negative projectors separately, the decomposition in (1) agreed with the direct inverse spectral sum to within $5.4\cdot10^{-13}$. All exterior bounds held within rounding error.

For (3)–(4) use the gamma average at $T=0.75\sqrt n,\ \delta=2/T$. The error column uses the computed $\|d^{1/2}Y_T\|$ in place of its upper bound $1/(2T)$.

| $q$ | $\tau$ | $\lvert S_\delta\rvert$ | $\bar J_T$ | Local signed pairing | Exterior error bound |
| ---: | ---: | ---: | ---: | ---: | ---: |
| $29^2$ | $1/n$ | 221 | 0.0771018 | 0.0777422 | 0.001124 |
| 853 | $1/n$ | 325 | -0.0009214 | -0.0009913 | 0.000345 |
| $389^2$ | 0.01 | 194 | 0.0831136 | 0.0830588 | 0.000786 |
| 153649 | 0.01 | 0 | $6.46\cdot10^{-8}$ | 0 | $7.60\cdot10^{-5}$ |
| $389^2$ | $1/n$ | 37033 | 0.0766179 | 0.0766857 | 0.000126 |

To obtain $Y_T$, first solve $x=H_{tB}^{-1}e$, set $r=t\Sigma Vx$, and solve $x_2=H_{tB}^{-1}PVr$. Then $Y_T=\epsilon^2 t(r+t\Sigma Vx_2)$. This follows by multiplying by $A+\epsilon$ and uses two damped symmetric solves, not an undamped time inversion. In the displayed calculations the stationary residuals are below $5\cdot10^{-11}$, the half-angle source residuals below $6\cdot10^{-11}$, the damped solve residuals below $4\cdot10^{-9}$, and (4) agrees with the pairing within $5\cdot10^{-11}$. These are floating-point diagnostics. In particular the large extreme set in the last row warns against transferring the fixed-floor critical-rank bound to decreasing floors. The prime target remains a bound on the actual restricted **signed** pairing in (1) or (3), at an order of limits for which the retained part is known to cancel.
