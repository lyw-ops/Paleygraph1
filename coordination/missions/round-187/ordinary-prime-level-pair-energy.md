# Proposed research mission: ordinary-prime-level-pair-energy

Coordinator record: coordination/round-186.json
Record SHA-256: fc1582d2c07b0aacef5bbde79d30e880ef62e39d6e80fd74fe35c9b6e0c5fea0
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
For the actual g = |f|^2 with the cap, can the pair energy E(U;U') of level-set pieces U in S_a, U' in S_a' be bounded with less BSG loss than Lemma M plus Reiher-Schoen gives, ideally (HC') E(U;U') << p^(4/3) (a a')^(-2) for a, a' in [c p^(-1/6), 1], or at least with a pair excess kappa e, kappa < 11/12, for example through a Lemma M variant whose structured side uses Lemma S1 (E^x(W) >= t^2 |W|^4/(C sqrt p)) directly with no BSG piece?

## Why this call is worth making
Round 186 moved delta_C from 1/664 to 5/296 and located the binding term exactly (BSG doubling K^4 and size loss K^(-1/2) at heights p^(-e), e < 1/15); no Reiher-Schoen-shape BSG passes delta_C ~ 0.0239, so the lever is a K-free or BSG-free level-set input.

## Current proof obligation
One-match: (HC') E(U;U') << p^(4/3) (a a')^(-2) for level-set pieces at heights [c p^(-1/6), 1] reaches the scheme floor sup C = p^(4/3+o(1)), covariance p^(43/24+o(1)); any pair excess kappa e with kappa < 11/12 gives delta_C = (1/24)/(1 + 8 kappa/5); reaching O(p^(3/2)) needs a non-point-plane input (floor p^(7/4)) and the generic six-word class below p^(9/2). First mass: X = O(p^(1+1/1280)) needs a prime-only input at light levels. Support energy only as a power rate gamma < 3/8. Propagate delta_C to the Round 176/180 fixed-a generic squared mass. Generic J sum and zero-match unchanged.

## Scope
Actual g with the cap n max nu <= C_cap sqrt p; no near-critical input unless stated and marked. Use Round 186 Lemma M, Proposition P, Theorem B and the corrected (HC') height range as accepted, and Round 185 Lemmas 4-5. Keep sup C separate from X. Quote any new external theorem from its source with hypotheses verified at the scales used. Exact exponent arithmetic. Large-p models should reach heights p^(-e) with e visibly positive (p >= 1e7 or tailored laws); floating results are evidence only. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: (HC') gives sup C = O(p^(4/3+o(1))) and one-match covariance p^(43/24+o(1)), the floor of point-line pricing; a partial kappa gives delta_C = (1/24)/(1 + 8 kappa/5).
- If refuted: A model of admissible level sets with E(U;U') >= p^(4/3+c) (a a')^(-2) at some height in range shows point-line pricing of sup C stalls near 2125/1184; the next lever is a non-point-plane input.
- If inconclusive: Return the best kappa and the configuration that binds.

## Read these sources

- research/round-185-acceptance.json (SHA-256 157de3b64f9e2a2140fdc46d342f3a3b1d19447fd51ab7492d00bde001f59f9d)
- research/round-186-acceptance.json (SHA-256 9f1a0ccb93a4ba4f75e8397105ae59418230856e0ee1e678f95f7169542626ee)
- research/native-claude-audit-186.md (SHA-256 2b61a763b2021d4447d176326807abdef9dea83c24b017d26d51c5f6dfbdbc48)
- research/native-claude-ordinary-prime-sup-c-heavy-price-186.md (SHA-256 9220d8860c7039ce143e730e76946a903946a16900f167b29666d4854045f0d3)
- research/paley-186-supc-exponents.py (SHA-256 93debdd567a6b99fb5c77dc382f72dc2e895b478bd9e9dfd2acb2b67f7a67b8f)
- research/paley-186-audit-supc-check.py (SHA-256 3380c48f1954d2ca7bcbab5447f1df30e80c3923841c3bcaa4f3becb8e0b6521)
- research/native-claude-ordinary-prime-near-critical-band-autocorrelation-185.md (SHA-256 4f0cd362412e92ef37163b039bc010bd4c837036250dbe4421ec13594af84473)
- research/native-claude-ordinary-prime-shifted-level-energy-182.md (SHA-256 5c34d1fd84ae4b3bcc82a984d7f4fc1a29fd5c21f8bb24df73ac1b524750a331)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

