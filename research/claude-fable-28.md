# Position-space form of the stationary pair, an ℓ∞–ℓ1 transfer, and one flagged tension

Round 28, Fable 5.2 independent line, 2026-11-18. Ordinary theta / ETH Problem 26.

**Status: Problem 26 is not solved here and nothing below should be read as a proof of it.**
Main's acceptance review retained A1–A3 and replayed all 220 diagnostic records.
It corrected the support-radius, finite-depth-envelope and equivalence claims in C/E below;
the detailed [independent audit](parallel-integrability-28.md) explains these limitations.
This file separates (A) statements proved in this note, (B) floating-point diagnostics, (C) an
order-of-limits finding about sup-norm criteria that needs Main's audit (no prior draft is shown
wrong; one sufficient criterion's hypothesis is argued, conditionally, to be unattainable at
primes), and (D) what failed.
Replay: `research/claude-fable-28-check.py` (floating point), output
`research/claude-fable-28-check.jsonl` (220 records). Command:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 .venv/bin/python -B \
        research/claude-fable-28-check.py > research/claude-fable-28-check.jsonl

The `identities` section checks Propositions 1–3 by direct `O(n^2)` convolution at `p = 101, 401`
and `q = 11^2, 19^2`: all residuals are below `2e-12`, inequality (4) and bound (6) hold at seven
trial points per case. Only the three files with this prefix were written.

## 0. Conventions

`Q` is the group of nonzero squares of `F_q`, `n=|Q|`, `s(x)=chi(1-x)` on `Q` (`s(1)=0`),
`D_± = {x in Q : s(x)=±1}`; both are closed under `x -> 1/x` because `q = 1 mod 4`.
`eta_k` are the characters of `Q`, `hat f(k) = sum_x f(x) eta_k(x)` (unnormalized),
`K = F diag(s) F^{-1}`, so `K = K^T`, `K^2 = I - J`, `K 1 = 0`.
`w_0 = 1`, `w_k = tau/n` (`k != 0`), `W = sum w = 1 + tau(n-1)/n`, `m = sqrt(W/n)`.
`Phi(v)_k = sqrt(v_k^2 + 4 w_k)`, `v* = K Phi(v*)` the exact stationary point, `Phi* = Phi(v*)`,
`u_± = (Phi* ± v*)/2`. All vectors are real and even.

Define the **positional witnesses** and their off-identity parts

    f_±(x) = (1/(n m)) sum_k u_±(k) conj(eta_k(x)),      phi_± = f_± - delta_1 .

So `u_± = m hat f_±`. Put `A = sum_x phi_+(x)`, `B = sum_x phi_-(x)`.

## A. Proved statements

### A1. Exact position-space form of the stationary equations

**Proposition 1.** With `gamma = (1 - tau/n)/W` (so `1 - gamma = tau/W`):

1. `f_±(1) = 1`, `f_+ = 0` on `D_-`, `f_- = 0` on `D_+`; `hat f_± > 0` pointwise.
2. (factorization) under multiplicative convolution on `Q`,

       f_+ * f_- = gamma * 1_Q + (1 - gamma) delta_1 .                         (1)

3. `(1+A)(1+B) = n/W`.
4. (quadratic positional equation) for every `x != 1`,

       phi_+(x) + phi_-(x) + (phi_+ * phi_-)(x) = gamma ,                      (2)

   i.e. `phi_+ = gamma - phi_+ * phi_-` on `D_+` and `phi_- = gamma - phi_+ * phi_-` on `D_-`.
5. (inverse) `f_+` is convolution-invertible and

       f_+^{-1} = ( f_- - gamma/(1+A) ) / (1 - gamma) .                          (3)

   In particular **`f_+^{-1}` is constant, equal to `-gamma/((1-gamma)(1+A))`, on `D_+`**, and
   symmetrically `f_-^{-1}` is constant on `D_-`.

