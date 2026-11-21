# Independent audit of Round 190 (session/r190-audit)

- **Auditor:** Claude subagent started by the Round 190 coordinator (session/r190-audit). This is an agent audit, not human acceptance and not a mathematical certification. The auditor wrote none of the three reports and is not the coordinator.
- **Status of this file:** written incrementally. The "Blind overlap review" section below was saved before any file under `coordination/shared-obligations/`, `coordination/drafts/` or any `coordination/round-*-inflight.json` was opened.
- **Read before the blind review:** `AGENTS.md`, `docs/WORKFLOW.md`, `docs/ROUND_REVIEW.md`, `coordination/checkpoints/round-189.md`, `research/native-claude-audit-189.md`, the three missions in `coordination/missions/round-190/`, and the three reports.

Verdict key (per claim the report labels as proved, or as bookkeeping that the coordinator may carry forward):
- **ACCEPTED:** correct as written, for the stated hypotheses.
- **ACCEPTED WITH CORRECTION:** true after the stated correction, which does not change the report's main conclusion.
- **CONDITIONAL:** correct given a named input that is not proved or not checked.
- **REJECTED:** false as written, or not supported.

Reports, abbreviated:
- **GPLIT** = `native-claude-ordinary-gp-shifted-energy-literature-190.md` (MPRRS Theorem 37 and the literature table), with `paley-190-gplit-exponents.py`. Report verdict: supported.
- **STOCK** = `native-claude-ordinary-obligation-map-stocktake-190.md` (links L0–L6b, pieces P1–P9, ranking, bookkeeping B1–B6), with `paley-190-stock-exponents.py`. Report verdict: yes, with qualifications.
- **NC** = `native-claude-ordinary-nc-excludes-sector-laws-190.md` (Lemma 1, Theorem 1, Lemma 2, Corollary 1.1, Propositions 2–3, Theorem 4, Corollary 4.1, Criteria 5.1–5.2), with `paley-190-nc-*.py`. Report verdict: inconclusive.

## 1. Blind overlap review

Written after reading the three reports and their missions. No shared-obligation, draft or inflight file had been opened.

| Pair | Classification | Reason |
|---|---|---|
| GPLIT – STOCK | **touch, not an overlap** | GPLIT changes the external input of the Round 189 method cap (`cand:gp-shifted-energy`: \(|I|^{5/2}\to|I|^{32/13}\)). STOCK cites that cap only as a status line (P7(c), P8(c)–(d): "Below \(p^{5/4}\), admissible-only arguments need (GP)"; "The obstruction uses MPRRS Lemma 33"). STOCK's ranking and its L3 composition do not use the cap's numerical value, so GPLIT makes those two status lines out of date (the cap threshold becomes \(p^{16/13}\)) but changes no STOCK conclusion. No common estimate is proved by both. |
| GPLIT – NC | **touch, different statements** | Both concern geometric progressions \(I=\{\zeta^k:|k|\le K\}\subset Q\), \(|I|\asymp\sqrt p\), in \(\mathbb F_p\), but they are **different statements**: GPLIT is about the **multiplicative energy** \(E^\times(I-1)\) (a sum-product incidence count; `cand:gp-shifted-energy`); NC's (GP-Sub\(_c\)/\(_\kappa\)) is about **character-sum constancy**, \(\chi(1-\zeta^k)\) constant for \(1\le k\le c\sqrt p\) (geometric-progression Paley cliques). Neither implies the other: Theorem 37 says nothing about the Legendre symbol on \(1-I\), and (GP-Sub) says nothing about the energy. The interaction is in use: NC's Corollary 4.1(i) and Criterion 5.2 quote the cap with the Lemma 33 value \(p^{5/4}\); with GPLIT the same statements hold with threshold \(p^{16/13}\) (Corollary 4.1(i) then says: (NC)-non-sector arguments reaching \(T_0\le p^{16/13-\delta}\) must prove \(E^\times(I-1)\ll|I|^{32/13-2\delta}\)). NC's "next test 1" (literature on \(\sum\chi(1-\zeta^k)\), GP Paley cliques) was **not** part of GPLIT's mission and is not answered by it. |
| STOCK – NC | **independent in substance; both touch `cand:slope-row-mass-x` in use** | STOCK uses (NC) only through accepted floors (\(X\ge(2-o(1))p\), \(\Gamma_{\rm tot}\le(\frac12+o(1))\sqrt p\), hence \(W\asymp\sqrt p\)). NC proves new (NC) facts (\(G_{-\rho}\le1+o(1)\), \(\sup_{T_{-\rho}}g\to0\)) that STOCK does not use and that do not change STOCK's L4/B6 tightness claim (B6 uses only \(\Gamma_{\rm tot}\le(\frac12+o(1))\sqrt p\)). STOCK's open item (its §6, item 4) ("whether the R189 obstruction applies to \(\mathcal M_w\)") is not answered by NC, which works with \(T_0\), \(X\) and \(\Gamma_{\rm tot}\) only and states that it did not write out a sector reduction of \(X\). No duplicated work. |

- **No shared estimate is proved twice.** The three calls answered three different questions (an external value, an internal map, an internal structure question).
- **Would an overlap review have changed dispatch?** Partly, for GPLIT–NC: had the coordinator anticipated NC's (GP-Sub), it could have added "character sums \(\sum_{k\le M}\chi(1-\zeta^k)\) at \(M\asymp\sqrt p\) and geometric-progression Paley cliques" to the literature call's scope. That is an extension of scope, not a duplication; it does not invalidate either call. GPLIT – STOCK and STOCK – NC: no.
- **Candidate touches.** `cand:gp-shifted-energy`: value changed by GPLIT (a published bound at \(|I|^{32/13+o(1)}\)); touched in use by NC (Cor. 4.1(i)) and STOCK (status lines). `cand:slope-row-mass-x`: touched in use by STOCK (the ranking promotes \(\mathcal M_w=O(p)\) / \(X=O(p)\) as the closest closing obligation) and NC (no value). NC proposes a new candidate (GP-Sub); none of the three records it.

### After unblinding

Opened afterwards: `coordination/round-190-inflight.json`, `coordination/shared-obligations/round-190-before.json` and `coordination/drafts/round-190-dependency-assessment.json` (no `round-190-after.json` exists yet).

- The coordinator's pre-dispatch comparison (`comparison_status: assessed`, `known_shared: []`, empty `candidate_ids_by_call`) dispatched the three calls as independent. It says the literature and structural calls "address the same obstruction from two sides but need different statements" (external energy theorem versus a structural property of the actual law), and asks each report to "state any input that bears on the other". The stocktake "shares no estimate with either".
- **Agreement.** My blind classification matches: no shared estimate; GPLIT – NC is a touch in use on the same obstruction through different statements.
- **Request honoured?** NC did (its "Shared estimates" names `cand:gp-shifted-energy` and proposes (GP-Sub) for a literature check together with (GP)). GPLIT did not mention the structural call; this is immaterial because GPLIT's mission had no character-sum item beyond "Stepanov-type or character-sum bounds for shifted short geometric progressions", which it answered (§3(b): none for non-subgroup progressions). GPLIT's §3(b) answer is about energy-type and fibre-count statements, not about \(\sum_k\chi(1-\zeta^k)\); so NC's (GP-Sub) literature question is **still unasked**.
- **What the pre-dispatch comparison did not foresee:** the literature result moves the cap that NC's Corollary 4.1(i) and Criterion 5.2 quote (from \(p^{5/4}\) to \(p^{16/13}\)), and STOCK's status lines P7(c)/P8(d) cite the pre-GPLIT value. These are touches on `cand:gp-shifted-energy` found after the calls, recorded under the existing ID; no new shared ID is needed for them. (GP-Sub) is a candidate proposed by NC; whether to record it is assessed in §6.2.
- **Dispatch effect:** none for the three calls as run. The scope extension for a literature call noted above is carried into my Round 191 recommendation (§6.3). Lane labels `session/r190-gp-literature`, `session/r190-stocktake`, `session/r190-nc-sector` match the report headers; all three share one `started_utc_epoch` (recorded once before the three launches, as the manifest says).

## Summary of verdicts

