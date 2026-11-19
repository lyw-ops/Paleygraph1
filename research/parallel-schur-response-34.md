# Actual Schur response: joint clipping, an exact Paley trace, and cold finite certificates

Round 34, 2026-11-18. ETH Problem 26, **ordinary theta**.

**The cold prime-uniform hard-tail estimate remains unproved.** This note
does not use UI as an input to HR, and does not claim the subsequent
marked arithmetic comparison or the theta asymptotic. Its new uniform
finite identities combine the actual reciprocal circulants, the actual
Paley difference counts, and the actual bulk hinge. They identify a
specific linear loss in a proposed positive-trace argument, even on an
actual prime source. A separate rigorous continuous-cover method extends
finite cold all-threshold HR certificates to prime 153649.

The substantive results are:

* The CP clipping inequality holds jointly as a **Gram domination for
  every finite collection of thresholds and all signed mixtures**. This
  includes soft superpositions without using Minkowski. It retains the
  single-coefficient weights beta; it does not turn them into triangle
  edge weights.
* The relevant principal-block trace has an exact formula involving one
  cubic Legendre correlation. The CP Gram bound controls that correlation
  by a Hasse/Cauchy bound. At the actual zero hinge, including the exact
  mark correction, the trace divided by n tends to
  `(1+2 tau)/(4(1+tau))`. Meanwhile the actual HR ratio is bounded at that
  hinge. Thus replacing the source vector by this trace incurs an
  **Omega_tau(n) loss on the actual pair**, not just on a non-Paley model.
* At `tau=.01`, both exact stationary sides satisfy `H(R)^2 <= eta(R)`
  for every real `R>=0` at primes 4001, 10009, 40009, and 153649. At
  prime 40009 the stronger `H(R)^2 <= .456 eta(R)` is certified.
  Both inequalities are strict when `eta(R)>0`; at a zero hinge both
  sides vanish. These are Arb finite certificates, not a uniform
  assertion through primes.

The requested inputs were read:
[audit 33, Sections 1--4](parallel-audit-33.md),
[circulant source 32](parallel-circulant-source-32.md), and
[hard-tail 33](astra-hardtail-33.md). No two old non-Paley counterfamilies
are combined, and no new non-Paley counterexample is needed here.

## 1. Normalization, including the mark

Let `q=2n+1=1 mod 4`, `0<c=tau/n<1`,

\[
 W=1+(n-1)c,\quad a=\sqrt{W/n},\quad \rho=\tau/W,
 \quad u=A/a,\quad v=B/a.
\]

These are the actual positive stationary spectra. Their means are one,
their bulk product is rho, and `u0 v0=n/W`. The position circulants
`C_A,C_B` have eigenvalues `u,v`, diagonal one and opposite off-diagonal
supports. In particular

\[
 C_A\circ C_B=I,\qquad
 C_AC_B=\rho I+\frac{1-c}{W}\mathbf1\mathbf1^T.
 \tag{1}
\]

Put `epsilon=-sigma`, `s(k)=chi(1-g^(2k))`,
`E={k:s(k)=epsilon}`, and `P=P_-sigma`. The normalized Fourier
coefficients are

\[
 \beta_k=\operatorname{DFT}(v)_k/n,\qquad
 q_R=(u-R)_+\mathbf1_{i\ne0},\quad
 \kappa_R=\operatorname{DFT}(q_R)/n.
\]

Write `eta_R=E_n q_R`, `nu_R=E_n(q_R^2/u)` and
`zeta_R=E_n(q_R/u)`. Let `C_R` have eigenvalues `q_R`.
With

\[
 d=\rho/u=v-(1-c)v_0e_0,\qquad
 t=\frac{(1-c)v_0}{n}=\frac{b}{an},\qquad
 M=C_B[E,E]-t\mathbf1\mathbf1^T,
 \tag{2}
\]

the **corrected** matrix M is positive definite: the full circulant
`C_B-t 11^T` has the positive eigenvalues d, including `d0=c v0`.
For `h_R=a q_R`, the response is exactly

\[
 H(R)^2=W\,\kappa_R[E]^*M\kappa_R[E].
 \tag{3}
\]

Thus every quadratic form below retains the marked subtraction. In the
original triangle notation, (3) is
`n r* C_B[E,E] r -(b/a)|sum r|^2`, with `r=a kappa_R[E]`.

## 2. Joint CP Gram domination, rather than separate threshold bounds

