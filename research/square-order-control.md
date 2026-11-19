# What the prime-field hypothesis has to exclude

## A square-order comparison

Let $r$ be an odd prime, $q=r^2$, and $Q$ the nonzero squares in $\mathbb F_q$. Write $n=(q-1)/2$, and use the same sign $s(a)=\chi_q(1-a)$, Fourier multiplier $K$, and smoothing weights as in the [prime-order calculation](smoothing.md).

On square orders the exact value is

$$\vartheta(\overline H_q)=r-1,\qquad \vartheta(H_q)=(r+1)/2.$$

Indeed, $B=\mathbb F_r^\times$ lies in $Q$, and the difference of any two distinct elements of $B$ is also in $B$. Thus $B$ is a clique of size $r-1$. For the matching bound use the row $f_-=\mathbf 1_{\{1\}}+2\mathbf 1_{\{s=-1\}}/(r+1)$ on the other support. For a nontrivial character $k$ on $Q$, its Fourier coefficient is $1+(-1-\lambda_k)/(r+1)$, where $\lambda=Fs$. The two-lift Jacobi bound $|\lambda_k|\le\sqrt q=r$ gives nonnegativity. Since $\sum_Q s=-1$, there are $n/2$ negative signs, and the marked Fourier coefficient of the row is $1+n/(r+1)=(r+1)/2$. The complementary product identity now bounds the other theta value from above by $r-1$. In particular the square-order normalized limit is $\sqrt2$. [Fourier witness conventions](fourier.md)

The [fixed-depth inertia proof draft](iteration-parity.md) applies to this family with field size $q$ in place of $p$. Its geometric arguments use tame inertia at $1$ in odd characteristic. The rank and bad-character counts for any fixed expression come from tame conductor bounds, and the weight estimate is $O(q^{-1/2})$. Fourier inversion and the two-to-one character restriction use the cyclic multiplicative group, which also exists at these orders. Thus the same argument gives $v_0^{(t)}\to0$ for every fixed depth, including the averaged updates.

The exact fixed point has a different limit behavior. For each fixed $0<\tau<1$, the [marked-coordinate bracket](smoothing.md) gives

$$\liminf_{r\to\infty}\operatorname{arsinh}(v_0^*/2)\ \ge\ \tfrac12\log\frac{2}{1+\tau}\ >\ 0.$$

