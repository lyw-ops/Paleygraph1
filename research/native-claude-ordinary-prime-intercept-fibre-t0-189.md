# Round 189 native Claude draft: the intercept fibre T₀ (coupled triangle pricing)

- **call_id:** `ordinary-prime-intercept-fibre-t0`
- **Author:** Claude subagent started by the Round 189 coordinator (session/r189-t0). This is an agent assessment. It is not an audit, not human acceptance and not a mathematical certification.
- **Mission:** `coordination/missions/round-189/ordinary-prime-intercept-fibre-t0.md`, exported from `coordination/round-188.json` (record SHA-256 `2c6221ec…0492c` as printed in the export).
- **Inputs read.** All eight SHA-256 values listed in the mission match:
  - `research/round-187-acceptance.json` (`edc1d3eb…1d9`) and `research/round-188-acceptance.json` (`e0face6c…dcc6`): `proof_scope`, `failed_paths_and_open_bounds`, `main_ranked_closeout`, `target_status`;
  - `research/native-claude-audit-188.md` (`300664ba…9894`): in full, §2 and §5 line by line;
  - `research/native-claude-ordinary-prime-beyond-point-plane-188.md` (`cee51251…1919`): in full;
  - `research/native-claude-ordinary-prime-level-pair-energy-187.md` (`52686317…b7`): in full;
  - `research/ordinary-mixed-row-autocorrelation-180.md` (`357f5058…85aa`): in full;
  - `research/paley-188-bpp-exponents.py` (`1651c7fc…5740`) and `research/paley-188-audit-bpp-check.py` (`d2ee413c…e403b`): hashes checked, not replayed.

  Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-188.md`. For the external quotes I also read §6.3 of `research/native-claude-ordinary-prime-sup-c-heavy-price-186.md`.
- **Scripts (all new):**
  - `research/paley-189-t0-exact.py`: exact integer checks of every identity in §§1–3 at p ≤ 109. It also runs one floating check of the interval-law inequality at p ≤ 257.
  - `research/paley-189-t0-models.py`: floating-point models at p ≤ 6421 (evidence only).
  - `research/paley-189-t0-exponents.py`: exact `Fraction` arithmetic for every exponent in this report.
- **Nothing was committed.** I wrote only this file and the three scripts.

## Result summary

**Verdict: refuted, as a method cap with the scope stated in §6.** No bound T₀ − c ≤ p^{4/3−δ} is proved. The unconditional one-match exponent stays **43/24**. The findings:

1. **Exact κ-form (Proposition 1, proved).** With ψ(x) = g(1+x):
   \[
   T_0=\sum_{\kappa}\sum_{\varepsilon=\pm1}c_\varepsilon(\kappa)A_\varepsilon(\kappa)-Z,\qquad X=\sum_{\beta\in Q\setminus\{1\}}c(\beta)^2 .
   \]
   - c_ε(κ) is the shifted multiplicative correlation of ψ restricted to the quadratic class ε.
   - A_ε(κ) is the same correlation with the triangle weight inserted.
   - Z ≥ 0.

   So T₀ is the X-pairing with one factor replaced by its triangle-weighted version.
2. **Three-pencil lemma (Lemma 2, proved; uses (H3) and p ≡ 1 mod 4).** A multiplicative triangle (s, σ, σs) of g lies on three pencil lines through (1,1), with slopes κ, 1−κ and 1−1/κ. Hence
   \[
   A_\varepsilon(\kappa)\le\min\{c_\varepsilon(\kappa),\ c_\varepsilon(1-\kappa),\ c_{\chi(\kappa)\varepsilon}(1-1/\kappa)\},
   \]
   \[
   T_0-c\ \le\ \sum_{\kappa\ne1}\sum_\varepsilon c_\varepsilon(\kappa)\min\{c_\varepsilon(\kappa),c_\varepsilon(1-\kappa),c_{\chi(\kappa)\varepsilon}(1-1/\kappa)\}.
   \]
   This is the coupling between g(Y′/Y) and the shifted correlation in closed form. Equality holds throughout for subgroup laws, which then have an exactly anharmonic-invariant correlation, c_ε(κ) = c_ε(1−κ) = c_{χ(κ)ε}(1−1/κ).
3. **Transfer (Proposition 3, proved).**
   - (a) For every subgroup law g = 1_H, H ≤ Q, T₀ = X exactly. Such a law is admissible with the cap when |H| ≤ C√p.
   - (b) If g ≥ τ′ on a set I = I⁻¹ and g ≥ τ on I·I⁻¹, then T₀(g) ≥ ττ′⁴ X(1_I).
   - (c) The interval law (ν flat on an interval of characters, which is admissible) has g ≥ 4/π² on I·I⁻¹ for a symmetric geometric progression I ⊂ Q with |I| ≍ √p. So T₀(g_J) ≥ (4/π²)⁵ X(1_I).
   - Consequence: the triangle weight saves at most a constant factor on admissible sector-type laws. A uniform bound T₀ ≤ p^{5/4−δ} would bound the masked multiplicative energy of shifted geometric progressions of length ≍ √p by |I|^{5/2−2δ}. That is below the exponent 5/2 of the only bound I know for this case (MPRRS Lemma 33, quoted second-hand, §3).
   - The F_{r²} control is the case H = F_r^×. There T₀ = X ≍ q^{3/2}, so any saving must come from a prime-specific input inside X itself.
4. **Method caps for the 43/24 threshold (§4, method statements).** Every pricing of T₀ − c I could build from the coupled form and the current inputs lands at or above p^{31/24}:
   - the **half-structured Cauchy–Schwarz** \(T_0-c\le(\sum_{\kappa\ne1}A^2)^{1/2}X^{1/2}\), with the structured side priced at N^{5/2} = p^{5/4} (MPRRS) and X at p^{4/3}, gives exactly **31/24**, i.e. covariance exactly 43/24. By the transfer, beating it needs the same geometric-progression energy improvement;
   - the anharmonic cross sum \(\sum c(\kappa)c(1-\kappa)\): it is not a pencil, but Stevens–de Zeeuw gives p^{11/8} and even Szemerédi–Trotter strength gives p^{4/3};
   - pointwise pricing of Δ(λ, 0) as a sum over ≤ N pencil slopes: d = 7/8 with Stevens–de Zeeuw / Lemma M′ rich-slope counts, and d = 5/6 even at Szemerédi–Trotter strength. The 43/24 threshold needs d < 3/4. Cauchy–Schwarz reaches d = 3/4 only at the floor X ≍ p;
   - light-triangle splitting gives back the auditor's \((G X D_0^*)^{1/2}\) (thresholds d < 2/3 and d < 3/4);
   - the Plancherel form has floor p^{5/4}.
5. **One reduction that does hold (Proposition 5, proved).** The part of T₀ with a light triangle weight g(Y′/Y) < p^{−θ} is at most p^{−θ}X. So beating 43/24 only needs the **heavy-triangle part**, which comes from λ in the level set {g ≥ p^{−1/24−δ}} of size ≤ G·p^{1/24+δ}.
6. **Evidence (floating, models, p ≤ 6421).**
   - (T₀ − c)/(X − c) is exactly 1 for subgroup laws, ≈ 0.47–0.55 for the interval law and ≈ 0.71 for the geometric-progression control. It decays like p^{−1/2} only for random laws.
   - The anharmonic cross sum is ≈ 1.0–1.35 X: no anti-correlation between c(κ) and c(1−κ).
   - max_{λ≠1} Δ(λ, 0)/√p is 0.01–1.6, with no visible growth.

**X and Γ₂, stated separately:** no new bound on X, \(\mathcal M_w\), Γ₂ or Γ_tot is proved. The transfer shows that the T₀ route below 7/4 carries the sector (geometric-progression) case of the X problem; this is a touch on `cand:slope-row-mass-x` in use, not in value (see "Shared estimates").

## Setup and hypotheses

Notation is that of Rounds 168–188 (Round 188 BPP setup), with counting norms.

- p ≡ 1 (mod 4) prime, n = (p−1)/2, Q the squares, χ the Legendre symbol. Note χ(−1) = 1.
- ν ≥ 0 is a probability on \(\widehat Q\), f = Σ ν_η η on Q (zero off Q), and g = |f|². Hence:
  - ω ≥ 0;
  - (H3) g(1/x) = g(x);
  - g(1) = 1 and 0 ≤ g ≤ 1;
  - the cap G = Σ g ≤ n max ν ≤ C_cap √p.
- **Chart (Round 171).** μ(r, b) = g(Y)g(D) on Y ≠ D in F_p∖{0,1}, with r = (Y−D)/(1−D) = (1−b)Y, b = u_Y/u_D (u_x = (1−x)/x), and the mask b ∈ Q.
  - Δ(λ, 0) = Σ_{r,b} μ(r,b)μ(λr,b), T₀ = Σ_λ g(λ)Δ(λ,0), X = Σ_r m(r)² = Λ₀ (Lemma A1), c = Σ μ².
  - D₀* = max_{λ≠1} Δ(λ, 0).
- **Shifted objects.**
  - ψ(x) = g(1+x) for x ≠ 0, and ψ(0) = 0. So supp ψ ⊆ P := {x ≠ 0 : 1+x ∈ Q}.
  - For ε = ±1: c_ε(κ) = Σ_{χ(z)=ε} ψ(z)ψ(κz), and c = c₊ + c₋.
  - A_ε(κ) = Σ_{χ(x)=ε} ψ(x)ψ(κx) g((1+κx)/(1+x)).
  - Z = Σ_{x,x′} ψ(x)²ψ(x′)² g((1+x)/(1+x′)) ≥ 0.
- **Accepted inputs used:**
  - Round 188 Theorem A: covariance ≪ p^{3/2} + min(W T₀, 𝒯/4), W ≤ G;
  - Round 188 Lemma A1 and Proposition B;
  - Round 187 Theorem 2 / Corollary 4: X ≤ E^×(h) ≪ p^{4/3}(log p)^{32/3};
  - Round 187 Lemma C and Lemma M′: used only in §4 method statements.
- **External statements, used only in method statements, never in a proof of a bound:**
  - Stevens–de Zeeuw Theorem 4 (arXiv:1609.06284), as quoted verbatim in Round 187 (accepted).
  - MPRRS Lemma 33 (arXiv:1702.01003v5), as quoted verbatim in Round 186 §6.3: "Let A, B ⊂ F such that |A||AA||B| ≤ p² and also max(|AA|, |B|) ≤ (|A||AA||B|)^{1/2}. Then for any α ∈ F^*, E^×(A + α, B) ≪ |AA|^{3/2}|B|^{3/2}/|A|^{1/2}."
  - **I did not re-read Lemma 33 at source.** The arXiv PDF fetched in this session could not be converted to text with the tools available. Its hypotheses at the scale used are checked in `paley-189-t0-exponents.py`: |A| ≍ |AA| ≍ |B| ≍ √p gives |A||AA||B| ≍ p^{3/2} ≤ p², and max ≤ (·)^{1/2}.
  - Macourt–Shkredov–Shparlinski (subgroups) is mentioned only as Round 186 reported it, not re-read.
- **No near-critical (NC) input is used anywhere.**

## 1. The κ-form of T₀ (Proposition 1; proved)

**Proposition 1.** For any weight g on F_p^× with (H3), supported on Q, and g(0) = 0:
- (i) \(T_0=\sum_{\kappa\in\mathbb F_p^\times}\sum_{\varepsilon}c_\varepsilon(\kappa)A_\varepsilon(\kappa)-Z\);
- (ii) \(c=\sum_\varepsilon c_\varepsilon(1)^2-\sum_x\psi(x)^4\);
- (iii) \(X=\sum_{\beta\in Q\setminus\{1\}}c(\beta)^2\).

Consequently, when g(1) = 1, \(T_0-c\le\sum_{\kappa\ne1}\sum_\varepsilon c_\varepsilon(\kappa)A_\varepsilon(\kappa)\).

*Proof.*
1. Two maps with the same intercept b have slope ratio Y′/Y, because r = (1−b)Y. So
   \[T_0=\sum_{b}\sum_{Y,Y'}v_b(Y)v_b(Y')g(Y'/Y),\qquad v_b(Y)=g(Y)g(D_b(Y)).\]
2. Change variables to x = u_Y ∈ F_p∖{0, −1}, so Y = 1/(1+x). By (H3), g(Y) = g(1+x) = ψ(x). Also u_D = x/b, so g(D) = ψ(x/b).
3. Put β = 1/b ∈ Q∖{1}. Then
   \[T_0=\sum_{x,x'}\psi(x)\psi(x')g\Big(\frac{1+x'}{1+x}\Big)\sum_{\beta\in Q\setminus\{1\}}\psi(\beta x)\psi(\beta x').\]
4. Here g(Y′/Y) = g((1+x)/(1+x′)) = g((1+x′)/(1+x)) by (H3).
5. With κ = x′/x and z = βx, the inner sum runs over z ∈ xQ, z ≠ x. It equals \(c_{\chi(x)}(\kappa)-\psi(x)\psi(x')\).
6. Group by κ and by the class of x. This gives (i), and the subtracted terms are Z.
7. The κ = 1 term is \(c_\varepsilon(1)A_\varepsilon(1)=c_\varepsilon(1)^2\), since g(1) = 1. Together with the diagonal part of Z, it is (ii) (c = Σ_b Σ_Y v_b(Y)²).
8. (iii) is Lemma A1 with m′(b) = Σ_x ψ(x)ψ(x/b) = c(1/b) and c(1/β) = c(β). ∎

*Exact check:* `paley-189-t0-exact.py` Part 1. The chart definition of T₀, c and X agrees with (i)–(iii) for 15 random inversion-symmetric integer weights at p = 13, 17, 29, 37, 41.

## 2. The three-pencil lemma (Lemma 2; proved)

**Lemma 2.** Assume (H3), supp g ⊆ Q, p ≡ 1 (mod 4). Fix κ ∉ {0, 1}. For x with ψ(x)ψ(κx) ≠ 0, put s = 1+x, u = 1+κx and σ = u/s, all in Q. Then the three pairs

| pair | both entries in supp ψ (weights) | slope | class |
|---|---|---|---|
| (x, κx) = (s−1, u−1) | ψ(x) = g(s), ψ(κx) = g(u) | κ | χ(x) |
| (z, (1−κ)z), z = 1/s − 1 = −x/(1+x) | ψ(z) = g(s), ψ((1−κ)z) = g(σ) | 1−κ | χ(z) = χ(x) |
| (w, (1−1/κ)w), w = 1/u − 1 = −κx/(1+κx) | ψ(w) = g(u), ψ((1−1/κ)w) = g(σ) | 1−1/κ | χ(w) = χ(κ)χ(x) |

lie on lines through the origin of P × P. The maps x ↦ z and x ↦ w are injective. Hence the following hold.
- **Identities (any weights):**
  \[A_\varepsilon(\kappa)=\sum_{\chi(z)=\varepsilon}\psi(z)\psi((1-\kappa)z)\,\psi(\kappa x(z))=\sum_{\chi(w)=\chi(\kappa)\varepsilon}\psi(w)\psi((1-\tfrac1\kappa)w)\,\psi(x(w)).\]
- **Inequality (0 ≤ g ≤ 1):** drop the factor ≤ 1 that is not part of the pair. Then
  \[A_\varepsilon(\kappa)\le\min\{c_\varepsilon(\kappa),\ c_\varepsilon(1-\kappa),\ c_{\chi(\kappa)\varepsilon}(1-1/\kappa)\}.\]

*Proof.*
- **Slopes.** σ − 1 = (u−s)/s = (κ−1)x/(1+x) = (1−κ)z. Also 1/σ − 1 = (s−u)/u = (1−κ)x/(1+κx) = (1−1/κ)w.
- **Weights.** ψ(z) = g(1/s) = g(s) and ψ((1−κ)z) = g(σ). Likewise ψ(w) = g(1/u) = g(u) and ψ((1−1/κ)w) = g(1/σ) = g(σ). This uses (H3).
- **Classes.** χ(z) = χ(−1)χ(x)χ(s)⁻¹ = χ(x), since s ∈ Q and χ(−1) = 1. Likewise χ(w) = χ(κx).
- **Injectivity.** z = −x/(1+x) is a Möbius involution. ∎

**Corollary 2.1 (coupled pricing).** With g(1) = 1:
\[T_0-c\ \le\ \mathrm{CPL}:=\sum_{\kappa\ne1}\sum_\varepsilon c_\varepsilon(\kappa)\min\{c_\varepsilon(\kappa),c_\varepsilon(1-\kappa),c_{\chi(\kappa)\varepsilon}(1-1/\kappa)\}.\]
In particular \(T_0-c\le\mathrm{ICR}:=\sum_{\kappa\ne1}\sum_\varepsilon c_\varepsilon(\kappa)c_\varepsilon(1-\kappa)\).

**Corollary 2.2 (subgroup laws).** If g = 1_H for a subgroup H ≤ Q, then σ = u/s ∈ H automatically. So A_ε = c_ε. Applying Lemma 2 to κ and to 1−κ gives
\[c_\varepsilon(\kappa)=c_\varepsilon(1-\kappa)=c_{\chi(\kappa)\varepsilon}(1-1/\kappa)\qquad(\kappa\ne0,1).\]
That is, the shifted-subgroup correlation is invariant under the anharmonic group, and every inequality in Lemma 2 is an equality.

*Exact checks:* `paley-189-t0-exact.py`.
- Part 1 checks the two identities (integer weights).
- Part 2 checks the inequality and Corollary 2.1 for 15 random 0/1 inversion-symmetric weights at p = 29, …, 61.
- Part 3 checks Corollary 2.2 at nine (p, |H|) pairs, p ≤ 109.

**Reading.**
- Lemma 2 says exactly what the triangle weight can buy: a multiplicative triangle forces three pencil lines through (1,1) to be simultaneously occupied, at slopes in one anharmonic orbit. A pricing of T₀ that gains over X must show that rich slopes κ rarely have 1−κ and 1−1/κ rich as well.
- Corollary 2.2 shows that this is false for subgroups: there every orbit is uniformly rich. By §3, it is false up to constants for sectors.

## 3. Transfer: T₀ is not easier than X on sector-type laws (Proposition 3; proved)

**Proposition 3.**
- **(a) Subgroup laws.** Let H ≤ Q have order d. ν uniform on the annihilator \(H^\perp\subseteq\widehat Q\) (|H^⊥| = n/d) is a probability. It gives f = 1_H, so g = 1_H. Then ω ≥ 0 and (H3) hold, and n max ν = d, so the cap holds when d ≤ C_cap√p. For this law, **T₀ = X**, because Δ(λ, 0) ≠ 0 forces λ = Y′/Y ∈ H, where g = 1.
- **(b) Restriction.** Let I ⊂ Q∖{0} with I = I⁻¹. Suppose g ≥ τ′ on I∖{1} and g ≥ τ on I·I⁻¹. Then
  \[T_0(g)\ \ge\ \tau\,\tau'^4\,X(\mathbf 1_I),\]
  where X(1_I) = Λ₀(μ_I) = Σ_{κ∈Q∖{1}} c_{h_I}(κ)², with h_I(z) = 1_I(1−z) (Lemma A1 for the 0/1 weight 1_I). This is the masked multiplicative energy of 1 − I.
- **(c) Interval laws.** Let J ⊂ \(\widehat Q\cong\mathbb Z/n\) be an interval of length L, ν = 1_J/L and n/L ≤ C_cap√p, and let γ generate F_p^×. Then g(γ^{2k}) = F_L(k) := (sin(πLk/n)/(L sin(πk/n)))², and F_L(k) ≥ 4/π² for |k| ≤ n/(2L). With I = {γ^{2k} : |k| ≤ n/(4L)}, a symmetric geometric progression with ratio γ², |I| ≍ n/L ≍ √p and I·I⁻¹ ⊆ {|k| ≤ n/(2L)}:
  \[T_0(g_J)\ \ge\ (4/\pi^2)^5\,X(\mathbf 1_I).\]

*Proof.*
- (a) As stated.
- (b) Every term of \(T_0=\sum_b\sum_{Y,Y'}v_b(Y)v_b(Y')g(Y'/Y)\) is ≥ 0. Keep only Y, Y′, D_b(Y), D_b(Y′) ∈ I. Then \(v_b(Y)\ge\tau'^2\mathbf 1_I(Y)\mathbf 1_I(D_b(Y))\) and g(Y′/Y) ≥ τ, so \(T_0\ge\tau\tau'^4\sum_b(\sum_Y\mathbf 1_I(Y)\mathbf 1_I(D_b(Y)))^2=\tau\tau'^4\Lambda_0(\mu_I)\).
- (c) For |x| = L|k|/n ≤ 1/2: sin(πx) ≥ 2x and L sin(πk/n) ≤ πx. So F_L(k) ≥ (2/π)². The rest is (b) with τ = τ′ = 4/π². ∎

*Checks.*
- `paley-189-t0-exact.py` Part 3: T₀ = X exactly for nine subgroup laws.
- Part 4 (floating) checks (c) at p = 101, 197, 257. The minimum of g on I·I⁻¹ is 0.41–0.59 ≥ 0.405, and T₀(g_J)/X(1_I) = 2.9–3.8 ≥ (4/π²)⁵ ≈ 0.011.

**Corollary 3.1 (method cap below 7/4).** Suppose a proof gives T₀(g) ≤ C p^{5/4−δ} for every admissible law with a fixed cap constant. Then by (c), for every p and every generator γ, the symmetric progression I = {γ^{2k} : |k| ≤ K} with K ≍ √p satisfies
\[X(\mathbf 1_I)\ \le\ (\pi^2/4)^5C\,p^{5/4-\delta}=O(|I|^{5/2-2\delta}).\]
- This is a "few products, many sums" energy estimate for shifted geometric progressions at length √p in F_p, below the exponent 5/2.
- The bound I know for this case is MPRRS Lemma 33 with A = I (|AA| < 2|A|), α = −1, B = I − 1. It gives X(1_I) ≤ E^×(I−1) ≪ |I|^{5/2} = p^{5/4} (hypotheses checked at this scale).
- I know of no published improvement below |I|^{5/2} at |I| ≍ √p in F_p. A short web search found none, but it was not exhaustive.
- So **a T₀ route below 7/4 is at least as hard as improving the geometric-progression energy below N^{5/2}**. The same holds for the pointwise route: Δ_{g_J}(λ, 0) ≥ (4/π²)⁴ Δ_{1_I}(λ, 0).

**Corollary 3.2 (F_{r²} control).**
- In F_q, q = r², the subfield H = F_r^× lies in the squares and has |H| = √q − 1. The weight g = 1_H satisfies (H3), ω ≥ 0 and the cap. By (a), T₀ = X, and X ≍ |H|³ ≍ q^{3/2} (all ratios lie in F_r).
- So the triangle weight gives no field-general saving. Through Theorem A the covariance exponent there is 2.
- Any saving on T₀ in F_p must come from a prime-only input, and by (a) and (c) it must be an input that already bounds X on subgroup or sector configurations.
- For subgroups such an input exists: Stepanov's method, through the Macourt–Shkredov–Shparlinski bound E^×(Γ+λ) ≪ |Γ|² log|Γ| as reported in Round 186, which gives T₀ = X ≪ p log p for subgroup laws. For geometric progressions (sectors) I know none beyond N^{5/2}.

**What the transfer does not say.**
- It gives **no** obstruction at the 43/24 threshold. The geometric-progression energy N^{5/2} = p^{5/4} lies below p^{31/24}, so sector laws are compatible with T₀ ≤ p^{31/24−δ}.
- The obstruction at 43/24 is the general-law pricing (§4), where X itself is priced at p^{4/3} by Round 187 and the triangle weight does not demonstrably help.
- Nor is the transfer a lower bound for T₀ or X of any actual law: models have X ≍ p.

## 4. Method caps at the 43/24 threshold (method statements)

Exponents are powers of p, with N = p^{1/2} for level sets of size ≍ √p. Each value is checked in `paley-189-t0-exponents.py`. Theorem A gives covariance exponent ½ + e(T₀), with thresholds e(T₀) < 5/4 (below 7/4) and < 31/24 (below 43/24).

| pricing of T₀ − c | best value with current inputs | needed for < 43/24 | status |
|---|---|---|---|
| T₀ ≤ X (Round 188) | 4/3 → covariance 11/6 | — | accepted |
| **half-structured CS:** (Σ_{κ≠1} A²)^{1/2} X^{1/2} | structured side at the MPRRS value 5/4, X at 4/3: **exactly 31/24** → covariance **exactly 43/24** | Σ A² ≤ p^{5/4−δ} (and ≤ p^{7/6−δ} for < 7/4) | lands on the threshold. By Prop. 3(b),(c), Σ A² on interval laws dominates (4/π²)^{10}·X(1_I)-type sector energies, so going below needs the geometric-progression improvement of Cor. 3.1 |
| anharmonic cross sum ICR = Σ c(κ)c(1−κ) (Cor. 2.1), as incidences of N² points P × P with the N² non-concurrent lines x₃x₂ + x₁x₄ = x₁x₃ | Stevens–de Zeeuw Theorem 4 (a = b = N, n = N²; ab² ≤ n³ and an = p^{3/2} ≪ p² hold): **11/8**; even Szemerédi–Trotter strength: 4/3 | ≤ 31/24 directly, or ICR ≤ p^{5/4} inside (X·ICR)^{1/2} | worse than or equal to X; models: ICR/X ≈ 1.0–1.35 |
| auditor (i): (T₃ G E^×)^{1/2} | 17/12 | T₃ ≤ p^{2/3−δ}, against T₃ ≍ p | retired (Round 188) |
| auditor (ii), and light-triangle splitting τX + (G/τ)D₀*: (G X D₀*)^{1/2} | D₀* priced at d = 11/12 | d < 3/4 (< 2/3 for 7/4) | see next row |
| pointwise D₀* as Σ of r over ≤ N pencil slopes: rich-slope counts t(h) ≪ N⁴/h⁴ (Lemma M′ Step 4 at K ≍ 1) | d = **7/8** | d < 3/4 | capped |
| same, with Szemerédi–Trotter-strength counts t(h) ≪ N³/h³ (not available in F_p at this scale) | d = **5/6** | d < 3/4 | capped even at characteristic-0 strength |
| same, by Cauchy–Schwarz (N X)^{1/2} | d = 11/12 now, 3/4 at X ≍ p | d < 3/4 | needs X below its floor; impossible |
| Plancherel: T₀ ≤ (Γ_tot E₀)^{1/2}, E₀ = Σ_λ Δ(λ,0)² ≥ c² ≍ p² | floor 5/4 at Γ_tot ≍ √p; with E₀ − c² ≤ D₀* X it reduces to auditor (ii) | — | no new gain |

**Proposition 4 (pencil cap for the pointwise route; method statement).**
- Δ(λ, 0) = Σ_{s∈S_λ} r(M_λ(s)), where M_λ(s) = (λs−1)/(s−1) is injective. So Δ(λ, 0) is the number of incidences between the grid S × S and at most N lines of the pencil through (1,1).
- Any bound that uses only the distribution of r(κ) satisfies Δ ≤ NH + Σ_{h≥H} h·t(h).
  - With t(h) ≪ N⁴/h⁴ it optimises at H = N^{3/4} to N^{7/4}, i.e. d = 7/8.
  - With t(h) ≪ N³/h³ it optimises at H = N^{2/3} to N^{5/3}, i.e. d = 5/6.
- Both exceed 3/4. A pointwise bound D₀* ≤ p^{3/4−δ} therefore needs information on **which** slopes M_λ(S_λ) occupies (a Möbius image of a subset of S). Rich-slope counts alone cannot supply it.

**Why the Round 187 barriers do not move.**
- **Young / light levels.** If one of the four X factors g(s), g(u), g(t), g(t′) is below τ, the contribution is ≤ τ G T₃ ≤ τ G² Γ_tot. That is the same order τp^{3/2} as the Young term τG³ for X when Γ_tot ≍ √p.
- **The triangle factor.** It saves only when the triangle factor itself is light (Proposition 5).
- **Height 1 and moderate heights.** On whole level sets at a common height, Lemma 2 gives A ≤ min(c(κ), c(1−κ), …). Nothing available bounds the joint richness of κ and 1−κ beyond the uncoupled counts, and Corollary 2.2 shows that it can be maximal.

**Proposition 5 (heavy-triangle reduction; proved).** For every θ > 0:
\[T_0-c\ \le\ p^{-\theta}X+\sum_{\lambda\ne1,\ g(\lambda)\ge p^{-\theta}}g(\lambda)\Delta(\lambda,0).\]
*Proof:* split T₀ − c = Σ_{λ≠1} g(λ)Δ(λ, 0) by the height of g(λ), and use Σ_λ Δ(λ, 0) = X (Lemma A2 at χ = 1 together with Lemma A1). ∎

With X ≪ p^{4/3+o(1)} and θ = 1/24 + δ, beating 43/24 needs only the heavy-triangle part:
\[\sum_{\lambda\ne1,\ g(\lambda)\ge p^{-1/24-\delta}}g(\lambda)\Delta(\lambda,0)\le p^{31/24-\delta'}.\]
The sum runs over a level set of size ≤ G p^{1/24+δ} = p^{13/24+δ+o(1)}. Pricing it by |level set|·D₀* again needs d < 3/4 − δ. This is the sharpest form of the open step I can state.

## 5. Evidence (floating point; models; not certificates)

`paley-189-t0-models.py 401 809 1601 3209 6421` (about 3 minutes in all).
- Laws are flat ν on S ⊂ Z/n with |S| ≈ n/√p: `rand`, `interval`, `halfint`.
- Controls:
  - `gp01` = 1_I, I a symmetric geometric progression in Q of length ≈ √p (inversion symmetric, not of the form |f|²);
  - `subgroupd` = 1_H for a divisor d of n in [√p/2, 2√p] when one exists.
- Columns are as defined in the script header.

| model, p | Γ_tot/√p | X/p | (T₀−c)/p | (T₀−c)/(X−c) | ΣA²/p^{5/4} | √(ΣA²·X)/(T₀−c) | CPL/(T₀−c) | ICR/X | D₀*/√p |
|---|---|---|---|---|---|---|---|---|---|
| rand, 1601 | 0.116 | 0.450 | 0.023 | 0.051 | 0.0002 | 1.02 | 18.8 | 1.003 | 0.026 |
| rand, 6421 | 0.060 | 0.478 | 0.012 | 0.025 | 0.0000 | 1.01 | 38.5 | 1.001 | 0.013 |
| interval, 1601 | 0.667 | 0.639 | 0.211 | 0.495 | 0.053 | 2.19 | 3.09 | 1.219 | 0.458 |
| interval, 6421 | 0.668 | 0.647 | 0.206 | 0.473 | 0.038 | 2.27 | 3.28 | 1.250 | 0.350 |
| halfint, 6421 | 0.345 | 0.514 | 0.059 | 0.127 | 0.0067 | 3.00 | 8.27 | 1.076 | 0.145 |
| gp01, 1601 | 1.025 | 0.837 | 0.254 | 0.710 | 0.141 | 3.41 | 3.81 | 1.270 | 0.525 |
| gp01, 6421 | 1.011 | 0.925 | 0.305 | 0.712 | 0.105 | 3.06 | 3.40 | 1.246 | 0.449 |
| subgroup20, 1601 | 0.500 | 0.217 | 0.079 | **1.000** | 0.046 | 3.20 | 3.71 | 1.345 | 0.400 |
| subgroup107, 6421 | 1.335 | 2.412 | 1.529 | **1.000** | 0.364 | 1.84 | 2.13 | 1.352 | 1.585 |

Reading (models only):
- **The triangle coupling saves only a constant on sector-type laws.** (T₀−c)/(X−c) is flat in p: interval 0.55 → 0.47 over p = 809–6421; gp01 0.71; subgroups exactly 1. It decays (≈ p^{−1/2}) only for `rand`, where Γ_tot ≪ √p and the heuristic (G/p)X applies. This is Proposition 3 seen numerically.
- **No anti-correlation in the anharmonic orbit.** ICR/X stays in 1.00–1.35. So in the models, c(κ) and c(1−κ) are positively correlated, never anti-correlated.
- **All quantities sit at their floors.** X/p, ΣA²/p and D₀*/√p are bounded. The models show no sign of p^{4/3}, p^{5/4} or d > 1/2. As in every earlier round, they cannot test an exponent.
- The half-structured CS bound is within a factor 1–3.4 of T₀ − c, and the coupled bound CPL within 2–40.
- Other rows (p = 401, 809, 3209) are in the script output; they show the same pattern.

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved.** Hypotheses: (H3), supp g ⊆ Q, g(0) = 0, p ≡ 1 (mod 4); 0 ≤ g ≤ 1 and g(1) = 1 where stated; the chart of Round 171. These hold for the actual g = |f|², with ω ≥ 0.
- (a1) Proposition 1: the κ-form of T₀, c and X.
- (a2) Lemma 2: the three-pencil identities, and A_ε(κ) ≤ min{c_ε(κ), c_ε(1−κ), c_{χ(κ)ε}(1−1/κ)}.
- (a3) Corollary 2.1: T₀ − c ≤ CPL ≤ ICR.
- (a4) Corollary 2.2: anharmonic invariance of c_ε for subgroups.
- (a5) Proposition 3: T₀ = X for subgroup laws (admissible with the cap when |H| ≤ C√p); T₀(g) ≥ ττ′⁴X(1_I) under the restriction hypothesis; T₀(g_J) ≥ (4/π²)⁵X(1_I) for interval laws, with |I| ≍ √p.
- (a6) Corollary 3.1 as an implication: a uniform T₀ ≤ p^{5/4−δ} implies X(1_I) = O(|I|^{5/2−2δ}) for those geometric progressions. Corollary 3.2: in the F_{r²} control, T₀ = X ≍ q^{3/2}.
- (a7) Proposition 5: the heavy-triangle reduction.
- All exact checks: `paley-189-t0-exact.py` prints `ALL EXACT CHECKS OK`.

**Method statements (not lower bounds).** §4 table and Proposition 4. Exponents are in `paley-189-t0-exponents.py` (`ALL OK`).

**(b) Conditional criteria.**
- (b1) Σ_{κ≠1} Σ_ε A_ε(κ)² ≤ p^{5/4−δ} gives T₀ − c ≤ p^{31/24−δ/2+o(1)}, i.e. a one-match exponent below 43/24. Likewise ≤ p^{7/6−δ} gives below 7/4.
  - *Proof:* Cauchy–Schwarz in Corollary 2.1's sum, using Σ_{κ≠1}Σ_ε c_ε(κ)² = X + 2c₊(1)c₋(1) ≤ X + Γ_tot² ≪ X.
  - The identity Σ_κ Σ_ε c_ε(κ)² = Σ_{β∈Q} c(β)² follows by expanding over pairs z, z′ in one class, so that z′/z ∈ Q.
- (b2) The heavy-triangle sum of Proposition 5 ≤ p^{31/24−δ} beats 43/24.
- (b3) D₀* ≤ p^{3/4−δ} (resp. p^{2/3−δ}) beats 43/24 (resp. goes below 7/4). This is the auditor's criterion, re-derived via Proposition 5 with G in place of Γ₂.
- (b4) ICR ≤ p^{5/4−δ} also gives (b1)'s conclusion, through (X·ICR)^{1/2}.
- (b5) [external, conditional on a result I do not know to exist] An energy bound E^×(A+1) ≪ |A|^{5/2−η} for |AA| ≪ |A| at |A| ≍ √p in F_p removes the obstruction of Corollary 3.1 for sector laws. It does not by itself bound T₀ for general laws.

**(c) Evidence.** Exact identities at p ≤ 109. One floating check of the interval transfer at p ≤ 257. Floating models at p ≤ 6421 (§5).

## Remaining gap

1. **One-match.** The accepted exponent 43/24 is unchanged, and T₀ ≤ X ≪ p^{4/3+o(1)} (covariance 11/6 through Theorem A).
   - **Below 7/4 through T₀:** this needs the geometric-progression (sector) energy below N^{5/2} at N ≍ √p in F_p (Corollary 3.1). It is not available, and it is the same obstruction as for X restricted to sectors.
   - **Below 43/24 through T₀:** this needs one of (b1)–(b4). Every decoupled or half-coupled pricing I found lands at or above 31/24 (§4). The half-structured CS lands **exactly** on it with the MPRRS value.
   - The binding configuration is moderate- and height-1 level sets whose rich pencil slopes κ have 1−κ and 1−1/κ rich as well. Corollary 2.2 shows this happens with equality for subgroups, and the models show it up to constants for sectors.
2. **X / first mass:** unchanged, X ≪ p^{4/3+o(1)} against p^{1+1/1280}.
3. **Γ₂ / support energy:** unchanged.
4. Zero-match, the generic J sum, the cold route and the original theta-limit target are unchanged. **Nothing here proves or refutes the original target.**

## Shared estimates (for the coordinator)

- **`cand:slope-row-mass-x` (X form): touched in use, value unchanged.**
  - Proposition 3 shows that the T₀ route cannot be separated from the X problem on sector and subgroup laws: T₀ = X on subgroups, and T₀ ≥ (4/π²)⁵X(1_I) on interval laws.
  - So the mission's hope, a T₀ estimate that "does not need the harder X = O(p^{1+ε})", holds only between 31/24 and 4/3. Below 5/4, a T₀ estimate contains an X estimate for sector weights.
  - If the coordinator records a candidate for T₀, it should be compared with `cand:slope-row-mass-x` before dispatch.
- **Γ₂:** not touched. No new candidate ID is proposed.

## Ranked next tests

1. **The geometric-progression energy at length √p in F_p**: is E^×_Q(I − 1) ≪ |I|^{5/2−η} for symmetric geometric progressions I ⊂ Q, |I| ≍ √p? A literature call, quoting at source, should settle whether this is known; MPRRS (re-read at source), Rudnev–Shkredov–Stevens and Murphy–Rudnev–Shkredov–Shteinikov are the first places to look. If it is known, the sector obstruction of Corollary 3.1 disappears. If it is not, every one-match route below 7/4 through T₀ or X restricted to sectors needs it.
2. **A partial-product version of MPRRS Lemma 33.** The triangle relation gives each counted pair (s, u) a quotient u/s in S, a "partial product set" of size N with no BSG. A graph version of Lemma 33 would bound Σ A² by N^{5/2}, which puts T₀ exactly at 31/24 (§4). Beating 43/24 then needs that version with a power saving. This is the most concrete coupled lever I found; it was not attempted here.
3. Otherwise retire coupled incidence pricings of T₀ (§4), and rest the one-match route on (X) or (Γ), as the mission's refuted branch says.

## Replay

```bash
.venv/bin/python -B research/paley-189-t0-exponents.py     # exact Fractions; prints ALL OK (<1 s)
.venv/bin/python -B research/paley-189-t0-exact.py         # exact integers (Parts 1-3), floating Part 4; ALL EXACT CHECKS OK (~3 s)
.venv/bin/python -B research/paley-189-t0-models.py 401 809 1601 3209 6421   # floating models (~3 min)
```
numpy 2.3.5. Model seeds are deterministic in p.

SHA-256 of the scripts: see the final section.

## Verdict

**Refuted, in the mission's method-cap sense, with this scope.** Neither an exponent below 43/24 nor one below 7/4 is proved.
- **Below 7/4:** the transfer (Proposition 3, proved) shows that any uniform bound T₀ ≤ p^{5/4−δ} contains a shifted-geometric-progression energy bound below |I|^{5/2} at |I| ≍ √p in F_p. I know of no proof of such a bound.
- **Below 43/24:** every coupled or decoupled incidence pricing I could build lands at or above p^{31/24} (§4):
  - the half-structured Cauchy–Schwarz lands exactly at 31/24 with the MPRRS value;
  - the pointwise pencil route caps at d = 7/8 (5/6 even at Szemerédi–Trotter strength), against the needed d < 3/4.
- **Best exponent:** unchanged, one-match covariance 43/24 (Round 187); T₀ ≤ X ≪ p^{4/3+o(1)}.
- **Binding term:** the joint richness of the anharmonic orbit {κ, 1−κ, 1−1/κ} of pencil slopes for level sets at height 1 and at moderate heights. This is the geometric-progression (sector) energy. The triangle weight saves only a constant there (subgroups: exactly 1; interval law: ≈ 0.5 in models).
- **Not a refutation of the target:** these are statements about methods and a reduction. They give no lower bound for T₀ or X of any actual law, and the models sit at T₀ − c ≍ p.

## Script hashes (final)

| script | SHA-256 |
|---|---|
| `research/paley-189-t0-exact.py` | `37a85726dfc633319cd3ffac6cf3d57c63a586b3b03fc1a39f86c8848a415c5e` |
| `research/paley-189-t0-exponents.py` | `dbdcac3e92c76ba3855dfdcd4ba784ff791698c1550890a4d29f26acdebe9fe9` |
| `research/paley-189-t0-models.py` | `bb42cf8876f529fae4b422769046d8841aa34a71a62806c1ead12e3238b43c53` |

Final replay on 2026-11-21: exponents `ALL OK`; exact `ALL EXACT CHECKS OK`; the models were run once with the primes listed (output quoted in §5).
