# Diagonal damping of the stationary response

Use the [stationary notation](resolvent-sum-rule.md). On the mean-zero space let $B=PDP$, $H=K-B$, and $e=Pe_0$. Introduce a real damping parameter $0\le t\le1$ and set

$$H_t=K-tB,\qquad x_t=H_t^{-1}e,\qquad f_t=\langle e,x_t\rangle.$$

This regularizes a large activated diagonal through the Neumann series of $KD$. At a fixed Picard depth it gives marked cancellation for every fixed $t<1$ using the even-product closure rule alone. For the true stationary diagonal, the cost of sending $t$ to one is a scalar pairing with the total spectrum.

The [cap argument](bulk-caps.md) uses the same fixed-depth closure to bound the stationary coordinate directly through positive tail mass. It gives a separate criterion based on the capped Fourier spectra and their difference sets.

For the stripped marked inverse, [sitewise attenuation](stationary-attenuation.md) extends the removal estimate to a different factor on each bulk coordinate and retains the weighted squared energy of the changed coordinates.

## The exact damping identity

At stationarity define $a=4/u_0$, $b=2PM\nu_{\rm bulk}$ as in the [source identity](stationary-tails.md), and put

$$\Xi_t=(1-t)\langle u,x_t\rangle,\qquad Q_t=(1-t)\langle v,x_t\rangle.$$

Then

$$v_0=t a f_t+\Xi_t+t\langle b,x_t\rangle.$$

Indeed $Hv=ae+b$ gives $a f_t+\langle b,x_t\rangle=v_0-(1-t)\langle v,Bx_t\rangle$. Also $Kv=Pu$ and $Kx_t=e+tBx_t$ give $\langle u,x_t\rangle=v_0+t\langle v,Bx_t\rangle$. These give the identity including $t=0$. Another expression for the pairing is the real Abel average

$$\Xi_t=(1-t)\sum_{j\ge0}t^j\big((KB)^j v\big)_0\qquad(t<1).$$

In fact $H_t^{-1}=(I-tKB)^{-1}K$ on the mean-zero space and $(KB)^*=BK$, so $\langle u,(KB)^j K e\rangle=\langle (KB)^jv,e\rangle$.

## A uniform removal estimate

Put $M_t=(1-t^2D^2)^{1/2}$ and $r=PD\mathbf1/\sqrt n$. The stationary equation implies

$$H_t Pu=(1-t)v+2t\sqrt W\, r,\qquad
t\langle r,x_t\rangle+\frac1{\sqrt n}=\frac{u_0-Q_t}{2\sqrt W}.$$