For thresholds `R_1,...,R_m`, define the real symmetric matrices

\[
 G_{ij}=\mathbb E_n(q_{R_i}q_{R_j}/u)-\eta_{R_i}\eta_{R_j},
 \quad
 B_{ij}=\sum_{k\in E}|\beta_k|^2
                  \overline{\kappa_{R_i}(k)}\kappa_{R_j}(k).
\]

**Lemma 1.** For every actual pair and every finite collection of
thresholds,

\[
 \boxed{0\preceq B\preceq G.}                              \tag{4}
\]

**Proof.** The Schur map `Phi(X)=C_B circ X` is CP and
`Phi(C_A)=I`. For arbitrary complex coefficients `z_i`, put
`F=sum_i z_i C_Ri`, a circulant with eigenvalues `f=sum_i z_i q_Ri`.
The positive block matrix

\[
 \begin{pmatrix}C_A&F\\F^*&F^*C_A^{-1}F\end{pmatrix}
\]

stays positive under the amplified Schur map. Its Schur complement gives
`Phi(F)^* Phi(F) <= Phi(F^* C_A^-1 F)`. A diagonal entry says

\[
 \sum_k|\beta_k\widehat f(k)|^2\le\mathbb E_n(|f|^2/u).
\]

The k=0 term is `|E_n f|^2`, beta vanishes off `{0} union E`,
and subtraction gives `z* B z <= z* G z`. Positivity of B is immediate.
This proves (4). The argument in fact works for any f, with the same
normalized Fourier convention. It is not dependent on a numerical
stationary approximation. \(\square\)

The diagonal recovers
`sum_E beta_k^2 kappa_R(k)^2 <= nu_R-eta_R^2`.
Equation (4) is stronger than its separate diagonal statements: it
controls all cross-threshold correlations and signed combinations.
At a fixed finite field it also passes to integrals of the hinge curve,
so a soft superposition need not pay a separate Minkowski bound at each
threshold **for this weighted coefficient norm**.

The distinction in audit 33 remains: (4) contains `beta_k^2`, whereas
(3) contains `beta_(k-l)`. Removing these weights, or applying the
unweighted support Schur mask as a positive map, would be invalid.

## 3. Exact Paley triangle incidence and the corrected trace

For `d!=0`, set `alpha=g^(2d)` and

\[
 L_d=\sum_{x\in\mathbb F_q}\chi(x(x-1)(x-\alpha)),\qquad
 N_E(d)=|E\cap(E+d)|.
\]

**Lemma 2 (actual incidence).** One has

\[
 |E|=\frac{q-3-2\epsilon}{4},\qquad
 \boxed{8N_E(d)=q-7-4\epsilon-4\epsilon s(d)+L_d.}          \tag{5}
\]

In particular, for d in E,

\[
 N_E(d)=m_\epsilon+L_d/8,\qquad
 m_\epsilon=\frac{q-11-4\epsilon}{8},\qquad
 |L_d|\le2\sqrt q.                                       \tag{6}
\]

To check all exceptional terms in (5), expand
`(1+chi x)(1+epsilon chi(1-x))(1+epsilon chi(alpha-x))`.
Its sum is `q-1-2 epsilon+L_d`. The spurious contributions at
`x=0,1,alpha` sum to
`(1+epsilon)^2+4(1+epsilon s(d))`. Subtracting them and dividing
by eight gives (5). The cubic is squarefree because `alpha!=0,1`;
the last inequality in (6) is the Hasse bound already used in
[Schur mixing 32](schur-mixing-32.md). Equivalently, (5) follows by
expanding the exact cyclic convolution of the two E indicators. No
prime-only cancellation is asserted in this count.

Define the two traces

\[
 \widetilde Q_R=\operatorname{tr}(C_B[E,E]C_R[E,E]),\quad
 S_R=\mathbf1^TC_R[E,E]\mathbf1,\quad
 Q_R=\operatorname{tr}(M C_R[E,E])=\widetilde Q_R-tS_R.
\]

**Lemma 3 (signed weighted trace identity).** Exactly,

\[
 \boxed{\widetilde Q_R=
 \frac{q+5}{8}\eta_R+m_\epsilon\rho\zeta_R
       +\frac18\sum_{d\in E}L_d\beta_d\kappa_R(d).}        \tag{7}
\]

Moreover

\[
 \left|\sum_{d\in E}L_d\beta_d\kappa_R(d)\right|
 \le2\sqrt{q|E|}\sqrt{\nu_R-\eta_R^2},                    \tag{8}
\]

