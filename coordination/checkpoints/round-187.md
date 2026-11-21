---
---

# Paley synthesis checkpoint after round 187

Generated from `coordination/round-187.json` by the Claude Opus 5.5 coordinator, generation-1 brain session (agent assessment after an adversarial independent agent audit run as a background subagent, prepared while the user was asleep; not human acceptance). Evidence labels: Round 187 Lemma C, Lemma M', Proposition P', Theorems 1-2 and Corollary 4 are proved for the actual g = |f|^2 with the cap, without near-critical input, from Stevens-de Zeeuw Theorem 4 only; the one-match exponents 1193/664, 2125/1184 and 43/24 of Rounds 185-187 are agent-accepted and await human review, and the auditor advises a human read of Lemma M' before downstream reliance. The cold Propositions M and H and Lemma 3 are proved; Theorem 1 is proved for k <= 9 and conditional beyond; Proposition 6 is conditional on (ST-down); the 2^k growth of C_k is a heuristic; physical rows up to n = 5e7 are floating evidence. Open target, unchanged: the ordinary Lovász theta limit of the prime Paley localizations stated in the repository README. Routes set aside: BSG / Reiher-Schoen pricing of sup C and the Round 186 Theorem B machinery; extraction-plus-Young pricing of E^x(h), X and M_w (at the method cap p^(4/3)); searches for (HC')-violating models; floating searches for a bounded sup/RMS ratio at larger p; size-only or rotation-invariant arguments for Criterion D. Shared obligations: none in this batch; the X form of cand:slope-row-mass-x is now 4/3 + o(1) and stays open at p^(1+1/1280).

## Question examined

What did this round change in the search for the ordinary Lovász theta limit of prime Paley localizations, and what should a fresh coordinator test next?

## What we learned