*Proof.* Pairing `v* = K Phi*` with `v*` and using `K^2 = I-J` gives `mean(Phi*) = 2m`. Hence
`K v* = Phi* - 2m 1`, and adding/subtracting, `K u_+ = u_+ - m 1`, `K u_- = -u_- + m 1`.
In position space `K` is multiplication by `s`, so `s F^{-1}u_+ = F^{-1}u_+ - m delta_1`:
evaluating at `x=1` (`s=0`) gives `f_+(1)=1`, and at `x in D_-` gives `f_+(x) = 0`. Same for `f_-`.
For (1): `hat f_+ hat f_- = u_+ u_- / m^2 = n w / W`, whose inverse transform is
`(1/W)[(1 - tau/n) 1 + tau delta_1]`. Item 3 is (1) at frequency `0`. Item 4 is (1) expanded with
`f_± = delta_1 + phi_±`; at `x=1` the convolution term vanishes because the supports are disjoint and
inversion-closed. For (3) convolve `f_+` with `f_- - c 1`: by (1) the result is
`(1-gamma) delta_1 + (gamma - c(1+A)) 1`, which is `(1-gamma) delta_1` iff `c = gamma/(1+A)`. ∎

Remarks. (i) (1)–(3) are the Cayley/circulant form of the log-det central path of the theta SDP:
`M_+ = [f_+(a/b)]` is positive definite with the zero pattern of the edges of the complement, and
`M_+^{-1}` is, modulo the all-ones matrix, supported on the complementary pattern.
Equivalently `hat f_+ / mean` is the weighted analytic centre maximizing
`sum_k w_k log U_k` over `{U >= 0, U in 1 + V_+}` (stationarity is `w/U in R1 + V_-`).
(ii) Squares satisfy (1)–(3) too. Nothing in A1 is prime-specific.
(iii) Because `<hat f_+, hat g> = n` for every feasible `g` on the opposite side, all first-order
variational comparisons inside the feasible set (translates, convolution with any probability
measure, Schur powers `f_+^j`) are *identities*, not inequalities; see D2.

### A2. A discrepancy inequality with the stationary pairing isolated

For any real `v` put `r = v - K Phi(v)` and hyperbolic coordinates
`(Phi(v) ± v)/2 = sqrt(w) e^{± g}`, and `g*` likewise for `v*`.

**Proposition 2.**

    sum_k w_k ( cosh(g_k - g*_k) - 1 )  <=  <r, v - v*>/4 - |r|^2/8 .            (4)

*Proof.* Let `p_± = (Phi(v) ± K Phi(v))/2 = (Phi(v) ± v)/2 ∓ r/2`, `c = mean Phi(v)`.
Then `p_± - (c/2)1 in V_±` and `u_∓ - m 1 in V_∓`, so `<p_+,u_-> = <p_-,u_+> = n c m/2`.
Adding, `2 sum_k w_k cosh(g_k-g*_k) = n c m - <r,v*>/2`. From `|K Phi|^2 = |Phi|^2 - n c^2`
and `K Phi = v - r`: `n c^2 = 4W + 2<v,r> - |r|^2`, so
`n c m = sqrt(W) sqrt(4W + 2<v,r> - |r|^2) <= 2W + <v,r>/2 - |r|^2/4`. ∎

This is the same mechanism as Chen et al. Prop. 4.3 used in `iteration-parity.md`; it is restated
only to isolate the single term `<r, v*>` that involves the unknown stationary point. In particular
the mark obeys `cosh(g_0 - g*_0) - 1 <= <r, v - v*>/4`, and
`|log(theta_+/sqrt n) - g*_0| <= (1/2) log W`.

### A3. Position-space transfer: ℓ∞ on the residual, ℓ1 on the stationary witness

For real even `r` let `R(x) = sum_k r_k eta_k(x)` and `rho(r) = max_{x != 1} |R(x)|`.

**Proposition 3 (exact identity and bound).** For every real even mean-zero `r`,

    <r, v*> = m sum_{x != 1} ( phi_+(x) - phi_-(x) ) R(x) ,                      (5)
    |<r, v*>| <= rho(r) * m ( |phi_+|_1 + |phi_-|_1 ) .                          (6)

If `r = v - K Phi(v)` then `R(x) = hat v(x) - s(x) hat{Phi(v)}(x)`; for a Picard step
`v = v_T`, `r_T = v_T - v_{T+1}`, this is `R_T(x) = s(x) ( G_{T-1}(x) - G_T(x) )` with
`G_T = hat{Phi(v_T)}`, so `rho(r_T) = max_{x != 1} |G_T(x) - G_{T-1}(x)|`.

