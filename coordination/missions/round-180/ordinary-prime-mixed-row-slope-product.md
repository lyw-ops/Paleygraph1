# Proposed research mission: ordinary-prime-mixed-row-slope-product

Coordinator record: coordination/round-179.json
Record SHA-256: 0d2b2f3633381aa466d6cd694d8380cdab8f0c6b54af01385fd0e33eacda2741
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Can the summed weighted slope-product distribution Σ_ξ W_ξ^(3/2) in the actual point-plane energy be improved below the Round 178 scale by retaining the genuine mixed row structure (m(r) together with the shifted or inverted row correlations), rather than max W_ξ and interpolation?

## Why this call is worth making
Round 178 gave E(μ)=O(p^(11/4−3/836)) for the genuine right energy, with the W_ξ^(3/2) term dominant. Round 179 showed that Young's inequality at exponent 6/5 plus interpolation between row first and second norms reproduces the same bound, so any gain must use structure of the actual rows.

## Current proof obligation
Reach O(p^(3/2)) while retaining both D amplitudes and w; test the summed matched J classes, with J=0 separated. The completed triple moment itself has lower bound (p−1)G^6/p^2, hence cannot reach target scale when G is comparable to sqrt(p). Separate one-match and zero-match estimates remain open.

## Scope
Actual μ(r,b)=g(Y)g(D) with the square mask and interior exclusions of Round 171, counting normalization, the point-plane chart of Round 178. Keep W_ξ=Σ_r m(r)m(ξ/r) and state any extra arithmetic input with its exact hypotheses. Disclose whether a gain changes the whole right energy E(μ), the weighted affine incidence and the one-match bound for H_α.

## How the result changes the next decision
- If supported: A power gain in Σ_ξ W_ξ^(3/2) improves the right energy and propagates through the Round 178 one-match criterion; the next call then checks whether it reaches the one-match target.
- If refuted: A proved or explicit lower bound for Σ_ξ W_ξ^(3/2) from the actual rows shows this energy cannot improve, and the one-match estimate must avoid the point-plane route.
- If inconclusive: Return the precise row correlation that would be needed, with its exact size requirement.

## Read these sources

- research/round-178-acceptance.json (SHA-256 10dceeac23ed58c55637d159d8804d83e445c239ccc84608195160ae3e0d394e)
- research/round-179-acceptance.json (SHA-256 2c7ee0603b7d5ebdac1773b4b43573530fcacc84c81f2e8b345b0fdafd1ec414)
- research/ordinary-weighted-slope-product-incidence-178.md (SHA-256 9e4589c664dc84d30e86206288183a3af9dfb1ae29f8d49ebd6faa1db01f1d71)
- research/ordinary-shifted-energy-four-factor-diagonal-177.md (SHA-256 8d230eebf51c30edfe4c55b4655036e455e90d7f71ad95ec49d1e909f3aacb34)
- research/ordinary-affine-line-energy-171.md (SHA-256 55418fa1dd79a53b5842d88c369c0c2da3ddb63f8680345b69fbe2679b626707)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

