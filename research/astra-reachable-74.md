# Counting-norm widths for the realized Paley Picard orbit

Let $p=2n+1\equiv1\pmod4$ be prime, $a=2031/128$, and $D_r=\{|t-a|<r\}$. All unnormalized norms below use counting measure. The first exact Picard remainder on $D_{1/4}$ requires and admits order $\log n$ common linear dimensions for bounded counting-$L^2$ error. The lower bound allows an arbitrary prime-dependent subspace. For each of the first four realized returns, the full nonlinear remainder about the seed has a trace-polynomial approximation of counting error $O(n^{-1/2})$ on the same disk. These are finite-depth theorems. The disk meets the established stationary rectangle because its real interval contains $(1040021,1040023)/65536$. [Established physical overlap](astra-legendre-63.md)

Write $K=K^*=K^{\mathsf T}$, $K^2=I-J$, $K1=0$, $S=2\sqrt nKe_0=sX$, $s=2\sqrt{p/n}$, with $X$ the real normalized Jacobi row and $\|X\|_\infty\le1$. Here $J=11^{\mathsf T}/n$. Use $F_t(x)=\sqrt{4t+x^2}$ and replace $t$ by $n$ at coordinate zero in the vector map $\Phi_t$. Our exact orbit is $V_0=S, V_{j+1}=K\Phi_t(V_j)$. Put $R_1=V_1-S$. Its exact formula is
\[
 R_1=KF_t(S)+d(t)Ke_0,\qquad
 d(t)=F_n(S_0)-2\sqrt n-F_t(S_0).
\]
The coefficient $d$ is bounded uniformly on $D_{1/2}$. All roots agree with the positive ones on the real interval. [Physical recursion and exact marked correction](marked-domain-53.md)

## A sharp growth obstruction on the physical first step

Suppose $U_p\subset\mathbb C^n$ has dimension $d$ and
\[
 \sup_{D_{1/4}}\operatorname{dist}_2(R_1(t),U_p)\le\epsilon .
\]
Then for some absolute $C>1$, all sufficiently large primes, and $d+2\le\log n$,
\[
                 \epsilon\ \ge\ \sqrt n\,C^{-(d+3)}.                 \tag{1}
\]
In particular a bounded error requires $d=\Omega(\log n)$. Conversely $O(\log n)$ explicit common Jacobi modes suffice even for $o(1)$ error. This dimension threshold concerns uniform approximation on the disk. A row at a single floor spans one line.

To prove (1), use $K^2=I-J$. The rows $F_t(S)$ have distance at most $\epsilon$ from
\[
 W=K U_p+\mathrm{span}\{1,(I-J)e_0\}.
\]
This step retains the true mark, and costs at most two dimensions. Let $m=d+2$, $r=1/8$, $w_i=\sqrt{4a+S_i^2}$, and $u_i=4r/(4a+S_i^2)$. The coefficients of $F_{a+rz}(S)$ as a power series in $z$ are
\[
             A_j(i)=w_i\tbinom{1/2}{j}u_i^j.
\]
Cauchy's formula on the unit circle after orthogonal projection gives $\|(I-P_W)A_j\|_2\le\epsilon$. There is a complex unit vector $b\in\mathbb C^{m+1}$ with $P_W\sum_{j=0}^m b_j A_j=0$, so $\|\sum b_jA_j\|_2\le\sqrt{m+1}\epsilon$.

The empirical law of $X$ on intervals differs from the cosine of a uniform angle by $O(p^{-1/4})$, uniformly in the interval. For example symmetrize the empirical angles $\pm\arccos X$. The $k$-th Fourier moment is $\mathbb E_n T_k(X)=O(k/\sqrt p)$. Erdős–Turán at cutoff $\lfloor p^{1/4}\rfloor$ gives the claim, including the exceptional lifts. Equivalently use Xi's interval discrepancy for the good Jacobi arguments and add their two omitted full lifts. [Finite Jacobi moment estimate](astra-charged-68.md) · [Xi, Equidistributions of Jacobi sums](https://arxiv.org/abs/1809.04286)

