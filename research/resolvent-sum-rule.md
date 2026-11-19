# A stationary sum rule for the marked resolvent

Use the mean-zero space $P\mathbb R^n$, where $P=I-J$ and $K^2=P$. Set $B=PDP$, $H=K-B$, $G=K+B$, and $e=Pe_0$. Here $D$ is real diagonal with $|D_i|<1$. Put $M_i=\sqrt{1-D_i^2}$ and $r=P D\mathbf1/\sqrt n$.

## The sum rule

On the mean-zero space,

$$HG+GH=2(I-B^2)=2(PM^2P+rr^{\mathsf T}).$$

The rank-one term is the correction for compressing $D$ to mean zero. For $\eta>0$ write $x_\eta=(H-i\eta)^{-1}e$, $m_\eta=e^{\mathsf T}x_\eta$, and $k_\eta=r^{\mathsf T}x_\eta$. Taking the quadratic form on $x_\eta$ makes the left side $2\operatorname{Re}(e^{\mathsf T}Gx_\eta)$, since $Hx_\eta=e+i\eta x_\eta$ and $G$ is self-adjoint. Also $Ge=He+2D_0e-2r/\sqrt n$. These give

$$\|Mx_\eta\|_2^2+|k_\eta|^2=\|e\|_2^2-\eta\operatorname{Im}m_\eta+2D_0\operatorname{Re}m_\eta-2\operatorname{Re}k_\eta/\sqrt n.$$

Completing the two squares, with $x_{\eta,0}=m_\eta$ and $\|e\|_2^2=1-1/n$, yields the exact identity

$$M_0^2\left|m_\eta-\frac{D_0}{M_0^2}\right|^2+\|P_{\ne0}Mx_\eta\|_2^2+\left|k_\eta+\frac1{\sqrt n}\right|^2+\eta\operatorname{Im}m_\eta=\frac1{M_0^2}.$$

All four terms on the left are nonnegative.

## Transfer from a regularized signed response

Now take the true stationary $D_i=v_i/u_i$ with $w_0=1$, $w_i=\tau/n$ in the bulk, $W=\sum_i w_i$, and $u=\Phi(v)$. The equations $Ku=v$, $Du=v$ and $\overline u=2\sqrt{W/n}$ give $H P u=2\sqrt W\,r$. Consequently

$$k_\eta+\frac1{\sqrt n}=\frac{u_0+i\eta u^{\mathsf T}x_\eta}{2\sqrt W}.$$

Let $R_\eta=\eta^2(H^2+\eta^2)^{-1}$ on the mean-zero space and $T_\eta=\langle u,R_\eta e\rangle$. The real part of $u_0+i\eta u^{\mathsf T}x_\eta$ is $u_0-T_\eta$. Keeping just the first and third terms in the sum rule proves

$$M_0^2\left|m_\eta-\frac{D_0}{M_0^2}\right|^2\le\frac1{M_0^2}-\frac{(u_0-T_\eta)^2}{4W}\ll \tau+(T_\eta)_+$$

