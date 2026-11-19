# Independent audit of the first nested full-character lift

Round 31, 2026-11-18. The initial sections accept the finite identities
and cubic reduction in [nested-lift-31.md](nested-lift-31.md), after
independent algebra and a default replay. That lift calculation alone
establishes no new group or arithmetic phase. The later appendix
separately audits Astra's completed rank-three proof, including its
square-field cubic result. The remaining prime determinant sign is not
identified. No earlier-round audits are repeated.

## Full-group conjugation and exact aliases

Use \(N=q-1=2n\) and the unnormalized Fourier convention of the
note. On positional arrays let inversion be \(\iota\), so
\(\iota s=\chi s\), and let \(\mathcal S\) be quadratic
frequency shift. Since both \(\mathcal S\) and \(\mathcal K\)
are diagonalized by the full Fourier transform, they commute.
Reality of \(s\) gives exactly

$$J^\chi=\overline J,\qquad
\overline{\mathcal K f}=\mathcal S\mathcal K\overline f.$$

Moreover
\((s*s)(a^{-1})=\chi(a)(s*s)(a)\). Hence the positional
array \(s(s*s)/q\) is inversion-even and \(V\) is real.
This checks the conjugation claims without discarding complex
coordinates of any full-character field.

For \(a\in Q\setminus\{1\}\), the square-subgroup indicator
gives

$$2(s|_Q*s|_Q)(a)=(s*s)(a)
+\sum_{b\ne0}\chi((1-b)(b-a))=(s*s)(a)-2.$$

The complete quadratic sum is \(-1\), and its removed zero term
equals \(\chi(-a)=1\). At \(a=1\), the convolution formula
has an exception, but multiplication by \(s(1)=0\) removes it
before the Fourier transformation. Thus the second alias, including
its \(-x/\sqrt n\) correction, holds at every frequency.

Restriction gives the first alias directly. For the third one,
lift a square-subgroup frequency array to a quadratic-shift-invariant
full array. Its full inverse transform is supported on \(Q\), so
\(\mathcal K\) acts on the lift exactly as \(K_Q\), without
an additional factor of two. If \(R=\mathcal K(JV)\), then the
four product images are

$$\begin{array}{c|c}
\text{product}&\mathcal K\text{-image}\\\hline
JV&R\\
JV^\chi&\overline R\\
J^\chi V&\overline{R^\chi}\\
J^\chi V^\chi&R^\chi
\end{array}$$

Their sum is \(2\operatorname{Re}(R+R^\chi)\). With
\(a=\sqrt{q/n}\) and \(b=a q/(4n)\), this proves all three
aliases in (2), especially

$$z=b\operatorname{Re}(R+R^\chi)-y/\sqrt n.$$

These are identities for the raw arrays with exceptional
characters retained. A real-array replacement of the full-group
operator would not be justified.

## Cubic expansion and a uniform remainder

The quadratic shift preserves \(\operatorname{Re}J\) and exchanges
\(\operatorname{Re}R\) and \(\operatorname{Re}R^\chi\).
Therefore the four terms in the cube combine into exactly
\(2C+6D\). The lifted expression is shift-invariant, so its
full-character mean equals its square-subgroup mean. No mean
normalization factor is missing in (3).

The exact scalar coefficient is

$$ab^3=\frac{(q/n)^5}{64}=\frac12+O(n^{-1}).$$

The remainder estimate in (4) requires no uniform bound or group
theorem for \(R\). Parseval gives
\(\|x\|_{2,n}^2=(n-1)/n\). The known first-feedback bounds
then yield

$$\|x\|_\infty<2,\quad \|y\|_\infty\le4,
\quad\|y\|_{2,n}<2,\quad\|z\|_{2,n}<4.$$

Expanding the correction \(y/\sqrt n\), using these norms and
Cauchy--Schwarz, gives for example the conservative explicit bound

$$\left|\mathbb E_Q[x(z+y/\sqrt n)^3]-\mathbb E_Q[xz^3]\right|
\le\frac{384}{\sqrt n}+\frac{192}{n}+
\frac{32}{n^{3/2}}.$$

