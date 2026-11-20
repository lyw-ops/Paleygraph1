---
---

# Paley synthesis checkpoint after round 181

Generated from `coordination/round-181.json` by the Claude Opus 5.5 coordinator, generation-1 brain session (agent assessment, not human acceptance). Evidence labels: Round 181 is an evidence-only round. Its full drafts and audit were lost with the launching session's scratchpad, so nothing from it is proved for this checkpoint; every Round 181 statement below is an audited claim whose proof must be redone before use (only cold Proposition 1 survives verbatim). Floating results come from auxiliary models (sinc model, subgroup mixtures, Fejér bumps), not the actual optimiser. Open target, unchanged: the ordinary Lovász theta limit of the prime Paley localizations stated in the repository README; neither ordinary route nor the cold route is closed. Routes set aside: slope-fibre-mass-only arguments for the one-match covariance (blocked for the listed inequalities, realisability unchecked); the unsigned Round 180 secant-rate form (needs kappa0 < 0.052).

## Question examined

What did this round change in the search for the ordinary Lovász theta limit of prime Paley localizations, and what should a fresh coordinator test next?

## What we learned

- **Actual ordinary positive completion and marked cancellation** (unchanged) — No accepted change (evidence only; proofs lost). Audited claims to re-prove before use: S(t)=M_1^2G^2/p+||pi(mu)h_t°||^2, ||pi(mu)||_HS^2=p sum mu^2 - sum m^2, a=1 and c=0 fibre costs O(p^(2-3/418)); slope-fibre masses with the listed inequalities cannot pass 115/64 (abstract configuration of value p^(147/64), realisability unchecked); conditional criteria b1, b1', b2, b3. First mass: M_w <= E_Q(h)/4 with an exact row-pair reformulation over kappa=1-r; target needs near-sharp shifted multiplicative energy E^x(1-S_t) of actual level sets; Shkredov Theorem 6 settles only exact coset models.
- **Actual common marked cold domain** (unchanged) — No accepted change (evidence only). Proposition 1 (text preserved; audited with two added hypotheses: price-class closure under the recursion and uniform correction constants) reformulates the price route as a small-ball Kantorovich criterion: u_{j+1} <= p0 + kappa0 u_j + c u_j^2 with (1-kappa0)^2 > 4 c p0 bounds every displacement price and gives confinement without Criterion D or compact transfer; with p0=0.01272 and c<=1.0043 this needs kappa0 < 0.77395. The existing P_5000 has rate 1.066. The seed-linear multiplier is priced exactly (L2 0.2510, dimension price <= 0.7101, weighted <= 0.5326).

## What resists

- **Actual ordinary positive completion and marked cancellation** — One-match covariance O(p^(3/2)), e.g. via ||pi(mu)||_op=O(p^(3/4)) for the actual twisted physical interior. Direct first mass M_w=O(p^(1+1/1280)), e.g. via shifted multiplicative energy of actual level sets below Round 177's exponent 36/13. The generic J sum (O(p^(9/4))) and the zero-match estimate are unchanged.
- **Actual common marked cold domain** — A signed cross-vertex collected price at V_602 with kappa0 < 0.77395 and its own p0, c, class closure and uniform corrections; the uncontrolled part is the transported non-seed multiplier (h=V_602-S and higher Taylor terms), budget about 0.24 against a crude h-linear cost about 0.50. Alternatively a signed source price p0 <= 1e-6 relaxes the target to kappa0 < 0.998. Uniform complex stationary domain and derivative transfer remain separate.

## Proposed next step

The user chose to record Round 181 as evidence only and continue. The proof plan is unchanged, but the three routes are sharpened: the slope-fibre approach is blocked for the listed inequalities, the first mass is reduced to shifted multiplicative energy of level sets, and the cold price route is reduced to one number kappa0 < 0.77395. Each Round 182 call must re-prove any Round 181 claim it uses, because the Round 181 proofs are lost. Calls run as Claude Code research sessions (the GPT gateway key is not available), each writing its candidate to a repository path before hand-back.

