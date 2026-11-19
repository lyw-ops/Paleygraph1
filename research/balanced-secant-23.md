# A balanced circulant example where the secant condition fails

[Astra's tail analysis](astra-secant-23.md) distinguishes the endpoint theta limit from the large-width secant condition. The following example gives an exact distinction even with balanced Fourier ranks and a cyclic group. It consists of regular Cayley graphs whose two theta values are exactly $\sqrt n$ but whose plus secant has a positive limit.

Take odd $m\ge3$ and write $G=\mathbb Z_4\times\mathbb Z_{m^2}$, a cyclic group of order $n=4m^2$. Let $H$ be the subgroup of order $m$ in the second factor. Use the connection set

$$
D_+=\bigl(\{1,3\}\times\mathbb Z_{m^2}\bigr)
\cup\bigl(\{0\}\times(H\setminus\{0\})\bigr).
$$

This is the lexicographic product of the four-cycle with a union of $m$ disjoint $m$-cliques. It has a clique of size $2m$, by choosing a clique in each of two adjacent blocks. It has an independent set of size $2m$, by choosing one vertex from each inner clique in two nonadjacent blocks. The product law for vertex-transitive theta then gives both theta values exactly $2m=\sqrt n$. It also gives the translated point cap $W_i\le1/(2m)$ for feasible mass-one spectra on both signs. The Fourier ranks divided by $n$ are $1/2+(m-1)/(4m^2)$ and $1/2-1/(4m)$.

## Exact moving-width limit

Write $W(k,j)$ for a plus mass-one Fourier row. In the outer frequency $k\in\mathbb Z_4$, it has the form

$$
W(k,j)=a_j+b_j\cos(\pi k/2)+c_j\sin(\pi k/2),
$$

since outer position 2 is forbidden. The coefficient $a_j$ is the average in $k$ and is constant on cosets of $I=H^\perp$ in the inner frequency group. This is the remaining positional support constraint, at outer position zero. Conversely these conditions, positivity and total mass one describe all such rows. For the real even optimum, the minimizing rows below already have that symmetry.

Set $x=4m a_0$, the mass on $\mathbb Z_4\times I$, and $z=2mW(0,0)$. Nonnegativity gives $|b_0|\le a_0$. Thus $0\le z\le x\le1$, and every pair $(x,z)$ in that triangle is feasible. For fixed $(x,z)$ the least squared norm takes $c_j=0$ everywhere, $b_j=0$ away from $j=0$, and $a_j$ uniform on the complement of $I$. Indeed

$$
\|W\|_2^2=4\sum_j a_j^2+2\sum_j(b_j^2+c_j^2);
$$

the first term is minimized by the uniform choice at fixed mass and the root fixes only $b_0=(2z-x)/(4m)$. The choices attain the minimum and satisfy positivity. In the notation of the [one-sided quadratic](one-sided-quadratic-22.md), the resulting minimum energy is

$$
\sqrt n\bigl(\|W\|_2^2-1/n\bigr)
= \frac{m}{2(m-1)}(x-1/m)^2+\frac{(2z-x)^2}{4m}.
\tag{1}
$$

This converges uniformly on the triangle to $x^2/2$. Consequently the field-size limit of the plus-witness $F_n(R)$ at fixed $R>0$ is

$$
f(R)=\max_{0\le z\le x\le1}\frac{z^2}{1+Rx^2/2}
=\frac1{1+R/2}.
$$

For any fixed $z$, the least limiting energy takes $x=z$, and the resulting quotient increases with $z$. The endpoint mark is one, the broad mark is zero, and

$$
\lim_{R\to\infty}R\bigl(f(R/2)-f(R)\bigr)=2.
$$

Balanced rank, translation symmetry, the point cap, and exact theta reciprocity therefore do not make the secant necessary. This example has a large projector entry unavailable in Paley localization. The plus projector at outer frequency difference 2 and inner difference zero has entry $(-2m^2+m-1)/(4m^2)$, tending to $-1/2$. The Jacobi entry bound for Paley is of order $n^{-1/2}$ off the diagonal. Whether the secant is necessary with that extra structure remains open.

An independent dense Fourier quadratic solve at $m=3,5$ and $R=1/4,1,8$ agrees with the two-variable minimization to within $4.1\cdot10^{-13}$ in all six comparisons.
