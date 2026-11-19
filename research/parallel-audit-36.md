# Endpoint implementation, finite witnesses, and a universal completion bound

Round 36. This note accepts the one-FFT endpoint implementation and
the inspected finite positive-witness protocol. It also proves a new
deterministic completion bound: for every actual eligible Paley field,
at each fixed positive floor, the prescribed averaged proposal can be
made strictly positive by one round-34 reflection after \(O_\tau(n^{5/4})\)
exact Picard steps. An energy-only bound first gives \(O_\tau(n^2)\);
the known finite stationary cap improves its exponent. This is a
polynomial-depth statement, **not** the
short-window prime estimate required for ETH26.

Only this audit prefix is written.

## 1. The endpoint implementation is exactly the projected average

Use the notation of [averaged-mark-35](averaged-mark-35.md):
\(v_{t+1}=K\phi_t\), \(\phi_t=\sqrt{v_t^2+4w}\), \(v_0=0\),
\(\mu_t=\mathbb E_n\phi_t/2\), \(M=T^{-1}\sum_{t=1}^T\mu_t\).
The projected averages satisfy

$$
X_{\sigma,T}
=\frac{\mu_T-\mu_0}{2T}1
+\frac1{4T}\sum_{t=1}^T
 [\phi_t+\phi_{t-1}+\sigma(v_t+v_{t+1})].
\tag{1}
$$

The implementation in [endpoint-stress-36.py](endpoint-stress-36.py)
accumulates \(\sum(v_t+v_{t-1})\). Its terminal addition is
\(v_T+v_{T+1}-v_1\), since \(v_0=0\). Exactly,

$$
\sum_{t=1}^T(v_t+v_{t-1})+v_T+v_{T+1}-v_1
=\sum_{t=1}^T(v_t+v_{t+1}).
$$

Its activation sum and constant \((\mu_T-\mu_0)/(2T)\) therefore
have the correct indices and factors. The initial \(v_1\) and the
look-ahead \(v_{T+1}\) are necessary. Apart from initialization and
terminal repair, the optimized generator uses one application of
\(K\) per Picard step. Its optional direct-projection diagnostic
deliberately performs extra transforms.

The independent checker verifies (1) as an **exact vector identity**
at the actual rational prime-13 kernel for arbitrary even rational
activations and \(T=1,2,5\). This algebra needs only
\(v_{t+1}=K\phi_t\), so these rows are not mislabeled as fixed-weight
orbits. It also calls the optimized implementation with its direct
comparison at \((p,T)=(13,1),(13,8),(17,8)\). These floating
implementation checks are not positivity certificates.

## 2. A quantitative endpoint bound on the actual clipped deficit

Let

$$
C_{\sigma,T}=\frac1T\sum_{t=1}^T
             \frac{\phi_t+\sigma v_t}{2}>0,\qquad
U_\sigma=C_{\sigma,T}/M.
$$

The \(C\)'s have common mean \(M\), and \(U_\sigma\) have mean one.
The opposite component telescopes:

$$
\boxed{\quad
X_{\sigma,T}=C_{\sigma,T}
 +\frac{\sigma}{2T}P_{-\sigma}(v_{T+1}-v_1).
\quad}\tag{2}
$$

Define the normalized endpoint error

$$
h_\sigma=
\frac{\|P_{-\sigma}(v_{T+1}-v_1)\|_2}
     {2T\sqrt n\,M},\qquad z_\sigma=X_{\sigma,T}/M.
$$

Since \(C_{\sigma,T}\) is positive,

$$\mathbb E_n(z_\sigma)_-^2\le h_\sigma^2.\tag{3}$$

For the actual canonical weights, each raw pair has product \(w_i\).
Cauchy--Schwarz over time gives
\(C_{+,T}(i)C_{-,T}(i)\ge w_i\). Assuming \(0<\tau<n\), this is
at least \(c=\tau/n\). Hence
\(U_+U_-\ge c/M^2=:r\). In particular
\(\mathbb E_n(1/U_\sigma)\le1/r\).

For any \(\kappa>0\), the scalar inequality
\(x(2\kappa-x)_+\le\kappa^2\) and the Lipschitz property of
clipping prove

