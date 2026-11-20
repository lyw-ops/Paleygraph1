# Round 182 native Claude draft: cold prime signed non-seed price

- call_id: `cold-prime-signed-nonseed-price`
- agent_label: `session/r182-cold-price`
- Mission: `coordination/missions/round-182/cold-prime-signed-nonseed-price.md` (record `coordination/round-181.json`, SHA-256 f237fdab…)
- Author: a native Claude research session. This is an agent draft. It is not an audit, not an acceptance and not a human review.
- Scripts written by this session (replay commands and outputs are in the last section):
  - `research/paley-182-cold-criterion-check.py`: exact rationals. Covers the Proposition 1 and 2 constants, the threshold bracket and the crude multiplier costs.
  - `research/paley-182-cold-seed-power-check.py`: exact integers and rationals. Computes the one-step and m-step growth of the seed-linear multiplier under the Round 80 per-simple rule.
  - `research/paley-182-cold-fixedpoint-diagnostic.py`: floating-point numpy diagnostic of the actual stationary row. Evidence only.
- Input hashes were verified (SHA-256) and all match the mission export:
  - round-180-acceptance 489e1a25…
  - round-181-acceptance ad983e94…
  - native-claude-cold-prime-delocalization-price-181 dff5a06d…
  - native-claude-audit-181 08ac949c…
  - paley-181-cold-kantorovich-check b0b6842f…
  - cold-growing-prefix-delocalization-180 3a8eb51a…
  - cold-seed-centered-larger-tube-177 12c7cff4…
  - cold-first-prefix-step-174 8d28cc54…

## Result summary

**Outcome: inconclusive.** No price is certified with κ0 < 0.774. The proved frozen rate is still 1.066 for P_5000. What changed:

1. **Proposition 1 is restated and re-proved (a).** It is stated for an abstract sup-dominating seminorm price. The audit's two hypotheses are explicit: (H1) closure of the price class under the recursion, and (H2) correction constants uniform over inputs. The proof shows exactly how (H2) is used: one prime threshold p₁, independent of j, absorbs all corrections through the strict slack.
2. **The exact threshold of this criterion is κ* ∈ [0.7741471, 0.7741472] (a, exact rationals),** with p0 = 0.01272 and the Round 174 coefficient c(M0+u).
   - The value is attained near u ≈ 0.1087, where c(M0+u) ≤ 1.001215.
   - The audit's κ0 < 0.77395 is also exact, but it is the threshold for the non-optimal fixed ball u = 0.113 with c rounded up to 1.0043. It remains a valid sufficient value; it is not the sharp threshold of the form.
3. **New: a finite-horizon Duhamel form (Proposition 2, a).** It replaces the one-step rate by the price resolvent Γ_k = Σ_{m<k} ‖L^m‖_P over the Round 173 horizon k = k_n, and the source price by the signed source σ_k = max_j P(Σ_{i<j} L^i R_602).
   - It needs only power bounds, and only for m < k_n.
   - With ‖L^m‖ ≤ Cλ^m the condition is exactly λ < 1 − C(1−κ*).
   - It also proves a necessity statement: any use of either criterion needs Γ_{k_n} bounded uniformly in n. The one-step bound 1.066 cannot supply that. A tiny source price (the p0 ≤ 10⁻⁶ alternative) changes only the number, to κ* ∈ [0.9980707, 0.9980708]; it does not remove the need for a power rate below one.
4. **The Round 181 seed rates are re-proved, and their m-step growth is computed (a, compact model, per simple).**
   - Plain dimension price: rate 4·s_p/(4|√t|) → 0.71006.
   - Weighted price π₁ = r + z: rate 3·s_p/(4|√t|) → 0.53255.
   - The m-step growth G_m is computed exactly for m ≤ 8. Example: α = 1 gives rate 0.51366 at m0 = 8, with constant 1.0749.
   - Through the perturbation lemma (Corollary 2.2), the best non-seed one-step budget available from the seed is:
     - 0.24159 in π₁ (one step);
     - 0.12439 in plain dimension price (8-step power form, up from 0.06409 for one step).
5. **The blocking term is the non-seed multiplier, now quantified.** The h-linear term alone needs ρ·A(h) < 1.925 (π₁) or < 0.991 (dimension, power form), where ρ is the per-simple rank-growth factor.
   - The provable ρ is 4 (π₁) or 2 (dimension).
   - The conditional bound is A(h) ≤ 1.9946. This requires the seed to be designated in V_602's representation, which is unproved.
   - So the crude costs are 1.0015 (π₁) and 0.5007 (dimension). The crude higher Taylor non-seed cost is another 0.6462.
   - Floating evidence (c): the actual stationary row has physical sup|h| ≈ 0.55 and RMS(h) ≈ 0.175 at p up to 4·10⁵. This is far below the 1.963 sup bound of Round 177.
   - Since A(h) ≥ sup|h| on the coset, the evidence rules out the plain dimension price (power form needs A(h) < 0.496). It also rules out π₁ with the crude ratio ρ = 4 (needs A(h) < 0.481).
   - What survives is a weighted price with a proved non-seed ratio ρ ≲ 3.5 and A(h) close to its sup lower bound, with the higher Taylor terms folded into the same 0.24 budget.

## Setup recalled

- **Parameters.**
  - p ≡ 1 (mod 4) is a large eligible prime and n = (p−1)/2.
  - a = 2031/128, and Q is the original closed complex square of half-width 2⁻¹⁷ about a.
  - N = 4(a − 2⁻¹⁷), so |√t| ≥ √N/2 on Q.
  - Physical mark t₀ = n, both lifts, genuine nine-center start.
