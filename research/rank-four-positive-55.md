# The rank-four feedback bounds the fourth positive-trial increment

For the actual real stationary marks through eligible primes, the centered degree-16 four-step trial gives
\[
 \limsup_{p\to\infty}\sup_{27/4\le t\le7}|m_p(t)|<0.01699,\qquad
 \limsup_{p\to\infty}\sup_{13/2\le t\le27/4}|m_p(t)|<0.0218 .
\]
It extends the prime \(0.017\) tolerance down to \(27/4\). The arithmetic input is a conditional moment law for \(K(xz)\). Its four rank-four constituents have independent special linear derived groups, also relative to the older fields. The new determinant phases are unnecessary for the second moment and are retained as an inequality for the fourth.

## Boundary weights and the four constituents

Use \(x=\sqrt nKe_0,\ y=K(x^2),\ z=K(xy)\), \(n=(q-1)/2\), as in the [rank-three joint law](joint-law-32.md). Write \(w=K(xz)\). Denote the rank-one Jacobi convolution object by \(L\), and the rank-three objects by \(R,R^\chi\), with superscript \(\chi\) denoting quadratic Kummer twist. The local tables give these Frobenius weights in the fiber functors at the two full Mellin characters.
\[
\begin{array}{c|c|c}
 &1 &\chi\\ \hline
L & -1 & 1\\
L^\vee & 1 & -1\\
R & -1,-1,3 & -1,0,0 .
\end{array}
\]
The negative and positive weights encode the Jordan block sizes at zero and infinity, respectively. In the trace normalization the two lifts of \(L\) are dual. [Katz, Theorem 16.1](https://web.math.princeton.edu/~nmk/mellin331.pdf) · [Rank-three local table](astra-nested-moment-31.md#2-the-actual-new-rank-and-local-monodromy)

Let \(A,B\) be the ordinary quadratic twists by \(\chi(1-a)\) of \(L\star R,L^\vee\star R\), respectively, with \(\star\) the middle convolution. The convolution tensors each fiber by a line. Acting by \(K\) preserves the zero-boundary blocks and switches the infinity characters. Thus
\[
\begin{array}{c|c|c}
 &1 &\chi\\ \hline
A & -2,-2,1,1 & 0,0,0,2\\
B & 0,0,0,0 & -2,-1,-1,4 .
\end{array}                                                       \tag{1}
\]
The rank is four, since the sum of absolute weights over both fibers is eight. Convolution by the invertible \(L\) preserves irreducibility, and twisting the underlying local system preserves it again. The products before the twist have positive inertia type at \(1\) by the even-product closure, so the new objects have negative type there and convolution dimension four. In particular \(1\) is their unique interior singularity. This also applies to \(A^\chi,B^\chi\). [Two-character closure](astra-feedback-52.md#reading-rank-from-two-mellin-characters)

The exact aliases for \(x,z\) give the eight Mellin fields from products of \(L,L^\vee\) with \(R,R^\chi,R^\vee,(R^\chi)^\vee\), times \(q^2/(16n^2)\), with uniform error \(O(q^{-1/2})\) after \(K\). The two signs of the Jacobi and rank-three perverse traces cancel. Lower-rank alias terms are bounded fields with \(O(q^{-1/2})\) coefficients and bounded representation ranks after taking the product and applying \(K\). Errors at bad full characters are confined to the mark, and applying \(K\) to a marked unit has sup norm \(O(q^{-1/2})\). Dualizing a full object commutes with the \(\chi(1-a)\) twist up to a quadratic Kummer twist, by the identity for \(\chi(1-a^{-1})\). As both twists occur in the sum, at a good full character representing the cyclic coordinate we obtain
\[
 w=\frac{q^2}{8n^2}
   \bigl(\Re\operatorname{tr} A+\Re\operatorname{tr} A^\chi+
         \Re\operatorname{tr} B+\Re\operatorname{tr} B^\chi\bigr)
   +O(q^{-1/2}).                                                   \tag{2}
\]
This gives \(|w|\le8+o(1)\) on good frequencies. The one exceptional coordinate is also bounded, by the finite representation ranks. [Exact aliases](joint-law-32.md#2-a-concrete-compact-probability-model) · [Exceptional correction](marked-domain-53.md#the-exceptional-character-stays-at-the-mark)

## Geometric independence and conditional moments

Apply the single-block criterion to \(A^\chi\), with the boundaries exchanged. There is one unipotent block at infinity and none at zero. The unique interior singularity excludes nontrivial multiplicative translates. This gives the connected geometric derived group \(\mathrm{SL}_4\) for \(A^\chi\) and \(A\). [Katz, Theorem 17.1](https://web.math.princeton.edu/~nmk/mellin331.pdf)

For \(B\), the same no-translate criterion gives geometric Lie irreducibility. A proper connected irreducible semisimple subgroup of \(\mathrm{SL}_4\) in dimension four is self-dual in that action. The possibilities are the standard \(\mathrm{Sp}_4\), the third symmetric power of \(\mathrm{SL}_2\), and the tensor product of two standard \(\mathrm{SL}_2\) actions. This follows from the smallest irreducible dimensions in the simple root systems, with \(\mathfrak{sl}_3\) having no four-dimensional irreducible. The normalizer would then preserve the unique nondegenerate invariant bilinear form up to scale. The Frobenius torus at \(\chi\) contains the cocharacter of exponents \((-2,-1,-1,4)\). Indeed taking absolute values of each multiplicative relation on eigenvalues gives its vanishing on the weight vector. Its determinant is one, so its similitude scalar on that form would be trivial. The weights cannot be paired into opposite weights. The arithmetic group normalizes the geometric derived group, giving a contradiction. Hence \(B\) and \(B^\chi\) also have geometric derived group \(\mathrm{SL}_4\). [Katz, the Frobenius-torus argument in Corollary 16.2](https://web.math.princeton.edu/~nmk/mellin331.pdf)

At the trivial full Mellin character the respective centered weight lists of \(A,A^\chi,B,B^\chi\) are
\[
 (-3/2,-3/2,3/2,3/2),\quad (-1/2,-1/2,-1/2,3/2),\quad
 (0,0,0,0),\quad (-2,-1,-1,4).
\]
They are distinct even up to negation. Convolution by a rank-one object shifts all weights by a common value, and duality negates them. A geometric comparison may be made after finite base change, where any extra scalar normalization likewise drops out on centering. Goursat–Kolchin–Ribet therefore gives the full geometric derived product \(\mathrm{SL}_4^4\). Taking the direct sum with the older fields preserves this product acting trivially on the older fields, since their derived factors have types \(\mathrm{SL}_2,\mathrm{SL}_3\). [Katz, Theorem 13.5](https://web.math.princeton.edu/~nmk/mellin331.pdf)

The summed weights also determine the geometric determinant lines. For \(A\) they are \(-2,+2\) at \(1,\chi\), so the line is geometrically \(L^{\star2}\) up to multiplicative translation by Katz's rank-one criterion. This hypergeometric object has its singularity at \(1\). The determinant line belongs to the convolution category generated by an object adapted to \(\{1\}\), so the translation is trivial. For \(B\) all summed weights vanish at both characters, and all other full characters are good already. The determinant has no bad characters, hence is geometrically punctual, with support \(1\) by the same convolution closure. The two quadratic twists have inverse and trivial geometric determinant, respectively. These identifications do not compute the arithmetic constant factors. [Katz, Corollary 16.3 and Lemma 19.4](https://web.math.princeton.edu/~nmk/mellin331.pdf)

On a determinant coset, a real trace of a Haar \(\mathrm{SU}_4\) translate has second moment \(1/2\), odd moments zero, and fourth moment \(3/4+\Re(\det)/8\). Expand the real trace into trace and conjugate. The balanced fourth complex moment is two, the purely holomorphic fourth is the determinant, and the odd moments vanish by \(-I\). Thus for the limit scaling \(1/2\) in (2), the conditional second moment is \(1/2\) and the fourth is at most \(25/32\), independently of the determinant phases.

Precisely, for every fixed continuous \(F(x,y,z)\) the means of \(Fw,Fw^3\) tend to zero, and \(\mathbb E_n(Fw^2)-\mathbb E_n(F)/2\to0\). For nonnegative \(F\), the limsup of \(\mathbb E_n(Fw^4)-25\mathbb E_n(F)/32\) is nonpositive. For fixed polynomial tests, project the algebraic representations to the invariants of the new derived product. The remaining trace terms have no geometrically trivial constituent and mean \(O(q^{-1/2})\) by the fixed-word identity stalk bound. The invariant component is exactly the preceding moment computation, with the fourth bound uniform on arithmetic compact cosets. Boundedness of the coordinates gives the continuous version by approximation. This proves the conditional moment statements through eligible primes and squares without selecting the new determinant phases. [Fixed-word argument](joint-law-32.md#2-a-concrete-compact-probability-model)

## Fourth increment and positive transfer

Use the [same centered trial and third-step notation](nested-positive-54.md). In particular \(S=2x,\ G=V_1-S\), \(G=by+G_{\rm tail}+o(1)\) with tail RMS at most \(\tau+o(1)\), and \(\|\delta_2-\lambda z\|_{2,n}\le\epsilon+o(1)\) for \(\delta_j=V_j-V_{j-1}\). Let \(B_1,B_2\) be the sup bounds for \(V_1,V_2\), and \(\Delta_j\) for \(\delta_j\). Set \(H(u)=\sqrt{4t+u^2}\) and
\[
 h=(4\sqrt t)^{-1},\quad \ell=(H(B_1)+H(B_2))^{-1},\quad
 r=(h+\ell)/2,\quad \nu=4\lambda r.
\]
Replacing the reciprocal secant denominator by \(r\) makes the leading part of the third increment \(K(2rS\lambda z)=\nu w\). The residual norm is at most \(\xi+o(1)\), where
\[
 \xi=
 \frac{(B_1+\Delta_2/2)\epsilon}{H(B_1+\Delta_2/2)}
 +\frac{h-\ell}{2}\lambda(2\sqrt2+2g+\lambda\sqrt{3/4}+a)
 +r\lambda(2g+\lambda/\sqrt2+a)+e_1+e_2,
\]
with \(g=b/2+3\sqrt2\,\tau,\ a=3\sqrt2\,\epsilon\). For the first term use the actual secant slope on the error \(\delta_2-\lambda z\), bounded by the midpoint slope by convexity of \(H\). For the second term bound the denominator error times \(\lambda z(2V_1+\delta_2)\). Here \(g\) bounds \(\|Gz\|_{2,n}\) by independence of \(Y,Z\) and the tail bound, and \(a\) bounds \(\|(\delta_2-\lambda z)z\|_{2,n}\). Also \(\|Sz\|\to\sqrt2\), \(\|z^2\|\to\sqrt{3/4}\). In the constant-denominator term \(\lambda^2 rK(z^2)\), subtract the mean of \(z^2\) since \(K\) kills constants. Its centered norm tends to \(1/\sqrt2\). The \(e_j\) are the polynomial errors.

The fourth midpoint differs from \(S+by+\lambda z+\nu w/2\) by normalized Euclidean norm at most \(\tau+\epsilon+\xi/2+o(1)\). Tilting by \(2w^2\) keeps the older law, gives conditional mean zero to \(w\), and bounds its tilted conditional second moment by \(25/16\). The function \(u\mapsto u^2/(4t+u^2)\) has second derivative bounded above by \(1/(2t)\). Taylor's inequality, conditioning first on older fields and then on \(X\), bounds its tilted mean at the modeled midpoint by
\[
 L_t=1-\sqrt{\frac{t}{t+2}}+\frac{b^2+\lambda^2}{8t}
         +\frac{25\nu^2}{256t}.
\]
The old conditional mean of \(bY+\lambda Z\) given \(X\) vanishes, with second moment \((b^2+\lambda^2)/2\). The first term is the arcsine average at \(S=2\sqrt2\cos\Theta\). These conditioning calculations can be made on any subsequential joint limit of the bounded fields, since the conditional moment identities hold for every continuous older test. The bound is independent of that limit. Convexity of \(H\) on the actual secant, the \(1/(2\sqrt t)\) Lipschitz constant of \(H'\), and the good-frequency bound for \(w\) now give the fourth increment bound
\[
 \nu\sqrt{L_t/2}
 +\frac{(B_2+\Delta_3/2)\xi}{H(B_2+\Delta_3/2)}
 +\frac{4\nu}{\sqrt t}(\tau+\epsilon+\xi/2)+e_2+e_3+o(1).
\]
The same product positivity and marked transfer as in round 54 apply. The [interval checker](rank-four-positive-55-check.py) covers both floor ranges by rational slabs of width \(1/512\), including strict limiting scaled bulk-product lower bounds \(2.6\) and \(1.5\), respectively. Its [two records](rank-four-positive-55-checks.jsonl) certify the scalar margins. The fixed tolerance still requires further control near \(t=1/2\).

1. Determine the constant arithmetic factors relative to the geometric lines \(L^{\star2}, (L^\vee)^{\star2}\) and the two units. An exact Frobenius trace distinguishing the candidate constant factors would decide which determinant contractions enter a signed complex invariant.
2. Retain more of the third increment, for example the term from \(K(yz)\), to reduce \(\xi\) near \(13/2\). Strict product positivity and transfer below \(0.017\) would extend the construction. A larger rigorous actual increment could reject the proposed estimate; loss of scalar slack only rejects its enclosure.
