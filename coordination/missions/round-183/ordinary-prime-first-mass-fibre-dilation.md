# Proposed research mission: ordinary-prime-first-mass-fibre-dilation

Coordinator record: coordination/round-182.json
Record SHA-256: bd56aa4c740ba06b77db3c9c24ca60e4681feb6d3ac85b3e9d27dda6dd40680f
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Is M_w = sum_r sum_{b != b'} mu(r,b) mu(r,b') w(b/b') = O(p^(1+1/1280)) when treated directly as a w-weighted dilation correlation inside the slope fibres of the actual mu, for example through a per-slope-fibre multiplicative energy rather than the whole-level E^x(1-S_t)?

## Why this call is worth making
The Round 182 audit proved the exact identity rewriting M_w as a fibre dilation correlation of the one-match weight mu, and Round 182 showed the level-set route (BSG pieces plus Young) cannot go below E^x(h)=O(p^(4/3)); the fibre form keeps w and every amplitude and avoids the BSG size loss.

## Current proof obligation
One-match O(p^(3/2)) via b1'' (k=3 translation discrepancy of slope-closed six-words: verified O(p^(177/32)), need O(p^(144/32))), or via sum g^2=o(sqrt p) and (b1'''). Direct first mass O(p^(1+1/1280)) without the BSG size loss (the BSG-plus-Young scheme is capped at E^x(h)=O(p^(4/3))). Generic J sum O(p^(9/4)) and zero-match estimate unchanged.

## Scope
Actual g, w=g(1-g), mu(r,b)=g(Y)g(D) on the Round 171 chart with the square mask and Y != D, counting norms. Re-derive the identity of research/native-claude-audit-182.md section 4 (checked at p=29,53 by research/paley-182-audit-shifted-energy-check.py) before using it. Use Lemma SE and E^x(h)=O(p^(34/23)) from Round 182 where helpful. State whether w is kept or majorized; state any incidence or character-sum input exactly with hypotheses. Compute M_w and its restriction to the large multiplicative spectrum of w in subgroup-mixture and Fejér models (floating evidence) and say whether a per-fibre energy reaches p^(1+o(1)) there. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: M_w=O(p^(1+1/1280)) closes J in {0,1} at target scale (D_0+D_1=O(p^(3/2))) and lowers each generic J class to O(p^(3/2+1/1280)).
- If refuted: An admissible family consistent with the proved constraints on g in which the fibre dilation correlation grows by a power over p shows the first mass needs signed cancellation from w, not positivity.
- If inconclusive: Return the exact fibre class (slope r, size of the fibre, multiplicative structure of b) where the bound fails, with its verified bound.

## Read these sources

- research/round-181-acceptance.json (SHA-256 ad983e94b84fce4466bd29303e579f9bbf1d34576ec81bd92a27ab5f63bb0910)
- research/round-182-acceptance.json (SHA-256 78471bc51e0eaed7c99f92141d3a573d4a2d55f8fc4d7510c187da60e976bec6)
- research/native-claude-ordinary-prime-shifted-level-energy-182.md (SHA-256 5c34d1fd84ae4b3bcc82a984d7f4fc1a29fd5c21f8bb24df73ac1b524750a331)
- research/native-claude-audit-182.md (SHA-256 82edca1551678b235a57bc8f945d8ce24135501c1949834f8641ec82f77eef79)
- research/paley-182-audit-shifted-energy-check.py (SHA-256 c2dbe98686bae3a2ba9b54360e7da480960d9667a3e68ac802cbe7acaf1370ca)
- research/ordinary-paired-J-cross-ratio-180.md (SHA-256 f800b53b7d6678f7d12f79352255261a0808823e137d79d898c286d1693ef0fa)
- research/ordinary-mixed-row-autocorrelation-180.md (SHA-256 357f5058dd8ef16cf330a252680252d77c815ec5f3f6175e86bfa904d68e85aa)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