- **Map.**
  - V_{h+1} = KΦ_t(V_h), with Φ_t(x) = √(4t + x²) coordinatewise (t_i = t off the mark, t₀ = n).
  - K is the real symmetric circulant with ‖K‖_{2→2} ≤ 1.
  - R_h = V_{h+1} − V_h, and D_h = diag Φ_t′(V_h).
  - The seed is S = 2√n K e₀ = s_p C, where s_p = 2√(p/n) ↓ 2√2 and C = Re J for the Jacobi line J (Round 80).
- **Frozen-base identity at 602 (exact, every j ≥ 0).** Put U_j = V_{602+j} − V_602, L = KD_602, R = R_602 and T(U) = K(Φ_t(V_602+U) − Φ_t(V_602) − D_602U). Then
  U₀ = 0,  U_{j+1} = R + L U_j + T(U_j).
  Proof: U_{j+1} = KΦ_t(V_602+U_j) − V_602 = T(U_j) + LU_j + (KΦ_t(V_602) − V_602), and KΦ_t(V_602) − V_602 = R. The identity needs V_602 + U_j to lie in the analytic domain of Φ_t. This holds on the Round 177 polydisk of radius 3/8 about V_602, whose radicand margin includes the mark.
- **Inherited fixed inputs (not re-proved here; cited as in Rounds 162/174/177).** These hold for all sufficiently large eligible p, uniformly on Q and both lifts.
  - P_5000(R_602) < p0 = 0.01272 (Round 174).
  - ‖KD_602‖_{P_5000} < 1.066 (Round 162).
  - P_5000(T(U)) ≤ c(M)P(U)² + O(n^{−1/2}P(U)²) with M = 4.823 + P(U). Here c(M) = (2/√N)(1 + x/2)(1−x)^{−5/2} and x = M²/N (Round 174).
  - Counting Lipschitz rate q = 0.545 on the 3/8 polydisk, and the Round 173 tail after k_n = ⌈(4/7)log₂n⌉ (Rounds 173/177).
- **Compact model, per simple (Round 80).** Transport 𝒦 sends a positive nonpunctual simple of generic rank r to a negative simple of dimension r. A negative simple of dimension r has two boundary fibres with r weight slots each, and pooled first absolute moment r. The line J shifts the fibres by (−1, +1). The transport placement rule is the one in astra-dissipation-80.md, lines 82–112.
- **Prices.** A(f) = Σ|c_M|d_M is the minimal Deligne-type (Fourier-algebra) price. π_α(simple) = r + α z, with z the pooled zero multiplicity, is extended to fields by Σ|c_M| π_α(M). P_5000 is the translated base-pair packet price (Rounds 126/130/162).

## Argument

### 1. Proposition 1, restated with the audit's hypotheses, and its proof (a)

Fix a large eligible p, a point t ∈ Q and a lift. Let 𝒳 ⊂ ℂⁿ be a complex subspace (the represented price class) and P: 𝒳 → [0,∞) a seminorm with ‖x‖_∞ ≤ P(x) (sup domination). An infimum over absolutely convergent representations of Σ|coefficient|·cost is such a seminorm.

**Proposition 1.** Suppose there are constants p0, κ0, c ≥ 0, radii 0 < u ≤ 3/8 − η with η > 0, and a function ε(p) → 0 such that:
- (H1) *class closure*: R ∈ 𝒳, L𝒳 ⊂ 𝒳, and T(U) ∈ 𝒳 whenever U ∈ 𝒳 and P(U) ≤ u;
- (H2) *bounds with corrections uniform over inputs*: for every U ∈ 𝒳,
  - P(R) ≤ p0 + ε(p);
  - P(LU) ≤ (κ0 + ε(p))P(U);
  - P(T(U)) ≤ (c + ε(p))P(U)² whenever P(U) ≤ u;
  - ε(p) does not depend on U, j, t or the lift;
- (H3) *strict invariance*: p0 + κ0u + cu² < u.

Then there is p₁, depending only on ε(·) and on the slack in (H3), such that for p ≥ p₁ we have P(U_j) ≤ u for **every** j ≥ 0. In particular ‖V_{602+j} − V_602‖_∞ ≤ u ≤ 3/8 − η. By the inherited counting contraction q = 0.545 on the 3/8 polydisk, the Picard rows then converge for each such n, uniformly on Q, to a stationary row that is holomorphic on the interior of Q (as in Rounds 173/177).

*Proof.*
- Let δ = u − (p0 + κ0u + cu²) > 0. Choose p₁ so that ε(p)(1 + u + u²) < δ for p ≥ p₁.
- Put f_p(x) = (p0+ε) + (κ0+ε)x + (c+ε)x². It is nondecreasing on [0,∞), and f_p(u) < u.
- Base case: U₀ = 0 ∈ 𝒳 and P(U₀) = 0 ≤ u.
- Inductive step: if U_j ∈ 𝒳 and P(U_j) ≤ u, then (H1) gives U_{j+1} ∈ 𝒳. Subadditivity, (H2) and monotonicity give P(U_{j+1}) ≤ P(R) + P(LU_j) + P(T(U_j)) ≤ f_p(P(U_j)) ≤ f_p(u) < u.
- The threshold p₁ was fixed before the induction and does not depend on j, because ε(p) is uniform over inputs (H2). So the induction runs over all j.
- Sup domination places every U_j in the coordinate polydisk of radius u ≤ 3/8 − η about V_602. That is inside the Round 177 disks, where the frozen-base identity is valid and the counting rate is 0.545.
- The rest is the inherited Round 173/177 argument. ∎

