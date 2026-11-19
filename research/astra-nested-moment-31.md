# A rank-three reduction of the nested Paley field

> Round-32 update: the determinant sign left open below is now
> [uniformly positive](astra-prime-phase-32.md), with an
> [independent proof](parallel-audit-32.md) in the Paley congruence range.
> The [joint law of this family](joint-law-32.md) extends the listed moments.

2026-11-18. New calculation for the nested field, not a reuse of the
unnested path-column law. No ordinary-theta endpoint conclusion is claimed.

**Result.** For every odd prime power \(q\equiv1\pmod4\), with the
normalizations of round 30,

\[
 \langle x^2z^2\rangle=\frac12+O(q^{-1/2}),\qquad
 \langle z^4\rangle=\frac34+O(q^{-1/2}).                         \tag{1}
\]

The implied constants are absolute for these fixed words, independent of
the characteristic and extension degree. Thus (1) applies both to varying
primes \(p\equiv1\pmod4\) and to all odd prime squares \(r^2\), with errors
\(O(p^{-1/2})\) and \(O(r^{-1})\), respectively. It also applies in fixed
odd characteristic as the allowed field orders increase. No assertion of
a common full arithmetic group at different fields is needed.

**Additional square-field result.** Vertical reality proves that the
remaining determinant phase is a sign, and is \(+1\) on every odd square
field. Consequently

\[
 \langle xz^3\rangle=\frac18+O(r^{-1})\qquad(q=r^2,\ r\text{ odd}).
                                                               \tag{1a}
\]

For primes \(p\equiv1\pmod4\), the proof gives
\(\langle xz^3\rangle=c_p/8+O(p^{-1/2})\), with \(c_p\in\{1,-1\}\);
the general prime sign is not identified. Section 6b separately verifies
finite certificates selecting \(+1\) at \(p=9413,153649\).

The proof identifies the new generator as a reflected rank-three
hypergeometric sheaf, proves that its two quadratic twists have independent
\(SL_3\) derived factors, and computes the invariant contractions.
Section 6 reduces the remaining prime test to one explicit constant-field
sign, rather than to an unspecified nested word. Section 6a proves the
square result without a global rational model or a cross-prime
finite-Artin assumption.
The proof is supplied for independent review; numerical checks below
verify the exact reductions and normalizations, not the sheaf arguments.

## 1. An exact Pfaff reduction before taking moments

Write \(\chi(0)=0\), \(G=\mathbb F_q^\times\), \(Q=G^2\),
\(n=(q-1)/2\). Use unnormalized multiplicative convolution on the indicated
group. On the full group put

\[
 \ell(a)=\chi(1-a),\quad
 L(a)=\sum_{v\in\mathbb F_q}\chi(v(v-1)(v-a)),\quad
 B(h)=\sum_{v\in\mathbb F_q}\chi(v(v-h))L(v).                   \tag{2}
\]

For nonzero arguments, \(L=\ell*\ell\) and \(B=\ell*\ell*\ell\).
The formulas in (2) also define their values at zero, without extending
the group convolution to zero. In particular \(L(1)=-1\), \(B(0)=1\).
Inversion gives

\[
 L(a^{-1})=\chi(a)L(a),\qquad B(a^{-1})=\chi(a)B(a).            \tag{3}
\]

Let \(D=\ell*(\ell L)\) on \(G\). The useful exact identity is

\[
 D(a)=1+\chi(a)B(1-a^{-1})\quad(a\ne0).                       \tag{4}
\]

Here is an elementary proof, including the correction (1).
For \(v\ne1\), the change of variable in the cubic character sum gives

\[
 L\left(\frac v{v-1}\right)=\chi(1-v)L(v).
\]

For \(a\ne0,1\), substitute \(w=v/(v-1)\) in
\(D(a)=\sum_v\chi(v(v-a))\chi(1-v)L(v)\). The new summand is
\(\chi(w((1-a)w+a))L(w)\). Completing the sum at \(w=1\) subtracts
\(L(1)=-1\). Consequently

\[
 D(a)=1+\chi(1-a)B\left(\frac a{a-1}\right)
     =1+\chi(a)B(1-a^{-1}).
\]