$$
\boxed{\quad
\mathbb E_n d_\sigma
\le\frac{\kappa^2M^2}{c}+h_\sigma
\le\frac{\kappa^2 B_{n,T}}{\tau}+h_\sigma,
\quad
d_{\sigma,0}=0,\
d_{\sigma,i}=(2\kappa-z_\sigma(i))_+.
\quad}\tag{4}
$$

The deletion of the marked deficit only decreases this upper bound.
This estimates the actual, specified clipped proposal, rather than
an arbitrary perturbation or an unknown stationary row.

There is a fully uniform energy upper bound. Put

$$a_1=(1-\sqrt c)^2(1-1/n),\qquad
H_0=n\mu_0^2=\frac{[1+(n-1)\sqrt c]^2}{n}.$$

The energy telescope gives
\(E_{T+1}\le E_1+4WT=4(a_1+WT)\), and
\(\mu_t\ge\mu_0\). Consequently

$$
h_\sigma
\le\frac{\sqrt{WT+a_1}+\sqrt{a_1}}{T\sqrt{H_0}}.
\tag{5}
$$

For \(n\ge16\), \(a_1\le1\), \(H_0\ge\tau/2\), and \(W\ge1\);
thus the convenient coarser bound is

$$\boxed{h_\sigma\le4\sqrt{W/\tau}\,T^{-1/2}.}\tag{6}$$

The independent rational endpoint checks also verify (3)--(4)
without square-root comparisons, by squaring the nonnegative
remainder in (4). Their arbitrary activations have a rigorously
computed positive minimum raw product; the actual constant-weight
specialization is proved above.

## 3. Universal positive completion from endpoint estimates

**Theorem.** Suppose \(n\ge16\), \(0<\tau<n\). Set

$$
s=\min(\tau,1),\qquad
\kappa=\frac{s}{24W\sqrt n},\qquad
T\ge \frac{331776\,W^3}{\tau s^2}\,n^2.
\tag{7}
$$

For the exact averaged rows \(z_\sigma\), the one-step clipped reflection

$$p_\sigma=z_\sigma+2L_\sigma d_\sigma$$

is strictly positive, has mean one, remains in the actual sector,
is even, and preserves its marked value. In fact its bulk entries
are at least \(5\kappa/4\), and its marked value exceeds \(\kappa\).

**Proof.** The inherited actual coherence bound for the pinned
reflection is \(\Gamma_{n,\sigma}\le3/\sqrt n\). Since
\(B_{n,T}\le W+1\le2W\), the first term of (4) contributes at most

$$
3\sqrt n\frac{2W}{\tau}\kappa^2
=\frac{\kappa s}{4\tau}\le\frac{\kappa}{4}
$$

to \(\Gamma\|d_\sigma\|_1\). The condition (7), whose prefactor is
\(576^2\), and (6) give

$$
3\sqrt n\,h_\sigma\le\frac{\kappa}{2}.
$$

Thus the full absolute spill is at most \(3\kappa/4\).
Every clipped bulk value is at least \(2\kappa\), so every repaired
bulk value is at least \(5\kappa/4\).

It remains to check the mark rather than assume it. At the mark,
time Cauchy--Schwarz gives \(C_+(0)C_-(0)\ge1\), while each
\(C_\sigma(0)\le nM\) by positivity. Hence
\(U_\sigma(0)\ge1/(nM^2)\ge1/B_{n,T}\).
The coordinate error from (2) is at most \(\sqrt n\,h_\sigma\).
Therefore

$$
z_\sigma(0)\ge
\frac1{2W}-\frac{s}{144W\sqrt n}>\kappa.
$$

The last strict inequality uses \(s\le1,\sqrt n\ge4\);
after multiplication by \(W\), its margin is at least
\(1/2-7/576=281/576>0\).
The pinned projection preserves that mark, as well as mean and
sector. Evenness is preserved at each operation. This proves the theorem.

For fixed \(\tau\), (7) is \(O_\tau(n^2)\) exact Picard depth.

**Sharper diameter version.** The known finite stationary cap gives

$$\|v^*\|_2\le R=2\sqrt W\,Q^{1/4},\qquad Q=2n+1.$$

For completeness, existence is supplied by the strictly concave
positive weighted barrier. The stationary identity and coherence give
\(\|v^*\|_1\le2\sqrt{nW}\),
\(\|v^*\|_\infty\le2\sqrt{QW/n}\), hence
\(\|v^*\|_2^2\le4W\sqrt Q\).
The Picard map is nonexpansive, so each orbit point lies within
\(\|v^*\|_2\) of \(v^*\). In particular
\(\|v_{T+1}-v_1\|_2\le2R\), without a convergence rate.
Consequently (5) improves to

