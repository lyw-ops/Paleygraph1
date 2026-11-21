# Proposed research mission: cold-prime-perron-nonseed-price

Coordinator record: coordination/round-188.json
Record SHA-256: 2c6221ec080ac072c5b8d93710427d4ed6f28d964d778bfd111c8ea8e590492c
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
In the compact model at t = a (then complex t in Q, both lifts), is the one-step norm of the non-seed part B_h of the frozen-base multiplier at V_602 (the h-linear term and all higher Taylor terms) below 0.274632 in the Perron-weighted sup-dominating price pi_phi of Round 188, so that kappa_0 = lambda_A + beta < kappa*; or is the pi_phi ratio of multiplication by the actual simples of h at least the budget?

## Why this call is worth making
Round 188 shows (conditionally) that the stated Criterion D cannot hold asymptotically and (unconditionally) that no dimension-price-dominating argument reaches its supported branch; both remaining cold routes need exactly this non-seed price, and the budget grew from 0.2416 to 0.2746 with C_S = 1.

## Current proof obligation
A sup-dominating price for the non-seed part B_h (h-linear and higher Taylor terms) with one-step rate below 0.274632 in pi_phi, under (b1), (H1), (H2), uniformly over t in Q and both lifts; or the angular variant of Criterion D with a growing-height L^2 decoupling; plus D2-D4, (b-Jk), (b-T), the stationary domain and derivative transfer. Proved frozen rate stays 1.066.

## Scope
Round 182 Proposition 1 / Corollary 2.2 framework; (b1), (H1), (H2) stated as hypotheses or re-proved in pi_phi; (R80) and (R80-4) as inherited; Round 186 Theorem N (size-only prices of h fail) and Round 185 Theorem 3 as accepted; certified outward arithmetic, floating only for orientation; extend the seed certificate to complex t in Q and the second lift. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: The price route closes in the compact model, subject to (b1), (H1), (H2) and the transfer statements; Criterion D is no longer needed.
- If refuted: Per-simple sup-dominating prices of this kind are retired for the cold route; only signed, leaf-cancellation arguments remain.
- If inconclusive: Return the certified range for the B_h price and the blocking term.

## Read these sources

- research/round-187-acceptance.json (SHA-256 edc1d3eb551e96c049cae265dd10c15cadb5b6ea641f5760cd02afa6df26a1d9)
- research/round-188-acceptance.json (SHA-256 e0face6c633785fa83b9412704fc613744fa7613fcf0b99586182465e684dcc6)
- research/native-claude-audit-188.md (SHA-256 300664ba3a9dab8e5e699254578f304d1b9798b4cbf61c75ff70ab479a1e9894)
- research/native-claude-cold-prime-compact-sup-growth-188.md (SHA-256 9c9b45f15ddb2398df05958c402125400c26056a771d096d7c189d2f7c6b765b)
- research/paley-188-cold-sup-growth-certify.py (SHA-256 6ddad2ca33c7b3033976a511fb9a5301257e80943f95440388856bc14e8f59bb)
- research/native-claude-cold-prime-hybrid-price-186.md (SHA-256 6a597c9a88b7b6e370fffe17a97eda014302c245d0c5a254e067cfff4845f738)
- research/native-claude-cold-prime-picard-leaf-inequivalence-185.md (SHA-256 45515537fbbf9b5b757328259b9efe8a5ebf0105c4765630c6bf07395f858dc1)
- research/native-claude-cold-prime-signed-nonseed-price-182.md (SHA-256 c8023a9bece7318be9122e2b0ec2ef007780e7b83835bb2eac8e84e91b4161e6)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

