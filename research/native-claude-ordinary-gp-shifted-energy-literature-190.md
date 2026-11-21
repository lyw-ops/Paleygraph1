# Round 190 literature call: shifted geometric-progression energy (cand:gp-shifted-energy)

Author: Claude subagent started by the Round 190 coordinator (session/r190-gp-literature). Agent literature report; not human acceptance, not a mathematical certification.

Call ID: `ordinary-gp-shifted-energy-literature`. Mission: `coordination/missions/round-190/ordinary-gp-shifted-energy-literature.md` (coordinator record `coordination/round-189.json`, SHA-256 8901a11c...ce822, checked).

Status: complete. **Verdict: supported** (a published bound below |I|^{5/2} at |I| ≍ √p in F_p exists: MPRRS Theorem 37, exponent 32/13 = 5/2 − 1/26 up to logarithms). It does not reach the target size |I|^2 and does not by itself bound T_0 or X for general laws.

## 0. Sources read and hashes checked

All six listed sources match the mission's SHA-256 values (checked with `shasum -a 256` at the start of this session):

- research/round-188-acceptance.json e0face6c...dcc6
- research/round-189-acceptance.json ad4e0b5a...6506
- research/native-claude-audit-189.md 0bf8b1c3...f508 (read §2 and §5)
- research/native-claude-ordinary-prime-intercept-fibre-t0-189.md 2a586af8...b852
- research/native-claude-ordinary-prime-sup-c-heavy-price-186.md 9220d886...d0d3
- research/native-claude-audit-186.md 2b61a763...bc48

## Method of reading

- PDFs were downloaded from arxiv.org with `curl` into the session scratchpad and converted to text locally with PyMuPDF; quotations below are copied from that extracted text (line breaks and PDF ligatures normalised, mathematical symbols as extracted). Each source is identified by arXiv identifier and version as printed in the PDF margin stamp.
- No statement is reported from memory. Where I could not read a source, I say so.

## 1. Key finding (MPRRS Theorem 37): the |A|^{5/2} value is not the best published bound

Source: B. Murphy, G. Petridis, O. Roche-Newton, M. Rudnev, I. D. Shkredov, "New results on sum-product type growth over fields", arXiv:1702.01003v5 (19 May 2019), Mathematika 65 (2019) 588-642. URL https://arxiv.org/abs/1702.01003 (PDF https://arxiv.org/pdf/1702.01003v5). Section 4.5, "A bound for multiplicative energy in terms of |A + A|", pp. 43-46. This is the same paper as Lemma 33.

Verbatim (v5, p. 45):

> Theorem 37. Suppose A ⊂ F such that |AA| = M|A| and |A| ≤ p^{13/23}M^{10/23}. Then for any α ∈ F^∗ one has
> E^×(A + α) ≲ M^{33/13}|A|^{32/13}.
> Note that 32/13 = 5/2 − 1/26, so for M sufficiently small, this improves the bound E^×(A) ≪ M^{3/2}|A|^{5/2} provided by Lemma 33.

(The remark says "E^×(A)"; from the proof and context it means E^×(A + α), the quantity Lemma 33 bounds with B = A + α.)

Conventions (v5, p. 3-4, verbatim): "Let F be a field. We assume throughout that F has positive characteristic p, let F_p denote the corresponding prime residue field" and "by f ≲ g we mean that there is a constant C > 0 such that f ≪ (log g)^C g".

Proof structure (as printed, pp. 45-46): Theorem 34 (extracted from Shkredov, "Some new results on higher energies", Trans. Moscow Math. Soc. 74 (2013) 31-63) with G = F^∗ applied to the set A + α; D2 = M^{3/2} from Lemma 33 ("whenever M|A|^2|B| ≤ p^2", needed only for |B| ≤ 4|A|^4/E^×(A + α)), and D1 = M^5 log|A| from Lemma 32 (E^×_3(A + α) ≪ |AA|^5 log|A|/|A|^2 under |AA| ≤ p^{2/3}, "whenever |A| < p^{2/3}/M"). Theorem 34 verbatim (p. 43):

