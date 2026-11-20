---
---

# Paley synthesis checkpoint after round 182

Generated from `coordination/round-182.json` by the Claude Opus 5.5 coordinator, generation-1 brain session (agent assessment after an independent agent audit, not human acceptance). Evidence labels: Lemma SE, E^x(h)=O(p^(34/23)) (with the BSG/Schoen form taken from Rounds 163/173/177 without re-reading the paper), the re-proved Round 181 identities and the cold Propositions 1-2 are proved for large eligible primes; statements marked (H_sat) are conditional; model tables (0/1 one-match models, log-interval and subgroup energies, the numpy cold stationary row) are floating evidence about auxiliary models, not the actual optimiser. Open target, unchanged: the ordinary Lovász theta limit of the prime Paley localizations stated in the repository README. Routes set aside: the unrestricted b1' operator-norm criterion (saturated by the output row s=1 under (H_sat)); the BSG-pieces-plus-Young level-set scheme for M_w (capped at E^x(h)=O(p^(4/3))); one-step cold rates above one (they cannot keep Gamma_{k_n} bounded). Shared obligations: none; the blind audit found reports 1 and 2 share the object mu but need different estimates of it.

## Question examined

What did this round change in the search for the ordinary Lovász theta limit of prime Paley localizations, and what should a fresh coordinator test next?

## What we learned

- **Actual ordinary positive completion and marked cancellation** (reformulated) — Lemma SE E^x(1-B) << K^(2/3)N^(8/3) (Stevens-de Zeeuw Thm 4) and E^x(h)=O(p^(34/23)) are accepted; the row-pair formula M_w <= E^x(h)/4, the splitting S(t) and the trace identity tr((pi pi*)^k)=pT_k - T_k^x(m) are re-proved. The degenerate output row s=1 saturates b1' under (H_sat); the physical criterion is the row-deleted b1'' ||R pi(mu)||_op=O(p^(3/4)). Exact identity (audit): M_w = sum_r sum_{b!=b'} mu(r,b)mu(r,b')w(b/b'), a w-weighted dilation correlation inside slope fibres of mu. Headline exponents unchanged: one-match 115/64, M_w 11/8.
- **Actual common marked cold domain** (reformulated) — Proposition 1 re-proved with (H1) class closure and (H2) uniform corrections; sharp threshold kappa* = 0.77414706... at p0=0.01272. Finite-horizon Duhamel form: with ||L^m||_P <= C lambda^m the condition is lambda < 1 - C(1 - kappa*), and any use of either criterion needs Gamma_{k_n}=sum_{m<k_n}||L^m||_P bounded uniformly in n, which a one-step bound above 1 cannot give. Seed rates re-proved (0.71006 dimension, 0.53255 weighted) with exact m-step growth (alpha=1: 0.51366 at m0=8, C=1.0749).

## What resists

