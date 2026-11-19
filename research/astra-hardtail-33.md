# Hard-tail response: a hot theorem, exact cold checks, and two excluded shortcuts

Round 33, 2026-11-18. ETH Problem 26, **ordinary theta**.

**The cold prime-uniform HR inequality is still open.** This round does not
assume UI to prove HR, and does not claim to solve the subsequent marked
comparison. The actual-Paley positive result is a uniform **hot-floor** HR
theorem, with the optimal order of growth of its constant as the floor tends
to infinity. Its arithmetic input is the existing large-floor invariant ball.
There are also rigorous finite cold-floor HR certificates, rather than just
floating stationary diagnostics.

The new results, with their different scopes, are:

* For every fixed `tau >= 1024`, every actual field order `q=1 mod 4` with
  `n=(q-1)/2 >= tau`, both signs and every `R>=0`,
  `H(R)^2 <= 6(sqrt(tau+9)+3) eta(R)`. No UI hypothesis is used.
  The least eventual prime-uniform constant is bounded below by
  `(sqrt(tau+9)-3) / [4(sqrt(tau+1)-sqrt(tau+9)+3)]`.
  Thus its hot growth is **Theta(sqrt(tau))**, not a floor-independent constant.
* The full weighted opposite Fourier projection has norm at least
  `Omega_tau(n^(1/4))` on the **actual stationary weights**, even though every
  individual Fourier-coordinate projection is uniformly bounded. Consequently
  a full weighted multiplier bound cannot be used to prove HR. The actual
  hinge restriction and the removed input mark matter.
* An exact **cyclic, even** stationary family has UI of both sources and
  energies `O_tau(log n)`, but a hard-tail ratio at least `(1/72+o(1))n`.
  It lacks Paley coherence and the Paley sector dimensions. This excludes a
  theorem using only cyclicity, the reciprocal analytic-center constraints,
  and UI; it does not exclude the actual Paley estimate.
* With rigorous stationary enclosures, `C=1` is certified for **all** thresholds
  at `p=101,401,1009`, both signs, at each of `tau=.05,.01,.001`.
  At the actual prime `p=9413`, `tau=1024`, `R=.9`, both ratios are rigorously
  greater than `1.2355`, showing why the constant's floor dependence cannot
  be omitted. These finite results do not prove cold prime-uniform HR.

The four requested notes were read in full:
[source-pair 29](parallel-source-pair-29.md),
[coherent-source 31](parallel-coherent-source-31.md),
[circulant-source 32](parallel-circulant-source-32.md), and
[Schur mixing 32](schur-mixing-32.md).
The accepted round-32 scope remains as recorded in
[nested-joint-32-acceptance.json](nested-joint-32-acceptance.json).

## 1. Conventions and the actual hot theorem

Keep

\[
 c=\tau/n,\quad W=1+(n-1)c,\quad a=\sqrt{W/n},\quad
 \rho=\tau/W,\quad w=c\mathbf1+(1-c)e_0.
\]

The positive stationary spectra are
`A=a1+x`, `B=a1+y`, with `x in V_sigma`, `y in V_-sigma`, `AB=w`.
Write

\[
 u=A/a,\quad d=c/(aA),\quad D=\operatorname{diag}d,
 \quad P=P_{-\sigma},\quad e=Pe_0,
\]

and retain **all** output coordinates in

\[
 h_R=a(u-R)_+\mathbf1_{i\ne0},\quad
 \eta(R)=\frac{\sum_i h_R(i)}{na},\quad
 H(R)^2=\sum_i d_i(Ph_R)_i^2.
 \tag{1}
\]

### 1.1 Input from the existing hot argument

The [large-smoothing note](large-smoothing.md), using its rank-squared
Mellin norm and signed even-product closure, proves

\[
 \sqrt n\,\|A-B\|_\infty\le6
 \quad(n\ge\tau\ge1024).                                  \tag{2}
\]

This is a previously established arithmetic input, **not a new proof here
of that sheaf argument**. The deductions below use its pointwise form,
including the mark. They are not deductions from coherence alone.
Set

