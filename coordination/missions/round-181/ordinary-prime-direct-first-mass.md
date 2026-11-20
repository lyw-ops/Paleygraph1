# Proposed research mission: ordinary-prime-direct-first-mass

Coordinator record: coordination/round-180.json
Record SHA-256: 7037e26f9bd685e695f4b90801d59b0e2027d8e93c2bd9db0f846d6ce65accf5
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Is the weighted first mass M_w=sum_s w(s)P_s of the actual positive diagonal O(p^(1+1/1280)), proved directly rather than by Cauchy–Schwarz from the second moment?

## Why this call is worth making
Round 180 showed D_0+D_1<=4R_*M_w with R_*=O(p^(1/2-1/1280)) and each generic class D_J<=2G M_w. Currently M_w=O(p^(11/8)) only through Round 179's diagonal. A direct first-mass bound O(p^(1+1/1280)) closes J in {0,1} at target scale and lowers each generic class to O(p^(3/2+1/1280)).

## Current proof obligation
The sufficient whole diagonal O(p^(3/2)) through the generic J sum (still O(p^(9/4)), positive classes, no J cancellation), or a direct first mass M_w=O(p^(1+1/1280)) for J in {0,1}. The one-match covariance needs O(p^(3/2)) by a route avoiding E(mu), which stops at p^(13/8) when M_1 is comparable to p. The zero-match estimate is unchanged.

## Scope
Actual g, w=g(1-g), G, physical masks and nonzero interior of Round 178, the cross-ratio chart of Round 180 (A,C,Y,D as cross-ratios of X,pi,rho), counting norms. Keep w(s) and as many of the four amplitudes as possible; state which are majorized by one. Note M_w is a sum over lines e and outputs s of w(s)g(A)g(C)g(Y)g(D): exploit that Y and D do not depend on s and A,C are Möbius images of X with the same line. Distinguish proved bounds from heuristics.

## How the result changes the next decision
- If supported: Closes the classes J in {0,1} at O(p^(3/2)) and reduces the sufficient diagonal to the generic J sum alone.
- If refuted: A lower bound M_w>>p^(1+1/1280) under the proved constraints shows Criterion 7 of Round 180 cannot be met and J in {0,1} needs a second-copy saving.
- If inconclusive: Return the precise exponent obtained and the line or output class that blocks it.

## Read these sources

- research/round-179-acceptance.json (SHA-256 2c7ee0603b7d5ebdac1773b4b43573530fcacc84c81f2e8b345b0fdafd1ec414)
- research/round-180-acceptance.json (SHA-256 489e1a259667fe13a6f2e6893358de175eaf8240bc49f02bb9679186702e128a)
- research/ordinary-paired-J-cross-ratio-180.md (SHA-256 f800b53b7d6678f7d12f79352255261a0808823e137d79d898c286d1693ef0fa)
- research/ordinary-affine-triple-diagonal-179.md (SHA-256 1511abc52dacf6b6785fe7ff9544b9c55b473e9e7dc0fa6fc10ead61983e42ee)
- research/ordinary-parabolic-row-mean-square-178.md (SHA-256 89d64995b12626f4983f1594fe3e80f266b972b274737f4e28647f6c91d02282)
- research/ordinary-weighted-affine-vertical-saving-173.md (SHA-256 61e959f2defb68dec2f44205fb1601b0e98e210f3b45b38aed9ed68c3e3a2023)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

