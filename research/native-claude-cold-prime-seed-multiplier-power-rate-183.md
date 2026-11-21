# Round 183 native Claude draft: cold prime seed multiplier power rate

- call_id: `cold-prime-seed-multiplier-power-rate`
- Mission: `coordination/missions/round-183/cold-prime-seed-multiplier-power-rate.md` (record `coordination/round-182.json`, SHA-256 bd56aa4c…)
- Author: a native Claude research session (Claude Opus 5.5, side session started by the Round 183 coordinator). This is an agent draft. It is not an audit, not an acceptance and not a human review.
- Input hashes verified (SHA-256); all match the mission export:
  - round-181-acceptance ad983e94…, round-182-acceptance 78471bc5…
  - native-claude-cold-prime-signed-nonseed-price-182 c8023a9b…, native-claude-audit-182 82edca15…
  - paley-182-cold-seed-power-check 868e9cb8…, paley-182-audit-cold-check 830147c1…
  - cold-growing-prefix-delocalization-180 3a8eb51a…, cold-seed-centered-larger-tube-177 12c7cff4…
  - Also read, for the Taylor constant: `cold-height-602-frozen-kernel-162.md` (lines 30–46) and `cold-first-prefix-step-174.md` (lines 1–30); for the line rule: `astra-dissipation-80.md` lines 82–112 and `weighted-arithmetic-57.md` line 17.
- Scripts written by this session (replay commands and full outputs at the end):
  - `research/paley-183-cold-seed-taylor-power.py`: exact rationals and integer square roots, outward rounding. Fourier coefficients of the full seed multiplier, its exact m-step growth under the Round 80 rule extended to J^k, the re-derived constants, the budgets for the non-seed part. (A floating LP only proposes supports; every printed bound is recomputed exactly.)
  - `research/paley-183-cold-seed-taylor-bruteforce.py`: extends the Round 182 audit brute force (Part 2 of `paley-182-audit-cold-check.py`) from J^{±1} to J^k, |k| ≤ 7, on explicit simples. Exact, plus a labelled floating FFT cross-check.
  - `research/paley-183-cold-h-picard-diagnostic.py`: floating diagnostic of the Picard pieces of h. Evidence only.

## Result summary

**Verdict: inconclusive.** No uniform power bound for the full frozen multiplier at V_602 below 1 − C(1 − κ*) is certified. The best certified one-step rate for the full multiplier is still 1.066 (P_5000, Round 162). So Γ_{k_n} is not shown to be bounded uniformly in n. What changed:

1. **Moving the seed-only Taylor terms into L_S = KΦ_t′(S)·costs almost nothing (a, compact model, per simple).**
   - Φ_t′(S) = (s/(2√t)) Σ_{k odd} ĝ_k(β) J^k exactly, with β = s²/(4t). Uniformly on Q and for p ≥ 10⁶: |ĝ_{±1}| ≤ 0.47807257, |ĝ_{±3}| ≤ 0.00703959, |ĝ_{±5}| ≤ 0.00015639 (Lemma 1).
   - The Round 80 per-simple rule extends to J^k (shift (−k, +k)), with nonnegative refill (Lemma 2).
   - The exact m-step growth G_m(α) of the full seed multiplier is computed for m ≤ 8 and α ∈ {0, 1/16, …, 1}. Every value is an exact supremum (primal = dual), not a bracket (Proposition 3).
   - Net effect of the seed-only Taylor terms, against the linear seed: one-step rate 0.69959 vs 0.71007 (α = 0); 0.53519 vs 0.53255 (α = 1, the only case where it is worse, by +0.0026). Every m ≥ 2 rate improves, e.g. 8-step rate 0.53220 vs 0.53619 (α = 0). The audit's charge of +0.104 (or +0.21) for these terms disappears.
   - Side result: the Round 182 mediant values G_up are the exact suprema (approached by the {0, ±K}, K → ∞ simples). This closes the Round 182 bracket [G_lo, G_up].
2. **The h-linear allowance in π₁ is restored to 1.912** (one-step 1.901 = 0.23859·√N from the α = 1, m0 = 1 row of §4 of the output), against 1.925 in Round 182 (seed-only Taylor ignored) and 1.094 in the audit (seed-only Taylor charged). This holds under Round 182's reading (b1) of the inherited constants.
3. **The inherited constants are re-derived for π_α (a, as an implication of the inherited Round 126/162/174 inputs) (Lemma 4).**
   - The Round 162/174 Taylor coefficient becomes c_α(M) = ((1+α)/2)·c(M). The factor 2 in c(M) is exactly "output price ≤ 2·rank" in P_5000; in π_α it is (1+α)·rank.
   - So c(M) survives verbatim in π₁, and halves in the plain dimension price A = π₀.
   - The source price becomes p0_α ≤ (1+α)·0.01272. This uses Round 174's statement that P_5000 dominates the dimension budget, read as A ≤ P_5000 on the unshifted class.
   - The sharp thresholds are κ*_α = 1 − (1+α)(1 − κ*_A), with κ*_A ∈ [0.83790251, 0.83790253] for A and κ*_{π₁} ∈ [0.67580502, 0.67580504] for π₁.
   - So in π₁ the doubled source eats most of the budget. **The best price is the plain dimension price A (α = 0).**
4. **The non-seed multiplier is priced explicitly around the seed (Lemma 5).**
   - Φ_t″(S) = (1/(2√t)) Σ b̂_{2i}(β) J^{2i}. Its Fourier ℓ¹ norm is exactly 1/(2√t) at real t, by an alternating-sign identity.
   - With the word-rank rule rank(H·J^k·F) ≤ (|k|+2)dr, the h-linear term costs (1+α)·ρ₀·A(h)/√N. The effective ratio is ρ_eff = (1+α)ρ₀, with ρ₀ = Σ(|k|+2)|b̂_k| ≤ 2.17565.
   - The h-higher Taylor terms cost (1+α)H(A(h)) by a word majorant that counts the seed lines.
5. **Exact budget of the blocking term (Proposition 6).**
   - Best case: dimension price A, 8-step seed power form (λ_S ≤ 0.53244, C_S ≤ 1.3146), re-derived constants. Cor. 2.2 then gives the criterion **2.17565·A(h)/√N + H(A(h)) < 0.19359, i.e. A(h) < 0.6179** (bracket [0.6179, 0.6180]).
   - Under the verbatim reading (b1) the best is A(h) < 0.4488 (α = 5/16).
   - The only available bound is A(h) ≤ 1.994573, and it is conditional on designating the seed (b2). It gives a full-multiplier power rate ≤ 1.646, against the needed 0.838.
6. **Evidence (c).**
   - A(h) ≥ sup|h| ≈ 0.557 (floating), so the target A(h) < 0.618 is not excluded by the sup.
   - In the compact model, the first Picard piece h₁ = K(bulk Φ_t(S)) has A(h₁) ∈ [0.4945, 0.4946] (exact model value).
   - The floating remainder h − h₁ has sup ≈ 0.19, which already lower-bounds its A-price. So any proof that prices h₁ and h − h₁ separately cannot get below about 0.68 > 0.618.
   - Reaching 0.618 would need cancellation between Picard pieces in the A-representation. The floating sup (sup|h| = 0.557 > sup|h₁| = 0.499) shows none at the extremal coordinate.

## Setup recalled (from Round 182, unchanged)

- p ≡ 1 (mod 4) is a large eligible prime and n = (p−1)/2. Q is the original closed square of half-width 2⁻¹⁷ about a = 2031/128, and N = 4(a − 2⁻¹⁷), so |√t| ≥ √N/2 on Q. Physical mark t₀ = n, genuine nine-center start, both lifts.
- V_{h+1} = KΦ_t(V_h), with Φ_t(x) = √(4t + x²). The seed is S = 2√nKe₀ = s_pC, with C = Re J and s_p = 2√(p/n) ↓ 2√2.
- Frozen-base identity at 602: U_{j+1} = R + LU_j + T(U_j), with L = KD_602, D_602 = diag Φ_t′(V_602) and V_602 = S + h.
- Proposition 1, Proposition 2, Corollary 2.1 (λ < 1 − C(1−κ*)) and Corollary 2.2 (‖(L_S+B)^m‖ ≤ C_S(λ_S + C_Sβ)^m, valid for C_S ≥ 1 per the audit) are from Round 182, as accepted. Remark 2.3 (any use needs Γ_{k_n} bounded uniformly in n) is also accepted in Round 182.
- **Compact model, per simple (Round 80, (b4) of Round 182).** A negative simple of dimension r has two boundary fibres with r weight slots each, and Σ|w| = 2r. J shifts the fibres by (−1, +1). The positive product has generic rank r′ = ½Σ|w′|. Transport K keeps negative weights in their fibre, moves positive weights to the other fibre, and refills each fibre with zeros up to r′.
- **Prices.**
  - A(f) = Σ|c_M|d_M is the minimal Deligne-type price (Round 181): |f| ≤ A(f) on the coset, and A(fg) ≤ A(f)A(g).
  - π_α(M) = r + αZ/2, where Z is the number of zero slots in both fibres. It extends to fields by the infimum over representations. So A = π₀ ≤ π_α ≤ (1+α)A, because Z ≤ 2r.
