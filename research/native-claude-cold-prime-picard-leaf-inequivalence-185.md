# Round 185 native Claude draft: cold prime Picard leaf inequivalence

- call_id: `cold-prime-picard-leaf-inequivalence`
- Mission: `coordination/missions/round-185/cold-prime-picard-leaf-inequivalence.md`, exported from coordinator record `coordination/round-184.json` (SHA-256 46fb9ed1…).
- Author: a native Claude research session (Claude Opus 5.5), started by the Round 185 coordinator session. This is an agent draft. It is not an audit, not an acceptance and not a human review.
- Input hashes verified (SHA-256). All eleven match the mission export:
  - round-183-acceptance aae5b4aa…, round-184-acceptance c3066021…, native-claude-audit-184 b074da5e…
  - native-claude-cold-prime-h1-product-rule-184 a45402f0…, paley-184-cold-h1-product-ratio fa25f9bf…, paley-184-cold-h-rest-diagnostic 53dbaec5…, paley-184-audit-cold-check ad19165d…
  - native-claude-cold-prime-seed-multiplier-power-rate-183 90c2eaee…, native-claude-cold-prime-signed-nonseed-price-182 c8023a9b…, shifted-resolvent-96 ec9c2eb7…, cold-first-prefix-step-174 8d28cc54…
- Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-184.md`, audit §3 and §6 of `native-claude-audit-184.md`, `astra-dissipation-80.md` lines 82–112 (the Round 80 leaf-inequivalence argument and transport rule), and the shared notes of the Round 184 cold session.
- Scripts written by this session (all new; none imports or copies an earlier script):
  - `research/paley-185-cold-model.py`: the model layer, as a module. It holds weight data, the line shift, the tensor and transport rules, and the Fourier coefficients as complex balls (python-flint `acb`) containing every value on Q × {p ≥ 10⁶}.
  - `research/paley-185-cold-picard-leaves.py`: exact. It enumerates the Picard pieces, applies the identification criterion, and computes the signed and unsigned prices to depth 3 (linear chain to depth 5). About 4 s.
  - `research/paley-185-cold-tails.py`: exact/outward, except §T3, which is an exact enumeration used only as evidence. It covers the Fourier-truncation terms, the linear tail and the depth-4 nonlinear pieces. About 7 s.
  - `research/paley-185-cold-bruteforce.py`: an independent cross-check with explicit slot lists and FFT Fourier coefficients. Weight data are exact; prices are [float]. About 16 s.
  - `research/paley-185-cold-depth5-evidence.py`: depth-5 nonlinear pieces. [float] evidence. About 25 s.
  - `research/paley-185-cold-physical-gram.py`: physical mean squares and inner products of the pieces. [float] evidence. About 65 s.

## Result summary

**Verdict: route retired.** This is the decision of the mission's "supported" branch. One correction to its premise: **small opposite-sign collisions do exist** (two families, listed in item 3). They move the price by less than 10⁻³ and cannot bring it near the allowance. The depth-3 statement is certified. The full-model statement depends on one uncertified term, N5. Details are at the end.

1. **The linear chain has no collisions at all (Proposition 1; proved in the compact model under (b4), (b-Jk), Round 80 injectivity).**
   - The 55,986 transported simples K(J^{k_j}⋯K(J^{k₁}K(J^{k′}))⋯) of L_S^j h₁, j ≤ 5, |k′| ≤ 6, |k_i| ≤ 5, are pairwise inequivalent.
   - 55,982 of them already have pairwise distinct two-fibre weight data.
   - The remaining 4 pairs (depth 5, dimension 31, same sign) are separated by their pre-transport data (Round 80: K is injective).
   - So no two paths, from the same piece or from different pieces L_S^j h₁, L_S^{j′} h₁, produce the same simple, with either sign.
2. **The nonlinear pieces to depth 3 (Q₁, L_S Q₁, X₁ = K(Φ″h₁·L_S h₁), C₁ = ⅙K(Φ‴h₁³)) never have the full weight data of a linear simple (Proposition 2).**
   - They can share a *constituent* with a linear simple only where a multiset-containment condition holds.
   - The objects for which this is possible with **opposite sign** carry total price ≤ **0.002608** (against the simples of h − h₁) and ≤ **0.001617** (against the roots of h₁).
3. **Opposite-sign collisions that do occur (identified; confirmed physically; evidence (c)).**
   - **Q₁ ⊇ the roots K(J^{±2}) of h₁**, with coefficient −7.58·10⁻⁵ against +0.1218.
   - **C₁ ⊇ the four dim-3 simples K(J^{±1}K(J^{±2})) of L_S h₁**, with coefficient ≈ −1.0·10⁻⁵ against +0.0207.
   - Both come from the trivial constituent of K(J^k)⊗K(J^k) (self-dual roots): a mean-field renormalization of Φ by the variance of h₁.
   - The physical inner products converge to the predictions: ⟨h₁, Q₁⟩ → −1.822·10⁻⁵ (prediction −1.847·10⁻⁵) and ⟨L_S h₁, C₁⟩ → −8.402·10⁻⁷ (prediction −8.374·10⁻⁷).
   - Price effect: ≈ 4·10⁻⁴ on h, ≈ 1.2·10⁻⁴ on h − h₁.
4. **Exact signed model A_𝒳-price to depth 3 (Theorem 3; certified, outward, uniform on Q × {p ≥ 10⁶}, both lifts).**

   | object | certified lower bound | upper bound | allowance |
   |---|---|---|---|
   | (h − h₁)_{≤3} | **0.434571** (0.442593 counting only opposite-sign overlaps) | 0.510376 | 0.3411 |
   | h_{≤3} | **0.912537** (0.935500) | 1.004901 | 0.7499 |

   - The linear part alone is exact: 0.445201–0.445204 for h − h₁ and ≥ 0.939725 for h. Signed equals unsigned, by item 1.
5. **Full model (Corollary 5; certified except one term).**
   - A_𝒳(h − h₁) ≥ 0.416286 − N5 and A_𝒳(h) ≥ 0.904816 − N5.
   - N5 is the opposite-sign overlap mass of the nonlinear pieces of depth ≥ 5 (plus the Fourier-omitted depth-4 nonlinear terms).
   - The route survives in the model only if N5 ≥ 0.0751 for h − h₁ (≥ 0.1549 for h).
   - Evidence that it is not that large:
     - At depth 4 the exact opposite-sign overlap bound is 0.003542. At depth 5 the containment bound is 0.020016 [float], but containment becomes uninformative there (item 6).
     - The only collisions found physically are the mean-field ones of item 3.
     - The physical ⟨L_S^j h₁, Nl⟩/|L_S^j h₁|², j = 1, 2, 3, tend to 0 like n^{−1/2} (−0.0036, −0.0030, −0.0053 at p = 4·10⁶). Cancellation of the needed size would show as about −0.2.
6. **What the compact model cannot decide.**
   - Weight data cannot decide whether a constituent of a deep tensor-product piece is isomorphic to a linear simple.
   - The containment test becomes uninformative with depth: 26% / 39% / 80% of the nonlinear mass at depth 3 / 4 / 5 passes it.
   - The nonlinear unsigned mass per depth does not decay yet: 0.0242, 0.0410, 0.0438, 0.0429 for depths 2–5.
   - That is why N5 is not certified.

## Setup and hypotheses (inherited, as accepted in Rounds 80, 182–184)

- p ≡ 1 (mod 4) prime, n = (p − 1)/2, t ∈ Q (closed square of half-width 2⁻¹⁷ about a = 2031/128), s² = 8 + 8/(p − 1), p ≥ 10⁶, β = s²/(4t). Both lifts.
- Frozen-base fixed point with the mark removed (Rounds 182–183): h = V₆₀₂ − S satisfies
  h = h₁ + L_S h + Σ_{m≥2} K(Φ_t^{(m)}(S)h^m)/m!.
  - h₁ = 2√t Σ_{k′ even ≠ 0} b′_{k′} K(J^{k′}) (Round 183 / 184 definition) and L_S = K(Φ_t′(S)·).
  - Φ_t′(S) = (s/(2√t)) Σ ĝ_k J^k and Φ_t″(S) = (1/(2√t)) Σ b̂_{2i} J^{2i} (Round 183 Lemmas 1, 5, accepted).
  - New (elementary calculus; the coefficients are checked by quadrature in the brute-force script):
    - Φ_t‴(S) = −(3s/(2√t)³) Σ e_c J^c, with e_c the Fourier coefficients of cos θ (1 + β cos²θ)^{−5/2};
    - Φ_t⁽⁴⁾(S) = (3/(2√t)³) Σ f_c J^c, with f = 4(1 + β cos²θ)^{−5/2} − 5(1 + β cos²θ)^{−7/2}.
- **Compact model** (as accepted in Round 184): (b4) the Round 80 transport rule; (b-Jk) the line shift; (b-T) the tensor rule in equality form.
  - (b-T) is used only for the nonlinear pieces. The linear chain needs only (b4) and (b-Jk).
- **Price.** In the model, distinct (inequivalent) simples have linearly independent traces, so every f in the span has well-defined simple coefficients coef_M(f).
  - For any representation f = Σ a_j H_j by terms H_j that are sums of simples with ranks adding, Σ|a_j| r(H_j) ≥ Σ_M dim M · |coef_M(f)|.
  - Hence A(f) and A_𝒳(f) are both ≥ Σ_{M∈𝒮} dim M |coef_M(f)| for every set 𝒮 of simples (the "dual functional" bound), with equality for 𝒮 = all simples (audit §6.3, call 1).
  - Every lower bound below is of this form, so it bounds both A and A_𝒳.
- **Depth.** The depth of a term is (number of transports K in its expression tree) − 1. The graded pieces are:
  - h^(0) = h₁;
  - h^(1) = L_S h₁;
  - h^(2) = L_S² h₁ + Q₁, with Q₁ = ½K(Φ″h₁²);
  - h^(3) = L_S³ h₁ + L_S Q₁ + X₁ + C₁, with X₁ = K(Φ″h₁·L_S h₁) and C₁ = ⅙K(Φ‴h₁³).
  - "To depth 3" means the truncation Σ_{d≤3} h^(d). It contains every piece the mission names up to L_S³ h₁ and L_S Q₁.
- **Ranges kept exactly:** |k′| ≤ 6, |k| ≤ 5 (seed), |2i| ≤ 6 (b̂), |c| ≤ 5 (e_c). Everything else is bounded in §6 (T1).
- **Uniformity.** Every coefficient is computed as an `acb` ball containing all its values on Q × {p ≥ 10⁶}: t ∈ a + [−2⁻¹⁷, 2⁻¹⁷](1 + i) and s² ∈ [8, 8 + 8/(10⁶ − 1)]. The series tails are added as rigorous radii.
  - Lower bounds use the lower end of |·| of these balls, so they are uniform on the region.
  - Every coefficient real part has a determined sign (no ball meets 0), so "same sign / opposite sign" below is rigorous.
- **Both lifts (Lemma 0, proved).**
  - Fibre exchange maps J^k ↦ J^{−k} and K(J^k) ↦ K(J^{−k}).
  - The coefficients satisfy ĝ_{−k} = ĝ_k, b′_{−k} = b′_k, b̂_{−2i} = b̂_{2i} and e_{−c} = e_c.
  - So the expansion is mapped to itself, path p ↦ −p, with equal coefficients. Exchanging the pairing in a tensor product amounts to replacing a factor by its mirror (Round 184 lift remark).
  - Checked: W(−p) is the fibre exchange of W(p) for all 55,986 paths, and c(−p) = c(p).
  - So every price below is the same for both lifts.

## 1. The identification criterion

Let O, O′ be model objects with two-fibre weight data W(O), W(O′).

- **(C1) Invariant.** If W(O) ≠ W(O′), then O ≇ O′.
  - The fibre weights are local invariants of the object, so they are isomorphism invariants. In the compact model this is part of the definition of the weight data; under (b4), (b-Jk), (b-T) the computed data are the data of the object.
- **(C2) Peeling (Round 80).** For non-punctual simples, K(J^a X) ≅ K(J^b Y) ⇔ J^a X ≅ J^b Y ⇔ X ≅ J^{b−a} Y.
  - This is the injectivity of transport and of line multiplication, used in `astra-dissipation-80.md` line 108.
  - Consequences:
    - Equal pre-transport data are necessary.
    - If the last steps agree (a = b), recurse on the parents.
    - If a ≠ b, compare W(X) with the shift of W(Y) by b − a: if these differ, (C1) separates the pair.
    - A pair with X ≅ J^c Y, c ≠ 0 and equal shifted data cannot be peeled further; it is declared "possibly equal".
  - Possibly-equal pairs are merged into blocks (connected components). Merging can only lower Σ_B dim_B |Σ_{p∈B} c_p|. So the block price is a certified *lower* bound whenever each path object is one simple, which holds for the linear chain (Round 80 line 104: line multiplication preserves geometric simplicity, and transport of a non-punctual simple is simple).
- **(C3) Constituents of nonlinear objects.** A nonlinear object N = K(P_N), with P_N = J^c ⊗ F₁ ⊗ ⋯ ⊗ F_m (m ≥ 2), may be reducible. A linear simple M = K(P_M) can occur as a constituent of N only if W(P_M) ⊆ W(P_N) as multisets at both fibres. The reasons:
  - K is additive and injective on non-punctual simples;
  - P_N is semisimple (purity);
  - the weight data of a direct sum are the union of the data of the summands.
  - Call such N **touching** M. The sign of a constituent's coefficient is the sign of c_N, because multiplicities are positive.

(C1)–(C2) are what the mission calls "Round 80 inequivalence extended to J^odd multipliers on roots K(J^{2i})". In this form they are proved model statements: they need only the invariance of weight data and the Round 80 injectivity. They are applied by a finite exact computation, not by a general theorem for all depths.

(C3) is only a *necessary* condition. When it fails, a collision is excluded. When it holds, the model cannot decide, and §§4–6 treat that case conservatively (by subtraction).

## 2. The linear chain: no collisions (Proposition 1)

**Proposition 1** (proved; compact model under (b4), (b-Jk); (C1), (C2); `…-picard-leaves.py` §§1–2; independently `…-bruteforce.py` (1)–(2)).
- The 55,986 objects O(p), p = (k′; k₁, …, k_j), 0 ≤ j ≤ 5, |k′| ∈ {2, 4, 6}, |k_i| ∈ {1, 3, 5}, are valid simples (refill ≥ 0, Σ|w| = 2r) and pairwise inequivalent.
  - 55,982 have pairwise distinct weight data, so (C1) suffices for them.
  - In the 4 remaining pairs the pre-transport data differ (dimension 24 against 22), so (C2) separates them:
    - (2,1,3,1,−1,1) vs (4,1,1,1,−1,1);
    - (2,−1,3,−1,−1,−1) vs (4,−1,1,−1,−1,−1);
    - and the two mirrors.
  - Both members of each of these pairs have the same sign anyway.
  - No pair was left undecided.
- Consequently, for the linear part of h, the signed price equals the unsigned price, depth by depth and across depths:

| depth j | paths | P(L_S^j h₁) = A_𝒳 (certified, uniform) | Round 184 (upper) |
|---|---|---|---|
| 0 | 6 | [0.494524, 0.494526] | 0.494530 |
| 1 | 36 | [0.260137, 0.260139] | 0.2602 |
| 2 | 216 | [0.122824, 0.122825] | 0.1229 |
| 3 | 1296 | [0.062239, 0.062241] | 0.0623 |
| 4 | 7776 | [0.030629, 0.030630] | 0.0307 |
| 5 | 46656 | [0.015369, 0.015370] | 0.0154 |

- Sums: depths 1–3: [0.445201, 0.445204]; depths 1–5: [0.491200, 0.491204]; with h₁: ≥ 0.939725 (0–3) and [0.985724, 0.985729] (0–5).
- Remarks:
  - Along every path the dimension increases strictly (checked to depth 5). A depth-j simple has dimension ≥ j + 2.
  - Most of the price is in few simples. The four dim-3 simples K(J^{±1}K(J^{±2})) carry 0.248 of the depth-1 price 0.260, and simples with |c|/dim ≥ 3·10⁻³ carry 0.248 of the depth-1–3 price 0.445.

## 3. The nonlinear pieces to depth 3 (Proposition 2)

`…-picard-leaves.py` §§4, 6. The objects are merged over permutations of the tensor factors. All of them are valid, i.e. Lemma B1 holds on these explicit objects.

| piece | objects | unsigned price (certified) | could contain a root (h₁) | could contain a linear simple of depth 1–3 |
|---|---|---|---|---|
| Q₁ = ½K(Φ″h₁²) | 147 | 0.024199 | 81 objects, ≤ 0.016557 | none |
| L_S Q₁ | 882 | 0.013503 | none | 594, ≤ 0.008871 |
| X₁ = K(Φ″h₁ L_S h₁) | 1512 | 0.026803 | 576, ≤ 2·10⁻⁶ | 604, ≤ 0.001091 |
| C₁ = ⅙K(Φ‴h₁³) | 336 | 0.000669 | none | 336 (all), ≤ 0.000669 |
| total | 2877 | **0.065172** | | |

**Proposition 2** (proved; compact model under (b4), (b-Jk), (b-T); (C1)–(C3); purity of P_N).
- (i) No nonlinear object of depth ≤ 3 has the full weight data of any linear simple of depth ≤ 5. So no such object *is* a linear simple.
- (ii) Six classes of nonlinear objects share full weight data among themselves, all with equal signs. If all of them were identified, the loss would be 0.
- (iii) The nonlinear objects that could contain a linear simple of **opposite sign** carry price:
  - ≤ **0.002608** for linear simples of depth 1–3 (1058 objects; the same 0.002608 for depth 1–5);
  - ≤ **0.001617** for roots of h₁ (337 objects).
  - Those touching only same-sign simples carry ≤ 0.008022 and ≤ 0.014942 respectively. They cannot lower the price: |Re(c_M + δ)| ≥ |Re c_M|.

## 4. The signed model price to depth 3 (Theorem 3)

**Theorem 3** (certified; compact model under (b4), (b-Jk), (b-T), (C1)–(C3), purity; outward balls; uniform on Q × {p ≥ 10⁶}; both lifts).

- **Lower bounds** (dual functional on the linear simples of the truncation):
  - A_𝒳((h − h₁)_{≤3}) ≥ 0.445201 − 0.010630 = **0.434571**.
    - Subtracting only the opposite-sign overlaps, and pricing by |Re c|: ≥ 0.445201 − 0.002608 = **0.442593**.
  - A_𝒳(h_{≤3}) ≥ 0.939725 − 0.027188 = **0.912537**. Opposite-sign only: ≥ **0.935500**.
- **Upper bounds:** A_𝒳 is at most the unsigned path sum: ≤ 0.445204 + 0.065172 = **0.510376** and ≤ 1.004901.
  - If every nonlinear object is a single simple distinct from the linear ones, the truncation's price is exactly 0.510376 (h − h₁) and 1.004901 (h). The physical mean squares of §7 support this up to the small mean-field overlaps.
- **Against the certified allowances:**
  - A_𝒳(h − h₁) < 0.3411 (joint L_S + B₁, Duhamel; Round 184 Prop. C): the depth-3 model price exceeds it by ≥ 0.0934.
  - A_𝒳(h) < 0.7499 (seed only): exceeded by ≥ 0.1626.

The mission's estimate "model A_𝒳(h − h₁) ≥ 0.50" is the *upper* end. The certified lower end at depth 3 is 0.434571.

## 5. Opposite-sign collisions: the list asked for in the inconclusive branch

The objects that could carry an opposite-sign overlap at depth ≤ 3 are listed by the script (§6). The ones that actually collide, according to the physical test of §7, are these:

| nonlinear object | coefficient | linear simple contained | its coefficient | mechanism |
|---|---|---|---|---|
| K(J^{±2} ⊗ K(J^k) ⊗ K(J^k)), k = ±2 (and ±4, ±6, negligible) | −3.79·10⁻⁵ each (two per root) | root K(J^{±2}) of h₁ | +0.1218 | K(J^k)⊗K(J^k) ⊇ 1, so J^{±2}⊗(⋯) ⊇ J^{±2} |
| K(J^c ⊗ K(J^k)^{⊗3}) and K(J^c ⊗ K(J^{k′})^{⊗2} ⊗ K(J^k)), k, k′ = ±2, c = ±1 | −2.0·10⁻⁶ (×2 multiplicity) and −2.0·10⁻⁶ (×3 orderings) | K(J^c K(J^k)), the dim-3 simples of L_S h₁ | +0.0207 | X^{⊗3} ⊇ 2X and X⊗X⊗Y ⊇ Y, both from X⊗X ⊇ 1 |

These are **mean-field renormalizations**:
- The trivial constituent of h₁ ⊗ h₁ is the constant E|h₁|² = Σ_k c_k² ≈ 0.0297.
- Through the Taylor terms it replaces Φ by its Gaussian smoothing.
- The relative changes of the coefficients are −6.2·10⁻⁴ (roots K(J^{±2})) and −4.9·10⁻⁴ (dim-3 simples).
- Price effect: about 1.2·10⁻⁴ on A(h − h₁) (4 simples × dim 3 × 1.0·10⁻⁵), and about 4·10⁻⁴ on A(h) (of which 3.0·10⁻⁴ comes from the two roots: 2 × dim 2 × 7.58·10⁻⁵). Both are inside the certified subtractions of Theorem 3.

## 6. Beyond depth 3 (Proposition 4, Corollary 5; `…-tails.py`)

**Proposition 4** (certified).

(T1) **Fourier-truncation terms omitted from the enumeration** (unsigned, uniform).
- The per-simple bound is dim K(J^c ⊗ F₁ ⊗ ⋯ ⊗ F_m) ≤ (m + |c|) Π dim F_i (Round 184 Prop. A).
- Inputs:
  - P(h₁) over all k′ ≤ 0.494552; the omitted roots |k′| ≥ 8 contribute ≤ 2.71·10⁻⁵;
  - omitted seed lines |k| ≥ 7: per-step ratio τ ≤ 3.031·10⁻⁵ (Round 184's τ_S ≤ 3.861·10⁻⁴ used a coarser tail).
- Omitted linear paths at depth j = 0…5: ≤ 2.71, 3.40, 3.43, 3.13, 2.71, 2.25 (·10⁻⁵).
- Omitted nonlinear terms at depth ≤ 3: ≤ 1.954·10⁻⁵.

(T2) **Linear depth ≥ 6.**
- The Round 184 value g_S = Σ_m G_m(L_S) ≤ 2.467879 (Prop. B/C, accepted) and the Prop. C word expansion with the omitted lines give Σ_{m≥1}‖L_{S,full}^m‖ ≤ 1.468064.
- With P(L_S⁵ h₁) ≤ 0.015393, this gives **Σ_{j≥6} P(L_S^j h₁) ≤ 0.022598**.
- The linear simples of depth 4 and 5 are pairwise inequivalent to every depth-≤3 simple (Proposition 1), so they contribute nothing to those coordinates.

(T3) **Nonlinear depth 4** (exact enumeration, 41,706 objects).

| piece | unsigned price |
|---|---|
| L_S(L_S Q₁ + X₁ + C₁) | 0.020969 |
| K(Φ″h₁ L_S²h₁) | 0.012519 |
| K(Φ″h₁ Q₁) | 0.002506 |
| ½K(Φ″(L_S h₁)²) | 0.006755 |
| ½K(Φ‴h₁² L_S h₁) | 0.001012 |
| (1/24)K(Φ⁽⁴⁾h₁⁴) | 0.000037 |
| total | **0.043795** |

- Objects that could contain a depth-1–3 linear simple carry ≤ 0.017102.
- With opposite sign: ≤ **0.003542**. With an opposite-sign root: ≤ 0.004351.

**Corollary 5** (certified except for N5; dual functional on the depth-1–3 linear simples).
- A_𝒳(h − h₁) ≥ 0.445201 − 0.002608 − 0.003542 − 0.022598 − 1.685·10⁻⁴ = **0.416286 − N5**.
- A_𝒳(h) ≥ **0.904816 − N5**.
- N5 is the price of the nonlinear objects of depth ≥ 5, plus the Fourier-omitted depth-4 nonlinear terms, that contain an opposite-sign linear simple of depth ≤ 3 (or a root, for h).
- The per-simple route can meet its allowance in the model only if **N5 ≥ 0.0751** (h − h₁), or N5 ≥ 0.1549 (h).

**N5 is not certified, for these reasons:**
- **Containment stops being informative at depth 5** ([float], `…-depth5-evidence.py`, 594,630 objects):
  - nonlinear unsigned price at depth 5: 0.042859;
  - objects that could contain a depth-1–3 simple: 0.034311 (80%);
  - with opposite sign: 0.020016 (47%);
  - with an opposite-sign root: 0.001676.
  - Large tensor products contain almost any small multiset, so (C3) no longer excludes anything.
- **The nonlinear unsigned mass per depth has not started to decay:** 0.0242, 0.0410, 0.0438, 0.0429 (depths 2–5).
- **No majorant closes:**
  - The crude path-sum majorant (sup ratios G_m and the word rule for products) has no fixed point. For example, x = 1.0012 + 2.468·0.1365·x² has none.
  - The certified tails stop here, and the infinite nonlinear sum is not bounded in the model price.

## 7. Physical evidence for the identification ([float]; `…-physical-gram.py`)

The physical cold map is the one of the Round 182–184 diagnostics: t = a, mark t₀ = n, one real lift, p up to 4·10⁶. Its pieces are l₀ = h₁, l_{j+1} = L_S l_j, Lin = Σ_j l_j, Nl = h − Lin, and the physical Q₁, L_S Q₁, X₁, C₁.

**Test (i): mean squares against the model's Σ|c|², which assumes unit-normalized, pairwise distinct simples.** Physical/model at p = 4,000,037:

| piece | physical | model |
|---|---|---|
| l₀ | 0.029718 | 0.029665 |
| l₁ | 0.001712 | 0.001710 |
| l₂ | 0.000099 | 0.000099 |
| Q₁ | 4.408·10⁻⁶ | 4.374·10⁻⁶ |
| L_S Q₁ | 2.540·10⁻⁷ | 2.521·10⁻⁷ |
| X₁ | 6.756·10⁻⁷ | 6.722·10⁻⁷ |
| C₁ | 5.800·10⁻¹⁰ | 1.647·10⁻¹⁰ |
| Nl | 5.334·10⁻⁶ | 5.299·10⁻⁶ (sum of the depth-≤3 pieces) |

- The physical values converge to the model's from above as p grows.
- The only discrepancy is C₁. It is explained by the mean-field collision of §5: C₁ contains the dim-3 simples of l₁.

**Test (ii): normalized inner products** ⟨l_j, Nl⟩/|l_j|².

| p | j = 0 | j = 1 | j = 2 | j = 3 |
|---|---|---|---|---|
| 100049 | −0.0003 | −0.0166 | −0.0195 | −0.0249 |
| 400009 | −0.0006 | −0.0087 | −0.0117 | −0.0155 |
| 1000033 | −0.0006 | −0.0063 | −0.0077 | −0.0118 |
| 4000037 | −0.0006 | −0.0036 | −0.0030 | −0.0053 |

- For j ≥ 1 these decay like n^{−1/2}.
- For j = 0 they converge to −0.00064, against the mean-field prediction −0.00062 (Q₁ ⊇ roots).
- The two mean-field predictions match:
  - ⟨h₁, Q₁⟩ per coordinate: −1.0655, −1.7105, −1.7909, −1.8220 (·10⁻⁵) against −1.8473·10⁻⁵;
  - ⟨l₁, C₁⟩: −9.294, −8.582, −8.445, −8.402 (·10⁻⁷) against −8.374·10⁻⁷.

**Reading.**
- An opposite-sign coincidence that lowered the depth-1–3 linear price from 0.445 to 0.3411 by proportional cancellation would force ⟨l_j, Nl⟩/|l_j|² → about −0.23. The data show no such limit.
- **Limitation of this test:**
  - The ℓ² test weights a simple by |c_M|, while the price weights it by dim M·|c_M|.
  - Cancellation confined to simples with small |c_M|/dim M would be ℓ²-invisible. Those simples carry 0.197 of the 0.445 (ratio < 3·10⁻³) and 0.061 (ratio < 10⁻⁴).
  - Same-sign overlaps could mask opposite-sign ones in an ℓ² sum.
- So this is evidence, not a bound on N5.

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved here.** Compact model; exact integers for weight data; outward complex balls for coefficients, uniform on Q × {p ≥ 10⁶}; both lifts.
- (a1) Lemma 0: lift symmetry of the whole expansion.
- (a2) Proposition 1: pairwise inequivalence of all 55,986 linear path simples (depth ≤ 5, kept ranges), from (C1) and (C2). So the linear chain has no collisions of either sign.
  - Under (b4), (b-Jk) and the Round 80 injectivity of K and J^c.
- (a3) Proposition 2: no nonlinear depth-≤3 object equals a linear simple in full weight data. The opposite-sign constituent overlaps allowed by (C3) carry ≤ 0.002608 (h − h₁) and ≤ 0.001617 (roots).
  - Additionally under (b-T) and the purity (semisimplicity) of the pre-transport products.
- (a4) Theorem 3: the certified depth-3 model prices.
  - A_𝒳((h − h₁)_{≤3}) ∈ [0.434571, 0.510376] (≥ 0.442593 counting opposite-sign overlaps only);
  - A_𝒳(h_{≤3}) ∈ [0.912537, 1.004901].
  - Both exceed the allowances 0.3411 and 0.7499.
- (a5) Proposition 4: the Fourier-truncation bounds (T1); Σ_{j≥6} P(L_S^j h₁) ≤ 0.022598 (T2, using Round 184 g_S); and the exact depth-4 nonlinear prices and overlap bounds (T3: 0.043795; opposite-sign 0.003542).
- (a6) Corollary 5: A_𝒳(h − h₁) ≥ 0.416286 − N5 and A_𝒳(h) ≥ 0.904816 − N5, as stated, in the full compact model.

**(b) Conditional / inherited.**
- (b4), (b-Jk) and (b-T), as accepted in Round 184 (the audit labels (b-T) a new reading in equality form).
- (C1) is the identification of the computed weight data with the isomorphism-invariant fibre weights.
- (C2) is Round 80's injectivity, as used there.
- (C3) additionally uses purity.
- The model price identity (unique simple coefficients, rank additivity) is the audit's statement in §6.3. Its transfer to the actual field (D2–D4) is unchanged from Round 184.
- **Hypothesis (H-N5): N5 < 0.0751.** This is the only input separating Corollary 5 from a certified full-model retirement. A sufficient structural form is (MF): every coincidence between a nonlinear constituent and a linear simple arises from trivial pairings X ⊗ X^∨ ⊇ 1 of factors. Under (MF) the coincidences are mean-field renormalizations, of relative size about ½E|h|²·|e₁|·3/((2√t)²ĝ₁) ≈ 6·10⁻⁴ per affected coefficient and order. N5 would then be of order 10⁻⁴. This is an estimate, not a proof.

**(c) Evidence.**
- Depth-5 containment numbers [float].
- The physical mean squares and inner products of §7, including the verified mean-field predictions.
- The brute-force replay, an independent representation. It matches all weight data and all prices to 10⁻⁶ [float].

## Exact remaining gap

- **For the model question.** A bound N5 < 0.0751: the opposite-sign overlap mass of the nonlinear pieces of depth ≥ 5 with the depth-≤3 linear simples. Equivalently, a proof of (MF), or of any identification of constituents finer than weight-data containment, for tensor products of transported simples.
  - The weight-data model cannot decide this.
  - Physically it holds up to 10⁻³ (§7).
- **For the cold route itself, unchanged from Round 184:**
  - A_𝒳(V₆₀₂ − S − h₁) < 0.3411 or A_𝒳(V₆₀₂ − S) < 0.7499, uniformly on Q, both lifts, for the actual field;
  - D2–D4;
  - the readings (b4), (b-Jk), (b-T);
  - the uniform complex stationary domain and derivative transfer.
  - This report shows that the compact model's own value of the first two quantities is above the allowances: certified at depth 3; for the full model, under (H-N5).

## Verdict

**Route retired, as the mission's "supported" branch decides, with one correction: opposite-sign collisions are not absent, but they are negligible.**

- **Collisions.**
  - Across the linear Picard pieces h₁, L_S^j h₁ (j ≤ 5) there are **none** (proved, Proposition 1).
  - Between nonlinear and linear pieces there are opposite-sign collisions: Q₁ against the roots of h₁, and C₁ against the dim-3 simples of L_S h₁.
    - They are identified in §5 and confirmed physically to three digits.
    - They are mean-field renormalizations of relative size about 5·10⁻⁴.
  - The model admits further *possible* opposite-sign overlaps of total price ≤ 0.0026 (depth ≤ 3) and ≤ 0.0035 (depth 4). These are certified upper bounds; their actual size is unknown.
- **Signed model price to depth 3.**
  - A_𝒳((h − h₁)_{≤3}) ≥ 0.4345 > 0.3411;
  - A_𝒳(h_{≤3}) ≥ 0.9125 > 0.7499.
  - Certified, uniform on Q × {p ≥ 10⁶}, both lifts.
- **Full model.**
  - A_𝒳(h − h₁) ≥ 0.4162 − N5 and A_𝒳(h) ≥ 0.9048 − N5.
  - N5 is uncertified, and the route would need N5 ≥ 0.075.
  - The evidence (depth-4 exact 0.0035; the physical Gram data; the mean-field mechanism) puts the actual collisions about two orders of magnitude below that.
- **Decision for the next call.** The per-simple dimension-price route, with h priced through its Picard expansion, cannot meet 0.3411 or 0.7499 in the compact model. The cold route returns to Criterion D, sup transfer or a hybrid price (Round 184 next test 2).
- **Scope.**
  - Nothing here proves or refutes the original target, the ordinary Lovász theta limit of the prime Paley localizations.
  - All certified statements are compact-model statements.
  - A certified *failure* of the model price does not by itself prove that the actual A_𝒳(h − h₁) is ≥ 0.3411. It shows that the route's only proposed mechanism, signed cancellation between Picard pieces, does not occur at the needed size.
  - The proved frozen rate stays 1.066.

## Ranked next tests

1. **Hybrid price (Round 184 next test 2).**
   - Keep the per-simple dimension price for the seed structure, and price multiplication by h through a counting or sup bound.
   - Floating sup|h| ≈ 0.61 < 0.7499 is the seed-only Duhamel allowance; the Round 128 counting rate 0.5145 and the Round 177 rate 0.545 are inputs.
   - This report removes the alternative (cheap A-price of h).
2. **Only if a certified full-model retirement is wanted: prove (MF) or bound N5.**
   - A finite form: show that for tensor products of transported simples with pairwise non-dual factors, no constituent is isomorphic to a linear Picard simple.
   - Or find an invariant finer than weight data (e.g. determinants, boundary characters, monodromy group) that excludes containment for non-paired factors.
   - Low value for the main line: the decision above does not depend on it.
3. **Sanity follow-up (cheap).**
   - The mean-field mechanism predicts the full sign and size of every linear/nonlinear coincidence from E|h|² alone.
   - A physical check at the next order (⟨l₂, ½K(Φ‴h₁²l₁)⟩ and ⟨l₁, X-type⟩) would test (MF) at depth 4.

## Replay commands and outputs

All runs are from the repository root, 2026-11-21, python-flint 0.9.0, numpy. Runtimes: model about 0.1 s, leaves 4 s, tails 7 s, brute force 16 s, depth-5 evidence about 25 s, physical Gram about 65 s.
- The leaves and tails scripts certify statements about exact constants of the compact model, by exact integers and outward balls. §T3 of the tails script is an exact enumeration that bounds the depth-4 pieces. They certify no saved rounded input.
- Lines tagged [float], and the whole of the brute-force, depth-5 and physical scripts, are double-precision evidence.

```bash
.venv/bin/python -B research/paley-185-cold-picard-leaves.py
```
```
== 1. linear chain to depth 5: 55986 path objects; all valid simples (refill >= 0, sum|w| = 2r): True
   depth 0:     6 paths, unsigned path-summed price in [0.494524, 0.494526], dims [2, 4, 6] (max 6)
   depth 1:    36 paths, unsigned path-summed price in [0.260137, 0.260139], dims [3, 6, 7, 10, 11, 13, 20, 21] ... (max 31)
   depth 2:   216 paths, unsigned path-summed price in [0.122824, 0.122825], dims [4, 8, 10, 14, 16, 18, 20, 22] ... (max 160)
   depth 3:  1296 paths, unsigned path-summed price in [0.062239, 0.062241], dims [5, 6, 7, 10, 12, 13, 14, 15] ... (max 825)
   depth 4:  7776 paths, unsigned path-summed price in [0.030629, 0.030630], dims [6, 8, 10, 14, 16, 18, 20, 22] ... (max 4250)
   depth 5: 46656 paths, unsigned path-summed price in [0.015369, 0.015370], dims [7, 8, 9, 10, 11, 12, 13, 14] ... (max 21891)
