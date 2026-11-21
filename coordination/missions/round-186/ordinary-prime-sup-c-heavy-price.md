# Proposed research mission: ordinary-prime-sup-c-heavy-price

Coordinator record: coordination/round-185.json
Record SHA-256: f5b2ff1fc84f0b0fac4b6a531b4658bb802a125f92cfe6fe5eb801324cbf8344
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Within the Round 185 three-step scheme (Steps L/B/H for C^sharp_lambda), how large can delta_C in sup_{lambda!=1} C(lambda) = O(p^(11/8-delta_C)) be made, for example by pricing the all-heavy term C^sharp_lambda[g_H^(x4)] directly in the quadrilinear form rather than through Hoelder to E^x(h_>=), by a BSG variant with smaller size loss or higher energies (Round 185 Proposition 6) in the extraction, or by a stronger incidence input for structured Cartesian products of size asymp sqrt p; and is the scheme's cap sup C = p^(4/3) attainable?

## Why this call is worth making
Round 185 moved the one-match exponent for the first time since Round 180 and identified the binding pair exactly: the band gain tau_1^(1/4) against the Phase-1 price p^(1/3) t^(-8/3); the gap to the scheme cap (1/664 against 1/24) is large.

## Current proof obligation
One-match: push delta_C beyond 1/664 (scheme cap 1/24, covariance p^(43/24)); below that needs an all-heavy price below p^(4/3) or a better incidence input; reaching O(p^(3/2)) needs a non-point-plane input (floor p^(7/4)) and the generic six-word class below p^(9/2). First mass: X = O(p^(1+1/1280)) via a quantitative prime-only input. Support energy only as n E(nu) - 1 = O(p^gamma), gamma < 3/8. Downstream Round 176/180 fixed-a generic squared mass not re-derived. Generic J sum O(p^(9/4)) and zero-match estimate unchanged.

## Scope
Actual g = |f|^2 of a probability on Q^ with the accepted cap n max nu <= C_cap sqrt p; no near-critical input unless stated and marked. Use Round 185 Lemmas 4-5, Theorems 1-2 and Proposition 6 as accepted, and the Round 178/180 chain with the Round 184 output p^(1/8) E^(1/4) M_1. Keep sup C separate from X and max W. Quote any new external theorem from its source with hypotheses verified at the scales used. Exact exponent arithmetic. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: Any delta_C > 1/664 gives one-match covariance O(p^(115/64-delta_C/8)), down to p^(43/24) at the scheme cap.
- If refuted: A model or argument showing that the all-heavy term needs p^(4/3+c) for these inputs: the one-match line within point-plane methods stalls near 1193/664 and the next lever is a non-point-plane input.
- If inconclusive: Return the best delta_C and the binding term.

## Read these sources

- research/round-184-acceptance.json (SHA-256 c30660213a26e69b172ce6e7f21a1fe33fe4eba5bfcec7fd976247ebd5d5e3ef)
- research/round-185-acceptance.json (SHA-256 157de3b64f9e2a2140fdc46d342f3a3b1d19447fd51ab7492d00bde001f59f9d)
- research/native-claude-audit-185.md (SHA-256 03d3a66b3c17574380db8829b476738a593d7ee3e8ab4eb81218052c1080646e)
- research/native-claude-ordinary-prime-near-critical-band-autocorrelation-185.md (SHA-256 4f0cd362412e92ef37163b039bc010bd4c837036250dbe4421ec13594af84473)
- research/paley-185-band-exponents.py (SHA-256 27472f8dba15fe323a7818b99e4386fd51887742073cb01d6f7840901e4ceeb3)
- research/paley-185-audit-band-check.py (SHA-256 f1c95aa42a90638e99cb0faccd9c17ebca63dbf3b4c5874a81eede899a29d557)
- research/native-claude-ordinary-prime-near-critical-slope-row-mass-184.md (SHA-256 85702949b82c262a1d68dce098c89c995308880d63fbdc35765d571e6e6c02ec)
- research/native-claude-ordinary-prime-shifted-level-energy-182.md (SHA-256 5c34d1fd84ae4b3bcc82a984d7f4fc1a29fd5c21f8bb24df73ac1b524750a331)
- research/ordinary-mixed-row-autocorrelation-180.md (SHA-256 357f5058dd8ef16cf330a252680252d77c815ec5f3f6175e86bfa904d68e85aa)
- research/ordinary-weighted-slope-product-incidence-178.md (SHA-256 9e4589c664dc84d30e86206288183a3af9dfb1ae29f8d49ebd6faa1db01f1d71)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

