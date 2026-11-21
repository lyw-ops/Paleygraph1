# Proposed research mission: ordinary-gp-shifted-energy-literature

Coordinator record: coordination/round-189.json
Record SHA-256: 8901a11cd6437da90e0862a8e8b52c9d727ed0d5350df6610c466830ba8ce822
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Is there a published bound E^x(A+alpha) << |A|^(5/2-eta), or E^x(A+alpha, B) below the MPRRS Lemma 33 value, for A in F_p with |AA| << |A| at |A| asymp sqrt p, in particular for geometric progressions {gamma^k : |k| <= K}, K asymp sqrt p (cand:gp-shifted-energy); and are there Stepanov-type or character-sum bounds for shifted short geometric progressions, improvements of Stevens-de Zeeuw for Cartesian products in F_p (Mohammadi-Stevens and later) that move Lemma 33, or a graph (partial-product) version of Lemma 33?

## Why this call is worth making
Round 189 proved that every admissible-only argument below 7/4 must contain exactly this estimate, and Rounds 186, 187 and 189 all stopped at the same N^(5/2) value; a literature answer settles in one call whether the barrier is a known theorem away or an open problem.

## Current proof obligation
Below 7/4: (GP) E^x(I-1) << |I|^(5/2-eta) for symmetric geometric progressions of length asymp sqrt p in F_p (recorded here as cand:gp-shifted-energy, an apparently open sum-product statement), or an actual-law input from (NC) excluding sector-type laws. Beating 43/24: the heavy-triangle sum or X below p^(31/24-delta). Target: T_0 or X = O(p) logarithm-free. First mass X = O(p^(1+1/1280)) unchanged. Zero match and generic J sum O(p^(9/4)) not revisited since Round 178 or earlier.

## Scope
Quote statements verbatim from the source (arXiv HTML or PDF; record URL and version); check hypotheses at |A| asymp sqrt p in F_p; note whether primality is used (the F_(r^2) control rules out field-general statements); no new proofs; report the best known exponent and its source, and the closest results with exact gaps. Cite accepted project statements by round.

## How the result changes the next decision
- If supported: The sector obstruction of Round 189 Corollary 3.1 disappears; the next call applies the bound to X(1_I)-type pieces and the height-1 level sets of Round 187.
- If refuted: Record (GP) as an external open problem under cand:gp-shifted-energy; retire T_0 / X routes below 7/4 for admissible-only arguments.
- If inconclusive: Return the closest results with their exact gaps (exponent, size range, structure assumed).

## Read these sources

- research/round-188-acceptance.json (SHA-256 e0face6c633785fa83b9412704fc613744fa7613fcf0b99586182465e684dcc6)
- research/round-189-acceptance.json (SHA-256 ad4e0b5aaaec51fec6be5df96359071f1360c09ff8ae7e4533b7852346176506)
- research/native-claude-audit-189.md (SHA-256 0bf8b1c3a04c795cad47c38adbb4ecc95e25d12934e3bffe8f247b6208e7f508)
- research/native-claude-ordinary-prime-intercept-fibre-t0-189.md (SHA-256 2a586af800b25cb2249a226ac6815ba74a810f2b438c1b4e2f5f7b67fb53b852)
- research/native-claude-ordinary-prime-sup-c-heavy-price-186.md (SHA-256 9220d8860c7039ce143e730e76946a903946a16900f167b29666d4854045f0d3)
- research/native-claude-audit-186.md (SHA-256 2b61a763b2021d4447d176326807abdef9dea83c24b017d26d51c5f6dfbdbc48)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

