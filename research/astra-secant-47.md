# A finite quotient obstruction on the actual larger-side face

Suppose the normalized larger ordinary-theta mark exceeds one by a fixed amount, and its exact endpoint probability concentrates on a marked subgroup of order between roughly $2\sqrt n$ and $\sqrt{5n}$. Then a bounded cyclic quotient configuration already witnesses an ordinary-theta excess at the same primes, up to a vanishing error. The quotient comes from the actual Paley signs, and its size can be bounded in terms of the claimed excess. This extends the [previous mass gap](astra-face-46.md), which treats smaller marked subgroups. It is an inverse theorem for this concentration pattern. No unrestricted signed late-secant upper bound is obtained.

## Recovering a positive quotient row from the exact face

Write $G=\widehat Q$, $n=|Q|=(p-1)/2$, $B\le Q$, $b=|B|$, $H=B^\perp$, $m=n/b$, and $L=Q/B$. Let $\mu$ be any sign-feasible probability, $e=\mu(H^c)$, and $\alpha=\sqrt n\,\mu_0$. If $e<1/2$, then $B\setminus\{1\}$ has the allowed sign, since the real part of its positional transform is at least $1-2e$ there. Assume this monochromaticity for the rest of the argument. Let $A\subset L\setminus\{1\}$ consist of the cosets containing no forbidden point. It is inverse closed. Write $M(L,A)$ for the maximum of $m\rho_0$ over probabilities on $H=\widehat L$ with positional transform supported on $\{1\}\cup A$. This is a finite Fourier LP. Define $C_b=(\sqrt p+1)/b+10p/b^2$. Then

\[
 \boxed{\quad \alpha\le \frac b{\sqrt n}M(L,A)[1+(C_b-1)e].\quad}       \tag{1}
\]

Conversely, extending any such quotient probability by zero outside $H$ gives a feasible probability for the full sign, with normalized mark $b(m\rho_0)/\sqrt n$. In particular, if $X$ is the actual larger-side endpoint and $b\asymp\sqrt n$, its mark differs by $O(e)$ from the lifted optimum when $e<1/2$. Here $bM/\sqrt n$ is uniformly bounded since it is a feasible full-field mark.

To prove (1), write $f(C)=\sum_{h\in H}\mu_h h(C)$ and invert its truncation to $\{1\}\cup A$, calling the resulting real row $z$ on $H$. Its mass is $1-e$. On every remaining coset $C$, $f(C)$ equals the negative of the exterior transform averaged over $C\cap D$, where $D$ is the forbidden sector. Thus simultaneously for all $h\in H$,
\[
 m(z_h-\mu_h)=\sum_{i\notin H}\mu_i T_{i\bar h},\qquad
 T_k=\sum_{C\notin\{1\}\cup A}\frac1{|C\cap D|}\sum_{t\in C\cap D}k(t).
\]
Each exterior character $i\bar h$ is still nontrivial on $B$. The proof of the reciprocal-count bound in [round 46](astra-face-46.md) gives $|T_k|\le C_b$ even with the empty fibers omitted. In detail, replacing each inverse count by $2/b$ costs at most $2p/b^2$ on cosets with $|\sum_C s|\le b/2$ and at most $8p/b^2$ on the others by quotient Parseval. The replacement main term uses all forbidden positions, since the omitted cosets have none. Its modulus is at most $(\sqrt p+1)/b$ by the full Jacobi bound. Consequently adding $C_b e/m$ at every coordinate makes $z$ nonnegative, preserves the quotient support condition and gives a marked coordinate at least $\mu_0$. Dividing by its new mass proves (1). Discarding the outside coordinates without this uniform repair need not preserve the sector.

## The prime rectangle bound and bounded odd relations

