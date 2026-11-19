# Actual reciprocal circulants: positive Schur clipping and a precision obstruction

Round 33, 2026-11-18. This supplies finite statements about the **actual**
positive reciprocal circulant pair. It does not prove HR, prime UI, or
Problem 26. No general-coherence counterfamily is used.

The useful positive statement is an automatic Loewner and weighted
Fourier-coefficient bound for every actual bulk hard hinge. It uses
positive definiteness, not entrywise positivity of the position rows.
The accompanying obstruction explains why this bound cannot be passed
through the unweighted support mask by a positive-map argument, or by
calling the precision matrix a near M-matrix.

## 1. Exact normalized position kernels

Use \(c=\tau/n\), \(W=1+(n-1)c\), \(a=\sqrt{W/n}\), and
\(\rho=c/a^2=\tau/W\). Let

$$A=a u>0,\qquad B=a v>0,\qquad AB=w,\qquad
\mathbb E_nu=\mathbb E_nv=1,\qquad A_0B_0=1.$$

Assume \(0<c<1\), which holds for all sufficiently large fields
at each fixed positive floor.

Let \(f_A,f_B\) be their normalized inverse Fourier rows, so the
circulant matrices \(C_A,C_B\) have eigenvalues \(u,v\), unit
diagonals, and opposite off-identity supports \(D_\sigma,E=D_{-\sigma}\).
They are positive definite. Write \(u_0=A_0/a\), \(v_0=B_0/a\).
The accepted position factorization gives, exactly,

$$C_A\circ C_B=I,\qquad
C_AC_B=\rho I+\gamma\mathbf1\mathbf1^{\mathsf T},\qquad
\gamma=(1-c)/W.$$

Normalizing their row sums gives symmetric signed stochastic kernels

$$T_A=C_A/u_0,\qquad T_B=C_B/v_0,\qquad
\boxed{T_AT_B=cI+(1-c)J.} \tag{1}$$

Translation caps imply all their eigenvalues lie in \([c,1]\), with
constant eigenvalue one. If a position row is nonnegative, its normalized
matrix really is a positive semidefinite Markov kernel.

There is a quantitative version when it has a negative part. Put
\(\epsilon_A=\sum_k(f_A(k))_-/u_0\), and similarly for \(B\).
Normalizing the entrywise positive part gives a symmetric Markov kernel
\(\widehat T_A\) with

$$\|\widehat T_A-T_A\|_{\rm op}\le2\epsilon_A,\qquad
\|\widehat T_A\widehat T_B-[cI+(1-c)J]\|_{\rm op}
\le2(\epsilon_A+\epsilon_B). \tag{2}$$

Indeed \(T_A=(1+\epsilon_A)M_A^+-\epsilon_AM_A^-\), where
the two \(M\)'s are symmetric Markov kernels. Their operator norms are
at most one. The product bound also uses \(\|T_B\|_{\rm op}\le1\).
This is a valid positive approximation supplied by small normalized
negative positional mass. It does not control inverse weights at their
small spectral scale \(c\asymp n^{-1}\). For example inverse perturbation
would require \(2\epsilon_A<c\), and then pays
\(2\epsilon_A/[c(c-2\epsilon_A)]\). A small constant negative fraction
does not meet that requirement.

## 2. Automatic positive Schur bound for the actual hard hinge

For each \(R\ge0\), put

$$q_R(i)=(u_i-R)_+\mathbf1_{i\ne0},\quad
\eta_R=\mathbb E_nq_R,\quad
\nu_R=\mathbb E_n(q_R^2/u),\quad
\kappa_R=\operatorname{DFT}(q_R)/n.$$

Let \(C_R\) be the circulant with eigenvalues \(q_R\), and write
\(\beta=\operatorname{DFT}(v)/n=f_B\). All rows here are real even;
the Fourier orientation consequently causes no inversion ambiguity.
The actual bulk root deletion is included in \(q_R\). Since
\(0\le q_R\le u\), one has

$$0\preceq C_R\preceq C_A.$$

