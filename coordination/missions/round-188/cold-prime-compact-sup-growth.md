# Proposed research mission: cold-prime-compact-sup-growth

Coordinator record: coordination/round-187.json
Record SHA-256: 36fbe33d8dedca6cd2fdccc3abd6a034b9ae45c034d2ebc17e11a1237fc384b3
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
In the compact (subsequential) model at the real floor, does the sup of the increments R^comp_(602+k) (equivalently of the seed iterates L_S^k d and the single-B words) decay at a certified rate below 1.94 x 0.2401 ~ 0.466 per step, so that C_k = ||R^comp||_inf / ||R^comp||_2 <= Lambda gamma^k with gamma < 1/q_rho, or is there a sign-aligned family with sup >= c 0.50^k; and how does it compare with the angular variant's allowance 1/q_ang(2.338) >= 2.161?

## Why this call is worth making
Round 187 reduced the n -> infinity content of Criterion D to the growth of C_k (Proposition 6, given (ST-down)), proved the exact seed L^2 rate l_S = 0.2400606, and its heuristic puts C_k ~ 2^k within 3% of the allowance; a compact-model computation can decide it, unlike more floating searches.

## Current proof obligation
Certify the compact sup growth rate of the increments R^comp_(602+k) against 0.466 per step (angular variant allowance 2.161), or a Criterion D variant with an averaged counting rate and a physical growing-height L^2 decoupling; plus (ST-down), D2-D4, (b4), (b-Jk), (b-T), the stationary domain and derivative transfer. Proved frozen rate stays 1.066.

## Scope
Compact model of Rounds 79/80/179 at t = a, real segments; start from the Round 182 per-simple slot-count transfer matrix and the independence of transported factors; certified outward bounds for the rate, floating only for orientation. State (ST-down) and the Round 80 (4) reading as hypotheses. Use Round 187 Lemma 3, Proposition 6 and Theorem 1 as accepted. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: A certified rate below 0.466 fits Criterion D's gamma in the n -> infinity regime; the remaining gap is (ST-down) plus uniformity in k < k_n at finite n.
- If refuted: A certified C_k >= c theta^k with theta > 1.9436 means Criterion D in its stated form fails asymptotically (given (ST-down)); move to the averaged-rate variant if theta < 2.161, or to a price with rate below one.
- If inconclusive: Return the certified two-sided range for the rate and the term that blocks.

## Read these sources

- research/round-186-acceptance.json (SHA-256 9f1a0ccb93a4ba4f75e8397105ae59418230856e0ee1e678f95f7169542626ee)
- research/round-187-acceptance.json (SHA-256 edc1d3eb551e96c049cae265dd10c15cadb5b6ea641f5760cd02afa6df26a1d9)
- research/native-claude-audit-187.md (SHA-256 714513ca7c9be14aa397b2c8a5a6786345da9d58cb9170e4524d7c7c50d657ff)
- research/native-claude-cold-prime-b-word-delocalization-187.md (SHA-256 6e7fc0d4e897581361046a67c9d3eb92d2033784dda3943ae3c4ebca53d361d2)
- research/paley-187-cold-constants.py (SHA-256 429b028d63443f63abdea019a533fa617395650859d574858b206f5d262a7895)
- research/native-claude-cold-prime-hybrid-price-186.md (SHA-256 6a597c9a88b7b6e370fffe17a97eda014302c245d0c5a254e067cfff4845f738)
- research/cold-growing-prefix-delocalization-180.md (SHA-256 3a8eb51ab257dc2b834142c7954357e533472676b4c5a06e1a0953db64e9b8c8)
- research/native-claude-cold-prime-signed-nonseed-price-182.md (SHA-256 c8023a9bece7318be9122e2b0ec2ef007780e7b83835bb2eac8e84e91b4161e6)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

