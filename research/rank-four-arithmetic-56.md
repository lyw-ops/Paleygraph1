# Exact arithmetic determinants of the four rank-four feedbacks

For every odd prime power \(q\equiv1\pmod4\), the rank-four objects of [round 55](rank-four-positive-55.md) satisfy the following **arithmetic** identities.
\[
 \det A=L^{\star2},\qquad
 \det A^\chi=(L^\vee)^{\star2},\qquad
 \det B=\det B^\chi=\mathbf1.
\]
Here \(\mathbf1\) is the punctual convolution unit at one. These identities use the actual rank-three normalization from round 32.

## Frobenius on the distinguished boundary spaces

Put \(u=q^{-1/2}\). The trivial-character Deligne fiber of \(L\) has eigenvalue \(u\) from its inertia invariant at zero, and its quadratic-character fiber has eigenvalue \(u^{-1}\) by the arithmetic identity \(L^\chi=L^\vee\). The normalized rank-three \(R\) has the following fiber data.
\[
\begin{array}{c|c|c|c}
 \text{twist} & \text{weights} & \text{determinant} & \text{specified eigenvalue}\\ \hline
 1&-1,-1,3&u^{-1}&q^{3/2}\text{ in weight }3\\
 \chi&-1,0,0&u&u\text{ in weight }-1
\end{array}
\]
The determinants follow from \(\det R=L^\vee\), and the positive-weight eigenvalue was computed in the independent round-32 boundary proof. For the negative-weight eigenvalue in the second row, let \(F\) be the unnormalized ordinary sheaf with trace \(r\), so \(R=F(3/2)[1]\). Its ordinary determinant is \(q^3\) times the Kummer line of \(a(1-a)\). At zero, with uniformizer \(a\), its unramified determinant factor is \(q^3\) since the residual unit of \(a(1-a)\) is one. The two trivial inertia lines have Frobenius determinant \(q^2\) by the rank-two pure stalk computation. The remaining quadratic inertia line consequently has unramified eigenvalue \(q\). Trivializing its inertia by the quadratic twist at zero adds no arithmetic factor in this uniformizer. Weight normalization gives \(q/q^{3/2}=u\). [Ordinary determinant](astra-prime-phase-32.md#1-arithmetic-normalization-of-the-ordinary-hypergeometric-determinant) · [Rank-two stalk and positive-weight eigenvalue](parallel-audit-32.md#2-the-rank-two-stalk-and-its-determinant)

The negative weight spaces of a Deligne fiber come from the inertia invariants at zero, and the positive weight spaces from inertia \(H^1\) at infinity. The intervening proper cohomology is weight zero. Tensor compatibility gives all eigenvalues of the fibers before applying the twist by \(\chi(1-a)\). That twist leaves the negative weight spaces unchanged. At infinity it exchanges the positive weight spaces of the two character fibers, with arithmetic factor \(\chi(-1)=1\) since \(1-a=-(1/a)^{-1}(1-1/a)\). [Katz, Theorem 16.1](https://web.math.princeton.edu/~nmk/mellin331.pdf)

For \(A\) at the trivial character there are two negative and two positive eigenvalues with no weight-zero part. The negative determinant is the product of the two negative eigenvalues of \(L\star R\) at the trivial character. It equals \(u^2u^{-1}/q^{3/2}=q^{-2}\). The positive determinant comes from the two weight-zero eigenvalues of \(R\) at \(\chi\), shifted up by one using \(L\). It equals \(u^{-2}(u/u)=q\). Thus the fiber determinant is \(q^{-1}\), exactly that of \(L^{\star2}\). The geometric comparison in round 55 leaves only an unramified scalar, so this equality selects \(+1\).

For \(B\) at \(\chi\), all three eigenvalues of \(L^\vee\star R\) at \(\chi\) have negative weights. Their product is \(u^3 u=q^{-2}\). The only positive eigenvalue comes from the weight-three eigenvalue of \(R\) at the trivial character, shifted up by one using \(L^\vee\). It equals \(u^{-1}q^{3/2}=q^2\). The full determinant is one. The same geometric comparison now gives \(\det B=\mathbf1\). Quadratic twisting is a symmetric tensor equivalence, fixes constant-field twists, and exchanges the two Jacobi lines, giving the other two identities.

## Common compact law and an exact fourth moment

The independent derived factors in rounds 32 and 55 give the full kernel over the Jacobi torus, and the Jacobi projection is onto. The arithmetic identities above place the arithmetic group inside precisely that same extension, with determinant relations \((J^2,J^{-2},1,1)\) for the new four standard factors. This proves equality of the arithmetic and geometric groups by the kernel-and-surjectivity argument of round 32. Multiplying the older positive-sum variables by their common central element leaves the new determinant constraints unchanged because the two Jacobi exponents are even. Conditional on \(J\), the four new unitary matrices are independent and Haar on their indicated determinant cosets, independently of the earlier two \(SU(2)\) and two \(SU(3)\) cosets. Set \(W\) to half the sum of the new four real traces as in round 55. The fixed-word argument yields this common joint law for \((x,y,z,w)\) through varying primes and squares. [Older compact model](joint-law-32.md#2-a-concrete-compact-probability-model) · [Rank-four independence and normalization](rank-four-positive-55.md#geometric-independence-and-conditional-moments)

In particular the conditional fourth moment is exact. With \(X=\sqrt2\Re J\),
\[
 \mathbb E(W^4\mid X,Y,Z)
 =\frac34+\frac{2+2\Re(J^2)}{128}
 =\frac34+\frac{X^2}{64}.
\]
In the first expression \(2+2\Re(J^2)=4(\Re J)^2\) depends only on \(X\). The factor \(1/128\) is \(1/16\) from the half-sum times \(1/8\) from the real trace fourth moment. In particular \(\mathbb E W^4=49/64\). This determines the signed degree-four determinant contractions for the two rank-four families, including which contributions are punctual.

## Exact finite normalization check

Write \(\ell(a)=\chi(1-a)\), \(h_q=(\ell*\ell*\ell)(1)\), and let \(r\) be the rank-three unnormalized ordinary trace as above. The unnormalized perverse trace rows of \(A,B\), obtained by multiplying their traces by \(q^2\), are
\[
 a_q(a)=\ell(a)\big((\ell*r)(a)+1+q\chi(a)\big),\qquad
 b_q(a)=\ell(a)\big(((\chi\ell)*r)(a)+h_q\big).
\]
For the convolution before the \(\ell(a)\) twist, raw compact convolution gives the right transform at every good character. At a bad character, retrieve the compact Mellin eigenvalues from the Deligne fiber by replacing each positive-weight eigenvalue of weight \(j\) by \(q^{-j}\) times that eigenvalue. This exchanges \(H^1\) of the local unipotent block at infinity with its invariant line. All other eigenvalues remain unchanged. The trivial-character compact trace of \(R\) is \((h_q+1)/q^{3/2}\). Its quadratic-character trace equals the full Deligne trace there, since there are no positive weights. Both raw traces of \(L\) and \(L^\vee\) at the two bad characters equal \(q^{-1/2}\). It follows that the compact Mellin correction to the unnormalized first convolution is \(q-1\) at the trivial character and \(q(q-1)\) at the quadratic character. The correction for the second convolution is \(h_q(q-1)\) at the trivial character and zero at the quadratic character. Inverse Fourier transform gives the three displayed positional terms. Omitting this correction before twisting would change even the good Mellin traces of \(A,B\).

The [checker](rank-four-arithmetic-56-check.py) constructs both rows over extension degrees one through four and folds them by the norm to each base. For all 18 good characters over the base fields \(5,9,13\), it recovers each determinant by the fourth Newton identity in the exact cyclotomic quotient. The unnormalized targets are \(q^7 J(\alpha,\chi)^2\) and \(q^8\). Twisting by \(\chi\) just exchanges two tested characters. The [three records](rank-four-arithmetic-56-checks.jsonl) check those normalizations independently of the determinant products. The field-uniform assertion follows from the fiber calculation.

## The next distinguished complex feedback

Use the exact lift fields \(C_1,W\) of [round 55](astra-rankthree-55.md#exact-feedback-and-arithmetic-weights). Define \(F_4\) as one eighth the sum of the standard and dual Mellin traces for \(A,A^\chi,B,B^\chi\), extending to the two bad characters by their raw compact Mellin traces. The product \(C_1W\) is the corresponding sum for \(L\star R,L^\vee\star R\), their quadratic twists and their duals, at good characters. Both positive-sum factors change sign when written in perverse coordinates, so the product has positive sign. Restriction to squares and then applying \(K\) gives
\[
 K(C_1W)=F_4-\frac{n(1+q+h_q)}{2q^2}K e_0 .
\]
Indeed, with \(r^\vee(a)=r(a^{-1})\), the raw positional row of \(C_1W\) is \(1/(8q^2)\) times the restriction of \((\ell+\chi\ell)*(r+\chi r+r^\vee+\chi r^\vee)\). On squares, this convolution is twice the sum of \(\ell*r,(\chi\ell)*r\) and their inversions, since \(\ell(a^{-1})=\chi(a)\ell(a)\). Apply \(K\) by multiplying this row by \(\ell\). The row of \(F_4\) is \(1/(4q^2)\) times the sum of \(a_q,b_q\) and their inversions, since the two Kummer lifts coincide on squares. For \(A,B\) the middle-extension stalk at \(1\) vanishes. Duality therefore gives the conjugate inverse trace at every nonzero position, using purity at the lisse positions. The rows differ by \((1+q+h_q)\ell/(2q^2)\) on squares. The transform of \(\ell|_Q/n\) is \(K e_0\). The identity is also checked at all square positions in the three small replay fields, and \(|h_q|\le2q\) from the pure rank-two stalk gives the \(O(1)\) coefficient required in the complex invariant.

In the notation of the complex packet bounds, the weighted fiber measure of \(F_4\) is the same at \(1,\chi\). Using the rank-four table and its sign-reversed duals, it is
\[
 D_{F_4}=\frac74\delta_0+\frac12(\delta_{-1}+\delta_1)
         +\frac12(\delta_{-2}+\delta_2)+\frac18(\delta_{-4}+\delta_4).
\]
Its quadratic unit has coefficient \(1/8\), from the eight ordered standard–dual pairings. In degree two the two dual exterior squares of \(A,A^\chi\) shift by the inverse determinant lines \(L^{\star(-2)},L^{\star2}\), respectively. The exterior squares of the two unit-determinant factors are self-dual. In degree four the eight pure determinant contractions have Jacobi exponents \(2,-2,0\) with multiplicities \(2,2,4\), respectively, before the overall coefficient \(8^{-4}\). Thus all the shifts and units in those contractions are known on both prime families.

1. Insert the four arithmetic standard factors and their duals into the next signed complex invariant. The quadratic unit and exterior-power terms must combine with their actual Jacobi exponents before taking magnitudes. Test whether the new invariant overlaps the established section and reaches below the full rank-three escape floor.
