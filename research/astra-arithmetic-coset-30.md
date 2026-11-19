# Arithmetic-coset audit: what quadratic splitting does and does not prove

2026-11-18. Completed arithmetic-premise audit, including exact replay.
Only this prefix is written. Ordinary theta / ETH Problem 26 remains open.

The general premise (a') in `claude-fable-28.md` C is neither proved nor
refuted for the actual Paley expression family here. The existing
joint-law theorem for `x` and `K(x^2)` is verified and reused, alongside a finite-Artin
criterion which would prove the required transfer without identifying prime
and square compact groups. The outstanding step is identification of the
arithmetic punctual multiplicity spaces of subsequent nested words.

The source of the gap is precise. For a finite tensor expression W, the
fixed-complexity character mean is

    mu_q(W) = Tr(Frob_q | I_W,q) + O_W(q^(-1/2)),

where I_W,q is the multiplicity space of the *geometric* convolution unit
in W. Purity makes its Frobenius eigenvalues unitary, not necessarily roots
of unity. At q=r^2 the action is Frob_r^2, provided W is base-change
compatible, rather than Frob_r or automatically the identity. Negative
inertia kills odd invariant spaces; it does not compute the even ones.

A finite set of integer Legendre signs can all be made +1 by taking primes
1 modulo 8 times their odd prime divisors. Dirichlet supplies infinitely
many such primes. This matches those signs at squares. It does not identify
I_W,q or its remaining Frobenius action. The finite-Artin
proposition below states a sufficient geometric/arithmetic input, not an assertion
that this input holds for all Paley words.

Primary-source audit: Katz, *Convolution and Equidistribution*, Lemma 7.1
allows unitary constant twists of infinite order; Theorem 27.1 assumes a
common identified geometric/arithmetic group. Neither is a cross-prime
identification theorem. Theorem 15.2 does identify both groups for the two
quadratic twists of TwLeg, giving the positive low-complexity result below.
Source: https://web.math.princeton.edu/~nmk/mellin331.pdf

The known low-order laws are reused, not counted as new results. The
new audit result is conditional: a common finite-Artin model of each
required finite list is enough, while the inherited fieldwise category
properties are insufficient. No actual Paley non-Artin invariant is
identified below.

## 1. Exact scope and the object which must be computed

Use q congruent to 1 modulo 4, n=(q-1)/2, x=Fs/sqrt(n), and
K=F diag(s) F^(-1), as in the supplied notes. A *word* here means a
finite syntactic expression obtained from the quadratic Kummer seed,
its chi(a) twist, convolution duals, direct sums, middle convolution,
and the chi(1-a) twist of the nonpunctual positive part. Numerical
coefficients and fixed polynomial approximations are kept outside the
sheaves. This is narrower than the entire negative-type category.

For a word W write I_W,q for the Frobenius module in its maximal
geometrically trivial punctual summand:

    W_q = (I_W,q tensor delta_1) direct-sum W'_q.

This is a semisimple decomposition for the trace calculation. I_W,q is
not an ordinary stalk of an arbitrary lisse input, and not the full
Mellin fiber at a chosen character. Its geometric dimension may itself
need a specialization argument. With uniformly bounded complexity,
character orthogonality, the lower weight of the nonpunctual stalk,
and boundedly many bad characters give

    mean_good m_W = Tr(Frob_q | I_W,q) + O_W(q^(-1/2)).                 (1)

Normalizing by the number of good characters instead of all characters
changes the expression only by O_W(q^(-1)). Lift averages on Q are
handled by expanding into the two Kummer lifts. All ensuing statements
concern the simultaneous list of expanded words.

For a construction which commutes with finite-field base change,

    I_W,r^2 = I_W,r as a vector space,
    Frob_(r^2) = Frob_r^2.                                         (2)

Here r is a base prime; comparison to another prime p is a *different*
operation. Equation (2) does not identify either I_W,r with I_W,p or
their arithmetic actions. The odd-word parity theorem proves I_W,q=0
for the odd mixed tensors of negative objects. In even words, dimension
alone does not determine the trace in (1).

The tensor generator and approximation must also be common syntactic
ones. A list of simple constituents of bounded dimension, allowed to
vary arbitrarily with q, does not provide a model over Z. The uniform
algebra draft suggests the following legitimate route: at fixed depth
choose the binomial/polynomial approximations before q grows, use the
fixed-depth limit of the marked forcing coefficient b_t to 2, and keep
raw convolution/twist words instead of choosing unrelated simple bases
at each q. Bounded-l1 exceptional corrections after K have representation
cost O(q^(-1/2)) and can be discarded in this tail approximation. This
still leaves identification and specialization of the I_W,q to prove.
It does not prove that they have finite arithmetic monodromy.

## 2. The finite-Artin transfer theorem

**Proposition 1 (a sufficient arithmetic input, with no common Mellin
compact group assumed).** Fix a finite list of words W_1,...,W_m. Assume
there is a finite Galois extension L/Q, containing Q(i), and complex
representations R_j of H=Gal(L/Q), such that outside a fixed finite set
of primes the *normalized* invariant modules in (1) satisfy

    Tr(Frob_(p^e) | I_(W_j,p^e)) = Tr(R_j(Frob_p^e))                 (3)

for e=1,2, whenever the relevant field construction is defined. Assume
also the uniform fixed-word error in (1). Then for any sequence of
squares r^2 tending to infinity there is a subsequence of these squares
and a positive-density set of primes p congruent to 1 modulo 4 on which
all the good-character means of W_1,...,W_m match in the limit.

*Proof.* There are finitely many conjugacy classes in H. Pass to an
infinite subsequence on which Frob_r has one fixed class, represented
by h. At every corresponding square the leading term is Tr R_j(h^2).
Chebotarev gives a positive-density set of primes with Frob_p conjugate
to h^2. Such primes split in Q(i), because h^2 is trivial on its
order-two Galois group. Thus they are 1 modulo 4. Their leading terms
are the same, simultaneously for every j. The remaining errors are
O(p^(-1/2))+O(r^(-1)). This proves the assertion. No identification of
prime and square geometric convolution groups was used. QED.

Chebotarev in the form used here is stated in [Sutherland, *Sato-Tate
distributions*, Theorem 1.1](https://math.mit.edu/~drew/conm14904.pdf).
Its role is finite Galois conjugacy, not complex equidistribution of
normalized positive-weight Frobenius eigenvalues.

Condition (3) is a concrete geometric/arithmetic theorem to try to
prove: the punctual multiplicity spaces must spread out, with the
actual specialization and normalization, as finite-image representations.
It is stronger than merely bounding their dimensions or proving purity.
It is sufficient, not necessary; an infinite-image module can also have
the prime subsequences required by (a').

**Proposition 1b (an integrality test which implies finite Artin).**
Suppose a candidate invariant family has already been realized as a
continuous semisimple l-adic representation R of G_Q, unramified outside
a finite set. Suppose its Frobenius traces lie in a fixed number field E,
are algebraic integers, and all their complex conjugates have absolute
value at most a fixed d (as weight zero of rank d would imply). Then R
has finite image. In particular this proves the finite-image part of
Proposition 1 if verified for the correctly normalized invariant modules.

*Proof.* The ring of integers of E is a lattice in its Minkowski space.
Only finitely many elements have every archimedean absolute value at most
d. Thus Frobenius traces lie in a finite set S. Chebotarev density and
continuity give Tr R(g) in S for every g in G_Q. Let A be the algebra
spanned by R(G_Q). Semisimplicity of R makes A a semisimple matrix algebra,
and the bilinear form (a,b) -> Tr(ab) on A is nondegenerate: on each
simple matrix block it is a positive integral multiplicity times the
usual trace pairing, in characteristic zero. Choose a basis of A from
R(g_1),...,R(g_m). Each R(g) is uniquely determined by the m numbers
Tr(R(g)R(g_i))=Tr R(gg_i), all in S. There are at most |S|^m possibilities,
so the image is finite. QED.

This is an actual reduction of the structural question. It is enough
to prove a common semisimple model plus **integrality after the weight
normalization**, in a fixed coefficient field. Integrality before
normalizing a weight-2w cohomology group and then dividing Frobenius
by p^w does not imply the required integrality. The CM example in
Section 4 exhibits this distinction explicitly. Nor has the necessary
common model and normalized integrality been proved here for the
nested Paley modules. The result is not a claim that all weight-zero
objects of geometric origin have finite image.

There is a useful stronger simplification. If all R_j factor through a
multiquadratic extension, then R_j(h^2)=I for every h. Taking p split
completely gives matching to **every** sufficiently good square, not
just a selected square subsequence. In this case all means tend to the
geometric invariant dimensions. If L has higher-order or nonabelian
finite quotients, taking all finite integer signs +1 alone need not
select h^2 in those quotients; Proposition 1 uses the full finite L.

**Corollary 2 (what the proposed CRT argument actually proves).** Let
S be a finite set of nonzero rational numbers. There is an arithmetic
progression of primes p congruent to 1 modulo 4 on which chi_p(a)=1
for every a in S. For integral a it suffices to take

    p = 1 modulo M,
    M = 8 times the product of odd prime divisors of all nonzero a.

For rational a include numerator and denominator prime divisors.
Quadratic reciprocity, chi_p(-1)=chi_p(2)=1, and multiplicativity give
the result; Dirichlet gives infinitely many primes. Every such rational
constant is also a square in F_(r^2), away from its zero denominators.
Thus **if** the finite invariant traces are fixed functions of just
these signs, this proves their matching. The italicized assertion is
exactly the extra structural statement; it is not supplied by CRT.

No uniformity in T or the polynomial degree is required in Proposition
1. The field-first application permits a different L, progression and
prime subsequence for each fixed depth and tolerance.

## 3. Reusing the known Paley range where matching is proved

**Proposition 3.** Put y=K(x^2). As q tends to infinity through *any*
odd field orders q congruent to 1 modulo 4, the empirical joint law of
(x,y) tends to

    (sqrt(2) Re Z, (Tr H_1 + Tr H_2)/2),                            (4)

where Z is Haar on U(1), H_1,H_2 are independent Haar SU(2), and all
three variables are independent. Every fixed polynomial moment and
every fixed continuous cutoff in these two coordinates therefore has
the same limit at primes and squares. No restriction on chi(2), chi(3)
or any further finite sign is needed.

This is existing project mathematics, not a newly discovered law:
[parallel-witness-6.md](parallel-witness-6.md) supplies the Legendre calculation,
[parallel-graph-shapes-23.md](parallel-graph-shapes-23.md) already gives this
all-frequency joint law, and [parallel-random-circulant-25.md](parallel-random-circulant-25.md)
uses its moments. The proof is recalled to delimit the arithmetic scope.
The present contributions are the premise audit, the finite-Artin transfer
criterion, and the explicit separation of phase and sign information.

*Proof.* Set lambda=Fs and X=lambda/sqrt(q). Let

    t(a) = sum_u chi(u(u-1)(u-a)),
    N = TwLeg(1)[1],   N' = N tensor L_chi(a).

For a in Q other than 1, direct expansion of the square indicator gives

    (s*s)(a) = (t(a)-2)/2.

Thus for any lift psi of k in the character group of Q,

    K(2X^2-1)_k = (m_N(psi)+m_N'(psi))/2 - 2 lambda_k/q.             (5)

The coefficient at a=1 contributes zero because s(1)=0. Consequently

    y_k = q/(2n) K(2X^2-1)_k,
    x_k = sqrt(q/n) X_k.                                         (6)

The seed object M=L_chi(1-a)(1/2)[1] has convolution dimension one.
It is nonpunctual; hence its geometric convolution group is G_m
(a proper algebraic subgroup would be finite). Its arithmetic group
is the same G_m, since the representation is one dimensional. At good
characters its Mellin trace has modulus one. The two lifts of the
Jacobi sum are reciprocal, so X_k is its real part, up to the harmless
common minus sign from the shift.

For N direct-sum N', the geometric and arithmetic convolution groups
are both SL(2) times SL(2). This is the explicit theorem applicable
here, not an inferred property of all negative objects. Now let G be
the geometric group for the direct sum with M. It is a subgroup of
G_m times SL(2)^2 surjecting onto both factors. Its identity component
surjects onto SL(2)^2: the image is a closed normal subgroup of finite
index in a connected group. Its derived subgroup still surjects onto
that perfect group and projects trivially to G_m. Therefore G contains
{1} times SL(2)^2, and its projection onto G_m then implies

    G = G_m times SL(2)^2.

The arithmetic group is contained in the same product (each individual
arithmetic group was identified), and contains G, so it equals G.
In particular Frobenius acts trivially on every geometric invariant of
this specific tensor family. Testing mixed representation characters,
the nonconstant ones have zero geometric invariant space. Formula (1)
gives O(q^(-1/2)) for each fixed test, uniformly over field orders.
The trivial representation has mean one. Polynomial approximation on
the bounded trace ranges then gives the product Haar law. Equations
(5)-(6), with the Jacobi bound on lambda, prove (4). QED.

The external group facts used in this proof are [Katz, Theorem 6.4 and
Theorem 15.2](https://web.math.princeton.edu/~nmk/mellin331.pdf). The
uniform fixed-word trace estimate is the one derived in the supplied
fixed-depth notes. This theorem does not require identifying the group
of a subsequent chi(1-a) twist of an arbitrary tensor polynomial.

For example (all frequencies, or after deleting boundedly many),

| Moment | Proven limit |
|---|---:|
| mean x^2, mean x^4, mean x^6 | 1, 3/2, 5/2 |
| mean y^2, mean y^4, mean y^6 | 1/2, 5/8, 35/32 |
| mean x^2 y^2, mean x^4 y^2, mean x^2 y^4 | 1/2, 3/4, 5/8 |

The SU(2) even trace moments 1,2,5 give the entries by expanding
(Tr H_1+Tr H_2)^j/2^j. Odd powers in either independent coordinate
have zero limiting mean.

Two additional exact reductions expose where a further group calculation
is first needed in this chosen test list. Put

    z=K(xy),  d=K(x^4),  <f>=n^(-1) sum_k f_k.

Since K^2=I-J,

    <z^2> = <x^2 y^2> - <xy>^2  -> 1/2,
    <d^2> = <x^8> - <x^4>^2     -> 17/8.                          (7)

However the moments

    <x^2 z^2>,   <z^4>,   <x z^3>                                (8)

are not evaluated by that isometry or Proposition 3. They require the
joint/new invariant modules involving T(M_x*M_y), with
lift expansions and nonpunctual projection understood. They are concrete
next tests, **not** established earliest counterexample words. In
particular arbitrary-degree polynomial approximations to the first
activation already use K(x^4), K(x^6), etc.; Proposition 3 does not cover
an entire nonlinear Picard depth at arbitrary accuracy by itself.

There is also a stronger existing range in the fixed-path-column section
of `parallel-graph-shapes-23.md`: the fields K T_m(X), for each fixed
finite list of m, have the independent compact symplectic trace laws
proved there. This covers the whole unnested family of fixed polynomial
feedbacks K P(x), not merely y. In particular d=K(x^4) is **not** a new
uncomputed family: asymptotically d=2Y_2+Y_4/2 with independent Y_2,Y_4,
where each is an average of two standard symplectic traces (dimensions
2 and 4 respectively). Their variances are 1/2, and their fourth moments
are 5/8 and 3/4. Thus

    <d^4> -> 16(5/8) + 6(4)(1/4)(1/2)^2 + (1/16)(3/4)
           = 739/64.                                            (8a)

This is a reuse of that existing path-group argument; it is not claimed
as a fresh independent audit of every hypergeometric identification in
that longer proof. The tests in (8) instead introduce the nested feedback
z=K(x K(x^2)), which is not just a polynomial path column.

## 4. An exact warning against promoting the category to an arithmetic theorem

Here is a countermodel to deriving (a') from negative inertia, bounded
complexity, reality, and even a connected geometric group. It is **not**
a word generated from the untwisted Paley seed, and hence does not
refute the actual (a'). Its purpose is to isolate an indispensable
arithmetic control, rather than merely say that the proof is missing.

Take the same one-dimensional negative M as above, and let C_c be a
constant weight-zero rank-one sheaf with Frobenius

    c=(3+4i)/5,    |c|=1.

Choose the auxiliary l-adic prime away from 5 and the field
characteristic. This constant representation is admissible; c is an
l-adic unit and its powers have compact l-adic closure. Set

    A=M direct-sum M^dual,
    B=(C_c tensor M) direct-sum (C_(c^-1) tensor M^dual).

Both are negative-type, tame, lisse off 1, and their good Mellin traces
are real. Their geometric group is the connected circle, acting with
weights +1,-1 in each pair; it contains simultaneous -I. At an extension
of degree e, write the good Mellin value of M as u on the unit circle.
The two real traces are

    a=u+u^-1,       b=c^e u+c^-e u^-1.

Their mixed second tensor word is

    a b = c^e u^2 + (c^e+c^-e) + c^-e u^-2.

Its geometric invariant trace, and hence its asymptotic character mean,
is exactly c^e+c^-e. Thus the prime-degree value is 6/5 and the
quadratic-extension value is -14/25, separated by 44/25. There is no
prime subsequence that removes this gap if this same c is installed
at each base prime. If Q-lift invariance is required, replace B by
(B+B tensor L_chi(a))/2 at the level of the finite expression. Its
trace is (c^e+c^-e)(u+u^-1)/2, and its mixed mean with A is still
c^e+c^-e. Thus passing to the square-subgroup lift average does not
remove the countermodel. All the local geometric properties just listed
remain identical. No Legendre sign choice changes c.

Moreover c has infinite order: if it were a root of unity, the rational
number c+c^-1=6/5 would be an algebraic integer, hence an integer. Thus
the obstruction is an actual continuous constant phase, not a missed
quadratic sign. Reality of the observed fields merely pairs c with
its inverse; it does not remove the phase from even mixed invariants.

This family is deliberately *not* asserted to spread as one compatible
motivic system over Z: prescribing the same c at every rational prime
need not do so. This is why it refutes only a deduction from the
fieldwise category hypotheses. To rule it out for Paley, one must use
something additional about the actual arithmetic construction. Merely
postulating connected geometric groups, or changing the base field to
its square, does not accomplish that.

Even requiring global geometric origin does not make finite sign tests
automatically control normalized phases. For illustration, for
E: v^2=u^3-u let a_p=p+1-#E(F_p). The weight-zero module
Sym^2 H^1(E)(1) has trace a_p^2/p-1. Its underlying normalized
nonconstant eigenvalues need not be roots of unity. Exact point counts
at three primes all congruent to 1 modulo 120 give:

| p | chi_p(2), chi_p(3), chi_p(5) | a_p | a_p^2/p-1 |
|---:|---|---:|---:|
| 241 | +,+,+ | -30 | 659/241 |
| 601 | +,+,+ | 10 | -501/601 |
| 1201 | +,+,+ | 50 | 1299/1201 |

The nonintegral rational traces already rule out all eigenvalues being
roots of unity at these primes. These are exact finite examples, not
an assertion that these three primes disprove subsequential matching,
nor an assertion that this CM module occurs in a Paley I_W. Continuous
phase control can sometimes be proved by separate arithmetic theorems;
quadratic reciprocity alone is not such a theorem.

One must also keep three different uses of Frobenius apart:

* phases in a single good-character Mellin fiber;
* phases in geometric invariant multiplicity spaces I_W,q;
* finite permutation/sign actions coming from a global finite quotient.

Only the second enters the leading mean (1). For example the Legendre
objects in Proposition 3 have nonconstant character-wise Frobenius
traces, but their arithmetic action on all geometric tensor invariants
is trivial. Seeing elliptic behavior in individual coordinates would
therefore not itself refute (a').

## 5. What primary references do and do not settle

The finite-field quotient in [Katz, Lemma 7.1](https://web.math.princeton.edu/~nmk/mellin331.pdf)
is of multiplicative type and can carry infinite-order unitary constants.
Its description does not assert finite image. Theorem 27.1 is an
across-field equidistribution theorem *under* identified groups, not a
proof of that identification for recursively constructed objects.

[Rojas-Leon, Section 5 and Proposition 6.1](https://arxiv.org/pdf/1106.1398)
control geometric local convolution and tame Jordan-block data. They do
not compute the arithmetic punctual modules required here. In particular
the local inertia parity argument cannot be upgraded to a calculation
of the even invariant Frobenius traces by citing those local formulas.
This is not a defect in the parity proof: that proof only needs the
odd invariant spaces to vanish.

The finite-Artin alternative in Proposition 1 is one usable route.
Another, substantially different, route would construct common normalized
Frobenius parameters for the actual invariant modules and prove that
prime parameters, with p=1 mod 4, accumulate at the relevant squared
parameters. A suitable joint horizontal Sato-Tate support theorem would
suffice if its hypotheses and correct finite components were established.
Finite-quotient Chebotarev does not by itself prove such an archimedean
support statement. Proximity in an l-adic quotient is not proximity of
normalized complex eigenvalues. No such horizontal theorem for all these
nested words has been identified or proved in this audit.

These alternatives separate two tasks that should not be merged: first
construct and specialize the invariant modules for the actual finite
words; then control their arithmetic Frobenius action. A finite list of
words does not imply that its Frobenius actions have finite image.

## 6. Consequence for the terminal-source criterion, with correct quantifiers

This section uses the compact approximation and uniform cutoff-sampling
inputs of `uniform-fixed-depth.md` as stated in that proof draft; it does
not independently reprove its Banach-algebra argument. The deterministic
part is also recorded by Main in [top-tail-transfer-30.md](top-tail-transfer-30.md).

Fix tau in (0,1), rho in (0,1], and a fixed T. On the bulk put

    G_q,T = sqrt(n) hat_g_T,
    k_n/sqrt(n) -> kappa_tau = sqrt(1+tau)-sqrt(tau) > 0.

The source is a fixed finite geometric combination of the 1-Lipschitz
functions sqrt(Y_j^2+4tau)-2sqrt(tau). Therefore a fixed-accuracy sup
approximation with a bounded counting-l1 exceptional error passes to
the source. If F_q is its finite class-function approximant and M_q its
maximum on *its own* arithmetic coset, compact packing and cutoff
sampling give a positive fraction of rows within any fixed tolerance of
M_q, uniformly over q at that fixed complexity. Bounded exceptions and
uniform boundedness imply

    Top_(k_n)(hat_g_T) = kappa_tau M_q + O(epsilon) + o_q(1).        (9)

The coefficient in O(epsilon) is fixed at T,tau,rho. This is stronger
input than a weak law: sqrt(n) bounded outliers can change the left
side while leaving a weak law unchanged. An arbitrary limiting law
alone is not being identified with a maximum here.

Round 29 gives on actual square trajectories

    liminf_r Top_(k_n)(hat_g_T,bulk)
      >= (rho c_tau/C_tau) T - beta_T(2+d_tau),                    (10)

with the constants exactly as in `astra-source-window-29.md` (18)-(21).
Fix a lower threshold just below the right side divided by kappa_tau.
By (9) and uniform packing, squares have a positive, possibly extremely
small, cutoff mean above this threshold. Approximate that cutoff by a
fixed polynomial and expand its finitely many word means as in (1).

If Proposition 1's finite-Artin hypothesis holds for this list, choose
a square subsequence and then its Chebotarev prime set. The polynomial
cutoff means match. Choose the polynomial approximation error smaller
than the positive square cutoff mass. The prime cutoff is then positive
by a fixed amount; hence a positive fraction of prime rows exceeds the
slightly lower threshold. Since k_n=o(n), this suffices for a lower
bound on the prime top sum. Letting tolerances go to zero proves

    limsup_p Top_(k_n)(hat_g_T,bulk)
      >= (rho c_tau/C_tau) T - beta_T(2+d_tau).                    (11)

Only lower-tail transfer is needed on the prime side; no assertion of
equality of prime and square maxima is used. The prime subsequence may
depend on T and on the cutoff accuracy because the conclusion has an
inner limsup_p.

To reject round 29's condition

    liminf_T T^(-1) limsup_p Top_(k_n)(hat_g_T,bulk) = 0,

one needs (11) for **every sufficiently large fixed T** (or other control
that genuinely bounds this liminf). An unbounded subsequence of depths
with (11) only forces a positive limsup_T and is insufficient. If the
finite-Artin hypothesis held for every required fixed word list, then
(11) for every fixed T would give a lower liminf at least rho c_tau/C_tau,
which is positive. Presently it has not been established for those lists.
Thus the prime terminal-source criterion remains a valid, unrefuted
sufficient criterion. This audit does not force a growing horizon.

## 7. Replay, limitations, and the precise next arithmetic obligation

The standalone [script](astra-arithmetic-coset-30-check.py) and its
[20 JSONL records](astra-arithmetic-coset-30-check.jsonl) contain:

* the exact rational phase countermodel (one record);
* five exact cyclic-convolution audits over q=13,17,25,49,121,
  including x^2,y^2,y^4,x^2 y^2,x^2 z^2,z^4,x z^3;
* three exact elliptic point-count examples, explicitly outside the
  asserted Paley word family;
* eleven floating diagnostics: seven prime fields, including four
  primes 1 modulo 120, and four square fields.

For the exact audit let s be its integer cyclic array,
`t_i=s_i (s convolve s)_i`;
let `u_i=s_i (s convolve t)_i`. Then

    x=F(s)/sqrt(n),  y=F(t)/n,  z=F(u)/n^(3/2).

Consequently even mixed moments are rational zero coefficients of
integer cyclic convolutions. The replay computes those coefficients
with Python integers and Fractions, independently of the floating DFT.
All five cross-checks pass; the maximum discrepancy is below 3e-15.
The exact Parseval identity for y is also asserted rationally.

The uncomputed tests (8), at two nearby large field orders, are:

| q | mean x^2 z^2 | mean z^4 | mean x z^3 |
|---:|---:|---:|---:|
| 290041 (prime; signs 2,3,5 all +) | 0.49375881 | 0.73884274 | 0.12183456 |
| 541^2 | 0.50970692 | 0.78089158 | 0.13542691 |

These data do not identify a non-Artin invariant or a limiting gap.
The observed differences are compatible with vanishing finite-field
errors. No earliest failing actual word has been found. No stationary
solver, optimizer, or interval claim is involved in this replay.

Reproduction:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-arithmetic-coset-30-check.py \
  > research/astra-arithmetic-coset-30-check.jsonl
```


### One explicit arithmetic sum beyond the verified initial laws

The mixed nested test <x z^3> admits an exact formula without sheaf
terminology. Define, on Q,

    U(a)=s(a) sum_(b,c in Q) s(b) s(a/b) s(c) s(a/(bc)).

Then U is precisely the integer positional array u used in the replay,
and Fourier orthogonality gives

    <x z^3> = n^(-5) sum_(a,b,c in Q) s(abc) U(a) U(b) U(c).       (12)

We used s(t^-1)=s(t), valid since q=1 mod 4. Expanding U makes (12)
a fixed nine-variable sum of a product of sixteen quadratic-character
factors, divided by n^5. This is a concrete next invariant-trace task:
identify its order-n^5 term, and jointly the analogous terms for the
other cutoff words. The normalized sum is not determined by the finite
signs of the written rational constants merely because the expression
is finite; its variables range over the full field. Formula (12) alone
also does not prove that a non-Artin leading term occurs.

In tensor language the relevant new generator is the chi(1-a) twist
of the nonpunctual part of the convolution of the Jacobi negative
object and the twisted-Legendre negative object, with both quadratic
lifts included. Its invariant tensors relative to the old Jacobi and
Legendre generators, rather than just its individual limiting trace
law, are needed. Even separate marginal group identifications would
not automatically settle these mixed invariants. This specifies an
actual nested word and an exact character sum to audit, without
asserting an unverified smallest failing word.

The unresolved input is now more specific than (a'): for the common
finite word list of each fixed-depth source cutoff, identify its
normalized punctual multiplicity modules over varying characteristics.
Prove either (i) the finite-Artin specialization statement (3), or
(ii) the needed joint prime accumulation for their genuinely infinite
phase factors. Already the new modules in (8) are explicit useful
arithmetic tests. Neither their dimensions, their parity, a putative
common connected group, nor prescribing finitely many Legendre symbols
can replace this arithmetic computation. Proposition 3 settles a real
initial subfamily; Proposition 1 describes an effective sufficient
structural theorem; the exact countermodel proves why that structural
step cannot be omitted from an argument using only the inherited
fieldwise category properties.
