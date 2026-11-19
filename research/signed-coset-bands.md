# Signed spectral gaps at the critical support size

Use the [stationary notation](stationary-tails.md). In particular $H=K-PDP$ on the mean-zero space, and $m_0=n/\sqrt q$ is the critical scale. The argument below treats the positive and negative eigenvalues of $H$ separately. The first two steps apply to any strict diagonal $D$, including the actual smoothing diagonal.

## Transfer from one sign of the diagonal

Let $P_\sigma=(P+\sigma K)/2$ be the orthogonal projector onto the $\sigma$ eigenspace $V_\sigma$ of $K$. Define

$$L_\sigma=P_\sigma(I-\sigma D)P_\sigma\big|_{V_\sigma}.$$

For $t\ge0$, the number of eigenvalues of $\sigma H$ in $(0,t]$ is at most the number of eigenvalues of $L_\sigma$ at most $t$, with multiplicities. In the decomposition $V_\sigma\oplus V_{-\sigma}$ the diagonal blocks of $\sigma H$ are $L_\sigma$ and $-L_{-\sigma}$. Both $L_\sigma$ and $L_{-\sigma}$ are positive definite since $\|D\|<1$. If the off-diagonal block is $T$, the positive inertia of $\sigma H-tI$ equals the positive inertia of

$$L_\sigma-tI+T(L_{-\sigma}+tI)^{-1}T^*.$$

At $t=0$ this is positive definite, so $\sigma H$ has exactly $\dim V_\sigma$ positive eigenvalues. The Schur correction is positive semidefinite for every $t\ge0$. The eigenvalue count follows by the min–max principle. For an individual eigenvalue $0<\lambda\le t$ of $\sigma H$ and corresponding eigenvector, its $V_\sigma$ component is nonzero. The same elimination shows that this component, normalized to a unit vector $y$, satisfies $\langle y,L_\sigma y\rangle\le t$.

Suppose $\sigma D_i\le\rho<1$ off a set $S$ and let $\beta=1-\rho$. Then

$$L_\sigma\succeq\beta(I_{V_\sigma}-P_\sigma P_S P_\sigma),\qquad
\lambda_{\min,+}(\sigma H)\ge\frac{\beta}{2}\left(1-\lambda_{\max}(\sigma K_{SS})\right).$$

Indeed the nonzero eigenvalues of $P_\sigma P_S P_\sigma$ coincide with those of $(P_\sigma)_{SS}=(I_S-J_{SS}+\sigma K_{SS})/2$. The argument also bounds the number of eigenvalues in $(0,t]$ by the number of eigenvalues of $\sigma K_{SS}$ at least $1-2t/\beta$, when $t<\beta$. This estimate allows $\sigma D_i$ to approach $-1$ at every frequency outside $S$. For a unit $y$ obtained from an individual eigenvector as above, $\|P_{S^c}y\|_2^2\le t/\beta$.

For an empty high set the direct bound is $L_\sigma\succeq\beta I_{V_\sigma}$.

## A union of frequency cosets

Let $G$ be a subgroup of the frequency group, let $B=G^\perp$ have size $b$, and let $U$ be the union of $r$ distinct cosets $a_j+G$. In the positional Fourier basis the compression to $U$ is a direct sum over $C\in Q/B$. The block on each $C$ has the orthonormal basis of the restrictions of the $r$ coset characters to $C$, normalized by $\sqrt b$. The block entries have the form

$$\frac1b\sum_{x\in C}s(x)\gamma(x),$$

where $\gamma$ is the quotient of two coset characters. The diagonal entries all equal $F(C)/b$, where $F(C)=\sum_{x\in C}s(x)$. Expand the indicator of $C$ as an average of the $|G|$ characters in $G$ with unit phase factors. The entrywise Jacobi bound $|Fs|\le\sqrt q$ then gives $|\sum_{x\in C}s(x)\gamma(x)|\le\sqrt q$ for every $\gamma$. A row-sum bound on the off-diagonal part yields

$$\lambda_{\max}(\sigma K_{UU})\le
\frac{(r-1)\sqrt q+\max_{C\in Q/B}\sigma F(C)}{b}.$$

