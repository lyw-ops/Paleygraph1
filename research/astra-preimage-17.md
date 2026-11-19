# Localizing the actual preimage without losing its root

**Result: a necessary local response profile, an exact mixed-current law,
and a certified obstruction to a positive response. No improved prime
energy bound is proved.** The original dual can be replaced by a dual
whose forcing is confined to a high level of the **actual** potential.
The root contrast stays exactly one. The change has an exact quadratic
cost equal to the discarded primal energy divided by the product of the
two retained energies. On the remaining low active set, the new potential
and preimage have opposite signs, with the exact relation `d=-eta w`.
They therefore cannot simply be deleted.

The localized dual carries exactly unit signed current through **every**
actual potential level between zero and its forcing level. Its high set
must also contain a positive-positive response core with an explicit
energy-mass lower bound. These are simultaneous constraints on the
preimage, root, and actual level set, rather than conditions on an
arbitrary opposite-sector vector.

At the genuine prime `p=29`, a strict Arb certificate proves that the
canonical preimage has negative entries on **both** signs. At `p=153649`,
a numerical cut retains more than 98% of primal bulk energy, but the
localized preimage still has more than 51% of its norm on the discarded
low active set. At the square `389^2`, the plus response is instead
strongly concentrated on the subfield annihilator: that set carries
about 98.75% of the canonical preimage norm and 40.57% of primal energy.
The square comparison shows that the new profile alone cannot establish
the prime target.

Starting points are [round 16](astra-source-16.md),
[the actual high cuts](astra-cuts-15.md), and
[prime additive rigidity](prime-additive-rigidity.md). Exact additive
rank is already available and is not reproved here. No conditioning
claim for arbitrary signed-sector vectors is used. A sign below is not
identified as the larger ordinary-theta sign from its positive-width
marker.

## 1. Keep the two different potentials separate

Fix either sign, a prime power `q=1 mod 4`, and $0<r<1$. Use the actual normalized
reciprocal pair

\[
Q=J+rP+r^{-1}N,\quad y=Qx,\quad x,y\ge0,
\quad x_0=a,\quad y_0=a^{-1},\quad x_i y_i=0\ (i\ne0).
\]

Let `n=(q-1)/2`, `j=1/sqrt(n)`, `c=<j,x>=<j,y>`, and put

\[
\eta=\frac{r^2}{1-r^2},\qquad \beta=\frac r{1+r},\qquad
R=N+\beta J,\qquad Q=(r^{-1}-r)(R+\eta I).
\tag{1}
\]

Write

\[
I=\{i\ne0:x_i>0\},\quad v=x_I,\quad E=\|v\|^2>0,\quad
C=E_I^*RE_I,\quad T=C+\eta I,\quad f=-aE_I^*Re_0.
\]

Actual complementarity is `Tv=f`. The canonical round-16 dual is

\[
w=T^{-1}v/E,\qquad d=RE_Iw,\qquad -ad_0=1.
\tag{2}
\]

In formulas involving coordinates outside `I`, `w` means its extension
by zero, including at the root. This convention is also used for all
localized responses below.

The **actual primal potential**, distinct from `d`, is

\[
\Psi=-Nx/\eta,\qquad
t=\frac{\beta c}{\eta\sqrt n}=\frac{(1-r)c}{r\sqrt n}.
\]

The full identity `Psi-t 1=x-y/r` gives, off the root,

\[
x_i=(\Psi_i-t)_+,
\quad I=\{i\ne0:\Psi_i>t\},
\quad U_\tau=\{i\ne0:\Psi_i>t+\tau\}
           =\{i\in I:v_i>\tau\}.
\tag{3}
\]

Thus a cut below is specified by the actual potential and its actual
threshold. It is not a mask chosen after inspecting an arbitrary dual.

## 2. An exact coupled budget for the original response

For any preimage `z` on `I`, set `D_z=RE_I z` and `W_z=sum_I z_i`.
Define

\[
\mathcal B(z)=
 \|(D_z)_I\|^2+\eta^2\|z\|^2
 +2\eta\|D_z\|^2
 +\frac{2\eta\beta(1-\beta)}n W_z^2.
\]

Then

\[
\boxed{\mathcal B(z)=\|Tz\|^2.}
\tag{4}
\]

