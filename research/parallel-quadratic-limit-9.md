# The reciprocal quadratic path: exact secants and the zero penalty endpoint

This is a deterministic calculation for the quadratic path proposed for [Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/). The sum of the two sector energies is monotone and selects the two minimum-norm theta witnesses at the endpoint. Their difference drives the value and need not have a fixed sign, even at prime order. The estimates give a finite-cutoff certificate and locate a square-order obstruction at the scale $n^{-1/2}$. They do not close the prime-field boundary estimate.

## A two-point identity

Use the [Fourier conventions](fourier.md) and write $P=P_\sigma$, $N=P_{-\sigma}$, $C=\{b\ge0:b_0=1\}$. Fix one sign, and use $r$ for the penalty parameter, not the square root of the field order. For $r>0$ let

$$
 Q_r=J+rP+r^{-1}N,\qquad b_r=\arg\min_C b^\mathsf TQ_r b,\qquad y_r=Q_r b_r,\qquad M_r=(y_r)_0.
$$

The normal equations give $y_r\ge0$, $b_r\odot y_r=M_r e_0$, and $M_r=b_r^\mathsf TQ_r b_r>0$. The inverse matrix is $Q_{-\sigma}(r)$, and $y_r/M_r$ is its rooted optimizer by the same equations. Define

$$
 a_r=\langle b_r,\mathbf1/\sqrt n\rangle,\quad u_r=Pb_r,\quad z_r=Ny_r,
 \quad w_r=(u_r,z_r),\quad H_r=\|w_r\|^2,\quad S_r=\|u_r\|^2-\|z_r\|^2.
$$

Then $Jb_r=Jy_r$, $Nb_r=r z_r$, $Py_r=r u_r$, and

$$ M_r=a_r^2+rH_r,\qquad M'_r=S_r. \tag{1} $$

The derivative follows by differentiating the objective at its unique minimizer. In particular the derivative of $\log M_r$ in logarithmic time is $g_r=rS_r/M_r$, with $|g_r|\le rH_r/M_r$.

For $0<s<r$ define the two nonnegative contact losses

$$ d_{sr}=\langle b_s,y_r\rangle-M_r,\qquad d_{rs}=\langle b_r,y_s\rangle-M_s. $$

Subtract the spectral relations at $s,r$, and use $\langle b_r-b_s,y_r-y_s\rangle=-d_{sr}-d_{rs}$. The resulting identity is

$$
 \boxed{\frac{r-s}{2}(H_s-H_r)
  =\frac{r+s}{2}\|w_r-w_s\|^2+(a_r-a_s)^2+d_{sr}+d_{rs}.} \tag{2}
$$

Thus $H_r$ is nonincreasing. In particular a large change of the active spectra costs a drop of total energy or requires a large ratio of scales. The exact signed cross secant is

$$
 M_r-M_s=(r-s)(\langle u_s,u_r\rangle-\langle z_s,z_r\rangle)-d_{sr}+d_{rs}. \tag{3}
$$

Both identities use full Fourier coordinates, including the mark. The losses vanish when the two solutions have the same positive support for $b$ off the mark. Formula (2) continues to hold when either support switches.

For another computable secant interval, use the saddle function

$$ L_r(b,z)=\|Jb\|^2+2\langle z,b\rangle+r(\|Pb\|^2-\|z\|^2),\qquad b\in C,\ z\in\operatorname{ran}N. $$

Maximizing out $z$ gives the original energy. The pair $(b_r,z_r)$ is a saddle: its derivatives in the two variables give $y_r$ and $Nb_r-rz_r=0$, respectively. Compare $L_r(b_s,z_r)$ and $L_r(b_r,z_s)$ to their counterparts at $s$ to obtain

$$
 \|u_r\|^2-\|z_s\|^2\ \le\ \frac{M_r-M_s}{r-s}\ \le\ \|u_s\|^2-\|z_r\|^2. \tag{4}
$$

