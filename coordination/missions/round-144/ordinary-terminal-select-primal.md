# Proposed research mission: ordinary-terminal-select-primal

Coordinator record: coordination/round-143.json
Record SHA-256: 96bf377e5aac06ecc6bd14562ae7c7bae1912647a5752fe8719ebb0136f8245d
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Can we construct or select an optimizer on the actual mean-one face with sublinear terminal activation?

## Why this call is worth making
The first moment suffices and is weaker than the quadratic triple test. Exact support and optimal-face selection can exploit constraints beyond positivity alone.

## Current proof obligation
Obtain a prime-uniform o(T) upper on the minimum weighted actual terminal activation or its exact reduced dual, each sign at selectable growing time. Keep the floor fixed until after the prime limit.

## Scope
For each sufficiently small fixed tau>0 and each ordinary sign s, along all p=1 mod 4 primes p tending to infinity, there is a choice of a genuine mean-one optimum F on sign s and T=T(p) tending to infinity with T+1 in the proved simultaneous marked window for which E[1_bulk F sqrt(n) g_T]=o(T), with n=(p-1)/2 and g_T the actual fixed-tau zero-start activation increment. The tau limit follows the prime limit. Use the primal side and keep the exact root optimum throughout.

## How the result changes the next decision
- If supported: Prove the stated bound by genuine prime geometry or an explicit choice of an actual optimizer.
- If refuted: Exhibit a precisely scoped obstruction on primes or to a proposed selection mechanism.
- If inconclusive: Give a useful construction whose remaining prime-uniform arithmetic estimate is explicit.

## Shared proof obligations

- `cand:actual-face-terminal-first-moment` — For each sufficiently small fixed tau>0 and each ordinary sign s, along all p=1 mod 4 primes p tending to infinity, there is a choice of a genuine mean-one optimum F on sign s and T=T(p) tending to infinity with T+1 in the proved simultaneous marked window for which E[1_bulk F sqrt(n) g_T]=o(T), with n=(p-1)/2 and g_T the actual fixed-tau zero-start activation increment. The tau limit follows the prime limit.

## Read these sources

- research/round-142-acceptance.json (SHA-256 b0f26806496694755bfd9f347ab1165e3aa1473853ee43cc71909f491de1da08)
- research/round-143-acceptance.json (SHA-256 4556186fcb37a735c72d1878966f216394799d9178f8ad4c58e40ce3fa75d3b7)
- research/ordinary-terminal-face-dual-143.md (SHA-256 41a6e3ff3da185c7b22f2d3b008a5f13b04bf4cf5d6269b3d2c3ce5b34d051bb)
- research/averaged-hinge-opposite-141.md (SHA-256 92641e5bef3da4349ef50fa3a0db73e771a49f9431ee91a15a2d9d65fa087d26)
- research/ordinary-terminal-offdiagonal-142.md (SHA-256 958ff834c39cdb71002730a3017aecfdd33acb909147eed83f0245c587801e03)
- research/opposite-autocorrelation-73.md (SHA-256 0e9dea1c29103b22ee5b345845fc5233abfa137e16634c92a07d9473dc43f92a)
- research/averaged-completion-dual-140.md (SHA-256 56dca52b029fc096f42ad60ddeaeb38d305a0a0c8861bf3269f7e3649e269595)
- research/parallel-depth-window-30.md (SHA-256 00373a4818a2798c5d0f169a396eb602dff12392c69fce657647995b7aba1eaf)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

