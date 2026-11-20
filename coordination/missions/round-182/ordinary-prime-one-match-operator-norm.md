# Proposed research mission: ordinary-prime-one-match-operator-norm

Coordinator record: coordination/round-181.json
Record SHA-256: f237fdabcd6e145d9f29bd8512ab62d67eb41b26d091f20d033237e245dd2d51
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Is ||pi(mu)||_op = O(p^(3/4)) (or any bound giving one-match covariance below O(p^(115/64))) for the actual twisted physical interior mu, where pi is the (p-1)-dimensional representation of the affine group — for example through a mean-subtracted sixth-moment energy E_3 of mu?

## Why this call is worth making
Round 181 (evidence only) showed that slope-fibre masses together with the listed proved inequalities cannot beat 115/64, and that ||pi(mu)||_op=O(p^(3/4)) (criterion b1') would give the one-match target O(p^(3/2)); the auxiliary sinc model has ||pi(mu)||_op/p^(3/4) between 0.32 and 0.56.

## Current proof obligation
One-match covariance O(p^(3/2)), e.g. via ||pi(mu)||_op=O(p^(3/4)) for the actual twisted physical interior. Direct first mass M_w=O(p^(1+1/1280)), e.g. via shifted multiplicative energy of actual level sets below Round 177's exponent 36/13. The generic J sum (O(p^(9/4))) and the zero-match estimate are unchanged.

## Scope
Use the actual mu(r,b)=g(Y)g(D) with the square mask and interior exclusions of Round 171, the twisted physical chart of Rounds 169 and 173 and its one-match normalization, the actual w and D amplitudes, counting norms. First re-prove the splitting S(t)=M_1^2G^2/p+||pi(mu)h_t°||^2 and the Hilbert-Schmidt identity you use. A trace-moment route bounds ||pi(mu)||_op^(2k) by tr((pi(mu)pi(mu)*)^k); state exactly which energy each moment equals, which part of it the trivial representation removes, and which incidence or sum-product input (with hypotheses) controls it. Report exponents exactly and say which weights are majorized by one. Any Round 181 claim used (see research/round-181-acceptance.json proof_scope) must be re-proved in full in this draft; the Round 181 proofs are lost and are not citable.

## How the result changes the next decision
- If supported: ||pi(mu)||_op=O(p^(3/4)) proves the one-match estimate O(p^(3/2)), leaving the zero-match estimate and the whole diagonal; any operator bound improving 115/64 is an accepted improvement.
- If refuted: A mu consistent with the proved constraints whose operator norm exceeds p^(3/4) by a power (for instance a level set concentrated near a coset of a subgroup of the affine group) shows criterion b1' is false and the one-match target needs the vector h_t°, not the operator norm.
- If inconclusive: Return the exact moment k and the energy term that blocks it, with its verified bound.

## Read these sources

- research/round-180-acceptance.json (SHA-256 489e1a259667fe13a6f2e6893358de175eaf8240bc49f02bb9679186702e128a)
- research/round-181-acceptance.json (SHA-256 ad983e94b84fce4466bd29303e579f9bbf1d34576ec81bd92a27ab5f63bb0910)
- research/native-claude-ordinary-prime-one-match-slope-fibres-181.md (SHA-256 54e743fb43c3047a1e52443dd89b52c2923821e8f905939f288cb1382dcb7855)
- research/paley-181-one-match-identity-check.py (SHA-256 25771ca9c8bfabe077668f8897f76fbe61a3b880dc219516084e5c97fabd9344)
- research/ordinary-mixed-row-autocorrelation-180.md (SHA-256 357f5058dd8ef16cf330a252680252d77c815ec5f3f6175e86bfa904d68e85aa)
- research/ordinary-weighted-slope-product-incidence-178.md (SHA-256 9e4589c664dc84d30e86206288183a3af9dfb1ae29f8d49ebd6faa1db01f1d71)
- research/ordinary-one-match-twisted-physical-169.md (SHA-256 8f683813155b15dd91aea2a0f5cbbc01aa3e704501212007bd7ae63c975f1d77)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

