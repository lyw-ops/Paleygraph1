# Round 22: the moving-width mark barrier

This note separates two valid ways to use a reciprocal solution at
`r=C/sqrt(n)` from an invalid free extrapolation of its mark. It gives a
proof-grade scalar sufficient condition for an `O(n^(1/4))` minimum pinned
defect, and an actual-support obstruction to raw-row extrapolation. Neither
result proves that condition on both prime signs. All new files have the
prefix `research/astra-transport-22`.

## 1. Notation and an exact scalar certificate

Use the conventions of [quadratic theta](quadratic-theta.md) and
[anchored repair](anchored-repair-20.md). Write `P=P_{-sigma}`,
`U_{-sigma}=R1+im P`, `n=(q-1)/2`. For a prescribed normalized mark `a>0`, let

\[
d_a=\min\{\|(-Y)_{+,\mathrm{off}}\|_2:
Y\in U_{-\sigma},\ \overline Y=1,\ Y_0=a\sqrt n\}.
\]

For `a sqrt(n)>1`, Round 20 gives the exact dual

\[
d_a=\sup_{W\ge0,\ W\in U_\sigma,\ W_0=1}
\frac{(a\sqrt n-S)_+}{T},\qquad
S=\sum W,\quad T=\|W_{\mathrm{off}}\|_2. \tag{1}
\]

The denominator cannot vanish for these sectors. At a positive minimum a
maximizing witness exists. This is the actual Fourier-support dual, not a
relaxation to arbitrary positive vectors.

**Scalar certificate.** For any `0<r<1`, if

\[
M_\sigma(r)\ge r+(1-r)a^2, \tag{2}
\]

then

\[
\boxed{d_a^2\le \frac{nr a^2}{M_\sigma(r)-r}
\le\frac{nr}{1-r}.} \tag{3}
\]

Proof: an admissible `W` in (1) is also an anchored trial for the reciprocal
quadratic program, with forbidden projection exactly zero. Therefore

\[
M_\sigma(r)\le (1-r)S^2/n+r(1+T^2). \tag{4}
\]

Put `A=M_sigma(r)-r`, `B=1-r`, `z=S/sqrt(n)`. Only `z<a` contributes.
Then `T^2 >= (A-Bz^2)/r`. Under (2), the denominator is positive on this
interval, and

\[
\frac{(a-z)^2}{A-Bz^2}\le \frac{a^2}{A}.
\]

For example its derivative has the sign of `B a z-A`, which is nonpositive
because `A>=Ba^2`. Substitute in (1). Equality at `z=a` causes no difficulty:
that witness has zero numerator. This proves (3).

At `r=C/sqrt(n)`, the last bound is
`d_a <= sqrt(C/(1-C/sqrt(n))) n^(1/4)`. The constant is explicit and the
argument does not require any support identification or descent convergence.
A rigorous lower scalar bound for `M_sigma(r)` suffices in (2); by exact
reciprocity it can be supplied by an upper-energy trial of the opposite sign.

At least one sign has `M_sigma(r)>=1`. Consequently at **every field** at
least one sign has `d_1 <= sqrt(nr/(1-r))`. The selected sign may depend on
the field and width. This is not new endpoint information: endpoint
reciprocity already makes mark one feasible on at least one endpoint sign.
The useful additional input would be (2) on both signs.

A useful sufficient hypothesis for all prescribed marks `a<1` is

\[
\lim_{C\to\infty}\liminf_{p\to\infty}
\min_{\sigma=\pm}M_\sigma(C/\sqrt n)=1. \tag{5}
\]

For any `a<b<1`, choose a finite `C` with the inner liminf above `b^2`;
then (2) holds eventually. Thus (5) implies the required uniform defect bound
for each `a<1`, and the large-penalty decay in [Round 21](soft-tail-21.md).
Equation (5) is still unproved here. It is a large-`C` mesoscopic statement,
whereas the full endpoint conjecture uses the small-`C` limit. No converse
from bounded defect to (5) has been established: (4) only tests endpoint-
sector rows, while the minimizer defining `M_sigma(r)` can have nonzero
forbidden projection.

