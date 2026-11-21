# Round 193 independent agent audit

- **Author:** Claude auditor session (Round 193), started by the Round 193 coordinator. This is an agent audit. It is not human acceptance and not a mathematical certification.
- **Scope:** the two Round 193 calls
  1. `review-lemma-mprime-theorem-a` (report `research/native-claude-review-lemma-mprime-theorem-a-193.md`, script `research/paley-193-review-checks.py`);
  2. `ordinary-ss-star-literature` (report `research/native-claude-ordinary-ss-star-literature-193.md`, script `research/paley-193-ssstar-checks.py`).
- **Files written:** this file only (plus, if needed, `research/paley-193-audit-*.py`). Nothing committed.
- **Labels:** ACCEPTED / ACCEPTED WITH CORRECTION / REJECTED / NOT CHECKED.

## 0. Blind overlap assessment (written before opening `coordination/shared-obligations/`, `coordination/drafts/` or `coordination/round-193-inflight.json`)

Read for this section: `AGENTS.md`, `docs/WORKFLOW.md`, the two mission files under `coordination/missions/round-193/`, and the two reports. Nothing else under `coordination/`.

- **Shared `cand:` ID.** Both missions carry the same boilerplate "Current proof obligation" paragraph naming `cand:gp-shifted-energy` and `cand:gp-sector-constancy`, but neither call *works on* a shared candidate estimate:
  - Call 1 touches `cand:gp-shifted-energy` only as a reviewer: its item 3 (R190 application of MPRRS Theorem 37) is what supports the recorded status "known at |I|^{32/13}" of that candidate. It does not touch `cand:gp-sector-constancy`.
  - Call 2 touches `cand:gp-sector-constancy` only in its mission-requested side remark (§5: a progression-shaped failure of (SS) would reduce to (GP-Sub_κ) at lengths below √p). It does not touch `cand:gp-shifted-energy`.
  - So no `cand:` ID is used as a load-bearing input by both calls. My classification: **no shared estimate**; a boilerplate mention of the same two IDs.
- **Shared inputs.** Both read `research/round-191-acceptance.json` and `research/round-192-acceptance.json` (same hashes in both missions) and both are exported from `coordination/round-192.json` (SHA-256 `6237ed51…`). These are context, not a shared estimate. Mathematical inputs are disjoint: call 1 uses R187/R188/R190 and MPRRS/Stevens–de Zeeuw; call 2 uses R192 §3, AUD192 §2.9 and the idempotent/spectral literature.
- **Would one result have changed the other's dispatch?**
  - Call 2's outcome cannot affect call 1 (a literature check on (SS\*) says nothing about Lemma M′, Theorem A or MPRRS).
  - Call 1's *refuted* branch says "mark which accepted downstream statements (R187–R192) depend on it and must be reassessed before any further ordinary call". Read literally, a refutation would have gated further ordinary calls, which in principle includes call 2. But call 2 is a source-level literature question about (SS\*), whose statement and conditional use (R192 Theorem E, vertex route) do not, as far as the two reports show, rest on Lemma M′, Theorem A or the MPRRS application. A refutation in call 1 would therefore have changed call 2's *priority* at most, not its content or validity. Since call 1 came back supported, the issue did not arise.
  - My blind answer: **no dispatch change**; at most a one-directional, low-weight timing dependency (call 1 refuted ⇒ possibly defer call 2), unrealised.

