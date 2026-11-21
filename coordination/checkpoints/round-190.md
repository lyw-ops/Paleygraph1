---
---

# Paley synthesis checkpoint after round 190

Generated from `coordination/round-190.json` by the Claude Opus 5.5 coordinator, generation-1 brain session (agent assessment after an independent agent audit run as a background subagent, prepared while the user was asleep; not human acceptance). Evidence labels: MPRRS Theorem 37 is a published theorem confirmed verbatim at source (its proof was not re-verified); the stocktake's fixed-block composition is a re-derivation from accepted statements; the structural Lemma 1, Theorems 1 and 4 and Propositions 2-3 are proved on (NC); Criteria 5.1-5.2 are conditional on (GP-Sub); clique-run counts and D_theta models are finite evidence. The unconditional one-match exponent 43/24 (Rounds 185-187) and Theorem A (Round 188) remain agent-accepted and await human review. Open target, unchanged: the ordinary Lovász theta limit of the prime Paley localizations stated in the repository README. Routes set aside: one-match as a standalone target; zero match and the J-split / full-diagonal routes as closing routes; sector-free (NC) arguments below 45/26 and the Gamma_tot route built from them; further general literature searches for the energy bound; subgroup laws as an obstruction; cold per-simple prices (cold paused). Shared obligations: none in this batch; cand:gp-shifted-energy is now known at |I|^(32/13) and open below; (GP-Sub) is recorded as cand:gp-sector-constancy; a new ordinary obligation (A) assembly is named.

## Question examined

What did this round change in the search for the ordinary Lovász theta limit of prime Paley localizations, and what should a fresh coordinator test next?

## What we learned

- **Actual ordinary positive completion and marked cancellation** (reformulated) — The obligation map is redrawn. One-match O(p^(3/2)) is a sufficient choice, not necessary; one-match closes nothing alone because zero match carries no recorded sign or exponent. M_w = O(p) logarithm-free (or X = O(p)) closes each fixed moderate block alone (composition of R162, R166, R172), but assembling the full favorable off-diagonal loses powers under every current majorant: a new obligation (A) assembly. MPRRS Theorem 37 gives E^x(I-1) << |I|^(32/13+o(1)) = p^(16/13+o(1)), so cand:gp-shifted-energy is known at 32/13 and the admissible-only obstruction weakens to p^(16/13) (one-match 45/26). On (NC) the sector condition is the only input that sees the obstruction family: diluted-interval laws satisfy every sector-free (NC) consequence and still obstruct; exact subgroup and interval laws are excluded; the sector lever reduces to (GP-Sub), recorded as cand:gp-sector-constancy (known only for c > 1/sqrt 2, Hanson-Petridis). Unconditional exponents unchanged.

## What resists

- **Actual ordinary positive completion and marked cancellation** — (A) assembly of fixed moderate blocks into the full O(p) favorable off-diagonal (or the contradiction on the critical branch), with its exact uniform form if it does not follow. (F) M_w = O(p) logarithm-free for each fixed block, now p^(4/3+o(1)) at its route's method cap. Below one-match 45/26: cand:gp-shifted-energy below |I|^(32/13), or the sector condition with (GP-Sub). Whether the sector obstruction binds M_w with the weight w kept.

## Proposed next step

Round 190 redrew the ordinary obligation map: one-match is off the critical path, the closest closing form is M_w = O(p) per fixed moderate block, and a new obligation (A) assembly is needed to turn fixed blocks into the target. The literature call found MPRRS Theorem 37 (|I|^(32/13)), weakening the Round 189 obstruction, and the structural call isolated (GP-Sub). Round 191 follows the audit's ranking: the assembly (A) first, because without it every fixed-block estimate is insufficient in principle; then two cheap calls in parallel, whether the sector obstruction binds M_w with w kept, and a literature check of (GP-Sub). Cold stays paused. If Round 191 confirms that the ordinary line rests on frontier sum-product inputs plus (A), the coordinator records them as external problems and holds estimate rounds. Weekly quota is near 80%, so Round 191 is the last full batch before slowing to one call per round.

**First proposed mission** `ordinary-fixed-block-assembly`

From the accepted reduction (R152-R154 top level; R157 conditional lower bound; R159-R166 cuts and blocks), does O(p) for every fixed moderate block, together with the paid cuts, imply the O(p) favorable off-diagonal or the contradiction on the critical branch (for example through the R157/R160 device that a cut keeps the lower bound >> pD when the deleted squared mass is o(D)); if not, what single uniform estimate is needed on the slope bands p^(-(1-2 gamma)) < g < s_0, the near-unit slopes and the vertex layers C/sqrt p < |F|^2 < a, and does M_w = O(p), X = O(p) or a weighted first mass with the true vertex amplitudes kept imply it?
The Round 190 stocktake showed that every ordinary route closes only fixed blocks, and the audit showed that the assembly loses powers under every current majorant; without (A), retargeting to M_w may aim at a statement that does not close the target.
Cite accepted statements by round and line; exact loss exponents; mark compositions as bookkeeping; no new incidence estimates; models only as evidence. Cite accepted statements by round; re-prove anything taken from an unaccepted draft. Locate the R152-R166 reduction files through research/README.md and the acceptance records' proof_scope fields.

- If supported — M_w = O(p) (or X = O(p)) is recorded as a genuinely sufficient ordinary target.
- If refuted — (A) is recorded with its exact uniform form as a separate ordinary obligation; fixed-block estimate rounds are insufficient in principle until (A) is addressed.
- If inconclusive — Return the list of unassembled pieces with their exact loss exponents.

- **Queued** `ordinary-first-mass-sector-obstruction` — For laws with g >= tau on I I^(-1) (the Round 189 interval laws and the Round 190 diluted-interval laws D_theta), is M_w(g) >= c(tau) X(1_(I')) for a sub-progression I' of comparable length, so that admissible-only and sector-free (NC) arguments for M_w <= p^(16/13-delta) must prove E^x(I'-1) << |I'|^(32/13-2 delta); or does the weight w(b/b'), small where g ~ 1, remove the sector pieces? The stocktake names M_w = O(p) as the weakest closing form for fixed blocks; whether that pivot is easier in kind than T_0 hinges on exactly this restriction computation in the fibre form of Round 183 Proposition A.
- **Queued** `ordinary-gp-sector-constancy-literature` — Is (GP-Sub_c) for some c <= 1/sqrt 2, or (GP-Sub_kappa), known (cand:gp-sector-constancy): nontrivial bounds for sum_{k <= M} chi(zeta^k + a) (character sums with exponential functions, shifted geometric progressions) at M asymp sqrt p or below, bounds on Paley cliques that are geometric progressions or multiplicative Bohr sets, or a Stepanov / Hanson-Petridis argument adapted to progressions? The Round 190 structural call proved that the sector condition is the only (NC) input that sees the obstruction family and reduced its use to (GP-Sub); the Round 190 literature call covered energies, not character sums.

**Reading path**

- `research/round-190-acceptance.json`
- `research/native-claude-audit-190.md`
- `research/native-claude-ordinary-obligation-map-stocktake-190.md`
