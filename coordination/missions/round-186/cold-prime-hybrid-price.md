# Proposed research mission: cold-prime-hybrid-price

Coordinator record: coordination/round-185.json
Record SHA-256: f5b2ff1fc84f0b0fac4b6a531b4658bb802a125f92cfe6fe5eb801324cbf8344
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Can a hybrid price, keeping the per-simple dimension price for the seed iteration and bounding multiplication by h = V_602 - S through a sup or counting norm (Round 128 counting rate 0.5145, Round 177 rate 0.545; floating sup|h| about 0.61), meet the Round 184 Duhamel allowance (seed-only A_X(h) < 0.7499 or its hybrid analogue), uniformly on Q, both lifts?

## Why this call is worth making
Round 185 retired, on certified depth-3 bounds plus model evidence, the cheap per-simple dimension price of h through its Picard expansion, which was the only alternative to a hybrid; the cold dimension-price programme now depends on whether a mixed price is submultiplicative in the needed direction.

## Current proof obligation
The cold obligation returns to Criterion D, sup transfer or a hybrid price (per-simple dimension price for the seed iteration, sup or counting norm for multiplication by h; floating sup|h| about 0.61 against the seed-only allowance 0.7499; Round 128 counting rate 0.5145, Round 177 rate 0.545), uniformly on Q, both lifts; plus D2-D4, (b4), (b-Jk), (b-T), the uniform complex stationary domain and derivative transfer. Proved frozen rate stays 1.066.

## Scope
Compact model under (b4), (b-Jk), (b-T); D2-D4 inherited. State precisely which price is submultiplicative against which, and whether the Round 182 Proposition 2 criterion applies to the hybrid price (prove (H1)/(H2) or state them as hypotheses). Use Round 184 Propositions A-C and Round 185 Theorem 3 as accepted. Certified outward arithmetic, allowances printed as lower bounds; separate exact from floating. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: A concrete certified cold criterion whose remaining input (a certified sup or counting bound for h) is computable.
- If refuted: The cold dimension-price programme reduces to Criterion D or sup transfer.
- If inconclusive: Return the certified gap and the term that blocks.

## Read these sources

- research/round-184-acceptance.json (SHA-256 c30660213a26e69b172ce6e7f21a1fe33fe4eba5bfcec7fd976247ebd5d5e3ef)
- research/round-185-acceptance.json (SHA-256 157de3b64f9e2a2140fdc46d342f3a3b1d19447fd51ab7492d00bde001f59f9d)
- research/native-claude-audit-185.md (SHA-256 03d3a66b3c17574380db8829b476738a593d7ee3e8ab4eb81218052c1080646e)
- research/native-claude-cold-prime-picard-leaf-inequivalence-185.md (SHA-256 45515537fbbf9b5b757328259b9efe8a5ebf0105c4765630c6bf07395f858dc1)
- research/native-claude-cold-prime-h1-product-rule-184.md (SHA-256 a45402f0da4ed714a095fda92abccf0fb41dd8724b39fbf8e47cd70b32529a90)
- research/native-claude-cold-prime-seed-multiplier-power-rate-183.md (SHA-256 90c2eaee1ee9cf890e4f2f58ca6ad4f25a7182ea4d344c9e001c6947a7433007)
- research/native-claude-cold-prime-signed-nonseed-price-182.md (SHA-256 c8023a9bece7318be9122e2b0ec2ef007780e7b83835bb2eac8e84e91b4161e6)
- research/cold-first-prefix-step-174.md (SHA-256 8d28cc54df9a57240886c543783a1dca331348a016dd359608e46b6fa177989e)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

