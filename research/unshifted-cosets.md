# Marked response on the annihilator

Let $B\le Q$ have order $b$, let $A=B^\perp$ have size $m=n/b$, and write $S=A\setminus\{0\}$. The eigenvalues of the compression $K_{AA}$ are $\alpha_C=F(C)/b$ for $C\in Q/B$, where $F(C)=\sum_{a\in C}\chi(1-a)$. Define the smallest sign deficit

$$k=b-\max_{C\in Q/B}|F(C)|.$$

We first work at the zero reference and hold the marked entry of the diagonal at zero. For the background considered below, the marked entry is also held at zero.

## An exact formula

For $-1<d<1$ let $h(d)=X(dP_A)_{00}$, where $P_A$ projects onto $A$ in the frequency basis and $X$ is the [extended inverse](response-locality.md). Then

$$h(d)=\frac1m\sum_{C\in Q/B}\frac{\alpha_C}{1-d\alpha_C},\qquad
R(dP_S)_{00}=\frac{h(d)}{1+dh(d)}.$$

In fact $X(D)=K+KDX(D)$ by $K^2=P$. Compress the equation for $X(dP_A)e_0$ to $A$. In the positional eigenbasis of $K_{AA}$, the inverse Fourier image of an eigenvector is a normalized constant on its positional coset. Its squared inner product with $e_0$ is $b/n=1/m$. The second formula uses the rank-one inverse update for the removal of $de_0e_0^{\mathsf T}$ and the identity $R(D)_{00}=X(D)_{00}$ at $D_0=0$. Monotonicity bounds the entry for every strict real diagonal supported in $S$ between the two limits of this formula as $d\to\pm1$. Constant diagonals approach both bounds.

## The asymptotic scale of the sign deficit

