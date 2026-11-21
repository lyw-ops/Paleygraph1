# Proposed research mission: ordinary-prime-near-critical-support-energy

Coordinator record: coordination/round-183.json
Record SHA-256: 1231bfe2ad7af3148d2574dab427d0f9c6c3e831b6207a8ccef72451daab4f8e
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
On the near-critical branch (NC), does the flat support S of the actual law satisfy E(S) = o(|S|^3), or is there a near-critical configuration with E(S) asymp |S|^3 (necessarily <= (1/2)|S|^3); equivalently, is sum g^2 = o(sqrt p)?

## Why this call is worth making
Round 183 reduced sum g^2 exactly to the normalized additive energy E(S)/|S|^3 of the flat near-critical support and capped it at 1/2 through the Round 20 gap theorem; it gates (b1''') and relaxes every operator target, but no ordinary headline moves without the slope-row-mass call, so it ranks below it.

## Current proof obligation
Shared cand:slope-row-mass-x: for the actual near-critical g, max_xi W_xi = O(p^(1+epsilon)) with epsilon<3/16 (one-match below 115/64) and X = E_Q(h) = O(p^(1+1/1280)) (first mass target, D_0+D_1 = O(p^(3/2))). One-match target O(p^(3/2)) additionally needs the generic six-word class below p^(9/2). Decide E(S)/|S|^3 -> 0 on (NC) (equivalently sum g^2 = o(sqrt p)). Generic J sum O(p^(9/4)) and zero-match estimate unchanged.

## Scope
Near-critical branch only. Round 20 gap theorem and flattening, Round 151 coset-mass exclusion and Round 183 Propositions 1.1, 1.2, 1.4 (as accepted on (NC)) as inputs. Say explicitly which energy range (delta|S|^3, (1/2)|S|^3) is excluded. Floating models are evidence only. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: E(S) = O(|S|^3 p^(-delta)) relaxes every operator target by p^(delta/2) and makes the s=1 row negligible.
- If refuted: b1' is exactly critical and the one-match route must go through the generic six-word class.
- If inconclusive: Return the largest excluded energy constant below 1/2.

## Read these sources

- research/round-182-acceptance.json (SHA-256 78471bc51e0eaed7c99f92141d3a573d4a2d55f8fc4d7510c187da60e976bec6)
- research/round-183-acceptance.json (SHA-256 aae5b4aa2a8e1a8b216249c1f01ad9b1d3676853325a5b5cc30a9174db9f0fa9)
- research/native-claude-audit-183.md (SHA-256 e2803038572b7c521b32d336c8cec7cf2cbdd05f1856aef765f888c551e43f32)
- research/native-claude-ordinary-prime-row-deleted-one-match-183.md (SHA-256 9af6768f701354214a612f0bbe9fc52b38910517fac95095aae3fe47f085a26a)
- research/anchored-repair-20.md (SHA-256 141a0fb1c0017bae3c3fe4c900259be588bddfa1333dc8c65c7c504df5bf3721)
- research/ordinary-prime-coset-spread-151.md (SHA-256 2029d03cff0d88b9afb13a1e6a2957cee9d30842213d7ca79240432047823282)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