Indeed `R-R^2=beta(1-beta)J`, so

\[
z^TCz=\|D_z\|^2+\beta(1-\beta)W_z^2/n.
\]

Expand `||Cz+eta z||^2` to prove (4). In particular

\[
\mathcal B(w)=1/E.
\tag{5}
\]

This retains the mean correction and the relation between the four
costs. Separate norm upper bounds discard that relation. As in round 16,
`0<=C<=I` and `R^2<=R` also give

\[
\|d_I\|\le E^{-1/2},\qquad
\eta\|w\|\le E^{-1/2},\qquad
\sqrt\eta\|d\|\le(2\sqrt E)^{-1}.
\tag{6}
\]

The factor `1/2` in the last estimate uses
`s/(s+eta)^2<=1/(4eta)`, rather than just dropping terms in (4).

## 3. High-level localization with exactly preserved contrast

Take any nonempty subset `U` of the actual `I`, and let

\[
v_U=\mathbf1_Uv,\quad E_U=\|v_U\|^2,\quad
L=I\setminus U,\quad E_L=E-E_U.
\]

Here `v_U` still has coordinates on the **whole** space `R^I`. Define

\[
\boxed{w^{U}=T^{-1}v_U/E_U,\qquad d^{U}=RE_Iw^{U}.}
\tag{7}
\]

This inverse uses the entire actual support. It is not an inverse of the
principal block on `U`. Since `f=Tv`,

\[
f^Tw^U=v^Tv_U/E_U=1,
\qquad -ad^U_0=1.
\tag{8}
\]

All three bounds in (6) hold with `E_U,w^U,d^U` in place of `E,w,d`,
and `B(w^U)=1/E_U`. More precisely,

\[
\boxed{
\mathcal B(w^U-w)=\frac{E_L}{EE_U}.}
\tag{9}
\]

For the proof, apply (4) and use the disjoint supports of `v_U,v_L`:

\[
\left\|\frac{v_U}{E_U}-\frac vE\right\|^2
=\frac1{E_U}-\frac1E=\frac{E_L}{EE_U}.
\]

The difference itself has zero root potential. Operator contraction
gives the useful individual estimates

\[
\begin{split}
\|(d^U-d)_I\|&\le\sqrt{E_L/(EE_U)},\\
\eta\|w^U-w\|&\le\sqrt{E_L/(EE_U)},\\
\sqrt\eta\|d^U-d\|&\le\tfrac12\sqrt{E_L/(EE_U)}.
\end{split}
\tag{10}
\]

Now take `U=U_(lambda/sqrt(n))` from (3). The actual mass bound gives

\[
E_L\le\frac\lambda{\sqrt n}\sum_{i\in I}v_i\le\lambda.
\tag{11}
\]

In particular, on any subsequence failing the desired prime bound,
`E>=epsilon log_2^* p`, we can choose `lambda_p -> infinity` with
`lambda_p=o(log_2^*p)`. Then

\[
\begin{gathered}
E_U/E\longrightarrow1,\qquad |U|\le n/\lambda_p=o(n),\\
\sqrt E\,\|(d^U-d)_I\|\longrightarrow0,\qquad
\eta\sqrt E\,\|w^U-w\|\longrightarrow0,\\
\sqrt{\eta E}\,\|d^U-d\|\longrightarrow0.
\end{gathered}
\tag{12}
\]

Thus every bad **actual** source admits a nearby root-normalized dual
with forcing on an `o(n)` actual high-potential set. Equation (12) is
relative to the natural upper-bound scales in (6), not necessarily to
the measured norms of the three vectors. No lower bound on those
measured norms is being assumed.

At a prime cubic width, the new dual also retains the already proved
full additive translation rank `p`. Indeed, writing `x=a b`, the
coordinates of `a w^U` and `a d^U` lie in the same coefficient field as
in round 16, and `a d_0^U=-1`. Thus high-level localization does not
evade the existing prime nonvanishing theorem; it adds constraints to
its quantitatively insufficient conclusion.

### What happens on the discarded active layer

The full equations in (7) say exactly

\[
\begin{cases}
d_i^U+\eta w_i^U=v_i/E_U,&i\in U,\\
d_i^U=-\eta w_i^U,&i\in L.
\end{cases}
\tag{13}
\]

