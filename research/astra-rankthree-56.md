# Full arithmetic collection at a rank-three Picard node

For every sufficiently large eligible prime or prime square the actual marked section extends across \(t=127/8\) to the rectangle
\[
     4063/256<\Re t<1017/64,\qquad |\Im t|<1/8192,
     \qquad |m_q(t)|\le 3/\sqrt n .
\]
It overlaps the [round-55 rectangle](astra-rankthree-55.md). At \(t=16251/1024\), exactly \(1/1024\) below the new left endpoint, the **fully signed arithmetic character collection at every node**, with the same two distinguished coefficients, has an escaping positive packet recursion. These are bounds at specific floors. Monotonicity in the floor, singularity of the actual branch and the all-prime theta limit remain unproved.

## An arithmetic expansion with a unique label

Use the actual scale \(s=2\sqrt{q/n}\), the seed \(S=s C_1\), the Legendre average \(Y\) and \(W=(\operatorname{tr}U+\operatorname{tr}U^*+\operatorname{tr}V+\operatorname{tr}V^*)/4\) from [round 55](astra-rankthree-55.md). Write the actual vector \(S+\alpha Y+\beta W+Z\). The rank-two factors \(A,B\) are copies of \(SL_2\). The full rank-three factors obey \(\det U=m^{-1},\det V=m\) over the ground field in both families. Their derived groups are independent of each other and of \(A,B\). The positive Jacobi and rank-three traces use the central translation of [round 32](joint-law-32.md), which respects tensor character identities pointwise.

For \(a,b\ge0\) use the rational \(GL_3\) irreducible \(R_{ab}\) of highest weight \((a,0,-b)\). Unique labels for the arithmetic irreducibles are
\[
 m^e R_{ab}(U)R_{cd}(V)\operatorname{Sym}^u A\operatorname{Sym}^v B .
\]
Restriction to the four derived factors determines all nonnegative indices. The remaining quotient torus determines \(e\). Tensoring \(R_{ab}\) with the standard changes its labels to
\[
 (a+1,b),\quad (a-1,b+1)\det,\quad (a,b-1).
\]
For the dual the changes are \((a,b+1),(a+1,b-1)\det^{-1},(a-1,b)\). Omit negative labels. These are the three row additions or removals from the highest weight, with its middle entry subtracted into the determinant. Thus the determinant increments the Jacobi exponent by its **negative** in the \(U\) slot and by its **positive** in the \(V\) slot. Iterating the four tensor choices gives the full integer multiplicity \(M_l(a,b,c,d,g)\) in \((4W)^l\). For instance the third power has two scalar copies at each of \(m,m^{-1}\), from the two compatible determinant lines in that direction.

At twist one use \((-1,-1,3)\) in \(U\), \((-1,0,0)\) in \(V\), and weight \(-1\) for \(m\). The weight multiset of \(R_{ab}\) at a triple \((x_1,x_2,x_3)\) comprises
\[
 i x_1 +(h+k-i)x_2+(a-b-h-k)x_3,\qquad
 0\le h\le a,\quad -b\le k\le0,\quad k\le i\le h .
\]
This follows from the \(GL_3\) Gelfand–Tsetlin branching pattern. The Legendre contribution is \((v+1)\sum_{i=0}^u\delta_{4i-2u}\). At twist \(\chi\) interchange both pairs of factors and negate the Jacobi weight. The symmetric coefficients and the involution \(U\leftrightarrow V,\ m\leftrightarrow m^{-1},\ A\leftrightarrow B\) equate the **summed** two twist costs. Duality also makes this common kernel symmetric about zero. The integer control reproduces the two twist histograms for \((4W)^l\) through \(l=8\).

Write \(d_{rk,uv}\) for the signed Legendre coefficients after translating the degree-28 activation by \(\alpha Y\) as in round 55, before distinguished subtractions. With \(c=c_{02}\), use \(\alpha_0=c+c_{22}c^2/2\), and choose \(\alpha=\alpha_0+\delta_a\), \(\beta=2d_{01,10}+\delta_b\). Both offsets vanish in the upper proof. At \(r=0\) first subtract \(\alpha C_2+\beta C_1Y\) in these coefficients. The two exact all-lift identities of round 55 turn these into the designated outputs up to \(O(n^{-1/2})\) in the first packet. Denote the resulting signed Jacobi-exponential coefficients by \(b_{r,f,uv}\). They equal the amended cosine coefficient at \(|f|\), divided by two at \(f\ne0\).

For residual arity \(j\), the signed coefficient at the displayed irreducible is
\[
 B_{j,e,a,b,c,d,u,v}=
 \sum_{l,g}\binom{j+l}{j}(\beta/4)^l
          M_l(a,b,c,d,g)\,b_{j+l,e-g,uv}.
\]
This formula also defines the infinite-degree root coefficients using the exact analytic activation with the finite distinguished subtractions. Multiply the modulus of each coefficient by its individual weight measure **after this sum**. Then convolve with the \(j\) independently lifted copies of the residual measure and apply the [packet projection](astra-feedback-52.md). This defines the full positive map tested below. Taking absolute values between successive activations drops trace identities involving the residual's descendants.

## One upper rectangle