$$
h_\sigma\le\frac{R}{T\sqrt{H_0}}
\le\frac{2\sqrt2\,\sqrt{W/\tau}\,Q^{1/4}}{T}.
\tag{8}
$$

With the same \(s,\kappa\), it is therefore sufficient to take

$$
\boxed{\quad
T\ge \frac{288\sqrt2\,W^{3/2}}{s\sqrt\tau}\,
              nQ^{1/4}.
\quad}\tag{9}
$$

Indeed (8)--(9) imply
\(3\sqrt n\,h_\sigma\le\kappa/2\) and
\(\sqrt n\,h_\sigma\le s/(144W\sqrt n)\), exactly the two
endpoint estimates used in the proof above. All the same strict
positivity, mean, sector, evenness, mark, and bulk-floor conclusions
follow. This is \(O_\tau(n^{5/4})\).

The constants are intentionally conservative. Its improved asymptotic
exponent does not mean it gives a smaller numerical horizon than every
other bound at the listed finite primes. This theorem gives no efficient
small-depth claim, and does not certify floating generation of that
long exact orbit. Its eventual rational positive witnesses can be
verified by the same finite Fourier protocol.

The depths in (7) and (9) are far outside the currently proved simultaneous
marked arithmetic window. The theorem does **not** show that both
preserved physical marks approach one there. It therefore yields
no theta limit and is compatible with every square obstruction
in round 35. Its purpose is a deterministic completion baseline,
separating eventual feasibility from the short-depth prime finish.

## 4. The finite Astra witnesses have the right exact proof premises

I inspected [astra-averaged-positive-36.py](astra-averaged-positive-36.py),
the two small records, and the available large positive record.
The two \(p=9413\) inputs were independently replayed to
[parallel-audit-36-small-replay.jsonl](parallel-audit-36-small-replay.jsonl);
the records are byte-for-byte identical. No million-order FFT is
repeated in this audit.

The exact proof of the affine constraints is:

1. Integer Fourier coefficients have exact DC coefficient equal to the
   scale, exact inversion symmetry, and exact zero forbidden coefficients.
   Their exact Fourier transform is thus a real even row with mean one
   in \(1+V_\sigma\).
2. The exactly defined clipped deficit is even and has \(d_0=0\).
   Interval comparisons certify every clipping branch; ambiguous
   branches cause rejection.
3. With \(\ell=P_\sigma e_0\), \(a_\sigma=\ell_0\), the implemented
   correction is \(2[P_\sigma d-\ell\langle\ell,d\rangle/a_\sigma]
   =2L_\sigma d\). Its mean and marked entry are exactly zero and
   its sector is \(V_\sigma\). It also preserves evenness.

The additional interval balls containing zero for mean, mark,
evenness, energy, and Fourier support are independent checks, not
the logical proof of exact equality. Nonnegativity is different:
strict positive lower endpoints for every output coordinate
really do prove it.

Only positivity is needed for theta, so failure of the former
\(\kappa=.001\) floor test is harmless. The \(p=9413,T=128\)
row has positive repaired minima on both sides, while its
\(T=64\) row has strictly negative certified coordinates. The
available million-order \(T=128\) record likewise has positive
minima, including the plus minimum around \(4.74\cdot10^{-5}\);
it does not claim the old floor.

The exact Fourier marks give valid theta intervals directly.
They need not be related to an exact Picard orbit for this finite
witness argument. In particular **the exact Picard budget is not
automatically inherited by the rounded proposals**. Both the
generation metadata and replay explicitly disclaim that extra
claim. To invoke the asymptotic exact-orbit theorem for a rounded
family would require orbit shadowing, an explicit rounding-error
bound, or a separate budget proof.

## 5. The new large negative control has a narrow, valid scope

Main reports a validated negative coordinate for the saved
\(p=7340033,T=128\) Fourier input generated from the optimized
floating endpoint proposal. The same native replay protocol,
when it proves a negative upper endpoint, excludes positivity
of **that explicitly defined reflected exact Fourier trial**.

