# Exact complex continuation from one exceptional Jacobi coordinate

There is a common complex domain for the actual marked Paley branch through all sufficiently large eligible primes and prime squares. It contains
\[
 \begin{split}
 \mathcal D_{\rm explicit}={}&
 \{\,\Re t>0,\ 22<|t|<2048\,\}\\
 &{}\cup\{\,2319/128<\Re t<23,\ |\Im t|<1/4\,\}\\
 &{}\cup\{\,527/32<\Re t<145/8,\ |\Im t|<1/32\,\}.
 \end{split}
\]
The bound \(|m_q(t)|\le3/\sqrt n\), \(n=(q-1)/2\), holds throughout the union once \(q\) is sufficiently large. The exact stationary factors also continue on this domain. The argument does not yield a common domain near \(t=1/2\).

## The exceptional character stays at the mark

Keep the [round-52 two-character category and pooled weight measure](astra-feedback-52.md). Let \(L\) be the rank-one Jacobi object and \(x=\sqrt n K e_0\). Its two-lift field is \(x\) up to the scale \(\sqrt{q/n}\) and a common sign. The only boundary characters of \(L\) at zero and infinity are \(1,\chi\), as required by that category. Its averaged signed weight measure is \((\delta_{-1}+\delta_1)/2\), of mass and second moment one.