Choose a fixed nondegenerate closed interval $I$ strictly inside the image of $1/4<X<3/4$ under $X\mapsto4r/(4a+8X^2)$. As $s^2\to8$, the $u_i$ occupy every subinterval $I'\subset I$ with empirical mass $\ge c|I'|-O(p^{-1/4})$. This follows by pulling back along the positive $X$ branch, where the derivative is bounded and separated from zero. Set $P(x)=\sum_{j=0}^m b_j\binom{1/2}{j}x^j$. Some monomial coefficient has modulus $\ge4^{-m}/\sqrt{m+1}$, using the binomial coefficient recurrence. For every polynomial of degree $m$, each monomial coefficient is bounded by $C_I^{m+1}\|P\|_{L^\infty(I)}$. Indeed the Chebyshev coefficients after affinely mapping $I$ to $[-1,1]$ are bounded by twice that norm. The three-term recurrence bounds the monomial coefficient sum of each affine Chebyshev polynomial exponentially. Thus $\sup_I|P|\ge C_1^{-(m+1)}$. Markov's polynomial derivative bound gives a one-sided interval $I'\subset I$ of length $c_I/(m+1)^2$ on which $|P|\ge\sup_I|P|/2$. For complex coefficients apply the real inequality to the real part after rotation at a maximum. Since $m\le\log n$, this interval carries $\gg(m+1)^{-2}$ empirical mass. As $w_i\ge\sqrt{4a}$, the counting norm of $w_iP(u_i)$ is at least $\sqrt n\,C_2^{-(m+1)}$, absorbing polynomial factors. This proves (1).

For the converse, truncate the binomial series of $F_t(S)$ through $S^{2L}$ on $D_{1/4}$. Here $s^2/(4|t|)<1/6$ eventually. Apply $K$ and include $Ke_0$ with its exact coefficient. The counting error is $O(\sqrt n\,6^{-L})$ because $K$ is contractive. The span is independent of $t$, with generators $KT_{2h}(X)$, $1\le h\le L$, and $Ke_0$. In particular counting accuracy is possible with much less than the ambient dimension.

## The entire next nonlinear feedback at all translated columns

For the actual incoming row $R_1(t)$ form the actual Taylor remainder
\[
 B(t)=\Phi_t(S+R_1)-\Phi_t(S)-\Phi_t'(S)R_1.
\]
Products and differentiation here are coordinatewise. Define the normalized generators
\[
 X,\qquad G_h= KT_{2h}(X)/(2h+1/100),\quad h\ge1
\]
of formal degrees $1,2h$, respectively. For all sufficiently large $p$, every generator has negative-field representation mass at most one. For $X$ this is the normalized Jacobi field. For $G_h$, the even Chebyshev mode has geometric output mass at most $2h$. The bad cyclic coordinate costs at most $2\sqrt p/n<1/100$ in total extra Jacobi mass. The same correction bound is uniform in $h$. In particular all these physical rows have sup norm at most one. On applying $K$ to an even-length monomial of length $k>0$ in the normalized generators, the output sup norm is at most $k+1/100$ by the mixed rank bound and the same marked exception. This argument uses absolute sums over the component representations and the exact Jacobi correcting column. [Mixed rank bound](astra-warm-51.md) · [Uniform bad-character correction](marked-domain-53.md)

Use $\rho=101/100$ and the sum of absolute monomial coefficients charged by $\rho^{\mathrm{degree}}$. Keep the marked correction $d(t)Ke_0=d(t)sX/(2\sqrt n)$ in $R_1$. On $D_{1/2}$ we have eventually $s<2.83, s\rho<2.86, 4|t|>61.2, 2\sqrt{|t|}<8.1$, and $v=(s\rho)^2/(4|t|)<0.134$. Expand $X^{2j}$ into Chebyshev modes. Their nonnegative coefficients are the probabilities of the absolute displacement of a $2j$-step symmetric sign walk. Its expected absolute displacement is at most $j$ by pairing steps and using the triangle inequality. The zero mode is killed by $K$. Thus the weighted price of $R_1$ is at most
\[
 8.1(1.01)\sum_{j\ge1}j|\tbinom{1/2}{j}|v^j+O(n^{-1/2})
 =8.1(1.01)\frac{v}{2\sqrt{1-v}}+O(n^{-1/2})<0.60.
\]
In particular $V_1=S+R_1$ has weighted price less than $3.46$. The series for $F_t(S+R_1)$, $F_t(S)$ and $F_t'(S)R_1$ all converge in this weighted norm with a uniform constant on the larger disk. This follows from the binomial series and $3.46^2<61.2$. Their signed difference gives $B$ before replacing its marked site. Add the exact marked difference as a single scalar multiple of $e_0$. This scalar is bounded on $D_{1/2}$, since the constant $2\sqrt n$ cancels from the marked remainder and the input is bounded. The $n$-floor derivative here is $S_0/F_n(S_0)$.