*Proof.* `v*_k = u_+(k) - u_-(k) = m sum_x (f_+ - f_-)(x) eta_k(x)`; exchange sums; the `x=1` term
vanishes because `f_+(1) = f_-(1)`. ∎

**Corollary 4.** If `phi_± >= 0` pointwise then `m(|phi_+|_1 + |phi_-|_1) = Phi*_0 - 2m <= Phi*_0`,
and `Phi*_0 = 2 cosh g*_0 <= 2 sqrt(q W / n)` by the point cap. In general

    m(|phi_+|_1 + |phi_-|_1) = Phi*_0 - 2m + 2 m N ,   N = sum_{x != 1} (phi_+ + phi_-)^-(x)   (7)

(the supports are disjoint), so the constant in (6) is governed by the **negative positional mass** `N`.

Combining (4) and (6): for every trial `v`,

    cosh(g_0 - g*_0) - 1 <= (1/4) [ |r| |v| + rho(r) (Phi*_0 + 2 m N) ] .         (8)

What is new relative to the ℓ2–ℓ2 bound `|<r,v*>| <= |r| |v*|`: the stationary factor is the ℓ1 norm
in *position* space, which is weaker than a bounded stationary ℓ2 norm
(`|phi|_1 <= sqrt(n) |phi|_2`) and — unlike the ℓ2 norm — **stays bounded in every square-order run
below**. The price is the positional sup norm `rho(r)` of the residual. On squares the entire failure
is in `rho`: it stalls on the subfield `F_r^* subset Q`, see B2.

## B. Floating-point diagnostics (not certificates)

All runs use the exact Picard recurrence to residual `< 1e-13`; `tau = 0.05` unless stated.

### B1. Sign and ℓ1 mass of the stationary positional witnesses

| order | tau | `|v*|_2` | `v*_0` | fraction of `x in D_+` with `f_+<0` | `(sum_{D+} |f_+|)/sqrt n` | `(sum_{D+} f_+)/sqrt n` | `sum_{D+} f_+^2` |
|---|---|---|---|---|---|---|---|
| 401 | .05 | 2.1345 | -0.0298 | 0 | 0.8909 | 0.8909 | 2.156 |
| 1997 | .05 | 2.2225 | -0.0046 | 0.028 | 0.9534 | 0.9420 | 2.309 |
| 9413 | .05 | 2.2927 | 0.0008 | 0.037 | 0.9770 | 0.9617 | 2.486 |
| 9413 | .01 | 2.3407 | 0.0008 | 0.053 | 1.0054 | 0.9809 | 2.697 |
| 37253 | .05 | 2.2980 | -0.0007 | 0.043 | 0.9866 | 0.9682 | 2.511 |
| 37253 | .01 | 2.3421 | -0.0008 | 0.051 | 1.0151 | 0.9873 | 2.710 |
| 19^2 | .05 | 3.9697 | 0.5513 | 0 | 1.2069 | 1.2069 | 14.03 |
| 43^2 | .05 | 6.0234 | 0.6093 | 0 | 1.2847 | 1.2847 | 33.52 |
| 97^2 | .05 | 9.1229 | 0.6350 | 0 | 1.3192 | 1.3192 | 78.18 |

The minus side behaves the same way at primes (negative fraction 0.036–0.056, ℓ1/sum ratio 1.016–1.027);
at the four squares tested (`19^2, 43^2, 97^2, 193^2`) `f_- > 0` on `D_-` as well. So:

* **Pointwise positivity of `f_±` is false at primes** (first failure seen at `p=401, tau=.01`);
  a "Schrijver-type" positivity shortcut to Corollary 4 is not available.
* `m(|phi_+|_1+|phi_-|_1)` is `2.0023` (`p=9413`), `2.0283` (`p=153649`), `2.0685` (`97^2`),
  `2.0865` (`193^2`), against `Phi*_0 = 2.000, 2.000, 2.098, 2.102`. The positional ℓ1 mass is
  bounded in all runs, including the squares where `|v*|_2` grows like `n^{1/4}`.