At \(a=1\) the same calculation before factoring (1-a) gives
\(D(1)=1+B(0)=2\). This proves (4) everywhere required.

In particular, the full-group nested positional row is exactly
$\ell D=r\circ\mathrm{inv}+\ell$. Thus the full-character field
$K_G(JK_G(J^2))$ is $A_{\alpha^{-1}}+J_\alpha/q$.
Its pure rank-three part is the convolution **dual** of the generator
chosen below. This distinguishes the two determinant orientations in a
cubic probe and fixes the local blocks without guessing them from a
compactly supported fiber rank.

On \(Q\), write

\[
 s=\ell|_Q,\quad h=s*s,\quad t=sh,\quad u=s(s*t),\quad
 r(a)=\chi(1-a)B(1-a)\quad(a\in G).                           \tag{5}
\]

Then the nested kernel has the exact reduction

\[
 \boxed{\quad
 4u(a)=r(a)+r(a^{-1})-4t(a)+2s(a),\quad a\in Q.
 \quad}                                                        \tag{6}
\]

Equivalently,

\[
 4u(a)=s(a)\{B(1-a)+B(1-a^{-1})-2L(a)+6\}.                    \tag{7}
\]

For a direct check of (7), expand the two square indicators in the
diamond sum

\[
 u(a)=s(a)\sum_{b,c\in Q}
   \chi((1-b)(b-a)(b-c)(c-a)).
\]

For \(a\in Q\setminus\{1\}\), the four completed full-field sums
with additional weights \(1,\chi(b),\chi(c),\chi(bc)\) are, in that order,

\[
 1,\quad -L(a),\quad B(1-a^{-1}),\quad 1+B(1-a).               \tag{8}
\]

Removing the zero-variable boundaries changes these to
\(2-L(a),2-L(a),1+B(1-a^{-1}),1+B(1-a)\).
For the third completed sum, use \(b=a+(1-a)v,c=a+(1-a)w\), then (3).
For the fourth, the quartic character sum in \(b\) is

\[
 \sum_b\chi(b(b-1)(b-a)(b-c))
 =\chi(a-c)L\left(\frac{c(a-1)}{a-c}\right)-1
 \quad(c\ne a).
\]

It follows by \(b=av/(v-1)\); the excluded \(v=1\) contributes (1).
Multiplication by \(\chi(c(c-a))\), followed by the displayed fractional
linear change in \(c\), gives the fourth entry of (8). The term \(c=a\)
has zero weight. Summing the four boundary-corrected entries proves (7).
Use \(h(a)=(L(a)-2)/2\) off (1) to obtain (6). At \(a=1\), both sides
of (6) and (7) vanish.

Thus the nine-variable expression from round 30 has the exact reduction

\[
 \langle xz^3\rangle
 =\frac1{64n^5}\sum_{a,b,c\in Q}s(abc)W(a)W(b)W(c),\qquad
 W=r+r\circ\mathrm{inv}-4t+2s.                                \tag{9}
\]

This is a three-variable correlation of explicitly identified
hypergeometric traces with all lower-order corrections retained. It is
not by itself an estimate of that correlation.

## 2. The actual new rank and local monodromy

The full-group triple convolution \(B\) is the trace, up to the harmless
constant normalization and perverse shift, of the rank-three balanced
hypergeometric with upstairs parameters \(1,1,1\) and downstairs
parameters \(\chi,\chi,\chi\). The disjoint parameter sets give geometric
irreducibility; the ordinary trace has weight two. The local monodromies
at \(0,1,\infty\) are

\[
 \operatorname{Unip}(3),\quad 1\oplus1\oplus\chi,
 \quad\chi\otimes\operatorname{Unip}(3).
\]