**First proposed mission** `ordinary-prime-one-match-operator-norm`

Is ||pi(mu)||_op = O(p^(3/4)) (or any bound giving one-match covariance below O(p^(115/64))) for the actual twisted physical interior mu, where pi is the (p-1)-dimensional representation of the affine group — for example through a mean-subtracted sixth-moment energy E_3 of mu?
Round 181 (evidence only) showed that slope-fibre masses together with the listed proved inequalities cannot beat 115/64, and that ||pi(mu)||_op=O(p^(3/4)) (criterion b1') would give the one-match target O(p^(3/2)); the auxiliary sinc model has ||pi(mu)||_op/p^(3/4) between 0.32 and 0.56.
Use the actual mu(r,b)=g(Y)g(D) with the square mask and interior exclusions of Round 171, the twisted physical chart of Rounds 169 and 173 and its one-match normalization, the actual w and D amplitudes, counting norms. First re-prove the splitting S(t)=M_1^2G^2/p+||pi(mu)h_t°||^2 and the Hilbert-Schmidt identity you use. A trace-moment route bounds ||pi(mu)||_op^(2k) by tr((pi(mu)pi(mu)*)^k); state exactly which energy each moment equals, which part of it the trivial representation removes, and which incidence or sum-product input (with hypotheses) controls it. Report exponents exactly and say which weights are majorized by one. Any Round 181 claim used (see research/round-181-acceptance.json proof_scope) must be re-proved in full in this draft; the Round 181 proofs are lost and are not citable.

- If supported — ||pi(mu)||_op=O(p^(3/4)) proves the one-match estimate O(p^(3/2)), leaving the zero-match estimate and the whole diagonal; any operator bound improving 115/64 is an accepted improvement.
- If refuted — A mu consistent with the proved constraints whose operator norm exceeds p^(3/4) by a power (for instance a level set concentrated near a coset of a subgroup of the affine group) shows criterion b1' is false and the one-match target needs the vector h_t°, not the operator norm.
- If inconclusive — Return the exact moment k and the energy term that blocks it, with its verified bound.

- **Queued** `ordinary-prime-shifted-level-energy` — Is the shifted multiplicative energy E^x(1-S) of the actual level sets S of g (or of log-intervals P_N with N ~ sqrt(p) as the first model) bounded by p^(o(1))(|S|^2+|S|^4/p) — or by any exponent below the Round 177 incidence exponent 36/13 — enough to give the direct first mass M_w=O(p^(1+1/1280))? Round 181 (evidence only) reduced the direct first mass to M_w <= E_Q(h)/4 with h(z)=g(1-z) and showed the target needs near-sharp shifted multiplicative energy for level sets with t >= p^(-1/2); exact coset models are settled by Shkredov's Theorem 6 (arXiv:1504.04522) but the high levels are only approximate subgroups.
- **Queued** `cold-prime-signed-nonseed-price` — Is there a signed cross-vertex collected price at V_602 whose frozen rate satisfies kappa0 < 0.77395 — in particular, can the transported non-seed multiplier (the h-linear term with h=V_602-S, plus higher Taylor terms) be priced below its budget of about 0.24 — or alternatively a signed source price p0 <= 1e-6, so that the small-ball Kantorovich criterion gives growing-prefix confinement? Round 181 (evidence only) turned the cold price route into one number: with p0=0.01272 and c<=1.0043, the small-ball criterion needs kappa0 < 0.77395, against the proved 1.066 for P_5000; the seed-linear part is priced exactly (weighted rate <= 0.5326) and the non-seed h-linear term costs about 0.50 crudely.

**Reading path**

- `research/round-181-acceptance.json`
- `research/native-claude-ordinary-prime-one-match-slope-fibres-181.md`
- `research/paley-181-one-match-identity-check.py`
- `research/ordinary-mixed-row-autocorrelation-180.md`
- `research/ordinary-weighted-slope-product-incidence-178.md`
- `research/ordinary-one-match-twisted-physical-169.md`
