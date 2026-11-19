# A uniform signed bound on the near-unit frequencies of the marked cubic

At every sufficiently large eligible prime, delete the positional output frequencies where either genuine optimal row has Fourier coefficient of absolute value above \(1-\epsilon\). Their contribution to the scaled marked cubic of round 84 is \(O(\sqrt\epsilon)\), uniformly in the optimum and the prime. This includes negative coefficients in ordinary theta. On a fixed larger-side gap the primary near-unit set has at most half the prime Paley clique bound. Neither estimate controls the rest of the marked cubic.

## Resolve the cubic by its output character

Write \(n=(p-1)/2\), \(Q=\mathbb F_p^{\times2}\), \(G=\widehat Q\), \(d(x)=\chi(1-x)\), \(k(i)=p^{-1/2}\sum_{x\in Q}d(x)i(x)\), and \(E=n^{-1}\sum_{i\in G}\). Take any two complementary optimal probabilities \(q,r\), with signs \(s,-s\), marks \(a,b\), and \(nab=1\). Their characteristic functions \(F(x)=\sum_i q_i i(x)\) and \(R(x)=\sum_i r_i i(x)\) are supported off the identity on \(d=s,-s\) respectively. The two functions may be complex for a noneven row. Optimality gives \(q_i r_i=0\) at all exterior sites. Both normalized marks are bounded above and bounded away from zero. Put \(U=(nq-1)/\sqrt p\), \(V=(nr-1)/\sqrt p\). [Marked identities and endpoint caps](astra-complement-84.md)

For every inversion-stable \(T\subset Q\setminus\{1\}\), form the actual partial Jacobi column \(k_T(i)=p^{-1/2}\sum_{x\in T} d(x)i(x)\). The exact identity for the chosen mark is
\[
 pE(k_T UV)=\frac1{\sqrt p}\sum_{x\in T}d(x)[1-F(x)-R(x)].                 \tag{1}
\]
Indeed the ordinary transform of \(pUV/n\) away from the identity is \(1-F-R\), by expanding the product and using \(nq_i r_i=\mathbf1_{i=0}\). Equivalently, (1) is the weighted arithmetic cubic with first factor \(k_T\) and the other two full Jacobi columns centered at the independently drawn \(i\sim q,j\sim r\), with the overall minus sign from the opposite sectors. Summing over all \(x\ne1\) recovers (7) of round 84. The 1 in the bracket is required for a partial output mask.

## Word products, prime cliques and concentration away from the mark

