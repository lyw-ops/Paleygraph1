# One-sided deletion and de-damping at the stationary pair

For [Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/), the true stationary pair gives two one-sided estimates. Deleting same-sign activations can be tested against a weighted overlap of the stationary spectrum and the marked leverage column. In removing real diagonal damping, the correction in either direction is bounded by a positive quadratic form on just one Fourier sector. Both estimates allow saturation of the opposite sign. Neither establishes the needed prime-field bound unconditionally. There is an exact square-order comparison at **any** sequence of positive floors tending to zero.

## Stationary column and same-sign deletion

Use the notation of [stationary-tails](stationary-tails.md) and [marked-response](marked-response.md). On the mean-zero space set $H=K-PDP$, $X=H^{-1}P$, $e=Pe_0$, $x=Xe$, and $m=x_0$, with the inverse extended by zero on constants. Write $\nu_i=\sqrt{w_i}$, $W=\sum_i w_i$, $M_i=2\nu_i/u_i$, $A_{\sigma,i}=(u_i+\sigma v_i)/2$ for $\sigma=\pm1$, and let $M$ also denote the diagonal matrix. The weights are $w_0=1$, $w_i=\tau/n$ on the bulk, with $0<\tau\le1/2$. The elementary bound on $u_0$ gives $M_0\gtrsim1$.

The stationary weighted response satisfies
$$
R=MXM-D=\Pi_+-\Pi_-,\qquad R^2=I-\nu\nu^{\mathsf T}/W,\qquad
R_{00}=\Delta=M_0^2m-D_0.
$$
In particular $|\Delta|\le1-1/W$ and $\sum_{i\ne0}R_{i0}^2=1-1/W-\Delta^2\le\tau$. The product $A_{+,i}A_{-,i}=w_i$ gives the exact cancellation of weights
$$
(1+\sigma D_i)x_i=\frac{A_{\sigma,i}}{M_0\nu_i}R_{i0}\qquad(i\ne0),
\tag{1}
$$
since $(1+\sigma D_i)/M_i=A_{\sigma,i}/\nu_i$.

Let $S$ exclude the mark and lie in $\{\sigma D_i\ge0\}$. Write $D^\circ$ for $D$ with its mark set to zero, $m^\circ=m(D^\circ)$, and $m_T^\circ=m(D^\circ\mathbf1_{S^c})$ for the exterior-only response, with $m(B)=\langle e,(K-PBP)^{-1}e\rangle$. The column $x_F$ at $D^\circ$ is $x/(1+D_0m)$; its denominator is $(1+D_0\Delta)/M_0^2$, separated from zero. Let $x_T$ be the exterior-only column and define
$$
\mathcal L_\sigma(S)=\frac1\tau\sum_{i\in S}(\sqrt n A_{\sigma,i})^2R_{i0}^2.
$$
Then
$$
\begin{aligned}
0\le \sigma(m^\circ-m_T^\circ)&\le 2\sum_{i\in S}|D_i|(x_F)_i^2
\ \lesssim\ \mathcal L_\sigma(S),\\
\sum_{i\in S}|D_i|(x_T)_i^2&\le 2\sigma(m^\circ-m_T^\circ).
\end{aligned}
\tag{2}
$$
In particular, if $\min_S|D_i|\ge d_*>0$, then $\|(x_T)_S\|_2^2\lesssim d_*^{-1}\mathcal L_\sigma(S)$. The estimate applies to the **undamped** exterior with no sup norm gap there.

