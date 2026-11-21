# Independent audit of Round 191 (session/r191-audit)

- **Auditor:** Claude subagent started by the Round 191 coordinator (session/r191-audit). This is an agent audit, not human acceptance and not a mathematical certification. The auditor wrote none of the three reports and is not the coordinator.
- **Status of this file:** written incrementally. The "Blind overlap review" section below was saved before any file under `coordination/shared-obligations/`, `coordination/drafts/` or any `coordination/round-*-inflight.json` was opened.
- **Read before the blind review:** `AGENTS.md`, `docs/WORKFLOW.md`, `docs/ROUND_REVIEW.md`, `coordination/checkpoints/round-190.md`, `research/native-claude-audit-190.md`, the three missions in `coordination/missions/round-191/`, and the three reports.

Verdict key (per claim the report labels as proved, or as bookkeeping that the coordinator may carry forward):
- **ACCEPTED:** correct as written, for the stated hypotheses.
- **ACCEPTED WITH CORRECTION:** true after the stated correction, which does not change the report's main conclusion.
- **CONDITIONAL:** correct given a named input that is not proved or not checked.
- **REJECTED:** false as written, or not supported.

Reports, abbreviated:
- **ASM** = `native-claude-ordinary-fixed-block-assembly-191.md` (Propositions 1–2, the \(\mathcal M_w\) loss table, (A\(_V\)), (V), (A\(_{\rm unif}\)), bookkeeping C1–C6), with `paley-191-assembly-exponents.py` and `paley-191-assembly-models.py`. Report verdict: no.
- **MWS** = `native-claude-ordinary-first-mass-sector-obstruction-191.md` (Lemma 1, Proposition 2, Lemma 3, Theorems 3–4, Corollaries 3.1/4.1, Proposition 5), with `paley-191-mwsector-*.py`. Report verdict: yes (supported, method-cap sense).
- **GPSUB** = `native-claude-ordinary-gp-sector-constancy-literature-191.md` (literature table, §3.1 Vinogradov consequence, §3.2 \(\mathbb F_{r^2}\) example), with `paley-191-gpsub-checks.py`. Report verdict: refuted ((GP-Sub) open).

## 1. Blind overlap review

Written after reading the three reports and their missions. No shared-obligation, draft or inflight file had been opened.

| Pair | Classification | Reason |
|---|---|---|
| ASM – MWS | **touch in use on the same object (\(\mathcal M_w\) as the fixed-block target); complementary, not duplicated** | ASM asks whether \(\mathcal M_w=O(p)\) is *sufficient* (it is not: it fails the slope part of (A); \(X\) or \(\mathcal M_{\sqrt g}\) is needed), and proposes retargeting to \(X\)/\(\mathcal M_{\sqrt g}\). MWS asks whether \(\mathcal M_w\) is *obstructed* (it is, for admissible-only and \(\mathcal H\)-only arguments). ASM §4 "Remark on the weight \(w\)" anticipates MWS: pieces that \(w\) removes near unit slopes reappear in (A-slope), where only unweighted masses pay them. MWS's answer (the \(\eta\)-mixtures defeat \(w\) for every hypothesis class in use) makes ASM's remark moot for classes but not for individual laws. **Interaction the reports do not state:** since \(\sqrt g\ge g(1-g)\) pointwise, any lower bound for \(\mathcal M_w\) on a family is also a lower bound for \(\mathcal M_{\sqrt g}\) and \(X_c-\mathrm{diag}\); so ASM's recommended retarget (\(X\) or \(\mathcal M_{\sqrt g}\)) meets the same wall, and even the *pure* subgroup law (for which \(\mathcal M_w=0\)) obstructs \(\mathcal M_{\sqrt g}\) directly. No common estimate proved twice. |
| ASM – GPSUB | **independent in substance** | ASM uses no character-sum or clique input; GPSUB uses no part of the R152–R166 reduction. ASM's proposed next question ("does (NC2) force (V)?", the Round 20 low-energy question) is a sector-condition question; GPSUB's outcome ("retire the (NC) sector lever below 45/26") is about the sector lever *for excluding GP-type laws*, not about vertex tightness, so it does not decide ASM's question. Contextual touch only: GPSUB's remark that Randomstrasse101 Conjecture 26 is the project's own target (to be checked, §4). |
| MWS – GPSUB | **touch in use on `cand:gp-sector-constancy`; consistent** | MWS Proposition 5 transfers Round 190 Criteria 5.1–5.2 to \(\mathcal M_w\), with a clique of length \(4K'+1\) (twice as long as for \(T_0\)). GPSUB shows (GP-Sub\(_c\)) known only for \(c>1/\sqrt2\) and (GP-Sub\(_\kappa\)) only for \(c_0>1\) (Vinogradov), so MWS (b2) stays conditional on an open external input. GPSUB's wording correction ("for every \(c_0>0\)") applies equally to MWS (b2). MWS's observation that HP excludes \(4K'+1>(\sqrt{2p-1}+1)/2\) concerns progressions of length \(>\sqrt{p/2}/2\) in \(K'\); together with GPSUB this means \(\mathcal M_w\)-relevant cliques with \(K'\gtrsim0.18\sqrt p\) are already excluded unconditionally, which removes some (not all) of MWS's mixtures on (NC) — to be checked in §3. |

