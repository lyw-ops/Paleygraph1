# Three-point Jacobi caps on arbitrary frequency supports

There is a quantitative obstruction beyond the one-point deficit test in [critical sets](critical-sets.md). At the critical scale $m\asymp\sqrt q$, an arbitrary set $S$ with mean squared Jacobi deficit $O(q^{-1/2})$ must have a nonzero translate overlapping it on $\gg q^{7/24}$ points. If all nonzero overlaps are $O(q^{1/4})$, the deficit is instead $\gg q^{-1/3}$. For $m\le m_0+o(q^{1/6})$, this gives a compression gap larger than the stationary critical width. The estimate also has a weighted version for feasible spectra. It applies to primes and squares; the exact square witness shows why an upper bound on the overlaps or another prime-specific input remains necessary.

## Two widths in the triangle count

Let $q\equiv1\pmod4$ be an odd finite field order, $Q=(\mathbb F_q^\times)^2$, $n=|Q|$, $m_0=n/\sqrt q$, $s(x)=\chi(1-x)$ on $Q$, and $\lambda=Fs$. Write the dual of $Q$ additively. For $0<t\le1/4$, define

$$L_t=\{h:1-\lambda_h^2/q\le t\},\qquad
\mathcal T_t=\{(u,v):u,v,v-u\in L_t\}.$$

The bound is

$$|\mathcal T_t|\ll q^2(\sqrt t+q^{-1/4})(t+q^{-1/3}). \tag{1}$$

