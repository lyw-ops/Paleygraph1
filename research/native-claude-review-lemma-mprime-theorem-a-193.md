# Round 193 independent agent review: Lemma M′ / Proposition P′ (R187), Theorem A (R188), MPRRS Theorem 37 application (R190)

- **call_id:** `review-lemma-mprime-theorem-a`
- **Author:** Claude research session (Round 193), started by the Round 193 coordinator session. This is an agent review. It is not human acceptance and not a mathematical certification.
- **Mission:** `coordination/missions/round-193/review-lemma-mprime-theorem-a.md`, exported from `coordination/round-192.json` (SHA-256 `6237ed51…cbf`).
- **Files written:** this report and `research/paley-193-review-checks.py` (exact arithmetic). Nothing else was touched. Nothing was committed.

## Inputs (SHA-256 checked against the mission; all eight match)

| file | SHA-256 |
|---|---|
| `research/native-claude-ordinary-prime-level-pair-energy-187.md` | `5268631747d5ac3757ee328799f4e4205dd19afd5dc28184971a30255304e4b7` |
| `research/native-claude-ordinary-prime-beyond-point-plane-188.md` | `cee51251577d7d04c79a290c798dc3980a9153f494d9a87c320b68b9d0721919` |
| `research/native-claude-ordinary-gp-shifted-energy-literature-190.md` | `557777a493c1dcc5804540de7329c60a06217bbb6404c7713a3e11f230c53dd0` |
| `research/native-claude-audit-187.md` | `714513ca7c9be14aa397b2c8a5a6786345da9d58cb9170e4524d7c7c50d657ff` |
| `research/native-claude-audit-188.md` | `300664ba3a9dab8e5e699254578f304d1b9798b4cbf61c75ff70ab479a1e9894` |
| `research/native-claude-audit-190.md` | `6237bffb438242a90b78540f5aaf2cf158c049853a43f94713c37f7f6cc97b80` |
| `research/round-191-acceptance.json` | `51b868043d590e9d1453de4cdc7fea270a58c666c27c75927270ddf3a0449538` |
| `research/round-192-acceptance.json` | `25a7b70e92e6a4640c3d671af94cedbb1f0445934e55f763b9caa577b0cc1041` |

**Method.**
- I re-derived each step of the three source reports myself, and wrote my own exact check script, **before** opening the corresponding audit. The audits were read afterwards (§1.4, §2.4, §3.5), and only §§1–2 and the summary table of each.
- The external statements were read at source:
  - MPRRS: arXiv:1702.01003v5, margin stamp "arXiv:1702.01003v5 [math.CO] 19 May 2019";
  - Stevens–de Zeeuw: arXiv:1609.06284v4, stamp "18 Jul 2017".
  - The PDFs were fetched with WebFetch. Their text was extracted with my own zlib-based content-stream reader (no PDF library), so this is a third, independent extraction route; Round 190 used PyMuPDF and its audit used pypdf. The extracted text is not saved in the repository.
- Labels:
  - **proof** = ordinary argument, re-derived here;
  - **exact** = integer/`Fraction` computation;
  - **inherited** = an accepted earlier input that I did not re-derive.
- No floating-point diagnostic is used as evidence in this report.

**Notation.** Counting norms, p ≡ 1 (mod 4) prime, Q the squares, ν ≥ 0 a probability on \(\widehat Q\), \(f=\sum\nu_\eta\eta\) on Q, g = |f|², exactly as in Rounds 171–188. I keep every hypothesis and normalisation of the source reports.

---

## 1. Lemma M′ and Proposition P′ (Round 187)

### 1.1 Lemma C (chunked Stevens–de Zeeuw), the only external input

**Source check (SdZ Theorem 4, arXiv:1609.06284v4, read in my own extraction):**
> "Theorem 4. Let A, B ⊂ F be sets with |A| = a, |B| = b, a ≤ b and ab² ≤ n³. Let L be a finite set of lines of size n. If F has positive characteristic p, assume an ≪ p². Then I(A × B, L) ≪ a^{3/4} b^{1/2} n^{3/4} + n."

This matches Round 187's quote word for word. The proof in §2 of the paper begins by removing vertical lines ("they together contribute at most ab incidences"). A is the first coordinate and is the smaller set.

**Re-derivation of Lemma C (proof):**
1. **Orientation.** The coordinate swap \((x,z)\mapsto(z,x)\) sends the line Z = cX + d (c ≠ 0) to X = (Z − d)/c. That is again a line that is neither vertical nor horizontal. Distinct lines stay distinct. So s = |X| ≤ b = |Z| may be assumed. This is needed, because SdZ puts the smaller set first.
2. **Chunks.** Take n₀ = ⌊c₀p²/s⌋. Since s ≤ p, c₀p²/s ≥ c₀p ≥ 2 for large p, so n₀ ≥ c₀p²/(2s). Each chunk has s·n_j ≤ c₀p², which is SdZ's an ≪ p².
3. **Per chunk.** If sb² ≤ n_j³, SdZ applies. Otherwise each line is a graph over the first coordinate, so I_j ≤ sn_j. Also n_j < s^{1/3}b^{2/3} gives sn_j < s^{4/3}b^{2/3} ≤ b² (as s ≤ b), so sn_j ≤ s^{3/4}b^{1/2}n_j^{3/4}.
4. **Sum.** Hölder gives \(\sum n_j^{3/4}\le k^{1/4}n^{3/4}\), with k ≤ n/n₀ + 1 and k^{1/4} ≤ (n/n₀)^{1/4} + 1. Then \(s^{3/4}n_0^{-1/4}\le(2/c_0)^{1/4}s\,p^{-1/2}\).

