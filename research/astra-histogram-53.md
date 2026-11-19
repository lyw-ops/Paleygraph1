# A signed Mellin weight histogram and its escape threshold

For all eligible primes and prime squares, the actual real marked logarithm satisfies
\[
 \sup_{33/2\le t\le145/8}|m_q(t)|=O(n^{-1/18500}),\qquad n=(q-1)/2.
\]
The full positive tree majorant used in this proof diverges at \(t=127/8\), even at radius one. This gives a concrete obstruction to extending this particular proof by retaining more of the histogram. A separate positive trial through primes gives strict limiting bounds \(0.0169\) on \([15/2,63/8]\) and \(0.0222\) on \([7,15/2]\). The ordinary all-prime theta limit remains open.

## The exact positive recursion

Put \(Q_a=(\delta_a+\delta_{-a})/2+(a-1)\delta_0\), \(a\ge1\). Its mass, first absolute moment and second moment are \(a,a,a^2\). The geometric seed-mode measure before activation is \(C_k=(\delta_{-k}+\delta_k)/2\), including \(C_0=\delta_0\). Symmetry holds at every subsequent node by induction on the recursion, even when the boundary distributions for the individual Mellin characters differ. By the [two-character calculation](astra-feedback-52.md), a symmetric pre-activation distribution \(\nu\) is taken by the geometric part of \(K\) to
\[
  L\nu=\sum_{a\ge1}2\nu(a)Q_a .
\]
This positive linear formula retains the whole pooled distribution and the zero weight created at each output. The absolute Laurent coefficients of the activation yield the increasing map
\[
 \mathcal F(\mu)=\sum_{j,k}|c_{jk}|\rho^{k+1}
           L(C_k*\mu^{*j}).
\]
Starting at zero gives the positive tree majorant of bounded height. The convolution power at zero arity is the unit mass at zero.

Keep the coefficients of \(Q_1,\ldots,Q_{16}\) as a finite sum \(G\), and bound the mass and second moment of a remaining symmetric sum of packets \(E\) by \((u,v)\). The remainder includes **all descendants** in which a previously omitted packet was used, even when the output returns to a small weight. Every sum of packets, including this remainder, has mean zero and first absolute moment equal to mass.

Write \(b=\int1\,dG,c=\int w^2\,dG\). In a product of \(j\) inputs take the all-core part \(G^{*j}\) exactly. Its mass and second moment are \(B_j=b^j,D_j=jc b^{j-1}\), starting at \((1,0)\). For the product terms with at least one remainder let \(U_j,V_j\) bound mass and second moment, starting at \((0,0)\). Appending one input gives
\[
 U_{j+1}=U_j(b+u)+B_j u,\qquad
 V_{j+1}=V_j(b+u)+U_j(c+v)+D_j u+B_jv .
\]
For a seed mode \(k\) the second moment of these mixed terms is bounded by \(A=k^2U_j+V_j\), both before and after \(K\). Their output mass is bounded by the minimum of \((j+k)U_j,\sqrt{U_jA}\), and, for \(k>0\), \(kU_j+V_j/(4k)\). These bounds follow by applying the triangle inequality to each mixed product, Cauchy–Schwarz, and averaging over the two seed signs, respectively. Assign the entire mixed output to the remainder. For the all-core output, compute the finite convolution exactly, keep all packets up to 16, and send the mass and second moment of the larger packets to the remainder. All operations used as upper bounds are increasing in the nonnegative input packet coefficients and remainder budgets. In particular the zero weight in the core equals \(\sum_{a}(a-1)h_a\).

## The invariant and the genuine positive pair

For \(\rho=10003/10000\), a single vector of eighteen rational bounds is invariant on \([33/2,145/8]\). The [first replay record](astra-histogram-53-checks.jsonl) gives its sixteen packet coefficients and two remainder bounds in units of \(10^{-10}\). The total mass bound, which controls every correction coordinate, is exactly \(1.4609735201\); the second-moment bound is \(3.4698904366\). **Each** of the sixteen output coefficients and both output remainder bounds are strictly below \(999/1000\) of their respective input caps, uniformly on the closed interval.

The [Arb checker](astra-histogram-53-check.py) takes the coordinatewise maximum of the absolute degree-28 Laurent polynomial coefficients over rational floor slabs of width \(1/128\), using the round-51 uniform enclosure of the seed scale. It convolves the finite polynomials for these coefficients against the all-core powers. For all Taylor orders \(2\ell\ge30\) send the entire absolute expansion to the remainder. With \(B=b+u\), \(D=c+v\), \(r=(s\rho+B)^2/(4t)\), the mass and second moment for each such order are bounded respectively by
\[
 2\sqrt t\,\rho |{1/2\choose15}|r^\ell\,2\ell,\qquad
 2\sqrt t\,\rho |{1/2\choose15}|r^\ell(4\ell^2+2\ell D/B).
\]
The binomial magnitudes decrease, and the absolute cosine coefficients of a seed power sum to one. The second bound follows from \(k\le2\ell\), \(j\le2\ell\) and the product second moment. The checker sums both geometric tails. Splitting the Taylor expansion before the absolute values enlarges the bound if a high-order term contributes to an already retained Laurent mode.