Apply the [weighted inverse sum rule](resolvent-sum-rule.md#the-sum-rule) to $tD$ at real spectral parameter zero. It gives

$$
(M_t)_{00}^2\left(f_t-\frac{tD_0}{(M_t)_{00}^2}\right)^2
+\|P_{\ne0}M_t x_t\|_2^2+\frac{(u_0-Q_t)^2}{4W}
=\frac1{(M_t)_{00}^2}.
$$

For $0<\tau\le1$, $u_0$ is bounded by the elementary Jacobi bound, and the marked entry $M_{00}=2/u_0$ of the undamped multiplier is separated from zero. The right side is at most $1/M_{00}^2=u_0^2/4$. The displayed equality therefore shows $|f_t|\ll1$ and

$$\|P_{\ne0} M_t x_t\|_2^2\ll\tau+(Q_t)_+.$$

Since $M_t^2\ge(1-t^2)I$, writing $\beta=1-t$ and $d=\beta\|v\|_2^2$ gives $\beta\|x_t\|_2^2\ll\tau+\beta+(Q_t)_+$. Cauchy–Schwarz then gives $(Q_t)_+\ll\sqrt{d(\tau+\beta+(Q_t)_+)}$, so $(Q_t)_+\ll\tau+\beta+d$. The same estimate bounds $|\Xi_t|$ because $\|Pu\|_2=\|v\|_2$. Also $|\langle b,x_t\rangle|\le 2\|\nu_{\rm bulk}\|_2\,\|P_{\ne0} M_t x_t\|_2$. Consequently

$$|f_1-t f_t|\ll \tau+(1-t)(1+\|v\|_2^2).$$

The argument at $t=1$ uses $\langle b,x_1\rangle=O(\tau)$. More generally the damping identity and the uniform bound on $\|M_t x_t\|_2$ give $|v_0-t a f_t-\Xi_t|\ll\sqrt\tau$. At weights tending to zero, a value $f_t=o(1)$ therefore leaves $\Xi_t$ as the required correction. This parallels the [imaginary cutoff](resolvent-sum-rule.md#using-the-signed-stationary-spectrum), with a different stationary pairing.

## What parity proves at fixed damping

Let $D^{(j)}=v^{(j)}/\Phi(v^{(j)})$ come from any fixed Picard depth $j$ at fixed $\tau$. Use the [fixed-depth inertia estimates](iteration-parity.md) as the arithmetic input. For fixed $t<1$ the reference column is

$$x_t^{(j)}=\sum_{k\ge0}t^k(KD^{(j)})^k K e.$$

After scaling by $\sqrt n$, each fixed term is approximable in normalized $\ell_2$ by bounded combinations of negative-type fields. The starting vector is the first Jacobi field. Multiplication by the bounded odd activation $D^{(j)}$ produces an even polynomial approximant, and $K$ on it gives another negative-field approximant. At an approximation step, first choose a bounded approximant to the vector being multiplied, then approximate the diagonal in normalized $\ell_2$ so that the product error is small. The actual mark of the diagonal contributes a negligible error when approximating its bounded activation in that norm. The unscaled $\ell_2$ norms of the series terms before damping are at most one. Thus the series can be truncated and then approximated to any fixed accuracy by a uniformly bounded field after scaling.

In particular the column has $o(1)$ squared norm on any $o(n)$ set, so $f_t(D^{(j)})\to0$. Moreover, if another real diagonal $D'$ with $\|D'\|\le1$ differs from $D^{(j)}$ by $o(1)$ in normalized $\ell_2$, the resolvent identity gives

$$|f_t(D')-f_t(D^{(j)})|\le\frac{t}{1-t}
\|(D'-D^{(j)})x_t^{(j)}\|_2=o(1).$$

To see the last step, approximate the scaled reference column by a bounded field in normalized $\ell_2$. The product of this approximant with the diagonal difference tends to zero, and the product of the approximation error with that difference is controlled by the uniform bounds on the diagonals. The comparison allows arbitrary changes on $o(n)$ frequencies, including the mark, and needs no compression gap because $t<1$ is fixed. This calculation uses only $K$ on even polynomial inputs. The [odd moment approach for imaginary regularization](marked-response.md#what-fixed-depth-parity-gives-for-the-symmetric-operator) already has a new odd-field pairing at moment seven.

### An iterated-limit transfer

The conclusion $f_t(D)\to0$ also follows from the more flexible approximation

$$\lim_{j\to\infty}\limsup_{p\to\infty}
\left(\frac1n\sum_i |D_i-D_i^{(j)}|^2\right)^{1/2}=0.$$

Here no uniform-in-depth bound on the approximants to the resolvent columns is required. Write $w_k(E)=(K E)^k K e$. Inductively, $w_k(D)$ is approximable in unscaled $\ell_2$ by vectors with $\ell_\infty$ norm at most $C/\sqrt n$ at any fixed accuracy, and

$$\lim_{j\to\infty}\limsup_{p\to\infty}\|w_k(D)-w_k(D^{(j)})\|_2=0.$$

The base $k=0$ follows directly from the Jacobi bound. Given this assertion at $k$, the difference at $k+1$ is bounded by the difference at $k$ plus $\|(D-D^{(j)})w_k(D)\|_2$. Approximate $w_k(D)$ by a bounded scaled vector at a fixed accuracy first, then apply the normalized diagonal approximation. This proves the convergence at $k+1$. Choose a fixed sufficiently large $j$ and use the bounded scaled approximants for $w_{k+1}(D^{(j)})$ to establish the approximation property for $w_{k+1}(D)$. Each fixed term thus vanishes at the mark, and the norm bound on the geometric tail proves $f_t(D)\to0$ for each fixed $t<1$.

For the all-prime target one sufficient combination along fixed weights $\tau\downarrow0$ is $f_t\to0$ for each fixed $t<1$ through primes and $\lim_{t\uparrow1}\limsup_p|\Xi_t|=0$. The first condition reduces to the iterated-limit diagonal approximation above. The second is an estimate on the removal of damping. Both conditions for the true stationary diagonal remain open.

## Numerical comparison

The [window probe](../response_windows.py) with the diagonal damping option uses MINRES on $H_t$, with $1-t$ equal to the reported width. It records both pairings and compares the exact identities at the true numerical stationary diagonal. At $\tau=0.05$ and $1-t=0.25$, the results are

| Field order | $f_1$ | $f_t$ | $\Xi_t$ | $Q_t$ |
|---:|---:|---:|---:|---:|
| $389^2$ | 0.394327 | -0.370149 | 1.084300 | 1.580955 |
| 151337 | -0.001094 | 0.000072 | -0.002315 | 0.616668 |

The prime comparison shows cancellation in the pairing that appears in the damping identity, even while the other pairing in the sum rule is substantial. In the [60 recorded runs](../data/response-damping.csv) the sum-rule discrepancy is at most $5.8\cdot10^{-11}$, the source discrepancy is at most $8.3\cdot10^{-9}$ and the solve residual is at most $1.3\cdot10^{-8}$. At four small prime and square orders, 24 dense inverses across six widths agree with the FFT-based marked entries to within $8.2\cdot10^{-14}$.

At the same weight, the normalized $\ell_2$ difference between the stationary diagonal and depths $4,16,64$ is approximately $(0.37979,0.12762,0.00150)$ at $p=1000033$ and $(0.89648,0.89520,0.87976)$ at $389^2$. These diagnostics use `smoothing(sign, 0.05, 0, j + 1)` for the depth-$j$ vector and the diagonal returned by `marked_system`. The numerical stationary residual is below $10^{-9}$ in both cases. The two sets of measurements distinguish the fixed-depth approximation problem from the removal of damping.