\[
 L_\tau=\sqrt{\tau+9}-3,\qquad U_\tau=\sqrt{\tau+9}+3;
 \quad L_\tau U_\tau=\tau.
\]

From the exact positive root formula for `A,B`, (2) gives, off the mark,

\[
 \frac{L_\tau}{\sqrt n}\le A_i,B_i\le\frac{U_\tau}{\sqrt n},
 \qquad
 \frac{L_\tau}{\sqrt W}\le d_i\le\frac{U_\tau}{\sqrt W}.
 \tag{3}
\]

At the mark,

\[
 A_0,B_0\le \sqrt{1+9/n}+3/\sqrt n\le11/10,
\]

and

\[
 d_0=\frac{cB_0}{a}
 \le \frac{\tau(\sqrt{n+9}+3)}{n\sqrt W}
 \le\frac{U_\tau}{\sqrt W}\le11/10.                         \tag{4}
\]

The middle inequality uses that `(sqrt(t+9)+3)/t` is decreasing and
`n>=tau`; the last uses `W>=tau` and `tau>=1024`.
In particular the output weight, including its exceptional entry, has a
uniform upper bound. No false lower bound on `d0` is used.

### 1.2 All thresholds, with a square-root floor constant

**Theorem.** Under (2),

\[
 \boxed{H(R)^2\le6U_\tau\,\eta(R)\quad\text{for all }R\ge0.}
 \tag{5}
\]

**Proof.** Use the physical threshold `t=aR`.
If `t>=L_tau/sqrt(n)`, every nonzero hinge entry is at most `6/sqrt(n)`.
The unweighted orthogonal projection is a contraction, so

\[
 H^2\le\frac{U_\tau}{\sqrt W}\|h\|^2
 \le\frac{U_\tau}{\sqrt W}\frac6{\sqrt n}\sum h
 =6U_\tau\eta.                                           \tag{6}
\]

For `0<=t<=L_tau/sqrt(n)`, all bulk entries are active. Exactly

\[
 Ph=(t-A_0)e,\qquad
 \eta=1-\frac{A_0}{na}-\frac{n-1}{na}t.                    \tag{7}
\]

The ratio of the positive quadratic numerator to this positive affine
mass is convex on the interval. It is enough to check the endpoints.
The upper endpoint is covered by (6). At zero, with
`p=e0^T P e0<=1/2`,

\[
 \frac{H(0)^2}{\eta(0)}
 \le\frac{(11/10)^3/2}{1-11/(10\cdot1024)}<1<6U_\tau.
 \tag{8}
\]

Here `||e||^2=p`, `na=sqrt(nW)>=1024`, and (4) were used. This proves
(5), including zero hinges. Both signs obey the same proof. ∎

### 1.3 A matching order lower bound on the required constant

This lower bound also concerns **actual** Paley stationary pairs, not the
cyclic counterfamily below. Fix `tau>=1024` and the single threshold

\[
 R_*=\frac{L_\tau}{\sqrt{1+\tau}}<1.
\]

Since `W<=1+tau`, (3) ensures every bulk entry is active at `R_*` for
every field under consideration. Equation (7) is therefore exact.
As the field grows, (2) gives `A0 -> 1`, and
`p=(1-(1-sigma)/n)/2 -> 1/2`. Off the mark,

\[
 \sum_{i\ne0}d_i e_i^2
 \ge\frac{L_\tau}{\sqrt W}(p-p^2),
 \quad \eta(R_*)\longrightarrow1-R_*.
\]

Thus for either sign, through primes or any growing eligible fields,

\[
 \boxed{\liminf_{q\to\infty}\frac{H(R_*)^2}{\eta(R_*)}
 \ge \frac{L_\tau}{4(\sqrt{1+\tau}-L_\tau)}=:c_\tau.}
 \tag{9}
\]

