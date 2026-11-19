# Exact additive propagation at rational-power widths

[The prime source calculation](astra-source-16.md) uses additive translations of a multiplicative Fourier lift of the actual quadratic optimizer. Exact propagation also holds at the endpoint comparison width $r=c/\sqrt p$ for rational $c>0$, although the coefficient field can then intersect the $p$th cyclotomic field. The same argument works for every rational-power width with denominator prime to $p$.

## The orbit of a single additive root

Let $p\equiv1\pmod4$, $n=(p-1)/2$, $Q=\mathbb F_p^{\times2}$, and $K=\mathbb Q(\zeta_p)$. For a positive integer $k$ with $p\nmid k$, set

$$F=\mathbb Q(\zeta_{\operatorname{lcm}(k,n)}),\qquad L=F(\rho),\qquad \rho=p^{1/k}>0.$$

The fields $F$ and $K$ are linearly disjoint by coprimality of their conductors. The prime $p$ is unramified in $F$, so $X^k-p$ is Eisenstein at any prime over $p$ and irreducible over $F$. Its splitting field over $F$ is $L$, and $L/\mathbb Q$ is Galois. The automorphism $\tau$ of $L/F$ given by $\rho\mapsto\zeta_k\rho$ generates the cyclic group. Complex conjugation fixes $\rho$ and takes $\tau$ to $\tau^{-1}$ by conjugation. The commutator subgroup of $\operatorname{Gal}(L/\mathbb Q)$ therefore contains $\tau^2$.

The intersection $E=K\cap L$ is abelian over $\mathbb Q$. Thus $EF\subseteq L^{\langle\tau^2\rangle}$ and $[EF:F]\le2$. Since $E\subset K$, disjointness gives $[E:\mathbb Q]=[EF:F]\le2$. In particular $\operatorname{Gal}(K/E)$ contains all elements indexed by the squares. Each such element extends to $KL$ while fixing $L$.

Take any $t\in\mathbb F_p^\times$. The $n$ elements $(\zeta_p^{t u})_{u\in Q}$ are linearly independent over $L$. Indeed a relation with coefficients in $L$ can be conjugated by every square to give the matrix $(\zeta_p^{t uv})_{v,u\in Q}$. Inverting the column labels makes it a convolution matrix on $Q$. Its eigenvalues are

$$\sum_{u\in Q}\eta(u)\zeta_p^{tu},\qquad \eta\in\widehat Q,$$

up to inversion of the character. They are nonzero since $\eta(u)\in F$ and the only degree-at-most-$p-1$ relation over $F$ is a multiple of $\Phi_p$. The polynomial for each displayed sum has zero constant term and nonzero coefficients on its support. The matrix is therefore invertible. This proof uses the quadratic-residue orbit even when $E$ is nontrivial.

## Application to actual sources

For $r\in(0,1]$ of the form $u p^{-a/k}$ with $u\in\mathbb Q_{>0}$ and $a\in\mathbb Z$, fix the exact anchored quadratic minimizer $b$ and its positive support $S$. Its restriction satisfies

$$b_S=\frac{Q_\sigma(r)_{SS}^{-1}e_0}{(Q_\sigma(r)_{SS}^{-1})_{00}},\qquad b_{S^c}=0.$$

The matrix and the inverse lie in $L$. Multiplicative Fourier transformation stays in $L$ before any scalar normalization. Hence every nonzero cut or restricted source whose frequency coordinates are in $L$ up to a common nonzero scalar has an additive lift, supported on $Q$, with nonzero Fourier coefficient at every $t\ne0$. Its centered additive translates span the entire complex mean-zero space. The statement applies to the high-level cut of the actual optimum and the signed source from the compressed normal equations. The same reasoning applies at $r=0$ to anchored endpoint LP vertices using $F=\mathbb Q(\zeta_n)$, since their coordinates come from linear active constraints over that field.

At the width $r=c/\sqrt p$, write $k=2$. This avoids requiring disjointness of $\mathbb Q(\sqrt p)$ and $\mathbb Q(\zeta_p)$ for that comparison. The proof gives exact nonvanishing only. In particular it supplies no lower bound at the scale of the positive-width signed source error.

The orbit matrices also have full modular rank for $(p,\ell)=(13,157),(17,137),(29,349),(41,821)$ after replacing $\zeta_p$ with a primitive $p$th root modulo $\ell$. Gaussian elimination gives ranks $6,8,14,20$ respectively.