Equivalently,

\[
w_L^U=-(C_{LL}+\eta I)^{-1}C_{LU}w_U^U.
\tag{14}
\]

This is the exact response through the low active layer. A small
discarded **primal** energy in (11) does not bound its preimage norm.
Deleting it changes the root by

\[
-a(RE_Uw_U^U)_0-1=a(RE_Lw_L^U)_0
\]

and creates low-layer residual `C_LU w_U^U`. Neither quantity is licensed
to be ignored at the source scale `eta`. The elimination formula on `U`
is the Schur complement

\[
\left[C_{UU}+\eta I-
 C_{UL}(C_{LL}+\eta I)^{-1}C_{LU}\right]w_U^U=v_U/E_U.
\tag{15}
\]

Replacing this matrix by `C_UU+eta I` is a different problem.

## 4. A necessary positive response core inside the high set

Write `W=sum_I w_i^U` and define

\[
H_U=\|d^U\|^2+\frac{\beta(1-\beta)}n W^2
                 +\eta\|w_L^U\|^2>0.
\]

The root contrast ensures strict positivity. Pair (13) on `L` with
`w_L^U`, and use `w^{U T}Cw^U=||d^U||^2+beta(1-beta)W^2/n`, to obtain

\[
\boxed{\sum_{i\in U}w_i^U d_i^U=H_U.}
\tag{16}
\]

Every low-layer product is nonpositive. Thus the high layer must pay
for the global dual energy, its mean correction, and the entire low-layer
preimage energy in (16). This is stronger than merely asking for a
nonnegative total quadratic form.

For a dimensionless local description set, on `U`,

\[
\rho_i=v_i^2/E_U,\qquad
s_i=\eta E_Uw_i^U/v_i,\qquad
\Delta_U=\eta E_U H_U.
\]

Then

\[
\boxed{\sum_{i\in U}\rho_i s_i(1-s_i)=\Delta_U>0.}
\tag{17}
\]

The probability weights `rho` are the **actual high-level energy
profile**. Both members of the response are positive precisely when
`0<s_i<1`. Since `s(1-s)<=1/4` there and is nonpositive elsewhere,

\[
\boxed{
\sum_{i\in U:\ 0<s_i<1}\rho_i\ge4\Delta_U.}
\tag{18}
\]

The same calculation also bounds an interior band. For `0<delta<1/2`,
put `b=delta(1-delta)`. Since `s(1-s)<=b` outside that band,

\[
\sum_{\delta\le s_i\le1-\delta}\rho_i
\ge\frac{(\Delta_U-b)_+}{1/4-b}.
\tag{19}
\]

One cannot replace the weighted identity by a claim that every
preimage entry is positive, or that every high-level entry has
`0<s_i<1`. The numerical replay finds entries outside this interval.
The `p=29` certificate below disproves positivity of even the original
canonical preimage.

These inequalities do not assert a uniform positive lower bound on
`Delta_U`. The finite data show it decreasing in the tested range, for
both primes and square plus. Such a lower bound would require another
argument.

## 5. Unit signed current through all lower actual levels

Let `S={0} union I`, extend `w^U` by zero at the root, and for distinct
indices put

\[
G_{ij}=-R_{ij}=\frac12\left(\sigma K_{ij}+
                                  \frac{1-r}{(1+r)n}\right).
\]

These conductances are signed. For `V subset I` define the outward
current

\[
\mathcal F_U(V)=
\sum_{i\in V,\ j\in S\setminus V}
G_{ij}(x_j w_i^U-x_i w_j^U).
\tag{20}
\]

The exact mixed law is

\[
\boxed{\mathcal F_U(V)=\frac1{E_U}
                  \sum_{i\in V\cap U}x_i^2.}
\tag{21}
\]

For a direct proof, the divergence at a bulk index is

\[
\sum_{j\in S}G_{ij}(x_jw_i^U-x_iw_j^U)
=x_i(Rw^U)_i-w_i^U(Rx)_i
=x_i(d_i^U+\eta w_i^U),
\]

since `(Rx)_i=-eta x_i` on `I`. Now use (13). Internal edge currents
cancel when summing over `V`. The divergence at the root is `ad_0^U=-1`,
so the unit source is balanced exactly by the root sink.