*Remarks.*
1. When the constants are fixed, the hypothesis of the Round 181 text is equivalent to (H3) for some u: f(u) < u has a solution iff (1−κ0)² > 4cp0, and then every u ∈ (u₋, u₊) works.
2. (H1) and (H2) are hypotheses about a price, not theorems for a new price. For P_5000 the audit reads Rounds 130/162/174 as stating (H2) with ε = O(n^{−1/2}). The word rules of Rounds 126/130/174 (odd multiplier words, and even Taylor words followed by transport, both keep the base pair) are what would give (H1) by induction on absolutely convergent representations. I did not re-derive them, and they are not used below except as inherited inputs.
3. For Round 173 only j ≤ k_n = O(log n) is needed. On that horizon even per-step relative corrections that accumulate are harmless: (1 + O(n^{−1/2}))^{k_n} = 1 + O(n^{−1/2}log n).

**Exact threshold of the criterion (a; `paley-182-cold-criterion-check.py`).** With p0 = 0.01272 and the Round 174 coefficient evaluated on the ball, c = c(4.823 + u), condition (H3) holds for some u ∈ (0, 3/8) iff
  κ0 < κ*(p0) := sup_u [1 − p0/u − c(4.823+u)·u].
- c(M) ≤ g is certified by the squared comparison 4(1 + x/2)² ≤ g²N(1−x)⁵.
- The lower bracket of κ* is a certified admissible radius.
- The upper bracket uses monotonicity of c in M, applied on an adaptive partition of (0, 3/8].

| p0 | κ* (exact bracket) | certifying u | c(M0+u) ≤ |
|---|---|---|---|
| 0.01272 | [0.7741471, 0.7741472] | 0.10868 | 1.001215 |
| 10⁻³ | [0.9383484, 0.9383485] | 0.03210 | 0.950126 |
| 10⁻⁶ | [0.9980707, 0.9980708] | 0.00104 | 0.930594 |
| 10⁻¹² | [0.9999981, 0.9999981] | ≈10⁻⁶ | 0.929954 |

The script also re-confirms the audit's exact statements:
- c(4.936) ≤ 1.0043 is true, and c(4.936) ≤ 1.0042 is false;
- c(5.198) < 1.22 is true, and c(5.198) ≤ 1.2182 is false;
- c(4.873) < 1 is true;
- with the constant c = 1.0043, the discriminant is positive at κ0 = 0.77394 and not at 0.77395.

So "κ0 < 0.77395" is a correct sufficient threshold for that ball, and the sharp threshold of the same criterion is 0.774147. The self-consistent check at u = 0.11255 also admits κ0 = 0.77395 and 0.77396.

### 2. Proposition 2: the finite-horizon Duhamel form (a)

Keep (H1), and keep the Taylor part of (H2) on P(U) ≤ u. For a horizon k ≥ 1 put
  Γ_k = Σ_{m=0}^{k−1} ‖L^m‖_P,  σ_k = max_{1≤j≤k} P(Σ_{i<j} L^i R),
where ‖·‖_P is the operator price on 𝒳 and σ_k is the signed propagated source.

**Proposition 2.** Suppose σ_k + Γ_k c u² < u, with u ≤ 3/8 − η and the corrections absorbed with strict slack as in Proposition 1. Then P(U_j) ≤ u for 0 ≤ j ≤ k.

*Proof.*
- The recursion gives the variation-of-constants identity U_j = Σ_{i<j} L^i R + Σ_{i<j} L^{j−1−i} T(U_i). Check by induction: U_{j+1} = R + L U_j + T(U_j).
- Assume P(U_i) ≤ u for i < j. Then P(U_j) ≤ σ_k + Σ_{i<j}‖L^{j−1−i}‖_P · c u² ≤ σ_k + Γ_k c u² < u.
- Strong induction on j ≤ k finishes the proof. ∎

**Corollary 2.1 (power bounds).** Suppose ‖L^m‖_P ≤ Cλ^m for m < k. Then Γ_k ≤ C/(1−λ) and σ_k ≤ Γ_k p0. Proposition 2 applies if (C/(1−λ))(p0 + c(M0+u)u²) < u for some u, that is, if
  λ < λ_max(C) = 1 − C(1 − κ*).
For C = 1 this is Proposition 1 again. The script certifies:

| C | 1 | 1.25 | 1.5 | 2 | 3 |
|---|---|---|---|---|---|
| λ_max(C) | 0.77415 | 0.71768 | 0.66122 | 0.54829 | 0.32244 |

With k = k_n the conclusion is exactly the Round 173 finite-prefix confinement with clearance η. Only power bounds for m < k_n and one source estimate are needed, at each large p with n-independent constants.

**Corollary 2.2 (seed plus non-seed perturbation).** Write L = L_S + B. Suppose ‖L_S^m‖_P ≤ C_Sλ_S^m for m < k and ‖B‖_P ≤ β. Then ‖L^m‖_P ≤ C_S(λ_S + C_Sβ)^m.

*Proof.* Expand (L_S + B)^m into words. A word containing j factors B has j+1 maximal L_S-blocks of total length m−j, so its price is at most C_S^{j+1}β^jλ_S^{m−j}. There are binom(m, j) such words. Sum over j. ∎

