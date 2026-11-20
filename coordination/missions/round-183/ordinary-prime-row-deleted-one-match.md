# Proposed research mission: ordinary-prime-row-deleted-one-match

Coordinator record: coordination/round-182.json
Record SHA-256: bd56aa4c740ba06b77db3c9c24ca60e4681feb6d3ac85b3e9d27dda6dd40680f
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Is the row-deleted criterion ||R pi(mu)||_op = O(p^(3/4)) provable for the actual mu — first by deciding whether sum g^2 = o(sqrt p) for the actual law (which relaxes the target through (b1''')), and otherwise through the k=3 translation discrepancy of slope-closed six-words below its verified O(p^(177/32))?

## Why this call is worth making
Round 182 showed b1' is saturated by the degenerate output row s=1 under (H_sat), that the physical one-match criterion never sees that row, and that the k=3 discrepancy is the blocking term (need O(p^(144/32))); whether sum g^2 is o(sqrt p) decides whether the row itself matters.

## Current proof obligation
One-match O(p^(3/2)) via b1'' (k=3 translation discrepancy of slope-closed six-words: verified O(p^(177/32)), need O(p^(144/32))), or via sum g^2=o(sqrt p) and (b1'''). Direct first mass O(p^(1+1/1280)) without the BSG size loss (the BSG-plus-Young scheme is capped at E^x(h)=O(p^(4/3))). Generic J sum O(p^(9/4)) and zero-match estimate unchanged.

## Scope
Actual mu(r,b)=g(Y)g(D) on the Round 171 chart, the twisted physical chart of Rounds 169/173, the actual law omega with max omega = O(p^(-1/2)), counting norms. Part 1: decide sum g^2 for the actual law using sum_alpha omega(alpha)^2 = 2 sum g^2/(p-1) and the square-class balance, with every structural fact about the near-critical law cited to its accepted round. Part 2: compute tr((R pi pi* R)^3) exactly for p <= 677 split by six-word type, and seek a point-conic incidence input with exact hypotheses for the dominant type. Use the Round 182 trace identity and interlacing as accepted. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: ||R pi(mu)||_op = O(p^(3/4)) proves the one-match estimate O(p^(3/2)); sum g^2 = O(p^(1/2-delta)) alone relaxes the operator target by p^(delta/2) and is an accepted improvement.
- If refuted: A proof that sum g^2 asymp sqrt p for the actual law together with a word type whose exact count exceeds p^(9/2) by a power in models shows the operator-norm route cannot close the one-match estimate.
- If inconclusive: Return the exact six-word type and its verified bound, and the status of sum g^2.

## Read these sources

- research/round-181-acceptance.json (SHA-256 ad983e94b84fce4466bd29303e579f9bbf1d34576ec81bd92a27ab5f63bb0910)
- research/round-182-acceptance.json (SHA-256 78471bc51e0eaed7c99f92141d3a573d4a2d55f8fc4d7510c187da60e976bec6)
- research/native-claude-ordinary-prime-one-match-operator-norm-182.md (SHA-256 b5362892c520902de0db58761bbaaec27991414388073c21743b76287db216ae)
- research/native-claude-audit-182.md (SHA-256 82edca1551678b235a57bc8f945d8ce24135501c1949834f8641ec82f77eef79)
- research/paley-182-opnorm-identities.py (SHA-256 0de89988d380d4912f43b91c09e856611cb3cf7523dbc10acb4e1bae8b0a93d7)
- research/ordinary-one-match-twisted-physical-169.md (SHA-256 8f683813155b15dd91aea2a0f5cbbc01aa3e704501212007bd7ae63c975f1d77)
- research/ordinary-affine-line-energy-171.md (SHA-256 55418fa1dd79a53b5842d88c369c0c2da3ddb63f8680345b69fbe2679b626707)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