> Theorem 34. Let A be a finite subset of an abelian group G. Suppose there are parameters D1 and D2 such that E_3(A) ≤ D1|A|^3 and for any finite set B ⊂ G E(A, B) ≤ D2|A||B|^{3/2}. Then E(A) ≪ D1^{6/13} D2^{2/13} |A|^{32/13} log^{12/13}|A|.

Lemma 32 verbatim (p. 41): "Let A ⊂ F and let α ∈ F^∗. Suppose |AA| ≤ p^{2/3}. Then E^×_3(A + α) ≪ |AA|^5 log|A| / |A|^2." It is proved from the collinear-quadruple bound for Cartesian products (the paper's Theorem 11) applied to P = (AA ∪ −αA) × (AA ∪ −αA).

Lemma 33 verbatim (p. 42), unchanged from Rounds 186/189: "Let A, B ⊂ F such that |A||AA||B| ≤ p^2 and also max(|AA|, |B|) ≤ (|A||AA||B|)^{1/2}. Then for any α ∈ F^∗, E^×(A + α, B) ≪ |AA|^{3/2}|B|^{3/2}/|A|^{1/2}." Note: Theorem 37 follows Lemma 33 four pages later in the same section of the same paper; Rounds 186-189 quoted Lemma 33 but not Theorem 37.

Corollary 38 (p. 46, verbatim): "Let A be a subset of F such that |AA| = M|A|, |A| ≤ p^{13/23}M^{10/23}. Then T(A) ≲ M^{33/13}|A|^{9/2 − 1/26}." (T(A) = collinear triples in A × A.)

### 1.1 Hypotheses at the project's scale

- I = {γ^{2k} : |k| ≤ K} ⊂ Q ⊂ F_p^× (or {γ^k : |k| ≤ K}), |I| = N = 2K + 1 ≍ √p. II = {γ^{2j} : |j| ≤ 2K} has 4K + 1 < 2N elements, so M = |II|/|I| < 2 (assuming the γ^{2k} are distinct, i.e. ord(γ^2) > 4K; if not, I is a subgroup or a union of cosets and the subgroup bound applies a fortiori).
- Size condition: |A| ≤ p^{13/23}M^{10/23}. With M ≥ 1 it suffices that N ≤ p^{13/23}; since 13/23 > 1/2, N ≍ √p satisfies it for all large p. The condition is in terms of the characteristic p.
- α = −1 ∈ F_p^∗. Output: E^×(I − 1) ≲ 2^{33/13} N^{32/13} = N^{5/2 − 1/26} (log N)^{O(1)}, i.e. p^{16/13 + o(1)}.
- The point 0 ∈ I − 1 (from γ^0 = 1): Theorem 34 is applied in G = F^∗, so A + α must avoid 0. Apply the theorem to I' = I \ {1} (|I'I'| ≤ |II| < 2N, so M ≤ 2N/(N − 1) = O(1)); solutions of x1 x2 = x3 x4 with some x_i = 0 number O(N^2), so E^×(I − 1) ≤ E^×(I' − 1) + O(N^2) and the exponent is unaffected.
- Geometric progressions that are not subgroups: the theorem needs only |AA| ≪ |A|, so it applies to them directly. No subgroup structure or Stepanov method is used.
- Primality / F_{r^2} control: the size condition is |A| ≤ p^{13/23}M^{10/23} with p the characteristic. In F_{r^2} with A = F_r^× one has |A| ≈ p = r, so the condition fails, consistent with Round 189 Corollary 3.2 (E^× ≍ q^{3/2} there). In F_p (q = p) the condition holds at |A| ≍ √p. So the statement is "field-general" only with a characteristic-size restriction, which is exactly where primality enters.
- Masked vs unmasked: Round 189's Corollary 3.1 concerns X(1_I) (energy restricted to quotients in Q); the audit (§2.4) shows X(1_I) ≤ E^×(I − 1) and E^×(I − 1) ≤ 16(X(1_I) + |I|^2). Theorem 37 bounds the unmasked E^×(I − 1), hence X(1_I) ≲ N^{32/13}.

### 1.2 Exponent obtained

