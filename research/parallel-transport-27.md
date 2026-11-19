# Actual-increment transport, high-amplitude cores, and a finite inverse lemma

Round 27, 2026-11-18. **This does not prove the prime-uniform activation-loss
estimate or ETH Problem 26.** It proves a deterministic finite inverse
lemma for consecutive increments of the actual heterogeneous smoothing
orbit. Low total loss gives signed near-isometric transport. If the
normalized increment cores also have a nearly critical adjacent ℓ¹
product, thresholding them gives flat sending and receiving magnitudes on
actual high-amplitude coordinates, at every time of the specified finite
interval. The proof does not derive critical concentration or constant
signs from low activation loss.

The distinction matters even on the actual square orbit: a small broad
increment tail can badly inflate its global ℓ¹ product. A trimming lemma
below charges discarded **ℓ² energy**, then tests the ℓ¹ product of the
remaining, normalized cores. The prime samples remain broad. No statement
about arbitrary directions or a field-first fixed-depth limiting law is
used as a prime-uniform actual-orbit estimate.

The starting point is [Round 26](parallel-activation-26.md). The older
[flat transport analysis](parallel-cap-19.md), [anchored concentrated-defect
gap](anchored-repair-20.md), [critical-set restrictions](critical-sets.md),
and [nonalternating prime gap](parallel-rectangle-20.md) describe precisely
which extra spatial and sign hypotheses would make the inverse output
arithmetically useful. All arithmetic inputs here are inherited from
those notes; the new lemmas below are independent linear algebra and
scalar activation calculations.

## 1. Actual normalization and signed transport

Let `q=2n+1`, `m₀=n/√q`, and use the real symmetric Paley operator with

\[
 K^2=I-J,\quad KJ=0,\quad J=\mathbf1\mathbf1^T/n,
 \qquad |K_{ij}|\le m_0^{-1}.
 \tag{1}
\]

The entry bound is the Jacobi bound in the cited notes, with
`Kᵢⱼ=k(i-j)/m₀`. Both signs of `K` are allowed. The actual orbit is

\[
 c_0=4n,\quad c_i=4\tau\ (i\ne0),\qquad
 V_0=0,\quad V_{t+1}=K\sqrt{V_t^2+c}.
 \tag{2}
\]

Write `Dₜ=Vₜ₊₁−Vₜ`, `uₜ=Dₜ/‖Dₜ‖₂` when nonzero, and

\[
 d_{t,i}=\frac{V_{t,i}+V_{t+1,i}}
 {\sqrt{V_{t,i}^2+c_i}+\sqrt{V_{t+1,i}^2+c_i}},\quad
 a_{t,i}=|d_{t,i}|,\quad \Sigma_t=\operatorname{diag}(\operatorname{sign}d_t).
\]

A sign at zero can be chosen arbitrarily. Define the full activation and
mean losses, **including the mark**, by

\[
 \delta_t=\sum_i(1-d_{t,i}^2)u_{t,i}^2,\quad
 \mu_t=\|J(d_tu_t)\|_2^2,\quad
 r_t=\frac{\|D_{t+1}\|_2}{\|D_t\|_2}
      =\sqrt{1-\delta_t-\mu_t}.
 \tag{3}
\]

The exact recurrence is `Dₜ₊₁=K(dₜDₜ)`. Thus

\[
 \|u_{t+1}-K\Sigma_tu_t\|_2
 \le \sqrt{\delta_t}+1-r_t.
 \tag{4}
\]

For the inverse lemma it is preferable to keep the pairing rather than
lose a square root. Put

\[
 \gamma_t=1-\langle u_{t+1},K\Sigma_tu_t\rangle\ge0.
\]

When `rₜ>0`, the following sharper bound is valid:

\[
 \boxed{\quad
 \gamma_t\le 1-r_t+\frac{\sqrt{\mu_t\delta_t}}{r_t}.
 \quad} \tag{5}
\]

To prove it, set `x=Σₜuₜ`, `z=aₜx`, and `e=x−z`. Then
`Kz=rₜuₜ₊₁`, `‖e‖₂²≤δₜ`, `‖Jz‖₂²=μₜ`, and
`⟨z,e⟩=Σ aᵢ(1−aᵢ)xᵢ²≥0`. Therefore

