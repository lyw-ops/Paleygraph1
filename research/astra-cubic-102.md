# Displaced dual returns on the physical stationary section

For every eligible prime \(p=2n+1\) with \(n\ge10^{30}\), the unforced nine-center iteration has a holomorphic physical stationary row on
\[
 16640182.375<2^{20}\Re t<16640183.125,\qquad 2^{20}|\Im t|<1.
\]
Its open overlap with [round 101](astra-rank-101.md) is \((16640183,16640183.125)\) in the same units. The left edge moves \(5/8\) of a unit and leaves \(2222.375/2^{20}\) to the right edge of the nominated square.

## The two displaced coefficients

Use the round-101 signed coefficient \(A_{r,a,u,b,e}\) on the rank-four scalar, with its full zero, quadratic and quartic rank-four terms. This includes the two quartic returns at determinant shifts \(\pm2\). The source Jacobi mode is at most nine, the rank-three labels run through degree four, \(u+b\le5\), and an unavailable arity or source contributes zero. Suppress \(a,u,b\) below. Denote the last four signed amplitudes by \(\delta,z,w,v\); in particular \(w\) multiplies \(D+D^\vee\). Write \(Q=\delta^2/16+z^2+2w^2+2v^2\).

The arithmetic line \(\det D=m^4\) has phase \(+1\). Thus \(\bigwedge^3D=D^\vee m^4\) and \(\bigwedge^3D^\vee=Dm^{-4}\), each once. For \(0\le j\le5\), at final label \(D^\vee m^e\) collect
\[
 w\big[(j+1)A_{j+1,e}+3\tbinom{j+3}{3}Q A_{j+3,e}\big]
       +\tbinom{j+3}{3} w^3 A_{j+3,e-4}.
\]
At \(Dm^e\) the displaced source is \(A_{j+3,e+4}\). Each added coefficient comes from three identical children of the opposite standard. The six balanced contractions at each standard stay in the bracket. At final arity zero omit \(a=0,e=0,(u,b)=(1,0),(0,1)\), including the native mixed-symplectic and dual-pair root pools. Each displaced input reaches exactly one final exponent for its chosen constituent. At the first boundary the added savings use the four weights \((0,0,0,4)\) for \(D^\vee\) and \((-4,0,0,0)\) for \(D\). [Arithmetic determinant](two-node-groups-59.md) · [Native cubic roots](astra-joint-64.md)

There is a second displacement on the same factor. Put \(H=\bigwedge^2D\); then \(\bigwedge^2 D^\vee=Hm^{-4}\). The two exterior-square constituents of \((D+D^\vee)^2\) have multiplicity one each. At \(Hm^e\), for \(0\le j\le6\), their joint coefficient is
\[
   \tbinom{j+2}{2}w^2\big(A_{j+2,e}+A_{j+2,e+4}\big).
\]
The boundary measure of \(H\) has multiplicity three at each of \(-4,0\). This follows by choosing an unordered pair of distinct entries in the first list of weights of \(D\). The checker also enumerates rational \(GL_4\) highest weights before the determinant is identified with the old arithmetic line. It finds the balanced multiplicity six and displaced multiplicity one in each direction.

For both families add the rank-three boundary weight and Legendre weight \(-2u+4i\), subtract the *final* exponent \(e\), and include the multiplicity \(b+1\). The quadratic-twist exchange swaps the two dual standards and the Legendre and rank-three factors, and reverses the boundary sites. For the square it rewrites the exchanged pair in the same \(H\) convention. At each pair of opposite sites debit at most their smaller lower saving. Endpoints with just one coefficient have zero triangle saving.

## Charges available after earlier returns

