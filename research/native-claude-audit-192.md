# Independent audit of Round 192 (session/r192-audit)

- **Auditor:** Claude subagent started by the Round 192 coordinator (session/r192-audit). This is an agent audit, not human acceptance and not a mathematical certification. The auditor did not write the report and is not the coordinator.
- **Status of this file:** written incrementally. The "Blind overlap review" section below was saved before any file under `coordination/shared-obligations/`, `coordination/drafts/` or any `coordination/round-*-inflight.json` was opened.
- **Read before the blind review:** `AGENTS.md`, `docs/WORKFLOW.md`, `docs/ROUND_REVIEW.md`, `coordination/checkpoints/round-191.md`, `research/native-claude-audit-191.md`, the mission `coordination/missions/round-192/ordinary-nc-vertex-tightness.md`, and the report.

Verdict key (per claim the report labels as proved, or as bookkeeping that the coordinator may carry forward):
- **ACCEPTED:** correct as written, for the stated hypotheses.
- **ACCEPTED WITH CORRECTION:** true after the stated correction, which does not change the report's main conclusion.
- **CONDITIONAL:** correct given a named input that is not proved or not checked.
- **REJECTED:** false as written, or not supported.

Report, abbreviated:
- **VT** = `research/native-claude-ordinary-nc-vertex-tightness-192.md` (Proposition A, Lemma S, Proposition B / Corollary B, Proposition C, Lemma J / Corollary J, Proposition D, Proposition F, (SS)/(SS\*) and Theorem E, §4, §6 exponents), with `research/paley-192-vertex-exponents.py`, `research/paley-192-vertex-models.py`, `research/paley-192-vertex-sharp-search.py`. Report verdict: inconclusive; (V) fails on (NC) if (SS\*) holds.

## 1. Blind overlap review

Written after reading the report and its mission only. No shared-obligation, draft or inflight file had been opened. Round 192 is a single call, so there is no pair to compare; the review covers candidate touches and repetition of Rounds 183–191.

**Candidate touches.**
- `cand:gp-sector-constancy`: **contextual touch, not in value.** VT uses no sector statement along geometric progressions. Lemma J is a sector count on a *full subgroup* \(\Gamma\) of order \(>\sqrt p\), which is the complete-progression end of the (GP-Sub) family; there Jacobi/Weil sums settle it and (GP-Sub) is not needed. The §3 remark that a failure of (SS) through progression-shaped spectra would need (GP-Sub) is a forward-looking remark, not a use. Value and status unchanged.
- `cand:gp-shifted-energy`: **not touched.** No energy of shifted progressions appears.
- `cand:slope-row-mass-x`: **contextual touch only.** Lemma S (c) lists the SRM Prop. 2 floor \(X\ge(2-o(1))p\) among the sector forms and observes that it says nothing about low-level vertex mass on \(T_\rho\). No bound on \(X\) is used or changed.
- **New proposed ID:** `cand:sharp-spectrum-structure` = (SS)/(SS\*), proposed by VT, not recorded. Single call, so `shared_candidates` would not need it under AGENTS.md unless a later call needs the same estimate.

**Repetition of Rounds 183–191 (to be checked after unblinding and in §2).**
- Proposition C item 2's consequence \(a\le\frac12+o(1)\) is ASM C5 / AUD191 (a8), already accepted; the new content is the lower bound \(|\Lambda_a|\ge(2-o(1))\sqrt p\) and the uncertainty product.
- Proposition F's first bullet (the \(\mathbb F_{r^2}\) control satisfies (V) with \(m_{<a}\approx2\)) was already recorded by ASM and AUD191 §2.5 ("Square-field control"); the new content is the check that the control satisfies every sector form.
- Lemma J looks like a specialisation of statements already accepted in Round 191: the GPSUB Vinogradov consequence (AUD191 (g4): \(E_\rho\ge(M-\sqrt p)/2\) on a geometric progression of length \(M\)), and R190's Jacobi-sum input (R190:112–114). For a full subgroup, Vinogradov with \(A=B=\Gamma\) gives \(|\sum_{y\in\Gamma}\chi(1-y)|\le\sqrt p\), the same bound up to the strict inequality. If so, Lemma J is correct but not new; to be checked.
- Proposition B(ii) rests on the accepted R190 Theorem 4; B(i) (random flat laws in \(\mathcal H\)) upgrades ASM §5.3 model evidence and R190 Cor. 4.1(iii). To check whether R190 already contains the random-flat statement.
- Theorem E, Proposition A, Lemma S and Proposition D look new.

**Would an overlap review have changed dispatch?** No: there was one call, chosen by the user.

### After unblinding

Opened afterwards: `coordination/round-192-inflight.json`, `coordination/shared-obligations/round-192-before.json` (SHA-256 `6e0725f1…7c12b`, matches the inflight binding) and `coordination/drafts/round-192-dependency-assessment.json`. No `round-192-after.json` exists yet. `coordination/round-191.json` (`5af57ceb…7296ad`, matches the mission header and the inflight binding) has `shared_candidates: []`.

- The pre-dispatch comparison (`comparison_status: assessed`, `known_shared: []`, `candidate_ids_by_call` empty for the one call) says the call "touches cand:gp-sector-constancy only if it uses the sector forms along geometric progressions, and it is asked to state any such use". **Agreement:** VT states its use explicitly (§3 remarks, §8) and does not use sector forms along progressions; my blind classification (contextual touch, not in value) agrees.
- **Difference:** none in classification. The comparison did not anticipate the `cand:slope-row-mass-x` contextual touch (Lemma S (c)); it is harmless and changes nothing.
- **Dispatch effect:** none. Lane label `session/r192-vertex-tightness`; mission file hash in the manifest (`1f1d3c4d…54967`) matches the file on disk; the report's script hashes match the files on disk (§3). The report header calls the author "Claude session started by the Round 192 coordinator", consistent with the manifest.
- **Candidate bookkeeping:** VT proposes `cand:sharp-spectrum-structure`. Assessed in §4.3.