E^×(I − 1) ≪ |I|^{32/13}(log|I|)^{C}, 32/13 = 5/2 − 1/26 ≈ 2.461538; in terms of p, p^{16/13+o(1)} = p^{5/4 − 1/52 + o(1)}. In Round 189 notation (X(1_I) = O(|I|^{5/2−2δ})) this is the strength corresponding to δ = 1/52 (up to logarithms).

### 1.3 Independent re-statement in a later paper

I. D. Shkredov, "On asymptotic formulae in some sum–product questions", arXiv:1802.09066v2 (2 Mar 2018), p. 33, restates Theorem 37 for F_p, citing "[36, Section 4.5]" (MPRRS), verbatim:

> Lemma 43 Let A ⊆ F_p be a set and |AA| = M|A|, |A| ≤ p^{13/23}M^{10/23}. Then for any α ∈ F^∗_p one has E^×(A + α) ≲ M^{33/13}|A|^{32/13}.

He uses it (with D^×(A) ≤ |A|^4 max_{α∈A} E^×(A − α)) to prove his Theorem 41. So the statement has been reused by an author of the source, but I found no independent re-proof; it is a published, refereed theorem (Mathematika 2019), and this report does not re-verify its proof. Theorem 34's source (Shkredov 2013) was not re-read here.

## 2. Other sources read (all at source, arXiv PDF text)

