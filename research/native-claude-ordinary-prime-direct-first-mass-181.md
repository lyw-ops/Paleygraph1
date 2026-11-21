# Round 181 native Claude draft: direct first mass (summary only)

- **call_id:** `ordinary-prime-direct-first-mass`
- **agent_label:** `native-claude/first_mass_181`
- **Mission:** `coordination/missions/round-181/ordinary-prime-direct-first-mass.md`
- **Script from this lane:** `research/paley-181-first-mass-check.py`, copied from the draft's `first_mass_check.py`. Its second part defaults to 60000. A replay of all `paley-181-*.py` scripts was killed (exit 137) during this run, so it has not been replayed.
- **Audit script for this lane:** `research/paley-181-audit-first-mass-check.py`, copied from the auditor's `audit_r2.py`. Replay printed `OK`.

**Summary only — the original text is not recoverable.** The full draft (`ordinary-prime-direct-first-mass-candidate.md`, about 14 KB) was in a scratchpad directory that has since been cleared. The coordinator never read that file. Its context holds only the agent's hand-back summary, reproduced verbatim below.

What is missing:
- all report sections: Setup recalled, Argument, Proved vs conditional vs evidence, Exact remaining gap, and the full next tests;
- the proofs of the reformulation and the energy bound;
- the random-model and extremal-model arguments;
- the Shkredov application details;
- the numeric tables.

Files that were not copied into the repository and are lost:
- `fejer_model.py`
- `first_mass_check.txt`
- `fejer_ratio1.txt`
- `fejer_ratio2.txt`

---

## Agent hand-back summary (verbatim)

**Result: inconclusive.** I could not prove M_w = O(p^{1+1/1280}) or refute it. The best proved bound stays at O(p^{11/8}), via Cauchy–Schwarz against the Round 179 second moment.

**What is proved (a):**
- **Exact reformulation.** With κ = 1−r and rows R_κ = {(Y,D) in (Q\{1})^2 : 1−Y = κ(1−D)}:
  M_w = Σ_{κ∈Q\{1}} Σ_{(Y,D),(A,C)∈R_κ} g(Y)g(D)g(A)g(C) w((A/C)/(Y/D)).
  The masks b≠1 and s≠b are vacuous; only κ∈Q survives. This was checked exactly against the chart sum at p = 13, 17, 29, 37, 41 (c).
- **Energy bound.** M_w ≤ ¼·E_Q(h), the shifted multiplicative energy of h(z) = g(1−z).
- **Exact requirement.** M_w = Σ_e μ(e)I_e with Σμ ≤ G². So the μ-average of I_e must be O(p^{1/1280}) when G ≍ √p.
- **Where the difficulty sits.** The trivial frequency of w costs only O(p^{1−3/418}). The rows that block the target are the rich ones with p^{1/1280} < m(κ) ≤ R_*.
- **Genuine subgroup models meet the target.** For g a combination of cosets of H with |H|² < p, Shkredov's Theorem 6 (arXiv:1504.04522, checked against the paper) gives M_w ≪ G⁴ log|H| / |H|². That is O(p log p) at |H| ≍ √p.

**Conditional (b):** if every level set S_t with t ≥ p^{−1/2} has E^×(1−S_t) ≤ C p^{1/1280}(|S_t|² + |S_t|⁴/p), then the target holds and D_0+D_1 = O(p^{3/2}).

**Evidence (c):**
- In the random model M_w ≍ p^{1/2}. The extremal models allowed by the proved constraints give M_w ≍ p.
- M_w/G² stayed between 0.013 and 0.10, with no growth, for p from 10³ to 2.6·10⁵. This held both for subgroup mixtures and for Fejér bumps on a log-interval, which meet the cap exactly.

**Obstruction:** the target needs near-sharp shifted energy for the actual level sets.
- The high levels are only approximate subgroups (BSG pieces, log-intervals). Stepanov's method needs an exact group, and the best incidence bound is Round 177's N^{36/13`}, against the needed 2+1/640.
- Light levels down to p^{−1/2} would need character-sum equidistribution, which is not available for a general g.

**Next tests, ranked:**
1. Prove E^×(1−P_N) ≪ p^{o(1)}N² for a log-interval P_N with N ≍ √p, or any exponent below 36/13.
2. Search admissible families for power growth of M_w/G², up to p = 10⁶.

Files are in /private/tmp/claude-501/-Users-lyuyuwei--claude-spares-spare-6UwrMo/5c2fbe9f-e42f-418e-9bd9-cc365745ecfe/scratchpad/r181/:
- ordinary-prime-direct-first-mass-candidate.md (the full report)
- first_mass_check.py
- fejer_model.py
- first_mass_check.txt
- fejer_ratio1.txt
- fejer_ratio2.txt (stops at p = 16001; I stopped the p = 50021 run)