- **Word-rank rule (Round 126, used in Rounds 162/174).** Let a product of factors have pooled first absolute moments μ_i and dimensions d_i. Its generic rank is at most ½Σ_i μ_i ∏_{j≠i} d_j. A negative simple has μ = 2d. The line J^k has d = 1 and μ = 2|k|. For k negative factors this gives rank ≤ k∏d.

## Argument

### 1. The seed multiplier with all seed-only Taylor terms (Lemma 1; a)

At a good coordinate, J = e^{iθ} has modulus one, so J⁻¹ = J̄ and S = s cos θ. For t ∈ Q, put β = s²/(4t); then |β| < 0.127. We have Φ_t′(S) = S(4t+S²)^{−1/2} = (s/(2√t))·g_β(θ), where g_β(θ) = cos θ(1 + β cos²θ)^{−1/2}. Expanding (1+y)^{−1/2} = Σ(−1)^l c_l y^l with c_l = binom(2l,l)/4^l, and cos^{2l+1}θ = 2^{−(2l+1)}Σ_i binom(2l+1, i) e^{i(2i−2l−1)θ}, gives

  Φ_t′(S) = (s/(2√t)) Σ_{k odd} ĝ_k(β) J^k,  ĝ_k(β) = Σ_{l ≥ (|k|−1)/2} (−1)^l c_l β^l binom(2l+1, l+(|k|+1)/2)/2^{2l+1}.

The double series converges absolutely: Σ_k Σ_l |·| ≤ (1−|β|)^{−1/2}. It is the same expansion as the "seed-only higher Taylor terms" of Round 182 §4(ii), regrouped by net exponent k. A word in J, J⁻¹ with net exponent k is J^k, so the grouping is exact.

**Uniform bounds** (exact rationals; `paley-183-cold-seed-taylor-power.py` §1).
- For p ≥ 10⁶ we have s_p² = 8 + 8/(p−1) ≤ 8 + 8/(10⁶−1).
- For t ∈ Q: |t − a| ≤ √2·2⁻¹⁷ and |t| ≥ a − 2⁻¹⁷.
- Hence |β − 256/2031| ≤ δ = 2.17·10⁻⁷ and |s_p/(2√t)| ≤ ϖ ≤ 0.355030238.
- Then |ĝ_k(β)| ≤ |ĝ_k(β₀)| + b^{41}/(1−b) + δ·½(1−b)^{−3/2} with b = β₀ + δ, which gives γ_k:

| k | ĝ_k(256/2031) (exact bracket) | uniform γ_k ≥ \|ĝ_k(β)\| |
|---|---|---|
| ±1 | [0.478072428819, 0.478072428820] | 0.478072561593 |
| ±3 | [−0.007039456508, −0.007039456507] | 0.007039589281 |
| ±5 | [0.000156252275, 0.000156252276] | 0.000156385050 |
| ±7 | [−0.000003858441, −0.000003858440] | 0.000003991214 |
| ±9 | [0.000000100092, 0.000000100093] | 0.000000232867 |

- The signs alternate as (−1)^{(|k|−1)/2}.
- The ℓ¹ mass is Σ|ĝ_k(β₀)| = 0.97054… This is below the linear seed's 1, but above sup g_β = (1+β₀)^{−1/2} = 0.94237.
- A floating FFT reproduces all five values to about 10⁻¹⁵ (`…-bruteforce.py`, [float]).
- For |k| > 81 the tail is |ĝ_k(β)| ≤ b^{(|k|−1)/2}/(1−b).

### 2. Per-simple rule for J^k and the exact m-step growth (Lemma 2, Proposition 3; a in the compact model)

**Lemma 2 (the J^k child is a valid simple).** Let k be odd, and let the parent be a valid negative simple of dimension r (Σ|w| = 2r over 2r slots). Multiply by J^k: fibre A shifts by −k and fibre B by +k. Then transport. The result has generic rank r′ = ½Σ|w′|, with r(|k|−1) ≤ r′ ≤ r(|k|+1), and both refills r′ − nz_F′ are ≥ 0.

*Proof.*
- **Bounds on r′.** |w ∓ k| ≥ |k| − |w| and |w ∓ k| ≤ |w| + |k|. Summing over the 2r slots gives the two bounds.
- **|k| ≥ 3.** Then r′ ≥ 2r, which is at least the number of slots in either fibre, so both refills are nonnegative.
- **k = +1.** The nonzero count of fibre A′ is #(A: w ≤ 0) + #(B: w ≥ 0). Let τ = #(A: w ≥ 1) + #(B: w ≤ −1). By Round 182 Lemma 3.1, r′ = 2r − τ. Adding, nz_A′ + τ = #A + #B = 2r, so the refill of A′ is exactly 0.
- For fibre B′, nz_B′ ≤ #(|w| ≥ 2) and τ ≤ #(nonzero).
- Since Σ_{slots}(|w| − 1) = 0, we have #(|w| ≥ 2) ≤ Σ_{|w|≥2}(|w|−1) = #(zeros).
- Hence nz_B′ + τ ≤ #zeros + #nonzero = 2r, that is, nz_B′ ≤ r′.
- **k = −1.** This is symmetric. ∎

The model input (b-Jk) is this. J^k acts as k-fold line multiplication before one transport. By the Round 57 weight calculus, tensoring by L shifts the weights at the two boundary points by (−1, +1), so L^{⊗k} shifts them by (−k, +k). And r′ = ½Σ|w′| holds as in Round 80. The bound r′ ≤ (|k|+1)r agrees with the word-rank rule (μ(J^k) = 2|k|). The brute force verifies Lemma 2 on all 2413 parents with r ≤ 4 and |k| ∈ {1, 3, 5, 7}: zero negative refills, and the destination-fibre refill under J^{±1} is exactly zero.

**Linearity.** As in Round 182 Lemma 3.2, each step x ↦ M_k x is linear on slot-count vectors, and π_α is linear. Put M = Σ_{|k|≤5} γ_k M_k. Then

  ‖L_S^m‖_{π_α} ≤ G_m(α)·ϖ^m + (|k| ≥ 7 perturbation),  G_m(α) = sup_{valid x} π_α(M^m x)/π_α(x).

G is submultiplicative because children of valid simples are valid. The terms with |k| ≥ 7 cost at most τ_α = ϖ·Σ_{|k|≥7}(1+α)(1+|k|)γ_k per step. They enter through Cor. 2.2 as λ ↦ λ + C τ_α, with τ ≈ 10⁻⁵.

**Exactness (LP duality).**
- Every valid simple is a nonnegative combination of "atoms": one nonzero slot of value v with its induced zeros |v|/2 − [own fibre] in each fibre.
- For |v| ≥ 5m+2 the m-step numerator is affine in |v|. The script checks this exactly by vanishing second differences.
- So G_m(α) is a linear-fractional programme over the atoms with |v| ≤ 5m+6 plus four |v| → ∞ direction columns, under two constraints (zero counts ≥ 0).
- The script evaluates the exact primal value on the support proposed by a floating LP, and the exact dual objective max_t (n_t + μ·z_t)/d_t at the exact dual point.
- **They coincide in all 136 cases** (α ∈ {j/16}, m ≤ 8).
- The optimum is a |v| → ∞ direction (the {0, ±K} simples, K → ∞, as in Round 182 §3), so the supremum is approached, not attained. The exception is α = 1, m = 1, where the supremum is attained.
- The same LP applied to the Round 182 linear seed returns exactly 4, 12, 104, 6928 (α = 0) and 3, 9, 75, 4915 (α = 1). So **the Round 182 G_up values are the exact suprema**. Round 182's G_lo restricted |v|, and its bracket is closed from above.

