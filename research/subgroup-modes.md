# Slow modes supported near frequency subgroup cosets

The Möbius incidence bound extends from flat indicator vectors to approximate null vectors of the [marked linearization](marked-response.md) that are concentrated on a fixed number of subgroup cosets. The coordinates within those cosets can have arbitrary amplitudes and phases. The argument uses the Fourier block structure of the compression to recover positional concentration before applying the [prime-field incidence estimate](mobius.md#a-power-saving-for-subgroup-indicator-overlaps-at-prime-order).

## Compression to frequency cosets

Use the unitary Fourier transform $\mathcal F=n^{-1/2}F$ from positions $Q$ to frequencies $\widehat Q$. Let $B\le Q$ have order $b$, let $A=B^\perp\le\widehat Q$, and let $S$ be a union of at most $r_0$ cosets of $A$. Here $r_0$ is fixed and $b$ is comparable to $\sqrt q$. Write $P_S$ for coordinate projection onto $S$ and $K_S=P_S K P_S$ as an operator on that subspace.

The space on $S$ and $K_S$ commute with frequency translations by $A$. On the positional side these translations are multiplication by characters from $A$, whose simultaneous eigenspaces are the coordinate spaces of the positional cosets $cB$. Thus $K_S$ splits into blocks, each of dimension at most $r_0$, and their inverse Fourier images are supported on the respective positional cosets.

The Jacobi entry bound $|K_{ij}|\le\sqrt q/n$ gives

$$\|K_S\|_{\mathrm F}^2\le\frac{q|S|^2}{n^2}\le\frac{q r_0^2}{b^2}.$$

It follows that the eigenvectors of $K_S$ with absolute eigenvalue at least $1/2$ have inverse Fourier support in a union of $O_{r_0}(1)$ positional cosets of $B$, with the size-range constant for $b$ held fixed. The statement uses the whole spectral subspace, so it allows multiplicities and linear combinations of the eigenvectors.

For a single frequency coset each block is scalar. Its eigenvalue is exactly $b^{-1}\sum_{a\in cB}s(a)$, because conjugating $P_S K P_S$ by $\mathcal F$ compresses positional multiplication by $s$ to the vectors of constant modulus and prescribed phase on each $cB$. At $q=r^2$ and $B=\mathbb F_r^\times$, the eigenvalue on the identity coset is $(r-2)/(r-1)$ and all the others are $-2/(r-1)$ by the [quadratic norm calculation](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy). In prime fields, a uniform power saving for the scalar averages at $b\asymp\sqrt p$ would be an estimate at the scale of [Bourgain's shifted-subgroup character-sum problem](https://arxiv.org/pdf/1401.4618). The block count above uses only the Jacobi entry bound.

### Which scalar blocks can approach norm one

Extend $s(a)=\chi(1-a)$ to $\mathbb F_q^\times$. For a coset $C=cB$ of $B$ in the full multiplicative group write $F(C)=\sum_{a\in C}s(a)$. The exact second moment is

$$\sum_{C\in\mathbb F_q^\times/B} F(C)^2=q-2b.$$

Indeed, sum $|\sum_{a\in B}\chi(1-ca)|^2$ over all $c\in\mathbb F_q$. The diagonal pairs contribute $b(q-1)$. Each distinct pair gives $-1$ by the nondegenerate quadratic character sum because $a$ and its partner are squares. Remove the value $b^2$ at $c=0$ and divide by $b$ to pass from scalars to cosets.

For $C\subset Q$ we have $F(C)=F(C^{-1})$ by inversion symmetry of $s$. Therefore every block indexed by a coset with $C\ne C^{-1}$ has absolute eigenvalue at most $\sqrt{(q-2b)/2}/b$. At $b\sim\sqrt q$ this leaves at most the two self-inverse cosets of $Q/B$ as possible blocks of norm tending to $1$.

There are further restrictions on the identity coset. The identity $s(a)s(-a)=s(a^2)$ holds for $a\in Q$. If $b$ is odd, squaring permutes $B$ and $-B$ is a distinct coset in $Q$. On $B\setminus\{1\}$, $s(-a)=s(a)s(a^2)$. For $u,v\in\{\pm1\}$ and $\sigma\in\{\pm1\}$, $uv\ge 1-|u-\sigma|-|v-\sigma|$. Sum with $\sigma$ chosen to be the sign of $F(B)$ and include $a=1$ using $s(-1)\ge-1$. This gives $F(-B)\ge 2|F(B)|-b$. Thus with $x=|F(B)|/b$ the second moment implies

$$x^2+(2x-1)_+^2\le(q-2b)/b^2,$$

and $x\le4/5+o(1)$ at $b\sim\sqrt q$. If $b$ is even, use $uv\ge-1-u-v$ on $[-1,1]^2$ in the same identity. Writing $F_2=\sum_{a\in B^2}s(a)$ gives $2F_2\ge-b-2F(B)$, since every square in $B$ has two preimages there. As $F(B)-F_2\ge-b/2$, the identity block has eigenvalue $F(B)/b\ge-1/2$. The remaining cases are the positive identity block for even $b$ and the nonidentity self-inverse block when $Q/B$ has even order. The square-order subfield realizes the positive identity case.

If $4\mid b$, the nonidentity self-inverse coset also has a uniform gap. Write $C=cB=C^{-1}\ne B$ and $G=B^2$. We have $c^2\in B\setminus G$, since $c^2\in G$ would imply $c\in B$ using $-1\in B$. The squaring map takes each pair $\{a,-a\}$ in $C$ to one element of $B\setminus G$. There are $(b-|F(C)|)/2$ entries of minority sign in $C$, so at most that many pairs have product $s(a)s(-a)=-1$. Consequently

$$F(B\setminus G)\ge b/2-(b-|F(C)|).$$

Since $G$ has even order, the preceding identity-coset estimate gives $F(G)\ge-b/4$. Thus $F(B)\ge |F(C)|-3b/4$. Applying the second moment to the two distinct cosets $B,C$ gives

$$x^2+(x-3/4)_+^2\le(q-2b)/b^2,\qquad x=|F(C)|/b.$$

For $b\sim\sqrt q$ this bounds $x$ by $(3+\sqrt{23})/8+o(1)<1$. A near-unit nonidentity block can therefore occur only for $b$ odd or $b\equiv2\pmod4$.

At prime order and $b(b-1)>n$, every positional coset $C\subseteq Q$ satisfies $|F(C)|\le b-2$ if $C\ne B$, and $|F(B)|\le b-3$. Indeed, exact constancy of the sign on $C$ away from $1$ would give a constant sign for all nonzero differences $x-y$ with $x\in B$, $y\in C$, because $x$ is a square and $y/x\in C$. Scale both sets by a nonsquare for a negative sign. The [Hanson–Petridis sumset bound, Theorem 1.2](https://arxiv.org/abs/1905.09134) yields $b^2\le n+|B\cap C|$, which contradicts the size assumption. The integer steps of the sign sum give the claimed deficit. This supplies a prime-order gap of at least $2/b$ for the compression to a single frequency coset, including the remaining self-inverse cases. A gap bounded away from zero would require substantially more than exclusion of exact constancy.

## Consequence for the linearized equation

Let $D$ be any even real diagonal with $\|D\|\le1$, let $P_\perp=I-J$, and on mean-zero vectors set $H=K-P_\perp D P_\perp$. This includes the diagonal from the true smoothing equation. Suppose $y$ is a unit mean-zero even vector with $\|Hy\|_2\le\eta$ and $\|P_{S^c}y\|_2\le\epsilon$. By $K^2=P_\perp$, $\|P_\perp Dy\|_2\ge1-\eta$ and $\|JDy\|_2\le\sqrt{2\eta}$ for $0\le\eta\le1$. Hence

$$\|P_{S^c}Ky\|_2\le\epsilon+\sqrt{2\eta}+\eta,\qquad
\|K_S P_S y\|_2\ge1-2\epsilon-\sqrt{2\eta}-\eta.$$

The norm deficit of $P_S y$ under $K_S$ is then $O(\epsilon+\sqrt\eta)$ in squared norm. On the part of the compression with absolute eigenvalue below $1/2$ that deficit is at least $3/4$ of its squared norm. Together with the original tail this shows that $\mathcal F^{-1}y$ lies within $O(\sqrt\epsilon+\eta^{1/4})$ in $\ell_2$ of a vector supported on the union $E$ of the $O_{r_0}(1)$ positional cosets identified above. Enlarge $E$ by inversion so the coordinate restriction of the even positional vector remains even. The bound also holds when $2\epsilon+\sqrt{2\eta}+\eta\ge1$ by increasing the constant.

Now take prime order $p$ and let $B'\le Q$ have order comparable to $\sqrt p$. Every positional coset of $B'$ meets the Möbius image $U(E)$ in at most $O_{r_0}(p^{9/20})$ points. Indeed, lift each coset pair by squaring and use the bounded-doubling version of the incidence estimate. To count images on inverse pairs, count both representative choices, or use the inversion invariance of $E$. The identity orbit changes the intersection by at most one.

If $T$ is a frequency coset of $(B')^\perp$, the inverse Fourier image of any vector supported on $T$ has constant modulus on each positional coset of $B'$. For $z$ supported on $T$ this gives

$$\|\mathbf1_{U(E)}\mathcal F^{-1}z\|_2^2\le O_{r_0}(p^{-1/20})\|z\|_2^2.$$

Taking the adjoint, using $C=\mathcal F U\mathcal F^{-1}$, and adding the positional tail gives the estimate

$$\|P_T C y\|_2=O_{r_0}\big(p^{-1/40}+\sqrt\epsilon+\eta^{1/4}\big).$$

It also holds for any fixed number of tested frequency cosets, with a constant depending on their number. Thus a slow mode concentrated in a fixed number of critical-size cosets in the original basis has vanishing mass in every such coset in the transformed basis. A general slow mode may have more irregular frequency concentration. The estimate does not establish which shapes occur for the prime-order stationary diagonal.

## Arbitrary sets at the smallest possible scale

The same argument up to $\|K_S P_S y\|_2\ge 1-2\epsilon-\sqrt{2\eta}-\eta$ applies to arbitrary $S$. Since $\|K_S\|\le\|K_S\|_{\mathrm F}\le |S|\sqrt q/n$, a sequence of unit slow modes with $\epsilon,\eta\to0$ requires $|S|\ge(1-o(1))n/\sqrt q$.

If $m=|S|=(1+o(1))n/\sqrt q$ attains this lower scale, then $\|K_S\|\to1$ and $\|K_S\|_{\mathrm F}\to1$. The following two further necessary conditions hold:

$$\frac1{m^2}\sum_{i,j\in S}\left(1-\frac{|\lambda_{i-j}|^2}{q}\right)\longrightarrow0,
\qquad\left\|\,|P_S y|-m^{-1/2}\mathbf1_S\,\right\|_2\longrightarrow0.$$

The first is the equality case of the entrywise bound in the sum of squared entries. For the second, the spectral theorem gives $K_S=\alpha b b^*+o_{\mathrm F}(1)$ for a unit vector $b$ and $|\alpha|\to1$, since all other squared eigenvalues sum to $o(1)$. Also $P_S y$ is within $o(1)$ of a scalar of modulus $1$ times $b$. Entrywise absolute values are Lipschitz in Frobenius norm. The nonnegative matrix $|K_S|$ of entrywise absolute values has maximum entry $(1+o(1))/m$ and squared Frobenius norm tending to $1$. Therefore its entry sum is $(1+o(1))m$, and its Frobenius distance to $m^{-1}\mathbf1_S\mathbf1_S^*$ tends to zero. This gives the same rank-one approximation for $|b||b|^*$ and proves the asserted flatness in magnitude.

This supplies a concrete arithmetic test for arbitrary sets of the smallest possible size. A uniform positive lower bound on the displayed mean Jacobi deficit would exclude all such modes at prime order. Larger supports are outside this equality-case argument. The square subfield mode meets both necessary conditions.

The [endpoint concentration argument](critical-sets.md) shows in addition that almost all pairs in such a set must have differences with growing multiplicity. It gives a numerical comparison over arbitrary supports and the square controls.

## Square-order control and numerical probe

At order $r^2$ the normalized $P_\perp\mathbf1_A$ for $B=\mathbb F_r^\times$ is already an exact $+1$ eigenvector of $K$. Its mass outside $A$ tends to zero. For example, choose $D_i=1-1/r$ on $A\setminus\{0\}$ and $D_i=0$ elsewhere. The vector is then an approximate null vector of $H$ with residual $O(r^{-1/2})$. The [explicit formula for $C\mathbf1_A$](mobius.md#square-order-comparison) places a nonvanishing amount of its mass in each of the two transformed subgroup cosets. Thus the prime-field conclusion genuinely uses the incidence estimate even for a diagonal with $D_0=0$.

[The compression and stationary-response probe](../data/subgroup-modes.csv) lists the maximal subgroup-coset bias and where the actual inverse response lies at $\tau=0.5$. At $q=389^2$, the compression for $b=388$ has norm $387/388\simeq0.9974$, and its constant mode alone carries $99.59\%$ of the squared response. At $p=1000033$ the largest compression norm across the tested sizes is $0.15152$, and the largest coset carries $0.214\%$ of the squared response. The compression values are integer coset sums divided by the subgroup order. The response values are floating point. The scalar eigenvalues were cross-checked against the dense Fourier compression at small orders.