for $0<\tau\le1$, using $u_0=2/M_0=O(1)$. By the [leverage identity](marked-response.md#a-symmetric-operator-for-the-response), $M_0^2m(0)-D_0=\Delta$ with $|\Delta|\le\tau$. In particular

$$|\operatorname{Re}m_\eta-m(0)|\ll \sqrt{\tau+(T_\eta)_+}.$$

At weights $\tau_p\to0$, proving $\operatorname{Re}m_{\eta_p}\to0$ and $(T_{\eta_p})_+\to0$ for a choice of widths would imply $D_0\to0$ and give Conjecture 26 by the theta bracket. This criterion tests the signed response in the retained window and a single mixed correlation in the removed window.

The [stationary spectral-mass bound](stationary-tails.md) gives $\mu([-t,t])\ll t^2\|v\|_2^2+\tau t$. Integrating the squared filter, with dyadic annuli beyond $\eta$, yields $\|R_\eta e\|_2^2\ll \eta^2\|v\|_2^2+\tau\eta$. Since $\|Pu\|_2=\|v\|_2$, we obtain $(T_\eta)_+\ll\eta\|v\|_2^2+\sqrt{\tau\eta}\|v\|_2$. Therefore the signed difference is $O(\sqrt\tau+\sqrt\eta\|v\|_2)$. At $\tau_p\to0$ this controls the signed cutoff below the critical width for all rates of decay of the weights. At width $O(p^{-1/2})$, the extra bound $\|v\|_2^2=o(\sqrt p)$ suffices. Estimating $T_\eta$ directly could account for wider windows where the norm estimate is too large.

At any zero of $\operatorname{Re}m_\eta$ the same sum rule gives $|u_0-T_\eta|\le2\sqrt W$, since the first term is at least $D_0^2/M_0^2$. Such a zero necessarily exists along any sequence with $\tau\to0$ and $|D_0|$ bounded away from zero. The sign at $\eta=0$ is the sign of $D_0$ by the leverage identity, whereas $\eta^2\operatorname{Re}m_\eta\to\langle e,He\rangle=-D_0+O(1/n)$ as $\eta\to\infty$. Hence a hypothetical counterexample forces $T_\eta\ge u_0-2\sqrt W$ at every zero. Finding a zero by itself supplies no estimate of the theta limit.

## Using the signed stationary spectrum

Write $a=4/u_0=2M_0$ and $b=2PM\nu_{\rm bulk}$, where $\nu_i=\sqrt{w_i}$. The [stationary source identity](stationary-tails.md#a-strongly-coupled-narrow-band-forces-stationary-mass) is $Hv=ae+b$. Pairing with $x_\eta$, taking real parts, and subtracting the equality at zero width gives

$$a\big(m(0)-\operatorname{Re}m_\eta\big)
=\langle v,R_\eta e\rangle+b^{\mathsf T}(\operatorname{Re}x_\eta-x_0).$$

The sum rule bounds $\|P_{\ne0}Mx_\eta\|_2$ uniformly for all $\eta\ge0$ when $\tau\le1$, so the last term is $O(\sqrt\tau)$. Keeping the contribution of the mean term in the sum rule also bounds the squared bulk norm by $O(\tau+(T_\eta)_+)$. At $\eta=0$ this is $O(\tau)$. With $V_\eta=\langle v,R_\eta e\rangle$ we obtain the two bounds

$$a\big(m(0)-\operatorname{Re}m_\eta\big)=V_\eta+O(\sqrt\tau),\qquad
|m(0)-\operatorname{Re}m_\eta|\ll\tau+\eta\|v\|_2^2.$$

For the second bound, $|V_\eta|$ and $(T_\eta)_+$ are both $O(\tau+\eta\|v\|_2^2)$ from the sharper squared-filter estimate. The source correction is $O(\tau+\sqrt{\tau(T_\eta)_+})$, by Cauchy–Schwarz against the two bulk norms. The first bound gives a sufficient criterion using **signed** $V_\eta$ in place of the positive part of $T_\eta$. At $\tau_p\to0$, vanishing of $\operatorname{Re}m_{\eta_p}$ and $V_{\eta_p}$ implies $m(0)\to0$ and then the theta limit. It permits cancellation between the positive and negative components of the stationary spectrum in the removed window.

## Measuring cancellation in regularized windows

The [diagonal damping comparison](diagonal-damping.md) uses a real inverse and a different stationary pairing. It gives fixed-damping cancellation on the fixed-depth Picard diagonal using the even-product inertia rule.

The [window probe](../response_windows.py) solves $(H^2+\eta^2)y=e$. Then $x_\eta=Hy+i\eta y$, $T_\eta=\eta^2\langle u,y\rangle$, and $b_\eta=\eta\operatorname{Im}m_\eta$ is the filtered marked mass. Write $J_\eta^+$ and $J_\eta^-$ for the two nonnegative integrals of $|\lambda|/(\lambda^2+\eta^2)$ against the marked spectral measure on the positive and negative spectra. Since $|\lambda|\le2$,

$$J_\eta^++J_\eta^-\ge\frac{\|e\|_2^2-b_\eta}{2},\qquad J_\eta^+-J_\eta^-=\operatorname{Re}m_\eta.$$

The probe combines these relations into a lower bound on each contribution. Its output includes both regularized and unregularized signed entries, the mixed correlation, and the residual of the sum-rule identity. The numerical diagonal comes from a converged floating-point smoothing run.

At $\tau=0.05$ and $\eta=0.05$, the following cases compare the retained signed value with the two separate spectral contributions. The lower bounds at $p=151337$ show that each sign contributes at least $0.2485$ to within the recorded numerical accuracy.

| Order | $m(0)$ | $\operatorname{Re}m_\eta$ | $T_\eta$ | Lower bound on $J_\eta^+$ | Lower bound on $J_\eta^-$ |
|---|---:|---:|---:|---:|---:|
| $389^2$ | 0.394327 | -0.481654 | 1.466675 | 0.006691 | 0.488346 |
| $151337$ | -0.001094 | -0.001177 | 0.011719 | 0.248506 | 0.249683 |

At width $4/\sqrt q$, the mixed correlation is about $0.98250$ at $389^2$ and $0.000523$ at $151337$. Across the [60 recorded windows](../data/response-windows.csv), the sum-rule identity holds to within $3.6\times10^{-12}$ and the regularized solve residuals are at most $10^{-10}$. Dense complex resolvents and direct spectral sums cross-check four widths at two small prime and two small square orders. A proof through all primes still needs uniform cancellation and mixed-correlation control.

The same file now records $V_\eta$ and the bulk source term, with stationary source errors below $10^{-8}$. At $\tau=0.05$, $\eta=0.25$, and $p=151337$, the total-spectrum correlation $T_\eta$ is about $0.202175$ and the signed correlation $V_\eta$ is about $-0.000647$. At $389^2$ these are $1.513552$ and $1.368335$ respectively. The wider window illustrates the cancellation available in the signed criterion.
