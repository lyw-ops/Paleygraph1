# Round 184 native Claude draft: cold prime h₁ product rule

- call_id: `cold-prime-h1-product-rule`
- Mission: `coordination/missions/round-184/cold-prime-h1-product-rule.md`, exported from coordinator record `coordination/round-183.json` (SHA-256 1231bfe2…).
- Author: a native Claude research session (Claude Opus 5.5), started by the Round 184 coordinator session. This is an agent draft. It is not an audit, not an acceptance and not a human review.
- Input hashes verified (SHA-256). All nine match the mission export:
  - round-182-acceptance 78471bc5…, round-183-acceptance aae5b4aa…, native-claude-audit-183 e2803038…
  - native-claude-cold-prime-seed-multiplier-power-rate-183 90c2eaee…, paley-183-cold-seed-taylor-power 803ac0dd…, paley-183-audit-cold-check 11681026…
  - cold-height-602-frozen-kernel-162 3ab42deb…, cold-first-prefix-step-174 8d28cc54…, native-claude-cold-prime-signed-nonseed-price-182 c8023a9b…
- Also read:
  - `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-183.md`;
  - audit §3 and §6 of `native-claude-audit-183.md`;
  - Round 182 report §§1–2 (Propositions 1–2);
  - `astra-adjoint-82.md` line 11 (definition of π and of the packet price);
  - `shifted-resolvent-96.md` lines 9–28 (P_Λ, eq. (1), and the bad-character corrections);
  - `cold-actual-first-insertion-126.md` and `cold-combined-height-130.md` (word rules and corrections);
  - `astra-dissipation-80.md` lines 82–112 (the per-simple line rule);
  - `weighted-arithmetic-57.md` lines 1–30 (the weight calculus);
  - `native-claude-cold-prime-delocalization-price-181.md` lines 84–87 (the price A);
  - the Round 183 diagnostic script, for its conventions only.
- Scripts written by this session (all new; none imports or copies a Round 183 script):
  - `research/paley-184-cold-h1-product-ratio.py`: exact integers and Fractions, plus outward python-flint balls. It contains the coefficients, the one-step ratio, validity on the cone, the exact m-step growth (seed, h₁, joint), κ*_A, H, budgets, the Duhamel criterion, model prices of the Picard tail, and the joint growth with L_S h₁. Runtime about 1 min.
  - `research/paley-184-cold-h1-bruteforce.py`: an independent forward simulation on explicit simples, child by child. Exact. About 6 s.
  - `research/paley-184-cold-h-rest-diagnostic.py`: physical rows in double precision, p up to 4·10⁶. Floating, evidence only. About 10 s.

## Result summary

