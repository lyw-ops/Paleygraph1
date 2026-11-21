# Round 186 native Claude draft: cold prime hybrid price

- call_id: `cold-prime-hybrid-price`
- Mission: `coordination/missions/round-186/cold-prime-hybrid-price.md`, exported from coordinator record `coordination/round-185.json` (SHA-256 f5b2ff1f…).
- Author: a native Claude research session (Claude Opus 5.5), started by the Round 186 coordinator session. This is an agent draft. It is not an audit, not an acceptance and not a human review.
- Input hashes verified (SHA-256). All eight match the mission export:
  - round-184-acceptance c3066021…, round-185-acceptance 157de3b6…, native-claude-audit-185 03d3a66b…
  - native-claude-cold-prime-picard-leaf-inequivalence-185 45515537…, native-claude-cold-prime-h1-product-rule-184 a45402f0…
  - native-claude-cold-prime-seed-multiplier-power-rate-183 90c2eaee…, native-claude-cold-prime-signed-nonseed-price-182 c8023a9b…, cold-first-prefix-step-174 8d28cc54…
- Also read:
  - `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-185.md`;
  - §3 and §5 of `native-claude-audit-185.md`;
  - `cold-actual-quadratic-128.md` (counting rate 0.5145), `cold-seed-centered-larger-tube-177.md` (rate 0.545, ‖S‖_∞ < s_*, ‖V₆₀₂ − S‖_∞ < 1.963), `cold-logarithmic-finite-tube-173.md` (sup|Φ′(V₆₀₂)| < 0.518, the tail), `cold-growing-prefix-delocalization-180.md` and §R3 of `native-claude-audit-180.md` (Criterion D, the size of R₆₀₂);
  - `shifted-resolvent-96.md` line 7 (K² = I − P₁), `astra-adjoint-82.md` line 11 (sup domination of the price);
  - the Round 184 diagnostic `paley-184-cold-h-rest-diagnostic.py`, for its conventions only;
  - the shared notes of the Round 182–185 cold sessions.
- Scripts written by this session (both new; neither imports or copies an earlier script):
  - `research/paley-186-cold-hybrid-constants.py`: exact rationals, integers and outward python-flint balls. It covers the exact identities for K, the curvature floor m″(γ), the Theorem N constant c_N(γ, n) and its thresholds, the counting-horizon arithmetic, the Taylor constant of the hybrid seminorm, the counting rates, the seed resolvent of the hybrid, and the per-simple floor remark. Runtime under 1 s.
  - `research/paley-186-cold-hybrid-witness.py`: physical rows in double precision, p up to 4·10⁶. Floating, evidence only. Runtime about 1–2 min.

## Result summary

**Verdict: refuted, for the hybrid as posed.** The decision is the mission's "refuted" branch: the cold dimension-price programme reduces to Criterion D or sup transfer, unless multiplication by h is priced through structured (A-type) information about h, which is the route Round 185 retired. The refutation rests on proved statements, not on model evidence. It is a refutation of a proof method. It does not refute confinement, and it says nothing about the original target.

1. **Which price is submultiplicative against which (Proposition 1; proved).**
   - The per-simple dimension price A_𝒳 is an algebra price: A(fg) ≤ A(f)A(g) (Round 181). K acts on it per simple (Round 184 Proposition A), and the seed resolvent is finite: g_S ≤ 2.467879.
   - The counting norm is a module over the sup norm: ‖fg‖₂ ≤ ‖g‖_∞‖f‖₂. K is a contraction on it (its eigenvalues are 0 and ±1). But it dominates the sup only with a factor √n.
   - The sup norm is an algebra norm, but K and the seed operator L_S are unbounded on it: ‖K‖_{∞→∞} ≥ 2(n − 1)/(s√n) and ‖L_S‖_{∞→∞} ≥ 0.1182√n·(1 − o(1)) (Lemmas 2–3).
   - So there is no mixed inequality of the form "price of K(g·f) ≤ C·‖g‖_∞·price of f".
2. **No sup or counting price for the multiplier (Theorem N; proved).** Let P be any seminorm with P(f) ≥ |f(x₀)| at good coordinates x₀ and P(S) ≤ s_p. This covers A, A_𝒳 and the hybrid seminorm below, and also π_α and P₅₀₀₀ up to the constant in P(S) = O(1). Then
   sup over real g with ‖g‖_∞ ≤ γ of P(K((Φ_a′(S+g) − Φ_a′(S))S))/P(S) ≥ c_N(γ, n), where c_N(γ, n) ~ (8γ m″(γ)/s³)√n.
   - At γ = 0.61 (the floating sup|h|) the slope is ≥ 0.020951. So c_N exceeds the seed-only Duhamel budget 0.24310 for every n ≥ 151, and exceeds 1 for every n ≥ 2294.
   - The same holds for the counting norm (γ = 0.1749, n ≥ 1478) and for every rearrangement-invariant norm of g.
   - So the cost ρ₀‖h‖_∞/√N + H(‖h‖_∞) proposed in Round 184 test 2 (0.19073 at ‖h‖_∞ = 0.61) is not a valid operator bound in any such price, uniformly in n.
3. **Round 182 Proposition 2 applies to the natural hybrid seminorm (Propositions 3–4; proved, modulo inherited D1–D4).** Take H_λ = A_𝒳 infimal-convolved with λ‖·‖_{ℓ²}, λ ≥ 1.
   - It is sup-dominating, (H1) is trivial, H_λ(R₆₀₂) < 0.01272, and the Taylor part of (H2) holds with constant max(c_A, κ₂/2) = c_A, since κ₂(u)/2 ≤ 0.083338 < 0.464976 ≤ c_A(M₀ + u) for every u ≤ 3/8.
   - Hence κ*_H = κ*_A. The seed resolvent is unchanged, g_H = g_S, because the counting rate of L_S (≤ 0.334571) is below every per-step seed A-ratio (≥ 0.339459).
   - **The hybrid analogue of the allowance is the same number:** ‖B‖_{H_λ} < 0.24310 suffices (Round 184 Proposition C form).
   - But the only n-uniform bound for ‖B‖_{H_λ} is A-type. Its counting branch costs λ·β_∞·√n (Proposition 4), and Theorem N shows that no sup or counting information about h removes that √n.
4. **The counting rates 0.5145 and 0.545 cannot pay back the √n inside the Round 173 horizon (Proposition 5, Corollary 6; proved).**
   - A B-factor followed by b contracting steps costs √n·q^b in sup. This is at most 1 only if b ≥ θ(q)log₂n, with θ(q) = 1/(2log₂(1/q)).
   - The horizon is k_n = ⌈(4/7)log₂n⌉. The fraction of it in which this is possible is [0.08736, 0.08737] at q = 0.5145, [0.07795, 0.07796] at the frozen q = 0.518, and [0.00076, 0.00077] at q = 0.545.
   - Every Duhamel word of length below θ(q)log₂n → ∞ gets no help.
   - A pure counting hybrid is exactly Criterion D with Λ_n ≍ √n. Round 180 shows that any Λ_n → ∞ defeats Criterion D, because liminf ‖R₆₀₂‖_{2,n} > 0. With the ineffective limsup 9.07·10⁻²⁰⁹ it would confine only while n < 10^414.197.
5. **What remains (gap).**
   - A hybrid can meet the allowance only through a bound on the non-seed multiplier that uses the structure of h: either an A-type price of B (the retired per-simple route), or a delocalization/sup-transfer input (Criterion D, sup transfer).
   - Remark on the retired route: with the exact per-simple floor 1.91541 in place of the word rule, the seed-only ceiling for A(h) rises from 0.7499 to about 0.8192 (with the h-higher majorant H). That is still below the certified model value 0.912537. It rises to 1.011122 only if the h-higher terms were free. So the Round 185 retirement is robust to the ratio bookkeeping, but it relies on the h-higher terms costing at least 0.023703 in that form.
