# Reciprocal source tails: a Schur identity, a stripped certificate, and an exact obstruction

Round 29, 2026-11-18. ETH Problem 26, ordinary theta.

**Result and limitation.** The complete stationary reciprocal pair yields a
Schur-complement identity between the two sector compressions. It also yields
a finite upper certificate for the **first inverse source-moment tail**, with
the anomalous mark stripped explicitly. The certificate uses an ordinary
weighted norm of a specified opposite-sector projection of the actual
truncated spectrum. It has no second-inverse-moment factor, and therefore
does not require a bound on the stationary Euclidean energy. Source uniform
integrability controls its spatial and constant terms; an additional
opposite-sector leakage estimate remains necessary and is not proved for
Paley primes.

There is a strict algebraic obstruction to dropping that extra estimate.
Below is an **exact positive-floor stationary family for other reflections**
with both reciprocal diagonals, the true mark product, the Paley sector
dimensions and marked projector values, bounded marked spectra, and uniformly
integrable sources. Both centered energies are asymptotic to `t/2`, while
`n=2t^8`. Nevertheless almost all the first inverse source-moment mass
approaches eigenvalue zero. These are unique stationary points and limits of
zero-start Picard iteration for their constructed reflections, rather than
approximate profiles. They are **not Paley kernels**: in particular their
marked-row coherence constant grows. This is an obstruction to deductions
from the reciprocal identities alone, not a counterexample at prime order.

For orientation, at `t=1000, tau=.05`, the exact-model formulas give energy
about `501.998`, a small eigenvalue about `.00199102`, and first inverse
energy mass about `.999488` on that eigenvalue. The source tail first mass
is only `.001`. The proof is algebraic below; these decimals are diagnostics.

## 1. Actual pair and conventions

Use counting norms. Let `n=(q-1)/2`, `0<tau<n`,

\[
 c=\tau/n,\quad w=c\mathbf1+(1-c)e_0,\quad
 W=1+(n-1)c,\quad a=\sqrt{W/n},\quad \rho=\tau/W=c/a^2.
 \tag{1}
\]

Write `P=I-J`, `P_sigma=(P+sigma K)/2`, `V_sigma=im P_sigma`.
For the **actual** stationary pair, fix a sign and abbreviate

\[
 A=A_\sigma>0,\quad B=A_{-\sigma}>0,\quad AB=w,
 \quad A=a\mathbf1+x,\quad B=a\mathbf1+y,
 \quad x\in V_\sigma,\ y\in V_{-\sigma}.
 \tag{2}
\]

Both means are `a`, `A_0B_0=1`, and `x` and `y` are orthogonal. Set

\[
 d=\frac{c}{aA},\quad D=\operatorname{diag}(d),\quad
 T=P_\sigma D P_\sigma|_{V_\sigma},\quad
 e=P_\sigma e_0,\quad b=\frac{1-c}{A_0}.
 \tag{3}
\]

The identities from [round 28](parallel-reciprocal-28.md) are

\[
 Tx=be,\qquad Q:=\langle x,Tx\rangle
       =(1-c)(1-a/A_0)<1,\qquad
 d=B/a-(b/a)e_0.
 \tag{4}
\]

The opposite diagonal is `d_-=c/(aB)`. Its product with `d` is `rho`
off the mark and **`rho c` at the mark**. Neither product is replaced by
a freely chosen diagonal in any Paley claim in this note.

Let `mu` be the spectral measure of `T` at `e`, and define the positive
inverse-energy source measure

\[
 d\nu(\lambda)=b^2\lambda^{-1}d\mu(\lambda).
 \qquad \nu((0,\infty))=Q,\quad
 \int\lambda^{-1}d\nu=\|x\|^2=:E.
 \tag{5}
\]

The target considered here is tightness at zero of `nu`, which is weaker
at the level of spectral measures than a uniform bound on `E`. A bounded
`E` gives `nu((0,epsilon])<=epsilon E`; the converse need not hold. No
strict separation between complete sufficient hypotheses for the actual
Paley family is asserted merely from this observation.

## 2. A coupled reciprocal Schur identity

Put `U=diag(A/a)`, let

\[
 S=P_{-\sigma}U P_{-\sigma}|_{V_{-\sigma}},\qquad
 C=P_{-\sigma}U P_\sigma,
 \quad R=J+P_{-\sigma}=I-P_\sigma.
\]