- **Actual ordinary positive completion and marked cancellation** — One-match O(p^(3/2)) via b1'' (k=3 translation discrepancy of slope-closed six-words: verified O(p^(177/32)), need O(p^(144/32))), or via sum g^2=o(sqrt p) and (b1'''). Direct first mass O(p^(1+1/1280)) without the BSG size loss (the BSG-plus-Young scheme is capped at E^x(h)=O(p^(4/3))). Generic J sum O(p^(9/4)) and zero-match estimate unchanged.
- **Actual common marked cold domain** — A uniform power rate for the full frozen multiplier: the non-seed part (h-linear plus higher Taylor) blocks; after charging the seed-only Taylor terms the h-linear allowance is rho*A(h) <~ 1.09 in pi_1 unless those terms are moved into the seed multiplier K Phi'_t(S). Floating evidence: sup|h| ~ 0.55, RMS ~ 0.175. Uniform complex stationary domain and derivative transfer remain separate.

## Proposed next step

Round 182 accepted one genuine input improvement (Lemma SE, E^x(h)=O(p^(34/23))) and re-proved the Round 181 reformulations, but no headline exponent moved. The audit's blind overlap review found no shared estimate. The three Round 183 calls follow the audit's ranking: the first mass as a fibre dilation correlation (avoiding the BSG cap), the cold power rate with the seed-only Taylor terms moved into the seed multiplier, and the row-deleted one-match criterion together with the sum g^2 question. Calls run as Claude Code research sessions with reports written to repository paths.

**First proposed mission** `ordinary-prime-first-mass-fibre-dilation`

Is M_w = sum_r sum_{b != b'} mu(r,b) mu(r,b') w(b/b') = O(p^(1+1/1280)) when treated directly as a w-weighted dilation correlation inside the slope fibres of the actual mu, for example through a per-slope-fibre multiplicative energy rather than the whole-level E^x(1-S_t)?
The Round 182 audit proved the exact identity rewriting M_w as a fibre dilation correlation of the one-match weight mu, and Round 182 showed the level-set route (BSG pieces plus Young) cannot go below E^x(h)=O(p^(4/3)); the fibre form keeps w and every amplitude and avoids the BSG size loss.
Actual g, w=g(1-g), mu(r,b)=g(Y)g(D) on the Round 171 chart with the square mask and Y != D, counting norms. Re-derive the identity of research/native-claude-audit-182.md section 4 (checked at p=29,53 by research/paley-182-audit-shifted-energy-check.py) before using it. Use Lemma SE and E^x(h)=O(p^(34/23)) from Round 182 where helpful. State whether w is kept or majorized; state any incidence or character-sum input exactly with hypotheses. Compute M_w and its restriction to the large multiplicative spectrum of w in subgroup-mixture and Fejér models (floating evidence) and say whether a per-fibre energy reaches p^(1+o(1)) there. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

- If supported — M_w=O(p^(1+1/1280)) closes J in {0,1} at target scale (D_0+D_1=O(p^(3/2))) and lowers each generic J class to O(p^(3/2+1/1280)).
- If refuted — An admissible family consistent with the proved constraints on g in which the fibre dilation correlation grows by a power over p shows the first mass needs signed cancellation from w, not positivity.
- If inconclusive — Return the exact fibre class (slope r, size of the fibre, multiplicative structure of b) where the bound fails, with its verified bound.

- **Queued** `cold-prime-seed-multiplier-power-rate` — With the seed-only higher Taylor terms moved into the seed multiplier L_S = K Phi'_t(S), is there a price P with a uniform power bound ||L^m||_P <= C lambda^m and lambda < 1 - C(1 - 0.77414706) for the full frozen multiplier at V_602, so that Gamma_{k_n} stays bounded uniformly in n? Round 182 proved that either cold criterion needs Gamma_{k_n} bounded uniformly in n, computed the seed-linear m-step growth exactly, and the audit showed that leaving the seed-only Taylor terms outside L_S cuts the h-linear allowance from 1.925 to about 1.09 in pi_1.
- **Queued** `ordinary-prime-row-deleted-one-match` — Is the row-deleted criterion ||R pi(mu)||_op = O(p^(3/4)) provable for the actual mu — first by deciding whether sum g^2 = o(sqrt p) for the actual law (which relaxes the target through (b1''')), and otherwise through the k=3 translation discrepancy of slope-closed six-words below its verified O(p^(177/32))? Round 182 showed b1' is saturated by the degenerate output row s=1 under (H_sat), that the physical one-match criterion never sees that row, and that the k=3 discrepancy is the blocking term (need O(p^(144/32))); whether sum g^2 is o(sqrt p) decides whether the row itself matters.

**Reading path**

- `research/round-182-acceptance.json`
- `research/native-claude-ordinary-prime-shifted-level-energy-182.md`
- `research/native-claude-audit-182.md`
- `research/paley-182-audit-shifted-energy-check.py`
- `research/ordinary-paired-J-cross-ratio-180.md`
- `research/ordinary-mixed-row-autocorrelation-180.md`