| Report | Main verdict | Corrections / conditions |
|---|---|---|
| GPLIT. Shifted geometric-progression energy, literature | (g1) **Theorem 37 quote ACCEPTED** (read at source by this audit, arXiv:1702.01003v5 p. 45, verbatim match); (g2) **applicability to symmetric GPs at \(|I|\asymp\sqrt p\) ACCEPTED**; (g3) **internal constraints (Lemmas 32–33, Theorem 34) ACCEPTED WITH CORRECTION**; (g4) **\(E^\times(I-1)\ll|I|^{32/13+o(1)}=p^{16/13+o(1)}\) ACCEPTED**; (g5) **cap moves to \(p^{16/13}\) / one-match \(45/26\) ACCEPTED WITH CORRECTION** (a weakening of the obstruction, not a cap theorem); (g6) **"Rounds 186–189 missed it" ACCEPTED**; (g7) **"does not apply to partial-product graphs" ACCEPTED**; (g8) Shkredov Lemma 43 restatement **ACCEPTED** (read at source); other table rows **not re-read** (accepted as reported). Verdict **supported: ACCEPTED**. | (i) The tilde hides \((\log|A|)^{18/13}\) (from Theorem 34's \(\log^{12/13}\) and \(D_1^{6/13}\)); (ii) the proof of Theorem 37 checks only the first condition of Lemma 33; the second, \(\max(|AA|,|B|)\le(|A||AA||B|)^{1/2}\), i.e. \(M\le|B|\le M|A|^2\), holds for \(|B|\le|A|^{20/13}M^{-33/13}\) at the upper end, and for \(|B|<M\) the trivial bound \(E^\times(A+\alpha,B)\le|A||B|^2\le M^{1/2}|A||B|^{3/2}\) suffices; (iii) the 45/26 statement is: below covariance 45/26 the sector family still obstructs admissible-only arguments; between 45/26 and 7/4 it is no longer known to obstruct. Nothing shows an admissible-only argument can reach \(T_0\le p^{5/4-\delta}\); (iv) §5's mention of "the Round 187 height-1 pricing pieces where Lemma 33 was used" is inaccurate: no accepted proof used Lemma 33 (R186 §6.3, R187 line 72), and the height-1 use would need a mixed \(E^\times(A+\alpha,B)\) bound, which Theorem 37 does not give. |
| STOCK. Obligation-map stocktake | (s1) **B1 / L3 composition ACCEPTED** as a fixed-block statement (re-derived line by line below); (s2) **"one-match \(O(p^{3/2})\) is not necessary" ACCEPTED** (formal: only one + zero is constrained; no mechanism for a negative zero-match class is known); (s3) **current values ACCEPTED**; **B3** zero-match bookkeeping **ACCEPTED**; Katz-implied \(p^{5/2}\) **ACCEPTED as bookkeeping** (not re-derived from R168 in detail); (s4) **ranking ACCEPTED** as arithmetic (script and my Part A); (s5) **B4** J classes 0,1 \(\to p^{7037/3840+o(1)}\) and \(\mathcal D_J\ll p^{11/6+o(1)}\) **ACCEPTED**; **B5**, **B6 ACCEPTED**; (s6) §6 "could not be recovered" items **ACCEPTED**, with §6.2 **strengthened**. Headline "\(\mathcal M_w=O(p)\) closes each fixed moderate block on its own" **ACCEPTED**; the reading "closes the target" **REJECTED** (the report does not claim it, but §0.3, the "closes alone?" column and §8 invite it). Verdict **"yes, with qualifications" ACCEPTED WITH CORRECTION**. | Correction: every route in the map (one-match + zero, \(\mathcal D\), J split, \(\mathcal M_w\), \(X\)) proves at most the **fixed-block** obligation \(O_{a,b,s_0,s_1}(p)\). The assembly into the uncut favorable off-diagonal is a separate, unrecovered obligation, and under the first-mass bound it **loses powers**: \(p^{\sigma/2}\) on a slope band \(g\asymp p^{-\sigma}\) (\(0<\sigma<1-2\gamma\)), a factor \(1/(1-s_1)\) as \(g\to1\), and \((a^2b^2)^{-1}\) as the vertex thresholds fall towards \(p^{-1}\). The \(\mathcal D\) route loses the same powers. So "closest closing obligation" means "closest obligation that closes the fixed block". The C-S "no order loss" (B6) is a statement about the conversion of targets, not about the size of the actual \(\mathcal D\). |
| NC. (NC) and sector laws | (n1) **Lemma 1 ACCEPTED** (re-derived; independent replay from Round 20's formula); (n2) **Theorem 1 ACCEPTED**; (n3) **Lemma 2 ACCEPTED**; **Corollary 1.1 ACCEPTED**; Hanson–Petridis **confirmed at source** (Corollary 1.5 of arXiv:1905.09134v3); (n4) **Proposition 2 ACCEPTED**; (n5) **Proposition 3 ACCEPTED**, its "What it gives" Paley-triangle remark **ACCEPTED WITH CORRECTION** (fixed heights only); (n6) **Theorem 4 ACCEPTED**, **Corollary 4.1 ACCEPTED WITH CORRECTION** (threshold \(p^{16/13}\) after GPLIT; list of sector forms incomplete); (n7) Criteria 5.1, 5.2 **CONDITIONAL** on (GP-Sub\(_c\)) for all \(c\), resp. (GP-Sub\(_\kappa\)); status of (GP-Sub\(_c\)) for \(c>1/\sqrt2\) **ACCEPTED** (HP at source). Evidence §7 **reproduced**. Verdict **inconclusive ACCEPTED**. | (i) After GPLIT, Cor. 4.1(i)/(iii) and Criterion 5.2 hold with threshold \(p^{16/13}\) (covariance 45/26) instead of \(p^{5/4}\) (7/4): the D\(_\theta\) family is no longer known to obstruct \(T_0\le p^{5/4-\delta}\) for \(\delta\le1/52\); (ii) Cor. 4.1(iii)'s list of sector forms should also name \(M_1=(1+o(1))p\) and the Round 184 SRM Prop. 2 floors (\(X\ge(2-o(1))p\) etc.), which are derived from it; D\(_\theta\) has \(M_1\approx p/2\); (iii) Prop. 3's "both \(Y,Y'\) of a heavy term may be taken heavy … Paley \(\rho\)-triangle" holds for fixed heights \(\tau\); at \(\tau=p^{-1/24-\delta}\) Theorem 1(4) does not apply, only the count \(\le(1+o(1))p^{1/24+\delta}\) of heavy points in \(T_{-\rho}\); (iv) the §7.2 cell "17 (≤0.283√p, at p=1013)" conflates two maxima (17 at \(p=8537\); the ratio 0.283 at \(p=1013\)). |

## 2. Report GPLIT: `native-claude-ordinary-gp-shifted-energy-literature-190.md`

**Sources checked.** The full report and mission; `paley-190-gplit-exponents.py` (read; replayed, `ALL OK`). **At source (this audit):** MPRRS arXiv:1702.01003v5 (PDF fetched through WebFetch from `https://arxiv.org/pdf/1702.01003v5`, text extracted locally with pypdf; margin stamp "arXiv:1702.01003v5 [math.CO] 19 May 2019"): conventions p. 3, notation for \(\lesssim\) p. 4, energy definitions pp. 10–11, Lemma 32 p. 41, Lemma 33 p. 42, Theorems 34–35 p. 43, Theorem 37 with its proof p. 45, Corollary 38 p. 46. Shkredov arXiv:1802.09066v2 (stamp "2 Mar 2018"), Lemmas 42–43 pp. 32–33. Hanson–Petridis arXiv:1905.09134v3 (for NC). Not re-read: Rudnev–Shkredov–Stevens, MSS (read at source by the Round 189 audit), Shkredov 2106.09615, Rudnev–Shkredov 1812.01671, Lund–Pham–Vinh, Kerr, the Stepanov-type subgroup papers, and Shkredov 2013 (the source of Theorem 34).

### 2.1 Theorem 37 at source (check 1)

- **Verbatim (p. 45, pypdf text):** "Theorem 37. Suppose A ⊂ F such that |AA| = M|A| and |A| ≤ p^{13/23}M^{10/23}. Then for any α ∈ F∗ one has E×(A + α) ≲ M^{33/13}|A|^{32/13}." Followed by: "Note that 32/13 = 5/2 − 1/26, so for M sufficiently small, this improves the bound E×(A) ≪ M^{3/2}|A|^{5/2} provided by Lemma 33." **Matches the report's quote** (the report's reading that "E×(A)" in the remark means \(E^\times(A+\alpha)\) is right: Lemma 33 bounds \(E^\times(A+\alpha,B)\)).
- **What \(\mathbb F\) is (p. 3):** "Let F be a field. We assume throughout that F has positive characteristic p, let F_p denote the corresponding prime residue field and F_q the field with q elements and characteristic p." So \(\mathbb F\) is any field of characteristic \(p\); the size condition is in terms of the characteristic. \(\mathbb F=\mathbb F_p\) is included.
- **What \(\lesssim\) hides (p. 4):** "by f ≲ g we mean that there is a constant C > 0 such that f ≪ (log g)^C g". In the proof, Theorem 34 gives \(D_1^{6/13}D_2^{2/13}|A|^{32/13}\log^{12/13}|A|\) with \(D_1=M^5\log|A|\), \(D_2=M^{3/2}\), so the hidden factor is \((\log|A|)^{18/13}\) times an absolute constant (my Part A). The report's "(log N)^{O(1)}" is correct; the exact power is 18/13.
- **Energy (pp. 10–11):** \(E(A,B)\) is defined for finite sets in an abelian group; \(E^\times\) is the multiplicative version, and Theorem 34 is applied "where G is the multiplicative group F∗". So \(A+\alpha\subset\mathbb F^*\) is needed, which is why the report removes \(1\) from \(I\) when \(\alpha=-1\).
- **Shkredov arXiv:1802.09066v2, p. 33 (verbatim):** "Lemma 43 Let A ⊆ F_p be a set and |AA| = M|A|, |A| ≤ p^{13/23}M^{10/23}. Then for any α ∈ F∗_p one has E×(A + α) ≲ M^{33/13}|A|^{32/13}." Introduced (p. 32) by "We need two lemmas from [36, Section 4.5]." His convention: "signs ≲, ≳ mean some powers of logarithm of |A|". **Matches the report.** It is a restatement by an author of MPRRS, not an independent proof.

### 2.2 Application to symmetric geometric progressions (check 2)

