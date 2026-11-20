# Proposed research mission: cold-actual-remaining-derivative

Coordinator record: coordination/round-145.json
Record SHA-256: c7b48953b288e4b16d645e85e7d2e7fe433f757989a5b73f5d37eec8eaf0fac3
This exports a proposal; it does not launch an agent or record a past dispatch.

## Question
Can the selected contracting cold derivative absorb the omitted terms of the actual height-601 and height-602 rows?

## Why this call is worth making
The full selected two-pair norm is now below 0.959 or below 0.920 after two steps. The actual height change is already bounded by 0.017.

## Current proof obligation
Price the actual neglected derivative terms at heights 601 and 602 below 0.041 per step or the two-step error below 0.080. A bound for the full frozen derivative and a nonlinear invariant with a marked half step remain open.

## Scope
Use A_h=KD_h for both genuine actual cold rows on the original closed square with t0=n. Let B=K(D^J+D^L), matching the actual chosen Legendre coefficient. Include other center and higher Legendre terms and Picard residuals. Keep the nonlinear invariant and half step separate.

## How the result changes the next decision
- If supported: Establish ||A_h-B||<0.041 at each height or ||A_602 A_601-B^2||<0.080 in the physical two-pair P5000 norm.
- If refuted: Identify an unavoidable exact label or analytic term defeating a specific omitted-block charge, with precise scope.
- If inconclusive: Bound one actual omitted sector or reduce the block error to a tractable same-row signed comparison using the true height-change estimate.

## Read these sources

- research/round-144-acceptance.json (SHA-256 535511b40cc4d5cd786c6bd8dd8bd24603e17b9cb88cac69cfc6544a351cd1b4)
- research/round-145-acceptance.json (SHA-256 6e4ae6076ec9d4bf14910c64e09300c610bc896f31ab9849e7f123c19aa54ad8)
- research/cold-jacobi-linear-legendre-145.md (SHA-256 7e299fc5ddd123a77577117e0a0919244631dbc7bacff8e15a4a83500edc6ad1)
- research/cold-frozen-cross-reduction-138.md (SHA-256 6a4283f05e6c58c7a1a0b581917838d2174303f2a9b82e40e8c1921aa7640225)
- research/cold-paired-height-transfer-139.md (SHA-256 cbf58984310d26616253184ad9bee2fd6fdbe598d90e06f2c04f162d31e8d7aa)
- research/cold-resummed-136.md (SHA-256 5a9c7bc44dbfe00958b3a9b4ed007cff1cf1dcb46c12f9068c36e2e2eceef161)
- research/cold-combined-height-130.md (SHA-256 45f678cd4b68b76bf8f08308f4030255de865d84c60cbd758a077bd53c713920)
- research/cold-quintic-complete-selected-pools-144.md (SHA-256 65d491945951070b9db8565942bcec62ce32784750acfa7d7e417c361c36fa06)
- research/shifted-resolvent-96.md (SHA-256 ec9c2eb7e001e71142295e67717fee4499bd89ff49f660a51a8d4ae1dec41a36)
- research/astra-predictor-76.md (SHA-256 65c95ee66e62b321a6b1255ea6c4b4f8bab8a858bc471a22310a76916316f9ef)

Report the argument, its hypotheses, evidence and remaining gap. Preserve unrelated work. A finite check or a failed sufficient bound does not settle the asymptotic target.