6. **Evidence (c, floating, p up to 4·10⁶).**
   - The actual ‖B_h S‖_∞ stays at 0.16–0.20 and ‖B_h h₁‖_∞ at about 0.02.
   - Multipliers with the same sup as h give values growing like 0.11√n (77.5 at n = 500016, 154.8 at n = 2000018).
   - Multipliers with the same modulus at every coordinate as h give values growing like 0.026√n.
   - So the true operator is benign. The obstruction is in certifying it from size information.

## Setup and hypotheses (inherited, as accepted in Rounds 80, 96, 173–185)

- p ≡ 1 (mod 4) prime, n = (p − 1)/2, Q the closed square of half-width 2⁻¹⁷ about a = 2031/128, and N = 4(a − 2⁻¹⁷). Physical mark t₀ = n; both lifts.
- **K** is the real symmetric circulant on ℤ/n with eigenvalues λ_j = χ(1 − g^{2j}) (Round 96: K² = I − P₁; Round 180: K_{ik} = S_{k−i}/(2√n)). Write κ = Ke₀, so K(x, y) = κ(x − y) = κ(y − x).
- **Seed:** S = 2√n Ke₀ = s_p Re J, with s_p ≤ s := 2.828428539 for p ≥ 10⁶.
  - (I1) **‖S‖_∞ ≤ s_p**: Rounds 88/177 ("‖S‖_∞ < s_*" for all large eligible p), inherited. The witness checks it.
- **Frozen-base identity at 602** (Round 182): U_{j+1} = R + LU_j + T(U_j), where:
  - L = KD₆₀₂ = L_S + B, with L_S = K(Φ_t′(S)·) and B = B_h = K((Φ_t′(S+h) − Φ_t′(S))·);
  - h = V₆₀₂ − S;
  - T is the Taylor remainder.
- **Accepted inputs used:**
  - Round 182 Proposition 2 (finite-horizon Duhamel form) and Remark 2.3 (any use needs Γ_{k_n} bounded uniformly in n);
  - Round 183 Lemma 4(ii), c_A = c(M)/2;
  - Round 184 Propositions A–C, D1 (A_𝒳(R₆₀₂) < 0.01272), g_S ≤ 2.467879, κ*_A ∈ [0.83790250, 0.83793100] and the seed-only budget β′ < 0.24310 (A(h) < 0.7499);
  - Round 185 Theorem 3 (model A_𝒳(h_{≤3}) ≥ 0.912537);
  - Round 173: sup_i|Φ′(V₆₀₂,i)| < 0.518, so ‖L‖_{2→2} < 0.518;
  - Round 177: counting rate 0.545 on the 3/8 polydisk, ‖V₆₀₂ − S‖_∞ < 1.963 and the seed-centred geometry Re(4t + z²) ≥ |z|² + N − 2B² for |z − S_i| ≤ B;
  - Round 180: 0 < liminf ‖R₆₀₂‖_{2,n} ≤ limsup < 9.07·10⁻²⁰⁹ (ineffective), and Criterion D.
- **Norms:**
  - ‖f‖_{∞,good} is the supremum over good coordinates; the number b₀ of other coordinates is bounded (at most two cyclic coordinates plus the mark; b₀ ≤ 3 is used);
  - ‖f‖₂ is the unnormalized counting norm and ‖f‖_{2,n} = ‖f‖₂/√n;
  - A_𝒳 is the Round 184 dimension price on the unshifted class, +∞ off 𝒳.
- **Price hypotheses (D2–D4, (b4), (b-Jk), (b-T))** are inherited exactly as in Round 184 and used only where an A_𝒳 statement is quoted.

## 1. Which price is submultiplicative against which

**Lemma 1 (exact identities for K; proved).**
- (i) Σ_j λ_j = −1.
- (ii) λ_j = 0 iff j = 0.
- (iii) λ_{n−j} = λ_j.

Consequently:
- ‖K‖_{2→2} = 1;
- ‖κ‖₂² = (n − 1)/n;
- Σ_x S_x² = 4(n − 1);
- S₀ = −2/√n.

*Proof.*
- (i) As j runs over ℤ/n, y = g^{2j} runs once over the nonzero squares. So Σ_jλ_j = Σ_{y∈□*}χ(1 − y) = ½Σ_{x≠0}χ(1 − x²) = ½(Σ_xχ(1 − x²) − 1).
  - For a quadratic polynomial with nonzero discriminant, Σ_xχ(ax² + bx + c) = −χ(a). Here a = −1, and χ(−1) = 1 since p ≡ 1 (mod 4).
  - So Σ_jλ_j = ½(−1 − 1) = −1.
- (ii) λ_j = 0 iff 1 − y = 0, i.e. j = 0.
- (iii) 1 − y⁻¹ = −y⁻¹(1 − y) and χ(−y⁻¹) = 1.
- The consequences follow. K is diagonal in the Fourier basis with eigenvalues in {0, ±1}. By Parseval, ‖κ‖₂² = n⁻¹Σλ_j². And κ(0) = n⁻¹Σλ_j = −1/n. ∎

The script checks (i)–(iii) with integers for all p ≡ 1 (mod 4), 5 ≤ p < 2000. The witness reproduces Σλ = −1, √n S₀ = −2 and ΣS²/(4(n − 1)) = 1 to 12 digits at p ≤ 4·10⁶.

**Lemma 2 (K on the sup norm; proved under (I1)).** ‖K‖_{∞→∞} = Σ_x|κ(x)| ≥ Σκ²/max|κ| ≥ 2(n − 1)/(s√n).
- For n = 10⁶ this is ≥ 707.105.

**Lemma 3 (the seed operator on the sup norm; proved under (I1), at t = a).** ‖L_S‖_{∞→good} ≥ c_LS(n), where
  c_LS(n) = 8(n−1)(n−1−1/n)/(s²n^{3/2}√(4a+s²)) − 2b₀√(n−1)/n ~ 0.118288·√n.
- c_LS > 1 for n ≥ 160.

*Proof.*
- Fix a good x₀. Put f_x = sgn(κ(x₀ − x)Φ_a′(S_x)) for x ≠ 0, and f₀ = 0.
- Then (L_S f)(x₀) = Σ_{x≠0}|κ(x₀ − x)||Φ_a′(S_x)| ≥ (4a + s²)^{−1/2}W(x₀), where W(x₀) = Σ_{x≠0}|κ(x₀ − x)||S_x|.
- Average over x₀ as in the proof of Theorem N. ∎

**Proposition 1 (pairings).** For the three operations of the frozen map, multiplication M_g by a coordinate function g and transport K, the following hold (all proved, or inherited where cited):

| price of the output | against | inequality | n-uniform? |
|---|---|---|---|
| A (algebra) | A | A(fg) ≤ A(f)A(g) (Round 181) | yes |
| A after K, per simple | A-type data of the multiplier | sup_F A(K(GF))/A(F) = Σ_j\|c_j\|(d_j + μ_j/2) (Round 184 Prop. A), ≥ 1.91541·Σ\|c\|d/(2\|√t\|) for multipliers Φ″(S)G (Cor. A2) | yes, but costs the A-price of the multiplier, never its sup |
| counting ‖·‖₂ | sup of the multiplier | ‖fg‖₂ ≤ ‖g‖_∞‖f‖₂ | yes |
| counting after K | counting | ‖K‖_{2→2} = 1 (Lemma 1) | yes |
| sup | counting | ‖f‖_∞ ≤ ‖f‖₂ = √n‖f‖_{2,n} | **loses √n** |
| sup after K | sup | ‖K‖_{∞→∞} ≥ 2(n−1)/(s√n) (Lemma 2); ‖L_S‖_{∞→∞} ≥ 0.1183√n (Lemma 3) | **no** |
| sup-dominating P after K | sup of the multiplier | P(K(Φ″-type(g)·f)) ≤ F(‖g‖_∞)P(f) | **impossible** (Theorem N) |