On the slab intervals the [Arb checker](astra-rankthree-56-check.py) explicitly pools all contributions with \(j\le6,l\le4,u+v\le3,|f|\le7\) at degree at most 28. Every other term in that Taylor polynomial is charged with its positive character measure after Legendre collection. The complementary source set is disjoint. The triangle inequality makes this calculation an upper bound for the full root collection. Since \(s^2=8+4/n\), the interval \(\sqrt8\pm 10^{-12}\) contains every sufficiently large actual \(s\).

The 46-entry off-zero table and \(\eta=1/5\) use the [frozen zero argument](astra-signed-54.md#freezing-the-zero-weight) with symmetric excess norm \(\epsilon=2\cdot10^{-6}\). The core zero cap is \(\sum_{k\ge1}(k-1)h_k+\epsilon/\eta+10^{-8}\). The entire analytic Taylor tail is bounded using the positive dimension measure before any collection, at input hyperbolic-cosine norm
\[
 s\cosh\eta+|\alpha|(1+\cosh(2\eta))+
 |\beta|(1+3\cosh(\eta)/2+\cosh(3\eta)/2)+\|M\|_\eta+\epsilon ,
\]
where \(M\) is the core including its zero atom. On 40 subslabs the resulting joint envelope has off-zero excess norm below \(1.7\cdot10^{-6}\) and full dimension bound below \(4.66\). Strict slack absorbs the exact marked-only product and seed corrections as in [round 55](astra-rankthree-55.md). On the entire rectangle \(4.66/\sqrt{4(4063/256)-4.66^2}<3/4\), so the exact Picard iteration from the two distinguished seeds converges locally uniformly. Positivity on the real overlap identifies the actual branch, with the marked inverse hyperbolic sine bound as in the [positive-factor identification](marked-domain-53.md#from-scalar-slack-to-the-actual-holomorphic-section).

## Lower bounds for the fully collected map

For the lower test include **all** source Jacobi modes in the degree-28 polynomial for \(l\le L\), and all Legendre labels of degree at most four. Discarding higher Legendre labels loses only positive cost, since they cannot coincide with a retained label. Greater \(l\) can contribute to existing labels, even to the unit. For every arity and every individual boundary weight, debit the full positive cost of all \(l>L\) in the degree-28 polynomial at that weight, across every Legendre sector. This bounds the change by the reverse triangle inequality for each arithmetic coefficient, followed by its representation's nonnegative weight multiplicities. The remaining positive part is a genuine lower bound through degree 28.

For the infinite Taylor tail let \(K_0=s+2|\alpha|+3|\beta|\) and \(r=(K_0+R)^2/(4t)<1\). At arity \(j\) debit each individual weight by at most
\[
  R^{-j}\,2\sqrt t\,\left|\binom{1/2}{15}\right|r^{15}/(1-r).
\]
Indeed summing the changes of absolute coefficients with input dimension times \(R^j\) over all arities is bounded by the displayed ordinary Taylor tail before its \(R^{-j}\) factor. Arithmetic decomposition preserves this dimension. The checker minimizes the upper bound over a finite list of admissible positive \(R\) separately at each arity.

Retain arities through nine, boundary shifts through 18 and off-zero packets through 28. Iterating these lower kernels gives the following strict mass bounds. The offsets vary independently on the real intervals. The center of \(\beta\) uses the actual perturbed \(\alpha\).

| Real floor | Each offset bound | \(L\) | First certified height with mass \(>21\) |
|---|---:|---:|---:|
| \(16251/1024\) | zero | 5 | 2815 |
| \(1015/64\) | \(25/10^6\) | 4 | 373 |
| \(63/4\) | \(500/10^6\) | 4 | 149 |

Every case retains a zero-shift coefficient of arity two exceeding \(1/20\). The full projected measure of mass \(b\) has mean zero and first absolute moment \(b\). For two independent normalized draws, conditional Jensen gives expected absolute sum at least one. The next mass consequently exceeds \(b^2/20\). Monotonicity in the input measure now forces escape and excludes every finite-mass invariant majorizing the zero-start recursion. This tests the specified map with all arithmetic root collisions, even at arbitrarily high degree. Stronger propagation of signs through more than one node remains possible.

Replay from the workspace with the following command.

    .venv/bin/python -B research/astra-rankthree-56-check.py

All five [records](astra-rankthree-56-checks.jsonl) are exact integer controls or Arb192 certificates. The optional [floating table search](astra-rankthree-56-probe.py) supplies trial caps only.

## Ranked next tests

1. Extract the distinguished \(K(C_1 W)\) from the arithmetic rank-four constituents, using their determinant phases. Carry the signed \(m^e\) shifts through quadratic and exterior-power collisions. A common overlapping rectangle through \(16251/1024\) breaks the fully collected rank-three obstruction above. A lower escape for the exact new positive map at that same floor rules out that prescription.
2. Preserve signed identities through two adjacent activations, beginning with the full arity-one action \(K[H'_t(S+\alpha Y+\beta W)Kf]\) on the explicit arity-zero residual sources \(f\). Test whether strict interval slack below \(16251/1024\) persists after debiting every complementary term. Alternatively a truncated, reverse-triangle lower iteration of the two-step map passing a certified superlinear escape threshold excludes that two-step positive grouping.