The Schur map \(\Phi_B(X)=C_B\circ X\) is completely positive,
unital, and satisfies \(\Phi_B(C_A)=I\). Therefore

$$\boxed{0\preceq X_R:=C_B\circ C_R\preceq I.} \tag{3}$$

No assertion that \(\beta\) is entrywise nonnegative is needed.
For a sharper inequality, the positive block matrix

$$\begin{pmatrix}C_A&C_R\\C_R&C_RC_A^{-1}C_R\end{pmatrix}\succeq0$$

remains positive under the amplified Schur map. Its Schur complement
gives \(X_R^2\preceq Y_R:=\Phi_B(C_RC_A^{-1}C_R)\).
Since \(q_R^2/u\le q_R\), also \(Y_R\preceq X_R\). Taking a diagonal
entry yields the exact coefficient bound

$$\sum_k|\beta_k\kappa_R(k)|^2\le\nu_R\le\eta_R.$$

Here \(\beta_0=1\), \(\kappa_R(0)=\eta_R\), and \(\beta\) vanishes
outside \(\{0\}\cup E\). Hence

$$\boxed{\sum_{k\in E}|\beta_k\kappa_R(k)|^2
\le\nu_R-\eta_R^2\le\eta_R(1-\eta_R).} \tag{4}$$

Cauchy--Schwarz with \(\mathbb E_nu=1\) verifies
\(\nu_R\ge\eta_R^2\), so the right side is nonnegative. For the
actual hard hinge \(h_R=a q_R\) and coefficients
\(r_k=\operatorname{DFT}(h_R)_k\mathbf1_E/n\), this reads

$$\boxed{\sum_{k\in E}|\beta_kr_k|^2
\le a^2(\nu_R-\eta_R^2).} \tag{5}$$

This is a uniform finite estimate on the actual source, stronger
than a statement about arbitrary test matrices alone.

## 3. The unweighted HR mask does not preserve this order

HR concerns a different quadratic form:

$$H(R)^2=n\,r_E^*C_B[E,E]r_E
-\frac ba\left|\sum_{k\in E}r_k\right|^2.$$

The matrix \(C_B[E,E]\) contains \(\beta_{k-l}\), whereas (5)
weights each single coefficient by \(\beta_k\). These are not
interchangeable.

In particular the Schur mask with entries \(\mathbf1_E(i-j)\)
is not a positive map. Its matrix has zero diagonal and nonzero
off-diagonal entries, so it is not positive semidefinite. Applying
it to a rank-one all-ones positive matrix already exhibits the
failure. There is even a failure within the **actual bulk hinge**
family: at \(R=0\),

$$C_R=C_A-u_0J,\qquad
\mathbf1_E\circ C_R=-(u_0/n)\,[\mathbf1_E(i-j)].$$

This is nonzero with zero diagonal and is indefinite. Equivalently
\(P_{-\sigma}q_0=-u_0P_{-\sigma}e_0\ne0\). Thus deleting the
mark before projection really matters, and the Loewner relation
in (3) cannot simply be passed to the unweighted support restriction.
Doing so would incorrectly force this actual hinge response to zero.

Nor does an all-vector comparison against the weights in (5) give
a uniform shortcut. The diagonal of the HR matrix
\(C_B[E,E]-(b/(an))\mathbf1\mathbf1^{\mathsf T}\) tends to one.
A comparison with \(M\operatorname{diag}(|\beta_E|^2)\) would force
every \(|\beta_k|^2\gtrsim1/M\). But Parseval and the root cap give
\(\sum_{E}|\beta_k|^2=\|B-a\mathbf1\|^2/W=O_\tau(\sqrt n)\).
Since \(|E|\asymp n\), any such all-vector comparison needs
\(M=\Omega_\tau(\sqrt n)\). This does not exclude a source-specific
bound on the actual hinge coefficients; that is precisely the
remaining HR issue.

## 4. Why the precision is not a near M-matrix

The exact inverse is

