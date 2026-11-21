# Proposed research mission: ordinary-obligation-map-stocktake

Coordinator record: coordination/round-189.json
Record SHA-256: 8901a11cd6437da90e0862a8e8b52c9d727ed0d5350df6610c466830ba8ce822
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
From the accepted reduction of the target (Rounds 167-173 and later), what exact size does the target need for each ordinary piece (one-match covariance, zero match, generic J sum O(p^(9/4)), first mass), what is the current best proved exponent of each, and is the one-match requirement O(p^(3/2)) necessary for the chain or only the sufficient form chosen in Round 173?

## Why this call is worth making
Both lines are at method caps; the one-match target needs a near-sharp energy statement far beyond the known |I|^(5/2), while the zero-match and generic J-sum obligations have not been revisited since Round 178 or earlier and the acceptance records carry no current exponent for them; the coordinator needs to know which obligation is closest and whether any requirement has slack.

## Current proof obligation
Below 7/4: (GP) E^x(I-1) << |I|^(5/2-eta) for symmetric geometric progressions of length asymp sqrt p in F_p (recorded here as cand:gp-shifted-energy, an apparently open sum-product statement), or an actual-law input from (NC) excluding sector-type laws. Beating 43/24: the heavy-triangle sum or X below p^(31/24-delta). Target: T_0 or X = O(p) logarithm-free. First mass X = O(p^(1+1/1280)) unchanged. Zero match and generic J sum O(p^(9/4)) not revisited since Round 178 or earlier.

## Scope
Re-derivation only, no new estimates: cite accepted statements by round and file; exact exponents; mark each requirement 'necessary for this chain' or 'sufficient choice'; list the external inputs each piece depends on; include the Rounds 185-189 one-match changes and Theorem A.

## How the result changes the next decision
- If supported: Slack in a requirement, or a piece closer than one-match: Round 191 is redirected to it.
- If refuted: The ordinary line hinges on (GP)-type sum-product progress or an actual-law structure theorem; record this plainly and reduce ordinary estimate rounds.
- If inconclusive: Return the list of pieces whose current statement could not be recovered.

## Read these sources

- research/round-188-acceptance.json (SHA-256 e0face6c633785fa83b9412704fc613744fa7613fcf0b99586182465e684dcc6)
- research/round-189-acceptance.json (SHA-256 ad4e0b5aaaec51fec6be5df96359071f1360c09ff8ae7e4533b7852346176506)
- research/native-claude-audit-189.md (SHA-256 0bf8b1c3a04c795cad47c38adbb4ecc95e25d12934e3bffe8f247b6208e7f508)
- research/native-claude-ordinary-prime-beyond-point-plane-188.md (SHA-256 cee51251577d7d04c79a290c798dc3980a9153f494d9a87c320b68b9d0721919)
- research/ordinary-weighted-affine-vertical-saving-173.md (SHA-256 61e959f2defb68dec2f44205fb1601b0e98e210f3b45b38aed9ed68c3e3a2023)
- research/ordinary-weighted-slope-product-incidence-178.md (SHA-256 9e4589c664dc84d30e86206288183a3af9dfb1ae29f8d49ebd6faa1db01f1d71)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

