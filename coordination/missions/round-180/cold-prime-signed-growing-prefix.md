# Proposed research mission: cold-prime-signed-growing-prefix

Coordinator record: coordination/round-179.json
Record SHA-256: 0d2b2f3633381aa466d6cd694d8380cdab8f0c6b54af01385fd0e33eacda2741
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Do the actual marked Picard rows V_602,…,V_{602+k_n}, k_n=ceil((4/7)log2 n), stay in the coordinate disks of radius 0.025 around V_602 with a fixed clearance η>0, uniformly on the original closed square and both lifts, using the actual signed coordinate increments rather than a fixed unnormalized threshold?

## Why this call is worth making
Round 173 reduced common continuation on the original square to this single finite-prefix confinement test. Round 179 proved the normalized fixed residual R_611 has positive liminf, so no fixed-height unnormalized counting threshold can supply the prefix. A coordinate (sup-norm) confinement must therefore use signed cancellation in the moving increments or a genuine moving predictor.

## Current proof obligation
Prove cap-controlled signed growing-height confinement or construct a genuine moving starter. The uniform complex stationary domain and derivative transfer remain separate.

## Scope
Genuine nine-center start, both lifts, physical t_0=n, original closed square around a=2031/128 of half-width 2^(-17), actual KΦ_t. Coordinate supremum norms for confinement; second-norm contraction q=0.525 only inside the disks. The compact transfer of Rounds 79–80 is fixed-height; any use at height growing with n must be justified separately. State whether the argument is a proof for all sufficiently large eligible primes, a conditional criterion, or finite evidence.

## How the result changes the next decision
- If supported: Proves the finite-prefix test and hence common stationary continuation on the interior of the original square for the cold route; derivative transfer remains the separate next obligation.
- If refuted: An explicit coordinate whose signed increments accumulate beyond 0.025 within k_n steps (proved, or shown for the compact limit with justified transfer) refutes this criterion and sends the cold route to a different domain or starter.
- If inconclusive: Return the precise signed coordinate sum or source term that is not controlled, with verified bounds on the parts that are, and say whether a larger radius disk with q<1 could replace 0.025.

## Read these sources

- research/round-178-acceptance.json (SHA-256 10dceeac23ed58c55637d159d8804d83e445c239ccc84608195160ae3e0d394e)
- research/round-179-acceptance.json (SHA-256 2c7ee0603b7d5ebdac1773b4b43573530fcacc84c81f2e8b345b0fdafd1ec414)
- research/cold-fixed-counting-source-obstruction-179.md (SHA-256 eb5594666fc3a815c40a539ca9fd40d3c3bcb71ef2afaa215b921010d2a09152)
- research/cold-logarithmic-finite-tube-173.md (SHA-256 3d0a8513125a95f4e045c0b9ccd99a531ca3f3ee7a29c195f4cf28eed93f7c37)
- research/cold-seed-centered-larger-tube-177.md (SHA-256 12c7cff4f9a20dc1c7bfeabef28ed87f3018a863a325c95b7b008f9a9a180c3c)
- research/astra-direction-83.md (SHA-256 241d871d9b6c767177f7301bdc85b8b370b0cbafd80dcb23b1b91dcd43a3d62d)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

