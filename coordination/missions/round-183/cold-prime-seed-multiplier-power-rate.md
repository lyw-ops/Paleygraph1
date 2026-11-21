# Proposed research mission: cold-prime-seed-multiplier-power-rate

Coordinator record: coordination/round-182.json
Record SHA-256: bd56aa4c740ba06b77db3c9c24ca60e4681feb6d3ac85b3e9d27dda6dd40680f
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
With the seed-only higher Taylor terms moved into the seed multiplier L_S = K Phi'_t(S), is there a price P with a uniform power bound ||L^m||_P <= C lambda^m and lambda < 1 - C(1 - 0.77414706) for the full frozen multiplier at V_602, so that Gamma_{k_n} stays bounded uniformly in n?

## Why this call is worth making
Round 182 proved that either cold criterion needs Gamma_{k_n} bounded uniformly in n, computed the seed-linear m-step growth exactly, and the audit showed that leaving the seed-only Taylor terms outside L_S cuts the h-linear allowance from 1.925 to about 1.09 in pi_1.

## Current proof obligation
A uniform power rate for the full frozen multiplier: the non-seed part (h-linear plus higher Taylor) blocks; after charging the seed-only Taylor terms the h-linear allowance is rho*A(h) <~ 1.09 in pi_1 unless those terms are moved into the seed multiplier K Phi'_t(S). Floating evidence: sup|h| ~ 0.55, RMS ~ 0.175. Uniform complex stationary domain and derivative transfer remain separate.

## Scope
True cold orbit on the original closed square, physical t0=n, frozen-base identity at V_602, Proposition 1 and Proposition 2 of research/native-claude-cold-prime-signed-nonseed-price-182.md as accepted in Round 182 (threshold kappa* = 0.77414706...). Re-price L_S including the seed-only Taylor terms with the Round 80 per-simple rule (extend the audit's brute force in research/paley-182-audit-cold-check.py), compute its exact m-step growth, then price the remaining h-linear term with an explicit rho and A(h); say whether c(M) survives in pi_1. Any new price needs its own p0, c, sup domination, class closure (H1) and uniform corrections (H2). Print certified brackets with outward rounding; separate exact from floating. Cite accepted statements by round; re-prove anything taken from an unaccepted draft.

## How the result changes the next decision
- If supported: A certified power rate below 1 - C(1 - kappa*) proves the Round 173 finite-prefix confinement and common stationary continuation on the interior of the original square; derivative transfer becomes the next cold obligation.
- If refuted: An exact lower bound showing Gamma_m grows for every price in the stated class (for the seed multiplier with its Taylor terms) retires the price route and sends the cold route back to Criterion D or sup transfer.
- If inconclusive: Return the best certified power rate and the exact multiplier term that blocks the rest, with its budget.

## Read these sources

- research/round-181-acceptance.json (SHA-256 ad983e94b84fce4466bd29303e579f9bbf1d34576ec81bd92a27ab5f63bb0910)
- research/round-182-acceptance.json (SHA-256 78471bc51e0eaed7c99f92141d3a573d4a2d55f8fc4d7510c187da60e976bec6)
- research/native-claude-cold-prime-signed-nonseed-price-182.md (SHA-256 c8023a9bece7318be9122e2b0ec2ef007780e7b83835bb2eac8e84e91b4161e6)
- research/native-claude-audit-182.md (SHA-256 82edca1551678b235a57bc8f945d8ce24135501c1949834f8641ec82f77eef79)
- research/paley-182-cold-seed-power-check.py (SHA-256 868e9cb8c4de6c48e68365334070935e22e8b57bb2849ec05b4949cf33a71fed)
- research/paley-182-audit-cold-check.py (SHA-256 830147c16b5872ad0126107ec8c302a3bcbea0bfef68b68632d3b3a15c96370d)
- research/cold-growing-prefix-delocalization-180.md (SHA-256 3a8eb51ab257dc2b834142c7954357e533472676b4c5a06e1a0953db64e9b8c8)
- research/cold-seed-centered-larger-tube-177.md (SHA-256 12c7cff4f9a20dc1c7bfeabef28ed87f3018a863a325c95b7b008f9a9a180c3c)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

