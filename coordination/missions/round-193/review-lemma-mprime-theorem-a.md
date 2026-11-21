# Proposed research mission: review-lemma-mprime-theorem-a

Coordinator record: coordination/round-192.json
Record SHA-256: 6237ed51e1dd20dc0b2723760fbe15c43ac32d4390065bf4217bd83e9ae7fcbf
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Are Lemma M' (Round 187, popular-quotient pair-energy lemma without BSG, with Proposition P'), Theorem A (Round 188, twisted second-norm estimate without affine energy, for every t in F_p^x) and the Round 190 application of MPRRS Theorem 37 (E^x(A+alpha) << M^(33/13)|A|^(32/13), giving the p^(16/13) obstruction level and one-match 45/26) correct as stated, with every hypothesis, normalization and quantifier used where they are applied? For each, give a line-by-line verdict: correct, correct with a stated repair, or wrong with the first failing step.

## Why this call is worth making
Rounds 187-190 rest on these three results and they were accepted by agents overnight; the user has asked for an independent agent review in place of a human one before research builds further on them.

## Current proof obligation
(A-vertex): a genuinely signed estimate on the layers C^2/p < |F|^2 < a (every accepted device loses at least p^(1/2)). (A-slope): X = O(p) or M_sqrt(g) = O(p) logarithm-free behind cand:gp-shifted-energy (sharp form) or cand:gp-sector-constancy. Sigma g^2 >> sqrt p open. Cold paused.

## Scope
Review only; prove nothing new beyond the repairs a step needs. Work from the source reports and their audits; re-derive each step independently before reading the audit's verdict on it. For MPRRS Theorem 37, check the hypotheses (|AA| = M|A|, |A| <= p^(13/23)M^(10/23)) against the sets it is applied to, and check the statement at source if it can be retrieved; say if it cannot. Exact finite checks with exact arithmetic are allowed as evidence (research/paley-193-review-*.py); floating diagnostics are not proof. Keep the Round 187/188 hypotheses and normalizations exactly; state any place where an earlier audit's correction was needed and whether it suffices. This is an agent review, not human acceptance.

## How the result changes the next decision
- If supported: Record the three results as independently agent-reviewed; the plan is unchanged.
- If refuted: Record the failing step; mark which accepted downstream statements (R187-R192) depend on it and must be reassessed before any further ordinary call.
- If inconclusive: Record exactly which step could not be checked (for example the MPRRS source) and what would settle it.

## Read these sources

- research/round-191-acceptance.json (SHA-256 51b868043d590e9d1453de4cdc7fea270a58c666c27c75927270ddf3a0449538)
- research/round-192-acceptance.json (SHA-256 25a7b70e92e6a4640c3d671af94cedbb1f0445934e55f763b9caa577b0cc1041)
- research/native-claude-ordinary-prime-level-pair-energy-187.md (SHA-256 5268631747d5ac3757ee328799f4e4205dd19afd5dc28184971a30255304e4b7)
- research/native-claude-audit-187.md (SHA-256 714513ca7c9be14aa397b2c8a5a6786345da9d58cb9170e4524d7c7c50d657ff)
- research/native-claude-ordinary-prime-beyond-point-plane-188.md (SHA-256 cee51251577d7d04c79a290c798dc3980a9153f494d9a87c320b68b9d0721919)
- research/native-claude-audit-188.md (SHA-256 300664ba3a9dab8e5e699254578f304d1b9798b4cbf61c75ff70ab479a1e9894)
- research/native-claude-ordinary-gp-shifted-energy-literature-190.md (SHA-256 557777a493c1dcc5804540de7329c60a06217bbb6404c7713a3e11f230c53dd0)
- research/native-claude-audit-190.md (SHA-256 6237bffb438242a90b78540f5aaf2cf158c049853a43f94713c37f7f6cc97b80)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

