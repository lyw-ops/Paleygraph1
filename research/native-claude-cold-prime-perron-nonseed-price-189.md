# Round 189 native Claude draft: cold prime Perron non-seed price

- call_id: `cold-prime-perron-nonseed-price`
- Mission: `coordination/missions/round-189/cold-prime-perron-nonseed-price.md`, exported from coordinator record `coordination/round-188.json` (SHA-256 2c6221ec…).
- Author: Claude subagent started by the Round 189 coordinator (session/r189-cold-perron). Model: Claude Opus 5.5. This is an agent draft. It is not an audit, not an acceptance and not a human review.
- Input hashes verified (SHA-256). All eight match the mission export:
  - round-187-acceptance edc1d3eb…, round-188-acceptance e0face6c…, native-claude-audit-188 300664ba…
  - native-claude-cold-prime-compact-sup-growth-188 9c9b45f1…, paley-188-cold-sup-growth-certify 6ddad2ca…
  - native-claude-cold-prime-hybrid-price-186 6a597c9a…, native-claude-cold-prime-picard-leaf-inequivalence-185 45515537…, native-claude-cold-prime-signed-nonseed-price-182 c8023a9b…
- Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-188.md`, §3 and §5 of `native-claude-audit-188.md`, the cold entries of `round-188-acceptance.json`, and, for conventions and accepted statements, `native-claude-cold-prime-h1-product-rule-184.md` (Proposition A, the (b-T) rule, κ*_A) and `paley-185-cold-model.py` (its coefficient conventions; not imported).
- Scripts written by this session (all new; none imports or copies an earlier script):
  - `research/paley-189-cold-common.py`: shared layer (module). Coefficient balls by binomial series with rigorous tails, uniform on three parameter sets; pooled-operator helpers.
  - `research/paley-189-cold-seed-certify.py`: label (a). The Round 188 seed certificate on the complex square Q and for both lifts. About 1 s.
  - `research/paley-189-cold-nonseed-certify.py`: label (a). Certified lower bounds for the π_φ price of B_h and for the per-simple growth rate of L_S + B_h. 3 s at depth 8, 32 s at depth 40, about 8 min at depth 80.
  - `research/paley-189-cold-explore.py`: label (c), floating. Explicit enumeration of the Picard objects to depth 5 (cross-check of the aggregated method).
  - `research/paley-189-cold-aggregate-explore.py`: label (c), floating. The aggregated unsigned Picard model to depth 160, scaling experiments, proportional-cancellation test.

## Result summary

**Verdict: refuted** (the mission's refuted branch), in the compact model at the level of per-simple prices computed from the Picard representation of h. The decisive numbers are certified with outward arithmetic, uniformly on Q × {p ≥ 10⁶}, both lifts. The statement for the minimal (true-coefficient) per-simple price is conditional on a non-cancellation hypothesis, stated and quantified in §6. Nothing here bears on the original target.

1. **Seed certificate on Q and both lifts (Theorem 0; proved under (R80)).**
   - One rational trial vector φ (the Round 188 Perron vector, recomputed) gives ‖L_S‖_{π_φ} ≤ λ_up with C_S = 1 at every point:
     - t = a, s² = 8: λ_A ∈ [0.4995143243, 0.4995143256] (inside Round 188's bracket);
     - t ∈ Q, s² = 8: [0.4995141642, 0.4995144858];
     - t ∈ Q, s² ∈ [8, 8 + 8/(10⁶ − 1)] (every eligible p ≥ 10⁶): [0.4995141305, 0.4995147825].
   - The second lift is the fibre exchange, under which the pooled operator is unchanged (Lemma 0′).
   - Uniform non-seed budget under (b1): κ* − ‖L_S‖ ≥ **0.2746323** (≥ 0.2746325 in the compact model s² = 8). Constants c_lo = 0.617365, c_hi = 1.454513, K = 2.356002, the same as Round 188.
   - Without (b1), using only the A_𝒳 constants of Round 184 multiplied by K, the budget is ≥ 0.118583 (Remark 0.2).
2. **Exact formula for any per-simple π_φ price of a multiplier (Theorem 1; proved under (R80), (b-Jk), (b-T)).**
   - The Picard term set of h, and of every Taylor term of B_h, is closed under fibre exchange σ and weight negation ν, with equal coefficients (Lemma 1).
   - For such a multiplier, the per-simple π_φ one-step norm equals sup_{b≥1} N(b), where N(b) is an explicit functional of one symmetric measure ω on ℤ (the symmetrized slot measure of the multiplier) and of ψ_b = φ_b + φ₀(b − 1).
   - In A (ψ_b = b) the formula reduces to Round 184 Proposition A, with the supremum at large slots. In π_φ the supremum is on the slot-size-1 ray, because ψ₁/1 = c_lo is the cheapest slot and multiplication by h moves size-1 slots to larger sizes.
3. **The π_φ price of B_h is above the budget (Theorem 2; certified).** Per-simple π_φ norm of B_h (Taylor orders 1–3), Picard representation, lower bounds uniform on Q × {p ≥ 10⁶}, both lifts:

   | h truncated at Picard depth | N(1) ≥ | large-slot limit ≥ | budget (b1) ≤ |
   |---|---|---|---|
   | 3 (Round 185's truncation) | **0.294301** | 0.228833 | 0.2746331 |
   | 5 | 0.339788 | 0.262941 | |
   | 8 | 0.381648 | 0.294037 | |
   | 20 | 0.454300 | 0.347440 | |
   | 40 | 0.497644 | 0.379013 | |
   | 80 | 0.531182 | 0.403328 | |

   - So κ₀ = λ_A + β < κ* fails in π_φ already for the depth-3 truncation. The margin is 0.0197; the floating full-model value is about 0.56 (§5).
   - The *answer to the mission's alternative*: the π_φ ratio of multiplication by the actual simples of h is at least the budget.
4. **Stronger: every per-simple sup-dominating price fails (Proposition 3 and Theorem 4; proved, numbers certified).**
   - For any per-simple price π (any weights π_M ≥ dim M), the per-simple one-step norm of L = L_S + B_h is at least the growth rate λ_L of the path-summed dimension. The same holds for every power ‖L^m‖_π^{1/m}, so it applies to the one-step, the power and the Duhamel forms of Round 182.
   - λ_L is the Perron root of one pooled operator. Certified lower bounds (Collatz–Wielandt, exact rationals) with h truncated at depth D:

     | D | 3 | 5 | 8 | 20 | 40 | 80 |
     |---|---|---|---|---|---|---|
     | λ_L ≥ | 0.746485 | **0.783612** | 0.817518 | **0.875829** | 0.910330 | **0.936899** |

   - λ_L > κ*(b1) = 0.7741472 from D = 5 on, and λ_L > κ*_A = 0.8379310 (Round 184's threshold for A_𝒳) from D = 20 on.
   - So, in the compact model and with the Picard representation, no per-simple price can meet Round 182 Proposition 1 or 2 with the constants of P₅₀₀₀ (b1) or of A_𝒳. The joint Perron price of L_S + B_h (the natural repair of π_φ) is included.
5. **Floating evidence: the unsigned Picard model is near-critical (c).**
   - The depth-d unsigned mass of the nonlinear Picard pieces decays only like d^{−1.4} (0.0035 at d = 40, 0.00049 at d = 160). λ_L increases with the depth: 0.947 at D = 90, 0.961 at D = 160.
   - Scaling h₁ by 0.95 makes the model subcritical (λ_L → 0.882). Scaling by 1.05 makes it diverge (λ_L > 1 by D = 90).
   - So the actual model sits within a few per cent of the critical scale, where λ_L → 1. If so, no per-simple price can give a power rate below one, whatever its source and Taylor constants (Round 182 Remark 2.3).
6. **What is not certified: the minimal-coefficient version (§6).**
   - The h-linear term over the *linear* Picard simples of depth ≤ 5 is collision-free (Round 185 Proposition 1). It gives only N(1) ≥ 0.260050 < 0.2746 and λ_L ≥ 0.720017 < 0.7741.
   - The refutation therefore uses the nonlinear Picard pieces and the products of the Taylor terms. If the true simple decomposition cancelled part of them, the minimal price could be lower.
   - Floating, proportional test at depth 40: the π_φ refutation survives unless more than 93.9% of that per-simple mass cancels. The all-prices refutation under (b1) survives unless more than 71.7% cancels.
   - Round 185's physical evidence found only mean-field collisions of relative size about 10⁻³.

## Setup and hypotheses

- **Parameters.**
  - p ≡ 1 (mod 4) prime, n = (p − 1)/2, a = 2031/128.
  - Q is the closed complex square of half-width 2⁻¹⁷ about a, and s_p² = 8 + 8/(p − 1).
  - Compact model of Rounds 79/80/179/185: S = s cos θ, J ↔ e^{iθ}, β = s²/(4t).
  - Fourier data as accepted in Rounds 183–185 (coefficients even in the line index):
    - Φ_t(S) = 2√t Σ b′_k J^k;
    - Φ_t′(S) = (s/(2√t)) Σ ĝ_k J^k;
    - Φ_t″(S) = (2√t)⁻¹ Σ b̂_k J^k;
    - Φ_t‴(S) = −(3s/(2√t)³) Σ e_k J^k;
    - Φ_t⁗(S) = (3/(2√t)³) Σ f_k J^k.
- **Frozen-base fixed point (Rounds 182–185).** h = V₆₀₂ − S satisfies
  h = h₁ + L_S h + Σ_{m≥2} K(Φ^{(m)}(S)h^m)/m!,  h₁ = 2√t Σ_{k′ even ≠ 0} b′_{k′} K(J^{k′}).
  The non-seed multiplier is
  B_h = K((Φ_t′(S + h) − Φ_t′(S))·) = Σ_{m≥1} K((1/m!) Φ^{(m+1)}(S) h^m ·).
  - Its order-1 term is the h-linear term K(Φ″(S)h·). The orders m ≥ 2 are the higher Taylor terms.
- **Picard representation.**
  - Iterating the fixed-point identity writes h as a formal sum of model objects, indexed by expression trees. Its unsigned convergence is not proved; it is near-critical, §5. Only finite truncations enter the certified statements. Each object is a root K(J^{k′}), a transported line product K(J^k O), or a transported Taylor product K(J^c O₁ ⊗ ⋯ ⊗ O_m).
  - The coefficient of an object is the product of the Fourier coefficients along its expression tree.
  - Its depth is the number of transports minus one. A product K(Φ^{(m)} O₁ ⋯ O_m) has depth Σ d_i + m.
  - The multiplier B_h is represented by the objects J^c ⊗ O₁ ⊗ ⋯ ⊗ O_m with c of the parity of m + 1.
  - "Picard representation" below always means this indexed family, with one term per expression tree (ordered products).
- **Hypotheses (named once).**
  - (R80): the Round 80 per-simple rule (transport placement, refill, injectivity, twist exclusion), as in Round 188.
  - (b-Jk): the line shift J^c: A − c, B + c.
  - (b-T): the tensor rule, per fibre the multiset of pairwise sums, with generic rank ½Σ|w|. Round 184, accepted as a model reading.
  - (R80-4): used only through the inherited statements quoted from Round 188.
  - (b1), (H1), (H2): Round 182 Proposition 1's hypotheses for the price used (§0.2). They are stated as hypotheses. Remark 0.2 replaces (b1) by the inherited A_𝒳 inputs at the cost of the factor K.
- **Prices.**
  - π_φ(χ_M) = φ(n_M)/(2c_lo), with n_M the pooled |w|-histogram of M (Round 188). It is extended to fields by Σ|c_M|π_φ(M).
  - Per-simple norm of an operator X = Σ_j c_j K(G_j ⊗ ·): ‖X‖^{ps}_π = sup_M Σ_j |c_j| π(K(G_j ⊗ M))/π(M), taken over valid simples M. This is the unsigned path-sum bound that Rounds 182–188 use. It dominates the true operator norm.
  - The **minimal** per-simple norm uses the true simple decomposition of the multiplier. The **representation** norm uses the Picard representation. The two agree unless distinct Picard terms are isomorphic with cancelling coefficients.
- **Thresholds.**
  - κ* ∈ [0.7741471, 0.7741472]: Round 182 Proposition 1 with the P₅₀₀₀ constants, i.e. under (b1).
  - κ*_A ∈ [0.83790250, 0.83793100]: Round 184, for A_𝒳 with c_A = c(M)/2.
  - The budget is κ* − ‖L_S‖_{π_φ}. Round 188 had ≥ 0.274632 at t = a.

## 0. The seed certificate on Q and both lifts

**Lemma 0′ (both lifts; proved under (R80)).**
- The second lift acts on the compact model as the fibre exchange σ (Round 184 lift remark, Round 185 Lemma 0).
- The pooled operator P_m of Round 188 Lemma 1 sums over the two children J^{±m}. It only sees the pooled |w| histogram, which σ preserves.
- σ maps J^{±m} to J^{∓m}, and the coefficient moduli w_m = |[J^m]Φ_t′(S)| are even in m. Hence P(t) = Σ w_m(t)P_m is the same operator for both lifts. ∎

**Theorem 0 (certified; `…-seed-certify.py`).** Let φ be the rational trial vector of the script: the floating Perron vector at t = a, rationalized with denominator 2⁶⁴, tabulated for b < 300 and affine beyond.
- (i) For every t ∈ Q, every s² ∈ [8, 8 + 8/(10⁶ − 1)] and both lifts: φP(t) ≤ λ_up φ on every slot size, with λ_up = 199805913/400000000 = 0.49951478…
  - The harmonics m ≤ 23 are taken with the upper ends of their balls.
  - The tail m ≥ 25 uses |[J^m]Φ′(S)| ≤ |s/(2√t)| |β|^{(m−1)/2}/(1 − |β|), from |binom(−½, l)| ≤ 1.
  - The affine range of slot sizes is checked by slope and one value, as in Round 188.
- (ii) Lower certificate on the same region: λ_lo = 999028261/2000000000 = 0.49951413….
  - At t = a, s² = 8 the bracket is [0.4995143243, 0.4995143256].
  - On Q with s² = 8 it is [0.4995141642, 0.4995144858].
- (iii) c_lo = 0.617365 (at b = 1), c_hi = 1.454513, K = 2.356002. So π_φ is sup-dominating and ‖L_S‖_{π_φ} ≤ λ_up with C_S = 1, uniformly.
- (iv) Under (b1), the uniform non-seed budget is κ*_lo − λ_up ≥ 0.2746323 (≥ 0.2746325 at s² = 8). Its largest possible value anywhere on the region is κ*_hi − λ_lo ≤ 0.2746331.

The coefficient balls come from the binomial series of cos^jθ(1 + β cos²θ)^α with an explicit tail (`…-common.py`). At the point they reproduce Round 188's β₁/2 = 0.169730042096 to 10⁻¹². Parseval against ℓ_S² is checked.

**Remark 0.2 ((b1) replaced by inherited A_𝒳 inputs; proved as an implication).** π_φ(χ_M) ≤ K·dim M. So on Round 184's class 𝒳:
- π_φ(R₆₀₂) ≤ K·A_𝒳(R₆₀₂) < K·0.01272 (D1);
- π_φ(T(U)) ≤ K·A_𝒳(T(U)) ≤ K·c_A(M₀ + u)·π_φ(U)² whenever π_φ(U) ≤ u, using A_𝒳 ≤ π_φ;
- (H1) is the class closure of A_𝒳.

Hence the Proposition 1 threshold in π_φ is κ*_φ = 1 − K(1 − κ*_A) ≥ 0.618098, and the budget without (b1) is ≥ 0.118583. Every refutation below holds a fortiori against this smaller budget.

## 1. Symmetry and the exact per-simple formula

Let Γ = {1, σ, ν, σν} act on two-fibre weight data by σ(A, B) = (B, A) and ν(A, B) = (−A, −B).

**Lemma 1 (Γ-invariance of the Picard representation; proved under (R80), (b-Jk), (b-T)).**
- (i) σ and ν commute with ⊗, σJ^c = νJ^c = J^{−c}, K∘σ = σ∘K and ν∘K = K∘σν.
  - The last identity holds because K(νW) has A-fibre −(positives of A ∪ negatives of B), which is the A-fibre of νσK(W), and the refills agree.
- (ii) Every coefficient is even in its line index, because Φ^{(m)}(s cos θ) is even in θ. The roots satisfy νK(J^{k′}) = K(J^{k′}) and σK(J^{k′}) = K(J^{−k′}).
- (iii) By induction on the expression tree, σ maps the object of a tree to the object of the tree with all line indices negated. ν maps K(J^c ⊗ X₁ ⊗ ⋯) to K(J^c ⊗ σνX₁ ⊗ ⋯).
  - In both cases the image is an object of the representation with the same coefficient.
  - The truncations used below (|k′| ≤ 8, |k| ≤ 7, |c| ≤ 8, depth ≤ D, orders ≤ 4 and ≤ 3) are Γ-symmetric.
- (Check: in the explicit enumeration of `…-explore.py`, the aggregated two-fibre histograms of depth ≤ 3 are σ-symmetric to rounding.) ∎

For a multiplier object G with weight data (G_A, G_B), put U_G = G_A ⊎ G_B ⊎ (−G_A) ⊎ (−G_B), a symmetric multiset of 4·dim G integers. For X = Σ_j c_j K(G_j ⊗ ·) put
  ω = ¼ Σ_j |c_j| 𝟙_{U_{G_j}},  Ω = Σ_x ω(x)ψ_{|x|},  N(b) = [Σ_x ω(x)ψ_{|b+x|} + (b − 1)Ω]/ψ_b  (b ≥ 1).

**Theorem 1 (exact per-simple π_φ norm; proved under (R80), (b-Jk), (b-T)).**
- (i) If the weighted term set {(G_j, |c_j|)} is Γ-invariant, then ‖X‖^{ps}_{π_φ} = sup_{b≥1} N(b), the supremum over valid configurations.
  - The large-slot value is lim_b N(b) = |ω| + Ω/(s + φ₀), because Σ_x xω(x) = 0.
- (ii) Without invariance, ‖X‖^{ps}_{π_φ} ≥ N(b) for every b.
- (iii) With ψ_b = b (the dimension price A), sup_b N(b) = lim_b N(b) = |ω| + Σ_x ω(x)|x| = Σ_j|c_j|(d_j + μ_j/2). This is Round 184 Proposition A.

*Proof.*
1. Transport relabels fibres, drops zeros and refills. So φ(K(G ⊗ F)) = Σ ψ_{|y|} over the nonzero slots y of G ⊗ F. This depends only on the pooled |·| multiset of G ⊗ F.
2. The pooled |·| multiset of G ⊗ gF equals that of g⁻¹G ⊗ F. For σ the fibre pairing is swapped. For ν all sums change sign.
3. Hence, for the symmetrized configuration F̄ = ⊎_g gF, a slot v of F contributes Σ_j |c_j| Σ_{x∈U_{G_j}} ψ_{|v+x|} = 4Σ_x ω(x)ψ_{|v+x|}. This depends only on |v|, since U is symmetric. Also φ(F̄) = 4φ(F).
4. With n_0 = Σ_b (b − 1)n_b on valid configurations, R(F̄)/φ(F̄) is the mediant of the N(b) with weights n_bψ_b.
5. Every pooled ray occurs:
   - for b ≥ 2, take two slots b in fibre A, with b − 2 zeros in A and b zeros in B;
   - for b = 1, take (1, 1 | 1, 1).
   Since R(F̄)/φ(F̄) ≤ max_g R(gF)/φ(gF), this gives (ii).
6. Under invariance, R(gF) = R(F) for every g. So R(F)/φ(F) is exactly the mediant, which gives (i).
7. (iii): with ψ_b = b the numerator is at most |ω|b + bΣω|x|, with equality in the limit. ∎

*Remark.* The seed itself has ω(±m) = |β_m|/2, and Theorem 1 reproduces Round 188's row form. All the pooled operators below are of this one-measure type. The joint operator of L_S + B_h has ω_L = ω_seed + ω_B.

## 2. Aggregated Picard data (the computational lemma)

**Lemma 2 (linearity; proved under (R80), (b-Jk), (b-T)).** For a family of objects with weights |c_O|, put H_f(w) = Σ_O |c_O|·#{slots of weight w in fibre f of O}. Then:
- J^c ⊗ (family) has the shifted H;
- the family of products O ⊗ O′ (ordered pairs) has the fibrewise convolution H * H′;
- transport is linear on H. The nonzero slots move as in (R80), and the refill z_A(O) = Σ_slots(|w|/2 − [w < 0, f = A] − [w > 0, f = B]) is linear in the slot counts.

So the aggregate of each Picard depth, and ω of each Taylor order of B_h, follow from a finite linear recursion, with no enumeration.

Replacing every |c_O| by a certified lower bound (products of lower ends of coefficient balls) gives the exact aggregate of the same objects with smaller nonnegative weights. Because every object's histogram is nonnegative, this is an entrywise lower bound, uniform on the region. N(b) is a nonnegative combination of the entries of ω. The pooled operator is monotone in ω. So every lower bound below is monotone in these aggregates.

*Cross-checks.*
- The aggregated recursion reproduces Round 185's certified unsigned depth masses: linear 0.494524, 0.260137, 0.122824, 0.062239, 0.030629, 0.015369; nonlinear 0.024199 (depth 2), 0.040974 (depth 3), 0.043795 (depth 4) and the [float] 0.042859 (depth 5).
  - The certified script keeps more Fourier terms (roots |k′| ≤ 8, lines |k| ≤ 7, Taylor lines |c| ≤ 8 against Round 185's 6, 5, 6/5). Its lower bounds 0.040977 and 0.043801 at depths 3 and 4 therefore exceed Round 185's truncated values by under 10⁻⁵, as they should.
- The explicit enumeration of `…-explore.py` gives the same N(1) values to 10⁻⁴.

## 3. Theorem 2: the π_φ price of B_h

**Theorem 2 (certified; `…-nonseed-certify.py` §4; compact model, Picard representation, uniform on Q × {p ≥ 10⁶}, both lifts, under (R80), (b-Jk), (b-T)).** With φ the trial vector of Theorem 0, the per-simple π_φ one-step norm of B_h satisfies ‖B_h‖^{ps}_{π_φ} ≥ N_D(1), with the values in the table of the summary:
- 0.294301 for the depth-3 truncation of h (orders 1–3);
- 0.339788 at depth 5;
- 0.381648 at depth 8;
- 0.454300 at depth 20;
- 0.497644 at depth 40;
- 0.531182 at depth 80.

Each exceeds the largest possible budget 0.2746331. Hence the criterion κ₀ = λ_A + β < κ* of Round 182 Corollary 2.2 fails in π_φ. It also fails with the exact joint one-step norm sup_b[(ψP)_b + (ψQ)_b]/ψ_b. On the b = 1 ray this is ≥ λ_lo + N(1) ≥ 0.4995141 + 0.294301 = 0.793815 > κ*, because the lower seed certificate gives (ψP)_b ≥ λ_lo ψ_b on every ray.

*Proof.* Lemma 1 and Theorem 1(i) (or (ii), which needs no symmetry) on the slot-size-1 ray, with the certified aggregated ω of Lemma 2. ∎

**Where the cost sits.** Contributions to N(1) at the depth-3 truncation (floating split; total certified):

| part | N(1) |
|---|---|
| h-linear term over the roots h₁ | 0.1320 |
| h-linear term over L_S h₁, L_S² h₁, L_S³ h₁ | 0.1157 |
| h-linear term over the nonlinear pieces Q₁, L_S Q₁, X₁, C₁ | 0.0184 |
| order 2, ½Φ‴(S)h² | 0.0242 |
| order 3 | 0.0040 |

- **The slot-size-1 ray.** ψ₁ = c_lo·1 is the cheapest slot in π_φ. A multiplier weight x sends a size-1 slot to |1 + x|, whose price ψ_{|1+x|} is up to (1 + |x|)c_hi.
  - For a root K(J^{±2}) with the J⁰ line, ω(±2) = ½ and ω(0) = 1 per unit coefficient. So N(1) = ½ψ₃/ψ₁ + 3/2 = 3.950 per unit, against A's supremum 2|k| = 4. The Perron weighting that lowers the seed rate does not make multiplication by h cheaper.
  - The large-slot limit is lower (0.2288). On the seed's own Perron slot law (n₀ : n₁ : n₂ = 0.424 : 0.335 : 0.136) the ratio is 0.2505 at depth 3 but 0.2890 at depth 5 [float].
  - So even restricted to inputs with the leaves' slot law, π_φ fails once h is taken to depth 5.
- **Round 182's normalization.** At depth 3 the order-1 (h-linear) part alone costs N(1) = 0.2661 for an unsigned A(h_{≤3}) = 1.0049 [float]. This is a per-simple ratio ρ_φ = 0.2661·2√a/1.0049 ≈ 2.11, against Round 182's requirement ρ·A(h) < budget·2|√t| ≈ 2.188.
  - The h-linear term alone over the depth-3 truncation is therefore just inside the budget.
  - The h-higher Taylor terms (0.028 at b = 1) and the deeper Picard pieces push it out.
  - This is the π_φ analogue of Round 185's finding that the h-higher terms carry the decision in A.

## 4. Every per-simple price: the growth-rate obstruction

**Proposition 3 (proved under (R80), (b-Jk), (b-T), Lemma 1).** Let π be any per-simple price, i.e. a weight π_M ≥ dim M on simples extended by Σ|c_M|π_M. Let M₀ be a valid simple with π_{M₀} < ∞, and let λ_L be any number with a positive vector φ_L such that (φ_L Q_{ω_L})_a ≥ λ_L φ_{L,a} for all a ≥ 0, where ω_L is the symmetrized measure of (a sub-family of) the representation of L = L_S + B_h. Then for every m ≥ 1:
  ‖L^m‖^{ps}_π ≥ K_L⁻¹ λ_L^m dim M₀/π_{M₀},  hence  ‖L‖^{ps}_π ≥ λ_L,
and the spectral radius of L on the per-simple space of π is ≥ λ_L. Here K_L = c_hi(φ_L)/c_lo(φ_L).

*Proof.*
1. By Γ-invariance, the four path sums of L^m from gM₀ have equal dimension totals.
2. Their pooled sum evolves exactly by Q_{ω_L}, by step 3 of the proof of Theorem 1 applied at every step. This uses that the multiset of first-step outputs over a Γ-orbit is Γ-invariant, by Lemma 1(i).
3. The certificate gives φ_L(Q^m n) ≥ λ_L^m φ_L(n), and φ_L is comparable to the mass within K_L.
4. Finally π-path-sum ≥ A-path-sum ≥ ‖·‖_∞ per simple, and π-path(L^mχ_{M₀}) ≤ ‖L^m‖ π_{M₀}.
5. For the spectral radius, ‖L^m‖^{1/m} ≥ (const)^{1/m}λ_L → λ_L, and ‖L^m‖ ≥ r^m for every m (Gelfand). ∎

**Consequences for Round 182's criteria.**
- One-step (Proposition 1) needs ‖L‖ < κ*(π).
- The power form (Corollary 2.1) needs ‖L^m‖ ≤ Cλ^m with λ < 1 − C(1 − κ*) ≤ κ*.
- The Duhamel form (Proposition 2 in the Round 184 Proposition C form) needs Γ_k < 1/(1 − κ*), while Γ_k ≥ Σ_{m<k} r^m ≥ Σ_{m<k} λ_L^m.

So λ_L ≥ κ*(π) defeats all three, for every per-simple price whose provable constants give κ*(π).

**Theorem 4 (certified; `…-nonseed-certify.py` §5; same scope as Theorem 2).** ω_L consists of:
- the seed harmonics |k| ≤ 23 (lower ends of balls on the region);
- B_h orders 1–3 over the depth-D Picard truncation, entries |x| ≤ 70 kept.

Exact rational Collatz–Wielandt certificates (rows for all a < 300 + max|x|, affine range by slope and value) give:

| D | 3 | 5 | 8 | 20 | 40 | 80 |
|---|---|---|---|---|---|---|
| certified λ_L ≥ | 0.746485 | 0.783612 | 0.817518 | 0.875829 | 0.910330 | 0.936899 |
| K_L | 2.137 | 2.111 | 2.088 | 2.051 | 2.031 | 2.016 |

Hence λ_L > κ*(b1) ≤ 0.7741472 from D = 5 on, and λ_L > κ*_A ≤ 0.8379310 from D = 20 on.

In particular, the obvious repair of π_φ fails: the joint Perron price of L_S + B_h has one-step norm ≈ λ_L (floating 0.7836 at D = 5), above κ*(b1).

## 5. Floating evidence (c)

`…-aggregate-explore.py` (t = a, s² = 8, double precision, Fourier lines |c| ≤ 31; h-Taylor orders ≤ 5 for the rows to depth 90, ≤ 4 for the depth-160 row):

| h to depth | unsigned A(h) | N(1) of B_h | joint growth λ_L |
|---|---|---|---|
| 3 | 1.0049 | 0.2950 | 0.7470 |
| 5 | 1.1376 | 0.3409 | 0.7844 |
| 12 | 1.3478 | 0.4180 | 0.8466 |
| 44 | 1.5761 | 0.5083 | 0.9184 |
| 90 | 1.6626 | 0.5443 | 0.9467 |
| 160 | 1.7064 | 0.5619 | 0.9607 |

- **Near-criticality.**
  - The nonlinear depth masses decay like d^{−1.4}, with no visible exponential factor through d = 160 (0.003534, 0.001309, 0.000735, 0.000491 at d = 40, 80, 120, 160).
  - Scaling h₁ by 0.95 gives geometric decay and λ_L → 0.882. Scaling by 1.05 gives growing depth masses and λ_L = 1.141 at D = 160. At 0.8 and 0.5 the limits are 0.764 and 0.636.
  - So the unsigned Picard model of h sits within a few per cent of its critical scale, where the minimal fixed point of the unsigned recursion has Jacobian spectral radius 1.
  - The Jacobian of that recursion is exactly the per-simple L_S + B_h (N′(h) = B_h). If the model is exactly critical, λ_L → 1 and no per-simple price can have power growth below one, whatever its source and Taylor constants (Round 182 Remark 2.3).
  - The extrapolated unsigned A(h) (about 1.9 from a d^{−0.4} tail) is close to the inherited budget 4.823 − s = 1.9946 of Round 182 (b2). This suggests that the inherited dimension budget is itself near the critical point of the same majorant. That is a reading, not a computation.
- **Proportional-cancellation test.** Put ω_θ = ω_{V1} + θ(ω_{full} − ω_{V1}), where V1 is the collision-free part (h-linear term over the linear Picard simples of depth ≤ 5). The smallest surviving fraction θ that still reaches the thresholds is:
  - D = 20: θ* = 0.0751 (N(1) vs the π_φ budget), 0.3458 (λ_L vs κ*(b1)), 0.7560 (λ_L vs κ*_A);
  - D = 40: 0.0614, 0.2828 and 0.6182.
- **Explicit enumeration** (`…-explore.py`, depth ≤ 5 linear, 55,986 simples; depth ≤ 3 nonlinear, unmerged): N(1) = 0.2943 (depth-3), 0.3095 (linear to depth 5 with nonlinear to depth 3), joint λ_L = 0.7465 and 0.7590. This agrees with the aggregated method.

## 6. The minimal-coefficient question

The certified statements concern the Picard representation. For the true simple decomposition of the multiplier the situation is as follows.

- **Certified, minimal.** The h-linear term over the linear Picard simples of depth ≤ 5 has pairwise distinct multiplier simples J^{2i}X:
  - the X are pairwise inequivalent (Round 185 Proposition 1);
  - J^{2i}X ≅ J^{2i′}X′ forces i = i′ by twist exclusion (R80).

  For this part (V1): N(1) ≥ 0.260050 and λ_L ≥ 0.720017. Both are below the thresholds.

  The true coefficients of these X differ from the Picard ones by nonlinear overlaps. Round 185 bounds the opposite-sign overlaps at depth ≤ 4 (0.004225 and 0.003542/0.004351 in price units); N5 is uncertified. So V1 is a lower bound only up to those overlaps.
- **Hypothesis (NCP) (non-cancellation of the products).** In the true decomposition of Φ_t′(S + h) − Φ_t′(S), the per-simple mass of the nonlinear Picard pieces and of the order-2 and order-3 products is not cancelled beyond a fraction 1 − θ. Under (NCP) with θ ≥ 0.07 (depth 20), the minimal π_φ price exceeds the budget. With θ ≥ 0.35, every per-simple price fails under (b1) (proportional reading; floating).
- **Evidence for (NCP).** Round 185's physical Gram tests found only mean-field coincidences (trivial pairings X ⊗ X^∨ ⊇ 1) of relative size 5·10⁻⁴, at depth ≤ 3. The mean squares of Q₁, L_S Q₁ and X₁ match the no-collision model to 1%.
- **What (NCP) cannot be.** The weight-data model cannot decide it beyond depth ≈ 4 (Round 185 §6, Round 188 Remark 4.3). An invariant finer than weight data is needed.

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved here.** Exact rationals and outward arb/acb balls; uniform on Q × {p ≥ 10⁶}; both lifts.
- (a1) Lemma 0′ and Theorem 0.
  - λ_A ∈ [0.4995141305, 0.4995147825] on the region and [0.4995141642, 0.4995144858] on Q at s² = 8.
  - The point bracket [0.4995143243, 0.4995143256] lies inside Round 188's.
  - C_S = 1, K = 2.356002, budget ≥ 0.2746323 under (b1).
  - Remark 0.2: κ*_φ ≥ 0.618098 and budget ≥ 0.118583 from the A_𝒳 inputs (D1–D4) with loss K.
- (a2) Lemma 1 (Γ-invariance of the Picard representation and its truncations) and Theorem 1 (exact per-simple π_φ norm as sup_b N(b); the lower bound N(b) without invariance; reduction to Round 184 Proposition A in A).
- (a3) Lemma 2 (linearity of the aggregated recursion; monotone lower bounds).
- (a4) Theorem 2: ‖B_h‖^{ps}_{π_φ} ≥ 0.294301 (depth-3 truncation), up to ≥ 0.531182 (depth 80), against a budget ≤ 0.2746331.
- (a5) Proposition 3 and Theorem 4: every per-simple price has ‖L‖^{ps}, and the spectral radius of L in it, ≥ λ_L. Certified λ_L ≥ 0.783612 (D = 5) > κ*(b1), ≥ 0.875829 (D = 20) > κ*_A, ≥ 0.910330 (D = 40) and ≥ 0.936899 (D = 80).
- (a6) Collision-free part V1: N(1) ≥ 0.260050 and λ_L ≥ 0.720017.

All (a) statements are compact-model statements for the Picard representation. They inherit (R80), (b-Jk) and (b-T).

**(b) Conditional.**
- The comparison with the budget 0.2746 uses (b1), (H1), (H2) for π_φ. Without (b1) the budget is smaller (Remark 0.2), so the refutation is stronger.
- The comparison with κ*_A uses Round 184's D1–D4.
- Transfer of every statement from the minimal-coefficient price needs (NCP) (§6). Without it, only (a6) is certified for the minimal price, and it does not reach the thresholds.
- Transfer from the compact model to the actual multiplier at finite p is D2–D4, as before.

**(c) Evidence.**
- The near-critical scaling of the unsigned model and λ_L(160) = 0.961.
- The proportional-cancellation thresholds θ*.
- The seed-law ratios.
- The explicit-enumeration cross-checks.

## Exact remaining gap

- **For the price route as posed (π_φ):** closed negatively in the compact model, at the representation level. Theorem 2 shows a gap of at least 0.0197 at depth 3 and at least 0.223 at depth 40.
- **For any per-simple price:** Theorem 4 retires them under (b1) and against κ*_A.
  - The only per-simple escape left is a price whose *proven* source and Taylor constants give κ* > 0.936899 (certified, depth 80), or > 0.961 (floating, depth 160), possibly → 1.
  - By Round 182's table (κ*(p₀ = 10⁻³) = 0.9383485 with the same Taylor coefficient), that needs a source price of order 10⁻³ or below at depth 80, and below that at depth 160, against the proven 0.01272. If the unsigned model is exactly critical, no constants suffice.
- **For the minimal-coefficient version:** (NCP) is the open input. Equivalently, a proof that tensor products of transported simples from different Picard trees do not share opposite-sign constituents beyond mean-field pairings. This is Round 185's (MF) extended to the multiplier.
  - If (NCP) failed massively (more than 93% cancellation of the nonlinear and product per-simple mass), π_φ could survive. That would itself be a signed, leaf-cancellation argument, the mission's remaining class.
- **Unchanged:** D2–D4, (b-Jk), (b-T), the uniform complex stationary domain, derivative transfer, the angular variant's growing-height L² decoupling. The proved frozen rate stays 1.066.
- Nothing here proves or refutes the original target, the ordinary Lovász theta limit of the prime Paley localizations.

## Verdict

**Refuted.**
- In the compact model, uniformly on Q × {p ≥ 10⁶} and both lifts, with h in its Picard representation, the π_φ per-simple one-step norm of B_h is certified ≥ 0.2943 (depth-3 truncation; ≥ 0.5312 at depth 80). That is above the budget ≤ 0.2746331.
- So κ₀ = λ_A + β < κ* fails, and the π_φ ratio of multiplication by the actual simples of h is at least the budget.
- More strongly, the growth rate of the per-simple path sums of L_S + B_h is certified ≥ 0.7836 > κ*(b1) (depth 5), ≥ 0.8758 > κ*_A (depth 20) and ≥ 0.9369 (depth 80). So **per-simple sup-dominating prices of every kind are retired for the cold route** under (b1) and against κ*_A, including the joint Perron price.
- The certified range for the B_h price in π_φ is [0.294301, ∞) for the representation price. The floating full-model value is about 0.56, and it is not certified from above: the unsigned model is near-critical.
- The minimal-coefficient version rests on (NCP). The collision-free part alone (0.2601) does not reach the budget.
- Per the mission: only signed, leaf-cancellation arguments remain for the cold route. This report quantifies how much cancellation they would need.

## Ranked next tests

1. **(NCP) at depth 4–6 by a finer invariant (decisive for the minimal-coefficient reading).**
   - Find an isomorphism invariant beyond weight data (determinant or boundary character, monodromy at a second point) that separates constituents of products from different Picard trees.
   - Or prove Round 185's (MF) for the multiplier products J^c ⊗ O₁ ⊗ O₂: coincidences only through trivial pairings.
   - Outcome:
     - (NCP) with θ ≥ 0.07 makes the π_φ refutation minimal;
     - with θ ≥ 0.35, it makes the all-prices refutation under (b1) minimal;
     - massive cancellation would locate the signed mechanism the cold route needs.
2. **Exact criticality of the unsigned model.**
   - Decide whether the scale of h₁ is exactly critical for the unsigned Picard recursion. This could be done by a majorant (generating-function) argument on the pooled histogram operator, or by locating the critical scale σ_c to 10⁻⁴ (floating) and then certifying λ_L ≥ 1 − ε at large D.
   - If σ_c = 1 exactly, it is a structural fact. It ties to the inherited budget M₀ = 4.823 and kills per-simple prices with any constants.
3. **Signed (leaf-cancellation) pricing for the cold route.** Round 188 Corollary 4.1 and this report together say that any proof of confinement through prices must use cancellation between leaves or between Picard terms. The angular variant with a growing-height L² decoupling (Round 187 next test 2) is the remaining route that does not price B_h per simple. Its decoupling (D) would replace the price entirely.
4. **Do not renew:** per-simple sup-dominating prices of B_h or of L_S + B_h (π_α, π_φ, joint Perron, A, A_𝒳, hybrids with per-simple A-part) as a route to Round 182 Propositions 1–2. Also do not renew re-certification of the seed rate (closed by Theorem 0).

## Replay commands and outputs

Run from the repository root on 2026-11-21 (python-flint 0.9.0, numpy 2.3.5).

```bash
.venv/bin/python -B research/paley-189-cold-seed-certify.py          # about 1 s; label (a); ends "ALL CHECKS OK"
.venv/bin/python -B research/paley-189-cold-nonseed-certify.py 8     # 3 s; label (a); also 20 (5 s), 40 (32 s), 80 (see below)
.venv/bin/python -B research/paley-189-cold-explore.py 5             # 4 s; floating (c)
.venv/bin/python -B research/paley-189-cold-aggregate-explore.py 40 4   # about 20 s; floating (c)
P189_ROOTSCALE=0.95 .venv/bin/python -B research/paley-189-cold-aggregate-explore.py 160 4   # scaling experiment; also 1.0, 1.05
```

Key lines of the seed certificate (all 15 checks `[OK]`):
```
  region: w_1 in [0.169729987392, 0.169730174588], w_3 in [2.499215e-03, 2.499225e-03], w_5 in [5.547411e-05, 5.547451e-05]
  [OK] point value w_1 agrees with Round 188 beta_1/2 = 0.33946008419161/2 (to 1e-12)
  [OK] Parseval at the point: sum 2 w_m^2 <= l_S^2 <= that + 2 (tail)^2
  region: harmonic tail m >= 25: sum w_m <= 7.476e-12, sum m w_m <= 1.891e-10
  [float proposal] Perron root at t = a: 0.499514324350
  sha256 of the rational trial vector: d5a0d13a583d8e2e...
  point: certified dimension-price rate in [0.4995143243, 0.4995143256]  (lam_lo = 4995143243/10000000000, lam_up = 624392907/1250000000)
  qcompact: certified dimension-price rate in [0.4995141642, 0.4995144858]  (lam_lo = 2497570821/5000000000, lam_up = 2497572429/5000000000)
  region: certified dimension-price rate in [0.4995141305, 0.4995147825]  (lam_lo = 999028261/2000000000, lam_up = 199805913/400000000)
  c_lo = 0.617365 (b = 1), c_hi = 1.454513; K = 2.356002
  region: non-seed budget kappa* - ||L_S|| in [0.2746323, 0.2746331]
  (b1) replaced by the A_X inputs with loss K: ... kappa*_phi >= 1 - K (1 - kappa*_A) >= 0.618098;  budget >= 0.118583 (uniform on the region)
  psi_b for b = 0..6 (exact rationals, as floats): 0.000000 0.617365 1.722573 3.025298 4.414021 5.839968 7.282081