Hence the criterion holds if
  β < β_max := (1 − λ_S)/C_S − (1 − κ*),  with 1 − κ* ≤ 0.225853.

**Remark 2.3 (necessity of a sub-unit power rate; a).**
- For Proposition 2, a u with σ + Γcu² < u exists iff 4σΓc < 1. Here σ_{k_n} ≥ P(R_602) ≥ ‖R_602‖_∞ ≥ ‖R_602‖_{2,n}, and liminf_p ‖R_602‖_{2,n} > 0 (Round 180, ineffective). So the hypothesis forces Γ_{k_n} to be bounded uniformly in n.
- The only available bound is Γ_{k_n} ≤ Σ_{m<k_n} 1.066^m, which is at least 1.066^{k_n−1} ≥ n^{1/20}/1.066. The exact check is 1.066⁸⁰ > 2⁷, so (4/7)log₂1.066 > 1/20.
- That bound diverges. So no source estimate, however small, can verify the hypothesis from the one-step rate 1.066.
- The "p0 ≤ 10⁻⁶" alternative only moves the target, to κ* = 0.99807. Both alternatives need a price whose power growth is below one, uniformly in n.

### 3. The seed-linear multiplier: exact per-simple growth (a, compact model per simple)

The seed-linear part of the frozen multiplier is L_S f = K(S f/(2√t)) = (s_p/(4√t))·𝒦((J + J⁻¹)f). Everything below uses the Round 80 rule recalled in the setup. Each statement is per simple, at each prime, before the physical O(n^{−1/2}) corrections. It extends to fields by the triangle inequality, so collisions only help.

**Lemma 3.1 (exact rank rule).** Let the negative input have dimension r, and let NZ be the number of nonzero slots over both fibres.
- The child under J^e has dimension r′_e = 2r − τ_e, where τ_e is the number of nonzero slots that the shift moves towards zero.
- Summing over e = ±1 gives r′₊ + r′₋ = 4r − NZ.

*Proof.*
- r′ = ½Σ|w′|. A zero slot contributes 1. A nonzero slot contributes |w| ± 1 according to whether the shift moves it away from zero or towards it.
- With Z + NZ = 2r and Σ|w| = 2r, this gives r′ = ½(Z + 2r + NZ − 2τ) = 2r − τ.
- Each nonzero slot moves towards zero under exactly one of the two shifts. ∎

**Consequences (re-proofs of the audited Round 181 rates).**
- The plain dimension ratio is (r′₊ + r′₋)/r = 4 − NZ/r ∈ [2, 4).
- The supremum 4 is approached by the slot multisets {0, k} with k → ∞. So ‖L_S‖_A ≤ 4·s_p/(4|√t|) ≤ 2s_p/√N → 4√2/√N = 0.71006.
- For π_α, the extreme rays give ratio 2+α (all |w| = 1) and (4k−2+α(2k−2))/(k+α(k−1)) → (4+2α)/(1+α) (the {0, k} rays). The minimax is at α = 1, with value 3, so the weighted rate is (3/4)s_p/|√t| → 0.53255.
- The script finds G₁(0) = 4 and G₁(1) = 3 exactly: the lower bound from feasible rays and the upper bound from the mediant coincide.

**Lemma 3.2 (linearity and submultiplicativity).**
- On slot-count vectors, one step x ↦ M_e x is linear. The dimension is ½Σ|w′|·count, the placements are fixed by sign and fibre, and each fibre is filled with r′ − (nonzero count in that fibre) new zeros.
- π_α is linear in the counts.
- Hence the m-step path sum is π_α((M₊ + M₋)^m x), and G_m(α) := sup over valid simples of the path-summed π_α divided by π_α(parent) satisfies ‖L_S^m‖_{π_α} ≤ G_m(α)(s_p/(4|√t|))^m.
- Children of valid simples are valid simples, so G_{m+k} ≤ G_mG_k.
- Upper bound: the mediant bound max_t n_t/d_t over single slot types t, with the induced zero counts substituted. It holds because every d_t > 0. Slot values with |v| > m+1 never reach zero, so n_t and d_t are affine in |v|; the script checks this exactly by vanishing second differences, and the |v| → ∞ limit is included.
- Lower bound: the maximum over feasible extreme rays (supports of at most three types, zero constraints tight).

| m | G_m(0) upper | rate | G_m(½) upper | rate | G_m(1) upper | rate |
|---|---|---|---|---|---|---|
| 1 | 4 | 0.71006 | 10/3 | 0.59172 | 3 | 0.53255 |
| 2 | 12 | 0.61493 | 10 | 0.56135 | 9 | 0.53255 |
| 4 | 104 | 0.56688 | 254/3 | 0.53847 | 75 | 0.52240 |
| 8 | 6928 | 0.53618 | 5586 | 0.52194 | 4915 | 0.51366 |

Here rate = G_m^{1/m}·√2/√N. The lower bounds are close: at m = 8 they are 6451.4, 5326 and 4742.4. The leading-field growth 2√2 (rate 0.50206) is the apparent limit. That it holds for all j remains a conjecture, as in Round 181.

By submultiplicativity with m0 = 8, G_m ≤ Cλ̂^m for all m:
- α = 0: rate 0.53618, C = 1.3243;
- α = ½: rate 0.52194, C = 1.1567;
- α = 1: rate 0.51366, C = 1.0749.

