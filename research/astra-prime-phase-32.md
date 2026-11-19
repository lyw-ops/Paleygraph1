# The nested determinant sign is +1 over every odd finite field

Round 32, 2026-11-18. Only the `astra-prime-phase-32*` prefix is written.
No commit or push. The uniform argument below is a fieldwise arithmetic
calculation, not an extrapolation from finite tests or a postulated
cross-prime Galois representation.

**Theorem.** With exactly the directly convolved normalization of
[round 31](astra-nested-moment-31.md), for every odd prime power $q$,

\[
\boxed{\det_{\rm conv}\mathcal R_q=\mathcal M_q^\vee,
       \qquad c_q=+1.}                                      \tag{1}
\]

Here $\ell(a)=\chi(1-a)$, $B=\ell*\ell*\ell$ on
$\mathbb F_q^\times$, $r(a)=\chi(1-a)B(1-a)$ off $a=1$,
and $r(1)=0$. The trace of the pure perverse object $\mathcal R_q$
is $-q^{-3/2}r(a)$. The trace of $\mathcal M_q$ is
$-q^{-1/2}\ell(a)$. The positive square root convention is retained.

More concretely, let $F$ be the **ordinary**, unnormalized rank-three
middle-extension sheaf with trace $r$, and let

\[
 J(\alpha,\chi)=\sum_{a\in\mathbb F_q^\times}
                  \alpha(a)\chi(1-a).
\]

For every character $\alpha\ne1,\chi$ there is an exact identity

\[
\boxed{\det\bigl(\operatorname{Frob}_q\mid
 H_c^1(\mathbb G_{m,\bar q},F\otimes\mathcal L_\alpha)\bigr)
       J(\alpha,\chi)=-q^5.}                                \tag{2}
\]

The proof has two parts: determine the ordinary determinant of $B$
from its trivial-character compact cohomology, then compare epsilon
factors with an explicit sum of rank-one sheaves. The comparison cancels
all unrestricted Gauss sums; only a **square of the quadratic Gauss sum**
remains. This is why the last sign is computable without a global model.

Using the inherited rank/group and fixed-word estimates, (1) gives

\[
 T_q=\frac{(r*r*r*\ell)(1)}{q^5}=1+O(q^{-1/2}),\qquad
 \langle xz^3\rangle=\frac18+O(q^{-1/2})
       \quad(q\equiv1\pmod4).                              \tag{3}
\]

The second assertion has the same range and uniformity as the round-31
mixed-moment reduction. The existing explicit bound becomes
$|T_q-1|\le108/\sqrt q+1080/(q-1)$ wherever that previously audited
bound applies. No claim about all later nested words or Problem 26 follows.

## 1. Arithmetic normalization of the ordinary hypergeometric determinant

Write $\mathcal B$ for the unnormalized ordinary hypergeometric sheaf
with trace $B$. We use the already identified rank-three balanced
hypergeometric and its **middle-extension** values, including at 1.
Its inertia types are

\[
\begin{array}{c|ccc}
 &0&1&\infty\\ \hline
\mathcal B&\operatorname{Unip}(3)&1\oplus1\oplus\chi
 &\chi\operatorname{Unip}(3).
\end{array}                                                   \tag{4}
\]

