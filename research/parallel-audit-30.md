# Independent acceptance audit: reciprocal source tails and top-tail transfer

Round 30, 2026-11-18. This audits
[the completed source-pair note](parallel-source-pair-29.md) and
[Main's top-tail transfer note](top-tail-transfer-30.md). No material
mathematical error was found in the requested statements. Their limiting
claims have the stated conditional scope. Main separately replayed the
69 source-pair records byte-for-byte; this audit does not duplicate that
suite or turn its floating-point diagnostics into interval certificates.
No unfinished round-30 research notes were read.

## 1. Resolvent decomposition and the stripped finite certificate

Use the source-pair conventions, including counting norms,
\(R=I-P_\sigma=J+P_{-\sigma}\), \(Tx=be\),
\(D=\operatorname{diag}(d)\), and
\(L_\delta=R(D+\delta I)^{-1}R|_{\operatorname{im}R}\).
The inverse-compression dual formula is

$$f_\delta:=\langle e,(T+\delta I)^{-1}e\rangle
=\min_{q:\,P_\sigma q=e}
\langle q,(D+\delta I)^{-1}q\rangle.$$

Writing \(q=e_0+z\) with \(z\in\operatorname{im}R\) gives
exactly (13). At \(\delta=0\), the minimizer is
\(q_0=Dx/b\). Its value at positive \(\delta\) is
\(f_0-S_\delta/b^2\). Its weighted gradient in the complementary
space is \(-R(\theta x)/b\), since \(Rx=0\). Completing the
quadratic minimum subtracts
\(\langle R(\theta x),L_\delta^{-1}R(\theta x)\rangle/b^2\).
This proves (10) with the displayed plus sign and no missing factor.

The extension minimum (14) is also exact. If
\(t_\delta=\theta x-\theta_0x_0e_0\) and
\(m_\delta=n^{-1}\sum t_\delta\), then

$$R(\theta x)=\theta_0x_0Re_0
+m_\delta\mathbf1+P_{-\sigma}t_\delta.$$

Using the original extensions \(e_0\), \(\mathbf1\), and
\(P_{-\sigma}t_\delta\) in (14), followed by the triangle
inequality, proves (11). In particular the first extension costs
\(\sqrt{d_0+\delta}\). Replacing it with the full weighted norm
of \(Re_0\) would lose the useful stripping. The opposite-sector
projection can create a new marked coordinate; its contribution is
correctly retained in \(\ell_\delta\).

For the inverse-energy source measure
\(d\nu=b^2\lambda^{-1}d\mu\),
\(\Delta_\delta=\int\delta/(\lambda+\delta)\,d\nu\).
The multiplier is at least \(1/2\) on \((0,\epsilon]\) when
\(\epsilon\le\delta\), proving (12). This is a sufficient
explicit upper certificate, not an equivalence or an assertion that
its upper bound is always sharp.

## 2. UI estimates, leakage and the mark

Put \(u=A/a\). Then \(d=\rho/u\), \(x=a(u-1)\),
\(na^2=W\), and \(W\rho=\tau\). In \(S_\delta\), splitting
at \(u=R_0\ge2\) gives the low part
\(2W\delta(R_0+1)\) and high part
\(\tau\mathbb E_n[u\mathbf1_{u>R_0}]\), exactly as in (15).
The same split in the absolute mean of \(t_\delta\) gives
\(2\delta R_0/\rho+2\mathbb E_n[u\mathbf1_{u>R_0}]\) after
division by \(a\). Removing the mark only removes a term from
these absolute estimates.

The identity \(\sum d=n-b/a<n\) yields
\(a\sqrt{\sum(d+\delta)}\le\sqrt{W(1+\delta)}\).
At a fixed floor, the stationary root caps for both spectra and
\(A_0B_0=1\) give a positive lower as well as upper bound for
\(A_0\). Hence \(x_0=O_\tau(1)\) and
\(d_0=O_\tau(n^{-1/2})\). The stripped mark term vanishes when
the field grows first and then \(\delta\downarrow0\).

On the bulk, the source UI relation

$$G=\sqrt W(u+u_-)-2\sqrt\tau$$

indeed implies UI of each nonnegative normalized spectrum. Its root
contributes only \(O_\tau(n^{-1/2})\) to a normalized first
moment, so the full-coordinate estimates remain valid. Taking the
field limit, then \(\delta\downarrow0\) at a fixed truncation,
and finally increasing the truncation proves the claimed vanishing
of \(S_\delta\) and the constant term. The additional leakage
assumption (16) therefore suffices for tightness of \(\nu\) away
from zero. It is not supplied by UI or by the finite certificate.

For (17),

$$x_0-(x_\delta)_0=\Delta_\delta/b,$$

and spectral calculus gives

$$\|T^{1/2}(x-x_\delta)\|^2
=\int\left(\frac\delta{\lambda+\delta}\right)^2d\nu
\le\Delta_\delta.$$

The stated test-pairing bound then follows by weighted
Cauchy--Schwarz. Bounding the test's inverse norm remains a separate
requirement. Also, the operator \(T\) depends on the exact stationary
pair; no fixed-depth arithmetic formula for its regularized inverse
is established here.

## 3. Exact reflection family: stationary equation and UI

For \(n=2t^8\), \(m=t^5\), \(H=t^2\), and
\(M=t^8-t^5-1\), the right side of (19) tends to
\(2\sqrt{1+\tau}>2\sqrt\tau\). The larger root \(L\)
therefore exists, stays bounded, and tends to
\(\sqrt{1+\tau}+1\). The table has total size
\(2+2m+2M=n\). Direct summation proves both means are \(a\),
and every pair product has the prescribed heterogeneous weight.
Thus the centered vectors are orthogonal exactly, not just
asymptotically.

Their equal energies satisfy

$$E=\frac{mH^2}{n}+O_\tau(1)=t/2+O_\tau(1).$$

The normalized bulk source is bounded on the backgrounds and
has height \(t^2+O_\tau(1)\) on a fraction \(t^{-3}\) of all
coordinates. Its first tail mass is
\(t^{-1}+O_\tau(t^{-3})\), giving the uniform
\(O_\tau(R_0^{-1/2})\) first-moment tail. The normalized spectra
have the same UI property; their growing root value carries only
\(O(t^{-4})\) normalized first mass. Both divergent energies are
subcritical relative to \(\sqrt n\).

In (22), \(j,g,h\) are orthonormal. The vector \(z\) is
orthogonal to all three and

$$z_0=\|z\|^2=1-1/n-2\alpha^2=l_++l_-.$$

Since the balanced \(w_*\) is orthogonal to all group-constant
vectors, \(p\) is unit, orthogonal to \(j,g,h\), and
\(p_0=\sqrt{l_+}\). The seven-dimensional space has two plus
directions, four minus directions and the constant zero direction.
The stated dimensions on its complement sum to \(n-7\), giving
the exact full sector dimensions in (23). Also

$$ (P_+)_{00}=\alpha^2+l_+=1/2-1/n,$$

which proves all the marked projector and diagonal values. Since
\(Kx=x\), \(Ky=-y\), and \(AB=w\), equation (24) is exact.

Uniqueness and actual zero-start Picard convergence follow at each
finite dimension. On any finite ball centered at this existing fixed
point, all scalar derivatives
\(|v_i|/\sqrt{v_i^2+4w_i}\) are bounded by a common number less
than one. Thus \(K\Phi\) is a strict contraction there and maps
the ball to itself. Choosing a ball containing zero gives convergence;
choosing one containing any purported second fixed point proves
uniqueness. The contraction constant depends on the model index;
there is no uniform-time conclusion.

## 4. Source spectrum and explicit loss of Paley coherence

The diagonal \(D\) preserves the seven-dimensional space, as well
as its orthogonal complement. Therefore the plus marked source,
which lies in \(\operatorname{span}\{g,p\}\), has a complete
two-by-two spectral description. The source equation gives
\(T_{11}=Q/E\) and \(T_{12}=b\sqrt{l_+}/\sqrt E\).

On the second tail, \(z_i\sim-H/(\sqrt n E)\). Its weighted
contribution to \(\langle z,Dz\rangle\) is
\(H/(\sqrt W E)\sim2t/\sqrt{1+\tau}\). The squared
\(\widehat z\) coefficient in \(p\) tends to \(1/2\), the
balanced background contribution stays bounded, and the other
contributions are lower order. Hence
\(T_{22}\sim t/\sqrt{1+\tau}\), verifying (25).
The off-diagonal Schur correction is \(O(t^{-2})\), so (26)
follows. The large-eigenvalue inverse mass is \(O(1/t)\), while
the total inverse mass tends to one. This proves (27) for the stated
measure \(\nu\), as distinct from the unweighted source measure
\(\mu\).

For a second-tail coordinate, the marked row is

$$K_{0i}=1/n+2\alpha g_i+2p_0p_i
\sim-\frac{H}{\sqrt n E}
\sim-\frac1{\sqrt{Em}}.$$

Consequently \(\sqrt n|K_{0i}|\sim2t\), proving the explicit
failure of a uniform Paley coherence constant. The construction
also lacks the required convolution/translation structure. It does
not refute a UI-to-tightness implication that uses such additional
Paley information.

Two useful scope consequences are worth retaining. First,
\(A_0=B_0=1\), so the model's stationary marker itself is
\(v_0=\gamma_0=0\). It obstructs an inference about inverse-source
tails and leakage, not marked cancellation. Second, the displayed
proofs quantify the leakage failure: at each fixed \(\delta>0\),
\(\Delta_\delta\to1\), whereas the other terms in (11) vanish
in the subsequent \(\delta\downarrow0\) limit by UI. Thus in
this constructed model

$$\liminf_{\delta\downarrow0}\liminf_{t\to\infty}
\ell_{t,\delta}\ge1.$$

This follows from
\(\ell\ge\sqrt{(\Delta-S)_+}-\text{mark term}-\text{constant term}\)
and the already proved ordered estimates. It is not a prime lower
bound.

## 5. Top-tail stability, sampling, and conditional arithmetic transfer

The fractional top sum is a support function. For a maximizing
weight \(0\le\lambda_i\le1\), \(\sum\lambda_i=k\), its dual
norm is at most \(k^{1-1/p}\). This proves (1), with \(k=0\)
handled trivially. Counting-to-normalized conversion gives exactly
\(k^{1-1/p}n^{1/p-1/2}\) in (2). At \(p=2\),
\(k\asymp\sqrt n\), the loss is \(n^{1/4}\); the supplied
bounded-array example attains the scale. Therefore an unquantified
normalized \(L^2\) approximation cannot be used for this tail.
Bounded counting \(\ell_1\) exceptional error and a prescribed
sup error have the stated cheaper costs.

In the sampling lemma (3), one can select all \(k\) weight from
the \(\delta n\) near-maximum entries for the lower bound. For
the upper bound, the nonexceptional entries cost at most
\(M_n+\epsilon\) each, and at most \(N_0\) exceptional weight
can cost \(B\). The displayed correction is conservative even
when \(M_n\) is negative. A positive Haar neighborhood is not by
itself a positive empirical frequency fraction; the cutoff-mean
sampling hypothesis remains necessary. At fixed depth the bulk
source activation is 1-Lipschitz in the scaled iterate, so the
conditional passage of the draft's approximation to that source
is justified.

The conditional square-to-prime transfer uses only scalar cutoff
means. It requires simultaneous matching of the expressions in
the chosen cutoff along a suitable infinite prime subsequence,
with an error leaving a fixed positive fraction; for example, an
error at most half the square cutoff's uniform positive lower
bound suffices. No shared compact group, geometric group, or
arithmetic coset is established across fields. The missing premise
is not implied by finite residue patterns or by inertia parity.

If that matching premise holds at each sufficiently large fixed
depth, it transfers the linear square lower bound to
\(\limsup_p\) at every such depth. This would contradict the
\(\liminf_T\) criterion. An unbounded set of successful depths
is insufficient for that contradiction: the criterion could use
other depths. Prime subsequences may depend on the depth and the
chosen tolerance, which is compatible with the separate field
\(\limsup\) and does not justify a moving-depth statement.

Neither source-pair29 nor top-tail30 proves the required arithmetic
matching, the prime leakage bound, a prime source-tail estimate,
or the marked limit. The accepted conclusion is the finite
resolvent certificate, the exact non-Paley obstruction, and a
precise error and sampling budget for any future Paley transfer.

## 6. Added top-seminorm propagation obstruction

The newly added Section 3 of Main's note is also correct. If
\(|K_{ij}|\le\mu/\sqrt n\), a Rademacher vector \(y\)
on \(k\) nonroot coordinates has row coefficient square sum at
most \(\mu^2k/n\). Hoeffding at

$$t_k=\mu\sqrt{2k\log(4n)/n}$$

gives probability at most \(1/(2n)\) of a row exceeding \(t_k\)
in absolute value. A union bound leaves a realization with
\(\|Ky\|_\infty\le t_k\). For \(e=Ky\), both \(e\) and
\(Ke=Py\) have mean zero. Every support coordinate has
\(|(Py)_i|\ge1-k/n\), whereas
\(\mathcal N_k(e)\le kt_k\), proving the displayed ratio.
Its denominator cannot vanish: a mean-zero vector with zero bulk
seminorm would be zero, which would imply \(Py=0\), impossible
for the nonconstant supported sign vector.

For the inversion-even version, take even \(k\) and at least
\(k/2\) available nontrivial inverse pairs. These pairs exist in
the cyclic Paley square subgroup in the stated \(k\le n/2\)
range for large orders. Each shared-sign coefficient is the sum
of two matrix entries, giving total coefficient square sum at
most \(2\mu^2k/n\). The correct threshold is therefore
\(2\mu\sqrt{k\log(4n)/n}\), as stated. Commutation with
inversion preserves evenness. For a general involution with too
few nontrivial pairs, commutation alone would not supply that
pair construction; this is no restriction for the Paley application.

At \(k\asymp\sqrt n\) the lower bound grows like
\(n^{1/4}/\sqrt{\log n}\). Paley kernels have a uniformly
bounded coherence constant, so the obstruction applies to the
actual linear kernels, including prime kernels. It concerns
arbitrary even mean-zero errors. It does not show that the
nonlinear activation, an approximation scheme, or an actual orbit
produces these errors. Consequently it blocks a generic closure
estimate for this seminorm, while leaving open propagation bounds
that exploit additional structure of the actual errors.

## 7. Scoped acceptance of the completed growing-depth note

This checks [the growing-depth note](parallel-depth-window-30.md),
principally Sections 3--4 and 9, assuming the inherited quantitative
parity/closure package identified there. That package is not reproved
in this audit. No material error was found in the new deduction.

For the ellipse parameter \(\varrho=1+\sqrt\tau/U\), the vertical
semiaxis is
\(U(\varrho-\varrho^{-1})/2<\sqrt\tau\). Therefore
\(\operatorname{Re}(z^2+4\tau)>0\) throughout the ellipse.
The principal square root is analytic there. Its major semiaxis is
at most \(U+\tau/(2U)\); using \(U\ge2\sqrt\tau\) shows
\(|\sqrt{z^2+4\tau}|<U+3\sqrt\tau=M\). The coefficient bound
\(|a_j|\le2M\varrho^{-j}\) and the chosen even degree give the
stated error. The monomial coefficient norm of \(T_j\) is at
most \((1+\sqrt2)^j\), so the displayed bound on \(S_U(P)\)
is conservative. The degree is indeed
\(O_\tau(U\log(C_\tau U/\epsilon))\).

The unweighted resource bookkeeping is necessary and is included.
If \(N,D_*,R_*\le U\), expanding degree \(m\) gives count
and maximum rank/dimension with logarithms bounded by
\(O(m\log(CU))\). The same bound controls the sum of ranks and
dimensions of the resulting list, not just the coefficient-weighted
norm. Substituting the degree bound gives

$$\log U'\le C_\tau U[\log(C_\tau U/\epsilon)]^2.$$

This controls tiny-coefficient large-rank objects as claimed.
The coefficient weight has a smaller compatible bound from
\(S_U(P)\); retained terms, the actual forcing coefficient
\(b_t\in[0,2]\), duals and lift choices are all covered by the
stated conservative ledger. With
\(U\ge\max(C_\tau,\epsilon^{-2})\), enlarging the fixed
constant makes \(2^{C_\tau U^2}\) a valid majorant.

Choose the initial resource of polynomial size in
\(\epsilon^{-1}\), as the construction permits. If
\(V_0=(U_0+C_\tau+2)^4\), \(V_{j+1}=2^{V_j}\), then
\(U_j\le V_j^{1/4}\) follows from
\(C_\tau\sqrt{V_j}\le V_j/4\), after enlarging the base
constant once. For \(\epsilon=T^{-(B+2)}\),
\(\log_2^*V_0\le\log_2^*L+O_{\tau,B}(1)\), where
\(L=\log_2^*q\). The chosen
\(T=\lfloor L-\log_2^*L-c_{\tau,B}\rfloor\) therefore
ensures \(\log_2^*V_{T+1}\le L-2\), so
\(U_{T+1}<q^{1/4}\). This is a quantitative simultaneous
window, rather than a diagonal extraction from fixed-depth limits.

The actual root forcing in (4) is exact and is kept with its
field-dependent coefficient. The induction needs a sup bound on
the formal approximant, not on the actual scaled field: activation
is 1-Lipschitz and \(K\) is an RMS contraction. Under the
resource cap this gives the stated linear accumulation of
\(\epsilon+q^{-1/4}\). The scalar test uses
\(\|x\|_{2,n}\le1\). The relaxed root recursion is convex,
so no extra factor \(T\) enters its maximum. The resulting mark
error is bounded by
\(C(T\epsilon+Tq^{-1/4}+n^{-1})\), which implies the advertised
\(O_{\tau,B}(T^{-B})\) bound on the window.

For a square field and a fixed positive relaxation, the exact
finite source inequality applies at this same moving horizon.
Uniformly small roots give \(\bar\eta=o(1)\) and
\(\widehat u_{T,0}=2\beta_T+o(1)=O(1)\). The remaining
baseline term \(k_n\beta_Ta\) is bounded, while the energy and
dissipation reserves are nonnegative. Dividing the finite inequality
by \(T\to\infty\) therefore proves the positive lower bound
\(\rho c_\tau/C_\tau\). It also proves it on every diverging
subhorizon below the marked window. This conclusion is genuinely
about actual square trajectories on a growing window; it neither
identifies a prime arithmetic law nor supplies the prime tail bound.

The corrected Section 8 now distinguishes bounded kurtosis of
the normalized increment from an absolute fourth-moment bound.
Formula (26) supports the stated rates: with bounded normalized
kurtosis, relative increment error and vanishing endpoint error
suffice for fixed cutoff Lipschitz constant; with only an absolute
fourth-moment bound, the sufficient endpoint rate is \(o(d^2)\).
No such kurtosis or actual prime small-ball estimate is proved.

## 8. Scoped acceptance of the arithmetic-coset audit

The main new statements in
[Astra's arithmetic note](astra-arithmetic-coset-30.md) are valid
with their explicit hypotheses. The low-order joint law is reused
from earlier project results, not counted here as a new theorem or
a fresh audit of all their sheaf identifications.

For Proposition 1, the finite list has one common finite Galois
model \(L/\mathbb Q\), including \(\mathbb Q(i)\). Along a
subsequence of base-prime squares, \(\operatorname{Frob}_r\)
has one conjugacy class \(h\), so square leading traces are
\(\operatorname{Tr}R_j(h^2)\). Finite Chebotarev gives positive
density of primes with Frobenius conjugate to \(h^2\),
simultaneously for all representations. The restriction of
\(h^2\) to the order-two quotient for \(\mathbb Q(i)\) is
trivial, so those primes are \(1\bmod4\). The fixed-word errors
vanish. No common Mellin compact group is needed. The premise is
a common finite-Artin model of the correctly normalized invariant
modules, not merely a finite list of syntax trees or residue signs.

Proposition 1b also checks. Boundedness of **all** archimedean
conjugates and integrality in a fixed number field make the set of
possible Frobenius traces finite. Chebotarev and continuity then
put every group trace in that same finite set. The matrix algebra
spanned by a semisimple representation is semisimple, and its
representation trace pairing is nondegenerate in characteristic
zero. A basis chosen from group matrices therefore determines
each image matrix by finitely many traces, each from the finite
set, forcing finite image. Semisimplicity, a common global model,
and integrality **after normalization** are substantial hypotheses;
none has been silently obtained for the nested Paley modules.

The constant-phase countermodel has the claimed limited scope.
For \(c=(3+4i)/5\), \(c+c^{-1}=6/5\) and
\(c^2+c^{-2}=-14/25\), with gap \(44/25\). The phase is not
a root of unity because its rational trace is not an algebraic
integer. At an auxiliary prime away from 5 it defines a continuous
constant rank-one representation. Pairing it with its reciprocal
keeps the observed fields real without removing its even mixed
invariant trace. The two-lift Jacobi reciprocity gives the stated
lift-invariant version. This is an allowed fieldwise phase model,
not a word from the untwisted Paley construction or an established
common compatible model over varying rational primes. Thus it
does not refute the actual arithmetic matching premise.

The normalized CM trace example likewise shows why integrality
before a Tate normalization is insufficient. It is not evidence
that this elliptic module occurs among the actual Paley punctual
invariants. Finite-Artin Chebotarev and a hypothetical horizontal
phase-support theorem are appropriately kept separate.

Finally the nine-variable formula has the correct normalization.
With counting convolution,

$$t=s(s*s),\qquad u=s(s*t),\qquad
x=Fs/\sqrt n,\quad y=Ft/n,\quad z=Fu/n^{3/2}.$$

Consequently Fourier orthogonality gives

$$\langle xz^3\rangle
=\frac{(s*u*u*u)(1)}{n^5}
=\frac1{n^5}\sum_{a,b,c\in Q}s(abc)u(a)u(b)u(c).$$

Inversion-evenness of \(s\) removes the inverse in the last
factor. Expanding each \(u(a)\) uses two more variables and five
sign factors, so the final expression has nine variables and
sixteen factors, exactly as stated. There is no extra Fourier
factor of \(n\).

The conditional transfer retains the correct quantifiers: a
simultaneously matched cutoff list at each sufficiently large fixed
depth could refute the \(\liminf_T\) prime criterion; matching
only an unbounded selection of depths could not. The note proves
neither this common finite-Artin premise nor the needed phase
accumulation for the nested words. The prime criterion and Problem
26 therefore retain their previous open status.
