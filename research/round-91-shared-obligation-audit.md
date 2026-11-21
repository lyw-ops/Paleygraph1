# Shared obligations through Paley round 91

Codex reviewed the [published round-91 snapshot][snapshot] on 2026-11-20 to answer the question in [Issue #13][issue]. The scope is the 91-round run discussed in the issue.

**One documented consolidation of two approaches at closeout. Zero cases with enough surviving pre-dispatch evidence to establish that the overlap was missed at launch.** The first count describes the written handoff. The second is a count of verifiable cases. The actual frequency of missed overlaps is unknown.

## How the count was made

I used the ledger and the 66 acceptance files to find explicit reductions, shared tests and consolidated follow-ups. The acceptance records cover rounds 37–91 continuously, with individually named records for some earlier rounds. I screened 210 ranked proposals for text similarity within each round, across 48 rounds with per-route rankings, excluding designated auditors and reviewers. I also checked the consolidated rankings in rounds 64–91 and read the relevant proofs for the closest matches. Different wording can hide an overlap from this screen. The four archived dispatch manifests are for rounds 33–36. Rankings report what agents proposed at closeout and give limited evidence about the original assignment or what the coordinator knew at launch. [Ledger][ledger] · [Round-36 dispatch manifest][dispatch] · [Round-91 acceptance][r91]

I counted a consolidation when separate approaches in the research record were subsequently tied to the same concrete obstruction, with an identity or implication at the level of the same mathematical objects. A stronger claim that the overlap went unnoticed before dispatch also needs an earlier plan treating the approaches as independent and a later record identifying the overlap. Repeated mentions of one obligation count once.

| Where | Evidence and classification |
| --- | --- |
| **Rounds 90–91. Incoming phase integral and real switch prices.** | One documented closeout consolidation. The round-91 contact argument locates the first tie at $\left|\int\dot z_i\right|=1/\sqrt3$ on the genuine incoming branch. In the two-real-pair formulation, (4) identifies a cap contact with a zero common bulk weight $k_i$. The price of the first such zero is an alternate sufficient exclusion test. The round-91 acceptance explicitly ranks the two approaches in one item. Round 90 already named cap contact and the exact correction as issues, so the record establishes the later bridge between formulations and leaves the coordinator's pre-dispatch knowledge undetermined. A tie may have zero correction, and the two proposed quantitative bounds have different forms. [Round 90][r90] · [Contact law][contact] · [Real switch, (4)–(5)][switch] · [Round 91 closeout][r91] |
| **Rounds 88–89. Masked quartic minimum and opposite-law shortfall.** | An exact shared estimate, introduced as a dual reformulation. The round-88 closeout proposes bounding the quartic on the actual adaptive mask. Equation (3) in round 89 proves the normalized opposite-law supremum equals the fourth root of that same minimum. The recorded sequence follows one proof obligation into its dual. [Round 88][r88] · [Round 89 duality][quartic] |
| **Round 83. Reverse Jacobi head and whole-face head.** | The closeout combines the approaches and asks for one optimizer at the same time. The reverse construction controls collision on a paying head, while the whole-face construction prices a joint capacity and height objective. The records show related tests and give no equivalence of those estimates. [Round 83 acceptance][r83] · [Reverse head][reverse] · [Joint capacity dual][joint] |
| **Round 10. Tangent width and dual extension.** | The extension LP is exactly equivalent to the tangent-width test. The extension section explicitly derives its test from the existing tangent LP. The written record indicates a deliberate primal–dual reformulation. [Tangent LP][tangent] · [Dual extension][extension] |
| **Round 91. Contact route and independent audit.** | The contact contributor and the auditor both recommend the actual coordinate integral. The acceptance describes the auditor's overlapping review of the contact law and the finite example. The repeated recommendation belongs to an intentional review. [Round 91 acceptance][r91] |

## Handoff check

I followed the [checkpoint's reading path](explorations/2026-11-20-paley-round-91-synthesis.md) in a clean export of `9c734d2`. It recovered the open target, the exact cold ray and phase threshold, the two forcing columns in (4a), the zero-weight interpretation of a tie, and the order of the two real follow-ups. The path suffices to specify the next test without the older discussion. This was a walkthrough in the authoring session, using the frozen source files.

The checkpoint passed the parser from [draft PR #14][format]. All 38 file hashes and the previous-record hash in the acceptance matched. Four checkers reproduced all seven JSONL records. In the upstream parser, `artifacts:` paths must be inside `research/runs/`. Paley keeps these historical outputs directly in `research/`, so the checkpoint cites the pinned JSONL files in its body.

[issue]: https://github.com/human-ai-mathematics/conjecture-search-template/issues/13#issuecomment-7014272236
[format]: https://github.com/human-ai-mathematics/conjecture-search-template/pull/14/files
[snapshot]: https://github.com/lyw-ops/Paleygraph1/tree/9c734d28e1cf4f8df68482f6deac371058c6a2aa
[ledger]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/ledger.md
[dispatch]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/round-36-dispatch.json
[r83]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/round-83-acceptance.json
[r88]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/round-88-acceptance.json
[r90]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/round-90-acceptance.json
[r91]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/round-91-acceptance.json
[tangent]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/parallel-endpoint-10.md#the-finite-test-on-the-actual-endpoint
[extension]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/endpoint-norm.md#the-exact-tangent-width-as-a-dual-extension
[reverse]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/astra-average-83.md
[joint]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/astra-split-83.md
[quartic]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/astra-quartic-89.md#an-exact-opposite-law-criterion-and-its-cubic-contact
[contact]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/astra-contact-91.md
[switch]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/real-two-marks-91.md#the-exact-remaining-bulk-system-and-the-switching-price