These are the hypergeometric inputs of round 31; the usual disjoint
parameter irreducibility and tame local descriptions are reviewed in
[Katz, *G₂ and hypergeometric sheaves*, §2](https://web.math.princeton.edu/~nmk/g2hyper62finalcorr.pdf).
Everything in this section is valid also when $\chi(-1)=-1$.

We first determine the Frobenius eigenvalue on $\mathcal B^{I_0}$,
instead of silently choosing an arithmetic normalization for a
geometrically isomorphic hypergeometric.
The complete multiplicative character sum is elementary:

\[
 \sum_{a\ne0}\ell(a)=-1,\qquad
 \sum_{a\ne0}B(a)=(-1)^3=-1.                                \tag{5}
\]

On $\mathbb G_m\setminus\{1\}$, the sheaf has rank 3; its stalk at
1 has dimension 2. Tameness and Euler characteristic give
$\chi_c(\mathbb G_m,\mathcal B)=-3+2=-1$.
Irreducibility and nonconstancy imply $H_c^0=H_c^2=0$, so $H_c^1$
is one dimensional. The boundary sequence for
$\mathbb G_m\hookrightarrow\mathbb P^1$ injects
$\mathcal B^{I_0}\oplus\mathcal B^{I_\infty}$ into this $H_c^1$:
the preceding $H^0(\mathbb P^1,j_*\mathcal B)$ is zero.
The two boundary invariant dimensions are 1 and 0. Consequently this
injection is an arithmetic isomorphism. By the trace formula and (5),

\[
 \operatorname{Frob}_q\mid\mathcal B^{I_0}=1.                \tag{6}
\]

The Frobenius eigenvalues in the semisimplification of the unipotent
size-three block at zero are therefore $1,q,q^2$. This uses the
usual geometric-Frobenius/Tate convention: the monodromy filtration of
a block with invariant eigenvalue $u$ has eigenvalues

\[
 u,qu,\ldots,q^{n-1}u.
\]

In particular its ordinary determinant is $q^3$.
The geometric determinant from (4) is the rank-one Kummer sheaf
$\mathcal L_{\chi(1-t)}$. The ratio of these rank-one sheaves is
geometrically constant; evaluating at the unramified point $t=0$
fixes the constant by (6). We obtain the **arithmetic** identity

\[
 \boxed{\det_{\rm ordinary}\mathcal B
       =\overline{\mathbb Q}_\lambda(-3)
                   \otimes\mathcal L_{\chi(1-t)}.}            \tag{7}
\]

Here $\lambda\ne\operatorname{char}\mathbb F_q$ is the auxiliary
adic prime, distinct from the function $\ell$. This argument uses
the actual sum (5), not just geometric monodromy or purity.

Reflection $t=1-a$ and the rank-one twist defining $F$ now give

\[
 \boxed{\det_{\rm ordinary}F
       =\overline{\mathbb Q}_\lambda(-3)
                     \otimes\mathcal L_{\chi(a(1-a))}.}       \tag{8}
\]

The power three on the quadratic twist reduces to one. Although (8)
is not itself the convolution determinant, it is exactly the arithmetic
local input required to compute that determinant.

### 1a. Checking the hypergeometric stalk at 1, with no correction term

For an additional check of a crucial input in both proofs, set
$\epsilon=\chi(-1)$, fix a nontrivial additive character $\psi$, and use the positive-sum
quadratic Gauss sum $G_q=\sum_{y\ne0}\psi(y)\chi(y)$.
The ordinary trace of the standard type-(1,1) hypergeometric is

\[
 h_{1,q}(t)=-\sum_{x=ty}\psi(x-y)\chi(y)
           =-\epsilon G_q\ell(t),
\]

including $t=1$, when both sides vanish. Expanding the three
counting convolutions gives, again **including $t=1$**,

\[
 h_{3,q}(t):=-\sum_{x_1x_2x_3=t y_1y_2y_3}
       \psi\left(\sum x_i-\sum y_i\right)\chi(y_1y_2y_3)
   =h_{1,q}^{*3}(t)=-\epsilon G_q^3 B_q(t).                 \tag{8a}
\]

All variables in the displayed sum are nonzero. Katz's §2, printed
page 4, explicitly states that the hypergeometric trace formula at
the missing point $t=1$ is the trace of the **middle-extension
stalk**. Thus (8a) includes no punctual or lower-weight additive term.
The parameter lists $1^3,\chi^3$ are disjoint in every odd
characteristic. The standard sheaf has generic weight 5. Its
normalization factor is $-\epsilon/G_q^3$, of weight $-3$.
This is a genuine constant-field twist: Hasse–Davenport gives

\[
 G_{q^e}=(-1)^{e-1}G_q^e,\qquad
 -\chi_{q^e}(-1)/G_{q^e}^3=(-\epsilon/G_q^3)^e.
\]

Consequently (8a) realizes the whole arithmetic sheaf $\mathcal B$
with trace $B$, and generic weight 2. The reflection at 1 has
nontrivial quadratic determinant, hence is semisimple of order two,
with invariant dimension two. Local monodromy purity (all blocks have
size one) makes this invariant stalk pure of weight 2. Equivalently,
a local quadratic tame cover kills this inertia and the pulled-back
sheaf extends lisse there. This verifies explicitly the no-pollution
and stalk-purity inputs raised by the independent audit.

## 2. A rank-one reference with matching boundary characters

Put $\epsilon=\chi(-1)$, and fix $\alpha\ne1,\chi$.
Set $F_\alpha=F\otimes\mathcal L_{\alpha(a)}$. Compare it with

\[
 E_\alpha=
 \mathcal L_{\alpha(a)}^{\oplus2}\ \oplus
 \mathcal L_{\alpha\chi(a)}\otimes\mathcal L_{\chi(1-a)}.
                                                               \tag{9}
\]

All sheaves are extended as ordinary middle extensions on
$\mathbb P^1$. The notation $D_s$ below means the determinant of
Frobenius on the local semisimplification, after using the displayed
uniformizer to fix the canonical Kummer factors. In particular it is
**not** the determinant on inertia invariants only.

\[
\begin{array}{c|c|c|c|c|c}
s&\pi_s&\text{inertia of }F_\alpha&D_s(F_\alpha)
 &\text{inertia of }E_\alpha&D_s(E_\alpha)\\ \hline
0&a&\alpha,\alpha,\alpha\chi&q^3
 &\alpha,\alpha,\alpha\chi&1\\
1&a-1&\chi\operatorname{Unip}(3)&\epsilon q^3
 &1,1,\chi&\epsilon\\
\infty&1/a&\alpha^{-1}\operatorname{Unip}(3)&\epsilon q^3
 &\alpha^{-1},\alpha^{-1},\alpha^{-1}&\epsilon.
\end{array}                                                     \tag{10}
\]

The arithmetic entries for $F$ follow directly from (8): the units in
$a(1-a)$ at these three places are respectively $1,-1,-1$.
For the reference sheaves, the factor $1-a$ contributes the unit
$-1$ at 1 and at infinity. This retains both occurrences of
$\chi(-1)$; suppressing them would invalidate the argument over
fields $3\pmod4$.

## 3. Epsilon-factor ratio and the exact determinant

The primary formula used here is Laumon's product formula, in the
explicit conventions of [Dettweiler, *On the ℓ-adic Fourier transform
and the determinant of the middle convolution*, §4.1](https://arxiv.org/pdf/1501.07807v2):
equations (4.2), (4.8), (4.9), (4.10), (4.12), and the quadratic
Gauss identity (3.1). We need only multiplicativity of $\varepsilon_0$,
the unramified-twist exponent, and the square of the quadratic local
constant. All these formulas are used in **ratios**, so an overall
Gauss-sum sign convention cannot select the answer.

Take the global differential $da$, with orders $0,0,-2$ at
$0,1,\infty$. Denote the local epsilon factor of a single quadratic
Kummer sheaf with canonical uniformizer and differential $d\pi$ by

\[
 e_\chi=\varepsilon(\mathcal L_{\chi(\pi)},d\pi).
\]

Its square is

\[
 e_\chi^2=\chi(-1)q=\epsilon q.                              \tag{11}
\]

For a nontrivial tame character, the stalk is zero. If its unramified
Frobenius scalar is $u$, the dependence of its local factor on $u$
is $u^{1+\operatorname{ord}(da)}$. Multiplicativity applies to a
unipotent block too, by its monodromy filtration; its determinant already
includes all the powers of $q$. For an unramified sheaf at a regular
differential the local epsilon factor is 1.

We can now compute every quotient in (10).

* At 0 all inertia characters are nontrivial and the character multisets
  agree. The character-dependent factors cancel, leaving
  $D_0(F_\alpha)/D_0(E_\alpha)=q^3$.
* At infinity all inertia characters again agree and are nontrivial.
  The exponent is $1-2=-1$. The ratio is therefore $q^{-3}$.
  The common factor coming from $da=-\pi^{-2}d\pi$ also cancels.
* At 1 the numerator is
  $D_1(F_\alpha)e_\chi^3=\epsilon q^3e_\chi^3$.
  The two smooth reference summands contribute 1 each and the remaining
  reference summand contributes $\epsilon e_\chi$.
  The ratio is $q^3e_\chi^2=\epsilon q^4$.

The global prefactors cancel because both sheaves have rank 3; every
other place contributes 1. Thus

\[
 \frac{\varepsilon(\mathbb P^1,F_\alpha)}
      {\varepsilon(\mathbb P^1,E_\alpha)}
       =q^3q^{-3}(\epsilon q^4)=\epsilon q^4.                \tag{12}
\]

For $F_\alpha$, all three boundary invariant spaces vanish.
Its compactly supported cohomology is concentrated in degree 1 and
has dimension 3. For $E_\alpha$, the first two summands have zero
global cohomology: they are nontrivial Kummer sheaves on $\mathbb G_m$.
The third has one-dimensional $H_c^1$, with Frobenius eigenvalue
$-J(\alpha\chi,\chi)$. Both surviving dimensions, 3 and 1,
are odd, so passing from $\det(-\operatorname{Frob})$ in the epsilon
formula to $\det(\operatorname{Frob})$ introduces the same sign in
numerator and denominator. Formula (12) gives

\[
 \det(\operatorname{Frob}_q\mid H_c^1(F_\alpha))
       =-\epsilon q^4J(\alpha\chi,\chi).                     \tag{13}
\]

The elementary Gauss/Jacobi formula, valid since
$\alpha,\alpha\chi\ne1$, gives

\[
 J(\alpha,\chi)J(\alpha\chi,\chi)
   =G(\chi)^2=\epsilon q.                                  \tag{14}
\]

Multiplying (13) by $J(\alpha,\chi)$ proves (2). Notice that
the two factors of $\epsilon$ cancel. The proof never replaces
$\mathcal M^\vee$ by $\mathcal M\otimes\mathcal L_\chi$
without its constant twist.

## 4. Passing to the convolution determinant, including q=3

At a good character the Mellin fiber of $\mathcal R$ is
$H_c^1(F_\alpha)(3/2)$, of dimension 3. Its determinant is therefore

\[
 q^{-9/2}\det(\operatorname{Frob}\mid H_c^1(F_\alpha))
      =-\frac{\sqrt q}{J(\alpha,\chi)}.                      \tag{15}
\]

The Mellin eigenvalue of $\mathcal M$ is
$-J(\alpha,\chi)/\sqrt q$; its reciprocal is exactly (15).
The previously established geometric identification
$\det_{\rm conv}\mathcal R=c_q^{\deg}\otimes\mathcal M^\vee$
then forces $c_q=1$, for any $q>3$, by one good character.
One may equivalently apply the equality over every finite extension
and the Mellin fiber functor. No unverified arithmetic identification
is inserted at this stage.

There is no good character over $\mathbb F_3$. Base change gives
$c_9=c_3^2$ and $c_{27}=c_3^3$. Both left sides are 1 by the
argument just proved, whence $c_3=1$. This small-field step does not
even need the earlier vertical-reality theorem. It proves (1) for
**every odd prime power**, rather than only for the Paley congruence.

## 5. Exact replay independent of epsilon-factor manipulation

Run from the repository root:

```sh
.venv/bin/python -B research/astra-prime-phase-32-check.py \
  > research/astra-prime-phase-32-check.jsonl
```

The [script](astra-prime-phase-32-check.py) uses FLINT finite fields,
integer cyclic polynomial multiplication, and exact cyclotomic
quotients. It defines $B$ by **direct triple convolution** in every
characteristic and extension degree. It does not use the $q=1\pmod4$
Pfaff shortcut or an uncorrected cubic-character-sum formula.

For each base $q=3,5,7,9,11,13,25,27$, it constructs the extensions
of degrees 1, 2 and 3. An explicit root of the base defining polynomial
specifies the embedding; a recorded discrete logarithm specifies the
norm lift of every base character. This avoids identifying unrelated
primitive elements in different fields.

For each good character let

\[
 S_e=-\sum_{a\in\mathbb F_{q^e}^\times}
             (\alpha\circ N_{q^e/q})(a)r_{q^e}(a).
\]

These are the power traces of the same unnormalized three-dimensional
Frobenius module. The script computes

\[
 d=\frac{S_1^3-3S_1S_2+2S_3}{6}
\]

and checks both $d=-\epsilon q^4J(\alpha\chi,\chi)$ and
$dJ(\alpha,\chi)=-q^5$ exactly. It also checks (14).
Separately, applying the same Newton formula to the three pointwise
traces $B_{q^e}(t)$ checks (7) at every $t\ne0,1$ in each base.
Small-field cyclic products are cross-checked against independent
Python-integer double loops.

The [17 JSONL records](astra-prime-phase-32-check.jsonl) report:

| Base q | Good Mellin characters | Ordinary determinant points |
|---:|---:|---:|
| 3 | 0 | 1 |
| 5 | 2 | 3 |
| 7 | 4 | 5 |
| 9 | 6 | 7 |
| 11 | 8 | 9 |
| 13 | 10 | 11 |
| 25 | 22 | 23 |
| 27 | 24 | 25 |
| Total | 76 | 84 |

All pass; the largest field used is $27^3=19683$.
These are normalization checks of the exact formula, **not** a
finite substitute for the uniform proof. In particular $q=3$ contributes
no direct good-character determinant check.

## 6. Attempts, discarded routes, and audit boundaries

1. **Reading off the sign from the geometric hypergeometric parameters:**
   insufficient. They leave an unramified twist. The new arithmetic input
   is (5)–(6), which fixes the actual ordinary determinant before any
   Mellin comparison.
2. **Direct multiplication of three absolute local epsilon factors:**
   an exploratory calculation mixed Gauss-sum and differential conventions
   and returned the wrong overall sign already for a rank-one Jacobi
   sheaf. It was rejected, not used as evidence. The reference object
   (9) cancels those common factors. The surviving quadratic Gauss factor
   is squared, and the cohomological sign is explicitly checked in (13).
3. **Clausen / symmetric-square pullback:** exploratory direct sums at
   small primes on both sides of 4 support the familiar identity
   $B(1-u^2)=L((1-u)/2)^2-q$. This route would require auditing the
   arithmetic descent through the quadratic cover; it is unnecessary
   here and no new Clausen theorem is claimed. The independent proof
   (5)–(7) fixes the determinant without that identity or descent.
4. **A common one-dimensional Artin model over the rationals:** not
   constructed or assumed. The calculation works anew over each odd
   field with uniform formulas. Thus the general ramification,
   integrality, and specialization obligations in round 30 are neither
   silently discharged nor needed for this particular invariant.
5. **Exact positivity / divisibility of $T_q$:** not needed and no such
   universal statement is asserted. For example the previously recorded
   $T_3=-1/243$ is compatible with $c_3=1$, since $T_q$ includes
   non-leading contributions. The new exact identity is (2), for a
   three-dimensional Mellin determinant, rather than positivity of the
   much larger cubic contraction.

The mathematical inputs retained from prior work are the actual
middle-extension hypergeometric model (4), the geometric convolution
determinant direction, the Mellin tensor formalism, and, for (3), the
already audited invariant computation and uniform error estimate.
The new argument does not re-prove the independence of the two $SL_3$
factors or the fixed-depth transfer theorem. It supplies their previously
missing arithmetic sign in this one nested family.

Primary sources were checked on 2026-11-18. Besides the local
hypergeometric reference above, [Katz, *Convolution and
Equidistribution*, Chapters 16–17](https://web.math.princeton.edu/~nmk/mellin331.pdf)
was checked to distinguish ordinary and convolution determinants;
Corollary 16.3 alone is geometric and does not select this scalar.
The epsilon-factor source is the v2 dated 2023-10-19, not an assumed
cross-prime compatibility theorem. Its §4.1 cites Laumon,
*Transformation de Fourier, constantes d'équations fonctionnelles et
conjecture de Weil*, Publ. Math. IHÉS 65 (1987), 131–210.

## 7. Independent audit of the subsequently supplied bad-character route

After the epsilon-factor proof and its first exact replay were complete,
the main chat supplied `audit_square`'s proposed alternative: prove
$B(1)\not=0$ modulo 4, then use the determinant of the stalk at 1
and the trivial-character Deligne fiber. The following is an independent
check of that route, with its narrower congruence range explicit.

**Orbit calculation.** Suppose $\epsilon=1$. In the set of triples
$abc=1$ with $a,b,c\ne1$, act by swapping $a,b$ and by simultaneous
inversion. The weight $\chi((1-a)(1-b)(1-c))$ is constant on each
orbit. Inversion has no fixed point: all three coordinates would have
to be $-1$, whose product is $-1$. Inversion followed by the swap
also has no fixed point: $ab=1,c=-1$ again contradicts $abc=1$.
Only the swap can stabilize a point. Its fixed triples are
$(a,a,a^{-2})$, $a\ne0,\pm1$, so there are $q-3$ such points,
in $(q-3)/2$ orbits of size two. Every nonzero weight is $\pm1$.
The four-element orbits vanish modulo 4 and each two-element orbit
contributes 2 modulo 4. Therefore

\[
 H_q:=B_q(1)\equiv q-3\equiv2\pmod4.                        \tag{16}
\]

**Purity.** At 1 the local inertia (4) is semisimple; all Jordan blocks
have size one. Local monodromy purity thus makes the two invariant
Frobenius eigenvalues pure of weight 2, each of complex modulus $q$.
This is stronger than the general upper weight bound for an arbitrary
singular stalk; that general bound alone would not suffice. Their sum
is the real, nonzero integer $H_q$. Two complex numbers of modulus
$q$ with real nonzero sum have product $q^2$: their imaginary parts
are opposite, and equal moduli force the real parts to agree unless
the sum is zero. Hence

\[
 \det(\operatorname{Frob}\mid\mathcal B_1)=q^2
                    \quad(q\equiv1\pmod4).                 \tag{17}
\]

**Boundary normalization.** Here is an arithmetic calculation valid over
every odd field, not just the Paley congruence:

\[
 \sum_{a\ne0}r(a)
 =\sum_{t\ne0,1}\chi(t)B(t)
 =J(\chi,\chi)^3-B(1)=-\epsilon-B(1).                       \tag{18}
\]

The unnormalized $F$ has $H_c^1$ of dimension three. Its boundary
invariants have dimensions two at 0 and one at infinity. As in §1,
their direct sum injects into $H_c^1$, hence is all of it; the
projective middle cohomology vanishes. At zero the invariant module
is exactly $\mathcal B_1$, since the twisting unit is 1. The trace
formula and (18) now fix the invariant eigenvalue at infinity as
$\epsilon$, rather than an undetermined cube root.

The Deligne functor
$\omega(N)=H^0(\mathbb A^1,j_{0!}N)$ is a tensor fiber functor
**at the trivial character as well**, by Katz Theorem 3.1. It is not
being identified with compact cohomology at this bad character.
The two exact sequences in the proof of Katz Theorem 16.1 give the
two-dimensional zero-boundary submodule and the one-dimensional
$H^1(I_\infty,F_\infty)$ quotient; the middle projective term is zero.
For the unnormalized unipotent size-three block, this latter quotient
has eigenvalue $\epsilon q^3$: its coinvariant eigenvalue is
$\epsilon q^2$, followed by the additional $(-1)$ Tate twist in
inertia $H^1$. After normalizing $F$ by $q^{-3/2}$,

\[
 \det\omega(\mathcal R)
 =\bigl(q^{-3}\det\mathcal B_1\bigr)
       (\epsilon q^{3/2})
 =\epsilon q^{-3/2}\det\mathcal B_1.
\]

The trivial-character fiber eigenvalue of $\mathcal M$ is
$q^{-1/2}$, so that of its convolution dual is $q^{1/2}$.
Consequently the proposed identity is correct, with its general-field
sign included:

\[
 \boxed{c_q=\epsilon\,\det(\operatorname{Frob}\mid\mathcal B_1)/q^2.}
                                                               \tag{19}
\]

Equations (16)–(19) independently prove $c_q=1$ for all
$q\equiv1\pmod4$. For $q\equiv3\pmod4$, inversion instead
forces $H_q=0$, and this nonzero-real-trace argument stops. The
epsilon-factor proof above supplies the additional range without
assuming a sign for a zero-trace pair. It also gives
$\det\mathcal B_1=\epsilon q^2$ in that range via (19).

The replay now also records (18), the exact special-stalk determinant
from $H_q,H_{q^2}$, and a complete orbit enumeration for the four
bases $5,9,13,25$ with $q\equiv1\pmod4$ in its list.
These added checks pass. No file of the other audit was modified;
its file was not yet present when this independent check was made.

## 8. Audit of the proposed full joint law for (x,y,z)

The main chat subsequently proposed identifying the entire joint group,
not only the three moments of round 31. Under the derived-subgroup
inclusion already proved there, this consequence is correct. There is
one presentational distinction: negating the Frobenius matrices is a
translation of the group, not a new linear representation. It does not
alter the Haar law here, for the explicit reason below.

Work throughout this section with $q\equiv1\pmod4$. Let the actual
representation coordinates of the Jacobi, two rank-three, and two old
rank-two objects be $(m,g,h,s,t)$. The new arithmetic determinant
identities, together with the old arithmetic $SL_2$ identifications,
give the upper bound

\[
 G_{\rm geom}\subseteq G_{\rm arith}\subseteq H,\qquad
 H=\{(m,g,h,s,t):
       \det g=m^{-1},\ \det h=m,\ \det s=\det t=1\}.            \tag{20}
\]

Here $m\in\mathbb G_m$, $g,h\in GL_3$, and $s,t\in SL_2$.
The projection of $G_{\rm geom}$ to $m$ is onto, by the Jacobi
geometric torus theorem. Round 31 supplies the contained subgroup

\[
 K=\{1\}\times SL_3\times SL_3\times SL_2\times SL_2
       \ \subseteq G_{\rm geom}.                             \tag{21}
\]

But $K$ is exactly the kernel of $H\longrightarrow\mathbb G_m$.
For any point of $H$ over an algebraically closed coefficient field,
choose a point of $G_{\rm geom}$ with the same $m$; their quotient lies
in $K$, hence in $G_{\rm geom}$. This proves

\[
 \boxed{G_{\rm geom}=G_{\rm arith}=H.}                         \tag{22}
\]

There is no further finite or central coupling compatible with (21)
and the onto projection. Connectedness follows directly as well:
$H$ is an extension of the connected torus by the connected group
$K$. Explicitly one can use the section
$(m,\operatorname{diag}(m^{-1},1,1),
\operatorname{diag}(m,1,1),I_2,I_2)$ and its action on $K$.
Thus one must not replace $H$ by $GL_3^2$ with unrestricted determinants.

For the positive trace conventions of the question set

\[
 j=-m,\qquad U=-g,\qquad V=-h.
\]

The rank-three parity gives
$\det U=-\det g=j^{-1}$ and $\det V=-\det h=j$.
Moreover

\[
 z_0=(-1,-I_3,-I_3,I_2,I_2)\in H
\]

is a central group element. The simultaneous sign change is precisely
translation by $z_0$ in $H$, so Haar measure is unchanged. This
justifies using the same determinant equations with $(j,U,V,S,T)$
as positive trace coordinates. It does not assert that the function
$g\mapsto-g$ is a representation homomorphism.

The compact form has $j\in U(1)$, $U,V\in U(3)$ with these determinant
constraints, and $S,T\in SU(2)$. A description without a choice of
cube root is: take independent Haar variables
$j\in U(1)$, $U_0,V_0\in SU(3)$, $S,T\in SU(2)$ and put

\[
 U=\operatorname{diag}(j^{-1},1,1)U_0,\qquad
 V=\operatorname{diag}(j,1,1)V_0.                             \tag{23}
\]

Conditioned on $j$, the two rank-three matrices are independent Haar
variables on their fixed-determinant cosets. Unconditionally they have
correlated determinants. The two $SU(2)$ variables are independent of
everything else.

The exact coefficients in round 31, equation (14), tend to
$a_q\to1/\sqrt2$ and $b_q\to1/(2\sqrt2)$; its correction to $z$ tends
uniformly to zero. The old first-feedback normalization gives $y$.
Consequently the proposed law is indeed

\[
 \boxed{
 X=\sqrt2\,\operatorname{Re}j,\qquad
 Y=\frac{\operatorname{Tr}S+\operatorname{Tr}T}{2},\qquad
 Z=\frac{\operatorname{Re}\operatorname{Tr}U+
              \operatorname{Re}\operatorname{Tr}V}{\sqrt2}.} \tag{24}
\]

As a sign/coefficient check, the only surviving terms in the mixed
cubic contraction are $j(\operatorname{Tr}U)^3$,
$j(\overline{\operatorname{Tr}V})^3$, and their conjugates. Each has
integral 1, and the coefficient is $1/32$, giving
$\mathbb E[XZ^3]=1/8$ as required.

Fixed trace polynomials have the inherited uniform
$O_P(q^{-1/2})$ error. Polynomial approximation on the common bounded
trace ranges then proves convergence for every fixed continuous test
of $(x,y,z)$. One should claim only $o_f(1)$ for a general continuous
test without a separate approximation-rate argument.
The lift involution is
$(j,U,V,S,T)\mapsto(j^{-1},V,U,T,S)$; all three observables (24) are
invariant. Thus averaging over the two lifts of each character of the
square subgroup gives the same joint observable law.

This establishes the proposed extension for the actual five generators
and their continuous trace observables, on the inherited group and
uniformity inputs. It does not identify a new generator obtained by
another nonlinear feedback step, and it does not establish the
all-depth terminal-source transfer required for Problem 26.
