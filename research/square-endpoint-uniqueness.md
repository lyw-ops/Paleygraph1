# Uniqueness of the subfield optimum over large prime squares

Let $q=h^2$, where $h$ is an odd prime. For the positive sector of Problem 26, the subfield gives $\theta_+=h-1$. It also gives the **unique** optimal spectrum, even when other frequencies attain the maximum Jacobi eigenvalue. The proof uses an algebraic-torus argument and a finite exact rank check at 16 small characteristics. In particular, with the two spectra normalized to sum $\sqrt n$, the least squared norms at the two optima are $h-1$ and $2h/(h+1)$. The result describes the square obstruction to a uniform prime-power argument.

## From pure Jacobi sums to three types of positional functions

Write $B=\mathbb F_h^\times$, $T=\{t\in\mathbb F_{h^2}^\times:t^{h+1}=1\}$, $Q=(\mathbb F_{h^2}^\times)^2$, $n=|Q|$, $d=(h+1)/2$, and $H=B^\perp\le\widehat Q$. Both groups lie in $Q$, their intersection is $\{1,-1\}$, and $BT=Q$ by their orders. The [constant minus witness](square-order-control.md#a-square-order-comparison) at the exact optimum forces every plus optimizer to be supported on $E=\{0\}\cup\{i:\widehat s(i)=h\}$. Here $s(x)=\chi_{h^2}(1-x)$ and the nontrivial $\widehat s(i)$ are real parts of Jacobi sums of absolute value $h$. Saturation requires the full Jacobi sum to equal $h$.

Akiyama's classification applies to the full character lifts, with quadratic second character and nontrivial restriction to $Q$. One type has order dividing $h+1$, hence restricts into $H$. The second type has order $2(h-1)/k$ with $k$ odd. Away from $H$ it can have sign $+h$ only for $h\equiv3\pmod4$. In that case its exponent in the full cyclic character group is an odd multiple of $d$, so on $T$ its restriction is the nontrivial quadratic character $\eta(t)=t^{(h+1)/2}$. The remaining types have orders 24 and 60. The character orders and signs are those of the pure Jacobi sum theorem. [Akiyama, *On the pure Jacobi sums*](https://www.math.tsukuba.ac.jp/~akiyama/papers/Jacobi_priv.pdf)

For a plus optimum let $\mu$ be its mass-one nonnegative spectrum and put $f(x)=\sum_i\mu_i i(x)$. Thus $f(1)=1$ and $f(x)=0$ wherever $s(x)=-1$. Splitting its spectrum according to the three types gives

$$ f(bt)=F(t)+\eta(t)G(b)+E_0(b,t),\qquad b\in B,\ t\in T. \tag{1} $$

Here $F(t)$ uses the frequencies in $H$, $G$ is zero if $h\equiv1\pmod4$, and $E_0$ is a sum of products of the restrictions of the exceptional characters to $B$ and $T$. Frequencies in more than one class can be assigned to any one of their classes. Take $B_0\le B$ to be the common kernel of the exceptional restrictions on $B$, and $T_0\le T$ their common kernel on $T$ intersected with $\ker\eta$. Both indices are at most $\operatorname{lcm}(24,60)=120$. In particular $E_0(b,t)$ depends only on the cosets of $B_0,T_0$.

## The forbidden cells determine the values off the subfield

For a fixed $t\ne\pm1$, the quadratic polynomial in $b$

$$ N(1-bt)=1+b^2-b(t+t^{-1}) $$

has no root in $\mathbb F_h$ and nonzero discriminant. Its quadratic character sum over $\mathbb F_h$ is $-1$, and the term at $b=0$ is one. Using $\chi_{h^2}(1-bt)=\chi_h(N(1-bt))$, the set $R_t=\{b\in B:s(bt)=-1\}$ therefore has $(h+1)/2$ elements. In particular $R_t\cap R_{t'}\ne\varnothing$ for every pair of nonidentity columns $t,t'\ne\pm1$.

For $t,t'$ in the same $T_0$-coset, take $b$ in that intersection and apply (1) at both forbidden points. The values of $G$, $\eta$ and $E_0$ agree in the two equations, so $F(t)=F(t')$. Therefore for each fixed $b$, the value $f(bt)$ depends only on the $T_0$-coset of $t$ as long as $t\ne\pm1$.

For fixed $b\ne\pm1$, every $T_0$-coset contains a forbidden point once $|T_0|>2\sqrt h$. To see it, view $T$ as the rational points of the norm-one algebraic torus over $\mathbb F_h$. For every multiplicative character $\omega$ of $T$ one has

$$ \left|\sum_{t\in T}\omega(t)\chi_h(1+b^2-b(t+t^{-1}))\right|\le2\sqrt h. \tag{2} $$

Over the algebraic closure the torus is $\mathbb G_m$. The quadratic Kummer factor has distinct simple zeros $b,b^{-1}$ and its only boundary poles are at zero and infinity. A Lang character factor is lisse on the torus and tame at the boundary. Their product is geometrically nontrivial because of its quadratic inertia at a simple zero. On the projective line minus these four punctures, the two extreme compact-support cohomology groups vanish, and the tame Euler characteristic makes the middle group two-dimensional. The weight bound gives (2). The two zeros are outside $T(\mathbb F_h)$ for $b\ne\pm1$. Coset averaging gives the same $2\sqrt h$ bound for the unweighted character sum on each $T_0$-coset. The points $t=\pm1$ have positive sign for such $b$, so a negative term is a nonidentity column. The tame character construction and weight bound are the same as in [the cyclic torus argument](parallel-torus-8.md#a-uniform-bound-for-twisted-translate-correlations). [Deligne, Weil II](https://numdam.org/articles/10.1007/BF02684780/)

Consequently $f(bt)=0$ for every $b\ne\pm1$ and $t\ne\pm1$. For the two remaining rows, there is a $b'\ne\pm1$ in the same $B_0$-coset as $b$ when $|B_0|>2$. If $G=0$, equation (1) gives identical rows. Otherwise $h\equiv3\pmod4$, and for $t\in T\setminus\{1\}$ the identity $(1-t)^{h-1}=-t^{-1}$ gives $s(t)=\eta(t)$. Also $\eta(-1)=1$. Choose a column with $\eta(t)=-1$. Both $f(bt)$ and $f(b't)$ vanish there, the first by its sign and the second by the preceding argument. Their difference in (1) proves $G(b)=G(b')$. All nonidentity columns vanish in the special rows as well.

Under the two size assumptions, $f$ is supported on $B$. Its Fourier spectrum is constant on the cosets of $H$. The marked value is $\mu_0=1/d$, so the coset $H$ alone has mass one. Nonnegativity now forces $\mu=\mathbf1_H/d$, as claimed. Positivity enters in this last mass step after the complex-valued grid equations.

## Exhausting the small characteristics

The index of $T_0$ divides the gcd of $h+1$ with the least common multiple of 2 and the applicable exceptional orders. The analogous bound for $B_0$ uses $h-1$ and omits 2. It suffices to take the following thresholds. In the two-order case the congruences force $h\equiv41\pmod{120}$.

| Possible exceptional orders and congruence | $[T:T_0]$ at most | $[B:B_0]$ at most | Sufficient $h$ |
|:---|---:|---:|---:|
| Neither | 2 | 1 | $h>16$ |
| Only 24, $17\pmod{24}$ | 6 | 8 | $h>144$ |
| Only 24, $19\pmod{24}$ | 4 | 6 | $h>64$ |
| Only 60, $41\pmod{60}$ | 6 | 20 | $h>144$ |
| Only 60, $49\pmod{60}$ | 10 | 12 | $h>400$ |
| Both | 6 | 40 | $h>144$ |

These conditions leave only the characteristics

$$3,5,7,11,13,17,19,41,43,89,101,109,113,137,229,349.$$

For these inputs, [exact rank replay](../square_endpoint_rank.py) uses the classification to list every possible saturated frequency. It tests the remaining exceptional candidates by checking $\widehat s(i)=h$ by exact cyclotomic reduction. On the resulting set $E$, it measures rank of forbidden-position Fourier rows over an auxiliary prime field whose multiplicative group contains a primitive $n$th root. A nonzero modular minor certifies the same rank lower bound in characteristic zero. The subfield vector supplies a kernel, so finding rank $|E|-1$ certifies uniqueness even in the full complex support kernel. The replay attains that rank in all 16 cases. The selected rows are just candidates for the minor. Rank is exact, regardless of how the rows are selected.

## Least norms

The plus optimizer of sum $\sqrt n$ is $X=\alpha\mathbf1_H$ with $\alpha=(h-1)/\sqrt n$, so $\|X\|^2=h-1$. The constant minus witness in this normalization is $Y=j+\alpha P_-e_0$, with $j=\mathbf1/\sqrt n$ and $(P_-)_{00}=1/2$. Among all vectors in $U_-$ of fixed mean and mark, the minimum norm is this vector: the least-norm mean-zero correction with the prescribed value at zero is parallel to $P_-e_0$. It is a feasible minus optimum, so $\|Y\|^2=1+\alpha^2/2=2h/(h+1)$. The minus formula holds at every prime-square order, without the plus uniqueness argument.

The plus result settles the norm of the actual minimizing endpoint on the square control. It rules out the possibility that the larger-theta side can choose a dispersed spectrum of bounded norm while preserving the optimal mark. The expulsion of exceptional modes here uses exact square saturation to invoke the pure Jacobi classification. At prime order it does not control approximate saturation on growing frequency sets.
