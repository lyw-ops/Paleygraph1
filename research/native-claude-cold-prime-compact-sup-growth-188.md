# Round 188 native Claude draft: cold prime compact sup growth

- call_id: `cold-prime-compact-sup-growth`
- Mission: `coordination/missions/round-188/cold-prime-compact-sup-growth.md`, exported from coordinator record `coordination/round-187.json` (SHA-256 36fbe33d…).
- Author: Claude subagent started by the Round 188 coordinator (session/r188-cold-supgrowth). Model: Claude Opus 5.5. This is an agent draft. It is not an audit, not an acceptance and not a human review.
- Input hashes verified (SHA-256). All eight match the mission export:
  - round-186-acceptance 9f1a0ccb…, round-187-acceptance edc1d3eb…, native-claude-audit-187 714513ca…
  - native-claude-cold-prime-b-word-delocalization-187 6e7fc0d4…, paley-187-cold-constants 429b028d…
  - native-claude-cold-prime-hybrid-price-186 6a597c9a…, cold-growing-prefix-delocalization-180 3a8eb51a…
  - native-claude-cold-prime-signed-nonseed-price-182 c8023a9b…
- Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-187.md`, §3 and §5 of `native-claude-audit-187.md`; the Round 80 per-simple rule and the identities (2)–(4) in `astra-dissipation-80.md`; the Round 182 seed-power script `paley-182-cold-seed-power-check.py` (read and its numbers reproduced, not modified); for the Goursat practice of the project, `weighted-arithmetic-57.md`, `shifted-groups-68.md`, `astra-mixed-81.md`, `rank-four-positive-55.md` (excerpts).
- Scripts written by this session (both new; neither imports an earlier script):
  - `research/paley-188-cold-sup-growth-certify.py`: arb balls with outward rounding and exact Fractions (label (a)). Runtime under 1 s.
  - `research/paley-188-cold-sup-growth-explore.py`: exact consistency checks of the reduction (Part 1, exact integers) and floating orientation (Part 2, label (c)). Runtime about 4 s.

## Result summary

**Verdict: refuted, conditionally** (the mission's refuted branch, given (ST↓) and the sign-alignment hypothesis (SA) below; unconditionally the question stays open, with the certified range in item 4). The decisive quantity turns out to be computable exactly, and it lies strictly between the two thresholds.

1. **Exact branching structure (Lemmas 1, F, 2; proved under the inherited Round 80 per-simple rule).** In the compact model at t = a, L_S^k χ_M is a sum over paths of orthonormal, pairwise distinct leaf characters. Summed over the two children J^{+m}, J^{−m}, the pooled |weight| histogram of a simple evolves by a fibre-free nonnegative linear operator P_m. So the dimension price A(L_S^k χ_M) is half the mass of P^k n_M with P = Σ_{m odd}(|β_m|/2)P_m, where β_m are the cosine coefficients of Φ_a′(√8 cos θ). The per-fibre zero fill of the Round 80 rule is never negative (Lemma F, proved for every configuration and every odd shift; this removes the fill part of Round 182's caveat (b4)).
2. **The J^{±1} part has an exact Perron eigenvector in ℚ(√2) (Theorem 2; proved).** Its path-summed dimension grows exactly like (2√2)^k, within the factors √2 ∓ 1. This proves the Round 182 conjecture (c3) G_m^{1/m} → 2√2 in sharper form. With the exact coefficient β₁/2 the ratio to ℓ_S is θ₁ = 2/√(1 + Σ_{m≥3}β_m²/β₁²) ∈ [1.99978311, 1.99978311], just below 2. That is where the Round 187 "2^k" heuristic comes from.
3. **The full multiplier: certified dimension-price rate (Theorem 3; outward).** The rate is λ_A ∈ [0.4995143223, 0.4995143263]. For every valid simple M of dimension r and every k ≥ 0, K⁻¹λ_lo^k r ≤ A(L_S^kχ_M) ≤ Kλ_up^k r with K = 2.356002. So θ_A = λ_A/ℓ_S ∈ [2.08078462, 2.08078464].
   - The J^{±3} harmonic (coefficient |β₃|/2 = 0.0025) raises the rate from 0.48007 to 0.49951. It shifts slot sizes by 3. Its marginal value in the growth rate is about 7.4 per unit coefficient, against 2√2 = 2.83 for J^{±1} (floating). In L² it counts only through its square.
4. **Consequences for the compact sup of the seed iterates.**
   - (Unconditional within the model.) ℓ_S^k‖d‖₂ ≤ ‖L_S^kd‖_∞ ≤ Kλ_up^k A(d). So the certified sup rate lies in [0.2400606, 0.4995143], which contains 0.466. Hence C_k^seed ≤ K·θ_A^k·A(d)/‖d‖₂ with θ_A < 2.1610 ≤ 1/q_ang(2.338). The seed iterates fit the angular-variant allowance, with a margin of 3.86%.
   - (Under (SA), i.e. the compact sup is comparable to the dimension price.) The sup decays at exactly λ_A = 0.49951 > 0.46659, and C_k^seed ≥ c·θ_A^k with θ_A > 1/q for every counting rate in use (largest 1/q = 1.94363; margin 7.06%). This is the sign-aligned family the mission asks about, with sup ≥ c·0.4995^k. By Round 187 Proposition 6, given (ST↓), Criterion D in its stated form cannot hold for these words.
   - (Floating, orientation.) Aligning only "all leaves at +dimension" (a global/parity alignment) gives the signed rate 0.46191 < 0.46659. That alone would not refute. The refutation needs per-leaf sign freedom, which is what (SA)/(IND) supply.
5. **Full increments R^comp_{602+k} (conditional transfer, Corollary 5).** The same conclusion holds for the actual increments if, in addition: (NC) the seed sector is not cancelled by B-words; (SA) holds for them; and the L² rate obeys a decoupling (D). Under (D) and Round 80 (4), the L² rate is at most ℓ_*(η) with η = ‖U₆₀₂ − S‖₂². The transfer needs η < 0.60613 (‖U₆₀₂ − S‖₂ < 0.7785 at q = 0.5145). The floating RMS(h) ≈ 0.175 gives ℓ_* = 0.24095, against a measured physical rate of 0.2405–0.2407. The proved sup cap 1.963 alone does not suffice.
6. **By-product for the price programme.** The Perron-weighted price π_φ is sup-dominating, and L_S has one-step norm ≤ 0.4995143 with constant 1. This improves Round 182's best seed rate, 0.53255 (π₁, seed-linear part only). The Round 182 non-seed budget rises from 0.24159 to κ* − λ_up ≥ 0.274633, under Round 182's (b1).
7. **What blocks an unconditional decision:** (SA). Under Goursat independence of the leaf monodromies (IND), the sup equals the dimension price. The project's weight-list test cannot certify IND at depth: from K(J²), classes of up to 6 leaves with identical weight data occur by depth 12 (exact count).

## Setup and hypotheses

- **Parameters.** p ≡ 1 (mod 4) prime, n = (p − 1)/2, a = 2031/128, real floor t = a, real segments. Compact subsequential model of Rounds 79/80/179: J is the Jacobi line (Haar on the circle), S = √8 Re J, 𝒦 is the positive-to-negative transport.
- **Operator.** L_S f = 𝒦(Φ_a′(S)f) with Φ_a′(x) = x/√(4a + x²). Write
  - Φ_a′(√8 cos θ) = Σ_{m odd ≥ 1} β_m cos mθ = Σ_m (β_m/2)(J^m + J^{−m}).
  - The β_m are real and alternate in sign: β₁ = 0.339460…, β₃ = −0.0049984…, β₅ = +1.109·10⁻⁴, …
- **Dimension price.** A(f) = Σ_M |c_M| d_M over the (unique, L²-orthonormal) expansion of f in geometric simples. Since |χ_M| ≤ d_M pointwise, ‖f‖_∞ ≤ A(f) (unconditional).
- **C_k.** C_k := ‖R^comp_{602+k}‖_∞/‖R^comp_{602+k}‖₂ (Round 187). C_k^seed is the same ratio for L_S^k d.
- **Thresholds.** Criterion D (Round 180) with Proposition 6 (Round 187, accepted as an implication) needs C_k ≤ Λγ^k with γ < 1/q_ρ ≤ 1/0.5145 = 1.94363. The rate threshold is 1.94363·ℓ_S = 0.46659. The angular variant allows γ < 1/q_ang(2.338), with 1/q_ang(2.338) ≥ 2.1610 (Round 187 Lemma 3(c), accepted). Its rate threshold is 2.1610·ℓ_S = 0.51877.

**Hypotheses, stated once and referred to by name.**
- **(R80) Round 80 per-simple rule and twist exclusion, inherited.**
  - A negative simple of dimension r has two boundary fibres of r weight slots with Σ|w| = 2r.
  - Multiplying by J^e shifts the trivial fibre by −e and the quadratic fibre by +e. The positive product has generic rank r′ = ½Σ|w′|.
  - Transport keeps negative weights in their fibre, moves positive weights to the other fibre, drops shifted zeros and refills each fibre with zeros up to r′.
  - Transport and line multiplication are injective. A twist M′ ≅ J^kM between negative simples of dimension > 1 forces k = 0 (the |k|d ≤ 2d bound, the parity exclusion of odd k, and the endpoint exclusion of |k| = 2).
  - Round 182 used the rule with e = ±1 as its (b4). Here the rule is used for J^{±m}, m odd, as Round 80 states for J^k. That the actual transported simples obey this rule is inherited, not re-derived.
- **(R80-4)** The Round 80 identity (4), the orthogonality of the transported simples behind it, and E(U²|J) = S² + ‖U − S‖₂² for true compact feedbacks (Round 80, the paragraph after (4)). As in Round 187 Lemma 3(a), these give ‖L_S^kd‖₂ = ℓ_S^k‖d‖₂.
- **(ST↓)** Round 187's lower fixed-height sup transfer (unproved). It is used only through Proposition 6.
- **(SA_κ) sign alignment = Round 187's H-sup.** There is κ > 0 such that for every k the compact essential supremum of the field in question is at least κ times its dimension price.
  - Sufficient condition (IND): at each depth, the pairwise non-isomorphic leaves have jointly independent (Goursat-full) compact monodromy factors, also over the Jacobi circle. Each factor's coset must contain elements whose character has real part ≥ κd and ≤ −κd, after the phase of the coefficient. For example, −I in Sp/SO(even), or scalar elements of SU(d) cosets with d ≥ 3 (κ ≥ cos(π/d) ≥ ½).
  - Unproved. See §4.3.
- **(NC), (D), (η)** are used only for the transfer to R^comp in §5 and are stated there.

## 1. The branching structure of the seed iterates

**Lemma 1 (fibre-free histogram; proved under (R80)).** For a negative simple M, let n(M) = (n_b)_{b ≥ 0} be the pooled histogram of |w| over both fibres, so that Σ_b n_b = Σ_b b·n_b = 2r. For odd m ≥ 1 let P_m act on histograms as follows:
- a slot of size a ≥ 1 goes to sizes |a − m| (dropped if 0) and a + m;
- a zero slot goes to two slots of size m;
- then n′₀ := Σ_{b≥1}(b − 1)n′_b zeros are added.

Then n(𝒦(J^mM)) + n(𝒦(J^{−m}M)) = P_m n(M), and the two child dimensions sum to ½ mass(P_m n(M)), where mass(n) = Σ_b b·n_b.

*Proof.*
1. A trivial-fibre slot of value v becomes v − m in one child and v + m in the other. A quadratic-fibre slot becomes v + m and v − m. In both cases the pair of moduli is {||v| − m|, |v| + m}, and for v = 0 it is {m, m}.
2. Transport only relabels fibres and drops zero values.
3. Each child refills to 2r′_e = Σ|w′| slots in total. So it adds Σ_{nonzero}(|w′| − 1) zeros, which is linear and independent of the fibres. ∎

(Exact check: 32 000 children of 4000 random valid simples, m ∈ {1, 3, 5, 7}. The m = 1 operator also reproduces Round 182's independently computed fibre-resolved bounds G_up(m) = 4, 12, 36, 104, 300, 856, 2440, 6928 for m ≤ 8; explore script Part 1.)

**Lemma F (the per-fibre fill is never negative; proved).** For every formal configuration (two fibres of r slots, Σ|w| = 2r) and every integer e ≥ 1, each fibre of the child under J^{±e} receives at most r′ nonzero slots.

*Proof for e > 0 and the trivial fibre.*
- Put u = v on trivial-fibre slots and u = −v on quadratic-fibre slots.
- The condition 2r′ − 2NZ′_A ≥ 0 reads Σ_slots h(u) ≥ 0, with h(u) = |u − e| − 2[u < e].
- Since Σ_slots(|u| − 1) = 0, it suffices that Σδ(u) ≥ 0, where δ = h − (|u| − 1). Explicitly:
  - δ = e − 1 for u ≤ 0;
  - δ = e − 1 − 2u for 0 < u < e;
  - δ = 1 − e for u ≥ e.
- Using #{u = 0} = Σ_{u≠0}(|u| − 1) ≥ Σ_{u>(e−1)/2}(u − 1) and dropping nonnegative terms:
  Σδ ≥ Σ_{(e−1)/2<u<e}(e − 3)u + Σ_{u≥e}(e − 1)(u − 2) ≥ 0.
- The quadratic fibre is the same computation with h(u) = |u − e| − 2[u > e]. This gives Σ_{(e+1)/2<u≤e}(e − 1)u + Σ_{u>e}(e + 1)(u − 2) ≥ 0. Negative e is the mirror case.
- For e = 1 the trivial fibre receives exactly r′ nonzero slots. ∎

(Exhaustive exact check: all configurations with r ≤ 5, values in [−2r, 2r] and |e| ≤ 5, 63 030 children, no negative fill.) So the rule always outputs formally valid simples. This settles the part of Round 182's (b4) that concerned the fill. That actual simples obey the rule remains (R80).

**Lemma 2 (no collisions; proved under (R80)).** Let d = Σ c_M χ_M be a combination of distinct negative simples of dimension > 1 (for example, any output of 𝒦). Then the leaves 𝒦(J^{e_k} ⋯ 𝒦(J^{e₁}M)) over all roots M and all odd paths (e₁, …, e_k) are pairwise geometrically non-isomorphic.

*Proof.* Suppose 𝒦(J^eX) ≅ 𝒦(J^{e′}X′). Then injectivity gives X′ ≅ J^{e−e′}X with e − e′ even and X, X′ negative of dimension > 1. Twist exclusion forces e = e′ and X ≅ X′. Induct on the depth. ∎

**Proposition 1 (exact formulas; proved under (R80), (R80-4)).**
- L_S^kχ_M = Σ_paths (∏_i β_{|e_i|}/2) χ_leaf, with orthonormal leaves, so ‖L_S^kχ_M‖₂ = ℓ_S^k (Parseval: Σ_mβ_m²/2 = E[Φ_a′(S)²] = ℓ_S²; certified cross-check in §2 of the certify script).
- A(L_S^kχ_M) = Σ_paths |∏β/2|·d_leaf = ½ mass(P^k n(M)), with P = Σ_{m odd}(|β_m|/2)P_m.
- For d as in Lemma 2: ‖L_S^kd‖₂ = ℓ_S^k‖d‖₂ and A(L_S^kd) = Σ_M |c_M| A(L_S^kχ_M).

## 2. Theorem 2: the J^{±1} part, exactly

Let P₁ be the two-child operator of Lemma 1 for m = 1, with unit weight per child. Put μ = √2 − 1 and
- φ₀ = √2 − 1, φ_b = (b − 1) + (2 − √2)μ^{b−1} for b ≥ 1;
- ψ_b := φ_b + φ₀(b − 1) = √2(b − 1) + (2 − √2)μ^{b−1}.

**Theorem 2 (proved).** φP₁ = 2√2·φ exactly. Hence for every valid simple M of dimension r and every k:
  Σ_{±1-paths} φ(n_leaf) = (2√2)^k φ(n(M)),  and  (√2 − 1)(2√2)^k r ≤ Σ_{±1-paths} d_leaf ≤ (√2 + 1)(2√2)^k r.

*Proof.*
- On histograms, (φP₁)₀ = 2ψ₁ and (φP₁)₁ = ψ₂. For a ≥ 2, (φP₁)_a = ψ_{a−1} + ψ_{a+1}.
- With μ + μ⁻¹ = 2√2:
  - 2ψ₁ = 2(2 − √2) = 2√2φ₀;
  - ψ₂ = 4√2 − 4 = 2√2φ₁;
  - ψ_{a−1} + ψ_{a+1} = 2√2(a − 1) + (2 − √2)μ^{a−1}·2√2 = 2√2φ_a.
- On valid histograms (n₀ = Σ(b − 1)n_b), φ(n) = Σ_{b≥1}ψ_b n_b. Also ψ_b/b increases from 2 − √2 (at b = 1) towards √2. So φ(n)/mass(n) ∈ [2 − √2, √2], and √2/(2 − √2) = 1 + √2. ∎

(arb check of the eigen-equations for b ≤ 59 in the certify script, §3.)

Consequences:
- **Round 182's conjecture (c3) is proved.** G_m(0) ≤ (1 + √2)(2√2)^m for all m, and G_m^{1/m} → 2√2. Check: G₈ = 6928 ≤ 2.414·4096 = 9889.
- With the seed-linear coefficient s/(4√a) the rate is 0.5020882 (Round 182 quoted 0.50206 at |√t| ≥ √N/2).
- With the exact J^{±1} coefficient β₁/2 the rate is √2β₁ ∈ [0.4800690549, 0.4800690549], and θ₁ = √2β₁/ℓ_S = 2/√(1 + Σ_{m≥3}β_m²/β₁²) ∈ [1.99978311, 1.99978311].
- So "2^k" is exactly the J^{±1} value, and it is slightly below 2. Taken alone it already exceeds 1.94363.

## 3. Theorem 3: the full multiplier, certified

**Theorem 3 (proved under (R80), (R80-4); outward arithmetic).** Let P = Σ_{m odd}(|β_m|/2)P_m. Then:
- (i) There is a positive vector φ with φP ≥ λ_lo φ and φP ≤ λ_up φ on every slot size b ≥ 0, where
  λ_lo = 9990286447/(2·10¹⁰) = 0.4995143223… and λ_up = 9990286527/(2·10¹⁰) = 0.4995143263….
- (ii) For every valid simple M of dimension r and all k ≥ 0, K⁻¹λ_lo^k r ≤ A(L_S^kχ_M) ≤ Kλ_up^k r, with K = c_hi/c_lo = 2.356002 (c_lo = 0.617365 ≤ ψ_b/b ≤ c_hi = 1.454513).
- (iii) For every d as in Lemma 2 with A(d) < ∞:
  K⁻¹(λ_lo/ℓ_S)^k A(d)/‖d‖₂ ≤ A(L_S^kd)/‖L_S^kd‖₂ ≤ K(λ_up/ℓ_S)^k A(d)/‖d‖₂,
  with λ/ℓ_S ∈ [2.08078462, 2.08078464]. Since A(d) ≥ ‖d‖₂, the left side is ≥ K⁻¹(λ_lo/ℓ_S)^k.

*Proof and certificate* (`…-certify.py` §§2, 4, 5).
1. **Coefficients.** β_m for m ≤ 23 come from rigorous arb integration of √8 cos z cos(mz)/√(4a + 8cos²z) on [0, π], with the analytic flag on the square root.
   - The harmonic tail uses Cauchy's estimate on |z| = 4. There |cos θ| ≤ 17/8 and 8(17/8)² < 4a, so the branch locus is avoided, and |β_m|/2 ≤ 1.149410·4^{−m}.
   - For m ≥ 25 this gives Σw_m ≤ 1.09·10⁻¹⁵ and Σmw_m ≤ 2.74·10⁻¹⁴.
   - Parseval cross-check: Σ_{m≤23}β_m²/2 ≤ ℓ_S² ≤ the same plus the tail, both ∈ [0.05762907272008].
2. **Trial vector.** A floating power iteration proposes φ. It is rationalized with denominator 2⁶⁴, tabulated for b < 300 and affine (s·b + κ) beyond. In this form (φP_m)₀ = 2ψ_m and (φP_m)_a = [a ≠ m]ψ_{|a−m|} + ψ_{a+m}.
3. **Lower certificate.** P_lo keeps the harmonics m ≤ 23 with the lower ends of |β_m|/2. Dropping harmonics only lowers a nonnegative operator.
   - φP_lo ≥ λ_lo φ is checked exactly for b ≤ 322.
   - For b ≥ 323 both sides are affine in b. The slope 2W(s + φ₀) − λ_lo s = +2.0·10⁻⁹ ≥ 0, and the value at 323 is ≥ 0.
4. **Upper certificate.** P_hi uses the upper ends for m ≤ 23. The tail m ≥ 25 is bounded via ψ_o ≤ (s + φ₀)o + κ_max, giving 2(s + φ₀)(aT₀ + T₁) + 2κ_maxT₀.
   - φP_hi + tail ≤ λ_up φ is checked exactly for b ≤ 322.
   - The affine range has slope −2.0·10⁻⁹ ≤ 0 and value ≤ 0 at 323.
5. **From the certificate to (ii).**
   - Since P ≥ P_lo entrywise and everything is nonnegative, φ(P^kn) ≥ λ_lo^kφ(n). Likewise φ(P^kn) ≤ λ_up^kφ(n).
   - On valid histograms, φ(n) = Σ_{b≥1}ψ_b n_b ∈ [c_lo, c_hi]·mass(n). Beyond 300, ψ_b/b = (s + φ₀) + (κ − φ₀)/b is monotone, so its range is covered.
   - Proposition 1 then gives (ii). (iii) follows from Proposition 1 and Lemma 2. ∎

**Mechanism (floating decomposition; the rates are certified, the reading is not).**
- The Perron slot-size law of the leaves has n₀ : n₁ : n₂ : … = 0.424 : 0.335 : 0.136 : 0.059 : …, with mean slot size exactly 1. Small slots dominate.
- A J^{±3} factor turns a zero slot into two slots of size 3 and a size-1 slot into sizes 2 and 4. On the Perron law, one step multiplies the dimension per unit coefficient by 6.16 for the pair J^{±3}, against 2.85 for J^{±1} and 10.03 for J^{±5}. The marginal values ∂λ/∂w_m (left-eigenvector pairing) are 2.83, 7.42 and 13.56.
- The L² cost of J^{±3} is quadratic in its tiny coefficient (|β₃/β₁|² = 2.2·10⁻⁴), but its dimension gain is linear (|β₃/β₁| = 1.5·10⁻²).
- This moves θ from 1.99978 to 2.08078: above 1.94363, and still below 2.1610.

## 4. Consequences for the compact sup

**Corollary 4.1 (unconditional within (R80), (R80-4)).** For every d as in Lemma 2 with A(d) < ∞, and every k:
  ℓ_S^k‖d‖₂ = ‖L_S^kd‖₂ ≤ ‖L_S^kd‖_∞ ≤ A(L_S^kd) ≤ Kλ_up^kA(d).
So C_k^seed ≤ K·(2.08078464)^k·A(d)/‖d‖₂.
- The certified decay rate of the sup lies in [0.2400606, 0.4995144]. This range contains 0.46659, so no unconditional decision follows.
- The dimension price itself decays at exactly 0.49951 > 0.46659. So a proof of the supported branch (sup rate < 0.466) cannot go through any bound of the form sup ≤ A, or any price dominating A. It must exhibit cancellation between leaves, which is incompatible with (IND).
- **Angular variant.** θ_A ≤ 2.08078464 < 2.1610 ≤ 1/q_ang(2.338). The seed iterates fit the averaged-rate variant's allowance, with constant Λ = K·A(d)/‖d‖₂ and margin 3.86%. This bound holds for the seed iterates only; the B-words are not controlled (see §5).

**Theorem 4.2 (conditional on (SA_κ)).** For every d as in Lemma 2:
  ‖L_S^kd‖_∞ ≥ κA(L_S^kd) ≥ κK⁻¹λ_lo^kA(d),  and  C_k^seed ≥ κK⁻¹(2.08078462)^k.
- Since 2.08078462 > 1/q for every certified counting rate in use (q ∈ {0.5145, 0.5174, 0.518, 0.5193, 0.535, 0.5441, 0.545}; the largest 1/q is 1.94363; margin 7.06%), no pair (Λ, γ) with γ < 1/q_ρ satisfies C_k^seed ≤ Λγ^k for all k.
- This is the mission's "sign-aligned family". Its sup is ≥ c·0.49951^k: the 0.50^k of the heuristic, sharpened.
- *Proof.* Theorem 3(iii) gives the A-ratio, and (SA_κ) gives the sup. ∎

**Remark 4.3 (what (SA) really needs).**
- **Global alignment is not enough.** At a point where every leaf character equals +d_leaf (or −d_leaf), the field equals ±Σ_paths(∏β_{|e_i|}/2)d_leaf. This is the signed operator Σ(β_m/2)P_m, whose rate is 0.46191 (floating; ratio 1.92414 < 1.94363).
  - The J^{±3} coefficient is negative, so the global parity element of Round 80 (−I on all negative generators) aligns only to this signed value.
  - A refutation therefore needs leaf-by-leaf sign freedom, along the parity of the number of J^{±(4j+3)} factors in each path. That freedom is what (IND) supplies.
- **The weight-list Goursat test cannot certify (IND) at depth.** Rounds 55–68 established independence by distinguishing weight lists modulo shift (rank-one twist) and negation (duality).
  - Exact count on the J^{±1} tree from K(J²): through depth 8 the leaves fall into classes of exactly 2 with identical weight data (presumably the dual/mirror pairs). At depth 9 all 512 are separated.
  - From depth 10 on, classes of size 4 appear, and of size 6 at depth 12. They cannot be separated this way.
  - So (IND) at growing depth needs a new arithmetic input: for example, big monodromy for transported simples together with a non-isomorphism criterion beyond weight data.
- **Consistency with the floating record.** Under (IND), a physical row is a sum of many independent leaf traces. At accessible p its values are approximately Gaussian (central limit), and the sup over n coordinates reaches the compact value κA only once n is large enough to sample a jointly aligned point. That event has Haar probability roughly exp(−cΣ_leaf d²). This is consistent with the Round 187 floating law √(2 ln(n/2)) at n ≤ 5·10⁷, and with the ineffectiveness of Theorem 1. It also suggests that the (ST↓) regime of Proposition 6 sits at n doubly exponential in the height. (Heuristic; nothing here uses it.)

## 5. The increments R^comp_{602+k} and the single-B words

**Seed-tailed single-B words.** Take w^S_{a,b} = L_S^b B_h L_S^a R^comp_{602}. Here B_hL_S^aR is an output of 𝒦, so Lemma 2, Theorem 3 and (R80-4) apply to it as the root d.
- Its A-ratio grows in b exactly like θ_A^b. The upper bound is unconditional; the lower bound for the sup needs (SA).
- The dependence on a passes through B_h and is not controlled. For words L^bB_hL_S^aR with the full L, the B-parts of L^b are not controlled either.

**Corollary 5 (conditional transfer to the actual increments).** Assume (ST↓), Round 187 Proposition 6, and:
- **(SA_κ)** for R^comp_{602+k};
- **(NC)** no cancellation of the seed sector: A(R^comp_{602+k}) ≥ c·A(L_S^kR^comp_{602}) for all k. This holds, for example, if the leaves produced by words containing B_h, and by the nonlinear terms, are non-isomorphic to the seed leaves; under a global (IND) that includes the simples of h, they are;
- **(D)** decoupling E(|f|² | U₆₀₂) = ‖f‖₂² for the increments, the growing-height analogue of Round 80 (4) with J replaced by U₆₀₂. Then ‖R^comp_{602+k+1}‖₂ ≤ ‖Φ_a′(U₆₀₂)‖₂‖R^comp_{602+k}‖₂ up to the secant correction, which is relatively O(‖R₆₀₂‖);
- **(η)** η := ‖U₆₀₂ − S‖₂² < η_max(q_ρ).

Then C_k ≥ c′(λ_lo/ℓ_*)^k with λ_lo/ℓ_* > 1/q_ρ, so Criterion D in its stated form fails asymptotically.

*Proof of the L² step (exact; certify script §6).*
- By (R80-4), E(U₆₀₂²|J) = S² + η.
- y ↦ y/(4a + y) is concave and increasing, so E[Φ_a′(U)²|J] ≤ (S² + η)/(4a + S² + η).
- Averaging over θ with E[1/(A + B cos²θ)] = (A(A + B))^{−1/2} gives ‖Φ_a′(U₆₀₂)‖₂² ≤ ℓ_*(η)² := 1 − 4a/√((4a + η)(4a + η + 8)). ∎

Certified thresholds: η_max = 0.60613 (q = 0.5145), 0.66041 (0.5174), 0.67169 (0.518), 0.99833 (0.535), 1.19692 (0.545). Equivalently ‖U₆₀₂ − S‖₂ < 0.7785, …, 1.0940.

| η | ℓ_*(η) | remark |
|---|---|---|
| 0 | 0.240061 | = ℓ_S |
| 0.0306 | 0.240952 | [float input] RMS(h)² = 0.175² of Round 182; the physical full rate measured in Round 187 is 0.2405–0.2407 |
| 0.25 | 0.247225 | |
| 3.853 | 0.329703 | proved sup cap 1.963²; does not suffice |

(η) is plausibly provable from the inherited compact prefix: ‖U₆₀₂ − S‖₂ ≤ ‖U₀ − S‖₂ + ‖R₀‖₂/(1 − 0.428236) by the Round 80 real contraction. But it needs an L² bound on the initial increment that is better than the crude "below four", and I did not establish one. (NC), (SA) and (D) are open arithmetic statements.

## 6. Floating evidence (c) (explore script Part 2; double precision; orientation only)

- Fourier coefficients by the trapezoid rule agree with the arb values (β₁ = 0.33946008419, β₃ = −0.0049984361, …). The Perron roots of the truncated histogram operators (B = 300 and 1200 agree to 10 digits) are:

| operator | rate | rate/ℓ_S |
|---|---|---|
| seed-linear only (Round 182) | 0.5020882 | 2.0915 |
| exact J^{±1} term only | 0.4800691 | 1.99978 |
| full, \|β_m\|/2 | 0.4995143 | 2.08078 |
| full, signed β_m/2 | 0.4619104 | 1.92414 |

- **Growth from concrete roots.** Starting from K(J²) (r = 2), from a simple with all slots of size 1 (r = 6), and from a {0, 6}-type simple, the step ratios of A(L_S^kχ_M) converge to 0.49951 within about 20 steps. The transients range from 0.355 to 0.640.
- **Corners of Q** (t = a + 2⁻¹⁷(±1 ± i), complex β_m(t)): the |β|-rate is 0.4995142–0.4995144 and the ratio 2.080785 at all four. The real-floor certificate's margins (7.06% and 3.86%) are about 10⁶ times larger than this variation. This is not a certificate for complex t or for the second lift.

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved here (outward arb balls, exact rationals).**
- (a1) Lemma 1 (fibre-free histogram operator), under (R80). Exact checks are recorded; the operator reproduces Round 182's G_up(m), m ≤ 8.
- (a2) Lemma F: per-fibre fills are nonnegative for every formal configuration and every shift. This is unconditional as a statement about the rule.
- (a3) Lemma 2 (no collisions) and Proposition 1 (exact L² and A formulas for L_S^kχ_M), under (R80), (R80-4).
- (a4) Theorem 2: the J^{±1} part has the exact Perron vector in ℚ(√2), growth (2√2)^k within the factors √2 ∓ 1. This proves Round 182's conjecture (c3). θ₁ = √2β₁/ℓ_S ∈ [1.99978311, 1.99978311].
- (a5) Theorem 3: λ_A ∈ [0.4995143223, 0.4995143263], two-sided bounds with K = 2.356002, θ_A ∈ [2.08078462, 2.08078464].
- (a6) Corollary 4.1:
  - unconditional sup-rate range [0.2400606, 0.4995144] for the seed iterates;
  - C_k^seed ≤ K·2.08078464^k·A(d)/‖d‖₂, below the angular allowance 2.1610;
  - the impossibility of the supported branch through any A-dominating bound.
- (a7) The certified comparisons θ_A > 1/q for all seven counting rates, and θ_A < 2.1610.
- (a8) The L² step of Corollary 5: ℓ_*(η) and η_max(q).
- (a9) By-product, under Round 182's (b1) and at t = a only: the Perron-weighted price π_φ dominates the sup, ‖L_S‖_{π_φ} ≤ 0.4995143263 with C_S = 1, and the non-seed budget is β_max ≥ 0.274633 (Round 182: 0.24159).

**(b) Conditional.**
- Theorem 4.2 needs (SA_κ). With Round 187 Proposition 6 and (ST↓) it says that the stated Criterion D is incompatible with the seed iterates in the n → ∞ fixed-height regime.
- Corollary 5 needs, in addition, (NC), (D) and (η) for the actual increments.
- Everything inherits (R80) (the rule for J^{±m}) and (R80-4).

**(c) Evidence.**
- The signed rate 0.46191: global alignment would not refute.
- The weight-data class counts (exact, but they only show what the Goursat weight-list test cannot do).
- Corner sensitivity at complex t.
- The heuristic link with the Gaussian physical regime and doubly exponential saturation.

## Exact remaining gap

- **Unconditionally, the question is undecided.** The certified sup rate of the seed iterates lies in [0.24006, 0.49951], across 0.46659. The upper end is attained exactly when the compact sup equals the dimension price.
- **The blocking term is (SA)**, equivalently the Goursat independence (IND) of the leaf monodromies at growing depth, with sign/phase availability.
  - Under (SA), the stated Criterion D fails asymptotically (given (ST↓)), first for the seed iterates and then, with (NC), (D) and (η), for the increments.
  - Without (SA), a proof of the supported branch must exhibit systematic cancellation between leaves that is invisible to every A-dominating price.
- **Angular / averaged-rate variant.** The seed part fits (θ_A ≤ 2.08078 < 2.1610) unconditionally in the compact model. That variant still needs:
  - the physical growing-height L² decoupling (Round 187 next test 2);
  - control of the B-words' dimension price, which is the old non-seed multiplier problem: ‖B_h‖ in a zero-tracking price, Round 182;
  - (ST↓) only if a necessity statement is wanted.
- **Unchanged:** (ST↓), D2–D4, (b-Jk), (b-T), the uniform complex stationary domain, derivative transfer, the complex points of Q and the second lift (the real floor only is certified here); the proved frozen rate stays 1.066. Nothing here bears on the original target, the ordinary Lovász theta limit of the prime Paley localizations.

## Verdict

**Refuted, conditionally.**
- In the compact model at t = a, the dimension price of the seed iterates (and of the seed-tailed single-B words) decays at the certified rate λ_A ∈ [0.4995143223, 0.4995143263]. That is above 0.46659 and below 0.51877.
- If the compact sup is comparable to the dimension price (SA; for example, under Goursat independence of the leaves), then C_k ≥ c·θ^k with θ ∈ [2.08078462, 2.08078464]. That exceeds every 1/q_ρ ≤ 1.94363, so Criterion D in its stated form fails asymptotically (given (ST↓); for R^comp itself, also given (NC), (D) and (η)).
- θ < 2.1610, so the coordinator's rule "move to the averaged-rate variant if θ < 2.161" applies.
- Unconditionally the result is inconclusive: the certified two-sided sup-rate range is [0.24006, 0.49951], and the blocking term is (SA).

## Ranked next tests

1. **Averaged-rate (angular) Criterion D** (Round 187 next test 2), now with a quantitative target.
   - Re-prove Round 180's induction with an L² rate from a decoupling (D) instead of the pointwise q_ρ. Under (D) the needed L² rate is ℓ_*(η) ≈ 0.241, which leaves γ up to about 4. The seed part's C_k grows only like 2.0808^k (unconditional upper bound).
   - The remaining input is a sup-dominating price for B_h with rate below 1 − 0.4995 (one step, C = 1).
   - Outcome: either the variant closes for the seed sector and the problem reduces to the non-seed price, or (D) fails at growing height.
2. **Non-seed price with the Perron-weighted seed price π_φ** (Round 182 next test 1, re-targeted). The budget is now β_max ≥ 0.2746 instead of 0.2416, with C_S = 1. Price ‖B_h‖ in π_φ using the actual envelope of V₆₀₂. Decisive in either direction, as Round 182 described.
3. **(Lower value) (SA)/(IND) at small depth.** Test the Goursat independence of the depth-2 to depth-4 leaves from K(J²) and K(J^{±1}J^{±3}) by monodromy arguments, as in Rounds 55–68, beyond weight data. Also test whether the leaf groups' cosets contain the needed sign elements. This would show whether the conditional refutation is real. It cannot by itself reach growing depth.
4. **(Bookkeeping)** Record that Round 182's conjecture (c3) and its fill caveat in (b4) are settled (Theorem 2, Lemma F), and that the "2^k" heuristic is θ₁ = 1.99978, with the true θ_A = 2.08078.
5. **Do not renew:** floating searches at larger p (Round 187), and attempts to prove sup rate < 0.466 through any price that dominates the dimension price (Corollary 4.1).

## Replay commands and outputs

Run from the repository root on 2026-11-21 (python-flint 0.9.0, numpy 2.3.5). Script SHA-256 at the time of writing: certify 6ddad2ca…, explore bb87e016….

```bash
.venv/bin/python -B research/paley-188-cold-sup-growth-certify.py     # under 1 s; label (a); ends "ALL CHECKS OK"
.venv/bin/python -B research/paley-188-cold-sup-growth-explore.py     # about 4 s; Part 1 exact checks, Part 2 floating (c)
```

Key lines of the certify script (the 12 "imaginary part contains 0" and 12 "consistency" checks are all `[OK]` and omitted here):
```
  l_S^2 in [0.057629072720, 0.057629072720];  l_S in [0.240060560526, 0.240060560526]
  beta_1  in [0.33946008419161 +/- 3.7e-50]
  beta_3  in [-0.0049984361254126 +/- 5.6e-49]
  beta_5  in [0.00011094848301093 +/- 2.5e-63]
  Cauchy tail: |beta_m|/2 <= M_R 4^-m with M_R = [1.149410, 1.149410] (R = 4)
  harmonic tail (m >= 25): sum w_m <= 1.089e-15, sum m w_m <= 2.737e-14
  [OK] Parseval: sum_{m<=MH} beta_m^2/2 <= l_S^2 <= that + tail bound
  [OK] left eigen-equations phi P_1 = 2 sqrt2 phi hold (b <= 59, arb balls contain 0)
  rate with the exact J^{+-1} coefficient beta_1/2: 2 sqrt2 * beta_1/2 = sqrt2 beta_1 in [0.4800690549, 0.4800690549]; / l_S in [1.999783, 1.999783]
  rate with the seed-linear coefficient s/(4 sqrt a) (Round 182): [0.5020882046, 0.5020882046] (Round 182 conjectured 0.50206)
  [float proposal] Perron root of sum_m |beta_m|/2 P_m: 0.499514324350
  [OK] lower: phi P_lo >= lam_lo phi for sizes 0..322 (exact)
  [OK] lower: affine range b >= 323: slope 2.006e-09 >= 0 and value at 323 >= 0
  [OK] upper: phi P_hi + tail <= lam_up phi for sizes 0..322 (exact)
  [OK] upper: affine range b >= 323: slope -2.007e-09 <= 0 and value at 323 <= 0
  certified dimension-price rate lambda_A in [0.4995143223, 0.4995143263]
  c_lo = 0.617365, c_hi = 1.454513; K = c_hi/c_lo = 2.356002
  theta_A = lambda_A / l_S in [2.08078462, 2.08078464]
  [OK] theta_A > 1/q = 1.94363 (q = 0.5145); rate threshold q^-1 l_S = 0.466590
  [OK] theta_A > 1/q = 1.83486 (q = 0.545); rate threshold q^-1 l_S = 0.440478
  [OK] theta_A < 2.1610 <= 1/q_ang(2.338) (angular variant allowance, Round 187 Lemma 3(c))
  margins: theta_A / 1.94363 - 1 >= 0.0706; 2.1610 / theta_A - 1 >= 0.0386
  J^(+-1) term alone: theta in [1.99978311, 1.99978311] (> 1.94363: True)
  non-seed budget beta_max = kappa* - lam_up >= 0.274633  (Round 182: 0.24159 from pi_1 with the seed-linear part only)
    q = 0.5145: eta_max in [0.60613, 0.60613], i.e. ||U_602 - S||_2 < 0.7785
    eta = 0.0306: l_*(eta) in [0.240952, 0.240952]
    eta = 3.853: l_*(eta) in [0.329703, 0.329703]
