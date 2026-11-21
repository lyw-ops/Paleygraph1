# Round 187 native Claude draft: cold prime B-word delocalization

- call_id: `cold-prime-b-word-delocalization`
- Mission: `coordination/missions/round-187/cold-prime-b-word-delocalization.md`, exported from coordinator record `coordination/round-186.json` (SHA-256 fc1582d2…).
- Author: Claude subagent started by the Round 187 coordinator (session/r187-cold-bword). Model: Claude Opus 5.5. This is an agent draft. It is not an audit, not an acceptance and not a human review.
- Input hashes verified (SHA-256). All seven match the mission export:
  - round-185-acceptance 157de3b6…, round-186-acceptance 9f1a0ccb…, native-claude-audit-186 2b61a763…
  - native-claude-cold-prime-hybrid-price-186 6a597c9a…, paley-186-cold-hybrid-witness b810fa51…
  - cold-growing-prefix-delocalization-180 3a8eb51a…, native-claude-cold-prime-signed-nonseed-price-182 c8023a9b…
- Also read:
  - `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-186.md`; §3 and §5 of `native-claude-audit-186.md`;
  - `cold-fixed-counting-source-obstruction-179.md` (the fixed-height lower bound and its compact transfer), `astra-dissipation-80.md` (the identities E(d | J) = 0 and E(|d|² | J) = ‖d‖²), `astra-direction-83.md` (the 0.00042 source floor);
  - for the nine-centre start: `astra-predictor-76.md`, `astra-joint-65.md`, `astra-joint-64.md`, `astra-legendre-63.md`, `astra-primitive-62.md`, `astra-ranknext-58.md`, `weighted-arithmetic-57.md`, and the amplitude routine `coefficients()` of `astra-primitive-62-check.py` (run, not modified).
- Scripts written by this session (all new; none imports an earlier script):
  - `research/paley-187-cold-constants.py`: exact rationals and outward python-flint balls (label (a)). Runtime under 1 s.
  - `research/paley-187-cold-bword-rows.py`: physical rows in double precision, p up to 1.0·10⁸, with the nine-centre start. Floating, evidence only (label (c)).
  - `research/paley-187-cold-bword-fit.py`: fits and tables over the saved rows (label (c)).

## Result summary