\[
 0\le S_R\le\frac{(1+\sqrt q)^2}{4}\eta_R,
 \qquad Q_R\ge0.                                        \tag{9}
\]

**Proof.** Circulancy and the actual difference counts give

\[
 \widetilde Q_R=|E|\eta_R+
                  \sum_{d\in E}N_E(d)\beta_d\kappa_R(d).
\]

By Parseval, evenness, and the bulk deletion,
`sum_E beta_d kappa_R(d)=E_n(v q_R)-eta_R=rho zeta_R-eta_R`.
Now (6) and `|E|-m_epsilon=(q+5)/8` give (7).
Hasse, Cauchy--Schwarz, and Lemma 1 give (8), with all signs in (7)
still present.

For (9), Fourier diagonalization gives

\[
 S_R=\frac1n\sum_i q_R(i)
                       |\operatorname{DFT}(\mathbf1_E)_i|^2.
\]

The mark term vanishes because `q_R(0)=0`. At every other frequency,
`DFT(1_E)=(-1+epsilon DFT(s))/2`, and the actual Paley coherence
bound gives `|DFT(s)|<=sqrt(q)`. This proves the upper bound.
Finally M and `C_R[E,E]` are positive semidefinite. \(\square\)

This is a legitimate joint use of CP, actual Paley arithmetic, and the
specific deleted hinge. It does not yet bound the source-vector triangle
in (3). The following calculation pinpoints what is lost by taking a trace.

## 4. The actual zero hinge proves a linear loss in the trace route

The positive principal block of `C_R` at `{0} union E` gives
`kappa_R[E] kappa_R[E]^* <= eta_R C_R[E,E]`. Thus a valid estimate is

\[
 \boxed{H(R)^2\le W\eta_R Q_R.}                            \tag{10}
\]

The exact marked M is used, not the uncorrected `C_B[E,E]`.

**Proposition 4.** At each fixed positive floor, through any growing
eligible fields, including primes, the actual zero hinge obeys

\[
 \boxed{\frac{Q_0}{n}\longrightarrow
                  \frac{1+2\tau}{4(1+\tau)}>0,\qquad
         \frac{H(0)^2}{\eta_0}=O_\tau(1).}                 \tag{11}
\]

Consequently the upper bound `W Q_0` on the HR ratio supplied by
(10) has order n on an actual hinge whose true ratio is bounded.

**Proof.** The actual root caps give `A0,B0=Theta_tau(1)`, with
`A0 B0=1`. For completeness these follow from
`A0,B0 <= a(1+sqrt(q))` and their product. Hence
`u0,v0=Theta_tau(sqrt(n))`. At R=0,

\[
 q_0=u-u_0e_0,\quad
 \eta_0=\nu_0=1-u_0/n,\quad
 \zeta_0=(n-1)/n,\quad
 \kappa_0(d)=-u_0/n\quad(d\in E).                         \tag{12}
\]

In particular `nu_0-eta_0^2=O_tau(n^(-1/2))`. Equations (7)--(8)
show

\[
 \widetilde Q_0
   =\frac n4(1+\rho)+O_\tau(n^{3/4}).
\]

Equation (9) gives `t S_0=O_tau(sqrt(n))`. This is a bound on the
**trace correction only**, not permission to discard the mark in the
source-vector energy. Since `rho -> tau/(1+tau)`, the first limit in
(11) follows for the corrected trace itself.

For the actual response, `P h_0=-A0 P e0`. Set `e=P e0`.
The diagonal satisfies `|e0|<=1/2`; off the diagonal,
`|e_i|<=(1+sqrt(q))/(2n)`. Also `sum d<n` and `d0=c v0`.
It follows that

\[
 H(0)^2\le A_0^2\left[\frac{cv_0}{4}
                         +\frac{(1+\sqrt q)^2}{4n}\right]
             =O_\tau(1).
\]

Together with `eta_0 -> 1` this proves the second assertion. \(\square\)

Proposition 4 strengthens the earlier observation that this trace method
only gives an order-n estimate: it proves that the loss actually occurs
in its scalar upper bound on the exact Paley source, after correction.
It does **not** exclude a proof that uses the joint CP constraint and
additional source-vector signed correlations without taking (10).
It also gives no obstruction to actual HR, which may hold uniformly.

## 5. Actual coefficient and signed-split diagnostics