\[
 \langle u_{t+1},Kx\rangle
 =r_t+\frac{\langle z,e\rangle-\langle Jz,Je\rangle}{r_t}
 \ge r_t-\sqrt{\mu_t\delta_t}/r_t.
\]

In particular `δₜ+μₜ≤ε≤1/2` implies `γₜ≤2ε`.
Low **activation** loss without control of the true mean reserve is not
the same as near preservation of the increment norm. Equation (5) retains
that reserve and uses the actual coordinatewise secant signs.

For any finite interval, (4) also gives the explicit composition error

\[
 \left\|u_{b+1}-(K\Sigma_b)\cdots(K\Sigma_a)u_a\right\|_2
 \le\sum_{t=a}^b(\sqrt{\delta_t}+1-r_t).
 \tag{6}
\]

The diagonal signs in this product cannot be commuted through `K`.

## 2. Trimming with an explicit loss, and actual high amplitudes

Choose any actual coordinate cores `Gₜ` and put

\[
 \rho_t=\|u_t\mathbf1_{G_t^c}\|_2^2<1,\quad
 z_t=\frac{u_t\mathbf1_{G_t}}{\sqrt{1-\rho_t}},\quad
 b_t=\|z_t-u_t\|_2
 =\sqrt{2-2\sqrt{1-\rho_t}}.
 \tag{7}
\]

Their transport defect satisfies the finite bound

\[
 \boxed{\quad
 1-\langle z_{t+1},K\Sigma_t z_t\rangle
 \le \Gamma_t:=\frac12(\sqrt{2\gamma_t}+b_t+b_{t+1})^2.
 \quad} \tag{8}
\]

Here is a short proof avoiding a first-order loss `O(√ρ)` in the pairing.
The block operator

\[
 U=\begin{pmatrix}K&J\\J&-K\end{pmatrix}
\]

is an orthogonal involution by (1). Embed every vector as `(v,0)`.
The full transport pair has squared distance `2γₜ` under this involution.
The triangle inequality after replacing the two vectors by their cores
gives (8), since both core vectors still have norm one. This proof permits
cores chosen from the actual orbit and permits the time interval to
depend on the field. It is a finite identity, not an independence claim.

A useful choice, used in the replay, is

\[
 G_t(\eta)=\{i:1-d_{t,i}^2\le\eta\},\qquad 0<\eta<1.
 \tag{9}
\]

Then `ρₜ≤δₜ/η`; one can retain the much better observed or independently
proved `ρₜ` instead. Every coordinate in this core satisfies

\[
 \boxed{\quad
 \max(|V_{t,i}|,|V_{t+1,i}|)
 \ge\sqrt{c_i}\sqrt{\frac{1-\eta}{\eta}}.
 \quad} \tag{10}
\]

Indeed with `Vₜ,ᵢ=√cᵢ sinh A`, `Vₜ₊₁,ᵢ=√cᵢ sinh B`, the secant is
`tanh((A+B)/2)`. At least one endpoint has absolute rapidity at least that
of the midpoint. Off the mark, the lower bound is
`2√τ√((1−η)/η)`. At the mark it is
`2√n√((1−η)/η)`, as required by the heterogeneous activation.

This only proves a high **maximum endpoint**. For example `Vₜ,ᵢ=0` and
`Vₜ₊₁,ᵢ→+∞` have saturated secants. To claim that both endpoints are
high, an additional endpoint-comparability estimate is needed. No such
estimate is silently included in (10).

No root mass is discarded for free: if one elects to exclude coordinate
zero from `Gₜ`, its increment energy must be added to `ρₜ` in (7).
This is compatible with Round 26's two-step root transfer, but does not
replace that transfer by a bulk-only assumption.

## 3. A quantitative signed cap inverse lemma

**Finite cap lemma.** Let `x,y` be real unit vectors, `K` obey (1), and

\[
 \langle y,Kx\rangle\ge1-g,\qquad
 C=\|x\|_1\|y\|_1/m_0.
\]