**Verdict: inconclusive** (the mission's third branch). The measured growth law and the term that blocks a proof are below.

1. **Exact reformulation (Proposition M; proved).** For any vector, the sup/RMS ratio is squeezed between the normalized moments: M_{2m}^{1/(2m)} ≤ ratio ≤ (n M_{2m})^{1/(2m)}. So "bounded uniformly in n" means the empirical moments of the normalized entries stay below C^{2m} up to order m ≈ ln n. "Growth like √(ln n)" means Gaussian-size moments, of order (2m − 1)!!, up to that order.
2. **At every fixed height the ratio is bounded (Theorem 1; proved, inheriting the Round 179 fixed-height transfer).** For 0 ≤ k ≤ 9 (and for every k ≥ 10 under Criterion D's own polydisk hypothesis), limsup over p of sup_Q ‖R_{602+k}‖_{∞,good}/‖R_{602+k}‖_{2,n} is finite. So no √(ln n) lower bound can hold at a fixed height. The mission's refuted branch could only be realized by words whose length grows with n (k ≍ log n). The constant is ineffective and astronomically large (the bound obtained at the real floor is about 10^956), far above the Criterion D budget 9.4·10²⁰⁶. So Theorem 1 does not verify Criterion D, even at fixed k.
3. **Compact counting rates (Lemma 3; proved from the Round 80/179 compact identities).** The seed part has the exact compact counting rate ℓ_S = (1 − √(4a/(4a+8)))^{1/2} ∈ [0.2400606, 0.2400606]. The physical seed part reproduces it to 4 digits at n ≈ 10⁷. A weighted version of the Round 179 test raises the fixed-height lower rate from 0.0195 to ℓ(2.338) ∈ [0.027565, 0.027582].
4. **Without arithmetic structure the ratio grows like √(2 ln n) (Proposition H; proved, model).** Replace the Fourier eigenbasis of K by a Haar-random one, keeping its spectrum. Then K y has sup/RMS = √(2 ln n)(1 + o_P(1)) for every input y, uniformly in y. If each transport in a word is an independent such copy, every Duhamel word does the same. So a bounded ratio, if true, must come from the arithmetic structure of K.
5. **Floating evidence (p ≤ 1.0·10⁸, nine-centre start, t = a and corners of Q).** The physical ratios follow the Gaussian extreme-value law for n/2 independent values (the rows are even, f_i = f_{n−i}). This holds for R_602, for R_{602+k}, for all single-B words L^b B_h L_S^a R_602 with a + b + 1 ≤ k_n, and for the B-parts of R_{602+k}. Over n ∈ [10³, 5·10⁷], a bounded model is rejected and √(2 ln n) growth with slope ≈ 1 fits (§7). Tail counts agree with Gaussian ones up to 5σ. Fields of height ≥ 2 already behave this way. The rank-two field Y and the height-one seed iterate saturate at their compact bound 2√2.
6. **Reading (heuristic, labelled).** Items 2 and 5 are compatible: at accessible n the B-words are in a pre-asymptotic Gaussian regime; at each fixed height the ratio eventually saturates at its compact value C_k. Criterion D in its n-independent form then needs C_k ≤ Λγ^k with q_ργ < 1 (Proposition 6, conditional on a lower sup transfer). In the per-simple model the compact sup/L² ratio grows like θ^k with θ = 2 (dimension growth 2√2 against L² growth √2 per step). That is just above every allowance 1/q ≤ 1.9436 of the stated criterion and just below the allowance 1/q_ang ≥ 2.161 of an angular-rate variant. So the decisive quantity for Criterion D is this compact growth rate, not the √(ln n) seen at accessible n.
7. **Remaining gap.** Criterion D needs control uniform over growing heights k < k_n. Equivalently (Proposition M), it needs moment bounds of order ≈ ln n, or a sup transfer, for words of length ≍ log n. The available inputs are fixed-height only (Theorem 1), and their rates (sup side 1.066 or 2ρ; L² side ≥ 0.0276) are far from the observed 0.24/0.24.

## Setup and inherited statements

- p ≡ 1 (mod 4) prime, n = (p − 1)/2, a = 2031/128, Q the closed square of half-width 2⁻¹⁷ about a, N = 4(a − 2⁻¹⁷). Physical mark t₀ = n; both lifts; genuine nine-centre start.
- K is the real symmetric circulant on ℤ/n with eigenvalues λ_j = χ(1 − g^{2j}). So K = FΛFᵀ, with F the real Fourier basis, Λ = diag(λ_j), λ₀ = 0 and λ_j = ±1 otherwise, and Σλ_j = −1 (Round 186 Lemma 1). In particular K² = I − P₀, where P₀ is the projection on constants, and ‖Ky‖₂² = ‖y‖₂² − |Σy|²/n exactly.
- S = 2√n Ke₀; V_{h+1} = KΦ_t(V_h), Φ_t(x) = √(4t + x²); R_h = V_{h+1} − V_h.
- Frozen operators at 602 (Round 182): L = KD₆₀₂ = L_S + B_h, with L_S = K(Φ_t′(S)·) and B_h = K((Φ_t′(V₆₀₂) − Φ_t′(S))·).
- Ratio: Rat(f) := ‖f‖_{∞,good}/‖f‖_{2,n}. Good coordinates exclude the mark and the at most b₀ ≤ 3 bad coordinates (as in Round 186).
- **Criterion D (Round 180, inherited verbatim).** Fix ρ ∈ {0.025, 0.05, 3/8} with contraction q_ρ, and fix 0 < η < ρ, Λ ≥ 1 and γ ≥ 1 with q_ργ < 1. Suppose that for all large eligible p, all t ∈ Q, both lifts, and every k < k_n = ⌈(4/7)log₂n⌉ along a prefix that has so far stayed in the ρ-polydisk,
  ‖R_{602+k}‖_∞ ≤ Λγ^k‖R_{602+k}‖_{2,n}.
  Then the prefix stays in the (ρ − η)-polydisk with clearance η, and the Round 173 tail gives common stationary continuation on the interior of Q. With γ = 1 and η = ρ/2, any n-independent Λ below 6.5·10²⁰⁵ suffices at ρ = 0.025, and below 9.4·10²⁰⁶ at ρ = 3/8. The criterion is sufficient, not necessary.
  - The contractions are q_{0.025} ≈ 0.5174, q_{0.05} ≈ 0.5193 and q_{3/8} ≈ 0.5441 (Round 180). The certified counting rates elsewhere are 0.5145 (Round 128), 0.518 (Round 173, frozen) and 0.545 (Round 177). So 1/q ≤ 1.9436 for every rate in use (constants script §5).
- **Other inherited inputs:**
  - Round 177: ‖V₆₀₂ − S‖_∞ < 1.963.
  - Round 180: the fixed prefix through V₆₁₂ lies in the 3/8-disks; 0 < liminf_p inf_Q ‖R₆₀₂‖_{2,n} ≤ limsup < 9.07·10⁻²⁰⁹ (ineffective).
  - Round 179: the fixed-height compact transfer with the mark; the compact identities E(d | J) = 0 and E(|d|² | J) = ‖d‖² for genuine increments; isometry of 𝒦 modulo constants on even activation inputs; caps |U_j − S| ≤ 2.338 through height 612; the real-floor source bound liminf_p‖R₀(a)‖_{2,n} > 0.00042 (Round 83).
  - Round 186: Theorem N.
  - Round 182 Lemma 3.2 for the per-simple seed rates, which are quoted only in the heuristic §6.

## 1. What "bounded versus √(ln n)" means exactly

**Proposition M (proved; elementary).** Let f ∈ ℂⁿ with ‖f‖_{2,n} > 0. Let 𝒢 be its good coordinates, n_g = |𝒢|, and put M_{2m}(f) = n_g⁻¹Σ_{x∈𝒢}(|f_x|/‖f‖_{2,n})^{2m}. Then for every m ≥ 1:
  M_{2m}(f)^{1/(2m)} ≤ Rat(f) ≤ (n_g M_{2m}(f))^{1/(2m)}.

*Proof.* The maximum dominates every power mean, and its 2m-th power is at most the sum. ∎

**Corollary M1 (the dichotomy, exactly).**
- (i) If Rat(f_n) ≤ Λ for all n, then M_{2m}(f_n) ≤ Λ^{2m} for every m and n.
- (ii) Conversely, if M_{2m}(f_n) ≤ C^{2m} at the single order m = ⌈ln n⌉, then Rat(f_n) ≤ e^{1/2}C, since n^{1/(2m)} ≤ e^{1/2}.
- (iii) If M_{2m}(f_n) ≥ (2m − 1)!! at m = ⌊ln n⌋, then Rat(f_n) ≥ ((2m − 1)!!)^{1/(2m)} ≥ (1 − o(1))√(2 ln n/e). If moreover M_{2m} ≤ (2m − 1)!! at m = ⌈ln n⌉, then Rat(f_n) ≤ (1 + o(1))√(2 ln n).

So Criterion D with an n-independent Λ (at fixed k) is equivalent, up to the factor e^{1/2}, to n-uniform bounds M_{2m} ≤ C^{2m} for all orders m up to ln n. The √(ln n) alternative is Gaussian moment growth up to that order. Any proof either way must control moments of order ≍ log n, or the sup directly. Fixed-order moment transfer (Rounds 79/80) does not reach that order.

Numbers (constants script §4, exact): ((2m − 1)!!)^{1/(2m)} = 1.316, 1.570, 1.789, …, 2.478 (m = 8), 3.014 (m = 12). Also √(2 ln n) reaches the Criterion D budgets 6.5·10²⁰⁵ and 9.4·10²⁰⁶ only when log₁₀n ≥ 9.17·10⁴¹⁰ and 1.92·10⁴¹³ respectively.

## 2. Theorem 1: every fixed height has a bounded ratio

**Theorem 1 (proved; inherits the ineffective Round 179 fixed-height compact transfer).** Fix k ≥ 0 and ρ ∈ (0, 3/8]. Assume:
- (H_k) for all sufficiently large eligible p, all t ∈ Q and both lifts, the rows V₆₀₂, …, V_{603+k} lie in the closed coordinate polydisk of radius ρ about V₆₀₂.

Then there are c_k > 0 and p_k, both ineffective, such that for p ≥ p_k, all t ∈ Q and both lifts:
  ‖R_{602+k}‖_{2,n} ≥ c_k, and hence Rat(R_{602+k}) ≤ 2ρ/c_k.
- (H_k) holds with ρ = 3/8 for 0 ≤ k ≤ 9, by Round 180's fixed prefix through V₆₁₂.
- For k ≥ 10, (H_k) is exactly the inductive hypothesis under which Criterion D is applied.

*Proof.*
1. **Upper bound on the sup.** Every coordinate of R_{602+k} = (V_{603+k} − V₆₀₂) − (V_{602+k} − V₆₀₂) has modulus ≤ 2ρ, by (H_k).
2. **Caps.** For j ≤ 612, Round 179 gives the compact caps |U_j − S| ≤ 2.338. For 612 < j ≤ 603 + k, (H_k) and Round 177 give |V_j − S| ≤ |V_j − V₆₀₂| + |V₆₀₂ − S| < ρ + 1.963 ≤ 2.338 at every coordinate. Then |V_j| ≤ s_p + 2.338 < 5.2, which is the coordinate cap Round 179's cutoff construction uses.
3. **Fixed-height transfer.** With these caps, Round 179's argument applies verbatim at the fixed height 603 + k. That argument consists of the cutoff activation, the joint second-norm identification of the rows along a compact subsequence, the restoration of the mark, the nonvanishing initial increment, and the chain of lower secant factors on every step whose segment lies within 2.338 of S. A violating sequence with ‖R_{602+k}(t_p)‖_{2,n} → 0 would converge to a compact increment that is both zero and nonzero. ∎

**Corollary 1.1 (no fixed-word √(ln n) law).** Under (H_k), Rat(R_{602+k})/√(ln n) → 0 uniformly on Q and both lifts. Consequently:
- A statement "Rat ≥ c√(ln n) for all large n" is false at every fixed k ≤ 9, and at every fixed k under (H_k).
- The √(2 ln n) behaviour measured at accessible n (§7) must saturate at each fixed height.
- A provable √(ln n) obstruction to Criterion D can only come from heights k → ∞ with n, i.e. from the growing part of the horizon.
- Likewise, the n-dependence of Λ_n := max_{k<k_n} Rat(R_{602+k})/γ^k is entirely a growing-height phenomenon.

**Corollary 1.2 (quantitative at the real floor; same ineffective threshold).** At t = a the chain constant can be made explicit:
- c_k ≥ 0.00042·ℓ(2.338)^{602+k}, using the Round 83 source floor and Lemma 3(b) below. Round 179 used 0.019 per step.
- For k ≤ 9, log₁₀c_k ≥ −956.32. So Rat(R_{602+k}(a)) ≤ 10^{956.2} for all p beyond an ineffective threshold (constants script §3).
- This is bounded but far above the Criterion D budget (≤ 9.4·10²⁰⁶). Theorem 1 therefore settles the n-dependence at fixed height and nothing more.

**Corollary 1.3 (single-B words at fixed length; conditional).** Fix (a, b). Suppose:
- (P) there is a sup-dominating price P on a class containing R₆₀₂, closed under L, L_S and B_h, with n-uniformly finite ‖L‖_P, ‖L_S‖_P, ‖B_h‖_P and P(R₆₀₂). An example is A_𝒳 under D1–D4 with the Round 184 Propositions A–C and a finite A(h), as quoted in Round 186.
- (W⁺) liminf_p inf_Q ‖w_{a,b}‖_{2,n} > 0 for w_{a,b} = L^bB_hL_S^aR₆₀₂.

Then Rat(w_{a,b}) is bounded uniformly in n. Without (W⁺), only the numerator is controlled. (W⁺) is plausible (in the compact model ‖B_h f‖₂ = ‖(Φ′(V) − Φ′(S))f − mean‖₂), but it is not proved here.

## 3. Lemma 3: compact counting rates of the increments

All statements are in the subsequential compact model of Rounds 79/179, at the real floor t = a, with real segments. A *compact increment* d is a field with E(d | J) = 0 and E(|d|² | J) = ‖d‖₂² (Round 179 for genuine adjacent differences; Round 80 (4) for differences of transported fields).

**Lemma 3.**
- **(a) Exact seed rate.** For every compact increment d, ‖𝒦(Φ_a′(S)d)‖₂ = ℓ_S‖d‖₂, with ℓ_S² = E_θ[Φ_a′(√8 cos θ)²] = 1 − √(4a/(4a + 8)) and ℓ_S ∈ [0.2400606, 0.2400606].
  - If L_S^jd stays in the class of compact increments (inherited reading of Round 80 (4) for transported fields), then ‖L_S^kd‖₂ = ℓ_S^k‖d‖₂ exactly.
- **(b) Weighted lower rate.** Let d = U_j − U_{j−1} be a compact increment whose segment satisfies |z − S| ≤ c. Then ‖U_{j+1} − U_j‖₂ ≥ ℓ(c)‖d‖₂, with ℓ(c)² = E_θ[Φ_a′((√8|cos θ| − c)_+)²]. Certified values:
  - ℓ(2.338) ∈ [0.027565, 0.027582];
  - ℓ(1.988) ∈ [0.054027, 0.054052];
  - ℓ(0.985) ∈ [0.143017, 0.143061] [float cap input];
  - ℓ(0) ∈ [0.240031, 0.240090], consistent with (a).
- **(c) Angular upper rate.** Under the same hypotheses, ‖U_{j+1} − U_j‖₂ ≤ q_ang(c)‖d‖₂, with q_ang(c)² = E_θ[Φ_a′(√8|cos θ| + c)²]. Certified values:
  - q_ang(1.94) ∈ [0.428191, 0.428251] (the real-floor analogue of Round 80's 0.449922);
  - q_ang(2.338) ∈ [0.462690, 0.462748], so 1/q_ang(2.338) ≥ 2.1610.

*Proof.*
- (a) Put T = Φ_a′(S)d. Then E T = E[Φ_a′(S)E(d | J)] = 0, and ‖T‖₂² = E[Φ_a′(S)²E(|d|² | J)] = E[Φ_a′(S)²]‖d‖₂². The transport is an isometry modulo constants, so ‖𝒦T‖₂ = ‖T − ET‖₂ = ℓ_S‖d‖₂. The closed form uses E[1/(A + B cos²θ)] = (A(A + B))^{−1/2}.
- (b) Let D̃ = ∫₀¹Φ_a′(U_{j−1} + sd)ds, so that T = F(U_j) − F(U_{j−1}) = D̃d. Put σ = sgn S and m(S) = Φ_a′((|S| − c)_+).
  - Where |S| > c, every segment point z is real with σz ≥ |S| − c > 0. Since Φ_a′ is odd and increasing, σD̃ ≥ m(S) ≥ 0. Where |S| ≤ c, m = 0.
  - Test against τ = σ m(S) d. Then E τ = E[σ m E(d | J)] = 0, and ‖τ‖₂² = E[m²]‖d‖₂².
  - Re⟨T − ET, τ⟩ = E[σD̃ m|d|²] ≥ E[m²|d|²] = E[m²]‖d‖₂².
  - So ‖𝒦T‖₂ = ‖T − ET‖₂ ≥ E[m²]^{1/2}‖d‖₂.
  - Round 179's test is the special case m = indicator × 0.349/8, giving 0.349/(8√5) = 0.01951.
- (c) Pointwise |D̃| ≤ Φ_a′(|S| + c). Hence ‖T − ET‖₂² ≤ ‖T‖₂² ≤ E[Φ_a′(|S| + c)²|d|²] = q_ang(c)²‖d‖₂².
- The numbers are monotone Riemann sums with 4000 cells in outward arithmetic. Both integrands are monotone in θ on [0, π/2]. ∎

**Floating check of (a).** The physical seed part L_S^kR₆₀₂ has a per-step RMS ratio of 0.25071 (n ≈ 10³), 0.24234 (10⁴), 0.24104 (2·10⁵), 0.24009 (5·10⁶) and 0.24013 (10⁷). This converges to ℓ_S = 0.2400606. The full increments have rate 0.2405 at n ≈ 10⁷, against Round 80's upper bound 0.449922.

## 4. Proposition H: the Haar model grows like √(2 ln n)

**Proposition H (proved; model).** Let E₀ = 𝟙^⊥ ⊂ ℝⁿ. Let Λ be a fixed self-adjoint involution of E₀ with |tr Λ| ≤ C₀√n (the Paley Λ has tr = −1). Let U be Haar-distributed on O(E₀) and put K_U = UΛUᵀ on E₀, K_U𝟙 = 0. The physical K is the case U = F. Then for every ε > 0:
  sup_{y∉ℝ𝟙} P(|Rat(K_U y)/√(2 ln n) − 1| > ε) → 0 as n → ∞.
The same holds with Rat taken over any set of coordinates of size n − O(1).

*Proof.*
1. **Reduction.** Let y₀ = y − ȳ𝟙 ≠ 0 and f = K_U y = K_U y₀. Then |f| = |y₀|, since Λ is orthogonal on E₀.
2. **Invariance.** For V ∈ H := {V ∈ O(E₀) : Vy₀ = y₀}, VU is again Haar and K_{VU}y₀ = VK_Uy₀. So f has the same law as Vf for every V ∈ H.
3. **Decomposition.** Write f = αy₀ + w with w ⊥ y₀. The scalar α is H-invariant, and |w|² = (1 − α²)|y₀|². H acts on E₁ = E₀ ∩ y₀^⊥ as all of O(E₁). Hence, conditionally on α, w is uniform on the sphere of radius |w| in E₁.
4. **Size of α.** α = Σ_jλ_jξ_j, where ξ_j = (Uᵀŷ₀)_j² has the Dirichlet(½, …, ½) law in N = n − 1 coordinates. So E α = tr Λ/N and Var α ≤ 2/(N + 2). Hence |α| = O_P(n^{−1/2}), and |α|·‖y₀‖_∞ ≤ |α||y₀| = O_P(n^{−1/2})·√n‖f‖_{2,n} = O_P(1)·‖f‖_{2,n}.
5. **The uniform part.** Realize w = |w|·Pg/|Pg|, with g standard Gaussian in ℝⁿ independent of α and P the orthogonal projection onto E₁. Then |(Pg)_i − g_i| ≤ |⟨g, ŷ₀⟩| + |⟨g, 𝟙⟩|/n, with ⟨g, ŷ₀⟩ and ⟨g, 𝟙⟩/√n standard normal. Also max_i|g_i|/√(2 ln n) → 1 and |Pg|/√n → 1 in probability (classical; removing O(1) coordinates changes nothing).
6. **Conclusion.** √n·max|w_i|/|y₀| = √(2 ln n)(1 + o_P(1)), and ‖f‖_{2,n} = |y₀|/√n. The bounds in steps 4–5 do not depend on y. ∎

**Corollary H1 (independent-transport model of the words).** Let K₁, …, K_m be independent copies of K_U, and let D₁, …, D_m and r be deterministic. Then every word w = K_mD_m ⋯ K₁D₁r with D_m(K_{m−1}⋯) ∉ ℝ𝟙 satisfies Rat(w)/√(2 ln n) → 1 in probability, uniformly in m, the D's and r.

*Proof.* Condition on K₁, …, K_{m−1}. The input of K_m is then independent of U_m, and Proposition H applies uniformly. ∎

**Reading.**
- In the rotation-invariant ("free") model of the cold map, every B-word has ratio √(2 ln n)(1 + o(1)). So Criterion D fails in its n-independent form there, for every word length.
- Combined with Theorem 1, any proof of a bounded ratio must use the arithmetic structure of K: its Fourier eigenbasis and the Deligne-type structure of the fields. This is the ratio analogue of Round 186 Theorem N, which says the same for the price.
- The physical rows at p ≤ 10⁸ are numerically indistinguishable from this model (§7). The even symmetry f_i = f_{n−i} of the physical rows halves the number of independent values, so the physical reference law is that of n/2 values.

## 5. Proposition 6: the n → ∞ limit at fixed height (conditional)

**Hypothesis (ST↓_k), a lower fixed-height sup transfer.** Along every subsequence of eligible primes with t_p → t ∈ Q on which the rows converge to a compact model (Round 179):
- liminf ‖R_{602+k}‖_{∞,good} ≥ ‖R^comp_{602+k}‖_∞, the essential supremum of the compact increment;
- ‖R_{602+k}‖_{2,n} → ‖R^comp_{602+k}‖₂ (the second part is the inherited fixed-height L² transfer).

The first part would follow from equidistribution of the Frobenius classes in the compact monodromy group together with continuity of the compact field (finite price). It is not proved here.

**Proposition 6 (proved under (ST↓_k) for all k).** If Criterion D holds with constants (Λ, γ), then every subsequential compact model satisfies
  C_k := ‖R^comp_{602+k}‖_∞/‖R^comp_{602+k}‖₂ ≤ Λγ^k for all k ≥ 0,
with q_ργ < 1, so γ < 1/q_ρ ≤ 1.9436.

*Proof.* Criterion D quantifies over all large p and every k < k_n, and k_n → ∞. Fix k and pass to the limit along the subsequence. ∎

So in the n → ∞ regime the n-independent Criterion D is a statement about the growth in k of the compact sup/L² ratio, not about √(ln n). Theorem 1 says C_k < ∞ for each k (under (H_k)). The question is whether C_k grows more slowly than (1/q_ρ)^k.

## 6. Heuristic: the compact ratio grows like 2^k (labelled heuristic; not used in any proof)

- **L² side.** By Lemma 3(a), the seed part of the compact increments decays exactly like ℓ_S^k, with ℓ_S = 0.24006. The physical full increments decay at 0.2405 (§7).
  - In the per-simple model (Round 182), the seed-linear part sends each simple to two children with coefficient factor s/(4√a) = 0.17752. On orthonormal traces this is an L² growth of √2·0.17752 = 0.2510 per step. The exact 0.2401 includes the cubic and higher seed terms.
- **Sup side.** If the compact sup of a field whose simples carry independent Haar factors equals its dimension price up to collisions (heuristic H-sup: align each factor near ±identity), then the sup decays like the dimension-price rate.
  - That rate is (r′₊ + r′₋)/r × 0.17752 ∈ [0.355, 0.710) per step (Round 182 Lemma 3.1).
  - Asymptotically it is 2√2 × 0.17752 = 0.50206, the leading-field limit that Round 182 records as a conjecture (G_m^{1/m}: 3.02, 2.94, 2.89 at m = 8 for α = 0, ½, 1, decreasing towards 2√2).
- **Ratio.** The per-step growth of C_k is then θ = (2√2·0.1775)/(√2·0.1775) = 2 asymptotically. With the exact seed L² rate in the denominator it is θ ∈ [2.0914, 2.0914] at the leading-field rate, and [2.2184, 2.9578] at the one-step rates (constants script §5).
- **Comparison.**
  - Against the stated criterion, 1/q ∈ {1.9436, 1.9327, 1.9305, 1.8692, 1.8349} for q ∈ {0.5145, 0.5174, 0.518, 0.535, 0.545}. All are below 2.
  - A variant of Criterion D whose convexity step uses an upper counting rate for the increments instead of the pointwise rate q_ρ would allow γ < 1/q_ang(2.338), with 1/q_ang(2.338) ≥ 2.1610. That is above 2, but below the one-step values.
  - Equivalently, the pointwise frozen rate q₀ = sup|Φ_a′(V₆₀₂)| would need |V₆₀₂| < 4.5996 at real t for 1/q₀ > 2 (exact; Round 173 uses the cap that gives 0.518; the floating sup|V₆₀₂| ≈ 3.32 gives 0.3847).
- **Reading.** If H-sup holds, Criterion D in its stated form (with the certified q_ρ) fails in the n → ∞ fixed-height regime by a small margin, for a reason unrelated to √(ln n).
  - Confinement itself would not be affected: the sups would still decay like ≈ 0.50^k, and Σ_k‖R_{602+k}‖_∞ ≈ 2·(compact sup of R₆₀₂) ≤ 2A(R₆₀₂) < 0.0255 < 3/16.
  - The natural tool in that regime is a sup-dominating price with rate < 1, i.e. the price programme, which Theorem N restricts to structured information about h.
  - These are heuristics stacked on a conjectured Perron root and an unproved sup/price identification. They are recorded to locate the decisive quantity, not as a result.

## 7. Floating evidence (c) (`…-bword-rows.py`, `…-bword-fit.py`; double precision, evidence only)

**What was computed.**
- **Primes.** 49 primes p ≡ 1 (mod 4) with n = (p − 1)/2 13-smooth: four near each n ∈ {10³, 2·10³, 5·10³, 10⁴, 2·10⁴, 5·10⁴, 10⁵, 2·10⁵, 5·10⁵, 10⁶}, then 2 primes near each of 2·10⁶, 5·10⁶, 10⁷ and 2·10⁷, and p = 100018801 (n = 50009400).
- **Start.** The nine-centre row
  V₀ = S + αY + βW + γF₄ + δG + zR + wQ + v(U + U′),
  built from its physical fields as recorded in Rounds 57–65 (formulas in the script header). The Legendre traces A, B are the Mellin transforms of ℓ·(ℓ∗ℓ) at the two lifts. The amplitudes are (α, β, γ, δ) = (0.243408316565, 0.082584064225, 0.0279615357329, −0.0094859449111), from `astra-primitive-62-check.py` `coefficients()` (Arb radius < 5·10⁻¹³), and z = 1.701367523·10⁻³, w = 8.50649424·10⁻⁴, v = −9.00249249·10⁻⁴.
  - Two exceptional constants were dropped: the unknown h_q in D₄, and D_q in G. Each changes coordinates by O(n^{−1/2}).
  - Checks: E A² = 0.99960 at p = 10009; the Legendre traces are real (|Im| < 2.1·10⁻¹⁵); AB and A² + B² are even rows; sup|V₀ − S| ≈ 0.49–0.54.
- **Iteration.** The exact map is applied for 602 steps, with the increment carried as (log scale, unit direction) through the stable secant R(2V + R)/(Φ(V + R) + Φ(V)). Below double precision this is the tangent map at the numerically fixed row. Measured: log₁₀‖R₆₀₂‖_{2,n} ≈ −375.2 at large n, consistent with Round 180's < 9.07·10⁻²⁰⁹. The per-step rate is 0.2405–0.2407.
- **Measured vectors.** R_{602+k} = L^kr₆₀₂ for k < k_n (this equals the actual increments up to relative O(‖R₆₀₂‖)); all single-B words w_{a,b} = L^bB_hL_S^ar₆₀₂ with a + b + 1 ≤ k_n (up to 120 words at n = 5·10⁷); the B-parts L^kr − L_S^kr; and the seed parts.
- **Controls.** iid Gaussian vectors; the nine-centre fields; and growing-height seed iterates L_S^mS.
- **Symmetry.** All real rows are even (f_i = f_{n−i}, checked to 10⁻¹⁵), because S is even and K, Φ preserve evenness. So a row has n/2 distinct good values. The reference law is E_G(n/2), the expected maximum of n/2 iid |N(0, 1)|, and tail counts come in pairs.

**Table (selected primes; full table in the fit output).** All entries are sup_good/RMS.

| p | n | k_n | E_G(n/2) | R₆₀₂ | B r₆₀₂ | mean over words | max over words | Λ_n(γ=1) = max_k Rat(R_{602+k}) | mean B-part | iid control (E_G(n−1)) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2017 | 1008 | 6 | 3.244 | 3.072 | 3.231 | 2.978 | 3.231 | 3.072 | 2.961 | 3.215 (3.437) |
| 9901 | 4950 | 8 | 3.675 | 4.498 | 3.576 | 3.627 | 4.102 | 4.498 | 3.654 | 3.946 (3.849) |
| 100673 | 50336 | 9 | 4.232 | 4.433 | 4.041 | 4.211 | 5.138 | 4.681 | 4.288 | 4.356 (4.386) |
| 1006237 | 503118 | 11 | 4.725 | 4.800 | 4.608 | 4.663 | 5.460 | 5.188 | 4.773 | 4.807 (4.864) |
| 10001881 | 5000940 | 13 | 5.173 | 5.417 | 5.315 | 5.183 | 6.310 | 5.417 | 5.112 | 5.286 (5.301) |
| 40080041 | 20040020 | 14 | 5.427 | 5.279 | 5.368 | 5.420 | 6.337 | 6.008 | 5.357 | 5.506 (5.549) |
| 100018801 | 50009400 | 15 | 5.588 | 5.548 | 5.697 | 5.612 | 6.280 | 5.794 | 5.598 | 5.618 (5.707) |

**Growth-law fits over the 49 primes.** Weighted least squares. Single vectors use σ = sd of the Gaussian maximum; averages use the across-prime residual scatter. The bootstrap is over primes, 4000 resamples. The Gaussian reference slope of E_G(n/2) on √(2 ln n) over this range is b_G = 1.049.

| family | bounded c: χ²/dof | a + b√(2 ln n): b (OLS), 95% CI | E_G(n/2) + d: d, χ²/dof | k·E_G(n/2): k |
|---|---|---|---|---|
| R₆₀₂ (one vector per prime) | 206.1/48 = 4.29 | 0.760, [0.605, 0.908] | +0.042, 1.30 | 1.005 |
| B r₆₀₂ | 303.2/48 = 6.32 | 1.034, [0.943, 1.126] | −0.044, 0.67 | 0.990 |
| mean over all single-B words | 2234.2/48 = 46.6 | 1.021, [0.962, 1.079] | +0.009, 1.00 | 1.001 |
| mean over R_{602+k}, k < k_n | 224.0/48 = 4.67 | 0.846, [0.698, 0.972] | +0.086, 1.00 | 1.015 |
| mean over B-parts of R_{602+k} | 1405.0/48 = 29.3 | 0.996, [0.939, 1.059] | +0.014, 1.00 | 1.002 |
| iid Gaussian control | 840.1/48 = 17.5 | 1.007, [0.941, 1.067] | −0.023 (vs E_G(n−1)), 0.74 | 0.995 |

- **Excess of the word mean over E_G(n/2), by decade:** +0.050 (n ∈ [10³, 10⁴)), −0.024, −0.016, +0.024 and +0.004 (n ∈ [10⁷, 10⁸)). The B-generated part shows no trend away from the Gaussian law.
- **The lower slope for R₆₀₂ alone** comes from the smallest primes. At n ≈ 10³ the increment direction is sometimes localized: M₁₆/15!! = 57 at p = 2081, and the R₆₀₂ excess is +0.40 for n < 10⁴. From n ≥ 10⁴ on, R₆₀₂ also tracks E_G (excess −0.04, +0.02, −0.08, −0.10 by decade).
- **Tails.** At p = 100018801 the counts above 2, 3, 4, 4.5, 5, 5.5 and 6 RMS are, for R₆₀₂: 2276014, 135152, 3266, 350, 20, 2, 0. The Gaussian expectations are 2275441, 135015, 3168, 340, 28.7, 1.9, 0.1. The pair-corrected z-scores are within ±1.2. For B r₆₀₂ the counts are 3168, 330, 36 and 4 above 4, 4.5, 5 and 5.5; for w_{0,14} they are 3290, 386, 30 and 2. One count in about 60 lies at |z| ≈ 4 (R₆₀₃ above 5.5: 10 against 1.9).
- **Moments.** M_{2m}/(2m − 1)!! for R₆₀₂ at n = 5·10⁷ is 1.000, 1.000, 0.999, 0.998, 0.994, 0.986, 0.970 for 2m = 4, …, 16. The last values fall slightly below 1 because a sample of n/2 values truncates the high moments. This holds at every n ≥ 10⁶.
- **Fixed-height fields at n = 5·10⁷** (sup/RMS; M₄/3):
  - Y: 2.825; 0.834. This is the rank-two field. It is bounded and saturates at 2√2 = 2.828 from n ≈ 10⁵ on.
  - W 5.533, F₄ 5.805, G 5.451, R 5.591, Q 4.969, U + U′ 5.018, all with M₄/3 ≈ 1.00. These still rise with n like E_G.
  - S: √2 exactly; h = V₆₀₂ − S: 3.58.
- **Height growth (seed iterates L_S^mS).** m = 0: √2; m = 1: 2.83, which saturates at 2√2 like Y. For m ≥ 2 the curve is already at the Gaussian level: the mean over m ≥ 4 is 3.27, 4.01, 4.91, 5.63 at n ≈ 10³, 2·10⁴, 10⁶, 5·10⁷, against E_G(n/2) = 3.24, 4.02, 4.86, 5.59.
- **Counting rates.** The seed-part per-step RMS ratio is 0.25071, 0.24524, 0.24224, 0.24064, 0.24024, 0.24007 at n ≈ 10³, 5·10³, 10⁵, 5·10⁵, 2·10⁶, 5·10⁷. Lemma 3(a) predicts 0.2400606. The full increments have rate 0.2407.
- **Sensitivity.**
  - The three distinct corners a ± 2⁻¹⁷(1 ± i), at p = 200201 and 2002001, reproduce every ratio of the real floor to three decimals. (pm and mm are complex conjugates of pp and mp, with the same moduli.)
  - The seed start V₀ = S changes individual vectors (R₆₀₂: 4.771 → 5.092 at p = 200201), but not the statistics: word mean 4.396 vs 4.371, and 4.908 vs 4.931 at p = 2002001. The increment direction depends on the start, since the top of the spectrum of L is a dense near-degenerate ring of radius ≈ RMS(Φ′(V)). This was seen in a dense eigenvalue check at p ≤ 10⁴ (scratch, not saved). The sup/RMS law does not depend on the start.
- **Reading.**
  - Over n ∈ [10³, 5·10⁷], every B-generated family behaves like the maximum of n/2 Gaussian values: Rat ≈ E_G(n/2) ≈ √(2 ln(n/2)) − O(ln ln n/√(ln n)).
  - A bounded law is rejected throughout this range (χ²/dof 4–47). The fitted slope on √(2 ln n) is 1.02 ± 0.06 for the word mean, against 1.05 for the Gaussian law and 0 for a bounded law.
  - This is the pre-asymptotic regime described in §§2, 4 and 6. It says nothing about saturation beyond 5·10⁷, which Theorem 1 guarantees at each fixed height.
- Not covered: the second square-root sheet, i.e. a sign change of Φ on some coordinates (one principal branch only); interval arithmetic of any kind.

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved here.** Every number is given by exact rationals or outward balls (`…-constants.py`).
- (a1) **Proposition M** and **Corollary M1**: sup/RMS is squeezed by the normalized moments. The n-independent ratio is equivalent, up to e^{1/2}, to moment bounds C^{2m} up to order ⌈ln n⌉; √(ln n) growth is Gaussian moment growth up to that order. Constants: ((2m − 1)!!)^{1/(2m)}, and the thresholds log₁₀n ≥ 9.17·10⁴¹⁰ and 1.92·10⁴¹³ at which √(2 ln n) reaches the Criterion D budgets.
- (a2) **Theorem 1** and **Corollaries 1.1–1.2**: for each fixed k (k ≤ 9 unconditionally on inherited inputs; k ≥ 10 under (H_k)), the ratio Rat(R_{602+k}) is bounded uniformly in n, uniformly on Q and both lifts, with an ineffective constant. Hence no √(ln n) lower bound holds at any fixed height. At the real floor the bound is ≤ 10^{956.2} beyond an ineffective threshold, far above every Criterion D budget. The proof inherits Round 179's fixed-height compact transfer, Round 180's prefix through V₆₁₂ and Round 177's 1.963.
- (a3) **Lemma 3** (compact model, real floor; given the Round 80/179 identities):
  - (a) the exact seed rate ℓ_S ∈ [0.2400606, 0.2400606];
  - (b) the weighted lower rate ℓ(2.338) ∈ [0.027565, 0.027582], against Round 179's 0.0195;
  - (c) the angular upper rates q_ang(1.94) ∈ [0.428191, 0.428251] and q_ang(2.338) ∈ [0.462690, 0.462748].
- (a4) **Proposition H** and **Corollary H1** (model): with a Haar eigenbasis (balanced spectrum ±1), Rat(K_Uy) = √(2 ln n)(1 + o_P(1)) uniformly in y, and every word in the independent-transport model behaves the same way.
- (a5) **Proposition 6**, as an implication: Criterion D together with (ST↓) implies C_k ≤ Λγ^k with γ < 1/q_ρ ≤ 1.9436.

**(b) Conditional / inherited.**
- Round 179's fixed-height compact transfer, caps 2.338 and the source floor 0.00042 (Round 83); Round 180's prefix through V₆₁₂ in the 3/8-disks; Round 177's 1.963. All are used in Theorem 1.
- Round 80 (4) for transported fields (E(|d|² | J) = ‖d‖²). It is used to iterate Lemma 3(a).
- Corollary 1.3 needs a price (P), e.g. A_𝒳 under D1–D4, and the positivity (W⁺), which is unproved.
- Proposition 6 needs the lower sup transfer (ST↓), which is unproved.
- §6 is heuristic. It relies on H-sup (compact sup ≈ dimension price), on the conjectured leading-field Perron rate 0.50206 (Round 182), and on dominance of the seed-linear part.

**(c) Evidence.** The §7 tables. Physical ratios follow the Gaussian maximum law of n/2 values for every B-generated family, with slope 1.02 ± 0.06 on √(2 ln n); bounded fits are rejected on n ∈ [10³, 5·10⁷]. Gaussian tails hold to 5.5σ and moments to order 16. The rank-two field and the height-one seed iterate saturate at 2√2. The seed counting rate matches ℓ_S to 4 digits.

## Exact remaining gap

- **Criterion D (n-independent Λ) needs control uniform over growing heights k < k_n ≍ log n.** Equivalently (Proposition M), it needs moment bounds of order ≈ ln n, or a sup transfer, for words of length ≍ log n. The available inputs are fixed-height:
  - Theorem 1 bounds each fixed k, with a constant that is ineffective and exceeds the budget by about 10⁷⁵⁰;
  - the rates available uniformly in k are 1.066 (P₅₀₀₀, sup side, frozen) or the trivial 2ρ, against an L² lower rate of only 0.0276 (Lemma 3(b), compact, fixed height);
  - the observed rates are 0.24 on both sides.
- **The blocking term.** In the n → ∞ regime the n-independent criterion is a statement about the compact ratio growth C_k ≤ Λγ^k with γ < 1/q_ρ ≤ 1.9436 (Proposition 6, given (ST↓)). The per-simple heuristic gives growth 2^k, just above the allowance. So deciding Criterion D requires either:
  - a proof that the compact sup of the increments decays at a rate below 1.94 × 0.2401 ≈ 0.466 per step; or
  - a version of Criterion D with a better counting rate, e.g. the angular 0.4627 (needing a physical, growing-height analogue of the E(|d|² | J) decoupling).
- **Not settled here:** whether √(ln n) growth persists along k ≍ log n at astronomically large n. A refutation in the mission's sense (provable √(ln n) growth) would need Gaussian moment lower bounds of order ln n for words of length ≍ log n. No tool for that exists in the programme, and Proposition H shows that it would be the generic (non-arithmetic) behaviour.
- **Unchanged:** D2–D4, (b4), (b-Jk), (b-T), the uniform complex stationary domain and derivative transfer; the proved frozen rate stays 1.066. Nothing here bears on the original target, the ordinary Lovász theta limit of the prime Paley localizations.

## Verdict

**Inconclusive.**
- **Measured growth law.** In the accessible range n ≤ 5·10⁷ (p ≤ 1.0·10⁸), the sup/RMS ratio of every B-generated Duhamel word, of R_{602+k} and of the B-parts follows the Gaussian extreme-value law for n/2 values: ≈ √(2 ln(n/2)), slope 1.02 ± 0.06 on √(2 ln n). This holds on Q's corners and with the nine-centre start. A bounded law is rejected in this range.
- **Proof obtained.**
  - At every fixed height the ratio is provably bounded in n (Theorem 1; ineffective, about 10⁹⁵⁶). So the √(ln n) growth is pre-asymptotic, and no fixed-word √(ln n) obstruction exists.
  - Without arithmetic structure (Haar eigenbasis) the ratio provably grows like √(2 ln n) (Proposition H).
  - The dichotomy is exactly moment growth up to order ln n (Proposition M).
- **What blocks a decision.** The uniformity over heights k ≍ log n. In the n → ∞ regime this is the compact sup/L² growth rate of the increments: heuristically 2 per step, against Criterion D's allowance of at most 1.944. That suggests reformulating the criterion with an averaged counting rate rather than settling √(ln n).

## Ranked next tests

1. **Compact sup growth of the seed iterates (decisive for Criterion D in the n → ∞ regime).** For the per-simple model of L_S^kd, either prove that the compact sup decays at a rate < 0.466 per step (then Criterion D's γ fits), or exhibit sign-aligned group elements giving sup ≥ c·0.50^k (then Criterion D in its stated form fails, by Proposition 6, given (ST↓)). Start with the Round 182 slot-count transfer matrix and the independence of transported factors.
2. **Criterion D with an averaged counting rate.** Re-prove Round 180's induction with ‖R_{602+i}‖_{2,n} ≤ q′^iε′ where q′ is an angular (decoupled) rate. The compact value is q_ang(2.338) = 0.4627, so γ < 2.161. This needs a physical growing-height version of E(|d|² | J) ≈ ‖d‖² (an L² decoupling, much weaker than delocalization). Outcome: if it holds, the criterion's room exceeds the heuristic θ = 2.
3. **(Lower value) Lower sup transfer (ST↓) at fixed height**, from Frobenius equidistribution and continuity of finite-price compact fields. This turns Proposition 6 into an unconditional necessity statement.
4. **Do not renew:** floating searches for bounded sup/RMS at larger p. Through 5·10⁷ the law is Gaussian, and Theorem 1 already says the bounded regime is ineffective and astronomically far away.

## Replay commands and outputs

Run from the repository root on 2026-11-21, with python-flint 0.9.0, numpy 2.3.5 and scipy 1.16.3.

```bash
.venv/bin/python -B research/paley-187-cold-constants.py          # under 1 s; exact/outward (a)
```
Key output lines:
```
  l_S^2 in [0.0576291, 0.0576291];  l_S in [0.2400606, 0.2400606]
  c = 2.338 (inherited cap 1.963 + 3/8 (Rounds 177/179)): l(c) in [0.027565, 0.027582]
  c = 0.000 (c = 0 (no displacement; compare l_S)): l(c) in [0.240031, 0.240090]
  Round 179 real-floor indicator test 0.349/8/sqrt5 = 0.019510 (Round 179 rounds it to 0.019)
  Lemma 3 l(2.338) lower end: log10(0.00042 * rate^(602+9)) <= -956.317
  m =  8: (2m-1)!! = 2027025, ((2m-1)!!)^(1/(2m)) in [2.47844, 2.47844], sqrt(2m/e) = 2.42612
  sqrt(2 ln n) >= 6.5e205 iff log10 n >= Lambda^2/(2 ln 10) = 9.17447e+410 (log10 of that in [410.9626, 410.9626])
  sqrt(2 ln n) >= 9.4e206 iff log10 n >= Lambda^2/(2 ln 10) = 1.91871e+413 (log10 of that in [413.2830, 413.2830])
  leading-field limit 2sqrt2 s/(4 sqrt a) (Round 182, conjectural): rate 0.50206; theta = rate / l_S in [2.0914, 2.0914]
  counting rate q = 0.5145: 1/q in [1.9436, 1.9436]
  counting rate q = 0.545: 1/q in [1.8349, 1.8349]
  Phi_a'(v) < 1/2.0 iff |v| < [4.5996, 4.5996] (real t = a)
  b = 1.940 (Round 80 cap B = 1.94): q_ang in [0.428191, 0.428251]; 1/q_ang >= 2.3351
  b = 2.338 (cap 1.963 + 3/8): q_ang in [0.462690, 0.462748]; 1/q_ang >= 2.1610
```

```bash
OUT=/tmp/paley-187-main.jsonl      # any scratch path; the rows file is not part of the repository
.venv/bin/python -B research/paley-187-cold-bword-rows.py $OUT 2017 2029 2081 2113 4001 4057 3889 4201 \
  9901 10141 9857 9829 20021 20161 19801 19501 39937 39313 40961 41161 99793 100673 100801 101089 \
  200201 197569 202753 196561 397489 403369 396001 395137 995329 1006237 1006721 1008001 \
  2002001 1995841 2007721 1990657 3993601 3991681 10001881 9966529 19992701 19987969 \
  39975937 40080041 100018801
SENS=/tmp/paley-187-sens.jsonl
.venv/bin/python -B research/paley-187-cold-bword-rows.py $SENS 200201 2002001 --start seed
.venv/bin/python -B research/paley-187-cold-bword-rows.py $SENS 200201 2002001 --t pp
.venv/bin/python -B research/paley-187-cold-bword-rows.py $SENS 200201 2002001 --t mm
.venv/bin/python -B research/paley-187-cold-bword-rows.py $SENS 200201 2002001 --t pm
.venv/bin/python -B research/paley-187-cold-bword-fit.py $OUT $SENS
```
- Runtime of the main run is about 50 min, single-threaded FFTs. The largest prime takes 927 s.
- Peak memory was measured at 1.5 GB for n = 10⁷ and 3.0 GB for n = 2·10⁷. It is estimated at about 7 GB for n = 5·10⁷.
- Last lines of the main run:
```
[float] p=39975937 n=19987968 t=a start=nine: ratio(R602)=5.304 ratio(B r)=5.144 gauss_med=5.516 rate=0.2406 log10 sigma_end=-375.2 (374s)
[float] p=40080041 n=20040020 t=a start=nine: ratio(R602)=5.279 ratio(B r)=5.368 gauss_med=5.516 rate=0.2406 log10 sigma_end=-375.2 (449s)
[float] p=100018801 n=50009400 t=a start=nine: ratio(R602)=5.548 ratio(B r)=5.697 gauss_med=5.675 rate=0.2407 log10 sigma_end=-375.2 (927s)
```
(`gauss_med` in these lines is the median of the maximum of n − 1 iid values, a quick control. The fits use E_G(n/2).) The fit output reproduces the tables of §7.