In particular `c_tau ~ sqrt(tau)/12` as `tau -> infinity`, whereas the
upper constant in (5) is asymptotic to `6 sqrt(tau)`. The infimum of
admissible eventual prime-uniform HR constants therefore has growth
`Theta(sqrt(tau))` in the hot regime. At `tau=1024`, (9) exceeds `2.5`.
A floor-independent proposal `C=1` would fail. Round 32 only proposed
that number at its tested **cold** floors, so this does not contradict
that note's correctly restricted diagnostic statement.

The field-uniform input (2) is unavailable at cold floors. Real
analyticity in the floor, or a finite numerical continuation from (2),
does not extend (5) to them. That is the unresolved part of this result.

## 2. The full weighted multiplier shortcut fails on the actual source

For this section fix **any** positive floor, take `n>tau`, and let the actual field grow.
Put `b=(1-c)/A0`, and continue to let `P` be the opposite projection.
Exact stationarity and the retained marked subtraction give

\[
 d=B/a-(b/a)e_0,\qquad
 S_d:=\sum_i d_i=n-b/a,
\]

\[
 \langle e,d\rangle
 =\frac{B_0}{a}\{1-(1-c)p\}-1=:m.
 \tag{10}
\]

For (10), `P(B-a1)=B-a1`, so `<e,B>=B0-a`.
Weighted Cauchy--Schwarz then gives

\[
 M:=\langle e,De\rangle\ge m^2/S_d.
\]

Test `P` on the input `e0` in the weighted norm. It follows that

\[
 \boxed{\|D^{1/2}P D^{-1/2}\|_{2\to2}^2
 \ge \frac{M}{d_0}\ge
 \frac{[B_0a^{-1}(1-(1-c)p)-1]^2}
 {(n-b/a)cB_0/a}.}                                       \tag{11}
\]

This is an exact finite inequality for the actual nonlinear weight.
The coherence/root cap `A0,B0 <= a(1+sqrt(q))` and `A0B0=1` bound both
roots above and below at a fixed floor. Since `p -> 1/2`, (11) implies

\[
 \frac{\|D^{1/2}P D^{-1/2}\|^2}{\sqrt n}
 \ge \frac{B_0}{4\tau\sqrt W}-O_\tau(n^{-1/2}),
\]

and in particular

\[
 \boxed{\liminf_{q\to\infty}
 \frac{\|D^{1/2}P D^{-1/2}\|^2}{\sqrt n}
 \ge\frac1{4\sqrt2\,\tau(1+\tau)}>0.}                     \tag{12}
\]

This is already a prime obstruction to a full `L2(D)` Fourier multiplier
bound, including in the hot range where HR is proved above.
**The test input in (11) is the marked coordinate. It is excluded from
`h_R`.** No failure of the hinge estimate, or of a bulk-restricted operator
bound, is inferred from (12).

There is a useful contrast that precisely identifies a misleading scalar
weight test. For **every individual complex Fourier-character projection**
`Q_k`, the rank-one formula gives

\[
 \|D^{1/2}Q_kD^{-1/2}\|^2
 =\left(\frac1n\sum d\right)\left(\frac1n\sum d^{-1}\right)
 =\frac{1-b/(na)}\rho\le\rho^{-1}.                         \tag{13}
\]

