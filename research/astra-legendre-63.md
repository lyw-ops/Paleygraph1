# An exact mixed Legendre fifth center and its rank-24 dual return

For all sufficiently large eligible primes and prime squares, the actual physical marked section is holomorphic with \(|m_q(t)|\le 3/\sqrt n\), \(n=(q-1)/2\), on
\[
 1040021/65536<\Re t<1040023/65536,\qquad |\Im t|<2^{-20}.
\]
The interval \((1040022,1040023)/65536\) gives open overlap at the full previous imaginary width. At the proposed floor \(2031/128=1039872/65536\), the new fully collected single-vertex map escapes. Even after a non-Jacobi rank-24 dual pair is retained across adjacent vertices, its quadratic return is too small for the specified map. Both lower bounds exceed mass 21 at height 1246. These estimates leave the physical section at that floor open. [Previous rectangle and normalization](astra-primitive-62.md)

## Exact feedback at the marked frequency

Let \(N,N^\chi\) be the two perverse Legendre standards, \(M=N\star N^\chi\) and \(R=\mathcal T(M)\), with \(R\) also denoting its compact Mellin trace. The old coordinates \(A,B\) have the same Legendre sign, so their product is the Mellin product of \(N,N^\chi\). It is invariant under exchange of the two lifts of a square-subgroup character. The exact identity in the full physical frequency vector is \(K(AB)=R\).