**Consequence for the non-seed budget (Corollary 2.2; a, given transfer of p0 and c into the chosen price).** β_max = (1 − λ_S)/C_S − 0.225853:

| price, seed bound used | λ_S | C_S | β_max |
|---|---|---|---|
| dimension, one step | 0.71006 | 1 | 0.06409 |
| dimension, 8-step power | 0.53618 | 1.3243 | 0.12439 |
| π_½, 8-step power | 0.52194 | 1.1567 | 0.18745 |
| π₁, one step | 0.53255 | 1 | **0.24159** |
| π₁, 8-step power | 0.51366 | 1.0749 | 0.22660 |

So the m-step seed analysis doubles the budget in plain dimension price, but in π₁ the one-step bound stays best: the constant C_S > 1 costs more than the gain in rate. A caveat that applies to the whole table: p0 = 0.01272, c(M) and M0 = 4.823 are P_5000 quantities, and here they are assumed unchanged in A or π_α. That transfer is not a lemma (audit §3.5). It is hypothesis (b1) below.

### 4. The non-seed multiplier: what must be priced and what it costs crudely

Write D_602 = Φ_t′(V_602) with V_602 = S + h. The non-seed operator is B = K((Φ_t′(S+h) − S/(2√t))·). It consists of:
- (i) the h-linear term K(h·/(2√t));
- (ii) the higher Taylor terms Σ_{l≥1}(−1)^l c_l V^{2l+1}/(4t)^{l+1/2} with c_l = binom(2l,l)/4^l. These split into their seed-only part and their part containing h.

**Crude costs (a as implications; the A(h) input is conditional).**
- A product of a non-seed simple of dimension d with an input simple of dimension r has generic rank at most 2dr. This follows from additivity of normalized first absolute moments (Round 126 word cost with k = 2). After transport, the output dimension equals that rank.
- Plain dimension price: the h-linear cost is therefore at most 2A(h)/√N. In π₁ it is at most 4A(h)/√N, because z′ ≤ r′.
- If the seed is designated with its exact coefficients in V_602's minimal representation (unproved, audit §3.5), then A(h) ≤ 4.823 − s_p < 1.994573. The costs become ≤ 0.50073 (dimension) and ≤ 1.0015 (π₁).
- For the higher Taylor terms the word bound "rank ≤ (2l+2)∏d" gives a seed-only part ≤ G(2√2) ≤ 0.10425 and a non-seed part ≤ G(4.823) − G(s_p) ≤ 0.64623. Here G(y) = (y/√N)[2(1−x)^{−1/2} + x(1−x)^{−3/2} − 2] with x = y²/N.
- Together this crude plain-dimension total is ≈ 1.96, against 1.066 for P_5000. The packet Schur test of Rounds 82/130 is far sharper than this word bound, but it is unsigned.

**What the h-linear term alone must satisfy.** Let ρ be the proved per-simple ratio factor for multiplying by non-seed simples. The requirement is ρ·A(h) < β_max·√N, with √N > 7.9667. Concretely:
- dimension, one step: ρA(h) < 0.5105;
- dimension, 8-step power: ρA(h) < 0.991, so A(h) < 0.496 at ρ = 2;
- π₁: ρA(h) < 1.9247, so A(h) < 0.481 at the provable ρ = 4, and A(h) < 0.962 if ρ = 2 could be proved in π₁.

**Evidence (c; §5).** The actual stationary row gives physical sup|h| ≈ 0.551–0.557 for p ∈ {100049, 400009}. A(h) is at least the coset supremum of |h|. The physical coordinates sample the coset, so heuristically this lower bound is about 0.55. If so:
- every plain-dimension version is excluded (it needs A(h) < 0.496);
- π₁ with the crude ρ = 4 is excluded (it needs A(h) < 0.481).

What survives is a π₁-type (zero-tracking) price in which:
1. the non-seed product ratio is proved to be at most about 3.5;
2. A(h), or the better signed multiplier price of h, is close to its sup lower bound;
3. the higher Taylor non-seed terms fit in the same 0.2416 budget. Their crude cost 0.646 alone already exceeds it.

The evidence also shows the inherited sup bound ‖V_602 − S‖_∞ < 1.963 (Round 177) and the dimension budget 4.823 are loose by a factor of about 3.5 against the actual row. The source of the trouble is the representation budget, not the dynamics.

### 5. Floating diagnostic (c; `paley-182-cold-fixedpoint-diagnostic.py`)

- **Setup.** Double-precision numpy at real t = a, with t₀ = n and the positive branch (one real lift). Iterating from S reaches step RMS < 10⁻¹⁴, so the row is the stationary row V_*. V_602 agrees with it far below double precision (Round 180: ‖R_602‖_{2,n} < 10⁻²⁰⁸).
- **Stationary row.**
  - p = 100049: sup|S| = 2.8284, sup|V| = 3.2710, sup|h| = 0.5513, RMS(h) = 0.1752, sup|Φ′(V)| = 0.3798.
  - p = 400009: sup|V| = 3.3155, sup|h| = 0.5566, RMS(h) = 0.1749, sup|Φ′(V)| = 0.3842.