Then the following is an exact operator identity on `V_sigma`:

\[
 \boxed{\quad
 \rho T^{-1}
 =P_\sigma U P_\sigma-C^*S^{-1}C
                 -\frac{x\otimes x}{na^2}.
 \quad}                                                     \tag{6}
\]

In terms of the actual opposite positive source compression,

\[
 S=T_{-\sigma}+\frac{b_-}{a}e_-\otimes e_-,
 \qquad b_-=(1-c)/B_0,\quad e_-=P_{-\sigma}e_0.
 \tag{7}
\]

Thus replacing `S` by `T_-` would incorrectly delete the mark correction.

**Proof.** Exactly `D^{-1}=U/rho`. In the decomposition
`R^n=V_sigma + R 1 + V_-sigma`, multiplication by `U` has constant
block one, constant-to-`V_-sigma` block zero, and constant-to-`V_sigma`
block `x/(a sqrt(n))`. The zero block uses `A in R 1+V_sigma`.
Eliminating the last two blocks therefore gives the right side of (6).
The inverse-compression/Schur formula gives it as
`(P_sigma U^{-1}P_sigma)^{-1}=rho T^{-1}`. Equation (7) follows from
`d_-=A/a-(b_-/a)e_0`. All diagonal operators and compressions are positive
definite, so the inverses exist. This proves (6)--(7). No prime arithmetic
has entered. ∎

Equation (6) records precisely where the two full spectra interact. A
global lower bound on `T` is not inferred from it: the subtraction can
be large and source-dependent.

## 3. Exact resolvent decrement and a finite upper certificate

For `delta>0`, define

\[
 \begin{split}
 \theta_i&=\frac{\delta}{d_i+\delta},\qquad
 S_\delta=\sum_i\frac{\delta d_i}{d_i+\delta}x_i^2,\\
 t_\delta&=\theta x-\theta_0x_0e_0,\qquad
 m_\delta=n^{-1}\sum_i(t_\delta)_i,\\
 \ell_\delta^2&=\sum_i(d_i+\delta)
                         [P_{-\sigma}t_\delta]_i^2,\\
 L_\delta&=R(D+\delta I)^{-1}R|_{\operatorname{im}R}.
 \end{split}                                                \tag{8}
\]

The mark is removed **before** taking the opposite projection in `ell`.
All coordinates of the projection, including its new marked coordinate,
are retained in its weighted norm.

The actual source resolvent decrement is

\[
 \begin{split}
 \Delta_\delta
 &:=b^2\langle e,[T^{-1}-(T+\delta I)^{-1}]e\rangle\\
 &=\int\frac{\delta}{\lambda+\delta}\,d\nu(\lambda).
 \end{split}                                                \tag{9}
\]

**Finite theorem.** One has the exact decomposition

\[
 \boxed{\quad
 \Delta_\delta=S_\delta+
     \langle R(\theta x),L_\delta^{-1}R(\theta x)\rangle,
 \quad}                                                     \tag{10}
\]

and the entirely explicit upper certificate

\[
 \boxed{\quad
 \Delta_\delta\le
 S_\delta+
 \left[
 |\theta_0x_0|\sqrt{d_0+\delta}
 +|m_\delta|\sqrt{\sum_i(d_i+\delta)}
 +\ell_\delta
 \right]^2=:F_\delta.
 \quad}                                                     \tag{11}
\]

In particular, for every `0<epsilon<=delta`,

\[
 \nu((0,\epsilon])\le2F_\delta.                              \tag{12}
\]

This upper certificate uses a diagonal weight, one opposite Fourier
projection, and scalar operations. It does not require an inverse or
eigenvalue computation, an assumed small support, or a norm bound on `x`.
It is a sufficient inequality rather than a renaming of `Delta_delta`:
the inequality can be strict, even substantially so in the replay.

**Proof of (10).** The elementary dual minimum for a diagonal compression
is

\[
 f_\delta:=\langle e,(T+\delta I)^{-1}e\rangle
 =\min_{z\in\operatorname{im}R}
       \sum_i\frac{[(e_0+z)_i]^2}{d_i+\delta}.               \tag{13}
\]