Fixed positive width does not provide (3) at the desired scale: it gives
only `O(sqrt(n))`. Substitution of a slowly vanishing width likewise leaves
the factor `sqrt(nr)` unless there is new scalar control at the moving width.

## 2. Exact transport of the actual reciprocal row

Let `x=A_sigma(r)`, `y=A_{-sigma}(r)` be the actual reciprocal pair, and

\[
x=cj+u+rv,\quad y=cj+ru+v,\quad
c^2+r(\|u\|_2^2+\|v\|_2^2)=1.
\]

Set `H=(J+P)y=cj+v`, `a_r=H_0>0`. Let
`ell=Pe_0`, `kappa=P_00`, and `M=1-ell/kappa`; `M_0=0`, mean `M=1`, and
`M_i>0` off the mark for sufficiently large fields. For a target mark `a`, put

\[
t=a/a_r,\qquad
Y^{\mathrm{raw}}_a=t\sqrt n H+(1-tc)M. \tag{6}
\]

This is **exactly** in the target sector with mean one and mark `a sqrt(n)`.
If `tc<=1`, its padding is nonnegative, hence

\[
\boxed{d_a\le\|(-Y^{\mathrm{raw}}_a)_+\|_2
\le t\sqrt{nr(1-c^2)}.} \tag{7}
\]

Indeed `H=y-ru`, `y>=0`, so the negative-part norm is at most `r||u||`.
Thus raw transport is free up to the normalized mark `a_r/c`, which can be
larger than `a_r`; the mean reserve must be included in the comparison.
This improves the threshold obtained by preserving the original raw mark.

At a fixed-width target one may take `a=H_s(0)` in (6). Nothing in this
identity implies `a<=a_r/c`. The field-first fixed-width limit of `H_s(0)`
does not compare it to a moving-width reference.

## 3. A sharp support obstruction to extending (7)

The actual reciprocal supports give more than a norm bound. Complementarity
says `x_i y_i=0` off the mark, and elimination of `u` gives

\[
H_i=\frac{y_i-rx_i+r(1-r)c/\sqrt n}{1-r^2}. \tag{8}
\]

On the **actual** zero set `Z={i !=0:y_i=0}`, (6) becomes

\[
Y^{\mathrm{raw}}_{a,i}
=-\frac{tr\sqrt n}{1-r^2}x_i
+\frac{trc}{1+r}-(tc-1)M_i.
\]

It follows, without approximation, that

\[
\boxed{\|(-Y^{\mathrm{raw}}_a)_+\|_2^2
\ge\sum_{i\in Z}\left[(tc-1)M_i-\frac{trc}{1+r}\right]_+^2.} \tag{9}
\]

For `tc>=1`, the weaker cardinality version uses `M_min=min_{i!=0} M_i`:

\[
\|(-Y^{\mathrm{raw}}_a)_+\|_2
\ge \left[(tc-1)M_{\min}-\frac{trc}{1+r}\right]_+\sqrt{|Z|}. \tag{10}
\]

Since `M_min=1-O(n^(-1/2))`, at `r=C/sqrt(n)` a fixed overshoot
`tc-1>=delta>0` and `|Z|>=eta n` force `Omega(sqrt(n))` raw defect. Thus the
raw extrapolation can lose a full factor `n^(1/4)` even though its source
has the desired defect scale. Positivity at coordinates outside `Z` cannot
cancel this lower bound. It also applies when both members vanish there.