== 2. identification of the 55986 linear path simples ==
distinct weight data: 55982; weight-data classes with >1 path: 4 (4 pairs)
pairs separated by peeling: C2:pre: 4
pairs NOT separated (possibly equal; twist X ~ J^c Y with equal weight data): 0
blocks: 55986; blocks with >1 member: 0
blocks with members of opposite sign: 0
== 3. signed block price of the linear chain (certified lower / upper; uniform on Q x {p>=10^6}) ==
   depth 0 alone: signed in [0.494524, 0.494526]  (unsigned <= 0.494526)
   depth 1 alone: signed in [0.260137, 0.260139]  (unsigned <= 0.260139)
   depth 2 alone: signed in [0.122824, 0.122825]  (unsigned <= 0.122825)
   depth 3 alone: signed in [0.062239, 0.062241]  (unsigned <= 0.062241)
   depth 4 alone: signed in [0.030629, 0.030630]  (unsigned <= 0.030630)
   depth 5 alone: signed in [0.015369, 0.015370]  (unsigned <= 0.015370)
   depths 1..5 (linear part of h - h_1): signed in [0.491200, 0.491204]  (unsigned <= 0.491204)
   depths 0..5 (linear part of h):       signed in [0.985724, 0.985729]  (unsigned <= 0.985729)