- **No shared estimate is proved twice.** The three calls answered three different questions (sufficiency, obstruction, an external status).
- **Would an overlap review have changed dispatch?** Probably not. ASM and MWS are complementary halves of "is \(\mathcal M_w\) the right target" (sufficient? obstructed?). A coordinator could have asked MWS to state its result for \(X\) and \(\mathcal M_{\sqrt g}\) as well, anticipating ASM's retarget; that is a scope extension, settled by a one-line monotonicity in this audit.
- **Candidate touches.**
  - `cand:gp-shifted-energy`: touched in use by MWS (Corollaries 3.1/4.1: now binds \(\mathcal M_w\) below \(p^{16/13}\); sharp form \(O(|I'|^2)\) for the target); value unchanged. ASM: not in value; only indirectly through its §4 remark. GPSUB: listed as an alternative only.
  - `cand:gp-sector-constancy`: value/status set by GPSUB (open for \(c\le1/\sqrt2\); quantitative form only for \(c_0>1\); false in \(\mathbb F_{r^2}\) for \(c<1\); wording correction); touched in use by MWS (Proposition 5). ASM: no.
  - `cand:slope-row-mass-x`: touched in use, strongly, by ASM (Proposition 2: \(\sum_{t\ne1}P_t=X_c-\mathrm{diag}\); \(X\) pays the slope part of (A); retarget from \(\mathcal M_w\) to \(X\)/\(\mathcal M_{\sqrt g}\)); touched in use by MWS (lower bounds for \(\mathcal M_w\) on families, which transfer to \(X\)); value unchanged by all three.
  - New objects proposed: ASM names (A-slope), (A-vertex)=(A\(_V\)), (V) and (A\(_{\rm unif}\)); none proposes a new `cand:` ID. Whether (V) should be recorded is assessed in §6.

### After unblinding

Opened afterwards: `coordination/round-191-inflight.json`, `coordination/shared-obligations/round-191-before.json` (SHA-256 `060ea6ce…4a00`, matches the inflight binding) and `coordination/drafts/round-191-dependency-assessment.json`. No `round-191-after.json` exists yet. Also checked: `coordination/round-190.json` (`b8f6e40f…05cc`) has `shared_candidates: []`; `cand:gp-sector-constancy` and `cand:gp-shifted-energy` occur only in prose there and in the Round 190 acceptance.

- The coordinator's pre-dispatch comparison (`comparison_status: assessed`, `known_shared: []`, empty `candidate_ids_by_call`) dispatched the three calls as independent: assembly "shares no estimate with either"; first-mass (energies, `cand:gp-shifted-energy`) and literature (character-sum constancy, `cand:gp-sector-constancy`) "touch the same configuration through different statements".
- **Agreement and difference.** My blind review agrees that no estimate is shared and that MWS–GPSUB is a touch through different statements. It differs on **ASM–MWS**: the comparison said the assembly call "shares no estimate with either"; in fact ASM and MWS both assess \(\mathcal M_w\) as the fixed-block target (`cand:slope-row-mass-x` in use), from opposite sides, and ASM's retarget to \(X\)/\(\mathcal M_{\sqrt g}\) is caught by MWS's lower bounds by monotonicity (§3.6). This is a touch, not a duplicate, and would not have changed dispatch; it changes how the two results must be combined at closeout (§6).
- **Candidate bookkeeping.** `candidate_ids_by_call` is empty although the literature mission's own question names `cand:gp-sector-constancy` and the first-mass mission's obligation text names `cand:gp-shifted-energy`. Under AGENTS.md a `shared_candidates` entry is needed only when two proposed calls need the same estimate; in Round 191 each ID was named by one call, so the empty list is consistent with the rule, but the IDs are carried only in prose. Recording both IDs (and `cand:slope-row-mass-x`) under `shared_candidates` in the Round 191 coordinator record would make the closeout hook able to see them. Flagged for the coordinator; not a defect in any report.
- **Dispatch effect:** none for the three calls as run. Lane labels `session/r191-assembly`, `session/r191-mw-sector`, `session/r191-gpsub-literature` match the report headers; mission-file hashes in the manifest match the files on disk (`12cbc167…`, `6f98e26f…`, `59a63f9b…`); all three share one `started_utc_epoch`, recorded once before the launches as the manifest says.

## Summary of verdicts

| Report | Main verdict | Corrections / conditions |
|---|---|---|
| ASM. Fixed-block assembly | (a1) **"No": fixed blocks + paid cuts do not give the target ACCEPTED**; (a2) **R160:27 excludes slope cuts ACCEPTED** (verbatim); (a3) **the C²/p correction ACCEPTED** (it corrects the Round 190 audit and the mission); (a4) **Proposition 1 ACCEPTED** (re-derived; conditional, like the whole reduction, on the critical-branch hypotheses R157:3/R160:3); (a5) **Proposition 2 ACCEPTED** (exact, independent code); (a6) **\(\mathcal M_{\sqrt g}\) as the weakest slope-complete first mass ACCEPTED WITH CORRECTION**; (a7) **loss exponents 441/890, 441/1780, 209/422, 209/844, 13/27, 13/54, 3/7, 627/1477, 26/63 ACCEPTED**; (a8) **(A\(_V\)), (V), (V)⇒\(\sum g^2\ge(a-o(1))\sqrt p\), \(a\le\frac12+o(1)\) ACCEPTED** (bookkeeping; the vertex sector is \(T_\rho\), checked); (a9) losses of the accepted devices on the low layers **ACCEPTED**, the \(p^{3/4}\) "floor for absolute pricing" **ACCEPTED WITH CORRECTION** (evidence, not a proved method cap); (a10) (A\(_{\rm unif}\)) and the three-masses table **ACCEPTED WITH CORRECTION** (labelling of \(X\) in §0 item 6); (a11) \(D_\theta\)/model evidence **labelled as evidence: ACCEPTED**; C4, C6 **ACCEPTED**. Verdict **no ACCEPTED**. | (i) §0 item 6 and §6 say "\(X\approx1.4p\)" in the models; the 1.1–1.5 values are \((X_c-\mathrm{diag})/p\) at \(p\le3209\); Part A gives \(X/p\approx0.48\)–\(0.72\). (ii) "Weakest slope-complete first mass" holds within first masses \(\sum_t\varphi(t)P_t\) with the R166 vertex weights; by \(w\le\sqrt g\) it **inherits every lower-bound obstruction proved for \(\mathcal M_w\)** (MWS), and on pure subgroup laws \(\mathcal M_{\sqrt g}(\mathbf 1_H)\ge E_{\rm off}(H)\) exactly (audit Part B), so the recommended retarget to \(X\)/\(\mathcal M_{\sqrt g}\) does not escape the geometric-progression wall. (iii) §5.2's "at least \(p^{3/4}\) for admissible absolute pricing" is a model observation (\(\mathfrak M^\natural/p^{7/4}\approx0.02\) at \(p\le3209\)); no admissible family with \(\mathfrak M^\natural\gg p^{7/4}\) is proved. (iv) Proposition 1 and (A\(_V\)) given \(X=O(p)\) are equivalent to the contradiction (as the report says, "tautological"); the content is the split into (A-slope) and (A-vertex), not a new estimate. |
| MWS. \(\mathcal M_w\) and the sector obstruction | (m1) **Lemma 1 ACCEPTED** (sharp on \(g_H\)); (m2) **Proposition 2(a)–(c) and Lemma 3 ACCEPTED**; (m3) **Theorem 3 ACCEPTED** (admissible); (m4) **Theorem 4 ACCEPTED** (each \(\mathcal H\) item re-derived); (m5) **Corollaries 3.1, 4.1 ACCEPTED** as implications; (m6) **Proposition 5 ACCEPTED**, (b2) **CONDITIONAL** on (GP-Sub), with GPSUB's re-quantification; (m7) model and \(j\)-profile evidence **reproduced**; (m8) **\(M_w(\mathbf 1_H)=0\) ACCEPTED**; (m9) "4/39 of the remaining 1/3" **ACCEPTED**. Verdict **yes (method-cap sense) ACCEPTED**. | (i) Reconciliation with ASM (§3.6): \(w\) does remove sector pieces for individual plateau-at-1 laws (subgroups completely), and those pieces sit exactly on near-unit/unit slopes, where (A-slope) must pay them with \(\mathcal M_{\sqrt g}\) or \(X\); there they are not removed (\(\mathcal M_{\sqrt g}(\mathbf 1_H)\ge E_{\rm off}(H)\)). So keeping \(w\) gains nothing for the target: either the mixtures obstruct \(\mathcal M_w\), or the removed pieces obstruct (A-slope). (ii) Proposition 5 addendum: on (NC), Hanson–Petridis already excludes the restriction hypothesis once \(4K'+1>(\sqrt{2p-1}+1)/2\), i.e. \(|I'|\gtrsim0.354\sqrt p\); this does not touch the \(\mathcal H\)-only cap (Corollary 4.1), which uses all lengths. (iii) "(GP-Sub\(_\kappa\)) with \(K'\ge c_0\sqrt p\)" must be read "for the relevant small \(c_0\)" (GPSUB §5). |
| GPSUB. (GP-Sub) literature | (g1) **HP Corollary 1.5 ACCEPTED** (read at source by this audit); (g2) **CYY Corollary 4.6 ACCEPTED** (at source); (g3) **Shparlinski Problem 1 and Chang–Shparlinski "resisting all attempts" ACCEPTED** (at source); (g4) **Vinogradov consequence \(E_\rho\ge(M-\sqrt p)/2\) ACCEPTED** (re-derived; independent check); (g5) **\(\mathbb F_{r^2}\) runs ACCEPTED** (re-derived; independent field arithmetic); (g6) **Randomstrasse101 Conjecture 26 = the project's target: TRUE, context only**; (g7) **re-quantification of (GP-Sub\(_\kappa\)) ACCEPTED**; (g8) non-transfer remarks (Kerr, additive structure, Yip, KYY) **ACCEPTED as agent remarks**; other quoted rows **not re-read**. Verdict **refuted, i.e. (GP-Sub) open in the needed range, ACCEPTED** (as a literature finding, not a proof of openness). | (i) §0 item 8 and §5 say Randomstrasse101 states HP "is the best bound"; the post says "Recently, Hanson and Petridis … showed" the bound. The CYY 2026 sentence quoted at source is the stronger corroboration. (ii) The reduction "(GP-Sub) is a special case of Chang's Problem 3 weakened to non-constancy" is correct but is an agent observation; no source states (GP-Sub) separately. |

## 2. Report ASM: `native-claude-ordinary-fixed-block-assembly-191.md`

**Sources checked.** The full report and mission; both scripts (read; replayed). Re-read at source: R152 `ordinary-affine-correlations-152.md` lines 29, 43–70; R153 `ordinary-affine-jacobi-factorization-153.md` line 15; R154 `ordinary-lift-and-gauss-kernel-154.md` line 3; R157 `ordinary-marked-frequency-localization-157.md` lines 1–54; R160 `ordinary-matched-physical-truncation-160.md` lines 1–38; R160 `ordinary-rank-two-slope-orthogonality-160.md` lines 55–62; R162 `ordinary-physical-slope-fiber-count-162.md` lines 1–30; R163 `ordinary-shifted-layer-energy-saving-163.md` lines 45–82; R164 `ordinary-physical-pair-slope-pinning-164.md` lines 18–56; R166 `ordinary-regular-character-collisions-166.md` lines 1–15; R183 `native-claude-ordinary-prime-first-mass-fibre-dilation-183.md` lines 36–56; `research/round-183-acceptance.json` lines 264, 270. Not re-read: R155, R156, R158, R159 (beyond what the Round 190 audit checked), R165, R172, R180; R154:77–93 taken as cited (\(f(1)=1\); \(t=1\iff x=y\)).

### 2.1 The lower bound and the device (R157:39–41, R160:13–27)

- **R157** (lines 33–43): on a subset of \(I_{\rm arc}\) of \(\nu\)-mass bounded below, \(D_{g_a}\gg E^{-1/2}/\log(2/E)=D\), and \(M_a\ge pD_{g_a}\); hence \(\sum_{I_{\rm arc}}\nu_aM_a\gg pD\). With \(M_a\ge0\), \(\mathcal M_\nu(F)=\sum_a\nu_aM_a\ge c_1pD\). **Correct.**
- **R160** (lines 3–27): \(\|C_{G,H}\|_{\ell^2(\mu,u)}\le\sqrt{n\max\nu}\,\|G\|\|H\|\) for \(\mu\le\nu\); \(\mu=\nu\) is allowed. Line 27 deletes "all sites with \(|F(x)|\le C/\sqrt p\)" (squared mass \(\le C^2|Q|/p\le C^2/2\)) and ends: "These are cuts among the original four physical factors. They impose no bound on cutting the slope weight \(f_{\rm arc}\) itself." **(a2) ACCEPTED: R160:27 excludes slope cuts.**
- **(a3) The C²/p correction is right.** The paid vertex layer is \(|F|^2\le C^2/p\). The mission text ("vertex layers \(C/\sqrt p<|F|^2<a\)"), inherited from the Round 190 audit §3.5/§6.2 and the Round 190 checkpoint, mixed \(|F|\) and \(|F|^2\). The unpaid layers are \(C^2/p<|F|^2<a\); the layer \(|F|^2\asymp p^{-1/2}\) is unpaid and carries the vertex mass of flat laws.

### 2.2 Proposition 1, line by line (a4)

1. **Expansion.** R152:58–63: averaging \(|C_a(u)|^2\) with \(\nu\) replaces the anchor orthogonality by \(f(r_u(y)/r_u(x))\), with \(r_u(y)/r_u(x)=C_yA_x/(C_xA_y)=t\). It is linear in the rows, so it holds for \(F_{\ge a}\). *Independent numerical check* (audit Part F): the direct \(\sum_a\nu_a\sum_{u\ne1}|C_a(u)|^2\) equals the five-factor expansion to \(10^{-8}\) relative error at \(p=61,101,149\), flat and peaked laws.
2. **Cut.** \(C_{F,F}=C_{F_{\ge a},F_{\ge a}}+C_{F,E}+C_{E,F_{\ge a}}\) (bilinearity, \(E=F-F_{\ge a}\)); each cross term \(\le\sqrt{n\max\nu}\,\|F\|\|E\|\). **Correct.**
3. **Kept part.** Diagonal \(x=y\): \(\sum_u\sum_x|F_{\ge a}(ux)|^2|F_{\ge a}(x)|^2\le\|F_{\ge a}\|^4\). Off-diagonal: each vertex factor has \(|F|^2=g\ge a\), so \(\sqrt{g_1g_2g_3g_4}=g_1g_2g_3g_4/\sqrt{g_1g_2g_3g_4}\le a^{-2}g_1g_2g_3g_4\). Completion (R166:9–11) only adds nonnegative terms. **Correct.**
4. **Consequence.** With \(n\max\nu\ll\sqrt p\) and \(\|F\|^2\ll\sqrt p\): \(c_1pD\le2(\|F\|^4+\mathfrak M^\natural)+8n\max\nu\|F\|^2m_{<a}\ll p+\mathfrak M^\natural+p\,m_{<a}\). **Correct.**
5. *Numerical check of the inequality* (audit Part F, independent code; small \(p\), not near-critical): holds in all six runs.

**Verdict (a4): ACCEPTED** (agent bookkeeping, now audited). It uses absolute values on every off-diagonal term, so it needs neither R154's sign split nor the fixed-block machinery.

### 2.3 Proposition 2 and \(\mathcal M_{\sqrt g}\) (a5, a6)

- **Identity.** Expanding \(c(u)^2\) over \((x,y)\) and grouping by slope gives \(\sum_tP_t=X_c\); injectivity of \(r_u\) (R152:50) gives \(t=1\iff x=y\), so \(P_1=\mathrm{diag}\). With \(z=vx\), \(c(u)=\sum_{z\in\mathbb F_p}g(1-z)g(1-uz)=c_h(u)+g(1)^2\), so \(X_c=X+2\sum_uc_h(u)+(n-1)\) exactly, \(=X+O(p)\) since \(\sum c_h\le G^2\). **ACCEPTED.** *Independent exact check* (audit Part A): both identities and \(X_c=X+2\sum c_h+(n-1)\) at \(p=13,17,29,37,41\), two marks \(v\), random rational \(|f|\).
- **Consequence.** \(\sum_{t\ne1}|f(t)|P^\natural_t(\ge a)\le a^{-2}(X_c-\mathrm{diag})\). So \(X=O(p)\) pays every slope \(t\ne1\) at a fixed vertex level at once, including the bands and near-unit slopes. This is elementary once stated, but it is new and it changes the R190 picture: the near-unit "\(1/(1-s_1)\)" and band "\(p^{\sigma/2}\)" losses are artefacts of the weight \(w\), not of the slope part as such.
- **\(\mathcal M_w\le\mathcal M_{\sqrt g}\le X_c-\mathrm{diag}\)** (from \(w\le g\le\sqrt g\le1\)): checked exactly (Part A). **(a6) "weakest slope-complete first mass": ACCEPTED WITH CORRECTION (ii)** of the summary table: weakest among weights \(\varphi(t)\ge c|f(t)|\); and it is no easier than \(\mathcal M_w\) with respect to obstructions (§3.6).

### 2.4 Loss exponents (a7)

Recomputed in exact Fractions (audit Part C), against the accepted inputs:
- **Bands, fixed vertex level.** Under \(\mathcal M_w=O(p)\) alone, a band \(g\asymp p^{-\sigma}\) costs \((ab)^{-2}\max(|f|/w)\,\mathcal M_w\asymp p^{1+\sigma/2}\); the largest unpaid \(\sigma\) is \(1-4/445\) (R163:61), giving \(441/890\). R163's \(\sum_uh(u)^2\ll p^{3/2-2/445}\) gives the band at \(p^{3/2-2/445-\sigma/2}\) (consistent with its endpoint \(\sigma=1-4/445\)); the crossover at \(\sigma=\frac12-\frac2{445}\) gives \(441/1780\). R164 (lines 43–54) gives \(\sum_tN_t\ll p^{3/2-\gamma}\) and \(N_t\ll p^{1-\gamma}\), hence \(209/422\), \(209/844\) (\(\gamma=1/211\)) and \(13/27\), \(13/54\) (\(\gamma=1/54\), endpoint \(26/27\) from R163:80). **All correct.**
- **Near-unit slopes.** \(\min(p/\epsilon,\ p^{3/2-\gamma}(E+\epsilon)^{1/6}\log^{1/3})\) from R159's count times \(N_t\). The crossover is \(\epsilon=p^{-(6/7)(1/2-\gamma)}\), loss \((3-6\gamma)/7\): \(3/7\), \(627/1477\), \(26/63\). If \(E\) exceeds that \(\epsilon\), the loss is \(\frac12-\gamma+\frac16\log_pE\), larger. Since \(E\ge p^{-1/2}\), the regime \(E\le p^{-3/7}\) is nonempty, and at \(E=p^{-3/7}\) the two regimes agree. **Correct.**
- **Low layers.** R160: loss \(p^{1/2}\) against \(O(p)\) when \(m_{<a}\asymp\sqrt p\); against \(o(pD)\) at least \(p^{1/4}\log p/2\) (since \(D\le p^{1/4}/\log(2\sqrt p)\)). Majorant at \(\alpha=C/p\): \(\alpha^{-2}\asymp p^2\) with true amplitudes, \((\alpha^2\beta^2)^{-1}\asymp p^4\) with R166's. Rank-two (R160 rank-two:57–61): \(\sqrt{p-4}\prod\|h_j\|\) with \(\|h_j\|\le p^{1/4-(\alpha_j-1/4)_+}\) gives \(p^{7/4-\sum(\alpha_j-1/4)_+}\), loss \(3/4\) when all \(g\ge p^{-1/2}\). **Correct.**

### 2.5 The vertex part (a8, a9)

- **The decisive sign check.** (V) would be trivial if the physical vertices lived in the light sector \(T_{-\rho}\) (then \(m_{<a}\le G_{-\rho}=O(1)\) on (NC)). They do not: the reflection uses \(\chi(v)=\rho\) (R152:29, R153:15, R154:3), so a contributing vertex \(y=1-vx\), \(x\in Q\), has \(\chi(1-y)=\chi(vx)=\rho\), i.e. \(y\in T_\rho\), the heavy sector; R153:15 confirms that the nonsquare-\(x\) part (\(\chi(1-y)=-\rho\)) has mass \(O(1)\). Hence \(G^{\rm vert}=\sum_{T_\rho}g\ge(1-o(1))\sqrt p\) on (NC). **ASM's use is correct.**
- **(V)⇒(A\(_V\))** via R160's price \(\ll(p\,m_{<a})^{1/2}=o(\sqrt{pD})\): correct. **(V)⇒\(\sum g^2\ge a(G^{\rm vert}-m_{<a})\ge(a-o(1))\sqrt p\)**: correct. With R183 acc:264 (\(\sum g^2\le(\frac12+o(1))\sqrt p\)), \(a\le\frac12+o(1)\): correct. Low-energy sub-branch: \(\sum_{g\ge a}g\le\sum g^2/a=o(\sqrt p)\) (Chebyshev): correct. R183 acc:270 records the low-energy regime as open since Round 20: confirmed verbatim.
- **(V) is strictly stronger than high energy.** The \(D_{1/4}\) models have \(\sum g^2\approx0.17\sqrt p\) (high energy, \(\frac23\theta\)) and still \(m_{<0.05}\approx0.28\)–\(0.39\sqrt p\) (replayed). So even a resolution of the Round 20 question in the high-energy direction would not give (V).
- **Square-field control** (R157:45–54): \(g=4/(s-1)^2\) on \(Q\setminus H\), so \(m_{<a}\approx2\); the report's "(V) holds there" is right; with \(X\asymp P^{3/2}\) there, it shows (V) alone is not enough. Not re-derived beyond this arithmetic.
- **(a9) correction.** The "\(p^{3/4}\) floor for absolute pricing on admissible laws" is model evidence (\(\mathfrak M^\natural/p^{7/4}\approx0.016\)–\(0.026\) at \(p\le3209\), replayed). The report's own header says "(evidence)"; its sentence "This is a method statement on the admissible class, in the style of R183 Proposition C" overstates it: R183 Prop. C is proved, this is not.

### 2.6 What ASM changes

- **Confirmed:** (A) is a separate obligation, and fixed-block rounds cannot close the target in principle. The diagonal absorption of fixed-block constants (§2, C6) is correct and is the only free assembly.
- **New and correct:** (A) splits as (A-slope), which \(X=O(p)\) (or \(\mathcal M_{\sqrt g}=O(p)\)) discharges completely, and (A-vertex) = (A\(_V\)), which no first-mass form touches. Under \(\mathcal M_w=O(p)\), (A-slope) itself fails by the exponents above.
- **The real content for the plan:** on any law whose vertex mass sits below every fixed level (flat laws, \(D_\theta\), the low-energy sub-branch), the fixed-threshold programme of R162–R166, and every first-mass route built on it, addresses a vanishing share of the mass. (A-vertex) then requires a signed estimate on the layers \(C^2/p<|F|^2<a\), and every accepted device loses at least \(p^{1/2}\) there.

## 3. Report MWS: `native-claude-ordinary-first-mass-sector-obstruction-191.md`

**Sources checked.** The full report and mission; the three scripts (read; replayed in full). Re-read: R183 lines 36–56 (H1–H4, \(c_h\), \(E_Q(h)\)); the Round 190 audit's §4.6 table of \(\mathcal H\) items (which this audit's predecessor checked against the Round 183–189 `proof_scope` entries); R189 audit §2.4 (masked-to-unmasked) as cited. Not re-read at source: R183 Prop. A's proof (the row form; accepted in Round 183, and MWS Part I checks four forms agree exactly), R189 Prop. 3(a)–(c) beyond the cited statements, R190 Theorem 4's concentration proof.

### 3.1 Lemma 1 (m1)

Every row-form term is \(\mu(P)\mu(P')w(AD/(CY))\ge0\) (\(0\le w\le\frac14\)), so restricting to nontrivial \(I'\)-quadruples lowers the sum. On those, \(\mu\mu'\ge\tau'^4\); \(AD/(CY)\in\Sigma(I')\setminus\{1\}\) since \(P\ne P'\) (R183 A2); their number is \(\sum_\kappa c_{I'}(c_{I'}-1)=X_{\rm off}(\mathbf 1_{I'})\) (for \(\kappa\ne1\), \(Y\ne D\) is automatic). Sharpness on \(g_H=\delta_1+\frac14\mathbf 1_{H\setminus1}\): \(\tau'=\frac14\), \(\tau''=\frac3{16}\), product \(\frac3{4096}\), equal to R183 Prop. C(2); exact in MWS Part III (replayed). **ACCEPTED.** The comparison with R189 Prop. 3(b) (the triangle weight \(g\) is large near ratio 1, \(w\) vanishes there) is the right diagnosis.

### 3.2 Pure laws (m2, m8)

- (a) \(g=\mathbf 1_H\Rightarrow w\equiv0\Rightarrow\mathcal M_w=0\), while \(X(\mathbf 1_H)>0\). **ACCEPTED** (and audit Part B: \(\mathcal M_w(\mathbf 1_H)=0\) for every subgroup at \(p=101,109,113\)).
- **Lemma 3.** \(1-F_L(j)=\frac2L\sum_{|t|<L}(1-\frac{|t|}L)\sin^2(\pi tj/n)\) (from \(\frac1L\sum(1-\frac{|t|}L)=1\)); \(|tj/n|\le\frac{L-1}{2L}<\frac12\); \(4y^2\le\sin^2\pi y\le\pi^2y^2\) on \(|y|\le\frac12\); \(\sum_{|t|<L}(1-\frac{|t|}L)t^2=(L^3-L)/6\) (exact, audit Part C for \(L<60\)). Gives \([\frac43,\frac{\pi^2}3](L^2-1)(j/n)^2\). **ACCEPTED.**
- (b) Both sides follow with \(F_L\in[4/\pi^2,1]\) on the window (\(4K'\le n/(2L)\)). \((L^2-1)/n^2\le1/(64K'^2)\) for \(K'=\lfloor n/(8L)\rfloor\); \(\varepsilon^2X^{(\varepsilon)}\le X_2/K'^2\le16X_{\rm off}\) since \(|j|\le4K'\). **ACCEPTED.** (c) follows from R190 Theorem 4's uniform approximation; \((L'^2-1)K'^2/n^2\to1/64\). **ACCEPTED** (asymptotic).

### 3.3 The mixtures (m3–m5)

- **Theorem 3.** \(\sum_{\eta'\in\widehat Q}\eta'(x)=n\mathbf 1_{x=1}\) gives \(f=(1-\eta)f_J+\eta\mathbf 1_{x=1}\), so \(g=(1-\eta)^2F_L\) off 1 and \(g(1)=1\); cap \((1-\eta)n/L+\eta\); \(\omega=\frac12\nu*\check\nu\ge0\); (H3) since \(\nu\) is real. \(w\) concave, so its minimum on \([a,b]\) is at an endpoint; \(b=(1-\eta)^2<1\). At \(\eta=\frac12\): \(a=\pi^{-2}\), \(w_0=w(a)=(\pi^2-1)/\pi^4<w(\frac14)=\frac3{16}\), \(c=(\pi^2-1)/\pi^{12}=9.596\cdot10^{-6}\) (audit Part C). **ACCEPTED.**
- **Corollary 3.1.** \(L=\lfloor n/(8K')\rfloor\) gives \(\lfloor n/(8L)\rfloor\ge K'\); the cap holds when \(8(1-\eta)K'\le(C_{\rm cap}-\epsilon)\sqrt p\); monotonicity of \(X_{\rm off}\); masked-to-unmasked; \(|I'|^2\ll|I'|^{32/13-2\delta}\iff\delta<3/13\). Because \(\eta\) is free, every fixed \(C_{\rm cap}>0\) and every length \(\asymp\sqrt p\) is covered. **ACCEPTED** as an implication.
- **Theorem 4, item by item** (\(D_\theta^\eta\), \(S=S_1\sqcup S_2\)):

| Item | Check | Audit |
|---|---|---|
| 1–3 admissible, (NC1), flat | \(\nu=\mathbf 1_S/m\), \(0\notin S\), \(n/m\sim\sqrt p\) | correct |
| 4 (A2) | \(\mathcal E(S)\le m^2+\max_{a\ne0}|S\cap(S+a)|\,m^2\), so \(\mathcal E/m^3\le\theta(1-\eta)+o(1)<\frac12\) | correct |
| 5 (A5) | \(|S_1\cap(S_1+a)|\le\theta^2(L'-|a|)_++O(\sqrt{m\log p})\le\theta m_1+o(m)\); three cross terms have mean \(O(m^2/n)=O(1)\), McDiarmid + union bound over \(n\) shifts | correct |
| 6 (A6) | coset of order \(e\le2m_0\) is an AP of step \(\ge\sqrt p/2\); meets \(J'\) in \(\le L'e/n+1\to(1-\eta)/\theta+1\) points (\(m_0m/n\to\frac12\)); \(S_2\) part \(O(\log p)\) by Chernoff over \(\le n\,d(n)\) cosets | correct |
| 7 (A4) | as in R190 Theorem 4 item 7, plus \(|B|\sup_{x\ne1}|f_{S_2}|^2=O(\sqrt p)\,o(1)\) | correct |
| 8 obstruction | \(\mathbb Ef_{S_2}(x)=O(L'/n)\) off 1; deviation \(O(\sqrt{\log p/(\eta m)})\); \(f_{S_1}\to D_{L'}\); so \(g=(1-\eta)^2F_{L'}+o(1)\) uniformly off 1 | correct (needs \(\eta\) fixed \(>0\), as stated) |
| 9 | \(\Gamma_{\rm tot}\ge(a-o(1))^2|W'|\) | correct |

  Sector forms (NC2), (A3), R184 SRM Prop. 2, R184 Lemma 0, \(d_\rho(S)\to0\) are excluded from \(\mathcal H\), consistent with the Round 190 audit's correction (ii). **Theorem 4 ACCEPTED; Corollary 4.1 ACCEPTED** (\(|I'|=(\frac{\theta}{4(1-\eta)}+o(1))\sqrt p\), every fixed multiple of \(\sqrt p\) reachable).

### 3.4 Proposition 5 (m6)

\(w\ge\tau''\Rightarrow g\ge\tau''\) on \(\Sigma(I')\setminus\{1\}=\{\zeta^k:1\le|k|\le4K'\}\) (ord \(\zeta>8K'\)); R190 Theorem 1(4) puts it in \(T_\rho\) for fixed \(\tau''\); R190 Lemma 2 with \(K=2K'\) gives a \(\rho\)-clique of size \(4K'+1\le\sqrt p\). (ii) by Markov (R190 Theorem 1(3)) applied to both \(I'\) and \(\Sigma(I')\). **ACCEPTED.** Addendum (summary correction (ii)): Hanson–Petridis excludes the hypothesis on (NC) once \(4K'+1>(\sqrt{2p-1}+1)/2\), i.e. \(K'>(\sqrt2/8+o(1))\sqrt p\approx0.177\sqrt p\). MWS's sentence "Hanson–Petridis already excludes \(4K'+1>\dots\)" says this; it should add that this is an (NC2)-using exclusion and leaves Corollary 4.1 intact.

### 3.5 Evidence (m7)

All quoted §6.1 rows (including \(p=1009,5009,100049\) "in the script output") and §6.2 \(j\)-profiles reproduce exactly (replay log). The pure-law refinement (whether nontrivial energy concentrates at \(|j|=o(K')\)) is correctly marked as not needed for the cap.

### 3.6 Reconciliation with ASM's caution

ASM §4: "if \(w\) removes the sector pieces near unit slopes, they reappear in the slope part of (A)". Both branches are now settled:
- **For the hypothesis classes**, \(w\) removes nothing (Theorems 3–4): \(\mathcal M_w\ge c(\eta)X_{\rm off}(\mathbf 1_{I'})\).
- **For individual plateau-at-1 laws** \(w\) does remove the sector piece (Proposition 2(a)), and those pieces sit on slopes with \(g(t)=1\). The slope part of (A) must pay them through \(|f(t)|=\sqrt{g(t)}\), and there they are not removed: by the slope form, \(\mathcal M_{\sqrt g}(\mathbf 1_H)=X_{\rm off}(\mathbf 1_H)+2\sum_{\kappa\in Q\setminus1}c_H(\kappa)\ge E_{\rm off}(H)\) (audit Part B, exact for every subgroup at \(p=101,109,113\); the extra term is the completed physical zero \(z=0\)).
- **Monotonicity.** \(\mathcal M_w\le\mathcal M_{\sqrt g}\le X_c-\mathrm{diag}\) for every law, so Corollaries 3.1 and 4.1 hold verbatim for \(\mathcal M_{\sqrt g}\) and \(X\) (and already held for \(X\), \(T_0\) by Rounds 189–190). The admissible-only subgroup obstruction becomes \(E_{\rm off}(H)=O(p)\) with constant 1 for \(\mathcal M_{\sqrt g}\) (MSS: \(|H|^4/p+O(|H|^2\log|H|)\), so \(p\log p\) at \(|H|\asymp\sqrt p\)).
- **Combined statement (audit).** Every first-mass form that discharges (A-slope) (\(X\), \(\mathcal M_{\sqrt g}\)) meets the geometric-progression wall below \(p^{16/13}\) for admissible-only and \(\mathcal H\)-only arguments, and its target \(O(p)\) needs \(E^\times(I'-1)=O(|I'|^2)\) without logarithm. \(\mathcal M_w\) meets the same wall and does not even discharge (A-slope). Keeping \(w\) buys nothing.

## 4. Report GPSUB: `native-claude-ordinary-gp-sector-constancy-literature-191.md`

**Sources checked at source by this audit** (PDFs fetched with WebFetch and saved by the harness outside the repository; text extracted in the session scratchpad with a minimal stream decoder written for this audit; pages fetched with WebFetch):
- **Hanson–Petridis** arXiv:1905.09134v3 (margin stamp "arXiv:1905.09134v3 [math.NT] 6 May 2020"): Corollary 1.5 matches the report's quote verbatim ("Let p be a prime, d properly dividing p − 1 and suppose A ⊆ F_p is such that A − A ⊆ Z_d ∪ {0}. Then |A|(|A| − 1) ≤ d. In particular, for p ≡ 1 (mod 4), we have ω(G_p) ≤ (√(2p − 1) + 1)/2"); "The method developed to prove Theorem 1.2 only works in prime fields" present; Vinogradov "still the best known estimate for S_χ(A, B)" present.
- **Cochrane–Yip–Yoo** arXiv:2608.02568v3 (abs page: v3 submitted 6 Oct 2026): Corollary 4.6 "If p > 41 is prime and p ≡ 1 (mod 4), then ω(P_p) ≤ (1+√(2p−17))/2" matches; the §4.2 sentence "Little progress beyond the trivial upper bound √p was known, until Hanson and Petridis [8] famously proved the sharper bound" and the introduction's "while the range δ < 1/2 remains widely open" match. The text also derives \((1+\sqrt{2p-9})/2\) from Kalmynin's classification first; Corollary 4.6 improves the constant term only, as the report says.
- **Shparlinski**, "Open Problems on Exponential and Character Sums", dated "May 4, 2016": Problem 1 matches the report's quote (the \(\sum_{x=1}^N\chi(g^x+a)\) case "with very small values of N relative to p").
- **Chang–Shparlinski** arXiv:1401.6611v2 (stamp "15 Feb 2014"): "have been resisting all attempts to improve the classical bound (2)", with (2) \(|\sum_{\lambda\in G}\chi(a+\lambda)|\le\sqrt p\): matches.
- **Randomstrasse101** post (posted Dec 15, 2025; updated Dec 18, 2025), the arXiv:2603.29571v1 Section 12 (Entry 12, "On the clique number of the Paley Graph", Bandeira), and clopen OP-00041 (status Open; attributes the problem to Bandeira, Conjecture 26 of Randomstrasse101, Entry 12 of arXiv:2603.29571).

**(g4) Vinogradov consequence, re-derived.** For \(I=\{\zeta^j:0\le j\le M\}\), \(\chi(\zeta^{j'}(\zeta^h-1))=\chi(1-\zeta^h)\) (\(\zeta,-1\in Q\)) gives \(\sum_{x,x'\in I}\chi(x-x')=\sum_{0<|h|\le M}(M+1-|h|)\chi(1-\zeta^h)\); \(\sum_{0<|h|\le M}(M+1-|h|)=M(M+1)\) and \(M+1-|h|\le M\) give \(\rho\cdot\text{sum}\ge M(M+1)-2E_\rho M\); Vinogradov with \(A=I\), \(B=-I\) bounds the sum by \(\sqrt p(M+1)\); so \(E_\rho\ge(M+1)(M-\sqrt p)/(2M)\ge(M-\sqrt p)/2\). Exactly the count of points of \(\{\zeta^k:0<|k|\le M\}\) with \(\chi(1-y)=-\rho\). **Correct.** Audit Part D (independent code): identity exact in 2836 cases (\(p\le101\)), bound in 265044 cases (\(p\le400\)). Consequently the Round 190 wording of (GP-Sub\(_\kappa\)) ("there are \(\kappa>0\) and \(c_0>0\)") is **true but vacuous for \(D_\theta\)** (take \(c_0>1\)); the needed statement is "for every \(c_0>0\) there is \(\kappa>0\)". **(g7) ACCEPTED.**

**(g5) \(\mathbb F_{r^2}\).** \(\mathbb F_r^*\subset\) squares of \(\mathbb F_{r^2}\) (\(x^{(r^2-1)/2}=(x^{r-1})^{(r+1)/2}=1\)); for a generator \(\zeta\) of \(\mathbb F_r^*\), \(1-\zeta^k\in\mathbb F_r^*\) for \(1\le k\le r-2\), so \(R(\zeta)=\sqrt q-2\) with \(\operatorname{ord}\zeta=\sqrt q-1\). **Correct**; (GP-Sub\(_c\)) fails there for every \(c<1\), so primality must enter any proof below \(c=1\). Audit Part E (independent \(\mathbb F_r[i]\) arithmetic), \(r\in\{7,11,19,23,31,43\}\).

**(g6) "Randomstrasse101 Conjecture 26 is the project's own 1-localization theta target": TRUE.** Conjecture 26 reads \(\vartheta(\overline{G_{p,1}})\sim\sqrt{p/2}\) for primes \(p\equiv1\bmod4\), with \(G_{p,1}\) the subgraph induced on the neighbours of 0 (the nonzero squares). The repository README states the target as \(\vartheta(\overline H)/\sqrt n\to1\), \(H\) the Paley graph induced on the nonzero squares, \(n=(p-1)/2\), and links the same post; \(\sqrt n\sim\sqrt{p/2}\). The acceptance records cite arXiv:2603.29571 §12 and OP-00041, which attribute the same conjecture to Bandeira. **Context only**: it confirms the target is a recognised, published open problem; it is not new information for the project and is not evidence about any route. Note also (from those sources) that the conjecture would recover Hanson–Petridis through \(\omega(G_p)\le\vartheta(\overline{G_{p,1}})+1\), so the target is at least as strong as the current best Paley clique bound, up to \(1+o(1)\).

**Other rows.** Yu 2001 (zbMATH review), Shteinikov 2017, Gong 2014, Chang's survey, Yip, Kim–Yip–Yoo, Kerr, Chang 2008, Shkredov–Volostnov, Hanson 2015, Kunisky, Forbes et al. were **not re-read**. The Kerr non-transfer computation is re-derived: \(p^{-1/2}\sum_{t\ne0}|S(t,N)|\ge p^{-1/2}(pN-N^2)/N\ge N\) for \(N\le\sqrt p\) roughly, so the completion route is trivial there regardless of individual bounds. The Kim–Yip–Yoo arithmetic \(s(R-s+1)\le(p-3)/2\Rightarrow R\lesssim\sqrt{2p}\) is correct.

**Verdict.** "Refuted" in the mission's sense (open as far as the search reaches) **ACCEPTED**. A literature search cannot prove openness; the 2026 CYY remark on the Paley graph conjecture, the 2014–2017 open-problem statements and the absence of any progression-specific result support it.

## 5. Replay log

Run from the repository root on 2026-11-21 with `.venv/bin/python -B` (numpy from the repository `.venv`). Outputs went to the session scratchpad. "Matches" means every quoted output line or table row appears in the run, timing text excepted.

| Script | Command | rc | Time | Result |
|---|---|---|---|---|
| assembly exponents | `research/paley-191-assembly-exponents.py` | 0 | <1 s | `ALL OK` (Part B identities at \(p=13,\dots,41\)) |
| assembly models | `research/paley-191-assembly-models.py` | 0 | 4 s | matches ASM §8 Parts A and B (all twelve "R160 ok"/"Prop1 ok" True) |
| mwsector exponents | `research/paley-191-mwsector-exponents.py` | 0 | <1 s | `ALL OK` |
| mwsector exact | `research/paley-191-mwsector-exact.py` | 0 | 2 s | `ALL EXACT CHECKS OK` |
| mwsector models | `… --check` | 0 | 1 s | `CHECK OK` |
| mwsector models | `… laws 1009 5009 20011 100049 1000033 4000037` | 0 | 14 s | matches every §6.1 row |
| mwsector models | `… jdist 0.25 …` / `… jdist 0.5 …` | 0 | 1 s each | matches every §6.2 row |
| gpsub checks | `research/paley-191-gpsub-checks.py` and `--pmax 1000` | 0 | 1 s / 2 s | Part V 3,431,852 cases, margin 1.062 at \(p=17\); Part F \(R=r-2\); Part X `ALL OK` |
| audit | `research/paley-191-audit-check.py` | 0 | <1 s | `ALL AUDIT CHECKS OK` (74 checks, Parts A–F) |

SHA-256 (as audited):
- reports: ASM `6bb5df8ac903432a72e805a48e1e2922f83cf4aaa73fe6c8e114e1e1ad64b69c`, MWS `ea04d03bad2960ad2ba7baa38d90d9c686d99136709b7f17446621361417f22b`, GPSUB `738c6594f78658ba8beca24fba4f61ebe9ebfd7e95d9d75e2fed2997679c09c9`
- scripts (all match the hashes printed in the reports): `paley-191-assembly-exponents.py` `2df3ce44…b32f`, `paley-191-assembly-models.py` `b7935762…615d`, `paley-191-mwsector-exact.py` `1cd6ffde…8a2a`, `paley-191-mwsector-exponents.py` `f9df0841…b7f9`, `paley-191-mwsector-models.py` `4b3582ea…1912`, `paley-191-gpsub-checks.py` `91a88be6…1a58`
- mission sources: `coordination/round-190.json` `b8f6e40f…05cc`, `research/round-190-acceptance.json` `11c42c0a…409b` (both match the missions); mission files match the inflight manifest.

**Not checked:**
- ASM: R155, R156, R158, R159, R165, R172, R180 beyond what earlier audits checked; R154:77–93 (taken as cited); the R160 pair-cut homogeneity (C4) beyond the bilinear form of R160:29–38; whether (V) is compatible with (NC) (§6.4).
- MWS: the proof of R183 Prop. A (row form) beyond MWS's exact four-form check; R189 Prop. 3(a)–(c) and R190 Theorem 4's concentration step beyond their statements; asymptotics beyond the replayed models.
- GPSUB: every row not listed in §4 as read at source; the report's search coverage (arXiv/zbMATH/Semantic Scholar screens) was not repeated. I ran no independent literature search.

## 6. Ranked closeout

### 6.1 What Round 191 changes

| Obligation | Before (Round 190 acceptance) | After Round 191 (as audited) | Effect |
|---|---|---|---|
| (A) assembly | named; "loses \(p^{\sigma/2}\), \(1/(1-s_1)\), \((a^2b^2)^{-1}\)" under \(\mathcal M_w\); unpaid vertex layers written "\(C/\sqrt p<|F|^2<a\)" | **Split.** (A-slope): every slope \(t\ne1\) at a fixed vertex level; discharged exactly by \(X=O(p)\) or \(\mathcal M_{\sqrt g}=O(p)\) (Proposition 2: \(\sum_{t\ne1}P_t=X_c-\mathrm{diag}\)); **not** by \(\mathcal M_w=O(p)\) (losses 441/890 alone, 441/1780 with R163; near-unit unbounded alone, ≥3/7 with R159). (A-vertex) = (A\(_V\)): the layers \(C^2/p<|F|^2<a\), all slopes, signed; closed by (V) \(m_{<a}=o(D)\) for one fixed \(a\le\frac12\); otherwise needs a signed estimate; accepted devices lose \(p^{1/2}\) (R160), \(p^{3/4}\) (rank-two at \(g\ge p^{-1/2}\)). Fixed-block rounds are insufficient in principle. | **reformulated** + **new_obstruction** (to "first mass closes the target") |
| Fixed-block target | \(\mathcal M_w=O(p)\) named the weakest closing form (fixed blocks) | **Demoted.** The weakest form that also pays (A-slope) is \(\mathcal M_{\sqrt g}=O(p)\) (implied by \(X=O(p)\)). All three are \(\ll p^{4/3+o(1)}\). | reformulated |
| GP wall for first masses | known for \(T_0\), \(X\) (R189–R190); open for \(\mathcal M_w\) | **Binds \(\mathcal M_w\)** (Theorems 3–4: \(\eta\)-mixtures defeat \(w\)), hence \(\mathcal M_{\sqrt g}\) and \(X\) by monotonicity. Admissible-only or \(\mathcal H\)-only arguments below \(p^{16/13}\) must prove `cand:gp-shifted-energy` below \(|I'|^{32/13}\); for the target \(O(p)\), \(E^\times(I'-1)=O(|I'|^2)\) log-free. Subgroup log obstruction for \(\mathcal M_{\sqrt g}\) with constant 1. | **new_obstruction** (method cap extended) |
| `cand:gp-sector-constancy` | open below \(c=1/\sqrt2\) (HP), not searched | **Searched; open.** Known: (GP-Sub\(_c\)) for \(c>1/\sqrt2\) (HP; CYY 2026 refines the constant term only); (GP-Sub\(_\kappa\)) only for \(c_0>1\) (Vinogradov); false in \(\mathbb F_{r^2}\) for \(c<1\). Implied by the Paley graph conjecture and by \(\omega(G_p)=o(\sqrt p)\), both open. Wording must be "for every \(c_0>0\)". | evidence_only (status recorded; external) |
| (NC) sector lever | reduced to (GP-Sub); Criteria 5.1–5.2 conditional | unchanged mathematically; with GPSUB, the lever below 45/26 rests on an open external problem; retire it as an estimate route | unchanged (retired) |
| One-match, zero match, \(\mathcal D\), J split | off the critical path | unchanged | unchanged |
| Cold line; the target | paused; open | unchanged; target confirmed to be Randomstrasse101 Conjecture 26 / OP-00041 (context) | unchanged |

### 6.2 The full current ordinary obligation map

On the hypothetical critical branch (R157/R160 hypotheses), the contradiction follows from **(S\(_a\)) and (V\(_a\)) for one fixed \(a\in(0,\frac12]\)** (ASM Proposition 1; weakest found form (A\(_{\rm unif}\))):

1. **(A-slope) = (S\(_a\))**: \(\sum_{t\ne1}|f(t)|P^\natural_t(\ge a)=O(p)\). Sufficient: \(X=O(p)\) or \(\mathcal M_{\sqrt g}=O(p)\), logarithm-free.
   - Current: \(X,\mathcal M_{\sqrt g},\mathcal M_w\ll p^{4/3+o(1)}\) (R187), at the accepted method cap of that route. Floor \(X\ge(2-o(1))p\) on (NC): the statement is sharp-order with no room for a logarithm.
   - **GP wall:** admissible-only and \(\mathcal H\)-only arguments cannot go below \(p^{16/13}\) without improving MPRRS Theorem 37 (`cand:gp-shifted-energy`), and cannot reach \(O(p)\) without \(E^\times(I-1)=O(|I|^2)\) for all symmetric GPs of length \(\asymp\sqrt p\) (gap \(6/13\) in \(|I|\)). Subgroup laws add a log obstruction (\(E_{\rm off}(H)\), MSS \(p\log p\)).
   - **Sector route:** (NC2) excludes the fixed-height GP laws only under (GP-Sub\(_c\)) for all \(c\) (`cand:gp-sector-constancy`, open below \(1/\sqrt2\)), and the lower-height ones only under quantitative (GP-Sub\(_\kappa\)) at small \(c_0\) (open below \(c_0=1\)); even then it removes an obstruction family and proves no bound.
2. **(A-vertex) = (A\(_V\))**, or its sufficient form **(V)** \(m_{<a}=o(D)\):
   - (V) implies \(\sum g^2\ge(a-o(1))\sqrt p\), i.e. the high-energy side of the Round 20 low-energy question (R183 acc:270, open since Round 20), and is strictly stronger than high energy (\(D_\theta\) models).
   - Without (V): a genuinely signed estimate on the layers \(C^2/p<|F|^2<a\), with all slopes and both signs. This is the original oscillation problem restricted to the low layers, where flat laws carry all of their mass; every accepted device loses at least \(p^{1/2}\).
3. **External problems the map rests on:** `cand:gp-shifted-energy` (sharp form), `cand:gp-sector-constancy`; and the target itself.
4. **Off the critical path:** one-match \(43/24\) (+ zero match), \(\mathcal D\), J split, \(\mathcal M_w\) as a target.

### 6.3 Which obligations are recognised external open problems

- **The target** (\(\vartheta(\overline{G_{p,1}})\sim\sqrt{p/2}\)): Randomstrasse101 Conjecture 26, arXiv:2603.29571 §12, clopen OP-00041 ("Open"). It would recover the Hanson–Petridis clique bound.
- **`cand:gp-sector-constancy`:** a special case (non-constancy along geometric progressions) of statements recorded as open: the Paley graph conjecture (Chang's survey Problem 4.3; CYY 2026: "remains widely open" for \(\delta<\frac12\)), \(\omega(G_p)=o(\sqrt p)\), Shparlinski's 2016 Problem 1, Chang's Problem 3. The special case itself is not stated in the literature (GPSUB found none); recognised by implication.
- **`cand:gp-shifted-energy` below \(|I|^{32/13}\):** an improvement of MPRRS Theorem 37 / Shkredov Lemma 43 for shifted sets with small product set, a recognised sum-product frontier question; the sharp form \(O(|I|^2)\) needed for \(X=O(p)\) by admissible-only arguments is far beyond it. I did not find (and did not search for) a source stating that exact form as a conjecture; record it as "frontier, recognised in kind".
- **Internal, not recognised as such:** (A-vertex)/(V), and \(X=O(p)\) for the actual law. \(X=O(p)\) by arguments that do not see the sector reduces to the two external problems above; (A-vertex) has the depth of the target restricted to the low layers.

### 6.4 Strategic recommendation (frank)

- **Pause ordinary estimate rounds, and record the ordinary line as reduced to external problems plus one internal structural gap, as was done for cold.** Round 191 met the Round 190 audit's hold condition exactly: (A) does not follow from fixed blocks; \(\mathcal M_w\) is sector-obstructed; (GP-Sub) is open. It also showed more: the first-mass forms that could discharge (A-slope) (\(X\), \(\mathcal M_{\sqrt g}\)) meet the same wall, and no first-mass form touches (A-vertex). Every remaining ordinary obligation is either (a) behind `cand:gp-shifted-energy` in sharp form or `cand:gp-sector-constancy`, or (b) (A-vertex), which on flat or low-energy laws is the whole problem. A further method-cap or pricing round would re-derive these walls.
- **What the hold record should state** (exact hypotheses kept): the reduction R152–R166 plus Proposition 1; the split (A-slope)/(A-vertex); the current \(p^{4/3+o(1)}\) for \(X\), \(\mathcal M_{\sqrt g}\), \(\mathcal M_w\); the GP walls with MPRRS Theorem 37 and the (GP-Sub) status; that the D\(_\theta\)/mixture families and all models are finite or method evidence; that nothing proves or refutes the target.
- **At most one internal call is defensible**, and only if the coordinator wants a final structural test before holding:

  **`ordinary-nc-vertex-tightness`** (structural; desk check of accepted results plus models; no new incidence estimates).
  - **Question:** Do the accepted (NC) consequences, **including** the sector forms ((NC2) \(V_{-\rho}\to0\), (A3) \(G_{-\rho}=O(1)\), \(M_1=(1+o(1))p\), R184 SRM Prop. 2 and Lemma 0, \(d_\rho(S)\to0\)), imply vertex tightness (V) \(m_{<a}=o(D)\) on \(T_\rho\) for some fixed \(a\le\frac12\), or at least \(\sum g^2\gg\sqrt p\)? Or is there an obstruction: an argument (or an explicit family consistent with every accepted (NC) statement) with \(m_{<a}\asymp\sqrt p\) for every fixed \(a\)?
  - **Why now:** after Round 191, (A-vertex) is the only ordinary obligation not already reduced to an external problem, and (V) is its only accepted sufficient form; whether (NC) can reach it decides whether the internal programme has any remaining lever. ASM ranks it first.
  - **Scope:** hypotheses exactly as in R157:3/R160:3 and Round 183's (NC); vertex sector \(T_\rho\) (\(\chi(v)=\rho\)); cite accepted statements by round and line; distinguish sector-free and sector forms; models only as evidence; no claim about the actual law beyond accepted statements. Note for the researcher: the Round 20 low-energy question (R183 acc:270) is the weaker statement and has been open since Round 20; an uncertainty-principle reading (vertex mass on \(\asymp\sqrt p\) points at levels \(\ge a\), with \(\nu\) flat on \(\asymp n/\sqrt p\) points) suggests (V) forces near-coset structure, which (A2)/(A6) exclude; this heuristic is the auditor's, unverified.
  - **If yes ((NC) forces (V)):** (A-vertex) is discharged; the ordinary line reduces to \(X=O(p)\) (or \(\mathcal M_{\sqrt g}=O(p)\)) alone, still behind the GP walls; record that and hold.
  - **If no (an obstruction to (V) on (NC)):** (A-vertex) needs a signed estimate on the low layers with no accepted tool; record (A-vertex) as an internal open problem of target depth and hold.
  - **If inconclusive:** record the exact (NC) statement that would decide (V) and hold.
  - **My expectation:** "no" or inconclusive. Either way the decision after it is hold. Given the weekly quota (near 80%, per the Round 190 checkpoint), skipping it and holding now is also reasonable; I recommend holding now unless the coordinator values the extra clarity on (A-vertex) more than the quota.
- **Do not run:** further first-mass pricings (\(\mathcal M_w\), \(\mathcal M_{\sqrt g}\), \(X\)) without a new arithmetic input; further general literature searches on (GP-Sub) or shifted GP energies (both now covered); the pure-law \(j\)-concentration refinement (does not change the cap); cold (paused).

### 6.5 Routes to retire

- **\(\mathcal M_w=O(p)\) as a target** (it does not pay (A-slope) and is sector-obstructed).
- **Fixed-block estimate rounds** of any closing form, until (A-vertex) is addressed.
- **The (NC) sector lever below 45/26** (rests on open (GP-Sub)); **sector-free (NC) or admissible-only arguments for \(T_0\), \(X\), \(\mathcal M_{\sqrt g}\), \(\mathcal M_w\) below \(p^{16/13}\)**.
- **Literature searches** for (GP-Sub) and for \(E^\times(A+\alpha)\) beyond Theorem 37.
- Still retired from Round 190: one-match as a standalone target; zero match; J-split / full-diagonal routes; subgroup laws as an obstruction; cold per-simple prices.
- **Not retired:** (A-vertex)/(V) as a named internal problem (optional call above); \(X=O(p)\) as the named slope-complete target (pending an external input).

### 6.6 Bookkeeping for the coordinator

- Correct "\(C/\sqrt p<|F|^2<a\)" to "\(C^2/p<|F|^2<a\)" wherever the Round 190 records carry it.
- Re-quantify `cand:gp-sector-constancy`'s quantitative form: "for every \(c_0>0\) there is \(\kappa>0\) …"; record its status (open for \(c\le1/\sqrt2\), \(c_0\le1\); false in \(\mathbb F_{r^2}\) for \(c<1\)).
- `cand:gp-shifted-energy`: value unchanged; now binds \(\mathcal M_w\), \(\mathcal M_{\sqrt g}\), \(X\), \(T_0\).
- `cand:slope-row-mass-x`: value unchanged (\(p^{4/3+o(1)}\)); role changed: \(X=O(p)\) is the slope-complete target; record the identity \(\sum_{t\ne1}P_t=X_c-\mathrm{diag}\), \(X_c=X+2\sum c_h+(n-1)\).
- Consider recording the three IDs under `shared_candidates` in the Round 191 coordinator record (§1, after unblinding); a new ID for (V) is justified only if the optional call is made.
- ASM corrections (i)–(iv), MWS (i)–(iii), GPSUB (i)–(ii) of the summary table.

## 7. Status of this audit

This is an agent audit, not human acceptance or certification.

**What I checked:**
- ASM: Proposition 1 line by line from R152:43–70, R157:1–54, R160:1–38 and R166:1–15; Proposition 2 by an exact independent computation; the vertex sector \(T_\rho\) from R152:29, R153:15, R154:3; every loss exponent in exact arithmetic against R159 (as cited), R162:1–30, R163:45–82, R164:18–56 and R160 rank-two:55–62; (V) and its consequences against R183 acc:264/270; the R160 correction; model replays.
- MWS: Lemma 1, Proposition 2, Lemma 3, Theorems 3–4 item by item, Corollaries 3.1/4.1, Proposition 5; the reconciliation with ASM, including an exact computation of \(\mathcal M_{\sqrt g}(\mathbf 1_H)\) for every subgroup at three primes; all replays.
- GPSUB: HP Corollary 1.5, CYY Corollary 4.6 (with both quoted sentences), Shparlinski Problem 1, Chang–Shparlinski's "resisting" sentence, all at source; the Randomstrasse101 post, arXiv:2603.29571 §12 and OP-00041 against the README; the Vinogradov consequence and the \(\mathbb F_{r^2}\) example, re-derived with independent code.

**What I did not check:** listed under "Not checked" in §5.

**Files:** nothing was committed. Only this file and `research/paley-191-audit-check.py` were written. Replay outputs, fetched PDFs' extracted text and the small PDF text decoder went to the session scratchpad.

Final SHA-256 of the audit script: `paley-191-audit-check.py` `74cbe398b37cf67597971a268c75e2ec1a16dc3bb8a4cf12dc2d81c8761749f3`.