**Verdict: correct.** The only hypothesis added is "p larger than an absolute constant", and the source states it.

### 1.2 Lemma M′, step by step (proof)

Hypotheses as in the source: A, R ⊆ F_p∖{0,1}, |A| = α, |R| = m, E = E^×(R) = m³/K, L₀ = ⌊log₂m⌋ + 1.
Note 1 ≤ K ≤ m, because m² ≤ E ≤ m³.

| step | claim | my check |
|---|---|---|
| 1 | some dyadic class F = {ρ ≤ r < 2ρ} has Σ_F r² ≥ E/L₀ | r takes values in [1, m], so there are at most L₀ classes (pigeonhole). ✓ |
| 1 | \(P=\sum_Fr\ge\sum_Fr^2/(2\rho)\ge E/(2\rho L_0)\); \(\vert F\vert\le E/\rho^2\) | r < 2ρ gives r² < 2ρr. ✓ |
| 1 | η = P/m² ≤ 1 and 1/η ≤ 2L₀K | P ≤ Σ_w r = m²; ρ ≤ m gives P ≥ E/(2mL₀) = m²/(2KL₀). ✓ |
| 1 | (2.1) \(\vert F\vert\le4L_0^2K\eta^2m\) | \(\vert F\vert\le E/\rho^2\) with ρ ≥ E/(2PL₀) gives \(\vert F\vert\le4P^2L_0^2/E=4\eta^2m^4L_0^2K/m^3\). ✓ |
| 2 | Σ_y d(y) = P and d ≤ min(m, \|F\|) | d(y) = #{y′ ∈ R : y/y′ ∈ F}, summed over y, counts the pairs behind Σ_F r. Also v ↦ vy is injective. ✓ |
| 2 | Σ_B d ≥ P/2, so \|B\| ≥ P/(2 min(m, \|F\|)) | The y ∉ B contribute < m·P/(2m). ✓ |
| 2 | \|B\|² ≥ P²/(4m\|F\|) ≥ m²/(16L₀²K) | Multiply the two lower bounds and use (2.1). ✓ |
| 2 | B depends only on R | F, d and B are functions of the quotient distribution of R (with a fixed tie-break among qualifying classes). ✓ |
| 3 | ℓ_{u,v}: Z = v(uX + 1 − u) are pairwise distinct, none vertical or horizontal | slope vu ≠ 0; slope + intercept = v recovers v, then u. ✓ |
| 3 | (x, vy) ∈ ℓ_{u,v} when 1 − y = u(1 − x); the map (u,v,x,y) ↦ (line, point) is injective | ux + 1 − u = y; y = (vy)/v. ✓ |
| 3 | I(A×F, 𝓛) ≥ h·t·P/(2m) = htηm/2 | Each u ∈ T_h has ≥ h pairs, each with y ∈ B, so d(y) ≥ P/(2m). ✓ |
| 4 | the threshold excludes the 2nd and 3rd SdZ terms | If (hη/2)·tm ≤ 3C₂·(term 2 or 3), the assumed hη/2 > 3C₂ max(1, s′b′^{1/2}p^{-1/2}) is contradicted (t ≥ 1; t = 0 is trivial). ✓ |
| 4 | tm ≤ 6⁴C₂⁴s′³b′²/(hη)⁴ and s′³b′² ≤ α²\|F\|²μ_* | s′ ≤ min(α, \|F\|) ≤ μ_*, since \|F\| ≤ 4L₀²Kη²m ≤ 4L₀²Km (η ≤ 1). ✓ |
| 4 | (2.2) t(h) ≤ C₄L₀⁴α²K²mμ_*/h⁴ | \|F\|²/η⁴ ≤ 16L₀⁴K²m²: **η cancels exactly** (η¹ in the incidence count, \|F\|^{1/2} ∝ η). ✓ |
| 4 | H_* ≤ 12C₂L₀ max(K, (αKmμ_*)^{1/2}p^{-1/2}) + 1 | s′b′^{1/2} = (α\|F\|)^{1/2}s′^{1/2} ≤ 2L₀η(αKmμ_*)^{1/2}; 1/η ≤ 2L₀K. ✓ |
| 5 | E(A;B) ≤ Hα\|B\| + (16/3)C₄L₀⁴α²K²mμ_*/H² | rows below H: Σm² ≤ HΣm = Hα\|B\|; dyadic shells above use (2.2) at 2ⁱH ≥ H_*. ✓ |
| 5 | the stated three terms | H₂ = L₀^{4/3}(αK²mμ_*/\|B\|)^{1/3} balances both pieces to L₀^{4/3}α^{4/3}\|B\|^{2/3}K^{2/3}m^{1/3}μ_*^{1/3}; H_*α\|B\| gives terms 2–3; α\|B\| ≤ Kα\|B\|. Form I follows from μ_* ≤ α. ✓ |