If $U$ is the union of $B$ and the cosets in $A$, every nonzero member of $U-B$ has the allowed quadratic sign. Indeed $x-y=y(x/y-1)$ with $y\in B\subset Q$, and $\chi(-1)=1$. Dilate by a nonsquare for the minus sign. The full **rectangle** inequality of [Hanson and Petridis, Theorem 1.2](https://arxiv.org/pdf/1905.09134) gives
\[
                      (1+|A|)b^2\le n+b.                             \tag{2}
\]
It uses intersection size $b$. Separately, any quotient clique of size $k$ lifts to a clique of size $kb$, so $kb\le h_p=\lfloor(1+\sqrt{1+4n})/2\rfloor$. These deductions use prime order.

Fix $c>0$. On a supercritical prime sequence $\alpha\ge1+\delta$, assume $c\sqrt n\le b\le h_p/2$ and $e\to0$. Then the Cayley graph on $L$ with steps $A$ has a **bounded-length odd closed walk** at all sufficiently large indices, with bound depending only on $c,\delta$.

Here are the bounds establishing that statement. The degree $k=|A|$ is bounded by (2). Suppose instead the length of the shortest odd walk to the identity tends to infinity (use infinity for bipartite graphs). Take integers $r\to\infty$ with $2r+3$ smaller than this length. Balls $V_j$ about the identity have $|V_j|\le(2j+1)^k$ by commutativity. Some $j<r$ has $|V_{j+1}|/|V_j|\le(2r+1)^{k/r}$. On $V_j$ every internal edge reverses distance parity, since a failing edge gives an odd walk of length at most $2j+1$. Set $w(x)=(-1)^{\operatorname{dist}(1,x)}\mathbf1_{V_j}(x)$, zero also on other components. Translating by each $a\in A$ has correlation with $w$, divided by $|V_j|$, in $[-1,-1+\epsilon]$ where $\epsilon=(2r+1)^{k/r}-1$; only the points leaving the ball lose the minus sign. By Parseval the normalized squared Fourier coefficients of $w$ give a probability on $H$ with character means in this interval for every $a$.

For a quotient probability $\rho$, form the nonnegative trigonometric polynomial $P(h)=m\rho_h$ with constant coefficient one, other coefficients of modulus at most one and supported on $A$. Its value at the identity plus its expectation under the preceding probability is at most $2+k\epsilon$. Hence $M(L,A)\le2+k\epsilon$. Since $b/\sqrt n\le1/2+o(1)$, (1) contradicts the excess. The case $A=\varnothing$ gives $M=1$ directly.

## A bounded cyclic witness on the next interval

For fixed $\eta>0$ restrict further to
\[
                    (1/\sqrt5+\eta)\sqrt n\le b\le h_p/2.           \tag{3}
\]
Then $k\le3$ eventually by (2). The cyclic inverse-closed set is empty, a singleton involution, or has one inverse pair $a,a^{-1}$ and at most the unique involution $u$. The first two cases have $M\le2$. For the latter put $R=\operatorname{ord}(a)$. There is a character with $\operatorname{Re}h(a)\le-\cos(2\pi/R)$, and $h(u)=-1$ if $u$ occurs. On the cyclic subgroup generated by $a$, take the exponent nearest $R/2$, requiring it odd if $u=a^{R/2}$ occurs. Its distance from $R/2$ is at most one. An independent involution can be prescribed separately. Characters of a subgroup of a finite cyclic group extend to the full group. Now the average of $P(h)$ at this character and its inverse, added to $P(1)$, gives
\[
              M(L,A)\le 2+2(1-\cos(2\pi/R)).
\]
Thus $R$ is bounded in terms of $\delta$ if $e\to0$ and $\alpha\ge1+\delta$. All the allowed steps lie in a cyclic subgroup $L'\le L$ of order at most $2R$. Fourier polynomials supported on $L'$ depend only on the restriction of a character to $L'$, so $M(L,A)=M(L',A)$ exactly. Equation (1) and the converse lift show that this particular bounded LP already supplies a prime witness with normalized mark at least $1+\delta-o(1)$. The quotient graph in (3) is triangle-free by the lifted clique bound. An odd cycle of length at least five is compatible with the derived inequalities. Its occurrence on an unbounded prime sequence with the required ratio is unproved.