In particular, at prime order, write $\Delta_p=\sqrt p-\max_{B'\le Q,\ C\in\mathbb F_p^\times/B'}|F(C)|$. The [arithmetic estimate](coset-defects.md#excluding-every-bounded-deficit) gives $\Delta_p\to\infty$. The block estimate now gives

$$\|K_{UU}\|\le\frac{|U|}{m_0}-\frac{\Delta_p}{b}.$$

With $r$ bounded and $|U|=m_0+o(\Delta_p)$, we have $b\asymp\sqrt p$, so $1-\|K_{UU}\|\gg_r \Delta_p/m_0$. The spectral gap persists after adding a disjoint set $E$ of $o(\Delta_p)$ frequencies. In fact $\|K_{UE}\|^2\le |U||E|/m_0^2=o(\Delta_p/m_0)$ and $\|K_{EE}\|=o(1)$. For either sign, bound twice the absolute off-diagonal form by $4\|K_{UE}\|^2\|x\|^2+\|y\|^2/4$ on vectors $(x,y)$ supported on $U\sqcup E$. This leaves a gap of order $\Delta_p/m_0$ on $U\cup E$ and on any of its subsets. Combining with the signed transfer excludes a band of width $O(p^{-1/2})$ on that sign whenever its high set is covered by this family and $1-\rho$ stays bounded below.

## Turning overlap into a coset cover at the required precision

Let $S$ have size $m=m_0+o(\Delta_p)$ and suppose $1-\|K_{SS}\|=o(\Delta_p/m_0)$. We prove that

$$E(S)\le(1/2+o(1))m^3,$$

where $E(S)=\sum_h |S\cap(S+h)|^2$. More generally, the same conclusion holds with $m\le m_0+o(\Delta_p)$, since $\|K_{SS}\|\le m/m_0$ forces $m\ge m_0-o(\Delta_p)$.

To see the precision of the rounding argument, take a real unit vector $x$ on $S$ maximizing the Rayleigh quotient of $\sigma K_{SS}$ for the optimizing sign $\sigma$. Let $\epsilon=1-\sigma\langle x,Kx\rangle$ and put $a=(|m-m_0|+1)/m_0+\epsilon$. Then

$$\|K_{SS}-\sigma xx^{\mathsf T}\|_{\rm F}
+\|(K-\sigma I)x\|_2
+\big\|\,|x|-m^{-1/2}\mathbf1_S\,\big\|_2=O(\sqrt a).$$

For the first term, expand the squared Frobenius norm and use $\|K_{SS}\|_{\rm F}\le m/m_0$. For the second, use $\|Kx\|\le1$. For the last, the entry bound gives $(\sum_i|x_i|)^2\ge m_0(1-\epsilon)$. Comparing $\sum_i|x_i|$ with $\sqrt m$ proves the claimed squared error $O(a)$.

Fix $c\in(1/2,1)$, let $T=S+h$, $I=S\cap T$, $r(h)=|I|/m$, and let $z$ be the translate of $x$ to $T$. The two rank-one compressions restricted to $I$ differ by $O(\sqrt a)$ in Frobenius norm. When $r(h)>c$, their vectors on $I$ have squared norms $r(h)+O(\sqrt a)$, so $|\langle x_I,z_I\rangle|=r(h)+O_c(\sqrt a)$. On $S\setminus T$, the contribution $K_{S\setminus T,I}z_I$ has norm at least $r(h)\sqrt{1-r(h)}-O_c(\sqrt a)$. The other contribution $K_{S\setminus T,T\setminus S}z_{T\setminus S}$ has norm at most $(1-r(h))\sqrt{1-r(h)}+O(\sqrt a)$ by the entrywise bound. Since $Kz-\sigma z=O_{\ell_2}(\sqrt a)$, this gives

$$1-r(h)=O_c(a)\qquad(r(h)>c).$$

The symmetric-difference triangle inequality now makes $G=\{h:r(h)>c\}$ an exact subgroup for all sufficiently large orders. Averaging $|S\triangle(S+h)|$ over $G$ and rounding the densities on the cosets changes $O_c(ma)=o(\Delta_p)$ entries. The energy estimate $E(S)/m^3\le c+(1-c)|G|/m$ follows by splitting $\sum_h r(h)^2$ over $G$ and its complement. If $E(S)\ge(1/2+\delta)m^3$ for a fixed $\delta>0$, choose $1/2<c<1/2+\delta$. It follows that $|G|\gg_\delta m$ and the rounded union uses boundedly many cosets. The union has size $m_0+o(\Delta_p)$ and the remaining extra frequencies number $o(\Delta_p)$. The arithmetic coset estimate contradicts $\epsilon=o(\Delta_p/m_0)$.

As a consequence, take a fixed $\rho<1$ and let $S_\sigma=\{i:\sigma D_i>\rho\}$ for the actual stationary diagonal. If $|S_\sigma|\le m_0+o(\Delta_p)$ and $\sigma H$ has a positive eigenvalue of size $O(p^{-1/2})$, the signed spectral bound forces $|S_\sigma|=m_0+o(\Delta_p)$ and $E(S_\sigma)\le(1/2+o(1))|S_\sigma|^3$. This rules out the highly overlapping configurations at the critical size, even with arbitrarily saturated coordinates of the opposite sign. The available lower energy bound from [Jacobi endpoint counts](critical-sets.md#repeated-differences-are-necessary) is of order $m^{5/2}$ at width $O(p^{-1/2})$ and $|S_\sigma|\le m_0+O(1)$. It leaves the intermediate-energy region open.

## A stationary mass test without an eigenvalue hypothesis

Write $A_\sigma=(u+\sigma v)/2$ for the positive stationary spectrum on the $\sigma$ support. Its exact equation is $(I-\sigma K)A_\sigma=\sqrt{W/n}\mathbf1$. For any frequency set $S$, let $z=P_{S^c}A_\sigma$. Expanding in the nonnegative quadratic form $I-\sigma K$ gives

$$\big(1-\lambda_{\max}(\sigma K_{SS})\big)\|P_S A_\sigma\|_2^2
\le W-2\sqrt{W/n}\sum_i z_i+\langle z,(I-\sigma K)z\rangle
\le W+2\|z\|_2^2.$$

For $S=S_\sigma=\{i:\sigma D_i>\rho\}$ and $0\le\rho<1$, the reciprocal product relation gives $A_{\sigma,i}^2\le w_i(1+\rho)/(1-\rho)$ off $S_\sigma$. Thus the right side stays bounded at fixed $\rho$ and $0<\tau\le1$. Moreover, writing $\mu_\sigma=A_\sigma/\sqrt{nW}$, the bound on the unmarked entries gives

$$\mu_\sigma(S_\sigma)\ge
1-\sqrt{\frac{\tau(1+\rho)}{W(1-\rho)}}-O_\rho(n^{-1/2}).$$

Consider a sequence where this lower bound is separated from zero, for instance $\tau\to0$ at fixed $\rho$. If $|S_\sigma|\le m_0+o(\Delta_p)$, the positive mass and Cauchy–Schwarz give $\|P_{S_\sigma}A_\sigma\|_2^2\gg m_0$. The first inequality therefore forces $1-\lambda_{\max}(\sigma K_{S_\sigma S_\sigma})=O_\rho(1/m_0)$, even without a hypothesis about $H$. The preceding coset exclusion and energy restriction now apply directly to the stationary high set. For a fixed $\rho$ at weights where either signed high set has positive mass, a bounded-coset cover of that sign at critical size is impossible through primes. At square orders the subfield support supplies a compatible gap of order $1/m_0$.

The same form identity tests any prescribed critical coset union $U$ without imposing a bound on $D$ outside $U$. If $\mu_\sigma(U)\ge\epsilon>0$, the gap of order $\Delta_p/m_0$ forces $\|P_{U^c}A_\sigma\|_2^2\gg_\epsilon\Delta_p$. At a fixed threshold $\rho<1$ the squared mass on the exterior indices with $\sigma D_i\le\rho$ is bounded. The entry bound $\|A_\sigma\|_\infty=O(1)$ for $\tau\le1$ then shows that at least order $\Delta_p$ further indices of the same high sign are needed outside $U$. This statement allows arbitrary opposite-sign activations throughout the exterior.

## Prime and square comparisons

The [replay](../coset_bands.py) computes the positional blocks for unions of one, two and three consecutive frequency cosets at $\tau=0.05$. It chooses their total size closest to $m_0$, with the subfield annihilator as the single-coset square control. It uses the observed one-sided maximum of $D_i$ outside each tested set for $\rho$. The [72 rows](../data/coset-bands.csv) report positive and negative compression endpoints, the arithmetic row bounds, and the stationary spectral gap lower bounds obtained from the actual compression values. Selected positive endpoints are

| Field order | Number of cosets | Size | Compression endpoint | Row bound | Spectral gap lower bound |
|---:|---:|---:|---:|---:|---:|
| $389^2$ | 1 | 195 | 0.997423 | 0.997423 | 0.000693 |
| 153649 | 1 | 194 | 0.126263 | 0.126263 | 0.000817 |
| $389^2$ | 3 | 195 | 0.355027 | 0.997423 | 0.000000249 |
| 153649 | 3 | 198 | 0.127648 | 0.719898 | 0.000816 |

The last column depends on the exterior activation as well as the compression. In the three-coset square row, the exterior still contains most of the activation on the subfield annihilator, so the compression by itself gives a poor estimate for that choice of support. The stationary residuals are below $10^{-9}$ in the recorded sweep. Five small fields also give 30 direct dense checks of the signed gap inequality. A separate dense check at eight small field orders compared the blocks with the original compressions to within $3\cdot10^{-15}$, and tested the signed eigenvalue counts in 100 cases with prescribed, nearly saturated opposite-sign exteriors. The mass identities were checked in 56 stationary truncations, with maximum discrepancy below $4.2\cdot10^{-10}$.
