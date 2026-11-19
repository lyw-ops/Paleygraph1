# The two rank-six transports are old exterior squares

For every odd prime power \(q\equiv1\pmod4\), in the normalized arithmetic middle-convolution category,
\[
 Z:=Z_{-,D}\simeq L^{-1}\star\bigwedge^2_\star A,\qquad
 Z^\chi=Z_{+,D^\vee}\simeq L\star\bigwedge^2_\star(A^\chi).
\]
The first isomorphism follows from a Frobenius correlation exceeding an explicit upper bound for a zero geometric Hom space at one prime, tame specialization, and an arithmetic boundary eigenvalue. The second follows by the quadratic Mellin twist. In the nine-center recursion their first linear return together decreases the positive \(m^2\) coefficient by between \(10.901\) and \(10.941\) in units of \(10^{-12}\) at \(t=2031/128\).

## A single fiber forces a geometric intertwiner

Write \(W=L^{-1}\star\bigwedge^2_\star A\). Both \(Z,W\) are geometrically simple perverse sheaves. For \(W\), the old derived group acts through the irreducible exterior square of the standard \(\mathrm{SL}_4\), and \(L^{-1}\) is invertible. Both have ordinary generic rank six and convolution dimension six. They are middle extensions from \(U=\mathbf P^1-\{0,1,\infty\}\) and tame at its boundary. Their fibers have weight lists \((-3,0^4,3)\) and \((-1^3,1^3)\) at the trivial and quadratic Mellin characters. At each of the positional boundaries zero and infinity this gives one trivial-character Jordan block of length three and three quadratic-character blocks of length one. The inertia invariants of ordinary \(\operatorname{Hom}(W,Z)\) at each of these two points have dimension \(3+3^2=12\). At one the stalk of \(Z\) vanishes. [Round 66 transport and weight comparison](astra-shifted-66.md) · [Old derived groups](rank-four-positive-55.md#geometric-independence-and-conditional-moments)

Suppose the two geometric lisse systems on \(U\) are nonisomorphic. Form their ordinary rank-36 Hom sheaf \(E\) of weight zero. By irreducibility, \(H^0(U_{\bar k},E)=H^2_c(U_{\bar k},E)=0\). The tame Euler formula gives \(\dim H_c^1(U_{\bar k},E)=36\). In its exact sequence for \(j:U\hookrightarrow\mathbf P^1\), the boundary invariants inject. At least 24 dimensions of \(H_c^1\) therefore have weights at most zero, from the stalks of \(j_*E\). All remaining dimensions have weights at most one by Weil II. Write \(z,w\) for the normalized **positional perverse traces**, of lisse weight \(-1\), so that \(qz(a)\overline{w(a)}=\operatorname{tr}(E,a)\) on \(U(k)\). The trace formula gives the convenient bound
\[
 \left|\sum_{a\in k^\times} z(a)\overline{w(a)}\right|
 \le 12/\sqrt q+36/q .
\]
The identity position contributes zero. No comparison of the Jordan forms at one is required.

Now set \(q=401\). Let hats denote the full unnormalized multiplicative Fourier transform. The exact integer calculation gives \(\widehat z=\widehat w\) at all 398 good characters, and
\[
 \frac1{400}\sum_{\alpha\ne1,\chi}|\widehat z(\alpha)|^2
 =\frac{112309360376291}{103686416020010}.
\]
At each of the two bad characters each compact trace has absolute value at most six. Indeed each positive-weight Deligne-fiber eigenvalue of weight \(h\) is multiplied by \(q^{-h}\) in the compact trace, and the other eigenvalues already have absolute value at most one. Taking real parts in Parseval, the correlation is at least
\[
 \frac{234114513731723}{259216040050025}
 >\frac{1383}{2005}
 =\frac{12}{20}+\frac{36}{401}.
\]
Since \(\sqrt{401}>20\), a zero Hom space is impossible. Geometric simplicity turns any nonzero intertwiner into an isomorphism.

For reproducibility the [integer checker](astra-rank-six-67-check.py) uses the [exact numerator rows and quadratic norm pullback](astra-shifted-66-collision.py). With \(n=400\), subtract the two Newton expressions in \(\mathbf Z[X]/(X^n-1)\), clearing their common denominator. The resulting coefficients alternate between the two constants \(8307732728,8546249132\). This is equivalent to vanishing at every good character and allows the two compact exceptions to differ from the raw Newton product. Compute the good energy independently from the squared norm of the positional \(Z\) row by subtracting its two bad Fourier energies. The [record](astra-rank-six-67-checks.jsonl) gives the exact fractions. This finite calculation enters a strict separation inequality for sheaves.

## Specialization through all odd characteristics

Take \(\ell=2\) and \(S=\operatorname{Spec}\mathbf Z[1/2]\). Before imposing any weight-normalizing constant-field twists the lisse restrictions of the two constructions have relative models on \(U_S\). Here are the details, needed to pass from one geometric fiber to the others.

* Start from the quadratic Kummer sheaves in \(a\) and \(1-a\) on \(U_S\). Pullback by \(a\mapsto1-a\) and inversion, ordinary duality and ordinary tensoring all preserve relative lissity. With \(\sigma(a)=1-a\) and \(\mathcal T\) the ordinary twist by \(\chi(1-a)\) followed by middle extension, the geometric constructors in these conventions are \(N=\mathcal T(L^{\star2})\), \(R=\mathcal T(\sigma^* L^{\star3})\) on the open, \(A=\mathcal T(L\star R)\), \(D=\mathcal T(\operatorname{Sym}^2_\star N)\), and \(Z=\mathcal T(L^{-1}\star D)\). In particular the pure nested \(\mathcal T(L\star N)\) has the dual orientation to the chosen \(R\), by the Pfaff identity in round 31. [Rank-three construction](astra-nested-moment-31.md#2-the-actual-new-rank-and-local-monodromy)
* At a convolution with output variable \(t\in U_S\), use the smooth proper relative \(x\)-line with the four disjoint sections \(0,1,t,\infty\) over \(U_S\). On their complement take the lisse sheaf \(F(x)\otimes G(t/x)\) for the input ordinary local systems. The generic middle-convolution local system is its parabolic \(H^1\), the image of \(R^1\pi_!\to R^1\pi_*\) on that complement. Indeed the internal punctures \(1,t\) are distinct, so the tensor of the two input middle extensions there is the middle extension of the tensor. The compact-to-ordinary image on \(\mathbf G_m\) is equivalently \(H^1(\mathbf P^1,j_* (F\otimes G))\) with all four punctures filled. These identifications also follow from the curve localization sequence. Katz's relative curve theorem gives lissity and formation compatible with base change for the two direct images, hence for their image. Apply it over the normal characteristic-zero-generic base \(U_S\). [Katz, *Convolution and Equidistribution*, §§2, 22](https://web.math.princeton.edu/~nmk/mellin331.pdf) · [Katz, *Another Look at the Dwork Family*, Theorem 6.4(1)–(3)](https://web.math.princeton.edu/~nmk/dworkfam64.pdf)
* For equal inputs the convolution commutativity operator is relative, induced by \(x\mapsto t/x\) and exchange of the two shifted inputs, including the Koszul factor \((-1)^{1\cdot1}=-1\) on the two \([1]\) shifts. Its symmetric and exterior projectors are idempotents in characteristic-zero coefficients. Their images are lisse and specialize to the same projectors. This realizes both \(\operatorname{Sym}^2_\star N\) and \(\bigwedge^2_\star A\) on the open. The individual intermediates subsequently convolved are full-support simples, by invertibility of the relevant \(L\) powers and the old \(\mathrm{SL}_2,\mathrm{SL}_4\) derived group calculations. In \(N\star N\) the punctual unit is \(\bigwedge^2_\star N\) because \(\det N=1\). All punctual summands restrict to zero on \(U\). The symmetric projection selects the full-support symmetric square, and \(\bigwedge^2_\star A\) also has positive generic rank. Thus the restrictions being used do recover the inputs' middle extensions when they are used again. [Legendre symmetric square](two-node-groups-59.md#the-individual-quadratic-legendre-source)

Apply Theorem 6.4(4) of the same relative curve theorem to the two resulting lisse sheaves on \(U_S\), with the sections \(0,1,\infty\) of \(\mathbf P^1_S\). Geometric irreducibility and isomorphism at 401 imply that the relative systems agree up to a character from the base. In particular their geometric restrictions agree in every odd characteristic. Omitting the constant-field normalizations in building relative models does not affect this geometric comparison. The trace functions are also compatible with changing the auxiliary prime, by middle convolution and the character-sum formulas, or by matching all finite-extension traces and Chebotarev.

## Arithmetic normalization and the marked coordinate

Fix an eligible field. Geometric simplicity now leaves only an arithmetic constant. In the trivial-character Deligne fiber the weight \(-3\) eigenline of \(Z\) has eigenvalue \(q^{-3/2}\). It comes from the weight \(-4\) eigenvalue \(q^{-2}\) of \(D\), multiplied by the trivial-fiber \(q^{1/2}\) of \(L^{-1}\). The ordinary twist by \(\chi(1-a)\) is unramified with value one at zero. In \(W\) the same unique line is \(q^{1/2}\) times the determinant of the two weight \(-2\) eigenvalues of \(A\). This determinant is \(q^{-2}\) by the earlier arithmetic calculation. Therefore the constant is one. Quadratic twisting preserves the tensor projectors, exchanges \(L,L^{-1}\), and sends \(D\) to \(D^\vee\). This proves both stated arithmetic identifications, in particular for every extension of the given field. [Rank-four boundary determinant](rank-four-arithmetic-56.md#frobenius-on-the-distinguished-boundary-spaces) · [Transport boundary eigenvalues](astra-shifted-66.md#transport-and-compact-feedback)

Both identifications include the compact Mellin traces of the middle extensions. For the *physical* paired inputs with the previous compact convention the exact feedback is
\[
 K(m^{-1}D+mD^\vee)
 =-(W+W^\chi)+2\frac{q-1}{q^{5/2}}K e_0.
\]
Here both terms on the right use their compact extensions at the mark. The correction has the same sign on the exchanged lift. This follows by substitution into the round-66 compact feedback identity. A raw product of compact Jacobi traces and compact Newton expressions can still require correction at those two full characters. [Finite-field feedback proof](astra-shifted-66.md#transport-and-compact-feedback)

## A linear cancellation on the actual old group

Use the nine-center \(V\), \(H_1=f'(V)\), and \(H_0\) with its root amendments at \(t=2031/128\). Lift exchange makes the direct \(H_0\) source coefficients on \(m^{-1}D\) and \(mD^\vee\) equal. Write \(s_D\) for their common value. The two transported leaves have signed input \(-s_D(Z+Z^\chi)\). For projection on the physical \(m^2\) character, their full arity-one term satisfies
\[
 -10940435\cdot10^{-18}
 <[m^2]\,H_1[-s_D(Z+Z^\chi)]
 <-10901825\cdot10^{-18}.
\]
The direct \([m^2]H_0\) is positive in \((48530,48548)10^{-12}\). The new linear term therefore cancels part of that direct coefficient.

For the calculation, on the old rank-four factor write every integral dominant weight in the tensor powers of the sum of standard and dual standards. The shape \((l+1,l+1,l,l)\) is \((\det A)^l\bigwedge^2 A=L^{2l+1}Z\), with good multiplier \(-m^{2l+1}\). At degree two the entire row on \(Z\) is \(-m-m^{-1}\). Pieri adds or removes one box while keeping dominant order. All marked rows are reciprocal in \(m\) by duality, so both exchanged lifts have the same projection. Replace the scalar moment table of the first old rank-four factor in the nine-center calculation by these marked rows and retain the ordinary scalar tables for all other factors. Conditional Haar integration then gives the complete arithmetic projection, including every determinant shift, at each polynomial degree. The uniform degree-28 Taylor remainder for \(H_1\) bounds the projection error since \(\|Z\|_1\le\|Z\|_2=1\) on the arithmetic compact law. The [Arb192 checker](astra-rank-six-67-linear.py) gives \([m^2](H_1Z)\in(37777,37912)10^{-12}\) and uses the direct range \(10^{12}s_D\in(144290995,144291015)\) enclosing the two old lift bounds. The [linear record](astra-rank-six-67-linear.jsonl) uses just the two indicated returned terms at the first refreshed level. Higher powers of these leaves, the other six shifted outputs and the full complementary packet cost require separate accounting. [Earlier source projections and marked moment tables](astra-joint-65.md#the-chosen-amplitude-and-its-signed-coefficients)

1. Combine the entire nonlinear pair \(-s_D(Z+Z^\chi)\) with every old derived multiplier at overlapping levels. A strict physical invariant with the marked and sibling costs across \(2031/128\) passes. A fully debited crossing of 21 with a surviving superlinear coefficient rejects that prescription.
2. For the remaining six outputs, compare specific candidate old representations by bounding ordinary Hom inertia dimensions and computing a single exact positive-correlation separation on a suitable prime. Exceeding the zero-Hom bound and matching an arithmetic eigenline identifies a factor uniformly by the same relative construction. One mismatching normalized good trace disproves a proposed arithmetic identification.