$$C_A^{-1}=\rho^{-1}(C_B-\kappa\mathbf1\mathbf1^{\mathsf T}),
\qquad \kappa=\gamma/u_0=(1-c)v_0/n. \tag{6}$$

Its off-diagonal entries on \(D_\sigma\) are forced negative.
On \(E\), their total is

$$\rho^{-1}\{v_0-1-|E|\kappa\}.$$

Thus the row mass \(L_+\) of its positive off-diagonal part satisfies

$$\boxed{L_+\ge\rho^{-1}
\left[v_0-1-\frac{|E|}{n}(1-c)v_0\right]_+
\ge\rho^{-1}\left[\frac{1+c}{2}v_0-1\right]_+.} \tag{7}$$

The last inequality uses the actual Paley counts \(|E|\le n/2\).
At each fixed floor the root caps give \(v_0=\Omega_\tau(\sqrt n)\),
so \(L_+=\Omega_\tau(\sqrt n)\), even if \(f_B\) has no negative
entry at all. The diagonal of the precision stays \(O_\tau(1)\).
Consequently its rowwise distance to every matrix with nonpositive
off-diagonal entries is at least this much. The nonnegative
off-diagonal positive part is circulant, so its spectral radius is
exactly \(L_+\); positive diagonal similarity cannot eliminate this
row-mass obstruction.

Small negative mass in \(f_B\) therefore describes a near-Markov
normalized **covariance** kernel, not a near M-matrix precision.
Confusing those two operators would bypass the centering term in
(6) and lose the actual scale. None of (1)--(7) is a counterexample
to actual Paley HR. They supply positive constraints and identify
two invalid ways of converting them into HR.

## 5. Replay scope

The [small-field checker](parallel-audit-33.py) and
[forty records](parallel-audit-33.jsonl) evaluate (1)--(7) on actual
numerical stationary pairs: primes 101 and 401, square order 361,
and a smaller floor at 401, with both sectors and four thresholds.
The eight pair rows check the Markov product, its positive-kernel
approximation, the precision identity and the positive-off-diagonal
lower bound. The thirty-two hinge rows check the full Schur spectral
inequalities, weighted coefficient estimate, and actual indefinite
support mask. No dense large matrix is needed: all these matrices
are circulant and their eigenvalues are Fourier transforms of rows.

The maximum observed Loewner violation is below
\(3.331\cdot10^{-16}\), inverse identity error below
\(2.843\cdot10^{-14}\), and numerical stationary residual below
\(1.993\cdot10^{-12}\). For example at \(p=401,\tau=.01\), one
side has normalized negative positional mass about .000558, yet
precision positive-off-diagonal row mass about 720.17 and diagonal
about 93.78. This illustrates the distinction in (7); it is not an
interval-certified assertion about that stationary point.

These are floating normalization checks, not stationary enclosures
or a prime-uniform HR theorem. The finite identities and inequalities
are proved above independently of the solver.

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
      research/parallel-audit-33.py > research/parallel-audit-33.jsonl

Only files with this prefix are written.

## 6. Independent acceptance of the complex-floor criterion

I independently checked [complex-floor-33](complex-floor-33.md), Sections
1--3, its checker, and all seven records. The independent output
[parallel-audit-33-complex-replay.jsonl](parallel-audit-33-complex-replay.jsonl)
is byte-for-byte identical to the saved seven-record output. The replay was

    .venv/bin/python -B research/complex-floor-33.py \
      > research/parallel-audit-33-complex-replay.jsonl

The conditional continuation argument is correct. On the fixed hot interval
the inherited pointwise invariant ball applies once \(n\ge T+1\), which is
automatic in its field limit. It gives

$$|m_q(t)|\le3/\sqrt n\le6/\sqrt q.$$

