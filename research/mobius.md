# The Möbius transform of the Paley Fourier multiplier

This is an exact normal form for $K$ on the even subspace of the Fourier LP. It yields a prime-field bound separating one specific mechanism for concentration from its square-order analogue.

## Conjugation to a half-period shift

Let $Q=(\mathbb F_q^\times)^2$, $q\equiv1\pmod4$, and $n=|Q|$. On $\mathbb F_q\setminus\{0,1,-1\}$, the Möbius involution $\rho(t)=(1-t)/(1+t)$ satisfies $\rho(-t)=1/\rho(t)$ and $\rho(1/t)=-\rho(t)$. Thus $\{t^2,t^{-2}\}\mapsto\{\rho(t)^2,\rho(t)^{-2}\}$ is an involution of inverse pairs in $Q\setminus\{1\}$. Extend it by fixing $1$ and call its pullback $U$ on even functions on $Q$. It preserves orbit sizes, including the singleton $-1$, so $U$ is orthogonal and self-adjoint. It fixes the constant and the delta at $1$.

For $a=t^2\ne1$,

$$s(\rho(t)^2)=\chi(1-\rho(t)^2)=\chi(4t/(1+t)^2)=\chi(t)=\xi(a),$$

where $\xi$ is the unique character of order two on $Q$. At $1$, $s$ is zero. Write $C=FUF^{-1}$ on real even Fourier vectors, let $R$ shift by $\xi$ on $\widehat Q$, and let $J$ project onto constant Fourier vectors. Then

$$C^2=I,\qquad C e_0=e_0,\qquad C\mathbf1=\mathbf1,\qquad K=C(R-J)C.$$

In a cyclic coordinate $R$ shifts by $n/2$. Equivalently, a feasible spectrum for either sign maps under $C$ to a constant plus a mean-zero vector in the corresponding $R$ eigenspace. Thus the linear constraints in the transformed coordinates are pairwise equalities or antisymmetries. Nonnegativity remains a constraint in the original coordinates. For a diagonal activation derivative $D$, the even restriction of the [marked linearization](marked-response.md) becomes $R-J-P_\perp C D C P_\perp$ under $C$ and the marked source stays fixed.

## Matrix entries as three-factor character sums

Write $\Pi_{\rm ev}$ for even projection in $\widehat Q$ and $\rho_k(t)=k(t^2)$ for the character attached to $k\in\widehat Q$. For nontrivial $k,l$, with the Fourier convention $Ff(k)=\sum_{a\in Q}k(a)f(a)$, we have

$$\langle e_k,C\Pi_{\rm ev} e_l\rangle
=\frac1n+\frac1{2n}\sum_{t\ne0,\pm1}\rho_k(t)\,\overline{\rho_l(1-t)}\,\rho_l(1+t).$$

