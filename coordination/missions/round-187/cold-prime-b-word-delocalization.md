# Proposed research mission: cold-prime-b-word-delocalization

Coordinator record: coordination/round-186.json
Record SHA-256: fc1582d2c07b0aacef5bbde79d30e880ef62e39d6e80fd74fe35c9b6e0c5fea0
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Is ||w||_inf,good / ||w||_2,n bounded uniformly in n for the B-generated Duhamel words w = L^b B_h L_S^a R_602 (Criterion D with an n-independent Lambda), uniformly on Q, both lifts; or does a fixed-height sup transfer through 611 hold?

## Why this call is worth making
Round 186 proved (Theorem N) that no size-only price of the non-seed multiplier works, while the actual operator is benign (||B_h S||_inf about 0.2, sup/RMS 4.1-5.3, close to sqrt(2 ln n)); bounded versus sqrt(ln n) growth is exactly what Criterion D needs settled.

## Current proof obligation
Criterion D with an n-independent ratio ||w||_inf,good / ||w||_2,n for the B-generated Duhamel words w = L^b B_h L_S^a R_602, uniformly on Q, both lifts; or a fixed-height sup transfer through 611; or a new signed price that sees row-multiplier cancellation. Plus D2-D4, (b4), (b-Jk), (b-T), the uniform complex stationary domain and derivative transfer. Proved frozen rate stays 1.066.

## Scope
Physical rows at p up to about 1e8 with the full nine-centre row (floating evidence), plus any proof attempt; inherit the Round 180 Criterion D statement exactly and the Round 186 Theorem N and hybrid seminorm as accepted (Proposition 3 conditional on D1-D4). Separate certified from floating; outward rounding. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: A provably bounded ratio closes the cold criterion through Criterion D, modulo D2-D4 and the stationary-domain inputs.
- If refuted: Provable sqrt(ln n) growth means Criterion D fails in its n-independent form; only a signed sup transfer or a new signed price remains.
- If inconclusive: Return the measured growth law and the term that blocks a proof.

## Read these sources

- research/round-185-acceptance.json (SHA-256 157de3b64f9e2a2140fdc46d342f3a3b1d19447fd51ab7492d00bde001f59f9d)
- research/round-186-acceptance.json (SHA-256 9f1a0ccb93a4ba4f75e8397105ae59418230856e0ee1e678f95f7169542626ee)
- research/native-claude-audit-186.md (SHA-256 2b61a763b2021d4447d176326807abdef9dea83c24b017d26d51c5f6dfbdbc48)
- research/native-claude-cold-prime-hybrid-price-186.md (SHA-256 6a597c9a88b7b6e370fffe17a97eda014302c245d0c5a254e067cfff4845f738)
- research/paley-186-cold-hybrid-witness.py (SHA-256 b810fa5115e98ce921b8e5bec9cae51d8641752f65aa6a26afcaefbd20f6aa6e)
- research/cold-growing-prefix-delocalization-180.md (SHA-256 3a8eb51ab257dc2b834142c7954357e533472676b4c5a06e1a0953db64e9b8c8)
- research/native-claude-cold-prime-signed-nonseed-price-182.md (SHA-256 c8023a9bece7318be9122e2b0ec2ef007780e7b83835bb2eac8e84e91b4161e6)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

