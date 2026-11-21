# Proposed research mission: ordinary-prime-near-critical-band-autocorrelation

Coordinator record: coordination/round-184.json
Record SHA-256: 46fb9ed1fd4d060744d3e6ccc8211580e7159c5e10d4ed8da6bb74e0e735d2a4
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
For the actual near-critical g, is sup_{lambda!=1} C(lambda) = O(p^(11/8-delta)), or max_xi W_xi = O(p^(11/8-delta)), or sum_xi W_xi^(3/2) = O(p^(43/16-delta)), for some delta > 0, using structure of the level sets S_t, p^(-1/8) < t < p^(-1/192), of the flat near-critical law beyond Lemma S1 (one-match form of cand:slope-row-mass-x)?

## Why this call is worth making
Round 184 showed that the one-match threshold is epsilon < 3/8, that Round 180's sup C = O(p^(11/8)) sits exactly at it, and that every level outside the band is already harmless; the square-field method cap does not apply to the band, and the flat law makes the band level sets large-spectrum sets of S, a structured object not yet exploited.

## Current proof obligation
One-match: sup_{lambda!=1} C(lambda) or max_xi W_xi = O(p^(11/8-delta)), or sum_xi W_xi^(3/2) = O(p^(43/16-delta)), from structure of the band level sets beyond Lemma S1; reaching O(p^(3/2)) also needs a non-point-plane input (floor p^(7/4)) and the generic six-word class below p^(9/2). First mass: X = O(p^(1+1/1280)) via a quantitative prime-only input or signed cancellation from w (prototype E^x(1-P_N) = O(N^(2+o(1))) for geometric progressions N asymp sqrt p). Support energy only as n E(nu) - 1 = O(p^gamma), gamma < 3/8. Generic J sum O(p^(9/4)) and zero-match estimate unchanged.

## Scope
Actual mu on the Round 171 chart, counting norms; near-critical inputs as accepted (Round 183 sector concentration and M_1 = (1+o(1))p, Round 20 flattening and gap theorem, Round 151 coset-mass exclusion, Round 184 Theorem 2 overlap dichotomy). Keep sup C, max W and sum W^(3/2) separate. Use Round 184 Propositions 1-3 (slope-row-mass report) as accepted. Quote any new external input (large-spectrum / Chang-type structure, incidence bounds) from its source with hypotheses. Models: flat laws with band mass (the ap+rand family), not g_H or the square control; floating results are evidence only. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: One-match covariance O(p^(115/64-delta/8+o(1))), the first headline move since Round 180.
- If refuted: A flat admissible family with sup C >= p^(11/8-o(1)) shows Round 180 is sharp for these inputs; the one-match route then needs a non-point-plane input and the slope-row-mass line is retired for one-match use.
- If inconclusive: Return the best delta for each quantity and the band configuration that blocks.

## Read these sources

- research/round-183-acceptance.json (SHA-256 aae5b4aa2a8e1a8b216249c1f01ad9b1d3676853325a5b5cc30a9174db9f0fa9)
- research/round-184-acceptance.json (SHA-256 c30660213a26e69b172ce6e7f21a1fe33fe4eba5bfcec7fd976247ebd5d5e3ef)
- research/native-claude-audit-184.md (SHA-256 b074da5e7a830b2220d10e67ebf27fae20e75ee513002daa56714baa7afb2b2f)
- research/native-claude-ordinary-prime-near-critical-slope-row-mass-184.md (SHA-256 85702949b82c262a1d68dce098c89c995308880d63fbdc35765d571e6e6c02ec)
- research/native-claude-ordinary-prime-near-critical-support-energy-184.md (SHA-256 9cac897617cced4bb48a97cb8c73f904a76958daf38798b2f4748a816a45c1fa)
- research/paley-184-rowmass-models.py (SHA-256 3ce9208c77e3fd125ca9ec45b997926c030984fe49bb6e62999f79b42e3743ba)
- research/ordinary-mixed-row-autocorrelation-180.md (SHA-256 357f5058dd8ef16cf330a252680252d77c815ec5f3f6175e86bfa904d68e85aa)
- research/ordinary-weighted-slope-product-incidence-178.md (SHA-256 9e4589c664dc84d30e86206288183a3af9dfb1ae29f8d49ebd6faa1db01f1d71)
- research/native-claude-ordinary-prime-shifted-level-energy-182.md (SHA-256 5c34d1fd84ae4b3bcc82a984d7f4fc1a29fd5c21f8bb24df73ac1b524750a331)
- research/ordinary-prime-coset-spread-151.md (SHA-256 2029d03cff0d88b9afb13a1e6a2957cee9d30842213d7ca79240432047823282)
- research/anchored-repair-20.md (SHA-256 141a0fb1c0017bae3c3fe4c900259be588bddfa1333dc8c65c7c504df5bf3721)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