Thus neither that global product of means nor boundedness of every
individual frequency projection controls the sum over the Paley sector.
This is not a claim about the local interval `A2` characteristic. Weighted
interval/Riesz-projection results do not automatically apply to this
frequency set; the general weighted multiplier issue is also distinct in
[Nikolski--Verbitsky, arXiv:1404.4380](https://arxiv.org/abs/1404.4380).
No theorem from that paper is used in (10)--(13).

### What all cyclic translations do bound

Let `p_h=P_{h0}`. The exact cyclic ratio identity of round 32 yields

\[
 \begin{split}
 \|D^{1/2}P D^{-1/2}\|_{\rm HS}^2
 &=\sum_h p_h^2\sum_i\frac{A_{i+h}}{A_i}\\
 &=np+\frac{1-c}{c}
     \left[p-\frac1{A_0}\sum_h p_h^2 A_h\right]
 \le\frac{np}\rho.
 \end{split}                                               \tag{14}
\]

This uses the full cyclic cross correlation, not merely unshifted
orthogonality. It controls the **average** squared singular value. The
exceptional amplification in (12) is compatible with (14); replacing
an average bound by an operator bound would be a genuine error.
At `R=0`, the same Cauchy calculation also supplies the nontrivial actual
lower bound `liminf H(0)^2/eta(0) >= 1/[4(1+tau)]`.

## 3. A cyclic UI obstruction to a universal analytic-center theorem

This family differs from the rank-twelve noncirculant model of rounds
31--32. It is exactly cyclic and even, but deliberately does **not** have
Paley coherence or Paley sector dimensions.

Fix `tau>0` and let `n=2^k` with `k` even and growing, eventually `n>tau`.
Use `c,W,rho` above, and put

\[
 \kappa=(1-c)/W,\quad T_j=\rho+\kappa2^j,
 \quad T_0=1,\quad T_k=n/W.
\]

On `Z/nZ` let `E_j` be conditional averaging on congruence classes modulo
`2^j`, so `E0=J`, `Ek=I`. The mutually orthogonal martingale differences
`Delta_j=E_j-E_{j-1}` are **cyclic convolution** projections. Set

\[
 P_+=\sum_{j\text{ even}}\Delta_j,\qquad
 P_-=\sum_{j\text{ odd}}\Delta_j,\qquad K=P_+-P_-.
 \tag{15}
\]

Equivalently the multiplier on a character of order exactly `2^j` is
`(-1)^j`, with multiplier zero at the trivial character. It is real and
even, and `K^2=I-J`.

### 3.1 Exact reciprocal stationary pair

Let `U0=V0=1`. On the root congruence class, define its successive means:

\[
 \begin{array}{c|cc|cc}
 &U_j&V_j&u\text{ on the nonroot child}&v\text{ on that child}\\\hline
 j\text{ even}&T_j/V_{j-1}&V_{j-1}&\rho/V_{j-1}&V_{j-1}\\
 j\text{ odd}&U_{j-1}&T_j/U_{j-1}&U_{j-1}&\rho/U_{j-1}.
 \end{array}                                               \tag{16}
\]

The nonroot child at level `j` has size `n/2^j`; at the final root put
`u0=Uk`, `v0=Vk`. These are positive rational numbers when `tau` is
rational. Since `T_j+rho=2T_{j-1}`, each parent mean is exactly the
average of its two child means. At every level `U_j V_j=T_j`.
Consequently

\[
 \mathbb E u=\mathbb E v=1,\quad uv=\rho\ (i\ne0),
 \quad u_0v_0=n/W,
 \quad u-1\in\operatorname{im}P_+,\quad v-1\in\operatorname{im}P_-.
 \tag{17}
\]

Thus `A=au`, `B=av` have **exactly** the stipulated mass and product
`AB=w`. They are the nonlinear stationary pair for (15):
`K(A+B)=A-B`, `Phi(A-B)=A+B`. Finite-dimensional strict contraction on
a ball containing any two proposed fixed points proves uniqueness; the
ball about this point also proves zero-start Picard convergence. No
uniform contraction rate is asserted.

This family satisfies the full shifted cross correlation
`sum_i A_{i+h}B_i=W`, the shifted ratio and logarithmic identities of
round 32, and the corresponding weighted analytic-center stationarity.
These facts are not being inferred from numerical near-stationarity.

### 3.2 Uniform integrability and subcritical energies

Each root-mean update factor `T_j/T_{j-1}` lies in `[1,2]`. On the
nonroot child at level `j`, both `u,v` are at most `2^(j/2)`; at the
root both are at most `sqrt(n)`. (The value that does not grow on a
child is at most `rho<1`.) Therefore, for `R>=1`,

\[
 \frac1n\sum_{i\ne0}u_i\mathbf1_{u_i>R}
 \le\sum_{j:2^{j/2}>R}2^{-j/2}\le\frac{C}{R},
 \tag{18}
\]

and likewise for `v`. The marked first mass, when it exceeds `R`, is
at most `1/R` by the same root bound. Both sources are UI, uniformly
in the family. This also gives UI of the usual bulk source
`sqrt(W)(u+v)-2sqrt(tau)`.
Moreover

\[
 \|A-a\mathbf1\|^2,\ \|B-a\mathbf1\|^2\le W(k+1)
 =O_\tau(\log n).                                        \tag{19}
\]

The roots are bounded above by `sqrt(W)` and below by its reciprocal,
using `A0B0=1`. Thus the failure below is not caused by an unbounded root
or a failure of UI.

### 3.3 A proved linearly divergent hard-tail ratio

For even `k>=4`, take the actual threshold `R=U_{k-4}` and write
`L=U_{k-2}-U_{k-4}>0`. The stripped hinge `h_R/a` is exactly `L` on
`{n/4,3n/4}` and zero elsewhere. Thus `eta=2L/n`.
At the unmarked point `i=n/2`, which has `u_i=rho/V_{k-1}`, summing
the **signed** martingale differences gives

\[
 (P_-h_R)_{n/2}
 =-aL\frac{n+2}{3n},\qquad d_{n/2}=V_{k-1}.
 \tag{20}
\]

Indeed the odd levels through `k-3` contribute
`aL sum_{j odd<=k-3}2^j/n`, and level `k-1` contributes `-aL/2`.
Keeping this single positive energy term proves

\[
 \begin{split}
 \frac{H(R)^2}{\eta(R)}
 &\ge W L V_{k-1}\frac{(n+2)^2}{18n^2}\\
 &=W T_{k-1}\left(1-\frac{T_{k-3}}{T_{k-2}}\right)
                 \frac{(n+2)^2}{18n^2}
 =\left(\frac1{72}+o(1)\right)n.
 \end{split}                                               \tag{21}
\]

Here `W kappa=1-c -> 1`. This is an exact algebraic counterexample to
universal cyclic HR, even with both-source UI and logarithmic energies.
It is **not** a Paley counterexample:

\[
 \dim V_+=2(n-1)/3,\quad \dim V_-=(n-1)/3,\quad
 K_{ii}=(n-1)/(3n)\longrightarrow1/3.                       \tag{22}
\]

In particular its coherence constant grows at least as `sqrt(n)/3`.
It does not decide whether cyclicity **plus** the sharp Paley coherence,
let alone the actual signed Paley multiplier, suffices.
No inference of failure of inverse-source tightness is made merely from
the failure of the sufficient HR estimate.

The exact rational replay checks (16)--(21), including all spatial shifts
at `n=16,64`, and handles larger sizes in the `k+1` shell representation.
For `tau=.05`, the evaluated ratios divided by `n` approach `.0218254`;
the proved single-coordinate lower coefficient approaches `1/72`.
Those decimal displays accompany exact rational checks and are not used
in the asymptotic proof.

## 4. Rigorous finite actual-Paley HR certificates

The finite certificates address a real gap in a floating stationary scan:
a small residual alone is not a distance enclosure, and a grid does not
cover all thresholds. The following method handles both issues.

### 4.1 Enclosing the exact stationary pair

Choose an exactly even rational vector `vhat` from the numerical solver.
At 128-bit precision, Arb's outward-rounded DFT evaluates a rigorous
bound `epsilon` on `||K Phi(vhat)-vhat||_2`. For the rational radius
`r=10^-9`, bound throughout its Euclidean ball

\[
 L=\max_i\frac{|\widehat v_i|+r}
 {\sqrt{(|\widehat v_i|+r)^2+4w_i}}<1.
\]

The replay verifies with interval comparisons
`epsilon < (1-L) r`. Since `||K||<=1`, the map sends this closed ball
into itself and is a strict contraction there. Banach's theorem gives
an exact fixed point at distance at most `r`. Global uniqueness follows
from the same strict scalar Lipschitz argument on a bounded set containing
any two fixed points. Thus the enclosure concerns the intended stationary
point, not an unspecified approximate branch.

The positive-root map `v_i -> (sqrt(v_i^2+4w_i)+sigma v_i)/2` has derivative
of absolute value at most one. Allowing for the tiny rounding of its rational centers
`Ahat_i`, the replay gets a certified coordinate error `r_A` and positive
bounds

\[
 A_i\in[\widehat A_i-r_A,\widehat A_i+r_A],\qquad
 d_i\le d_i^{\rm up}=\frac{c}{a(\widehat A_i-r_A)}.
 \tag{23}
\]

The exact integer Paley signs and their evenness are checked. Because all
input vectors are exactly even, two forward DFTs implement the inverse
transform correctly. All acceptance comparisons use Arb bounds; floats
choose trial centers and display diagnostics only.

### 4.2 Certifying every threshold, including an unknown terminal knot

The true threshold knots in physical units are `0` and all bulk `A_j`.
For a knot `A_j`, compute the rational nominal hinge
`hhat_i=(Ahat_i-Ahat_j)+`, with its mark stripped. The true hinge differs
by at most `2r_A` in every bulk coordinate. At zero the bound is `r_A`.
With this error denoted by `e_A`, and `dmax=max d_i^up`,

\[
 H\le\left(\sum_i d_i^{\rm up}(P\widehat h)_i^2\right)^{1/2}
             +e_A\sqrt{n d_{\max}},\quad
 na\eta\ge\sum_i\widehat h_i-ne_A.                        \tag{24}
\]

If the lower mass is positive, (24) certifies the ratio directly. If it
is nonpositive, use the nonnegative-hinge bound

\[
 H^2\le d_{\max}\|h\|_1^2,
 \quad \frac{H^2}{\eta}\le na\,d_{\max}
                     (\|\widehat h\|_1+ne_A).              \tag{25}
\]

It includes the possible zero hinge without dividing by a vanishing
lower bound. No unproved ordering of almost equal knots is needed.
Inversion symmetry reduces the list to `j=1,...,n/2`.

Between successive **true** knots, `Ph` is affine in the threshold and
`eta` is positive affine. The quadratic-over-linear ratio is convex;
the final interval tends to zero. Certified bounds at every true knot
therefore give the claim for **all real R>=0**. The script verifies
`H^2/eta<1` at every knot by (24) or (25).

Outward-rounded summary upper bounds, taking the worse sign:

| prime | floor `.05` | floor `.01` | floor `.001` |
|---:|---:|---:|---:|
| 101 | .241459 | .236177 | .236856 |
| 401 | .277523 | .276522 | .276346 |
| 1009 | .283047 | .280869 | .279968 |

These are rigorous finite bounds under the documented Arb arithmetic and
mathematical enclosure argument, **not Lean/kernel formal verification**.
They cover 18 exact stationary sides, with 26, 101, and 253 knots per
side respectively: 2280 knot tests in total. There is no interval claim
about all primes or about a million-order numerical solution.

The optional hot witness mode reverses (24) using lower diagonal bounds
and an upper tail mass. At `p=9413,tau=1024,R=.9`, it proves

\[
 H_+^2/\eta_+>1.23553534,\qquad H_-^2/\eta_->1.23599050.
 \tag{26}
\]

This certifies failure of `C=1` at that floor, not failure of HR with its
allowed `tau`-dependent constant. It is consistent with (5) and (9).

## 5. Signed-triangle attempts and the remaining cold obstruction

The actual triangle identity is retained without a sign shortcut. With
`E={k:s(k)=-sigma}`, `beta=DFT(B/a)/n`, and
`r=(DFT(h_R)/n) 1_E`,

\[
 H^2=n\sum_E|r_k|^2+
 n\sum_{k,l\in E,\ k-l\in E}\overline r_k\beta_{k-l}r_l
 -\frac ba\left|\sum_Er_k\right|^2.                        \tag{27}
\]

The final term is the exact marked subtraction. Both `beta` and `r` can
be negative. Direct small-field replays compare (27) with the physical
weighted norm; no positive-kernel replacement is made.

Three attempted estimates were examined:

1. **Translate/ratio or global weight control.** The strongest direct
   Hilbert--Schmidt consequence obtained was (14), while (12) proves that
   the hoped-for full operator conclusion is false even on the actual
   source. This is a concrete obstruction, not just missing technique.
2. **Positive semidefinite Fourier matrices and analytic-center constraints.**
   If `U` is the circulant matrix with eigenvalues `u` and `F` that with
   eigenvalues the nonnegative bulk hinge `(u-R)+`, then `0<=F<=U`.
   Let `Y` have eigenvalues `B/a`. Complementary frequency supports give
   `U_ij Y_ji=0` off the diagonal. The principal-block trace bound is
   `tr(Y_EE F_EE)<=tr(Y_EE U_EE)=|E|`. Together with the positive block
   bound `F_E0 F_0E <= F_00 F_EE`, it only gives an `O(n eta)` response
   bound after normalization. Replacing this trace by an order-one bound
   is not justified. The exact cyclic family (15)--(21) shows that the
   cyclic reciprocal analytic-center structure alone cannot repair it.
3. **Coherence and squared-kernel mixing.** These control squared entries
   and unweighted averages but discard the signed, actual-source triangle
   in (27). The accepted rank-twelve family already excludes that route
   even with UI and the strong Schur gap. The cyclic family here lacks
   coherence, so combining the two counterexamples would be invalid.

None supplies a cold actual Paley estimate. The hot proof succeeds because
(2) directly bounds every bulk spectrum and hence the output weight, not
because it proves a universal weighted multiplier theorem.
The finite cold certificates establish that the conjectured inequality
really holds at their exact sources; they do not justify extrapolation.
The remaining target is still a field-uniform estimate for (27) on the
actual cold hinges, or a genuinely weaker estimate sufficient for their
soft superposition. No HR/UI circular implication is invoked.

## 6. Reproduction and file scope

Run from the repository root, with bytecode writes disabled:

```sh
.venv/bin/python -B research/astra-hardtail-33-exact.py \
  > research/astra-hardtail-33-exact.jsonl
OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/astra-hardtail-33-actual.py \
  > research/astra-hardtail-33-actual.jsonl
OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/astra-hardtail-33-certified.py \
  > research/astra-hardtail-33-certified.jsonl
OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/astra-hardtail-33-certified.py --tau .01 \
  > research/astra-hardtail-33-certified-floor01.jsonl
OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/astra-hardtail-33-certified.py --tau .001 \
  > research/astra-hardtail-33-certified-floor001.jsonl
OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/astra-hardtail-33-certified.py \
  --primes 9413 --tau 1024 --witness-R 0.9 \
  > research/astra-hardtail-33-hot-certified.jsonl
```

The complete replay audit is:

```sh
OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/astra-hardtail-33-audit.py \
  > research/astra-hardtail-33-acceptance.jsonl
```

It reruns all six computations in subprocesses, compares their parsed JSON
with the stored records exactly, and checks every final success row. The
[acceptance output](astra-hardtail-33-acceptance.jsonl) passed for all
**84 primary records**. It is an implementation replay audit; the hot
asymptotic theorems and the cyclic asymptotic bound have the ordinary
mathematical proofs given above.

The six primary outputs have respectively 9, 41, 10, 10, 10, and 4
records. The first uses exact rational arithmetic, the second is explicitly
floating, and the final four use rigorously rounded stationary enclosures.
Their final `all_checks_passed` rows are included in these counts.
The earlier exploratory random-mask script and its five rows are retained
as `astra-hardtail-33-explore.py/.jsonl`; they are not proof evidence and
are not needed for any result above.

Only `research/astra-hardtail-33*` files were written. No README/ledger,
other research prefixes, commits, pushes, or external messages were changed.