At zero, the minimizing full vector is `q_0=Dx/b`, since
`P_sigma q_0=e`. Testing this vector at positive `delta` gives value
`f_0-S_delta/b^2`. Its component of the weighted gradient in `im R` is

\[
 R(D+\delta I)^{-1}q_0
   =b^{-1}R[(1-\theta)x]=-b^{-1}R(\theta x).
\]

Completing this quadratic minimum subtracts
`b^{-2}<R(theta x),L_delta^{-1}R(theta x)>`. Multiplication by `b^2`
proves (10).

**Proof of (11).** For any vector `h`, the extension minimum gives

\[
 \|Rh\|_{L_\delta^{-1}}^2
 =\min_{z\in V_\sigma}\sum_i(d_i+\delta)(h_i+z_i)^2
 \le\sum_i(d_i+\delta)h_i^2.                                \tag{14}
\]

Decompose
`R(theta x)=theta_0 x_0 R e_0 + m_delta 1 + P_-sigma t_delta`.
Use the triangle inequality in the `L_delta^{-1}` norm. Apply (14)
to the three original extensions `e_0`, `1`, and
`P_-sigma t_delta`, respectively. This gives exactly the three terms in
(11). In particular the mark cost is `sqrt(d_0+delta)`, rather than the
usually much larger weighted norm of `R e_0`. Finally
`delta/(lambda+delta)>=1/2` on `(0,epsilon]` proves (12). ∎

### What uniform integrability supplies, and what it does not

For fixed `tau`, put `u_i=A_i/a`, so `E_n u=1` and `d_i=rho/u_i`.
For every `R0>=2`, the following elementary quantitative bounds hold:

\[
 \begin{split}
 S_\delta
 &\le2W\delta(R_0+1)+\tau\mathbb E_n[u\mathbf1_{u>R_0}],\\
 |m_\delta|/a
 &\le2\delta R_0/\rho
                    +2\mathbb E_n[u\mathbf1_{u>R_0}].
 \end{split}                                                \tag{15}
\]

For the first, split at `u=R0`, use
`(u-1)^2 <= (R0+1)(u+1)` below the cutoff, and
`delta rho (u-1)^2/(rho+delta u)<=rho u` above it. For the second,
use `theta<=delta R0/rho` below the cutoff and
`|u-1|<=u+1<=2u` above it. Removing the mark can only decrease these
absolute estimates.

The exact identity `sum d=n-b/a<n` gives
`a sqrt(sum(d+delta))<=sqrt(W(1+delta))`. At a fixed floor the actual
stationary coordinate cap and `A_0B_0=1` give `x_0=O_tau(1)` and
`d_0=O_tau(n^{-1/2})`. Consequently, source uniform integrability and

\[
 \boxed{\quad
 \lim_{\delta\downarrow0}\limsup_{p\to\infty}
       \ell_{p,\sigma,\delta}=0
 \quad}                                                     \tag{16}
\]

imply tightness at zero of `nu_sigma` through primes. Indeed, in (15)
first let the field grow, then let `delta` decrease at a fixed `R0`,
and finally increase `R0`. Equations (11)--(12) finish the proof.
The implication applies separately to either sign, or to both.

Here source UI means UI of the normalized bulk source from
[the round-28 integrability note](parallel-integrability-28.md).
It implies UI of both `A/a` and `B/a`: on the bulk,

\[
 G=\sqrt n(A+B-2\sqrt c)
       =\sqrt W(u+u_-)-2\sqrt\tau,
\]

and both normalized spectra are nonnegative. The bounded root contributes
only `O(n^{-1/2})` to a normalized first moment. That earlier note proved
only subcritical energy from UI, not the weighted leakage estimate (16).

Equation (16) is an additional arithmetic target. It concerns the actual
opposite sector and actual weight; no positive-cone estimate can be
applied to its generally signed projection without a further argument.
Neither a bounded union of critical cosets nor a shared prime/square
arithmetic coset is assumed. The exact model in the next section shows
why this extra condition cannot simply be deleted using reciprocity.

### A useful consequence at the mark

Let `x_delta=b(T+delta I)^{-1}e`. Then

\[
 0\le x_0-(x_\delta)_0=\Delta_\delta/b\le F_\delta/b,
 \qquad
 \|T^{1/2}(x-x_\delta)\|^2\le\Delta_\delta.                 \tag{17}
\]

