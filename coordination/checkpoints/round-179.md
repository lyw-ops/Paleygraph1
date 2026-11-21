---
---

# Paley synthesis checkpoint after round 179 (resumption)

Written by the Claude Opus 5.5 coordinator when the search resumed after the user's pause, from `coordination/round-179.json` (the paused version is kept at `coordination/round-179-hold.json`). This is an agent assessment, not human acceptance or certification of the mathematics.

## Question examined

What did Round 179 change in the search for the ordinary Lovász theta limit $\vartheta(\overline H)/\sqrt n\to1$ for prime Paley localizations, and which calls are worth making on resumption? **The target remains open.** No new mathematics has been accepted since Round 179. The proof plan is unchanged; the reassessment only selects the next tests.

## What we learned

- **Ordinary positive completion (weakened).** Proved: the exact two-copy product chart and a weighted affine triple moment bound the whole actual diagonal $\sum_s w(s)P_s^2$ by $O(p^{9/4})$, improving the Round 178 exponent by $73/1600$. Proved: the paired maps preserve $J=d(k+d-1)/k$; each single $J$ class costs $O(p^2)$, or $O(p^{2-1/640})$ for $J\ne0$. These per-class bounds do not sum to the target. Proved limitation: the completed triple moment has lower bound $(p-1)G^6/p^2$, so the completion step itself cannot reach $O(p^{3/2})$ when $G\asymp\sqrt p$.
- **Cold common domain (weakened by a new obstruction).** Proved, with an ineffective constant from fixed-height compact transfer: the normalized $\|R_{611}\|_{2,n}$ has positive liminf uniformly on the original closed square. Therefore no prime-uniform fixed unnormalized counting threshold, such as $0.0556556$, can supply the finite prefix.
- **Negative result.** Young's inequality at exponent $6/5$ plus row-norm interpolation reproduces the Round 178 slope-product scale with no gain.
- **Process.** All three gateway calls returned HTTP 403. The results came from native agents and were independently audited.

## What resists

- **Ordinary:** the sufficient whole diagonal $O(p^{3/2})$ with both $D,D'$ amplitudes and $w$ retained (current $O(p^{9/4})$); separately the one-match and zero-match estimates.
- **Cold:** the Round 173 finite-prefix confinement. The rows $V_{602},\dots,V_{602+k_n}$ must stay in radius-$0.025$ coordinate disks with fixed clearance, where $k_n=\lceil(4/7)\log_2 n\rceil$. After that, derivative transfer remains.
- **Shared candidates:** none recorded. The diagonal and the slope-product energy are different sub-obligations of the ordinary route. The comparison is in `coordination/drafts/round-180-dependency-assessment.json`.

## Proposed next step

**First mission: `ordinary-prime-paired-J-fibers`.** Sort the genuine paired maps by $J$ with $D,D',w$ retained through the sort, price $J=0$ alone, and seek a summed bound below the completed triple moment.

- If supported, the sufficient diagonal is proved, or a power saving below $9/4$ is accepted.
- If refuted, a lower bound $\gg p^{3/2}$ on the summed classes retires this diagonal as the sufficient criterion.
- If inconclusive, we get the exact remaining $J$ range and the quantity to estimate.

**Queued:**

- `cold-prime-signed-growing-prefix`: the finite-prefix test in coordinate sup norm, using signed increments or a moving predictor.
- `ordinary-prime-mixed-row-slope-product`: a gain in $\sum_\xi W_\xi^{3/2}$ from the actual row structure.

**Set aside:**

- Fixed-height counting thresholds for the cold route (refuted in Round 179).
- Interpolation-only slope-product bounds (no gain in Round 179).
- Further improvements to the completed triple moment (bounded below at $G^6/p$ scale).

**Reading path**

1. `research/round-179-acceptance.json` (`proof_scope`, `failed_paths_and_open_bounds`)
2. `research/ordinary-affine-triple-diagonal-179.md`
3. `research/cold-fixed-counting-source-obstruction-179.md`
4. `research/cold-logarithmic-finite-tube-173.md`
5. `research/ordinary-weighted-slope-product-incidence-178.md`