For the actual cut `U=U_tau`, every `0<=s<=tau` therefore satisfies

\[
\boxed{\mathcal F_{U_\tau}(U_s)=1.}
\tag{22}
\]

This is a whole interval of exact unit-current levels, including the
entire positive support at `s=0`. The original canonical response has
the related law

\[
\mathcal F(V)=E_V/E,\qquad
\mathcal F(U_s)\ge1-s\sqrt n/E.
\tag{23}
\]

When `h_i=w_i^U/x_i` on `I` and `h_0=0`, (20) is equivalently
`sum_cross G_ij x_i x_j(h_i-h_j)`. For every cut in (22), the Jacobi
entry bound yields the necessary weighted oscillation

\[
\sum_{i\in U_s,\ j\in S\setminus U_s}
 x_i x_j|h_i-h_j|
\ge\frac{2n}{\sqrt q+(1-r)/(1+r)}.
\tag{24}
\]

The absolute values in (24) give a lower bound, not a replacement for
the signed equality (22). Positivity of individual conductances and a
maximum principle are unavailable. The factor-one normalization in
(21) uses `G=-R_off`; the round-15 cut conductance is twice this `G`.

This changes the form of a possible arithmetic target: a bad source
would have to sustain the entire current plateau (22), with the nearby
original response (12), the harmonic low layer (13), and the positive
high core (17). It does **not** turn an unknown source approximation at
accuracy `p^(-2/3)` into an already controlled order-one estimate. The
current contains the unknown response itself, potentially with large
signed contributions.

## 6. Square control: exact subfield identities and a distinct profile

Let `q=ell^2`, use plus, and let

\[
H=(\mathbb F_\ell^\times)^\perp,\qquad
k=|H|=(\ell+1)/2,\qquad m_H=k/\sqrt n.
\]

The [square Fourier calculation](square-order-control.md) gives
`N 1_H=0`. Testing the actual reciprocal equation against `1_H` gives
the exact identity

\[
\boxed{
r\sum_H x_i+(1-r)m_Hc=\sum_H y_i.}
\tag{25}
\]

It needs no assertion that `H\{0}` is active. Since `y_0=1/a`, it
forces the actual local energy bound

\[
\boxed{
\sum_{H\setminus\{0\}}x_i^2\ge
\frac1{k-1}\left(
\frac{a^{-1}-(1-r)m_Hc}{r}-a\right)_+^2.}
\tag{26}
\]

The parameters in this finite bound are the measured actual `a,c`.
No unproved asymptotic balance of the mark at `r=q^(-1/3)` is inserted.

For **every** preimage on `I`, the same subfield test gives

\[
\sum_H d_i=\frac{\beta k}{n}\sum_I w_i.
\tag{27}
\]

If `H\{0} subset I`, the canonical equations specialize to

\[
\boxed{
\eta\sum_{H\setminus\{0\}}w_i
 +\frac{\beta k}{n}\sum_Iw_i
=\frac1E\sum_{H\setminus\{0\}}x_i-\frac1a.}
\tag{28}
\]

For the localized dual, replace the first sum on the right by
`sum_(H intersect U) x_i/E_U`; the left uses `w^U`. Thus the mean
correction and the large response on the subfield must be kept together.
In the tested square plus cases all these subfield bulk coordinates are
active. That is a checked finite fact, not a general theorem in this note.

At `q=389^2`, (26) gives `1.47782583...` for subfield bulk energy,
versus actual numerical `1.48311911...`. The subfield contains 195
coordinates including the root. Its share of total primal bulk energy
is `0.40570915...`; its share of canonical preimage **norm** is
`0.98747861...`. This separates primal mass/energy concentration from
response concentration. The `lambda=1` localized dual has only
`0.08346047...` of its norm in the low active layer, compared with
`0.53279361...` at the nearby prime `153649,+`.

All localization, budget, core, and current identities in Sections 1–5
hold over squares. They remain compatible with the square failure of
the desired energy estimate proved in round 15. Formula (27), supplied
by the actual subfield, is the additional square mechanism in this
comparison; the data alone prove no prime exclusion of an approximate
version.

## 7. Finite replay and a genuine-prime sign certificate

