# Round 181 native Claude draft: cold delocalization price (partial text)

- call_id: `cold-prime-delocalization-price`
- agent_label: `native-claude/cold_deloc_181`
- Mission: `coordination/missions/round-181/cold-prime-delocalization-price.md`
- Scripts in the repository from this lane:
  - `research/paley-181-cold-kantorovich-check.py`, from the draft's `cpdp_kantorovich.py`. Replay exited with rc=0.
  - `research/paley-181-cold-seed-price-check.py`, from `cpdp_seed_weighted_price.py`.
  - `research/paley-181-cold-leading-ranks-check.py`, from `cpdp_leading_ranks.py`.
- Audit script for this lane: `research/paley-181-audit-cold-constants-check.py`, from the auditor's `audit_r3.py`. Replay exited with rc=0.

**Partial — the full original text cannot be recovered.** The full draft (`cold-prime-delocalization-price-candidate.md`, 21439 bytes) was in a scratchpad directory that has since been cleared.

The coordinator's context holds two pieces of the original:
1. The agent's hand-back summary, reproduced verbatim below.
2. A verbatim excerpt from file line 30 to line 72: the "Setup recalled" section, and "§1 Prices live on price balls; the small-ball Kantorovich criterion" with its Proposition 1, proof and remarks.

Not recoverable:
- the title block and Result summary, file lines 1–29;
- §2 Exact price of the seed-linear multiplier;
- §3 Where the 1.066 comes from and the remaining budget;
- §4 Route (ii);
- §5 Route (iii);
- Proved vs conditional vs evidence;
- Exact remaining gap;
- Two ranked next tests;
- the outputs `cpdp_*.out`.

The file's section headings, from a grep at the time, were:
- "Cold prime delocalization price: a small-ball price criterion and the exact seed share"
- "Result summary"
- "Setup recalled"
- "Argument"
- "### 1. Prices live on price balls; the small-ball Kantorovich criterion (implication proved, (a))"
- "### 2. Exact price of the seed-linear multiplier ((a), compact model at each prime)"
- "### 3. Where the 1.066 comes from and the remaining budget ((a) for the crude parts, otherwise heuristic decomposition)"
- "### 4. Route (ii): fixed-height suprema and growing heights ((a) at fixed heights, (a/method) at growing heights)"
- "### 5. Route (iii): no concentration at the mark ((a) at fixed heights; no claim at growing heights)"
- "Proved vs conditional vs evidence"
- "Exact remaining gap"
- "Two ranked next tests"

---

## Agent hand-back summary (verbatim)

**Outcome: inconclusive.** I proved no n-independent delocalization bound and found no coordinate concentration. What changed is the form of the price route and the number it has to reach.

**Label (a), proved for all sufficiently large eligible primes:**
- **Small-ball criterion.** A price rate can only be certified on a price ball; the 3/8 coordinate polydisk contains vectors of unbounded price. Feed the Round 174/177 recursion u_{j+1} ≤ p0 + κ0·u_j + c·u_j² into a Kantorovich-type fixed-point argument. If (1−κ0)² > 4·c·p0 with strict slack, every displacement V_{602+j}−V_602 has price ≤ u_- ≈ 0.11 for all j. That gives confinement, Picard convergence and stationary continuation on the interior of Q.
- **What it avoids.** It needs no cutoff k_n, no Criterion D, no compact transfer and no ineffective 9.07e-209 bound. All heights are reached legitimately, by inductive convergent trace expansions.
- **Numbers.** With the inherited p0 = 0.01272 and c ≤ 1.0043, the frozen price rate at V_602 must be **κ0 < 0.7740**. The Round 180 "rate below 0.966 on the 3/8 polydisk" form, with the secant rate estimated as κ0 + 2cρ, would need κ0 < 0.052; optimising its radius gives κ0 < 0.684. Any recursion of this form needs κ0 < 1 whatever p0 is.
- **Seed part priced exactly.** The seed-linear multiplier has L² rate exactly 0.2510. Its price rate is ≤ 0.7101 in plain dimension price and ≤ 0.5326 in the weighted price r+z, sharp per simple. On the leading fields the exact rate tends to 0.5021, with E r_j = 2^{(j+1)/2} computed exactly for j ≤ 17.
- **Prices cannot feed Criterion D.** Price/RMS grows by a factor 2 per step, above 1/q = 1.835.
- **Other routes.** Fixed-height sup transfer holds through height 611 but is ineffective. Within the expansion method, route (ii) at growing heights reduces to route (i). Parity rules out concentration at the mark.