Let \(w\) be either endpoint, \(W\) its characteristic function, and
\[
 A=A_w(\epsilon)=\{x\in Q:|W(x)|>1-\epsilon\},\qquad
 h=\left\lfloor(1+\sqrt{1+4n})/2\right\rfloor .
\]
The set includes the identity. For each \(x\in A\), the random character \(i(x)\) has \(L^2(w)\) distance less than \(\sqrt{2\epsilon}\) from \(W(x)/|W(x)|\). A product of \(j\) such phases or their conjugates has distance at most \(j\sqrt{2\epsilon}\) from the corresponding product of unit phases, by telescoping unit complex numbers. In particular every \(x\in A^k\) has \(|W(x)|\ge1-k^2\epsilon\). Every quotient of two elements of \(A^k\) has nonzero transform if \(4k^2\epsilon<1\). All distinct differences of field elements of \(A^k\) then have the same quadratic sign, since the elements are squares and the characteristic function vanishes on the forbidden sector. A nonsquare dilation handles the negative sign. Hence \(|A^k|\le h\). [Hanson–Petridis, Theorem 1.2](https://arxiv.org/abs/1905.09134)

Let \(B=\operatorname{stab}(A^k)\) under multiplication, and let \(l\) be the number of its cosets met by \(A\). The bound \(|A^k|\ge[k(l-1)+1]|B|\) follows by applying Kneser's theorem in \(Q/B\). Every prefix product in this quotient has trivial stabilizer, since any period persists through the remaining product. If \(l\ge2\), this gives \(|A^k|\ge k|A|/2\). Thus \(|A|>2h/k\) forces \(A^k=B\), since \(1\in A\). At \(k=3\) the sharper \(3l-2\ge2l\) shows that \(|A|>h/2\) already forces \(A^3=B\). [Kneser's addition theorem](https://arxiv.org/abs/1303.3539)

For \(A^k=B\), Parseval on \(B\) gives
\[
 \sum_{L\in G/B^\perp} w(L)^2=|B|^{-1}\sum_{x\in B}|W(x)|^2
 \ge (1-k^2\epsilon)^2 .
\]
Consequently some coset \(L\) has exterior mass \(e=1-w(L)\le2k^2\epsilon\). The distinguished mark locates this coset. If \(L\ne B^\perp\), its restriction character \(\phi\in\widehat B\) is nontrivial. Choose \(u\in B\) with \(|1-\phi(u)|\ge1\), and put \(z_i=(i(u)-\phi(u))w_i\). Then \(|z_0|\ge w_0\), \(\sum |z_i|\le2e\), and its transform vanishes on \(D_u=\{x:d(x)=d(ux)=-\operatorname{signsector}(w)\}\). Here \(u\ne1\). Expanding the two sign indicators, with at most two exceptional positions, gives
\[
 |D_u|\ge n/4-\sqrt p-2,\qquad
 \max_{i\ne0}\left|\sum_{x\in D_u}i(x)\right|\le\sqrt p+2 .
\]
The two single-shift terms cost at most \(\sqrt p\) each and the double-shift term costs at most \(2\sqrt p\), before division by four. Summing the zero transform of \(z\) over \(D_u\) yields
\[
     w_0(n/4-\sqrt p-2)\le 2e(\sqrt p+2).                         \tag{2}
\]
In particular \(e>1/100\) for all sufficiently large primes if \(\sqrt n w_0\ge1/2\), as holds for both actual endpoints. This tests an arbitrary nonmarked coset, including one of order two in the quotient. [Uniform twisted translate bounds](parallel-torus-8.md#a-uniform-bound-for-twisted-translate-correlations)

Take \(k=\lfloor1/(20\sqrt\epsilon)\rfloor\) for \(0<\epsilon\le1/6400\). In the subgroup case, \(e\le1/200\), so (2) forces \(L=B^\perp\). Then \(\Re W(x)\ge 1-2e>0\) throughout \(B\). Moreover the character variance gives
\[
 (1-e)|1-W(x)|^2\le\sum_i w_i|i(x)-W(x)|^2=1-|W(x)|^2<2\epsilon
 \quad(x\in A).
\]
The mass on \(B^\perp\) supplies the left side. Hence on a large set \(A\), every selected coefficient is within \(2\sqrt\epsilon\) of the number one even when the optimal row is noneven. In particular, **if even one near-unit coefficient has nonpositive real part, the entire absolute near-unit set has size at most \(2h/k\le80h\sqrt\epsilon\)**. In all cases \(|A|\le h\).

Apply (1) to the union \(T=(A_q(\epsilon)\cup A_r(\epsilon))\setminus\{1\}\). For each endpoint, a set larger than \(2h/k\) costs at most \(2\sqrt\epsilon h/\sqrt p\) by the variance estimate. A smaller set costs at most \(4h/(k\sqrt p)\) by \(|1-W|\le2\). The two sector supports are disjoint outside the identity, so
\[
             |pE(k_T UV)|\le320\sqrt\epsilon\,h/\sqrt p .   \tag{3}
\]
The bound holds for *every subset* of these frequencies as well, with conjugate pairing when a real test is desired. It proves cancellation between the mark and the appropriate one-law price on a large absolute near-unit set and controls the number of the remaining near-unit modes by prime geometry. The complementary test \(k-k_T\) has sup norm \(\le 1+2h/\sqrt p\). For any \(\epsilon(p)\downarrow0\) it carries the entire original scaled cubic up to \(o(1)\) at the prescribed mark. The removed part is bounded in absolute total contribution after the output fibers are summed individually.

## Half the clique cap on a supercritical face

Suppose \(\gamma=\sqrt n a\ge1+\delta\). The [marked subgroup mass gap](astra-face-46.md#the-marked-subgroup-and-a-reciprocal-forbidden-count-test) gives \(1-q(B^\perp)\ge c_\delta>0\) whenever \(|B|>h/2\), uniformly at sufficiently large primes. Fix \(\epsilon_\delta>0\) so small that \(36\epsilon_\delta<1\) and \(18\epsilon_\delta<\min(c_\delta,1/100)\). If \(|A_q(\epsilon_\delta)|>h/2\), the three-fold product is one subgroup \(B\) of size above \(h/2\). Its concentration satisfies \(e\le18\epsilon_\delta\), and (2) places it in the marked coset, contradicting the mass gap. Therefore
\[
 |A_q(\epsilon_\delta)|\le h/2,\qquad
 \sum_{x\notin A_q(\epsilon_\delta)} F(x)\ge \gamma\sqrt n-h/2.     \tag{4}
\]
The second assertion is signed and keeps the full contribution from ordinary-theta negative coefficients.

For every integer \(m\ge2\), physical convolution smoothing now gives
\[
 \sqrt n(q^{*m})_0\le\frac{h}{2\sqrt n}
                  +\gamma(1-\epsilon_\delta)^{m-2}.                    \tag{5}
\]
Use \(n(q^{*m})_0=\sum F(x)^m\le\sum|F(x)|^m\) and \(\sum |F|^2=n\sum q_i^2\le na\) by the optimal point cap. In particular this includes even powers. Although \(q^{*m}\) can cease to be optimal, it is a true primary probability with the exact opposite displacement law. The aligned law \(n(q^{*m})_i r_i\) therefore gives at least \(1-h/(2\gamma\sqrt n)-(1-\epsilon_\delta)^{m-2}\) of its total mass to nonroot sites. At \(m=1\) all its mass was at the root.

On the [relative-density-one set of primes avoiding critical divisors](coset-progression-gap.md#removing-the-exception-on-density-one-primes), for every \(\eta>0\) choose a fixed \(k>4/\eta\) and \(\epsilon<1/(4k^2)\). Then either endpoint has \(|A_w(\epsilon)|\le\eta\sqrt n\) eventually. Otherwise \(A_w^k=B\) gives a divisor of \(n\) between \(\eta\sqrt n\) and \(h\). This variant applies to every sector probability irrespective of mark. For the optima it gives \(\lim_{m\to\infty}\limsup_p\sqrt n(w^{*m})_0=0\) along that prime set, by the same collision bound. This argument does not assert density-one convergence of theta.

## Exact cancellation of the displacement average in the distinct-center sum

Put \(C(i,j)=E_z k(z)k(z-i)k(z-j)\), \(A(t)=E_z k(z)^2 k(z-t)\) in this paragraph only, and write
\[
 B_0=s\sqrt p(a\Delta_r-b\Delta_q)+pab A(0),
 \qquad \Delta_w=w(k^2)-Ek^2 .
\]
For \(t\ne0\), the uniform mean of \(C(i,i+t)\) over \(i\notin\{0,-t\}\) is \(-2A(t)/(n-2)\). Indeed the unrestricted sum vanishes by \(Ek=0\), and both excluded values equal \(A(t)\) by inversion. The true exterior displacement masses are \(d_t=1/n-a r_t-b q_{-t}+ab\mathbf1_{t=0}\), with \(d_0=0\). Thus the contribution of this conditional uniform mean to the *scaled* true exterior sum is exactly
\[
 p\sum_{t\ne0}d_t\frac{-2A(t)}{n-2}
             =-\frac{2B_0}{n-2}=O(p^{-1}).                           \tag{6}
\]
Here \(\sum A(t)=0\), \(q(A)=s\Delta_q/\sqrt p\), and \(r(A)=-s\Delta_r/\sqrt p\) follow from the sector equations. Subtraction leaves the exact identity
\[
 pE(kUV)=\frac n{n-2}B_0
   -p\sum_{i,j\ne0,\ i\ne j}q_i r_j
      \left[C(i,j)+\frac{2A(j-i)}{n-2}\right].
\]
The bracket has zero sum on each individual distinct-center displacement fiber. The uniform displacement budget alone misses its signed correlation with the actual within-fiber weights.

The [384-bit checker](astra-cubic-85-check.py) reconstructs complementary optima at \(53,101,257,409,769\). It checks the individual output identity at all 787 nonidentity modes across those primes, every displacement mean by arithmetic convolution, and (6). It also verifies the annihilated transform and (2) on 82 off-mark cosets across the two signs. At \(p=257\) the absolute threshold \(1/20\) selects 115 modes, including three negative ones, with scaled marked contribution between 0.036492133 and 0.036492134. The seventh-power aligned root probability lies between 0.050366061 and 0.050366062 at \(p=769\). These finite cutoffs test the identities. [Outward interval records](astra-cubic-85-checks.jsonl)

1. On one fixed-gap primary face, combine the signed mass below the fixed cutoff in (4) with the opposite face's output sum (1). A bound on their *difference* must retain the deterministic partial root term on the same mask. Absolute control of the near-unit outputs is already supplied by (3).
2. Estimate the correlation of the centered bracket in (6) with \(q_i r_{i+t}\) after conditioning on \(t\). The required comparison is with \(nB_0/(n-2)\) at additive error \(o(1)\), which would settle the original conjecture.