The [diagnostic checker](parallel-schur-response-34.py) checks (4)--(10)
on actual numerical stationary pairs. Three separate exact-integer rows
check every nonzero d in (5), including direct cubic Legendre sums, at
primes 13, 101, and 401: **506 incidence identities** in total.
The other rows are expressly floating, with primes 401, 1009, 9413,
153649, 1000033 and square orders 361, 151321, both sides.

At `p=1000033,tau=.01`, side +:

| threshold R | actual H²/eta | actual weighted coefficient square / CP upper bound | Q_R/n |
|---:|---:|---:|---:|
| 0 | .305098 | .0038730 | .251616 |
| 1 | .196935 | .00003385 | .138987 |
| 2 | .180278 | .00001642 | .064030 |
| 4 | .219396 | .00002471 | .005432 |

The R=0 trace limit from (11) is `.2524752475...`. At R=2, the CP
upper bound is `.04581109...`, while its actual left side is only
`7.52066e-7`. This is substantial finite slack in the currently available
weighted estimate; it is not evidence of a prime-uniform improvement.

The signed triangle cancellation is large at the same R=2:

\[
 H^2=.0873925942+16.0930431158-16.1342842070
       =.0461515031\quad\text{(floating)}.                 \tag{13}
\]

Thus the mark is far larger than the final response and is essential.

To test beta-small suppression, split the actual coefficient vector into
`L={k in E:sqrt(n)|beta_k|<=t0}` and its complement. For each part
compute the physical inverse Fourier vector and use **d=rho/u** for
all three quadratic pieces. This retains the exact mark in low-low,
high-high, and signed mixed terms. At the same prime and hinge,
`t0=.3` gives

\[
 \frac{|L|}{|E|}=.0566542,\qquad
 \frac{\sum_L|\kappa_2|^2}{\sum_E|\kappa_2|^2}=.0805066,
\]

\[
 H^2=.00707795+.05020386-.01113031=.04615150.
\]

The source coefficient mass is enriched, rather than depleted, relative
to vertex density in this finite example. With `t0=1`, about 21.23% of
vertices carry 28.27% of coefficient square mass, and the signed mixed
energy is `-.03337226`. These floating checks do not rule out a more
subtle weighted distribution estimate; they do not justify a suppression
or independence assumption, nor discarding the mixed term.

The maximum recorded trace identity error is `3.871e-9`, and the maximum
triangle identity error is `2.762e-13`. Every joint five-threshold Gram
check passed. These normalizations are not interval stationary enclosures.

## 6. Rigorous finite all-threshold coverage with few anchor transforms

The [Arb checker](parallel-schur-response-34-certified.py) uses the same
Banach existence/uniqueness argument as hard-tail 33, with a sharper
L2 treatment of hinge errors and a continuous interval cover. It need
not enumerate all unknown exact knots.

### 6.1 Exact stationary enclosure and L2 hinge error

An exactly even rational center vhat is selected by the floating solver.
Arb bounds its fixed-point residual by epsilon and bounds the derivative
on the closed L2 ball of radius r by L. Acceptance requires
`epsilon < (1-L) r` and `L<1`. The map has an exact fixed point in that
ball. The strict scalar contraction on a bounded set containing any two
fixed points proves global uniqueness. The exact integer Paley multipliers
and their evenness are checked; two forward DFTs give the inverse for
these even vectors.

The root map to A has scalar derivative of absolute value at most one.
After allowing for the rational-center rounding in L2, the checker has

\[
 \|A-\widehat A\|_2\le r_A,\qquad
 d_i\le d_i^+=\frac{c}{a(\widehat A_i-r_A)},\quad
 d_{\max}=\max_i d_i^+.                                  \tag{14}
\]

For a fixed rational **physical** threshold L, let
`hhat=(Ahat-L)+` with the input mark deleted. Scalar clipping is
1-Lipschitz, so the hinge error in L2 is at most r_A, rather than
`sqrt(n) r_A`. Thus rigorous anchors are

\[
 H(L)\le H_L^+:=
       \left(\sum_i d_i^+(P\widehat h)_i^2\right)^{1/2}
                     +\sqrt{d_{\max}}r_A,
\]

\[
 \sum_i h_L(i)\ge m_L^-:=\sum_i\widehat h_i-\sqrt{n-1}r_A.
 \tag{15}
\]

All output coordinates, including the mark, enter the anchor norm.