For either vector `v=x,y`, let `ℓ=‖v‖₁`, define its half-height layer

\[
 S(v)=\{i:|v_i|\ge1/(2\ell)\},\qquad
 e=\sqrt{2g}+(C-1)_+,\quad f=\sqrt{e+e^2}.
\]

Then

\[
 \boxed{\quad
 \left\|v-\frac{\operatorname{sign}(v)}{\ell}\mathbf1_{S(v)}\right\|_2
 \le f,\qquad
 \left|\frac{\sqrt{|S(v)|}}\ell-1\right|\le f.
 \quad} \tag{11}
\]

If `F(v)=sign(v)1_{S(v)}/√|S(v)|`, then

\[
 \|v-F(v)\|_2\le2f.
 \tag{12}
\]

**Proof.** Symmetry, contraction, and the pairing imply
`‖x−Ky‖₂, ‖y−Kx‖₂≤√(2g)`. The entry cap gives
`|Ky|≤‖y‖₁/m₀=C/ℓ` for the first vector. Put `b=1/ℓ`.
The set `{|v|>b}` has at most `b⁻²` elements, so

\[
 \|(|v|-b)_+\|_2\le\sqrt{2g}+(C-1)_+=e.
\]

Writing `w=|v|`, the exact identity `Σ w(b−w)=bℓ−1=0` shows

\[
 P:=\sum_{w\le b}w(b-w)
 =\sum_{w>b}w(w-b)\le e.
\]

On `w<b/2`, `w²≤w(b−w)`; on `b/2≤w≤b`,
`(b−w)²≤w(b−w)`. Above `b` the squared error sums to at most `e²`.
Thus the squared error in (11) is at most `e+e²`.
The remaining assertions follow from the reverse triangle inequality and
normalization. This proof allows arbitrary vector signs. It does not
replace actual-orbit estimates by an arbitrary-direction assertion.

The balance assumption is only a **product** assumption. Even if `C→1`,
the two effective sizes `‖x‖₁²` and `‖y‖₁²` need not separately approach
`m₀`. Their product approaches `m₀²`. A further balance condition is needed
to use a prime gap formulated for two sets both of size `(1+o(1))m₀`.

There is a sharper elementary variant when the cores have nearly critical
**cardinality product**. Suppose `x,y` are supported on `A,T`, respectively,
and set `c=√(|A||T|)/m₀`, `α=⟨y,Kx⟩>0`. The entry cap and Cauchy--Schwarz
give

\[
 \frac{\|x\|_1}{\sqrt{|A|}}\frac{\|y\|_1}{\sqrt{|T|}}
 \ge\alpha/c,
 \qquad 0<\frac{\|x\|_1}{\sqrt{|A|}},
 \frac{\|y\|_1}{\sqrt{|T|}}\le1.
\]

Each factor is therefore at least `α/c`, and the signed uniform vectors
on the **whole original cores** satisfy

\[
 \left\|x-\frac{\operatorname{sign}(x)}{\sqrt{|A|}}\mathbf1_A\right\|_2,
 \left\|y-\frac{\operatorname{sign}(y)}{\sqrt{|T|}}\mathbf1_T\right\|_2
 \le\sqrt{2(1-\alpha/c)}.
 \tag{12a}
\]

If desired, threshold `|x|` at `1/(2√|A|)` and `|y|` at `1/(2√|T|)`.
At most `8(1−α/c)` of either core's counting mass is removed, by (12a).
Thus this version gives the better `O(√(g+ζ))` magnitude error when
`α≥1−g` and `c≤1+ζ`. Its extra cardinality hypothesis is stronger than
the ℓ¹ hypothesis used in (11); the latter deliberately tolerates tiny
entries on larger cores. Both variants keep the actual high-amplitude
relation because they never add sites outside the chosen cores.

## 4. A finite multi-step inverse statement

Take any finite consecutive interval of actual nonzero increments, choose
cores as in (7), and assume its edges have the explicit bounds (8). Put

\[
 \ell_t=\|z_t\|_1,\quad C_t=\ell_t\ell_{t+1}/m_0,
\]