[astra-preimage-17.py](astra-preimage-17.py) and its
[32 numerical rows](astra-preimage-17-results.jsonl) cover both signs
at nine primes through `153649` and seven squares through `389^2`, at
`r=q^(-1/3)`. Each nonempty high cut at scaled thresholds
`lambda=0.5,1,2,4` has a new whole-support response solve. Five actual
potential levels test the mixed current, including its unit plateau.
The replay checks the original source, preserved root, coupled budget,
exact localization cost, low harmonic equation, high mixed pairing,
and positive-core bound.

The largest identity discrepancy is below `2.3e-10`; the largest
reported QP residual is below `2.0e-11`. These use numerical support
detection at `1e-8`, not interval certificates of the large supports.
The support-restricted conjugate-gradient solve is checked against its
full residual. The theorem statements above do not depend on a numerical
zero threshold.

For `lambda=1`, selected diagnostics are:

| Order, sign | `E` | `E_U/E` | `||w_L^U||/||w^U||` | Canonical negative norm fraction | `Delta_U` |
|---|---:|---:|---:|---:|---:|
| `9413,+` | 2.09824 | 0.97535 | 0.55336 | 0.65297 | 0.02997 |
| `153649,+` | 2.50557 | 0.98119 | 0.53279 | 0.69402 | 0.01172 |
| `153649,-` | 2.51333 | 0.98208 | 0.51655 | 0.69470 | 0.01072 |
| `97^2,+` | 2.75484 | 0.97873 | 0.15982 | 0.25025 | 0.03449 |
| `389^2,+` | 3.65562 | 0.98625 | 0.08346 | 0.15177 | 0.01474 |

Norm fractions in the table are not squared energy fractions. These
observations warn against dropping the low preimage; they do not prove
an asymptotic lower bound for its norm fraction at primes.

The separate [192-bit Arb replay](astra-preimage-17-certified.jsonl)
certifies the unique actual supports at `p=29,r=29^(-1/3)` by solving
the positive block and verifying every active primal sign and inactive
dual sign. It then encloses the canonical preimage. On plus,

\[
w_3=w_{11}=-0.03963822929646111512\ldots<0;
\]

on minus,

\[
w_1=w_{13}=-0.97722346266690525847\ldots<0.
\]

Both are actual responses to `v/E`, with the prescribed root source and
the exact cubic width. This refutes a sign restriction `w>=0` even when
the sign of larger ordinary theta is unspecified, because both signs
fail at the same prime. It also rules out a nondecreasing local model
`w_i=F(Psi_i-t)` with `F(0)=0` on the bulk: all active arguments are
positive, so such a model would make every active response nonnegative.
No assertion against arbitrary signed local interpolation is made.

The same certificate verifies the high-cut root and mixed profile. For
`lambda=1`, `U={4,10}` on plus and `U={6,8}` on minus. The respective
values of `Delta_U` are approximately `0.13387721789` and
`0.24996938092`; all the high energy belongs to the positive-positive
core in these two small cases. The minus lower bound `4 Delta_U` is
within `0.000122477` of one.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python -B research/astra-preimage-17.py --large \
  > research/astra-preimage-17-results.jsonl
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 \
  .venv/bin/python -B research/astra-preimage-17.py --certificate \
  > research/astra-preimage-17-certified.jsonl
```

## 8. Remaining prime question

The remaining energy target is still `E=o(log_2^*p)` on the larger
ordinary-theta side, equivalently the round-15 source test at compressed
accuracy `o(p^(-2/3) sqrt(log_2^*p))`. This round does not improve that
accuracy or the target exponent.

A failure now has the following precise necessary profile: a high
actual-potential set of density tending to zero retains almost all bulk
energy; a root-preserving dual near the canonical one is driven only on
that set; its low active layer has exactly opposite potential/preimage
signs; its high layer has the weighted positive core (17); and unit
signed current crosses all intervening actual levels. Arbitrary
full-rank signed-sector examples need not satisfy this collection of
conditions. Conversely, it remains unproved that primes exclude it,
and the square mechanism demonstrates why a field-independent argument
from these conditions alone cannot suffice.

Only this note, its uniquely named script, and its two JSONL outputs
were written. README, ledger, shared scripts, and remotes were not edited.