- **Frozen powers on structured inputs (v = h, v = S).** The sup-norm decay (‖L^mv‖_∞/‖v‖_∞)^{1/m} is about 0.25 at m = 8–12, and sup/RMS stays between 3 and 5. That is close to √(2 ln n), as the Round 180 draft observed. So the actual frozen dynamics decays in sup norm far below 0.774 on these vectors. The obstruction lies in certifying it through a price, not in the dynamics.
- **Limits.** This is not the nine-center start; there is no complex t, no second lift and no interval arithmetic. It supports no (a) or (b) statement.

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved here.**
- (a1) The frozen-base identity, and Proposition 1 for an abstract sup-dominating seminorm price under (H1), (H2) (corrections uniform over inputs) and (H3), with a j-independent prime threshold. The conclusion (all-j confinement, then Picard convergence on Q) uses only the inherited Round 173/177 contraction.
- (a2) The exact threshold of that criterion with p0 = 0.01272 and c = c(4.823+u): κ* ∈ [0.7741471, 0.7741472]. Also the brackets for p0 = 10⁻³, 10⁻⁶ and 10⁻¹², and the audit's 0.77395 as the fixed-ball (u = 0.113, c = 1.0043) threshold. Exact rationals.
- (a3) Proposition 2 (finite-horizon Duhamel form), Corollary 2.1 with λ_max(C) = 1 − C(1−κ*) and its table, and Corollary 2.2 (perturbation by a non-seed part).
- (a4) Remark 2.3. Proposition 2's hypothesis forces Γ_{k_n} to be bounded uniformly in n. The one-step bound 1.066 gives only Γ ≥ n^{1/20}/1.066 as its bound, so it cannot verify the criterion whatever the source price.
- (a5) Compact model, per simple, Round 80 rule:
  - Lemma 3.1, r′₊ + r′₋ = 4r − NZ, which re-proves the rates 0.71006 (dimension) and 0.53255 (π₁, minimax at α = 1);
  - linearity and submultiplicativity of the m-step growth;
  - the certified upper bounds G_m(α) for m ≤ 8 and the power constants;
  - the β_max table, under (b1).
- (a6) The crude cost bounds of §4 as implications from the cited word-rank rules: 2A(h)/√N, 4A(h)/√N, and the higher Taylor G-bounds.

**(b) Conditional.**
- (b1) p0, c(M) and M0 carry over unchanged to A or π_α. Without this, the budgets 0.064/0.124/0.2416 are targets, not gaps.
- (b2) A(h) ≤ 1.994573 requires the seed to be designated with its exact coefficients in the minimal representation of V_602.
- (b3) Any κ0 for a new price also needs its own (H1), (H2), sup domination and Taylor coefficient.
- (b4) The Round 80 per-simple rule is used as stated there, including the zero-fill placement. Nonnegativity of the fill on the actual child simples is part of that rule and was not re-derived.

**(c) Evidence.**
- (c1) Physical sup|h| ≈ 0.55 and RMS(h) ≈ 0.175 at p ≤ 4·10⁵. Together with A(h) ≥ coset sup, this means the dimension-price route and the crude-ratio π₁ route cannot meet the budget.
- (c2) The frozen sup-norm decay is about 0.25 per step on structured inputs.
- (c3) G_m^{1/m}·√2/√N → 0.50206, the leading-field rate, which remains a conjecture beyond the computed m.

## Exact remaining gap

The question is the price of the non-seed multiplier B = K((Φ_t′(V_602) − S/(2√t))·) in a zero-tracking price.
- Supported branch: certify ‖B‖_{π₁} < 0.2416, including the h-linear term and all higher Taylor terms. Then κ0 = 0.53255 + β < κ* follows. In addition, p0, c, M0, class closure (H1) and the uniform corrections (H2) must be re-proved in π₁.
- Equivalent requirement for the h-linear term: ρA(h) < 1.925, where ρ is a proved per-simple π₁ ratio for multiplication by the transported (non-seed) simples of V_602.
- Present provable values: ρ = 4 and A(h) ≤ 1.9946 (conditional). The evidence suggests A(h) ≥ 0.55.
- The crude higher Taylor non-seed cost, 0.646, must also come under the same budget, presumably by expanding around the seed rather than around zero.
- Alternative branch: a collected multi-step price with C_S ≈ 1 and power rate below 1 − C_S(0.2259). By Remark 2.3, any route needs n-uniform power growth below one.
- Uniform complex stationary domain and derivative transfer remain separate obligations.

## Two ranked next tests

1. **Weighted non-seed multiplier price from the actual envelope.** Extend the Round 130 finite envelope (outward intervals through height 601/602) to record, for the non-seed simples of V_602, the per-fibre weight data needed by the π₁ rule. Then compute by exact linear-fractional programming the one-step π₁ ratio of f ↦ K(B f) per input simple. Expand the multiplier around the seed: Φ′(S) is exact in the lines J^k, and the h-terms are paired with Φ″(S), Φ‴(S), and so on.
   - Decisive in either direction. If the certified value is below 0.2416, it settles the supported branch subject to the (b1)/(H1)/(H2) checks in test 2. If the per-simple π₁ ratio for multiplying by these actual simples is at least 4 − o(1) while A(h) ≥ 0.481, then no π₁-type price of this per-simple kind can reach κ*, and the one-step price route is retired.
2. **Re-derive p0, c(M), M0, (H1) and (H2) for π₁ (or A).** This needs:
   - π₁(R_602) from the Round 126/174 source chain;
   - the even Taylor word argument of Round 174, with π₁ in place of P_5000;
   - the dimension-type bound of V_602 in π₁.
   Without this, κ* = 0.774147 is the target only under (b1). A cheaper first step is to check whether the Round 174 coefficient c(M) survives verbatim when the output price counts zeros, since z′ ≤ r′ could double it.