\[
 e_t=\min_{s:\,t\in\{s,s+1\}}
       \{\sqrt{2\Gamma_s}+(C_s-1)_+\},\quad
 f_t=\sqrt{e_t+e_t^2}.
\]

The minimum is over the incident edges in the interval, so endpoints have
one choice. Define **one layer at each time**, usable simultaneously by
its incoming and outgoing edges:

\[
 S_t=\{i\in G_t:|z_{t,i}|\ge1/(2\ell_t)\},\qquad
 F_t=\frac{\operatorname{sign}(D_t)}{\sqrt{|S_t|}}\mathbf1_{S_t}.
\]

The cap lemma gives `‖Fₜ−zₜ‖₂≤2fₜ`, the size bounds (11), and

\[
 \boxed{\quad
 \langle F_{t+1},K\Sigma_t F_t\rangle
 \ge1-\Gamma_t-2f_t-2f_{t+1}.
 \quad} \tag{13}
\]

All selected sites remain in `Gₜ`, so (10) survives the thresholding.
The sending signs are `sign(dₜ,ⱼDₜ,ⱼ)` and the receiving signs are
`sign(Dₜ₊₁,ᵢ)`. In terms of the normalized Jacobi kernel, the exact signed
rectangle deficit is

\[
 d_t^{\rm rect}
 =\frac1{|S_t||S_{t+1}|}\sum_{i\in S_{t+1},j\in S_t}
 [1-\operatorname{sign}(D_{t+1,i})
     \operatorname{sign}(d_{t,j}D_{t,j})k(i-j)]
 =1-\frac{\langle F_{t+1},K\Sigma_t F_t\rangle}{A_t},
 \quad A_t=\frac{\sqrt{|S_t||S_{t+1}|}}{m_0}.
 \tag{14}
\]

In particular, if `fₜ,fₜ₊₁<1`,

\[
 (1-f_t)(1-f_{t+1})C_t\le A_t
 \le(1+f_t)(1+f_{t+1})C_t.
 \tag{15}
\]

Equations (13)--(15) are a quantitative near-isometric signed rectangle
with flat magnitudes. For example, when the right side of (13) is
positive, its deficit is at most

\[
 1-\frac{1-\Gamma_t-2f_t-2f_{t+1}}
 {(1+f_t)(1+f_{t+1})C_t}.
 \tag{16}
\]

The exact cap also supplies `Cₜ≥1−Γₜ`, so the denominator tends to one
when `Γₜ→0` and `(Cₜ−1)₊→0`.

There is an unconditional finite dichotomy on every low-loss edge: either
the normalized core ℓ¹ product exceeds the specified critical window, or
(11)--(16) apply with that window's explicit errors. A bound
`√(|Gₜ||Gₜ₊₁|)≤(1+ζ)m₀` is one stronger, cardinality-based way to
supply the upper window. The ℓ¹ formulation tolerates small entries on
larger cores. Consecutive products also give the exact width relation

\[
 \frac{\ell_{t+2}}{\ell_t}=\frac{C_{t+1}}{C_t}.
 \tag{16a}
\]

Thus near-critical products make the **effective widths** locally
two-periodic. They do not make the supports two-periodic; that inference
would discard the intervening diagonal signs.

This is valid at any stated field and any stated finite horizon, with no
field-size restriction hidden in its constants. To obtain uniform inverse
information along a growing prime horizon, one must prove that the
**actual** `δₜ, μₜ, ρₜ, (Cₜ−1)₊` have the required bounds throughout that
horizon. The lemma does not prove those hypotheses. In particular, small
`δₜ+μₜ` supplies no upper bound on `Cₜ`.

For the cores (9), a hypothetical uniform bound `δₜ+μₜ≤ε` allows
`η=√ε`, `ρₜ≤√ε`, and gives `Γₜ=O(√ε)` uniformly on the interval.
If in addition `(Cₜ−1)₊≤ζ→0`, then
`fₜ=O(ε^(1/8)+√ζ)`. The power is deliberately conservative. The useful
feature is that the estimates hold simultaneously on actual high-amplitude
layers at all stated times; they assert neither their critical concentration
nor an arithmetic prime bound.