For a negative object in this category, every full character outside \(\{1,\chi\}\) is good. Indeed a bad character must match an inertia eigencharacter at zero or infinity, and twisting by a quadratic character preserves the two-element set. The same applies to the intermediate convolutions by the two-character closure. The product of Mellin trace fields is exact on that good set, including the Chebyshev seed substitution by the corresponding invertible Jacobi powers. The two full characters \(1,\chi\) are the two lifts of the single trivial character of the square subgroup. Thus the entire error in the cyclic frequency vector is at coordinate zero. This uses good-character multiplicativity only away from that coordinate. [Katz, Chapters 1, 3 and 16](https://web.math.princeton.edu/~nmk/mellin331.pdf)

For a term \(T_k(S/s)\prod_{i=1}^j\mathcal A(M_i)\), where \(S=2x,\ s=2\sqrt{q/n}\), the error prior to \(K\) is a scalar times \(e_0\) of magnitude at most \(2\prod_i r_i\), where \(r_i\) are the negative factors' generic ranks. This follows from the compact-support trace bound by convolution dimension on each factor and on the intermediate object. The Chebyshev seed takes real values of magnitude at most one by the Jacobi entry bound. The dimension of each convolution of the seed powers and the factors is \(\prod_i r_i\). Purely punctual intermediate summands are discarded by \(K\), exactly as in the geometric rank calculation.

The actual correction is therefore a multiple of \(K e_0\). This is the unshifted Jacobi field, of mass and second-moment cost \(\sqrt q/n\). In the full weight distribution its measure is supported at \(\pm1\). The exact operation now has both of the geometric bounds from round 52, plus
\[
 \frac{2\sqrt q}{n}\prod_i r_i
\]
in the mass and second-moment bounds. The same quantity may be added to the first packet if using the full histogram. This estimate is independent of the ranks in the product except for their product, so it applies to arbitrarily high powers. Corrections at all stages remain in the same two-character category. A degree truncation with a field-dependent cutoff is unnecessary for the exact invariant.

## From scalar slack to the actual holomorphic section

Take a closed family of coefficient bounds for the Laurent expansion of \(H_t(S+R)\), \(H_t(z)=\sqrt{4t+z^2}\), as used in round 52 or the [packet calculation](astra-histogram-53.md). For the two-moment version let \((b,c)\) be the permitted mass and second moment of \(R\). The exact error for the term with indices \((j,k)\) is at most \(2\sqrt q\,b^j/n\) in both coordinates after summing the individual field representations. The bound for the packet version uses its total mass in place of \(b\). In both versions the factor to sum against this error is \(|c_{jk}(t)|\). The sum with \(b^j\) is uniformly finite whenever \(s+b<2\sqrt{|t|}\) with strict margin, by the binomial expansion. This holds on the domains below. The constant term is killed by \(K\).

For a precise invariant set take the closure, in the finite-dimensional space of frequency vectors, of all finite representations with the prescribed radii or packet bounds. In the packet version track a sum of prescribed packets and a residual with its own mass and second moment. Bounds for finite sums extend to the closure by continuity of each vector polynomial and absolute convergence of the series. Complex coefficients enter the representation cost by their absolute values. The mass of a representation bounds the coordinate sup norm.

Start the exact scaled Picard iteration at \(V^{(0)}=S\). On the bulk its activation is \(H_t(V_i)\), and at the mark it is \(\sqrt{4n+V_0^2}\). Thus the update of \(R=V-S\) is \(K H_t(S+R)\) plus
\[
 \left(\sqrt{4n+V_0^2}-\sqrt{4t+V_0^2}-2\sqrt n\right)K e_0 .
\]
For \(\|V\|_\infty\le4.6\) this last term is \(O(n^{-1/2})\) in mass and second moment, or in the first packet alone, uniformly on any bounded complex domain with \(t\) separated from zero. Both square roots use their power series about \(4n\) and \(4t\), with the positive branch for positive parameters. The extra contribution has the same exceptional support after application of \(K\). The strictly invariant scalar bounds absorb it and the prior \(O(n^{-1/2})\) product corrections for all sufficiently large \(q\). This bounds every exact iterate by \(4.6\) in sup norm.

On the region used here, \(|t|>16\). For any two iterates and their coordinatewise line segment, the absolute activation derivative on the bulk is bounded by \(4.6/\sqrt{4|t|-4.6^2}<3/4\). The marked derivative is at most \(4.6/\sqrt{4n-4.6^2}<3/4\) for large \(n\). Thus each successive difference in the complex Euclidean norm is at most \(3/4\) of the previous one, since \(\|K\|\le1\). Convergence is locally uniform in \(t\) at each fixed \(q\), and the limit is holomorphic with the same coordinate bound. On overlaps the iterates from the common seed and their square-root branches are the same, so the limits agree.

Rescale the limit back by \(1/\sqrt n\) to obtain \(v=Ku\), \(u_i^2-v_i^2=4w_i\), \(w_0=1,\ w_i=t/n\) on the bulk. The factors \((u\pm v)/2\) belong to the complementary spaces with equal means, and have product \(w_i\) at each coordinate. The common mean is the analytic positive branch of \(\sqrt{W/n}\) by bilinear orthogonality, with \(W=\sum_i w_i\). At positive real \(t\) all iterates are real and the factors at the limit are strictly positive. This identifies the unique actual real stationary pair, and the complex construction identifies its physical branch. At the mark \(m_q(t)=\operatorname{arsinh}(V_0/(2\sqrt n))\) in the analytic branch near zero. Integrating the derivative of \(\operatorname{arsinh}\) inside the disk of radius \(1/2\) gives the claimed \(3/\sqrt n\) bound.

## Verifying the common domain

The [complex scalar checker](marked-domain-53-check.py) combines Laurent mode coefficients in complex interval arithmetic on closed rectangles of half-width \(1/4\). It gives the following strict caps before the \(O(n^{-1/2})\) corrections.

| Real interval of rectangle | Allowed mass and second moment | Output bounds |
|---|---:|---:|
| \([2319/128,73/4]\) | \(1.740,\ 3.700\) | \(1.7393,\ 3.6899\) |
| \([73/4,19]\) | \(1.700,\ 3.620\) | \(1.695,\ 3.595\) |
| \([19,23]\) | \(1.650,\ 3.490\) | \(1.620,\ 3.425\) |

For the outer part of the domain, taking absolute Taylor coefficients before collecting the modes gives a radial majorant. Each term of arity \(2\ell\ge2\) is proportional to \(|t|^{1/2-\ell}\). The checker bounds the sums at \(|t|=22\) by \(1.64,3.45\), with radii \(1.65,3.49\). The remaining terms after degree 28 in these four checks are bounded by the geometric Taylor bounds of round 52, now with \(|t|\) in place of \(t\).

For the smallest-real-part rectangle take the rational packet radii from the real construction. Set the auxiliary radius to one and use upper bounds for every absolute Laurent coefficient on the closed rectangle \([527/32,145/8]\times[-1/32,1/32]\) in real and imaginary parts. The binomial tail uses its lower and upper moduli as in the real packet proof. Each of the 18 output entries is at most \(0.9996\) times its input cap, with total mass radius below \(1.47\). Exact errors fit in the slack of the first packet. This rectangle overlaps the wider one. All five checks are uniform interval bounds on scalar quantities, with no numerical stationary solve. [Interval records](marked-domain-53-checks.jsonl)

## A smaller region containing square ramification

Take the actual marked germ at \(T=64\) and the disk of radius \(R_{\rm big}=64-1/16\) about \(T\). The radius-42 circle is in the radial domain except for its point on \(|t|=22\), where continuity gives the same bound if a disk continuation exists. If the germ extends on the whole disk, the [marked sector theorem](parallel-cold-complex-36.md#3-uniform-growth-on-a-common-domain-with-explicit-constants) and Schwarz's lemma bound its modulus on the radius-\((64-1/8)\) circle by a constant independent of \(q\). Three circles from the radius-42 bound \(3/\sqrt n\) imply \(m_q(1/4)\to0\) through any sequence of such extensions. The actual square mark has a positive lower limit at \(1/4\), so no such extension exists at sufficiently large square order.

As in the [physical square ramification argument](parallel-cold-complex-36.md#why-this-forces-a-physical-marked-branch-point-in-1), the radius of the marked Taylor series at \(T\) is then strictly less than \(R_{\rm big}\). A point on its boundary outside \(|t|\le22\) cannot be singular, since the intersection of that centered disk with the radial domain is connected. Rotating towards the rightmost radius increases \(|t|\). The radial branch therefore agrees on the intersection and extends across any such boundary point. The positive-sector winding argument at a point of the normalized algebraic marked curve excludes zeros or poles of the mark along the accessible branch. Consequently for every sufficiently large prime square there is an accessible genuine marked branch point in \(\Re t>1/16,\ |t|\le22\). No location is asserted for an individual square.

1. Combine signed coefficients for the same geometric field before charging them to the invariant. The [unsigned packet divergence](astra-histogram-53.md#lower-escape-bound-for-the-full-positive-map) at \(127/8\) rules out simply increasing the number of packets. A strict signed invariant below that floor would extend the domain. An accessible prime marked ramification point inside a proposed domain would refute the extension itself.
2. At smaller floors, try a complex residual comparison that uses only control of the marked germ. The exact Picard proof above uses a full-coordinate contraction, and a prime-specific marked estimate could suffice even if a full-vector invariant is unavailable. Any such estimate must accommodate the verified square ramification.