It is not a shadowing certificate for the unrounded exact Picard
average. It does not exclude another positive completion preserving
the same marks, and does not show eventual failure over primes.
No such stronger inference is made here. The independent large
replay is being handled by Main; this audit does not duplicate it.

## 6. Reproduction and remaining scope

The independent [minimal checker](parallel-audit-36.py) emits nineteen
records: six exact endpoint-algebra checks, six small floating
direct-projection comparisons, six corresponding floating stress
rows, and a final success row. Two independent runs were
byte-for-byte identical.

    .venv/bin/python -B research/parallel-audit-36.py \
      > research/parallel-audit-36.jsonl

    .venv/bin/python -B research/astra-averaged-positive-36.py --replay \
      research/astra-averaged-positive-36-p9413-t128-input.json.gz \
      research/astra-averaged-positive-36-p9413-t64-input.json.gz \
      > research/parallel-audit-36-small-replay.jsonl

No stationary solve or large FFT was run. The finite algebra and
endpoint-completion theorems are proved independently of the recorded
floating signs. The open prime task remains much shorter-depth
positivity compatible with the marked arithmetic limit, or a
different way of controlling those preserved marks.

## 7. Acceptance of Astra's completed endpoint-horizon note

After the written [astra-averaged-positive-36](astra-averaged-positive-36.md)
appeared, I checked its weighted identities and uniform horizon in
addition to the finite protocol above. Its twelve endpoint/horizon
records were independently replayed to
[parallel-audit-36-endpoint-replay.jsonl](parallel-audit-36-endpoint-replay.jsonl)
and are byte-for-byte identical. Those evaluations do not execute
the very long trajectories.

The weighted decomposition retains the positive
\(\frac12\sum\alpha_t(A_{\sigma,t}+A_{\sigma,t-1})\) term.
Its scalar term is nonnegative by summation by parts and
\(\mu_t\ge\mu_0\). The terminal coefficients are exactly
\(-\alpha_2\) at \(v_1\), \(\alpha_{j-1}-\alpha_{j+1}\)
at interior \(v_j\), and the stated final two coefficients.
For decreasing weights the positive coefficients sum to
\(\alpha_1+\alpha_2\), proving the displayed absolute estimate.
The uniform-prefix vertices of the decreasing probability simplex
give its claimed uniform-weight minimum when \(T\ge3,b\le D\).
This optimizes that available absolute estimate, not actual signed
prime trajectories.

The stationary cap \(R\) used in (8) above also supplies the global
coordinate cap \(D=R+2\sqrt{QW/n}\) for every Picard iterate.
Hence every raw coordinate is at least
\(a_D=2c/(\sqrt{D^2+4c}+D)\). Combining that positive term with
the scalar sign and terminal bound proves its **unrepaired**
positivity horizon \(T>(2D+b)/(4a_D)\), of asymptotic order
\(n^{3/2}\) at fixed floor. The argument uses only a known finite
stationary cap, not a field-uniform bounded stationary energy.

For positivity alone, the independent reflection bound (9) improves
this asymptotic exponent to \(5/4\), at the expense of a correction,
a shrinking output floor, and large constants. Neither statement
controls the marked Cesaro condition at its depth. The unrepaired
bound may be numerically smaller at the listed finite orders.

The zero-time comparison also checks: including times \(0,\ldots,T\)
removes the budget penalty but changes the marked limit to
\(1-1/[2(T+1)]\). Comparing its squared squeeze constant with
\(1+\tau+1/T\) yields exactly
\(\tau<(T+1)/[T(4T+3)]\). Dropping that half-mark loss would
give the wrong comparison.

## 8. Acceptance of the automatic marked-phase theorem

I independently checked the complete proof and checker in
[parallel-cold-complex-36](parallel-cold-complex-36.md).
The eight exact/Arb records were independently regenerated as
[parallel-audit-36-complex-replay.jsonl](parallel-audit-36-complex-replay.jsonl)
and are byte-for-byte identical. No mathematical correction is needed.
This is a substantive reduction of the complex route: on a common
right-half-plane domain, the growth obligation is automatic.
The common **cold** domain through primes remains unproved.

### Conjugate identity and the phase component

For \(u=1+B\xi\), with \(B\) real, the stationary equations
\(B^T(w/u)=0\) can be paired with both \(\xi\) and
\(\overline\xi\). Thus both identities in its (4) are exact;
complex weights do not need to be conjugated in those equations.
Writing \(r_0=\overline u_0/u_0\),