ALL CHECKS OK
```

Non-seed certificate, depth 8 (3 s). The trial vector has the same hash d5a0d13a… as in the seed certificate:
```
  depth  2: linear A >= 0.122837, nonlinear A >= 0.024199
  depth  3: linear A >= 0.062249, nonlinear A >= 0.040977
  depth  4: linear A >= 0.030636, nonlinear A >= 0.043801
  depth  5: linear A >= 0.015374, nonlinear A >= 0.042867
  V1: A-mass of the multiplier >= 0.123736;  N(1) >= 0.260050, ..., large-slot limit >= 0.205350
  V2: A-mass of the multiplier >= 0.134475;  N(1) >= 0.294301, N(2) >= 0.244714, N(3) >= 0.233850, N(4) >= 0.230547; large-slot limit >= 0.228833
  V3: A-mass of the multiplier >= 0.153644;  N(1) >= 0.339788, ..., large-slot limit >= 0.262941
  V4 (D = 8): A-mass of the multiplier >= 0.170923;  N(1) >= 0.381648, ..., large-slot limit >= 0.294037
  [OK] V2 (depth-3 Picard truncation): the pi_phi norm of B_h exceeds the budget on the slot-size-1 ray, uniformly
  V1: certified lambda_lo = 0.720017;  V2: 0.746485;  V3: 0.783612;  V4 (D = 8): 0.817518   (exact Collatz-Wielandt)
  [OK] V4: certified growth rate > kappa*(b1) = 0.7741472
