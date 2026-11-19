# Thirteen signed leaves refreshed at every vertex

At the limiting real floor \(t=2031/128\), the eight Jacobi-shifted sources of round 65 give four rank-seven outputs and two outputs of each of ranks six and eight. Their complete Jacobi-line returns can be collected at **every** level, together with the full arithmetic multipliers of the five previously identified leaves and with arbitrarily many residual siblings. The thirteen coefficients are regenerated from the preceding signed output. Their feedback is a contraction with Lipschitz constant below 0.428. At every step with regenerated inputs, the eight larger leaves decrease the signed \(m^2\) coefficient by between \(408\) and \(495\) in units of \(10^{-12}\), relative to keeping the same five smaller inputs alone.

The full packet charge of this rule exceeds 21 by height 1381 and diverges. The non-Jacobi sectors of the eight transported outputs retain their separate charges. Thus the signed amplitudes converge while the complementary packet cost grows. Actual continuation across this floor and the all-prime theta limit remain open. [Nine-center seed, amplitudes and original one-vertex bounds](astra-joint-65.md)

## Transport and compact feedback

Write \(L\) for the Jacobi convolution line, whose good value is \(-m\), and \(\mathcal T\) for the ordinary quadratic twist by \(\chi(1-a)\) and middle extension. Let \(Z_{s,F}=\mathcal T(L^{\star s}\star F)\), \(s=\pm1\), \(F\in\{U,U',D,D^\vee\}\). In the physical sign convention a source \(m^sF\) gives \(-Z_{s,F}\), up to a marked-column correction. The geometric objects are simple, since convolution with an invertible and ordinary rank-one twisting preserve simplicity, and each intermediate object has positive generic rank. Both negative input factors give positive inertia before activation. After the twist the identity stalk vanishes.

| Source factor | \(s\) | Output weights at \(1\) | Output weights at \(\chi\) | Determinant |
|---|---|---|---|---|
| \(U\) | \(+\) | \(-5,-1,-1,1,1,1,1\) | \(0^6,3\) | \(L^3\) |
| \(U\) | \(-\) | \(-3,0^6\) | \(-1^4,1,1,5\) | \(L^3\) |
| \(D\) | \(+\) | \(-5,-1^3,1^3,5\) | \(0^8\) | \(1\) |
| \(D\) | \(-\) | \(-3,0^4,3\) | \(-1^3,1^3\) | \(1\) |

Superscripts on weights denote multiplicities. The \(U',D^\vee\) rows at \(s\) are obtained by swapping the two weight lists in the corresponding row at \(-s\), with inverse determinant. To calculate them, shift the input lists at \(1,\chi\) by \(-s,s\) respectively. Preserve negative entries, exchange the positive entries and fill by zeros to dimension half the sum of the two absolute weight sums. The starting lists for \(U\) are \((-4,0,0,4),(0^4)\), and for \(D\) are \((-4,0,0,0),(0,0,0,4)\). [The two-boundary rule](astra-feedback-52.md#reading-rank-from-two-mellin-characters) · [Fourth Jacobi group](parallel-graph-shapes-23.md) · [Arithmetic group and determinant of \(D\)](two-node-groups-59.md)

For each input, a weight \(-4\) eigenvalue is \(q^{-2}\) and a weight \(+4\) eigenvalue is \(q^2\). For \(U\), the first is the negative extreme in \(L^{\star4}\) before the ordinary twist, which is unramified with value one at zero. The second follows by its arithmetic self-duality. For \(D\) use the negative extreme of the Legendre symmetric square and \(D^\vee=D^\chi\). The old determinants \(1,L^4\) show that each old weight-zero subspace has determinant one. The geometric determinant line is fixed by the two weight sums in the single-interior-singularity Jacobi category. To evaluate its arithmetic constant, use the output fiber with no zeros, namely the first for the plus rows and the second for the minus rows. Each negative or positive block there comes from one old extreme or a whole old zero-weight subspace, shifted by the Jacobi eigenvalue \(q^{\mp s/2}\). Exchange at infinity has factor \(\chi(-1)=1\). Their products in table order are \(q^{-3/2},q^{3/2},1,1\), exactly the displayed lines on these fibers. In particular the two seventh exterior powers for \(U_\pm\) have the actual good phase \(-m^3\). [Geometric determinant comparison and evaluation in a zero-free fiber](weighted-arithmetic-57.md#arithmetic-determinants)

Dualizing after \(\mathcal T\) introduces the quadratic Mellin twist, by inversion of \(\chi(1-a)\). Since \((L^\vee)^\chi=L\), the exact dual of \(Z_{s,F}\) is \(Z_{s,(F^\vee)^\chi}\). For \(U\) its partner is \(U'\) at the same sign. Each of the four \(D,D^\vee\) outputs is individually self-dual. To find every possible Jacobi line in a product of two outputs, compare both lists with the negated lists of the other object shifted by \((e,-e)\). The eight ordered objects have exactly their stated dual partners, always at \(e=0\). This also proves geometric distinctness of the eight via dualization. Schur's lemma gives unit multiplicity one with the arithmetic phase fixed by these exact dualities. No group classification in ranks six or eight is needed.

For the finite-field normalization put \(c_q=(q-1)/q^{5/2}\). For a pair of lifted physical sources \(m^sF+m^{-s}F^\chi\), each extended at the two bad characters by the product of its compact input traces with the prescribed Jacobi sign, one has
\[
 K(m^sF+m^{-s}F^\chi)
 =-(Z_{s,F}+Z_{-s,F^\chi})+d_{s,F}c_q K e_0.
\]
Here \(d_{s,U}=1\) for both signs, \(d_{+,D}=0\) and \(d_{-,D}=2\), with the same values on exchanged lifts. Indeed the compact replacement sends a positive weight-\(w\) eigenvalue \(\lambda\) to \(q^{-w}\lambda\). Compact convolution minus raw product for the perverse \(L^s\) factor thus gives \(c_q\) precisely when its signed unit weight meets the opposite extreme of \(F\). All zero-weight eigenvalues commute with the replacement. At the trivial and quadratic character respectively the counts for \(U,U'\) are \((1,0),(0,1)\). Those for \(D_+,D_-\) are \((0,0),(1,1)\), where this subscript denotes the Jacobi shift. Averaging the exchanged lifts gives the formula with the physical minus sign. Thus these finite exceptions have an explicit first-packet coefficient even before passing to the limiting prescription. For an integer check use the positional numerator of \(U\) equal to \(\ell\,\ell^{*4}\) and that of \(D\) equal to \(\ell[(N*N)+2(q+1)]\), where \(N=\ell(\ell*\ell)\), \(\ell(a)=\chi(1-a)\) and both denominators are \(q^2\). Multiplication by \(\ell\) after convolving by \(-\ell\) or \(-\chi\ell\) needs exactly the displayed inverse-transform corrections, integers \(0,1,\chi,1+\chi\) in the numerator with denominator \(q^{5/2}\). Seven field rings check the square positions and all four dual identities.

## The overlapping signed rule

Write \(f(x)=\sqrt{4t+x^2}\) and let \(H_j\) be the nine-center kernels at argument \(V\), with the existing arity-zero amendments. At each level keep a signed field \(Y\) on \(U,U',D,D^\vee,R\), and a signed field \(X\) on the eight new \(Z_{s,F}\). For the latter include the physical sign of transport. Write \(p_h(m)\) for the sum of the Jacobi-line constituents of \(X^h\), before taking absolute values, with their actual arithmetic coefficients. Equivalently this is conditional integration of the new block over the geometric kernel of the Jacobi coordinate on the arithmetic compact coset, given \(m\). Integration retains every geometric line on this torus with its arithmetic phase. The input symmetry under lift exchange and conjugate duality is preserved by \(K\) on squares. In particular both fields are real on the compact group. The preceding dual calculation gives
\[
 p_0=1,\qquad p_1=0,\qquad p_2=C=\sum_{s,F}|x_{s,F}|^2 .
\]
This calculation also applies to the absolute input amplitudes. In old multipliers the two cubic shifts \(m^{-4}D,m^4D^\vee\) remain in the full seven- and nine-center arithmetic kernel.

Fix an ordered list of \(r\) untagged residuals. Across every such list pool the full arithmetic character of
\[
 S_r=\sum_{a,b\ge0}\frac{(r+a+b)!}{r!a!b!}\,
 H_{r+a+b}Y^a p_b(m).
\]
All other constituents of the large block retain their original separate unsigned charges. Equivalently, the future price of each list is its grouped multiplier plus those retained charges, followed by its unsigned boundary convolution. For \(r=0\), transport the projections of this very \(S_0\) on the thirteen original source labels into the next \((Y,X)\). All its other labels, and all separately charged non-Jacobi constituents, are residuals, even if one of their arithmetic labels occurs among the tagged labels. This last convention specifies exactly which histories are pooled. Initialize both fields to zero. There is no level reset. The rule includes successive returns through arbitrarily long connected all-tag histories.

For evaluating \(S_0\), draw the old coordinates from their compact law and draw \(X\) independently of them conditional on \(m\) using its actual conditional law. This auxiliary conditional integration is exactly the specified Jacobi projection. It requires no claim of independence between the true new and old derived factors. With \(A\) the fixed root amendments,
\[
 S_0=A+\mathbb E[f(V+Y+X)\mid\text{old}].
\]
The thirteen old source characters are distinct orthonormal characters for the old arithmetic law. The five old output characters are likewise orthonormal, and transport to the indicated single output incurs only a sign. Use Euclidean coefficient norms and the closed box
\[
 \|y\|_2\le3\cdot10^{-8},\quad |x_{s,U^{(\prime)}}|\le153\cdot10^{-6},\quad
 |x_{s,D^{(\vee)}}|\le145\cdot10^{-6}.
\]
Then \(C\le177736\cdot10^{-12}\), \(\|Y\|_\infty\le\sqrt{128}\,\|y\|_2\), and \(\|X\|_\infty\le 28(153+145)10^{-6}\). The last bound uses the four ranks seven and two each of six and eight. With \(M\) the nine-center dimension bound, \(|f'|<0.427\) on \(|x|\le M+\sqrt{128}\,3\cdot10^{-8}\). Also \(0\le f''\le1/(2\sqrt t)\) on the real line. Conditional Taylor expansion with \(p_1=0\), followed by Bessel's inequality, bounds the Euclidean displacement of the entire refreshed coefficient vector from the direct \(H_0\) projection by
\[
 \sup|f'|\,\|y\|_2+C/(4\sqrt t)<23951\cdot10^{-12}.
\]
The direct small vector has norm below \(4047\cdot10^{-12}\). The direct individual large coefficients have magnitudes below \(152705\cdot10^{-9}\) or \(144292\cdot10^{-9}\), respectively. This proves invariance. On including the dimension of \(X\) in the argument, \(\sup |f'|<0.427311\). For differences, conditional centering of \(X\) makes \(\Delta X\) orthogonal to \(\Delta Y\) on the auxiliary space, and the eight distinct characters give \(\|\Delta X\|_2^2=\sum|\Delta x_{s,F}|^2\). Conditional expectation and thirteen-coordinate projection contract \(L^2\). Thus the signed refresh is a strict contraction on its invariant, symmetry-preserving box and has a unique fixed point there for each arithmetic law.

The change to \([m^2]S_0\) from admitting \(X\) at fixed \(Y\) has leading term \(C[m^2]f''(V+Y)/2\). Its Taylor remainder is bounded by \(C\|X\|_\infty\sup|f'''|/6\), since the conditional second moment is the constant \(C\). Use \(\sup|f'''|\le3/(4t)\). Compare the leading derivative to the seven-center projection obtained from the round-65 signed binary by dividing by \(2v^2\). The argument difference is bounded by \(8|v|+\sqrt{128}\,3\cdot10^{-8}\). After the initial zero-input update, every large component differs from its direct value by the above displacement. The resulting strictly negative change lies in \((-495,-408)10^{-12}\) at every such step. This detects cancellation with the same smaller signed inputs through the full series.

## Full complementary cost and continued growth

Let \(B\) be a symmetric retained lower boundary, and \(T_*\) the true absolute boundary of the thirteen regenerated tags. The exact untagged part dominates \((B-T_*)_+\). This surrogate together with the exact tags dominates \(B\), and its untagged part is bounded above by \(B\). At fixed tag amplitudes each grouped residual list has a nonnegative price. This permits downward substitution independently at each level, even though the signed amplitudes depend on earlier levels. The box control is uniform over the full exact refresh.

Let \(P,G\) be positive boundary upper measures for the five and eight fields, obtained by multiplying their actual first-twist boundaries by the respective component caps and adding. By lift symmetry the second-twist aggregate is identical. An upper measure for the terms collected at total tagged count \(h\ge1\), also covering their original separate charges, is
\[
 A_h=P^{*h}+\binom h2 C_{\max}P^{*(h-2)}
 +\sum_{k=3}^h\binom hk P^{*(h-k)}*G^{*k}.
\]
The middle term is present only at \(h\ge2\). The absent \(k=1\) has zero Jacobi projection and keeps its full original price. At \(k=2\) only the proved eight ordered dual contractions can affect the grouped price. At \(k\ge3\) the entire unprojected positive measure pays for any collisions and determinant shifts. For every residual count \(r\le9\), start with the round-65 one-vertex lower measure at \(B\) and debit twice the convolution of \(B^{*r}\) against \(\sum_{h\ge1}\binom{r+h}r U_{r+h}*A_h\). This pays both the formerly separated terms and the possible reduction of their direct competitors. All residual lists with \(r>9\) carry their own nonnegative prices. The statement includes old multipliers sharing any of the five old factors with the tags. [Surrogate comparison](astra-mixed-61.md#a-lower-substitution-that-does-not-bound-the-true-iterate-from-above)

For the degree-28 polynomial use all \(h\le28-r\) and charge the largest off-strip upper atom against the whole residual mass. Write \(g=\|P+G\|_1<0.008345\), \(s=\|P\|_1\), and let \(E\) be the previous binomial tail at auxiliary radius 2 for the nine-center seed. The remaining analytic charge before doubling, per bin and per residual list, is at most
\[
 \frac{E}{2^r}\left((r+1)s/2+\binom{r+2}r(s^2+C_{\max})/4+
 \frac{\binom{r+3}r(g/2)^3}{1-(g/2)(1+r/4)}\right).
\]
This includes every tagged degree and sibling count affecting the retained outputs. Round down after each update with arity through 9, signed shifts through 18 and 28 positive packets. The full lower mass exceeds 21 by height 1381. Before multiplying by two residuals, the debited zero-shift lower atom at \(r=2\) exceeds 0.058284. The same double debit bounds the possible loss on this particular residual list. The untagged boundary of a full measure of mass \(M_0>21\) has mass at least \(M_0-g\). It is symmetric and its normalized first absolute moment is one. Conditional Jensen for two independent draws gives next full mass at least \((M_0-g)^2/20\), which grows strictly above the diagonal from 21 onward. The finite-width crossing therefore certifies continued growth of the full prescription.

The [Arb192/integer checker](astra-shifted-66-check.py) produces [four records](astra-shifted-66-checks.jsonl). Run `.venv/bin/python -B research/astra-shifted-66-check.py` at the repository root.

## A rank-six candidate inside the older group

There is a specific obstruction to treating the eight larger objects as new independent factors. For the earlier rank-four \(A\) with \(\det A=L^2\), the two boundary lists of \(L^{-1}\star\bigwedge^2_\star A\) coincide with those of \(Z_{-,D}\). The first exterior list of \(A\) is \((-4,-1^4,2)\), shifted up by one by \(L^{-1}\). The second is \((0^3,2^3)\), shifted down by one. The [separate exact diagnostic](astra-shifted-66-collision.py) also finds equal good-character traces in \(\mathbb Z[\zeta_{q-1}]\) at every good full lift for \(q=5,9,13,17,25,49,97\), including nonzero values in each field. To evaluate the exterior trace use \(((\operatorname{tr} A)^2-\operatorname{tr}(A^2))/2\), obtaining the second trace over \(\mathbb F_{q^2}\) with the character pulled back under the norm. The factor \(L^{-1}\) is the signed dual Jacobi trace. The [fieldwise record](astra-shifted-66-collision.jsonl) does not establish a uniform sheaf isomorphism. This comparison is independent of the four escape records. [Earlier rank-four rows and determinants](rank-four-arithmetic-56.md)

1. Prove or distinguish \(Z_{-,D}\simeq L^{-1}\star\bigwedge^2_\star A\) and its exchanged lift, including the arithmetic phase and compact correction. A proof would place both rank-six outputs inside the old group and permit complete linear collection against its actual multipliers. A certified mismatching good trace on an extension suffices to refute the identification.
2. Pool the non-Jacobi multipliers of the transported outputs on overlapping levels, including the candidate rank-six collision and the rank-seven determinant lines \(-m^{\pm3}\). An actual strict invariant crossing \(2031/128\) with full sibling and marked costs passes. A fully debited crossing of 21 with a surviving superlinear term rejects that stronger signed rule.