**Verdict: correct as stated.** Every quantifier matches the source: "there is B = B(R) … such that, for every such A". No size, doubling or characteristic condition is used beyond Lemma C. The constants C₂, C₃, C₄ are absolute.

**Exact check (Part M of `paley-193-review-checks.py`; my own code, not Round 187's).**
- Data: 40 random/structured (A, R) at p ∈ {13, …, 41} (random sets, geometric progressions, Q∖{1}, progression plus junk, subgroup cosets). The check runs over **every** qualifying popular class F, not only the first (47 pairs).
- It checks, exactly:
  - the pigeonhole step, \(\vert F\vert\rho^2\le E\), 2ρP ≥ Σ_F r², η ≤ 1, 1/η ≤ 2L₀K and (2.1);
  - Σd = P, d ≤ min(m, |F|), Σ_B d ≥ P/2 and 16L₀²m|B|² ≥ E;
  - line distinctness for all u ∈ F_p^×;
  - the incidence lower bound 2m·I(A×F, 𝓛) ≥ h·t·P against a brute-force incidence count, for **every** row threshold h.
- E^×(R) is checked against a brute-force product count.
- Output: `OK`.

### 1.3 Extraction and Proposition P′ (proof)

**Extraction.** U ⊆ S_t ⊆ Q∖{1} (supp g ⊆ Q, so 0 ∉ S_t; Lemma M′'s hypothesis R ⊆ F_p∖{0,1} holds).
- The remainders strictly decrease and the run ends with nothing left over.
- The pieces in the size class [M, 2M) are disjoint subsets of the first remainder of that class, so Σ|B| < 2M.
- There are at most log₂|U| + 1 components.

**Lemma S1** (inherited, Rounds 163/173/182; E^×(W) ≥ t²|W|⁴/(n max ν) for any W ⊆ {g ≥ t}, any size) gives
- K(R) ≤ C_cap√p/(t²m) ≤ K_M;
- min|B| ≥ M/(4L₀√K_M), using L₀(m) ≤ L₀(p).

**Prop. P′.**
- The triangle inequality for \(\|c_{\cdot,\cdot}\|_2\) over the disjoint pieces is legitimate, because \(1_{1-X_M}=\sum_B1_{1-B}\) and c is bilinear.
- Form I of Lemma M′ is applied with A = D (E is symmetric). Each term is nondecreasing in K and m, so K_M and 2M may be substituted.
- I recomputed the piece sums:
  - \(\sum|B|^{1/3}\le2M(\min|B|)^{-2/3}\le2(4L_0)^{2/3}M^{1/3}K_M^{1/3}\), constant \(2^{5/2}\le8\);
  - \(\sum|B|^{1/2}\le4L_0^{1/2}M^{1/2}K_M^{1/4}\), constants 4 and \(4\cdot2^{1/4}\le6\). ✓

**Exponents (proof; exact arithmetic by hand, consistent with the source table).** Put a = p^{-e}, M = p^{1/2−μ}, K_M ≍ p^{u}, u = 2e + μ, α < 2p^{1/2−μ_g}. The excesses over 2/3 are:
- T1: e_s/3 + μ_s/6 − e_g − 5μ_g/6 = (u_s − u_g)/6 − (2/3)(e_g + μ_g);
- T2: −1/6 + u_s/4 − u_g/2 = −5/24 − d/2 − w_s/4 + z/4;
- T3: −1/24 − (e_g + μ_g) − μ_s/4 = −w_g − w_s/4 − z/4.

Here d = u_g − u_s ≥ 0, w_i = e_i + μ_i ≥ −O(1/log p) and z = 1/6 − e_s ∈ [0, 1/6].

The constraints used are:
- μ_i ≥ −e_i − O(1/log p), because M ≤ |U| ≤ G/t ≤ 2C_cap p^{1/2+e};
- 0 ≤ e_s ≤ 1/6 + O(1/log p): heights in [cp^{-1/6}, 1] (e_s ≥ 0 is needed for z ≤ 1/6 in T2);
- u_s ≤ u_g, by choosing the structured side. Both sides are extraction components and E is symmetric, so this choice is legitimate.

So (3.1) holds: \(a_sa_gE(X_s;X_g)^{1/2}\ll(\log p)^{4/3}p^{2/3}\) for heights ≥ cp^{-1/6}.

**Verdict on P′: correct as stated**, with its hypotheses: (H1)/(H2) with the cap, Lemma S1, heights ≥ cp^{-1/6} on both sides, and the structured side chosen by smaller u.

**Downstream, also checked (proof).**
- Theorem 1: (log p)^{2+4/3}, squared, gives (log p)^{20/3}.
- Theorem 2:
  - light part: Minkowski \(\|c_{v,v'}\|_2\le\|v\|_2\|v'\|_1\) and the symmetric form, with \(\|h_<\|_2^2\le\tau_0G\);
  - heavy part: U_k ⊆ S_{a_k/2} covers {g ≥ τ₀}∖{1} pointwise, with z = 0 ↔ x = 1 excluded from h;
  - O(log⁴p) ordered pairs give \(E^\times(h)\ll p^{4/3}(\log p)^{32/3}\).

  These are correct. Corollaries 3–4 rest on inherited inputs (Round 185 Lemma 5, Round 182 Prop. 1(iv), the R178/R180/R184 chain), which I did not re-derive.

### 1.4 Comparison with `native-claude-audit-187.md` (read after §§1.1–1.3)

- The audit accepts Lemma C, Lemma M′, P′ and Theorems 1–2 with the same step list. On every step our derivations agree, including:
  - the η cancellation;
  - the H_* bound;
  - the excess identities;
  - the load-bearing constraints: without u_s ≤ u_g the T1 maximum is +5/36; at e = 1/5, T3 = +1/120.
- **The audit's wording correction is right.** Measured against |B| rather than m, the effective doubling is K^{5/4}. Indeed m^{1/3} ≤ (4L₀)^{1/3}K^{1/6}|B|^{1/3} turns term 1 into ≪ α^{5/3}|B|K^{5/6}, which is the Lemma-M shape with K′ = K^{5/4}. No exponent uses that phrase, so the correction suffices and nothing else needs repair.
- The audit replays Steps 1–3 at p ∈ [101, 409]. My Part M replays them at p ≤ 41 with an independent implementation, over all qualifying classes and all h. The two sets of checks are complementary.
- The audit's 𝔽_{r²} computation shows that term 3 is load-bearing. I agree on reading: Lemma C is the only place the characteristic enters.
- **No disagreement.**

---

## 2. Theorem A (Round 188)

Hypotheses as in the source:
- ν ≥ 0 a probability on \(\widehat Q\);
- the Round 171 chart μ(r,b) = g(Y)g(D) on Y ≠ D ∈ F_p∖{0,1}, with the mask b ∈ Q;
- F_μv(s) = Σμ(r,b)v((s−b)/r);
- h_t(e) = g(t/e) for e ≠ 0 and h_t(0) = 0;
- φ_t = h_t − G/p, π = F_μ|_{𝟏^⊥};
- the cap where stated.

### 2.1 The two hypotheses (proof)

- **ω ≥ 0.**
  - On Q, \(g=|\sum\nu_\eta\eta|^2=\sum_\zeta\lambda_\nu(\zeta)\zeta\) with λ_ν = ν∗ν̌ ≥ 0.
  - Since \(1_Q\zeta=\tfrac12(\tilde\zeta+\tilde\zeta\chi_2)\), both lifts of ζ carry ω = λ_ν(ζ)/2 ≥ 0.
  - Σω = (Σν)² = 1 = g(1).
- **(H3).** \(f(1/x)=\overline{f(x)}\) because ν is real, so g(1/x) = g(x). g real gives ω(ᾱ) = ω(α).

### 2.2 Lemma A1 (proof)

- The map u_x = (1 − x)/x is a bijection F_p∖{0,1} → F_p∖{0, −1}, and b = u_Y/u_D.
- Y ≠ D ⟺ b ≠ 1, and the mask is b ∈ Q.
- So, for b ∈ Q∖{1}, m′(b) = Σ_{v≠0} k(v)k(bv) with k(v) = g(1/(1+v)) and k(−1) := g(0) = 0.
- By (H3), k(v) = g(1 + v) = h(−v), so m′(b) = Σ_{z≠0} h(z)h(bz) = c_h(b).
- R183-A, inherited and also re-derived: with 1 − r = (1−Y)/(1−D) and Y, D ∈ Q on the support, b = (D/Y)(1−r) ∈ Q ⟺ 1 − r ∈ Q. So m(r) = c_h(1−r) on 1 − r ∈ Q∖{1}.
- Hence Λ₀ = X. **Correct.**

### 2.3 Lemma A2 and Theorem A (proof)

**Lemma A2.**
- χ((s−b)/r) = χ(s−b)χ̄(r), including s = b. So F_μχ = A∗χ with A_b = Σ_r μ(r,b)χ̄(r).
- Parseval gives ‖A∗χ‖² = p^{-1}Σ_ξ|Â(ξ)|²|χ̂(ξ)|², with χ̂(0) = 0 and |χ̂(ξ)|² = p for ξ ≠ 0 (Gauss sum, χ nontrivial). Hence ‖F_μχ‖² = pΣ_b|A_b|² − |m̂(χ)|².
- Expanding |A_b|² with r′ = λr gives S₀(χ) = Σ_λ χ(λ)Δ(λ,0).
- |A_b| ≤ m′(b) gives S₀ ≤ Λ₀. **Correct.**

**Theorem A.**
1. φ_t = Σ_α ω(α)α(t)ᾱ°. The trivial character has mean (p−1)/p, G = (p−1)ω(1), and 𝟏° = −(δ₀ − 1/p). F_μ fixes 𝟏^⊥ (Σ_s F_μv(s) = M₁Σv). This gives the splitting ‖F_μh_t‖² = M₁²G²/p + ‖F_μφ_t‖².
2. For α ≠ 1, ‖πᾱ‖² ≤ pS₀(ᾱ) by Lemma A2. For α = 1, ‖F_μ(δ₀ − 1/p)‖² = Λ₀ − M₁²/p ≤ pS₀(𝟏), since F_μδ₀ = m′.
3. **(i).** |α(t)| = 1, the triangle inequality and Jensen with weights ω ≥ 0, Σω = 1 give ‖πφ_t‖² ≤ pΣ_αω(α)S₀(ᾱ) = pΣ_λ g(1/λ)Δ(λ,0) = pT₀ (by (H3)). Then T₀ ≤ Σ_λ Δ(λ,0) = Λ₀ = X because 0 ≤ g ≤ 1. The bound holds for every t ∈ F_p^×.
4. **(ii).**
   - Orthogonality over t ∈ F_p^× gives (p−1)Σ_α ω(α)²‖πᾱ°‖².
   - Also c_g(λ) = (p−1)Σ_α ω(α)ω(ᾱ)ᾱ(λ) = (p−1)Σ_α ω(α)²ᾱ(λ), using ω(ᾱ) = ω(α).
   - So (p−1)Σω²S₀(ᾱ) = 𝒯, and the α = 1 bookkeeping gives ≤ p𝒯 − (p−1)²ω(1)²Λ₀ = p𝒯 − G²X.
   - Finally c_g ≤ c_g(1) = Γ_tot.
5. **Covariance.** The inputs are inherited: the Rounds 169/173/178/182 normalisation, the positive upper bound 0 ≤ H_α ≤ F_μh_t off s ∈ {0,1}, and the endpoints priced at O(p^{5/2}). Dropping s ∈ {0,1, t} only enlarges the sum. Then:
   - the uniform branch sums w(t)·pT₀;
   - the averaged branch uses w ≤ 1/4;
   - the mean term is WM₁²G²/p ≤ G⁷/p ≪ p^{5/2} under the cap.

   Dividing by p gives covariance ≪ p^{3/2} + min(WT₀, 𝒯/4) ≤ p^{3/2} + min(W, Γ_tot/4)X.

**An exact identity behind (ii)** (proof; new here, a slight sharpening):
\[
\sum_{t\in\mathbb F_p^\times}\|\pi\varphi_t\|^2\;=\;p\,\mathcal T-G^2\Lambda_0-\sum_{\lambda}c_g(\lambda)C(\lambda)+\frac{G^2M_1^2}{p},
\]
with C(λ) = Σ_r m(r)m(λr).

It follows from the exact Lemma A2 identity, and from (p−1)Σ_α ω(α)²|m̂(ᾱ)|² = Σ_λ c_g(λ)C(λ). The last two terms together equal −(p−1)Σ_{α≠1}ω²|m̂(ᾱ)|² − G²M₁²/(p(p−1)) ≤ 0. So the slack dropped in (ii) is a sum of nonnegative terms, and (ii) is exactly this identity with those terms dropped.

**Corollary A arithmetic (exact, by hand).**
- W ≤ G ≪ √p and X ≪ p^{4/3+o(1)} give 11/6; 11/6 − 43/24 = 1/24.
- X = O(p^{1+ε}) gives 3/2 + ε. The thresholds are ε < 1/4 (7/4), ε < 7/24 (43/24) and ε < 2/7 (against 7/4 + ε/8).

**Verdict: Theorem A is correct as stated.** Its hypotheses: ω ≥ 0 (for (i)), (H3) (for A1 and (i)), g real (for (ii)), the inherited chart, completion and covariance normalisation, and the cap for the mean term.

### 2.4 Exact check (Part A of `paley-193-review-checks.py`)

**Laws.** Rational test laws with ω ≥ 0 exactly: f = Σ_i c_i 1_{K_i}, with K_i subgroups of Q (order ≥ 3) and c_i ≥ 0 rational, Σc_i = 1. Then f = Σ_η ν_η η with ν = Σ c_i · uniform(annihilator of K_i) ≥ 0 a probability, and g = f² is rational with (H3). There are 24 such laws at p ∈ {13, 17, 29, 37, 41, 53, 61, 73}. Another 16 random rational (H3)-symmetric laws on Q (ω not controlled) are used for the identities only. In all, 5 354 chart entries.

**Verified exactly** (integers, scaled by powers of the common denominator):
- chart injectivity;
- Lemma A1 (m′ = c_h on Q∖{1}, 0 elsewhere) and R183-A (m = c_h(1−·));
- Λ₀ = X and Σ_λ Δ(λ,0) = Λ₀;
- the splitting ‖F_μh_t‖² = M₁²G²/p + ‖F_μφ_t‖², for every t;
- **Theorem A (i)**, ‖πφ_t‖² ≤ pT₀ for every t, on every ω ≥ 0 law; the largest ratio is 0.2784;
- T₀ ≤ X;
- the exact identity above;
- (ii) ≤ p𝒯 − G²X, and 𝒯 ≤ Γ_tot X.

Output: `OK`.

**Limits of the check.** These laws are multiplicatively structured. They test the identities and the inequality (i) exactly, not any exponent.

### 2.5 Comparison with `native-claude-audit-188.md` (read after §§2.1–2.4)

- The audit accepts A1, A2, Theorem A and Cor. A with the same derivations, including the one-line proof of (H3) and the α = 1 term. **No disagreement on the mathematics.**
- **Its corrections, and whether they suffice:**
  - (i) "X = O(p) is one sufficient route among several, not *the* obligation". Correct; it concerns wording only.
  - (ii) BPP's W = Σ_t w(t) ≤ G is not Round 184's max_ξ W_ξ. Correct, and important for anyone reading "min(W, Γ_tot/4)X". With max_ξ W_ξ ≍ p, the bound would be off by √p.
  - (iii) Cor. A's "any g with the cap" needs (H3) for A1, and ω ≥ 0 for branch (i). Correct. In my derivation, (ii) needs only g real and the chart; the reduction 𝒯 ≤ Γ_tot X, by contrast, uses Λ₀ = X and hence (H3).
  - (iv) An evidence row that does not reproduce is a floating issue, outside this review.

  All four corrections suffice. None touches the theorem.
- The audit's Theorem A checks were in double precision (plus exact integer checks of A1 and Prop. B). My Part A adds an **exact** check of (i), of (ii) and of the full t-sum identity on genuine ω ≥ 0 laws.

---

## 3. Round 190: application of MPRRS Theorem 37

### 3.1 The statement at source

From my own extraction of arXiv:1702.01003v5, printed page 45 (verbatim up to the extraction of symbols):
> "Theorem 37. Suppose A ⊂ F such that |AA| = M|A| and |A| ≤ p^{13/23} M^{10/23}. Then for any α ∈ F^* one has E^×(A + α) ≲ M^{33/13} |A|^{32/13}. Note that 32/13 = 5/2 − 1/26, so for M sufficiently small, this improves the bound E^×(A) ≪ M^{3/2}|A|^{5/2} provided by Lemma 33."

This matches Round 190's quote. I also read, on the same pages:
- **Lemma 32** (p. 41): "Let A ⊂ F and let α ∈ F^*. Suppose |AA| ≤ p^{2/3}. Then E^×_3(A + α) ≪ |AA|^5 log|A| / |A|^2."
- **Lemma 33** (p. 42): "Let A, B ⊂ F such that |A||AA||B| ≤ p² and also max(|AA|, |B|) ≤ (|A||AA||B|)^{1/2}. Then for any α ∈ F^*, E^×(A + α, B) ≪ |AA|^{3/2}|B|^{3/2}/|A|^{1/2}."
- **Theorem 34** (p. 43): "Let A be a finite subset of an abelian group G. Suppose there are parameters D1 and D2 such that E_3(A) ≤ D1|A|³ and for any finite set B ⊂ G E(A, B) ≤ D2|A||B|^{3/2}. Then E(A) ≪ D1^{6/13} D2^{2/13} |A|^{32/13} log^{12/13}|A|." The paper adds that the E(A,B) bound is needed only for |B| ≤ 4|A|⁴/E(A).
- **The proof of Theorem 37** (p. 45) takes D2 = M^{3/2} from Lemma 33 "whenever M|A|²|B| ≤ p²". It uses |B| ≤ 4|A|⁴/E^×(A+α) and the reduction to E^×(A+α) ≥ 4M^{33/13}|A|^{32/13} to get |B| ≤ |A|^{20/13}M^{−33/13} (the sign of the M exponent is lost in extraction; it is forced by the algebra). Then M|A|²|B| ≤ p² ⟸ |A|^{46/13}M^{−20/13} ≤ p², i.e. |A| ≤ p^{13/23}M^{10/23}. It takes D1 = M⁵ log|A| from Lemma 32 "whenever |A| < p^{2/3}/M", and applies Theorem 34 in G = F^*.

### 3.2 Hypotheses against the sets it is applied to (proof)

Round 190 applies it as follows: I = {γ^{2k} : |k| ≤ K} ⊂ Q, N = |I| ≍ √p, α = −1, A = I′ = I∖{1}.

| hypothesis / proof condition | at A = I′, α = −1 | status |
|---|---|---|
| A + α ⊂ F^* (Theorem 34 in G = F^*) | 0 ∉ I′ − 1 since 1 ∉ I′ | ✓ (this is why 1 is removed) |
| \|AA\| = M\|A\| with M = O(1) | I′I′ ⊆ II ⊆ {γ^{2j}: \|j\| ≤ 2K}, so M ≤ (2N−1)/(N−1). If ord γ² ≤ 4K, \|II\| ≤ ord γ² and the bound still holds | ✓ M ≤ 2 + O(1/N) |
| \|A\| ≤ p^{13/23}M^{10/23} | M ≥ 1 and N ≍ √p ≤ p^{13/23} for large p (13/23 > 1/2) | ✓ |
| Lemma 32: \|AA\| ≤ p^{2/3} (proof: \|A\| < p^{2/3}/M) | \|AA\| ≤ 2N ≪ √p | ✓ |
| Lemma 33, first condition M\|A\|²\|B\| ≤ p² | derived from the size hypothesis (above) | ✓ |
| Lemma 33, second condition max(\|AA\|, \|B\|) ≤ (\|A\|\|AA\|\|B\|)^{1/2}, i.e. M ≤ \|B\| ≤ M\|A\|² | **not addressed in the printed proof.** Upper end: \|B\| ≤ \|A\|^{20/13} ≤ M\|A\|². Lower end (\|B\| < M): E^×(A+α, B) ≤ \|A\|\|B\|² ≤ M^{1/2}\|A\|\|B\|^{3/2}, so D₂ = M^{3/2} still works | ✓ **after a one-line repair** (found independently here; the same repair is in the Round 190 audit) |
| ≲ | (log)^C; here (log\|A\|)^{18/13} from log^{12/13} and D₁^{6/13} | ✓ p^{o(1)} |

**Output.** E^×(I′ − 1) ≪ N^{32/13}(log N)^{18/13} = p^{16/13+o(1)}, since 32/13 · 1/2 = 16/13 and 16/13 = 5/4 − 1/52.

**Transfer to the masked quantity.** Put g = 1_I and h(z) = g(1 − z) on z ≠ 0. Then X(1_I) = Σ_{κ∈Q∖{1}} c_h(κ)² ≤ Σ_κ c_h(κ)² = E^×((1 − I)∖{0}) = E^×(1 − I′) = E^×(I′ − 1). The last step holds because negating all four coordinates preserves x₁x₂ = x₃x₄. So X(1_I) ≲ N^{32/13} directly. The O(N²) step in Round 190 §1.1 is correct but not needed. The definitions of E^×(A, B) in MPRRS (pp. 10–11, per the Round 190 audit) and in the project (quadruples / quotient counts) give the same number.

**Not re-verified:**
- the proof of Theorem 34 (Shkredov 2013, not read here, nor by Round 190 or its audit);
- MPRRS Theorem 11 (collinear quadruples, used in Lemma 32);
- the proof of Lemma 33.

These are refereed published results (Mathematika 65 (2019)). Only their hypotheses were checked against the sets they are applied to.

### 3.3 The "p^{16/13} obstruction level and one-match 45/26" (proof of the arithmetic, reading of the logic)

- **Arithmetic:**
  - 5/2 − 2δ = 32/13 ⟺ δ = 1/52;
  - p^{5/4−1/52} = p^{64/52} = p^{16/13};
  - covariance exponent = 1/2 + T₀ exponent (Theorem A's uniform branch with W ≤ G ≍ √p), so 1/2 + 16/13 = 45/26 = 7/4 − 1/52.

  All are exact.
- **Logic.** Round 189 Cor. 3.1 (inherited, not re-derived here, including its transfer constant (4/π²)⁵) says that a uniform admissible-only bound T₀ ≤ p^{5/4−δ} would yield X(1_I) ≪ |I|^{5/2−2δ}. Theorem 37 makes that conclusion a known theorem for δ ≤ 1/52. So the sector family no longer obstructs between 7/4 and 45/26, and it still obstructs below 45/26 (at T₀ ≤ p^{16/13−δ′}, beyond the published bound).
  - **This is a weakening of an obstruction, not an upper bound on T₀, X or the covariance for any law.** Round 190 says so ("a re-statement of the Round 189 cap … not a new cap theorem"), and that reading is the correct one.
  - Nothing in Theorem 37 shows that an admissible-only argument actually reaches any exponent in [45/26, 7/4).
- **One inaccuracy in Round 190 §5.** It mentions "the Round 187 height-1 pricing pieces where Lemma 33 was used". Round 187 states (line 72) that MPRRS Lemma 33 is **not** used. Moreover, Theorem 37 bounds only E^×(A + α), not the mixed E^×(A + α, B) that a height-1 pair price would need. This sentence does not affect the Round 190 result.

### 3.4 Verdict on item 3

**Correct with a stated repair.**
- Theorem 37 is quoted exactly.
- Its hypotheses hold for A = I∖{1}, α = −1, N ≍ √p.
- The printed proof omits the second condition of Lemma 33. The one-line repair in §3.2 closes that gap.
- The output E^×(I − 1), X(1_I) ≲ |I|^{32/13} = p^{16/13+o(1)} and the 45/26 arithmetic are right.
- The 45/26 statement is correct only in the weak "obstruction moves" sense described in §3.3.

### 3.5 Comparison with `native-claude-audit-190.md` (read after §§3.1–3.4)

- The audit read Theorem 37 at source (pypdf) and gives the same verbatim text.
- It finds the same gap in Lemma 33's second condition, with the same repair; the repair suffices.
- It gives the same log power (18/13) and the same weak reading of 45/26.
- It flags the same §5 inaccuracy, about the Round 187 height-1 pieces and the mixed energy.
- **No disagreement.** My extraction is a third independent reading of the same PDF page. I additionally note the direct inequality X(1_I) ≤ E^×(I′ − 1), which needs no O(N²) step.

---

## 4. Downstream dependence (for the coordinator)

No step failed, so no downstream statement needs reassessment on account of this review. For the record:
- Rounds 188–192 use these results as follows:
  - Round 188 Theorem A uses Round 187 Cor. 4 (X ≪ p^{4/3+o(1)}) only for its unconditional 11/6 and conditional readings. Theorem A itself does not depend on Lemma M′.
  - Rounds 189–191 use Theorem A (T₀ and X as one-match quantities). Round 191 calls the remaining obligation "(A-slope) behind cand:gp-shifted-energy / cand:gp-sector-constancy".
  - The cand:gp-shifted-energy status "known at |I|^{32/13}" rests on §3.
- **Inherited, not re-derived:**
  - Lemma S1;
  - Round 185 Lemma 5;
  - Round 182 Prop. 1(iv) and the R178/R180/R184 chain;
  - R183-A (re-derived in §2.2 and checked exactly);
  - the Round 169/173/178/182 covariance normalisation and positive completion;
  - Round 189 Cor. 3.1 and its (4/π²)⁵ transfer;
  - Theorem 34, Theorem 11 and Lemma 33 of MPRRS (proofs).

  A failure in any of these would propagate to the corresponding conclusion. This review does not cover them.

## 5. What this changes

- **Supported:** the three results can be recorded as independently agent-reviewed. The plan is unchanged.
- **Corrections to carry, all already in the audits, with no effect on the statements:**
  - "effective doubling K^{5/4} against |B|" (R187);
  - the W ≠ max_ξ W_ξ notation, (H3) in Cor. A, and "one sufficient route" (R188);
  - the Lemma 33 second-condition repair, the weak reading of 45/26, and the §5 Lemma 33/height-1 sentence (R190).
- **Small additions here:**
  - the exact t-sum identity in §2.3 (the slack in Theorem A (ii) is Σ c_gC − G²M₁²/p ≥ 0);
  - exact rational checks of Theorem A (i)/(ii) on genuine ω ≥ 0 laws;
  - an independent exact replay of Lemma M′ Steps 1–3 over every qualifying popular class;
  - X(1_I) ≤ E^×(I′ − 1) directly.
- **What would settle the remaining items:**
  - a human read of these proofs;
  - if wanted, a source check of Shkredov 2013 (Theorem 34) and MPRRS Theorem 11, which no agent has read.
- **This review proves nothing about the original theta-limit target.** The finite checks test identities and inequalities at small p. They do not test any exponent.

## Verdict

| item | verdict | first failing step | repair needed |
|---|---|---|---|
| 1. Lemma M′ and Proposition P′ (R187), with Lemma C; Theorems 1–2 checked as consequences | **Supported**: correct as stated | none | none (audit wording correction "K^{5/4} against \|B\|" is cosmetic) |
| 2. Theorem A (R188), with Lemmas A1–A2, every t ∈ F_p^× | **Supported**: correct as stated | none | none (audit corrections are scope/notation: (H3) in Cor. A; W = Σ_t w(t) ≠ max_ξ W_ξ) |
| 3. R190 application of MPRRS Thm 37: E^×(I−1) ≲ \|I\|^{32/13} = p^{16/13+o(1)}, 45/26 | **Supported**: correct with a stated repair | none in the application; the printed proof of Thm 37 omits Lemma 33's second condition | one line: \|B\| ≤ \|A\|^{20/13} ≤ M\|A\|² at the top end; trivial bound for \|B\| < M. The 45/26 is a weakened obstruction, not a bound |
| **Overall** | **Supported** (agent review; not human acceptance) | — | proofs of MPRRS Thm 34/Thm 11/Lemma 33 and the inherited project inputs listed in §4 were not re-verified |

**Scripts.**

| script | SHA-256 | command | output |
|---|---|---|---|
| `research/paley-193-review-checks.py` | `ef902621a215cdc25e5dedbcf924491ecdbb321a9335e4210efeb419de3ad5d1` | `python3 -B research/paley-193-review-checks.py` (Python 3.14, standard library only, < 1 s) | `Part M: Lemma M' Steps 1-3 exact on 47 (case, popular class) pairs: OK` / `Part A: Theorem A exact on 40 laws (p = 13..73): A1, R183-A, splitting, (i) on omega>=0 laws, (ii) identity and bounds: OK; max_t \|\|pi phi_t\|\|^2/(p T0) = 14682836797/52744721152 (0.2784); 5354 chart entries in total` / `ALL EXACT CHECKS OK` |