ALL CHECKS OK
```

The same script at D = 20, 40 and 80 (5 s, 32 s, 476 s) ends `ALL CHECKS OK` with:
- D = 20: N(1) ≥ 0.454300, λ_lo = 0.875829 (> κ*_A: True);
- D = 40: N(1) ≥ 0.497644, λ_lo = 0.910330;
- D = 80: N(1) ≥ 0.531182, large-slot limit ≥ 0.403328, λ_lo = 0.936899 (K_L = 2.0164); unsigned A of the truncation ≥ 1.643875.

The aggregated zero counts stay positive (upper end of the smallest is 1.6·10⁻²⁵ at D = 80, a deep linear piece).

Floating runs (label (c)):
```
explore.py 5:   B_h (orders 1-3) N(1) = 0.309502 (b = 1); joint one-step pi_phi norm 0.809017; joint growth rate 0.759032
aggregate 90 5:  h to depth  5 (A 1.1376): N(1) = 0.34088, seed-law ratio 0.28897; joint growth rate 0.78440
                 h to depth 90 (A 1.6626): N(1) = 0.54427, joint growth rate 0.94674
aggregate 160 4: h to depth 160 (A 1.7064): N(1) = 0.56186, seed-law ratio 0.47208; joint growth rate 0.96067
                 depth 40: proportional survival needed: N(1) theta* = 0.0614; kappa*(b1) 0.2828; kappa*_A 0.6182
