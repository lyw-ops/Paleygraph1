# Proposed research mission: ordinary-prime-shifted-level-energy

Coordinator record: coordination/round-181.json
Record SHA-256: f237fdabcd6e145d9f29bd8512ab62d67eb41b26d091f20d033237e245dd2d51
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Is the shifted multiplicative energy E^x(1-S) of the actual level sets S of g (or of log-intervals P_N with N ~ sqrt(p) as the first model) bounded by p^(o(1))(|S|^2+|S|^4/p) — or by any exponent below the Round 177 incidence exponent 36/13 — enough to give the direct first mass M_w=O(p^(1+1/1280))?

## Why this call is worth making
Round 181 (evidence only) reduced the direct first mass to M_w <= E_Q(h)/4 with h(z)=g(1-z) and showed the target needs near-sharp shifted multiplicative energy for level sets with t >= p^(-1/2); exact coset models are settled by Shkredov's Theorem 6 (arXiv:1504.04522) but the high levels are only approximate subgroups.

## Current proof obligation
One-match covariance O(p^(3/2)), e.g. via ||pi(mu)||_op=O(p^(3/4)) for the actual twisted physical interior. Direct first mass M_w=O(p^(1+1/1280)), e.g. via shifted multiplicative energy of actual level sets below Round 177's exponent 36/13. The generic J sum (O(p^(9/4))) and the zero-match estimate are unchanged.

## Scope
Actual g, w=g(1-g), G, physical masks and nonzero interior of Round 178, the Round 180 cross-ratio chart. First re-prove the row-pair reformulation over kappa=1-r and M_w <= E_Q(h)/4 (research/paley-181-first-mass-check.py checks the reformulation exactly at p<=41). Then attack E^x(1-S) for the level-set structure that the actual g has (state which structural facts about g you use and where they are proved). State any external input (Stepanov, Shkredov, Rudnev, Stevens-de Zeeuw) exactly with its hypotheses and check them against the sets used. Separate proved, conditional and floating evidence. Any Round 181 claim used (see research/round-181-acceptance.json proof_scope) must be re-proved in full in this draft; the Round 181 proofs are lost and are not citable.

## How the result changes the next decision
- If supported: M_w=O(p^(1+1/1280)) closes J in {0,1} at target scale and lowers each generic J class to O(p^(3/2+1/1280)); a shifted-energy exponent below 36/13 alone is an accepted improvement of the Round 177 input.
- If refuted: An admissible level-set family (consistent with all proved constraints on g) with E^x(1-S) or M_w/G^2 growing by a power of p shows the direct first mass needs cancellation, not positivity.
- If inconclusive: Return the exact level range t and set structure (approximate subgroup size, doubling) where the energy bound fails, with its verified bound.

## Read these sources

- research/round-180-acceptance.json (SHA-256 489e1a259667fe13a6f2e6893358de175eaf8240bc49f02bb9679186702e128a)
- research/round-181-acceptance.json (SHA-256 ad983e94b84fce4466bd29303e579f9bbf1d34576ec81bd92a27ab5f63bb0910)
- research/native-claude-ordinary-prime-direct-first-mass-181.md (SHA-256 ccd61cf9d7f3838b93572c80e1b24b27a50367675222963143cdbc31458d55c6)
- research/paley-181-first-mass-check.py (SHA-256 28b380ffe337a1da1f851e9b52e4fc1381001abfb6d3ce1a3371d9db1ad25941)
- research/ordinary-paired-J-cross-ratio-180.md (SHA-256 f800b53b7d6678f7d12f79352255261a0808823e137d79d898c286d1693ef0fa)
- research/ordinary-shifted-energy-four-factor-diagonal-177.md (SHA-256 8d230eebf51c30edfe4c55b4655036e455e90d7f71ad95ec49d1e909f3aacb34)
- research/ordinary-affine-triple-diagonal-179.md (SHA-256 1511abc52dacf6b6785fe7ff9544b9c55b473e9e7dc0fa6fc10ead61983e42ee)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