## 5. Return rigidity and the signs that still survive

A signed analogue of a useful part of the old overlap argument has a
short finite proof. Let `F₀,F₁,F₂` be unit signed flats on `S₀,S₁,S₂`,
let `Σ₀,Σ₁` be diagonal signs, and assume

\[
 \langle F_1,K\Sigma_0F_0\rangle\ge1-\nu_0,\qquad
 \langle F_2,K\Sigma_1F_1\rangle\ge1-\nu_1.
\]

Write `A=√(|S₀||S₁|)/m₀`,
`E=√(A²−1+2ν₀)`, and
`r=√(|S₂\S₀|/|S₂|)`. The expression inside the square root defining `E`
is nonnegative by the first pairing and the Frobenius cap. Then

\[
 \boxed{\quad
 \left|\frac1{|S_1|}\sum_{i\in S_1}(\Sigma_1)_{ii}\right|
 \ge1-\nu_1-E-r.
 \quad} \tag{17}
\]

Indeed `B=P_{S₁}KP_{S₀}` has Frobenius norm at most `A` and

\[
 \|B-F_1(\Sigma_0F_0)^T\|_F^2\le A^2-1+2\nu_0.
\]

Project the second receiving vector onto `S₀`, at cost at most `r` in
the pairing, and use symmetry to replace `BᵀΣ₁F₁` by
`Σ₀F₀ ⟨F₁,Σ₁F₁⟩`, at cost at most `E`. Its norm is the absolute
average in (17). Thus a near-critical two-step **spatial return** forces
the intervening actual activation signs to be nearly constant. A positive
fraction of both signs on that layer precludes such a return. This gives
a testable additional rigidity statement without assuming it occurs.

However, flat transport itself does not force a spatial return.
Equation (6) contains changing diagonal signs; the simplification to
`K²=I−J` from Round 19 is available only after sign coherence is supplied.
If each `Σₜ` is close to a scalar sign on the relevant increment, that
simplification gives a possible two-cycle of supports, not necessarily
one fixed support. The exact positive-excess recurrence in Round 19 has
more sign information than the smoothing increment recurrence here.

There is also a distinction between an almost constant **activation
sign** and an almost constant **increment sign**. Even if (17) gives the
first, it does not give the second. Actual values `Vₜ` contain the entire
earlier history; a nearly stationary increment may be too small to change
their signs. Saturation alone cannot replace that history by the current
increment. No unsigned rectangle is inferred by deleting the signs in
(14).

## 6. Connection to the inherited prime gap