For example, an explicit arithmetic candidate uses only a 5-cycle. If $a$ has order five modulo $B$ and $B\setminus\{1\},aB,a^{-1}B$ all have the allowed sign, take the quotient polynomial
\[
 P(j)=1+\sec(\pi/5)\cos(2\pi j/5),\qquad j\in\mathbb Z/5 .
\]
Its minimum is zero, its mean is one, and its marked value is $1+\sec(\pi/5)=\sqrt5$. Pulling it back by restriction to the order-five subgroup and lifting the corresponding probability yields the full-field mark $b\sqrt{5/n}$. Therefore an unbounded prime sequence of these configurations with $b/\sqrt n\ge 1/\sqrt5+\eta$ for fixed $\eta>0$ would refute the conjectured limit. No assumption on any other coset or on the computed endpoint enters this implication.

## Exact endpoint and orbit checks

The root-time obstacle also has a direct fixed-point expression. For complementary optima $X,Y$ of sums $\sqrt n$, signs $\sigma,-\sigma$ and marks $\alpha,1/\alpha$, let $w=\sigma(X-Y)$. Then $w=K\Phi(w)$, $\Phi_0(w)=\sqrt{4+w_0^2}$, $\Phi_i(w)=|w_i|$ elsewhere. For the true zero-start iterate $v_s$, its exact distance decrement to $w$ is
\[
 \|v_s-w\|^2-\|v_{s+1}-w\|^2
 =4(g_s-1)^2+\big[(v_s(0)-w_0)^2-(\Phi_0(v_s)-\Phi_0(w))^2\big]
       +4\sum_{i\ne0}(-v_s(i)w_i)_+.
\]
This follows from $K^2=I-J$ and the coordinate squares. Every term is nonnegative. At each depth in the arithmetic window the bracket is $4(\alpha+\alpha^{-1}-2)+o(1)$ uniformly by the marked cancellation and bounded marks. Summing over a late interval supplies a lower bound on the distance decrease, hence another necessity for supercriticality. It gives no upper bound on the signed secant of the larger endpoint alone: subtracting the complementary contribution would discard a term of uncontrolled sign. The quotient argument instead uses the actual endpoint mark and its exterior mass. It still allows an unstructured high-collision endpoint.

The [192-bit checker](astra-secant-47-check.py) certifies every quotient coordinate reconstruction on four exact complementary endpoint pairs, including prime 37 with a genuine missing inverse pair of order nine and prime 41 with a missing involution. The field signs, degrees and orders use integer arithmetic. The endpoint supports are proposed numerically and certified by the round-45 anchored systems. The [records](astra-secant-47-checks.jsonl) certify marks above one at 37, 73 and 101. The mark interval at 41 contains one. Replay with `.venv/bin/python -B research/astra-secant-47-check.py`.

1. For the bounded quotients in (3), test all actual monochromatic $B$ with the requisite allowed fibers and use their exact $M(L',A)$. Prove $bM(L',A)/\sqrt n\le1+o(1)$ on every fixed-order pattern. A fixed positive excess through an unbounded sequence of primes gives actual feasible counterexamples by the converse lift, regardless of what the exterior of an optimum does.
2. For the general larger-side endpoint, estimate its signed late secant using both fixed-point occupations on one long interval. Precisely, seek $(\langle\sigma(X-j),v_t-v_s\rangle-(E_t-E_s)/4)/(t-s)\le o(1)$ for one interval with $t\asymp D(p)$ and $t-s\asymp D(p)$. A subsequence with positive liminf of the minimum over each fixed comparable-length window rules out that choice. The two-endpoint distance decrement alone controls neither of these signed one-endpoint terms.