Suppose $b\sim\sqrt q$. The [exact second moment](subgroup-modes.md#which-scalar-blocks-can-approach-norm-one) gives $\sum_{C\in Q/B}\alpha_C^2\le(q-2b)/b^2=1+o(1)$, while $\sum_C\alpha_C=-1/b$. There is at most one $C$ with $|\alpha_C|>3/4$ for all sufficiently large orders. To evaluate $h$ at the endpoints, use

$$\frac{\alpha_C}{1-d\alpha_C}=\alpha_C+\frac{d\alpha_C^2}{1-d\alpha_C}.$$

The trace contributes $-1/n$ and the sum of the terms with $|\alpha_C|\le3/4$ is $O(1/m)$ uniformly in $d$. When $k>0$, the remaining term has absolute value at most $b/(mk)$ at both endpoints. Thus $k\to\infty$ implies vanishing marked response, uniformly over strict diagonals on $S$.

Conversely, along any subsequence with $k$ a fixed positive integer, the unique near-unit eigenvalue has the form $\sigma(1-k/b)$. At $d=\sigma$, $h(d)\to 2\sigma/k$ since $b/m\to2$. At the other endpoint $h(d)\to0$. Consequently

$$\sup_{\operatorname{supp}D\subseteq S,\ \|D\|<1}|R(D)_{00}|\ \longrightarrow\ \frac{2}{k+2}.$$

The same limit holds for the absolute response at $d=\sigma(1-o(1/b))$. If $k=0$ on a subsequence, $h(d)$ diverges at the aligned endpoint and the supremum tends to $1$, consistent with the same formula. This proves that $k\to\infty$ is equivalent to the vanishing response supremum for the prescribed support at zero background.

At prime order with $b\sim\sqrt p$, [Hanson–Petridis](subgroup-modes.md#which-scalar-blocks-can-approach-norm-one) gives $k\ge2$, or $k\ge3$ when the minimizing coset is $B$. These yield upper limits $1/2$ and $2/5$, respectively. A bounded deficit can occur only on a self-inverse positional coset, because any other near-unit eigenvalue occurs twice. If it occurs on $B$, its sign must be positive and $b$ even. If it occurs on the nonidentity self-inverse coset, $4$ cannot divide $b$. These are the [second-moment and squaring constraints](subgroup-modes.md#which-scalar-blocks-can-approach-norm-one). Also $k=O(1)$ forces $b\le\sqrt p+O(1)$ by $(b-k)^2\le p-2b$. If one separately assumes $b=\sqrt p+O(1)$, divisibility gives $p=b^2+jb+1$ with $j$ a bounded integer. There are only $O(\sqrt X)$ such candidates up to $X$ for a fixed bound on $|b-\sqrt p|$.

Inversion pairs sharpen these bounds in two cases. When $b$ is even, a nonidentity self-inverse coset contains neither $1$ nor $-1$ because both are in $B$. Its minority sign count is therefore even, so $k\ge4$ and its response has upper limit $1/3$. In the positive identity case with $p\equiv1\pmod8$, the possible singleton $-1$ has $s(-1)=\chi(2)=1$. Every negative sign occurs in an inversion pair, giving $k\ge5$ and upper limit $2/7$.

At $q=r^2$, the $B=\mathbb F_r^\times$ case has $k=1$ and limiting response $2/3$. The comparison concerns the same prescribed support and both endpoint bounds.

## Clipped fixed-depth backgrounds

The sufficient condition $k\to\infty$ also works when the reference diagonal $D_b$ is a clipped fixed-depth Picard diagonal with a fixed clipping bound $\rho<1$ and with $D_b$ zeroed on $A$. The conclusion is $R(D)_{00}=o(1)$ for all strict $D$ agreeing with $D_b$ outside $S$. This statement uses the [fixed-expression closure rules](iteration-parity.md) for that reference.

Write $X=X(D_b)$, $R=R(D_b)$ and $\ell=D_b X e_0$. For either $\sigma=\pm1$, the [quadratic form comparison](coset-response.md#a-clipped-arithmetic-reference) applies on $A$, since $D_b$ vanishes there. The shift estimate first gives a quadratic inverse bound on $S$ with column $P_SXe_0$. It is bounded above by the corresponding quadratic inverse bound on $A$ with column $c=P_AXe_0$: the variational characterization of a positive definite inverse quadratic form allows all test vectors on $A$ in place of just those on $S$. Thus the change is bounded by a constant depending on $\rho$ times

$$\sum_C\frac{|\langle f_C,Xe_0\rangle|^2}{1-\sigma\alpha_C},$$

where the unit eigenvectors $f_C$ of the compression to $A$ have inverse Fourier images $\mathbf1_C/\sqrt b$. The terms with $1-\sigma\alpha_C\ge1/4$ contribute $o(1)$ by the [delocalization of the reference column](response-locality.md#a-uniformly-bounded-background).

For the one possible remaining term, use $Xe_0=Ke_0+K\ell$ and $\ell|_A=0$. The term from $Ke_0$ is bounded by $b/(mk)$. For the other term, split $\mathcal F^{-1}\ell$ into its coefficient at $1$ and the rest. The inverse Fourier image of $(K-\sigma I)f_C$ is $(s-\sigma)\mathbf1_C/\sqrt b$. Its squared norm is at most $2(1-\sigma\alpha_C)$ and its squared coefficient at $1$ is at most $1/b$. The contribution of the coefficient at $1$, after division by $1-\sigma\alpha_C$, is at most $\|\ell\|_2^2/k=O_\rho(1/k)$. The remaining contribution is $o(1)$. Indeed, the same fixed-depth approximation of $\ell$ by bounded even expressions as in the [translated-coset argument](coset-response.md#a-clipped-arithmetic-reference) gives $\|\mathbf1_{C\setminus\{1\}}\mathcal F^{-1}\ell\|_2=o(1)$ uniformly over $|C|=b=O(\sqrt q)$. The reference marked entry is itself $o(1)$. These bounds prove the assertion.

This transfer requires the prescribed reference outside $S$. The stationary spectrum has additional restrictions recorded in [the translation notes](translation.md#mass-and-energy-outside-a-coset).

### Adding a small number of frequencies

The conclusion persists for arbitrary changes on $(A\setminus\{0\})\cup E$ when $E$ is disjoint from $A$ and $|E|=o(k)$. For a clipped reference, zero the reference also on $E$. The proof enlarges the comparison set to $T=A\cup E$. By the entrywise Jacobi bound, $\|K_{AE}\|^2\le q|A||E|/n^2=O(|E|/b)=o(k/b)$ and $\|K_{EE}\|=O(|E|/b)=o(1)$. Since $I-\sigma K_{AA}\succeq(k/b)I$ for each $\sigma$, Cauchy–Schwarz on the off-diagonal form gives

$$I-\sigma K_{TT}\succeq \tfrac12(I-\sigma K_{AA})\oplus \tfrac12 I_E$$

for all sufficiently large sizes. For example, bound twice the off-diagonal form by $4\|K_{AE}\|^2\|x\|^2+\|y\|^2/4$. The inverse comparison then separates the bound on $A$, already controlled above, from $O(\|P_E X e_0\|^2)=o(1)$. The delocalization and positional estimates for the clipped reference allow zeroing on $T$, since $|T|=O(\sqrt q)$.

## Replay

For $d=1-1/q$, the formula above uses only the integer coset sums $F(C)$. In cyclic positional order these are `sign.reshape(b, n // b).sum(axis=0)`. The following marked entries were evaluated by rational summation and independently checked using the [compression solve](../response_shift.py). All absolute differences were below $2\cdot10^{-12}$, including both signs of $d$ and three extra small fields.

| Field order $q$ | $b$ | $m$ | $k$ | Marked entry on $S$ |
|---:|---:|---:|---:|---:|
| $97^2$ | 96 | 49 | 1 | 0.655147170 |
| 9601 | 96 | 50 | 73 | 0.009723443 |
| $193^2$ | 192 | 97 | 1 | 0.660893482 |
| 37633 | 192 | 98 | 145 | 0.005316374 |
| $389^2$ | 388 | 195 | 1 | 0.663806396 |
| 153649 | 388 | 198 | 326 | 0.002402062 |

The [translated and unshifted comparisons](../data/response-cosets.csv) use the same orders. The [bounded-defect proof](coset-defects.md) establishes $k\to\infty$ for every prime sequence satisfying $b\ge\sqrt p-O(1)$ and records a scan over 7,472 prime–subgroup pairs. The response conclusions above therefore apply when $b\sim\sqrt p$ in this range.