## Summary of verdicts

| Item | Verdict | Correction or condition |
|---|---|---|
| (v1) Source hashes; branch hypotheses R157:3, R160:3, (NC) R183:53 | **ACCEPTED** | All nine mission sources and the three script hashes match. |
| (v2) **Proposition A** (transfer to \(S\); \((\mathrm V_{\rm rel})\) is a sharp-spectrum property of \(S\)) | items 1–4 **ACCEPTED**; item 5 **ACCEPTED WITH CORRECTION** | Item 5 is a remark about the available transfer (error \(o(\sqrt p)\)), not a theorem that \(S\) cannot determine (V) on (NC). |
| (v3) **Lemma S** (no accepted (NC) statement constrains the level distribution of \(g\) on \(T_\rho\) at absolute scale) | **ACCEPTED WITH CORRECTION** (bookkeeping) | True for every accepted statement about \(g\). It omits the exact linear identities \(\sum_Qf\overline{\psi^j}=n\nu_j\ge0\) (any law), e.g. \(\sum_{T_\rho}f=-1-\sum_{T_{-\rho}}f=O(\sqrt p)\). These are absolute-scale statements on \(T_\rho\) about \(f\); with R190 Lemma 1 they are the whole content of (NC). No accepted argument extracts level information from them, so the conclusion stands. |
| (v4) **Proposition B, Corollary B** (sector-free method cap) | (i) **ACCEPTED**; (ii-1) **ACCEPTED**; (ii-2) **ACCEPTED WITH CORRECTION**; Corollary B **ACCEPTED** | (ii-2) is for the Bernoulli variant of \(D_\theta\). Its membership in \(\mathcal H\) is asserted "by the same proof" and was not re-derived item by item. §0 item 2 attributes the both-signs bound \((1-3\theta)/2\) to "the \(D_\theta\) laws (R190 Theorem 4)". For R190's fixed-size \(D_\theta\) only the heavier-sign bound \(\frac12-\theta\) is proved. The cap does not need (ii-2): the random flat law (i) covers both signs. |
| (v5) **Proposition C** and the treatment of the Round 191 heuristic | **ACCEPTED** | Prop. C is Cauchy–Schwarz plus (A2) and Chebyshev. It excludes *near-equality stability* of the uncertainty principle as the mechanism. It does not exclude every structure argument: the constant-factor form gives only high energy, \(\mathcal E(S)\ge(a-o(1))|S|^3\) (§2.5). |
| (v6) **Lemma J, Corollary J** | **ACCEPTED** (not new) | A classical complete-subgroup bound. It is the full-progression case of the accepted Round 191 Vinogradov consequence (AUD191 (g4)), and equals Vinogradov's bound with \(A=\Gamma\), \(B=-\Gamma\) for \(\Gamma\le Q\). Corollary J (robust to \(o(\sqrt p)\) exceptions) is a correct small addition to R190 Prop. 2(4). |
| (v7) **Proposition D** (two-subgroup sharp family) | items 1, 3 **ACCEPTED**; item 2 **ACCEPTED WITH CORRECTION**; as a cap over sequences **CONDITIONAL** (b2) | (A6) is checked in the report only for \(\delta<350/256\) (the crude \(3/4\) bound). The full range \(\delta\in(0,2)\) needs the refined count (§2.6), under which the share is \(\le\frac12+o(1)\) for bounded \(d\). It is then true, and verified numerically for every subgroup of order \(\le2m_0\). The cap is conditional on \(\mathcal P\) being infinite with tolerances \(\to0\); the §2.6 "Cap" sentence that uses Prop. D must carry that condition. |
| (v8) **Proposition F** (field-general cap on refuting (V)) | **ACCEPTED** | Exact: \(m^Q_{<a}=2\) (the report's \(2(r+1)/(r-1)\) is a valid upper bound). Every listed sector form, and the (A2) and (A4) violations, were re-checked with independent \(\mathbb F_r[i]\) arithmetic. The (A5) item 2 and (A6)(a) violations are immediate, since \(S\) is a subgroup minus a point. |
| (v9) **(SS), (SS\*), Theorem E** | Theorem E **CONDITIONAL** on (SS\*), and correct as an implication. (SS\*) is field-free and unproved; quantifiers need to be fixed as in §2.9. | Interpretive correction (important): (NC) is the hypothetical branch the programme tries to empty. Given (SS\*), (V\(_{\rm rel}\)) on (NC) is not "false of an actual law". It *implies the emptiness of (NC)* by itself, through (A4), without (A-slope). (V) is therefore of target depth on the critical branch, not an independent lever. |
| (v10) §0 item 6 / §4 "(V) and high energy independent in both directions" | **REJECTED** as written | (V) implies \(\sum g^2\ge(a-o(1))G_\rho\) (ASM C5, accepted Round 191 (a8)); only "high energy does not imply (V)" holds (\(D_\theta\)). Prop. D's energy \(\frac14\) is consistent with the implication (\(a<\frac14\)). |
| (v11) §6 loss exponents, §5.4 exact arithmetic | **ACCEPTED** | Recomputed in Fractions (audit Part X). Note: several of the report's 48 "checks" are identities of the form \(x=x\). The substantive exact checks are fewer, though all are correct. |
| (v12) §5 evidence (models, search) | **ACCEPTED as evidence** | Every quoted row reproduces. The report itself says the annealing search is too weak to support (SS); I agree. |
| (v13) "probable answer no" (§0), "very unlikely" (§8), "counterexample to a robust idempotent theorem" (§8) | **ACCEPTED WITH CORRECTION** (labelling) | This is an agent expectation. Its support is the exact case (Green–Sanders, quoted from memory and not checked by me) and heuristics; the finite evidence is weak by the report's own account. (SS\*) is not a theorem, so "counterexample to a robust idempotent theorem" should read "counterexample to an unproved sparse robust idempotent statement". |
| (v14) §0 item 7 (no explicit (NC) family with current knowledge) | **ACCEPTED** (reading) | R190:351–354 says so verbatim in substance. Exhibiting an (NC) law is the open near-critical question itself. |
| **Verdict "inconclusive"** (mission definition; exact decisive statement recorded) | **ACCEPTED** | The decisive (NC) statement is "the near-critical support \(S\) has no sharp spectrum", i.e. \(\neg(\mathrm V_{\rm rel})\). (SS\*) is a field-free sufficient condition for it. Decision after the call: hold. |

## 2. Per-claim review

**Sources checked.** The full report and mission; the three scripts (read; replayed). At source, line by line:
- R20 `anchored-repair-20.md` lines 66–76 ((A1) flat and signed);
- R151 `ordinary-prime-coset-spread-151.md` (all, especially lines 5, 26–47 for (A4));
- R153 `ordinary-affine-jacobi-factorization-153.md` lines 5–11 (cap);
- R157:3 and R160:3 (branch hypotheses);
- R183 lines 47–125 (setup, (NC), Props. 1.1, 1.2, 1.4);
- R184-SE lines 30–170 (Lemma 0, Prop. 1, Theorem 2, Cor. 3, Prop. 4, (Sub\(_C\)));
- R184-SRM lines 128–141 (Prop. 2);
- R190 lines 70–176 (setup, Lemma 1, Theorem 1, Lemma 2, Prop. 2) and 186–240, 340–360 (Theorem 4, Corollary 4.1, remaining gap);
- ASM lines 196–212 ((A\(_V\)), (V), §5.2);
- AUD191 in full;
- the GPSUB report §2.6;
- R183 acc:264, acc:270, R184 acc:273, R190 acc:295, and the Round 185–191 acceptance lines that mention (NC).

### 2.1 Hypotheses and the classification table (v1)

- The branch hypotheses are cited correctly (R157:3: critical-size branch, actual \(b_0=0\), relative pin bound; R160:3: the physical row \(F(x)=f(1-vx)\)).
- R183:53 defines (NC). R190 Lemma 1 (accepted, R190 acc:295) shows that (NC) is *exactly* (NC1) plus \(V_{-\rho}\to0\), for laws with \(b\ge0\), \(b_0=0\).
- Every row of the §1 table matches its source:
  - cap: R153:5 "\(\max\nu_j=O(p^{-1/2})\)";
  - (A2): R183:104–120;
  - (A3): R183:76–91;
  - (A4): R151:47 "the relative Fourier mass outside every such \(B\) has a uniformly positive lower bound in this critical case";
  - (A5): R184-SE:79–114;
  - (A6): R184-SE:148–159;
  - SRM Prop. 2: R184-SRM:130–139.
- The "sector / sector-free" labels agree with R190 Cor. 4.1 (\(\mathcal H\), R190:228–233) and with its accepted correction (M\(_1\) and the SRM floors are sector-derived).
- I searched the Round 185–191 acceptance records for further (NC)-specific statements. They contain bounds valid for all admissible laws (band, Lemma M′, Theorem A, the \(T_0\) and \(X\) bounds) and R190 Prop. 3 (on \(T_{-\rho}\)). None constrains low levels on \(T_\rho\), so the table is complete for the purpose of Lemma S.

### 2.2 Proposition A (v2)

1. \(\nu-\mathbf 1_S/|S|=\|\nu\|(e-u_S)+(\|\nu\|-|S|^{-1/2})u_S\), with \(\|\nu\|_2=m_{\rm eff}^{-1/2}\) (R183:52) and \(|S|\sim m_0\sim m_{\rm eff}\). This gives \(o(m_0^{-1/2})\). Parseval on \(\mathbb Z/n\) gives \(\sum_Q|f-f_S|^2=n\|\nu-\mathbf 1_S/|S|\|^2=o(\sqrt p)\). Then \(\big||f|^2-|f_S|^2\big|\le|f-f_S|(|f|+|f_S|)\) and Cauchy–Schwarz give \(\Delta\le o(p^{1/4})\,O(p^{1/4})\). **Correct.** Checked numerically on perturbed flat laws (audit Part A: Parseval identity and \(\Delta\) bound at \(p=10009,40009\)).
2. **Level transfer.** The points with \(g<a\le b\le g'\) number at most \(\Delta/(b-a)\), and each contributes \(<a\). The rest contribute at most \(\sum_{g'<b}g'+\Delta\). The total is \(\Delta(1+a/(b-a))=\Delta b/(b-a)\), exactly the stated constant. **Correct.** Audit Part T: 20000 random instances.
3. \(Q\setminus\{1\}=T_+\sqcup T_-\) and \(g(1)=1\), so \(m^Q_{<a}-G_{-\rho}\le m_{<a}\le m^Q_{<a}\). **Correct** (Part A, both signs).
4. The two directions use levels \((a/2,a)\) both ways, and the normalization is \(\sum_{x\ne1}g_S=n/|S|-1\sim\sqrt p\). **Correct.**
5. "(V) at scale \(o(D)\) is not determined by \(S\)" is not proved as a statement about (NC) laws: no two (NC) laws with the same \(S\) are exhibited, and none can be (v14). What is proved is that item 1 is the only accepted link between \(g\) and \(S\), with error \(o(\sqrt p)\). **ACCEPTED WITH CORRECTION** (read as a statement about the transfer).

### 2.3 Lemma S and the absolute-scale claim (v3)

- (a)–(c) are correct:
  - \(G_\rho=G-1-G_{-\rho}\);
  - \(\sum_{T_\rho}g^2\ge\sum g^2-1-G_{-\rho}\) since \(g^2\le g\);
  - R190 Theorem 1(4);
  - \(M_1=\sum_\varepsilon(G_\varepsilon^2-\sum_{T_\varepsilon}g^2)\) (R183:89), and the SRM floors follow from \(M_1\) by Cauchy–Schwarz (R184-SRM:135–139).
- **Why the scalars cannot give (V) (strengthening the report's reading).** The only way a scalar pair \((G_\rho,\sum_{T_\rho}g^2)\) bounds low-level mass is through \(m_{<a}\le(G_\rho-\sum_{T_\rho}g^2)/(1-a)\), since \(g\le1\). By (A2), \(\sum g^2\le(\frac12+o(1))\sqrt p\), so the right side is at least \((\frac12-o(1))\sqrt p/(1-a)\), and the bound is vacuous at every scale below \(\sqrt p\). Both \(m_{<a}=0\) (all values at the weighted mean level, when that level is \(\ge a\)) and \(m_{<a}\asymp\sqrt p\) are compatible with any admissible scalar pair. So (a)–(c) neither prove nor refute (V).
- **The absolute-scale list.** The report lists \(V_{-\rho}\to0\), \(G_{-\rho}\le1+o(1)\) and \(\sup_{T_{-\rho}}g\to0\). It should also list the exact linear identities \(\sum_{x\in Q}f(x)\overline{\psi^j(x)}=n\nu_j\ge0\) (any law; R190 Lemma 1 proof, steps 1 and 5). In particular \(\sum_{T_\rho}f=-1-\sum_{T_{-\rho}}f\), which has modulus \(\le(\sqrt p+3)/2\).
  - These are absolute-scale statements on \(T_\rho\), but about \(f\), not \(g\).
  - With (NC2) they say: \(\nu\ge0\), and \(f\) is, up to \(\ell^2\)-small error, supported on \(T_\rho\cup\{1\}\).
  - That is the theta-type constraint itself, and no accepted statement turns it into level information.
- The report's own caveat ("a reading of the logical form of the accepted list, not a theorem about all possible arguments") is the right status. **ACCEPTED WITH CORRECTION.**

### 2.4 Proposition B and Corollary B (v4)

- **(i) Random flat law.**
  - Bernstein for \(\sum_{j\ne0}\xi_j\psi^j(x)\): mean \(-\pi\), variance \(\le m_0\), union bound over \(n\) points. This gives \(\sup_{x\ne1}g\le C\log p/m_0\).
  - Overlaps: the cycle edges of \(j\mapsto j-a\) split into \(\le3\) matchings of independent products, which gives \(\max_{a\ne0}|S\cap(S+a)|\le C\log p\).
  - Coset counts: Chernoff with mean \(\le1\).
  - \(\mathcal E(S)\le|S|^2(1+C\log p)\).
  - (A4): \(\sum_Bg\le|B|\sup g+1=O(\log p)\).
  - The quadratic form for \(G_\varepsilon\): diagonal \(|T_\varepsilon|/|S|=(\frac12+o(1))\sqrt p\). Off-diagonal: I re-derived the variance as linear part \(\le4\pi^3\sum_j|\text{row}_j|^2\) plus quadratic part \(\le2\pi^2\sum|c|^2\), with zero cross-covariance. Using \(\sum_{d}c(d)=0\) (since \(1\notin T_\varepsilon\)), this is \(O(p^2)\), i.e. \(O(1)\) after dividing by \(|S|^2\).
  - All **correct**. The wording "with probability \(1-o(1)\), for all large \(p\)" should read "for each large \(p\) with probability \(1-o(1)\)". Existence of one good \(S\) per prime is all that is used.
  - Audit Part B (\(p=160001,640009\)): \(\sup g=0.060,0.029\); \(G_\pm/\sqrt p\in[0.487,0.506]\); max overlap 5–6 and max coset count 3–5 against \(\log p\approx12\)–13.
- **(ii-1).**
  - Uniform approximation from R190:216.
  - \(g\ge a\) forces \(|D_{L'}|\ge\sqrt a/2\), hence \(|k|\le n/(L'\sqrt a)\). That is \(O(\sqrt p/\sqrt a)\) points, sharper than the report's \(O(\sqrt p/a)\); either suffices.
  - Parseval gives \(\sum|D_{L'}|^2=n/L'=(\theta+o(1))\sqrt p\).
  - **Correct.** The heavier-sign bound \(\frac12-\theta\) follows. (I also note \(m^Q_{<a}\ge(1-\theta-o(1))\sqrt p\), so the heavier sign has at least \(\frac{1-\theta}2\).)
- **(ii-2).**
  - Diagonal \(\theta(1-\theta)L'|T_\varepsilon|/m^2\to\frac{1-\theta}2\sqrt p\).
  - Off-diagonal: since \(|c(d)|\le(\sqrt p+1)/2\) and there are \(\le L'^2\) pairs, the variance is \(\le2\theta^2L'^2(p/4)/m^4\to2\). So the standard deviation is \(O(1)\); the report says \(O(1/\theta)\), which is also \(o(\sqrt p)\).
  - Cross term: variance \(O(\theta^2\sqrt p)\).
  - **Correct for the Bernoulli variant.** Its membership in \(\mathcal H\) "by the same proof" (McDiarmid replaced by Chernoff/Bernstein, \(|S|\) random with \(|S|/m\to1\)) is routine but was not re-derived; hence the correction in the summary.
  - Audit Part B: \(\theta=0.2,0.3\), both signs, above the bounds.
- **Corollary B.**
  - An argument that sees (NC) only through \(\mathcal H\) cannot define \(\rho\), so it must prove (V) for both signs or for an \(\mathcal H\)-definable sign such as the heavier one.
  - (i) defeats both cases. (ii) shows that adding \(\sum g^2\gg\sqrt p\) does not help.
  - **ACCEPTED.**
  - "Strengthens R190 Cor. 4.1(iii)" is loose: it is the analogous cap for a different target ((V) instead of \(T_0\) or \(X\)).

### 2.5 Proposition C and the uncertainty-principle heuristic (v5)

- **The bounds.** Item 1 is (A3) together with \((\mathrm V_{\rm rel})\) and \(\Lambda_a\subseteq T_\rho\). Item 2 is Cauchy–Schwarz with (A2) (lower bound) and Chebyshev (upper bound). Item 3 multiplies by \(|S|\sim n/\sqrt p\). Exact arithmetic in Part X. **Correct.**
- **The heuristic (AUD191 line 237)** said that vertex mass at levels \(\ge a\) on \(\asymp\sqrt p\) points, with \(\nu\) flat on \(\asymp n/\sqrt p\) points, suggests near-coset structure, which (A2)/(A6) exclude. The report handles it correctly in three steps:
  1. The literal mechanism, stability near equality in \(|S||\Lambda|\ge n\) (Donoho–Stark; equality only for cosets), cannot apply, because (A2) forces \(|S||\Lambda_a|\ge(2-o(1))n\). The models give 3.99.
  2. "(A2)/(A6) exclude" is true for single cosets (R184 Prop. 4(a) with (A2)). It is false for unions of cosets of different subgroups (Prop. D).
  3. The heuristic's *conclusion* ((V) fails) is recovered, conditionally on (SS\*), through (A4) instead of (A2)/(A6) (Theorem E).
- **What a constant-factor uncertainty bound does give.** \(|S||\Lambda_a|\le(1+o(1))n/a\) yields, through Cauchy–Schwarz, only \(\mathcal E(S)\ge(a-o(1))|S|^3\) (ASM C5). Inverse theorems such as Balog–Szemerédi–Gowers and Freiman then give structure on a positive *proportion* of \(S\), not on \((1-o(1))\) of the spectral mass. Theorem E's contradiction with (A4) needs the latter. That gap is exactly what (SS) asserts.
- The Donoho–Stark inequality and the equality case are quoted background, used in no proof. **ACCEPTED.**

### 2.6 Lemma J, Corollary J and Proposition D (v6, v7)

- **Lemma J.**
  - \(t\mapsto t^k\) is \(k\)-to-1 onto \(\Gamma\), so \(\sum_{y\in\Gamma}\chi(1-y)=\frac1k\sum_{\psi^k=1}J(\psi,\chi)\).
  - The trivial \(\psi\) gives \(-1\); \(\psi=\chi\) (when \(k\) is even) gives \(J(\chi,\chi)=-\chi(-1)=-1\); the others have modulus \(\sqrt p\).
  - For even \(k\) the bound is \((2+(k-2)\sqrt p)/k\le(1+(k-1)\sqrt p)/k\).
  - **Correct.** Audit Part J: the Jacobi identity with complex characters at \(p\le61\) for every \(k\), and the count bound for every subgroup of \(\mathbb F_p^\times\) (228 pairs, \(p\le241\), both signs; smallest ratio to the bound 1.065).
  - For \(\Gamma\le Q\) it coincides with Vinogradov (\(\sum_{x,x'\in\Gamma}\chi(x-x')=|\Gamma|\sum_y\chi(1-y)\), checked), i.e. the full-progression case of AUD191 (g4). **Not new.**
- **Corollary J** follows from (A3). It is also immediate from R190 Theorem 1(4), which puts every point with \(g\ge\tau\) in \(T_\rho\cup\{1\}\). **Correct.**
- **Proposition D.**
  - The two cosets are disjoint, since \(-1\notin H_1+H_2\) when \(\operatorname{lcm}<n\).
  - \(0\notin S\).
  - The transform of \(\mathbf 1_{x+H}\) is \(|H|\psi^x\mathbf 1_{H^\perp}\).
  - Overlaps: \(r_S=\beta_i\) on \(H_i\setminus H_j\); \(r_S\le2d/(h_1+h_2)\) off \(H_1\cup H_2\); \(r_S=1\) on \(H_*=H_1\cap H_2\).
  - \(\Gamma_*=(H_1\cap H_2)^\perp\supseteq\Gamma_1\cup\Gamma_2\), so R184 Theorem 2.3 is satisfied.
  - \(\sum g^2/G\to\beta_1^3+\beta_2^3\); \(m_{<a}\le|\Gamma'|=n/\operatorname{lcm}\to8d\).
  - All **correct.**
- **The (A6) correction.**
  - The report bounds a coset's share by \(\beta_i+\beta_j/2\to\frac34\), enough only for \(\delta<350/256\).
  - For \(\delta\in[350/256,2)\) (orders \(\le(2-\delta)m_0<0.64m_0<2h_i\)), use a sharper count. A subgroup \(K\supseteq H_i\) has \(|K|=th_i\) with \(t\le2(2-\delta)\), and \(|K\cap H_j|=\gcd(|K|,h_j)\le td\). If \(K\) contains neither \(H_i\), then \(|K\cap H_i|\le h_i/2\) for both \(i\). So the share is \(\le\frac12+o(1)\) for bounded \(d\), enough for \(\delta\le15/8\).
  - For \(\delta>15/8\), the share is \(\le2(2-\delta)\le((2-\delta)/2)^{1/4}\) (Part X, exact).
  - Numerically, over every subgroup of order \(\le2m_0\), the maximal share is 0.513, 0.501 and 0.508 at the three tabulated primes, and the inequality holds on a grid of 199 values of \(\delta\) (Part D).
- **Existence.**
  - \(\mathcal P\) needs primes \(p\equiv1\pmod{2\operatorname{lcm}(h_1,h_2)}\) with \(h_1,h_2\) close to \(\sqrt p/4\) and to each other.
  - With \(h_2=h_1+1\) this is a quadratic-polynomial prime problem. With a box of pairs it is a bilinear problem at moduli just beyond the Bombieri–Vinogradov range.
  - So the report is right to keep the asymptotic cap conditional ((b2)).

### 2.7 Proposition F (v8)

Built independently in \(\mathbb F_r[i]\) (\(r\equiv3\bmod4\), \(r\le43\); audit Part F):
- levels \(g=1\) on \(\mathbb F_r^\times\) and \(\beta=4/(r-1)^2\) elsewhere;
- \(\mathbb F_r^\times\setminus\{1\}\subseteq T_+\) (so \(\rho=+1\));
- \(V_-=0\), \(G_-=(r+1)/(r-1)\to1\), \(G=r+1\);
- the Lemma 0 identity;
- \(m^Q_{<a}=2\) exactly, and \(m_{<a}(T_+)=(r-3)/(r-1)\to1\);
- the energy ratio of \(S=I\setminus\{0\}\) tends to 1 (subgroup minus a point);
- \(t_B=2/(r+1)\to0\) for \(B=\mathbb F_r^\times\).

So the control is on the (NC) branch in \(\mathbb F_{r^2}\) (R190:123), satisfies (V) robustly, and violates exactly (A2), (A4), (A5) item 2 and (A6)(a). The cap ("a refutation of (V) cannot be field-general") is **correct**. The combined cap with Prop. D inherits (b2).

### 2.8 Exponents (v11)

Recomputed in Fractions (Part X):
- R160 price \(p\cdot m_{<a}=p^{3/2}\) against \(O(p)\): loss \(\frac12\); against \(o(pD)\) with \(D\le p^{1/4}/\log\): at least \(\frac14\). This agrees with AUD191 (a9).
- Scale gap between \(\frac14\) and \(\frac12\).
- \(\Delta=o(p^{1/2})\).
- Prop. C constants, Prop. D thresholds (\(350/256\), refined \(15/8\)), \(n/\operatorname{lcm}\to8d\), \(\beta_1^3+\beta_2^3=\frac14\), Prop. F exact values.

All correct.

### 2.9 (SS), (SS\*) and Theorem E (v9, v13)

- **Theorem E, step by step.**
  1. \(m_{<a}=o(\sqrt p)\) on a subsequence.
  2. Prop. A(3) gives \(m^Q_{<a}(g)=o(\sqrt p)\).
  3. Prop. A(2) with \((g_S,g)\) at levels \((a/2,a)\) gives \(m^Q_{<a/2}(g_S)\le m^Q_{<a}(g)+2\Delta=o(\sqrt p)\).
  4. (SS\*) gives \(\le L\) subgroups \(\Gamma_i\le Q\) of orders in \([c\sqrt p,\sqrt p/c]\) (since \(N/|S|=n/|S|\sim\sqrt p\)) carrying all but \(o(\sqrt p)\) of \(g_S\).
  5. Prop. A(1) transfers this to \(g\), so \(t_B\to0\).
  6. That contradicts R151:47, which holds uniformly for every fixed number of cosets and fixed \(c_1<c_2\) (the anchor deficit \(d_a\to0\) does not depend on \(B\)).
  - The sizes are right: \(|S|\sim m_0=n/\sqrt p\sim\sqrt{n/2}\).
  - Audit Part A checks the inequality chain of step 3 numerically.
  - **The implication is correct.**
- **Formulation of (SS\*).** As written ("spectral mass \(\ge c_0\) outside every union of \(\le L\) subgroups of order \(\asymp N_k/|S_k|\)"), the quantifiers are loose. The form Theorem E needs is:
  - For every \(a\in(0,\frac12]\) there are \(L\in\mathbb N\) and \(c\in(0,1]\) such that no sequence \(S_k\subseteq\mathbb Z/N_k\) with \(|S_k|\sim\sqrt{N_k/2}\) and \(\sum_{\xi\ne0,\,g_k<a}g_k=o(M_k)\) has
    \[\liminf_k\ \min_B\ \sum_{\xi\notin B}g_k/M_k>0,\]
    the minimum taken over unions \(B\) of at most \(L\) subgroups of the dual of orders in \([cN_k/|S_k|,\,N_k/(c|S_k|)]\).
  - Because (A4) holds for every fixed \((k,c_1,c_2)\), one pair \((L,c)\) per level suffices.
- **Is it field-free?** Yes. It mentions only cyclic groups, indicator functions and their Fourier transforms. Its use needs \(N=(p-1)/2\) only; no character of \(\mathbb F_p\) and no Paley input enters. Two remarks:
  - For prime \(N\) it predicts that no set of size \(\sim\sqrt{N/2}\) has a sharp spectrum at all, since there are no subgroups of the right order.
  - It is *not* the weakest decisive statement. One may add as hypotheses every field-free property the near-critical \(S\) is known to have:
    - flatness;
    - \(\mathcal E(S)\le(\frac12+o(1))|S|^3\) (and, from sharpness, \(\ge(a-o(1))|S|^3\));
    - the overlap dichotomy of (A5) with \(|H_*|=o(m_0)\);
    - (A6).
  - Call that (SS\(^{**}\)). It is weaker than (SS\*) and still suffices. The exact (NC) statement that decides \((\mathrm V_{\rm rel})\) is simply "the near-critical \(S\) has no sharp spectrum" (Prop. A(4)).
- **Status of "probable no".**
  - No source for (SS) or (SS\*) is given. The exact case \(g_S\in\{0\}\cup[a,1]\) reduces to the Green–Sanders idempotent theorem through \(\|\mathbf 1_S\|_A\le1/a\) (the arithmetic is checked here; the theorem is quoted from memory by the report and not read at source by me). The robust sparse case (relative \(L^2\) error \(o(1)\) at density \(N^{-1/2}\)) is not covered by it.
  - The finite evidence is weak, as the report says: the annealer does not even find the coset optimum in the composite controls. Heuristic attempts at counterexamples (reasoning only, not computed) all reduce to coset unions or have Fejér-type tails: Gauss periods of a multiplicative subgroup (spectrum flat at level \(\approx1/|S|\)), Singer-type difference sets (flat), random dense subsets of cosets (half the mass at level \(O(1/|S|)\)), and products of sharp sets (coset unions).
  - So (SS\*) is plausible, and "expected" is the right word. "Very unlikely" (§8) and "counterexample to a robust idempotent theorem" overstate it.
- **The interpretation that matters for the plan.** (NC) is the hypothetical critical-size branch the programme tries to show is empty. Theorem E says: given (SS\*), every (NC) sequence has \(m_{<a}\asymp\sqrt p\). Equivalently, \((\mathrm V_{\rm rel})\) on (NC), *by itself*, contradicts (A4). So a proof of \((\mathrm V_{\rm rel})\) from (NC) would already close the critical branch, without (A-slope) and without the R157/R160 assembly. Under (SS\*), then:
  - (V) is not "false for the actual law" (there may be no such law);
  - (V) is a target-depth statement on the critical branch, and cannot serve as an intermediate lever.
  - The mission's "refuted" branch, "(A-vertex) needs a signed estimate", is the correct consequence for the ASM assembly.

### 2.10 §4 and §0 item 6 (v10)

- "(V) and high energy are independent in both directions" is **false** as written. On any law with \(G_\rho\asymp\sqrt p\), (V) gives \(\sum g^2\ge\sum_{\Lambda_a}g^2\ge a(G_\rho-m_{<a})\), i.e. high energy. This is ASM C5, accepted in Round 191 (a8), and Prop. C uses it.
- Only the other direction fails: \(D_\theta\) has high energy without (V).
- Prop. D does not show "(V) without high energy". It has energy \(\frac14\) with (V) only for \(a<\frac14\), consistent with the implication.
- The remaining statements of §4 are correct:
  - \(\sum g^2\gg\sqrt p\) is unchanged and open (R183 acc:270);
  - it is not implied by \(\mathcal H\) (random flat law);
  - (SS) says nothing about energy beyond \(\ge a\) under sharpness.

## 3. Replay log

Run from the repository root on 2026-11-21 with `.venv/bin/python -B`. Outputs went to the session scratchpad. "Matches" means every quoted output line or table row appears in the run, timing text excepted.

| Script | Command | rc | Time | Result |
|---|---|---|---|---|
| exponents | `research/paley-192-vertex-exponents.py` | 0 | 1 s | `48 checks, 0 failures`, `ALL OK` |
| models | `… check` | 0 | <1 s | `SELF-CHECK OK` |
| models | `… A 10009 40009 160001 640009` | 0 | <1 s | matches every §5.1 row (flat 160001 and 640009, \(D_{0.25}\) and \(D_{0.10}\) at 640009) |
| models | `… B 20000 4000000` | 0 | 6 s | 2494 primes; matches every §5.2 number and the three-row sector table; \(m_{<a}\le0.636\) for \(a\le0.2\) |
| sharp search | `… E` | 0 | 4 s | matches §5.3 Part E (\(\min L_{0.2}\in[0.110,0.146]\); \(L_{0.05}=0\) at \(N=31,41,61\); controls 0) |
| sharp search | `… S 20000` | 0 | 142 s | matches §5.3 Part S (interval 0.114; rank-2 Bohr 0.22–0.26; half-interval 0.51–0.57; random 0.55→0.98; composite random seeds 0.62–0.94, controls 0) |
| audit | `research/paley-192-audit-check.py` | 0 | 3 s | `52 checks, 0 failures`, `ALL AUDIT CHECKS OK` (Parts X, J, T, A, D, F, B) |

SHA-256 (as audited):
- report `research/native-claude-ordinary-nc-vertex-tightness-192.md`: `509e0d4021ade6200dff650293f2487be6311b0d80f1ca9b88d3f32905b5d98b`;
- scripts (match the report's table): `paley-192-vertex-exponents.py` `ce622626…932c0a`, `paley-192-vertex-models.py` `69560155…84ef`, `paley-192-vertex-sharp-search.py` `72389a98…c01c6`;
- mission `1f1d3c4d…54967` (matches the inflight manifest); coordinator record `coordination/round-191.json` `5af57ceb…7296ad`.

**Not checked:**
- the Green–Sanders theorem and the Donoho–Stark inequality (quoted background, used in no proof);
- whether \(\mathcal P\) is infinite with tolerances \(\to0\);
- membership of the Bernoulli \(D_\theta\) variant in \(\mathcal H\), item by item;
- R151's proof of (A4) beyond its statement at line 47, and R20's proofs beyond lines 66–76 (all accepted earlier);
- any literature search for (SS) (none was run by me).

## 4. Ranked closeout

### 4.1 What Round 192 changes for (A-vertex) and (V)

Ranked by effect on the plan:

1. **(V) is reformulated and, conditionally, shown to be of target depth.** \((\mathrm V_{\rm rel})\) is exactly a sharp-spectrum property of the flat near-critical support \(S\) (Prop. A). Given the field-free (SS\*) (open), \((\mathrm V_{\rm rel})\) contradicts (A4) by itself on (NC) (Theorem E). So:
   - on any (NC) sequence, \(m_{<a}\asymp\sqrt p\) for every fixed \(a\);
   - a proof of (V) from (NC) would already empty the critical branch.

   Effect: **reformulated** + **new_obstruction** (conditional on (SS\*)) to "(V) as a lever".
2. **Method caps, unconditional.**
   - \(\mathcal H\) (every sector-free accepted (NC) consequence) implies neither (V) nor \(\sum g^2\gg\sqrt p\), on both signs (Prop. B(i), proved).
   - \(\mathcal H\) plus high energy does not imply (V) (\(D_\theta\)).
   - No field-general argument refutes (V) (Prop. F).

   Effect: **new_obstruction** (method cap).
3. **The Round 191 heuristic is settled.** Its mechanism (uncertainty-principle stability) cannot apply (Prop. C). Its exclusion claim is wrong for (A2)/(A6) and right for (A4) and (NC2) (Prop. D, Lemma J). Its conclusion is recovered conditionally (Theorem E). Effect: **evidence_only / reformulated** (bookkeeping).
4. **Unchanged:**
   - \(\sum g^2\gg\sqrt p\) (the Round 20 low-energy question, R183 acc:270);
   - (A-slope) and both geometric-progression walls;
   - the losses of every accepted device on the low layers (\(\ge p^{1/2}\) against \(O(p)\), \(\ge p^{1/4}\) against \(o(pD)\));
   - the target.

### 4.2 The final ordinary obligation map (after Round 192, as audited)

On the hypothetical critical branch (R157:3, R160:3, (NC) = (NC1) + \(V_{-\rho}\to0\)), the contradiction follows from (S\(_a\)) and (A\(_V\)) for one fixed \(a\in(0,\frac12]\) (ASM Prop. 1, accepted).

1. **(A-slope)** = (S\(_a\)): \(\sum_{t\ne1}|f(t)|P^\natural_t(\ge a)=O(p)\).
   - Sufficient: \(X=O(p)\) or \(\mathcal M_{\sqrt g}=O(p)\), logarithm-free.
   - Current: \(p^{4/3+o(1)}\). Floor on (NC): \(X\ge(2-o(1))p\).
   - Sector-free arguments need `cand:gp-shifted-energy` (sharp form \(E^\times(I-1)=O(|I|^2)\); known \(|I|^{32/13}\)). Sector arguments need `cand:gp-sector-constancy` (open for \(c\le1/\sqrt2\)). **Unchanged.**
2. **(A-vertex)** = (A\(_V\)), a signed estimate on the layers \(C^2/p<|F|^2<a\), all slopes, both signs.
   - Its only accepted sufficient form, (V) \(m_{<a}=o(D)\), is now:
     - (a) unreachable from \(\mathcal H\) (proved);
     - (b) equivalent at relative scale to "the near-critical \(S\) has a sharp spectrum";
     - (c) given (SS\*), incompatible with (A4) on (NC), so that proving it would itself close the branch.
   - In practice, (A-vertex) requires a **genuinely signed estimate** on layers that carry \(\asymp\sqrt p\) of vertex mass, where every accepted device loses \(\ge p^{1/2}\) (against \(O(p)\)) or \(\ge p^{1/4}\) (against \(o(pD)\)). No accepted tool addresses it.
3. **\(\sum g^2\gg\sqrt p\)**: open, unchanged. It is necessary for (V) and not sufficient.
4. **External problems the map rests on:** `cand:gp-shifted-energy` (sharp form) and `cand:gp-sector-constancy` (Paley-clique type), plus the target itself (Randomstrasse101 Conjecture 26 / OP-00041).
5. **Status determiner, not an obligation:** (SS\*) (or the weaker (SS\(^{**}\)) of §2.9). It decides (V) negatively if true and opens no route if false; a failure would only make the near-critical support a counterexample candidate.
6. **Off the critical path (unchanged):** one-match 43/24 (+ zero match), \(\mathcal D\), J split, \(\mathcal M_w\) as a target, the uncertainty-principle reading of (V).

### 4.3 Internal or external?

- **(A-vertex):** record as an **internal open problem of target depth**. It is the theta-type oscillation problem restricted to the low vertex layers. No literature source states it, and none is expected to: it is specific to the R152–R166 reduction. Per the mission's branches, the record should say "refuted conditionally on (SS\*); unconditionally inconclusive".
- **(SS\*):** record as an **internal open problem**, field-free (additive combinatorics in \(\mathbb Z/N\)), "recognised in kind": a sparse robust form of the idempotent theorem, whose exact form (Green–Sanders) is classical. It is not a recognised external problem as stated, because no source states it.
  - A `cand:` ID (`cand:sharp-spectrum-structure`) is not required under AGENTS.md while no call needs it. With every line on hold, I recommend recording (SS\*) in the acceptance record's open-bounds list with its precise quantifiers (§2.9), and creating the ID only if a future call is proposed.
- **External (unchanged):** `cand:gp-shifted-energy`, `cand:gp-sector-constancy`, the target.

### 4.4 Recommendation

**Hold.** Round 192 met the mission's inconclusive branch exactly. The decisive statement is recorded: "the near-critical \(S\) has no sharp spectrum", sufficient field-free form (SS\*). Every remaining ordinary obligation is now:
- behind an external geometric-progression problem ((A-slope)); or
- a signed low-layer estimate of target depth ((A-vertex)), whose only accepted sufficient form (V) is unreachable from the sector-free consequences, and, given (SS\*), equivalent to closing the branch outright.

No internal call has a remaining lever.

**At most one call, not recommended now:** a literature check, at source, for a robust or approximate idempotent theorem in the sparse regime, i.e. (SS\*) or (SS\(^{**}\)) as quantified in §2.9.
- If found, Theorem E becomes unconditional and the record changes from "inconclusive" to "(V) refuted on (NC)".
- The decision after it is hold in every case. So it changes the record's wording, not the plan. Run it only if the coordinator wants the (V) entry closed.

**Do not run:** further (NC)-to-(V) desk checks; model searches for sharp sets (the annealing evidence is uninformative); a proof attempt of (SS\*) inside this project (it would be a standalone additive-combinatorics problem with no effect on the target).

**Bookkeeping for the coordinator:**
- Carry the corrections (v2), (v3), (v4), (v7), (v10) and (v13) into the acceptance wording.
- In particular, drop "independent in both directions" and "very unlikely".
- Keep Prop. D's cap conditional ((b2)).
- State that Lemma J is a known special case of AUD191 (g4).

## 5. Status of this audit

This is an agent audit, not human acceptance or certification.

**What I checked:**
- every proved or bookkeeping claim of the report, line by line against the accepted sources listed in §2;
- independent code for Lemma J (all subgroups, Jacobi identity, Vinogradov comparison), the Prop. A transfer chain, the Prop. D family (including (A6) for every \(\delta\)), the \(\mathbb F_{r^2}\) control in \(\mathbb F_r[i]\), and the Prop. B families;
- exact Fraction arithmetic for every constant and exponent;
- full replays of the report's three scripts.

**What I did not check:** listed under "Not checked" in §3.

**Files:** only this file and `research/paley-192-audit-check.py` were written. Nothing was committed. Replay outputs went to the session scratchpad.

Final SHA-256 of the audit script: `paley-192-audit-check.py` `7f5b5a935e549e513f89a2ad5e600ff5b324365416228de422dead0ccffa193d`.