**Reading.**
- A price usable in Round 182 Propositions 1–2 must dominate the sup and must let the seed operator iterate with a bounded resolvent.
- Among the three, only A has both properties, and in A a multiplier costs an A-type quantity of itself.
- The counting norm lets L, L_S and B iterate (rates 0.518, 0.334571 and 0.299209) but does not dominate the sup.
- The sup norm dominates itself but lets neither K nor L_S iterate.
- This is the precise sense in which "per-simple price for the seed, sup price for h" is not submultiplicative: the composite L_S^b B L_S^a would need B to map A into a space on which L_S is bounded and which dominates the sup, and no such space receives sup-priced products.

## 2. Theorem N: no sup or counting price for the non-seed multiplier

For real g with g₀ = 0 put B_g f = K((Φ_t′(S + g) − Φ_t′(S))f). B_h is the actual non-seed multiplier (Round 182 §4). It contains the h-linear and all h-higher Taylor terms.

**Theorem N (proved; inputs Lemma 1, (I1); one point t = a ∈ Q, the real principal sheet).** Let P be any seminorm on a subspace of ℂⁿ, +∞ outside it, such that:
- (S) |f(x₀)| ≤ P(f) for every good coordinate x₀;
- (P_S) P(S) ≤ s_p.

Then for every γ > 0 and every n with c_N(γ, n) > 0:

  sup_{g∈ℝⁿ, g₀=0, ‖g‖_∞≤γ} P(B_g S) ≥ c_N(γ, n)·P(S),

  c_N(γ, n) = γ m″(γ)·[8(n−1)(n−1−1/n)/(s²n^{3/2}) − 2b₀√(n−1)/n]/s,  m″(γ) = 4a/(4a + (s+γ)²)^{3/2}.

*Proof.*
1. **Sign.** At real t = a, Φ_a′(y) = y/√(4a + y²) is strictly increasing on ℝ, with Φ_a″(y) = 4a/(4a + y²)^{3/2} even and decreasing in |y|. For |S_x| ≤ s and |g_x| ≤ γ, the mean value theorem gives Φ_a′(S_x + g_x) − Φ_a′(S_x) = g_xΦ_a″(ξ_x), with |ξ_x| ≤ s + γ. Its sign is sgn g_x and its modulus is ≥ |g_x|m″(γ).
   - If another sheet changes Φ by a sign on some coordinates, the same holds with that sign absorbed into the choice below.
2. **Alignment.** Fix a good x₀. Put g_x = γ·sgn(κ(x₀ − x)S_x) for x ≠ 0 (sgn 0 := 1) and g₀ = 0. Then every term of
   (B_g S)(x₀) = Σ_{x≠0}κ(x₀ − x)S_x[Φ_a′(S_x + g_x) − Φ_a′(S_x)]
   is ≥ 0, and (B_gS)(x₀) ≥ γm″(γ)W(x₀), with W(x₀) = Σ_{x≠0}|κ(x₀ − x)||S_x|.
3. **Averaging.**
   - Σ_{x₀}W(x₀) = (Σ_y|κ(y)|)(Σ_{x≠0}|S_x|).
   - By Lemma 2, Σ|κ| ≥ 2(n−1)/(s√n).
   - By Lemma 1 and (I1), Σ_{x≠0}|S_x| ≥ (Σ_xS_x² − S₀²)/s = (4(n−1) − 4/n)/s.
   - For every x₀, W(x₀) ≤ ‖κ‖₂‖S‖₂ ≤ 2√(n−1). So the at most b₀ non-good x₀ remove at most 2b₀√(n−1).
   - Hence max_{x₀ good}W(x₀) ≥ n⁻¹[8(n−1)(n−1−1/n)/(s²√n) − 2b₀√(n−1)].
4. **Conclusion.** By (S), P(B_gS) ≥ (B_gS)(x₀). By (P_S), P(S) ≤ s_p ≤ s. ∎

**Corollary N1 (no size-only multiplier bound).**
- There is no function F, independent of p, such that P(B_g f) ≤ F(‖g‖_∞)P(f) holds for all large eligible p, all real g with g₀ = 0, and f = S. Indeed F(γ) ≥ c_N(γ, n) → ∞.
- The same holds with F(‖g‖_{2,n}), because the constant-modulus g has ‖g‖_{2,n} ≤ γ.
- It holds also with F(N(g)) for any rearrangement-invariant norm N.
- Every price of the cold programme satisfies (S) and (P_S): A, A_𝒳 (A(S) = s_p·A(Re J) = s_p), π_α up to the factor 1 + α, and H_λ of §3. For P₅₀₀₀, (S) is the inherited sup domination and P₅₀₀₀(S) = O(1).

**Corollary N2 (numbers; `…-constants.py` §§1–2, outward).**

| γ | meaning | m″(γ) ≥ | slope 8γm″/s³ ≥ | c_N > 0.24310 for n ≥ | c_N > 1 for n ≥ |
|---|---|---|---|---|---|
| 0.1749 | floating RMS(h) (counting version) | 0.102838 | 0.006359 | 1478 | 24745 |
| 3/8 | Round 177 polydisk radius | 0.100250 | 0.013291 | 351 | 5677 |
| 0.61 | floating sup\|h\| | 0.097149 | 0.020951 | 151 | 2294 |
| 1.963 | Round 177 certified sup bound | 0.078993 | 0.054823 | 34 | 349 |

- c_N is increasing in n for n ≥ 3, so the bisection thresholds are valid. The reason: (n−1)/√n and (n−1−1/n)/n increase, and √(n−1)/n decreases for n > 2. The script also checks monotonicity on the grid 10 ≤ n < 400.
- At the physical sizes, c_N(0.61, n) ≥ 1.4797, 4.6853, 14.8152, 29.6305 for n = 5004, 50024, 500016, 2000018.
- **Consequence for Round 184 test 2.** That test proposed pricing B_h at ρ₀‖h‖_∞/√N + H(‖h‖_∞). This is in [0.190729, 0.190730] at 0.61, and in [0.242709, 0.242710] at 0.7499. As a bound valid for every multiplier of that size it is false for n ≥ 151, by a factor that grows like √n. It could hold for the actual h only through information about h other than its size.

**Remark N3 (sharpness).** ‖B_gf‖_∞ ≤ ‖B_gf‖₂ ≤ ‖Φ′(S+g) − Φ′(S)‖_∞‖f‖₂ ≤ κ₂γ√n‖f‖_∞. So √n is the exact order of the loss.

**Remark N4 (test vector R₆₀₂ instead of S; conditional).** The hypothesis (P_S) can be replaced by Proposition 2's own source hypothesis P(R₆₀₂) ≤ p₀. The same proof, with S_x replaced by R_x in step 2, gives
  sup_g P(B_gR) ≥ γm″·(Σ|κ|)(Σ_{good}|R_x|)/n − O(√n p₀) ≳ (2γm″/s)·√n·‖R‖²_{2,n,good}/p₀.
This needs a positive liminf of the good-coordinate part of ‖R₆₀₂‖_{2,n}. Round 180 states the liminf for the full normalized norm, so this version is conditional on that reading.

**Remark N5 (what Theorem N does not say).**
- It is not a lower bound on the actual operator: the actual ‖B_hS‖_∞ is about 0.2 (§6).
- It says that K's lack of ℓ^∞ control must be paid for by information about h that correlates with the rows of K. The dimension budget behind P₅₀₀₀'s 1.066 (Round 162) and the per-simple A-price are such information. Sup and RMS are not.

## 3. The hybrid seminorm and Round 182 Proposition 2

**Definition.** For λ ≥ 1 put H_λ(f) = inf{A_𝒳(a) + λ‖b‖₂ : a ∈ 𝒳, a + b = f}. This is the infimal convolution of the dimension price, used for the seed iteration, and the counting norm, used for anything that leaves 𝒳 or is cheaper in counting.