Iteration bounds every coefficient tree at \(\rho\). To obtain actual vectors, use the [round-52 finite-degree correction argument](astra-feedback-52.md#exceptional-characters-and-positive-factors) with \(D_n=\lfloor\log_2(n)/8\rfloor\). The checker also verifies that the coarse tree cost at the auxiliary radius \(1/2\) is below the same total mass cap. Hence the exceptional-column contribution through \(D_n\), measured at \(\rho\), is \(o(1)\). With the exact polynomials of that argument, \(KU=V-S\), \(\|V\|_\infty\le s+1.461+o(1)\), and \(\|U-H_t(V)\|_\infty=O(\rho^{-D_n})\). Set \(u_0=2\), \(u_i=U_i/\sqrt n\) elsewhere and \(v=Ku\). Since \(2\sqrt{33/2}>s+1.461\) eventually, both actual sector factors \((u\pm v)/2\) are strictly positive. The marked logarithm of the trial is \(O(n^{-1/2})\), and square-root weight comparison transfers the scaled bulk error to the actual mark. Finally \(\rho^{18500}>256\). This real proof uses the coarse correction route independently of any stronger complex-neighborhood result.

## Lower escape bound for the full positive map

At \(t=127/8,\rho=1\), discard every output packet above 16 and all omitted Laurent modes to get a lower iteration. For each retained mode subtract from the absolute degree-28 polynomial coefficient the rigorous error
\[
 2^{-j}\,2\sqrt t\,r_2^{15}/(1-r_2),\qquad r_2=(s+2)^2/(4t),
\]
taking the positive part. Indeed the sum of the omitted Laurent coefficients in absolute value, weighted by \(2^j\), is bounded by the geometric tail before combining signs. The fourth replay record checks that the retained mass exceeds \(21\) at height 164, and that \(|c_{20}|>1/20\). These are lower interval checks with downward-rounded packet coefficients at each height. They apply also to the limiting seed scale.

For any symmetric sum of packets of mass \(B>0\), normalize to the law of \(X\). Then \(\mathbb E|X|=1\), \(\mathbb E X=0\), and for an independent copy \(Y\), Jensen conditioning on \(X\) gives \(\mathbb E|X+Y|\ge1\). The quadratic \((j,k)=(2,0)\) term alone therefore contributes at least \(|c_{20}|B^2\) to the mass of the next **full** iterate. Starting above 21 implies divergence. This rules out every finite-total-mass positive histogram supersolution for these absolute tree coefficients at this floor. It leaves open cancellation of coefficients attached to the same vector and alternative positive trial constructions.

## Four positive updates with a centered polynomial

For these prime trials use the degree-16 polynomial
\[
 P_t(x)=\sqrt{4t+12}\sum_{\ell=0}^8{1/2\choose\ell}
               \left(\frac{x^2-12}{4t+12}\right)^\ell .
\]
The centering reduces the maximum magnitude of the Taylor variable on the input intervals. When \(|x|\le B\), use
\[
 r=\max(12,|B^2-12|)/(4t+12),\qquad
 e(B)=\sqrt{4t+12}|{1/2\choose9}|r^9/(1-r).
\]
The verifier checks \(r<1\) at each of the four inputs. Constant terms can be dropped from the coefficient accounting because \(K\) kills constants. The trial itself uses the entire displayed polynomial, including its constant term.

There is no need to run a second histogram recursion for differences. On each parameter slab choose a common pointwise upper envelope of absolute Laurent coefficients. For its **exact** positive map let \(M_i\) be the cumulative measure of the trees through height \(i\). Telescoping products, as in the [prime increment proof](prime-increments-52.md), bound \(R_i-R_{i-1}\) by the mass of the sum of trees of height exactly \(i\), namely \(M_i-M_{i-1}\). This is because a truncated Picard update expands in the same trees at both heights with identical coefficients for all shared trees. The retained core of the previous row, computed with the same coefficient envelope, is a lower submeasure of \(M_{i-1}\). Consequently the new upper total mass minus the previous **core** mass bounds the difference. Subtracting the previous upper remainder could give an unjustified improvement. The core arithmetic in the checker encloses those exact retained coefficients; the remainder budgets have no influence on the computed all-core part.

Apply the [tilted prime second-increment estimate and weight transfer](prime-increments-52.md) to this polynomial, with \(e(B)\) above at each step. The proof there uses the cosine coefficients for its first increment and the quadratic-tilt moments for its second, and applies unchanged to any fixed even polynomial with the stated uniform activation error. The next two increments use the Lipschitz bound for the true activation on the corresponding coordinate intervals. The difference-of-squares estimate controls the positive bulk product of the genuine trial \((u\pm Ku)/2\) with \(U=P_t(V_3)\). The second and third records cover the following closed intervals by rational floor slabs of width \(1/256\). Product bounds apply to \(n\) times the bulk product after normalization at the mark, in the uniform liminf, and mark bounds apply to the actual stationary marked scalar in the uniform limsup.

| Floor interval | Lower bulk product | Upper absolute mark |
|---|---:|---:|
| \([15/2,63/8]\) | \(4.7\) | \(0.0169\) |
| \([7,15/2]\) | \(3.3\) | \(0.0222\) |

## Ranked tests

1. To cross \(127/8\), combine signed contributions to the *same* geometric trace object before taking their absolute values. Retain at least the repeated quadratic feedback shapes. A lower positive iterate crossing the reciprocal of a surviving self-quadratic coefficient, with a justified Jensen lower mass bound for that grouped recursion, refutes the proposed grouped invariant.
2. At \(t=7\), bound the third normalized Euclidean increment using its correlation with the Jacobi seed and the first projected polynomial field. Positivity already has a strict uniform margin. A positive-pair transfer below 0.0169 would extend the tighter tolerance. A rigorous lower bound on that proposed increment exceeding its allotted value rejects the incremental estimate; the failure of an upper certificate alone does not reject the actual predictor.