For a common bounded rectangle \(D\), the two-constants principle on the
connected slit domain \(D\setminus[T,T+1]\), applied to
\(\log|m_q|\), gives exactly the exponent
\(\omega_a/2\) in (3). Zeros of \(m_q\) do not invalidate the subharmonic
argument. A holomorphic extension must be the extension of the actual
real germ; an unrelated polynomial branch would not suffice. The square
lower bound then forces the stated complex-size exponent
\(\omega_a/[2(1-\omega_a)]\), or failure of the common extension. This
does not prove a complex singularity for an individual square field.

For \(p=13\), differentiating the strictly concave one-variable logarithmic
objective gives the stated cubic with no extra interior real root. Its
quartic discriminant and four Hurwitz determinants are correct. The
leading cubic coefficient has its only zero at \(-6/5\), outside the right
half-plane. Consequently the three roots form unramified holomorphic
branches there; simple connectedness labels them globally. The branch
through \(x(6)=0\) is the real stationary branch. The exact identity
\(f(-1,t)=36\) and the nonvanishing of \(1+5t/6\) justify both logarithms
globally on that half-plane.

The Arb residual balls in the five stationary rows are normalization
checks, not by themselves existence proofs. Here existence and selection
come from the exact cubic and strict concavity; the validated real-root
isolation supplies their finite enclosures. The two remaining rows verify
the exact discriminant/Hurwitz arithmetic and isolate its four complex
zeros. No growing-prime complex domain or subpolynomial growth bound is
certified. Those are still the unproved hypotheses of this alternative
criterion.

## 7. Independent acceptance of the conic UI boundary slope

I checked [parallel-prime-ui-33](parallel-prime-ui-33.md), especially (7)--(22),
and inspected both its positive-pair replay and conic primal/dual replay.
No mathematical correction is required. The finite replays by Main are
not repeated here.

Opposite-sector orthogonality gives all four cross expectations exactly,
so the Hellinger identity (7) uses the full marked product \(uv=m\).
On disjoint bulk high sets the combined error term in the triangle
inequality is at most \(\mathcal D/\kappa\), rather than twice this
quantity. The remaining trial term is at most

$$\frac{\rho}{\kappa R}\mathbb E(p+q)
  =\frac{2\rho}{\kappa R}.$$

This proves (9) for \(R>\sqrt\rho\). Both floating and Arb replay paths
now enforce that restriction. The recorded \(R\ge2\) thresholds satisfy
it. Formula (11) is the upper root of the exact quadratic inequality;
the replay's lower root is evaluated in its stable rationalized form.
Its coordinatewise upper/lower tests therefore certify tails of the
unknown exact stationary source, without turning a floating residual
into a distance estimate.

The conic feasible sets are compact, contain the constant pair, and
interpolate convexly in the floor. The defect is convex by concavity of
the geometric mean. Hence \(d_n(0)=0\) and \(d_n(\kappa)/\kappa\) is
nondecreasing in \(\kappa>0\), including after field limsup.

In the reverse inequality of the boundary theorem, the canonical mixture
(18) gives

$$\frac{\mathcal D}{\kappa}\le \kappa+
\frac{\kappa(L+1)^2}{4(1-\kappa)^2\rho_n}
+(1+1/L)\mathbb E[z\mathbf1_{i\ne0,z>L}]
+\frac{(1-\kappa)(u_0+v_0)+\kappa}{n}.$$

The first term is the full \(\kappa^2\mathbb E m/\kappa\) contribution;
the last is the marked part of the \(\delta^2\) estimate. Fixed-floor root
caps make the last term vanish. No bounded stationary energy is assumed.
Since \(uv=\rho_n\) on the bulk and \(\rho_n\) has a positive finite limit,
the escaping first mass of \(z=u+v\) equals that of the two individual
tails in (14). The stated order (field limsup, then \(\kappa\downarrow0\)
at fixed \(L\), then \(L\to\infty\)) proves equality (15).

In fact the same two bounds show that the canonical affine mixture (18)
itself has field-first defect slope \(\Lambda_{\mathcal F}\). This is a
source-dependent interpretation, not an available primal construction.
At every fixed finite field the derivative at zero remains zero, so it
cannot replace the field-first boundary slope.

