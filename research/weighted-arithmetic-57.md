# The next feedback has independent rank-five, six, and seven factors

Write \(x=\sqrt n K e_0,\ y=K(x^2),\ z=K(xy),\ w=K(xz)\), and \(u=K(xw)\). Through eligible primes and prime squares the normalized Euclidean and uniform frequency bounds for the new field have the following form. For every fixed continuous test \(g\) of the older fields, every subsequential joint law satisfies
\[
 \mathbb E(U\mid X,Y,Z,W)=\mathbb E(U^3\mid X,Y,Z,W)=0,\qquad
 \mathbb E(U^2\mid X,Y,Z,W)=1/2,\qquad
 \mathbb E(U^4\mid X,Y,Z,W)=3/4 .
\]
Different subsequences can equivalently be avoided by the compact model below. Good frequencies have \(|u|\le23/\sqrt2+o(1)\). The bad cyclic frequency has a uniform bound and costs \(o(1)\) in a normalized Euclidean norm. The four new untwisted constituents also have exact arithmetic determinant lines.

## Constituents and boundary weights

Use \(A,B\) and \(L,L^\vee\) of [round 56](rank-four-arithmetic-56.md). Denote by \(C,D,E,F\) the ordinary twists by \(\chi(1-a)\) of
\[
 L\star A,\quad L^\vee\star A,\quad L\star B,\quad L^\vee\star B,
\]
respectively, where \(\star\) is middle convolution and the perverse normalization is maintained. Their other four constituents are obtained by applying the quadratic Mellin twist \(\chi(a)\). Convolution by an invertible line preserves geometric irreducibility, as does the ordinary twist. The round-52 two-character closure gives positive inertia type at one before this twist and negative type afterward, with no other interior singularity. Tensoring by \(L\) shifts the Deligne weights at \(1,\chi\) by \(-1,+1\); \(L^\vee\) shifts them by \(+1,-1\). The ordinary twist then exchanges the positive weights between the fibers and preserves the negative weights. The sum of absolute weights is twice the generic rank, which here equals convolution dimension. The remaining weights are zero. [Two-character weight calculus](astra-feedback-52.md#reading-rank-from-two-mellin-characters)
\[
\begin{array}{c|c|c|c}
 &\text{dimension}&1&\chi\\ \hline
C&6&-3,-3,1,1,1,3&0,0,0,0,0,0\\
D&5&-1,-1,0,0,1&-1,-1,-1,2,2\\
E&5&-1,-1,-1,-1,5&-1,0,0,0,0\\
F&7&0,0,0,0,0,0,3&-3,-2,-2,1,1,1,1
\end{array}                                                     \tag{1}
\]
Thus the total dimension counting both twists is \(46\). Each object has its unique interior singularity at one, so none admits a nonidentity geometric multiplicative translate. In particular each is geometrically Lie-irreducible. By the single-block criterion, \(E^\chi\) and \(F\) have geometric derived groups \(SL_5\) and \(SL_7\), since one of the two boundary invariant spaces has one block and the other is zero. This also determines the derived groups of \(E,F^\chi\). [Katz, Chapter 17](https://web.math.princeton.edu/~nmk/mellin331.pdf)

For \(D\) use the weight list \((-1,-1,-1,2,2)\) at \(\chi\). After centering and clearing the denominator the associated cocharacter has weights \((-6,-6,-6,9,9)\). This gives a determinant-one cocharacter in the arithmetic normalizer by the Frobenius-torus argument. The connected normalizer of an irreducible connected semisimple group acts by inner automorphisms up to its scalar centralizer, so this cocharacter lies in the connected derived group. In dimension five, every proper connected irreducible semisimple group is self-dual in this representation. Its determinant-one cocharacter weights would be symmetric about zero, which this list excludes. It follows that the derived group is \(SL_5\).

For \(C\) use \((-3,-3,1,1,1,3)\) at \(1\). It is already centered and again excludes all self-dual representations. The dimension-six list leaves two other proper possibilities: the symmetric square of a three-dimensional \(SL_3\) representation, or a tensor product of dimensions two and three. Indeed the simple irreducibles of dimension six are the standard of \(SL_6\) or \(Sp_6\), \(\bigwedge^2\) of \(SL_4\), \(\operatorname{Sym}^2\) of \(SL_3\) and their duals, and \(\operatorname{Sym}^5\) of \(SL_2\). This list follows from the Weyl dimensions for the simple root systems, with \(SO_6\) covered by \(SL_4\). A symmetric square with extremal weights \(-3,3\) has underlying extremal weights \(-3/2,3/2\) and middle weight zero by trace zero. Its six weights disagree with (1). For a tensor product the weights partition into three pairs of the same nonnegative difference. Two occurrences of \(-3\) cannot both have partner \(3\), and pairing each with a \(1\) leaves a pair with difference two. Difference zero fails by the odd multiplicity of \(1\). This excludes the tensor product. Hence \(C\) and \(C^\chi\) have derived group \(SL_6\). [Katz, Corollary 16.2 on Frobenius tori and Chapter 21 on prime dimensions](https://web.math.princeton.edu/~nmk/mellin331.pdf)

In each dimension the weight lists at the trivial character, after centering, distinguish the eight constituents from every other of the same dimension, including after reversal of signs. For the four dimension-five lists the diameters are \(2,3,6,1\). The two dimension-six lists are zero and nonzero. The two dimension-seven lists have diameters \(3,4\). Rank-one convolution twists shift all weights equally and duality negates them. Goursat–Kolchin–Ribet yields the independent product of all eight derived groups. Adding the first rank-two, rank-three, and rank-four fields preserves that derived product acting trivially on the older fields, since their simple factors have smaller dimension and different Lie type. [Katz, Theorem 13.5](https://web.math.princeton.edu/~nmk/mellin331.pdf)

## Arithmetic determinants

The weight sums in (1), together with the one-interior-singularity convolution category, give the geometric determinant lines \(1,L,L^\vee,L^{\star(-3)}\) in order. As in round 56, evaluate in a fiber with no zero weights to find the arithmetic constant. The known boundary determinants of \(A\) at \(1\) are \(q^{-2}\) on the negative and \(q\) on the positive spaces. At \(\chi\) the unique positive eigenvalue of \(A\) is \(q\), from the weight-two eigenvalue of \(L\star R\) at \(1\). Its determinant on the three zero-weight spaces is therefore one, since \(\det A=L^{\star2}\). The positive eigenvalue of \(B\) at \(\chi\) is \(q^2\), and at \(1\) its entire determinant is one. All these identities refer to Deligne fibers. The twist by \(\chi(1-a)\) exchanges the two infinity spaces with arithmetic factor \(\chi(-1)=1\).

| Object and fiber | Negative determinant after the twist | Positive determinant after the twist | Product |
| --- | --- | --- | --- |
| \(C\) at \(1\) | \(q^{-2}q^{-1}=q^{-3}\) | \(q\,q^2=q^3\) | \(1\) |
| \(D\) at \(\chi\) | \(1\cdot q^{-3/2}\) | \(q\,q=q^2\) | \(q^{1/2}\) |
| \(E\) at \(1\) | \(1\cdot q^{-2}\) | \(q^2q^{1/2}\) | \(q^{1/2}\) |
| \(F\) at \(\chi\) | \(q^{-2}q^{-3/2}\) | \(1\cdot q^2\) | \(q^{-3/2}\) |

These products agree with the stated geometric lines, evaluated using \(L(1)=q^{-1/2}\) and \(L(\chi)=q^{1/2}\) in the Deligne fibers. Thus all four constant arithmetic factors are \(+1\) for every odd \(q\equiv1\bmod4\). The four Kummer twists give the inverse determinant lines. The kernel over the Jacobi torus is precisely the derived product, so adjoining the new objects retains equality of the geometric and arithmetic groups by the same surjectivity argument as in [round 56](rank-four-arithmetic-56.md#common-compact-law-and-an-exact-fourth-moment).

## Exact lift feedback and compact moments

Let \(F_5\) be one sixteenth the sum of the eight standard and eight dual Mellin traces of (1) and its twists. As usual extend to the bad frequencies by raw compact traces. If \(a_q,b_q\) are the unnormalized rows of \(A,B\) in round 56, write \(s_A=\sum_a a_q(a)\), \(s_B=\sum_a\chi(a)b_q(a)\), with nonzero \(a\) throughout. Then
\[
 K(C_1F_4)=-F_5+\frac{n(s_A+s_B+q)}{4q^{5/2}}K e_0.                \tag{2}
\]
Here the coefficient is \(O(1)\), as \(|s_A|,|s_B|=O(q^{3/2})\) by their compact boundary weight lists. To verify (2), the four unnormalized rows in order are
\[
 \ell(a)\big(-(\ell_0*f)(a)+k_0+k_1\chi(a)\big),\quad
 (\ell_0,f,k_0,k_1)\in
 \{(\ell,a_q,s_A-h_q,0),(\chi\ell,a_q,h_q,q),
   (\ell,b_q,0,s_B-1),(\chi\ell,b_q,0,1)\}.
\]
The minus sign is the perverse Jacobi trace. For the bad-character corrections, let an eigenvalue \(\lambda\) of weight \(j\) have compact contribution \(q^{-\max(j,0)}\lambda\). Convolution by the line shifts \(j\) by \(+1\) or \(-1\) and multiplies \(\lambda\) by \(q^{1/2}\) or \(q^{-1/2}\). The raw compact Jacobi trace is \(q^{-1/2}\) in both fibers. For a shift by \(+1\), the difference from raw multiplication is therefore \((q^{1/2}-q^{-1/2})\lambda\) on the old negative spaces only. For a shift by \(-1\), it is \((q^{1/2}-q^{-1/2})q^{-j}\lambda\) on the old positive spaces only. Multiply by \(q^{5/2}\) and divide by \(q-1\) in Fourier inversion. Inserting the preceding boundary data yields the displayed \(k_0,k_1\). Restriction to squares identifies both quadratic lifts. Inversion agrees with the dual because all the new stalks at one vanish. Before the ordinary twist each of the four unsigned raw convolutions and its inversion appears twice in \(C_1 F_4\) with coefficient \(1/(16q^{5/2})\), as can also be checked by multiplying the two lift sums. Their sum after \(K\) differs from \(-F_5\) by \((s_A+s_B+q)\ell/(4q^{5/2})\) in position space, giving (2).

For the exact conversion to \(u\), set \(c=\sqrt{q/n}\) and \(D_4=n(1+q+h_q)/(2q^2)\). The round-55 identities \(y=c^2Y/2-x/\sqrt n\) and \(K(C_1Y)=W+C_1/q\) give
\[
 z=(c^3/2)(W+C_1/q)-y/\sqrt n,\qquad
 w=(c^4/2)(F_4-D_4 K e_0)+y/(2n)-z/\sqrt n .
\]
Here \(W\) in the exact first identity denotes the round-55 rank-three lift field. The second equality uses the exact rank-four lift formula and \(K(C_1^2)=y/c^2\). Multiplying the latter identity by \(x=c C_1\) and applying \(K\) produces exactly
\[
 u=(c^5/2)K(C_1F_4)-(c^4 D_4/(2\sqrt n))y+z/(2n)-w/\sqrt n .
\]
All corrections in this expression and (2) are uniformly \(O(n^{-1/2})\), so \(u=-2\sqrt2 F_5+o(1)\).

Thus the leading expression for \(U\) is \(-1/(2\sqrt2)\) times the sum of eight real standard traces, conditionally independent given the Jacobi circle and the old fields. The derived product gives Haar special-unitary factors on their prescribed determinant cosets. A real standard trace at any determinant on \(U(d)\) for \(d\ge5\) has mean and third moment zero, second moment \(1/2\) and fourth moment \(3/4\), by invariance under the center of \(SU(d)\) and the two balanced degree-four contractions. These moments give the stated moments for \(U\) with their exact normalization. The fixed-word averaging argument and polynomial approximation extend the identities to continuous older tests. The support radius follows by summing the 46 standard dimensions and applying the coefficient \(1/(2\sqrt2)\). [Fixed-word averages](joint-law-32.md#2-a-concrete-compact-probability-model)

For a later complex estimate the symmetric weight measure of \(F_5\) at either twist is
\[
 \frac94\delta_0+\frac98(\delta_{-1}+\delta_1)
  +\frac14(\delta_{-2}+\delta_2)
  +\frac5{16}(\delta_{-3}+\delta_3)+\frac1{16}(\delta_{-5}+\delta_5).
\]
The total dimension cost and the first absolute weight moment both equal \(23/4\).

The [checker](weighted-arithmetic-57-check.py) verifies the weight lists, recovers the determinants over the good characters of \(q=5,9\) by exact cyclotomic Newton identities, and checks (2) on every square position in those bases. These [records](weighted-arithmetic-57-checks.jsonl) check finite normalizations. The group and determinant arguments above provide the uniform statements.

1. Test whether the exact signed input in (2) can be added as a fourth distinguished field of the complex invariant. A strict overlapping invariant gives an actual marked continuation. A fully debited escape for the corresponding positive iteration refutes that specific grouping.