Thus (15)--(16) give a regularized marked-source approximation while
allowing a divergent second inverse moment. For any test `r in V_sigma` with
`<r,T^{-1}r><=M`, its pairing error is at most
`sqrt(M F_delta)`. A uniform bound on this additional test norm is
**not** supplied by UI. This last qualification is the same distinction
between integrability and residual transfer emphasized in round 28.

No fixed-depth arithmetic comparison for `x_delta` has been proved here.
Since `T` itself depends on the exact stationary pair, (17) by itself
does not identify the prime limiting mark or solve Problem 26.

## 4. Exact subcritical stationary obstruction to a UI-only inference

This construction retains the full nonlinear stationary equation. Its
loss of the Paley arithmetic is specified at the end.

Fix `tau>0`; all statements below hold for sufficiently large integers
`t`. Put

\[
 n=2t^8,\quad m=t^5,\quad H=t^2,\quad
 M=(n-2-2m)/2=t^8-t^5-1.
 \tag{18}
\]

Partition the coordinates into the mark, one neutral singleton, two
tail groups of size `m`, and two background groups of size `M`. Choose
`L>sqrt(tau)` by

\[
 L+\tau/L
 =\frac{n\sqrt W-\sqrt n-\sqrt\tau-m(H+\tau/H)}{M}.
 \tag{19}
\]

The right side tends to `2sqrt(1+tau)>2sqrt(tau)`, so the larger positive
quadratic root exists. Define `A,B` by their per-coordinate values:

| Group | Size | `A` | `B` |
|---|---:|---:|---:|
| Mark | 1 | `1` | `1` |
| Neutral | 1 | `sqrt(tau/n)` | `sqrt(tau/n)` |
| First tail | `m` | `H/sqrt(n)` | `tau/(H sqrt(n))` |
| Second tail | `m` | `tau/(H sqrt(n))` | `H/sqrt(n)` |
| First background | `M` | `L/sqrt(n)` | `tau/(L sqrt(n))` |
| Second background | `M` | `tau/(L sqrt(n))` | `L/sqrt(n)` |

Exactly `AB=w`, `sum A=sum B=na`, and `A_0B_0=1`. The pair is positive.
It has `A_i<=A_0=1`, `B_i<=B_0=1` for large `t`. Put `x=A-a1`,
`y=B-a1`. Swapping the tail groups and background groups exchanges the
two vectors, so their centered energies agree. Moreover

\[
 x\perp y,\quad x,y\perp\mathbf1,\quad
 E:=\|x\|^2=\|y\|^2=t/2+O_\tau(1).
 \tag{20}
\]

Orthogonality follows exactly from `sum AB=W=na^2`; the energy asymptotic
follows by retaining `mH^2/n=t/2`, while the root and background squared
norms stay bounded. In particular `E` diverges but is `o(sqrt(n))`.

The actual normalized bulk source has value
`H+tau/H-2sqrt(tau)` on the two tail groups, a bounded value on the
background, and zero on the neutral singleton. Its tail first mass is

\[
 \frac{2m}{n}(H+\tau/H-2\sqrt\tau)=t^{-1}+O_\tau(t^{-3}).
 \tag{21}
\]

It is uniformly integrable; its tail bound at level `R0` is
`O_tau(R0^{-1/2})` once `R0` exceeds the bounded background values.
Both normalized spectra are uniformly integrable for the same reason.

### Realizing this pair by an exact reflection with the correct mark

Let `j=1/sqrt(n) 1`, `g=x/sqrt(E)`, `h=y/sqrt(E)`, and
`alpha=(1-a)/sqrt(E)`. Let `w_*` be a balanced unit vector inside the
first background group: it has half its nonzero coordinates positive,
half negative, one zero coordinate if needed, and
`||w_*||_infty<=1/sqrt(M-1)`. It is orthogonal to every group-constant
vector. Define

\[
 \begin{split}
 z&=e_0-j/\sqrt n-\alpha g-\alpha h,\qquad \widehat z=z/\|z\|,\\
 l_+&=1/2-1/n-\alpha^2,\qquad l_-=1/2-\alpha^2,\\
 p&=\frac{\sqrt{l_+}\,\widehat z+\sqrt{l_-}\,w_*}
                {\sqrt{l_++l_-}}.
 \end{split}                                                \tag{22}
\]