lift symmetry: W(-p) = fibre exchange of W(p) for all paths: True; c(-p) = c(p) (balls overlap): True
== 4. nonlinear pieces to depth 3 (2877 objects after merging tensor permutations) ==
   Q_1     :   147 objects, unsigned price in [0.024197, 0.024199], max dim 222
   L_S Q_1 :   882 objects, unsigned price in [0.013502, 0.013503], max dim 1192
   X_1     :  1512 objects, unsigned price in [0.026802, 0.026803], max dim 1161
   C_1     :   336 objects, unsigned price in [0.000668, 0.000669], max dim 1228
   all nonlinear to depth 3: unsigned <= 0.065172
   Q_1      objects that could contain a roots (h_1)       :    81, unsigned price <= 0.016557
   Q_1      objects that could contain a linear depth 1-3  :     0, unsigned price <= 0.000001
   Q_1      objects that could contain a linear depth 4-5  :     0, unsigned price <= 0.000001
   L_S Q_1  objects that could contain a roots (h_1)       :     0, unsigned price <= 0.000001
   L_S Q_1  objects that could contain a linear depth 1-3  :   594, unsigned price <= 0.008871
   L_S Q_1  objects that could contain a linear depth 4-5  :     0, unsigned price <= 0.000001
   X_1      objects that could contain a roots (h_1)       :   576, unsigned price <= 0.000002
   X_1      objects that could contain a linear depth 1-3  :   604, unsigned price <= 0.001091
   X_1      objects that could contain a linear depth 4-5  :   224, unsigned price <= 0.000228
   C_1      objects that could contain a roots (h_1)       :     0, unsigned price <= 0.000001
   C_1      objects that could contain a linear depth 1-3  :   336, unsigned price <= 0.000669
   C_1      objects that could contain a linear depth 4-5  :     0, unsigned price <= 0.000001
   equal full weight data: linear-vs-nonlinear classes 0; nonlinear-only classes 6 (with opposite signs: 0)
   loss if all equal-weight nonlinear objects were identified (signed vs unsigned): <= 1.000e-300