$$
|W-r_0|\le(n-1)|c|
\quad\Longrightarrow\quad
\operatorname{Re}(W\overline r_0)\ge\operatorname{Re}W.
$$

The scaling direction is correct:
\(W\overline r_0=|W|A_0/\overline A_0\).
Therefore the marked values lie in two separated sectors about
the positive and negative real axes, of angular half-width
\(\frac12|\arg W|<\pi/4\). The opposite row has the same mean,
and its conjugate inner product with \(A\) is \(|W|\), so the
alternative normalization check agrees.

For a nonzero scalar continuation \(e^m\), continuity and
connectedness fix the positive sector from the real base point.
The analytic logarithm differs from the principal logarithm of
a positive-real-part function by a constant multiple of \(2\pi i\);
the real anchor makes that multiple zero. Thus the conclusion
bounds the unwrapped phase, not a separately chosen pointwise
argument.

### Generic scalar lifts

Saturating with \(s\prod_i u_i=1\) excludes coordinate-zero
components. At the positive real base point the stationary Jacobian
is invertible, so the saturated variety is smooth of dimension one
there and has one irreducible curve through that point. Its
projection to the parameter is nonconstant.

Its dominant image in the \((\tau,u_0)\) plane is an irreducible
curve. A dominant map of affine irreducible curves has image
containing a nonempty Zariski-open subset; its missing image
points are therefore finite. Equivalently the generically finite
function-field argument in the note applies. Consequently the
continued scalar polynomial identity can be lifted to a saturated
stationary point outside finitely many parameter values. This
justifies using the phase theorem even without a single-valued
full-row continuation.

A planar domain remains connected after finitely many points
are removed. For a continuation of \(A_0\) alone, its possible
zeros also lie among those finite lift exceptions, since the
generic lifted marked coordinate is nonzero. The positive-sector
choice extends by continuity to nonnegative real part throughout
the domain. The strong minimum principle and the positive base
value then make the real part strictly positive and exclude all
zeros. This supplies its canonical logarithm.

### Automatic growth and the actual square branch point

The strip \(|\operatorname{Im}m|<\pi/4\), after subtraction of
the real hot anchor, maps into the unit disk under \(\tanh\).
Schwarz's lemma and the principal inverse \(\operatorname{arctanh}\)
give exactly its (10). The latter inverse is applied only in the
strip where it is the inverse of \(\tanh\). A fixed inner compact
domain has an \(O(1)\) field-uniform bound, enough for the
two-constants argument. An arbitrary connected common domain
containing the real interval can be restricted to a common simply
connected tube inside it.

The explicit disk constants, \(65533\), the harmonic exponent,
and the \(n>e^{100000}\) sufficient threshold check. The inner
radius-1024 circle is in the hot region except for its left
endpoint, where continuity of the assumed extension supplies the
same bound. The square lower ratio is strictly larger than
\(4/3\) for \(h\ge11\) because its finite \(W<5/4\).

Failure of extension to the displayed centered disk makes the
actual Taylor radius strictly smaller than that disk radius.
Some boundary point is a singularity of this actual logarithmic
germ and has real part \(>1/16\). The intersection of its Taylor
disk with the hot region is connected: rotate each point about
the positive center toward its rightmost radius, which increases
its modulus about zero while staying in the Taylor disk.
Therefore a boundary point of modulus \(>1024\) would be extended
by the actual hot branch, a contradiction. The singularity is in
the claimed cold region.

Lastly, on the normalization near an accessible point write
\(\tau=\tau_*+t^k\), \(A_0=t^j h(t)\), \(h(0)\ne0\).
A sufficiently small full \(t\)-circle stays above the right
half-plane and avoids the finitely many lift exceptions.
Its marked values remain in one separated phase sector, so their
winding is zero. Their winding is also \(j\); hence \(j=0\).
Thus the first scalar-log singularity is neither an ordinary zero
nor pole. Since the marked function is algebraic, the remaining
obstruction is genuine marked ramification with finite nonzero
limiting value. This argument does not select a zero of an
unrelated eliminant or assume that every sheet is physical.

The square assertion is an existence theorem at a deliberately
enormous threshold. It gives no practical branch location and no
prime branch point. The finite prime-13, prime-17, and square-25
half-plane examples remain compatible with it.