ALL CHECKS OK
```

Key lines of the explore script:
```
  32000 children of 4000 random valid simples (m = 1, 3, 5, 7, both signs): histogram identity holds exactly
  exhaustive r <= 5, |e| <= 5: 63030 children, negative per-fibre fills: 0
  Round 182 G_up(m), m = 1..8, recomputed from the histogram operator: [4, 12, 36, 104, 300, 856, 2440, 6928] (matches Round 182: True )
  depth 10: 1024 leaves, 510 weight-data classes (mod shift, negation), largest class 4
  depth 12: 4096 leaves, 2030 weight-data classes (mod shift, negation), largest class 6
  full Phi_a'(S), |beta_m|/2 (dimension price); B = 1200: rate = 0.4995143243, rate/l_S = 2.080785
  full Phi_a'(S), signed beta_m/2 (all leaves at +dimension); B = 1200: rate = 0.4619104030, rate/l_S = 1.924141
  corner t = a + 2^-17 (+1+1i): |beta|-rate = 0.499514205, sqrt(sum|beta|^2/2) = 0.240060508, ratio = 2.080785
```
The certificates concern exact mathematical constants of the compact model: they use rational comparisons, with arb balls for the transcendental inputs. They certify no saved rounded input. The floating proposal vector is rationalized and then checked exactly, so its floating origin does not enter any certified statement.