- \(I=\{\gamma^{2k}:|k|\le K\}\subset Q\), \(N=|I|=2K+1\) (distinct when \(\operatorname{ord}\gamma^2>2K\)), \(II\subseteq\{\gamma^{2j}:|j|\le2K\}\), \(|II|\le2N-1\). Take \(A=I'=I\setminus\{1\}\): \(|A|=N-1\), \(|AA|\le|II|\le2N-1\), so \(M\le(2N-1)/(N-1)=2+O(1/N)\). \(\alpha=-1\in\mathbb F_p^*\), \(A+\alpha=I'-1\subset\mathbb F_p^*\).
- Size: \(|A|\le p^{13/23}M^{10/23}\) holds since \(M\ge1\) and \(N\asymp\sqrt p\le p^{13/23}\) for large \(p\).
- \(E^\times(I-1)\le E^\times(I'-1)+O(N^2)\) (solutions of \(x_1x_2=x_3x_4\) with a zero coordinate). Also, by the Round 189 audit §2.4, \(X(\mathbf 1_I)\le E^\times(I-1)\). **ACCEPTED.**
- Non-subgroup progressions: only \(|AA|\ll|A|\) is used. **ACCEPTED.** The hypothesis is about the set, not its law, so it applies to every symmetric GP in \(Q\) of length \(\le p^{13/23}\).

### 2.3 Internal constraints of the proof (check 3)

I re-derived each condition from the printed proof (p. 45) and Lemmas 32–33 (pp. 41–42):

| Step | Condition used | At \(|A|\asymp\sqrt p\), \(M=O(1)\) |
|---|---|---|
| Lemma 32 (\(D_1=M^5\log|A|\)) | \(|AA|\le p^{2/3}\); the proof writes "whenever \(|A|<p^{2/3}/M\)" | \(2N\le p^{2/3}\): holds |
| WLOG on \(B\) (Theorem 34 needs \(E(A,B)\le D_2|A||B|^{3/2}\) only for \(|B|\le4|A|^4/E\)) | if \(E<4M^{33/13}|A|^{32/13}\) nothing to prove; else \(|B|\le|A|^{20/13}M^{-33/13}\) | exact (Part A) |
| Lemma 33, first condition | \(|A||AA||B|=M|A|^2|B|\le p^2\Leftarrow|A|^{46/13}M^{-20/13}\le p^2\iff|A|\le p^{13/23}M^{10/23}\) | exact (Part A); holds |
| Lemma 33, second condition | \(\max(|AA|,|B|)\le(|A||AA||B|)^{1/2}\iff M\le|B|\le M|A|^2\) | **not addressed in the printed proof.** Upper end: \(|B|\le|A|^{20/13}\le|A|^2\). Lower end: for \(|B|<M\), \(E^\times(A+\alpha,B)\le|A||B|^2\le M^{1/2}|A||B|^{3/2}\le D_2|A||B|^{3/2}\). So the gap is harmless (auditor's step). |
| Consistency remark | new bound beats Lemma 33 only if \(M<|A|^{1/27}\); there \(p^{13/23}M^{10/23}\le p^{2/3}/M\) | \(27/26\) vs \(1/26\): exact; holds |
| Theorem 34 output | \(M^{5\cdot6/13+(3/2)\cdot2/13}=M^{33/13}\), log power \(18/13\) | exact |

The report's own table of internal constraints (script lines "46/13·1/2 ≤ 2", "1/2 < 2/3") is correct; it omitted the second condition of Lemma 33 (correction (ii) above). Theorem 34's source (Shkredov 2013) was not read by the report or by me; Theorem 37 is a refereed published theorem (Mathematika 65 (2019)) and its proof was not re-verified beyond these conditions.

### 2.4 Consequences (checks 4–5)

- **\(E^\times(I-1)\ll|I|^{32/13}(\log|I|)^{18/13}=p^{16/13+o(1)}\). ACCEPTED.** \(32/13=5/2-1/26\), \(16/13=5/4-1/52\) (exact).
- **The Round 189 obstruction.** Round 189 Cor. 3.1 is an implication: a uniform admissible-only \(T_0\le Cp^{5/4-\delta}\) (or \(X\le\)) gives \(X(\mathbf 1_I)\ll|I|^{5/2-2\delta}\). For \(\delta\le1/52\) that conclusion is now a known theorem (up to logarithms), so the sector family is **no longer an obstruction** in that range. Below, i.e. for \(T_0\le p^{16/13-\delta'}\), it still requires \(E^\times(I-1)\ll|I|^{32/13-2\delta'}\), beyond the published bound. In covariance units the obstruction threshold moves from \(7/4\) to \(1/2+16/13=45/26=7/4-1/52\). **ACCEPTED WITH CORRECTION:** this weakens the obstruction; it does not show that admissible-only arguments reach \(45/26\le\) covariance \(<7/4\), and it does not bound \(T_0(g_J)\) for interval laws from above (the law \(g_J\) is a Fejér kernel, not \(\mathbf 1_I\)). The report says "a re-statement of the Round 189 cap with an updated literature input, not a new cap theorem", which is the right reading.
- **Nothing on the actual law.** The unconditional one-match exponent stays 43/24. **ACCEPTED.**

### 2.5 "Rounds 186–189 missed it" (check 6)

- `grep` over `research/`, `coordination/`, `docs/` (excluding Round 190 files): "Theorem 37", "32/13", "33/13" and "1802.09066 Lemma 43" do not occur before Round 190. Round 186 (`…sup-c-heavy-price-186.md`:262–270) read MPRRS at source for Lemma 33 only; Round 186 cites Shkredov 1802.09066v2 Lemma 12 (an incidence bound), not Lemma 43; the Round 186 audit lists 1802.09066 as "not fetched"; Round 189 (report and audit §2.6) quote Lemma 33 and state "known only at \(|I|^{5/2}\)". The Round 189 audit's own literature check (mine, limited, as it said) missed Theorem 37. **ACCEPTED.** The statements "known only at \(|I|^{5/2}\) (MPRRS Lemma 33)" in the Round 189 report, audit, acceptance and checkpoint are out of date.

### 2.6 Partial-product graphs (check 7)

- Theorem 37 needs \(|AA|=M|A|\) for the whole product set. Lemma 32's proof builds the point set \(P=(AA\cup-\alpha A)^2\) and Lemma 33's bound is in \(|AA|\). For a graph \(\Gamma\subseteq A\times A\) with small partial product set \(\{ab:(a,b)\in\Gamma\}\), neither applies. **ACCEPTED.** Round 189's half-structured Cauchy–Schwarz row (which would need such a graph version) is not repriced. No graph version was found by the report; I did not search further.

### 2.7 Literature coverage

- I ran one independent web search for later improvements of the shifted energy for sets with few products; it returned nothing beyond the report's list (Warren 1812.01981, MSS, RSS 1607.05053, Zhelezov) and an unrelated 2026 paper (arXiv:2602.01781, energy distributions; abstract has no such bound). This is a spot check, not a survey. The report's Semantic Scholar screen of 68 citing papers is the main coverage; I did not repeat it.
- The report's answer to (b) "Stepanov-type or character-sum bounds for shifted short GPs" concerns energy and fibre counts. It does **not** cover character sums \(\sum_{k\le M}\chi(\zeta^k+a)\) (NC's (GP-Sub)). That question is still unasked (§6.3, call 3).

## 3. Report STOCK: `native-claude-ordinary-obligation-map-stocktake-190.md`

**Sources checked.** The full report and mission; `paley-190-stock-exponents.py` (read; replayed). Re-read at source: R162 `ordinary-physical-slope-fiber-count-162.md` lines 1–45; R164 `ordinary-physical-pair-slope-pinning-164.md` lines 45–56; R166 `ordinary-regular-character-collisions-166.md` lines 1–55; R172 `ordinary-full-diagonal-affine-172.md` lines 1–40; R178 `ordinary-parabolic-row-mean-square-178.md` lines 1–40; R180 `ordinary-paired-J-cross-ratio-180.md` lines 1–90; R152 `ordinary-affine-correlations-152.md` lines 60–70; R154 `ordinary-lift-and-gauss-kernel-154.md` lines 90–95; R160 `ordinary-matched-physical-truncation-160.md` lines 20–45; R163 `ordinary-shifted-layer-energy-saving-163.md` lines 60–70; R159 lines 95–102; R183 `native-claude-ordinary-prime-first-mass-fibre-dilation-183.md` lines 105–130; R184 SRM lines 120–140; the `proof_scope`/`failed_paths` entries of acceptance records 162–166 and 183–189. Every "acc:N" line I spot-checked (R152:152, R154:155, R164:194, R164:206, R166:207, R168:209, R179:248, R180:253, R183:262, R183:264, R184:271, R187:272, R187:277, R188:275) carries the quoted content. Not re-verified: the history of one-match and diagonal exponents (R171–R186), R168's Katz normalisation, R182 acc:260 (\(\mathcal M_w\le(X-\mathrm{diag})/4\), taken as cited).

### 3.1 The headline composition B1 / L3 (check 1), line by line

Setting (R162:3–5, 23–27): a block fixes vertex level sets \(\mathcal A\) (for \(A_x,A_y\)) and \(\mathcal B\) (for \(C_x,C_y\)), a slope set \(D\subseteq Q\setminus\{1\}\) on the favorable sign, and sums the five-factor physical sum over contributing triples \((x,y,u)\). Fixed squared thresholds mean \(g\ge a\) on \(\mathcal A\) and \(g\ge b\) on \(\mathcal B\) (this is the reading under which R166:9 has the factor \((a^2b^2)^{-1}\)).

1. **R162:23–27.** Bounding the four vertex amplitudes by \(|f|\le1\) and grouping triples by their slope: \(|\text{block}|\le\sum_{t\in D}|f(t)|\,N_t\), \(N_t\) = number of contributing triples with slope \(t\). (R162 states the two consequences \(\min(|\mathcal A|^2,|\mathcal B|^2)\sum_D|f|\) and \(|\mathcal A||\mathcal B|\min(\cdot)\,m_D\); the displayed inequality is the step before both. R164:47–54 states it with the pinned count.) **Correct.**
2. **R166:9.** Each contributing triple has \(g(A_x)g(A_y)\ge a^2\) and \(g(C_x)g(C_y)\ge b^2\), so it contributes at least 1 to \((a^2b^2)^{-1}\times\)(its four-\(g\) weight). \(P_t\) sums that nonnegative weight over \(u\in Q\setminus\{1\}\) and the full \(z\) at slope \(t\), i.e. over a superset of the contributing triples (completion only adds nonnegative terms; the possible added physical zeros are removed at pointwise \(O(\sqrt p)\), R166:11). So \(N_t\le(a^2b^2)^{-1}P_t\). **Correct.**
3. **R166:44.** On \(D\subseteq\{s_0\le g\le s_1\}\): \(w(t)=g(t)(1-g(t))\ge s_0(1-s_1)\), and \(|f(t)|\le\sqrt{s_1}\le1\).
4. **Composition.** Since \(P_t\ge0\) and \(w\ge0\) everywhere,
\[
|\text{block}|\le\frac{\sqrt{s_1}}{a^2b^2}\sum_{t\in D}P_t\le\frac{\sqrt{s_1}}{a^2b^2\,s_0(1-s_1)}\sum_{t\in D}w(t)P_t\le\frac{\mathcal M_w}{a^2b^2\,s_0(1-s_1)} .
\]
5. **Same \(P\).** R172:3 defines the diagonal with "the genuine completed nonnegative majorant \(P_s\) of Round 166 … Keep the actual physical mark and the square restriction"; R178–R180 and R187 use that \(P_s\) (chart form). Any difference between the R166 majorant and the chart form is an endpoint correction priced at pointwise \(O(\sqrt p)\) (R166:11; R172:21, 39); on a fixed band \(|D|\le G/s_0=O(\sqrt p)\), so it adds \(O(p)\) to \(\sum_{t\in D}P_t\). The composition is insensitive to it.

**Verdict B1: ACCEPTED** (agent bookkeeping, now audited): for every fixed \(0<s_0\le s_1<1\), \(a,b>0\), \(|\text{block}|\le C_{a,b,s_0,s_1}\mathcal M_w+O_{a,b,s_0}(p)\). Hence \(\mathcal M_w=O(p)\), with no logarithm, gives every fixed moderate block \(O(p)\), without the one-match, zero-match, \(\mathcal D\) or J obligations. **B2** (\(X=O(p)\Rightarrow\mathcal M_w=O(p)\) via \(\mathcal M_w\le X/4\)) **ACCEPTED** as cited. It is not deep: R166:27 already uses the first moment \(\sum_{t\in D}P_t\) implicitly (C-S over \(|D|=O(\sqrt p)\)), and R162/R165 phrase cuts in first-mass form; what is new is the observation that the \(w\)-weighted first mass is the weakest closing form, and that one-match is therefore not on the critical path.

### 3.2 Necessity of one-match; the \(\mathcal D\) decomposition (check 2)

- R166:40, 50–54: \(P_t-P_{\rm gen}(t)=O(\sqrt p)\) for \(t\ne1\), and \(\sum_tw|P_{\rm gen}|^2\) equals the \(\ell\)-weighted quadratic form exactly. Then \(\mathcal D=\sum w|P_{\rm gen}|^2+\text{cross}+O(\sqrt p)^2\sum w\), with \(|\text{cross}|\le2\,O(\sqrt p)(\sum w)^{1/2}(\sum w|P_{\rm gen}|^2)^{1/2}=O(p^{3/4}\mathcal D_{\rm gen}^{1/2})\) and the last term \(O(p^{3/2})\). R167 splits the form by matching numbers (≥2 classes \(O(p^{3/2})\), deletions \(O(p^{3/2})\)); R168: one-match \(=(p^3/m)\mathcal P_1+O(p^{3/2})\), \(\mathcal P_1\ge0\). So \(\mathcal D=O(p^{3/2})\iff\text{one}+\text{zero}=O(p^{3/2})\) (given the other pieces), and one \(\ge-O(p^{3/2})\). **ACCEPTED.**
- "One-match \(O(p^{3/2})\) is not necessary" is correct in two senses: (a) formally inside the split route (zero match is unsigned); (b) structurally, because the first-mass route bypasses \(\mathcal D\). Sense (a) has no content in practice (no mechanism for a negative zero-match class); sense (b) is the real finding. R173's word "necessary" is inaccurate; R178's "sufficient" is right. **ACCEPTED.**

### 3.3 Current values and the zero-match bookkeeping (check 3)

- One-match \(p^{43/24+o(1)}\) (R187), \(\mathcal D\) \(p^{9/4}\) (R179), \(\mathcal M_w,X\) \(p^{4/3+o(1)}\) (R187 Cor. 4), \(\mathcal D_0+\mathcal D_1\) \(p^{2399/1280}\) (R180), \(\mathcal D_J\) \(p^{15/8}\) per class (R180): **ACCEPTED** (cited lines checked).
- **B3** \(-O(p^{43/24+o(1)})\le\text{zero}\le O(p^{9/4})\): from \(\sum w|P_{\rm gen}|^2\le2\mathcal D+O(p^{3/2})\), one \(\ge-O(p^{3/2})\), ≥2 classes \(O(p^{3/2})\), and the one-match upper bound. **ACCEPTED** (bookkeeping).
- Katz-implied \(p^{5/2}\): accepted as bookkeeping; not re-derived from R168's normalisation.
- **B5** R179 majorant floor \(p^2\): \(\sum_hm(h)^3\ge(\sum_hm(h))^3/(p(p-1))^2=(p-1)G^6/p^2\asymp p^2\). **ACCEPTED.**
- **B6** \(W=G-\Gamma_{\rm tot}\ge(\frac12-o(1))\sqrt p\) on (NC). **ACCEPTED.** Wording: it shows the *target conversion* \(\mathcal M_w=O(p)\Leftarrow\mathcal D=O(p^{3/2})\) is exact in order; whether the actual \(\mathcal D\) is close to \(\mathcal M_w^2/W\) depends on how flat \(P\) is on \(\operatorname{supp}w\).

### 3.4 Ranking (check 4)

Re-derived in exact Fractions (my Part A; the report's script prints the same table): one-match gap \(7/24\) (cov) \(=7/48\) (fm); \(\mathcal D\) and \(\mathcal D_{\rm gen}\) \(3/8\) (fm); \(\mathcal M_w\), \(X\) \(1/3\) (fm); \(3/8-1/3=1/24\). **ACCEPTED as arithmetic.** Two cautions for the coordinator: the gaps compare *current bounds*, not difficulty; and the \(\mathcal M_w\) bound \(p^{4/3}\) sits at its accepted method cap (R187 acc:277), while the R179 diagonal route floors at \(p^2\) (B5). So the first mass is "closest" in exponent and also the only route without a known structural floor above the target, but its known obstructions (below) are of the same kind as for \(T_0\).

### 3.5 Missing assembly (check 5): does it lose powers?

Yes, under the bounds as stated. This is the most important correction in this audit.

- **What every route proves.** L2's necessary condition is "fixed moderate block \(=O_{a,b,s_0,s_1}(p)\) for every fixed thresholds". All routes in the map (one-match + zero, \(\mathcal D\), J split, \(\mathcal M_w\), \(X\), \(T_0\)) reach the favorable off-diagonal only through the R166 majorant on a fixed block, i.e. with the constant \((a^2b^2s_0(1-s_1))^{-1}\).
- **What is already paid** (R160:27–38; R162; R163:60–66; R164:54): vertex sites with \(|F|\le C/\sqrt p\); quadratically small pair cuts (both pairs with an \(O(1)\)-counting-norm factor); slope bands \(g\le p^{-\sigma}\) with \(\sigma\ge1-2\gamma\) (or \(\ge26/27\), etc.), **each at fixed vertex thresholds**.
- **What is not.** (i) Slope bands \(p^{-(1-2\gamma)}<g<s_0\): on \(g\asymp p^{-\sigma}\), \(|f|\asymp p^{-\sigma/2}\) and \(w\asymp p^{-\sigma}\), so step 4 gives \(|\text{band}|\le(a^2b^2)^{-1}p^{\sigma/2}\mathcal M_w\): with \(\mathcal M_w=O(p)\) this is \(p^{1+\sigma/2}\), a **power loss** up to \(p^{1/2-\gamma}\). The \(\mathcal D\) route loses the same \(p^{\sigma/2}\) (C-S on the band). (ii) Near-unit slopes \(g\to1\), \(t\ne1\): the factor \(1/(1-s_1)\) is unbounded; R159:100 says its quantitative bound "does not control \(S_{\rho,1}\) at the required \(O(p)\) scale". (iii) Vertex layers between \(C/\sqrt p\) and fixed thresholds: the factor \((a^2b^2)^{-1}\) grows up to \(p^{O(1)}\), because R166:9 counts a contributing triple through its four \(g\)-weights at the cost \(1/a\) (resp. \(1/b\)) per vertex (keeping the true amplitudes \(|f|=\sqrt g\) instead would cost \(a^{-1/2}\) per vertex, still unbounded as \(a\to0\)); and R160's deletion device only removes squared mass \(o(D)\) (the slowly diverging lower bound), far less than the \(\asymp\sqrt p\) squared mass of a layer \(\{g\le a\}\).
- **Consequence.** \(\mathcal M_w=O(p)\) (or \(X=O(p)\), or \(\mathcal D=O(p^{3/2})\)) closes every fixed block; it does **not** close the target as stated. The target needs, in addition, a uniform estimate that pays the growing slope bands, the near-unit slopes and the low vertex layers at \(O(p)\) in total (a dyadic decomposition into \(\gg1\) pieces each \(O(p)\) already fails, since the top-level \(O(p)\) has no logarithmic slack). A natural uniform form is a first mass with the true weights kept, e.g. \(\sum_{t\ne1}|f(t)|\,P^{(1/2)}_t=O(p)\) with \(P^{(1/2)}\) built from \(|f|\) rather than \(g\) at the four vertices; this is stronger than \(\mathcal M_w=O(p)\) and its size is unknown. Whether the top-level contradiction can instead be closed with fixed blocks plus an \(O(p)\) bound on the complement (without rate) is the open assembly question. STOCK §6.2 states the gap correctly; its §0.3, §4 column "closes alone? yes" and §8 should be read as "closes the fixed block".
- **This is not new to the project** (R163:66 "leaves fixed moderate slopes and the uncut ordinary target open"; R164 acc:206), but no acceptance record carries it as a named obligation. It applies equally to the one-match route. I record it in §6.2 as obligation (A).

### 3.6 Smaller claims (check 6)

- **B4.** \(\mathcal D_0+\mathcal D_1\le4R_*\mathcal M_w\) (R180:51) with \(R_*=O(p^{1/2-1/1280})\) (R173, R180:42) and \(\mathcal M_w\ll p^{4/3}(\log p)^{32/3}\) (R187): \(1/2-1/1280+4/3=7037/3840\) (exact). \(\mathcal D_J\le2G\mathcal M_w\ll p^{11/6+o(1)}\). **ACCEPTED** (bookkeeping). Still above \(3/2\); and \(\mathcal D_{\rm gen}\) does not sum.
- **P6(c)** subgroup obstruction for \(\mathcal M_w\): R183 Prop. C gives \(\mathcal M_w(g_H)=\frac3{4096}E_{\rm off}(H)\) exactly, so an admissible-only proof of \(\mathcal M_w=O(p)\) must give \(E_{\rm off}(H)=O(p)\) log-free for subgroups \(|H|\le2C_{\rm cap}\sqrt p-1\); MSS Cor. 4.1 gives \(|H|^4/p+O(|H|^2\log|H|)\). **ACCEPTED** (a logarithmic obstruction; the \(g_H\) law is not near-critical).
- **P7(d)/P8(d)** status lines: "below \(p^{5/4}\) … need (GP)" and "The obstruction uses MPRRS Lemma 33" are out of date after GPLIT (threshold \(p^{16/13}\)). Correction only.
- **STOCK §6 item 4** (whether the interval family obstructs \(\mathcal M_w\)): open, agreed. A restriction argument as in R189 Prop. 3(b) needs \(w(b/b')\ge c\) on the restricted fibres, i.e. \(g\le1-c\) there; for the Fejér law \(g\to1\) near \(k=0\), so it is not automatic. This is my call 2 (§6.3).

### 3.7 On the verdict

"Yes, with qualifications" is right in the mission's sense (structural slack: one-match is not on the critical path; the first mass is a weaker closing form), **with the correction** that "closing" means closing the fixed moderate block, and that the uncut target needs an unrecovered assembly that loses powers under every bound in the map. The report's honest conclusion, that the first-mass route "changes which statement must be proved, not how hard it is in kind", stands.

## 4. Report NC: `native-claude-ordinary-nc-excludes-sector-laws-190.md`

**Sources checked.** The full report and mission; the three scripts (read; all replayed). Re-read: Round 20 `anchored-repair-20.md` lines 1–16 and 60–80 (definition \(L=P-\ell\ell^{\mathsf T}/\kappa\), the gap theorem and flattening); Round 151 `ordinary-prime-coset-spread-151.md` lines 38–48 (\(I-\rho K=2P_\sigma+J\), coset mass); Round 183 row-deleted report lines 47–92 ((NC) definition, Prop. 1.2); Round 184 support-energy report lines 30–45 (\(k\), \(K\)); Round 184 SRM lines 120–140 (Prop. 2); acceptance `proof_scope` entries 183–189 mentioning (NC). Hanson–Petridis at source (below).

### 4.1 Lemma 1 (check 1)

- **Sign convention.** Round 20 writes \(2P=I-J-\sigma K\) for the projection it calls \(P_{-\sigma}\); Round 151/183 write \(I-\rho K=2P_\sigma+J\) with \(\rho=-\sigma\). These agree: the subscript convention is \(P_s=(I-J+sK)/2\). NC uses \(P_\sigma=(I-J-\rho K)/2\), consistent with the (NC) definition of Round 183 (line 53). (The Round 184 support-energy report's paraphrase "\(\sigma Ke=e+o(1)\)" uses Round 20's sign label; with Round 183's labels it reads \(\rho Ke=e+o(1)\), i.e. \(g\) concentrated on \(T_\rho\), consistent with Round 183 Prop. 1.2 and with NC.)
- **Proof re-derived.** \(K\) is multiplication by \(s\) in \(x\)-space, \(J\) by \(\mathbf 1_{x=1}\); so \(P_\sigma\) is multiplication by \((1-\mathbf 1_{x=1}-\rho s)/2\), which is 0 at \(x=1\) and on \(T_\rho\) and 1 on \(T_{-\rho}\). \(P_\sigma\) is an orthogonal projection, so \(P_\sigma-\ell\ell^{\mathsf T}/\ell_0\) projects onto \(\operatorname{im}P_\sigma\cap e_0^\perp\) (\(\langle v,\ell\rangle=v_0\) for \(v\in\operatorname{im}P_\sigma\)); \(v_0=\frac1n\sum_x\hat v(x)\), so in Fourier space it subtracts the mean on \(T_{-\rho}\). With \(\hat b=nrf\) and Parseval for the normalized norm, \(\|L_\sigma b\|_{2,n}^2=r^2V_{-\rho}\) and \(\|P_\sigma b\|_{2,n}^2=r^2G_{-\rho}\). The latter is consistent with Round 183 Prop. 1.2's \((2\|P_\sigma b\|^2+r^2)/\|b\|^2=(2G_{-\rho}+1)/G\) (so the normalized reading of \(\|\cdot\|_{2,n}\) is the accepted one). Step 5: \(\mathbf 1_{T_{-\rho}}=(1-\mathbf 1_{x=1}-\rho s)/2\) on \(Q\), \(|\sum_Qs\psi^j|=\sqrt p|k(j)|\le\sqrt p\), \(\nu_0=0\). Step 6 uses \(|T_{-\rho}|\ge(p-5)/4\). **ACCEPTED.**
- *Replay (my Part B):* \(L\) built literally from Round 20's formula with \(P=(I-J-\rho K)/2\), \(K=(1/n)\Psi\,\mathrm{diag}(s)\Psi^*\); \(\|Lb\|^2/r^2=V_{-\rho}\) and \(\|Pb\|^2/r^2=G_{-\rho}\) to relative error \(<10^{-10}\), \(p\in\{13,\dots,109\}\), both signs; the diagonal multiplier of \(P\) is \(0\) on \(\{1\}\cup T_\rho\) and \(1\) on \(T_{-\rho}\). The report's own `--check` also passes (\(p\le197\)).

### 4.2 Theorem 1 (check 2)

- (1) \(\sup_{T_{-\rho}}g\le(V^{1/2}+|\bar f|)^2\) with \(|\bar f_{-\rho}|\le2(\sqrt p+1)/(p-5)\): correct. (2) \(G_{-\rho}=V+|\sum_Tf|^2/|T|\le V+(\sqrt p+1)^2/(p-5)\to1\): correct; strictly stronger than Round 183's \(O(1)\), since (NC2) gives \(V\to0\) whereas Round 183 used only \(\|L_\sigma b\|\le Cr\). (3) Markov. (4) from (1), for **fixed** \(\tau\). **ACCEPTED.** "Sharp" refers to the field-general \(\mathbb F_{r^2}\) control (\(G_-\to1\)); not checked by me beyond the cited Round 184 Prop. 5(b).

### 4.3 Lemma 2, Corollary 1.1 and Hanson–Petridis (check 3)

- Lemma 2: \(x-x'=x(1-x'/x)\) with \(\chi(x)=1\); the injectivity of \((a,b)\mapsto a+\nu b\) (\(\chi(\nu)=-1\)) gives \(|I|^2\le p\); the converse uses \(\chi(1-\zeta^{-k})=\chi(1-\zeta^k)\) (\(\chi(-1)=1\), \(\zeta\in Q\)). **ACCEPTED.**
- Corollary 1.1: \(I I^{-1}\setminus\{1\}=\{\zeta^k:1\le|k|\le2K\}\) avoids 1 when \(\operatorname{ord}\zeta>4K\), and Theorem 1(4) puts it in \(T_\rho\). **ACCEPTED** (fixed \(\tau\)).
- **Hanson–Petridis at source** (arXiv:1905.09134v3, "6 May 2020", PDF via WebFetch, text extracted locally): "Corollary 1.5. Let p be a prime, d properly dividing p − 1 and suppose A ⊆ F_p is such that A − A ⊆ Z_d ∪ {0}. Then |A|(|A| − 1) ≤ d. In particular, for p ≡ 1 (mod 4), we have ω(G_p) ≤ (√(2p − 1) + 1)/2." The abstract states the cruder \(\sqrt{p/2}+1\). The report's quote from memory is **correct**. For \(\rho=-1\), apply it to \(\nu I\) with \(\nu\) a nonsquare. Corollary 1.5 also says the method "only works in prime fields". So (GP-Sub\(_c\)) holds for \(c>1/\sqrt2\) (an \(R\)-run gives a clique of size \(R+1\)).
- The exact-interval exclusion (by (A2): energy \(2/3>1/2\); by (A5): overlaps in \((\frac12,1)\)) **ACCEPTED**.

### 4.4 Proposition 2: subgroup laws (check 4)

\(f=((n/d)\mathbf 1_H-1)/(n/d-1)\) by orthogonality; \(G=n/(n/d-1)\), so (NC1) forces \(d\sim\sqrt p\); then \(S=H^\perp\setminus\{0\}\) is a subgroup of \(\mathbb Z/n\) minus a point, with energy ratio \(\to1>\frac12\), violating (A2) (Round 20 gap theorem: on (NC), \(\mathcal E(S)\le(\frac12+o(1))|S|^3\), either sign), and also (A6) and (A4). Item 4 (\(g\ge\tau\) on \(H\) forces a subgroup Paley clique; impossible for \(|H|>\sqrt{p/2}+1\)) and item 5 (MSS \(p\log p\)) correct. **ACCEPTED.**

### 4.5 Proposition 3: sector reduction of \(T_0\) (check 5)

\(\Delta(\lambda,0)\le c\) by Cauchy–Schwarz (\(r\mapsto\lambda r\) bijective); \(T_0=c+T_0^{(\rho)}+T_0^{(-\rho)}\) since \(g=0\) off \(Q\); \(T_0^{(-\rho)}\le G_{-\rho}c\) and \(\le\tau_p(X-c)\); \(c=\sum\mu^2\le\Gamma_{\rm tot}^2\le(\frac14+o(1))p\) on (NC) (the chart is injective in \((Y,D)\)). **ACCEPTED.** Correction to the remark "both \(Y,Y'\) of a heavy term may be taken heavy … Paley \(\rho\)-triangle": with a **fixed** height the Paley-triangle property holds (\(Y,Y'\in T_\rho\) by Theorem 1(4), \(\lambda=Y'/Y\in T_\rho\Rightarrow\chi(Y-Y')=\rho\)). At the heavy-triangle height \(p^{-1/24-\delta}\) Theorem 1(4) does not apply; only item (3) bounds the exceptions (at most \((1+o(1))p^{1/24+\delta}\) heavy points in \(T_{-\rho}\)). The report calls this "a structural restriction, not a power saving", which is right.

### 4.6 Theorem 4 and Corollary 4.1 (check 6), consequence by consequence

| Accepted (NC) consequence | Sector-free? | D\(_\theta\) (\(0<\theta<\frac12\)) | Audit |
|---|---|---|---|
| probability, \(\nu_0=0\), cap \(n\max\nu\le C\sqrt p\), \(\omega\ge0\), (H3) | yes | \(n/m\sim\sqrt p\); \(\nu\) real so \(g(1/x)=g(x)\); \(\omega=\frac12\nu*\check\nu\ge0\) | correct |
| (NC1) \(m_{\rm eff}/m_0\to1\), \(G\sim\sqrt p\) | yes | \(m_{\rm eff}=m=\mathrm{round}(m_0)\) | correct |
| (A1) flattening \(e=u_S+o(1)\), \(|S|\sim m_0\) | yes (without \(d_\rho(S)\to0\)) | exact | correct; \(d_\rho(S)\to0\) is the sector part and fails |
| (A2) R20 gap / R183 Prop. 1.4: \(\mathcal E(S)\le(\frac12+o(1))|S|^3\), \(\Gamma_{\rm tot}\le(\frac12+o(1))\sqrt p\) | yes | \(\mathcal E/m^3\to\frac23\theta\) (\(\le\theta\)); \(\Gamma_{\rm tot}=G\,\mathcal E/m^3\) | correct (Round 183 Prop. 1.1 identity) |
| (A3) R183 Prop. 1.2: \(G_{-\rho}=O(1)\), \(M_1=(1+o(1))p\) | **no** (sector) | fails (\(G_{-\rho}\approx G/2\), \(M_1\approx p/2\)) | correctly excluded from \(\mathcal H\) |
| R184 SRM Prop. 2: \(X\ge(2-o(1))p\), \(\max W\), \(\sup C\ge(1-o(1))p\) | **no**: proved from \(M_1=(1+o(1))p\) (SRM lines 130–140) | not required | **not listed by NC**; belongs with the sector forms in Cor. 4.1(iii) (correction (ii)) |
| (A4) R151 coset mass \(t_B\ge c_0\) | yes | \(\sum_Bg=O(1+c_2^2\theta^2)+o(\sqrt p)=o(G)\), so \(t_B\to1\) | correct (Dirichlet-kernel bound \(\min(1,n/(2L'|k|))\) summed over an AP of step \(\ge\sqrt p/(2c_2)\)) |
| (A5) R184 Lemma 0 / Theorem 2: dichotomy, \(H_*\), \(\max\hat g\le(\frac12+o(1))G\) | conclusions yes (Lemma 0's sector form is listed among (NC2) forms) | \(q_a\le\theta+o(1)<\frac12\), \(H_*=\{0\}\) | correct |
| (A6) R184 Prop. 4: no single coset of order \(\le(2-\delta)m_0\) | yes | \(\le1/\theta+1\) points of \(S\) per coset of order \(\le2m_0\) | correct |
| (NC2) \(V_{-\rho}\to0\) | sector | fails | by design |

- The concentration step (McDiarmid for uniform \(m\)-subsets with swap-Lipschitz constant \(O(1)\), union bound over \(n\) points and \(n\) shifts) is standard and gives \(\sup|f-(1+o(1))D_{L'}|=O(\sqrt{\log p/m})\) and overlaps \(\theta^2(L'-|a|)_++O(\sqrt{m\log p})\). Item 8: \(II^{-1}\subseteq\{|k|\le n/(2L')\}\) where \(F_{L'}\ge4/\pi^2\) (Round 189 Prop. 3(c), audited), so \(g\ge4/\pi^2-o(1)\); \(|I|\sim\theta\sqrt p/2\). Item 9 follows. **Theorem 4 ACCEPTED.**
- I found no other accepted, sector-free (NC) consequence in the `proof_scope` entries of Rounds 183–189 that D\(_\theta\) would violate. R183 Prop. 1.1 is an identity; R184 Prop. 5 concerns \(\mathbb F_{r^2}\); R184 Criteria C1/C2 are conditional.
- *Replay (my Part C, independent code):* D\(_\theta\) at \(p=1009,2017\), \(\theta\in\{0.25,0.4\}\): \(\mathcal E/m^3=0.24\)–\(0.31\), \(\min g\) on \(II^{-1}\) \(0.41\)–\(0.73\) (\(\ge4/\pi^2=0.405\)), coset counts \(\le3\); \(T_0\) and \(X(\mathbf 1_I)\) computed through a brute-force Round 189 chart: \(T_0/X(\mathbf 1_I)=5.5\), \(7.1\), \(29.6\), far above \((4/\pi^2)^5\approx0.011\). The maximal overlap at \(p=1009\), \(\theta=0.4\) is \(0.500\) (\(m=16\)): a finite-size fluctuation (the report notes the same at \(\theta=\frac12\)); Theorem 4 is asymptotic. The \(|I|\) here are tiny (5–9); this checks the inequality chain, not the asymptotics. The report's model table (\(p\le10^6\)) reproduces exactly.
- **Corollary 4.1 ACCEPTED WITH CORRECTION.** (i) is a correct implication. After GPLIT its *force* is: (NC)-non-sector arguments reaching \(T_0\) or \(X\le p^{16/13-\delta}\) must prove \(E^\times(I-1)\ll|I|^{32/13-2\delta}\); above \(p^{16/13}\) (covariance \(45/26\)) the D\(_\theta\) family is no longer known to obstruct. So (iii) should read "below \(45/26\)" (not "below \(7/4\)"). (ii) (\(\Gamma\) route cannot pass \(43/24\) from \(\mathcal H\)) is unaffected. Plus correction (ii) of the summary (list of sector forms).

### 4.7 Conditional criteria (check 7)

- **(GP-Sub\(_c\))** (no \(\zeta\in Q\), \(\operatorname{ord}\zeta>c\sqrt p\), with \(\chi(1-\zeta^k)\) constant for \(1\le k\le c\sqrt p\)) and **Criterion 5.1** (it excludes the interval family for fixed \(\tau\)): the implication is correct. **CONDITIONAL** on (GP-Sub\(_c\)) for all \(c>0\). Known for \(c>1/\sqrt2\) (HP Corollary 1.5, at source) and \(c>1\) (Lemma 2). For \(c\le1/\sqrt2\) it is a special case of "Paley cliques have size \(o(\sqrt p)\)" restricted to geometric progressions; I know of no result, and did not search. Completing the sum is trivial at \(M\asymp\sqrt p\), as the report says.
- **(GP-Sub\(_\kappa\))** and **Criterion 5.2**: the proof (\(p^\kappa\tau\le\sum_{P\cap T_{-\rho}}g\le G_{-\rho}\le1+o(1)\) with \(P=II^{-1}\), \(|P|\ge c_0\sqrt p\)) is correct. **CONDITIONAL.** With Theorem 37 in place of Lemma 33 the conclusion improves: the family no longer obstructs \(T_0\le p^{16/13-\delta}\) for \(\delta<5\kappa\) (equivalently \(T_0\le p^{5/4-\delta}\) for \(\delta<5\kappa+1/52\)). It removes an obstruction; it proves no bound, and lower-height sector laws on progressions longer than \(\sqrt p\) are not treated (the report says so).
- **The two statements are different from `cand:gp-shifted-energy`.** (GP) is an energy (incidence) bound for \(I-1\); (GP-Sub) is non-constancy of the Legendre symbol on \(1-I\). Neither implies the other.

### 4.8 Evidence (§7)

All quoted rows reproduced (identity check \(p\le197\); D\(_\theta\) rows at \(p=10009\)–\(1000033\); clique `--check`; `--list` at five primes; the \([10^3,2\cdot10^5]\) range: 8897 primes, per-range maxima 17/23, 23/29, 28/29, 28/33, ratio maxima 1.30/1.52/1.69/1.59, means 0.78/0.85/0.87/0.88). My Part D recomputes the generator maxima by plain-Python brute force at six primes and matches. Correction (iv): in the §7.2 table, "17 (≤0.283√p, at p=1013)" mixes the range maximum 17 (at \(p=8537\)) with the largest ratio \(R/\sqrt p=0.283\) (at \(p=1013\), \(R=9\)).

**Exactly what is proved (agent audit).** Lemma 1, Theorem 1, Lemma 2, Corollary 1.1, Propositions 2–3, Theorem 4, Corollary 4.1(i)–(ii) as implications, Corollary 4.1(iii) below \(45/26\). **Not proved:** any bound on \(T_0\), \(X\), \(\Gamma_{\rm tot}\); exclusion of the D\(_\theta\)-type laws on (NC); (GP-Sub) for \(c\le1/\sqrt2\).

## 5. Replay log

Run from the repository root on 2026-11-21 with `.venv/bin/python -B`. Outputs went to the session scratchpad. "Matches" means every quoted output line or table row appears in the run, timing text excepted.

| Script | Command | rc | Time | Result |
|---|---|---|---|---|
| gplit exponents | `research/paley-190-gplit-exponents.py` | 0 | <1 s | `ALL OK` (15 checks) |
| stock exponents | `research/paley-190-stock-exponents.py` | 0 | <1 s | table as in STOCK §4; "M_w from C-S on D: 11/8 … difference: 1/24"; "J classes … 7037/3840" |
| nc exponents | `research/paley-190-nc-exponents.py` | 0 | <1 s | `ALL OK` |
| nc identity | `research/paley-190-nc-identity.py --check` | 0 | 0.1 s | `PART A: ALL IDENTITY CHECKS OK` (rel. err \(\le2.7\cdot10^{-15}\)) |
| nc models | `research/paley-190-nc-identity.py 10009 40009 160001 640009 1000033` | 0 | 0.8 s | matches every §7.1 row |
| nc clique | `research/paley-190-nc-gpclique.py --check` | 0 | <1 s | OK |
| nc clique | `… --list 640009 1000033 4000037 10000121 30000001` | 0 | 5 s | matches (18/18/22/22/25) |
| nc clique | `… 1000 200000` | 0 | 58 s | 8897 primes; per-range maxima and ratios as in §7.2 (summarised by my own parse of the per-prime lines; the script prints per-prime lines and a global summary only) |
| audit | `research/paley-190-audit-check.py` | 0 | 2 s | `ALL AUDIT CHECKS OK` (41 checks) |

SHA-256 (as audited):
- reports: GPLIT `557777a493c1dcc5804540de7329c60a06217bbb6404c7713a3e11f230c53dd0`, STOCK `bced35fcbb697a9bf23e884de3a8c7686a6bf21fc409b6e57bef547f58442c8a`, NC `5081b11a0e05fadbed17d28e14f10535f0f603d2adb4520785ec77ccba60d817`
- scripts: `paley-190-gplit-exponents.py` `3462d89e…16b7` (matches GPLIT §6), `paley-190-stock-exponents.py` `0072e0c5…07e5` (STOCK prints no hash), `paley-190-nc-exponents.py` `4ff8df26…f2b6`, `paley-190-nc-gpclique.py` `05c798f6…1121`, `paley-190-nc-identity.py` `d2371d6a…651e` (all three match NC's table)
- mission source: `coordination/round-189.json` `8901a11c…ce822`, `research/round-189-acceptance.json` `ad4e0b5a…6506` (both match the missions)

External sources read at source by this audit (PDFs fetched through WebFetch, saved by the harness outside the repository, text extracted locally with pypdf; not saved in the repository): MPRRS arXiv:1702.01003v5; Shkredov arXiv:1802.09066v2; Hanson–Petridis arXiv:1905.09134v3 (and its abs page). PDF text extraction can garble formulas; the quoted statements were compared symbol by symbol with the reports' quotes and agree.

**Not checked:**
- GPLIT: the proof of Theorem 34 (Shkredov 2013) and of Lemma 33 ("implicit in" a cited reference); the other table rows (RSS, MSS, Shkredov 2106.09615, Rudnev–Shkredov 1812.01671, Lund–Pham–Vinh, Kerr, Stepanov-type papers); the report's citation-list screen.
- STOCK: the exponent histories (R171–R186); R168's Katz normalisation for the \(p^{5/2}\) zero-match value; R182 acc:260 (\(\mathcal M_w\le(X-\mathrm{diag})/4\)); the R152–R154 reduction itself (inherited); the identification of the R166 and chart forms of \(P_s\) beyond R172's statement and the \(O(\sqrt p)\) endpoint pricing.
- NC: the inherited (NC) inputs (Round 20 gap theorem, Round 151 coset mass, Round 184 Theorem 2 and Prop. 4) beyond their statements; the sharpness claim via Round 184 Prop. 5(b); D\(_\theta\) asymptotics beyond \(p\le10^6\) (models) and \(p\le2017\) (my chart replay); any literature on (GP-Sub).

## 6. Ranked closeout

### 6.1 What Round 190 changes

| Obligation | Before (Round 189 acceptance) | After Round 190 (as audited) | Effect |
|---|---|---|---|
| `cand:gp-shifted-energy` (GP) | "known only at \(|I|^{5/2}\) (MPRRS Lemma 33)"; admissible-only obstruction for \(T_0,X\le p^{5/4-\delta}\) (covariance 7/4) | **Known at \(|I|^{32/13}(\log|I|)^{18/13}\)** (MPRRS Theorem 37, Shkredov Lemma 43, both read at source); open below \(32/13\); target \(|I|^2\). The sector obstruction applies below \(T_0,X\le p^{16/13}\) (**covariance \(45/26=7/4-1/52\)**); between \(45/26\) and \(7/4\) it is no longer known to obstruct. | **weakened** (external input improved; no bound on the actual law) |
| One-match covariance | \(p^{43/24+o(1)}\); target \(O(p^{3/2})\), treated as a main ordinary obligation | **Exponent unchanged, 43/24.** Not on the critical path: it enters only the split route, and only through one + zero (zero match has no estimate). | **reformulated** (demoted) |
| First mass \(\mathcal M_w\) / \(X\) (`cand:slope-row-mass-x`) | \(p^{4/3+o(1)}\) against \(p^{1+1/1280}\) (for \(\mathcal D_0+\mathcal D_1\)) | **Value unchanged.** New role (audited bookkeeping B1): \(\mathcal M_w=O(p)\) log-free closes every **fixed** moderate block on its own (\(|\text{block}|\le\sqrt{s_1}(a^2b^2s_0(1-s_1))^{-1}\mathcal M_w+O(p)\)); \(X=O(p)\) implies it. Gap 1/3 (first-moment units), closest closing form. Admissible-only log-level obstruction (\(E_{\rm off}(H)=O(p)\) for subgroups); power-level (interval-family) obstruction for \(\mathcal M_w\) unknown. | **reformulated** (promoted to the weakest closing form) |
| \(\mathcal D_0+\mathcal D_1\); \(\mathcal D_J\) | \(p^{2399/1280}\); \(p^{15/8}\) per class | \(p^{7037/3840+o(1)}\); \(p^{11/6+o(1)}\) per class (bookkeeping with R187's \(\mathcal M_w\)); \(\mathcal D_{\rm gen}\le\mathcal D=O(p^{9/4})\) unchanged; R179 majorant floors at \(p^2\) | weakened (values), route dominated |
| Zero match | no exponent | \(-O(p^{43/24+o(1)})\le\text{zero}\le O(p^{9/4})\) (bookkeeping); only matters on the split route | evidence_only |
| **Assembly (new name)** | implicit ("uncut ordinary target open", R163/R164) | **Named obligation (A):** every route proves only fixed-block \(O_{a,b,s_0,s_1}(p)\); under \(\mathcal M_w=O(p)\) the growing slope bands lose \(p^{\sigma/2}\) (\(\sigma<1-2\gamma\)), near-unit slopes \(1/(1-s_1)\), low vertex layers \((a^2b^2)^{-1}\). | **new_obstruction** (to the reading "\(\mathcal M_w=O(p)\) closes the target") |
| (NC) structure | \(G_{-\rho}=O(1)\); obstruction status of (NC) unknown | Exact form of (NC2) (\(V_{-\rho}\to0\)); \(G_{-\rho}\le1+o(1)\), \(\sup_{T_{-\rho}}g\to0\); exact subgroup and interval laws excluded; \(T_0=c+T_0^{(\rho)}+O(p)\). **Method cap:** D\(_\theta\) laws satisfy every sector-free accepted (NC) consequence and carry the sector obstruction (below 45/26) and \(\Gamma_{\rm tot}\asymp\sqrt p\). So (NC)-based routes must use (NC2), which forces the obstruction onto geometric-progression Paley cliques; excluding them is (GP-Sub), open for \(c\le1/\sqrt2\). | **new_obstruction** (method cap for sector-free (NC) arguments) + reformulated |
| Cold line; the target | paused; open | unchanged | unchanged |

### 6.2 Precise remaining obligations

1. **(A) Assembly.** Show that the whole favorable Legendre off-diagonal (R154) is \(O(p)\) with no logarithm, given \(O(p)\) for every fixed moderate block and the paid cuts (R160, R162–R164); or identify the exact uniform estimate needed for the growing slope bands \(p^{-(1-2\gamma)}<g<s_0\), the near-unit slopes \(g\to1\) (\(t\ne1\)) and the vertex layers \(C/\sqrt p<|F|^2<a\). Under the current majorants it loses \(p^{\sigma/2}\), \(1/(1-s_1)\) and \((a^2b^2)^{-1}\). Unrecovered and not previously named.
2. **(F) Fixed moderate block**, weakest known closing form: \(\mathcal M_w=\sum_sw(s)P_s=O(p)\) with no logarithm (or \(X=O(p)\), or \(\mathcal D=O(p^{3/2})\)). Current \(p^{4/3+o(1)}\) (method cap of the extraction-plus-Young route). Admissible-only proofs must give \(E_{\rm off}(H)=O(p)\) log-free for subgroups \(|H|\le2C_{\rm cap}\sqrt p\) (known: \(p\log p\)). Whether the interval family forces (GP) for \(\mathcal M_w\) is open.
3. **One-match** \(O(p^{3/2})\): \(p^{43/24+o(1)}\); only useful together with zero match on the split route. Through Theorem A it follows from \(X=O(p)\), which already closes (F).
4. **`cand:gp-shifted-energy`**, re-recorded: "\(E^\times(I-1)\ll|I|^{32/13}(\log|I|)^{18/13}\) for symmetric geometric progressions \(I\subset Q\subset\mathbb F_p^\times\), \(|I|\le p^{13/23}\) (MPRRS arXiv:1702.01003v5 Theorem 37); open below \(|I|^{32/13}\) at \(|I|\asymp\sqrt p\) for non-subgroup progressions; \(|\Gamma|^2\log|\Gamma|\) for subgroups (MSS Cor. 4.1); needed for admissible-only (and sector-free (NC)) arguments below \(T_0,X\le p^{16/13}\) (covariance 45/26); the target needs \(|I|^{2}\) up to constants for sector-type pieces."
5. **(GP-Sub): recommend a new candidate**, `cand:gp-sector-constancy`, statement: "for every \(c>0\) and all large primes \(p\equiv1\bmod4\), no \(\zeta\in Q\) with \(\operatorname{ord}\zeta>c\sqrt p\) has \(\chi(1-\zeta^k)\) constant for \(1\le k\le c\sqrt p\) (GP-Sub\(_c\)); quantitative form (GP-Sub\(_\kappa\)): every symmetric progression \(\{\zeta^k:|k|\le M\}\subset Q\), \(c_0\sqrt p\le M<\operatorname{ord}\zeta/2\), has \(\ge p^\kappa\) points of each sign of \(\chi(1-y)\). Known for \(c>1/\sqrt2\) (Hanson–Petridis Cor. 1.5)." It is distinct from `cand:gp-shifted-energy` (character-sum constancy versus energy). It is touched by NC Criteria 5.1–5.2, Round 184 (Sub\(_C\)) and Round 184 Criterion C2's progression case. Recording it once is justified because two proposed calls below (a literature call and, conditionally, an (NC) pricing call) would need the same statement.
6. **(NC) lever.** Any (NC)-based route below 45/26 must use (NC2) (\(V_{-\rho}\to0\), or \(G_{-\rho}=O(1)\), \(M_1=(1+o(1))p\), \(d_\rho(S)\to0\), Round 184 Lemma 0) and an arithmetic input of (GP-Sub) type; (NC) has no rate, so any power saving must come from the arithmetic input.
7. **Cold.** Unchanged from Round 189 (signed mechanisms only; dispatch paused).
8. **Bookkeeping.** Record the GPLIT corrections (log power 18/13; Lemma 33's second condition; "cap moves" as a weakening; no height-1 use), the STOCK correction (fixed-block reading; assembly named), the NC corrections (threshold 16/13 in Cor. 4.1/Criterion 5.2; sector-form list; Paley-triangle remark at fixed heights; §7.2 cell). Update the Round 189 phrase "known only at \(|I|^{5/2}\)" wherever it is carried forward.

### 6.3 Recommended Round 191 calls (most valuable first)

**1. `ordinary-fixed-block-assembly` (structural; re-derivation plus elementary composition).**
- **Question:** From the accepted reduction (R152–R154 top level; R157 conditional lower bound; R159–R166 cuts and blocks), does \(O(p)\) for every fixed moderate block, together with the paid cuts, imply the \(O(p)\) favorable off-diagonal (or the contradiction on the critical branch, e.g. through the R157/R160 device that a cut keeps the lower bound \(\gg pD\) when the deleted squared mass is \(o(D)\))? If not, what single uniform estimate is needed for the slope bands \(p^{-(1-2\gamma)}<g<s_0\), the near-unit slopes and the vertex layers \(C/\sqrt p<|F|^2<a\), and does \(\mathcal M_w=O(p)\), \(X=O(p)\) or a weighted first mass with the true vertex amplitudes kept imply it?
- **Why now:** STOCK shows every ordinary route closes only fixed blocks, and this audit shows the assembly loses powers under every current majorant. Without it, retargeting Round 191+ to \(\mathcal M_w\) (or anything else) may aim at a statement that does not close the target.
- **Scope:** cite accepted statements by round and line; exact loss exponents; mark compositions as bookkeeping; no new incidence estimates; models only as evidence.
- **If yes:** \(\mathcal M_w=O(p)\) (or \(X=O(p)\)) is recorded as a genuinely sufficient ordinary target; the next call attacks it or its obstruction (call 2).
- **If no:** record (A) with its exact uniform form as a separate ordinary obligation; every fixed-block estimate round is then insufficient in principle until (A) is addressed.
- **If inconclusive:** the list of unassembled pieces with their exact loss exponents.

**2. `ordinary-first-mass-sector-obstruction` (method test; exact, cheap).**
- **Question:** For laws with \(g\ge\tau\) on \(II^{-1}\) (the Round 189 interval laws, and NC's D\(_\theta\)), is \(\mathcal M_w(g)\ge c(\tau)\,X(\mathbf 1_{I'})\) for a sub-progression \(I'\) of comparable length, so that admissible-only (and sector-free (NC)) arguments for \(\mathcal M_w\le p^{16/13-\delta}\) must prove \(E^\times(I'-1)\ll|I'|^{32/13-2\delta}\)? Or does the weight \(w(b/b')\) (small where \(g\approx1\), i.e. near \(k=0\)) remove the sector pieces?
- **Why now:** STOCK names \(\mathcal M_w=O(p)\) as the weakest closing form; whether a pivot to it is easier in kind than \(T_0\) hinges on exactly this. The fibre form \(\mathcal M_w=\sum_r\sum_{b\ne b'}\mu(r,b)\mu(r,b')w(b/b')\) (R183 Prop. A) makes it a restriction computation of the Round 189 Prop. 3(b) type.
- **Scope:** exact statements; fixed \(\tau\); \(w\) kept; models as evidence; cite R183 Prop. A/C, R189 Prop. 3, NC Theorem 4.
- **If yes:** \(\mathcal M_w\) meets the same (GP) wall as \(T_0\) and \(X\); record that the ordinary line below covariance-equivalent \(45/26\) needs (GP) or (GP-Sub) whichever form is targeted, and reduce ordinary estimate rounds.
- **If no:** a sector-free route for \(\mathcal M_w\) below \(p^{16/13}\) is not obstructed by sector laws; the next call prices \(\mathcal M_w\) on general laws with \(w\) kept.
- **If inconclusive:** the exact restricted energy that decides it.

**3. `ordinary-gp-sector-constancy-literature` (literature; quote at source; can run in parallel with 2).**
- **Question:** Is (GP-Sub\(_c\)) for some \(c\le1/\sqrt2\), or (GP-Sub\(_\kappa\)), known: nontrivial bounds for \(\sum_{k\le M}\chi(\zeta^k+a)\) (character sums with exponential functions, shifted geometric progressions) at \(M\asymp\sqrt p\) or below, bounds on Paley cliques that are geometric progressions or multiplicative Bohr sets, or a Stepanov/Hanson–Petridis argument adapted to progressions (`cand:gp-sector-constancy`)?
- **Why now:** NC proves that the sector condition is the only (NC) input that can see the obstruction family, and reduces its use to (GP-Sub); the Round 190 literature call covered energies, not character sums.
- **Scope:** verbatim statements with URL and version; hypotheses at \(M\asymp\sqrt p\), \(\zeta\) of order \(>4M\); primality; no new proofs; best known range and exact gaps.
- **If yes:** Criterion 5.1 (qualitative) or 5.2 (by \(p^{5\kappa}\)) becomes unconditional on (NC); the next call prices the non-progression part of \(T_0\) or \(X\) (or \(\mathcal M_w\)) on (NC).
- **If no:** record (GP-Sub) as an external open problem of Paley-clique type; retire the (NC) sector lever below 45/26.
- **If inconclusive:** closest results with exact gaps.

**Cold:** no call (unchanged from Round 189).

### 6.4 Routes to retire

- **One-match covariance as a standalone target** and its dedicated pricings (\(T_0\) heavy-triangle, three-pencil, further Theorem A refinements): it closes nothing without zero match, and \(X=O(p)\), which would give it, already closes the fixed block directly.
- **Zero-match estimation** and the **J-split / full-diagonal routes** (\(\mathcal D_0+\mathcal D_1\), \(\mathcal D_{\rm gen}\), R179 majorant, which floors at \(p^2\)): dominated by the first-mass form (C-S only loses).
- **Sector-free (NC) arguments** below 45/26 for \(T_0\), \(X\), and the \(\Gamma_{\rm tot}\) route from \(\mathcal H\) (NC Cor. 4.1).
- **Further general literature searches** for \(E^\times(A+\alpha)\) with \(|AA|\ll|A|\) beyond Theorem 37 (GPLIT's coverage is broad): record (GP) below \(32/13\) as an external open problem.
- **Subgroup laws as an obstruction** (excluded on (NC), and \(p\log p\) by MSS).
- Still retired from Round 189: coupled incidence pricings of \(T_0\) without a GP input (now below 45/26); cold per-simple sup-dominating prices; seed-rate re-certification.
- **Not retired:** \(\mathcal M_w\)/\(X=O(p)\) (pending calls 1–2); the (NC2) lever (pending call 3).

### 6.5 Strategic assessment (honest)

- **Should the project pivot to \(\mathcal M_w=O(p)\)?** Partly. Retargeting from one-match to \(\mathcal M_w\) (equivalently, from \(T_0\) to \(X\)) is correct bookkeeping: \(\mathcal M_w=O(p)\) is the weakest known form that closes a fixed block, and one-match closes nothing alone. But it is **not easier in kind**. (a) It is a sharp-order, logarithm-free statement: \(X\ge(2-o(1))p\) on (NC), \(\mathcal M_w\le X/4\), and floating evidence has \(\mathcal M_w/p\) flat, so there is no room for even a \(\log\). (b) The proved \(p^{4/3+o(1)}\) is at the accepted method cap of its route. (c) Admissible-only arguments already face a logarithmic obstruction (subgroup two-level laws need \(E_{\rm off}(H)=O(p)\), known \(p\log p\)), and very likely the power-level sector obstruction too (call 2), which would put \(\mathcal M_w\) behind the same (GP) wall: \(|I|^2\) needed, \(|I|^{32/13}\) known. (d) Even a proof would close only fixed blocks; the assembly (A) loses powers under the current majorants.
- **What Round 190 really changed.** The external wall moved slightly (\(5/2\to32/13\) in \(|I|\); \(7/4\to45/26\) in covariance), which confirms that the barrier is a recognised sum-product problem with a small known saving, not a missing citation. The (NC) lever reduces to a Paley-clique-type statement for geometric progressions. The stocktake removed one-match from the critical path and exposed the unnamed assembly obligation.
- **Realistic outlook.** For the ordinary target the project needs all of: (A) the assembly; (F) a sharp-order, log-free first-mass bound for the actual law; and, for any argument that cannot exclude sector-type laws, either a near-sharp shifted-GP energy theorem (\(|I|^2\) against the known \(|I|^{32/13}\)) or an (NC2)+(GP-Sub) exclusion. Each of the last two is at or beyond the frontier of current sum-product technology; (GP-Sub) is a special case of the Paley clique problem restricted to progressions, which may be more accessible but has no known handle below \(c=1/\sqrt2\). Incremental incidence pricing will not move the ordinary exponent in a way that changes this picture. The cold line is paused for an analogous reason.
- **Recommendation.** Spend Round 191 on the three cheap, decisive calls above (assembly first). If (A) turns out to lose powers irreparably, or call 2 shows \(\mathcal M_w\) is sector-obstructed **and** call 3 finds (GP-Sub) open, the coordinator should record the ordinary line as reduced to named external problems (`cand:gp-shifted-energy`, `cand:gp-sector-constancy`, plus (A)) and move to `decision: hold` for ordinary estimate rounds, as was done for the cold line, rather than run further method-cap rounds.

## 7. Status of this audit

This is an agent audit, not human acceptance or certification.

**What I checked:**
- GPLIT: Theorem 37, Lemmas 32–33, Theorems 34–35, Corollary 38 and the conventions of MPRRS arXiv:1702.01003v5 **at source**; Shkredov arXiv:1802.09066v2 Lemma 43 **at source**; every internal constraint of Theorem 37's proof at \(|A|\asymp\sqrt p\), including one the printed proof omits; the application to symmetric GPs; the 45/26 translation; the claim that Rounds 186–189 missed it (repository grep); the partial-product question.
- STOCK: the B1 composition line by line from R162, R164, R166, R172, R178, R180; the \(\mathcal D\) decomposition (R166–R168); every cited acceptance line listed in §3; B3–B6; the ranking and the J-class arithmetic in exact Fractions; the assembly question against R159, R160, R162–R164.
- NC: Lemma 1 (sign conventions of Rounds 20/151/183/184, normalisation, proof), Theorem 1, Lemma 2, Corollary 1.1, Propositions 2–3, Theorem 4 against each accepted (NC) consequence in Rounds 183–189's `proof_scope`, Corollary 4.1, Criteria 5.1–5.2; Hanson–Petridis **at source**; independent code for Lemma 1, D\(_\theta\) (including \(T_0\) and \(X(\mathbf 1_I)\) through a brute-force chart) and the progression runs.
- All report scripts replayed in full (§5).

**What I did not check:** listed under "Not checked" in §5.

**Files:** nothing was committed. Only this file and `research/paley-190-audit-check.py` were written. Replay outputs and the extracted PDF texts went to the session scratchpad.

Final SHA-256 of the audit script: `paley-190-audit-check.py` `8d536f09afb0529ce61149c0310866c94e55963c248df57bdcefbb1220d52988`.