## Replay commands and outputs

```bash
python3 -B research/paley-182-cold-criterion-check.py
```
Output, exact rationals; runtime about 19 s:
```
== Audit statements (Round 181), exact ==
c(4.936) <= 1.0043 : True
c(4.936) <= 1.0042 : False
c(5.198) <  1.22   : True
c(5.198) <= 1.2182 : False
c(4.873) <  1      : True
  constant c=1.0043, k0=0.77390: discriminant>0 = True
  constant c=1.0043, k0=0.77394: discriminant>0 = True
  constant c=1.0043, k0=0.77395: discriminant>0 = False

== Prop. 1 threshold kappa*(p0) (exact bracket) ==
p0=1e-02: kappa* in [0.7741471, 0.7741472]; certifying radius u=0.10868, c(M0+u)<=1.001215
p0=1e-03: kappa* in [0.9383484, 0.9383485]; certifying radius u=0.03210, c(M0+u)<=0.950126
p0=1e-06: kappa* in [0.9980707, 0.9980708]; certifying radius u=0.00104, c(M0+u)<=0.930594
p0=1e-12: kappa* in [0.9999981, 0.9999981]; certifying radius u=0.00000, c(M0+u)<=0.929954

self-consistent check k0=0.77395, u=0.11255: p0+k0 u+c u^2 < u : True  c(M0+u)<= 1.0039145
self-consistent check k0=0.77396, u=0.11255: p0+k0 u+c u^2 < u : True

== Prop. 2 (finite-horizon Duhamel) with power bound ||L^m||_P <= C lam^m ==
condition: exists u<=3/8 with (C/(1-lam))(p0 + c(M0+u)u^2) < u
C=1.00: need lam < 0.77415 (u=0.1085)
C=1.25: need lam < 0.71768 (u=0.1085)
C=1.50: need lam < 0.66122 (u=0.1085)
C=2.00: need lam < 0.54829 (u=0.1085)
C=3.00: need lam < 0.32244 (u=0.1085)

== Necessity of an n-uniform finite-horizon price resolvent (exact arithmetic) ==
1.066^80 > 2^7 (so 1.066^{k_n} >= n^{1/20}): True

== Crude non-seed multiplier costs in dimension price (conditional inputs) ==
A(h) <= 1.994573 ; h-linear dimension cost 2A(h)/sqrt N <= 0.50073
seed-linear plain dimension rate limit 2*sqrt(8)/sqrt(N) = 0.71006 (upper, using sqrt N lower)
seed-linear weighted (alpha=1) rate limit (3/4)*sqrt(8)/(sqrt(N)/2) = 0.53255
higher Taylor (l>=1) crude dimension costs, coefficient bound (2l+2) prod d:
  seed-only part G(2sqrt2) <= 0.10425 (s_p -> 2sqrt2)
  non-seed part G(M0)-G(s_p) <= 0.64623
one-step non-seed budget (kappa* lower 0.77414 minus seed rate): dimension 0.06408 ; weighted alpha=1 0.24159
  => need rho*A(h) < budget*sqrt(N):  dimension 0.5105 ; weighted 1.9247 (rho = per-simple ratio factor, crude 2 resp. 4)
```
Notes on this output:
- The "p0=1e-02" label is the printed rounding of p0 = 0.01272.
- The printed "u=0.00000" for p0 = 10⁻¹² is a radius of about 10⁻⁶.
- The 0.06408 in the last block uses the rounded-down κ* lower bound 0.77414; the 0.06409 in §3 uses 0.774147.

