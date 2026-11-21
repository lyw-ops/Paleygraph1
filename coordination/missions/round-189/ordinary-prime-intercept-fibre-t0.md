# Proposed research mission: ordinary-prime-intercept-fibre-t0

Coordinator record: coordination/round-188.json
Record SHA-256: 2c6221ec080ac072c5b8d93710427d4ed6f28d964d778bfd111c8ea8e590492c
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
For the actual g with the cap, is T_0 - c = sum_{lambda != 1} g(lambda) Delta(lambda, 0) = sum_{Y != Y'} g(Y) g(Y') g(Y'/Y) sum_{b in Q} g(D_b(Y)) g(D_b(Y')) at most p^(31/24-delta) (beats 43/24) or p^(5/4-delta) (below 7/4), or the averaged T <= p^(7/4-delta); equivalently max_{lambda != 1} Delta(lambda, 0) <= p^(3/4-delta) (resp. p^(2/3-delta)); or is there a method cap for incidence pricings of this sum?

## Why this call is worth making
Round 188 Theorem A removed the 7/4 floor; the one-match exponent now depends on T_0 (or X); T_0 <= X discards the triangle weight g(Y'/Y) and loses a factor 4-17 in models, and decoupled Cauchy-Schwarz pricings land at or above 43/24, so the open step is a coupled three-variable incidence estimate that does not need the harder X = O(p^(1+epsilon)).

## Current proof obligation
One-match: T_0 - c <= p^(31/24-delta) (beats 43/24) or p^(5/4-delta) (below 7/4), T_0 = O(p) for the target, by an estimate keeping the coupling between g(Y'/Y) and the shifted correlation (decoupled Cauchy-Schwarz gives nothing); or X <= p^(5/4-delta); or Gamma_tot <= p^(11/24-delta). First mass X = O(p^(1+1/1280)) unchanged. Generic J sum O(p^(9/4)) and zero-match unchanged. Fixed-a generic squared mass not re-derived.

## Scope
Actual g = |f|^2, omega >= 0, (H3), cap; Theorem A, Proposition B, Lemmas A1-A2 of Round 188 as accepted; Round 187 level extraction, Lemma C and Lemma M' as accepted; Stevens-de Zeeuw or other incidence theorems quoted from source with hypotheses checked at the scales used (sets of size asymp sqrt p, characteristic p); no near-critical input unless marked; exact exponent arithmetic; check against the F_(r^2) control (any saving must use primality). Report any bound on X or Gamma_2 separately (cand:slope-row-mass-x). Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: A one-match exponent below 43/24 (or 7/4); the remaining one-match obligation becomes T_0 = O(p).
- If refuted: A method cap for incidence pricings of T_0; the one-match route then rests on X or Gamma_tot, which coincide with the first-mass and support-energy obligations, and the coordinator weighs it against the zero-match and generic J-sum obligations.
- If inconclusive: Return the binding configuration and its size in the models (sector, interval, sumset).

## Read these sources

- research/round-187-acceptance.json (SHA-256 edc1d3eb551e96c049cae265dd10c15cadb5b6ea641f5760cd02afa6df26a1d9)
- research/round-188-acceptance.json (SHA-256 e0face6c633785fa83b9412704fc613744fa7613fcf0b99586182465e684dcc6)
- research/native-claude-audit-188.md (SHA-256 300664ba3a9dab8e5e699254578f304d1b9798b4cbf61c75ff70ab479a1e9894)
- research/native-claude-ordinary-prime-beyond-point-plane-188.md (SHA-256 cee51251577d7d04c79a290c798dc3980a9153f494d9a87c320b68b9d0721919)
- research/paley-188-bpp-exponents.py (SHA-256 1651c7fc38a76627b493d21271f001958a7f7299ccf03f75095c304b83645740)
- research/paley-188-audit-bpp-check.py (SHA-256 d2ee413c6668d101c5cb1cd13e46422fb1938ca1e8809d0bdb98a457fd7e403b)
- research/native-claude-ordinary-prime-level-pair-energy-187.md (SHA-256 5268631747d5ac3757ee328799f4e4205dd19afd5dc28184971a30255304e4b7)
- research/ordinary-mixed-row-autocorrelation-180.md (SHA-256 357f5058dd8ef16cf330a252680252d77c815ec5f3f6175e86bfa904d68e85aa)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