In particular, conditional on the fixed-depth proof draft, $\|v^*\|_2\to\infty$ at square orders for each such $\tau$. If it stayed bounded along a subsequence, the [averaged residual criterion](iteration-parity.md#the-remaining-analytic-limit) would put every subsequential limit of the normalized theta at most $\sqrt{1+\tau}$ there. This contradicts the exact square-order value. The same example exhibits the failure of interchanging the fixed-depth and field-size limits in the marker.

The [second criterion](iteration-parity.md#a-criterion-involving-only-the-iterates) fails quantitatively. Put $c_\tau=\frac12\log(2/(1+\tau))$. For each fixed depth $t$, the discrepancy estimate and $z^{(t)}_0\to0$ imply $\liminf_{r\to\infty}D_t\ge c_\tau^2$. For any fixed $T$, the telescoping inequality then gives $\liminf_{r\to\infty}\langle z^{(T)},v^*\rangle\ge Tc_\tau^2$. The marked term tends to zero and $\|v^*\|_1\le2\sqrt{nW}$. Consequently

$$\liminf_{r\to\infty}\sqrt n\max_{k\ne0}|z^{(T)}_k|\ge \frac{c_\tau^2}{2\sqrt{1+\tau}}T.$$

This bound is for the averaged iterates, with the field size sent to infinity at each fixed depth.

## The Fourier frequencies carrying the discrepancy

Let $A$ be the characters on $Q$ trivial on $B$. Then $|A|=(r+1)/2$ and

$$\lambda_0=-1,\qquad \lambda_k=r\quad(k\in A\setminus\{0\}),\qquad K\mathbf 1_A=\mathbf 1_A-\frac{1}{r-1}\mathbf 1.$$

For the transform values, sum $s$ on a coset $bB$ of $B$. At $b=1$ the sum is $r-2$. Otherwise the character is $\chi_r(N(1-tb))$ for $t\in\mathbb F_r^\times$, since $\chi_q=\chi_r\circ N$. The quadratic $N(1-tb)$ has nonzero discriminant $(b-b^r)^2$ and square leading coefficient because $b\in Q$. The complete quadratic character sum is $-1$, and removing $t=0$ gives $-2$. Orthogonality on $Q/B$ gives the stated transform values. The identity for $K\mathbf1_A$ follows by Fourier inversion since $s$ is $+1$ on $B\setminus\{1\}$ and zero at $1$.

The [paired FFT runs](../data/prime-square-control.csv) use $\tau=0.05$ at six square orders and six nearby prime orders. At $q=151321=389^2$, the third marker was about $-0.00113$ and the last marker was $0.65044$. The last iterate had norm $18.28$, with $99.4\%$ of its squared norm on $A\setminus\{0\}$. At the nearby prime order $151337$, the last iterate had norm $2.31$. These are numerical observations with the measured residual included in the CSV. The square-order theta values above follow from the exact certificate.

## A sector estimate that fails even at prime order

A sufficient condition for bounding $\|v^*\|_2$ at fixed $\tau$ would be a gap from $1$ for the compression of $K$ to the large coordinates of $u^*=\Phi(v^*)$. In fact, put $I=\{k:u^*_k>L/\sqrt n\}$. Then $|I|\le 2\sqrt W n/L$, and $\|(u^*)_{I^c}\|_2^2\le2L\sqrt W$. If $\|K_{I,I}\|\le\delta<1$, then $v^*=Ku^*$ and $\|u^*-|v^*|\|_2\le 2\sqrt W$ imply

$$ (1-\delta)\|(u^*)_I\|_2\le 2\sqrt W+\|(u^*)_{I^c}\|_2. $$

The proposed estimate with a gap for **all** sets of size at most $\epsilon n$, for any fixed $0<\epsilon<1$, fails through primes, even for Rayleigh quotients of even nonnegative vectors. To see this, fix $L$ and choose arbitrarily large primes $p$ congruent to $1$ modulo $8\prod_{j=1}^L(4^j-1)$. Infinitely many exist by Dirichlet's theorem. Quadratic reciprocity gives $s(4^j)=s(4^{-j})=1$ for $1\le j\le L$. The order $m$ of $4$ tends to infinity with $p$, since every bounded order requires $p$ to divide one of finitely many fixed integers.

For $k\in\widehat Q$, let $z_k=k(4)$ and put

$$h_k=\frac{1}{L+1}\big|1+z_k+\cdots+z_k^L\big|^2.$$

For $m>2L$, this Fejér kernel has average $1$ and normalized squared $\ell_2$ norm $\sum_{j=-L}^L(1-|j|/(L+1))^2\ge (L+1)/2$. Its inverse Fourier support is on $4^j$, $|j|\le L$, so $Kh=h-\mathbf1$. Take $I=\{k:|\arg(z_k)|\le\pi\epsilon/2\}$. The values $z_k$ range uniformly over the $m$-th roots of unity, so for sufficiently large $m$ the arc has $|I|\le\epsilon n$. The geometric-sum formula bounds $h_k$ off that arc by $1/[(L+1)\sin^2(\pi\epsilon/4)]$. Consequently $f=\mathbf1_I h$ has $\|f-h\|_2/\|h\|_2\to0$ as $L\to\infty$, choosing the prime sufficiently large for each $L$. Since $\|K\|\le1$ and the Rayleigh quotient of $h$ is $1-n/\|h\|_2^2\to1$, the Rayleigh quotient of the even nonnegative $f$ also tends to $1$. Changing the sign mask to $-s$ gives the same obstruction for the absolute operator norm.

The Fejér kernel itself is a feasible nonnegative spectrum on the plus support with average $1$ and unbounded normalized $\ell_2$ norm. Bounding the smoothing norm through positivity, average mass and Fourier support alone would therefore lose information used by the fixed-point equation. The compression criterion for its particular set $I$, or an estimate tailored to the relation $u_i^{*2}-v_i^{*2}=4w_i$, remains open.