Truncate the resulting signed expansion to total degree $D$, keeping $e_0$. Its error in sup norm is $O(\rho^{-D})$ and in counting norm is $O(\sqrt n\,\rho^{-D})$. Taking $D=\lceil\log n/\log\rho\rceil$ gives $O(n^{-1/2})$. The complete $t$-independent dictionary consists of the actual monomials up to degree $D$ and $e_0$. There is at most one generator of each positive degree, hence its size is at most $1+\sum_{d\le D}\mathsf p(d)=\exp(O(\sqrt D))=n^{o(1)}$, where $\mathsf p$ counts integer partitions. For example the partition generating function at $e^{-1/\sqrt D}$ gives this inequality by its logarithmic expansion. Every monomial is an explicit product of normalized seed and transported Jacobi modes, counted here as one row regardless of its decomposition into irreducibles. For every coordinate $i$, the error against the translated column $Ke_i$ is at most the counting error since $\|Ke_i\|_2\le1$. This includes the marked output and every bulk output simultaneously. It also applies to the full activation difference $\Phi_t(S+R_1)-\Phi_t(S)$, with the corresponding exact marked correction.

One may package the dictionary into $O(\log n)$ explicitly specified signed mixtures on $D_{1/4}$. The truncated vector on $D_{1/2}$ has norm $O(\sqrt n)$ uniformly. Use its Taylor coefficients about $a$ up to order $\lceil 3\log n/\log(3/2)\rceil$ as the new common rows. Cauchy on radius $3/8$ gives an additional counting error $O(\sqrt n(2/3)^{\lceil3\log n/\log(3/2)\rceil})$. Each coefficient is a specified linear combination of the trace monomials and $e_0$. This compression bounds the number of mixture rows. Their underlying dictionary and evaluation costs are larger.

The same expansion gives a coordinate cap through three actual updates. Let $b_j$ be an upper bound for the weighted representation price of $V_j-S$. Each transported even word of length $k$ can be entered as a new generator with its previous total degree, divided by $k+1/100$. This normalized field has representation mass at most one by the same rank and exceptional-column bound. Repeated appearances of that field count as individual factors at the next vertex. Keep a separate generator $X$ for the new exact mark correction. Take $z=2.86$, $H=61.2$ and $g(x)=x/\sqrt{1-x}$. We proved $b_1=0.60$ is admissible. At subsequent fixed steps an admissible bound is
\[
 b_{j+1}=0.60+8.1(1.005)\left[g((z+b_j)^2/H)-g(z^2/H)\right],\qquad z+b_j<\sqrt H .
\]
Indeed in the binomial expansion split off the pure seed contribution $KF_t(S)$ before charging powers. Its earlier price is strictly below $0.60$ with a fixed margin for the $O(n^{-1/2})$ actual marked correction whenever $V_{j,0}$ is bounded. In power $2l$ the mixed products containing at least one $R_j=V_j-S$ cost at most $(2l+1/100)((z+b_j)^{2l}-z^{2l})$. All their coefficients are bounded in modulus individually before summation. Replacing the true seed price by $z$ increases this positive difference. Summing with $2l+1/100\le 2l(1.005)$ gives the displayed recurrence. Since
\[
 g(2.86^2/H)>0.1435,\quad
 g(3.46^2/H)<0.2182,\quad g(4.07^2/H)<0.317,\quad g(4.88^2/H)<0.5
\]
by squaring positive rationals, one can use $b_2=1.21$, $b_3=2.02$, $b_4=3.51$ successively. In particular $\|V_2\|_\infty<4.07$, $\|V_3\|_\infty<4.88$, and $\|V_4\|_\infty<6.37$ throughout $D_{1/2}$. Each of these finite iterates has $|\operatorname{arsinh}(V_{j,0}/(2\sqrt n))|=O(n^{-1/2})$.