(Comparison with the coordinator's pre-dispatch files follows in §0.1, written after the above was saved.)

### 0.1 Comparison with the coordinator's pre-dispatch record (opened after §0 was saved)

Files: `coordination/drafts/round-193-dependency-assessment.json` and `coordination/shared-obligations/round-193-before.json` (captured 2026-11-21T04:32:40Z, coordinator `coordination/round-192.json`, SHA-256 `6237ed51…7fcbf`, which matches the file on disk; that file shows as modified in the working tree, but its bytes match the hash the missions name). I did not open `coordination/round-193-inflight.json`.

- **Agreement.** Both say: no shared estimate (`known_shared: []`); call 1 touches `cand:gp-shifted-energy` only as the source of the 32/13 bound it re-checks; call 2 touches `cand:gp-sector-constancy` only through the progression-shaped failure remark; no active earlier call; cold paused. My blind classification matches.
- **Small differences (bookkeeping, none changes the dispatch):**
  1. The coordinator writes "no input except the Round 192 acceptance". Both missions also list `research/round-191-acceptance.json` (same hash). Two shared context inputs, not one.
  2. `candidate_ids_by_call` is empty for both calls. Under the AGENTS.md wording ("touched" vs "shared"), it would be more informative to list `cand:gp-shifted-energy` for call 1 and `cand:gp-sector-constancy` for call 2 as *touched, not shared*. `known_shared: []` stays correct.
  3. The coordinator says "neither result changes the other's assignment". That is right for content. Read literally, call 1's refuted branch ("reassess … before any further ordinary call") would have deferred call 2. This one-directional timing dependency was not realised (call 1 came back supported) and should be recorded as "possible, unrealised", not as "none".

---

## 1. Replays and hashes

All hashes taken at the start of this audit with `shasum -a 256`. Python 3.14.5.

| file | SHA-256 | matches report? |
|---|---|---|
| `research/native-claude-review-lemma-mprime-theorem-a-193.md` | `1a2cb16adf0f36ed5633e1bbf4e04ffaff6cff5c513f8d08fbedb8454d362c8d` | (report) |
| `research/native-claude-ordinary-ss-star-literature-193.md` | `57d4dbaf41c4f899b92c31adc352332aa809f53421960ee59e856564f489ff2a` | (report) |
| `research/paley-193-review-checks.py` | `ef902621a215cdc25e5dedbcf924491ecdbb321a9335e4210efeb419de3ad5d1` | yes |
| `research/paley-193-ssstar-checks.py` | `ac4d042abed532f530aa30fb94e2c07c50d4c8fe244c8ab9060a1882314facc3` | yes |
| `coordination/missions/round-193/review-lemma-mprime-theorem-a.md` | `2516d380ae3162c794693f5e89a8ce062c5f231195c851905a9e6d9bb191c923` | — |
| `coordination/missions/round-193/ordinary-ss-star-literature.md` | `6b5399117f6c83df00f07f06641fc7e27d454e9a19d4950e55a269d2d24ee063` | yes (`6b539911…ee063`) |
| R187 / R188 / R190 reports, R192 report, AUD192 | `52686317…`, `cee51251…`, `557777a4…`, `509e0d40…`, `455c97ed…` | yes, all equal the mission hashes |

**Replays.**
- `python3 -B research/paley-193-review-checks.py` (0.8 s): prints exactly the three lines quoted in the report (`Part M … 47 … OK`, `Part A … 40 laws … 14682836797/52744721152 (0.2784); 5354 chart entries`, `ALL EXACT CHECKS OK`). Stdout SHA-256 `3428b7a9039c6caa5fb2c709c1f27e063e6d60d0eb97050037836b338f8e4c64`. The report does not give a stdout hash; the printed text matches.
- `python3 -B research/paley-193-ssstar-checks.py` (0.1 s): `ALL OK`; stdout SHA-256 `e1c399fed427d518d7cf7b3b70ad77a9bd2ca1cf2ef575abc4673a024487ac2d`, **identical** to the report's. Table values match the report's table.
- Script content: the review script uses `fractions.Fraction` and integers only for assertions (float appears only in one printed ratio); it does not import Round 187/188 code. The ss-star script is floating point and labelled as evidence only.

---

## 2. Call 1: `review-lemma-mprime-theorem-a`

### 2.1 Independence of the re-derivations (spot check)

- The report says each step was re-derived and the script written before the corresponding audit was read. That order is **self-reported and cannot be verified** from the files. What can be checked:
  - The script is a separate implementation (exact `Fraction` arithmetic; p ≤ 41 for Part M against the R187 audit's p ∈ [101, 409]; Theorem A (i)/(ii) checked exactly on genuine ω ≥ 0 laws, where the R188 audit used double precision). Different code and different test ranges: genuinely complementary evidence.
  - The MPRRS text was extracted by a third route (own zlib reader). I made a fourth extraction (own zlib reader, independent code, from `https://arxiv.org/pdf/1702.01003v5`): Theorem 37, Lemma 33 and Theorem 34 read **verbatim as quoted** in the report, and the printed proof says only "we may take D₂ = M^{3/2} whenever M|A|²|B| ≤ p²", i.e. the second condition of Lemma 33 is indeed not addressed.
  - The report's wording of the repair differs slightly from AUD190's (report: |B| ≤ |A|^{20/13} ≤ M|A|²; AUD190: ≤ |A|²). Consistent with, but not proof of, independent derivation.
  - The report finds **no disagreement anywhere** with three earlier audits. That is consistent with all three being right; it gives no evidence of independence by itself.
- **Label:** independence claim **NOT CHECKED** (unverifiable); the evidence it adds (exact checks, separate extraction) **ACCEPTED**.

### 2.2 Lemma C, Lemma M′, Proposition P′ (R187)

Re-derived here (not from the report's table):
- Step 4 algebra: I ≥ htηm/2 and I ≤ 3C₂s′^{3/4}b′^{1/2}(tm)^{3/4} (n = tm lines) give (tm)^{1/4} ≤ 6C₂s′^{3/4}b′^{1/2}/(hη), so tm ≤ 6⁴C₂⁴s′³b′²/(hη)⁴; s′³b′² = s′(s′b′)² = s′α²|F|² ≤ μ_*α²|F|²; |F|²/η⁴ ≤ 16L₀⁴K²m² by (2.1). Hence t ≤ C₄L₀⁴α²K²mμ_*/h⁴. **η cancels** as claimed. ✓
- (2.1): |F| ≤ E/ρ² and ρ ≥ E/(2PL₀) give |F| ≤ 4P²L₀²/E = 4η²m⁴L₀²K/m³. ✓
- P′ excess identities, checked symbolically by hand:
  - T1 = u_s/6 − u_g/6 − (2/3)(e_g + μ_g) expands to e_s/3 + μ_s/6 − e_g − 5μ_g/6 ✓;
  - T2 = −1/6 + u_s/4 − u_g/2 = −5/24 − d/2 − w_s/4 + z/4 with u_s = w_s + 1/6 − z ✓;
  - T3 = −1/24 − w_g − μ_s/4 = −w_g − w_s/4 − z/4 ✓.
  - Signs: T1 ≤ o(1) needs u_s ≤ u_g; T2 ≤ −1/6 + o(1); T3 ≤ o(1) needs z ≥ 0, i.e. e_s ≤ 1/6 + o(1). The constraints the report lists are exactly the load-bearing ones. ✓
- The term formulas themselves (that the three Lemma M′ terms, with K_M ≍ p^{2e+μ}, have these exponents) were taken from R187/its audit and not rebuilt from scratch by me.
- Verdicts: Lemma C **ACCEPTED**; Lemma M′ **ACCEPTED** (Step 4 algebra re-derived; Steps 1–3 replayed exactly by the report's script); P′ **ACCEPTED** (identities re-derived; term formulas inherited); "K^{5/4} against |B|" wording correction **ACCEPTED** (cosmetic, as the report says).

### 2.3 Theorem A (R188) and the new t-sum identity

- Lemma A1, A2, (i), (ii): spot-checked the orthogonality and α = 1 bookkeeping. With G = (p−1)ω(1) and Lemma A2 exact, one gets
  Σ_t‖πφ_t‖² = p𝒯 − G²Λ₀ − (p−1)Σ_{α≠1}ω(α)²|m̂(ᾱ)|² − G²M₁²/(p(p−1)).
  Using (p−1)Σ_{all α}ω²|m̂(ᾱ)|² = Σ_λ c_g(λ)C(λ) and m̂(𝟏) = M₁, this equals the report's p𝒯 − G²Λ₀ − Σc_gC + G²M₁²/p. ✓ The slack in (ii) is (p−1)Σ_{α≠1}ω²|m̂|² + G²M₁²/(p(p−1)) ≥ 0. ✓ The identity is also checked exactly by the script (replayed).
- The test laws f = Σc_i1_{K_i} (K_i ≤ Q, c_i ≥ 0, Σc_i = 1) do give ν = Σc_i·uniform(K_i^⊥) ≥ 0 a probability and (H3) (subgroups are inversion-closed), so the "ω ≥ 0" checks of (i) are on genuine admissible-sign laws. ✓ As the report says, they are multiplicatively structured and test no exponent.
- Verdicts: Theorem A **ACCEPTED**; new t-sum identity **ACCEPTED** (re-derived above and exact replay); assessment of the four AUD188 corrections **ACCEPTED**.

### 2.4 MPRRS Theorem 37 application (R190) and the repair

- Lemma 33's second condition with |AA| = M|A|: max(M|A|, |B|) ≤ (M|A|²|B|)^{1/2} ⟺ (M ≤ |B| and |B| ≤ M|A|²). ✓
- Upper end: WLOG E^×(A+α) ≥ 4M^{33/13}|A|^{32/13}, so |B| ≤ 4|A|⁴/E^× ≤ |A|^{20/13}M^{−33/13} ≤ |A|^{20/13} ≤ M|A|² (M ≥ 1, 20/13 < 2). ✓ The report's "|B| ≤ |A|^{20/13} ≤ M|A|²" is right (it drops the harmless M^{−33/13} ≤ 1).
- Lower end: E^×(A+α, B) ≤ |A||B|² (fix three coordinates) = |A||B|^{3/2}|B|^{1/2} < M^{1/2}|A||B|^{3/2} ≤ M^{3/2}|A||B|^{3/2} for |B| < M. ✓ (Since M ≤ 2 + O(1/N) here, this concerns |B| = 1 only.)
- First condition: M|A|²|B| ≤ |A|^{46/13}M^{−20/13} ≤ p² ⟺ |A| ≤ p^{13/23}M^{10/23}. ✓ Lemma 32: |AA| ≤ 2N ≪ p^{2/3}. ✓ D₁^{6/13}D₂^{2/13} = M^{30/13+3/13} = M^{33/13}; logs (log)^{6/13+12/13} = (log)^{18/13}. ✓
- Application: I′ = I∖{1}, |I′I′| ≤ 4K+1, |I′| = 2K, M ≤ 2 + 1/(2K); 0 ∉ I′ − 1. ✓
- Transfer: with h = 1_{1−I′}, X(1_I) = Σ_{κ∈Q∖{1}}c_h(κ)² (R188 line 84: m(r) = c_h(1−r) on 1−r ∈ Q∖{1}) ≤ E^×(1−I′) = E^×(I′−1). ✓
- Arithmetic: 32/13·1/2 = 16/13 = 5/4 − 1/52; 1/2 + 16/13 = 45/26 = 7/4 − 1/52; δ = 1/52. ✓
- **45/26 labelling:** the report's §3.3 and verdict table call it "a weakening of an obstruction, not an upper bound on T₀, X or the covariance for any law". ✓ Correct label.
- Verdicts: Theorem 37 quote **ACCEPTED** (fourth extraction, verbatim); hypotheses for A = I′, α = −1 **ACCEPTED**; repair **ACCEPTED**; E^×(I′−1), X(1_I) ≲ |I|^{32/13} **ACCEPTED**; 45/26 as obstruction **ACCEPTED**; "§5 inaccuracy" note **ACCEPTED**.
- **Correction (minor).** The report says it "additionally notes the direct inequality X(1_I) ≤ E^×(I′−1)". R190 §1 (line 57) already states X(1_I) ≤ E^×(I−1) (from the R189 audit). The only refinement is I′ in place of I, which removes the O(N²) term. Not a new result. **ACCEPTED WITH CORRECTION** (attribution).
- Still unread at source by any agent: Shkredov 2013 (Theorem 34's proof), MPRRS Theorem 11, Lemma 33's proof. The report lists them correctly. None of these enters a proof of the project; they support only the status line of `cand:gp-shifted-energy` and the obstruction bookkeeping.

### 2.5 Call 1 summary

| claim | label |
|---|---|
| Lemma C, Lemma M′, Prop. P′ correct as stated | ACCEPTED |
| Theorems 1–2 (R187) as consequences | ACCEPTED (inherited inputs listed by report not re-derived) |
| Theorem A (R188) correct as stated, every t | ACCEPTED |
| new exact t-sum identity (slack ≥ 0) | ACCEPTED |
| MPRRS Thm 37 quote, applicability, repair | ACCEPTED |
| 45/26 is an obstruction level, not a bound | ACCEPTED |
| "direct inequality X(1_I) ≤ E^×(I′−1)" as an addition | ACCEPTED WITH CORRECTION (already in R190 with I; only I′ is new) |
| independence of re-derivation (order of reading) | NOT CHECKED (self-reported) |
| downstream: no R187–R192 statement needs reassessment | ACCEPTED |

---

## 3. Call 2: `ordinary-ss-star-literature`

### 3.1 Statements matched

The report's §1 statement of (SS\*) is the AUD192 §2.9 form verbatim in substance (for every a, there are L, c; no sharp sequence with |S_k| ~ √(N_k/2) has liminf_k min_B Σ_{ξ∉B} g_k/M_k > 0, B over ≤ L dual subgroups of orders in [cN/|S|, N/(c|S|)]), and (SS\*\*) carries the four extra hypotheses of AUD192 §2.9. ✓ Normalisation ‖f‖_A = Σ_ξ|N^{-1}Σ_x f(x)e(−xξ/N)| agrees with Green–Sanders (checked at source: "the ℓ¹-norm of the Fourier transform of f", expectation normalisation on G) and with Konyagin–Shkredov (lower bounds ≍ (log)^{1/3} are only meaningful with the 1/p normalisation). ✓

### 3.2 Lemma 1 (adding o(|S|) points to a subgroup)

Re-derived: off H^⊥, \(\widehat{1_S}=\widehat{1_E}\), mass ≤ Nr/|S|². On H^⊥∖{0}, g < a forces |\(\widehat{1_E}\)| ≥ h − √a(h+r) ≥ (1−√a)h − r ≥ (1−√a)h/2; Chebyshev gives ≤ 4Nr/((1−√a)²h²) such ξ, each contributing < a, and h ≥ |S|/2. Sum ✓. Conclusion of (SS) with L = 1: H^⊥ has order N/h ~ N/|S|, inside the window. ✓ The audit script checks the bound on four instances (it is loose by a factor ~ 15–20).

- **Correction 1 (scope of the "Reading").** Lemma 1 is proved only for S = subgroup ∪ E. The general sentence "sharpness and the (SS) conclusion are both stable under adding or removing o(|S|) arbitrary points" is true for the (SS) conclusion, but for sharpness it holds only **with a level loss**: if S is sharp at a and |S Δ S′| = o(|S|), then S′ is sharp at every a′ < a (frequencies with g_S ≥ a and g_{S′} < a′ need |\(\widehat{1_{S\Delta S'}}\)| ≥ (√a − √a′ − o(1))|S|, Chebyshev count o(M); frequencies with g_S < a contribute ≤ 2g_S + 2|\(\widehat{1_E}\)|²/|S′|², total o(M)). At the same level a it can fail if mass sits at g ≈ a. Harmless for the argument, but the sentence should say "at any lower level". **ACCEPTED WITH CORRECTION.**

### 3.3 Lemma 2 and the bound ‖1_S‖_A ≤ a^{-1/2}

Re-derived: ‖h‖_A = αΣ_Λ g^{1/2} ≤ αa^{-1/2}Σ_Λ g ≤ a^{-1/2} (g^{1/2} ≤ g/√a on Λ; Σg = 1/α). E_x|1_S − h|² = α²Σ_{ξ∉Λ}g (Parseval; 0 ∈ Λ) = o(α). Chebyshev: #{|1_S−h| ≥ ε} ≤ ε^{-2}N·o(α) = o(|S|). |Λ| ≤ 1/(aα); |Λ| ≥ Σ_Λ g. Converse ✓. In the exact case h = 1_S gives ‖1_S‖_A ≤ a^{-1/2}, sharper than R192's 1/a (which bounded Σ_Λ g^{1/2} by |Λ|). Checked on the subgroup example: ‖1_H‖_A = 1. **ACCEPTED** (Lemma 2 and the a^{-1/2} bound).

### 3.4 The located gap ("robustness") — a correction that matters

The report says (§0 item 2, §2.3): every approximate idempotent theorem needs a sup-norm hypothesis; "Lemma 2 supplies smallness only outside o(|S|) points, and Lemma 1 shows the (SS) hypothesis cannot supply more."

- Green–Sanders Lemma 3.1, read at source by me (own extraction of arXiv:math/0611286v2, p. 4): f: G → **ℝ**, ‖f‖_A ≤ M, d(f, ℤ) ≤ e^{−C₁M⁴}, where d(f, ℤ) < ε means f takes values in ℤ + [−ε, ε] at every point. The hypothesis is about **f being near-integer**, not about f being near 1_S.
- The natural f is h itself (‖h‖_A ≤ a^{-1/2}). The relevant question is therefore whether sup_x d(h(x), ℤ) is small, not whether |1_S − h| is small everywhere. Lemma 1 shows the second fails (the added points are exceptional), but **not** the first: in Lemma 1's examples h ≈ 1_H + (averages of 1_E over H-cosets), so d(h, ℤ) ≤ r/h-type quantities. The audit script confirms it: for the subgroup + 2, 5, 7 random points, sup d(h, ℤ) = 0.033 = 1/30 while #exc = r; for the union of two cosets plus 3 points, 0.126; only the non-sharp interval has 0.498.
- **Auditor's reduction (sketch; derived from the GS proof, not a stated theorem; not used for any verdict).** Call (Clean_a): along the sharp sequence, sup_x d(h_k(x), ℤ) ≤ e^{−C₀a^{-2}} for large k (C₀ ≫ C₁ the GS constants). Under (Clean_a), the iteration in GS's proof of Theorem 1.3 runs from d₀ = sup d(h, ℤ) instead of 0 (each step at most doubles d plus ε; at most 2M−1 levels, M = a^{-1/2}), giving h_ℤ = Σ_{j≤L}±1_{x_j+H_j} with L ≤ e^{e^{Ca^{-2}}} and ≤ a^{-1/2} + 1/100 distinct H_j. Where |1_S − h| < 1/4, h_ℤ = 1_S; so ‖1_S − h_ℤ‖²_{ℓ²} ≤ (L+1)²·o(|S|) and the g-mass off ∪H_j^⊥ is o(M). With Proposition 3(2)'s window argument this is the ε-form of (SS) for that sequence. So the precise missing input is (Clean_a) (sup-norm near-integrality of the spectral truncation), not "an empty exceptional set for 1_S − h". Whether sharpness implies (Clean_a) is open; I found no example of a sharp set with sup d(h, ℤ) bounded below, and no proof.
- For **prime N**, the same reduction plus Corollary 4 below shows that (Clean_a) must fail for every sharp sequence of size ~√(N/2), if any exists.
- **Label:** the conclusion "no source implies (SS\*)" is unaffected. The justification "Lemma 1 shows the (SS) hypothesis cannot supply more [than an exceptional set]" is **REJECTED as stated**: it refers to the wrong function. Gap description **ACCEPTED WITH CORRECTION**: replace by "no source, and nothing proved here, gives sup_x d(h, ℤ) ≤ e^{−Ca^{-2}} for the Λ-truncation h; Lemma 1 does not obstruct this (its examples satisfy it)".

### 3.5 Proposition 3 (exact case, composite N)

- GS Theorem 1.3 at source (my extraction, p. 2): "Suppose that G is a finite abelian group and that f: G → ℤ is a function with ‖f‖_A ≤ M. Then we may write f = Σ_{j=1}^{L} ±1_{x_j+H_j} … L ≤ e^{e^{CM⁴}}. Furthermore the number of distinct subgroups H_j may be bounded above by M + 1/100." **The "M + 1/100" claim is confirmed.**
- Part 1 with M = a^{-1/2}: L ≤ e^{e^{Ca^{-2}}} and ≤ a^{-1/2} + 1/100 distinct subgroups. ✓ Sanders Thm 1.1 (exp(M^{4+o(1)}) = exp(a^{-2-o(1)})) **NOT CHECKED** at source by me.
- Part 2 re-derived: ξ ∉ B_η in some H_j^⊥ with |H_j| > |S|/η: fewer than mηN/|S| points, g ≤ 1. Other ξ ∉ B_η: \(\widehat{1_S}=\widehat{F_{\rm small}}\), Σ|\(\widehat{F_{\rm small}}\)|² = N‖F_small‖² ≤ N(Σ|H_j|^{1/2})² ≤ NL²η|S|. ✓
- **Correction 2 (one representation).** Part 1 mixes two representations: m ≤ a^{-1/2} + 1/100 comes from GS (with GS's L), the exp(a^{-2-o(1)}) bound from Sanders (whose representation carries no bound on the number of distinct subgroups except m ≤ L). The bound (m + L²)η in Part 2 must use one representation: (a^{-1/2} + 1/100 + L_GS²)η, or (L_S + L_S²)η. **ACCEPTED WITH CORRECTION.**
- Remark (auditor, re-derived): in the exact case the small components carry no mass at all once η < √a/L: at ξ outside B_η and the large duals, |\(\widehat{1_S}(\xi)\)| ≤ Σ_{small}|H_j| ≤ Lη|S|, so g ≤ L²η² < a, hence g = 0. The remainder then comes only from large-|H_j| components (≤ mηM). The fixed-c form of (SS) still does not follow (components with |H_j|/|S| → ∞ slowly, or bounded but above 1/c), as the report says. The report's caveat that this is an ε-form and that Theorem E's use depends on the c₁-dependence of (A4)'s c₀ is right. **ACCEPTED.**

### 3.6 Corollary 4 / Konyagin–Shkredov for prime N

- KS Theorem 3 at source (my extraction of arXiv:1403.8129v1, p. 2): p prime, A ⊆ ℤ_p, exp((log p/log log p)^{1/3}) ≤ |A| ≤ p/3, then ‖A‖_A ≫ (log(p/|A|))^{1/3}(log log(p/|A|))^{−1+o(1)}. **Matches the report.** With ‖1_S‖_A ≤ a^{-1/2} fixed and |S| ~ √(N/2) in range, contradiction for large N. **ACCEPTED.**
- **Correction 3 (KS is not needed).** For prime N the only subgroups are {0} and ℤ/N, so GS Theorem 1.3 already writes an exactly sharp 1_S as c·1 + Σ_{j≤L}±δ_{x_j}, with L ≤ e^{e^{Ca^{-2}}}; hence |S| ≤ L or |S| ≥ N − L, impossible for |S| ~ √(N/2) and N large. The KS citation is correct and gives a quantitative rate, but the corollary is already a consequence of GS (the report's Prop. 3 source). Not an error.
- The report's limit (prime N = n only for safe primes p = 2n+1) ✓.

### 3.7 Other source claims

| claim | my check | label |
|---|---|---|
| GS Lemma 3.1 is sup-norm (d(f, ℤ) ≤ e^{−C₁M⁴}) and the Thm 1.3 iteration starts from d = 0 | read at source (p. 4) | ACCEPTED |
| Sanders 2020 Thm 1.1, Prop. 1.2, Props 7.1/8.1 | not read | NOT CHECKED |
| Sanders 2019 (𝔽₂ⁿ) Thm 1.1, Thm 2.5 | not read | NOT CHECKED |
| CHZZ (Discrete Analysis 2024), approximate spectral norm, connectivity needed | abstract only: confirms title, venue, "if and only if … connectivity condition"; sup-norm definition not seen | ACCEPTED as to existence/topic; definition NOT CHECKED |
| GOSSW Thm 3.4 translation | algebra re-derived: f̂(ξ)² = 4α²g, μ² = 4α²Σ_{∉Λ}g, s ≥ (1−o(1))/α ⇒ low/M ≲ α³/1600 ✓; source not read | translation ACCEPTED; source NOT CHECKED |
| Chang's lemma dimension ≪ a^{-1}log(1/α) | standard form, ✓ | ACCEPTED |
| Croot–Sisask Cor. 1.2 constant 9/ε² | not read; any bound (β/2)^{C/ε²}|G| with C/ε² > 2 is empty at β = N^{-1/2}, so the conclusion is constant-insensitive | conclusion ACCEPTED; constant NOT CHECKED |
| Hosseini–Lovett Ex. 1.1 arithmetic | |A| = 2·2ⁿ − 1 = 2|G|^{1/2} − 1 ✓ | ACCEPTED (source NOT CHECKED) |
| Carenini–Franchi arXiv:2605.07916 | abstract read: exists (8 May 2026), strengthening of Chang via cosetwise ℓ¹ | ACCEPTED |
| §3.2 density-loss heuristic | labelled "agent analysis" by the report; reasoning plausible | ACCEPTED as heuristic only |
| §4 energy: 𝓔(S)/|S|³ = αΣg² ≥ a − o(1) | re-derived ✓; BSG/Sanders Prop. 8.1 consequences not read | computation ACCEPTED; source consequences NOT CHECKED |
| §5 progression-shaped failure touches `cand:gp-sector-constancy` via (GP-Sub_κ), known only for c₀ > 1 | dual of ℤ/n ≅ Q: additive progressions ↦ geometric progressions ✓; "known only for c₀ > 1" inherited from R191/AUD191 | ACCEPTED (inherited part NOT re-checked) |
| Not retrieved: Méla 1982, Host–Méla–Parreau 1986 | stated honestly | — |

### 3.8 Call 2 summary

| claim | label |
|---|---|
| Verdict "refuted": no read source implies (SS\*) or (SS\*\*) | ACCEPTED (a literature search cannot prove absence; report says so) |
| Lemma 1 | ACCEPTED; "Reading" generalisation ACCEPTED WITH CORRECTION (level loss) |
| Lemma 2 | ACCEPTED |
| ‖1_S‖_A ≤ a^{-1/2} in the exact case (sharper than 1/a) | ACCEPTED |
| Prop. 3 (ε-form of the order window, composite N) | ACCEPTED WITH CORRECTION (use a single representation for (m + L²)η) |
| "M + 1/100 distinct subgroups" from GS Thm 1.3 | ACCEPTED (read at source) |
| Cor. 4: no exactly sharp set of size ~√(N/2), large prime N (via KS Thm 3) | ACCEPTED; KS not needed (GS suffices) |
| Gap = robustness, "Lemma 1 shows (SS) cannot supply more" | REJECTED as stated; ACCEPTED WITH CORRECTION as the (Clean_a) formulation |
| GOSSW, Chang, Croot–Sisask parameter failures | ACCEPTED as derivations; sources NOT CHECKED by me |
| (SS\*\*) not covered | ACCEPTED |
| `cand:gp-sector-constancy` touched only via progression-shaped failures | ACCEPTED |

---

## 4. Strategic assessment after Round 193

- Call 1 removes a risk without changing the plan: the three foundations of R187–R190 now have one more agent review each, with exact checks; nothing downstream needs reassessment. It does not move (A-slope): the 32/13 input is an obstruction bookkeeping item, used in no proof.
- Call 2 confirms (SS\*) is unsourced; Theorem E stays conditional. Per AUD192 §4, (SS\*) is a *status determiner* (it would decide (V) negatively on (NC)), not a proof obligation for the target. Its exact case is now source-backed; the robust case reduces (auditor sketch, §3.4) to (Clean_a), an internal question.
- The open proof obligations are unchanged: (A-slope) X = O(p) or M_√g = O(p) logarithm-free, behind two external geometric-progression problems (`cand:gp-shifted-energy` sharp form, open below 32/13 against target 2; `cand:gp-sector-constancy` for c₀ ≤ 1); (A-vertex) a genuinely signed estimate on the layers C²/p < |F|² < a, of target depth; Σg² ≫ √p open; cold line paused since R189.
- None of these has a call whose likely outcome would change the proof plan. The two external GP problems are recognised open problems in additive combinatorics; another literature sweep is unlikely to find a solution not already found in R190/R191.

---

## Verdict

- **Call 1 (`review-lemma-mprime-theorem-a`): SUPPORTED — ACCEPTED** (agent review, not human acceptance). Lemma M′/P′, Theorem A and the R190 MPRRS application are correct as stated; the MPRRS repair (|B| ≤ |A|^{20/13}M^{−33/13} ≤ M|A|² at the top; trivial E^×(A+α,B) ≤ |A||B|² ≤ M^{1/2}|A||B|^{3/2} for |B| < M) is right; 45/26 is correctly labelled a weakened obstruction, not a bound. One attribution correction (X(1_I) ≤ E^×(I−1) was already in R190). Independence of the re-derivation is self-reported and not verifiable.
- **Call 2 (`ordinary-ss-star-literature`): REFUTED in the mission's sense — ACCEPTED WITH CORRECTION.** No read source implies (SS\*) or (SS\*\*). New Lemmas 1–2, the a^{-1/2} bound and Corollary 4 are correct; Prop. 3 needs a single-representation fix; Corollary 4 already follows from Green–Sanders without Konyagin–Shkredov. The location of the gap is mis-stated: the missing hypothesis is sup-norm near-integrality of the Λ-truncation h ((Clean_a)), not an empty exceptional set for 1_S − h, and Lemma 1's examples satisfy (Clean_a).
- **Overall:** plan unchanged. Nothing in Round 193 bears on the original theta-limit target beyond confirming existing records. Finite checks (both scripts and mine) are evidence only.

## Recommendation

**Hold.** No call is needed to keep the record correct. If the coordinator wants activity, at most these two, in this order:

1. **`ordinary-a4-c1-dependence` (internal bookkeeping; cheap).** Question: in R151's (A4) bound t_B ≥ c₀(k, c₁, c₂) on (NC), how does c₀ behave as c₁ → 0 and c₂ → ∞ with k fixed? Decides whether Theorem E can use an ε-form of (SS\*) (as Prop. 3 and the (Clean_a) reduction give) instead of the fixed-c form.
   - If c₀ is bounded below uniformly, or decays slower than any ε(c₁) the ε-form allows: record that the ε-form of (SS\*) suffices for Theorem E.
   - If c₀ → 0 too fast: record that only the fixed-c form suffices; the exact-case source results do not feed Theorem E even in principle.
   - If inconclusive: record the exact dependence that is missing.
2. **`ordinary-ss-clean` (internal; only after 1 is favourable).** Question: for S ⊆ ℤ/N with |S| ~ √(N/2) sharp at level a, is sup_x d(h(x), ℤ) → 0 (or ≤ e^{−Ca^{-2}}) for the Λ-truncation h? A self-contained reduction must first be written out in full (the GS iteration from d₀ > 0).
   - If proved (with call 1 favourable): Theorem E becomes unconditional, (V) fails on (NC), and (A-vertex) needs a genuinely signed estimate on the low layers; hold the vertex route.
   - If a sharp sequence with sup d(h, ℤ) bounded below is found: the Green–Sanders route to (SS\*) is closed, (SS\*) itself is untouched; hold.
   - If inconclusive: hold.
   Neither call touches (A-slope) or the original target directly. They only settle the status of (V) on (NC).

No call is recommended on (A-slope), (A-vertex) or the cold line now: the first is behind two external GP problems, the second is of target depth, and the third has no new input since R189. A human read of Lemma M′, Theorem A and the R190 application remains the step that would turn the agent reviews into acceptance.

## Scripts

| script | SHA-256 | command | output (stdout SHA-256) |
|---|---|---|---|
| `research/paley-193-review-checks.py` (call 1) | `ef902621a215cdc25e5dedbcf924491ecdbb321a9335e4210efeb419de3ad5d1` | `python3 -B research/paley-193-review-checks.py` (0.8 s) | `Part M … 47 … OK` / `Part A … 40 laws … max … 14682836797/52744721152 (0.2784); 5354 chart entries in total` / `ALL EXACT CHECKS OK` (`3428b7a9039c6caa5fb2c709c1f27e063e6d60d0eb97050037836b338f8e4c64`) |
| `research/paley-193-ssstar-checks.py` (call 2) | `ac4d042abed532f530aa30fb94e2c07c50d4c8fe244c8ab9060a1882314facc3` | `python3 -B research/paley-193-ssstar-checks.py` (0.1 s) | table as in the report, `ALL OK` (`e1c399fed427d518d7cf7b3b70ad77a9bd2ca1cf2ef575abc4673a024487ac2d`, identical to the report) |
| `research/paley-193-audit-ssstar.py` (this audit; floating point, evidence only) | `17d26a9977ce98732de6c700c32394de7361167fb3f511ba4910bdec4906a86f` | `python3 -B research/paley-193-audit-ssstar.py` (0.1 s) | sup d(h, ℤ) = 0.000 / 0.033 / 0.033 / 0.033 (subgroup, +2, +5, +7 points; #exc = 0, 2, 5, 7), 0.100 (subgroup minus 3-coset), 0.001 / 0.126 (two cosets, +3 points), 0.498 (interval, not sharp); Lemma 1 bound holds in all four instances; `ALL OK` (`e5f23ce28cef59d1d5b363b0ef30b76008a58de3f60394bb0e73af281eccc73d`) |

Source extractions for this audit (own zlib-based reader, text not saved in the repository): Green–Sanders arXiv:math/0611286v2 (Theorem 1.2, Theorem 1.3, Lemma 3.1); Konyagin–Shkredov arXiv:1403.8129v1 (Theorems 2–3); MPRRS arXiv:1702.01003v5 (Lemma 33, Theorem 34, Theorem 37 and its proof). Abstracts only: arXiv:2605.07916, arXiv:2409.10634.