**Label (b), the remaining gap:** a signed, cross-vertex collected price at V_602 with κ0 < 0.774, against 1.066 now. The uncontrolled part is the transported non-seed multiplier: the nine-center deviation h = V_602 − S plus the higher Taylor terms. Its budget is about 0.24 (0.14 in the worst case), against a crude cost of about 0.50 for the h-linear term alone. Alternatively, a signed source price p0 ≤ 1e-6 would relax the target to κ0 < 0.998.

**Label (c):** no new physical runs. That E r_j = 2^{(j+1)/2} holds for all j is a conjecture from the exact values.

**Next tests, ranked:** (1) a collected weighted frozen price at V_602 by outward interval arithmetic; (2) a signed price for R_602.

Report: /private/tmp/claude-501/-Users-lyuyuwei--claude-spares-spare-6UwrMo/5c2fbe9f-e42f-418e-9bd9-cc365745ecfe/scratchpad/r181/cold-prime-delocalization-price-candidate.md (scripts and outputs are the cpdp_* files in the same folder).

---

## Verbatim excerpt of the draft, file lines 30–72

## Setup recalled

- **Parameters.** \(p\equiv1\pmod4\) prime, \(n=(p-1)/2\), \(a=2031/128\), \(Q\) the original closed square of half-width \(2^{-17}\), \(N=4(a-2^{-17})\). Physical mark \(t_0=n\), genuine nine-center start, both lifts.
- **Map.** \(V_{h+1}=K\Phi_t(V_h)\), \(R_h=V_{h+1}-V_h\). \(K\) is a real symmetric circulant with \(\|K\|_{2\to2}\le1\). The seed is \(S=2\sqrt nKe_0\), with \(s_p=2\sqrt{p/n}\to2\sqrt2\).
- **Norms.** \(\|\cdot\|_{2,n}\) is normalized second norm and \(\|\cdot\|_\infty\) the coordinate supremum. \(P=P_{5000}\) is the translated base-pair packet price of Rounds 126/162 on the unshifted class. It dominates the coordinate supremum and the dimension budget.
- **Inherited fixed inputs** (for all sufficiently large eligible primes; Deligne-type, with \(O(n^{-1/2})\) physical corrections):
  - \(P(R_{602})<p_0=0.01272\) (Round 174);
  - \(\|KD_{602}\|_P<1.066\) (Round 162);
  - \(P(\mathcal T_{V_{602}}(U))\le c(M)P(U)^2+O(n^{-1/2})\), with \(c(M)=\frac{2}{\sqrt N}(1+x/2)(1-x)^{-5/2}\), \(x=M^2/N\), \(M=4.823+P(U)\) (Rounds 162, 174, 177; \(c(5.198)<1.2183\));
  - \(\mathcal T_V(U)=K(\Phi_t(V+U)-\Phi_t(V)-D_VU)\).
- **Compact model** (Rounds 79/80). At each prime the trace expansions live on the arithmetic coset of the monodromy group \(G_p\); subsequential limits give the compact model.
  - Transport \(\mathcal K\) is an \(L^2\) isometry modulo constants and sends a positive simple of generic rank \(r\) to a negative simple of dimension \(r\).
  - Negative simples have pooled mass equal to pooled first absolute weight moment, both \(r\).
  - The conditional covariance identity is \(E(\bar hk\mid J)=\langle h,k\rangle\) for transported fields.
  - The line-shift/transport weight rule is the one tabulated in Round 80.
- **Fourier-algebra price.** For a trace field \(f=\sum_Mc_M\chi_M\), the sum taken over Frobenius-fixed geometric simples (twisted characters on the coset), put \(A(f)=\sum_M|c_M|d_M\). Then:
  - \(|f|\le A(f)\) on the coset, hence \(|R_{h,i}|\le A(f_{p,h})\) at good coordinates;
  - \(A(fg)\le A(f)A(g)\), because a tensor constituent of multiplicity \(m\) has twisted-trace coefficient of modulus at most \(m\);
  - every representation \(\sum_ja_j\chi_{M_j}\) satisfies \(\sum|a_j|d_{M_j}\ge A(f)\), so \(A\) is the minimal Deligne-type price.

## Argument

### 1. Prices live on price balls; the small-ball Kantorovich criterion (implication proved, (a))