For the proof put $C=\operatorname{diag}(\sqrt{|D_i|}:i\in S)$ and $N=C(X_T)_{SS}C$, where $X_T$ is the exterior inverse. The [weighted response contraction](response-locality.md#contraction-and-response-derivative) holds for any strict diagonal. Its restriction to $S$ here is $(X_T)_{SS}$, since the reference diagonal vanishes there. Thus $\|N\|<1$, even if the exterior approaches saturation. The resolvent identity gives
$$
C(x_T)_S=(I-\sigma N)C(x_F)_S,\qquad
\sigma(m^\circ-m_T^\circ)=
\langle C(x_T)_S,(I-\sigma N)^{-1}C(x_T)_S\rangle
=\langle C(x_F)_S,(I-\sigma N)C(x_F)_S\rangle.
$$
Bound $I-\sigma N$ by $2I$ and its inverse from below by $I/2$, and then apply (1).

If also $1-\|K_{SS}\|\ge\delta>0$, the inside-only increment is at most $|S|/(\delta m_0^2)$, where $m_0=n/\sqrt q$, by the same compression formula at the zero reference and $\|(Ke)_S\|_2^2\le |S|/m_0^2$. Thus a fixed compression gap, $|S|=o(n)$ and $\mathcal L_\sigma(S)=o(1)$ suffice to make the [interaction](coset-activation.md#the-exact-interaction) vanish without estimating the two cross terms separately. For example, split at a fixed cap $L$ on $\sqrt n A_\sigma$. On the capped part it suffices that $\sum_{i\in S:\sqrt n A_{\sigma,i}\le L}R_{i0}^2=o(\tau)$. On the remainder one still needs the overlap itself to be $o(1)$. These are joint conditions along the chosen orders and floors. The global bound $\sum_{i\ne0}R_{i0}^2\le\tau$ alone does not supply them. A bound on the interaction is separate from a bound on $m_T^\circ$.

## One-sided spectral bound for removal of real damping

Use the [real damping](diagonal-damping.md) $f_t=\langle e,(K-tPDP)^{-1}e\rangle$. For $\varepsilon\ge0$ set $t=(1+\varepsilon)^{-1}$. Write $P_\sigma=(P+\sigma K)/2$, $x_\sigma=P_\sigma x$, and define on $V_\sigma=P_\sigma\mathbb R^n$
$$
L_\sigma=P_\sigma(I-\sigma D)P_\sigma\big|_{V_\sigma},\qquad
Z_\sigma=\sigma P_\sigma X P_\sigma\big|_{V_\sigma}.
$$
Both are positive definite there. In fact the Schur complement in the block decomposition of $\sigma H$ is $L_\sigma+C_\sigma L_{-\sigma}^{-1}C_\sigma^*$, where $C_\sigma$ is the off-diagonal block of $\sigma H$. Its inverse is $Z_\sigma$.

Define the nonnegative contributions
$$
E_\sigma(\varepsilon)=\varepsilon\langle x_\sigma,(I+\varepsilon Z_\sigma)^{-1}x_\sigma\rangle .
$$
Then
$$
-E_-(\varepsilon)\ \le\ m-t f_t\ \le\ E_+(\varepsilon).
\tag{3}
$$
Indeed, put $F(a,b)=\langle e,(H+aP_+-bP_-)^{-1}e\rangle$ for $a,b\ge0$. All inverses exist by the positive and negative diagonal blocks and their Schur complements. With $x(a,b)=(H+aP_+-bP_-)^{-1}e$, differentiation gives $\partial_aF=-\|P_+x(a,b)\|^2$, $\partial_bF=+\|P_-x(a,b)\|^2$. So $F(\varepsilon,0)\le F(\varepsilon,\varepsilon)\le F(0,\varepsilon)$. The middle entry is $t f_t$. The rank-update formula gives $F(0,0)-F(\varepsilon,0)=E_+(\varepsilon)$ and $F(0,\varepsilon)-F(0,0)=E_-(\varepsilon)$. The $E_\sigma$ are bounds from separate sector updates, not the positive and negative parts of the spectral measure of $H$.

The stationary pair supplies the energy estimate. With $r=PD\mathbf1/\sqrt n$, $HPu=2\sqrt W\,r$ follows from $v=Ku=Du$ and $\bar u=2\sqrt{W/n}$. Thus $r^{\mathsf T}x=(u_0-\bar u)/(2\sqrt W)$. The off-diagonal blocks in $KH+HK$ cancel, giving
$$
\sum_\sigma\langle x_\sigma,L_\sigma x_\sigma\rangle
=\langle x,Ke\rangle=(Kx)_0
=1+D_0m-\frac{u_0}{2\sqrt{nW}}\ \lesssim\ 1.
\tag{4}
$$
The last bound uses $M_0^2m=D_0+\Delta$. Consequently, with $g_\sigma=\lambda_{\min}(L_\sigma)$,
$$
\sigma(m-t f_t)\le E_\sigma(\varepsilon)
\ \lesssim\ \varepsilon\min\{g_\sigma^{-1},\,1+\mathcal L_\sigma(\{i\ne0\})\}.
\tag{5}
$$
For the gap bound use (4). For the overlap bound use $2x_\sigma=(I+\sigma D)x+\sigma(e-JDx)$; off the mark the last parenthesis is the constant $-u_0/(2\sqrt{nW})$, and the marked entries are bounded. Apply (1) on the bulk. This is the same overlap as in the exterior estimate, now on the entire bulk.

For example, if $S_\sigma$ includes all coordinates with $\sigma D_i>\rho$, where $0\le\rho<1$, and $\lambda_{\max}(\sigma K_{S_\sigma S_\sigma})\le1-\delta$, then $g_\sigma\ge(1-\rho)\delta/2$ by the [signed compression estimate](signed-coset-bands.md#transfer-from-one-sign-of-the-diagonal). For an empty high set use $g_\sigma\ge1-\rho$. The opposite-sign high set is unrestricted.

A joint-limit use is to take $\tau_p\to0$, $\varepsilon_p\to0$, $t_p=(1+\varepsilon_p)^{-1}$ through primes. If $f_{t_p}=o(1)$ at the true stationary diagonal and $\varepsilon_p/g_{\sigma,p}\to0$ (or $\varepsilon_p[1+\mathcal L_\sigma(\{i\ne0\})]\to0$), then $\limsup_p\sigma m\le0$. The leverage and theta brackets give $\limsup_p\sigma\log(\vartheta(\overline H_p)/\sqrt n)\le0$. Both directions would give the conjecture. A field-first version takes $p\to\infty$ at fixed floor $\tau>0$ and fixed $t<1$, then $t\uparrow1$, then $\tau\downarrow0$ along a sequence of floors. At each such floor a gap $g_\sigma\ge c(\tau)>0$ uniformly in large $p$ suffices for the correction, assuming cancellation of $f_t$ at every fixed $t<1$ on the true diagonals. Fixed-depth cancellation alone does not give that linear resolvent limit.

### A one-sided theta test using the gap without linear resolvent cancellation

There is another use of $g_\sigma\ge c(\tau)>0$ at fixed floor. It takes the fixed-depth input only for **nonlinear damped iterates**. At stationarity $PA_\sigma\in V_\sigma$, $\overline A_\sigma=\sqrt{W/n}$, and
$$
\|(I-\sigma D)^{1/2}A_\sigma\|_2^2=\sum_i 2w_i A_{\sigma,i}/u_i\le2W .
$$
The same upper bound $2W$ on the squared norm of the constant part after weighting gives $g_\sigma\|PA_\sigma\|_2^2\le8W$ by the triangle inequality.

Let $v_\alpha=\alpha K u_\alpha$, $u_\alpha=\sqrt{v_\alpha^2+4w}$, $0<\alpha<1$, and $A_{\alpha,\pm}=(u_\alpha\pm v_\alpha)/2$. Put $\gamma_0=\operatorname{arsinh}(v_0/2)$, $\gamma_{\alpha,0}=\operatorname{arsinh}(v_{\alpha,0}/2)$. Subtracting the squared norms of $u_\alpha$ and $v_\alpha$ gives $n\bar u_\alpha^2+(1-\alpha^2)\|Pu_\alpha\|_2^2=4W$. The directed mixed product is
$$
\begin{aligned}
e^{\sigma(\gamma_0-\gamma_{\alpha,0})}
&\le \langle A_\sigma,A_{\alpha,-\sigma}\rangle\\
&=\sqrt{nW}\,\bar u_\alpha/2
 +(1-\alpha)\langle PA_\sigma,P_\sigma u_\alpha\rangle/2\\
&\le W+\sqrt{W(1-\alpha)/(1+\alpha)}\,\|PA_\sigma\|_2 .
\end{aligned}
\tag{6}
$$
The first inequality retains only the marked product of the two positive vectors. The equality is orthogonality of the Fourier sectors. Conditional on the [fixed-depth trace argument](sparse-damping.md#taking-the-fixed-damping-limit), $\gamma_{\alpha,0}=o(1)$ at each fixed $\alpha,\tau$ by contraction. Take $p\to\infty$, then $\alpha\uparrow1$ at fixed $\tau$; a bounded $\|PA_\sigma\|_2$ suffices for $\limsup_p\sigma\gamma_0\le\log(1+\tau)$. If this holds along a sequence of fixed floors tending to zero, the theta bracket gives the same one-sided result as above. No norm bound on $PA_{-\sigma}$ is used. The prime-field gap, or the weaker one-sided stationary norm bound in (6), remains an assumption.

## Exact square-order control with decreasing floors

Take $q=r^2$ with $r$ odd prime, $n=(q-1)/2$, and any sequence $0<\tau_q\to0$. The [exact square theta certificate](square-order-control.md#square-order-comparison) gives $\vartheta(\overline H_q)=r-1$. The theta and leverage brackets imply $\gamma_0\to\tfrac12\log 2$, $D_0\to1/3$, $m\to3/8$, and $m^\circ\to1/3$. Meanwhile the **bulk** activation converges to $-1$ in normalized $\ell_2$.

To prove the bulk limit without identifying the support of an optimizer, let $l$ be the nonnegative mean-one minus spectrum from the square certificate. Its entries are $l_i=(r-\lambda_i)/(r+1)$ for $i\ne0$ and $l_0=(r+1)/2=n/(r-1)$, where $\lambda_i=(Fs)_i$. Orthogonality gives $\sum_i A_{+,i}l_i=\sqrt{nW}$. The normalized marked value of the stationary minus spectrum is at most the exact minus optimum $n/(r-1)$. Since $A_{+,0}A_{-,0}=1$, it follows that $A_{+,0}\ge(r-1)/\sqrt{nW}$, and hence $\sum_{i\ne0}A_{+,i}l_i\le\sqrt n(W-1)/\sqrt W$.

For $a_i=\sqrt n A_{+,i}$, the bulk identity $1+D_i=2a_i^2/(a_i^2+\tau)\le a_i/\sqrt{\tau}$ therefore gives, for each $c>0$,
$$
\frac1n\sum_{i\ne0}(1+D_i)\le\frac{\sqrt{\tau}}{c}+\frac2n\#\{i\ne0:l_i<c\}.
\tag{7}
$$
The empirical law of $\lambda_i/r$ tends to the real part of Haar measure on the circle. As in the [first-iterate calculation](smoothing.md#first-two-iteration-markers), away from the trivial frequency the two Jacobi lifts express $\lambda_i/r$ as the real part of $G(\psi)/G(\psi\chi)$ times the fixed unit phase $G(\chi)/r$ (which is real). [Katz, Theorem 9.6](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf) bounds each fixed nonzero moment of the ratio by $O_m(q^{-1/2})$ for the distinct shifts $1,\chi$ over any finite field. The two exceptional lifts have vanishing density, and quotienting by the two lifts leaves the real-part law unchanged. The endpoint $1$ has no atom. Fix $c$ in (7), let $r\to\infty$ with the chosen floors, and then let $c\downarrow0$. Boundedness by $2$ upgrades the normalized bulk $\ell_1$ estimate to $\ell_2$.

Fix $0<t<1$. Compare $tD^\circ$ to the reference $-t$ on the bulk and zero at the mark. The all-constant reference has inverse $(K-tP)/(1-t^2)$, with marked entry $c_t=[-1/n-t(1-1/n)]/(1-t^2)$. The rank-one change at the mark gives the entry $c_t/(1-tc_t)\to-t$ and a column with bulk entries $O_t(n^{-1/2})$. The resolvent identity against this column gives a marked scalar error $O_t((n^{-1}\sum_{i\ne0}(1+D_i)^2)^{1/2})=o(1)$. Thus the true stripped damped response tends to $-t$. Restoring the mark by rank one gives $f_t\longrightarrow-t/(1+t^2/3)$. The ordered real de-damping difference is
$$
\lim_{t\uparrow1}\lim_{r\to\infty}(m-tf_t)=\frac38+\frac34=\frac98 .
\tag{8}
$$
For the opposite order ($t\uparrow1$ at each fixed $r,\tau_q>0$) the difference is zero. By (3) and (5) the square family fails the uniform plus-sector control: $g_+\to0$ and the bulk $\mathcal L_+\to\infty$. A subsequence with either a positive gap lower bound or a bounded overlap would contradict (8) on that subsequence.

The same bulk limit computes the signed imaginary cutoff in the [resolvent sum rule](resolvent-sum-rule.md#using-the-signed-stationary-spectrum). At any fixed $\eta>0$, compare with the diagonal equal to $-1$ in the bulk and $D_0$ at the mark. Before changing the mark, the complex inverse of $K+P-i\eta I$ on the mean-zero space is $P_+/(2-i\eta)+P_-/(-i\eta)$. Its marked entry tends to
$$
c_\eta=\frac{1}{2(2-i\eta)}+\frac{1}{2(-i\eta)} .
$$
Changing the mark from $-1$ to $D_0$ is a rank-one update. The new resolvent column still has bulk sup norm $O_\eta(n^{-1/2})$ (use the Jacobi entry bound and the positive imaginary part of the constant-reference entry). The resolvent identity, the fixed-$\eta$ bound $\|(H-i\eta I)^{-1}\|\le1/\eta$, and the normalized bulk convergence show that the true marked complex entry tends to $c_\eta/(1-\tfrac43 c_\eta)$. Taking real parts and then $\eta\downarrow0$ gives $-3/4$, while $m\to3/8$. In the notation of the sum rule, $V_\eta=\langle v,\eta^2(H^2+\eta^2I)^{-1}e\rangle$, with $2M_0(m-\operatorname{Re}m_\eta)=V_\eta+O(\sqrt\tau)$. Thus
$$
\lim_{\eta\downarrow0}\lim_{r\to\infty}V_\eta
=\frac{4\sqrt2}{3}\,\frac98=\frac{3\sqrt2}{2}.
$$
This is an order-one signed contribution from the removed window of the true square stationary resolvent.

There is also an exterior comparison at the true square stationary pair. Let $S=\{i\ne0:D_i>0\}$, which has size $o(n)$ by (7), and put $D_T^\circ=D^\circ\mathbf1_{S^c}$. This diagonal is nonpositive and has the same bulk limit $-1$. The fixed-$t$ calculation yields $m(tD_T^\circ)\to-t$. Monotonicity in the diagonal and contractivity at the stripped mark give
$$
-1\le m(D_T^\circ)\le m(tD_T^\circ).
$$
Taking $t\uparrow1$ after the field limit gives $m(D_T^\circ)\to-1$ and $m^\circ-m(D_T^\circ)\to4/3$. Thus the same-sign overlap in (2) cannot vanish on this square-order set. The argument gives a nonzero marked deletion effect. Without an exterior compression gap it does not give a lower bound on the restricted exterior column norm.

### Finite-order checks

Dense inverses at orders $41,101,7^2,11^2,23^2$, with $\tau=0.05,0.01,0.003$ and both signs, check (2)–(4). The largest stationary residual was $9.95\times10^{-12}$; the largest discrepancies were $8.6\times10^{-15}$ for the deletion form, $5.9\times10^{-15}$ for the separate sector updates at $\varepsilon=0.03,0.3$, and $3.8\times10^{-14}$ for the energy. These are floating-point checks.

As a finite-order comparison at the fixed floor $\tau=0.001$, FFT solves give the following values. The stationary and inverse residuals are all less than $10^{-10}$ in these rows. The table does not approximate the ordered limits by interchanging the order of the parameters.

| $r$ | Bulk mean of $1+D$ | $f_{0.8}$ | $m(D_T^\circ)$ |
| ---: | ---: | ---: | ---: |
| 47 | 0.05371 | -0.35363 | -0.90801 |
| 97 | 0.03224 | -0.48404 | -0.94925 |
| 193 | 0.02240 | -0.56045 | -0.96854 |
| 389 | 0.01753 | -0.60394 | -0.97831 |

The prime problem still needs an arithmetic bound on the actual leverage overlap, a one-sided gap or norm bound at the relevant weights, or cancellation beyond the one-sided sector bounds. An exterior mass gap for the stationary spectrum alone gives none of these estimates.
