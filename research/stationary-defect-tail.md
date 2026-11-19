# Marked-source decay and the low dissipation modes

Let $K=K^{\mathsf T}$, $K^2=P=I-jj^{\mathsf T}$ and $j=\mathbf1/\sqrt n$. Write $e=Pe_0$ and let $F$ be a strict diagonal with $F_0=0$. Use $V=|F|^{1/2}$, $S=\operatorname{sgn}F$ with value $1$ at zeros, and

$$
C=SVKV,\qquad A=I-C,\qquad L=(A+A^{\mathsf T})/2,\qquad b=SVKe.
$$

The two blocks of $L$ on the signs of $F$ are $I-\sigma V_\sigma K_{\sigma,\sigma}V_\sigma$, $\sigma=\pm1$. In particular $L$ commutes with $S$. In the [signed time integral](parallel-sign-4.md#exact-tail-and-certificates-for-cancellation), put $h=A^{-1}b$ and $z(t)=e^{-tA}b$, so the signed tail after time $t$ is $J_t=\langle z(t),Sh\rangle$. Here $z(t)=y(2t)$ in that convention.

## The defect bounds the marked orbit

The missing marked coordinate supplies one full direction in the contraction defect:

$$
\begin{aligned}
I-CC^{\mathsf T}
 &=I-V^2+(SVj)(SVj)^{\mathsf T}
   + SVK(I-V^2)KVS\\
 &\succeq I-V^2+bb^{\mathsf T}. \tag{1}
\end{aligned}
$$

Indeed $I-V^2\succeq e_0e_0^{\mathsf T}$ and $Ke_0=Ke$. Multiply the bound $bb^{\mathsf T}\preceq I-CC^{\mathsf T}$ on both sides by successive powers of $C$ and $C^{\mathsf T}$ and telescope:

$$\sum_{k=0}^m (C^k b)(C^k b)^{\mathsf T}\preceq I-C^{m+1}(C^{\mathsf T})^{m+1}\preceq I.$$

Equivalently, $\|\sum_k a_k C^k b\|_2\le\|a\|_{\ell_2}$ for any square-summable coefficients. This is specific to the marked source and makes no assumption on a uniform gap of $C$.

Let $p_t(k)=e^{-t}t^k/k!$ for $k\ge0$ and $p_t(-1)=0$. Expand $z(t)=\sum_{k\ge0}p_t(k)C^k b$. The squared coefficient sum is bounded by $\max_k p_t(k)\ll (1+t)^{-1/2}$. For $Az(t)$ the coefficients are $p_t(k)-p_t(k-1)=(1-k/t)p_t(k)$. When $t\ge1$, their squared sum is at most $\max_k p_t(k)$ times the Poisson variance divided by $t^2$. Consequently

$$
\|z(t)\|_2\ll t^{-1/4},\qquad
\|Az(t)\|_2\ll t^{-3/4},\qquad
\|L^{1/2}z(t)\|_2\ll t^{-1/2}. \tag{2}
$$

The last bound uses $\langle z,Lz\rangle=\langle z,Az\rangle$. A mixed moment consequence is that the Hankel matrix with entries $b^{\mathsf T}SC^{j+k}b$ has operator norm at most one on $\ell_2$: it is the compression of $S$ by two copies of the contractive synthesis map $a\mapsto\sum_k a_k C^k b$.

For $T\ge1$ first take the uniform average on $[T,2T]$. Since $\int_0^\infty p_t(k)\,dt=1$ for every $k$, each averaged coefficient is at most $1/T$ and their sum is one. Thus $\|T^{-1}\int_T^{2T}z(t)\,dt\|\le T^{-1/2}$. Differentiation also gives

$$\int_T^{2T}\|L^{1/2}z(t)\|_2^2\,dt=\tfrac12(\|z(T)\|_2^2-\|z(2T)\|_2^2).$$

Removing the endpoint jumps of the averaging weight gives a stronger dissipation bound. Use the tent density $\omega_T(t)=4T^{-2}\min(t-T,2T-t)$ on $[T,2T]$, zero elsewhere. Write $\bar z_T=\int\omega_T(t)z(t)\,dt$ and $\bar J_T=\int\omega_T(t)J_t\,dt$ for this weighted average. Its Poisson coefficients still have sum one and maximum at most $2/T$. Also $A\bar z_T=\int\omega_T'(t) z(t)\,dt$ by integration by parts. The coefficients in the second integral have $\ell_1$ norm at most $\int|\omega_T'(t)|\,dt=4/T$ and maximum absolute value at most $4/T^2$. By the source bound and $\langle z,Lz\rangle=\langle z,Az\rangle$,

$$
\|\bar z_T\|_2\ll T^{-1/2},\qquad
\|A\bar z_T\|_2\ll T^{-3/2},\qquad
\|L^{1/2}\bar z_T\|_2\ll T^{-1}. \tag{2a}
$$

The averaged tail is still a criterion for the undamped limit. If the signed density $j_{\rm time}(t)=\|y_+(t)\|_2^2-\|y_-(t)\|_2^2$ tends uniformly to zero on compact time intervals, then for each fixed $T$ the difference $(m_F+1/n)-\bar J_T$ also tends to zero. It is the integral of $j_{\rm time}(s)$ against $\int_s^\infty\omega_T(t)\,dt$, a weight in $[0,1]$ supported on $s\le2T$.

## The half-angle solution has bounded dissipation energy

Take $F=B$ from the [half-angle column identity](stationary-secant.md#the-exact-inverse-column), with true stationary $v,u$, $a=u_0-2\sqrt{\tau/n}$ and $0<\tau\le1$. In this case $h=SVv/a$ is nonnegative coordinatewise. Its $L$-energy has a uniform estimate without an estimate on $\|v\|_2$:

$$
\|L^{1/2}h\|_2^2=h^{\mathsf T}Ah=h^{\mathsf T}b
=\frac{(Ke)^{\mathsf T}|B|v}{a}
=1+O(\sqrt\tau+n^{-1/2}). \tag{3}
$$

In fact $(Ke)^{\mathsf T}v=u_0-\bar u$ with $\bar u=2\sqrt{W/n}$. On the bulk

$$
(1-|B_i|)|v_i|
=2\sqrt{\tau/n}(1-e^{-|\gamma_i|})
\le2\sqrt{\tau/n}.
$$

The contribution from replacing $|B|$ by $1$ on the bulk is bounded by $2\sqrt{\tau/n}\|Ke\|_1\le2\sqrt\tau$. The error at the mark is $|v_0|/n$ since $K_{00}=-1/n$. Combine these with $a\gg1$ and the uniform bound on $u_0$.

There is also the smaller diagonal-defect energy $\|(I-V^2)^{1/2}h\|_2^2\ll\sqrt\tau$ from the same bulk calculation and $\|v\|_1\le2\sqrt{nW}$, since $h_0=0$.

## A small-rank reduction of the averaged tail

Let $\Pi_\eta=\mathbf1_{[0,\eta]}(L)$ with $0<\eta\le1/2$. Since $\Pi_\eta$ commutes with $S$, the two spectral parts of the pairing do not mix. Equations (2a) and (3) give

$$
\boxed{\quad
\left|\bar J_T-\langle\Pi_\eta\bar z_T,S\Pi_\eta h\rangle\right|
\ll\min\{\eta^{-1}T^{-1},\,\eta^{-1/2}T^{-1/2}\}.
\quad} \tag{4}
$$

To see this, in the high-mode term put $L^{1/2}$ on $h$ and $L^{-1/2}$ on $\bar z_T$. On that subspace $\|L^{-1/2}\bar z_T\|\le\min(\eta^{-1}\|L^{1/2}\bar z_T\|,\eta^{-1/2}\|\bar z_T\|)$. All constants are absolute. The low term continues to use the difference of the contributions of the two signs.

For the half-angle diagonal the number of low modes obeys the uniform bound

$$\operatorname{rank}\Pi_\eta\ll n\eta^2/\tau. \tag{5}$$

In fact $L\succeq I-V^2$, since $\sigma K\preceq I$ on both signed blocks. For $\eta$ smaller than a fixed absolute constant, let $U=\{i:1-|B_i|\le64\eta\}$. Every unit vector $y$ in $\operatorname{ran}\Pi_\eta$ has squared norm at most $1/64$ outside $U$. Moreover $\langle y,(I-L)y\rangle\ge1-\eta$, and restricting each copy of $y$ to $U$ changes this quadratic form by at most $2/8+1/64$, since $\|I-L\|\le1$. Thus the restriction to $U$ is injective on this subspace and the restricted image has Rayleigh quotient bounded below by an absolute positive constant for $(I-L)_{UU}$. It follows by the min-max principle that the dimension is bounded by a constant times $\|(I-L)_{UU}\|_{\mathrm F}^2$. The absolute Jacobi entry bound gives $\|(I-L)_{UU}\|_{\mathrm F}^2\le q|U|^2/n^2$. The [half-angle size bound](stationary-secant.md#uniform-transfer-along-the-hyperbolic-path) gives $|U|\ll n\eta/\sqrt\tau$, proving (5) for sufficiently small $\eta$. The trivial rank bound proves it for larger $\eta$ after increasing the constant.

In particular a window at a fixed multiple of $\sqrt{\tau/n}$ has bounded rank, even for varying $\tau$. For field-first limits at fixed $\tau$, taking $\eta=T^{-1+\epsilon}$ with any fixed $0<\epsilon<1$ in (4) leaves an $O(T^{-\epsilon})$ error and a rank fraction $O(\tau^{-1}T^{-2+2\epsilon})$. These are two different scales. The bound at the natural eigenvalue floor does not by itself justify sending the cutoff to that floor in the field-first order.

There is also a finite-rank statement at the natural relaxation time. If $P_\eta$ projects onto the right singular vectors of $A$ with singular values at most $\eta$, then the same proof as for (5) applies, since $\langle y,Ly\rangle\le\|Ay\|\|y\|$ on this subspace. Hence $\operatorname{rank}P_\eta\ll n\eta^2/\tau$. The projection of the test vector is not needed:

$$
\left|\bar J_T-\langle P_\eta\bar z_T,Sh\rangle\right|
\le\eta^{-1}\|A\bar z_T\|\,\|h\|\ll\eta^{-1}T^{-3/2}n^{1/4}.
$$

The last norm bound uses $\|v\|_\infty\ll1$ and $\|v\|_1\ll\sqrt n$. At $T=\sqrt{n/\tau}$ and $\eta=B_*\sqrt{\tau/n}$ for fixed $B_*>0$, the rank is $O(B_*^2)$ and the error is $O(B_*^{-1}\tau^{1/4})$. This concerns a growing-time tail; compact-time parity alone cannot control the response accumulated before that time.

A spatial alternative follows from the smaller diagonal-defect energy. For $U_\delta=\{i:1-|B_i|\le\delta\}$, the contribution from the other coordinates is bounded by

$$|\langle\mathbf1_{U_\delta^c}\bar z_T,Sh\rangle|\ll \tau^{1/4}\delta^{-1/2}T^{-1/2}.$$

This uses only the pointwise activation cutoff. It is weaker than spectral localization when the low modes occupy a small portion of the activity on $U_\delta$.

For a proof through primes it would suffice to control $\langle\Pi_\eta\bar z_T,S\Pi_\eta h\rangle$ in the iterated limit at fixed floors tending to zero, along with compact-time parity for the true half-angle diagonal. The rank estimate alone does not control the mark on those modes. The exact square tail shows that a nonvanishing signed contribution can survive in the reduced subspace.

The [hard-window and spatial bounds](parallel-half-modes-5.md) give complementary reductions using the symmetric half-angle inverse and the activation set directly. The [Krylov residual certificate](parallel-half-krylov-5.md) instead encloses a finite-order signed tail from a low-dimensional trial solve and a site-weighted residual.

## Numerical replay

The [probe](../stationary_defect_tail.py) computes the tent average with incomplete gamma coefficients, using $t p_t(k)=(k+1)p_t(k+1)$. It truncates at a degree where the Poisson tail of mean $2T$ is below $10^{-14}$. The [36 comparisons](../data/stationary-defect-tail.csv) use three pairs of Paley orders, two floors and three cutoffs. The stationary and half-angle source residuals are below $1.0\cdot10^{-10}$ and $4.9\cdot10^{-11}$, respectively. The largest checked dissipation Ritz residual is $7.3\cdot10^{-16}$. The eigenspace counts and tail values are floating-point diagnostics.

At $\tau=0.0005$, $T=32$ and $\eta=0.1/\sqrt T$, the largest pair gives

| Field order | Averaged signed tail | Positive low rank | Negative low rank | Signed low pairing | High pairing |
| ---: | ---: | ---: | ---: | ---: | ---: |
| $193^2$ | 0.31428382 | 1 | 0 | 0.31413243 | 0.00015139 |
| $37253$ | $8.47\cdot10^{-6}$ | 0 | 0 | 0 | $8.47\cdot10^{-6}$ |

The single observed positive low mode captures over $99.9\%$ of the square tail in this comparison. Tightening the threshold to $0.1/\sqrt{128}$ for the same square order puts the mode above the threshold. This illustrates that the high-mode term at a finite time can remain relevant when the threshold is too small.

An independent check on 48 dense prescribed diagonals across small prime and square orders verifies the matrix defect inequality. Across 96 averages at two cutoffs, direct matrix exponentials with quadrature agree with the streamed tent coefficient computation to within $3.7\cdot10^{-16}$ in Euclidean norm.