### B2. The pairing bound (6) along actual Picard prefixes

`bound1 = rho(r_T) m(|phi_+|_1+|phi_-|_1)`, `bound2 = |r_T| |v*|`.

| order | T | `|r_T|_2` | `rho(r_T)` | `<r_T,v*>` | bound1 | bound2 |
|---|---|---|---|---|---|---|
| 153649 | 8 | 3.81e-1 | 1.52 | -2.67e-2 | 3.08 | 0.879 |
| 153649 | 32 | 3.88e-2 | 1.79e-1 | -2.37e-4 | 3.63e-1 | 8.95e-2 |
| 153649 | 128 | 4.95e-6 | 2.03e-5 | 6.4e-10 | 4.12e-5 | 1.14e-5 |
| 193^2 | 8 | 3.90e-1 | 1.75 | -0.719 | 3.65 | 5.02 |
| 193^2 | 32 | 6.54e-2 | 6.48e-1 | -0.694 | 1.35 | 0.842 |
| 193^2 | 128 | 4.61e-2 | 4.65e-1 | -0.583 | 0.970 | 0.593 |

At the two primes `rho(r_T)/|r_T|_2` stays between 2.4 and 5.2 for `T` up to 128, i.e. `R_T` is flat
in position up to an extreme-value factor. At the squares `rho(r_T)` stops decaying
(`0.65 -> 0.53 -> 0.46` for `T = 32, 64, 128` at `193^2`) while `<r_T,v*>` stays near `-0.6`;
bound (6) is within a factor two of the truth there. In the replay the maximizing `x` lies in the
subfield `F_r^*` for every `T >= 8` at both squares, and for `T >= 32` `R_T` is nearly constant on it
(`min |R_T| = 0.385, 0.493, 0.436` against mean `-0.535, -0.510, -0.450` at `193^2`, `T = 32, 64, 128`)
while `max |R_T|` off the subfield is `0.143, 0.028, 0.022`.

Caveat on scope: for a *prime-uniform* use of (8) one would need both
(I) `N = O(sqrt n)` at fixed `tau` (equivalently `|phi_±|_1 = O(sqrt n)`), and
(II) `rho(r_T) -> 0` in the relevant order of limits. Neither is proved. An extreme-value loss
`rho ~ |r| sqrt(log n)` is expected at primes, and Section C argues that a field-first reading of
(II) is not attainable. This is a conditional transfer, not a convergence proof, and at primes it is
not stronger than the existing frequency-side ℓ∞–ℓ1 criterion (see C).

## C. Order of limits for sup-norm criteria (needs Main's audit; no prior draft is shown wrong)