For the weak dual, write \(r=a+z_- -\alpha\ge0\). Orthogonality and the
floor give

$$\mathbb E(\alpha p)=a-\mathbb E(rp)
 \le a-\kappa\mathbb E r=(1-\kappa)a+\kappa\mathbb E\alpha.$$

The analogous formula for \(q\), together with
\(\alpha\beta\ge m\), proves (22), with the displayed sign of its floor
term. No strong-duality or dual-attainment theorem is used. The replay
retains exact sector support and means through rational Fourier data,
constructs \(\alpha\beta=m\) algebraically, and checks the covers outward.
The resulting finite positive secants are not limiting boundary slopes.
Neither UI through primes nor ordinary theta follows from the saved
finite certificates.

## 8. Independent acceptance of the hot HR and multiplier distinction

I checked [astra-hardtail-33](astra-hardtail-33.md), Sections 1--4, its exact
dyadic checker, and its finite all-threshold Arb checker. Main's already
completed replay is the implementation acceptance; the checks here are of
the arguments and certificate scope.

The inherited large-floor pointwise bound gives the stated bulk intervals
with \(L_\tau U_\tau=\tau\). The exceptional marked weight is bounded
above as in (4), and is never assigned the false bulk lower bound. Above
the bulk lower spectral endpoint, the hinge is bounded by \(6/\sqrt n\),
which proves (6). Below it every bulk coordinate is active and the exact
projection is \((t-A_0)Pe_0\). Its squared norm divided by affine mass is
convex, so the endpoint argument includes every threshold, including the
zero hinge. The hot upper constant \(6U_\tau\) is correct.

At the fixed threshold \(R_*=L_\tau/\sqrt{1+\tau}\), the bulk remains
active. The marked contribution can be discarded in the lower bound;
the bulk contribution is at least

$$\frac{L_\tau}{\sqrt W}(p-p^2),\qquad p=P_{00}\longrightarrow\tfrac12.$$

Together with \(A_0\to1\) and \(\eta\to1-R_*\), this proves exactly the
constant in (9), asymptotic to \(\sqrt\tau/12\). Thus the optimal eventual
hot HR constant has order \(\sqrt\tau\), under the inherited arithmetic
input. This is an actual-field theorem; it does not analytically
continue its estimate to a cold floor.

The weighted operator lower bound (11) also checks: test the input \(e_0\),
use \(d_0=cB_0/a\), and apply weighted Cauchy--Schwarz to
\(\langle Pe_0,d\rangle\). Fixed-floor root caps then give (12), an
actual-source operator norm of order at least \(n^{1/4}\). This test input
is the mark, which is explicitly absent from the hard hinge. Consequently
it disproves the full weighted multiplier shortcut, not HR or a
bulk-input bound. The rank-one Fourier bounds and Hilbert--Schmidt
identity (13)--(14) are consistent with this distinction.

For the dyadic cyclic family, the recursion preserves means and products
exactly. Each source value on the level-\(j\) nonroot child is bounded by
\(2^{j/2}\); shell sizes give \(O(1/R)\) first-mass tails and logarithmic
unscaled energies. At \(R=U_{k-4}\) only the two stated bulk points are
active. At \(i=n/2\), summing the odd-level differences gives exactly
\(-aL(n+2)/(3n)\), and its single energy term yields \(n/72+o(n)\).
The growing diagonal coherence and unequal sector ranks are real defects
of this comparison family; it is not an actual Paley counterexample.

Finally, the finite Arb checker first proves an invariant contraction ball
around an exactly rational even trial vector. Its Lipschitz estimate for
the positive-root map transfers that enclosure to \(A\). At every true
hinge knot the nominal rational hinge has the stated coordinate error;
the terminal fallback uses \(\|h\|_2\le\|h\|_1\), so it remains valid even
when the mass lower bound vanishes. Convexity between true knots proves
all-threshold coverage without assuming an ordering of nearly equal
knots. These are finite exact-source bounds. Cold prime-uniform HR and
the later marked arithmetic comparison remain open.
