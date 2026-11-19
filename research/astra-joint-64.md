# Joint symmetric-square and mixed Legendre centers

For every sufficiently large eligible prime and prime square, the physical stationary section exists and satisfies \(|m_q(t)|\le 3/\sqrt n\) on
\[
 1040019/65536<\Re t<1040022/65536,\qquad |\Im t|<2^{-20},\qquad n=(q-1)/2.
\]
The overlap with round 63 is \((1040021,1040022)/65536\) at the full imaginary width. At the separate test point \(2031/128\) the limiting, fully collected one-vertex prescription with the specific new coefficients below exceeds mass 21 by height 1329 and diverges. Actual continuation there is open. [Round 63](astra-legendre-63.md)

## Exact physical feedback on both lifts

Write \(A,B\) for the two signed Legendre traces, \(S_A=A^2-1,S_B=B^2-1\) for their pointwise Chebyshev polynomials, and \(D=\mathcal T(\operatorname{Sym}^2_\star N)\). Its quadratic twist is its arithmetic dual \(D^\vee\). On the entire square-subgroup frequency vector,
\[
 K(S_A+S_B)=D+D^\vee-\frac{4n(q+1)}{q^2}K e_0.
\]
Indeed, write \(u=\ell(\ell*\ell)\) on the cyclic full group, with \(\ell(a)=\chi(1-a)\). The numerator of the raw square of the first trace less the punctual unit is \(u*u-q^2\delta_1\), with denominator \(q^2\). At the trivial character its value after division is \(4q^{-2}-1\), whereas the compact trace of the symmetric square is \(1+2q^{-2}\). The remaining lifts agree. The discrepancy \(2-2q^{-2}\) inverts to the constant row \(2(q+1)/q^2\). After multiplying by \(\ell\), the zero at one kills the punctual term and the output has zero intermediate-extension stalk there. The second lift is the same computation multiplied by \(\chi(a)\). The two terms on squares add, and \(\ell|_Q/n\) is the positional row of \(Ke_0\). This gives the sign and coefficient above. The correction is bounded independently of \(q\) and enters the previously controlled exceptional first packet. Seven finite group rings verify the subtraction at every square position, including the identity. The existing identity \(K(AB)=R\) has zero exceptional coefficient. [Boundary and determinant calculation](two-node-groups-59.md) · [Exceptional mark argument](marked-domain-53.md)

## Choice of centers and the signed arithmetic return