- **Actual ordinary positive completion and marked cancellation** (weakened) — (HC') proved on [c p^(-1/6), 1] up to (log p)^(20/3) by the BSG-free Lemma M' and the chunked Lemma C; E^x(h) << p^(4/3) (log p)^(32/3); sup C, X, max W and 4 M_w <= E^x(h), so delta_C = 1/24 (point-line scheme floor) and one-match covariance O(p^(43/24) (log p)^(4/3)), 43/24 = 115/64 - 1/192; M_w improves from 11/8 to 4/3 + o(1); E(mu), sum W^(3/2) << p^(8/3+o(1)). No near-critical input; Reiher-Schoen no longer used. Consistent with every accepted floor; the F_(r^2) control fails Lemma C's characteristic term.
- **Actual common marked cold domain** (reformulated) — Fixed-height sup/RMS is proved bounded as n grows (k <= 9; ineffective, ~10^956); the Haar-random model gives sqrt(2 ln n), so a bounded ratio must use the arithmetic of K; bounded versus sqrt(ln n) is exactly moment growth to order ln n; seed counting rate l_S = 0.2400606 and fixed-height lower rate 0.027565 (exact/outward); conditional on (ST-down), Criterion D forces the compact sup growth C_k <= Lambda gamma^k with gamma <= 1.9436. Floating rows up to n = 5e7 follow the Gaussian law.

## What resists

- **Actual ordinary positive completion and marked cancellation** — One-match: the Round 178 chain floors the covariance at p^(7/4) whatever sup C is; slope-row work can gain at most 1/24 more and only with a height-1 pair-energy input below N^(8/3); reaching O(p^(3/2)) needs an input that is not an affine-energy bound and the generic six-word class below p^(9/2). First mass: X, M_w at 4/3 + o(1) against the target p^(1+1/1280) (needs near-sharp shifted energies). Support energy, generic J sum O(p^(9/4)) and zero-match unchanged. Propagate sup C to the Round 176/180 fixed-a generic squared mass.
- **Actual common marked cold domain** — Certify the compact sup growth rate of the increments R^comp_(602+k) against 0.466 per step (angular variant allowance 2.161), or a Criterion D variant with an averaged counting rate and a physical growing-height L^2 decoupling; plus (ST-down), D2-D4, (b4), (b-Jk), (b-T), the stationary domain and derivative transfer. Proved frozen rate stays 1.066.

## Proposed next step

Round 187 moved the one-match exponent a third time (2125/1184 to 43/24, the point-line scheme floor) and lowered X and M_w to 4/3 + o(1), agent-accepted after an adversarial audit that recommends a human read of Lemma M'. The cold call reformulated Criterion D as a compact sup-growth question. Round 188 follows the audit's ranking with two calls: certify the cold compact sup growth rate, and find a one-match input beyond the affine energy (or a method cap at 7/4). The lower-value height-1 pair-energy call is deferred. BSG pricing of sup C, extraction-plus-Young pricing of E^x(h), X, M_w, (HC')-violating model searches, floating bounded-ratio searches and size-only arguments for Criterion D are retired. The X form of cand:slope-row-mass-x moves to 4/3 + o(1) and stays open at its target. Round 188 research runs as background subagents of the brain session.

**First proposed mission** `cold-prime-compact-sup-growth`

In the compact (subsequential) model at the real floor, does the sup of the increments R^comp_(602+k) (equivalently of the seed iterates L_S^k d and the single-B words) decay at a certified rate below 1.94 x 0.2401 ~ 0.466 per step, so that C_k = ||R^comp||_inf / ||R^comp||_2 <= Lambda gamma^k with gamma < 1/q_rho, or is there a sign-aligned family with sup >= c 0.50^k; and how does it compare with the angular variant's allowance 1/q_ang(2.338) >= 2.161?
Round 187 reduced the n -> infinity content of Criterion D to the growth of C_k (Proposition 6, given (ST-down)), proved the exact seed L^2 rate l_S = 0.2400606, and its heuristic puts C_k ~ 2^k within 3% of the allowance; a compact-model computation can decide it, unlike more floating searches.
Compact model of Rounds 79/80/179 at t = a, real segments; start from the Round 182 per-simple slot-count transfer matrix and the independence of transported factors; certified outward bounds for the rate, floating only for orientation. State (ST-down) and the Round 80 (4) reading as hypotheses. Use Round 187 Lemma 3, Proposition 6 and Theorem 1 as accepted. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

- If supported — A certified rate below 0.466 fits Criterion D's gamma in the n -> infinity regime; the remaining gap is (ST-down) plus uniformity in k < k_n at finite n.
- If refuted — A certified C_k >= c theta^k with theta > 1.9436 means Criterion D in its stated form fails asymptotically (given (ST-down)); move to the averaged-rate variant if theta < 2.161, or to a price with rate below one.
- If inconclusive — Return the certified two-sided range for the rate and the term that blocks.

- **Queued** `ordinary-prime-beyond-point-plane` — The Round 178 chain floors the one-match covariance at p^(7/4) (E(mu) >= p^(5/2)), and Round 187 put sup C, max W and X at p^(4/3+o(1)). Is there an estimate on the twisted second norm ||H_alpha||_2 (or on sum w |H_alpha|^2) that does not pass through the affine energy and can use these slope-row bounds to go below p^(7/4); or does every route through E(mu) or its known variants floor at 7/4, and what exact term must a new route control? Point-line pricing is exhausted in Round 187; further sup C work can gain at most 1/24 and cannot reach 3/2, so the value of the ordinary route now lies in the step after the slope-row quantities.

**Reading path**

- `research/round-187-acceptance.json`
- `research/native-claude-audit-187.md`
- `research/native-claude-cold-prime-b-word-delocalization-187.md`
- `research/paley-187-cold-constants.py`
- `research/native-claude-cold-prime-hybrid-price-186.md`
- `research/cold-growing-prefix-delocalization-180.md`
- `research/native-claude-cold-prime-signed-nonseed-price-182.md`