For a fixed inner label the rank-three prefix and rank-four scalar supply the constituents of \(A\). In particular every native scalar extraction that meets this pool has all its selected zero, two and four rank-four constituents within the same \(A\), including its shifted source terms. The earlier scalar zero/two collections also remain within one \(A\). Each remaining partial partition into older charged groups therefore has mass at least \(|A|\). This applies separately after attaching each of the selected later constituents. The round-99 one-child propagation and the round-101 two-child nonunit propagation copy lower bounds on cancellations *within* those older groups. Even after those debits the same inequalities hold. The other round-99 and round-100 propagated terms have complementary rank-three **source** indices or nontrivial rank-four shapes. [One-child accounting](astra-cold-99.md#propagation-to-one-later-child) · [Complementary sources and shapes](astra-return-100.md) · [Two-child nonunits](astra-rank-101.md#two-later-children-with-nontrivial-joint-label)

For the cubic calculation, round 101 can already have pooled the linear term with the six balanced contractions and the mixed unit insertions. Its lower debit leaves at least the modulus of the displayed bracket times \(|w|\); one more triangle inequality attaches the previously separate displaced copy. The native root omission is imposed at the output exponent even when the shifted *source* is elsewhere. For the quadratic calculation, the round-96 two-child pool selected only the arithmetic units. Neither exterior square is a unit. The older nonunit propagation improves each individual source's charge, and does not identify the two exterior-square sources at the shared output exponent. Their two remaining charges dominate the two separate \(|A|\)'s at that exponent with the stated common factor. No native two-child root amendment uses these squares. The two new debits use different later input degrees. All unselected Taylor terms and the exceptional column retain their charges.

On the entire box \(|2^{20}\Re t-16640183|\le1,\;2^{20}|\Im t|\le1\), take trivial inner labels. The scalar triangle saving before multiplying by the four boundary weights of \(D^\vee\), at \(j=0,e=5\) with cubic source exponent one, exceeds \(1.374\cdot10^{-12}\). The corresponding exterior-square witness at \(j=1,e=-3\) exceeds \(3.65\cdot10^{-10}\). These are separate lower bounds.

## Actual iteration and replay

In units of \(2^{-20}\) the three closed real intervals are \([16640182.875,16640183.125]\), \([16640182.5,16640183]\), and \([16640182.375,16640182.5625]\), with respectively two, four and four real cells. Each uses one upper imaginary cell of height one and its conjugate. The forcing is one. The 58-packet Arb192 image, including the full \(10^{-12}\) exceptional-column allowance, has tilted excess below \(1.85\cdot10^{-10}\) on the frozen integer caps, against a \(2\cdot10^{-10}\) budget. With the previous map the first of these same frozen caps overruns packet three by more than \(2.35\cdot10^{-9}\). The comparison concerns this cap. [Checker](astra-cubic-102-check.py) · [Integer caps](astra-cubic-102-caps.json) · [Five replay records](astra-cubic-102-checks.jsonl)

The coordinate bound is below \(4.654\), the secant bound is below \(.526\), including the mark, and the normalized successive increments are at most \(9.308(.526)^h\). The fixed-field limit agrees with the real physical stationary row and satisfies \(|m_p|<3/\sqrt n\). Its action is harmonic on the reciprocal image. For the finitely many smaller primes, the previous compactness argument allows a thinner complex neighborhood of each closed real subinterval. The nominated square and ordinary theta limit remain open. [Convergence and physical identification](astra-depth-95.md#field-first-decay-and-harmonic-action)

Run from the repository root:

    PYTHONPATH=. .venv/bin/python -B research/astra-cubic-102-check.py

## A common deletion for both real tails

For a fixed candidate first exit, row, sign, preceding time and nonzero lag matrix in the [real first-exit criterion](astra-exit-98.md), there is an exact minimum-cardinality deletion test for the simultaneous \(.00139\) bounds at **all** thresholds. Write \(a_x=\sigma C_{\ell,ix}\), and separate the two disjoint lists \(z_x>v_x\) and \(z_x<v_x\), dropping zero defects. In each list process the distinct defects in decreasing order. At each equal-defect group add the absolute values of all its negative entries to a running allowance initially equal to \(.00139\). Insert its positive entries one at a time into the kept list. Whenever the total kept positive weight exceeds the current allowance, erase one largest kept weight. Never erase a negative entry.

After each group, the constraint is exactly the corresponding signed-prefix bound. Grouping ties matters because the physical cut uses a strict threshold. The running allowance is nondecreasing. One removal restores feasibility after an insertion, since the removed weight is at least the inserted weight. To prove optimality, take an optimum consistent with all previously forced erasures. At an overflow it must omit some currently kept positive weight or the newly inserted weight: even the entire equal-defect group shares the same allowance, so keeping this overflowing subset is impossible. If the optimum keeps the chosen largest weight, exchange it for such an omitted weight. Earlier completed groups are feasible because the greedy-kept prefix before this overflow was feasible with all previous erasures. From the overflow group onward the exchanged total is no larger. This inductively gives an optimum consistent with every greedy erasure. The union of both lists' optimal erasures is therefore simultaneously feasible at every level and minimum in cardinality. An erasure elsewhere cannot reduce either list.

Consequently, a genuine first exit forces some lag for which these two minimum counts sum to more than \(\lfloor\sqrt n/6000\rfloor\). Indeed if the sum fits at every lag, use the unions as the independent per-time deletions allowed by round 98. Both cuts would be at most \(.00139\) at every lag, contradicting that round's signed response. This reduces the required real-orbit bound to a single integer per physical row, sign and time. The needed upper bound on that integer through primes remains open.

1. Bound the sum of the two optimal counts on actual pre-exit rows by \(\lfloor\sqrt n/6000\rfloor\). The common per-time deletion would then exclude real first exits.
2. In the same dual system, test the full quartic coefficient on \(\bigwedge^2D\) and its determinant translate against the already pooled two-square coefficient. Compute the quartic multiplicities at their actual shifts, retain the earlier square pooling as one term, and require another strict overlapping slab.
