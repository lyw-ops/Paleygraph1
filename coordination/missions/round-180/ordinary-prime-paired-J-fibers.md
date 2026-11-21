# Proposed research mission: ordinary-prime-paired-J-fibers

Coordinator record: coordination/round-179.json
Record SHA-256: 0d2b2f3633381aa466d6cd694d8380cdab8f0c6b54af01385fd0e33eacda2741
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Do the genuine paired affine maps, sorted by the exact invariant J=d(k+d-1)/k, admit a summed bound over J≠0 below the completed affine triple moment, with the J=0 class priced separately, while retaining both D and D' amplitudes and the actual w(s)?

## Why this call is worth making
Round 179 proved the J invariance of the paired maps h_k, h_{λ/k}, priced each single J class at O(p^2) (O(p^(2-1/640)) for J≠0), and showed the completed triple moment Σ_h m(h)^3 has lower bound (p−1)G^6/p^2, so it cannot reach target scale when G is comparable to sqrt(p). A summed J estimate is the next place where a power saving below O(p^(9/4)) could come from the genuine structure rather than the completion.

## Current proof obligation
Reach O(p^(3/2)) while retaining both D amplitudes and w; test the summed matched J classes, with J=0 separated. The completed triple moment itself has lower bound (p−1)G^6/p^2, hence cannot reach target scale when G is comparable to sqrt(p). Separate one-match and zero-match estimates remain open.

## Scope
Use the actual g, w, G, physical masks and nonzero interior of Round 178 with counting norms, p≡1 mod 4 prime. Keep the exact two-copy product chart of Round 179: (x−v)(u−v)=f_0(v)(s−1), D=s/(axu), x'=h_k(x), u'=h_{λ/k}(u), λ=f_0(v')/f_0(v). Do not majorize D, D' and w by one before the J sorting; if a step does so, state it and what it loses. Treat J=0 (d=0 or k+d=1) as its own class. Do not conflate distinct b with distinct r or k, and do not use a single-label coincidence cut that the chart does not provide. Report exponents exactly.

## How the result changes the next decision
- If supported: A summed J bound at O(p^(3/2)) proves the sufficient whole actual diagonal; any power saving below 9/4 is a new accepted reduction, and the next call targets the remaining J range or the zero class.
- If refuted: A proved lower bound or explicit configuration showing the summed J classes carry mass ≫ p^(3/2) even with D, D', w retained would refute this sufficient diagonal as stated, forcing the ordinary route to a different completion or to the one-match criterion alone.
- If inconclusive: Return the precise remaining J range with its verified bound and the exact quantity (in J, k, d, v, v') that would need to be estimated, so a later call can attack only that class.

## Read these sources

- research/round-178-acceptance.json (SHA-256 10dceeac23ed58c55637d159d8804d83e445c239ccc84608195160ae3e0d394e)
- research/round-179-acceptance.json (SHA-256 2c7ee0603b7d5ebdac1773b4b43573530fcacc84c81f2e8b345b0fdafd1ec414)
- research/ordinary-affine-triple-diagonal-179.md (SHA-256 1511abc52dacf6b6785fe7ff9544b9c55b473e9e7dc0fa6fc10ead61983e42ee)
- research/ordinary-parabolic-row-mean-square-178.md (SHA-256 89d64995b12626f4983f1594fe3e80f266b972b274737f4e28647f6c91d02282)
- research/ordinary-weighted-affine-vertical-saving-173.md (SHA-256 61e959f2defb68dec2f44205fb1601b0e98e210f3b45b38aed9ed68c3e3a2023)
- research/ordinary-shifted-energy-four-factor-diagonal-177.md (SHA-256 8d230eebf51c30edfe4c55b4655036e455e90d7f71ad95ec49d1e909f3aacb34)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

