# Proposed research mission: cold-prime-signed-nonseed-price

Coordinator record: coordination/round-181.json
Record SHA-256: f237fdabcd6e145d9f29bd8512ab62d67eb41b26d091f20d033237e245dd2d51
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Is there a signed cross-vertex collected price at V_602 whose frozen rate satisfies kappa0 < 0.77395 — in particular, can the transported non-seed multiplier (the h-linear term with h=V_602-S, plus higher Taylor terms) be priced below its budget of about 0.24 — or alternatively a signed source price p0 <= 1e-6, so that the small-ball Kantorovich criterion gives growing-prefix confinement?

## Why this call is worth making
Round 181 (evidence only) turned the cold price route into one number: with p0=0.01272 and c<=1.0043, the small-ball criterion needs kappa0 < 0.77395, against the proved 1.066 for P_5000; the seed-linear part is priced exactly (weighted rate <= 0.5326) and the non-seed h-linear term costs about 0.50 crudely.

## Current proof obligation
A signed cross-vertex collected price at V_602 with kappa0 < 0.77395 and its own p0, c, class closure and uniform corrections; the uncontrolled part is the transported non-seed multiplier (h=V_602-S and higher Taylor terms), budget about 0.24 against a crude h-linear cost about 0.50. Alternatively a signed source price p0 <= 1e-6 relaxes the target to kappa0 < 0.998. Uniform complex stationary domain and derivative transfer remain separate.

## Scope
True cold orbit on the original closed square, physical t0=n, the frozen-base identity at V_602 and the Round 174/177 recursion u_{j+1} <= p0 + kappa0 u_j + c u_j^2. First restate and re-prove Proposition 1 of research/native-claude-cold-prime-delocalization-price-181.md (its text survives) with the audit's two added hypotheses: closure of the price class under the recursion and uniformity of the correction constants over inputs. Any new price must come with its own p0, c, sup domination, class closure and uniform corrections. Separate exact/outward interval computations from floating diagnostics. Any Round 181 claim used (see research/round-181-acceptance.json proof_scope) must be re-proved in full in this draft; the Round 181 proofs are lost and are not citable.

## How the result changes the next decision
- If supported: kappa0 < 0.77395 (with the criterion's hypotheses) proves the Round 173 finite-prefix confinement and common stationary continuation on the interior of the original square; derivative transfer becomes the next cold obligation.
- If refuted: A signed lower bound on the non-seed multiplier rate showing every price in the stated class has kappa0 >= 0.77395 retires the small-ball price route and sends the cold route back to Criterion D or sup transfer.
- If inconclusive: Return the best certified kappa0 and the exact multiplier term that blocks the remainder.

## Read these sources

- research/round-180-acceptance.json (SHA-256 489e1a259667fe13a6f2e6893358de175eaf8240bc49f02bb9679186702e128a)
- research/round-181-acceptance.json (SHA-256 ad983e94b84fce4466bd29303e579f9bbf1d34576ec81bd92a27ab5f63bb0910)
- research/native-claude-cold-prime-delocalization-price-181.md (SHA-256 dff5a06d39cfbbab7066d16d8044afd761f2f45c01059a07a4225143b21bf4a6)
- research/native-claude-audit-181.md (SHA-256 08ac949cb99eefc6425aae0ff5d4c015e5eb4528ed3bb1e6140b97fb9be02d57)
- research/paley-181-cold-kantorovich-check.py (SHA-256 b0b6842fcdd3eb7563191e92b73a2bbc4e4f356ca1f148a39f62344054491bb4)
- research/cold-growing-prefix-delocalization-180.md (SHA-256 3a8eb51ab257dc2b834142c7954357e533472676b4c5a06e1a0953db64e9b8c8)
- research/cold-seed-centered-larger-tube-177.md (SHA-256 12c7cff4f9a20dc1c7bfeabef28ed87f3018a863a325c95b7b008f9a9a180c3c)
- research/cold-first-prefix-step-174.md (SHA-256 8d28cc54df9a57240886c543783a1dca331348a016dd359608e46b6fa177989e)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

