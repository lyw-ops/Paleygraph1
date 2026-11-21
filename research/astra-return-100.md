# Rank-three determinant cubics and repeated rank-four shifts

For every eligible prime \(p=2n+1\), \(n\ge10^{30}\), the unforced nine-center iteration has a common holomorphic physical stationary row on
\[
  16640185 < 2^{20}\Re t < 16640191,\qquad 2^{20}|\Im t|<1.
\]
The open overlap with [round 99](astra-cold-99.md) is \(16640190<2^{20}\Re t<16640191\). The left edge advances five units of \(2^{-20}\), leaving \(2225/2^{20}\) to the right edge of the nominated square.

## The rank-three complement

Let \(r\) be the free arity after the rank-three translation, \(h\) its number of \(W\)-inputs, \(k\) the unsigned Jacobi mode, and \((u,v)\) the two Legendre labels. Use the actual amended source at raw arity zero. For \(0\le r\le26\), take degrees \(0\le h\le4\), \(r+h+k\le28\), and select a source only when
\[
 r>8\quad\text{or}\quad k>9\quad\text{or}\quad u+v>5 .
\]
This test applies to each incoming source independently, including the two shifted cubic sources. Every selected source belonged to the positive complement before round 99. The rank-three derived shapes retained here are the trivial shape and the four standards and duals from degree one. For a shift \(d\) of multiplicity \(M_h(a,d)\) at derived shape \(a\), send the term
\[
 \binom{r+h}{r}(\beta/4)^h M_h(a,d)
 \frac{g_{r+h,k,u,v}}{1+\mathbf1_{k>0}}
\]
to each distinct output \(e=d\pm k\). Sum on a common \((r,a,u,v,e)\). For the scalar, first combine degrees zero and two without claiming their saving again. Their remaining charge is at least the modulus of this sum, because round 99 debited at most the original triangle saving. Both cubic determinant shifts \(d=\pm1\) have multiplicity two. Add these cubic terms to that sum and then the quartic term of multiplicity 48 at shift zero. For each standard, every original constituent of degrees one through four in this complement was still separately charged, so collect all its selected terms. The integer multiplicities follow from the [rank-three Pieri rule](astra-rankthree-56.md#an-arithmetic-expansion-with-a-unique-label).

For example, at \((r,u,v,e)=(12,0,0,0)\) the updated scalar and its cubic increment are
\[
 A=g_{12,0,0,0}+\binom{14}{2}\frac{\beta^2}{4}g_{14,0,0,0},
 \qquad B=2\binom{15}{3}(\beta/4)^3g_{15,1,0,0}.
\]
The two equal cubic contributions are from opposite shifts and opposite exponential halves of mode one. The outward lower bound on \(|A|+|B|-|A+B|\) is greater than \(1.9\cdot10^{-16}\) throughout the entire colder closed box. This particular saving is on a self-reflected scalar fiber.

## Rank-four shapes first appearing in degrees three and four

Now use only the old signed prefix, complementary in source indices to the preceding calculation. Let \(C_{r,a,u,v,i}\) denote the [arithmetic inner coefficient](astra-depth-95.md#eight-further-signed-rank-three-labels) at free arity \(r\le8\). Use every derived rank-three label through degree four. Among the rank-four shapes first appearing in \((8F)^h\), exactly 16 at \(h=3\) and 76 at \(h=4\) have two distinct determinant shifts, and 3 at \(h=4\) have three. Select these 95 shapes. For each shape \(s\), its full shift list \((d,M_h(s,d))\), remaining arity \(0\le j\le8-h\), and output exponent \(E\), collect
\[
 \binom{j+h}{h}(\gamma/8)^h\sum_d M_h(s,d) C_{j+h,a,u,v,E-d}.
\]
Each marked shift sends each source to exactly one output. Taking the union of attainable output exponents also includes endpoints with only a subset of the shifts. The checker groups shapes with identical relative shift and multiplicity lists after incorporating their smallest shift in the boundary weight. This preserves each signed sum. [Rank-four Pieri table and twist](astra-rankfour-57.md)

These shapes have no scalar, linear or quadratic occurrence. The preceding cubic debits selected the degree-one standards. The preceding quartic debits selected a scalar or a shape already present in degree two. Thus the selected cubic and quartic constituents still had separate charges even in the extracted scalar *inner* sector, where the native quartic collection used only scalar rank-four lines. The native distinguished subtractions and later Legendre return amendments use a rank-four scalar or standard. The two-child debit of [round 96](astra-paired-96.md#four-quadratic-unit-contributions-and-an-unforced-complex-extension) used rank-four degree zero or the previously combined scalar lines. The one-child propagation in round 99 used only the earlier marked shape constituents. Thus the full later translations of the 95 new shape families were separately charged as well.

## Boundary propagation and replay

Compute each successive triangle saving by the nonnegative [signed formula](astra-depth-95.md#eight-further-signed-rank-three-labels). At Jacobi exponent \(E\) and rank-three and rank-four weights \(w_3,w_4\), the site is \(w_3+w_4+b-E\), with \(b=-2u,-2u+4,\ldots,2u\) and multiplicity \(v+1\) times the two weight multiplicities. Use zero for an absent rank-four weight. Both index selections commute with reflection, the paired factor interchange, and Legendre interchange. The exact sum of triangle savings is independent of the order in which the selected terms are added, even for three unequal shifts. Debit at most the smaller outward lower saving on the two reflected sites. For a saving at residual arity \(r\), propagate to final arity \(j\) by the factor \(\binom rj\) and the \((r-j)\)-th convolution power of the sum of the full absolute boundary measures of the remaining centers. There are five such centers after the complementary rank-three calculation and four after the rank-four calculation. The multinomial expansion reproduces the positive native charges at every later input count. Retain all other charges, the Taylor tail and the physical exceptional allowance.

The [Arb192 checker](astra-return-100-check.py) uses two closed slabs in endpoint units \(2^{-20}\), \([16640185,16640188]\) and \([16640187,16640191]\). They have six and four real cells respectively, one upper imaginary cell each, and original forcing one. The [frozen 58-packet caps](astra-return-100-caps.json) have tilted excess below \(1.85\cdot10^{-10}\), including \(10^{-12}\) for the exceptional physical column, against budget \(2\cdot10^{-10}\). The coordinate cap is below \(4.654\). The round-99 map overruns the colder frozen cap in its first packet. [Replay records](astra-return-100-checks.jsonl)

Run from the repository root:

    PYTHONPATH=. .venv/bin/python -B research/astra-return-100-check.py

By the [field-first convergence argument](astra-depth-95.md#field-first-decay-and-harmonic-action), the derivative bound on every iteration segment is below \(.526\), including the mark. The normalized second-norm Picard increment is bounded by \(9.308(.526)^h\). The stationary row has \(|m_p|<3/\sqrt n\) on the open union and agrees with the physical branch on the real interval. Its action is harmonic on the reciprocal image. The previous small-prime compactness argument applies on closed real subintervals after shrinking the imaginary width. The common continuation to the nominated square, the two signed real log tails after a common legal erasure, and the ordinary theta limit remain open.

1. Bound both signed real log tails by \(.00139\) on the realized orbit after one legal erasure at each pre-exit time. This would exclude a real first exit throughout the nominated interval.
2. For each of the sixteen rank-five standards and duals in \(16G\), test the linear contribution against its cubic return with the same arithmetic exponent. The own-factor balanced words supply six copies and the other seven dual pairs supply six each, for 48 in all. Track the remaining linear charge after the round-99 one-child debit and retain the exceptional root amendments. A strict overlapping slab to the left of \(16640185/2^{20}\) would give a further common continuation.