**Proposition 3 (Round 182 Proposition 2 applies to H_λ; proved, with the A_𝒳 statements inherited as D1–D4).**
- (i) H_λ is a seminorm on ℂⁿ, with H_λ ≤ A_𝒳 on 𝒳 and H_λ ≤ λ‖·‖₂.
- (ii) **Sup domination.** For good x₀, |f(x₀)| ≤ |a(x₀)| + |b(x₀)| ≤ A_𝒳(a) + ‖b‖₂ ≤ A_𝒳(a) + λ‖b‖₂. Here |a(x₀)| ≤ A_𝒳(a) is Round 96/181, and λ ≥ 1.
- (iii) **(H1).** H_λ is finite on ℂⁿ, so class closure is automatic. The A-component's own closure, used inside the Taylor estimate, is Round 184 D3.
- (iv) **Source.** H_λ(R₆₀₂) ≤ A_𝒳(R₆₀₂) < 0.01272 (Round 184 D1).
- (v) **Taylor part of (H2).** H_λ(T(U)) ≤ (c_A(M₀ + H_λ(U)) + ε(p))H_λ(U)² whenever H_λ(U) ≤ u ≤ 3/8. Here ε(p) → 0 uniformly over inputs (from D2, A-part only).

*Proof of (v).*
- Take a near-optimal split U = a + b, and put x = A_𝒳(a) and y = λ‖b‖₂. At good coordinates ‖a‖_∞ ≤ x and ‖b‖_∞ ≤ ‖b‖₂ ≤ y, so V₆₀₂ + a + σb stays in the radius-u polydisk for σ ∈ [0, 1].
- Write T(U) = T(a) + Δ, with Δ = K(b∫₀¹[Φ′(V + a + σb) − Φ′(V)]dσ).
- **A-part.** A_𝒳(T(a)) ≤ (c_A + ε)x² (Round 183 Lemma 4(ii) with D2).
- **Counting part.** Pointwise |Φ′(V + a + σb) − Φ′(V)| ≤ κ₂(|a| + σ|b|), where κ₂ = κ₂(u) bounds |Φ_t″| on the polydisk. At the mark Φ″_{t₀} = O(n^{−1/2}). With ‖K‖_{2→2} = 1 this gives λ‖Δ‖₂ ≤ κ₂xy + (κ₂/2λ)y².
- **Sum.** c_Ax² + κ₂xy + (κ₂/2λ)y² ≤ max(c_A, κ₂/2)(x + y)².
- **Numbers.** Round 177's geometry gives κ₂(u) ≤ 4|t|/(N − 2(1.963 + u)²)^{3/2}. The script certifies κ₂/2 ≤ 0.078779 < 0.515106 ≤ c_A(M₀ + u) at the certifying radius u = 747/5000. For every u ≤ 3/8 it certifies κ₂(u)/2 ≤ κ₂(3/8)/2 ≤ 0.083338 < 0.464976 ≤ c_A(M₀) ≤ c_A(M₀ + u). So the constant is c_A. ∎

**Consequences.**
- **κ*_H = κ*_A.** Proposition 2 for H_λ holds on horizon k if σ_k + Γ_k(H_λ)c_Au² < u. In the Round 184 Proposition C form this reads Γ(H_λ) < 1/(1 − κ*_A), with 1/(1 − κ*_A) ≥ 6.16912.
- **Seed part, g_H = g_S.**
  - For x = a + b, H_λ(L_S^m x) ≤ G_mA_𝒳(a) + q_S^mλ‖b‖₂, where q_S = sup|Φ_t′(S)| ≤ s/√(N + s²) ≤ 0.334571.
  - Every one-step path-summed seed A-ratio is ≥ 2ϖ_lo|ĝ₁|_lo ≥ 0.339459. This uses Round 182 Lemma 3.1, r′₊ + r′₋ = 4r − NZ ≥ 2r, and children of valid simples are valid.
  - So G_m ≥ 0.339459^m > q_S^m, and ‖L_S^m‖_{H_λ} ≤ G_m. Hence Σ_m‖L_S^m‖_{H_λ} ≤ g_S ≤ 2.467879.
- **The hybrid analogue of the allowance is therefore identical to Round 184's seed-only allowance:** a bound ‖B‖_{H_λ} ≤ β′ < 0.24310, uniform in n, t ∈ Q and both lifts, closes the cold criterion through Proposition C and Proposition 2.

**Proposition 4 (the linear block of H_λ; proved as an upper bound).**
- For x = a + b,
  L^m x = L_S^m a + [Σ_{i<m}L^{m−1−i}BL_S^i a + L^m b].
  The first summand lies in 𝒳. The bracket can be priced in counting norm or, wherever available, in A_𝒳.
- With q₀ = ‖L‖_{2→2} < 0.518 (Round 173) and β_∞ = sup|Φ′(V₆₀₂) − Φ′(S)| ≤ κ₂(0)·1.963 ≤ 0.299209, the counting option gives
  ‖L^m‖_{H_λ} ≤ max{G_m + λβ_∞√n(1 + o(1))Σ_{i<m}q₀^{m−1−i}q_S^i, q₀^m}.
  The factor √n enters through ‖L_S^ia‖₂ ≤ q_S^i√n‖a‖_∞. The o(1) is the inherited bad-coordinate correction to sup domination.
- The A option replaces λβ_∞√n by an A-type cost of B. This is the per-simple route of Rounds 182–185.
- So H_λ is never worse than A_𝒳, but its only new option carries √n. By Theorem N (H_λ satisfies (S) and (P_S)), no estimate of ‖B‖_{H_λ} in terms of ‖h‖_∞ or ‖h‖_{2,n} can remove it.

**Remark (heuristic, not used).** In the compact model the dual functionals that give Round 185's lower bounds are Σ_{M∈𝒮}d_M ε_M coef_M. For a fixed finite set 𝒮 of simples they have counting-dual norm about Σ_{M∈𝒮}d_M/√n, by quasi-orthogonality of traces. So for large n they are admissible for H_λ, and H_λ coincides with A_𝒳 on fixed finite combinations of simples. I did not prove this. It would mean the counting component cannot lower model prices either.

## 4. The counting route: rates 0.5145, 0.518, 0.545 against the horizon

**Proposition 5 (proved).** Let q ≥ ‖L‖_{2→2} on the region considered. Let y be an input with ‖y‖_∞ ≤ P(y), and let w = L^bBy. Then
  ‖w‖_{∞,good} ≤ ‖w‖₂ ≤ q^bβ_∞‖y‖₂ ≤ √n·q^b·β_∞·‖y‖_∞.
- This improves on the trivial ℓ^∞ bound only if √n·q^b ≤ 1, i.e. b ≥ θ(q)log₂n with θ(q) = 1/(2log₂(1/q)).
- Inside the Round 173 horizon k_n = ⌈(4/7)log₂n⌉, the positions with b ≥ θ(q)log₂n make up the fraction 1 − θ(q)/(4/7):

| q | source | θ(q) | usable fraction of the horizon |
|---|---|---|---|
| 0.5145 | Round 128 (height 601) | [0.521508, 0.521509] | [0.08736, 0.08737] |
| 0.518 | Round 173 (frozen at V₆₀₂) | [0.526883, 0.526884] | [0.07795, 0.07796] |
| 0.535 | Round 174 (radius 0.05) | [0.554084, 0.554085] | [0.03035, 0.03036] |
| 0.545 | Round 177 (radius 3/8) | [0.570990, 0.570991] | [0.00076, 0.00077] |