The positive terms in (2) make its constraint stronger than a norm monotonicity check on a numerical path.

## Exactly which theta witnesses the path selects

At $s=0$, take any rooted nonnegative optimum $b_*$ in $\operatorname{ran}(J+P)$, and any rooted nonnegative optimum $c_*$ in $\operatorname{ran}(J+N)$. Their means, in units of $\mathbf1/\sqrt n$, are $\sqrt n/\theta_\sigma$ and $\sqrt n/\theta_{-\sigma}$. Set $M_*=n/\theta_\sigma^2$ and $y_*=M_*c_*$. The complementary theta identity implies $Jb_*=Jy_*$, and orthogonality then gives $\langle b_*,y_*\rangle=M_*$, so they are complementary off the mark. Consequently $(b_*,Ny_*)$ is a saddle also at $r=0$: at fixed $b_*$ the value is $M_*$ for any $z$, and the gradient of $L_0(\cdot,Ny_*)$ at $b_*$ is $2y_*$. Equations (2)–(4) apply with $s=0$ and with this **arbitrary** pair of endpoint witnesses.

Let $b_0^*,c_0^*$ be the minimum Euclidean norm witnesses among the respective theta optima. They exist and are unique: the fixed optimal mean makes each nonnegative feasible face compact, and the squared norm is strictly convex. These choices minimize $H_0$ independently in its two sectors. Equation (2) bounds $w_r$ by their $H_0$ and gives $a_r\to\sqrt{M_*}$ as $r\downarrow0$ for each fixed field. Any subsequential limit recovers a rooted complementary pair by $Nb_r=r z_r$ and $Py_r=r u_r$, and has energy at most $H_0$. It must therefore be this minimum-norm pair. Thus $M$ is right differentiable at the endpoint with

$$
 M_0=M_*,\qquad M'(0+)=\|P b_0^*\|^2-M_0^2\|N c_0^*\|^2. \tag{5}
$$

In particular the slope is a difference of two *separate* minimum-norm problems. A flat slope is consistent with both witnesses having large squared norm.

For a dimension bound, any rooted endpoint optimum has every coordinate at most $1$: otherwise translate a larger coordinate to the mark and rescale, strictly decreasing the mean at fixed root. Thus $y_0^*$ has every coordinate at most $M_0$, and

$$ H_0\le (1+M_0)\sqrt{nM_0}-2M_0=O(\sqrt n). \tag{6} $$