These are well-defined for large `t`. The vectors `g,p` are orthonormal,
orthogonal to `j,h`, and

\[
 p_0=\sqrt{l_+},\quad
 \|z\|^2=l_++l_-=1-1/n-2\alpha^2.
\]

Let `F` be the seven-dimensional space spanned by the six normalized
group indicators and `w_*`. On `F`, declare `g,p` to have eigenvalue
`+1`, `j` eigenvalue zero, and their orthogonal complement eigenvalue
`-1`. On `F^perp`, choose an orthogonal reflection with
`(n-6)/2` positive and `(n-8)/2` negative dimensions. The resulting `K`
is symmetric and obeys

\[
 \begin{gathered}
 K^2=I-J,\quad K\mathbf1=0,\quad
 \dim V_+=(n-2)/2,\quad\dim V_-=n/2,\\
 K_{00}=-1/n,\quad (P_+)_{00}=1/2-1/n,\quad(P_-)_{00}=1/2.
 \end{gathered}                                             \tag{23}
\]

The marked identity follows by substituting
`(P_+)00=alpha^2+p_0^2`. By construction `Kx=x` and `Ky=-y`.
Therefore, with `v=A-B`,

\[
 \Phi(v)=A+B,\qquad K\Phi(v)=x-y=v.
 \tag{24}
\]

This is the **exact**, fixed-positive-floor stationary vector of this
reflection. Indeed, at a fixed finite dimension and positive weights,
`Phi` is strictly Lipschitz below one on every bounded set. The map
`K Phi` is nonexpansive, is a strict contraction on a ball about an
existing fixed point, and keeps that ball invariant. Thus the fixed
point is unique and Picard iteration from zero converges to it. No
field-uniform convergence rate is asserted.

All positive source identities (3)--(5), both reciprocal diagonals and
their exceptional mark product, and the finite identities and bounds
(6)--(15), (17) now apply exactly to this family. The additional limiting
condition (16) will fail. Its energy divergence is not a perturbation error.

### Its actual first inverse source moment is not tight

Multiplication by `d` preserves `F`, so the plus source spectral measure
is entirely described by the two-by-two compression in the basis `g,p`.
In that basis the exact first row and the asymptotic second diagonal are

\[
 T_{11}=Q/E,\qquad
 T_{12}=b\sqrt{l_+}/\sqrt E,\qquad
 T_{22}\sim t/\sqrt{1+\tau}.
 \tag{25}
\]

The first two equalities follow from `Tx=be`. For the third,
`<z,Dw_*>=0`, and the second tail group has normalized `z` coordinate
asymptotic to `-1/sqrt(E)`, diagonal `H/sqrt(W)`, and hence contributes
`H/(sqrt(W)E)~2t/sqrt(1+tau)` to `<z,Dz>`. The coefficient of
`widehat z` in `p` has squared limit `1/2`. The `w_*` contribution is
bounded and all other contributions are lower order. This proves (25).

Consequently the two eigenvalues satisfy

\[
 \lambda_{\rm small}\sim2/t,\qquad
 \lambda_{\rm large}\sim t/\sqrt{1+\tau}.
 \tag{26}
\]

For example this follows from `T11~2/t`, `T12=O(t^{-1/2})`, and the
Schur correction `T12^2/T22=O(t^{-2})`.
The total `nu` mass is `Q=(1-c)(1-a)->1`. Its mass on the large
eigenvalue is bounded by `b^2||e||^2/lambda_large=O_tau(1/t)`. Hence

\[
 \boxed{\quad
 \nu(\{\lambda_{\rm small}\})\longrightarrow1,\qquad
 \lim_{\epsilon\downarrow0}\limsup_{t\to\infty}
          \nu((0,\epsilon])=1.
 \quad}                                                     \tag{27}
\]

This establishes failure of inverse-first-moment tightness despite exact
stationarity, both full reciprocal constraints, source UI, and divergent
subcritical energy. In particular UI cannot prove (16) by the displayed
reciprocal algebra alone. For each fixed `delta>0`, (9) tends to one;
the spatial, mean and mark terms vanish in the subsequent `delta->0`
limit, so the opposite leakage cannot vanish in that order.

**Precisely what is missing from this model.** The construction does not
give a Fourier convolution with the Paley multiplier `chi(1-x)`. It does
not preserve translation identities, convolution closure of the sectors,
or the Paley entry bound. In fact for a coordinate `i` in the second
tail group, direct substitution in (22) gives

