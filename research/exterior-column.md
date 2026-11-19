# An exterior activation can focus the marked inverse on two frequencies

Write $P=I-J$, and let $K$ be the real even circulant Paley multiplier with $K^2=P$ and $|K_{ij}|\le\sqrt q/n$. Extend the inverse $X_B=(K-PBP)^{-1}$ from the mean-zero space by zero on constants, put $e=Pe_0$, and write $m_B=e^{\mathsf T}X_Be$. The label $B$ here is a diagonal and its marked entry is always zero. The exterior in this note is prescribed independently of the stationary equations.

For each sufficiently large prime or square order there is an even, mean-zero diagonal supported on the exterior of a bulk pair $S=\{h,-h\}$, with $\|B\|\le1/16$, such that adding $1/4$ on $S$ changes the marked inverse by a positive constant independent of the field order. With zero on the exterior the same addition changes it by $O(n^{-1})$. Thus small size, a compression gap and a small exterior mean cannot by themselves bound the interaction in the [stationary coupling test](coset-activation.md).

## The column test for gapped covers

Let $S$ exclude the mark and assume $B=0$ on $S$ and $\|B\|\le\rho<1$. When $\|K_{SS}\|\le1-\delta$, the [Loewner comparison on a bounded background](coset-response.md#a-clipped-arithmetic-reference) gives $\|(X_B)_{SS}\|\le1-c_\rho\delta$. For any $-1<d<1$, direct inversion after a constant change on $S$ gives

$$m_{B+d\mathbf1_S}-m_B=
d\,c^{\mathsf T}(I-d(X_B)_{SS})^{-1}c,\qquad c=(X_Be)_S.$$

This is the resolvent identity on the restriction to $S$. Monotonicity of $m_B$ in each diagonal coordinate follows by differentiating the inverse, with derivative $(X_B e)_i^2$. Thus arbitrary changes on $S$ have absolute marked effect at most $(c_\rho\delta)^{-1}\|c\|_2^2$. Conversely, with $d=1/4$ the form is at least $\frac{d}{1+d/(1-\rho)}\|c\|_2^2$, by the norm bound on the full reference inverse. Smallness of the restricted column is therefore both necessary and sufficient to make every such change negligible, at a fixed compression gap. In particular the criterion applies to all sets of size $o(n/\sqrt q)$, since the entry bound gives a compression norm $o(1)$.

## Constructing a bounded, centered exterior

Let $k=Ke$ and $\ell_h=K(e_h+e_{-h})/\sqrt2$. There is a displacement $h$ with $h\ne-h$ and

$$\sum_{i\notin\{0,h,-h\}} |k_i(\ell_h)_i|\ge\frac1{2\sqrt2}-o(1).$$

Indeed, for each coordinate $i$, circulant symmetry and $K^2=P$ give

$$\sum_h(\ell_h)_i^2=1-2/n+\mathbf1_{2i=0},\qquad |(\ell_h)_i|\le\frac{\sqrt2}{m_0},\quad m_0=n/\sqrt q.$$

The cross sum of the two shifted rows is $(K^2)_{i,-i}$. Consequently $\sum_h|(\ell_h)_i|\ge m_0(1-2/n)/\sqrt2$. Also $\|k\|_1\ge m_0\|k\|_2^2=m_0(1-1/n)$. Averaging the displayed overlaps over $h$ now gives the claim since $m_0^2/n\to1/2$. Removing the at most two self-inverse displacements costs $O(1/n)$ in the average, using Cauchy–Schwarz. Removing $i=0,\pm h$ costs $O(1/n)$ at each displacement by the entry bound.

Fix one such $h$, let $T$ be the complement of $\{0,h,-h\}$, and set $b_i=\operatorname{sgn}(k_i(\ell_h)_i)$ on $T$. With $\overline b_T$ the mean on $T$, define $B_i=\rho(b_i-\overline b_T)/2$ on $T$ and zero elsewhere, where $\rho=1/16$. Both $k$ and $\ell_h$ are even, so $B$ is even. Its sum is zero and $\|B\|\le\rho$.

Write $f_h=(e_h+e_{-h})/\sqrt2$. The first correction in the Neumann series for $f_h^{\mathsf T}X_Be$ is

$$\langle\ell_h,Bk\rangle\ge\frac{\rho}{4\sqrt2}-o(1).$$

Centering changes the correction by $O(1/n)$, since $\sum_i k_i(\ell_h)_i=\langle e,P f_h\rangle=-\sqrt2/n$ and removing three coordinates costs $O(1/n)$. The zero-background term $f_h^{\mathsf T}Ke$ tends to zero. The sum of all terms of degree at least two in $B$ has magnitude at most $\rho^2/(1-\rho)$ by the operator norm bound and $\|e\|\le1$. Thus for large orders

$$f_h^{\mathsf T}X_Be\ge \frac1{64\sqrt2}-\frac1{240}-o(1)>\frac1{200}.$$

The constant shift formula with $d=1/4$ now gives an increment at least $15/(76\cdot200^2)$. On the zero background the increment is $O(n^{-1})$ by the entry bound and the two-point compression gap. In the interaction identity of [the previous comparison](coset-activation.md#the-exact-interaction), this gives a positive lower limit for $m_{B+d\mathbf1_S}-m_B-m_{d\mathbf1_S}+m_0^{\mathrm{inv}}$, where $m_0^{\mathrm{inv}}=-1/n$ is the zero-diagonal inverse entry. One may also negate the designed exterior to align the first correction with the finite-order sign of $f_h^{\mathsf T}Ke$. The resulting estimate uses the absolute column value and the same remainder bound.

The mechanism is the correlation of the exterior diagonal with the product of two Jacobi fields. Any proof of the true stationary column estimate must use some constraint excluding this correlation and its higher Neumann terms. Evenness, a bounded reference diagonal, and small mean accommodate the example at both prime and square orders.

## Comparison with scaled stationary exteriors

The [replay](../exterior_focus.py) chooses the largest overlap among the first 64 non-self-inverse displacements and aligns the first correction with the zero-background column. It compares the constructed exterior with the true stationary diagonal at $\tau=0.05$, then masks, centers and scales the latter by the same factor $\rho/2$. Thus both exteriors are bounded by $\rho$ and centered. The comparison concerns damped and recentered diagonals. The undamped stationary column is a separate estimate.

| Order | Designed first Neumann term | Scaled stationary first term | Designed interaction | Scaled stationary interaction |
|---:|---:|---:|---:|---:|
| $9413$ | $-0.02307383$ | $0.00038418$ | $0.00025235$ | $-0.00000193$ |
| $37253$ | $-0.02292197$ | $0.00029154$ | $0.00029366$ | $-0.00000206$ |
| $153649$ | $-0.02287832$ | $-0.00001157$ | $0.00020873$ | $0.00000005$ |
| $389^2$ | $0.02285686$ | $-0.00006529$ | $0.00018609$ | $-0.00000016$ |

All [12 measured inverse residuals](../data/exterior-focus.csv) are at most $4\times10^{-12}$. Centering and a small norm allow measurable concentration even through the prime family. The selected stationary-derived references have much smaller Jacobi-product correlations at the same displacements.