ROOTSCALE 0.95: h to depth 160 (A 1.4604): joint growth rate 0.88204   (geometric decay of depth masses)
ROOTSCALE 1.05: h to depth 160 (A 2.2153): joint growth rate 1.14056   (depth masses grow from d ~ 120)
```

The certified scripts concern exact constants of the compact model: rational comparisons, with arb/acb balls for the coefficients. They certify no saved rounded input. Floating vectors are only proposals and are checked exactly.

Script SHA-256 at the time of writing:
- 0be0f1ad2b7cda2d9ca6b0342577b2f1143f0aa6b5336944d180c46e1bd39532  research/paley-189-cold-common.py
- 2ea94905aaaad6dada45ad00af0770417a954b5ceaff1c3f08c3254c07ce0e31  research/paley-189-cold-seed-certify.py
- 7c03de3957f96d46ebc24f3591ea35341feaef8c08f4d690d082af2f1b01952e  research/paley-189-cold-nonseed-certify.py
- 7890033b50ff4a64dfdf124ffccd52eb49fd00e0ead617b76ebd1e4f7cfff571  research/paley-189-cold-explore.py
- f93aff04e899e03cb677d267752e9db8b447fee052805bd1d7850ad56471da7f  research/paley-189-cold-aggregate-explore.py

Nothing was committed. Files written: this report and the five scripts above.