== 5. model A_X-price of the depth-<=3 truncation (certified, uniform on Q x {p>=10^6}, both lifts) ==
   (h - h_1)_<=3: lower >= 0.434571  [= linear 0.445201 - nonlinear objects touching it 0.010630];  upper <= 0.510376  [= linear 0.445204 + nonlinear 0.065172]
   h_<=3        : lower >= 0.912537  [= linear 0.939725 - touching 0.027188];  upper <= 1.004901
   allowances: A_X(h - h_1) < 0.3411 (joint, Duhamel);  A_X(h) < 0.7499 (seed only)
   linear part to depth 5 (all separated): h - h_1 >= 0.491200, h >= 0.985724; nonlinear depth<=3 objects touching these: 0.010630 / 0.027188
== 6. possible constituent overlaps (containment) and their signs ==
   nonlinear objects possibly containing a roots (h_1)       of OPPOSITE sign:  337 (price <= 0.001617); only same sign:  320 (price <= 0.014942)
   nonlinear objects possibly containing a linear depth 1-3  of OPPOSITE sign: 1058 (price <= 0.002608); only same sign:  476 (price <= 0.008022)
   nonlinear objects possibly containing a linear depth 1-5  of OPPOSITE sign: 1146 (price <= 0.002609); only same sign:  452 (price <= 0.008022)
   equal final weight data, dim 31: (2, 1, 3, 1, -1, 1) vs (4, 1, 1, 1, -1, 1); separated by C2:pre; signs -1, -1
   equal final weight data, dim 31: (2, -1, 3, -1, -1, -1) vs (4, -1, 1, -1, -1, -1); separated by C2:pre; signs -1, -1
   equal final weight data, dim 31: (-2, 1, -3, 1, 1, 1) vs (-4, 1, -1, 1, 1, 1); separated by C2:pre; signs -1, -1
   equal final weight data, dim 31: (-2, -1, -3, -1, 1, -1) vs (-4, -1, -1, -1, 1, -1); separated by C2:pre; signs -1, -1
   Q_1 object ('Q', 0, (-2, 2)) could contain roots [(2,), (-2,)]; coef +1.704e-03
   Q_1 object ('Q', 0, (-4, 4)) could contain roots [(4,), (-4,)]; coef +9.374e-08
   Q_1 object ('Q', 0, (-6, 6)) could contain roots [(6,), (-6,)]; coef +2.063e-11
   Q_1 object ('Q', 2, (2, 2)) could contain roots [(2,)]; coef -3.791e-05
   Q_1 object ('Q', 2, (-2, 2)) could contain roots [(4,)]; coef -7.582e-05
   Q_1 object ('Q', 2, (-2, -2)) could contain roots [(2,)]; coef -3.791e-05
