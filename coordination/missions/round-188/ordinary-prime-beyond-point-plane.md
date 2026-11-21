# Proposed research mission: ordinary-prime-beyond-point-plane

Coordinator record: coordination/round-187.json
Record SHA-256: 36fbe33d8dedca6cd2fdccc3abd6a034b9ae45c034d2ebc17e11a1237fc384b3
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
The Round 178 chain floors the one-match covariance at p^(7/4) (E(mu) >= p^(5/2)), and Round 187 put sup C, max W and X at p^(4/3+o(1)). Is there an estimate on the twisted second norm ||H_alpha||_2 (or on sum w |H_alpha|^2) that does not pass through the affine energy and can use these slope-row bounds to go below p^(7/4); or does every route through E(mu) or its known variants floor at 7/4, and what exact term must a new route control?

## Why this call is worth making
Point-line pricing is exhausted in Round 187; further sup C work can gain at most 1/24 and cannot reach 3/2, so the value of the ordinary route now lies in the step after the slope-row quantities.

## Current proof obligation
One-match: the Round 178 chain floors the covariance at p^(7/4) whatever sup C is; slope-row work can gain at most 1/24 more and only with a height-1 pair-energy input below N^(8/3); reaching O(p^(3/2)) needs an input that is not an affine-energy bound and the generic six-word class below p^(9/2). First mass: X, M_w at 4/3 + o(1) against the target p^(1+1/1280) (needs near-sharp shifted energies). Support energy, generic J sum O(p^(9/4)) and zero-match unchanged. Propagate sup C to the Round 176/180 fixed-a generic squared mass.

## Scope
Actual g = |f|^2 with the cap; the Rounds 173/178/180/184 chain as accepted; cite Round 187 Theorem 2 and its corollaries; no near-critical input unless marked; exact exponent arithmetic; keep the generic six-word class separate. Quote any new external theorem from its source with hypotheses verified at the scales used. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: A one-match exponent below 7/4; the remaining one-match obligation becomes the generic six-word class.
- If refuted: A method cap at 7/4 for affine-energy routes; the coordinator then weighs the one-match route against the zero-match and generic J-sum obligations.
- If inconclusive: Return the binding term and its size in the models.

## Read these sources

- research/round-186-acceptance.json (SHA-256 9f1a0ccb93a4ba4f75e8397105ae59418230856e0ee1e678f95f7169542626ee)
- research/round-187-acceptance.json (SHA-256 edc1d3eb551e96c049cae265dd10c15cadb5b6ea641f5760cd02afa6df26a1d9)
- research/native-claude-audit-187.md (SHA-256 714513ca7c9be14aa397b2c8a5a6786345da9d58cb9170e4524d7c7c50d657ff)
- research/native-claude-ordinary-prime-level-pair-energy-187.md (SHA-256 5268631747d5ac3757ee328799f4e4205dd19afd5dc28184971a30255304e4b7)
- research/ordinary-weighted-slope-product-incidence-178.md (SHA-256 9e4589c664dc84d30e86206288183a3af9dfb1ae29f8d49ebd6faa1db01f1d71)
- research/ordinary-mixed-row-autocorrelation-180.md (SHA-256 357f5058dd8ef16cf330a252680252d77c815ec5f3f6175e86bfa904d68e85aa)
- research/ordinary-weighted-affine-vertical-saving-173.md (SHA-256 61e959f2defb68dec2f44205fb1601b0e98e210f3b45b38aed9ed68c3e3a2023)
- research/native-claude-ordinary-prime-near-critical-slope-row-mass-184.md (SHA-256 85702949b82c262a1d68dce098c89c995308880d63fbdc35765d571e6e6c02ec)
- research/native-claude-ordinary-prime-row-deleted-one-match-183.md (SHA-256 9af6768f701354214a612f0bbe9fc52b38910517fac95095aae3fe47f085a26a)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