There is a corresponding counting approximation to the full signed nonlinear remainder with $R_j$ in place of $R_1$ for $j=2,3,4$. At each of this fixed number of levels the number of generators of degree $d$ is $\exp(o(d))$. To see this inductively, words commute before transport, and there is at most one new transported generator per monomial, as well as the marked Jacobi correction. If the old numbers are $a_d=\exp(o(d))$ as upper bounds, the monomial generating product $\prod_{d\ge1}(1-u^d)^{-a_d}$ is finite for every real $0<u<1$. Its coefficients therefore grow subexponentially, as do their partial sums. All positive degrees stay positive and there is no degree-zero generator to transport since $K1=0$. Each $z+b_j$ above is below $\sqrt H$, so the full pretransport remainder converges in the weighted monomial norm and its separate $e_0$ correction stays bounded. The same total-degree truncation gives $O(n^{-1/2})$ counting error in a dictionary of $n^{o(1)}$ explicit finite-field rows. The Taylor grouping on the smaller disk again uses $O(\log n)$ common signed mixtures. For these later steps a generator may contain nested applications of $K$ to a product. The subexponential dictionary bound is at fixed depth.

## A finite horizon sufficient for stationary continuation

On $D_{1/4}$ put $\lambda=9/10$. On the coordinate disk $|x|\le5.1$, $5.1/\sqrt{4(a-1/4)-5.1^2}<\lambda$. The marked derivative is smaller for large $n$, and $\Phi_t$ uses its power-series branch throughout. The exact map followed by $K$ is thus $\lambda$-Lipschitz in counting norm on any coordinatewise segment inside this disk. Set
\[
            J=1+\left\lceil\frac{\log(1000\sqrt n)}{\log(10/9)}\right\rceil .
\]
If $\sup_{t\in D_{1/4}}\|V_j(t)\|_\infty\le5$ for $0\le j\le J$, then $\|V_1-V_0\|_2\le10\sqrt n$ and $\|V_J-V_{J-1}\|_2\le1/100$. The residual $\|K\Phi_t(V_J)-V_J\|_2\le\lambda/100$. The closed counting ball of radius $1/10$ about $V_J(t)$ lies inside the coordinate disk and maps into itself. Consequently the actual Picard iteration converges there, uniformly in $t$ at each $p$, and gives a holomorphic stationary row. The positive real stationary pair and analytic uniqueness on the overlap identify its physical branch. It would satisfy $|m_p(t)|\le3/\sqrt n$ there eventually by the marked inverse hyperbolic sine formula. More generally the same closing argument works at a single uniformly bounded holomorphic predictor with residual at most $1/100$ in counting norm and coordinate bound $5$, taking its real branch by positivity when the predictor is real. [Physical stationary identification](marked-domain-53.md)

All new estimates above are ordinary inequalities. There are no floating diagnostics or new interval computations. The first three updates satisfy the required coordinate cap $5$. The fourth has the separate bound $6.37$. Inequality (1) applies to a common linear approximation with fixed prime and varying floor. It permits floor-dependent coefficients and excludes bounded dimension, while $O(\log n)$ mixtures suffice for the stated shallow remainders. The common stationary continuation across $a$, its extension to the cold floor, and the ordinary all-prime theta problem remain open.

1. At each later actual iterate, estimate the full signed transported activation in the all-column sup norm. A uniform cap $5$ through the displayed logarithmic horizon closes the disk including the actual mark. Testing $V_4$ on this disk is the first missing case for that sequence of bounds.
2. Alternatively construct one real-on-real holomorphic approximate stationary row from the signed trace-polynomial mixtures. Prove a coordinate cap $5$ and counting residual at most $1/100$ on the disk, including the marked activation. This bypasses a uniform bound on every preceding iterate.