```

```bash
.venv/bin/python -B research/paley-185-cold-tails.py
```
```
== T1. Fourier-truncation terms omitted from the enumeration (certified unsigned upper bounds) ==
   roots: P(h_1) over all k' <= 0.494552; omitted |k'| >= 8: <= 2.708e-05
   seed per-step ratio (1+|k|) varpi |ghat_k|: kept <= 0.699581, omitted |k| >= 7: tau <= 3.031e-05
   omitted linear paths, depth j = 0..5: 2.71e-05, 3.40e-05, 3.43e-05, 3.13e-05, 2.71e-05, 2.25e-05
   omitted nonlinear (depth <= 3): Q_1 4.86e-06, L_S Q_1 4.42e-06, X_1 8.83e-06, C_1 1.45e-06; total <= 1.954e-05
== T2. linear chain beyond the enumeration (certified) ==
   g_S (Round 184) <= 2.467879; with omitted seed lines: sum_(m>=1) ||L_S,full^m|| <= 1.468064
   P(L_S^3 h_1) <= 0.062272  =>  sum_(j>=4) P(L_S^j h_1) <= 0.091419
   P(L_S^5 h_1) <= 0.015393  =>  sum_(j>=6) P(L_S^j h_1) <= 0.022598
   (depth 4 and 5 linear simples are proved inequivalent to every depth <= 3 simple: leaves script, depth 5 run)