Keep \(zR\) and the four older inputs from round 63. Denote by \(c_{j,u,v}\) its older degree-28, zero-Jacobi, four-step rank-three scalar prefix, before any \(R\) input. Take the two selected coefficients \(w_A=c_{0,2,0}\), \(w_B=c_{0,0,2}\). They agree identically by exchanging the two Legendre factors in each Chebyshev coefficient. Write \(w\) for their value, \(Q=D+D^\vee\), and append \(wQ\) to the seed. Subtract \(w(S_A+S_B)\) at the root and use the exact exceptional correction above. At \(s=\sqrt8,t=2031/128\), \(10^{12}w\) lies between 850649424 and 850649425. This is a selected polynomial coefficient. All complementary terms on the same two labels are retained. [Definition of the selected prefix](astra-legendre-63.md#the-fifth-distinguished-coordinate)

The two boundary lists of \(D\) are \((-4,0,0,0)\) and \((0,0,0,4)\), exchanged for its dual. The measures of the two incoming polynomials at either twist are \(D_Q=\delta_{-4}+6\delta_0+\delta_4\) and \(D_S=\delta_{-4}+4\delta_0+\delta_4\). The new \(SL_4\) is independent of the old derived group and \(Sp_8\). In \(Q^2\) the two ordered unit contractions have phase +1. The old part of \(Q^4\) consists of twelve unshifted units and the two lines \(m^{\pm4}\), each once with phase +1, by the arithmetic determinant. At cubic degree the six zero-determinant returns onto each of \(D,D^\vee\) come from three orderings and two contractions. Another return from three copies of the opposite standard has nonzero determinant shift and retains its charge in the upper estimate. [Arithmetic special linear factor](two-node-groups-59.md) · [Independent mixed factor](astra-rankeight-60.md)

Let \(H^{(5)}_j,H^{(7)}_j\) be the analytic root arities before and after adding the pair, with each profile's own root amendments. The following intervals hold at the limiting real floor.

| Signed quantity | Strict bounds after multiplication by \(10^{12}\) |
| --- | --- |
| \([m^2]H^{(5)}_0\) | \((56349,56365)\) |
| \(2w^2[m^2]H^{(5)}_2\) | \((-3688,-3687)\) |
| \([m^2]H^{(7)}_0\) | \((52661,52678)\) |
| \([\operatorname{Sym}^2 A]H^{(7)}_0\), also for \(B\) | \((-1506,-1489)\) |

For the projections, include the scalar multiplicities of every power of \(Q\) up to 28 with its arithmetic determinant exponents. Multiply their exponential generating table with the old independent derived-factor tables and the zero-partition moments of \(Sp_8\). For each chosen Legendre label retain its actual multiplicity. For mass bound \(M\) of all selected seeds and arity \(j\), the first omitted term bounds the uniform error after multiplication by \((1-(M^2/(4t)){32\choose j}/{30\choose j})^{-1}\). This follows by bounding the ratio of successive absolute binomial coefficients and using the decreasing arity ratio. Character orthogonality bounds the error in each projected coefficient by that uniform error. Thus the complete Jacobi coefficient has the stated decrease even allowing all fourth and higher determinant shifts. It stays positive at the test point, and the residual on the two subtracted symmetric squares is negative.

## Upper majorant and the physical overlap

Enlarge the old explicit rank-three prefix of the four-center *upper bound* to \(L=4,A=5,E=9,J=8\) and extract its scalar Jacobi shifts through 5. Keep the exact coefficient formulas of round 62, including the fraction \(499/500\) for the rank-four input. Every term outside this prefix is still charged in the complementary polynomial. Translate by \(R\) as in round 63. The two older selected symmetric squares are still separate labels of the zero-\(R\) and zero-higher-rank terms. Remove \(|w|D_S\) at arity zero. Translate all five-center polynomial kernels by \({j+h\choose j}|w|^h D_Q^{*h}\) for \(j+h\le28\). The upper sum includes the complete previous arithmetic unary kernel. [Prefix and complement](astra-rankfour-57.md) · [Four-center translation](astra-ranknext-58.md)

At the last root, collect the selected linear and cubic coefficients on \(Q(A+B)\). They are
\[
 x=wc_{1,1,0},\qquad y=(6w^3+3z^2w)c_{3,1,0}.
\]
The second summand uses the three orderings of \(R^2Q\) and the phase-one symplectic unit. The six cubic contractions above give the first summand. The corresponding coefficients on \(B\) agree. Deduct a lower endpoint for \(2(|x||y|-\Re(x\bar y))/(|x|+|y|+|x+y|)\) times \(D_Q*(\delta_{-2}+2\delta_0+\delta_2)\). Terms on determinant-shifted cubic labels, every other old label, and higher arities keep their original charge. The denominator is positive on the proved slabs.

In the weighted residual norm \(\sum_k h_k\cosh(k/5)\), a packet of index \(k\ge1\) contributes \((k-1)h_k\) to weight zero. Use \(k-1\le (14/5)\cosh(k/5)\). This is checked through ten and follows thereafter by convexity and the derivative at ten. The residual allowance \(3\cdot10^{-7}\) therefore costs at most \((14/5)(3\cdot10^{-7})\) at weight zero. Use the exact additional weighted seed norm \(|w|(6+2\cosh(4/5))\) in the degree-28 tail, and add \(8|w|\) to the coordinate cap. The checker covers 24 closed slabs and recomputes the positive core and all descendants of the weighted remainder. The excess including the entire Taylor tail is below \(207\cdot10^{-9}\). The full coordinate radius is below 4.654 and its full-disk bulk derivative bound is below \(3/4\). As in round 53, the uniform exceptional first packet fits in the slack for large fields, the mark derivative is also below \(3/4\), and exact Picard iteration converges locally uniformly. For positive real floors the stationary factors at the limit are positive, so uniqueness identifies the physical branch on the real overlap and holomorphy extends the identification. [Arity-wise upper invariant](astra-ranknext-58.md) · [True Picard iteration and mark](marked-domain-53.md#from-scalar-slack-to-the-actual-holomorphic-section)

## Fully collected lower test at the proposed floor

Use the limiting real profile above and collect every arithmetic label at a single root before taking absolute values. Residual sibling trees are charged independently across different vertices. Let \(L_j,U_j\) be the previous five-center lower and upper measures. Their lower estimate already allows arbitrary collisions on old arithmetic labels. Retain the linear \(Q\) term and, at quadratic degree, the two symmetric squares of \(D,D^\vee\) and the two copies of the adjoint. These have new derived labels distinct from all old and linear ones. Each label has a unique determinant shift, and the two adjoints have the same shift. The two exterior squares share their derived label with differing determinant shifts. To allow arbitrary old collisions, omit and debit both, as well as both unit copies. Their combined boundary polynomial is \(E=3\delta_{-4}+8\delta_0+3\delta_4\). Indeed \(\bigwedge^2 D\) has three weights \(-4\) and three zeros on the first twist. In each arity \(j\) the quadratic lower contribution is
\[
 {j+2\choose j}w^2\{L_{j+2}*(D_Q^{*2}-E)-U_{j+2}*E\}.
\]
The degree-zero and linear terms have their full old lower measures. At the root debit \(|w|D_S\) for the selected subtractions. Every degree \(h\ge3\) pays its entire upper charge. With \(E_0\) the previous five-center degree-28 tail at auxiliary radius two and \(b=8|w|\), the high-degree *analytic* part of this debit in each signed bin is at most
\[
 (E_0/2^j){j+3\choose j}(b/2)^3/[1-(b/2)(1+j/4)].
\]
Also charge \(14{j+2\choose j}|w|^2E_0/2^{j+2}\) on the possible returning quadratic terms. The polynomial complementary debit uses every \(h\) through \(28-j\). After all subtractions take the positive part, restrict to arity nine and signed shifts through 18, and retain 28 positive packets. The required previous lower source widths extend to 26 and arities to eleven. This computation remains valid if still more equal labels within a single vertex are identified.

Downward rounding gives mass above 21 by height 1329. The fully debited zero-shift atom at arity two is greater than \(1/20\). A symmetric packet distribution normalized by its full mass has mean zero and first absolute moment one. Conditional Jensen for two independent draws therefore gives next mass at least the square of the full mass divided by 20. Above 21 this bound diverges on iteration. This excludes a finite supersolution for this one-vertex limiting prescription. The cross-vertex signed dynamics and the physical section at \(2031/128\) are not bounded below by this escape. [Previous lower measures and their analytic tails](astra-legendre-63.md#full-complementary-debit-and-escape)

The [checker](astra-joint-64-check.py) emits [four proof records](astra-joint-64-checks.jsonl) with integer or Arb192 arithmetic. The [optional cap fit](astra-joint-64-probe.py) supplies only the frozen caps. Reproduce from the repository root with `.venv/bin/python -B research/astra-joint-64-check.py`.

1. Carry the **two signed quadratic Legendre coefficients as functions of the older Jacobi and Legendre labels**, including the determinant-shifted cubic return from three opposite standards, on two consecutive vertices. Require an actual overlapping invariant across \(2031/128\), or a complete complementary debit with a surviving growth term to exclude that two-vertex prescription there.
2. Recenter jointly on the two independent symplectic outputs of the older \(m^{\pm4}\) residual as well as the three Legendre quadratic outputs. Include the compact bad-lift correction and the mixed signed coefficients. An overlapping physical crossing passes. A fully debited one-vertex escape with a surviving quadratic term rejects the tested profile.