\[
 K_{0i}\sim-\frac1{\sqrt{Em}},\qquad
 \sqrt n\,|K_{0i}|\sim2t\longrightarrow\infty.              \tag{28}
\]

This rules out a uniformly Paley-sized entry constant already in the
marked row. The model thus does not prove that (16), or a UI-to-tightness
implication using the Paley arithmetic, is false at primes. Unlike a
generic near-stationary construction, however, it does rule out the
inference using only the full reciprocal source equations, the listed
marked data and source UI. A prime proof must use additional structure.

## 5. Replay and acceptance scope

Run, from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-source-pair-29.py \
  > research/parallel-source-pair-29.jsonl
```

The script imports the existing field construction, actual stationary
solver, and sector basis from the round-28 diagnostic. It stably recovers
both positive spectra using the reciprocal product. It emits 69 records:
21 seven-dimensional exact-model formula evaluations, and 48 Paley
field/floor/sign/regularizer records. The Paley fields are primes
`101,401,9413` and squares `17^2,31^2,97^2`, all at `tau=.05`.
Dense even-sector calculations at the four smaller orders independently
check (6), (9)--(12). The source and diagonal are even, so the omitted odd
sector has zero source measure and does not couple to these calculations.
The two larger orders test the explicit certificate terms using FFTs.

The maximum stationary residual is below `1.0e-12`; maximum positive
source discrepancy is below `4.91e-13`; maximum relative reciprocal Schur
discrepancy is below `5.19e-13`; and the largest exact-decomposition
discrepancy is below `1.75e-13`. All tested inequalities (11)--(12) hold.
For the exact-model formula evaluations, the maximum relative second
inverse source-energy discrepancy is below `1.23e-15` and maximum
reflection discrepancy below `1.17e-15`.

Some plus-side Paley certificate terms at `delta=.01`:

| Order | `E` | `S_delta` | `ell_delta^2` | `F_delta` |
|---:|---:|---:|---:|---:|
| 401 | 2.26284 | .0128121 | .0141175 | .143417 |
| `31^2` | 25.1455 | .0443273 | .272013 | 1.82165 |
| 9413 | 2.60977 | .0122681 | .0174193 | .189648 |
| `97^2` | 82.0901 | .0505299 | .406916 | 2.63173 |

These are finite diagnostics, not an ordered-limit estimate for (16).
At `401`, for example, the exact decrement at this regularizer is
`.0216366`, substantially below its `.143417` certificate. The certificate
is deliberately an upper bound, not a claimed equivalence. At a fixed
finite order every tail eventually vanishes with `delta`, which is not
the field-first assertion needed here.

The constructed model is evaluated in its invariant seven-dimensional
space, so even its very large `n` values do not represent an enormous
matrix computation. These evaluations, and the Paley solves, are floating
point. None is an interval certificate for a stationary point. The exact
model theorem and all finite identities are proved above independently
of numerical convergence.

**Comparison with the supplied notes.** Round 28 gave the exact source
equation, two inverse moments, the full-sector minimum `E^{-1/2}`, broad
soft-mode extraction, and the autocorrelation branch at energy comparable
to `sqrt(n)`. None bounds the subcritical regime. The integrability note
proved only `E_++E_-=o(sqrt(n))` and exhibited a functional obstruction
to residual pairing. Its counterexample did not impose exact nonlinear
stationarity. Fable's accepted positional identities remain valid, but
neither their negative-mass hypothesis nor a common prime/square
arithmetic law is used or proved here. Round 27's cone theorem does not
bound the signed opposite leakage in (16). The new items here are the
coupled identity (6), the mark-stripped finite certificate (10)--(16),
and the exact subcritical/UI stationary obstruction (18)--(28).

**Still missing.** No uniform prime estimate for the leakage (16), for
positional negative mass, or for the actual second inverse moment has
been proved. No transfer from this regularization of the exact stationary
weight to fixed-depth or growing-depth arithmetic expressions has been
proved. Thus neither the prime marked limit nor Problem 26 is resolved.

Only `research/parallel-source-pair-29.md`, `.py`, and `.jsonl` were written.
No shared files, commits, pushes, settings, credentials or external
communications were changed.