| Source (arXiv id, version read) | Statement relevant to E^×(A + α), |AA| ≪ |A| | Hypotheses at |A| ≍ √p in F_p | Applies to non-subgroup GPs? | Exponent for E^×(I − 1) |
|---|---|---|---|---|
| MPRRS 1702.01003v5, Lemma 33 | E^×(A + α, B) ≪ |AA|^{3/2}|B|^{3/2}/|A|^{1/2} (quoted in §1) | holds (|A||AA||B| ≍ p^{3/2} ≤ p^2) | yes | 5/2 |
| MPRRS 1702.01003v5, **Theorem 37** | E^×(A + α) ≲ M^{33/13}|A|^{32/13} | holds (1/2 < 13/23) | yes | **32/13 = 5/2 − 1/26** (plus logs) |
| MPRRS 1702.01003v5, Lemma 32 | E^×_3(A + α) ≪ |AA|^5 log|A|/|A|^2 (third energy) | holds (|AA| ≤ p^{2/3}) | yes | (third moment N^3 log N; input to Thm 37) |
| Shkredov 1802.09066v2, Lemma 43 | restatement of Theorem 37 over F_p | as above | yes | 32/13 |
| Rudnev–Shkredov–Stevens 1607.05053v5, Theorem 11 | "Let A ⊂ F. If F has positive characteristic p, suppose |A| ≤ p^{5/8}. Let α ∈ F^∗ and δ = 1/5. Then there are two disjoint subsets B and C of A such that A = B ⊔ C and max{E^×(B), E^×(α + C)} ≲ |A|^{3−δ}." | holds | a decomposition, not a bound on all of I; on a GP the B part is small (E^×(B) ≥ |B|^4/|BB|) but the resulting bound for the whole set is no better than 14/5 | 3 − 1/5 = 14/5 (weaker than 5/2) |
| Macourt–Shkredov–Shparlinski 1701.06192v2, Corollary 4.1 | "Let G be a multiplicative subgroup of F^∗_p. Then for any λ ∈ F^∗_p, we have E^×(G + λ) − |G|^4/p ≪ ... |G|^2 log|G|, if |G| < p^{1/2} log p" (third case quoted; Stepanov input via Mit'kin's Lemma 2.1) | holds for subgroups | **no** (subgroups only; Stepanov needs x^t = 1 structure) | 2 (+log) for subgroups |
| Shkredov 1504.04522v1 (abstract) | "E^∗(G + x) ≪ |G|^2 log|G|" for subgroups |G| < p^{1/2} | subgroups | no | 2 (+log) for subgroups |
| Murphy–Rudnev–Shkredov–Shteinikov 1712.00410v1, Theorem 3 | "Let A ⊂ R and |AA| ⩽ M|A|. Then E(A) ≪ M^{8/5}|A|^{49/20} log^{1/5}|A|. The same estimate, with M = 1 holds for a multiplicative subgroup Γ ⊂ F^×_p, with |Γ| ≤ √p." | additive energy of A, real or subgroup only | no (and it is E^+(A), not E^×(A + α)) | n/a |
| Rudnev–Shakan–Shkredov 1808.08465v4, Theorem 3, Corollary 7 | few products, many differences: K^{24}M^{36} ≳ |A|^{13}; E_4(A, D) bounds | cardinality / fourth additive energy | — | n/a (no E^×(A + α) bound) |
| Shkredov 2106.09615v1, Theorem 9 and Corollary 11 | asymptotic count of |{(a, b) ∈ A × B : a = f_∗(b)}| for Möbius f_∗ and A, B with small product with a set Z, |Z| ≥ p^δ, error K^2K_∗^2K̃ √(|A||B|) p^{−1/(16k)}, k ≪ 1/δ; Corollary 11 for two GPs with the same base | holds for GPs of length ≫ exp(C log p/log log p) | yes | pointwise only: sup_{λ≠1} r(λ) ≪ N^2/p + N^{1−c} (c > 0 absolute, inexplicit). Since E^× ≤ sup r · N^2 this gives only 3 − c, weaker than 5/2 unless c > 1/2 |
| Rudnev–Shkredov 1812.01671v3, Corollary 18 (39) | I(A × B, C × D) ≪ |A|^{5/8}|B|^{1/2}|C|^{13/16}|D|^{7/8} + ... for Cartesian-product line sets, |C| ≤ |D|^2, |C||D|^2 ≤ p^2 | an improvement on Stevens–de Zeeuw only when |A|^2 ≫ |C||D|^2 and |A|^3 ≫ |C||D| (their remark) | — | does not move Lemma 33 at balanced sizes |
| Lund–Pham–Vinh 2311.05148 (v3), Theorems 1.5, 1.7 | direction-sparse incidence bound; I(A × B, L) ≪ |A|^{7/8}|B|^{1/2}|L|^{3/8}E^+(C)^{1/4} for lines of the form C × C under |C||B|^2 ≤ E^+(C), |A||C|^2 = O(p^2) | Thm 1.7 needs C additively structured; the pencil of E^×(I − 1) has all directions | no visible application | n/a |
| Stevens–de Zeeuw 1609.06284v4, Theorem 4 | "I(A × B, L) ≪ a^{3/4}b^{1/2}n^{3/4} + n" (a ≤ b, ab^2 ≤ n^3, an ≪ p^2) | baseline | — | baseline for Lemma 33-type bounds |
| Kerr 1903.08841v1; Shkredov–Vyugin 1102.1172v1; Shkredov–Solodkova–Vyugin 1302.3839v3; Kim–Yip–Yoo 2309.09124 | multiplicative energy of GAPs/boxes (Kerr); Stepanov for shifts of subgroups | subgroups or additively structured sets | no | n/a |
| Zhelezov 1507.05548v1; Warren 1812.01981v2; Yao 2611.24034v1 (18 Nov 2026) | cardinality bounds for shifted products/quotients and almost-subgroups | — | — | no energy bound below 32/13 |

Search coverage: web searches (several phrasings), the arXiv API (abstract queries on multiplicative energy with shifts, geometric progressions, few products, small multiplicative doubling), and the Semantic Scholar list of 68 papers citing MPRRS (all titles screened; 25 downloaded and grepped for E^×(A ± α), geometric progressions and 32/13). No paper in that list improves 32/13 for E^×(A + α) with |AA| ≪ |A| in F_p. Not read: the journal versions (arXiv versions only), Shkredov "Some new results on higher energies" (2013) for the origin of Theorem 34, Garaev–Shen, and any paper not on arXiv.

## 3. Answers to the four questions

