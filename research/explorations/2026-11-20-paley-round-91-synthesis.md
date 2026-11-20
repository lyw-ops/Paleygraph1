---
candidates:
  - id: cand:paley-cold-cap
    statement: >-
      For every prime p = 1 mod 4 with n = (p-1)/2 at least 10^30, on each vertical
      segment from x to x + iy in the square |x - 2031/128|, |y| <= 2^-17, the genuine
      unforced branch from the positive real row remains strictly below the first bulk
      phase cap |tan(phi_i)| = 1/sqrt(2) in every coordinate i other than the mark.
      Equivalently, on the unforced segment up to and including any first tie, its
      coordinate integrals of (4a) in astra-contact-91.md have absolute value strictly
      below 1/sqrt(3).
  - id: cand:paley-masked-quartic
    statement: >-
      On a prime sequence with fixed larger-mark gap sqrt(n)*a >= 1+delta, at an
      admissible adaptive delayed-pin window with the counting saving from
      astra-persistent-88.md, the minimum of sum over i in P of (q_i/a)^4 over genuine
      primary optimizers q is O_delta(K^2), with P the physical deficit mask and K
      in the range of (6) in that note. Equivalently,
      the opposite-law supremum in (3) of astra-quartic-89.md is O_delta(K^(1/2)) on the
      same mask.
  - id: cand:paley-affine-first-price
    statement: >-
      For the genuine complementary zero-floor optimizers and strict affine matches of
      astra-fiber-91.md, the signed difference of the two first marginal prices at V=1
      is o(1) in the p^(-1/2) counting normalization through primes. Test it on a
      macroscopic interval and a data-selected positive-fraction union of third-coordinate
      cosets at d=o(E_A^(-2)), for fixed A>6, with probability tending to one over the
      short-prime draws. The main term of (1) would then exclude a fixed mark gap.
---

# Paley synthesis checkpoint after round 91