== T3. nonlinear pieces of depth 4 (exact enumeration; evidence for the nonlinear tail) ==
   41706 objects
   L_S(L_S Q_1 + X_1 + C_1)    :  16380 objects, unsigned price <= 0.020969
   K(Phi'' h_1 L_S^2 h_1)      :   9072 objects, unsigned price <= 0.012519
   K(Phi'' h_1 Q_1)            :   6174 objects, unsigned price <= 0.002506
   (1/2)K(Phi'' (L_S h_1)^2)   :   4662 objects, unsigned price <= 0.006755
   (1/2)K(Phi''' h_1^2 L_S h_1):   4536 objects, unsigned price <= 0.001012
   (1/24)K(Phi'''' h_1^4)      :    882 objects, unsigned price <= 0.000037
   all nonlinear depth 4: unsigned <= 0.043795   (depth 2: 0.024199; depth 3: 0.040974)
   containment scan : depth-4 nonlinear objects that could contain a linear depth 1-3 simple: price <= 0.017102; with OPPOSITE sign: <= 0.003542; an opposite-sign root: <= 0.004351
== summary: model A_X-price of h - h_1 and of h ==
   linear depth 1-3 priced by |Re c|: >= 0.445201 (by |c|: 0.445201); depth 0-3: >= 0.939725
   depth <= 3 truncation, h - h_1: >= 0.434571 (all touching subtracted), >= 0.442593 (opposite-sign touching subtracted);  <= 0.510376
   depth <= 3 truncation, h    : >= 0.912537 (all touching), >= 0.935500 (opposite-sign);  <= 1.004901
   full model, conditional on the nonlinear depth >= 5 overlap N5 (uncertified):
      A_X(h - h_1) >= 0.416286 - N5   [= 0.445201 - 0.002608 (depth<=3 opp.) - 0.003542 (depth 4 opp.) - 0.022598 (linear j>=6) - 1.685e-04 (Fourier)]
      N5 := opposite-sign overlap mass of the nonlinear pieces of depth >= 5 and of the Fourier-omitted depth-4 nonlinear terms
      A_X(h)       >= 0.904816 - N5
   route survives in the model only if N5 >= 0.0751 (h - h_1) or >= 0.1549 (h)
```
Note on T2: the line "sum_(j>=4) … <= 0.091419" is the crude g_S bound from depth 3 and is printed only for comparison. Corollary 5 subtracts only the j ≥ 6 bound 0.022598. The depth-4 and depth-5 linear simples (exact prices 0.030630 and 0.015370) are proved inequivalent to the depth-≤3 simples, so they contribute nothing to the coordinates that the dual functional uses. Zero quantities print as ≤ 0.000001 because of the outward margin.

```bash
.venv/bin/python -B research/paley-185-cold-bruteforce.py
```
```
(1) linear paths to depth 4: 9330; distinct weight data: 9330  (all distinct: True)
    to depth 5: 55986 paths, 55982 distinct weight data, equal-weight groups: 4
      (2, 1, 3, 1, -1, 1) vs (4, 1, 1, 1, -1, 1): pre-transport data equal? False; dims of pre 24, 22; coefficient signs -1, -1
      (2, -1, 3, -1, -1, -1) vs (4, -1, 1, -1, -1, -1): pre-transport data equal? False; dims of pre 24, 22; coefficient signs -1, -1
      (-2, 1, -3, 1, 1, 1) vs (-4, 1, -1, 1, 1, 1): pre-transport data equal? False; dims of pre 24, 22; coefficient signs -1, -1
      (-2, -1, -3, -1, 1, -1) vs (-4, -1, -1, -1, 1, -1): pre-transport data equal? False; dims of pre 24, 22; coefficient signs -1, -1
    dimension strictly increases along every linear path (depth <= 5): True
(2) weight data agree with the leaves script for all 55986 paths: True
    [float] depth 0: unsigned price (FFT coefficients, t=a, s^2=8) 0.494524; ball midpoints 0.494525
    [float] depth 1: unsigned price (FFT coefficients, t=a, s^2=8) 0.260138; ball midpoints 0.260138
    [float] depth 2: unsigned price (FFT coefficients, t=a, s^2=8) 0.122824; ball midpoints 0.122825
    [float] depth 3: unsigned price (FFT coefficients, t=a, s^2=8) 0.062240; ball midpoints 0.062240
    [float] depth 4: unsigned price (FFT coefficients, t=a, s^2=8) 0.030630; ball midpoints 0.030630
    [float] depth 5: unsigned price (FFT coefficients, t=a, s^2=8) 0.015370; ball midpoints 0.015370
(3) [float] nonlinear unsigned prices (independent): Q_1 0.024198, L_S Q_1 0.013503, X_1 0.026803, C_1 0.000668; certified balls (leaves script): Q_1 <= 0.024198, L_S Q_1 <= 0.013503, X_1 <= 0.026803, C_1 <= 0.000668
BRUTE FORCE DONE
```

```bash
.venv/bin/python -B research/paley-185-cold-depth5-evidence.py
```
```
[float] (f) quintic K(Phi^(5) h_1^5)/120: price <= about 3.4e-05 (crude)
[float] depth-5 nonlinear pieces: unsigned price; part that could contain a linear depth 1-3 simple; part with an OPPOSITE-sign possible overlap (depth 1-3 / roots)
[float]   (a) L_S N4            :  250236 objects, price 0.022949, could-contain 0.018701, opposite 0.010170 / roots 0.000483
[float]   (b) K(Phi'' h0 h3)    :  169092 objects, price 0.010728, could-contain 0.007170, opposite 0.005034 / roots 0.000749
[float]   (c) K(Phi'' h1 h2)    :   91476 objects, price 0.007972, could-contain 0.007238, opposite 0.003700 / roots 0.000363
[float]   (d) cubic             :   69714 objects, price 0.001132, could-contain 0.001124, opposite 0.001063 / roots 0.000081
[float]   (e) quartic           :   14112 objects, price 0.000079, could-contain 0.000078, opposite 0.000049 / roots 0.000000
[float]   total depth 5: price 0.042859, could-contain (depth 1-3) 0.034311, opposite-sign 0.020016, opposite-sign roots 0.001676
[float] depth 2/3/4/5 nonlinear unsigned: 0.0242 / 0.0410 / 0.0438 / 0.0429
```

```bash
.venv/bin/python -B research/paley-185-cold-physical-gram.py
```
```
[float] t = a, one real lift; mean squares E|.|^2 (physical) vs compact model sum |c|^2 (no coincidences)
[float] p = 100049:
[float]   l_0 0.031039/0.029665; l_1 0.001745/0.001710; l_2 0.000101/0.000099; l_3 0.000006/0.000006
[float]   Q_1 4.948e-06/4.374e-06; L_S Q_1 2.852e-07/2.521e-07; X_1 7.226e-07/6.722e-07; C_1 7.233e-10/1.647e-10  (naive: every diagonal Q_1 product as two simples: 5.832e-06)
[float]   E|Nl|^2 = 5.355e-06 (sum of depth<=3 model pieces Q_1+L_SQ_1+X_1+C_1: 5.299e-06);  E|Lin - h_1|^2 = 1.730e-03
[float]   <l_0,Nl>/|l_0|^2 -0.0003; <l_1,Nl>/|l_1|^2 -0.0166; <l_2,Nl>/|l_2|^2 -0.0195; <l_3,Nl>/|l_3|^2 -0.0249
[float]   Q_1: max_j corr(l_j, .) -0.3077 (j=1); L_S Q_1: max_j corr(l_j, .) -0.3069 (j=2); X_1: max_j corr(l_j, .) -0.2020 (j=2); C_1: max_j corr(l_j, .) -0.8274 (j=1)
[float]   <Lin - h_1, Nl>/|Lin - h_1|^2 = -0.0179;  <h_1, Nl>/|h_1|^2 = -0.0003;  corr(Lin, Nl) = -0.0981
[float] p = 400009:
[float]   l_0 0.029991/0.029665; l_1 0.001715/0.001710; l_2 0.000099/0.000099; l_3 0.000006/0.000006
[float]   Q_1 4.504e-06/4.374e-06; L_S Q_1 2.603e-07/2.521e-07; X_1 6.777e-07/6.722e-07; C_1 6.097e-10/1.647e-10  (naive: every diagonal Q_1 product as two simples: 5.832e-06)
[float]   E|Nl|^2 = 5.223e-06 (sum of depth<=3 model pieces Q_1+L_SQ_1+X_1+C_1: 5.299e-06);  E|Lin - h_1|^2 = 1.752e-03
[float]   <l_0,Nl>/|l_0|^2 -0.0006; <l_1,Nl>/|l_1|^2 -0.0087; <l_2,Nl>/|l_2|^2 -0.0117; <l_3,Nl>/|l_3|^2 -0.0155
[float]   Q_1: max_j corr(l_j, .) -0.1513 (j=1); L_S Q_1: max_j corr(l_j, .) -0.1514 (j=2); X_1: max_j corr(l_j, .) -0.1015 (j=2); C_1: max_j corr(l_j, .) -0.8393 (j=1)
[float]   <Lin - h_1, Nl>/|Lin - h_1|^2 = -0.0092;  <h_1, Nl>/|h_1|^2 = -0.0006;  corr(Lin, Nl) = -0.0848
[float] p = 1000033:
[float]   l_0 0.029790/0.029665; l_1 0.001711/0.001710; l_2 0.000099/0.000099; l_3 0.000006/0.000006
[float]   Q_1 4.438e-06/4.374e-06; L_S Q_1 2.553e-07/2.521e-07; X_1 6.721e-07/6.722e-07; C_1 5.892e-10/1.647e-10  (naive: every diagonal Q_1 product as two simples: 5.832e-06)
[float]   E|Nl|^2 = 5.239e-06 (sum of depth<=3 model pieces Q_1+L_SQ_1+X_1+C_1: 5.299e-06);  E|Lin - h_1|^2 = 1.775e-03
[float]   <l_0,Nl>/|l_0|^2 -0.0006; <l_1,Nl>/|l_1|^2 -0.0063; <l_2,Nl>/|l_2|^2 -0.0077; <l_3,Nl>/|l_3|^2 -0.0118
[float]   Q_1: max_j corr(l_j, .) -0.1023 (j=1); L_S Q_1: max_j corr(l_j, .) -0.1004 (j=2); X_1: max_j corr(l_j, .) -0.0638 (j=2); C_1: max_j corr(l_j, .) -0.8410 (j=1)
[float]   <Lin - h_1, Nl>/|Lin - h_1|^2 = -0.0065;  <h_1, Nl>/|h_1|^2 = -0.0006;  corr(Lin, Nl) = -0.0741
[float] p = 4000037:
[float]   l_0 0.029718/0.029665; l_1 0.001712/0.001710; l_2 0.000099/0.000099; l_3 0.000006/0.000006
[float]   Q_1 4.408e-06/4.374e-06; L_S Q_1 2.540e-07/2.521e-07; X_1 6.756e-07/6.722e-07; C_1 5.800e-10/1.647e-10  (naive: every diagonal Q_1 product as two simples: 5.832e-06)
[float]   E|Nl|^2 = 5.334e-06 (sum of depth<=3 model pieces Q_1+L_SQ_1+X_1+C_1: 5.299e-06);  E|Lin - h_1|^2 = 1.795e-03
[float]   <l_0,Nl>/|l_0|^2 -0.0006; <l_1,Nl>/|l_1|^2 -0.0036; <l_2,Nl>/|l_2|^2 -0.0030; <l_3,Nl>/|l_3|^2 -0.0053
[float]   Q_1: max_j corr(l_j, .) -0.0503 (j=0); L_S Q_1: max_j corr(l_j, .) -0.0512 (j=1); X_1: max_j corr(l_j, .) -0.0320 (j=2); C_1: max_j corr(l_j, .) -0.8432 (j=1)
[float]   <Lin - h_1, Nl>/|Lin - h_1|^2 = -0.0036;  <h_1, Nl>/|h_1|^2 = -0.0006;  corr(Lin, Nl) = -0.0629
[float] mean-field (trivial pairing of roots) predictions vs physical inner products (per coordinate):
[float]   p = 100049: <h_1, Q_1> -1.0655e-05 (pred -1.8473e-05);  <l_1, C_1> -9.2938e-07 (pred -8.3737e-07);  <h_1, Nl>/|h_1|^2 -0.00028 (pred -0.00062)
[float]   p = 400009: <h_1, Q_1> -1.7105e-05 (pred -1.8473e-05);  <l_1, C_1> -8.5824e-07 (pred -8.3737e-07);  <h_1, Nl>/|h_1|^2 -0.00059 (pred -0.00062)
[float]   p = 1000033: <h_1, Q_1> -1.7909e-05 (pred -1.8473e-05);  <l_1, C_1> -8.4454e-07 (pred -8.3737e-07);  <h_1, Nl>/|h_1|^2 -0.00061 (pred -0.00062)
[float]   p = 4000037: <h_1, Q_1> -1.8220e-05 (pred -1.8473e-05);  <l_1, C_1> -8.4021e-07 (pred -8.3737e-07);  <h_1, Nl>/|h_1|^2 -0.00064 (pred -0.00062)
```
The "naive" alternative in the Q₁ line counts every diagonal product as two simples, and the data reject it. Under the trivial-pairing picture only the i ≠ 0 diagonal objects gain a root-type constituent, and that changes the model value by less than 10⁻⁸.

Script SHA-256 at the time of this report:

- 2f05c65b56ede5f8105797d9a307d77868a1fe63501c83fcd0bf752fd169a8d6  research/paley-185-cold-bruteforce.py
- 2159ae873095924c92d77bfeb9c2bc98317eebdf0bf77c0e4347fe22a29b6f8e  research/paley-185-cold-depth5-evidence.py
- 22d76c6b738703be849c607f094995909f16b31457347660ac7c9cdab77aa5bf  research/paley-185-cold-model.py
- 358d4fbe1ff0e0a3f99c5b56113db9e63e993d13d6f8369da26fae53fca90566  research/paley-185-cold-physical-gram.py
- a0959ebd7f5fbeca79532cbec2612aae020fc7873a48aec25212a54350bcf6fd  research/paley-185-cold-picard-leaves.py
- cdd5675c4542be0b78df41c39d811f13f516945a47218253b1a6f689aea9b195  research/paley-185-cold-tails.py