For a nonzero $h$, let $\alpha$ be a lift to a character of $\mathbb F_q^\times$ and write $z(\alpha)=J(\alpha,\chi)/\sqrt q$. Then $|z|=1$, $z(\alpha\chi)=\overline{z(\alpha)}$ and $\lambda_h/\sqrt q=\operatorname{Re}z(\alpha)$, by the two-lift calculation in [critical sets](critical-sets.md#repeated-differences-are-necessary). Assign $z=1$ at the two exceptional characters. The positive test

$$P_M(h)=\frac{1}{M^2}\left|\sum_{j=0}^{M-1}z(\alpha)^{2j}\right|^2$$

is well defined on the dual of $Q$, independent of the lift. On $L_t$, the argument of $z^2$ is $O(\sqrt t)$ modulo $2\pi$. For $M\sqrt t$ smaller than a fixed absolute constant, $P_M\ge 1/4$ there, by taking real parts of the summands. The test with $M=1$ majorizes unconditionally. Its expansion in $z^{2j}$ has nonnegative coefficients of sum one and constant coefficient $1/M$.

In the Gauss-quotient formula for $z$, the numerator and denominator use the twists $1,\chi$, and the remaining factor is a constant of modulus one. If $u\ne0$ and $\beta$ lifts $u$, the product of powers at $h$ and $h-u$ uses the four distinct character twists $1,\chi,\bar\beta,\chi\bar\beta$. For exponents $j,k$ not both zero, [Katz's Gauss moment bound, Theorem 9.6](https://web.math.princeton.edu/~nmk/Katz-GKM.pdf) bounds the corresponding full-character mean of $z(\alpha)^{2j}z(\alpha\bar\beta)^{2k}$ by $O((|j|+|k|)/\sqrt q+1/q)$: omit the zero exponents, and use disjoint lists of twists for the positive and negative Gauss powers. The bound is uniform in the twists and in the displayed exponents. The assignments at the at most four exceptional characters cost $O(1/q)$. Although a monomial need not descend, the test and its translated product do, so averaging the expanded test over the full character group gives the desired averages on the dual of $Q$. In particular,

$$\mathbb E_h P_M(h)=M^{-1}+O(M/\sqrt q),\qquad
\mathbb E_h P_M(h)P_M(h-u)=M^{-2}+O(M/\sqrt q)\quad(u\ne0).$$

For the first count, take $M\asymp\min(t^{-1/2},q^{1/4})$, with the constant small enough for majorization. For the intersection count, take the wider test with $M\asymp\min(t^{-1/2},q^{1/6})$. Rounding to at least one costs only an absolute factor. This gives

$$|L_t|\ll q(\sqrt t+q^{-1/4}),\qquad
|L_t\cap(u+L_t)|\ll q(t+q^{-1/3})\quad(u\ne0).$$

Keeping the narrower single test on the first edge matters: $0\notin L_t$ since $\lambda_0=-1$, so one may sum the uniform intersection bound over just $u\in L_t$, proving (1). At $t\asymp q^{-1/2}$ this counts $O(q^{17/12})$ ordered patterns of relative differences, fewer than the order $q^{3/2}$ triples of a critical support.

## Translation multiplicities and a compression gap

For any probability $\mu$ on the frequency group, put

$$r_\mu(h)=\sum_i\mu_i\mu_{i+h},\qquad d_\mu=\sum_h r_\mu(h)(1-\lambda_h^2/q).$$

The mass of triples whose three differences lie in $L_t$ is at least $(1-3d_\mu/t)_+$, by the union bound and Markov. The weight of an ordered pattern $(u,v)$ is $b(u,v)=\sum_i\mu_i\mu_{i+u}\mu_{i+v}$. Expanding the squares gives the exact identity

$$\sum_{u,v} b(u,v)^2=\sum_h r_\mu(h)^3.$$

Indeed, two triples with the same pattern differ by one common translation $h$, and at fixed $h$ their three pairs can be summed independently. Cauchy–Schwarz on the good patterns and (1) give the uniform weighted inequality

$$\sum_h r_\mu(h)^3\gg
\frac{(1-3d_\mu/t)_+^2}{q^2(\sqrt t+q^{-1/4})(t+q^{-1/3})}. \tag{2}$$

Suppose $r_\mu(0)\le C_0 q^{-1/2}$. If $d_\mu=O(q^{-1/2})$, take $t=Aq^{-1/2}$ with a sufficiently large fixed $A$. Then $\sum_h r_\mu(h)^3\gg q^{-17/12}$. The zero shift costs at most $C_0^3 q^{-3/2}$, of smaller order. For $R_\mu=\max_{h\ne0}r_\mu(h)$ the remaining cubic sum is at most $R_\mu^2$, since $\sum_h r_\mu(h)=1$. Thus $R_\mu\gg q^{-17/24}$.

Conversely, if $R_\mu\le C_1 q^{-3/4}$, the full cubic sum is at most $(C_0^3+C_1^2)q^{-3/2}$. In (2) take $t=bq^{-1/3}$ with $b>0$ a sufficiently small constant depending on $C_0,C_1$. For large $q$ the denominator is at most an absolute constant times $\sqrt b\,q^{3/2}$. If $d_\mu\le t/6$, the lower bound contradicts the upper bound by the choice of $b$. Therefore $d_\mu\gg_{C_0,C_1} q^{-1/3}$.

For $\mu=\mathbf1_S/m$, $m=|S|\asymp m_0$, we have $r_\mu=r_S/m^2$ and $d_\mu=d(S)$. In particular:

- If $d(S)=O(q^{-1/2})$, then $\sum_{h\ne0}r_S(h)^3\gg m^{19/6}$ and some nonzero $h$ has $r_S(h)\gg m^{7/12}$. The one-point bound at this deficit scale requires only $\max_{h\ne0}r_S(h)\gg m^{1/2}$.
- If $\max_{h\ne0}r_S(h)\le Cq^{1/4}$, then $d(S)\gg_C q^{-1/3}$, with constants also depending on the comparison range for $m/m_0$. The Frobenius estimate $\|K_{SS}\|\le (m/m_0)\sqrt{1-d(S)}$ gives $\|K_{SS}\|\le 1-cq^{-1/3}$ for $m\le m_0+o(q^{1/6})$. This is uniform in the shape of $S$ and in the signs of the vectors tested against the compression.

## Exact stationarity and the square control

For a feasible probability of sign $\sigma$, $(I-\sigma K)\mu=\mathbf1/n$. Positivity and the entry bound give $r_\mu(0)\le\|\mu\|_\infty\le(1+\sqrt q)/n$. Pairing the equation with $\mu$ gives

$$\sum_h r_\mu(h)\frac{\sigma\lambda_h}{\sqrt q}= m_0\|\mu\|_2^2-\frac1{\sqrt q},\qquad
d_\mu\le 2\big(1+q^{-1/2}-m_0\|\mu\|_2^2\big).$$

The last inequality uses $1-a^2\le2(1-a)$ for $a\in[-1,1]$. Thus a positive normalized stationary spectrum within $O(q^{-1/2})$ of the maximum allowed *relative* squared norm must have a nonzero overlap $r_\mu(h)\gg q^{-17/24}$, regardless of its support. Under the diffuse-overlap hypothesis $R_\mu\ll q^{-3/4}$ the relative norm bound improves to $m_0\|\mu\|_2^2\le 1-cq^{-1/3}$.

For the actual one-sided high set $S_\sigma=\{i:\sigma D_i>\rho\}$, fix $0\le\rho<1$ and take $\tau>0$ sufficiently small in terms of $\rho$. The [reciprocal identity](parallel-stationary.md#transfer-to-the-actual-stationary-diagonal) bounds the normalized mass off $S_\sigma$ by $\sqrt{\tau(1+\rho)/(W(1-\rho))}+O(q^{-1/2})$. Write the unnormalized spectrum as $A=x+z$, with $x$ on $S_\sigma$ and $z$ on its complement. The same identity gives $\|z\|_2^2\le W(1+\rho)/(1-\rho)$. For $T=I-\sigma K$ one has $TA=\sqrt{W/n}\,\mathbf1$ and $0\le T\le2I$, so $\langle x,Tx\rangle=W-2\sqrt{W/n}\sum_i z_i+\langle z,Tz\rangle=O_\rho(W)$. Meanwhile positive normalized mass on $S_\sigma$ gives $\|x\|_2^2\gg nW/m$, with $m=|S_\sigma|$.

If $m\le m_0+o(q^{1/6})$, the quotient gives $\lambda_{\max}(\sigma K_{S_\sigma S_\sigma})\ge1-O_\rho(q^{-1/2})$ and the entry bound implies $m\sim m_0$. The compression gap above therefore excludes $\max_{h\ne0}r_{S_\sigma}(h)=O(q^{1/4})$ in this size range. With $m\le m_0+O(1)$ the same quadratic-form estimate and Frobenius bound give $d(S_\sigma)=O(q^{-1/2})$, with the constant depending on $\rho$ and the size slack, so the stronger $q^{7/24}$ overlap threshold applies. Neither transfer requires a coset cover or an eigenvalue hypothesis on the full stationary linearization.

At $q=r^2$ let $B=\mathbb F_r^\times$ and $S=B^\perp$. The [subfield formula](square-order-control.md#the-fourier-frequencies-carrying-the-discrepancy) gives $m=(r+1)/2$, $\lambda_h=r$ on $S\setminus\{0\}$ and $\lambda_0=-1$. Therefore $d(S)=(1-1/q)/m$, all $(m-1)(m-2)$ ordered nondegenerate patterns in $S^2$ belong to $\mathcal T_t$, and $\sum_{h\ne0}r_S(h)^3=(m-1)m^3$. The uniform probability on $S$ is an exact feasible plus spectrum because its positional transform is $\mathbf1_B$. Its normalized squared norm is $m_0/m=1-1/r$, so it also meets the weighted near-saturation hypothesis. Its nonzero overlaps on $S$ have size $1/m$, far above the diffuse range.

As an independent check, integer enumeration verified the pattern-square identity on weighted samples in cyclic groups of orders 5 through 38 and the subfield counts for $r=5,11,23,47,97$. For the same five square controls the FFT of the quadratic norm sign agreed with the stated endpoint values to within $10^{-10}$. The formulas above are exact; the FFT was only a check on the indexing.

The argument does not prove $\|v^*\|_2^2=o(\sqrt p)$. Even the near-critical case can have overlaps between the new power threshold and a fixed fraction of the support, with no large overlap subgroup. Near stationarity, controlling those overlaps requires additional prime-specific arithmetic or use of the two reciprocal spectra beyond the one-cone identity. At a fixed fraction of the maximal relative norm the deficit need not approach zero, and (2) does not exclude that case.