Retrospective prepared by Codex on 2026-11-20 from the [published round-91 snapshot][snapshot] and its [acceptance record][r91]. The `conj:`, `ap:` and `cand:` IDs are local to this checkpoint. The evidence links point to the original round-91 JSONL files. [Draft PR #14][format]

## Question examined

Which obligations remain after round 91, and which test should a fresh coordinator run first? The target `conj:paley-theta-limit` is open. For primes $p\equiv1\pmod4$, let $H$ be the Paley graph induced on the nonzero squares and $n=(p-1)/2$. The target is the ordinary Lovász theta limit $\vartheta(\overline H)/\sqrt n\to1$.

## What we learned

- **`ap:cold-contact` and `ap:cold-real-switch`** (*established*). Round 36 discharged the separate complex-growth bound under the hypothesis of a common right-half-plane domain carrying the actual scalar marked germs. Round 91 eliminated the marked unknown from each of two cold formulations. In the incoming differential, the eliminated operator $L$ has norm at most $1/\sqrt2$ and the bulk feedback has norm at most $1/2$. At a zero-correction tie, a complementarity problem gives both signed one-sided correction totals, including at analytic tangencies. In the equivalent real clipped formulation, the two real stationary pairs have common bulk weights $k$. Their marked midpoint solves one scalar equation with a uniform lower slope, including for zero bulk weights. The exact bulk system gives $k_i=(1-c\delta_i)_+$ and $e_i=(c\delta_i-1)_+$. A zero common weight is a cap contact, and an equality $c\delta_i=1$ carries zero correction. [Round 36][growth] · [Incoming response and contact law][contact] · [Two real stationary pairs][switch]
- **`ap:cold-contact` and `ap:cold-real-switch`** (*observed*, outward interval bounds). At $p=173$ on the ray $\Re t=1/50$, the first tie is the positive site 43 at $0.01294720<\Im t<0.01294721$. The right derivative of the unaveraged positive correction lies in $(678,679)$. The real formulation certifies a positive switch correction at $t=1/50+13i/1000$. These floors are outside the nominated cold square. [Contact records][contact-run] · [Switch record][switch-run]
- **`ap:quartic-primary` and `ap:quartic-shortfall`** (*established*). Round 89 equated the masked primal minimum to the fourth power of its sharp opposite-law shortfall supremum on the same mask. Round 91 identified the least corrected root coefficient across sharp witnesses as a secant on the full primary polytope. At the actual growing delayed pin, prime-quotient spreading and almost unit efficiency force order-length positive physical height on a displaced translate near the cap, even when the optimal coefficient is unbounded. The capacity of that excess remains open. The equality of primal and dual prices is also checked at $p=97$ (*observed*, exact cyclotomic comparison with outward sign checks). [Quartic duality][quartic] · [Secant and excess walk][discount] · [Finite record][discount-run]
- **`ap:affine-marginals` and `ap:affine-absolute-transport`** (*established*). The short-prime total-variation bound permits choosing a union of third-coordinate cosets after the draw at the admitted resolution. The leading signed price survives this selection. Under the displaced-atom hypothesis the centered absolute coupling has a positive cost even with separately fitted coset phases. In the diffuse case, sufficient energy over a small collection of modes forces residual for third-only fits. The signed comparison remains open. The finite arithmetic checks are at $p=53,257,409$ (*observed*). [Quotient prices and obstructions][fiber] · [Finite records][fiber-run]

## What resists

- **`cand:paley-cold-cap`** is shared by `ap:cold-contact` and `ap:cold-real-switch`. The incoming-coordinate integral and the real variational price of the first zero of $k$ are two ways to exclude contact. The weaker continuation objective is exact vanishing of the canonical nonnegative corrections throughout the square, which could also hold at a tie. Round 90's mean correction bound and round 91's Hilbert bound leave individual violating sites possible. A common unforced section here would address one cold floor. The round-36 conditional finish for the full theta limit still requires common hot-to-cold access to a sequence of positive floors tending to zero, with the prime limit taken first. [Cold square and correction bound][column] · [Conditional finish][growth]
- **`cand:paley-masked-quartic`** is shared by `ap:quartic-primary` and `ap:quartic-shortfall`. Test the upper capacity of $x^j(E)$ in (5) of the shortfall note, using the actual excess $E=(r-(A/\eta)\mu/a)_+$, its quotient fiber caps, and the normalized cubic on the same pin. The current forcing argument covers almost unit efficiency under spreading. Intermediate efficiencies and insufficient spreading remain separate cases. [Physical pin][pin] · [Walk and efficiency hypotheses][discount]
- **`cand:paley-affine-first-price`** is the remaining test for `ap:affine-marginals`. For $V=1$, the round-91 main term on a union $\mathcal U$ of cosets is $\alpha(|\mathcal U|/d)n(b-a)/(8\sqrt p)$, with $\alpha=|I|/p$ and actual marks $a,b$. On a fixed-gap sequence it already determines the sign for a union of positive fraction. A new signed comparison must use the complementary optimizer constraints beyond selecting or centering those cosets. [Price normalization and hypotheses][fiber]

## Proposed next step

**Mission.** Take the first item in the round-91 closeout and start with the vertical ray $t=2031/128+iy$, $0\le y\le2^{-17}$, for primes $p\equiv1\pmod4$ with $n\ge10^{30}$. Continue from the positive real row with bulk products $q_i=1$ and marked product $u+iv=n/t$. In the notation of (4a), integrate the actual $\dot z_B$ up to the first tie or the edge. Use $\dot u+i\dot v=-in/t^2$, both incoming columns $c_B,A_{B0}$ and the changing $D_B$. Aim for a prime-uniform strict margin below $1/\sqrt3$ in **every** bulk coordinate. With $q_i=1$, $z_i=\sin\phi_i$, so this is the exact first-contact threshold. The local law and the two real objectives supply checks at the threshold. [Ranked closeout][r91] · [Equations (1)–(4a) and the contact threshold][contact]

- **Strict margin on the ray.** This establishes cap-free passage on that ray. Next test uniformity over $|\Re t-2031/128|\le2^{-17}$ to reach the full square.
- **Genuine tie on the nominated ray.** This rules out strict separation there. Use the signed contact law or switch prices to distinguish a zero-correction tangency from positive clipping. A positive correction would defeat this cap-removal test at the exhibited floor.
- **Inconclusive.** Identify the coordinate and term in (4a) that prevents the bound and retain the proved field range and margin. An averaged estimate or another finite field cannot decide the unbounded-prime test.

**Set aside for this mission.** Keep the real switch calculation as an alternative test of the same contact, with (5)'s objective gap still needing a below-first-switch bound. Leave the same-sign singularity test for the local contact analysis, where it bears on derivative uniqueness. Keep the quartic excess-capacity and affine signed-price tests queued in that order. Their obstacles are the unbounded through-primes excess on the actual walk and the uncancelled first marginal difference, respectively. In the affine route, set aside absolute transport on a persistent displaced atom and third-only fits in the proved mode regime. [Round-91 closeout][r91] · [Switch-price identity][switch] · [Transport and mode obstructions][fiber]

**Reading path for a fresh session**

1. [Round-91 acceptance][r91] for `proof_scope`, `failed_paths_and_open_bounds` and `main_ranked_closeout`.
2. [Incoming response][contact], equations (1)–(4a) for the mission and (5)–(8) for the tie outcomes. [Round-90 cold square][column] gives the domain, chart and small-but-possibly-positive correction bound.
3. [Two real stationary pairs][switch], equations (4)–(5), for why the two approaches share the cap test and when a tie carries a correction.
4. [Round-91 ledger entry][ledger] for the two queued real tests and the route notes to open when resuming either one.

[format]: https://github.com/human-ai-mathematics/conjecture-search-template/pull/14/files
[snapshot]: https://github.com/lyw-ops/Paleygraph1/tree/9c734d28e1cf4f8df68482f6deac371058c6a2aa
[r91]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/round-91-acceptance.json
[ledger]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/ledger.md#round-91
[growth]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/parallel-cold-complex-36.md#3-uniform-growth-on-a-common-domain-with-explicit-constants
[column]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/astra-column-90.md
[contact]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/astra-contact-91.md
[switch]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/real-two-marks-91.md
[pin]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/astra-persistent-88.md
[quartic]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/astra-quartic-89.md
[discount]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/astra-discount-91.md
[fiber]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/astra-fiber-91.md
[contact-run]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/astra-contact-91-checks.jsonl
[switch-run]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/real-two-marks-91-checks.jsonl
[discount-run]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/astra-discount-91-checks.jsonl
[fiber-run]: https://github.com/lyw-ops/Paleygraph1/blob/9c734d28e1cf4f8df68482f6deac371058c6a2aa/research/astra-fiber-91-checks.jsonl