A price rate \(\|K\tilde D\|_{P}\) is a statement about represented vectors of bounded price. The coordinate polydisk \(\mathcal P_\rho\) contains vectors of sup norm \(\le\rho\) and arbitrarily large price, on which no price bound for the Taylor remainder holds. A price argument therefore confines the orbit to a price ball \(\{P(U)\le u\}\), which lies inside \(\mathcal P_u\).

**Proposition 1.** Let \(P\) be a sup-dominating price on the unshifted class. Suppose there are constants \(p_0,\kappa_0<1,c>0,u\) such that, for all sufficiently large eligible \(p\), all \(t\in Q\) and both lifts:
- \(P(R_{602})\le p_0\) and \(\|KD_{602}\|_P\le\kappa_0\);
- \(P(\mathcal T_{V_{602}}(U))\le cP(U)^2\) whenever \(P(U)\le u\);
- the vanishing physical corrections are absorbed with strict slack;
- \(\Delta:=(1-\kappa_0)^2-4cp_0>0\) and \(u_-:=\frac{(1-\kappa_0)-\sqrt\Delta}{2c}\le\min(u,3/8-\eta)\) for some \(\eta>0\).

Then \(P(V_{602+j}-V_{602})\le u_-\) for every \(j\ge0\). The Picard rows converge for each \(n\) and \(t\), uniformly on \(Q\), to a stationary row that is holomorphic on the interior of \(Q\).

*Proof.* Write \(U_j=V_{602+j}-V_{602}\) and \(T(V)=V+R_{602}\) at \(V=V_{602}\). Then \(U_{j+1}=R_{602}+KD_{602}U_j+\mathcal T(U_j)\), so \(u_{j+1}\le f(u_j)\) with \(f(x)=p_0+\kappa_0x+cx^2\). On \(x\ge0\) the map \(f\) is increasing and \(f(u_-)=u_-\), so \(0\le x\le u_-\) implies \(f(x)\le u_-\). Starting from \(u_0=0\), induction gives \(u_j\le u_-\le u\), so the Taylor hypothesis stays applicable. The bad-character and mark corrections perturb \(p_0,\kappa_0,c\) by \(o(1)\) uniformly, and the strict discriminant absorbs them. Since \(P\) dominates the supremum, every row lies in \(\mathcal P_{u_-}\subset\mathcal P_{3/8}\) with clearance \(\eta\). There the map is \(0.545\)-Lipschitz in \(\|\cdot\|_{2,n}\) (Round 177). For each fixed \(n\), the finite-dimensional contraction on the convex polydisk gives uniform convergence in \(t\), and the limit is holomorphic on the interior of \(Q\) as in Round 173. ∎

Remarks on Proposition 1:
- **Uniformity.** Every constant is a Deligne-type pointwise bound, valid at all heights. Heights growing with \(n\) are reached legitimately: each \(U_j\) is constructed inductively as an absolutely convergent trace expansion of price \(\le u_-\). No fixed-height compact transfer is used, and the ineffective Round 80/179 constants are not used.
- **Numbers** (`cpdp_kantorovich.py`, 60-digit decimals, outward padding). With \(p_0=0.01272\), the self-consistent ball \(u=0.113\) has \(c\le1.004229\), and the condition is \(\kappa_0<0.773958\) with \(u_-\approx0.1126\).
- **Sanity checks.** The script reproduces \(c(5.198)=1.21823<1.22\) (Round 177) and \(c(4.873)=0.9617<1\) (Round 174).
- **Trade-off with \(p_0\).** \(p_0=10^{-3}\) needs \(\kappa_0<0.938\); \(p_0=10^{-6}\) needs \(\kappa_0<0.998\); \(p_0=10^{-12}\) needs \(\kappa_0<0.999998\). For every \(p_0\), \(\kappa_0<1\) is necessary for a recursion of this form to stay bounded.
- **Comparison with the Round 180 formulation** (\(\eta\to0\)). Estimating the secant rate on the price ball of radius 3/8 by \(\kappa_0+2c(3/8)\) gives \(p_0/(1-\kappa_0-0.914)<3/8\), that is \(\kappa_0<0.0524\). Optimizing the radius in that secant form gives \((1-\kappa_0)^2>8cp_0\), that is \(\kappa_0<0.684\). The displacement recursion is sharper because it charges \(cu^2\) rather than \(2cu\cdot u\).