**Proposition 3 (exact growth of the full seed multiplier).** Here rate = G_m^{1/m}·ϖ, rounded upward. "lin" is the Round 182 linear seed with coefficient ½ on J^{±1}, in the same normalisation (its rates are Round 182's).

| m | G_m(0) | rate (lin) | G_m(½) | rate (lin) | G_m(1) | rate (lin) |
|---|---|---|---|---|---|---|
| 1 | 1.970484 | 0.69959 (0.71007) | 1.646972 | 0.58473 (0.59172) | 1.507429 | 0.53519 (0.53255) |
| 2 | 2.940449 | 0.60880 (0.61494) | 2.455376 | 0.55632 (0.56136) | 2.212839 | 0.52813 (0.53255) |
| 4 | 6.278417 | 0.56199 (0.56689) | 5.126611 | 0.53423 (0.53848) | 4.550709 | 0.51855 (0.52240) |
| 8 | 25.495420 | 0.53220 (0.53619) | 20.636210 | 0.51832 (0.52195) | 18.206605 | 0.51027 (0.51367) |

The values are exact suprema, printed rounded up to 6 decimals. All (α, m) for α ∈ {j/16} are in the replay output.

**Power bounds** (submultiplicativity with base m0, the |k| ≥ 7 tail included, exact rationals):
- α = 0, m0 = 8: λ_S ≤ 0.53244, C_S ≤ 1.3146;
- α = ½, m0 = 4: λ_S ≤ 0.53453, C_S ≤ 1.0946;
- α = 1, m0 = 3: λ_S ≤ 0.52224, C_S ≤ 1.0256;
- α = 1, m0 = 1: λ_S ≤ 0.53556, C_S = 1.

**Answer to the audit's correction.** With the seed-only Taylor terms inside L_S, they are no longer a separate charge. Their net per-step effect is −0.0105 (α = 0), −0.0070 (α = ½) and +0.0026 (α = 1) in rate. The audit's crude dimension charge was +0.104.
- Mechanism: the saturation of Φ_t′ lowers |ĝ_{±1}| from ½ to 0.478. That roughly pays for the J^{±3} terms, whose per-simple ratio is up to (1+α)(1+3).
- In π₁, under the Round 182 reading (b1) of the constants, the h-linear allowance becomes ρA(h) < 1.912 (best power form m0 = 3) or < 1.901 (one step: β_max = 0.23859 times √N). This is in Round 182 units, with cost = ρA/√N and h-higher terms not charged. Compare 1.925 in Round 182 and 1.094 in the audit.

### 3. Constants for the new price (Lemma 4; a as an implication of inherited inputs, with one reading flagged)

Proposition 1/2 need, in the price P = π_α: sup domination, p0, c, (H1) and (H2).

**(i) Sup domination.** ‖f‖_∞ ≤ A(f) ≤ π_α(f) at good coordinates (Round 181: |f| ≤ A(f)). Bad coordinates and the mark are the inherited O(n^{−1/2}) corrections.

**(ii) The Taylor coefficient.** I re-derive the Round 162/174 constant (162 lines 33–44; 174 line 24).
- T(U) = K(U²∫₀¹(1−s)(4t)^{−1/2}(1 + (V+sU)²/(4t))^{−3/2} ds). The series has coefficients b_l = (2l+1)binom(2l,l)/4^l.
- A word of order l has 2l+2 negative factors, and its rank is at most (2l+2)∏d by the word-rank rule.
- In P_5000 the transported output has "price at most twice that rank". The 1/2 from ∫(1−s) cancels that 2, giving c(M) = (2/√N)Σ(l+1)b_l x^l = (2/√N)(1+x/2)(1−x)^{−5/2}.
- In π_α the output simple of dimension r′ has π_α = r′ + αZ/2 ≤ (1+α)r′. The input dimensions are at most π_α(U) and 4.823 + π_α(U).
- So the same argument gives π_α(T(U)) ≤ ((1+α)/2)·c(M)·π_α(U)² + O(n^{−1/2}π_α(U)²), with M = 4.823 + π_α(U).
- **In π₁ the coefficient c(M) survives verbatim; in A it halves.** The O(n^{−1/2}) bad-character and mark corrections are inherited from Rounds 162/174 and not re-derived.

**(iii) The source.** π_α(R_602) ≤ (1+α)A(R_602), by taking A's near-optimal representation. Round 174 (line 3) states that P_5000 "dominates the coordinate supremum and the dimension budget on these unshifted packets". **Reading this as A ≤ P_5000 on that class** gives A(R_602) ≤ P_5000(R_602) < 0.01272, hence p0_α ≤ (1+α)·0.01272. The reading is flagged as (b5) below. The P_5000 chain itself (1.048·0.012 + 0.000140) does not transfer, because it uses ‖KD_601‖_{P_5000}.

**(iv) Threshold.** Scaling p0 by (1+α) and c by (1+α)/2 gives κ*_α = 1 − (1+α)·inf_{u ≤ 3/8}[p0/u + c(M0+u)u/2]. The brackets below are exact, certified by an adaptive partition with c bounded above and below by rational square-root intervals:

| price | κ* (reading b1*: re-derived) | radius u | κ* (reading b1: verbatim, Round 182) |
|---|---|---|---|
| A = π₀ | [0.83790251, 0.83790253] | 0.14944 | [0.77414706, 0.77414708] |
| π_{1/4} | [0.79737814, 0.79737816] | 0.14944 | same |
| π_{1/2} | [0.75685377, 0.75685379] | 0.14944 | same |
| π₁ | [0.67580502, 0.67580504] | 0.14944 | same |

- The verbatim bracket [0.77414706, 0.77414708] re-certifies the audit's corrected value 0.7741470636.
- (H1) class closure and (H2) uniform corrections for π_α are not re-derived. Both use the same word rules (odd multiplier words, even Taylor words followed by transport) as for P_5000. Like Round 182, I state them as hypotheses.

### 4. The non-seed multiplier priced around the seed (Lemma 5; a)

Write B = K((Φ_t′(S+h) − Φ_t′(S))·) = K(Φ_t″(S)h·) + K((Φ_t′(S+h) − Φ_t′(S) − Φ_t″(S)h)·).

**Lemma 5 (h-linear multiplier).** Φ_t″(x) = 4t(4t+x²)^{−3/2}. Hence Φ_t″(S) = (1/(2√t))·(1+β cos²θ)^{−3/2} = (1/(2√t))Σ_i b̂_{2i}(β)J^{2i}, with

  b̂_{2i}(β) = Σ_{l≥|i|} binom(−3/2, l) β^l binom(2l, l+i)/4^l.

For real β > 0, b̂_{2i} = (−1)^i|b̂_{2i}| and Σ_k |b̂_k| = 1.

*Proof.*
- Write cos²θ = (1 + cos 2θ)/2. Then (1+β cos²θ)^{−3/2} = (1+β/2)^{−3/2}(1 + q cos 2θ)^{−3/2} with q = (β/2)/(1+β/2) ∈ (0, 1).
- binom(−3/2, j) has sign (−1)^j. The powers cos^j(2θ) have nonnegative Fourier coefficients, supported on frequencies 2i with i ≡ j (mod 2).
- So the coefficient of cos 2iθ has sign (−1)^i. The ℓ¹ sum therefore equals the value at θ = π/2: (1 + β/2 − β/2)^{−3/2} = 1.
- The series converges absolutely, since Σ|binom(−3/2, j)|q^j = (1−q)^{−3/2}. ∎

**Uniform version.** For complex β with |β − β₀| ≤ δ, the absolute series gives Σ_k (|k|+2)|b̂_k(β) − b̂_k(β₀)| ≤ δΣ_l l|binom(−3/2,l)|b^{l−1}(2l+2). The exact values are b̂₀ = 0.915418…, b̂_{±2} = −0.040726…, b̂_{±4} = 0.001510…, and

  ρ₀ := Σ_k (|k|+2)|b̂_k(β)| ≤ 2.17565 (√N·SIGH, with SIGH ≤ 0.273091676),  Σ_k |b̂_k(β)| ≤ 1 + O(δ).

**h-linear cost.** By the word-rank rule (moment form), H·J^k·F has rank at most (|k|+2)dr for H of dimension d and F of dimension r. In π_α the output costs at most (1+α) times its rank, and the input costs at least r. So

  ‖K(Φ_t″(S)h·)‖_{π_α} ≤ (1+α)·ρ₀·A(h)/√N.

This is sharper than expanding around zero. That expansion gives 2A(h)/√N for K(h/(2√t)·), plus seed-h cross words A(h)[G_all′(s) − 2/√N] = 0.1227A(h), a total of 0.3737A(h). The seed-centred bound is 0.2731A(h). The ρ₀ = 2.1757 includes the seed lines. Without them ρ would be 2(1+α), as in Round 182, but the word rule does not allow dropping them.

**h-higher terms.** Words of order l with j ≥ 2 h-factors have rank at most (2l+2)∏d, counting the seed lines. Their total cost is at most (1+α)H(A), where

  H(A) = G_all(s+A) − G_all(s) − A·G_all′(s),  G_all(y) = Σ_l c_l(2l+2)y^{2l+1}/N^{l+1/2} = y(2N−y²)/(N−y²)^{3/2},

with G_all′(y) = N(2N+y²)/(N−y²)^{5/2}. H is increasing in s, so it is evaluated at s_p ≤ 2.828428539. Certified values:
- H(0.55) ≤ 0.01932;
- H(1) ≤ 0.07243;
- H(1.994573) ≤ 0.40151.

### 5. Proposition 6: the criterion and its exact budget (a as an implication; inputs (b))

Combine Cor. 2.1/2.2 (Round 182) with Proposition 3, Lemma 4 and Lemma 5. If for some α ∈ [0,1] and m0 ≤ 8

  (1+α)[ρ₀A(h)/√N + H(A(h))] < β_max(α, m0) := (1 − λ_S)/C_S − (1 − κ*),

then ‖L^m‖_{π_α} ≤ C_S λ^m with λ < 1 − C_S(1−κ*), uniformly in n (given (b1–b5)). Then Γ_{k_n} ≤ C_S/(1−λ) is bounded, and the Round 173 finite-prefix confinement follows by Proposition 2.

| price, reading | best m0 | λ_S ≤ | C_S ≤ | β_max ≥ | **A(h) needed <** |
|---|---|---|---|---|---|
| A (α = 0), b1* (re-derived) | 8 | 0.53244 | 1.3146 | 0.19359 | **0.6179** |
| A, b1* | 1 | 0.69977 | 1 | 0.13813 | 0.4579 |
| π_{1/4}, b1* | 6 | 0.53218 | 1.1857 | 0.19194 | 0.5036 |
| π_{1/2}, b1* | 4 | 0.53453 | 1.0946 | 0.18212 | 0.4072 |
| π₁, b1* | 3 | 0.52224 | 1.0256 | 0.14167 | 0.2462 |
| best over α ∈ {j/16}, b1 (verbatim) | 6 (α = 5/16) | 0.53001 | 1.1658 | 0.17730 | 0.4488 |
| π₁, b1 (verbatim) | 3 | 0.52224 | 1.0256 | 0.24001 | 0.4029 |

Each A(h) column entry is the certified lower end of a bracket of width 10⁻⁴ (see output).

**What blocks.** The blocking term is the h-linear term K(Φ_t″(S)h·), with ρ₀ = 2.17565 and the unproved size of A(h). In the best case, the A-price with b1*, the h-linear term alone may use 0.19359 − H(A) of a total budget of 0.19359.

Equivalently, the largest admissible effective ratio ρ_eff at a given A(h) (α = 0, m0 = 8, b1*, outward) is:

| A(h) | 0.55 | 0.60 | 0.70 | 0.80 | 1.00 | 1.50 | 1.9946 |
|---|---|---|---|---|---|---|---|
| ρ_eff needed < | 2.5245 | 2.2612 | 1.8325 | 1.4921 | 0.9653 | 0.0168 | < 0 |

- The word rule gives 2.17565. At A(h) ≥ about 1.51 even ρ = 0 fails, because the h-higher majorant alone exceeds the budget.
- The only proved-type bound, A(h) ≤ 4.823 − s_p < 1.994573, needs the seed designated in V_602's representation (b2). With it, the full-multiplier power rate is λ ≤ 1.6460 (A, one step), against the needed 0.8379. It is also worse than P_5000's 1.066.

### 6. Evidence (c): the size of A(h)

- **Compact model, exact at t = a (not a bound on A(h)).**
  - The first Picard piece from the seed is h₁ = K(bulk Φ_t(S)) = 2√t Σ_{k even ≠ 0} b′_k K(J^k), where b′_k are the Fourier coefficients of (1+β cos²θ)^{1/2}: b′_{±2} = 0.0152866, b′_{±4} = −0.000113.
  - K(J^k) is a negative simple of dimension |k| (weights (−k, +k), cf. the Round 80 table, where K(J²) has dimension 2). Distinct k give inequivalent simples.
  - So A(h₁) = 2√a Σ_{k≠0}|b′_k||k| ∈ [0.4945, 0.4946], and the model RMS is √2·2√a·b′₂ ≈ 0.1722.
- **Floating physical rows** (`paley-183-cold-h-picard-diagnostic.py`; real t = a, one lift, double precision):

| p | sup\|h\| | RMS(h) | sup\|h₁\| | RMS(h₁) | sup\|h−h₁\| | RMS(h−h₁) |
|---|---|---|---|---|---|---|
| 10009 | 0.5699 | 0.1949 | 0.6046 | 0.2074 | 0.1629 | 0.0407 |
| 100049 | 0.5513 | 0.1752 | 0.5125 | 0.1762 | 0.1761 | 0.0409 |
| 400009 | 0.5566 | 0.1749 | 0.4992 | 0.1732 | 0.1928 | 0.0415 |

- RMS(h₁) → 0.172 and sup|h₁| → about 0.49–0.50 agree with the model. The later Picard pieces have sup about 0.19, 0.05, 0.01, …
- **Reading.**
  - A(h) ≥ sup|h| ≈ 0.557. That is below 0.618, so the sup does not exclude the best case.
  - But A(h) ≤ A(h₁) + A(h−h₁) with A(h−h₁) ≥ sup|h−h₁| ≈ 0.19. So any proof that prices the first Picard piece and the rest separately ends at about 0.68 or more, which is above 0.618.
  - A per-simple Picard estimate (L_S h₁ alone costs about 0.51·A(h₁) ≈ 0.25 in A by the J^{±1} rule) gives, as a rough estimate (not computed), A(h) ≈ 0.9–1.1 for the unsigned series.
  - Meeting 0.618 would need cancellation between Picard pieces in the A-representation. At the extremal coordinate the pieces add (sup|h| > sup|h₁|).
  - The evidence therefore leans against the unsigned per-simple route even in its best reading. It is not a refutation: A(h) is not computed, and a signed or weight-resolved product rule could lower ρ_eff.

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved here** (compact model per simple where stated; exact rationals for every number):
- (a1) Lemma 1: the exact J^k expansion of Φ_t′(S), with uniform coefficient bounds on Q × {p ≥ 10⁶}. The signs alternate at β₀.
- (a2) Lemma 2: the J^k child is a valid simple (refill ≥ 0), with r(|k|−1) ≤ r′ ≤ r(|k|+1). Under J^{±1} the destination fibre is never refilled.
- (a3) Proposition 3: exact suprema G_m(α) for the full seed multiplier, m ≤ 8, α ∈ {j/16} (primal = dual in all 136 cases), and the power constants. The Round 182 G_up are exact suprema.
- (a4) Lemma 4 as implications: sup domination of π_α; c_α = ((1+α)/2)c(M) from the Round 162/174 word argument (c survives in π₁, halves in A); p0_α ≤ (1+α)A(R_602); and the κ*_α brackets.
- (a5) Lemma 5: Φ_t″(S) has Fourier ℓ¹ norm exactly 1/(2√t) for real t, and ρ₀ ≤ 2.17565 uniformly. Also the h-higher majorant H.
- (a6) Proposition 6 as an implication, with the A_max table. The full-multiplier rate is ≤ 1.646 at A(h) ≤ 1.994573.

**(b) Conditional / inherited, not re-derived:**
- (b1*) Lemma 4(iii) needs A(R_602) ≤ P_5000(R_602). This is my reading of Round 174's "dominates … the dimension budget". The O(n^{−1/2}) corrections in Lemma 4(ii) are inherited from Rounds 162/174. (b1) is the Round 182 verbatim transfer, kept for comparison.
- (b2) A(h) ≤ 1.994573 needs the seed designated in V_602's representation (Round 182 (b2)).
- (b3) (H1) class closure and (H2) uniform corrections for π_α.
- (b4) The Round 80 per-simple rule, as in Round 182 (b4). (b-Jk) J^k acts as k-fold line multiplication (Round 57 weight calculus) before one transport, and at good coordinates |J| = 1, so J⁻¹ = J̄.
- (b5) The word-rank rule of Round 126 in moment form, applied to products containing seed lines and non-seed simples. This is the same input as Round 182 (a6) and the Round 162/174 Taylor bound.

**(c) Evidence:**
- (c1) The physical h₁ matches the model (RMS 0.1732 vs 0.1722).
- (c2) sup|h| ≈ 0.557 and sup|h − h₁| ≈ 0.19, so the separately priced Picard pieces exceed 0.618.
- (c3) The FFT cross-checks of ĝ_k, b̂_k, and the identity Σ|b̂_k| = 1.

## Exact remaining gap

To make the cold criterion usable along this route, one has to prove, uniformly in n, all t ∈ Q and both lifts:
- **A(h) < 0.6179 for h = V_602 − S in the Fourier-algebra (dimension) price**, together with (b1*) and (b3). This holds with the word-rule ratio ρ₀ = 2.17565 and the 8-step seed power form.
- **Or** a product rule for the actual non-seed simples of V_602 with ρ_eff·A(h) + √N·H(A(h)) < 1.5424 (α = 0). For example, ρ_eff < 1.49 if A(h) ≈ 0.8, or < 0.97 if A(h) ≈ 1.

Present status:
- A(h) ≤ 1.9946 is conditional (b2).
- The model value A(h₁) = 0.4946 and the floating sup|h − h₁| ≈ 0.19 suggest that the unsigned A(h) is near 0.7–1.1.

**The single most decisive missing input is a weight-resolved per-simple rule for multiplying by the transported fields K(J^{2i}) (the simples of h₁) and their L_S-children.** Their two-fibre weights are known exactly, unlike the generic h-simples. This would replace ρ₀ = 2.1757 by an exact ratio for the dominant part of h.

The uniform complex stationary domain and derivative transfer remain separate obligations, unchanged.

## Ranked next tests

1. **Weight-resolved product ratio for h₁ (decisive for this route).**
   - Find the generic rank of K(J^{2i})·F for a negative simple F in the two-fibre calculus. This is a tensor product of two non-line simples, so the Round 80 line rule does not cover it. It needs the boundary-weight calculus of Rounds 57/126 for tensor products of two-fibre simples.
   - Compute the exact per-simple ratio of F ↦ K(Φ_t″(S)h₁F) by the same LP method.
   - If the ratio for the h₁ part times A(h₁) = 0.4946 leaves room under 0.19359 for the rest of h (sup about 0.19), the A-price route is alive. If the exact ratio is ≥ 2 − o(1), the per-simple A-route is retired.
2. **Check reading (b1*).**
   - Confirm from Rounds 126/130/162 that the P_5000 base price dominates A on the unshifted class, so that A(R_602) < 0.01272.
   - Re-derive the O(n^{−1/2}) corrections of Lemma 4(ii) in A.
   - Without (b1*), the route falls back to the verbatim threshold: A(h) < 0.4329 in A, or < 0.4488 at best (α = 5/16).
3. **Signed alternative.** Give up the per-simple ℓ¹ structure on h, and price the frozen multiplier as Σ_j (seed part)·(Picard piece h_j) with h₁ treated exactly as a known field. The h₁-linear part of B is then an explicit operator with exactly known simples, and only h − h₁ (sup about 0.19, RMS about 0.04) needs the crude word rule.

## Replay commands and outputs

All runs were made from the repository root on 2026-11-21.
- `paley-183-cold-seed-taylor-power.py`: about 13 s, needs scipy (in `.venv`) for the support-proposing LP.
- `paley-183-cold-seed-taylor-bruteforce.py`: about 24 s.
- `paley-183-cold-h-picard-diagnostic.py`: about 1 s.

The first two certify statements about exact mathematical constants in the compact model (rational comparisons). They certify no saved rounded input. The third uses double-precision rows computed on the fly and certifies nothing.

```bash
.venv/bin/python -B research/paley-183-cold-seed-taylor-power.py
```
Output (exact rationals; timing lines removed):
```
== constants (exact; printed outward) ==
N = 4(2031/128 - 2^-17); sqrt N in [7.966725769, 7.966725770]
primes p >= 1000000: s_p <= 2.828428539 (limit 2 sqrt 2 >= 2.828427124)
varpi = sup |s_p/(2 sqrt t)| <= 0.355030238   (182 per-line factor = varpi/2)
beta0 = 256/2031 = 0.126046282..; |beta - beta0| <= delta = 0.000000216957 on Q x {p >= 1000000}

== 1. seed multiplier Phi_t'(S) = (s/(2 sqrt t)) sum_k ghat_k(beta) J^k (exact bounds) ==
k=+-1: ghat_k(beta0) in [0.478072428819, 0.478072428820] (series to l=40, tail <= 1.5e-37); uniform gamma_k = 0.478072561593
k=+-3: ghat_k(beta0) in [-0.007039456508, -0.007039456507] (series to l=40, tail <= 1.5e-37); uniform gamma_k = 0.007039589281
k=+-5: ghat_k(beta0) in [0.000156252275, 0.000156252276] (series to l=40, tail <= 1.5e-37); uniform gamma_k = 0.000156385050
k=+-7: ghat_k(beta0) in [-0.000003858441, -0.000003858440] (series to l=40, tail <= 1.5e-37); uniform gamma_k = 0.000003991214
k=+-9: ghat_k(beta0) in [0.000000100092, 0.000000100093] (series to l=40, tail <= 1.5e-37); uniform gamma_k = 0.000000232867
sign pattern: ghat_k(beta0) has sign (-1)^((|k|-1)/2) for |k| <= 9: True
sum_k |ghat_k(beta0)| (|k|<=81) = 0.970544197764 .. vs 1/sqrt(1+beta0) = [0.942370927279, 0.942370927280]  (no sign identity for odd k: l1 > sup)
compare: linear seed term has ghat_{+-1} = 1/2 each, l1 mass 1

== 2a. regression against Round 182 (linear seed, coefficient 1 on J^{+-1}) ==
alpha=0 m=1: mediant G_up = 4 (Round 182: 4); exact sup in [4.000000, 4.000000]
alpha=0 m=2: mediant G_up = 12 (Round 182: 12); exact sup in [12.000000, 12.000000]
alpha=0 m=4: mediant G_up = 104 (Round 182: 104); exact sup in [104.000000, 104.000000]
alpha=0 m=8: mediant G_up = 6928 (Round 182: 6928); exact sup in [6928.000000, 6928.000000]
alpha=1 m=1: mediant G_up = 3 (Round 182: 3); exact sup in [3.000000, 3.000000]
alpha=1 m=2: mediant G_up = 9 (Round 182: 9); exact sup in [9.000000, 9.000000]
alpha=1 m=4: mediant G_up = 75 (Round 182: 75); exact sup in [75.000000, 75.000000]
alpha=1 m=8: mediant G_up = 4915 (Round 182: 4915); exact sup in [4915.000000, 4915.000000]
regression OK: True

== 2b. full seed multiplier, exact m-step growth (J^k, |k|<=5; weights gamma_k) ==
G_m(alpha) = sup over valid simples of pi_alpha(path-summed m-step child)/pi_alpha(parent),
  ||L_S^m||_{pi_alpha} <= G_m varpi^m (+ |k|>5 perturbation).  [lo, hi] = exact primal/dual values;
  lo == hi means exact.  'med' = Round 182 mediant method.  'lin' = exact sup for the linear seed
  (coefficient 1/2 on J^{+-1}, same normalisation).  rate = G^(1/m) varpi, outward.
alpha=  0 m=1: G in [1.970483, 1.970484] (exact) med=1.970484  rate<=0.69959 | lin [2.000000, 2.000000] rate<=0.71007
alpha=  0 m=2: G in [2.940448, 2.940449] (exact) med=2.940449  rate<=0.60880 | lin [3.000000, 3.000000] rate<=0.61494
alpha=  0 m=3: G in [4.374160, 4.374161] (exact) med=4.374161  rate<=0.58063 | lin [4.500000, 4.500000] rate<=0.58615
alpha=  0 m=4: G in [6.278416, 6.278417] (exact) med=6.278417  rate<=0.56199 | lin [6.500000, 6.500000] rate<=0.56689
alpha=  0 m=5: G in [8.992637, 8.992638] (exact) med=8.992638  rate<=0.55087 | lin [9.375000, 9.375000] rate<=0.55547
alpha=  0 m=6: G in [12.751860, 12.751861] (exact) med=12.751861  rate<=0.54266 | lin [13.375000, 13.375000] rate<=0.54700
alpha=  0 m=7: G in [18.062169, 18.062170] (exact) med=18.062170  rate<=0.53679 | lin [19.062500, 19.062500] rate<=0.54094
alpha=  0 m=8: G in [25.495419, 25.495420] (exact) med=25.495420  rate<=0.53220 | lin [27.062500, 27.062500] rate<=0.53619
alpha=1/4 m=1: G in [1.776376, 1.776377] (exact) med=1.776377  rate<=0.63067 | lin [1.800000, 1.800000] rate<=0.63906
alpha=1/4 m=2: G in [2.649404, 2.649405] (exact) med=2.649405  rate<=0.57789 | lin [2.700000, 2.700000] rate<=0.58338
alpha=1/4 m=3: G in [3.894834, 3.894835] (exact) med=3.894835  rate<=0.55860 | lin [4.000000, 4.000000] rate<=0.56358
alpha=1/4 m=4: G in [5.587333, 5.587334] (exact) med=5.587334  rate<=0.54585 | lin [5.775000, 5.775000] rate<=0.55037
alpha=1/4 m=5: G in [7.976939, 7.976940] (exact) med=7.976940  rate<=0.53782 | lin [8.300000, 8.300000] rate<=0.54211
alpha=1/4 m=6: G in [11.307969, 11.307970] (exact) med=11.307970  rate<=0.53190 | lin [11.837500, 11.837500] rate<=0.53598
alpha=1/4 m=7: G in [15.999270, 15.999271] (exact) med=15.999271  rate<=0.52757 | lin [16.850000, 16.850000] rate<=0.53149
alpha=1/4 m=8: G in [22.579893, 22.579894] (exact) med=22.579894  rate<=0.52419 | lin [23.917187, 23.917188] rate<=0.52797
alpha=1/2 m=1: G in [1.646971, 1.646972] (exact) med=1.646972  rate<=0.58473 | lin [1.666666, 1.666667] rate<=0.59172
alpha=1/2 m=2: G in [2.455375, 2.455376] (exact) med=2.455376  rate<=0.55632 | lin [2.500000, 2.500000] rate<=0.56136
alpha=1/2 m=3: G in [3.575283, 3.575284] (exact) med=3.575284  rate<=0.54288 | lin [3.666666, 3.666667] rate<=0.54747
alpha=1/2 m=4: G in [5.126610, 5.126611] (exact) med=5.126611  rate<=0.53423 | lin [5.291666, 5.291667] rate<=0.53848
alpha=1/2 m=5: G in [7.299807, 7.299808] (exact) med=7.299808  rate<=0.52836 | lin [7.583333, 7.583334] rate<=0.53240
alpha=1/2 m=6: G in [10.345374, 10.345375] (exact) med=10.345375  rate<=0.52408 | lin [10.812500, 10.812500] rate<=0.52795
alpha=1/2 m=7: G in [14.624004, 14.624005] (exact) med=14.624005  rate<=0.52084 | lin [15.375000, 15.375000] rate<=0.52458
alpha=1/2 m=8: G in [20.636209, 20.636210] (exact) med=20.636210  rate<=0.51832 | lin [21.820312, 21.820313] rate<=0.52195
alpha=3/4 m=1: G in [1.554539, 1.554540] (exact) med=1.554540  rate<=0.55191 | lin [1.571428, 1.571429] rate<=0.55791
alpha=3/4 m=2: G in [2.316782, 2.316783] (exact) med=2.316783  rate<=0.54040 | lin [2.357142, 2.357143] rate<=0.54508
alpha=3/4 m=3: G in [3.347032, 3.347033] (exact) med=3.347033  rate<=0.53108 | lin [3.428571, 3.428572] rate<=0.53535
alpha=3/4 m=4: G in [4.797523, 4.797524] (exact) med=4.797524  rate<=0.52544 | lin [4.946428, 4.946429] rate<=0.52947
alpha=3/4 m=5: G in [6.816142, 6.816143] (exact) med=6.816143  rate<=0.52117 | lin [7.071428, 7.071429] rate<=0.52501
alpha=3/4 m=6: G in [9.657807, 9.657808] (exact) med=9.657808  rate<=0.51810 | lin [10.080357, 10.080358] rate<=0.52181
alpha=3/4 m=7: G in [13.641672, 13.641673] (exact) med=13.641673  rate<=0.51570 | lin [14.321428, 14.321429] rate<=0.51929
alpha=3/4 m=8: G in [19.247863, 19.247864] (exact) med=19.247864  rate<=0.51383 | lin [20.322544, 20.322545] rate<=0.51733
alpha=  1 m=1: G in [1.507428, 1.507429] (exact) med=1.507429  rate<=0.53519 | lin [1.500000, 1.500000] rate<=0.53255
alpha=  1 m=2: G in [2.212838, 2.212839] (exact) med=2.212839  rate<=0.52813 | lin [2.250000, 2.250000] rate<=0.53255
alpha=  1 m=3: G in [3.175844, 3.175845] (exact) med=3.175845  rate<=0.52186 | lin [3.250000, 3.250000] rate<=0.52589
alpha=  1 m=4: G in [4.550708, 4.550709] (exact) med=4.550709  rate<=0.51855 | lin [4.687500, 4.687500] rate<=0.52240
alpha=  1 m=5: G in [6.453392, 6.453393] (exact) med=6.453393  rate<=0.51550 | lin [6.687500, 6.687500] rate<=0.51919
alpha=  1 m=6: G in [9.142131, 9.142132] (exact) med=9.142132  rate<=0.51339 | lin [9.531250, 9.531250] rate<=0.51697
alpha=  1 m=7: G in [12.904922, 12.904923] (exact) med=12.904923  rate<=0.51162 | lin [13.531250, 13.531250] rate<=0.51510
alpha=  1 m=8: G in [18.206604, 18.206605] (exact) med=18.206605  rate<=0.51027 | lin [19.199218, 19.199219] rate<=0.51367
exact (lo == hi) in 136 of 136 (alpha, m) cases

== 3. threshold kappa*(p0) of Proposition 1/Corollary 2.1 (exact, outward) ==
(b1)  p0=0.01272, c=c(M0+u): kappa* in [0.77414706, 0.77414708]
(b1*) re-derived transfer to pi_alpha: p0' = (1+alpha) p0 [A(R_602) <= P_5000(R_602), pi_alpha <= (1+alpha)A],
      c' = ((1+alpha)/2) c(M) [Round 162/174 Taylor words: output price <= 2 rank in P_5000, <= (1+alpha) rank in pi_alpha]
(b1*) alpha=    0: kappa*_alpha in [0.83790251, 0.83790253]  (u=0.14944)
(b1*) alpha= 1/16: kappa*_alpha in [0.82777142, 0.82777144]  (u=0.14944)
(b1*) alpha=  1/8: kappa*_alpha in [0.81764032, 0.81764034]  (u=0.14944)
(b1*) alpha= 3/16: kappa*_alpha in [0.80750923, 0.80750925]  (u=0.14944)
(b1*) alpha=  1/4: kappa*_alpha in [0.79737814, 0.79737816]  (u=0.14944)
(b1*) alpha= 5/16: kappa*_alpha in [0.78724705, 0.78724707]  (u=0.14944)
(b1*) alpha=  3/8: kappa*_alpha in [0.77711595, 0.77711597]  (u=0.14944)
(b1*) alpha= 7/16: kappa*_alpha in [0.76698486, 0.76698488]  (u=0.14944)
(b1*) alpha=  1/2: kappa*_alpha in [0.75685377, 0.75685379]  (u=0.14944)
(b1*) alpha= 9/16: kappa*_alpha in [0.74672267, 0.74672269]  (u=0.14944)
(b1*) alpha=  5/8: kappa*_alpha in [0.73659158, 0.73659160]  (u=0.14944)
(b1*) alpha=11/16: kappa*_alpha in [0.72646049, 0.72646051]  (u=0.14944)
(b1*) alpha=  3/4: kappa*_alpha in [0.71632940, 0.71632942]  (u=0.14944)
(b1*) alpha=13/16: kappa*_alpha in [0.70619830, 0.70619832]  (u=0.14944)
(b1*) alpha=  7/8: kappa*_alpha in [0.69606721, 0.69606723]  (u=0.14944)
(b1*) alpha=15/16: kappa*_alpha in [0.68593612, 0.68593614]  (u=0.14944)
(b1*) alpha=    1: kappa*_alpha in [0.67580502, 0.67580504]  (u=0.14944)

== 4. budget for the non-seed part B = K((Phi'(S+h) - Phi'(S)) .) ==
h-linear multiplier Phi''(S) h = (1/(2 sqrt t)) sum_k bhat_k J^k h:
  bhat_0, bhat_2, bhat_4 at beta0: 0.915418367, -0.040726490, 0.001510249; signs alternate: True
  sum_k |bhat_k| (beta0, |k|<=80) = 1.000000000000 (sign pattern: = value at theta=pi/2 = 1);  SIG1 = l1/sqrt N <= 0.125522352
  rank rule H*J^k*F <= (|k|+2) d r:  SIGH = sum_k (|k|+2)|bhat_k| / sqrt N <= 0.273091676  (= rho_eff/(1+alpha) / sqrt N; rho_eff = (1+alpha) * 2.17565)
  => h-linear cost <= (1+alpha) A(h) SIGH;  h-higher (j>=2) cost <= (1+alpha) H(A(h)),
     H(A) = G_all(s+A) - G_all(s) - A G_all'(s), G_all(y) = y(2N-y^2)/(N-y^2)^(3/2) (seed lines counted)
  H(A=0.550000) in [0.01931, 0.01932]
  H(A=1.000000) in [0.07242, 0.07243]
  H(A=1.994573) in [0.40150, 0.40151]
Corollary 2.2 (needs C_S >= 1): ||L^m|| <= C_S (lam_S + C_S beta)^m; criterion lam_S + C_S beta < 1 - C_S (1 - kappa*)
beta_max = (1 - lam_S)/C_S - (1 - kappa*_lo);  A_max = sup A(h) with cost(A) < beta_max [lo, hi]
alpha m0 read  lam_S(<=)  C_S(<=)   beta_max(>=)  A_max in
    0  1 b1   0.69977   1.0000     0.07438   [0.2579, 0.2580]
    0  1 b1*  0.69977   1.0000     0.13813   [0.4579, 0.4580]
    0  2 b1   0.60901   1.1492     0.11440   [0.3856, 0.3857]
    0  2 b1*  0.60901   1.1492     0.17815   [0.5746, 0.5747]
    0  4 b1   0.56222   1.2449     0.12582   [0.4207, 0.4208]
    0  4 b1*  0.56222   1.2449     0.18958   [0.6067, 0.6068]
    0  8 b1   0.53244   1.3146     0.12983   [0.4329, 0.4330]
    0  8 b1*  0.53244   1.3146     0.19359   [0.6179, 0.6180]
  1/4  1 b1   0.63090   1.0000     0.14324   [0.3862, 0.3863]
  1/4  1 b1*  0.63090   1.0000     0.16648   [0.4430, 0.4431]
  1/4  2 b1   0.57814   1.0914     0.16070   [0.4290, 0.4291]
  1/4  2 b1*  0.57814   1.0914     0.18393   [0.4848, 0.4849]
  1/4  4 b1   0.54611   1.1555     0.16699   [0.4443, 0.4444]
  1/4  4 b1*  0.54611   1.1555     0.19022   [0.4996, 0.4997]
  1/4  8 b1   0.52446   1.2154     0.16541   [0.4404, 0.4405]
  1/4  8 b1*  0.52446   1.2154     0.18864   [0.4959, 0.4960]
  1/2  1 b1   0.58501   1.0000     0.18914   [0.4215, 0.4216]
  1/2  1 b1*  0.58501   1.0000     0.17185   [0.3861, 0.3862]
  1/2  2 b1   0.55661   1.0511     0.19599   [0.4354, 0.4355]
  1/2  2 b1*  0.55661   1.0511     0.17870   [0.4002, 0.4003]
  1/2  4 b1   0.53453   1.0946     0.19941   [0.4423, 0.4424]
  1/2  4 b1*  0.53453   1.0946     0.18212   [0.4072, 0.4073]
  1/2  8 b1   0.51864   1.1521     0.19199   [0.4273, 0.4274]
  1/2  8 b1*  0.51864   1.1521     0.17469   [0.3920, 0.3921]
  3/4  1 b1   0.55224   1.0000     0.22191   [0.4237, 0.4238]
  3/4  1 b1*  0.55224   1.0000     0.16409   [0.3207, 0.3208]
  3/4  2 b1   0.54072   1.0214     0.22384   [0.4270, 0.4271]
  3/4  2 b1*  0.54072   1.0214     0.16602   [0.3242, 0.3243]
  3/4  4 b1   0.52578   1.0578     0.22248   [0.4247, 0.4248]
  3/4  4 b1*  0.52578   1.0578     0.16466   [0.3217, 0.3218]
  3/4  8 b1   0.51418   1.1061     0.21337   [0.4088, 0.4089]
  3/4  8 b1*  0.51418   1.1061     0.15555   [0.3050, 0.3051]
    1  1 b1   0.53556   1.0000     0.23859   [0.4007, 0.4008]
    1  1 b1*  0.53556   1.0000     0.14025   [0.2439, 0.2440]
    1  2 b1   0.52851   1.0134     0.23943   [0.4020, 0.4021]
    1  2 b1*  0.52851   1.0134     0.14108   [0.2453, 0.2454]
    1  4 b1   0.51893   1.0374     0.23791   [0.3997, 0.3998]
    1  4 b1*  0.51893   1.0374     0.13957   [0.2428, 0.2429]
    1  8 b1   0.51066   1.0713     0.23094   [0.3889, 0.3890]
    1  8 b1*  0.51066   1.0713     0.13259   [0.2312, 0.2313]

best certified A_max per alpha and reading (max over m0 <= 8):
  b1   alpha=    0: A_max in [0.4329, 0.4330] (m0=8, lam_S<=0.53244, C_S<=1.3146, beta_max>=0.12983)
  b1   alpha= 1/16: A_max in [0.4406, 0.4407] (m0=8, lam_S<=0.53018, C_S<=1.2819, beta_max>=0.14065)
  b1   alpha=  1/8: A_max in [0.4447, 0.4448] (m0=7, lam_S<=0.53205, C_S<=1.2436, beta_max>=0.15045)
  b1   alpha= 3/16: A_max in [0.4479, 0.4480] (m0=7, lam_S<=0.52986, C_S<=1.2183, beta_max>=0.16006)
  b1   alpha=  1/4: A_max in [0.4484, 0.4485] (m0=6, lam_S<=0.53218, C_S<=1.1857, beta_max>=0.16870)
  b1   alpha= 5/16: A_max in [0.4488, 0.4489] (m0=6, lam_S<=0.53001, C_S<=1.1658, beta_max>=0.17730)
  b1   alpha=  3/8: A_max in [0.4470, 0.4471] (m0=5, lam_S<=0.53303, C_S<=1.1368, beta_max>=0.18493)
  b1   alpha= 7/16: A_max in [0.4456, 0.4457] (m0=5, lam_S<=0.53077, C_S<=1.1212, beta_max>=0.19269)
  b1   alpha=  1/2: A_max in [0.4423, 0.4424] (m0=4, lam_S<=0.53453, C_S<=1.0946, beta_max>=0.19941)
  b1   alpha= 9/16: A_max in [0.4399, 0.4400] (m0=4, lam_S<=0.53212, C_S<=1.0823, beta_max>=0.20647)
  b1   alpha=  5/8: A_max in [0.4370, 0.4371] (m0=4, lam_S<=0.52987, C_S<=1.0709, beta_max>=0.21318)
  b1   alpha=11/16: A_max in [0.4325, 0.4326] (m0=3, lam_S<=0.53407, C_S<=1.0478, beta_max>=0.21886)
  b1   alpha=  3/4: A_max in [0.4291, 0.4292] (m0=3, lam_S<=0.53141, C_S<=1.0393, beta_max>=0.22504)
  b1   alpha=13/16: A_max in [0.4248, 0.4249] (m0=3, lam_S<=0.52891, C_S<=1.0324, beta_max>=0.23048)
  b1   alpha=  7/8: A_max in [0.4203, 0.4204] (m0=2, lam_S<=0.53424, C_S<=1.0092, beta_max>=0.23568)
  b1   alpha=15/16: A_max in [0.4166, 0.4167] (m0=2, lam_S<=0.53129, C_S<=1.0037, beta_max>=0.24116)
  b1   alpha=    1: A_max in [0.4029, 0.4030] (m0=3, lam_S<=0.52224, C_S<=1.0256, beta_max>=0.24001)
  b1*  alpha=    0: A_max in [0.6179, 0.6180] (m0=8, lam_S<=0.53244, C_S<=1.3146, beta_max>=0.19359)
  b1*  alpha= 1/16: A_max in [0.5879, 0.5880] (m0=8, lam_S<=0.53018, C_S<=1.2819, beta_max>=0.19427)
  b1*  alpha=  1/8: A_max in [0.5582, 0.5583] (m0=7, lam_S<=0.53205, C_S<=1.2436, beta_max>=0.19395)
  b1*  alpha= 3/16: A_max in [0.5308, 0.5309] (m0=7, lam_S<=0.52986, C_S<=1.2183, beta_max>=0.19342)
  b1*  alpha=  1/4: A_max in [0.5036, 0.5037] (m0=6, lam_S<=0.53218, C_S<=1.1857, beta_max>=0.19194)
  b1*  alpha= 5/16: A_max in [0.4786, 0.4787] (m0=6, lam_S<=0.53001, C_S<=1.1658, beta_max>=0.19040)
  b1*  alpha=  3/8: A_max in [0.4535, 0.4536] (m0=5, lam_S<=0.53303, C_S<=1.1368, beta_max>=0.18790)
  b1*  alpha= 7/16: A_max in [0.4306, 0.4307] (m0=5, lam_S<=0.53077, C_S<=1.1212, beta_max>=0.18553)
  b1*  alpha=  1/2: A_max in [0.4072, 0.4073] (m0=4, lam_S<=0.53453, C_S<=1.0946, beta_max>=0.18212)
  b1*  alpha= 9/16: A_max in [0.3862, 0.3863] (m0=4, lam_S<=0.53212, C_S<=1.0823, beta_max>=0.17905)
  b1*  alpha=  5/8: A_max in [0.3659, 0.3660] (m0=4, lam_S<=0.52987, C_S<=1.0709, beta_max>=0.17562)
  b1*  alpha=11/16: A_max in [0.3450, 0.3451] (m0=3, lam_S<=0.53407, C_S<=1.0478, beta_max>=0.17118)
  b1*  alpha=  3/4: A_max in [0.3264, 0.3265] (m0=3, lam_S<=0.53141, C_S<=1.0393, beta_max>=0.16723)
  b1*  alpha=13/16: A_max in [0.3076, 0.3077] (m0=3, lam_S<=0.52891, C_S<=1.0324, beta_max>=0.16254)
  b1*  alpha=  7/8: A_max in [0.2894, 0.2895] (m0=2, lam_S<=0.53424, C_S<=1.0092, beta_max>=0.15760)
  b1*  alpha=15/16: A_max in [0.2728, 0.2729] (m0=2, lam_S<=0.53129, C_S<=1.0037, beta_max>=0.15295)
  b1*  alpha=    1: A_max in [0.2462, 0.2463] (m0=3, lam_S<=0.52224, C_S<=1.0256, beta_max>=0.14167)
overall best (b1): alpha=5/16, m0=6: A_max in [0.4488, 0.4489]
overall best (b1*): alpha=0, m0=8: A_max in [0.6179, 0.6180]

== 5. the blocking term: the h-linear allowance X with rho_eff A(h) < X ==
X(A) = (beta_max - (1+alpha) H(A)) * sqrt N  (best m0);  rho_eff = (1+alpha) * sum_k(|k|+2)|bhat_k|
(Round 182 units: cost = rho A/sqrt N.  182: X = 1.925 in pi_1 without Taylor; audit 182 with the
 seed-only Taylor charged: 1.094 (dimension cost) / 0.264 (doubled).)
-- reading b1
   alpha=  0 (m0=8): X <= 1.0344 (h-higher not charged), X(0.55) <= 0.8806;  rho_eff <= 2.1757 (without seed lines 2);  A(h) needed < 0.4329
   alpha=1/4 (m0=6): X <= 1.3441 (h-higher not charged), X(0.55) <= 1.1518;  rho_eff <= 2.7196 (without seed lines 5/2);  A(h) needed < 0.4484
   alpha=1/2 (m0=4): X <= 1.5888 (h-higher not charged), X(0.55) <= 1.3580;  rho_eff <= 3.2635 (without seed lines 3);  A(h) needed < 0.4423
   alpha=3/4 (m0=3): X <= 1.7930 (h-higher not charged), X(0.55) <= 1.5237;  rho_eff <= 3.8074 (without seed lines 7/2);  A(h) needed < 0.4291
   alpha=  1 (m0=3): X <= 1.9122 (h-higher not charged), X(0.55) <= 1.6045;  rho_eff <= 4.3513 (without seed lines 4);  A(h) needed < 0.4029
-- reading b1*
   alpha=  0 (m0=8): X <= 1.5424 (h-higher not charged), X(0.55) <= 1.3885;  rho_eff <= 2.1757 (without seed lines 2);  A(h) needed < 0.6179
   alpha=1/4 (m0=6): X <= 1.5292 (h-higher not charged), X(0.55) <= 1.3369;  rho_eff <= 2.7196 (without seed lines 5/2);  A(h) needed < 0.5036
   alpha=1/2 (m0=4): X <= 1.4510 (h-higher not charged), X(0.55) <= 1.2202;  rho_eff <= 3.2635 (without seed lines 3);  A(h) needed < 0.4072
   alpha=3/4 (m0=3): X <= 1.3323 (h-higher not charged), X(0.55) <= 1.0631;  rho_eff <= 3.8074 (without seed lines 7/2);  A(h) needed < 0.3264
   alpha=  1 (m0=3): X <= 1.1287 (h-higher not charged), X(0.55) <= 0.8210;  rho_eff <= 4.3513 (without seed lines 4);  A(h) needed < 0.2462
full multiplier at A(h) <= 1.994573 (conditional b2), reading b1: best power rate lam <= 1.6460 (alpha=0, m0=1, C=1.0000); needed < 1 - C(1-kappa*) = 0.7741; P_5000 one-step: 1.066
full multiplier at A(h) <= 1.994573 (conditional b2), reading b1*: best power rate lam <= 1.6460 (alpha=0, m0=1, C=1.0000); needed < 1 - C(1-kappa*) = 0.8379; P_5000 one-step: 1.066
H(A=0.550000) in [0.01931, 0.01932];  h-linear (alpha=0) <= 0.15021
H(A=1.000000) in [0.07242, 0.07243];  h-linear (alpha=0) <= 0.27310
H(A=1.994573) in [0.40150, 0.40151];  h-linear (alpha=0) <= 0.54471

== 6. seed-only Taylor terms: net effect of moving them into L_S (exact) ==
alpha=0: one-step G (full Phi'(S)) in [1.970483, 1.970484] vs linear 2: rate change -0.01047 (Round 182 crude charge for the seed-only Taylor part: +0.10425 in dimension price)
alpha=1/2: one-step G (full Phi'(S)) in [1.646971, 1.646972] vs linear 5/3: rate change -0.00699 (Round 182 crude charge for the seed-only Taylor part: +0.10425 in dimension price)
alpha=1: one-step G (full Phi'(S)) in [1.507428, 1.507429] vs linear 3/2: rate change 0.00264 (Round 182 crude charge for the seed-only Taylor part: +0.10425 in dimension price)

== 7. model heuristic (NOT a bound on A(h)): first Picard correction of h ==
h1 = K(bulk Phi_t(S)) = 2 sqrt t sum_{k even != 0} b'_k K(J^k),  b'_k Fourier of (1+beta cos^2)^(1/2);
dim K(J^k) = |k| (two-fibre rule, weights (-k,+k)); A(h1) = 2|sqrt t| sum_{k!=0} |b'_k| |k| at t = a, beta = beta0
b'_2 = 0.015286637, b'_4 = -0.000113375; A(h1) in [0.4945, 0.4946]; sup bound of h1 <= same; compare threshold 0.6179 (A-price, reading b1*) and float sup|h| ~ 0.55

ALL EXACT CHECKS OK
```

```bash
.venv/bin/python -B research/paley-183-cold-seed-taylor-bruteforce.py
```
Output (exact part, then [float] lines):
```
Round 80 rule with J^k, |k|<=5, weights |ghat_k(beta0)|: 2413 parents r=2..4, depth 3; 0 stopped (negative refill)
lemma |k|=1 (destination fibre refill exactly 0) on all parents: True
lemma |k|>=3 (r' >= r(|k|-1), refill >= 0) for |k| in 3,5,7 on all parents: True
gamma_1 = |ghat_1(beta0)| = 4.780724288197e-01
gamma_3 = |ghat_3(beta0)| = 7.039456507727e-03
gamma_5 = |ghat_5(beta0)| = 1.562522759435e-04
  alpha=  0 m=1: max weighted path ratio 1.845487 <= G 1.970484: True  (linear seed, coefficient 1/2 each: 1.875000)  argmax ((-8, 0, 0, 0), (0, 0, 0, 0))
  alpha=  0 m=2: max weighted path ratio 2.690626 <= G 2.940449: True  (linear seed, coefficient 1/2 each: 2.750000)  argmax ((-8, 0, 0, 0), (0, 0, 0, 0))
  alpha=  0 m=3: max weighted path ratio 3.941643 <= G 4.374161: True  (linear seed, coefficient 1/2 each: 4.062500)  argmax ((-8, 0, 0, 0), (0, 0, 0, 0))
  alpha=1/2 m=1: max weighted path ratio 1.588148 <= G 1.646972: True  (linear seed, coefficient 1/2 each: 1.608696)  argmax ((-8, 0, 0, 0), (0, 0, 0, 0))
  alpha=1/2 m=2: max weighted path ratio 2.323763 <= G 2.455376: True  (linear seed, coefficient 1/2 each: 2.369565)  argmax ((-8, 0, 0, 0), (0, 0, 0, 0))
  alpha=1/2 m=3: max weighted path ratio 3.343865 <= G 3.575284: True  (linear seed, coefficient 1/2 each: 3.434783)  argmax ((-8, 0, 0, 0), (0, 0, 0, 0))
  alpha=  1 m=1: max weighted path ratio 1.507424 <= G 1.507429: True  (linear seed, coefficient 1/2 each: 1.500000)  argmax ((-1, -1), (-1, -1))
  alpha=  1 m=2: max weighted path ratio 2.128104 <= G 2.212839: True  (linear seed, coefficient 1/2 each: 2.166667)  argmax ((-8, 0, 0, 0), (0, 0, 0, 0))
  alpha=  1 m=3: max weighted path ratio 3.025050 <= G 3.175845: True  (linear seed, coefficient 1/2 each: 3.100000)  argmax ((-8, 0, 0, 0), (0, 0, 0, 0))
[float] FFT ghat_k(beta0) vs exact series:
[float]   k=1: fft +4.780724288196849e-01  exact +4.780724288196849e-01
[float]   k=3: fft -7.039456507726614e-03  exact -7.039456507726618e-03
[float]   k=5: fft +1.562522759434552e-04  exact +1.562522759434533e-04
[float]   k=7: fft -3.858440125932371e-06  exact -3.858440125935048e-06
[float] sum_k |b_k| for (1+beta0 cos^2)^(-3/2): 1.000000000000005 (sign pattern => 1)
[float] signs of b_(2i), i=0..4: [1, -1, 1, -1, 1]
[float] sum_k |ghat_k| = 0.970544197764919; 1/sqrt(1+beta0) = 0.942370927279923
BRUTE FORCE CHECKS OK
```

```bash
.venv/bin/python -B research/paley-183-cold-h-picard-diagnostic.py
```
Output (floating point, evidence only):
```
compact-model prediction: RMS(h_1) ~ 0.1722, sup(h_1) <= A(h_1) in [0.4945, 0.4946]
p=10009 n=5004 final step RMS=7.0e-15: sup|h|=0.5699 RMS(h)=0.1949 | h_1: sup=0.6046 RMS=0.2074 | h-h_1: sup=0.1629 RMS=0.0407
   Picard pieces h_j (j=1..6) sup/RMS: 0.6046/0.2074  0.1675/0.0438  0.0409/0.0100  0.0088/0.0023  0.0017/0.0005  0.0005/0.0001
   sup|S|*|h_1| correlation (|<S,h_1>|/(|S||h_1|)) = 0.5596
p=100049 n=50024 final step RMS=3.9e-15: sup|h|=0.5513 RMS(h)=0.1752 | h_1: sup=0.5125 RMS=0.1762 | h-h_1: sup=0.1761 RMS=0.0409
   Picard pieces h_j (j=1..6) sup/RMS: 0.5125/0.1762  0.1833/0.0411  0.0461/0.0098  0.0095/0.0023  0.0022/0.0006  0.0006/0.0001
   sup|S|*|h_1| correlation (|<S,h_1>|/(|S||h_1|)) = 0.2084
p=400009 n=200004 final step RMS=5.8e-15: sup|h|=0.5566 RMS(h)=0.1749 | h_1: sup=0.4992 RMS=0.1732 | h-h_1: sup=0.1928 RMS=0.0415
   Picard pieces h_j (j=1..6) sup/RMS: 0.4992/0.1732  0.1866/0.0411  0.0485/0.0099  0.0110/0.0023  0.0024/0.0006  0.0006/0.0001
   sup|S|*|h_1| correlation (|<S,h_1>|/(|S||h_1|)) = 0.1060
```

Script SHA-256 at the time of this report:

- 609fb8c80a239d15368dffb1b96e38e81fab43f17dc1abaef91364ca8a6e74b5  research/paley-183-cold-h-picard-diagnostic.py
- 70b99edcad77f26af872f292efe3c6d7ff2ee98e4baa24db7cf62fdc452597b1  research/paley-183-cold-seed-taylor-bruteforce.py
- 803ac0dd2b9a41e803942212d03c396222de3b3086ae6a39c1cfe5e0d3426715  research/paley-183-cold-seed-taylor-power.py