These standard hypergeometric inputs, including the pseudoreflection at
one, are in [Katz, *G₂ and hypergeometric sheaves*, §2](https://web.math.princeton.edu/~nmk/g2hyper62finalcorr.pdf).
Here and below the symbol \(\chi\) in a local table denotes the
nontrivial quadratic tame inertia character. It is not a constant-field
quadratic sign.

Let \(\mathcal R\) be the middle-extension perverse object with trace

\[
 \operatorname{tr}(\mathcal R,a)=-q^{-3/2}r(a),\qquad a\in G,
\]

obtained by reflection \(a\mapsto1-a\), twisting by
\(\mathcal L_{\chi(1-a)}\), weight normalization, and shift \([1]\).
Set \(\mathcal R'=\mathcal R\otimes\mathcal L_{\chi(a)}\).
The local table, now on the actual parameter \(a\), is

| Object | 0 | 1 | \(\infty\) |
|---|---|---|---|
| \(\mathcal R\) | \(1\oplus1\oplus\chi\) | \(\chi\operatorname{Unip}(3)\) | \(\operatorname{Unip}(3)\) |
| \(\mathcal R'\) | \(\chi\oplus\chi\oplus1\) | \(\chi\operatorname{Unip}(3)\) | \(\chi\operatorname{Unip}(3)\) |

Both have generic rank three and convolution dimension three: the only
interior rank drop is three at one, and both boundaries are tame. The
stalk at one vanishes. Reflection does not change geometric
irreducibility. There is no nonidentity multiplicative translation
preserving the unique interior singularity.

For \(\mathcal R'\), the unipotent part at zero is one block of size one;
at infinity it is zero. Applying [Katz, *Convolution and Equidistribution*,
Theorem 17.1](https://web.math.princeton.edu/~nmk/mellin331.pdf) gives

\[
 G_{\mathrm{geom},\mathcal R'}=G_{\mathrm{arith},\mathcal R'}=GL_3.
                                                                    \tag{10}
\]

Quadratic Kummer twisting is a tensor equivalence for convolution, so
the same holds for \(\mathcal R\). This proves the rank-three assertion;
it does not infer rank from the numerical fourth moment.

## 3. Excluding a hidden coupling between the two rank-three factors

It remains essential to prove joint independence of the derived factors.
The usual one-Jordan-block hypothesis at every boundary character fails
for \(\mathcal R\) at zero. Thus merely citing the general rank-growth
criterion in Katz's Theorem 20.3 would be incorrect here. The following
special calculation supplies the missing step.

**Rank lemma.** For every nonpunctual convolution-dimension-one object
\(\mathcal L\),

\[
 \operatorname{rk}(\mathcal R*_{\mathrm{mid}}\mathcal L)>3.
                                                                    \tag{11}
\]

Indeed such an object is a multiplicative translate of an irreducible
hypergeometric, of generic rank \(h\ge1\). Write \(i_0,i_\infty\) for
the dimensions of the boundary invariants in the generic multiplication
fiber. Euler characteristic and the boundary exact sequence give

\[
 \operatorname{rk}(\mathcal R*_{\mathrm{mid}}\mathcal L)
       =3+3h-i_0-i_\infty.                                    \tag{12}
\]

For completeness, the (3+3h) is the compactly supported first
cohomology dimension: the tame factor has rank and convolution dimension
both three, and the other factor has rank \(h\), dimension one.
There is no zeroth or second cohomology, since a dimension-three simple
object cannot be a translate of a dimension-one object's convolution
dual. Passing from compact support to middle image removes exactly the
two boundary invariant spaces. This is the boundary sequence used in
Katz's proof of Theorem 20.3, pp. 115–116.

At each boundary of an irreducible hypergeometric, every tame character
has just one Jordan block. Therefore the table in §2 gives

\[
 i_0\le3,\qquad i_\infty\le h.
\]

For \(h\ge2\), (12) is at least (2h>3). For \(h=1\), equality
\(i_0+i_\infty=3\) would require the other object's tame character to
be trivial at **both** boundaries: two invariants against the two
trivial lines at zero, and one against the unipotent block at infinity.
A rank-one irreducible hypergeometric cannot have those two matching
parameters. In type \(1,1\) they would cancel; types \(1,0\) and
\(0,1\) have one wild boundary. Thus \(i_0+i_\infty\le2\), and (12)
is at least four. This proves (11).

The assertion also holds with \(\mathcal R'\) in place of
\(\mathcal R\), by Kummer twisting, and with their convolution duals,
by dualizing. A punctual dimension-one object gives a translation.
The unique singularity forces that translation to be the identity.
But \(\mathcal R\not\cong\mathcal R'\) by the zero-inertia table, and
\(\mathcal R\not\cong(\mathcal R')^\vee\): the latter has a single
size-three Jordan block at zero, while \(\mathcal R\) has three
size-one blocks there. Hence none of the forbidden isomorphisms up to
a rank-one convolution twist exists.

The Goursat criterion, [Katz, Theorem 13.5](https://web.math.princeton.edu/~nmk/mellin331.pdf), now yields

\[
 SL_3\times SL_3\ \subseteq\ G_{\mathrm{geom},\mathcal R\oplus\mathcal R'}
 \ \subseteq\ G_{\mathrm{arith},\mathcal R\oplus\mathcal R'}
 \ \subseteq\ GL_3\times GL_3.                                \tag{13}
\]

This is an inclusion, not a claim of \(GL_3^2\): the determinants are
indeed geometrically coupled. Adding the old Jacobi object and the two
Legendre objects preserves an independent \(SL_3^2\times SL_2^2\)
derived subgroup. The \(SL_3\) and \(SL_2\) simple Lie algebras are
nonisomorphic, so Goursat cannot identify their factors; adjoining the
one-dimensional Jacobi object does not alter the derived subgroup.
This identifies the new derived factors relative to both old families.

## 4. Exact spectral normalization and uniform error

For a full multiplicative character \(\alpha\), put

\[
 J_\alpha=q^{-1/2}\sum_{a\in G}\alpha(a)\ell(a),\qquad
 A_\alpha=q^{-3/2}\sum_{a\in G}\alpha(a)r(a),\qquad
 C_\alpha=A_{\alpha\chi}.
\]

The last two arrays are minus the Mellin traces of
\(\mathcal R,\mathcal R'\). Their complex conjugates correspond to
the convolution duals at good characters. The minus signs cancel in
all the fourth-degree tests here. For any lift \(\alpha\) of a character
of \(Q\), (6) gives exactly

\[
 \begin{split}
 x&=a_q(J_\alpha+J_{\alpha\chi}),\quad
       a_q=\frac{\sqrt q}{2\sqrt n},\\
 z&=b_q(A_\alpha+C_\alpha+\overline{A_\alpha}
                  +\overline{C_\alpha})
       -\frac y{\sqrt n}+\frac x{2n},\quad
       b_q=\frac{q^{3/2}}{8n^{3/2}}.
 \end{split}                                                    \tag{14}
\]

In the first line \(J_{\alpha\chi}=\overline{J_\alpha}\) at good
characters (and in fact the character-sum conjugation equality holds
at the two exceptional characters too). The good Jacobi traces have
modulus one. Mellin dimensions bound \(A,C\) by three, and the known
first-feedback bound bounds \(y\) uniformly. Thus the explicit
correction in the second line is uniformly \(O(q^{-1/2})\).

The all-character averages of any fixed trace word used below equal
the Frobenius trace on its geometric invariant space, plus
\(O(q^{-1/2})\). One can use the fixed-word proof already given in
[parallel-witness-6.md](parallel-witness-6.md): the present inputs too
are tame, of fixed rank, and lisse off one. Successive middle
convolutions have bounded rank and singularity set; nonpunctual stalks
have weight at most minus one. Boundary ranks bound the number of bad
characters. Adding back those characters costs \(O(q^{-1})\).
All these bounds are uniform in odd characteristic; only fixed tensor
degrees occur. Averaging over full characters gives exactly the
subgroup-coordinate average for the lift-invariant expressions (14).

## 5. The two invariant calculations

Write \(V,W\) for the two standard three-dimensional representations
in (13). At total \(z\)-degree two, the only derived invariants are
the two evaluation pairings \(V\otimes V^\vee\) and
\(W\otimes W^\vee\), each in both possible orders. Each is fixed by
the full arithmetic group: evaluation is canonical. Hence, for
\(S=A+C+\bar A+\bar C\), its square projects to (4).

Adjoining the Jacobi torus gives

\[
 \operatorname{inv}\big[(J+\bar J)^2 S^2\big]=2\cdot4=8.
\]

The \(J^{\pm2}\) terms have no invariant, as the Jacobi geometric
group is the full torus. No determinant tensor of \(V\) or \(W\) can
appear at degree two. In particular unknown arithmetic determinant
phases cannot change this computation. Equations (14) yield

\[
 \langle x^2z^2\rangle
 =8a_q^2b_q^2+O(q^{-1/2})
 =\frac{q^4}{32n^4}+O(q^{-1/2})
 =\frac12+O(q^{-1/2}).                                       \tag{15}
\]

At total degree four, a single factor has two invariant contractions
in \(V^{\otimes2}\otimes(V^\vee)^{\otimes2}\), and there are
\(\binom42=6\) placements. This contributes (12) for each of \(V,W\).
Splitting two positions to each factor contributes
\(\binom42\cdot2\cdot2=24\). These are all the invariants: an
imbalance of three within a factor would leave a single unpaired trace,
in that factor or in the other factor. Consequently

\[
 \operatorname{inv}(S^4)=12+12+24=48.
\]

The two-contraction spaces are spanned by identity and permutation;
arithmetic Frobenius fixes both. Therefore

\[
 \langle z^4\rangle
 =48b_q^4+O(q^{-1/2})
 =\frac{3q^6}{256n^6}+O(q^{-1/2})
 =\frac34+O(q^{-1/2}).                                       \tag{16}
\]

These are new nested-word computations. In particular they do not
follow from the first-feedback law or the path-column groups.

## 6. What the preferred test \(\langle xz^3\rangle\) still needs

There is a further geometric reduction. Let \(\mathcal M\) denote the
Jacobi object with Mellin trace \(-J_\alpha\), so that
\(\mathcal M\otimes\mathcal L_\chi\cong\mathcal M^\vee\)
arithmetically. The determinant weight calculation from the local table
is as follows. For \(\mathcal R\), the character (1) has two
size-one blocks at zero and one size-three block at infinity; its net
determinant weight is \(-2+3=1\). The character \(\chi\) has one
size-one block at zero and none at infinity; its weight is (-1).
Thus the determinant is geometrically the hypergeometric of type
\(1,1\) with upstairs \(\chi\), downstairs (1). There is no
translation, since tensor constructions remain singular only at one.
The weight recipe is Corollary 16.3 and the singularity assertion is
Lemma 19.3 of [Katz's book](https://web.math.princeton.edu/~nmk/mellin331.pdf).
It follows that

\[
 \det\mathcal R\cong_{\rm geom}\mathcal M^\vee,
 \qquad \det\mathcal R'\cong_{\rm geom}\mathcal M.              \tag{17}
\]

Keep the arithmetic scalar instead of silently discarding it. For each
base field there is a unitary constant-field twist \(c_q^{\deg}\) with

\[
 \det\mathcal R=c_q^{\deg}\otimes\mathcal M^\vee,
 \qquad \det\mathcal R'=c_q^{\deg}\otimes\mathcal M.            \tag{18}
\]

The same scalar occurs because Kummer twisting is a symmetric tensor
equivalence, fixes constant twists, and exchanges the two Jacobi objects.
This statement is fieldwise; it does not assert finite image or a common
cross-prime model for \(c_q\).

At cubic degree in \(S\), the only derived invariant terms are
\(\det\mathcal R,\det\mathcal R',
(\det\mathcal R)^{-1},(\det\mathcal R')^{-1}\), each once.
Multiplying by the Jacobi factor and using (18) leaves
\(2(c_q+c_q^{-1})\). Therefore the explicit remaining arithmetic task is

\[
 \boxed{\quad
 \langle xz^3\rangle
   =\frac{\operatorname{Re}c_q}{8}+O(q^{-1/2}).
 \quad}                                                       \tag{19}
\]

For a construction based over \(\mathbb F_r\), extension to
\(\mathbb F_{r^e}\) raises this scalar to \(c_r^e\), with compatible
normalizations. Geometric \(GL_3\), purity, and (17) alone do not justify
removing \(c_q\). The additional reality argument below proves that its
square is one; it still does not select the prime sign.
The diagnostics \(\mathbb E[A^3J]\) in the replay directly test this
scalar with the correct orientation; \(\mathbb E[A^3\bar J]\) is a
different, asymptotically vanishing contraction.

## 6a. Vertical reality forces a sign and evaluates the square main term

The constructions needed for this paragraph are defined over **every**
odd field \(\mathbb F_b\), including \(b\equiv3\pmod4\). Define \(\ell\)
as before and define \(B=\ell*_{G}\ell*_{G}\ell\) directly on \(G\).
For the reflection put \(r(a)=\chi(1-a)B(1-a)\) for \(a\ne1\) and
\(r(1)=0\). Do not use the cubic-sum expression (2) without its
\(\chi(-1)\) correction when \(b\equiv3\pmod4\).
These full convolution and Kummer constructions commute with base
change. The local inertia table in §2 and the determinant weight
calculation (17) are unchanged. Only unramified local constants can
change. Thus over every odd base field there is an arithmetic identity

\[
 \det\mathcal R_b=c_b^{\deg}\otimes\mathcal M_b^\vee,\quad |c_b|=1.
                                                               \tag{20}
\]

Here is why the determinant direction in (20) does not require
\(\chi_b(-1)=1\). The Jacobi object has geometric boundary parameters
\((1;\chi)\), and its convolution dual has \((\chi;1)\), in every odd
characteristic. For \(\mathcal R_b\), the local blocks in §2 give
determinant weights \(+1\) at character \(1\), and \(-1\) at character
\(\chi\), exactly as above. Consequently its geometric determinant has
parameters \((\chi;1)\) over every odd base field. The singularity
argument removes the translation. All unramified discrepancies are
retained in \(c_b^{\deg}\).

In contrast, the arithmetic identification involving a Kummer twist is

\[
 \mathcal M_b^\vee
   =\chi_b(-1)^{\deg}\otimes
        (\mathcal M_b\otimes\mathcal L_{\chi_b}).
                                                               \tag{20a}
\]

It follows directly from
\(\ell(a^{-1})=\chi_b(-1)\chi_b(a)\ell(a)\), or from Verdier duality
and inversion of the normalized quadratic Kummer object. Thus
\(\mathcal M_b\otimes\mathcal L_{\chi_b}=\mathcal M_b^\vee\) is
**not** used at \(b\equiv3\pmod4\). Nor is the two-twist identity (18)
used in proving (23). The single identity (20), paired with
\(\mathcal M_b\) itself, is sufficient and fixes the contraction as
\(A^3J\), with no \(\chi_b(-1)\) prefactor.

Normalize half Tate twists by the positive real \(\sqrt b\); its \(e\)-th
power is the positive \(\sqrt{b^e}\). This ensures that the normalization
also commutes with extension. Define \(A_{b^e},J_{b^e}\) by the full
character sums in §4, using the directly convolved \(B\).

There is exactly one geometric invariant in
\(\mathcal R_b^{\otimes3}\otimes\mathcal M_b\): the alternating
determinant tensor, paired with \(\mathcal M_b\). Equation (20) says
that its arithmetic Frobenius trace at degree \(e\) is \(c_b^e\).
The fixed-word estimate, or just its vertical version at this fixed
base field, therefore gives

\[
 T_e:=\frac1{b^e-1}\sum_{\alpha}
          A_{b^e,\alpha}^{\,3}J_{b^e,\alpha}
       =c_b^e+O_b(b^{-e/2}).                                  \tag{21}
\]

The left side is **exactly real**, before taking a limit. The positional
rows \(r,\ell\) are real integers, so the character inversion
\(\alpha\mapsto\alpha^{-1}\) conjugates the summand. More explicitly,
orthogonality gives the rational number

\[
 T_e=\frac{(r*r*r*\ell)(1)}{(b^e)^5}.
                                                               \tag{22}
\]

Equations (20)–(22) hold for **every** \(e\ge1\), including odd \(e\)
when \(b\equiv3\pmod4\). Neither the Paley subgroup symmetry nor the
Pfaff formulas from §1 enter this argument. Restricting (21) to even
extensions would indeed be insufficient to conclude (23).

This reasoning does not extract a rational top-weight summand from a
rational total trace. Instead, (21) and reality imply
\(\operatorname{Im}(c_b^e)\to0\) for **all** positive integers \(e\).
Writing \(c_b=e^{i\theta}\), the identity

\[
 \sin\theta=\sin((e+1)\theta)\cos(e\theta)
                -\cos((e+1)\theta)\sin(e\theta)
\]

then gives \(\sin\theta=0\). Hence

\[
                 c_b\in\{1,-1\}\quad\text{for every odd }b.      \tag{23}
\]

In particular base change from any odd \(\mathbb F_b\) to its quadratic
extension gives \(c_{b^2}=c_b^2=1\). The field \(b^2\) is \(1\pmod4\),
so the subgroup normalization and invariant calculation (19) apply
there. They give (1a), with a uniform \(O(b^{-1})\) error from the
already uniform fixed-word estimate.

This proves the preferred cubic mixed leading term on squares, including
squares of primes \(3\pmod4\). It does not identify \(c_p\) at prime
orders \(p\equiv1\pmod4\), nor does it construct a global rank-one
Galois representation unramified outside two. No inference from the
positivity of finitely many numerical traces is used. Indeed the exact
full trace (22) at \(b=3,e=1\) is negative, \(-1/243\); small finite
traces cannot be substituted for their leading invariant trace.

## 6b. Audit of the finite prime sign certificate

The separate main-line [certificate script](nested-phase-31.py) uses the
correct orientation and admits the explicit bound

\[
 \left|\frac{(r*r*r*\ell)(1)}{q^5}-c_q\right|
       \le \frac{108}{\sqrt q}+\frac{1080}{q-1}.                \tag{24}
\]

This is a finite-field inequality, not merely an unspecified asymptotic
error. Here is an audit of its constants.

Let \(\mathcal W=\mathcal R^{*3}_{\rm mid}*_{\rm mid}\mathcal M\).
Its convolution dimension is \(3^3=27\). For the successive tame,
semisimple factors adapted to \(\{1\}\), generic rank satisfies

\[
 r(X*_{\rm mid}Y)\le r(X)d(Y)+r(Y)d(X).
\]

On a generic multiplication fiber the compactly supported second
cohomology vanishes: two nonpunctual irreducible constituents could
produce it only if one were the moving inverse-dual translate of the
other. Their interior singularities prevent that at generic parameter.
There are no tame, everywhere-lisse nonpunctual constituents in
\(\mathcal P\), since those would be shifted Kummer sheaves.
Euler characteristic gives the displayed upper bound for ! convolution,
and middle image cannot increase the rank. Punctual constituents also
respect the bound, contributing their dimension times the other rank.

Starting from \((r,d)(\mathcal R)=(3,3)\) and
\((r,d)(\mathcal M)=(1,1)\), the rank bounds are therefore

\[
 r(\mathcal R^{*2})\le18,\quad
 r(\mathcal R^{*3})\le18\cdot3+3\cdot9=81,\quad
 r(\mathcal W)\le81+27=108.
                                                               \tag{25}
\]

The unique geometrically trivial punctual component of \(\mathcal W\)
has trace \(c_q\). All remaining constituents are nonpunctual, with
total generic rank at most 108. Their weight-minus-one stalk bound at
one costs at most \(108/\sqrt q\). There are no punctual components
away from one, since the tensor category remains adapted to \(\{1\}\).

For the input direct sum
\(\mathcal R^{\oplus3}\oplus\mathcal M\), generic rank is ten, hence
there are at most 20 bad characters. This is deliberately conservative:
the repeated copies are not needed to get a smaller bound. At a good
character, the raw product \(A_\alpha^3J_\alpha\) equals the Mellin
trace of \(\mathcal W\). At every character, including bad ones,

\[
 |A_\alpha^3J_\alpha|\le27,\qquad |m_{\mathcal W}(\alpha)|\le27.
\]

Indeed compactly supported cohomology is concentrated in degree zero,
has dimension equal to convolution dimension after a tame Kummer
twist, and has weights at most zero. This uses
[Katz, Lemma 2.1 and the good-character discussion on pp. 13–14](https://web.math.princeton.edu/~nmk/mellin331.pdf).
Each discrepancy is consequently at most 54. Averaging at most 20
such discrepancies gives \(1080/(q-1)\). Finally, full-character
orthogonality averages \(m_{\mathcal W}\) to the stalk at one.
Together with (25), this proves (24).

The positional reconstruction in the certificate is also correct:
its full raw nested row is \(U=\ell(\ell*(\ell(\ell*\ell)))\);
equation (4) says \(U=r\circ{\rm inv}+\ell\). Thus its
\({\rm inv}(U-\ell)\) is exactly \(r\). The integer coefficient it
computes is precisely the left numerator of (24), with denominator
\(q^5\). All four perverse minus signs cancel. No Jacobi conjugation
or quadratic sign is missing at the two tested primes.

An independent rerun is recorded in
[astra-nested-moment-31-phase-audit.jsonl](astra-nested-moment-31-phase-audit.jsonl):

| \(p\) | Exact full contraction \(T_p\) | Lower exclusion gap \(T_p+1-E_p\), rounded down here |
|---|---|---:|
| 13 | \(224331/371293\) | negative; no sign selected |
| 9413 | \(73859407377179529891/73899294693571938293\) | \(>0.77154\) |
| 153649 | \(85565001652314817932485663/85634485014532191720043249\) | \(>1.71663\) |

The coefficient arithmetic uses exact FLINT integers. Arb evaluates the
error expression with an enclosing bound and tests a strictly positive
lower endpoint. Since §6a proves \(c_p\in\{1,-1\}\), these positive
gaps exclude \(-1\) and certify \(c_{9413}=c_{153649}=1\).
At \(p=13\), direct integer convolution was cross-checked but the
bound is too coarse to select a sign. These are two finite prime
certificates; they do not establish an all-primes sign formula.

Reproduction of this separate audit:

    .venv/bin/python -B research/nested-phase-31.py 13 9413 153649 \
      > research/astra-nested-moment-31-phase-audit.jsonl

## 7. Exact and floating verification

The independent [script](astra-nested-moment-31.py) and
[JSONL output](astra-nested-moment-31.jsonl) contain nine exact records at
\(q=5,13,17,29,41,9,25,49,121\). They use Python integers, explicit
prime/quadratic-field arithmetic, direct cubic sums, and cyclic
convolutions. Every field element is checked for (4); every square
element for (6)–(7); the mixed contraction (9) is checked as an exact
rational number. No floating rounding is used in these assertions.

As an additional independent identity check, all nonsingular points of
the Clausen pullback

\[
 B(1-d^2)=L((1-d)/2)^2-q,\qquad d\ne0,\pm1,
\]

pass in these fields. This familiar finite-field Clausen identity is
consistent with the new rank-three description; it is not needed for
the proofs of (15)–(16). See [Evans–Greene, Theorem 1.7](https://www.d.umn.edu/~jgreene/papers/Clausen_FFA.pdf).

Eight further floating records construct the full-group triple
convolution, evaluate (r\(a\)) by field subtraction, and check (14)
against a separately computed subgroup nested FFT. The largest
pointwise discrepancy is below \(4.7\times10^{-15}\). Representative
values are:

| \(q\) | \(\langle x^2z^2\rangle\) | \(\langle z^4\rangle\) | \(\mathbb E[A^3J]\), real part |
|---|---:|---:|---:|
| 9413 | 0.51772740 | 0.76163204 | 0.99967158 |
| 153649 | 0.49964344 | 0.74126445 | 0.99920162 |
| \(97^2\) | 0.54724188 | 0.98103773 | 1.02331927 |
| \(389^2\) | 0.51270388 | 0.78626951 | 1.00212334 |

Six additional exact full-contraction records cover
\(q=3,7,11,19,9,49\), explicitly including nonsquare fields \(3\pmod4\).
They check the integer coefficient and rational normalization (22)
against the full DFT. There are now 23 JSONL records: 15 exact and eight
floating. The vertical argument, rather than these six data points,
proves (23).

Square-field errors are visibly larger at these finite sizes. The
script records their \(\sqrt q\)-scaled errors; it does not fit or
certify an implied error constant. Nor do near-one cubic diagnostics
identify the remaining prime sign in (18).

Reproduce from the repository root:

```sh
.venv/bin/python -B research/astra-nested-moment-31.py \
  > research/astra-nested-moment-31.jsonl
```

Only this note and its prefixed script/JSONL were written. No shared
source, settings, credentials, commits, or external communications were
changed or used.
