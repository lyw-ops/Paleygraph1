# Proposed research mission: cold-prime-picard-leaf-inequivalence

Coordinator record: coordination/round-184.json
Record SHA-256: 46fb9ed1fd4d060744d3e6ccc8211580e7159c5e10d4ed8da6bb74e0e735d2a4
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
In the compact model, are the transported simples of the Picard pieces h_1, L_S^j h_1 (j >= 1) and L_S^j Q_1 mutually inequivalent across pieces and paths, or do some coincide with opposite-sign coefficients; accordingly, what is the exact signed model A_X-price of h - h_1 (and of h) to depth 3, against the certified allowances 0.3411 and 0.7499?

## Why this call is worth making
Round 184 reduced the cold dimension-price route to the single input A_X(h - h_1) < 0.3411; the unsigned path-summed model price is about 0.51-0.57, an upper bound that equals the model price exactly when no two paths produce the same simple with opposite signs. This finite exact computation settles the per-simple A route either way.

## Current proof obligation
A_X(V_602 - S - h_1) < 0.3411 (joint) or A_X(V_602 - S) < 0.7499, uniformly on Q, both lifts; decisive: whether transported simples of different Picard pieces (h_1, L_S^j h_1, L_S^j Q_1) coincide with opposite signs (if not, the model price is >= 0.50 and the per-simple A route is retired). Plus D2-D4 and the readings (b4), (b-Jk), (b-T). Uniform complex stationary domain and derivative transfer remain separate.

## Scope
Compact model under (b4), (b-Jk), (b-T); identify simples by their full two-fibre weight data and boundary characters, and state the identification criterion used (Round 80 inequivalence extended to J^odd multipliers on roots K(J^(2i)), proved or stated as a hypothesis). Use Propositions A, B, C and D1 of research/native-claude-cold-prime-h1-product-rule-184.md as accepted in Round 184 with the audit's corrections. Exact arithmetic; certified lower bounds for the model price, uniform on Q, both lifts; outward rounding; separate exact from floating. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: No opposite-sign collisions: model A_X(h - h_1) >= 0.50 > 0.3411 and A_X(h) about 0.99 > 0.7499 retire the per-simple dimension-price route; the cold route returns to Criterion D, sup transfer or a hybrid price.
- If refuted: Cancellation brings the signed model price below 0.3411: the route stays alive and the next call certifies A_X(h - h_1) for the actual field uniformly on Q, both lifts.
- If inconclusive: Return the certified lower bound obtained and the list of colliding simples with their signs.

## Read these sources

- research/round-183-acceptance.json (SHA-256 aae5b4aa2a8e1a8b216249c1f01ad9b1d3676853325a5b5cc30a9174db9f0fa9)
- research/round-184-acceptance.json (SHA-256 c30660213a26e69b172ce6e7f21a1fe33fe4eba5bfcec7fd976247ebd5d5e3ef)
- research/native-claude-audit-184.md (SHA-256 b074da5e7a830b2220d10e67ebf27fae20e75ee513002daa56714baa7afb2b2f)
- research/native-claude-cold-prime-h1-product-rule-184.md (SHA-256 a45402f0da4ed714a095fda92abccf0fb41dd8724b39fbf8e47cd70b32529a90)
- research/paley-184-cold-h1-product-ratio.py (SHA-256 fa25f9bf78a61dc0278887548ca2dda9bcbc3fd3774964557f3ead4a4cafdcd7)
- research/paley-184-cold-h-rest-diagnostic.py (SHA-256 53dbaec5f52a2ce4e2147fd7543f2dba9a0c34dbdb8dbb946d4410ff6e10a0ed)
- research/paley-184-audit-cold-check.py (SHA-256 ad19165d93c679cab11802cf5aa08ca46d42b6b23a9f78f0aba1be5550186995)
- research/native-claude-cold-prime-seed-multiplier-power-rate-183.md (SHA-256 90c2eaee1ee9cf890e4f2f58ca6ad4f25a7182ea4d344c9e001c6947a7433007)
- research/native-claude-cold-prime-signed-nonseed-price-182.md (SHA-256 c8023a9bece7318be9122e2b0ec2ef007780e7b83835bb2eac8e84e91b4161e6)
- research/shifted-resolvent-96.md (SHA-256 ec9c2eb7e001e71142295e67717fee4499bd89ff49f660a51a8d4ae1dec41a36)
- research/cold-first-prefix-step-174.md (SHA-256 8d28cc54df9a57240886c543783a1dca331348a016dd359608e46b6fa177989e)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