Here $M_0$ is bounded above and away from zero by the two [constant Fourier witnesses](fourier.md#feasible-parameters-and-objective) and reciprocity. The same bounds hold for every $0<r\le1$ by a direct calculation: $b_r-y_r=\kappa\sigma K(b_r+y_r)$ for $\kappa=(1-r)/(1+r)$, so the Jacobi point bound gives $|1-M_r|\le2\sqrt{q/n}\,a_r\le2\sqrt{q/n}\sqrt{M_r}$.

Equation (4) yields $|M_r-M_0|\le rH_0$. There is a different bound that can be sharper at a measured cutoff. Positivity of either cross loss gives

$$
 M_r\le \sqrt{M_0}\,a_r+r\langle u_0,u_r\rangle,qquad
 M_0\le \sqrt{M_0}\,a_r+r\langle z_0,z_r\rangle. \tag{7}
$$

For the first comparison use $M_r\le\langle b_0^*,y_r\rangle$; for the second use $M_0\le\langle b_r,y_0^*\rangle$. Using $a_r\le\sqrt{M_r}$, the uniform bounds on $M_r,M_0$, and Cauchy–Schwarz, these give

$$
 (\log M_r-\log M_0)_+\ll r\|u_0\|\|u_r\|,\qquad
 (\log M_0-\log M_r)_+\ll r\|z_0\|\|z_r\|. \tag{8}
$$

For example, a finite-cutoff certificate is $|\log M_r-\log M_0|\ll r n^{1/4}\sqrt{H_r}$. This bound uses the actual total energy at the cutoff; it does not require an endpoint solve. At $r=c/\sqrt n$ it is $O(\sqrt{c(1-a_r^2/M_r)})$ by (1). The power of $n$ alone does not ensure small error for larger $r$.

There is also a one-sided criterion. Under fixed-$r$ convergence, it would suffice to bound uniformly the minimum-norm endpoint energy $\|u_0\|^2$ of the sign with $M_0\le1$ (the larger theta). Indeed $M_r\le M_0+r\|u_0\|^2$ from the primal endpoint trial; then take the field limit for fixed $r$, followed by $r\downarrow0$. Conversely, if $M_0\le1-\delta$ along a subsequence, this sign's minimum-norm energy must diverge: for every fixed $r>0$ it is at least $\delta/(2r)$ eventually. This does not force divergence at a specified rate in the field order.

## The signed integral on a logarithmic mesh

For a fixed field each possible positive support $A\ni0$ gives a rational candidate, by solving the positive definite principal subproblem on $A$. Positivity and the remaining sign conditions are rational inequalities and there are finitely many supports. This makes the path piecewise rational for $r>0$, with finitely many pieces and $C^1$ value. No need to assume that the active support has stable size as the field grows. On each open piece the contact terms in (2) are zero; dividing by $(r-s)^2$ and letting $s\to r$ gives the exact dissipation $-H'_r/2=r\|w'_r\|^2+(a'_r)^2$. Its integral over $(0,\epsilon)$ is $(H_0-H_\epsilon)/2$ by continuity at the switches and the endpoint selection.

On an open piece with fixed support put $t=\log r$, $F(t)=\log M_r$, $T=P-N$, and $h_r=rH_r/M_r$. Write $x=\partial_t b_r$ and use the $Q_r$ inner product. If $W$ is the subspace supported on the active bulk coordinates, the differentiated first order equations give $x=-\Pi_W^{Q_r}(T b_r)$ and $b_r\perp_{Q_r}W$. In particular

$$
 \|x\|_{Q_r}^2\le \|T b_r-g_r b_r\|_{Q_r}^2=M_r(h_r-g_r^2),\qquad
 F''(t)=h_r-g_r^2-2\|x\|_{Q_r}^2/M_r. \tag{9}
$$

Hence $|F''(t)|\le h_r-g_r^2\le1$ on each piece, and $F'$ is globally $1$-Lipschitz in $t$ by continuity across the switches. If $M_r\to1$ for every fixed $r>0$, then $g_r\to0$ uniformly on each compact interval bounded away from zero, by this Lipschitz bound and difference quotients of $F$. This strengthens pointwise value convergence but leaves the unbounded logarithmic tail.

For instance, for $0<c<1$ and fixed $\epsilon>0$ with $c/\sqrt n<\epsilon$, one has the unconditional finite-field criterion

$$
 \left|\log M_0-\log M_\epsilon+\int_{c/\sqrt n}^{\epsilon}g_r\,\frac{dr}{r}\right|\ll c. \tag{10}
$$

Thus it suffices to cancel the signed integral over the moving interval as $c\downarrow0$ after the field limit. Midpoint evaluation on a log mesh of max width $h$ has deterministic error at most $h\log(\epsilon\sqrt n/c)/4$ by (9). The two-sided difference (4) gives an independent secant check. In particular fixed log mesh width does not give an order-uniform error for the full integral.

## Three controls

**Failure of analyticity inside the interval.** At $p=13$ take the plus sign and generator $4$ of the squares. Then $n=6$ and $K$ has first row $(-1,3,-1,-3,-1,3)/6$. The first row of $12rQ_r$ has the form $(N_0,N_1,N_2,N_3,N_2,N_1)$ where

$$ N_0=6+2r+4r^2,\quad N_1=-4+2r+2r^2,\quad N_2=2r-2r^2,\quad N_3=2+2r-4r^2. $$

The optimizer restricted to $\{0,1,5\}$ is $b=(1,a,0,0,0,a)$, $a=-N_1/(N_0+N_2)=(1-r)(r+2)/(r^2+2r+3)>0$ on $(0,1)$. Its $y_3$ is strictly positive there, and

$$ (Q_rb)_2=(Q_rb)_4=\frac{4(1-r)(r^2+3r-1)}{12r(r^2+2r+3)}. $$

For $r\ge r_*=(\sqrt{13}-3)/2$ this candidate is optimal all the way up to $1$; just below $r_*$ the coordinates $2,4$ activate. To see the loss of $C^2$, set $v=e_1+e_5$ and $w=e_2+e_4$. Eliminating the coefficient of $v$ gives a positive Schur complement $B=w^\mathsf TQ_rw-(v^\mathsf TQ_rw)^2/(v^\mathsf TQ_rv)$. The additional optimal coefficient of $w$ just below $r_*$ is $-w^\mathsf TQ_rb/B>0$. The other strict signs persist, so this is the full solution there, reducing the value by $(w^\mathsf TQ_rb)^2/B$. That numerator vanishes to exactly second order. The only smaller eligible prime is $5$, where the two values $2/(1+r)$ and $(1+r)/2$ are analytic throughout $(0,1)$.

**Failure of monotonicity at a prime.** For either sign $b_1=e_0$ and $M'_\sigma(1)=\sigma K_{00}=-\sigma/n$. In particular $M_+(r)>1$ immediately to the left of $1$. At $p=97$ there is a feasible plus row with marked Fourier value at least $6951/1003>\sqrt{48}$, so $M_+(0)<1$. An integer certificate uses generator $5$ of the field units and total pair masses on positive exponents $j$ of $25$:

```
j:      1    7    8   11   13   14   17   18   19   21   22   24
mass:1553  997 1486 1133  460  121  416 1988 1732  657 1365  -12
```

The masses appear in $f(25^j)+f(25^{-j})$, with the singleton counted once at $j=24$. Set $f(1)=2006$ and divide the whole row by $2006$. The [rational cosine enclosure routine](../theta.py) at scale $2000$ gives minimum lower bound $1743/2000$ before row normalization; the total row mass before normalization is $13902$. Both endpoints of the path are below its value at an interior point, so neither direction of monotonicity holds for $M_+$. By reciprocity neither direction holds for $M_-$ there either.

**A square layer survives at a moving cutoff.** For $q=h^2$ use the [subfield witness](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy) $b=\mathbf1_A$, $|A|=m=(h+1)/2$, $Pb=b-Jb$, $Nb=0$. Here $M_+(0)=m^2/n\to1/2$. The exact trial gives

$$ M_+(c/\sqrt n)\le m^2/n+c\,(m-m^2/n)/\sqrt n,\qquad \limsup_{h\to\infty}M_+(c/\sqrt n)\le 1/2+c/\sqrt2. $$

For every $0<c<1/\sqrt2$ the bound is strictly below $1$. If one uses the given fixed-$r$ convergence at squares, then for every fixed $\epsilon>0$ the signed integral from $c/\sqrt n$ to $\epsilon$ has liminf at least $-\log(1/2+c/\sqrt2)>0$. This control uses an explicit finite-field witness and separates the two scales. Any argument deriving the requisite signed cancellation from (1)–(10) and fixed-$r$ convergence alone would also have to apply to this square sequence. A prime-specific target is either the integral in (10), or a bound on the large-theta side's regularization cost strong enough to use the endpoint trial. Neither follows from just the total-energy monotonicity.

As normalization checks, 576 dense nonnegative least-squares solves over eight primes ($5$ to $173$), two signs and 36 penalties checked the contact identities to $1.5\cdot10^{-13}$. The maximum numerical secant inequality violation was $1.1\cdot10^{-11}$, and the curvature check agreed up to $2\cdot10^{-16}$. These checks are floating point; the $p=97$ certificate uses rational enclosures.