- The 0.545 row is the Round 173 design: 0.545⁸ < 2⁻⁷ makes √n·q^{k_n} = o(1), with a margin under 10⁻⁴ (0.545⁸ > 2⁻⁷ − 10⁻⁴, exact).
- **Consequence.** Every Duhamel word for U_j with j < θ(q)log₂n gets no help from the counting branch. Since θ(q)log₂n → ∞, the hybrid must bound Σ_{m<θ(q)log₂n}‖L^m‖ in a sup-dominating price without the counting branch. By Round 182 Remark 2.3 this needs n-uniform control of B in such a price, and Theorem N excludes size-only control.

**Corollary 6 (the counting hybrid is Criterion D with Λ_n ≍ √n; proved, with Round 180 inputs).**
- While the prefix stays in the 3/8 polydisk, ‖U_j‖_∞ ≤ ‖U_j‖₂ = √n‖U_j‖_{2,n} ≤ √n‖R₆₀₂‖_{2,n}/(1 − 0.545). This is the convexity step of Round 180.
- So pricing the non-seed part in counting norm and converting back is Criterion D with Λ_n = √n. Splitting off the seed part Y_j = Σ_{i<j}L_S^iR, with A(Y_j) ≤ g_S·p₀ ≤ 0.0314, changes only constants.
- Round 180 proves that any Λ_n → ∞ defeats Criterion D, because liminf‖R₆₀₂‖_{2,n} > 0.
- With the ineffective limsup 9.07·10⁻²⁰⁹ and η = 1/8, the argument would confine only while √n < 10^207.098, i.e. n < 10^414.197. That is not the uniform statement the mission asks for, and the threshold beyond which the limsup applies is itself ineffective.

## 5. Answer to the mission question

**Can a hybrid price meet the Round 184 Duhamel allowance uniformly on Q, on both lifts? Not with h entering through a sup or counting norm.**

1. **Which price is submultiplicative against which.**
   - The per-simple dimension price is submultiplicative against itself (an algebra, with K acting per simple and the seed resolvent g_S ≤ 2.467879). In it, multiplication by h costs an A-type quantity of h: exactly Σ|c|(d + μ/2) per simple, never its sup (Round 184 Prop. A, Cor. A2).
   - The counting norm is submultiplicative against the sup norm (a module) and K-invariant, but dominates the sup only with √n.
   - The sup norm is submultiplicative against itself, but K and L_S are unbounded on it (Lemmas 2–3).
   - No mixed inequality "A-price after K against sup of the multiplier" exists (Theorem N).
2. **Round 182 Proposition 2 applies to the hybrid price.** For H_λ = A_𝒳 infimal-convolved with λ‖·‖₂:
   - (H1) holds trivially;
   - sup domination and the source bound hold (Proposition 3);
   - the Taylor part of (H2) holds with the A-constant c_A, given the inherited D1–D4;
   - κ*_H = κ*_A and g_H = g_S.
   The remaining hypothesis, a bound on Γ_{k_n}(H_λ) uniform in n, is equivalent in the Proposition C form to ‖B‖_{H_λ} < 0.24310.
3. **That remaining hypothesis cannot be proved from ‖h‖_∞ or ‖h‖_{2,n}.** By Theorem N, size-only bounds fail by a factor ≥ c_N(γ, n) ~ 0.021√n at γ = 0.61, already above the budget for n ≥ 151. The counting branch is Criterion D with Λ_n ≍ √n (Corollary 6), and the rates 0.5145/0.545 cannot pay back √n inside the horizon (Proposition 5).
4. **Hence** a hybrid meeting the allowance needs structured information about h. Either:
   - an A-type price of B, which is the per-simple route retired in Round 185, or
   - a delocalization or sup-transfer input, which is Criterion D or sup transfer.

**Remark on the retired route** (`…-constants.py` §6; numbers certified, interpretation mine).
- In the seed-only Proposition C form, the h-linear term cannot cost less than floor·A(h)/(2|√t|) with floor 1.91541 (Round 184 Cor. A2). At the certified model value A(h_{≤3}) ≥ 0.912537 this is ≥ 0.219397, which leaves ≤ 0.023703 of the budget 0.24310 for the h-higher terms.
- Their majorant H(0.912537) is in [0.058797, 0.058798]. With the floor ratio and this majorant, the ceiling on A(h) is about 0.8192 (bisection; float print), against Round 184's 0.7499 with the word rule. So the Round 185 retirement survives the change from the word rule to the per-simple floor.
- If the h-higher terms cost nothing, the ceiling would be 1.011122 > 0.912537. So the retirement relies on a non-negligible per-simple cost of the h-higher terms. That cost is bounded above (by H), but no lower bound has been proved.
- This does not reopen the route: Round 185 recorded it as retired on model evidence, and the joint allowance A(h − h₁) < 0.3411 against 0.4346 is unaffected. It does locate the one place where a certified retirement would need an extra lower bound.

## 6. Evidence (c) (`…-hybrid-witness.py`; floating, t = a, one real lift, double precision)