**Verdict: inconclusive** (in the mission's terms). Details are at the end. In short:
- The exact one-step ratio of the h₁ simples is ≥ 2, the mission's "refuted" threshold. So one-step pricing of h₁ is retired.
- The joint multi-step treatment of L_S + B₁ is not retired. It leaves certified room A(h − h₁) < 0.3411, more than the floating sup proxy 0.19–0.22 that the mission's "supported" test names.
- But the compact model's own price of the Picard tail h − h₁ is about 0.51–0.57. That is above 0.3411.
- So the route stays alive only if the actual minimal price of h − h₁ is much closer to its sup than the unsigned model expansion. That is undecided.

1. **The exact one-step per-simple ratio has a closed form (Proposition A; proved in the compact model under (b4), (b-Jk), (b-T)).**
   - For any multiplier object G with d slots per fibre and pooled absolute weight moment μ(G), the per-simple A-ratio of F ↦ K(G·F) has supremum exactly d + μ/2 over valid simples F.
   - The supremum is approached along F_K = (A: −K, 0^{K/2−1} | B: 0^{K/2}) as K → ∞. It is attained for a single K(J^k), but not for the ± pair together.
   - One family F_K saturates every G at once. So for a signed sum of such objects the supremum is exactly Σ|c_G|(d_G + μ_G/2).
   - This is the moment-form word rule computed with the exact μ of the product J^{2i}·G. It is sharper than the factorwise word rule (|2i|+2)d only for i ≠ 0.
2. **The h₁ ratio (exact).**
   - Φ_t″(S)h₁ = Σ b̂_{2i}(β)b′_k(β) J^{2i}K(J^k), exactly; the factors 2√t cancel.
   - β₁ := sup_F A(K(Φ_t″(S)h₁F))/A(F) lies in [0.129836, 0.129840] uniformly on Q. The word rule gives 0.135052.
   - The effective ratio is ρ₁ = β₁/Σ|b′_k||k| ∈ [2.0916, 2.0917], against ρ₀ = 2.17565.
   - **K(J^{±2}) part (i = 0): the supremal ratio is exactly 2|k| = 4.** It equals the word-rule value.
   - The i = 0 terms alone force ρ ≥ 2|b̂₀| = 1.8308 for any simple (Corollary A2). The h₁ ratio therefore meets the mission's "refuted" threshold ≥ 2 − o(1) **as a one-step ratio**.
3. **Room under β_max = 0.19359 for h − h₁ (separate pricing, Round 183 power form): no.**
   - Using β₁ exactly leaves A(h − h₁) < 0.1372 (certified lower bound of the allowance, m0 = 8).
   - The floating sup proxy is sup|h − h₁| ≈ 0.21–0.22 at p ≥ 10⁶ (0.19 at p = 400009).
   - This confirms Round 183's evidence that pricing the two parts separately fails.
4. **New: the joint exact growth of L_S + B₁ (Proposition B; exact, compact model).**
   - The m-step path-summed A-growth of the seed multiplier plus the h₁-linear multiplier is computed exactly as a supremum over the extreme rays of the cone of valid simples, for m ≤ 12.
   - The 8-step rate is 0.64811, against λ_S + C_Sβ₁ = 0.7029 for the perturbative form.
   - Power form: A(h − h₁) < 0.2595 (m0 = 7).
5. **New: the Duhamel-sum criterion (Proposition C; an implication of the accepted Round 182 Proposition 2).**
   - The criterion Σ_m‖L^m‖ < 1/(1 − κ*_A) can be applied directly to the exact sequence G_m: Σ_m‖(L₀+B′)^m‖ ≤ g/(1 − β′g), where g = Σ_m G_m. This avoids the C·λ^m power form.
   - Seed only: the non-seed budget rises from 0.19359 to 0.24310. Round 183's requirement A(h) < 0.6179 becomes **A(h) < 0.7499**.
   - Separate pricing of h₁: A(h − h₁) < 0.2689.
   - **Joint L_S + B₁: A(h − h₁) < 0.3411** (certified lower bound of the allowance).
6. **(b1\*), the O(n^{−1/2}) corrections, (H1) and (H2) (Proposition D; reduced to inherited statements).**
   - Use the dimension price A_𝒳 on the Round 82/96 representation class 𝒳 (the unshifted base-pair class).
   - Then A ≤ A_𝒳 ≤ P_Λ on 𝒳 follows from Round 96 eq. (1) and π(k) ≥ k (Round 82). This is **(b1\*) without the Round 183 reading**, and gives p0 = 0.01272 for A_𝒳.
   - (H1) for A_𝒳 is literally (H1) for P_5000, because class closure does not depend on the price.
   - The O(n^{−1/2}) corrections and (H2) follow from the same Round 96/126/162 arguments. Those arguments bound the correction coefficients by absolute-coefficient × dimension sums, which are A_𝒳 quantities.
   - These are implications of inherited statements, not independent sheaf-level proofs.
7. **Evidence (c).**
   - **Floating:** sup|h| ≈ 0.607 and sup|h − h₁| ≈ 0.21–0.22 for p ∈ [10⁶, 4·10⁶] (Round 183 reported 0.557 and 0.19 at p ≤ 400009). Also sup|h − h₁ − L_S h₁| ≈ 0.05.
   - **Compact model, exact numbers, not bounds on A(h):** the unsigned per-simple prices of the explicit Picard pieces are A_ps(L_S^j h₁) = 0.2602, 0.1229, 0.0623, … They sum to ≤ 0.5067, and to about 0.567 with the first quadratic piece.
   - By the Round 80 inequivalence of leaves these are plausibly the actual model prices of the pieces. If so, A(h − h₁) ≈ 0.5–0.57 in the model, above the allowance 0.3411, unless there are cancellations between different Picard pieces.
   - **Joint growth with L_S h₁ as well (§6.3, exact):** putting the second piece L_S h₁ (model price ≤ 0.2604) into the joint operator leaves only A(h − h₁ − L_S h₁) < 0.1238. The model price of that remainder is ≈ 0.307 (floating sup ≈ 0.05). Each explicit piece added uses more budget than it removes.
   - **Floating:** the correlations between the pieces tend to 0 roughly like n^{−1/2} (from −0.40 at p = 10009 to −0.026 at p = 4·10⁶). The physical RMS(L_S h₁) = 0.0414 matches the model's coefficient structure (0.0413). Neither shows the cancellation between pieces that the route would need.

## Setup and hypotheses (inherited, as accepted in Rounds 182–183)

- p ≡ 1 (mod 4) is a large eligible prime and n = (p−1)/2. Q is the original closed square of half-width 2⁻¹⁷ about a = 2031/128, and N = 4(a − 2⁻¹⁷), so 2|√t| ≥ √N on Q. Physical mark t₀ = n, both lifts.
- Seed: S = 2√nKe₀ = s_pC with s_p ≤ 2.828428539 for p ≥ 10⁶.
- Frozen-base identity at 602 (Round 182): U_{j+1} = R + LU_j + T(U_j), with L = KD₆₀₂ = L_S + B, L_S = K(Φ_t′(S)·), B = K((Φ_t′(S+h) − Φ_t′(S))·) and h = V₆₀₂ − S.
- **Fourier data** (Round 183 Lemmas 1 and 5, accepted), with β = s²/(4t) and β₀ = 256/2031:
  - Φ_t′(S) = (s/(2√t))Σ_{k odd} ĝ_k(β)J^k;
  - Φ_t″(S) = (1/(2√t))Σ_i b̂_{2i}(β)J^{2i};
  - Φ_t(S) = 2√t Σ_i b′_{2i}(β)J^{2i}, with b′ the Fourier coefficients of (1+β cos²θ)^{1/2}.
- **First Picard piece (as defined in the mission and in Round 183 §6):** h₁ = 2√t Σ_{k even ≠ 0} b′_k(β)K(J^k). The seed comes from the mark; K of the constant is punctual and dies. So h − h₁ is *defined* as the difference, and no claim is made that h₁ equals the physical KΦ_t(S) − S.
- **Hypotheses of the compact model, per simple:**
  - (b4) The Round 80 rule: transport K keeps negative weights in their fibre, moves positive weights to the other fibre, and refills each fibre with zeros up to the generic rank r′ = ½Σ|w′|.
  - (b-Jk) J^k shifts the fibres by (−k, +k) (Round 57; Round 183 Lemma 2).
  - **(b-T) Tensor products of two-fibre simples.** For F ⊗ G, at each fibre the weights are the r·d pairwise sums w + x. The generic rank is ½ of their absolute sum.
    - This is Round 126's statement ("for a fixed full character, the normalized fiber weights under convolution add in law"), read as an identity of slot multisets, together with Katz 16.1 (Σ|w| = 2·rank).
    - For lines it is (b-Jk). Its triangle-inequality consequence is the moment-form word rule (b5) that Round 183 used.
    - A reducible product, including punctual weight-zero parts, enters linearly: slots, rank and A-price are additive over constituents.
    - *Remark (lift convention).* If a lift twist pairs F_A with G_B instead of G_A, every computation below is unchanged. The term sets {J^k}, {J^{2i}K(J^k)} and {J^{2i}K(J^kK(J^{k′}))} are closed under fibre exchange with equal coefficient moduli: exchanging fibres maps J^{2i}K(J^k) to J^{−2i}K(J^{−k}), and |b̂_{−2i}b′_{−k}| = |b̂_{2i}b′_k|.
- **Price.** A is the minimal Deligne-type price (Round 181). A_𝒳 is the same infimum restricted to the base-pair representation class 𝒳 (see §5). All per-simple statements hold for both: a per-simple bound applied to a near-optimal 𝒳-representation produces an 𝒳-representation.

## 1. The exact one-step ratio (Proposition A; proved, compact model, given (b4), (b-T))

**Proposition A.**
- Let G have fibre weight lists (G_A, G_B), each of length d, with μ(G) = Σ_{G_A}|x| + Σ_{G_B}|y|.
- For every valid negative simple F of dimension r (2r slots, Σ|w| = 2r), the product F ⊗ G has generic rank r′(F⊗G) ≤ (d + μ(G)/2)·r.
- Moreover sup_F r′(F⊗G)/r(F) = d + μ(G)/2. It is approached by F_K as K → ∞.
  For a single G it can be attained: K(J^k), k > 0, attains it at any F with F_A = 0^r. For the ± pair K(J^{±k}) together, attaining it would need F_A = F_B = 0, which is impossible, so the supremum of the sum is approached, not attained.
- For finitely many G_j and coefficients c_j:
  sup_F Σ_j|c_j| r′(F⊗G_j)/r(F) = Σ_j |c_j|(d_j + μ_j/2).

*Proof.*
- **Upper bound.** By (b-T),
  r′ = ½[Σ_{v∈F_A, x∈G_A}|v+x| + Σ_{v∈F_B, y∈G_B}|v+y|] ≤ ½[dΣ_F|v| + rμ(G)] = ½[2rd + rμ].
- **Lower bound.** F_K has r = K/2. Using |−K + x| ≥ K − |x|,
  2r′(F_K⊗G) ≥ dK − μ_A + (K/2 − 1)μ_A + (K/2)μ_B,
  so r′/r ≥ d + μ/2 − 2μ_A/K.
- **Sum.** F_K does not depend on G. So every term saturates simultaneously, and the supremum of the sum is the sum of the suprema. ∎

The script checks the F_K bracket exactly at K = 20000 for all 42 terms. It also checks the upper bound on 3000 random valid simples × 9 terms (0 violations). The brute force checks the F_K limit term by term.

**Corollary A1 (h₁).** For h₁:
- Φ_t″(S)h₁ = Σ_{i,k} b̂_{2i}(β)b′_k(β)·J^{2i}K(J^k), where 2√t·(1/(2√t)) = 1 exactly.
- G′_{ik} = J^{2i}K(J^k) has d = |k|. For k > 0 its weights are A: (−k−2i, k−2i, (−2i)^{k−2}) and B: (2i)^k; k < 0 is the fibre mirror.
- For i = 0: d + μ/2 = 2|k|, which equals the word rule (0+2)|k|.
- For i = ±1, k = ±2: 6 against the word rule 8. Further values: 10 vs 12 (2i = 4) and 14 vs 16 (2i = 6); for k = ±4: 8, 14, 20, 28 vs 8, 16, 24, 32.

Hence, exactly in the compact model and uniformly on Q × {p ≥ 10⁶} (`…-h1-product-ratio.py` §2):

  β₁ = Σ_{i,k} |b̂_{2i}b′_k|(|k| + μ_{ik}/2) ∈ [0.129836, 0.129840],  ρ₁ = β₁/Σ_k|b′_k||k| ∈ [2.0916, 2.0917].

- The lower end is the exact value at t = a. The upper end is uniform on Q, including the terms with |2i|, |k| > 6 (≤ 3.2·10⁻⁶).
- For comparison, the word rule gives Σ|b̂ b′|(|2i|+2)|k| ≤ 0.135052. With A(h₁) ≤ 0.494530 uniformly (at t = a, ≥ 0.494524) this is ρ₀A(h₁)/(2|√t|).
- **The K(J^{±2}) part:** the ratio is exactly 4 = 2|k| per unit |b′₂|. Its supremum is approached, not attained.

**Corollary A2 (floor for any per-simple product rule).**
- For any negative simple G, the i = 0 term contributes exactly 2d_G and every other term at least d_G.
- So the per-simple A-ratio of F ↦ K(Φ_t″(S)GF) is at least (2|b̂₀| + Σ_{i≠0}|b̂_{2i}|)·d_G ≥ 1.91541·d_G at β₀.
- *No per-simple one-step product rule can price the h-linear term below ρ ≈ 1.915.* For h₁ the exact value is 2.0916.

**Mission test.** The one-step ratio of the h₁ simples is ≥ 2 − o(1). Its K(J^{±2}) part is exactly 4 per unit, i.e. 2 per unit of A. This is the mission's "refuted" condition for the *one-step* per-simple A route (§2 shows what it means in budget terms). §§3–4 show that the multi-step joint treatment escapes it.

## 2. Separate pricing: is there room under β_max for h − h₁? (a, as an implication)

With the seed power form of Round 183 (re-derived below; Proposition 3 reproduced exactly), the criterion is λ_S + C_S(τ_S + β₁ + τ₁ + ρ₀X/√N + H(A(h₁) + X)) < 1 − C_S(1 − κ*_A), with X = A(h − h₁).
- τ_S ≤ 0.000386100 is the seed |k| ≥ 7 tail at ratio 1 + |k|.
- τ₁ ≤ 0.000003134 is the h₁ truncation.
- H is the Round 183 h-higher majorant, evaluated at A(h) ≤ A(h₁) + X.

| m0 | λ_S ≤ | C_S ≤ | allowance: A(h − h₁) < (certified lower bound) |
|---|---|---|---|
| 1 | 0.69959 | 1.0000 | none (fails at X = 0) |
| 4 | 0.56199 | 1.2449 | 0.1262 |
| 8 | 0.53220 | 1.3146 | **0.1372** |

The h₁ term alone uses β₁ ≈ 0.1298 of the 0.19359 budget. What is left does not cover the floating proxy sup|h − h₁| ≈ 0.21–0.22. **No room**, in agreement with Round 183's evidence. (With the Duhamel form of §4 the separate allowance is 0.2689, still not enough against the model tail of §6.)

## 3. Joint exact growth of L_S + B₁ (Proposition B; exact, compact model)

Let M₀ = ϖΣ_{|k|≤5} γ_k M_{J^k} + Σ_{|2i|,|k|≤6} c_{ik} M_{G′_{ik}}, with uniform coefficient bounds:
- ϖ ≤ 0.355030238;
- γ_k ≥ |ĝ_k(β)|: 0.478072476927, 0.007039473893, 0.000156253134;
- c_{ik} ≥ |b̂_{2i}(β)b′_k(β)|.

Each M_T maps the slot-count vector of a simple to that of its transported child under T, by (b-T) and (b4). Put G_m = sup over valid simples of r(M₀^m x)/r(x). This is the path-summed A-price of the m-step child, so ‖(L_S + B₁)^m‖_{A_𝒳} ≤ G_m in the compact model.

**Lemma B1 (validity).** For each of the 48 terms, the refills r′ − nz of the child are ≥ 0 on the whole cone of valid simples. So every child of a valid simple is valid, and G is submultiplicative.

*Proof (exact, `…-h1-product-ratio.py` §3).*
- The refill is a linear functional of the slot-count vector, so it is enough to check it on the extreme rays of the cone.
- The cone is {n_X(v) ≥ 0 for v ≠ 0; z_A, z_B ≥ 0}, where an atom "slot v in fibre X" carries |v|/2 − 1 own zeros and |v|/2 other zeros. Its extreme rays are:
  - single atoms with |v| ≥ 2;
  - pairs of a |v| = 1 atom with a partner that makes the violated zero constraint tight: (±1 in X) + u in the other fibre, weights |u| : 1; or (±1 in X) + u in X with |u| ≥ 3, weights (|u|−2) : 1.
- A ray with both zero constraints tight needs opposite z-vectors, so it reduces to a pair of a |v| = 1 slot in A and one in B.
- All rays with |v|, |u| ≤ 40 were checked: 0 negative refills, minimum 0.
- For |v| > max|x| the refill is affine in |v| along each ray family, with nonnegative slope. That is checked for single atoms; pair families are checked up to |u| = 40. ∎

The brute force also checks every explicit child of 120 random parents at depth 2 (joint) and depth 3 (seed).

**Lemma B2 (exact supremum).**
- G_m is the maximum over the extreme rays, because a ratio of linear functionals on a polyhedral cone attains its supremum on extreme rays or their limits.
- For |v| > mW, where W is the largest shift of one step, the descendants of the slot v never change sign. So the adjoint value φ_m(v, X) is affine in v.
- So along each ray family the ratio is linear-fractional, hence monotone, for |v| ≥ mW + 1. The supremum there is the larger of the value at mW + 1 and the limit.
- The script computes φ_m exactly by the backward (adjoint) recursion in integers over the common denominator 10¹⁵. It evaluates all rays up to mW + 4 and takes the limits. It checks the vanishing second differences, i.e. the affine tails. ∎

*Regression.*
- With Round 183's printed γ_k, the seed-only sequence reproduces Proposition 3 of Round 183 to all printed digits: 1.970484, 2.940449, 4.374161, 6.278417, 8.992638, 12.751861, 18.062170, 25.495420. This is an independent re-implementation: adjoint and extreme rays here, against a primal–dual LP there.
- With the tighter γ_k of this session the values are slightly lower (25.495034 at m = 8).
- The brute force finds the joint path sums of explicit simples below the certified G₁, G₂ and approaching them along F_K: 0.829311 at K = 4000 vs 0.829417, and 0.544439 vs 0.544535.

**Proposition B (values, exact suprema rounded up; seed part with ϖ included).**

| m | G_m(L_S) | G_m(L_S + B₁) | rate L_S | rate L_S + B₁ |
|---|---|---|---|---|
| 1 | 0.699581 | 0.829417 | 0.69959 | 0.82942 |
| 2 | 0.370632 | 0.544535 | 0.60880 | 0.73793 |
| 4 | 0.099749 | 0.217293 | 0.56199 | 0.68275 |
| 8 | 0.006436 | 0.031128 | 0.53220 | 0.64811 |
| 12 | 0.000403 | 0.004348 | 0.52133 | 0.63561 |

- At m = 1 the joint value is exactly the sum G₁(L_S) + β₁, since F_K saturates both.
- For m ≥ 2 the joint growth is far below the perturbative C_S(λ_S + C_Sβ₁)^m. Saturation does not persist: an L_S-child of F_K carries ±1 weights, and on those slots K(J^{+2}) is not saturated.
- The joint t = a values agree with the uniform ones to 10⁻⁶.

In the power form, λ_J + C_J(τ_S + τ₁ + ρ₀X/√N + H(A(h₁)+X)) < 1 − C_J(1 − κ*_A). The best case is m0 = 7 (λ_J ≤ 0.65336, C_J ≤ 1.2757): **A(h − h₁) < 0.2595**.

## 4. The Duhamel-sum criterion (Proposition C; a, as an implication of Round 182 Proposition 2)

Round 182 Proposition 2 (accepted) needs σ_k + Γ_k c u² < u, with Γ_k = Σ_{m<k}‖L^m‖ and σ_k ≤ Γ_k p0 (unsigned). In the dimension price, with c_A = c(M)/2 (Round 183 Lemma 4(ii)), this holds for some admissible u iff

  Γ_k < 1/(1 − κ*_A),  1 − κ*_A = inf_u [p0/u + c(M0+u)u/2].

**Proposition C.**
- Suppose ‖L₀^a‖ ≤ G_a for a ≥ 0 (G₀ = 1) and ‖B′‖ ≤ β′ in the same price, and put g = Σ_{a≥0} G_a.
- Then Σ_{m≥0}‖(L₀+B′)^m‖ ≤ g/(1 − β′g) whenever β′g < 1.
- Hence Γ_k < 1/(1 − κ*_A) for every k, provided β′ < 1/g − (1 − κ*_A).

*Proof.*
- Expand (L₀+B′)^m into words L₀^{a₀}B′L₀^{a₁}⋯B′L₀^{a_j}.
- A word with j factors B′ has norm ≤ β′^j∏G_{a_i}.
- Summing over all a_i ≥ 0 and j ≥ 0 gives Σ_jβ′^jg^{j+1}.
- The tail Σ_{a>12}G_a is bounded by submultiplicativity: G_{12q+j} ≤ G₁₂^qG_j. ∎

This replaces Corollary 2.1/2.2 (λ < 1 − C(1−κ*)) and loses no power-form constant. Per-step O(n^{−1/2}) relative corrections multiply G_a by (1 + O(n^{−1/2}))^a. Since G_a decays geometrically this changes g by o(1), and the strict slack absorbs it.

Numbers (certified, outward):
- κ*_A ∈ [0.83790250, 0.83793100] (certifying u = 747/5000; the upper end is a coarse partition), so 1/(1 − κ*_A) ≥ 6.16912.
- g_S = Σ G_m(L_S) ≤ 2.467879, and g_J = Σ G_m(L_S + B₁) ≤ 3.290671.

| setting | budget β′_max ≥ | requirement (certified allowance) |
|---|---|---|
| (a) seed only, all of h by the word rule (Round 183 setting) | 0.24310 (power form 0.19359) | **A(h) < 0.7499** (power form 0.6179) |
| (b) seed only; h₁ by its exact one-step ratio; h − h₁ by the word rule | 0.24310 | A(h − h₁) < 0.2689 |
| (c) joint L_S + B₁; h − h₁ by the word rule | 0.14179 | **A(h − h₁) < 0.3411** |
| (d) as (c) with the per-simple floor ρ ≥ 1.91541 for h − h₁ (optimistic) | 0.14179 | A(h − h₁) < 0.3710 |
| (e) joint L_S + B₁ + B₂′ (§6.3); rest = h − h₁ − L_S h₁ by the word rule | 0.08830 | A(rest) < 0.1238 |

In (c), the margin at given values is: at A(h − h₁) = 0.19, β′ ≤ 0.08331 against the budget 0.14179; at 0.25, 0.10599; at 0.30, 0.12542.

## 5. (b1\*), the O(n^{−1/2}) corrections, (H1) and (H2) for the dimension price (Proposition D)

**Definition.**
- 𝒳 is the unshifted represented class of Rounds 82/96: rows admitting finite representations f = Σ a_jH_j by negative terms H_j whose boundary characters lie in the base pair, and their closure in the finite field.
- For f ∈ 𝒳, A_𝒳(f) := inf Σ|a_j| r(H_j) over these representations.

**D1 ((b1\*)): A ≤ A_𝒳 ≤ P_Λ on 𝒳, for every Λ ≥ 1.** (a, from definitions accepted in Rounds 82/96/181)
- Round 96 eq. (1) prices a term by P_Λ(H) = Σ_kπ(k)h_k + Λb_H, with rank identity r = Σ_k k h_k + b_H.
- On the base pair b_H = 0. With π(k) ≥ k (Round 82 line 11) this gives P_Λ(H) ≥ r(H).
- P_Λ(f) is the infimum over the same representations of Σ|a_j|P_Λ(H_j). So P_Λ ≥ A_𝒳.
- A ≤ A_𝒳 by minimality of A (Round 181 line 87). This uses the reading that the P-class terms are traces, or lift averages of traces, of Frobenius-fixed geometric simples. That is the only reading left.
- Hence **A_𝒳(R₆₀₂) ≤ P₅₀₀₀(R₆₀₂) < 0.01272** (Round 174, including its vanishing error). This is p0 for A_𝒳 without Round 183's reading of "dominates … the dimension budget".
- Round 96 also states sup domination for this sum ("It is at least r, so the absolute-coefficient sum … bounds the coordinate sup norm").
- Every Round 183 statement made for A holds verbatim for A_𝒳, because the per-simple bounds and the Taylor word bound produce 𝒳-representations. The bound M0 = 4.823 is Round 174's dimension bound for V₆₀₁ + sE, hence for V₆₀₂, and it is an 𝒳-dimension bound.
- **The requirement in §4 is therefore A_𝒳(h − h₁) < 0.3411.** That is what any proof would produce in any case, since A ≤ A_𝒳.

**D2 (O(n^{−1/2}) corrections in A_𝒳).** (implication of inherited statements)
- Unshifted inputs differ from the compact-model per-simple operators only at the physical base coordinate. Round 126: "Missing full-character products and the marked derivative difference occur only at the physical base coordinate". Round 96 line 28 gives at most two cyclic coordinates in general.
- At that coordinate the product error of two single objects is at most twice the product of their convolution dimensions (Round 96).
- After K these errors are multiples of Ke₀. Ke₀ is a base-pair term of 𝒳-price √p/n (Round 82: π(1) = 1, r = 1).
- Summing the absolutely convergent word expansions with absolute coefficient × dimension gives:
  - for the linear part, A_𝒳(LU − L^{mod}U) ≤ C_L n^{−1/2}A_𝒳(U);
  - for the Taylor part, A_𝒳(T(U) − T^{bulk}(U)) ≤ C_T n^{−1/2}A_𝒳(U)² on A_𝒳(U) ≤ u.
- The constants C_L, C_T are the convergent dimension sums of Rounds 126/162/174: they depend on M0, the radius margin and the curvature bound, but not on U, j, t or the lift.
- The cited proofs state these bounds in the π-price. Their coefficient bounds are dimension sums ("twice the product of their convolution dimensions"; "uniformly by the convergent dimension sum"), so they apply to A_𝒳 unchanged.
- I did not re-derive the sheaf-theoretic inputs (Katz's fibre theorem, compact-support dimension estimate).

**D3 ((H1) for A_𝒳).**
- Class closure is a property of 𝒳, not of the price: R ∈ 𝒳, L𝒳 ⊂ 𝒳, and T(U) ∈ 𝒳.
- This is exactly the statement already used for P₅₀₀₀:
  - Round 96 lines 12–13: products and transport create no new boundary character;
  - Round 126: the corrections are multiples of Ke₀;
  - Ke₀ has boundary characters in {ξ, χξ} with ξ trivial, i.e. the base pair (Round 96 line 9).
- So (H1) for A_𝒳 ⟺ (H1) for P₅₀₀₀ (inherited; the Round 182 audit reads it from Rounds 126/130/174).

**D4 ((H2) for A_𝒳).**
- P(R) ≤ p0 + ε comes from D1.
- ‖L^m‖ ≤ G_m(1 + O(n^{−1/2}))^m comes from Proposition B with D2.
- P(T(U)) ≤ (c(M)/2 + O(n^{−1/2}))P(U)² comes from Round 183 Lemma 4(ii) with D2.
- The ε are uniform in U, j, t and the lift.

**Status.**
- D1 is proved from accepted definitions. The single residual reading is that P-class terms are A-admissible; it is not needed if A_𝒳 is used throughout.
- D2–D4 reduce (b3) and the correction part of (b1\*) to the *same* inherited Round 96/126/162/174 statements that P₅₀₀₀ already relies on. They are not independent sheaf-level proofs.

## 6. Evidence (c)

### 6.1 Floating physical rows (`…-h-rest-diagnostic.py`; real t = a, one lift, double precision)

| p | sup\|h\| | sup\|h₁\| | sup\|h−h₁\| | RMS(h−h₁) | sup\|h−h₁−h₂\| | sup\|h−h₁−L_Sh₁\| | sup\|L_Sh₁\| |
|---|---|---|---|---|---|---|---|
| 10009 | 0.5699 | 0.6046 | 0.1629 | 0.0407 | 0.0381 | 0.0421 | 0.1781 |
| 400009 | 0.5566 | 0.4992 | 0.1928 | 0.0415 | 0.0502 | 0.0479 | 0.1872 |
| 1000033 | 0.6063 | 0.4957 | 0.2207 | 0.0419 | 0.0502 | 0.0544 | 0.2033 |
| 2000029 | 0.6074 | 0.4890 | 0.2161 | 0.0421 | 0.0498 | 0.0491 | 0.2022 |
| 4000037 | 0.6065 | 0.4934 | 0.2095 | 0.0423 | 0.0536 | 0.0530 | 0.2010 |

- The sup over the n sampled coordinates grows with p and settles near sup|h| ≈ 0.61 and sup|h − h₁| ≈ 0.21–0.22. Round 183 sampled only p ≤ 400009 and reported 0.557 and 0.19.
- The proxies A_𝒳(h) ≥ 0.61 and A_𝒳(h − h₁) ≥ 0.22 are below the allowances 0.7499 (a) and 0.3411 (c).

### 6.2 Compact-model prices of the Picard tail (exact numbers about model objects; not bounds on A_𝒳(h))

- L_S h₁ = s Σ ĝ_k b′_{k′} K(J^kK(J^{k′})); the 2√t cancels.
- The path-summed price of L_S^j h₁ is 2|√t|Σ|b′_{k′}|φ_j^S(K(J^{k′})), with φ^S the seed adjoint. Uniformly on Q, for j = 1…12:
  0.2602, 0.1229, 0.0623, 0.0307, 0.0154, 0.0077, 0.0039, 0.0020, 0.0010, 0.0005, 0.0003, 0.0002.
  Their sum is ≤ 0.5067.
- The first quadratic piece Q₁ = ½K(Φ_t″(S)h₁²) costs ≤ 0.0242, and Σ_j L_S^jQ₁ costs ≤ 0.0598.
- Unsigned model estimate: A(h − h₁) ≈ 0.57, against the certified allowance 0.3411.
- Round 80 (leaves of the leading field are mutually inequivalent) suggests these path sums are the actual model A-prices of the individual pieces. A(h − h₁) could then be smaller only through cancellation *between* different pieces.
- For h₁ the sup equals the price (sup|h₁| ≈ 0.49 against 0.4945). For L_S h₁ the sup is only about 0.77 of the price (0.20 against 0.26).
- The higher pieces spread over more, and larger, simples whose phases do not align at one coordinate. So sup is a poor proxy for their A-price, and the mission's "≈ 0.19" proxy for A(h − h₁) understates the model price by a factor of about 2.6.

### 6.3 Joint growth with L_S h₁ as well (exact, compact model)

Write h = h₁ + h₂′ + rest with h₂′ := L_S h₁ = s Σ ĝ_k b′_{k′} C_{k,k′}, where C_{k,k′} = K(J^kK(J^{k′})) is the explicit transported child, |k| ≤ 5 and |k′| ≤ 4. These are 24 simples of dimensions 3, 6, 7, 10, 13 and 20.
- B₂′ = K(Φ_t″(S)h₂′·) has the terms J^{2i}C_{k,k′}, |2i| ≤ 4, with coefficient |b̂_{2i}|·s|ĝ_kb′_{k′}|/(2|√t|).
- A_ps(h₂′) ≤ 0.2604.
- The one-step exact ratio of B₂′ is ≤ 0.06870, against the word rule 0.07110.
- The truncation tail is ≤ 1.22·10⁻⁴.

| m | G_m(L_S + B₁) | G_m(L_S + B₁ + B₂′) |
|---|---|---|
| 1 | 0.829417 | 0.898114 |
| 2 | 0.544535 | 0.645201 |
| 4 | 0.217293 | 0.307269 |
| 8 | 0.031128 | 0.062857 |

- g ≤ 3.993529, so β′_max ≥ 0.08830.
- **Allowance: A(h − h₁ − L_S h₁) < 0.1238** (certified lower bound).
- The model price of that remainder is Σ_{j≥2}A_ps(L_S^jh₁) + A_ps(Σ_jL_S^jQ₁) ≈ 0.307. Floating sup ≈ 0.05.

So the ratio of allowance to model price falls from 0.3411/0.567 ≈ 0.60 (h₁ joint) to 0.1238/0.307 ≈ 0.40 (h₁ and L_S h₁ joint). Treating more Picard pieces exactly does not close the gap in the model. The model A-price of the whole of h (≈ 0.49 + 0.57 ≈ 1.06) is too large for the dimension-price criterion in any of the forms computed here; the best is A(h) < 0.7499 (seed only, Duhamel). This is evidence, not a certified failure:
- the comparison uses model prices (exact numbers about model objects);
- it relies on the Round 80-type inequivalence of leaves (not proved here for J^{odd} multipliers and K(J^{2i}) roots);
- a sufficient criterion that fails does not refute confinement.

### 6.4 Correlations between pieces (floating, same runs)

| p | ⟨h₁, h−h₁⟩ | ⟨h₁, L_Sh₁⟩ | ⟨L_Sh₁, rest⟩ | RMS(L_Sh₁) | RMS(rest) |
|---|---|---|---|---|---|
| 10009 | −0.3961 | −0.3627 | −0.5798 | 0.0459 | 0.0107 |
| 400009 | −0.0787 | −0.0759 | −0.1107 | 0.0414 | 0.0102 |
| 4000037 | −0.0263 | −0.0241 | −0.0383 | 0.0414 | 0.0104 |

- These are normalized inner products. They decay roughly like n^{−1/2}, consistent with a finite-p effect of the mark.
- In the limit the pieces are orthogonal, as distinct simples would be.
- The model RMS values 0.1722 (h₁) and 0.0413 (L_S h₁), computed from the coefficients as if each simple were distinct and unit-normalized, match the physical 0.1724 and 0.0414.
- So the coefficient structure that the model prices of §6.2 use is confirmed physically. No ℓ²-visible cancellation between pieces appears.

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved here.** Compact model, per simple, under (b4), (b-Jk), (b-T); exact rationals or outward balls for every number.
- (a1) Proposition A: sup_F r′(F⊗G)/r(F) = d + μ(G)/2 exactly, simultaneously for all G along F_K. Corollary A1: β₁ ∈ [0.129836, 0.129840] and ρ₁ ∈ [2.0916, 2.0917]. The K(J^{±2}) part has ratio exactly 2|k|. Corollary A2: the floor ρ ≥ 1.91541 for any per-simple one-step rule.
- (a2) Lemma B1: validity of the tensor rule on the whole cone, for the 48 terms and for the 120 B₂′ terms of §6.3 (both checked exactly on the rays). Lemma B2: exact suprema by extreme rays with affine tails.
- (a3) Proposition B: exact G_m(L_S + B₁) for m ≤ 12. Exact reproduction of Round 183 Proposition 3 from its γ_k.
- (a4) Proposition C: the Duhamel-sum criterion β′ < 1/g − (1 − κ*), as an implication of Round 182 Proposition 2. Its budgets and allowances: A(h) < 0.7499 (seed only), A(h − h₁) < 0.2689 (separate), A(h − h₁) < 0.3411 (joint). Every allowance is a certified lower bound.
- (a5) D1: A ≤ A_𝒳 ≤ P_Λ on 𝒳, from Round 96 eq. (1) and Round 82. Hence p0 = 0.01272 for A_𝒳, i.e. (b1\*) for A_𝒳.

**(b) Conditional / inherited.**
- (b4), (b-Jk): as in Round 183. (b-T): Round 126's "weights add in law", read as pairwise sums with the equality r′ = ½Σ|w′| (Round 80 form); the Round 183 word rule (b5) is its consequence.
- D2–D4: the O(n^{−1/2}) corrections, (H1) and (H2) for A_𝒳 are reduced to the inherited Round 96/126/162/174 statements (the same ones used for P₅₀₀₀). They are not re-proved at sheaf level. The reading "P-class terms are A-admissible" is needed only for A itself, not for A_𝒳.
- Lemma 4(ii) of Round 183 (c_A = c/2) and Lemma 5 (H majorant), as accepted.
- The decomposition h = h₁ + (h − h₁) uses h₁ as defined in the mission. The certified statements are about the operator with that explicit h₁.

**(c) Evidence.** Floating sups; model Picard-tail prices (exact numbers about model objects, not bounds on the physical A_𝒳(h)); the §6.3 comparison.

## Exact remaining gap

To make the cold criterion usable along the A-price route one must prove, uniformly in n, t ∈ Q and both lifts:

- **A_𝒳(V₆₀₂ − S − h₁) < 0.3411**, with the joint L_S + B₁ growth and the Duhamel criterion (or < 0.7499 for A_𝒳(V₆₀₂ − S) in the simpler seed-only form). In addition:
  - D2–D4, i.e. the inherited Round 96/126/162/174 statements used for P₅₀₀₀, re-read for A_𝒳 (no new estimate);
  - the hypotheses (b4), (b-Jk), (b-T).

Present status of the main input:
- Only A(h) ≤ 1.9946 is available, and it is conditional on (b2).
- Floating sups (≈ 0.22, ≈ 0.61) are compatible with both allowances.
- The compact model's unsigned price of the Picard tail (≈ 0.57, of which the linear tail alone is ≈ 0.51) is not.
- Treating L_S h₁ jointly as well lowers the remaining allowance to 0.1238, against a model price of about 0.307 for the remainder (§6.3).

The uniform complex stationary domain and derivative transfer remain separate obligations, unchanged.

## Verdict

**Inconclusive overall; the one-step sub-question is refuted.** Measured against the mission's definitions:

- **The question as posed: exact per-simple ratio, and room under β_max = 0.19359.**
  - The exact one-step ratio of F ↦ K(Φ_t″(S)h₁F) is ρ₁ ∈ [2.0916, 2.0917] (β₁ ∈ [0.129836, 0.129840]).
  - Its K(J^{±2}) part is exactly 2|k| = 4 per unit |b′₂|, i.e. 2 per unit of A: the word rule is attained.
  - That is ≥ 2 − o(1), the mission's "refuted" condition.
  - Separate pricing under the Round 183 power form leaves only A(h − h₁) < 0.1372. This is below the floating sup proxy 0.21–0.22, so there is **no room**.
- **"Retires the per-simple A route" does not follow.**
  - The joint exact growth of L_S + B₁ (Proposition B) with the Duhamel-sum criterion (Proposition C) leaves A_𝒳(h − h₁) < 0.3411. That is above the floating sup proxy.
  - By the letter of the "supported" clause ("leaving A(h − h₁) ≲ 0.19 feasible") the route is alive.
  - The seed-only requirement improves from A(h) < 0.6179 to A(h) < 0.7499.
- **Against this:**
  - The compact model's own prices of the Picard tail are A_ps(h − h₁) ≈ 0.57, with the linear tail alone ≤ 0.5067. They exceed 0.3411.
  - Adding L_S h₁ to the joint operator makes the gap worse (0.1238 against ≈ 0.307).
  - The floating evidence shows no cancellation between pieces.
  - So the route stays alive only if the true minimal price A_𝒳(h − h₁) is far below the unsigned model expansion. The evidence does not suggest that.
- **Returned, as the inconclusive branch asks.**
  - The exact ratio of the K(J^{±2}) part is 4 per unit |b′₂| (= 2|k|), supremum approached along F_K.
  - The remaining budget for the h − h₁ term (h-linear plus higher) is β′_max ≥ 0.14179 in the joint Duhamel form, so A(h − h₁) < 0.3411.
  - The seed-only budget is β′_max ≥ 0.24310, so A(h) < 0.7499.
  - With L_S h₁ also joint, β′_max ≥ 0.08830 and A(rest) < 0.1238.
- **Scope.** Nothing here proves or refutes the original target, the ordinary Lovász theta limit of the prime Paley localizations.
  - The proved frozen rate is still 1.066 (P₅₀₀₀).
  - Γ_{k_n} is not shown to be bounded uniformly in n.
  - All certified statements are compact-model, per-simple statements under (b4), (b-Jk), (b-T), with D2–D4 reduced to inherited inputs.

## Ranked next tests

1. **Inequivalence of the Picard-tail leaves (decisive for the A-price route).**
   - Extend Round 80's leaf-inequivalence argument from J^{±1} to the full seed multiplier (J^{odd}) acting on the roots K(J^{2i}), and *across* the pieces h₁, L_S^jh₁, L_S^jQ₁.
   - If the leaves are mutually inequivalent, the computed prices are the model A-prices: A(h − h₁) ≥ 0.50 > 0.3411 and A(h) ≳ 0.99 > 0.7499 in the model. The per-simple A route is then retired, and the cold route returns to Criterion D or sup transfer, as the mission's refuted branch says.
   - If collisions with opposite signs exist, compute the signed model A(h) exactly to depth 3. That decides whether 0.3411 is reachable.
   - The test should also certify the failure on the model side through exact lower bounds: Proposition A gives G₁(L_S + B_h) = G₁(L_S) + β_h exactly along F_K.
2. **A price in which multiplying by h costs its sup, not its Fourier-algebra norm.**
   - Proposition C with the seed priced per simple tolerates any non-seed cost β′ < 0.24310.
   - If h-multiplication cost ρ₀·sup|h|/√N + H(sup|h|), the floating sup|h| ≈ 0.61 would pass the seed-only requirement (< 0.7499) with margin.
   - This needs a hybrid price: per-simple dimension price for the seed structure, and a sup or counting-type bound for the non-seed multiplier. Prove the hybrid's analogue of Proposition B, i.e. how L_S acts on the counting part. The Round 128 counting rate 0.5145 and the Round 177 rate 0.545 are the natural inputs.
3. **Certified joint growth with the full model h (depth ≥ 3).**
   - The exact adjoint method of `…-h1-product-ratio.py` scales to a few hundred terms (§6.3 used 168).
   - Depth 3 needs about 10³ terms, i.e. a vectorised exact implementation.
   - It turns the extrapolation of §6.3 into a certified model statement. It matters only if test 1 finds cancellations.

## Replay commands and outputs

All runs were made from the repository root on 2026-11-21 with python-flint 0.9.0. Runtimes: about 53 s, 6 s and 10 s.
- The first two scripts certify statements about exact constants of the compact model: rational comparisons and outward balls. They certify no saved rounded input.
- Lines tagged [float] in the first script, and the whole third script, are double-precision evidence.

```bash
.venv/bin/python -B research/paley-184-cold-h1-product-ratio.py
```
Output (timing lines removed):
```
== 0. constants (exact rationals / outward arb) ==
N = 4(2031/128 - 2^-17); sqrt N >= 7.966725769;  1/sqrt N <= 0.125522082
varpi = s_up/sqrt N <= 0.355030238;  s_p <= 2.828428539 (p >= 10^6)
beta0 = 256/2031; |beta - beta0| <= delta = 0.000000216957;  |sqrt t| <= 3.983365279

== 1. Fourier coefficients (exact brackets at beta0; uniform bounds on Q x {p>=10^6}) ==
ghat_+-1: [0.478072428819, 0.478072428820]  uniform |.| <= 0.478072476927
ghat_+-3: [-0.007039456508, -0.007039456507]  uniform |.| <= 0.007039473893
ghat_+-5: [0.000156252275, 0.000156252276]  uniform |.| <= 0.000156253134
ghat_+-7: [-0.000003858441, -0.000003858440]  uniform |.| <= 0.000003858476
ghat_+-9: [0.000000100092, 0.000000100093]  uniform |.| <= 0.000000100095
bhat_+-0: [0.915418367922, 0.915418367923]  uniform |.| <= 0.915418577549
bhat_+-2: [-0.040726489718, -0.040726489717]  uniform |.| <= 0.040726603131
bhat_+-4: [0.001510249329, 0.001510249330]  uniform |.| <= 0.001510258432
bhat_+-6: [-0.000052273431, -0.000052273430]  uniform |.| <= 0.000052273958
b'_+-2:  [0.015286637450, 0.015286637451]  uniform |.| <= 0.015286666447
b'_+-4:  [-0.000113374043, -0.000113374042]  uniform |.| <= 0.000113374540
b'_+-6:  [0.000001681780, 0.000001681781]  uniform |.| <= 0.000001681793
rho_0 = sum_k (|k|+2)|bhat_k| : at beta0 >= 2.175608; uniform <= 2.175646 (Round 183: 2.17565)
sum_k |b'_k||k| : at beta0 >= 0.062073723; uniform <= 0.062074356
A(h_1) <= 2|sqrt t| sum|b'_k||k| <= 0.494530 on Q;  at t=a: >= 0.494524  (Round 183 model value [0.4945, 0.4946] at t=a)

== 2. one-step per-simple A-ratio of F -> K(G F): exactly d_G + mu(G)/2 (Prop. A) ==
for all 42 terms J^2i K(J^k), |2i|<=6, |k|<=6: F_K ratio <= d+mu/2 and within 2(d+mu)/K of it at K=20000: True
  i=0: d + mu/2 = 2|k| (= the word rule (|0|+2)|k|, attained); table of d+mu/2 vs word (|2i|+2)|k|:
  k=+-2: 2i=0: 4 vs 4; 2i=2: 6 vs 8; 2i=4: 10 vs 12; 2i=6: 14 vs 16
  k=+-4: 2i=0: 8 vs 8; 2i=2: 14 vs 16; 2i=4: 20 vs 24; 2i=6: 28 vs 32
triangle bound r' <= (d+mu/2) r on 3000 random valid simples x 9 terms: violations = 0
beta_1 := sup_F A-ratio of F -> K(Phi''(S) h_1 F) = sum |bhat b'|(d+mu/2):
   at beta0 >= 0.129836;  uniform on Q <= 0.129840  (word rule: <= 0.135052)
effective ratio rho_1 = beta_1 / sum|b'_k||k| in [2.0916, 2.0917]  (word rule rho_0 = 2.17565; the i=0 terms alone force rho_1 >= 2|bhat_0|, Cor. A2)
K(J^+-2), i=0 part alone: ratio exactly 2|k| = 4 per unit |b'_2| (not attained; approached by F_K)

== 3. validity of the rule on the cone of valid simples (exact) ==
extreme rays (singles |v|>=2; pairs with a |v|=1 slot), |v| <= 40: 780; all valid: True
refills r' - nz on every ray for 48 terms (6 seed lines, 42 h_1 terms): negative in 0 cases; minimum 0
  (for |v| > max|x| the refill is affine in |v| on each ray family; slopes checked below)
  asymptotic single-atom refill slopes negative: 0 (pair families: checked up to |u|=40)

== 4. exact m-step growth G_m = sup_valid A(path-summed m-step child)/A(parent) ==
4a. seed multiplier, weights gamma_k (|k|<=5), regression against Round 183 Prop. 3 (alpha=0):
   m=1: G <= 1.970481 (finite rays 1.859376, |v|->inf limit 1.970481, affine tails True)  [Round 183: 1.970484]
   m=2: G <= 2.940439 (finite rays 2.797690, |v|->inf limit 2.940439, affine tails True)  [Round 183: 2.940449]
   m=3: G <= 4.374138 (finite rays 4.192036, |v|->inf limit 4.374138, affine tails True)
   m=4: G <= 6.278372 (finite rays 6.053742, |v|->inf limit 6.278372, affine tails True)  [Round 183: 6.278417]
   m=5: G <= 8.992556 (finite rays 8.712162, |v|->inf limit 8.992556, affine tails True)
   m=6: G <= 12.751719 (finite rays 12.401249, |v|->inf limit 12.751719, affine tails True)
   m=7: G <= 18.061933 (finite rays 17.619604, |v|->inf limit 18.061933, affine tails True)
   m=8: G <= 25.495034 (finite rays 24.933493, |v|->inf limit 25.495034, affine tails True)  [Round 183: 25.495420]
4a'. same with the Round 183 printed gamma_k (0.478072561593, 0.007039589281, 0.000156385050):
   m=1: 1.970484; m=2: 2.940449; m=3: 4.374161; m=4: 6.278417; m=5: 8.992638; m=6: 12.751861; m=7: 18.062170; m=8: 25.495420   [Round 183: 1.970484, 2.940449, 4.374161, 6.278417, 8.992638, 12.751861, 18.062170, 25.495420]
4b. h_1 part alone (one step, uniform weights): G_1 <= 0.129837; Section 2 closed form beta_1 <= 0.129837; agree within coefficient rounding (<= 10^-12): True
4c. joint L_S + B_1 (varpi gamma_k on J^k, |k|<=5; |bhat b'| on J^2i K(J^k), |2i|,|k|<=6):
    m   G_m(seed, varpi)   G_m(joint, uniform)   G_m(joint, at t=a lower)   rate seed  rate joint
    1         0.699581             0.829417                 0.829416    0.69959   0.82942   affine True argmax ('s', 16, 0)
    2         0.370632             0.544535                 0.544533    0.60880   0.73793   affine True argmax ('s', 28, 0)
    3         0.195745             0.348024                 0.348022    0.58063   0.70341   affine True argmax ('s', 40, 0)
    4         0.099749             0.217293                 0.217292    0.56199   0.68275   affine True argmax ('s', 52, 0)
    5         0.050724             0.134538                 0.134537    0.55087   0.66953   affine True argmax ('s', 64, 0)
    6         0.025537             0.082810                 0.082809    0.54266   0.66021   affine True argmax ('s', 76, 0)
    7         0.012842             0.050820                 0.050819    0.53679   0.65336   affine True argmax ('s', 88, 0)
    8         0.006436             0.031128                 0.031127    0.53220   0.64811   affine True argmax ('s', 100, 0)
    9         0.003224             0.019045                 0.019044    0.52862   0.64397   affine True argmax ('s', 112, 0)
    10         0.001613             0.011644                 0.011643    0.52571   0.64064   affine True argmax ('s', 124, 0)
    11         0.000807             0.007116                 0.007115    0.52333   0.63790   affine True argmax ('s', 136, 0)
    12         0.000403             0.004348                 0.004347    0.52133   0.63561   affine True argmax ('s', 148, 0)

== 5. kappa*_A (b1*), h-higher majorant H, and the allowance for A(h - h_1) ==
kappa*_A in [0.83790250, 0.83793100] (certifying u = 747/5000); Round 183: [0.83790251, 0.83790253]
H(0.550000) in [0.01931, 0.01932]   (Round 183: 0.01932 / 0.07243 / 0.40151)
H(1.000000) in [0.07242, 0.07243]   (Round 183: 0.01932 / 0.07243 / 0.40151)
H(1.994573) in [0.40150, 0.40151]   (Round 183: 0.01932 / 0.07243 / 0.40151)
perturbations per step: seed |k|>=7: tau_S <= 0.000386100;  h_1 beyond |2i|,|k| <= 6: tau_1 <= 0.000003134

Criterion (Cor. 2.2 of Round 182, Prop. 2): lam + C beta' < 1 - C(1 - kappa*_A).
(I) separate pricing (Round 183 form, with the exact one-step beta_1 of Section 2):
     beta' = tau_S + beta_1 + tau_1 + rho_0 X/sqrt N + H(A(h_1)+X),  X = A(h - h_1)
   m0=1: lam_S <= 0.69959, C_S <= 1.0000: A(h-h_1) allowed below (none: X=0 already fails)
   m0=2: lam_S <= 0.60880, C_S <= 1.1492: A(h-h_1) allowed below >= 0.0942
   m0=3: lam_S <= 0.58063, C_S <= 1.2049: A(h-h_1) allowed below >= 0.1156
   m0=4: lam_S <= 0.56199, C_S <= 1.2449: A(h-h_1) allowed below >= 0.1262
   m0=5: lam_S <= 0.55087, C_S <= 1.2700: A(h-h_1) allowed below >= 0.1311
   m0=6: lam_S <= 0.54266, C_S <= 1.2892: A(h-h_1) allowed below >= 0.1342
   m0=7: lam_S <= 0.53679, C_S <= 1.3033: A(h-h_1) allowed below >= 0.1360
   m0=8: lam_S <= 0.53220, C_S <= 1.3146: A(h-h_1) allowed below >= 0.1372
(II) joint exact growth of L_S + B_1, perturbed by the rest:
     beta' = tau_S + tau_1 + rho_0 X/sqrt N + H(A(h_1)+X)
   m0=1: lam_J <= 0.82942, C_J <= 1.0000: A(h-h_1) allowed below (none: X=0 already fails)
   m0=2: lam_J <= 0.73793, C_J <= 1.1240: A(h-h_1) allowed below >= 0.1568
   m0=3: lam_J <= 0.70341, C_J <= 1.1792: A(h-h_1) allowed below >= 0.2064
   m0=4: lam_J <= 0.68275, C_J <= 1.2149: A(h-h_1) allowed below >= 0.2318
   m0=5: lam_J <= 0.66953, C_J <= 1.2389: A(h-h_1) allowed below >= 0.2465
   m0=6: lam_J <= 0.66021, C_J <= 1.2563: A(h-h_1) allowed below >= 0.2562
   m0=7: lam_J <= 0.65336, C_J <= 1.2757: A(h-h_1) allowed below >= 0.2595
   m0=8: lam_J <= 0.64811, C_J <= 1.2965: A(h-h_1) allowed below >= 0.2587
   m0=9: lam_J <= 0.64397, C_J <= 1.3132: A(h-h_1) allowed below >= 0.2579
   m0=10: lam_J <= 0.64064, C_J <= 1.3269: A(h-h_1) allowed below >= 0.2572
   m0=11: lam_J <= 0.63790, C_J <= 1.3409: A(h-h_1) allowed below >= 0.2551
   m0=12: lam_J <= 0.63561, C_J <= 1.3554: A(h-h_1) allowed below >= 0.2520
(III) as (II) with rho_floor = 2|bhat_0| + sum_(i!=0)|bhat_2i| >= 1.91541 for h - h_1 (no per-simple rule can price a generic simple of h - h_1 below this; an optimistic bound):
   m0=4: A(h-h_1) allowed below >= 0.2535
   m0=8: A(h-h_1) allowed below >= 0.2825
   m0=12: A(h-h_1) allowed below >= 0.2752

== 6. direct Duhamel sum: criterion sum_m ||L^m||_A < 1/(1 - kappa*_A) ==
1/(1 - kappa*_A) >= 6.16912;  g_S = sum_m G_m(seed) <= 2.467879;  g_J = sum_m G_m(joint) <= 3.290671
budget beta'_max = 1/g - (1 - kappa*):  seed only >= 0.24310 (power form, Round 183: 0.19359);  joint >= 0.14179
(a) seed only, all of h by the word rule (Round 183 setting): A(h) allowed below >= 0.7499  (power form: 0.6179)
(b) seed only, h_1 by its exact one-step ratio, h - h_1 by the word rule: A(h - h_1) allowed below >= 0.2689
(c) joint L_S + B_1, h - h_1 by the word rule: A(h - h_1) allowed below >= 0.3411
(d) as (c) with the per-simple floor rho_floor for h - h_1 (optimistic): >= 0.3710
    (c) at A(h-h_1) = 0.19: beta' <= 0.08331 vs budget >= 0.14179
    (c) at A(h-h_1) = 0.25: beta' <= 0.10599 vs budget >= 0.14179
    (c) at A(h-h_1) = 0.30: beta' <= 0.12542 vs budget >= 0.14179

== 7. compact-model evidence: unsigned per-simple prices of the Picard tail of h ==
A_ps(L_S^j h_1), j=1..12 (uniform on Q): 0.2602, 0.1229, 0.0623, 0.0307, 0.0154, 0.0077, 0.0039, 0.0020, 0.0010, 0.0005, 0.0003, 0.0002
sum_(j>=1) A_ps(L_S^j h_1) <= 0.5067  (tail after j=12 by G_1(seed) = 0.6996 per step)
A_ps(Q_1), Q_1 = (1/2) K(Phi''(S) h_1^2) <= 0.0242;  A_ps(L_S^j Q_1) summed over j >= 0 <= 0.0598 (crude: by G_j(seed))
unsigned model estimate of A(h - h_1): about 0.567 (linear tail + first quadratic piece; higher pieces not included)
compare: certified allowance (c) >= 0.3411;  floating sup|h - h_1| ~ 0.21-0.22 (p >= 10^6)
[float] model RMS(h_1) = 0.1722, model RMS(L_S h_1) = 0.0413  (physical, p = 4000037: 0.1724, 0.0414)

== 8. joint exact growth of L_S + B_1 + B_2' (B_2' = K(Phi''(S) L_S h_1 .)), and the allowance for rest ==
h_2' = L_S h_1: 24 simples C_(k,k'), dims [3, 6, 7, 10, 13, 20]; A_ps(h_2') <= 0.2604; tail tau_2 <= 0.000122
validity (Lemma B1) for the 120 B_2' terms on the 780 rays (|v| <= 40) and asymptotic single-atom slopes: negative cases = 0
one-step exact ratio of B_2' (Prop. A): <= 0.06870  (word rule rho_0 A(h_2')/sqrt N <= 0.07110)
    m   G_m(L_S+B_1)   G_m(L_S+B_1+B_2')
    1     0.829417       0.898114   affine True
    2     0.544535       0.645201   affine True
    3     0.348024       0.450255   affine True
    4     0.217293       0.307269   affine True
    5     0.134538       0.207915   affine True
    6     0.082810       0.139898   affine True
    7     0.050820       0.093860   affine True
    8     0.031128       0.062857   affine True
g = sum_m G_m(L_S+B_1+B_2') <= 3.993529;  budget beta'_max >= 0.08830
(e) joint L_S + B_1 + B_2', rest = h - h_1 - L_S h_1 by the word rule: A(rest) allowed below >= 0.1238
    compact-model unsigned price of rest: sum_(j>=2) A_ps(L_S^j h_1) + A_ps(sum_j L_S^j Q_1) about 0.307;  floating sup|h - h_1 - L_S h_1| ~ 0.05
ALL EXACT CHECKS OK
```
Notes on the output:
- "argmax" in 4c is the finite-ray argmax. The supremum is the |v| → ∞ limit (see 4a, where both are printed).
- The upper end of the κ*_A bracket comes from a coarse partition. Only its lower end, which is certified, is used.

```bash
.venv/bin/python -B research/paley-184-cold-h1-bruteforce.py
```
```
(1) 120 random valid parents (r<=4), joint 48 terms m<=2 and seed m<=3: every child valid (no negative refill, Sigma|w| = 2r): True
(2) max path-summed ratio, joint: m=1 0.676903 <= 829417/1000000: True;  m=2 0.417300 <= 108907/200000: True
    seed: m=1 0.567798 <= 699581/1000000: True; m=2 0.284991 <= 46329/125000: True; m=3 0.143909 <= 39149/200000: True
    family F_K (A: -K, 0^(K/2-1) | B: 0^(K/2)):
      K=   40: joint m=1 0.818847, m=2 0.535054; seed m=1 0.690705
      K=  400: joint m=1 0.828359, m=2 0.543586; seed m=1 0.698693
      K= 4000: joint m=1 0.829311, m=2 0.544439; seed m=1 0.699491
    (certified sups: joint 0.829417 / 0.544535, seed 0.699581; approached from below)
(3) F_K, K=20000: each h_1 term's ratio within 2(d+mu)/K below d+mu/2: True
    sum |bhat b'| ratio on F_K = 0.129833 (closed form beta_1 at beta0 = 0.129836..)
BRUTE FORCE OK
.venv/bin/python -B research/paley-184-cold-h1-bruteforce.py  6.16s user 0.01s system 99% cpu 6.173 total
```

```bash
.venv/bin/python -B research/paley-184-cold-h-rest-diagnostic.py
```
Output (floating point, evidence only):
```
[float] t = a = 2031/128, one real lift, double precision; evidence only
[float]       p   sup|h|  RMS(h) | sup|h1|  RMS(h1) | sup|h-h1| RMS(h-h1) argmax | sup|h-h1-h2| | sup|h-h1-L_S h1| sup|L_S h1|
[float]    10009 0.5699  0.1949 | 0.6046  0.2074 | 0.1629   0.0407  j=353     | 0.0381      | 0.0421           0.1781   (final step RMS 7.0e-15)
[float]          correlations: <h1, h-h1> -0.3961; <h1, L_S h1> -0.3627; <L_S h1, rest> -0.5798; <h1, rest> +0.0513; RMS(L_S h1) 0.0459, RMS(rest) 0.0107
[float]   100049 0.5513  0.1752 | 0.5125  0.1762 | 0.1761   0.0409  j=5357    | 0.0469      | 0.0515           0.1841   (final step RMS 3.9e-15)
[float]          correlations: <h1, h-h1> -0.1404; <h1, L_S h1> -0.1375; <L_S h1, rest> -0.2048; <h1, rest> -0.0001; RMS(L_S h1) 0.0418, RMS(rest) 0.0101
[float]   400009 0.5566  0.1749 | 0.4992  0.1732 | 0.1928   0.0415  j=37303   | 0.0502      | 0.0479           0.1872   (final step RMS 5.8e-15)
[float]          correlations: <h1, h-h1> -0.0787; <h1, L_S h1> -0.0759; <L_S h1, rest> -0.1107; <h1, rest> -0.0125; RMS(L_S h1) 0.0414, RMS(rest) 0.0102
[float]  1000033 0.6063  0.1756 | 0.4957  0.1726 | 0.2207   0.0419  j=258454  | 0.0502      | 0.0544           0.2033   (final step RMS 6.0e-15)
[float]          correlations: <h1, h-h1> -0.0495; <h1, L_S h1> -0.0479; <L_S h1, rest> -0.0704; <h1, rest> -0.0093; RMS(L_S h1) 0.0414, RMS(rest) 0.0103
[float]  2000029 0.6074  0.1761 | 0.4890  0.1724 | 0.2161   0.0421  j=108253  | 0.0498      | 0.0491           0.2022   (final step RMS 6.1e-15)
[float]          correlations: <h1, h-h1> -0.0355; <h1, L_S h1> -0.0341; <L_S h1, rest> -0.0493; <h1, rest> -0.0083; RMS(L_S h1) 0.0414, RMS(rest) 0.0104
[float]  4000037 0.6065  0.1764 | 0.4934  0.1724 | 0.2095   0.0423  j=895978  | 0.0536      | 0.0530           0.2010   (final step RMS 6.2e-15)
[float]          correlations: <h1, h-h1> -0.0263; <h1, L_S h1> -0.0241; <L_S h1, rest> -0.0383; <h1, rest> -0.0109; RMS(L_S h1) 0.0414, RMS(rest) 0.0104
.venv/bin/python -B research/paley-184-cold-h-rest-diagnostic.py  10.99s user 0.09s system 99% cpu 11.095 total
```

Script SHA-256 at the time of this report:

- fa25f9bf78a61dc0278887548ca2dda9bcbc3fd3774964557f3ead4a4cafdcd7  research/paley-184-cold-h1-product-ratio.py
- f77657888b18d6c5132c80e249e464f34309aa74fa8b566dd1ad856b92687810  research/paley-184-cold-h1-bruteforce.py
- 53dbaec5f52a2ce4e2147fd7543f2dba9a0c34dbdb8dbb946d4410ff6e10a0ed  research/paley-184-cold-h-rest-diagnostic.py