### 6.2 Covering intervals and the entire terminal tail

Let N_L bound the number of bulk entries with `A_i>L`, using (14).
For every physical threshold in `[L,L+Delta]`, hinge monotonicity gives

\[
 H(t)\le H_L^++\sqrt{d_{\max}N_L}\,\Delta,\qquad
 \sum h_t\ge m_L^- -N_L\Delta.
\]

Consequently the single strict Arb comparison

\[
 na\left(H_L^++\sqrt{d_{\max}N_L}\,\Delta\right)^2
       <C(m_L^- -N_L\Delta)                              \tag{16}
\]

certifies **every** threshold in that interval. A float proposes the
step; the stored program accepts it only after (16) is verified with
outward bounds. Each anchor is asserted to be an exact dyadic rational.

For the remaining tail, if `A_bulk<=M`, projection contraction and
`h_t^2<=(M-L)_+ h_t` show, for **all** `t>=L`,

\[
 \boxed{H(t)^2/\eta(t)\le na\,d_{\max}(M-L)_+.}            \tag{17}
\]

The zero hinge is interpreted as zero energy. This terminal test covers
unknown top knots without dividing by a vanishing mass. Consecutive
closed intervals from zero and (17) cover all real nonnegative
thresholds, not just a finite grid. No UI or uniform weighted multiplier
bound is used.

### 6.3 Finite results and scope

At `tau=.01`, 128-bit Arb, L2 radius `1e-8`:

| prime | target C | cover intervals (+, -) | certified upper bound on H²/eta, worse side |
|---:|---:|---:|---:|
| 4001 | 1 | 54, 45 | < .815 |
| 10009 | 1 | 48, 47 | < .827 |
| 40009 | 1 | 67, 69 | < .818 |
| 153649 | 1 | 71, 71 | < .954 |
| 40009 | .5 | 137, 145 | < .456 |

The upper bound includes the terminal test, not just the anchor values.
The last line repeats a source with a stronger target; there are **four
distinct primes and eight exact stationary sides**, not ten distinct
sides. The C=1 certificates use 472 intervals in total, and the stronger
40009 certificate uses another 282. They are rigorous finite arithmetic
certificates under the documented Arb/Banach argument, not Lean/kernel
formal verification. They do not bound the gaps between these primes,
the prime limit, or any other floor.

The exact fixed-point residual upper bounds are below `9.711e-15`;
Banach margins are positive. A small floating residual alone would not
establish any of these source enclosures.

## 7. What remains and reproduction

The joint Gram estimate controls beta-weighted single coefficients.
The exact Paley trace controls one low-order signed correlation, but
Proposition 4 prevents the positive-trace replacement from proving HR.
The beta-small diagnostics give no suppression theorem, and the finite
continuous covers have field-dependent anchors and bounds. None of these
facts yields the needed cold prime-uniform estimate for (3), or a weaker
uniform soft-integral estimate. UI is not assumed to bridge this gap.
No all-vector weighted multiplier hypothesis is introduced.

The following are the canonical computations, from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-schur-response-34.py --large \
  > research/parallel-schur-response-34.jsonl
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-schur-response-34-certified.py --primes 4001 --tau .01 \
  > research/parallel-schur-response-34-certified-trial.jsonl
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-schur-response-34-certified.py --primes 10009 40009 --tau .01 \
  > research/parallel-schur-response-34-certified.jsonl
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-schur-response-34-certified.py --primes 153649 --tau .01 \
  > research/parallel-schur-response-34-certified-large.jsonl
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-schur-response-34-certified.py --primes 40009 --tau .01 --C .5 \
  > research/parallel-schur-response-34-certified-half.jsonl
```

The primary outputs have respectively 130, 5, 9, 5, 5 records: **154**
in total. Runtime fields are informational and are excluded from
deterministic comparisons. The `all_threshold_ratio_upper` metadata is
the outward maximum of the previously certified cover and terminal
bounds; the same schema is used in all four certificate outputs.

The [saved-record audit](parallel-schur-response-34-audit.py) checks
counts, scopes, all final success markers, the Banach inequalities and
the continuous-cover summary inequalities, and reruns all 506 exact
incidence checks. Its [acceptance output](parallel-schur-response-34-acceptance.json)
is a consistency audit and exact-incidence replay, not an independent
recomputation of every large Arb transform.

Only `research/parallel-schur-response-34*` files were written. No other
prefix, README, ledger, commit, push, or external message was changed.
