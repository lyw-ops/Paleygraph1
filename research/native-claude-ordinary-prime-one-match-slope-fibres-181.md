# Round 181 native Claude draft: one-match slope fibres (summary only)

- call_id: `ordinary-prime-one-match-slope-fibres`
- agent_label: `native-claude/one_match_181`
- Mission: `coordination/missions/round-181/ordinary-prime-one-match-slope-fibres.md`
- Scripts in the repository from this lane:
  - `research/paley-181-one-match-identity-check.py`, copied from the draft's `r181_identity_check.py`;
  - `research/paley-181-one-match-saturation-exponents.py`, copied from `r181_saturation_exponents.py`.
- Audit script for this lane: `research/paley-181-audit-one-match-check.py`, copied from the auditor's `audit_r1.py`.

**Summary only — the original text cannot be recovered.** The full draft (`ordinary-prime-one-match-slope-fibres-candidate.md`, about 21 KB) was in a scratchpad directory that has since been cleared. The coordinator never read that file. Its context holds only the agent's hand-back summary, reproduced verbatim below.

Missing parts:
- all report sections: Setup recalled, Argument, Proved vs conditional vs evidence, Exact remaining gap, and the full statements of the two ranked next tests;
- the proofs of the identities and of the fibre costs;
- the explicit obstruction configuration;
- the detailed numeric tables.

Scripts that were not copied into the repository and are lost: `r181_fibre_rearrangement.py`, `r181_level_richness.py`, `r181_sinc_model.py`, `r181_weighted_richness.py`, and their outputs `fib_out.txt`, `sinc_out1.txt` and `sinc_out2.txt`.

---

## Agent hand-back summary (verbatim)

The mission is refuted for fibre-mass-only arguments: an argument built only from slope-fibre masses and the other proved inequalities cannot beat the current 115/64 covariance exponent, so it cannot reach the target 3/2 = 96/64. Nothing is proved unconditionally beyond 115/64.

Report: /private/tmp/claude-501/-Users-lyuyuwei--claude-spares-spare-6UwrMo/5c2fbe9f-e42f-418e-9bd9-cc365745ecfe/scratchpad/r181/ordinary-prime-one-match-slope-fibres-candidate.md. Scripts are the `r181_*.py` files in the same directory. No repository file was modified.

**Proved (a), on the inherited Round 169/173/178 chart:**
- The mean-subtracted target is an exact identity: S(t) = M_1²G²/p + ‖π(μ)h_t°‖². Here h_t° is h_t minus its mean and π is the (p−1)-dimensional representation of the affine group.
- Exact Hilbert–Schmidt identity: ‖π(μ)‖_HS² = pΣμ² − Σm(r)².
- The translation fibre a = 1 and the dilation line c = 0 each cost only O(p^{2−3/418}) per t.
- So the target is equivalent to the generic bound S_gen(t) = O(p²). Mean subtraction gains nothing at that scale.
- Fibre-wise additive energies reproduce exactly the existing E(μ) route, so they add nothing.

**Why fibre masses cannot help (a, a statement about the method):**
- One abstract configuration meets every proved inequality at once: C(a) ≤ p^{11/8}, E^×, Σ W^{3/2}, E(μ) ≤ p^{43/16}, the sup bounds, the transverse masses and the Rudnev–Shkredov rich-line count.
- Its value is exactly p^{147/64}, the Round 180 output, which is covariance p^{115/64}.
- The exponents are checked exactly with fractions.
- It is not shown to be realisable by an actual μ or level set.

**Conditional criteria (b):**
- (b1) Σg² = O(p^{1/3}) gives O(p^{3/2}).
- (b1′) ‖π(μ)‖_op = O(p^{3/4}) gives O(p^{3/2}).
- (b3) Generic weighted richness at most B gives O(B·p^{3/2}).
- (b2) This is the only criterion that uses C(a). If rich lines are spread over at most Λ|U|²/τ² slopes for τ ≥ p^{3/16}, the covariance is O(p^{108/64}Λ^{1/2}).

**Evidence (c), Round 170 auxiliary sinc model only, not the actual optimiser; floating point unless noted:**
- For p ≤ 1601, the per-t target holds with ratio 0.04–0.16.
- ‖π(μ)‖_op/p^{3/4} is 0.32–0.56, so (b1′) holds in the model; (b1) fails there.
- Generic richness is 3.3–5.0 weighted (p ≤ 1601), and at most 7 by exact count (p ≤ 10009).

**Next tests, ranked:**
1. A mean-subtracted sixth-moment energy E_3, aiming at (b1′).
2. A distinct-slope rich-line bound for level sets, aiming at (b2) and 108/64.