Conversely, with bounded `t,c`, this obstruction allows an `O(n^(1/4))` raw
bound only if the overshoot above `1+O(r)` is `O(n^(1/4)/sqrt(|Z|))`.
For a dense actual zero set the permitted overshoot is `O(n^(-1/4))`.
This is a necessary condition for **this trial**, not a lower bound on
`d_a`; root-zero Fourier optimization can redistribute these defects.
No assertion that every prime reciprocal zero set is dense is made.

## 4. Square controls and what they do not exclude

At square plus, let `h=(sqrt(q)+1)/2` and let `I` be the subfield annihilator.
The exact witness `1_I` in (1) yields, for every target mark,

\[
\boxed{d_a\ge\frac{(a\sqrt n-h)_+}{\sqrt{h-1}}.} \tag{11}
\]

For fixed `a>1/sqrt(2)`, the coefficient after division by `n^(1/4)` tends to
`2^(1/4)(a-1/sqrt(2))`. In particular an `o(n^(1/4))` universal theorem is
false, but (11) is compatible with the desired `O(n^(1/4))` theorem.
Round 20 has interval-certified attainment of (11) at its two specified
actual reference marks for `q=389^2`; that finite equality is not asserted
at every new mark or square here.

The same exact square trial in the reciprocal quadratic problem gives

\[
M_+(r)\le (1-r)h^2/n+rh. \tag{12}
\]

At `r=C/sqrt(n)` its limiting upper bound is `1/2+C/sqrt(2)`.
For instance, `C=1/4` makes the limiting upper bound below `0.677`, so
condition (2) cannot transport to `a=.98` or `a=1` on square plus at that
width. This uses an actual feasible Fourier-support row, not a synthetic
matrix model. It rules out a universal scalar near-one mark at small `C`,
but does not rule out the large-`C` hypothesis (5) or bounded pinned defect.

## 5. Reproducible actual-support replay

[The script](astra-transport-22.py) uses actual reciprocal fixed points on
three primes and two squares, both signs, `C=4,1,1/4`, and target marks
`.98,1`. It checks (6), (9), and (11), then applies 512 anchored signed
descent steps to distinguish raw transport cost from a better pinned trial.
The recorded zero count uses strictly positive entries of `x` separated from
the contraction residual error; it is still a floating-point diagnostic,
not an interval support certificate. The square lower bound (11) itself is
exact. Values named `scalar_bound` are evaluations of (3) using numerical
`M`, not certified finite bounds.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/astra-transport-22.py > research/astra-transport-22.jsonl
```

All 60 rows completed; the largest reported fixed-point residual was below
`9.87e-12`. Representative `C=1/4`, `a=1` rows are below. These are numerical
values rounded for display; only the square-lower column evaluates an exact
analytic formula.

| Order, sign | Free mark `a_r/c` | Raw defect | Support lower (9) | Defect after 512 steps | Square lower (11) |
|---|---:|---:|---:|---:|---:|
| 37253, + | 1.003693 | 0.086205 | 0 | 0.000020 | — |
| 37253, − | 1.002884 | 0.119692 | 0 | 0.039716 | — |
| 97², + | 0.955343 | 3.344528 | 1.800252 | 2.829751 | 2.826954 |
| 193², + | 0.956202 | 5.451323 | 3.680050 | 4.040660 | 4.028367 |

The square rows show why the distinction matters: raw mark extrapolation
creates extra defect on thousands of actual complementary-support sites,
while anchored descent nearly reaches the subfield lower bound. At `193²`
the squared-field lower coefficient is about `0.344835` after division by
`n^(1/4)`; the raw coefficient is `0.466642`. No asymptotic density conclusion
is inferred from these two fields. The sampled primes have free mark above
one, so (7) applies numerically to both prescribed targets. This is not a
uniform prime proof.

The missing uniform input is now explicit: prove a moving-width scalar lower
bound such as (2), show the actual free mark `a_r/c` reaches the target, or
control a genuinely new root-zero correction after the reserve is exhausted.
The raw Euclidean estimate at an uncontrolled moving mark does not by itself
supply any of these inputs.