Indeed, for \(\ell(a)=\chi(1-a)\), put \(n_q=\ell(\ell*\ell)\), with multiplicative cyclic convolution on the full group. The raw position row of \(AB\) is \((n_q*(\chi n_q))/q^2\). This is the middle-convolution compact row at all characters. At the two bad lifts the two factors have weight lists \((-2,2)\) and \((0,0)\), in opposite orders. The compact replacement \(\lambda\mapsto q^{-\max(w,0)}\lambda\) therefore distributes over every product of eigenvalues. At good lifts tensor multiplicativity applies directly. The row vanishes on nonsquares by interchange of the two factors. Multiplication by \(\ell\) on squares is the physical \(K\). The twist has zero middle-extension stalk at one because the incoming unipotent inertia becomes quadratic times unipotent. This proves the sign and gives zero exceptional-column coefficient here. For an integer check, splitting \(n_q\) into its even and odd exponent rows \(e,o\) gives numerator \((e*e)_j-(o*o)_{j-1}\) at exponent \(2j\), then multiplication by \(\ell(g^{2j})\) gives the new row. The checker evaluates these identities at seven field sizes including nonsquare primes and prime squares. [Compact trace of the mixed convolution](astra-rankeight-60.md#arithmetic-self-duality-and-its-sign) · [The operator on squares](weighted-arithmetic-57.md#exact-lift-feedback-and-compact-moments)

## The fifth distinguished coordinate

Take the four old coefficients of round 62 and \(V=sC_1+\alpha Y+\beta W+\gamma F_4+\delta G\). Write \(H_j=[y^j]\sqrt{4t+(V+y)^2}\) with the old subtractions at arity zero. Let \(c_{j,u,v}\) denote the selected old polynomial coefficient of \(\operatorname{Sym}^u A\,\operatorname{Sym}^v B\) at Jacobi exponent zero in the signed rank-three prefix of the degree-28 polynomial, at zero \(F_4,G\) degree. This includes every scalar tableau of \((4W)^h\) for \(0\le h\le4\). Explicitly, sum over its scalar determinant shifts \(e\) with multiplicity \(b_{h,e}\), taking the signed old Legendre/Chebyshev coefficient \(d_{j+h,|e|,u,v}\) with its usual arity-zero amendments. The summand is
\[
 b_{h,e}\binom{j+h}{j}(\beta/4)^h d_{j+h,|e|,u,v}/(1+\mathbf 1_{e\ne0}).
\]
Here \(|e|\le 7\) for every scalar in these four degrees. Fix the holomorphic coefficient \(z=c_{0,1,1}\) and add \(zR\) to the starting seed. This is a selected polynomial part of \([AB]H_0\). Its exact preactivation amendment is \(-zAB\). The untaken part of that same label remains charged. At the limiting real floor \(10^{12}z\in(1701367523,1701367524)\), while \(10^9[AB]H_0\in(1701364,1701365)\). [Old signed prefix](astra-rankfour-57.md#an-upper-bound-with-all-omitted-terms-charged)

At either twist the old \(AB\) measure is \(2\delta_{-2}+2\delta_2\). The output \(R\) has the same nonzero weights and four additional zero weights. Remove \(4|z|\) from old arity zero's combined second packet, using a lower endpoint for the deductible amount. For every new arity \(j\) translate the old unnormalized kernel \(U_{j+h}\) by \(\binom{j+h}j|z|^h D_R^{*h}\) for every \(0\le h\le28-j\). Here \(D_R=2\delta_{-2}+4\delta_0+2\delta_2\). The translated unary multiplier includes the entire old arithmetic kernel, including every non-Jacobi label. At arity zero further collect the two selected old coefficients on \(R(A+B)\). They are \(x=zc_{1,1,0}\) and \(y=3z^3c_{3,1,0}\), since \(R^3\) contains three copies of \(R\) and the three symplectic contractions have arithmetic phase one. Subtract
\[
 \frac{2(|x||y|-\Re(x\bar y))}{|x|+|y|+|x+y|}\ D_R*(\delta_{-2}+2\delta_0+\delta_2)
\]
using an interval lower endpoint. The denominator is positive on every slab. The remaining cubic constituents and every other Taylor term keep their full original charge.

The weighted input norm increases by \(|z|(4+4\cosh(2\eta))\) and the coordinate cap by \(8|z|\). Both increments are exactly four times the cost for an extra coefficient \(|z|\) in the old \(Y\) allocation. Sixteen closed slabs and fifty fixed rational caps give weighted excess below \(414\cdot10^{-9}\) with allowance \(6\cdot10^{-7}\) and full coordinate radius below \(4.654\). This includes the full degree-28 binomial remainder after inserting the new center. The inherited uniform first-packet bound absorbs the exceptional columns from the other terms and the physical mark. The full-disk bulk derivative is below \(3/4\), as is the mark derivative for large \(q\). The exact Picard limits therefore converge locally uniformly and give positive stationary factors on the real overlap. Uniqueness there identifies the holomorphic physical branch across the claimed rectangle. The caps were proposed numerically. Only their frozen values enter the interval proof. [Exact domain argument](marked-domain-53.md#from-scalar-slack-to-the-actual-holomorphic-section) · [Tail and full-coordinate check](astra-ranknext-58.md#certified-upper-rectangle)

## The non-Jacobi dual pair

Let \(U_A=\mathcal T(N\star R)\), \(U_B=\mathcal T(N^\chi\star R)\). Before activation these are independent-factor tensor irreducibles, with weight lists formed from \(D_R\) by adding \((-2,2)\) and \((0,0)\) respectively at the two twists. Their absolute sums are 32 and 16. Consequently each activated irreducible has dimension 24. The two input lists are exchanged by \(\chi\) and distinguish the inputs geometrically. Nonzero generic rank and twisting by an ordinary line followed by middle extension preserve simplicity and the distinction. Since \(R^\chi=R^\vee=R\), duality after the twist gives the arithmetic identity \(U_A^\vee=U_B\). Thus neither pure square contains a unit, and their product contains exactly one with arithmetic phase \(+1\). [Katz's boundary weights and independence](https://web.math.princeton.edu/~nmk/mellin331.pdf)

Write \(H'_j=[y^j]\sqrt{4t+(V+zR+y)^2}\), including all five amendments at \(j=0\). Put \(p=[RA]H'_0=[RB]H'_0\). The common Legendre trace sign can appear on both outputs and squares out. The two ordered cross contractions yield \(C=2p^2\). On the real floor the following strict enclosures include every old determinant shift and all Sp8 powers.

| Quantity | Lower endpoint | Upper endpoint | Scale |
|---|---:|---:|---:|
| \([A]H_1\) | 13978381702 | 13978384126 | \(10^{-12}\) |
| \([A]H_3\) | −76155083 | −76136703 | \(10^{-12}\) |
| \(p\) | 23782178 | 23782553 | \(10^{-12}\) |
| \([m^2]H'_0\) | 56169 | 56545 | \(10^{-12}\) |
| \([m^2]H'_2\) | −2548264 | −2548254 | \(10^{-9}\) |
| \(-2C[m^2]H'_2\) | 5765 | 5766 | \(10^{-15}\) |

For the extra factor use the symplectic minuscule tensor rule, adding or removing one box in a partition of length at most four. If \(\mu_h=[1]R^h\), its contribution to the projection on \(1\) is \(\mu_h\) and on \(R\) is \(\mu_{h+1}\). The signed tableau convolutions for the old factors are those of round 62. Schur orthogonality bounds the individual projection error by the uniform degree-24 binomial tail at total seed dimension including \(8|z|\). The positive direct \(m^2\) coefficient is larger than the magnitude of its negative binary return. The last table entry is the actual saving per Jacobi sign at the paired vertex. [Earlier signed projection](astra-primitive-62.md#the-signed-third-vertex-return)

## Full complementary debit and escape

For the obstruction take the old infinite, fully collected lower measures \(L_r\) on signed shifts through 24, built at arities through 12. Use the round-62 old upper polynomial rows and their analytic tails to bound \(U_r\). In the translated lower measure at arity \(j\), degrees \(h=0,1\) in \(R\) have distinct new labels. At \(h=2\) remove the single returning unit from the positive lower convolution and debit its old upper measure. At \(h=3\) do the same for the three returning copies of \(R\). The other cubic labels are the three partitions \((3),(2,1),(1,1,1)\) with multiplicities \(1,2,1\), all distinct from that linear label and from degree one and two. Each product with an old irreducible determines both irreducibles separately by independence. Thus all non-Jacobi linear interactions are retained, even after allowing all possible old arithmetic collisions. Explicitly the retained term at \(h\le3\) is
\[
 \binom{j+h}j z^h\{L_{j+h}*(D_R^{*h}-E_h)-U_{j+h}*E_h\},
 \qquad (E_0,E_1,E_2,E_3)=(0,0,\delta_0,3D_R).
\]
Subtract \(zD_{AB}\) at \(j=0\), allowing the original full old charge to diminish by its entire modulus. Every \(h\ge4\) costs the full upper measure and can cancel any retained label. The ten old trial radii already debit the old analytic tail in \(L_r\). For upper complements use the degree-28 tail \(E\) at old auxiliary radius two. Each old \(U_r\) has extra total mass at most \(E/2^r\). The polynomial part at \(h\ge4\) is debited through \(28-j\), and its analytic complement is bounded by
\[
 (E/2^j)\binom{j+4}j(4z)^4/[1-4z(1+j/5)].
\]
All denominators are positive. Per output bin use this entire tail, then take the positive part. Keeping final arities through nine, shifts through 18 and 28 packets gives the first escape at 1246. This single-vertex certificate allows every real \(z\) between the selected coefficient and the complete old \([AB]H_0\), including the exact full old subtraction at that floor.

For the paired test use the selected coefficient. Partition levels into disjoint pairs. At the second vertex pool the cross-unit of two distinguished \(U_A,U_B\) children with the original direct multiplier on each ordered list of residual siblings containing neither tag. This gives \(H'_r+\binom{r+2}r C H'_{r+2}\). All other tagged constituents, including products with at least three tags, retain their original charge. If the preceding lower measure is \(b\) and the exact tagged measure is \(T\), the true untagged measure dominates \((b-T)_+\). This surrogate together with the exact tag dominates \(b\), and its untagged part is bounded above by \(b\). After signed grouping each residual list has a fixed nonnegative convolution price. The resulting lower iteration therefore subtracts at most twice \(\binom{r+2}r C U'_{r+2}*b^{*r}\), once for the original unit and once for its direct competitor. The upper rows here use the recentered polynomial, its analytic tail at auxiliary radius two, and the largest polynomial atom off the signed strip times the total convolution mass. All higher residual counts have disjoint lists and nonnegative final output. This fully debited lower iteration also crosses 21 at height 1246.

The two transported tags together have mass \(48|p|<0.002\). After one full return debit the zero-shift atom at residual arity two remains greater than \(1/20\). Conditional Jensen for the two symmetric untagged negative inputs therefore bounds subsequent mass below by \((b_0-0.002)^2/20\) whenever full input mass \(b_0>21\), including on ordinary levels. The bound grows strictly above the diagonal throughout that range and its iterates diverge. This excludes a finite supersolution for both specified limiting maps.

Run `.venv/bin/python -B research/astra-legendre-63-check.py` from the repository root. The [checker](astra-legendre-63-check.py) produces [four records](astra-legendre-63-checks.jsonl).

1. Carry the whole signed \(R\) coefficient as a function of the older characters through consecutive updates. Resolve the arithmetic constituents shared by \(U_A\otimes U_B-1\) and the old derived factors, using both boundary lists. An actual overlapping invariant across \(2031/128\) passes. A fully debited higher-vertex lower escape with a surviving quadratic term rejects that specified rule. The direct fifth center and the single dual-pair return both fail this floor.
2. Recenter simultaneously on the other leading quadratic Legendre outputs \(\mathcal T(\operatorname{Sym}^2 N)\) and its dual together with \(R\), using independent coefficients fitted to their signed old residuals and exact compact lift corrections. An actual rectangle crossing the proposed floor passes. A certified escape after full one-vertex collection in the enlarged product group rejects those coefficients. The fifth-center upper test alone passes its smaller overlap.