(a) **E^×(A + α) below |A|^{5/2} for |AA| ≪ |A| at |A| ≍ √p in F_p.** Yes: MPRRS Theorem 37, E^×(A + α) ≲ M^{33/13}|A|^{32/13} for |A| ≤ p^{13/23}M^{10/23}. It applies to symmetric geometric progressions (M < 2, after removing the element 1) at N ≍ √p and gives E^×(I − 1) ≪ N^{32/13}(log N)^{O(1)}. This is the best published exponent I found for non-subgroup geometric progressions. For exact subgroups |Γ| < p^{1/2} log p, MSS Corollary 4.1 gives |Γ|^2 log|Γ| (Stepanov), which does not extend to progressions. I found no mixed version E^×(A + α, B) below Lemma 33 other than through Theorem 37's B = A + α case.

(b) **Stepanov-type or character-sum bounds for shifted short GPs.** No Stepanov bound for non-subgroup progressions was found; all Stepanov results read (Heath-Brown–Konyagin lineage via Mit'kin; Shkredov–Vyugin; Shkredov–Solodkova–Vyugin; Kim–Yip–Yoo) are for subgroups. The closest progression result is Shkredov 2106.09615 Theorem 9 / Corollary 11: an asymptotic formula with power saving for the number of points of I × J on one Möbius curve (this covers a − 1 = λ(b − 1) after inversion, since I = I^{−1}), with an inexplicit saving p^{−1/(16k)}. It controls each fibre r(λ) of E^×(I − 1) but not the energy below N^{5/2}.

(c) **Improvements of Stevens–de Zeeuw for Cartesian products in F_p.** Only regime-specific ones: Rudnev–Shkredov 1812.01671 Corollary 18 (lines much fewer than points) and Lund–Pham–Vinh 2311.05148 Theorems 1.5/1.7 (few directions, or additively structured line coefficients). Neither applies to the balanced, all-directions configuration behind Lemma 33. No general improvement of the 11/15 exponent was found. Theorem 37 does not need one: it gains through the third energy (Lemma 32) and Shkredov's higher-energy Theorem 34.

(d) **Graph (partial-product) version of Lemma 33.** None found. Searches on sum-product along graphs return only the Alon–Ruzsa–Solymosi line (reals/integers, cardinalities).

## 4. Conclusion

- **Best known exponent:** E^×(I − 1) ≪ |I|^{32/13}(log|I|)^{O(1)} for symmetric geometric progressions with |I| ≍ √p in F_p, i.e. p^{16/13+o(1)} = p^{5/4 − 1/52 + o(1)}. Source: MPRRS, arXiv:1702.01003v5, Theorem 37 (Mathematika 65 (2019)), restated as Shkredov arXiv:1802.09066v2 Lemma 43.
- **Barrier |I|^{5/2}:** broken, by 1/26 in the exponent of |I|, since 2017-2019, in the same paper and section as Lemma 33. The project's statement "known only at |I|^{5/2} (MPRRS Lemma 33)" in Round 189 (report §3, audit §2.4/§2.6/§5, checkpoint) is therefore out of date. The Round 189 audit's literature check (limited, as it said) missed Theorem 37.
- **Primality:** used through the size condition |A| ≤ p^{13/23}M^{10/23} in terms of the characteristic, which fails in the F_{r^2} control (|A| ≈ r = p). This is consistent with Round 189 Corollary 3.2.
- **Gap to the target:** 32/13 against the conjectural |I|^2 (Round 189 audit Part D numerics ≈ 2.5–2.9 |I|^2 for |I| ≤ 201; floating evidence only). The gap is 6/13 in the exponent of |I| (3/13 in p).
- **Near-sharp only for subgroups:** |Γ|^2 log|Γ| (MSS Corollary 4.1), which needs exact subgroups.

## 5. What this changes for the project (agent assessment, not a proof)

These are bookkeeping consequences of quoted statements combined with accepted Round 189 statements. They need the coordinator's and auditor's review.

- **Round 189 Corollary 3.1 as an implication stays true.** It says a uniform T_0 ≤ p^{5/4−δ} implies X(1_I) = O(|I|^{5/2−2δ}). What changes is the claim that the conclusion is unknown for every δ > 0. By Theorem 37 and X(1_I) ≤ E^×(I − 1), the conclusion is a known theorem for δ ≤ 1/52, up to logarithms: X(1_I) ≲ |I|^{32/13}.
- So the sector obstruction no longer sits at p^{5/4} (one-match 7/4). Under the same transfer (constant (4/π^2)^5), an admissible-only argument reaching T_0 or X ≤ p^{16/13−δ'} must still prove E^×(I − 1) ≪ |I|^{32/13−2δ'}, which is beyond the published bound. In covariance terms (covariance exponent = 1/2 + T_0 exponent, as in Round 189: 7/4 ↔ 5/4, 43/24 ↔ 31/24) the method cap moves from 7/4 to 1/2 + 16/13 = 45/26 = 7/4 − 1/52 ≈ 1.730769, up to p^{o(1)}. This is a re-statement of the Round 189 cap with an updated literature input, not a new cap theorem. The coordinator should restate it formally.
- **Not implied:** no bound on T_0, X, Γ_tot or the one-match covariance for the actual law, or for general admissible laws. Theorem 37 controls only the sector (interval-law) pieces X(1_I), and the Round 187 height-1 pricing pieces where Lemma 33 was used with |AA| ≪ |A|. The unconditional exponent 43/24 is unchanged by this report. The half-structured Cauchy–Schwarz row of Round 189 used the structured side Σ A^2 at an MPRRS-strength value. Theorem 37 needs |AA| ≪ |A| for the set itself, not a partial-product graph, so that row is not repriced (audit §2.5 correction stands).
- **cand:gp-shifted-energy:** should be re-recorded as "known at |I|^{32/13+o(1)} (MPRRS Thm 37); open below 32/13 at |I| ≍ √p for non-subgroup progressions; near-sharp |Γ|^2 log|Γ| for subgroups (MSS Cor. 4.1)", rather than as open below 5/2.
- **Mission outcome mapping:** "If supported: the sector obstruction of Round 189 Corollary 3.1 disappears." Precisely, it disappears down to p^{16/13} (δ ≤ 1/52) and persists below that, with 32/13 as the new external threshold. The next call proposed in the mission (apply the bound to X(1_I)-type pieces and the Round 187 height-1 level sets) is meaningful. Whether Theorem 37's hypotheses hold for the height-1 level sets (|AA| ≪ |A|, size ≤ p^{13/23}) must be checked there; it is not checked here.

## 6. Evidence and replay

- Exact exponent arithmetic: `python3 -B research/paley-190-gplit-exponents.py` prints `ALL OK` (15 checks in Fractions: 32/13 = 5/2 − 1/26, 16/13 = 5/4 − 1/52, δ = 1/52, 1/2 < 13/23, internal constraints of Theorem 37's proof at M = O(1), M^{33/13} bookkeeping, 45/26 = 7/4 − 1/52, comparison with 31/24, the F_{r^2} size failure). SHA-256 of the script: 3462d89e4df6aeb41dff912da42c6622d2278e56e61d2c8e47bb0347326616b7.
- Source texts: arXiv PDFs fetched 2026-11-21 from https://arxiv.org/pdf/<id> (versions as listed in §2) and converted with PyMuPDF in the session scratchpad. They are not saved in the repository. Quotes can be re-checked against the arXiv PDFs at the stated page numbers (MPRRS v5: Lemma 32 p. 41, Lemma 33 p. 42, Theorems 34-35 p. 43, Theorem 37 p. 45, Corollary 38 p. 46; Shkredov 1802.09066v2 Lemma 43 p. 33).
- Evidence label: literature quotation at source. The proofs of the quoted theorems were not re-verified. No finite computation was done.

## Verdict

**Supported.** A published bound below |I|^{5/2} at the relevant size exists: E^×(A + α) ≲ M^{33/13}|A|^{32/13} for |AA| = M|A|, |A| ≤ p^{13/23}M^{10/23} (MPRRS arXiv:1702.01003v5 Theorem 37). It applies to symmetric geometric progressions of length ≍ √p in F_p (not only subgroups) and gives E^×(I − 1) ≪ |I|^{5/2−1/26+o(1)}. Nothing better for non-subgroup progressions was found. The remaining external open problem is below |I|^{32/13}; the target size is |I|^2.