```bash
python3 -B research/paley-182-cold-seed-power-check.py
```
Output, exact integers and rationals; floats are echoes only; runtime about 7 s:
```
limit per-line factor s_p/(4|sqrt t|) = 0.177515
m=1 alpha=  0: G_lo=3.714286 G_up=4.000000  G_up^(1/m)=4.000000  rate=0.71006
m=2 alpha=  0: G_lo=11.000000 G_up=12.000000  G_up^(1/m)=3.464102  rate=0.61493
m=3 alpha=  0: G_lo=32.888889 G_up=36.000000  G_up^(1/m)=3.301927  rate=0.58614
m=4 alpha=  0: G_lo=95.200000 G_up=104.000000  G_up^(1/m)=3.193437  rate=0.56688
m=5 alpha=  0: G_lo=275.636364 G_up=300.000000  G_up^(1/m)=3.129135  rate=0.55547
m=6 alpha=  0: G_lo=790.000000 G_up=856.000000  G_up^(1/m)=3.081383  rate=0.54699
m=7 alpha=  0: G_lo=2262.153846 G_up=2440.000000  G_up^(1/m)=3.047283  rate=0.54094
m=8 alpha=  0: G_lo=6451.428571 G_up=6928.000000  G_up^(1/m)=3.020480  rate=0.53618
m=1 alpha=1/2: G_lo=3.200000 G_up=3.333333  G_up^(1/m)=3.333333  rate=0.59172
m=2 alpha=1/2: G_lo=9.478261 G_up=10.000000  G_up^(1/m)=3.162278  rate=0.56135
m=3 alpha=1/2: G_lo=27.692308 G_up=29.333333  G_up^(1/m)=3.084043  rate=0.54746
m=4 alpha=1/2: G_lo=79.931034 G_up=84.666667  G_up^(1/m)=3.033389  rate=0.53847
m=5 alpha=1/2: G_lo=229.500000 G_up=242.666667  G_up^(1/m)=2.999177  rate=0.53240
m=6 alpha=1/2: G_lo=656.114286 G_up=692.000000  G_up^(1/m)=2.974069  rate=0.52794
m=7 alpha=1/2: G_lo=1871.157895 G_up=1968.000000  G_up^(1/m)=2.955119  rate=0.52458
m=8 alpha=1/2: G_lo=5326.000000 G_up=5586.000000  G_up^(1/m)=2.940273  rate=0.52194
m=1 alpha=  1: G_lo=3.000000 G_up=3.000000  G_up^(1/m)=3.000000  rate=0.53255
m=2 alpha=  1: G_lo=8.666667 G_up=9.000000  G_up^(1/m)=3.000000  rate=0.53255
m=3 alpha=  1: G_lo=24.941176 G_up=26.000000  G_up^(1/m)=2.962496  rate=0.52589
m=4 alpha=  1: G_lo=71.894737 G_up=75.000000  G_up^(1/m)=2.942831  rate=0.52240
m=5 alpha=  1: G_lo=205.333333 G_up=214.000000  G_up^(1/m)=2.924710  rate=0.51918
m=6 alpha=  1: G_lo=586.260870 G_up=610.000000  G_up^(1/m)=2.912203  rate=0.51696
m=7 alpha=  1: G_lo=1667.840000 G_up=1732.000000  G_up^(1/m)=2.901681  rate=0.51509
m=8 alpha=  1: G_lo=4742.444444 G_up=4915.000000  G_up^(1/m)=2.893613  rate=0.51366

reference: 2*sqrt(2) = 2.828427 (leading-field growth, rate 0.50206)

Power bounds G_m <= C lam^m via submultiplicativity (lam from m0=8):
alpha=  0: lam_hat=3.020480 (rate 0.53618), C=1.3243
alpha=1/2: lam_hat=2.940273 (rate 0.52194), C=1.1567
alpha=  1: lam_hat=2.893613 (rate 0.51366), C=1.0749
```
Notes on this output:
- The "rate" column multiplies by the limit factor 0.177515 = √2/√N, using s_p → 2√2 and |√t| ≥ √N/2.
- At a finite prime the factor is s_p/(4|√t|) with s_p = 2√(2+1/n), which is larger by 1 + O(1/n).
- The values G_up, and hence the power constants, are certified. The floats are display only.

```bash
/usr/bin/python3 -B research/paley-182-cold-fixedpoint-diagnostic.py
```
Output, floating point, evidence only. It needs numpy, which on this machine is available in `/usr/bin/python3`. Runtime about 2 s.
```
p=1013 n=506 final RMS step=3.6e-15
  sup|S|=2.8298 sup|V|=2.5367 sup|h|=0.7501 RMS(h)=0.3812 sup|Phi'(V)|=0.3034
  v=h: ||L^m v||_inf/||v||_inf ^(1/m) at m=1,2,4,8,12: 0.213 0.216 0.216 0.209 0.207 | sup/RMS at m=1,4,12: 2.87 3.60 3.55
  v=S: ||L^m v||_inf/||v||_inf ^(1/m) at m=1,2,4,8,12: 0.268 0.259 0.231 0.220 0.213 | sup/RMS at m=1,4,12: 2.64 3.33 3.68
p=10009 n=5004 final RMS step=7.0e-15
  sup|S|=2.8286 sup|V|=3.0085 sup|h|=0.5699 RMS(h)=0.1949 sup|Phi'(V)|=0.3533
  v=h: ||L^m v||_inf/||v||_inf ^(1/m) at m=1,2,4,8,12: 0.266 0.252 0.229 0.227 0.227 | sup/RMS at m=1,4,12: 3.91 3.35 3.15
  v=S: ||L^m v||_inf/||v||_inf ^(1/m) at m=1,2,4,8,12: 0.310 0.314 0.265 0.245 0.240 | sup/RMS at m=1,4,12: 2.76 3.62 3.57
p=100049 n=50024 final RMS step=3.9e-15
  sup|S|=2.8284 sup|V|=3.2710 sup|h|=0.5513 RMS(h)=0.1752 sup|Phi'(V)|=0.3798
  v=h: ||L^m v||_inf/||v||_inf ^(1/m) at m=1,2,4,8,12: 0.317 0.292 0.253 0.241 0.242 | sup/RMS at m=1,4,12: 4.33 4.15 4.12
  v=S: ||L^m v||_inf/||v||_inf ^(1/m) at m=1,2,4,8,12: 0.339 0.341 0.285 0.259 0.252 | sup/RMS at m=1,4,12: 2.89 4.16 4.19
p=400009 n=200004 final RMS step=5.8e-15
  sup|S|=2.8284 sup|V|=3.3155 sup|h|=0.5566 RMS(h)=0.1749 sup|Phi'(V)|=0.3842
  v=h: ||L^m v||_inf/||v||_inf ^(1/m) at m=1,2,4,8,12: 0.343 0.299 0.255 0.250 0.247 | sup/RMS at m=1,4,12: 4.62 4.19 4.85
  v=S: ||L^m v||_inf/||v||_inf ^(1/m) at m=1,2,4,8,12: 0.341 0.361 0.292 0.263 0.255 | sup/RMS at m=1,4,12: 2.89 4.53 4.34
```
The certificates in the first two scripts concern exact mathematical constants (rational comparisons). They do not certify any saved rounded input. The third script uses double-precision rows computed on the fly and certifies nothing.