| p | n | sup\|h\| | RMS(h) | ‖B_hS‖_∞ (actual) | sup/RMS of B_hS | ‖B_hh₁‖_∞ (actual) | same-sup g: value | /√n | same-modulus g: value | /√n | Theorem N c_N(sup\|h\|, n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 10009 | 5004 | 0.5699 | 0.1949 | 0.1618 | 4.11 | 0.0221 | 7.360 | 0.1040 | 2.181 | 0.0308 | 1.39 |
| 100049 | 50024 | 0.5513 | 0.1752 | 0.1638 | 4.29 | 0.0191 | 22.343 | 0.0999 | 5.837 | 0.0261 | 4.27 |
| 1000033 | 500016 | 0.6063 | 0.1756 | 0.2035 | 5.27 | 0.0197 | 77.463 | 0.1095 | 18.322 | 0.0259 | 14.73 |
| 4000037 | 2000018 | 0.6065 | 0.1764 | 0.1917 | 4.94 | 0.0202 | 154.795 | 0.1095 | 36.717 | 0.0260 | 29.47 |

- **"Same-sup g"** has |g_x| = sup|h| off the mark. **"Same-modulus g"** has |g_x| = |h_x| at every coordinate, hence the same sup, RMS and value distribution as h. In both, the signs are aligned with the best row x₀ of K, and the vector K((Φ′(S+g) − Φ′(S))S) is evaluated explicitly at x₀.
- The observed ratio to A(S) = s_p (2.60, 7.90, 27.39, 54.73) exceeds the certified lower bound c_N (1.39, 4.27, 14.73, 29.47) in every case. The proof's Cauchy–Schwarz step Σ|S| ≥ ΣS²/s loses about the factor (2/π)·s²/4 ≈ 1.8.
- With the input f = h₁ (model A(h₁) = 0.4945), same-modulus multipliers give 0.294, 0.703, 2.166, 4.339, also growing like 0.0031√n. The actual ‖B_hh₁‖_∞ stays at about 0.02.
- **Counting conversion for the actual product:** √n·RMS(B_hS)/sup|B_hS| = 17.2, 52.2, 134.1, 286.1. That is the factor lost by pricing the product in counting norm and converting back to sup.
- **Reading.**
  - The actual non-seed multiplier is benign in sup: about 0.2 on S, against the would-be sup-priced bound β·A(S) ≈ 0.19·2.83 = 0.54.
  - Size information cannot certify this, since multipliers of the same size, or even the same modulus profile, produce values of order √n.
  - The actual sup/RMS of B_hS is 4.1–5.3, slowly growing and close to √(2 ln n) = 4.13–5.39. This range cannot distinguish a bounded ratio from √(2 ln n) growth, which is the question Criterion D would need answered for the B-generated part.
- Sanity checks reproduced at every prime: Σλ = −1, √n S₀ = −2.000000, ΣS²/(4(n − 1)) = 1.000000000000, and max|S| = s_p (to 6 digits).

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved here.** Exact rationals, integers or outward balls for every number.
- (a1) Lemma 1: Σλ_j = −1, a unique zero eigenvalue, symmetry; hence ‖K‖_{2→2} = 1, ΣS² = 4(n−1), S₀ = −2/√n.
- (a2) Lemmas 2–3: ‖K‖_{∞→∞} ≥ 2(n−1)/(s√n) and ‖L_S‖_{∞→good} ≥ c_LS(n) ~ 0.118288√n, under (I1). Proposition 1 (pairing table), with the A rows inherited from Rounds 181/184.
- (a3) Theorem N, Corollaries N1–N2 and Remark N3: no seminorm with (S) and (P_S) admits a size-only bound for the non-seed multiplier. The constants c_N(γ, n) and the thresholds n ≥ 151 (γ = 0.61), n ≥ 1478 (γ = 0.1749) for exceeding 0.24310 are certified. One point t = a ∈ Q suffices for the negative statement.
- (a4) Proposition 3: Round 182 Proposition 2 applies to H_λ. Sup domination, (H1), the source bound and the Taylor constant max(c_A, κ₂/2) = c_A hold, with κ₂(747/5000) ≤ 0.157557. Hence κ*_H = κ*_A. Also g_H = g_S, since q_S ≤ 0.334571 < 0.339459 ≤ the per-step seed ratio.
- (a5) Proposition 4 (upper bound with the √n off-diagonal), Proposition 5 (counting horizon fractions) and Corollary 6 (reduction to Criterion D with Λ_n ≍ √n; window n < 10^414.197).
- (a6) The remark's arithmetic: floor·A/(2|√t|) ≥ 0.219397 at A = 0.912537, the ceiling 1.011122, and H(0.912537) ∈ [0.058797, 0.058798]. The ceiling 0.8192 is a float print of a certified bisection end.

**(b) Conditional / inherited.**
- (I1) ‖S‖_∞ ≤ s_p (Rounds 88/177).
- Sup domination of A_𝒳 at good coordinates (Rounds 96/181), with bad coordinates at most b₀ ≤ 3.
- D1–D4, (b4), (b-Jk) and (b-T), exactly as in Round 184. They enter only through the A-part of Proposition 3 and the quoted A-numbers.
- Round 173 (q₀ < 0.518), Round 177 (geometry, 0.545, 1.963) and Round 180 (the liminf/limsup of ‖R₆₀₂‖_{2,n}, ineffective; Criterion D).
- Remark N4 additionally needs a positive liminf of the good-coordinate part of ‖R₆₀₂‖_{2,n}.
- The Remark in §3 on H_λ = A_𝒳 for model simples is heuristic.

**(c) Evidence.** The witness table of §6: the actual ‖B_hS‖_∞ ≈ 0.2, adversarial same-size values about 0.11√n and 0.026√n, and sup/RMS 4.1–5.3.

## Exact remaining gap

- **For the cold criterion through Proposition 2**, uniformly in n, t ∈ Q and both lifts, one needs a bound ‖B_h‖_P < 0.24310 in some price P with sup domination, finite seed resolvent and the inherited source and Taylor constants. Equivalently, in the joint form, the Round 184 allowances.
- Theorem N shows that such a bound must use information about h beyond any rearrangement-invariant size. The available candidates are:
  1. an A-type (structured) price of the multiplier: the per-simple route, retired in Round 185 on model evidence. The certified retirement would additionally need a lower bound ≥ 0.023703 for the per-simple cost of the h-higher terms in the floor form (§5 Remark);
  2. a delocalization input for the B-generated part, i.e. Criterion D or a sup transfer with an n-independent ratio;
  3. a new signed price that sees cancellation between K's rows and h, which no round has proposed yet.
- Unchanged: D2–D4, (b4), (b-Jk), (b-T), the uniform complex stationary domain and derivative transfer. The proved frozen rate stays 1.066.

## Verdict

**Refuted, for the hybrid as posed: multiplication by h priced through a sup or counting norm, with the per-simple dimension price for the seed iteration.**

- The refutation is proved (Theorem N, Proposition 5, Corollary 6), not based on model evidence:
  - in any sup-dominating price in which the seed has bounded price, a size-only bound for the non-seed multiplier is false by a factor ≥ c_N(γ, n) ~ (8γm″(γ)/s³)√n;
  - the counting branch is Criterion D with Λ_n ≍ √n, which Round 180 shows fails.
- The hybrid seminorm itself is admissible for Round 182 Proposition 2: (H1), sup domination, source and Taylor constant are proved, given D1–D4. Its allowance is the Round 184 number ‖B‖ < 0.24310. But its only new ingredient, the counting component, carries √n.
- **Decision for the next call, as the mission's refuted branch states:** the cold dimension-price programme reduces to Criterion D or sup transfer. The only other way is a structured price of the multiplier, which is the retired per-simple route; its margin is quantified in the §5 Remark.
- **Scope.** Nothing here proves or refutes the original target, the ordinary Lovász theta limit of the prime Paley localizations. A failed sufficient method does not refute confinement: the floating evidence shows the actual multiplier is benign in sup.

## Ranked next tests

1. **Criterion D or sup transfer for the B-generated part (decisive for the cold route).**
   - Bound ‖w‖_∞/‖w‖_{2,n} for the words w = L^bBL_S^aR₆₀₂ by an n-independent constant. Since the sup of a structured field is bounded by its A-type price (n-independent), this amounts to a lower bound on the RMS of the same fields.
   - Alternatively, give a fixed-height sup transfer through 611 (Round 180 next test 2).
   - The floating sup/RMS of B_hS (4.1–5.3, close to √(2 ln n)) does not settle whether the ratio is bounded. A test at p ≈ 10⁸ with the full nine-center row would sharpen this evidence.
   - Outcome: a bounded ratio closes the cold criterion via Criterion D; a √(ln n) growth defeats Criterion D in its n-independent form and leaves only a signed sup transfer.
2. **(Low value for the main line) a per-simple lower bound for the h-higher terms of B.**
   - A certified per-simple lower bound ≥ 0.023703 for the cost of K((Φ′(S+h) − Φ′(S) − Φ″(S)h)·), using Prop. A on the quadratic term ½Φ‴(S)h², would make the Round 185 retirement independent of the bookkeeping (§5 Remark).
   - Only worth a call if the coordinator wants a certified retirement.
3. **Do not renew:** hybrid prices in which the non-seed multiplier is bounded through ‖h‖_∞, ‖h‖_{2,n} or any symmetric norm of h (Theorem N), and counting-rate arguments inside the Round 173 horizon (Proposition 5).

## Replay commands and outputs

All runs are from the repository root on 2026-11-21, with python-flint 0.9.0 and numpy 2.3.5.
- The constants script certifies statements about exact constants (rational comparisons and outward balls). It certifies no saved rounded input.
- The witness script uses double-precision rows computed on the fly and certifies nothing.

```bash
.venv/bin/python -B research/paley-186-cold-hybrid-constants.py
```
Output (under 1 s):
```
== 0. exact identities for the physical Paley operator K (integers) ==
K = real symmetric circulant on Z/n with eigenvalues lambda_j = chi(1 - g^(2j)), j mod n (Round 96: K^2 = I - P_1).
Claim: sum_j lambda_j = -1 and lambda_j = 0 iff j = 0; hence ||K e_0||^2 = (n-1)/n, sum_x S_x^2 = 4(n-1),
       S_0 = 2 sqrt(n) (K e_0)_0 = (2/sqrt n) sum_j lambda_j / ... = -2/sqrt(n).  (proof in the report, Lemma 1)
  all primes p = 1 mod 4, 5 <= p < 2000: sum lambda = -1, unique zero at j = 0, lambda_j = lambda_(n-j): True

== 1. m''(gamma) := min_{|xi| <= s+gamma} Phi_a''(xi) = 4a/(4a + (s+gamma)^2)^(3/2)  (real t = a, outward) ==
Phi_a''(xi) = 4a/(4a+xi^2)^(3/2) > 0 is even and decreasing in |xi|; s = s_p <= 2.828428539.
  gamma = 0.1749 (RMS(h) ~ 0.1749 [float input]): m''(gamma) >= 0.102838
  gamma = 0.3750 (3/8): m''(gamma) >= 0.100250
  gamma = 0.6100 (sup|h| ~ 0.61 [float input]): m''(gamma) >= 0.097149
  gamma = 1.9630 (Round 177 sup bound 1.963): m''(gamma) >= 0.078993
  gamma = 1.0000 (1): m''(gamma) >= 0.091911

== 2. Theorem N: sup over real g with ||g||_inf <= gamma of ||K((Phi_a'(S+g)-Phi_a'(S)) S)||_inf,good / P(S) ==
Lower bound (Lemma 2 + Theorem N; b0 = number of non-good coordinates, taken b0 <= 3):
  c_N(gamma,n) = gamma m''(gamma) [ 8(n-1)(n-1-1/n)/(s^2 n^(3/2)) - 2 b0 sqrt(n-1)/n ] / s,
  using P(S) <= A(S) = s_p <= s, sum|S| >= sum S^2/s, sum S^2 = 4(n-1), S_0^2 = 4/n.
  asymptotically c_N ~ (8 gamma m''(gamma)/s^3) sqrt(n).
  gamma = 0.1749: slope 8 gamma m''/s^3 >= 0.006359;  c_N > 0.24310 (Prop. C seed budget) for all n >= 1478;  c_N > 1 for n >= 24745;  c_N > 1.066 for n >= 28117
  gamma = 0.3750: slope 8 gamma m''/s^3 >= 0.013291;  c_N > 0.24310 (Prop. C seed budget) for all n >= 351;  c_N > 1 for n >= 5677;  c_N > 1.066 for n >= 6449
  gamma = 0.6100: slope 8 gamma m''/s^3 >= 0.020951;  c_N > 0.24310 (Prop. C seed budget) for all n >= 151;  c_N > 1 for n >= 2294;  c_N > 1.066 for n >= 2605
  gamma = 1.9630: slope 8 gamma m''/s^3 >= 0.054823;  c_N > 0.24310 (Prop. C seed budget) for all n >= 34;  c_N > 1 for n >= 349;  c_N > 1.066 for n >= 394
  gamma = 1.0000: slope 8 gamma m''/s^3 >= 0.032495;  c_N > 0.24310 (Prop. C seed budget) for all n >= 71;  c_N > 1 for n >= 963;  c_N > 1.066 for n >= 1093
  n = 5004: c_N(0.61, n) >= 1.4797;  c_N(0.1749, n) >= 0.4491
  n = 50024: c_N(0.61, n) >= 4.6853;  c_N(0.1749, n) >= 1.4220
  n = 500016: c_N(0.61, n) >= 14.8152;  c_N(0.1749, n) >= 4.4965
  n = 2000018: c_N(0.61, n) >= 29.6305;  c_N(0.1749, n) >= 8.9931
  n = 1000000000000: c_N(0.61, n) >= 20951.9697;  c_N(0.1749, n) >= 6359.1395
  (c_N is increasing in n for n >= 10; monotone bisection is valid there. Checked below on a grid.)
  c_N(gamma, k) < c_N(gamma, k+1) for 10 <= k < 400, gamma in {0.61, 0.1749}: True
  ||K||_{inf->inf} = sum_x |kappa(x)| >= 2(n-1)/(s sqrt n):  n = 10^6 gives >= 707.105
  Lemma 3 (seed operator on sup): ||L_S||_(inf->inf,good) >= c_LS(n), slope 8/(s^2 sqrt(4a+s^2)) >= 0.118288;  c_LS(10^6) >= 118.281;  c_LS > 1 for n >= 160

== 3. Counting route: a B-factor followed by b contracting steps costs sqrt(n) q^b in sup (Proposition 5) ==
Horizon k_n = ceil((4/7) log2 n).  sqrt(n) q^b <= 1 needs b >= theta(q) log2 n, theta(q) = 1/(2 log2(1/q)).
Fraction of the horizon in which a B-factor can be priced by counting with factor <= 1: 1 - theta(q)/(4/7).
  q = 0.5180: theta(q) in [0.526883, 0.526884];  usable fraction of the horizon in [0.07795, 0.07796]
  q = 0.5145: theta(q) in [0.521508, 0.521509];  usable fraction of the horizon in [0.08736, 0.08737]
  q = 0.5350: theta(q) in [0.554084, 0.554085];  usable fraction of the horizon in [0.03035, 0.03036]
  q = 0.5450: theta(q) in [0.570990, 0.570991];  usable fraction of the horizon in [0.00076, 0.00077]
  exact: 0.545^8 < 2^-7 : True  (so theta(0.545) < 4/7; Round 173)
  exact: 0.545^8 > 2^-7 - 10^-4 : True  (the margin in Round 173's cutoff is tiny)
  Norm-only confinement (Criterion D with Lambda_n = sqrt n): ||U_j||_inf <= sqrt(n) eps0/(1-q), eps0 = 9.07e-209.
  holds while sqrt(n) < (3/8 - 1/8)(1 - 0.545)/eps0 = 10^207.098, i.e. n < 10^414.197; fails for all large n because liminf ||R_602||_{2,n} > 0 (Round 180)

== 4. Hybrid seminorm H_lambda = A_X infimal-convolved with lambda ||.||_{l2} (lambda >= 1): Taylor constant ==
H(T(U)) <= c_A A(a)^2 + kappa_2 A(a) lambda||b|| + (kappa_2/(2 lambda)) (lambda||b||)^2 <= max(c_A, kappa_2/2) H(U)^2
kappa_2(u) := sup |Phi_t''| on the radius-u polydisk about V_602 <= 4|t|/(N - 2(1.963+u)^2)^(3/2) (Round 177 geometry)
  u = 0.1494: kappa_2(u) <= 0.157557, kappa_2/2 <= 0.078779;  c_A(M0+u) = c(M0+u)/2 >= 0.515106;  kappa_2/2 < c_A: True
  u = 0.3750: kappa_2(u) <= 0.166676, kappa_2/2 <= 0.083338;  c_A(M0+u) = c(M0+u)/2 >= 0.609114;  kappa_2/2 < c_A: True
  all u in (0, 3/8]: kappa_2(u)/2 <= kappa_2(3/8)/2 <= 0.083338 < c_A(M0) = c(M0)/2 >= 0.464976 <= c_A(M0+u): True
  => the H_lambda Taylor constant is c_A itself for every u <= 3/8; kappa*_H = kappa*_A in
     [0.83790250, 0.83793100] (Round 184), so the Duhamel threshold Gamma < 1/(1-kappa*_A) >= 6.16912 is unchanged.

== 5. Counting rates and the Round 184 test-2 cost ==
  ||L_S||_(2->2) <= sup |Phi_t'(S)| <= s/sqrt(N + s^2) <= 0.334571   (|4t + x^2| >= Re 4t + x^2 >= N + x^2 for real x)
  ||B_h||_(2->2) <= sup|Phi_t'(V_602) - Phi_t'(S)| <= kappa_2(0) * 1.963 <= 0.299209   (Round 177 sup bound)
  would-be sup-priced cost rho_0 x/sqrt N + H(x) at x = 0.61 [float sup|h|]: in [0.190729, 0.190730]  (< 0.24310: True)
  would-be sup-priced cost rho_0 x/sqrt N + H(x) at x = 0.7499: in [0.242709, 0.242710]  (< 0.24310: True)
  would-be sup-priced cost rho_0 x/sqrt N + H(x) at x = 1.963 [Round 177]: in [0.920322, 0.920323]  (< 0.24310: False)
  Theorem N: no sup-dominating price admits this cost as a bound in terms of x = ||h||_inf; see report §3.

== 6. Seed part of the hybrid and the per-simple floor ==
  per-step path-summed seed A-ratio >= 2 varpi_lo |ghat_1|_lo >= 0.339459;  counting rate q_S <= 0.334571;  q_S < per-step lower bound: True
  => G_m >= (per-step)^m > q_S^m for all m, so ||L_S^m||_H <= max(G_m, q_S^m) = G_m and g_H = g_S <= 2.467879.
  model A(h) = 0.912537: per-simple h-linear cost >= floor*A(h)/(2|sqrt t|) >= 0.219397 (budget 0.24310 leaves <= 0.023703 for the h-higher terms; their majorant H(A(h)) in [0.058797, 0.058798])
  model A(h) = 1.004901: per-simple h-linear cost >= floor*A(h)/(2|sqrt t|) >= 0.241604 (budget 0.24310 leaves <= 0.001496 for the h-higher terms; their majorant H(A(h)) in [0.073245, 0.073246])
  optimistic ceiling, h-higher terms free and h-linear ratio at the floor: A(h) < 1.011122 (vs certified model A(h_<=3) >= 0.912537)
  with the h-higher majorant H kept: floor*A/(2|sqrt t|) + H(A) < 0.24310 iff A(h) < 0.8192 (bisection; float print)
```

```bash
.venv/bin/python -B research/paley-186-cold-hybrid-witness.py
```
Output ([float], about 1–2 min):
```
[float] t = a = 2031/128, mark t_0 = n, one real lift, double precision; evidence only

[float] p = 10009, n = 5004; fixed-point step RMS 7.0e-15
[float]  (0) sum sign row = -1; sqrt(n) S_0 = -2.000000 (exact -2); sum S^2/(4(n-1)) = 1.000000000000; max|S| = 2.828568 vs s_p = 2.828568
[float]  sup|h| = 0.5699, RMS(h) = 0.1949, sup|Phi'(V)-Phi'(S)| (non-mark) = 0.0642
[float]  (1) actual: ||B_h S||_inf = 0.1618  RMS 0.0394  sup/RMS 4.11;   ||B_h h1||_inf = 0.0221  RMS 0.0058
[float]  (2a) |g| = sup|h| = 0.5699: x0 = 1057; value at x0 = 7.360 (lower-weight sum 7.165); value/sqrt(n) = 0.1040; value/(s_p sqrt n) = 0.0368; Theorem N c_N/sqrt(n) = 0.0197; ratio to A(S): 2.60 vs c_N = 1.39
[float]  (2b) |g_x| = |h_x| (same sup 0.5699, same RMS 0.1949 as h): x0 = 536; value at x0 = 2.181; value/sqrt(n) = 0.0308; ratio to A(S): 0.77
[float]  (2c) |g_x| = |h_x|, input f = h_1: value at x0 = 0.294; value/sqrt(n) = 0.0042; ratio to A(h_1) = 0.4945: 0.59;  actual ||B_h h_1||_inf = 0.0221
[float]  (3) counting route for the actual product: sqrt(n) RMS(B_h S) / sup|B_h S| = 17.2 (the factor lost by pricing the product in counting norm and converting back to sup)

[float] p = 100049, n = 50024; fixed-point step RMS 3.9e-15
[float]  (0) sum sign row = -1; sqrt(n) S_0 = -2.000000 (exact -2); sum S^2/(4(n-1)) = 1.000000000000; max|S| = 2.828441 vs s_p = 2.828441
[float]  sup|h| = 0.5513, RMS(h) = 0.1752, sup|Phi'(V)-Phi'(S)| (non-mark) = 0.0640
[float]  (1) actual: ||B_h S||_inf = 0.1638  RMS 0.0382  sup/RMS 4.29;   ||B_h h1||_inf = 0.0191  RMS 0.0044
[float]  (2a) |g| = sup|h| = 0.5513: x0 = 31919; value at x0 = 22.343 (lower-weight sum 21.760); value/sqrt(n) = 0.0999; value/(s_p sqrt n) = 0.0353; Theorem N c_N/sqrt(n) = 0.0191; ratio to A(S): 7.90 vs c_N = 4.27
[float]  (2b) |g_x| = |h_x| (same sup 0.5513, same RMS 0.1752 as h): x0 = 17649; value at x0 = 5.837; value/sqrt(n) = 0.0261; ratio to A(S): 2.06
[float]  (2c) |g_x| = |h_x|, input f = h_1: value at x0 = 0.703; value/sqrt(n) = 0.0031; ratio to A(h_1) = 0.4945: 1.42;  actual ||B_h h_1||_inf = 0.0191
[float]  (3) counting route for the actual product: sqrt(n) RMS(B_h S) / sup|B_h S| = 52.2 (the factor lost by pricing the product in counting norm and converting back to sup)

[float] p = 1000033, n = 500016; fixed-point step RMS 6.0e-15
[float]  (0) sum sign row = -1; sqrt(n) S_0 = -2.000000 (exact -2); sum S^2/(4(n-1)) = 1.000000000000; max|S| = 2.828429 vs s_p = 2.828429
[float]  sup|h| = 0.6063, RMS(h) = 0.1756, sup|Phi'(V)-Phi'(S)| (non-mark) = 0.0740
[float]  (1) actual: ||B_h S||_inf = 0.2035  RMS 0.0386  sup/RMS 5.27;   ||B_h h1||_inf = 0.0197  RMS 0.0043
[float]  (2a) |g| = sup|h| = 0.6063: x0 = 325912; value at x0 = 77.463 (lower-weight sum 75.249); value/sqrt(n) = 0.1095; value/(s_p sqrt n) = 0.0387; Theorem N c_N/sqrt(n) = 0.0208; ratio to A(S): 27.39 vs c_N = 14.73
[float]  (2b) |g_x| = |h_x| (same sup 0.6063, same RMS 0.1756 as h): x0 = 418857; value at x0 = 18.322; value/sqrt(n) = 0.0259; ratio to A(S): 6.48
[float]  (2c) |g_x| = |h_x|, input f = h_1: value at x0 = 2.166; value/sqrt(n) = 0.0031; ratio to A(h_1) = 0.4945: 4.38;  actual ||B_h h_1||_inf = 0.0197
[float]  (3) counting route for the actual product: sqrt(n) RMS(B_h S) / sup|B_h S| = 134.1 (the factor lost by pricing the product in counting norm and converting back to sup)

[float] p = 4000037, n = 2000018; fixed-point step RMS 6.2e-15
[float]  (0) sum sign row = -1; sqrt(n) S_0 = -2.000000 (exact -2); sum S^2/(4(n-1)) = 1.000000000000; max|S| = 2.828427 vs s_p = 2.828427
[float]  sup|h| = 0.6065, RMS(h) = 0.1764, sup|Phi'(V)-Phi'(S)| (non-mark) = 0.0761
[float]  (1) actual: ||B_h S||_inf = 0.1917  RMS 0.0388  sup/RMS 4.94;   ||B_h h1||_inf = 0.0202  RMS 0.0043
[float]  (2a) |g| = sup|h| = 0.6065: x0 = 1576475; value at x0 = 154.795 (lower-weight sum 150.370); value/sqrt(n) = 0.1095; value/(s_p sqrt n) = 0.0387; Theorem N c_N/sqrt(n) = 0.0208; ratio to A(S): 54.73 vs c_N = 29.47
[float]  (2b) |g_x| = |h_x| (same sup 0.6065, same RMS 0.1764 as h): x0 = 1660962; value at x0 = 36.717; value/sqrt(n) = 0.0260; ratio to A(S): 12.98
[float]  (2c) |g_x| = |h_x|, input f = h_1: value at x0 = 4.339; value/sqrt(n) = 0.0031; ratio to A(h_1) = 0.4945: 8.77;  actual ||B_h h_1||_inf = 0.0202
[float]  (3) counting route for the actual product: sqrt(n) RMS(B_h S) / sup|B_h S| = 286.1 (the factor lost by pricing the product in counting norm and converting back to sup)
```
