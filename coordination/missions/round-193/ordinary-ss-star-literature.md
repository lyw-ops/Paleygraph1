# Proposed research mission: ordinary-ss-star-literature

Coordinator record: coordination/round-192.json
Record SHA-256: 6237ed51e1dd20dc0b2723760fbe15c43ac32d4390065bf4217bd83e9ae7fcbf
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Is there a published theorem, read at source, that implies (SS*) of Round 192 section 3, or (SS**) as quantified in the Round 192 audit section 2.9: a sparse, robust (approximate) form of the Green-Sanders idempotent theorem in Z/N, for sets with |S| ~ sqrt(N/2) whose normalised spectrum g = |hat 1_S|^2/|S|^2 is sharp at a fixed level a, with relative L^2 error o(1) at density N^(-1/2)? If not, what is the strongest published statement and which parameter (density, robustness, number of subgroups) it fails to reach?

## Why this call is worth making
Round 192 Theorem E refutes vertex tightness (V) on (NC) conditionally on (SS*); the audit named a source-level check for (SS*) as the only remaining optional follow-up. A source would turn the conditional refutation into a proved obstruction for (A-vertex).

## Current proof obligation
(A-vertex): a genuinely signed estimate on the layers C^2/p < |F|^2 < a (every accepted device loses at least p^(1/2)). (A-slope): X = O(p) or M_sqrt(g) = O(p) logarithm-free behind cand:gp-shifted-energy (sharp form) or cand:gp-sector-constancy. Sigma g^2 >> sqrt p open. Cold paused.

## Scope
Literature check at source (papers read, not quoted from memory): quantitative idempotent theorems (Green-Sanders and successors), approximate or robust versions, sparse or low-density versions, Chang/Bloom-Sanders type spectral structure, and almost-periodicity results with density dependence. Keep (SS*) exactly as in Round 192 section 3 and the audit's (SS**); report the source's hypotheses and constants against those parameters. Any short derivation from a source must be written out in full. Do not use (SS*) to claim anything about the actual near-critical law beyond Theorem E's conditional statement. Mention whether a failure of (SS) through progression-shaped spectra would touch cand:gp-sector-constancy.

## How the result changes the next decision
- If supported: Theorem E becomes unconditional: (V) fails on (NC) and (A-vertex) needs a genuinely signed estimate on the low layers; record that and hold the vertex route.
- If refuted: (SS*) stays an internal open problem; record the strongest source and the exact gap; hold.
- If inconclusive: Record which sources could not be retrieved and the closest statement found.

## Read these sources

- research/round-191-acceptance.json (SHA-256 51b868043d590e9d1453de4cdc7fea270a58c666c27c75927270ddf3a0449538)
- research/round-192-acceptance.json (SHA-256 25a7b70e92e6a4640c3d671af94cedbb1f0445934e55f763b9caa577b0cc1041)
- research/native-claude-ordinary-nc-vertex-tightness-192.md (SHA-256 509e0d4021ade6200dff650293f2487be6311b0d80f1ca9b88d3f32905b5d98b)
- research/native-claude-audit-192.md (SHA-256 455c97ed5f9928fb75ae5b6c7b1fcf9b8041449afe7bb755888b26eaed93d85b)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

