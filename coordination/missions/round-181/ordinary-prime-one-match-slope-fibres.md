# Proposed research mission: ordinary-prime-one-match-slope-fibres

Coordinator record: coordination/round-180.json
Record SHA-256: 7037e26f9bd685e695f4b90801d59b0e2027d8e93c2bd9db0f846d6ce65accf5
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Can the one-match covariance be bounded at O(p^(3/2)) (or any power below O(p^(115/64))) directly by slope fibres h=(a,c), using the new fixed-slope first masses sum_c Delta(a,c)=C(a)=O(p^(11/8)) for a≠1 and the translation overlaps of the level sets, without passing through the energy E(mu) and Rudnev–Shkredov?

## Why this call is worth making
Round 180 improved the one-match covariance to O(p^(115/64)) but proved that any route through E(mu) and the Rudnev–Shkredov second norm stops at p^(13/8) when M_1 is comparable to p. The new fixed-slope masses C(a)=O(p^(11/8)) are the first input that prices individual slope fibres.

## Current proof obligation
The sufficient whole diagonal O(p^(3/2)) through the generic J sum (still O(p^(9/4)), positive classes, no J cancellation), or a direct first mass M_w=O(p^(1+1/1280)) for J in {0,1}. The one-match covariance needs O(p^(3/2)) by a route avoiding E(mu), which stops at p^(13/8) when M_1 is comparable to p. The zero-match estimate is unchanged.

## Scope
Use the actual mu(r,b)=g(Y)g(D) with the square mask and interior exclusions of Round 171, the twisted physical chart of Rounds 169 and 173 and its one-match normalization, the actual w and the D amplitudes, counting norms. Write Delta(h)=sum_j mu(j)mu(jh) and m_U(h)=|U∩hU| for level sets U of the actual h_t. Treat a=1 (translations) separately. State any external incidence or sum-product input exactly with its hypotheses. Report exponents exactly and say which weights are majorized by one.

## How the result changes the next decision
- If supported: A bound O(p^(3/2)) proves the one-match estimate, leaving the zero-match estimate and the whole diagonal for the ordinary route; any power below 115/64 is an accepted improvement.
- If refuted: A configuration of slope-fibre masses consistent with all proved constraints and forcing the covariance above p^(3/2) shows the one-match target needs input beyond fibre masses.
- If inconclusive: Return the exact remaining fibre class (range of a, size of Delta(a,·), richness of m_U) with its verified bound.

## Read these sources

- research/round-179-acceptance.json (SHA-256 2c7ee0603b7d5ebdac1773b4b43573530fcacc84c81f2e8b345b0fdafd1ec414)
- research/round-180-acceptance.json (SHA-256 489e1a259667fe13a6f2e6893358de175eaf8240bc49f02bb9679186702e128a)
- research/ordinary-mixed-row-autocorrelation-180.md (SHA-256 357f5058dd8ef16cf330a252680252d77c815ec5f3f6175e86bfa904d68e85aa)
- research/ordinary-weighted-slope-product-incidence-178.md (SHA-256 9e4589c664dc84d30e86206288183a3af9dfb1ae29f8d49ebd6faa1db01f1d71)
- research/ordinary-one-match-twisted-physical-169.md (SHA-256 8f683813155b15dd91aea2a0f5cbbc01aa3e704501212007bd7ae63c975f1d77)
- research/ordinary-two-torus-projective-overlap-176.md (SHA-256 9d18188f1e3faced380ba0903f0b4c8577db72f794239a7095c41015aa194d99)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

