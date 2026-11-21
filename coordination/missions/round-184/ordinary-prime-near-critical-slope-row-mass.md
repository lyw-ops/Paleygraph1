# Proposed research mission: ordinary-prime-near-critical-slope-row-mass

Coordinator record: coordination/round-183.json
Record SHA-256: 1231bfe2ad7af3148d2574dab427d0f9c6c3e831b6207a8ccef72451daab4f8e
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
For the actual near-critical g on (NC), is max_xi W_xi = O(p^(1+epsilon)) for some epsilon < 3/16, where W_xi = sum_r m(r) m(xi/r), and is X = sum_r m(r)^2 = E_Q(h) = O(p^(1+1/1280)), using the near-critical structure that (H1)/(H2)/(H4)-only arguments ignore (shared estimate cand:slope-row-mass-x)?

## Why this call is worth making
Both Round 183 ordinary calls reduced to this one estimate: the first-mass report showed that (H1)/(H2)/(H4) alone force a bound on X itself (w is worth only 3/4 in the non-near-critical family g_H), and the row-deleted report showed that epsilon < 3/16 already moves the one-match exponent 115/64.

## Current proof obligation
Shared cand:slope-row-mass-x: for the actual near-critical g, max_xi W_xi = O(p^(1+epsilon)) with epsilon<3/16 (one-match below 115/64) and X = E_Q(h) = O(p^(1+1/1280)) (first mass target, D_0+D_1 = O(p^(3/2))). One-match target O(p^(3/2)) additionally needs the generic six-word class below p^(9/2). Decide E(S)/|S|^3 -> 0 on (NC) (equivalently sum g^2 = o(sqrt p)). Generic J sum O(p^(9/4)) and zero-match estimate unchanged.

## Scope
Actual mu(r,b)=g(Y)g(D) on the Round 171 chart, h(z)=g(1-z), m(r)=c_h(1-r), counting norms. Use the near-critical inputs as accepted: sector concentration G_{-rho}=O(1) and M_1=(1+o(1))p (Round 183, from Round 151), the flat law on |S| ~ m_0 (Round 20 flattening), Round 151's fixed Fourier mass outside coset unions; state each with its round and line. Keep the max-convolution version (max_xi W_xi) and the X version separate. Current verified values: X <= E^x(h) = O(p^(34/23)) (Round 182; BSG via Reiher-Schoen 2024 Theorem 1.2) and Round 180's sup_lambda C(lambda) = O(p^(11/8)). Models must be near-critical (flat law with m_eff ~ m_0, sector-concentrated), not g_H; floating results are evidence only. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: epsilon < 3/16 for max_xi W_xi gives one-match covariance O(p^(7/4+epsilon/4+o(1))), below 115/64; epsilon <= 1/1280 for X closes the first mass and D_0+D_1 = O(p^(3/2)).
- If refuted: A near-critical admissible family with X >= p^(1+delta) shows the shared route needs signed cancellation from w for the first mass and a non-point-plane input for the one-match covariance.
- If inconclusive: Return the best exponent for max_xi W_xi and for X from (NC) structure, and the exact level-set configuration that blocks.

## Read these sources

- research/round-182-acceptance.json (SHA-256 78471bc51e0eaed7c99f92141d3a573d4a2d55f8fc4d7510c187da60e976bec6)
- research/round-183-acceptance.json (SHA-256 aae5b4aa2a8e1a8b216249c1f01ad9b1d3676853325a5b5cc30a9174db9f0fa9)
- research/native-claude-audit-183.md (SHA-256 e2803038572b7c521b32d336c8cec7cf2cbdd05f1856aef765f888c551e43f32)
- research/native-claude-ordinary-prime-first-mass-fibre-dilation-183.md (SHA-256 d1e835add14e50720fbb7a15882b576cea33457a37335534237b6f61c44d6160)
- research/native-claude-ordinary-prime-row-deleted-one-match-183.md (SHA-256 9af6768f701354214a612f0bbe9fc52b38910517fac95095aae3fe47f085a26a)
- research/ordinary-prime-coset-spread-151.md (SHA-256 2029d03cff0d88b9afb13a1e6a2957cee9d30842213d7ca79240432047823282)
- research/anchored-repair-20.md (SHA-256 141a0fb1c0017bae3c3fe4c900259be588bddfa1333dc8c65c7c504df5bf3721)
- research/ordinary-weighted-slope-product-incidence-178.md (SHA-256 9e4589c664dc84d30e86206288183a3af9dfb1ae29f8d49ebd6faa1db01f1d71)
- research/ordinary-mixed-row-autocorrelation-180.md (SHA-256 357f5058dd8ef16cf330a252680252d77c815ec5f3f6175e86bfa904d68e85aa)
- research/native-claude-ordinary-prime-shifted-level-energy-182.md (SHA-256 5c34d1fd84ae4b3bcc82a984d7f4fc1a29fd5c21f8bb24df73ac1b524750a331)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