Thus the claimed \(O(n^{-1/2})\) follows without a conjectured
rank-three object or a bound on its higher moments.

Finally, expanding both real parts gives

$$16C=\mathbb E_G[(J+\overline J)(R+\overline R)^3].$$

Pairing conjugate terms gives exactly

$$C=\tfrac18\operatorname{Re}(T_3+T'_3)
+\tfrac38\operatorname{Re}T_{21}.$$

The definition of \(T_{21}\) includes both \(J\) and
\(\overline J\); the coefficient \(3/8\) is correct with
that convention. All these exact equalities use full-character
means. Means with two special characters deleted are separate
diagnostics and cannot be substituted into the finite identities.

## Conditional scope and independent replay

If the separately stated full-mean estimates
\(T_3=\alpha_q+O(q^{-1/2})\) and
\(T'_3,T_{21},D=O(q^{-1/2})\) are eventually proved, then
(3)--(5), the correction bound and \(ab^3\to1/2\) do give
\(\mathbb E_Q[xz^3]=\operatorname{Re}\alpha_q/8+O(q^{-1/2})\).
The arithmetic phase must still be identified. The independent
derived-group and determinant hypotheses, and the displayed
correlation estimates, are not consequences of the already known
first-feedback law. If a future proof estimates only good-character
means, it must also control the omitted characters before using
this full-array statement.

The default replay was saved to
[parallel-audit-31-replay.jsonl](parallel-audit-31-replay.jsonl).
It has four exact integer subgroup-convolution checks and five
complex-field diagnostics. All nine records equal Main's saved
`nested-lift-31-check.jsonl` records. The largest observed alias
error is below \(5.108\cdot10^{-15}\); the largest observed
finite cubic-reduction discrepancy is below
\(3.331\cdot10^{-16}\). The integer checks are exact, while
the Fourier diagnostics are floating point, not interval or
monodromy certificates.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/nested-lift-31.py > research/parallel-audit-31-replay.jsonl
```

Only this audit and its prefixed replay output were written at this
initial lift stage. The following appendices check the subsequently
completed identifications. Problem 26 remains open.

## Primary-checked acceptance of the completed rank-three proof

This appendix audits [Astra's completed new calculation](astra-nested-moment-31.md),
including its Section 6a. No material mathematical error was found.
The arithmetic sign remains unidentified at prime orders. The new
square result, together with the two even mixed moments, passes this
independent review.

The primary checks used [Katz, Convolution and Equidistribution](https://web.math.princeton.edu/~nmk/mellin331.pdf),
Theorems 13.5 and 17.1, Corollary 16.3, Lemma 19.3, and the proof of
Theorem 20.3 on printed pages 115--118. The balanced hypergeometric
local data were checked against [Katz, G2 and hypergeometric sheaves,
Section 2](https://web.math.princeton.edu/~nmk/g2hyper62finalcorr.pdf).
The new special rank argument is supplied by the note; it is not a
direct application of the more restrictive hypotheses of Theorem 20.3.

### Exact reductions and the arithmetic normalization

The Pfaff change \(v\mapsto v/(v-1)\) gives the stated correction
one from the excluded value whose Legendre sum is \(L(1)=-1\).
At \(a=1\), the unfactored expression gives \(D(1)=2\), so the
endpoint also agrees. The subgroup reduction retains both the zero
variable corrections and the lower-order \(-4t+2s\) terms. It yields
the exact alias (14), including \(-y/\sqrt n+x/(2n)\).
It also explains why the pure part of Main's raw full-character
nested field is the convolution dual of Astra's generator: for
\(q\equiv1\pmod4\), \(\ell D=r\circ\mathrm{inv}+\ell\).

The standard balanced hypergeometric is used for geometric local
data. Its conventional constant normalization must not be discarded
when determining the arithmetic phase. Here it can be fixed directly:
construct the triple convolution of the quadratic Kummer sheaf with
its actual trace \(\ell\). In the first double convolution, the
generic multiplication fiber has quadratic boundary characters and
no boundary invariants. In convolving once more, those characters
multiply the rank-two unipotent boundary blocks by \(\chi\),
again leaving no boundary invariants. Thus the generic compact and
middle images agree with the rank-three sheaf whose ordinary trace
is the direct sum \(B=\ell*\ell*\ell\). Its ordinary weight is
two. Reflecting, twisting and placing it in degree \(-1\), with
normalization \(q^{-3/2}\), gives perverse trace \(-A\).

This construction is compatible with finite-field base change over
every odd base. In particular, the all-extension argument need not
use the cubic character-sum expression for \(B\), which acquires
a \(\chi(-1)\) correction away from \(q\equiv1\pmod4\).
For the reflected row, the undefined value of \(B\) at zero is
irrelevant: the middle-extension stalk at \(a=1\) vanishes.

### Rank, local table and the special independence lemma

Reflection sends the rank-three local data to the displayed table:
\(1\oplus1\oplus\chi\) at zero,
\(\chi\operatorname{Unip}(3)\) at one, and
\(\operatorname{Unip}(3)\) at infinity. Quadratic twisting
therefore leaves a single trivial size-one block at zero and no
unipotent part at infinity for \(\mathcal R'\). The nontrivial
interior monodromy has its unique location at one, excluding any
nonidentity multiplicative translation. These are the hypotheses
needed for Theorem 17.1. The interior drop is three, so the
convolution dimension is three. Kummer twisting transfers the same
individual group conclusion to \(\mathcal R\).

The special rank lemma also checks, including wild boundary parts
of the possible dimension-one object. On a generic multiplication
fiber, the first factor is tame. Thus the compact rank is
\(3\dim(\mathcal L)+3\operatorname{rk}(\mathcal L)=3+3h\),
even when the second factor is wild at a boundary. Only its tame
parts can contribute boundary invariants. There is no constant
constituent or unwanted zeroth/second cohomology: such a constituent
would identify objects of convolution dimensions three and one.
The boundary exact sequence consequently subtracts exactly
\(i_0+i_\infty\).

At zero, the two trivial size-one blocks and one quadratic size-one
block can contribute at most \(i_0=3\), because a hypergeometric
has only one block for any one tame character. At infinity, pairing
with a single size-three unipotent block gives \(i_\infty\le h\).
For \(h\ge2\), this proves rank at least \(2h>3\). For
\(h=1\), equality \(i_0+i_\infty=3\) would require a trivial
tame character at both relevant boundaries. An irreducible
nonpunctual type \((1,1)\) cannot have these overlapping parameters;
types \((1,0)\) and \((0,1)\) have a wild boundary and cannot
supply both. Hence the sum is at most two and the rank is at least
four. Kummer twisting and convolution duality cover the other
objects required in the Goursat test.

For punctual dimension-one twists, the unique interior singularity
forces translation by one. The zero-inertia tables distinguish
\(\mathcal R\) from \(\mathcal R'\), and distinguish it from
\((\mathcal R')^\vee\), which has one size-three block at zero.
Thus the hypotheses of Theorem 13.5 are met. This gives independent
\(SL_3\) derived factors, not an unsupported assertion of two
independent determinant tori. The nonisomorphic \(SL_3\) and
\(SL_2\) simple factors also cannot be diagonally identified when
the old Legendre objects are adjoined.

### Canonical invariant counts and determinant direction

At degree two in \(S=A+C+\bar A+\bar C\), the four invariant
placements are the two evaluation pairings in either order. They
are fixed arithmetically. The two constant terms in
\((J+\bar J)^2\) therefore give eight invariants; the nonconstant
Jacobi-square terms have no invariant. This remains true even though
the Jacobi character and rank-three determinants are related: the
degree-two contraction spaces themselves have trivial determinant
weight.

At degree four in \(S\), each single rank-three factor contributes
six placements times two contractions, and the split between the
two independent factors contributes twenty-four. The total is
forty-eight. Identity and permutation span the two-contraction
spaces and are arithmetic-fixed. An imbalance of three cannot
give an additional degree-four invariant because of the remaining
unpaired factor. The coefficients in (15)--(16) then give the
claimed \(1/2\) and \(3/4\) limits with fixed-word errors.

The determinant weight of \(\mathcal R\) is \(-2+3=1\)
at the trivial character and \(-1\) at \(\chi\). The
dimension-one classification thus identifies its parameters as
\((\chi;1)\), which are those of \(\mathcal M^\vee\).
The adapted-singularity statement removes a multiplicative
translation. The remaining arithmetic constant must be retained.
For \(q\equiv1\pmod4\), Kummer twisting gives the same
constant for the other rank-three determinant. The cubic invariant
count is then \(2(c_q+c_q^{-1})\). The coefficient
\(a_qb_q^3\to1/32\) gives \(\operatorname{Re}c_q/8\).
The orientation is \(A^3J\), not \(A^3\bar J\).

### Why vertical reality proves a sign, including bases 3 modulo 4

This argument is valid because it uses all extension degrees and
the directly convolved \(B\). Over an arbitrary odd base
\(\mathbb F_b\), the same geometric determinant direction
holds, with a constant \(c_b\). The correct arithmetic duality is

$$\mathcal M_b^\vee=
\chi_b(-1)^{\deg}\otimes(\mathcal M_b\otimes\mathcal L_{\chi_b}).$$

Section 6a correctly keeps this factor. Its proof does not use the
two-determinant identity from a field where \(\chi(-1)=1\).
It instead uses only \(\mathcal R_b^{\otimes3}\otimes\mathcal M_b\).
There is one geometric invariant, the alternating determinant
contraction. The four Mellin trace minus signs cancel, so its
arithmetic contribution to \(\mathbb E[A^3J]\) is \(c_b^e\)
with no extra \(\chi_b(-1)\) prefactor.

Choosing the positive real square root for the half Tate twist is
compatible with every extension. The direct sheaf construction
therefore gives the same constant to the \(e\)-th power, not a
new independently chosen constant at each extension. The exact
full-character contraction is

$$T_e=\frac{(r*r*r*\ell)(1)}{(b^e)^5}\in\mathbb Q.$$

The fixed-word estimate gives
\(T_e=c_b^e+O_b(b^{-e/2})\) for every \(e\ge1\).
Reality consequently forces \(\operatorname{Im}(c_b^e)\to0\)
for all consecutive positive integers. For \(c_b=e^{i\theta}\),
the sine subtraction identity in the note then forces
\(\sin\theta=0\). Thus \(c_b=\pm1\). If only even
extensions had been available, that argument would not prove this
conclusion; the note's all-extension construction resolves exactly
that issue.

Compatible quadratic base change now gives
\(c_{b^2}=c_b^2=1\) for every odd base, including one of order
\(3\bmod4\). Hence the square-field cubic limit follows.
The fixed ranks and tame boundary data make the fixed-word error
uniform across odd characteristics. Nothing in this reasoning
chooses the sign at prime orders or proves a common global
rank-one representation over rational primes.

### Independent replay and acceptance boundary

The completed standalone script was independently replayed to
[parallel-audit-31-astra-replay.jsonl](parallel-audit-31-astra-replay.jsonl).
Its twenty-three records consist of nine exact reductions, six exact
real-phase contractions, and eight floating diagnostics. They match
the saved Astra output. The largest observed subgroup-alias FFT
discrepancy is below \(4.663\cdot10^{-15}\). The exact records
validate finite identities; neither they nor the floating records
prove the group or vertical argument, which were checked separately
above. In particular the negative small-field value at \(b=3\)
cannot be substituted for its asymptotic invariant sign.

Only this audit and its prefixed replay output were changed. The
accepted new conclusions are the two even mixed moments, the
fieldwise determinant sign reduction, and the positive square-field
cubic main term. The uniform prime sign and Problem 26 remain unresolved.

## Acceptance of the full-coherence stationary counterfamily

The theorem and completed prime-seeded corollary in
[parallel-coherent-source-31.md](parallel-coherent-source-31.md) pass
independent mathematical audit. Main handles its final numerical
replay. This is a counterfamily of general reflections with a fixed
finite entry constant, not a stationary counterexample for the
actual Paley operator.

The symmetric correction \(q\) has zero sum, and its pairing
with the centered half-sum is exactly

$$-h/n+r_Nq_Ns_N+(1/n-r_Nq_N)s_B=0.$$

Its symmetry implies \(q\perp x,y\). The antisymmetric part
has norm \(\beta|\mathbf k|^2=R^2\) and pairing
\(\beta\mathbf k\cdot\mathbf D=h\). Thus all root-row
constraints are exact. The norm slack is genuine:
\(\beta|\mathbf D|^2\to1+d^2>1\). All root-row coefficients
stay bounded, giving the asserted flatness.

The Walsh seed has the stated transform magnitudes, dimensions
and diagonal. Each full background coset has four Walsh modes;
removing \(m=O(\sqrt n)\) points costs only \(O(n^{-1/2})\)
in its normalized-indicator image. Therefore
\(\|K_0r\|_\infty=O(n^{-1/2})\). The root Householder normal
has denominator tending to \(\sqrt2\), is flat, and fixes the
root and constant vector. Expansion (21) gives full coherence.
Off the root, the stronger bound follows from

$$ (K_0w)_i=
\frac{(Pe_0)_i-(K_0r)_i}{\|r_0-r\|}=O(n^{-1/2}).$$

For a unit vector in \(F_0\), all unmarked groups have size
at least \(m\asymp\sqrt n\); its infinity norm and seed-image
infinity norm are \(O(n^{-1/4})\). The Householder expansion
preserves that bound off the root. At the root the image is zero
exactly, since \((K_1z)_0=\langle r,z\rangle=0\). This checks
both hypotheses (22), including the possible root exception.

The helper-cube lemma is valid. A vertex of a codimension-at-most
\(r\) cube section saturates at least \(k-r\) coordinates,
so its normalization has infinity norm at most
\((k-r)^{-1/2}\). There are only fixed-many constraints. Zero
mean and coherence give \(|\langle h,Lh\rangle|\le1/8\)
and \(\|P_\eta h\|^2\ge7/16\). Projection preserves the
required orthogonalities and gives a helper bounded by
\(O(n^{-1/4})\). Helpers of opposite signs are orthogonal
automatically; equal signs are handled by the extra constraints.
They are also orthogonal to every prescribed vector. Thus the
five swap normals are orthonormal. Both each normal and its
\(L\)-image are \(O(n^{-1/4})\); the fixed-size outer-product
expansion costs \(O(n^{-1/2})\) per entry, without a logarithm.
The invariant space \(\operatorname{span}\{j,e_0,r\}\) is
fixed, so the root data remain exact.

Although these swaps may mix \(F_0\) with helpers outside \(F\),
the conjugated reflection has the prescribed eigenvectors on every
direction of \(F_0\). It therefore preserves the whole space
\(F\), with exactly two plus directions. Since the diagonal
weight also preserves \(F\), the source has no modes outside
the stated two-dimensional block.

The exact matrix (27) follows from \(Tx=be\),
\(e=(\sqrt p,0)\), and
\(x=(h/\sqrt p)u+\sqrt{E_X}g\). Its determinant is
\(pF_tQ/(h^2E_X)\). On the backgrounds, the limiting scaled
residuals are \(\delta_j\pm(D_j^*-k_j^*)\), with positive
weights \((S_j^*\mp D_j^*)/s_*\). Their weighted squares give
(29); tails contribute \(O(1/t)\), the neutral group vanishes,
and the root residual is zero. Since \(d>0\), those squares
cannot all vanish. Thus \(0<F_*<\infty\) is algebraically
proved. The two eigenvalue limits and the escaped inverse mass
\(F_* /(1+F_*)\) follow from the trace and determinant, with
the large eigenvector approaching the source coordinate. This
really proves non-tightness, beyond energy divergence alone.

Source UI follows from height \(t^3\) on a fraction \(t^{-4}\),
while energy is \(t^2/2+O(1)=o(\sqrt n)\). The leakage lower
bound follows from the accepted finite resolvent certificate.
The marker is still zero. Finite-dimensional uniqueness and
zero-start convergence follow from contraction on a ball about
the known fixed point. Section 7's converse mass bound also checks:
the first moment controls \(\int\lambda\,d\mu\), and
Cauchy--Schwarz on the remaining spectrum gives (36). Fixed full
coherence forces some inverse mass to remain, but not all of it.

### Written prime-dimension corollary

Section 9 correctly replaces the Walsh seed by the actual Paley
matrix at any sufficiently large prime \(\ell\equiv1\pmod8\).
The four cyclic coset indicators again have four Fourier modes.
Their deletion error has the same order. Every later step needs
only this estimate, coherence, dimensions and root data, so no
power-of-two hypothesis remains. Rounding
\(m=\lfloor(n/2)^{1/2}\rfloor\) preserves the exact masses
and the stated asymptotics with \(H=(n/2)^{3/8}\).

The two conjugations move subspaces of dimensions one and five
and fix \(j,e_0\). Hence \(\operatorname{rank}(V-I)\le6\)
and \(\operatorname{rank}(K-K_{\rm Paley})\le12\). The
complex coefficients in (41) are correct; their common nonzero
frequency excludes cyclic convolution. Also \(\Delta>2d\)
shows the constructed spectra lose inversion-evenness. The root
row distance tends to \(\sqrt2\), proving the operator-norm
lower bound (42).

Thus low rank here is not a small perturbation. The new scaled
root row even has an empirical limit on the four values
\(\pm k_1^*,\pm k_2^*\), rather than the continuous Paley
Jacobi law. Neither that law nor the actual Paley initial field
is retained. The theorem supplies some finite coherence constant,
not a prescribed sharp Paley constant. Its prime dimensions and
Paley starting matrix do not make its final stationary pair a
Paley stationary pair.

## Acceptance of the two finite prime-phase certificates

The orientation and constants in [nested-phase-31.md](nested-phase-31.md)
and [its checker](nested-phase-31.py) pass audit. The Pfaff identity
gives \(U=r\circ\mathrm{inv}+s\), so the code's
\(r=\mathrm{inv}(U-s)\) computes \(\mathbb E[A^3J]\), not
the contraction with \(\bar J\).

The word \(\mathcal R^3\mathcal M\) has convolution dimension
27. The inherited tame generic-rank inequality gives successive
bounds 18, 81 and 108. Its nonpunctual stalk at one has dimension
at most 108 and weights at most minus one. Its sole punctual
invariant contributes \(c_q\), giving \(108/\sqrt q\).
There are at most twenty bad input characters by twice the sum
of the four input ranks. A good character is good for the generated
tensor category. At a bad character, both the product and word
trace have magnitude at most 27. Their mean replacement error is
therefore at most \(20\cdot54/(q-1)=1080/(q-1)\).

The FLINT products modulo \(X^N-1\) and the final scalar product
compute the integer zero coefficient of \(s*r^3\) exactly.
Arb encloses the rational value and elementary error bound. A
positive outward lower bound for \(T_q+1-B_q\) contradicts
the error inequality if \(c_q=-1\), so the exclusion direction
is correct.

An independent default replay was saved to
[parallel-audit-31-phase-replay.jsonl](parallel-audit-31-phase-replay.jsonl).
Its three records match the saved certificates. The gap lower
bounds exceed 0.77154 at 9413 and 1.71663 at 153649. Thus
\(c_p=+1\) is proved at those two stated primes. The small
prime 13 only checks integer convolutions and selects no sign.
These finite results do not identify a uniform prime sign or a
global rank-one model.

All edits and replay files remain in this audit's own prefix.
No source/shared file, commit or push was changed. The finite
signs and abstract coherent counterfamily leave Problem 26 open.
