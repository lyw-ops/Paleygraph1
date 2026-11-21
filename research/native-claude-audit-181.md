# Round 181 independent native Claude audit (partial original text)

## Provenance

- **Audit of three calls:**
  - `ordinary-prime-one-match-slope-fibres` (`native-claude/one_match_181`)
  - `ordinary-prime-direct-first-mass` (`native-claude/first_mass_181`)
  - `cold-prime-delocalization-price` (`native-claude/cold_deloc_181`)
- **Auditor:** a separate native Claude subagent, label `native-claude/audit_181`. It was not recorded in `coordination/round-181-inflight.json`.
- **Audit scripts now in the repository:**
  - `research/paley-181-audit-one-match-check.py` (auditor's `audit_r1.py`); replay printed `ALL OK`.
  - `research/paley-181-audit-first-mass-check.py` (auditor's `audit_r2.py`); replay printed `OK`.
  - `research/paley-181-audit-cold-constants-check.py` (auditor's `audit_r3.py`); replay exited with rc=0.
  - Not copied and now lost: `tj.py`, `pdfx.py`, and the auditor's extracted copy of the Shkredov PDF.

## What survives

**This is partial: the full original text cannot be recovered.** The full audit was `audit-181.md`, 16177 bytes, in a scratchpad directory that has since been cleared.

The coordinator's context holds two things:
1. The auditor's hand-back summary, reproduced verbatim below.
2. A verbatim excerpt from the start of the file through the heading "**Corrections.**" in §1.7. It was displayed with `cut -c1-600`, so any line longer than 600 characters is truncated at that point.

The following cannot be recovered:
- the body of §1.7 "Corrections" and any later Report 1 items, such as the verdicts on criteria b1, b1′, b2 and b3;
- the whole Report 2 (first mass) section;
- any closing overall summary.

For those parts only the hand-back summary remains.

---

## Auditor hand-back summary (verbatim)

Round 181 audit is done. None of the three reports proves the original target. I found no outright mathematical errors, but each report needs corrections. The full audit is at /private/tmp/claude-501/-Users-lyuyuwei--claude-spares-spare-6UwrMo/5c2fbe9f-e42f-418e-9bd9-cc365745ecfe/scratchpad/r181/audit-181.md, and my check scripts are in /private/tmp/claude-501/-Users-lyuyuwei--claude-spares-spare-6UwrMo/5c2fbe9f-e42f-418e-9bd9-cc365745ecfe/scratchpad/audit181/. No repository files were changed.

**Report 3 (cold price):**
- **Proposition 1: CONFIRMED-WITH-CORRECTION.** The recursion comes from an exact frozen-base identity at V_602, so it holds at every height j. Sources 130/162/174 state the small-error corrections uniformly over inputs, which lets the induction reach all heights without compact transfer. Rounds 174/177 only applied it at fixed steps, so two hypotheses must be stated: the price class is closed under the recursion, and the error constants are uniform over inputs.
- **Threshold:** the true value is κ0<0.77395, not 0.7740; c(4.936)≤1.0043 holds exactly.
- **Scope:** the proved bound for the existing price P_5000 is 1.066, so a new price is needed, and its p0 and c are unproved.
- **Seed rates** 0.2510, 0.7101 and 0.5326, and E r_j=2^{(j+1)/2}: CONFIRMED.
- **"Price/RMS grows by 2, so prices can never feed Criterion D":** overstated. It is shown only for the leading seed fields and relative to q=0.545.
- **Budget split, and route (ii) sup transfer through 611:** GAP; both are heuristic or sketched.
- **Route (iii), parity at the mark:** CONFIRMED but adds nothing beyond what the price bound already gives.

**Report 1 (slope fibres):**
- The splitting identity, the Hilbert–Schmidt identity, S=ΣΔm_t, the a=1 and c=0 fibre costs, and the generic overlap formula all hold exactly at p=13, 17, 29.
- **"Target ⇔ S_gen=O(p²)":** true only for the completed-upper chain and after w-averaging.
- **Obstruction configuration:** every exponent checks against the listed inequalities only, not "all proved constraints" (positive-definiteness, realisability and level-set constraints are unchecked).
- **Criteria b1, b1′, b2, b3:** CONFIRMED.

**Report 2 (first mass):**
- The reformulation matches the direct chart and the Round 180 cross-ratio labels exactly at p≤41. "s=b iff A=C" is a typo for A=κC.
- M_w≤¼E_Q and the O(p^{1−3/418}) trivial-frequency cost: CONFIRMED.
- **Shkredov Theorem 6:** checked against the arXiv PDF text; hypotheses |Γ||Π|<p and x,y≠0 match.
- **Correction:** at |H|=p^{1/2−1/2560} the bound is O(p^{1+1/1280}·log p), not O(p log p).

---

## Verbatim excerpt of `audit-181.md` (start of file through "**Corrections.**" in §1.7; lines truncated at 600 characters)

# Round 181 independent audit

This audit was written by an agent. It is not a human review and not an acceptance. No repository file was modified.

My own scripts are in `scratchpad/audit181/`. All use the Python standard library only.
- `audit_r1.py`: exact Fractions, p = 13, 17, 29, two random seeds each.
- `audit_r2.py`: exact, p = 13, 17, 29, 37, 41.
- `audit_r3.py`: rational comparisons, checked by squaring.
- The Shkredov paper was fetched from arXiv. Its text was extracted with stdlib zlib and read directly.

The sources were checked against the research notes for Rounds 80, 126, 130, 162, 173, 174, 176, 177, 178, 179 and 180, at the cited lines.

---

## Report 3: cold prime delocalization price (priority)

### 3.1 Proposition 1, the small-ball (Kantorovich) criterion

**Verdict: CONFIRMED-WITH-CORRECTION.** The implication is valid as a conditional criterion. It is not a result for \(P_{5000}\).

**What I checked.**

*The recursion comes from an exact identity, not from moving rows.*
- The identity is \(U_{j+1}=V_{603+j}-V_{602}=R_{602}+KD_{602}U_j+\mathcal T_{V_{602}}(U_j)\). It holds at every \(j\), because \(V_{603+j}=K\Phi_t(V_{602}+U_j)\).
- So the recursion needs only frozen-base bounds at \(V_{602}\) that are uniform over the input class:
  - the operator price \(\|KD_{602}\|_P\);
  - the Taylor bound \(P(\mathcal T(U))\le c\,P(U)^2\) for \(P(U)\le u\).
- No moving-secant bound is needed. This is a legitimate and sharper reformulation of the Round 180 test.

*\(\kappa_0\) is the frozen operator price at \(V_{602}\).* For \(P_{5000}\) the only proved bound is \(\kappa_0<1.066\) (Round 162). Round 162 builds this as the height-601 rate \(1.048\) (Round 130) plus the multiplier increments.

*Where the inherited constants come from, and their scope.*
- \(p_0=0.01272\) is \(P_{5000}(R_{602})\) (Round 174: \(1.048\cdot0.012+0.000140\)). It is a fixed-height input.
- \(c(M)=\frac{2}{\sqrt N}(1+x/2)(1-x)^{-5/2}\) is the Round 174 coefficient, with \(M=4.823+P(U)\) and the dimension bound \(4.823\) for \(V_{602}\) (Round 174).
- Exact rational checks:
  - \(c(4.936)\le1.0043\) is true, and \(c(4.936)\le1.0042\) is false;
  - \(c(5.198)<1.22\) is true, and \(c(5.198)<1.2182\) is false;
  - \(c(4.873)<1\) is true.

*Threshold arithmetic.*
- With \(c=1.0043\), \(\kappa_0=0.7739\) gives a positive discriminant and \(u_-=0.1102\le0.113\).
- \(\kappa_0=0.77395\) already fails.
- The report's value \(0.773958\) uses the unrounded \(c=1.004229\).
- **Correction:** the "0.7740" in the brief should read \(\kappa_0<0.77395\). The report's own "0.7739" is safe.
- Iterating the recursion from 0 converges to \(u_-\).
- My replay of the Round 177 ten-step table matches 1272, 2648, 4181, … ×10⁻⁵.

*Uniformity in \(j\) without compact transfer.*
- The vanishing corrections are stated uniformly over the input class in the sources:
  - Round 130: \(O_{5000}(n^{-1/2})\) "relative to the input price, uniformly over translated sources";
  - Rounds 162/174: the Taylor correction is \(O(n^{-1/2}A^2)\) "uniformly by the convergent dimension sum".
- Under that reading, the threshold "for all large \(p\)" does not depend on \(j\), and the induction reaches all heights.
- The sources, however, applied the recursion only to fixed steps:
  - Round 174: "for the fixed steps considered here … not a growing-depth convergence estimate";
  - Round 177: "fixed prefix".
- The reason there was the radius, not uniformity. Even so, applying the recursion for all \(j\) is new.
- **Correction:** Proposition 1 should state two items as explicit hypotheses, or prove them as a lemma:
  - closure of the unshifted packet class under \(R_{602}+KD_{602}(\cdot)+\mathcal T(\cdot)\), by induction on representations;
  - uniformity of the correction constants over all inputs of price at most \(u\).

*Sup domination, the mark and the lifts.*
- \(P_\Lambda\ge\) dimension dominates good coordinates. Bad characters and the mark enter only as the \(O(n^{-1/2})\) corrections.
- \(u_-\approx0.11\le3/8-\eta\) leaves the orbit inside the Round 177 polydisk, where the counting Lipschitz rate is \(q=0.545\), the mark is included because \(t_0=n\), and the radicand margin holds.
- Then \(\|R_{602+k}\|\le q^k\|R_{602}\|\) gives Picard convergence for each \(n\), uniformly on \(Q\). The limit is holomorphic on the interior.
- So the conclusion would indeed give stationary continuation on the interior of \(Q\), for both lifts and at the physical mark, provided all hypotheses hold uniformly in \(t\) and in both lifts.

**Main caveat (scope).**
- For \(P_{5000}\) the hypothesis is not met: the proved bound is 1.066.
- The report itself cites Round 83: single-vertex collection expands above 1.0029. So \(P_{5000}\)-type unsigned prices probably cannot reach \(\kappa_0<1\) at all.
- A new price is therefore needed. Its \(p_0\), \(c\), sup domination, class closure and correction uniformity must all be re-proved.
- The number 0.774 is meaningful only if \(p_0\) and \(c\) carry over unchanged. Calling it "the remaining gap" is a heuristic target, not an exact gap.

### 3.2 Comparison with the Round 180 form (κ0<0.052 and the optimised 0.684)

**Verdict: CONFIRMED-WITH-CORRECTION.**
- The arithmetic is right: \(1-0.01272/0.375-2(1.2182)(0.375)=0.0524\), and the optimised condition is \((1-\kappa_0)^2>8cp_0\).
- But the "secant rate \(\approx\kappa_0+2c\rho\)" is the candidate's own crude model of the Round 180 moving-secant price. It is not a statement from Round 180. So "the Round 180 form needs \(\kappa_0<0.052\)" means only "under this estimate".

### 3.3 Seed-linear rates

**L² rate \(s_p/(2\sqrt2|\sqrt t|)\to0.2510\): CONFIRMED** (inherited from the compact model).
- Round 80 (4): multiplication by \(s_pC\) followed by transport scales inner products by \(s_p^2/2\) on outputs of \(\mathcal K\).
- Dividing by \(2|\sqrt t|\) gives the stated rate.
- With \(s_p\to2\sqrt2\) and \(|\sqrt t|\approx3.983\), the value is 0.25104.

**Price rates 0.7101 (plain dimension) and 0.5326 (\(\pi_1\)): CONFIRMED** as a linear-fractional programme on the Round 80 weight and fill rule.
- I rederived the extreme rays by hand:
  - support \(\{|w|=1\}\) gives ratio \(2+\alpha\);
  - support \(\{0,k\}\) gives \(\frac{4k-2+\alpha(2k-2)}{k+\alpha(k-1)}\to\frac{4+2\alpha}{1+\alpha}\).
- The minimax is at \(\alpha=1\) with value 3. This gives \(3s_p/(4|\sqrt t|)=0.53255\). At \(\alpha=0\) the supremum is 4, giving 0.7101.
- Caveat: the rule is per simple and in the compact model at each prime. It is a bound for inputs in the negative span of dimension above one, not a physical statement.

**Leading-field ranks: CONFIRMED.**
- \(E\,r_j=2^{(j+1)/2}\) at odd \(j\le17\) (exact output). The worst path \(r_j=j+2\) holds through \(j=40\).
- The rate \(\sqrt2\,s_p/(2|\sqrt t|)\to0.5021\) follows. The pattern for all \(j\) is a conjecture, as the report says.

### 3.4 "Price/RMS grows by 2, so prices cannot feed Criterion D"

**Verdict: CONFIRMED-WITH-CORRECTION.**
- The factor 2 is exact on the leading seed fields \(H_j\) (asymptotically, and through \(j=17\)).
- "A Deligne-type price can never certify Criterion D" overreaches:
  - it is proved only for the leading fields, not for the actual increments;
  - it is relative to the currently available counting contraction \(q=0.545\). A proved L² rate near 0.25 would raise \(1/q\) to about 4.
- This should be stated as method evidence.

### 3.5 Budget split (seed share 0.533, non-seed about 0.24, \(h\)-linear about 0.50)

**Verdict: GAP (heuristic).** The report labels this heuristic. In addition:
- \(A(h)\le4.823-2.8285\) assumes the seed simples occur in \(V_{602}\)'s minimal representation with exactly the seed coefficients. This is not shown.
- Mixing the \(\pi_1\) seed price with \(P_{5000}\)'s \(p_0\) and \(c\) is not a lemma.

### 3.6 Route (ii): fixed-height sup transfer through 611

**Verdict: GAP.** The argument is a sketch: uniform truncation plus Hausdorff convergence of the block groups along subsequences. It is not verifiable from the cited sources, and bad coordinates are not treated. It is not used by Proposition 1. The method conclusion at growing heights is reasonable as method commentary.

### 3.7 Route (iii): parity at the mark

**Verdict: CONFIRMED-WITH-CORRECTION.**
- The central-character parity is right:
  - \(\Phi'\) is odd, since \(\Phi=\sqrt{4t+x^2}\);
  - \(S\), \(\tilde D\) and the increment each carry character \(-1\).
- The conclusion "\(R_{h+1,0}=O(\text{price})\)" is already implied by sup domination, so it adds nothing new.

### 3.8 (b) Remaining gap κ0<0.774 against 1.066

**Verdict: CONFIRMED,** with the scope caveat in 3.1: a new price with its own \(p_0\) and \(c\) is required.

---

## Report 1: one-match slope fibres

### 1.1 The splitting \(S(t)=M_1^2G^2/p+\|\pi(\mu)h_t^\circ\|^2\), and \(S=\sum_h\Delta m_t\)

**Verdict: CONFIRMED.**
- I rebuilt \(\mu\) on the Round 171 chart from scratch, with the square mask on \(b\), \(Y\ne D\) and labels not in \(\{0,1\}\). Injectivity was asserted.
- Checked exactly at p = 13, 17, 29, for every \(t\ne0\) and two seeds:
  - every kernel row sum equals \(M_1\);
  - the splitting identity holds;
  - \(S(t)=\sum_h\Delta(h)m_t(h)\), with \(h^{-1}e=(e-c)/a\).

### 1.2 Hilbert–Schmidt identity \(\|\pi(\mu)\|_{HS}^2=p\sum\mu^2-\sum m^2\)

**Verdict: CONFIRMED** (exact, same runs).
- The bound \(S\le G^6/p+p\Gamma^3\) follows from \(\sum\mu^2\le\Gamma^2\) and \(M_1\le G^2\). This gives criterion (b1).
- The arithmetic for (b1′) is right:
  - \(\|\pi\|_{op}\le(pE)^{1/4}\);
  - \(p^{75/32}\) at the current \(E\);
  - the trivial range \(p^{59/64}\).

### 1.3 Translation fibre \(a=1\) and dilation line \(c=0\) cost \(O(p^{2-3/418})\) per \(t\)

**Verdict: CONFIRMED.**
- Exact checks:
  - \(\sum_c\Delta(1,c)=\sum_r m(r)^2\);
  - \(\sum_a\Delta(a,0)=\sum_b n_b^2\);
  - \(\sum_c\Delta(a,c)=\sum_r m(r)m(ar)\) for every \(a\).
- \(m_t\le G\).
- The source bounds check out:
  - \(\sum m^2=O(p^{3/2-3/418})\) (Round 177, as restated in Round 178);
  - \(\sum n_q^2=O(p^{3/2-3/418})\) (Round 177, as cited in the Round 178 parabolic note).

### 1.4 Generic overlap \(m_t(a,c)=\sum_x g(x)g(atx/(t-cx))\) and the bound \(p^{1/2-1/1280}\)

**Verdict: CONFIRMED.**
- The formula was checked exactly for all generic \((a,c)\) and all \(t\).
- After inversion, \(1/\varphi\) is affine in \(1/x\) with \(\alpha\beta\ne0\). The Round 174 affine bound, or the Round 176 nonmonomial bound, applies.
- Minor: §2 cites Round 174 while the summary cites Round 176. Both are valid sources.

### 1.5 "Target ⇔ \(S_{\rm gen}(t)=O(p^2)\)"

**Verdict: CONFIRMED-WITH-CORRECTION.**
- The equivalence holds only for the completed-upper chain \(H_\alpha\le F_\mu h_t\), and only in \(w\)-average.
- "Uniformly in \(t\)" is sufficient, not necessary.
- It is not an equivalence with the original one-match target. The body of the report says so, but summary item 1 does not.

### 1.6 Per-fibre additive energies

**Verdict: CONFIRMED.**
- The identity \(\sum_aE^+(U,aU)=(p-1)N^2+N^2(N-1)^2\) is a correct count.
- The route returns \(E^{1/2}p^{1/2}N=p^{75/32}\).

### 1.7 Obstruction configuration with value \(p^{147/64}\)

**Verdict: CONFIRMED-WITH-CORRECTION.**
- I recomputed every exponent by hand and reran the script. All listed constraints hold:
  - \(M_1=p\);
  - \(C(a)=p^{11/8}\);
  - \(W_\xi=p^{11/8}\) on \(R\), so \(\sum W^{3/2}=p^{43/16}\) and \(E^\times=p^{27/8}\);
  - \(E(\mu)=p^{43/16}\);
  - transverse mass \(p\);
  - rich count \(N^5/t_0^4=p^{21/16}\);
  - the per-slope overlap mass \(p^{63/64}\le N^2\);
  - the exact identity \(\sum_{a,c}m'^2\approx2p^2\) can also be met.
- The value matches the Round 180 output: \(p^{1/8}E^{1/4}M_1\) for the covariance, i.e. 115/64.
- The source bounds are correctly stated:
  - Round 178 transverse mass \(O(p^{3/2-\kappa/2})\). The parabolic note's stronger \(O(p^{23/16-3/836})\) also holds in the configuration.
  - Round 176 generic \(p^{1-1/1280-1/840}\); Round 174 translation \(p^{1-2/1280}\) and dilation \(p^{1-1/1280}\).
  - Rich lines \(U^5/t^4\) for \(t\ge C\max(1,U^2/p)\).

**Corrections.**

[The excerpt ends here. The rest of the original audit is not recoverable; see the hand-back summary above for the remaining Report 1 and Report 2 verdicts.]