Indeed the inverse Fourier input is $n^{-1}\operatorname{Re}l(a)$. The identity orbit contributes $1/n$. In the remaining sum one can replace the real part of the character of $\rho(t)^2$ by the conjugate character because $t\mapsto-t$ inverts it and leaves $\rho_k(t)$ unchanged. The rank-one Kummer tensor in the displayed sum is nontrivial and tame, with four ramified punctures $0,1,-1,\infty$. The complete-sum bound is $2\sqrt q$ by the rank-one Weil bound, or by Euler characteristic and the weight bound on $H_c^1$. Thus the nonmarked entries of $C\Pi_{\rm ev}$ have absolute value at most $(\sqrt q+1)/n$. This bound also holds at square orders. [Katz, *Convolution and Equidistribution*](https://web.math.princeton.edu/~nmk/mellin331.pdf)

## A power saving for subgroup indicator overlaps at prime order

For a subgroup $B$ of $Q$, put $f_B=\mathbf1_{B^\perp}/\sqrt{|B^\perp|}$, where $B^\perp\subset\widehat Q$ is its annihilator. By unitary Fourier inversion this corresponds to the positional vector $\mathbf1_B/\sqrt{|B|}$. Consequently, if $D$ is a second subgroup, then

$$\langle f_B,C f_D\rangle=\frac{|B\cap U(D)|}{\sqrt{|B||D|}}.$$

Here $U(D)$ denotes the set obtained by applying the inverse-pair involution. This is meaningful since subgroups are invariant under inversion.

Suppose $q=p$ is prime and both subgroup sizes are comparable to $\sqrt p$. Then uniformly over such $B,D$,

$$|B\cap U(D)|=O(p^{9/20}),\qquad \langle f_B,C f_D\rangle=O(p^{-1/20}).$$

To prove it, lift $B,D$ by squaring to subgroups $G,L$ of $\mathbb F_p^\times$ of sizes $a=2|B|$ and $b=2|D|$. The intersection count equals $1$ plus half the number $M$ of $t\in G$ with $\rho(t)\in L$, where poles are omitted. Use the family $\mathcal T=\{x\mapsto h\rho(gx):g\in G,\ h\in L\}$. Its $N=ab$ members are distinct, since the zero and pole determine $g$ and the scale determines $h$. Every member has exactly $M$ incidences with $G\times L$ by multiplicative invariance, so the incidence count is $NM$.

The group energy $E(\mathcal T)$ counts pairs of quotients of two elements of $\mathcal T$ that agree. A quotient can be written $h_1\rho r\rho h_2^{-1}$ where $r=g_1/g_2\in G$ and a scalar is interpreted as a scaling map. The middle map has a matrix with diagonal entries $1+r$ and off-diagonal entries $1-r$. For $r=1$ or $-1$ it is a scaling or inversion, and each of these sectors contributes at most $bN^2$ to the energy. For $r\ne\pm1$, all four entries are nonzero. The diagonal-scaling invariant of the matrix, the product of diagonal entries divided by the product of off-diagonal entries, is $((1+r)/(1-r))^2$. This allows at most two values of $r$ for a given quotient. For each such $r$ the top-right and bottom-left entries divided by the bottom-right entry determine $h_1,h_2$. There are $a$ choices of $(g_1,g_2)$ per $r$. The multiplicity of each nondegenerate quotient is at most $2a$, so this sector contributes at most $2a N^2$. In total $E(\mathcal T)\le 2(a+b)N^2$.

Applying the incidence bound of Warren and Wheeler, Theorem 4, and dividing by $N$ gives

$$M\ll a^{3/10}b^{1/2}(a+b)^{1/10}+b^{1/2}.$$

Their theorem assumes the second coordinate set has size at most $\sqrt p$. When $b$ is larger by a bounded factor, partition $L$ into a bounded number of pieces of size at most $\sqrt p$ and sum the incidence bounds with the same $\mathcal T$. This preserves the estimate up to a constant depending on the size range. The bound above is $O(p^{9/20})$ at the specified scale. [Warren and Wheeler, Theorem 4](https://arxiv.org/pdf/2107.12286)

The saving also controls $C$ between the spans of all the unshifted $f_B$ in any fixed comparable size range. To see this, let $\sum_b c_b\mathbf1_{B_b}/\sqrt b$ be the unitary inverse Fourier image of a vector in that span, where $B_b$ is the subgroup of order $b$. Its value on elements of exact order $d$ is $g_d=\sum_{d\mid b}c_b/\sqrt b$, and its squared norm is $\sum_d\varphi(d)|g_d|^2$. Möbius inversion gives $c_b/\sqrt b=\sum_{b\mid d}\mu(d/b)g_d$. Every contributing $d$ in this sum is at least $b$ and divides a subgroup order in the chosen size range. The elementary bounds on the divisor function and $d/\varphi(d)$ give $\sum_b|c_b|\le p^{o(1)}$ times the vector norm. Taking two such combinations in the overlap formula gives operator norm $O(p^{-1/20+o(1)})$ for the compression of $C$ to that span.

The intersection estimate also holds for inversion-invariant sets $B,D$ of sizes comparable to $\sqrt p$ with $|B/B|=O(|B|)$ and $|DD|=O(|D|)$. Lift to $G,L$ as before. With arbitrary sets the same energy proof works: a fixed ratio $r$ has at most $a$ representations, and the two degenerate sectors have at most $2ab^2$ pairs total, each quotient with multiplicity at most $ab$. The transforms $h\rho(gx)$ each have at least $M$ incidences with the enlarged grid $(G/G)\times (LL)$, since $t\in G$ and $\rho(t)\in L$ give $x=t/g$ and $y=h\rho(t)$. Both enlarged sizes are still $O(\sqrt p)$, including after taking square roots since $G/G$ and $LL$ consist of both lifts of their images. Applying the same incidence bound gives $M=O(p^{9/20})$, with constants depending on the size and doubling bounds. Restoring the identity contributes at most $1$.

## Square-order comparison

At $q=r^2$, take $B=\mathbb F_r^\times$ and let $T_1$ be the norm-one torus in $\mathbb F_{r^2}^\times$. The condition $t^2\in B$ gives $t^r=\pm t$. On the first branch $\rho(t)^r=\rho(t)$, and on the second it equals $\rho(t)^{-1}$. Applying the involution backwards confirms, with the identity restored, that

$$U(B)=B^2\cup T_1^2.$$

The subgroup sizes are $(r-1)/2$ and $(r+1)/2$, and their intersection is $\{1\}$. Both lie in $\ker\xi$, since $n/2$ is divisible by both sizes. Thus their annihilator indicators are $R$-invariant. The overlaps of $C f_B$ with $f_{B^2}$ and $f_{T_1^2}$ are exactly $1/\sqrt2$ and $\sqrt{(r+1)/(2r-2)}$. The [power saving above](#a-power-saving-for-subgroup-indicator-overlaps-at-prime-order) separates these flat subgroup shapes at prime order. Controlling an arbitrary near-zero mode of the marked linearization would require an additional statement linking that mode to such shapes or controlling the rest of the operator independently.

[Exact overlap counts](../data/mobius-overlaps.csv) compare these cases with prime-order subgroups. In the tested size range, the largest observed overlap was about $0.000250$ at $p=1000000009$, compared with the square-order value near $0.7071$. The prime counts enumerate the squared Möbius images and use their multiplicative orders. The square rows use the subfield identity.