The [nonalternating prime gap](parallel-rectangle-20.md#3-consequence-for-within-set-rectangles)
can be applied to this output only after the required reductions are
actually proved. One sufficient set of additional hypotheses is:

* balanced layers `|Sₜ|,|Sₜ₊₁|=(1+o(1))m₀`;
* sending and receiving signs each constant up to `o(1)` counting mass,
  so (14) reduces to the old single-global-sign rectangle;
* the two layers overlap in `(1−o(1))m₀` sites;
* that common layer is `o(m₀)` from a union of a fixed number of cosets of
  one subgroup.

Under these hypotheses, a sequence with `Γₜ,(Cₜ−1)₊→0` contradicts the
inherited fixed prime gap. The high-energy overlap mechanism of Round 19
is another way to supply bounded coset covers, when its unsigned
hypotheses apply. Its energy threshold is of order `m₀³`; cap counts and
the repeated-difference restrictions in `critical-sets.md` alone only
supply a weaker lower bound and cannot be promoted to this threshold.

The following branches therefore remain open:

* **Broad cores:** `Cₜ` is bounded away from one or grows with the field,
  even with low actual loss. The finite cap inverse is then vacuous.
* **Unbalanced cores:** a near-critical adjacent product with alternating
  large and small effective sizes; the balanced prime gap does not apply.
* **Changing sign patterns:** nearly critical signed rectangles without
  nearly constant sending and receiving signs. An arbitrary sign gauge
  on a frequency coset union need not preserve its annihilator support,
  so the unsigned arithmetic proof cannot simply be reused.
* **Low-energy critical sets:** even globally signed, balanced rectangles
  need not have the high additive energy used for coset reduction.
* **Genuine alternation:** distinct paired coset unions or distinct single
  cosets can survive the inverse transport argument. The untwisted,
  nonalternating prime gap does not exclude the order-two displaced
  single-coset branch of Round 20, whose missing estimate is a pinned
  cross-ratio estimate.

The new return lemma constrains mixed activation signs **if a return is
known**. It does not prove that one of the above branches must disappear
on an actual prime orbit. The uniform arithmetic or actual-orbit estimate
is still the missing step.

## 7. Exact square normalization and floating replay

For a square `q=r²`, put `h=(r+1)/2` and let `H` be the annihilator of
`Fᵣ×`, so `|H|=h` and its indices are multiples of `r−1`.
The identity `s=1` on `Fᵣ×\{1}` gives

\[
 K\mathbf1_H=\mathbf1_H-\frac hn\mathbf1.
\]

Here `K₀₀=−1/n`. Comparing a row sum on `H` with the entry cap shows
that **every off-diagonal entry of `K_{HH}` equals `1/m₀`**: their capped
sum `(h−1)/m₀−1/n` is exactly `1−h/n`. Thus this also proves the constants
without a numerical Fourier transform.

For the shell `S=H\{0}`, `m=(r−1)/2`, the exact unit-flat quantities are

\[
 \frac{|S|}{m_0}=\frac r{r+1},\qquad
 \langle u_S,Ku_S\rangle
 =\frac{r^2-3r-2}{r^2-1},\qquad
 d^{\rm rect}(S,S)=\frac{2(r+1)}{r(r-1)}.
 \tag{18}
\]

These are exact rational formulas, independently of any assertion that
the actual increments lie on the shell. The actual replay tests that
assertion separately.

[The replay script](parallel-transport-27.py) starts exactly from the
source-generated `D₀=K√c`, evolves `Dₜ₊₁=K(dₜDₜ)`, and accumulates `Vₜ`
without subtracting nearly equal late FFT outputs. It checks (3), (5),
(8), and (11) at its checkpoints, including the trimming constants. A
fresh direct evaluation of (2) measures recurrence drift at each checkpoint.
Integer sign counts, exact symmetry, and the rational `K₀₀`, row energy,
and `m₀²` are recorded separately. No FFT output is an interval enclosure.

Changing `K` to `−K` gives exactly `Vₜ↦−Vₜ`, `Dₜ↦−Dₜ`, `dₜ↦−dₜ`, so
all squared losses, core magnitudes, and signed transport pairings are
identical. The primary runs use the plus sign; this exact conjugacy
accounts for the complementary sign rather than treating it as another
independent sample.

The [primary records](parallel-transport-27-primary.jsonl) use `η=.1` on
three primes `9413,153649,1000033` and two squares `97²,389²`, at floors
`.05,.001`, to depth 260. The [core-cutoff records](parallel-transport-27-core.jsonl)
repeat those same trajectories with `η=.001`. These are different
thresholds on the same underlying paths, not independent samples.
The [return replay](parallel-transport-27-returns.jsonl) includes the new
return-coherence and cardinality-flatness checks, with three transitions
per window. The [narrow-cutoff replay](parallel-transport-27-narrow.jsonl)
uses `τ=.001, η=10⁻⁵` on prime `151337` and squares `97²,389²`, to depth
516. Its much higher threshold can have an empty core; empty layers are
reported without a fabricated rectangle or inverse conclusion.

Here `C_full` is the adjacent ℓ¹ product before trimming, `mass` is the
first core's increment energy, `C_core` uses its normalized core, and
`flat error` is the first normalized core's error against its thresholded
flat at height `1/ℓ`. These are floating observations.

| Order | `τ` | Time | `η` | `C_full` | mass | `C_core` | flat layer size | flat error | signed rectangle deficit |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1000033 | .001 | 255 | .1 | 636.953 | .950075 | 605.789 | 253165 | .436185 | .998460 |
| 1000033 | .001 | 255 | .001 | 636.953 | .462241 | 295.189 | 123193 | .436750 | .998464 |
| 97² | .05 | 64 | .001 | 6.04336 | .954465 | .989363 | 48 | .020945 | .0210481 |
| 389² | .05 | 64 | .001 | 6.73449 | .987102 | .997400 | 194 | .006063 | .00516789 |
| 389² | .05 | 255 | .001 | 6.26954 | .988759 | .997412 | 194 | .004863 | .00516789 |
| 389² | .001 | 255 | .00001 | 10.0197 | .979660 | .997375 | 194 | .008499 | .00516789 |
| 389² | .001 | 511 | .00001 | 7.26083 | .978526 | .997436 | 194 | .0000639 | .00516789 |

On the square rows the selected layers are exactly `H\{0}` in the floating
classification, and every rectangle in the corresponding three-transition
window has the shell constants (18), to rounding. The off-diagonal
positivity and rational values of (18) are proved above; identification
of the actual threshold layer with that shell is a floating observation.
At `389², τ=.05`, time 64, the two normalized cores' whole-core uniform
errors are `.0060631,.0059619`, below the cardinality-based bound `.102020`
from (12a). The general ℓ¹-only bound is much less sharp and can be
numerically vacuous at these sizes; it is not advertised as a precise
finite prediction of flatness.

At the million-order prime, `τ=.001`, time 255, the **full actual** signed
transport pairing is `.9963766` and the squared increment retention is
`.9738911`. Yet the core retaining `95.0%` of energy has `C_core≈605.8`.
Its selected flat-to-flat pairing is only `.777844`, with size product
about `505.1 m₀`, so its signed entrywise rectangle deficit is near one.
A near-unit pairing of the original signed vectors is thus very different
from a near-extremal **critical flat rectangle** on these finite actual
paths. At `η=.001`, the higher prime cutoff retains only `46.2%` energy
and still has a broad product near 295.2; the discarded energy must not be
silently removed from (8).

The broad prime half-layers also have strongly mixed signs. In that same
primary prime window, the absolute mean sending and receiving signs on
the first pair of selected layers are `.0012292` and `.0003770`.
Those are observed counting proportions, not a proof of random signs or
an asymptotic distribution. On the square shell both means are exactly
one in the numerical classification. The return lemma gives activation
sign coherence at least `.890714` on the `389²` shell; the measured
coherence is one. It does not supply a return or sign coherence for the
prime layers.

Across the 26 primary, repeated-cutoff, return, and narrow replay audit
records, the maximum checkpoint energy-identity error is `1.12e−15`, and
the maximum directly recomputed recurrence RMS drift is `1.94e−14`
(both rounded upward). All applicable scalar-amplitude, signed-transport,
trimmed-transport, cap-flatness, cardinality-flatness, and return-coherence
checks passed their stated floating tolerances. This verifies algebraic
consistency of the implementation; it does not bound its distance from
the exact orbit by interval arithmetic or prove a uniform prime estimate.

Reproduction, from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-transport-27.py --depth 260 --starts 16 64 128 255 \
  --tau .05 .001 --eta .1 > research/parallel-transport-27-primary.jsonl

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-transport-27.py --depth 260 --starts 64 128 255 \
  --tau .05 .001 --eta .001 > research/parallel-transport-27-core.jsonl

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-transport-27.py --primes 9413 --square-roots 97 389 \
  --tau .05 --depth 260 --starts 64 128 255 --eta .001 \
  > research/parallel-transport-27-returns.jsonl

OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
  research/parallel-transport-27.py --primes 151337 --square-roots 97 389 \
  --tau .001 --depth 516 --starts 128 255 511 --eta .00001 \
  > research/parallel-transport-27-narrow.jsonl
```

The usable new reduction is (5), (8), (11)--(16), with the sharper
cardinality alternative (12a) and return constraint (17). Completing this
transport route requires control of the actual high-core concentration
or broad transport branch, followed by the relevant sign and alternation
reductions before importing the existing arithmetic gap.