**Summary (conditional).** A field-first frequency sup-norm criterion could fail to separate primes
from squares if the stronger arithmetic matching premise (a') below holds. A limiting law can
give a lower bound on extreme values; it need not determine their maximum, since exceptional
frequencies can affect a maximum without affecting that law. No such arithmetic matching is
proved here. The finite diagnostics show a separation when depth grows at the tested fixed orders;
they do not establish which hypotheses are attainable asymptotically.

Files and assertions involved.

* `research/iteration-parity.md`, section "A criterion involving only the iterates": the sufficient
  condition `lim_T (1/T) limsup_p sqrt(n) max_{k != 0} |z^{(T)}_k| = 0` (averaged iterates).
  The implication is correct. The question is whether its hypothesis can hold at primes.
* `research/ledger.md` rows "Complementary Fourier smoothing" ("sublinear growth of the extreme
  scaled bulk entries of averaged iterates would close the analytic limit") and "Explicit signed LP
  majorants" ("Bound the prime-order top sums after the field-first limit").
* `research/square-order-control.md`: at squares `liminf sqrt(n) max_k |z^{(T)}_k| >= c T`.
* `research/uniform-fixed-depth.md`, last section: at fixed depth each scaled cost is uniformly close,
  off boundedly many characters, to a class function on a compact group, and "a positive fraction of
  the frequency rows" lies within `epsilon` of its maximum "for all large `q`". That section uses this
  to transfer the square obstruction between the two *signs* at the same field.

What I add.

1. *Square subfield values are bulk values.* Assume the sup-norm approximation of
   `uniform-fixed-depth.md`. At squares the pairing `<z^{(T)}, v*> >= T c^2 - o(1)` cannot be carried
   by `O(1)` frequencies (each contributes `O(B_T n^{-1/2})`) nor by frequencies with
   `sqrt(n)|z_T| < theta_0 = T c^2/(4 sqrt W)` (total at most `T c^2/2` since `|v*|_1 <= 2 sqrt(nW)`).
   So `>> sqrt(n) T/B_T` good frequencies have class-function value at least `theta_0/2` after the
   ℓ1-bounded exceptional vector is discarded. Hence the class function exceeds `theta_0/4` on a
   nonempty open set, and by the draft's own positive-fraction argument a **positive proportion of
   all frequencies** of the square field have `sqrt(n)|z_T(k)| >= theta_0/4`.
2. *Transfer to primes is conditional on one stated premise:*
   (a') the fixed-expression good-character means (traces of the arithmetic coset on geometric
   invariants) at an infinite set of primes agree in the limit with those at squares.
   Under (a') the same positive proportion occurs at those primes, so
   `limsup_p sqrt(n) max_k |z^{(T)}_k| >= c' T` and the hypothesis of the iterates-only criterion
   **fails at primes for every `tau < 1`**. I have not proved (a'); arithmetic twist values such as
   `chi(2)` can differ between prime classes and squares, so (a') must be checked, not assumed.
3. *Numerical evidence for (a') and for the conclusion* (`tau = .05`, averaged iterates, replay
   section `highset`). `ref_T` is the mean of `sqrt(n) z_T` on the subfield annihilator at `389^2`.

| T | `ref_T` (`389^2`) | max over `k`, `p=153649` | max over `k`, `p=1000033` | fraction `>= ref_T/2`: `389^2` bulk / `p=153649` / `p=1000033` |
|---|---|---|---|---|
| 2 | 2.342 | 2.604 | 2.615 | .3092 / .3121 / .3122 |
| 4 | 3.633 | 4.501 | 4.596 | .2391 / .2432 / .2430 |
| 8 | 5.531 | 5.977 | 6.577 | .1126 / .1160 / .1175 |
| 12 | 7.201 | 6.687 | 7.190 | .0450 / .0484 / .0488 |
| 16 | 8.808 | 6.905 | 7.324 | .0131 / .0155 / .0157 |
| 24 | 11.957 | 7.053 | 7.211 | 5.0e-4 / 3.9e-4 / 5.0e-4 |
| 32 | 15.075 | 7.223 | 7.132 | 0 / 0 / 0 |
| 128 | 51.6 | 7.301 | 7.254 | — |

   Three things are visible. (i) For `T <= 8` the prime maxima already *exceed* the square subfield
   value: the subfield frequencies are not the largest observed fixed-depth values. (ii) The upper-tail
   fractions of the bulk agree between primes and squares to the sampling accuracy at every level
   where they are measurable; decay like `exp(-c T^2)` is a heuristic fit to these few tail fractions.
   (iii) Beyond `T ~ 12` the prime maximum stops at about `7.3` for all `T` up to 128 and moves
   only slowly with `p` (`6.90, 6.44, 7.30, 7.25` at `T=128` for `p = 9413, 37253, 153649, 1000033`),
   which is what an extreme value of `n` samples from a light-tailed law looks like, while the square
   subfield value keeps growing linearly (`51.6` at `T=128`).

Consequences.

* A common limiting law, if proved with the matching in (a'), would give a lower bound for
  `limsup_p sqrt(n) max_k |z^{(T)}_k|` through its support radius. It would not by itself give
  equality or an upper bound for the maximum. Under the additional matching premise, items 1–2
  would obstruct sublinear field-first growth. The premise remains an audit target, so the
  existing sufficient criterion is retained.
* The finite comparisons separate primes from squares as depth increases at the tested fixed orders:
  the maximum through the tested depths is about `7.3` at `n = 5*10^5` (primes), whereas square
  values continue growing. The all-depth supremum `S(n) = sup_T sqrt(n) max_k |z^{(T)}_k|`
  has not been bounded by these computations. A usable hypothesis is `S(n) = o(T(p))` on a horizon `T(p)` on which
  marked cancellation is available — i.e. the growing-depth envelope of `parallel-activation-26.md`,
  with the envelope allowed to depend on `n` like an extreme value (`~ sqrt(log n)` heuristically)
  rather than being `p`-uniform at fixed depth.
* An analogous criticism of residual hypothesis (II) would require a separate transfer argument;
  items 1–2 concern frequency extrema of averaged iterates and do not supply it. In the
  fixed-`n` comparisons the positional and frequency sup norms of `z_T` flatten at primes over the tested depths
  (`5.8/6.9` at `p=9413`, `6.4/7.3` at `p=153649`, `T` up to 256) and both grow linearly at squares
  (replay section `possup`). The frequency version needs only the proved bound
  `|v*|_1 <= 2 sqrt(nW)`; the positional version needs the unproved (I). So Proposition 3 is an
  exact reformulation that locates the square obstruction on the subfield, **not** a stronger
  criterion at primes.

Fixed depth versus uniform in depth, explicitly: everything in items 1–3 is a statement at each
fixed `T` with `q -> infinity`. Nothing here bounds or disproves a bound uniform as depth grows with
`p`; on the contrary the numerics suggest such a bound holds at primes with an `n`-dependent
extreme-value constant.

## D. What failed

1. **Soft proof of (I).** By (2), `|phi|_1 = |gamma - phi_+ * phi_-|_{l1(Q \ 1)}`, and the only
   general bound is Cauchy–Schwarz, which returns the stationary ℓ2 norm. Positive-definiteness,
   `|f| <= 1`, the cap and "the mark is the maximum of `hat f_+`" do not bound the negative mass:
   spectra with many comparable peaks at unstructured locations have `|f|_1 >> sum f`.
2. **Variational/entropy comparisons.** `hat f_+` is the weighted analytic centre. The feasible set is
   closed under translation, under convolution with any probability measure and under Schur powers,
   but every first-order comparison is the sector identity `<hat f_+, hat g> = n`
   (e.g. constancy of the cross-correlation of `hat f_+` and `hat f_-`), and the barrier carries
   total weight `tau`, against weight one on the mark. The duality-gap identity
   `[Psi_+ - L_+(U_+)] + [Psi_- - L_-(U_-)] = W KL(w/W || U_+U_-/n)` for feasible pairs is exact but
   requires exactly positive pairs, which is the original repair problem.
3. **Positivity shortcut.** `f_± >= 0` fails at primes (B1), so `|phi|_1 = sum phi` is not available.

## E. What is proved, what failed, what remains

Proved here (finite-dimensional, field-general, checked numerically): Proposition 1 (position-space
factorization, quadratic equation, inverse constancy), Proposition 2 (discrepancy inequality with the
stationary pairing isolated), Proposition 3 and (7) (exact positional pairing identity and ℓ∞–ℓ1 bound).

Diagnostics only: B1–B2, the tables in C.

Not proved, and flagged rather than asserted: premise (a') and hence the claim that field-first
sup-norm hypotheses fail at primes.

Failed: D1–D3.

Remaining arithmetic hypothesis, in the order of limits that the data support. For fixed `tau`
along a sequence tending to zero, a prime-uniform statement **at growing depth**: an envelope
`sup_{t <= T(p)} sqrt(n) max_k |z^{(t)}_k| = o(T(p))` (frequency form, with the proved
`|v*|_1 <= 2 sqrt(nW)`); alternatively, a sufficient positional hypothesis is `(I)` together with
`sup_{t <= T(p)} max_{x != 1} |hat{z^{(t)}}(x)| = o(T(p))`, on a horizon `T(p) -> infinity` on which
the marked coordinates of the averaged iterates are known to vanish. The square subfield violates
both forms. These are alternative sufficient hypotheses, not equivalent Fourier sup-norm bounds.
The attainability of field-first versions remains open; the conditional concern in C does not
establish their failure at primes.
(I) itself, `sum_{x != 1} (f_+ + f_-)^-(x) = O(sqrt n)`, holds in every run including squares and is
unproved. Problem 26 remains open.
