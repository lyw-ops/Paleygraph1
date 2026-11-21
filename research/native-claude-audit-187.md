# Independent audit of Round 187 (session/r187-audit)

- **Auditor:** Claude subagent started by the Round 187 coordinator (session/r187-audit). This is an agent audit, not human acceptance and not a mathematical certification. The auditor wrote neither report and is not the coordinator.
- **Status of this file:** written incrementally. The "Blind overlap review" section below was saved before any file under `coordination/shared-obligations/`, `coordination/drafts/` or any `coordination/round-*-inflight.json` was opened.
- **Read before the blind review:** `AGENTS.md`, `docs/WORKFLOW.md`, `docs/ROUND_REVIEW.md`, `coordination/checkpoints/round-186.md`, `research/native-claude-audit-186.md`, the two missions in `coordination/missions/round-187/`, and the two reports.

Verdict key (per claim the report labels as proved):
- **ACCEPTED:** correct as written, for the stated hypotheses.
- **ACCEPTED WITH CORRECTION:** true after the stated correction, which does not change the report's main conclusion.
- **CONDITIONAL:** correct given a named input that is not proved or not checked.
- **REJECTED:** false as written, or not supported.

Reports, abbreviated:
- **PAIR** = `native-claude-ordinary-prime-level-pair-energy-187.md` (one-match and side quantities; Lemma C, Lemma M′, Prop. P′, Theorems 1–2, Corollaries 3–4);
- **COLD** = `native-claude-cold-prime-b-word-delocalization-187.md` (sup/RMS ratio of B-generated Duhamel words; Prop. M, Theorem 1, Lemma 3, Prop. H, Prop. 6).

## 1. Blind overlap review

Written after reading the two reports and their missions. No shared-obligation, draft or inflight file had been opened.

| Pair | Classification | Reason |
|---|---|---|
| PAIR – COLD | **independent** | PAIR bounds point–line incidences and multiplicative pair energies of the ordinary weight \(g=|f|^2\) on \(\mathbb F_p\) (Stevens–de Zeeuw Thm 4, Lemma S1, Round 185 Lemma 5, the Round 178/180/184 chain). COLD studies sup/RMS ratios of the cold frozen-base Duhamel words on \(\mathbb Z/n\) (Criterion D of Round 180, the Round 179 compact transfer, a Haar-eigenbasis model, compact counting rates). No object, lemma, estimate, external theorem or script is common. Neither report cites the other or any input the other proves. |

- **No shared estimate.** The only common setting is \(p\equiv1\bmod4\), \(n=(p-1)/2\), the quadratic character. PAIR uses it only through \(\operatorname{supp}g\subseteq Q\); COLD uses the spectrum of \(K\).
- **Not duplicated.** Each call answered its own mission question.
- **Would an overlap review have changed dispatch?** No. Either outcome of one call leaves the other's question unchanged.
- **Touch on `cand:slope-row-mass-x` (X / first-mass form).** **PAIR touches it.** Its Corollary 4 bounds \(X=C(1)\le E^\times(h)\ll p^{4/3}(\log p)^{32/3}\) (Round 186: \(31/21\)) and \(\mathcal M_w\le E^\times(h)/4\). This moves the unconditional value of the X form from \(31/21\) to \(4/3+o(1)\), but not to its target \(p^{1+1/1280}\); the shared estimate stays open. PAIR declares the touch itself (Result summary item 6, Corollary 4). COLD does not touch it. Neither report touches \(\Gamma_2=n\mathcal E(\nu)-1\) (`cand:near-critical-square-mass`).

### After unblinding

Opened afterwards: `coordination/round-187-inflight.json`, `coordination/shared-obligations/round-187-before.json` and `coordination/drafts/round-187-dependency-assessment.json` (no `round-187-after.json` exists yet).

- The coordinator's pre-dispatch comparison (`comparison_status: assessed`, `known_shared: []`, empty `candidate_ids_by_call`) dispatched the two calls as independent and asked the ordinary call to state any input that also bounds \(X\) or \(\Gamma_2\).
- **Agreement.** My blind classification (independent) matches. PAIR honoured the request: Corollary 4 states the \(X\), \(\max W\) and \(\mathcal M_w\) consequences separately and says \(\Gamma_2\) is not touched.
- **The touch on `cand:slope-row-mass-x` was not pre-recorded** (the ordinary call had no candidate ID). It is a touch on the already-named shared estimate (X / first-mass form), found within one call, not a new overlap between the two calls. The closeout should record it under that existing ID.
- **Dispatch effect:** none. Lane labels `session/r187-pair-energy` and `session/r187-cold-bword` match the report headers.

## Summary of verdicts

| Report | Main verdict | Corrections / conditions |
|---|---|---|
| PAIR. Level-set pair energy | (a1) **Lemma C ACCEPTED**; (a2) **Lemma M′ ACCEPTED** (one wording correction); (a3) **Prop. P′ ACCEPTED**; (a4) **Theorem 1 ACCEPTED**; (a5) **Theorem 2 ACCEPTED**; (a6) **Corollary 3 ACCEPTED**; (a7) **Corollary 4 ACCEPTED**; (a8) method statements **ACCEPTED** as method statements. Verdict "supported" is honest. | **The headline survives every check I could make.** \(E^\times(h)\ll p^{4/3}(\log p)^{32/3}\); hence \(\sup_{\lambda\ne1}C(\lambda)\ll p^{4/3}(\log p)^{32/3}\) uniformly in \(\lambda\in\mathbb F_p\setminus\{0,1\}\) (\(\delta_C=1/24\)), \(\sum W^{3/2},\mathcal E(\mu)\ll p^{8/3}(\log p)^{16/3}\), and one-match covariance \(O(p^{43/24}(\log p)^{4/3})\), \(43/24=115/64-1/192\). Same hypotheses as the accepted Round 180/185/186 bounds ((H1)/(H2) with the cap; no (NC) input). Only external input: Stevens–de Zeeuw Thm 4, re-read at source; Reiher–Schoen is no longer used. Side claims: \(X,\ \max W,\ 4\mathcal M_w\le E^\times(h)\ll p^{4/3+o(1)}\). No contradiction with any accepted lower bound, floor or control (§2.5); the characteristic hypothesis of SdZ enters exactly through Lemma C's third term, and over \(\mathbb F_{r^2}\) that term is \(q^{3/2}\), matching the square control. Corrections: (i) "effective doubling \(K\)" is \(K^{5/4}\) when measured against \(|B|\) (it is \(K\) against \(m\)); no effect on any exponent; (ii) the \(43/24\) covariance already follows from \(\max W\le X\le E^\times(h)\) through Round 184 Prop. 1(ii), so Round 185 Lemma 5 for \(\lambda\ne1\) is not even needed for the headline (a robustness remark). All bounds carry \((\log p)^{O(1)}\); "\(O(p^{4/3})\)" means \(p^{4/3+o(1)}\). |
| COLD. B-word delocalization | (a1) Prop. M, Cor. M1 **ACCEPTED**; (a2) Theorem 1 **ACCEPTED** for \(k\le9\) (inheriting Rounds 177/179/180; ineffective), **CONDITIONAL** on \((H_k)\) for \(k\ge10\), as stated; Cor. 1.1 **ACCEPTED** (same scope); Cor. 1.2 **ACCEPTED** (real floor, ineffective threshold); Cor. 1.3 **CONDITIONAL** on (P) and (W⁺), as stated; (a3) Lemma 3 (a)–(c) **ACCEPTED** in the compact model given the Round 79/80/179 identities (the iterate formula in (a) is conditional on the Round 80 (4) reading, as stated); (a4) Prop. H, Cor. H1 **ACCEPTED** (model); (a5) Prop. 6 **ACCEPTED as an implication** (CONDITIONAL on (ST↓)). §6 heuristic: honestly labelled. Evidence: honest; replayed on a subset. Verdict **inconclusive: ACCEPTED.** | The mission question (bounded vs \(\sqrt{\ln n}\)) is not settled. Proved: at each fixed height the ratio is bounded in \(n\) (ineffective, \(\approx10^{956}\) at the real floor), so any \(\sqrt{\ln n}\) obstruction must live at heights \(k\asymp\log n\); in a Haar-eigenbasis model every word has ratio \(\sqrt{2\ln n}(1+o_P(1))\). Floating: physical ratios follow the Gaussian maximum of \(n/2\) values on \(n\le5\cdot10^7\) (replayed here on \(n\le10^6\)). |

## 2. Report PAIR: `native-claude-ordinary-prime-level-pair-energy-187.md`

**Sources checked by line.**
- `native-claude-ordinary-prime-shifted-level-energy-182.md` lines 20–235: (H1)–(H4); Proposition 1 and (iv) \(\mathcal M_w\le\frac14E^\times(h)\); Lemma S1 and its proof (no size restriction); Lemma S2; the verbatim SdZ quote; Lemma SE; Proposition 3; Proposition 4 (the method cap).
- `native-claude-ordinary-prime-near-critical-band-autocorrelation-185.md` lines 30–130: setup, R180-rel/lines/det, Lemma 4, **Lemma 5** (\(C^\sharp_\lambda[f_1,\dots,f_4]\le\prod\mathcal N(v_i)\); "for \(f=g\) this is \(C(\lambda)\le X\le E^\times(h)\)").
- `native-claude-ordinary-prime-near-critical-slope-row-mass-184.md` lines 88–141 (Proposition 1 (i)–(v); the floors \(X\ge(2-o(1))p\), \(\max W,\sup C\ge(1-o(1))p\) on (NC)) and lines 213–270 (Proposition 5, the \(\mathbb F_{r^2}\) square control and its method cap).
- `native-claude-ordinary-prime-first-mass-fibre-dilation-183.md` lines 14–31, 255–275 (the \(g_H\) family, Proposition C, Corollary C2).
- `native-claude-ordinary-prime-sup-c-heavy-price-186.md` §§2, 6–7, and `native-claude-audit-186.md` in full.
- Acceptance records 180–186, searched for every accepted lower bound or floor on \(X\), \(\max W\), \(\sup C\), \(E^\times(h)\).

**External source, fetched for this audit** (one fetch subagent, arXiv HTML rendering of 1609.06284v4, Section 1.3 and the proof in Section 2):
- **Stevens–de Zeeuw Theorem 4.** \(A,B\subset\mathbb F\), \(|A|=a\le b=|B|\), \(ab^2\le n^3\), \(\mathcal L\) a finite *set* of \(n\) lines; "if \(\mathbb F\) has positive characteristic \(p\), assume \(an\ll p^2\)"; then \(I(A\times B,\mathcal L)\ll a^{3/4}b^{1/2}n^{3/4}+n\). This agrees with PAIR's quote word for word.
- \(a\) is the **smaller** set and \(p\) is the **characteristic** (not the field size). The field is arbitrary. The proof removes vertical lines (they contribute \(\le ab\)); horizontal lines go through the pencil step. The implied constant is "the implicit constant in Theorem 4"; the paper does not discuss absoluteness, but the statement is uniform over fields and sets, which is how Rounds 180–186 use it.
- The paper has no multiplicative-energy corollary for shifted sets, so Lemma M′ is new to the project and is not a quoted result.

### 2.1 Lemma C (a1): ACCEPTED

- **Orientation.** Lines that are neither vertical nor horizontal stay so, and stay distinct, under the coordinate swap. So \(x=s\le b=z\) may be assumed, and every line is the graph of a function of the first coordinate.
- **Chunks.** \(n_0=\lfloor c_0p^2/s\rfloor\ge c_0p^2/(2s)\) because \(s\le p\) and \(c_0p\ge2\) for large \(p\). Each chunk satisfies \(sn_j\le c_0p^2\), the hypothesis \(an\ll p^2\) with \(a=s\) the smaller set.
- **Trivial branch.** If \(sb^2>n_j^3\), then \(I_j\le sn_j\le s^{3/4}b^{1/2}n_j^{3/4}\) (because \(sn_j<s^{4/3}b^{2/3}\le b^2\)).
- **Sum.** Hölder gives \(\sum n_j^{3/4}\le k^{1/4}n^{3/4}\) with \(k^{1/4}\le(n/n_0)^{1/4}+1\), and \(s^{3/4}n_0^{-1/4}\le(2/c_0)^{1/4}sp^{-1/2}\).

Every step checks. **Where primality enters.** Only here, through \(an\ll p^2\) with \(p\) the characteristic. In \(\mathbb F_p\) the characteristic equals the field size, so the chunk size \(p^2/s\) is never smaller than \(p\). This is the single place where the argument would change over \(\mathbb F_{r^2}\) (§2.5).

### 2.2 Lemma M′ (a2), re-derived line by line: ACCEPTED

Setting: \(A,R\subseteq\mathbb F_p\setminus\{0,1\}\), \(|A|=\alpha\), \(|R|=m\), \(E=E^\times(R)=\sum_wr(w)^2=m^3/K\), \(L_0=\lfloor\log_2m\rfloor+1\).

1. **Popular class \(F\).** The values \(r(w)\in[1,m]\) fall into \(\le L_0\) dyadic classes; one class \(F=\{\rho\le r<2\rho\}\) has \(\sum_Fr^2\ge E/L_0\). Then \(|F|\rho^2\le E\) and \(P=\sum_Fr\ge\sum_Fr^2/(2\rho)\ge E/(2\rho L_0)\). With \(\eta=P/m^2\le1\): \(1/\eta\le2L_0K\) (from \(\rho\le m\)), and, using \(\rho\ge E/(2PL_0)\),
   \(|F|\le E/\rho^2\le4P^2L_0^2/E=4L_0^2K\eta^2m\). **Checked.**
2. **The subset \(B\).** \(d(y)=\#\{y'\in R:y/y'\in F\}\), \(\sum_yd(y)=P\), \(d\le\min(m,|F|)\). \(B=\{d\ge P/(2m)\}\) carries \(\sum_Bd\ge P/2\), so \(|B|\ge P/(2\min(m,|F|))\) and \(|B|^2\ge P^2/(4m|F|)\ge E/(16L_0^2m)=m^2/(16L_0^2K)\). **Checked.**
   - **\(B\) depends only on \(R\).** \(F\) and \(d\) are defined from the quotient distribution of \(R\) alone (a deterministic tie-break among qualifying classes suffices). So one extraction serves every partner \(A\). **Checked.**
3. **Incidences.** \(\ell_{u,v}:Z=v(uX+1-u)\), \(u\in T_h\), \(v\in V=R^{-1}\): slope \(vu\ne0\), intercept \(v(1-u)\), sum \(v\); so the \(tm\) lines are pairwise distinct and none is vertical or horizontal (the row \(u=1\) gives \(Z=vX\), still admissible). For each row pair \((x,y)\in A\times B\) and each \(v\) with \(vy\in F\), the point \((x,vy)\in A\times F\) is on \(\ell_{u,v}\); the map is injective (\(y=vy/v\)). Since every \(y\) in a row lies in \(B\), \(I(A\times F,\mathcal L)\ge ht\cdot P/(2m)=ht\eta m/2\). **Checked**, including that the point set is a genuine Cartesian product \(A\times F\) and that the lines are a set.
4. **Rich rows.** Lemma C with \(s'=\min(\alpha,|F|)\), \(b'=\max(\alpha,|F|)\), \(n=tm\). If \(h\eta/2>3C_2\max(1,s'b'^{1/2}p^{-1/2})\), the left side \((h\eta/2)tm\) exceeds \(3C_2\) times the second and the third term, so the first term dominates and \(tm\le6^4C_2^4s'^3b'^2/(h\eta)^4\). With \(s'^3b'^2=(\alpha|F|)^2s'\le\alpha^2|F|^2\mu_*\) (\(s'\le\min(\alpha,|F|)\le\mu_*\) since \(\eta\le1\)) and \(|F|^2/\eta^4\le16L_0^4K^2m^2\): \(t(h)\le C_4L_0^4\alpha^2K^2m\mu_*/h^4\).
   - **The \(\eta\) cancellation is genuine.** The incidence lower bound carries \(\eta\) to the first power, the SdZ main term carries \(|F|^{1/2}\le2L_0K^{1/2}\eta m^{1/2}\), so after raising to the fourth power \(\eta^4\) cancels exactly. The same happens in the threshold: \((6C_2/\eta)\,s'b'^{1/2}p^{-1/2}\le(6C_2/\eta)\cdot2L_0\eta(\alpha Km\mu_*)^{1/2}p^{-1/2}\). **Checked.**
   - **Threshold.** \(H_*\le12C_2L_0\max(K,(\alpha Km\mu_*)^{1/2}p^{-1/2})+1\), from \(1/\eta\le2L_0K\) and the display above. **Checked.**
5. **Energy.** Rows below \(H\) contribute \(\le H\alpha|B|\); dyadic classes above contribute \(\le\frac{16}3C_4L_0^4\alpha^2K^2m\mu_*/H^2\); the balance \(H^3=L_0^4\alpha K^2m\mu_*/|B|\) gives \(L_0^{4/3}\alpha^{4/3}|B|^{2/3}K^{2/3}m^{1/3}\mu_*^{1/3}\); the \(H_*\) branch gives terms 2 and 3. **Checked.**

**Is the \(K^4\to K\) improvement right, or does it hide a lost factor?** It is right. The price is paid elsewhere and is visible: the lines run over all of \(V=R^{-1}\) (\(m\) of them per \(u\), not \(|B|\)), and the bound carries \(m\) rather than \(|B|\). Measured against \(|B|\ge m/(4L_0\sqrt K)\), the first term is \(\le\alpha^{5/3}|B|\,(4L_0)^{1/3}K^{5/6}\), i.e. the analogue of Lemma M's \(K'^{2/3}\) with \(K'=K^{5/4}\). **Wording correction:** PAIR's "the effective doubling is \(K\), not \(K^4\)" is true against \(m\) and is \(K^{5/4}\) against \(|B|\). PAIR's exponent bookkeeping uses \(m\) and \(|B|\) separately and is unaffected. The argument is the standard "popular ratios plus rich lines" device that avoids BSG; it uses only \(E^\times(R)\), never a small product set.

**Attempts to break it** (all in `paley-187-audit-pair-check.py`):
- *Exact replay of Steps 1–3* with my own code at 27 primes \(p\in[101,409]\), 276 cases (random sets, geometric progressions, subgroups, progression plus junk, a progression united with its shift, partners random, large, and \(1-R\)): \(\sum r=m^2\); \(\sum r^2=E^\times(R)\) against a brute-force product count; the class bounds; (2.1); \(\sum d=P\), \(d\le\min(m,|F|)\); \(|B|^2\ge m^2/(16L_0^2K)\); the bound \(s'^2b'\le4L_0^2\eta^2\alpha Km\mu_*\) behind \(H_*\); line distinctness; and \(I(A\times F,\mathcal L)\ge htP/(2m)\) against a brute-force incidence count at the smallest, median and largest row value. No failure.
- *Characteristic-free version is false.* Over \(\mathbb F_{r^2}\), \(A=B=R=\mathbb F_r\setminus\{0,1\}\) (\(K\asymp1\), \(B=R\)): exact brute force over all \(u\in\mathbb F_{r^2}^\times\), \(r=5,\dots,23\), gives \(E(A;A)=(r-2)^2+(r-2)(r-3)^2\asymp q^{3/2}\), and \(E/r^{8/3}\) grows like \(r^{1/3}\) (0.29 → 2.07). So terms 1–2 of Lemma M′ alone cannot hold in a general field. Lemma M′'s term 3, with the characteristic \(r\) in place of \(p\), is \(\alpha^2|B|(Km)^{1/2}r^{-1/2}\asymp r^3\): exactly the subfield energy. The lemma is consistent with this example, and the example shows that term 3 is load-bearing.
- *Adversarial partners in \(\mathbb F_p\).* \(R=H\) a multiplicative subgroup of order \(\approx\sqrt p\) (so \(K=1\), \(F=H\), \(\eta=1\), \(B=H\)); local search over \(A\) of sizes \(|H|\) and \(3|H|\) to maximise \(E(A;H)\), \(p=1009\)–\(8009\). Best \(E/T_1\) is 0.33 → 0.14, decreasing in \(p\); \(E/(\alpha|H|)\approx2.5\)–4.5 (near the generic size). PAIR's own adversarial run (`--adversarial 100049 1000033`) reproduces exactly (ratios \(\le0.07\)). This is evidence only; a constant cannot be tested at small \(p\).

### 2.3 Extraction and Proposition P′ (a3): ACCEPTED

- **Extraction.** \(R\leftarrow U\), remove \(B(R)\) until empty. Remainder sizes strictly decrease, so the pieces with \(m\in[M,2M)\) are consecutive and are disjoint subsets of the group's first remainder: \(\sum_{B\subseteq X_M}|B|<2M\). There is no leftover. At most \(\log_2|U|+1\) components.
- **Lemma S1 for every remainder.** \(R\subseteq S_t\subseteq\{x\in Q:g\ge t\}\), so \(E^\times(R)\ge t^2m^4/(C_{\rm cap}\sqrt p)\) and \(K(R)\le C_{\rm cap}\sqrt p/(t^2m)\le K_M\). No size condition (accepted in the Round 186 audit §2.2). The per-piece bound is nondecreasing in \(K\) and \(m\), so \(K_M\) and \(2M\) may be substituted; \(\min|B|\ge M/(4L_0\sqrt{K_M})\).
- **Piece sums.** \(\sum|B|^{1/3}\le2M(\min|B|)^{-2/3}\), \(\sum|B|^{1/2}\le2M(\min|B|)^{-1/2}\); constants \(8,4,4\cdot2^{1/4}\le6\). **Checked.**
- **Exponents, re-derived independently** as exact linear forms in \((e_s,\mu_s,e_g,\mu_g)\) from the per-piece bound and the piece sums (not from PAIR's table): T1 \(=\frac{u_s-u_g}6-\frac23(e_g+\mu_g)\), T2 \(=-\frac16+\frac{u_s}4-\frac{u_g}2\), T3 \(=-\frac1{24}-(e_g+\mu_g)-\frac{\mu_s}4\). All three agree with PAIR. Round 186 Prop. P (form I) minus T1 is exactly \(\frac{11}{12}u_s\).
- **Vertex enumeration** (own code, exact) of \(\{0\le e_i\le\frac16,\ -e_i\le\mu_i\le\frac12,\ u_s\le u_g\}\): 30 vertices, maxima \(0,-\frac16,0\).
- **Which constraints are load-bearing.**
  - Without the structured-side choice \(u_s\le u_g\), the T1 maximum is \(+\frac5{36}\). The choice is legitimate: both components are extraction components and \(E\) is symmetric, so either side may be priced by Lemma M′.
  - At \(e=\frac15\) (outside the range), whole level sets give T3 excess \(+\frac1{120}\). This is why the heavy range stops at \(p^{-1/6}\).
- **Slack.** \(\mu\ge-e-O(1/\log p)\) from \(|X|\le G/t\), and \(e\le\frac16+O(1/\log p)\); both cost \(O(1)\) factors.

### 2.4 Theorems 1 and 2 (a4, a5): ACCEPTED

- **Theorem 1.** Extract \(U\) at \(t=a\), \(U'\) at \(t=a'\); \(E(U;U')^{1/2}\le\sum_{X,X'}E(X;X')^{1/2}\) over \(\le(\log_2p+1)^2\) pairs; each pair \(\le C(\log p)^{4/3}p^{2/3}/(aa')\). Squaring gives \((\log p)^{20/3}\). **Checked.** Arbitrary subsets of level sets are covered. So the corrected (HC′) of the Round 186 audit holds on its full range \([cp^{-1/6},1]\), up to \((\log p)^{20/3}\).
- **Theorem 2.**
  - *Light part* (\(g<p^{-1/6}\)): \(\|h_<\|_2^2\le\tau_0G\), \(\|h\|_1\le G\), and \(\|c_{v,v'}\|_2\le\min(\|v\|_2\|v'\|_1,\|v\|_1\|v'\|_2\)) (Minkowski and \(c_{v,v'}(\kappa)=c_{v',v}(1/\kappa)\)). Light–light and both light–heavy terms are \(\le(\tau_0G)^{1/2}G\le C_{\rm cap}^{3/2}p^{2/3}\). **Checked.**
  - *Coverage of all level pairs.* Heavy levels \(U_k=\{\max(\tau_0,a_k/2)\le g\le a_k\}\), \(a_k=2^{-k}\ge\tau_0\), cover \(\{g\ge\tau_0\}\setminus\{1\}\) (\(k=0\) covers \([\frac12,1]\); the last level is cut at \(\tau_0\)); \(z=0\leftrightarrow x=1\) is excluded from \(h\). So \(h_\ge\le\sum_k\sum_{X\subseteq U_k}a_k1_{1-X}\) pointwise, and by bilinearity and monotonicity \(\|c_{h_\ge,h_\ge}\|_2\le\sum a_Xa_{X'}E(X;X')^{1/2}\) over all \(O((\log p)^4)\) **ordered** pairs, including pairs within one level and \(X=X'\). Every component has height \(\ge\tau_0\), so (3.1) applies to every pair. **Checked.**
  - Hence \(E^\times(h)^{1/2}\ll(\log p)^{16/3}p^{2/3}\).
- **Consistency with Round 182 Prop. 4's method cap.** Prop. 4 says that BSG-piece extraction plus Young on the light levels cannot beat \(E^\times(h)=O(p^{4/3})\). Theorem 2 attains exactly that value, with Young binding at \(g<p^{-1/6}\) and T3 binding at height \(p^{-1/6}\). Prop. 4 priced pieces by their own shifted energy; PAIR prices mixed pair energies against whole partner components (the Round 186 device), so it is not bound by Prop. 4's per-piece bookkeeping, only by its light-level cap, which it meets and does not cross. No conflict. The Round 185 acceptance's "scheme cap \(\sup C\ge p^{4/3}\)" is likewise a method cap, now attained.

### 2.5 Does the claim contradict any accepted lower bound, floor or control?

I searched acceptance records 180–186 for every accepted lower bound on \(X\), \(\max W\), \(\sup C\) or \(E^\times(h)\). None exceeds \(p^{4/3}\) on primes.

- **Round 184 Proposition 2 (on (NC)):** \(X\ge(2-o(1))p\), \(\max W,\sup_{\lambda\ne1}C\ge(1-o(1))p\). Compatible: \(p<p^{4/3}\).
- **Round 183 \(g_H\) family:** \(g_H=\delta_1+\frac141_{H\setminus\{1\}}\), \(|H|\le2C_{\rm cap}\sqrt p-1\). It satisfies (H1)/(H2) and Lemma S1 (\(E^\times(H)=|H|^3\)). Its shifted energy is \(\asymp E^\times(1-H)\), which is \(\ll|H|^{8/3}\ll p^{4/3}\) by PAIR (or SdZ directly) and \(\approx|H|^2+|H|^4/p\asymp p\) in the exact Round 183 counts. Compatible; the family is a method cap for keeping \(w\), not a lower bound above \(p\).
- **Round 184 Proposition 5 (square control over \(\mathbb F_{r^2}\), \(q=r^2\)):** \(X,\max W,\sup C\ge(1-o(1))q^{3/2}\). If PAIR's proof ran verbatim over \(\mathbb F_q\), it would give \(X\ll q^{4/3+o(1)}\): a contradiction. **It does not run there, and the obstruction is located exactly:**
  - every other ingredient holds over \(\mathbb F_q\): (H1)/(H2), Lemma S1 (Prop. 5 says the configuration satisfies it), the extraction, the line family, the incidence count and Round 185 Lemma 5;
  - Lemma C uses SdZ's \(an\ll(\operatorname{char})^2\). Over \(\mathbb F_q\) the characteristic is \(r=q^{1/2}\), so the chunk size becomes \(r^2/s=q/s\) and Lemma C's middle term becomes \(sb^{1/2}nr^{-1/2}=sb^{1/2}nq^{-1/4}\);
  - in Lemma M′ and Prop. P′ this raises the T3 excess at height 1 from \(-\frac1{24}\) to \(-\frac1{24}+\frac18=+\frac1{12}\) (in \(q\)-exponents), so the pair price is \(q^{3/4}\) and the method gives only \(E^\times(h)\ll q^{3/2}\), which is the true value;
  - the exact subfield computation in Part C shows term 3 is attained (\(E(A;A)\asymp r^3\)).

  So the prime-field proof uses a prime-only input (the characteristic hypothesis of SdZ at sets of size \(\asymp\sqrt p\)), exactly as Round 184 Prop. 5's method cap requires of any power saving. This also agrees with the Round 184 reading that "every power saving available today enters through the third kind of input applied to level sets".
- **Square-field arithmetic is exact** (Part A of my script): \(r^3=q^{3/2}\) for term 3, \(r^{8/3}=q^{4/3}\) for terms 1–2, T3 excess \(+\frac1{12}\).

### 2.6 The chain and the side claims (a6, a7): ACCEPTED

- **\(\sup C\le E^\times(h)\).** Round 185 Lemma 5 (accepted): \(C(\lambda)\le C^\sharp_\lambda[g,g,g,g]\le\prod_i\mathcal N(v_i)=E^\times(h)\) for \(\lambda\ne0,1\); "for \(f=g\) this is \(C(\lambda)\le X\le E^\times(h)\)". \(X\le E^\times(h)\) is also accepted Round 182 Prop. 3's first step.
- **Chain** (Round 184 Prop. 1(i),(iii), accepted; exact Fractions): \(E^\times(m)\le X^2+\sup C\cdot M_1^2\ll p^{10/3}\) (\(X^2\ll p^{8/3}\)); \(\sum W^{3/2}\le M_1E^\times(m)^{1/2}\ll p^{8/3}\); R178: \(\sum W^2/p\le\max W\cdot M_1^2/p\ll p^{7/3}\), \(G\log p\sum W\ll p^{5/2}\log p\); so \(\mathcal E(\mu)\ll p^{8/3}(\log p)^{16/3}\) and the covariance is \(O(p^{9/8}\mathcal E^{1/4}+p^{3/2})=O(p^{43/24}(\log p)^{4/3})\). \(43/24=115/64-1/192\).
- **Robustness.** Round 184 Prop. 1(ii) with \(\max W\le X\ll p^{4/3+o(1)}\) (\(\varepsilon=1/3\)) gives the same \(7/4+1/24=43/24\). So the headline has two independent routes from Theorem 2.
- **Side claims.** \(\max_\xi W_\xi\le X\) (Cauchy–Schwarz, accepted Round 184); \(\mathcal M_w\le\frac14(E_Q(h)-{\rm diag})\le\frac14E^\times(h)\) (Round 182 Prop. 1(iv), re-proving Round 181's row-pair identity). So \(X,\max W,4\mathcal M_w\ll p^{4/3}(\log p)^{32/3}\): \(X\) improves from \(31/21\), \(\mathcal M_w\) from \(11/8\) (Round 180). The first-mass target \(p^{1+1/1280}\) is untouched, and \(\Gamma_2\) is untouched.
- **Fixed-slope first mass \(C(a)\), \(a\ne1\):** improves the same way (it is \(C(\lambda)\)). The Round 176/180 fixed-\(a\) generic squared mass is not re-derived (PAIR says so).

### 2.7 Hidden assumptions

1. **Near-critical input:** none. Inputs: \(0\le g\le1\), \(\operatorname{supp}g\subseteq Q\), \(g=|f|^2\) of a probability (for S1), the cap, \(G\le C_{\rm cap}\sqrt p\).
2. **Uniformity:** in \(\lambda\) (Lemma 5 is uniform), in \(\nu\) subject to the cap, and in the subsets \(U,U'\).
3. **Constants:** the SdZ constant, \(c_0\), \(C_{\rm cap}\), \(c\) (height range), and \(p^{O(1/\log p)}\) from dyadic slack. No constant depends on \(p\). The \(L_0\) factors are \((\log p)^{O(1)}\) and are carried explicitly.
4. **Large \(p\):** Lemma C needs \(c_0p\ge2\); all statements are for large primes \(p\equiv1\pmod4\), as before.

### 2.8 Evidence (c): honest as evidence

- `paley-187-pair-exponents.py --lp`: `ALL OK`, every printed line matches the report; under 1 s.
- `paley-187-pair-lemma-check.py`: `EXACT CHECKS OK` (90 cases); 4.4 s.
- `paley-187-pair-models.py --adversarial 100049 1000033`: matches §9's adversarial description (ratios 0.012–0.069); 5.5 s.
- `paley-187-pair-models.py 10000189`: see the replay log (§4).
- The models are far inside the bounds (\(E^\times(h)\approx p\)); they test no exponent. PAIR says so.

**Exactly what is proved (agent audit).** Take the actual weight \(g=|f|^2\) of a probability \(\nu\) on \(\widehat Q\) with the cap \(n\max\nu\le C_{\rm cap}\sqrt p\), and large primes \(p\equiv1\pmod4\). Then:
- (HC′): \(E(U;U')\ll p^{4/3}(aa')^{-2}(\log p)^{20/3}\) for all \(U\subseteq S_a\), \(U'\subseteq S_{a'}\), \(a,a'\in[cp^{-1/6},1]\);
- \(E^\times(h)\ll p^{4/3}(\log p)^{32/3}\);
- \(\sup_{\lambda\in\mathbb F_p\setminus\{0,1\}}C(\lambda)\ll p^{4/3}(\log p)^{32/3}\);
- \(\sum_\xi W_\xi^{3/2},\ \mathcal E(\mu)\ll p^{8/3}(\log p)^{16/3}\);
- the matching-number-one covariance is \(O(p^{43/24}(\log p)^{4/3})\);
- \(X,\ \max_\xi W_\xi,\ 4\mathcal M_w\ll p^{4/3}(\log p)^{32/3}\).

The inputs are Stevens–de Zeeuw Thm 4 (through the new Lemma C), Lemma S1, Round 185 Lemma 5, Round 182 Prop. 1(iv) and the Round 178/180/184 chain, plus the new Lemma M′ proved in PAIR and re-derived here.

**What is not proved:**
- anything below \(p^{4/3+o(1)}\) for \(\sup C\), \(X\), \(E^\times(h)\) or \(\mathcal M_w\) (this pricing is at its own floor: Young at \(g<p^{-1/6}\), T3 at \(p^{-1/6}\), and \(N^{8/3}\) at height 1);
- the logarithm-free forms;
- \(X=O(p^{1+1/1280})\); any bound on \(\Gamma_2\);
- the one-match target \(O(p^{3/2})\) (point–plane floor \(p^{7/4}\) of the Round 178 chain; generic six-word class);
- the Round 176/180 fixed-\(a\) generic squared mass at the new exponent;
- the original theta-limit target.

## 3. Report COLD: `native-claude-cold-prime-b-word-delocalization-187.md`

**Sources.** The mission, the full report, and the inherited statements as COLD quotes them. I re-read Round 179 (`cold-fixed-counting-source-obstruction-179.md`, lines 7–46: the fixed caps \(|U_j-S|\le2.338\) through \(V_{612}\), the cutoff activation at radius 5.2, the joint second-norm identification) to check the scope of Theorem 1. The Round 80/83/177/180/182 statements (compact identities, source floor 0.00042, cap 1.963, Criterion D and its budgets, per-simple rates) were **not** re-read line by line; they are taken as COLD quotes them, cross-checked against the Round 186 audit.

| Item | Statement | Verdict | Notes |
|---|---|---|---|
| (a1) | **Prop. M** \(M_{2m}^{1/(2m)}\le{\rm Rat}\le(n_gM_{2m})^{1/(2m)}\); **Cor. M1** (i)–(iii) | **ACCEPTED** | Elementary. My script checks the squeeze exactly on 400 random rational vectors (\(m\le5\)), \(((2m-1)!!)^{1/(2m)}>\sqrt{2m/e}\) outward for \(m\le200\), and \(n^{1/(2m)}\le e^{1/2}\) for \(m\ge\ln n\). In (iii) the upper bound uses \(M_{2m}\le(2m-1)!!\) at \(m=\lceil\ln n\rceil\): \((n(2m-1)!!)^{1/(2m)}\approx e^{1/2}\sqrt{2m/e}=\sqrt{2m}\). Correct. The budget thresholds \(\log_{10}\log_{10}n\ge410.9626\), \(413.2830\) reproduce. |
| (a2) | **Theorem 1**: \(\liminf_p\inf_Q\|R_{602+k}\|_{2,n}\ge c_k>0\), hence \({\rm Rat}\le2\rho/c_k\) | **ACCEPTED** for \(0\le k\le9\); **CONDITIONAL** on \((H_k)\) for \(k\ge10\), as stated | Step 1 (sup \(\le2\rho\) from the polydisk) and Step 2 (caps: \(\rho+1.963=2.338\) at \(\rho=3/8\); \(s_p+2.338<5.2\)) check. For \(603+k\le612\) the Round 179 fixed-height transfer applies exactly as written there (heights through 612, coordinate cap 5.2, uniform on \(Q\), both lifts). For \(k\ge10\) it needs \((H_k)\) and that Round 179's compactness argument runs verbatim at a larger fixed height; I agree it does (it is a fixed-word argument with caps), but I did not re-derive it. The constant is ineffective. |
| (a2′) | **Cor. 1.1** (no fixed-word \(\sqrt{\ln n}\) law) | **ACCEPTED** (scope of Theorem 1) | Immediate. It correctly limits the mission's "refuted" branch to heights \(k\to\infty\) with \(n\). |
| (a2″) | **Cor. 1.2**: \(c_k\ge0.00042\,\ell(2.338)^{602+k}\); \(\log_{10}{\rm Rat}\le956.2\) at \(t=a\), \(k\le9\) | **ACCEPTED** | Real floor only (Lemma 3(b) needs real segments). Inherits Round 83's source floor and Round 179's identities for genuine adjacent differences. Arithmetic: \(\log_{10}(0.00042\cdot0.027565^{611})=-956.318\le-956.317\) and \(\log_{10}(0.75)+956.318=956.19\); with my tighter enclosure \(\ell(2.338)\ge0.027572\) the bound is \(-956.25\), so the report's figure is valid and conservative. |
| (b) | **Cor. 1.3** (single-B words at fixed length) | **CONDITIONAL** on (P) and (W⁺), as stated | (W⁺) is unproved; the report says so. |
| (a3) | **Lemma 3(a)**: \(\ell_S^2=1-\sqrt{4a/(4a+8)}\), \(\ell_S=0.2400606\) | **ACCEPTED** (compact model; Round 79/179 identities) | \(\Phi_a'(y)^2=1-4a/(4a+y^2)\) and \(\mathbb E[1/(A+B\cos^2\theta)]=(A(A+B))^{-1/2}\) give the closed form; my arb value \([0.2400605605\pm3\cdot10^{-11}]\). The iterate formula \(\|L_S^kd\|=\ell_S^k\|d\|\) is conditional on the Round 80 (4) reading for transported fields, as the report says. The physical seed rates (0.25071 → 0.24007) converge to it; my replay reproduces the seed-part rates on \(n\le10^6\). |
| (a3′) | **Lemma 3(b)** weighted lower rate; **(c)** angular upper rate | **ACCEPTED** | (b): \(\sigma\tilde D\ge m(S)\ge0\) because \(\Phi_a'\) is odd and increasing and \(\sigma z\ge|S|-c\) on real segments; testing against \(\tau=\sigma m(S)d\) (\(J\)-measurable weight, \(\mathbb E\tau=0\)) gives \(\|T-\mathbb ET\|\ge\mathbb E[m^2]^{1/2}\|d\|\). (c): \(|\tilde D|\le\Phi_a'(|S|+c)\) and \(\mathbb E(|d|^2\mid J)=\|d\|^2\). Numbers, by my own arb Riemann sums with 20000 cells: \(\ell(2.338)\in[0.027572,0.027575]\), \(\ell(1.988)\in[0.054037,0.054042]\), \(\ell(0.985)\in[0.143035,0.143043]\), \(\ell(0)\ni\ell_S\), \(q_{\rm ang}(1.94)\in[0.428215,0.428227]\), \(q_{\rm ang}(2.338)\in[0.462713,0.462725]\); all inside the report's intervals. |
| (a4) | **Prop. H** (Haar eigenbasis): \({\rm Rat}(K_Uy)=\sqrt{2\ln n}(1+o_P(1))\) uniformly in \(y\); **Cor. H1** | **ACCEPTED** (model) | Re-derived: \(|f|=|y_0|\); invariance under the stabiliser of \(y_0\); conditional uniformity of \(w\) on the sphere of \(E_1\); \(\alpha=\sum\lambda_j\xi_j\) with \(\xi\sim\) Dirichlet\((\frac12,\dots)\). I verified \(\operatorname{Var}\alpha=(1-\operatorname{tr}\Lambda^2/N^2)\frac2{N+2}\le\frac2{N+2}\) exactly for \(N<60\). Floating check (my script, \(p=2017,8009\)): Haar-model ratios \(/\sqrt{2\ln n}\) are 0.87–0.99 for spike, sign, smooth and \(e_0\) inputs, while the physical \(K\) maps \(e_0\) to \(S\) with ratio \(\sqrt2\). Scope: the model ignores the evenness of physical rows (\(n/2\) distinct values); the report notes this. It is a model statement, labelled as such. |
| (a5) | **Prop. 6**: Criterion D \(+\) (ST↓) \(\Rightarrow C_k\le\Lambda\gamma^k\), \(\gamma<1/q_\rho\le1.9436\) | **ACCEPTED as an implication**; CONDITIONAL on (ST↓) | Passing to the limit at fixed \(k\) is legitimate because Criterion D quantifies over all \(k<k_n\to\infty\); \(\|\cdot\|_\infty\ge\|\cdot\|_{\infty,\rm good}\) is the right direction. **Scope remark:** Criterion D is a sufficient criterion, so a failure of \(C_k\le\Lambda\gamma^k\) would refute that hypothesis, not confinement; the report says so (§6 "Confinement itself would not be affected"). |
| — | §6 heuristic (\(\theta=2\) per step) | **Honestly labelled heuristic** | It stacks H-sup, the conjectured Perron rate 0.50206 and seed-linear dominance. Not used in any proof. |
| (c) | §7 floating evidence and fits | **Honest as evidence** | Replayed on the 40 primes with \(p\le2.01\cdot10^6\) (see §4): every per-prime row present in both runs matches the report to every printed digit (e.g. \(p=2017,9901,100673,1006237\)); sensitivity rows at \(p=200201\) match (seed start \(4.771\to5.092\); corner pp \(=4.771\)). On this subset the word-mean slope on \(\sqrt{2\ln n}\) is \(0.987\) [0.901, 1.079] (report, 49 primes: 1.021 [0.962, 1.079]); the bounded fit has \(\chi^2/{\rm dof}=22.7\). For \(R_{602}\) alone the slope is 0.63 [0.39, 0.86] and bounded \(\chi^2/{\rm dof}=2.26\): weaker than the word mean, as the report says (lower \(R_{602}\) slope from small primes). |
| Verdict | "Inconclusive" | **ACCEPTED** | The question needs control uniform in heights \(k\asymp\log n\); the proved inputs are fixed-height (Theorem 1, ineffective) or model (Prop. H). |

**Is the reading "the decisive quantity is the compact growth rate \(C_k\), not \(\sqrt{\ln n}\)" justified?** As a reading of Prop. 6 it is, given (ST↓). Two caveats belong with it:
- the heuristic value \(\theta=2\) is unproved, and the comparison with \(1/q\le1.9436\) is a 3% margin between two heuristic or inherited numbers;
- Criterion D's allowance has a huge \(\Lambda\) (up to \(6.5\cdot10^{205}\) at \(\gamma=1\)). Prop. 6 constrains \(C_k\) only as \(k\to\infty\), i.e. at heights \(k<k_n\asymp\frac47\log_2n\) for astronomically large \(n\). So "Criterion D in its stated form fails" (if \(\theta=2\)) is an asymptotic statement about a sufficient criterion, and has no effect at any accessible \(n\).

## 4. Replay log

Run from the repository root on 2026-11-21 with `.venv/bin/python -B` (python-flint 0.9.0). "Matches" means every quoted output line or table row appears in the run output, timing text excepted. All six report-script SHA-256 values equal those quoted in PAIR (the cold report quotes none; its hashes are recorded here).

| Script | Command | rc | Time | Result |
|---|---|---|---|---|
| pair exponents | `research/paley-187-pair-exponents.py --lp` | 0 | <1 s | `ALL OK`; LP maxima 0, −1/6, 0 |
| pair lemma | `research/paley-187-pair-lemma-check.py` | 0 | 4.4 s | `EXACT CHECKS OK` (90 cases) |
| pair models (adversarial) | `research/paley-187-pair-models.py --adversarial 100049 1000033` | 0 | 5.5 s | Matches §9 (ratios 0.012–0.069, \(K=1.5\), \(|B|=m\)) |
| pair models | `research/paley-187-pair-models.py 10000189` | 0 | 365 s | Matches the §9 table: \(E^\times(h)/p=1.880,1.338,1.160,1.040,1.004,0.066\) |
| cold constants | `research/paley-187-cold-constants.py` | 0 | <1 s | Every key line quoted in the report's replay section matches |
| cold rows (**subset**) | `research/paley-187-cold-bword-rows.py OUT 2017 … 1990657` (the 40 report primes with \(p\le2.01\cdot10^6\)), then `--start seed` and `--t pp` at \(p=200201\) | 0 | 76 s | Per-prime rows match the report (e.g. 2017: 3.072/3.231; 9901: 4.498/3.576; 100673: 4.433/4.041; 1006237: 4.800/4.608); sensitivity rows match |
| cold fit (subset) | `research/paley-187-cold-bword-fit.py OUT SENS` | 0 | few s | Fits on 40 primes; see §3 (c) |
| audit pair | `.venv/bin/python -B research/paley-187-audit-pair-check.py` | 0 | 7 s | `ALL AUDIT CHECKS OK` (Part A exact Fractions; Part B exact integers, 276 cases; Part C exact \(\mathbb F_{r^2}\), \(r\le23\); Part D evidence) |
| audit cold | `.venv/bin/python -B research/paley-187-audit-cold-check.py` | 0 | 2 s | `ALL AUDIT CHECKS OK` (Part A outward arb; Part B exact; Part C float model check) |

**Not replayed:** the cold rows for the nine primes with \(p\ge3.99\cdot10^6\) (largest \(p=100018801\); about 45 of the 50 minutes and up to about 7 GB). The report's rows and fits at those primes, its tail counts at \(p=100018801\) and its moment table at \(n=5\cdot10^7\) are therefore taken as printed. The sensitivity runs at \(p=2002001\) (all modes) and the corners mm, pm at \(p=200201\) were not replayed.

SHA-256:
- `paley-187-pair-exponents.py` `4e217ec60a63afaeb2e94af3af3f4cc8c05e81203c83141631796d10b6a4780e`
- `paley-187-pair-lemma-check.py` `6a911ded24545ae6f677a0bd87cb02a1bb72f212dc28011e38b050bbc709fa36`
- `paley-187-pair-models.py` `01a8baca6f0c3d0ee401afb3cf05f2b3b2238c3c1ae0462a674341d96739321c`
- `paley-187-cold-constants.py` `429b028d63443f63abdea019a533fa617395650859d574858b206f5d262a7895`
- `paley-187-cold-bword-rows.py` `5bf1c66d8ab894146e10b507e20ed52ae887bccedb7b22354230911b94eef41a`
- `paley-187-cold-bword-fit.py` `df1a0c0ca6c00905cc16a539ae18bc41e36f25927096db6367656d2a6ecdb1e2`
- `paley-187-audit-pair-check.py` `2c5ae92869ada2d5ceececa7dff3fcf3ca4f5893795545e31991eb184da290bb`
- `paley-187-audit-cold-check.py` `e94c729cb86b0b148cb2d5a107a40641bb7d3970cd35b21b6a896c2b2148a154`
- reports as audited: PAIR `5268631747d5ac3757ee328799f4e4205dd19afd5dc28184971a30255304e4b7`, COLD `6e7fc0d4e897581361046a67c9d3eb92d2033784dda3943ae3c4ebca53d361d2`

**Not checked:**
- The proof of Stevens–de Zeeuw Theorem 4 (only its statement, hypotheses and the handling of vertical lines were re-read from source). Whether its constant is absolute is not stated in the paper; it is uniform over fields and sets, which is all that is used.
- Asymptotic constants (\(C_2,C_3,C_4,C_5\)) cannot be tested at small \(p\). The exact replays check the identities and inequalities each step uses, not the \(\ll\) constants.
- The cold inherited inputs (Round 80 (4), Round 83's 0.00042, Round 177's 1.963, Round 180's Criterion D and budgets, Round 182's per-simple rates) were not re-derived. Round 179's fixed-height transfer was re-read only for its scope (heights through 612, cap 5.2).
- Theorem 1 for \(k\ge10\): that Round 179's compactness argument runs verbatim at a larger fixed height was not re-derived.
- The cold large-\(p\) rows listed above.
- The downstream Round 176/180 fixed-\(a\) generic squared mass at the new exponent.

## 5. Ranked closeout

### 5.1 What Round 187 changes

| Obligation | Before (Round 186 acceptance) | After Round 187 (as audited) | Effect |
|---|---|---|---|
| **One-match covariance** (target \(O(p^{3/2})\)) | \(O(p^{2125/1184}(\log p)^2)\), \(2125/1184=115/64-5/2368\approx1.794764\); \(\sup_{\lambda\ne1}C\ll p^{11/8-5/296}(\log p)^8\); \(\sum W^{3/2},\mathcal E(\mu)\ll p^{43/16-5/592}(\log p)^4\). Binding: Reiher–Schoen BSG loss \(\frac{11}{12}u\). Scheme floor \(p^{4/3}\) not reached. | **\(O(p^{43/24}(\log p)^{4/3})\)**, \(43/24=115/64-1/192\approx1.791667\). \(\sup_{\lambda\ne1}C\le E^\times(h)\ll p^{4/3}(\log p)^{32/3}\) (\(\delta_C\): \(5/296\to1/24\), the point–line scheme floor). \(\sum W^{3/2},\mathcal E(\mu)\ll p^{8/3}(\log p)^{16/3}\) (\(43/16-1/48\)). New input: Lemma M′ (popular-quotient, BSG-free) and Lemma C (chunked SdZ). Reiher–Schoen no longer used. No (NC) input. (HC′) proved on \([cp^{-1/6},1]\) up to \((\log p)^{20/3}\). Point–plane floor \(p^{7/4}\) unchanged. | **weakened** (third consecutive move; now at the scheme floor) |
| **\(E^\times(h)\), first mass \(X\), \(\mathcal M_w\)** (target \(p^{1+1/1280}\)) | \(X\le E^\times(h)\ll p^{31/21}(\log p)^8\); \(\mathcal M_w=O(p^{11/8})\) (Round 180) | \(X,\ \max W,\ 4\mathcal M_w\le E^\times(h)\ll p^{4/3}(\log p)^{32/3}\). Attains Round 182 Prop. 4's method cap; target untouched. Binding inside this method: Young at \(g<p^{-1/6}\), T3 at height \(p^{-1/6}\), \(N^{8/3}\) at height 1. | weakened (side quantities); `cand:slope-row-mass-x` X form \(31/21\to4/3+o(1)\) |
| Support energy \(\Gamma_2\) | only \(n\mathcal E(\nu)-1=O(p^\gamma)\), \(\gamma<3/8\) matters | untouched | unchanged |
| **Cold growing-prefix confinement** | Criterion D with \(n\)-independent \(\Lambda\) for B-words, or sup transfer, or a signed price | Not decided. Proved: fixed-height ratios bounded (ineffective, \(\approx10^{956}\)); Haar model gives \(\sqrt{2\ln n}\); the dichotomy is moment growth to order \(\ln n\); compact rates \(\ell_S=0.2400606\), \(\ell(2.338)\ge0.027565\), \(q_{\rm ang}(2.338)\le0.462748\). Conditional (ST↓): Criterion D forces \(C_k\le\Lambda\gamma^k\), \(\gamma<1.9436\). Heuristic: \(C_k\sim2^k\). Floating: Gaussian law on \(n\le5\cdot10^7\). | **reformulated** (the open quantity is the compact sup growth in \(k\), with a sharper fixed-height lower rate) |
| Generic J sum, zero match, generic six-word class, D2–D4, (b4), (b-Jk), (b-T), stationary domain, derivative transfer; the target | open | unchanged | unchanged |

### 5.2 Precise remaining obligations

1. **One-match (ordinary).**
   - Point–line pricing of \(\sup C\) is at its floor \(p^{4/3+o(1)}\). The Round 178 chain floors the covariance at \(p^{7/4}\) whatever \(\sup C\) is (Round 184 Prop. 1(iii): \(\sup C=p^{1+\varepsilon}\) gives \(7/4+\varepsilon/8\)). So the remaining gain from slope-row bounds is at most \(1/24\) in the exponent (\(43/24\to7/4\)), and only below \(\sup C=p^{4/3}\), which needs a height-1 pair-energy input below \(N^{8/3}\) at heights \(e<1/15\) (SdZ's quadrilinear price handles light slots for \(\lambda\ne1\), Round 185 Lemma 4).
   - Reaching \(O(p^{3/2})\) needs an input that is not an affine-energy (point–plane) bound, and the generic six-word class below \(p^{9/2}\).
2. **First mass.** \(X\), \(E^\times(h)\), \(\mathcal M_w=O(p^{4/3+o(1)})\). Going lower needs, together, a height-1 bound below \(N^{8/3}\) and a light-level input for \(g<p^{-1/6}\) (Young barrier; Lemma S2 alone is no better, Round 182). The target \(p^{1+1/1280}\) needs near-sharp shifted energies (Round 182 (b1)), which at \(|S_t|\asymp\sqrt p\) is a sum-product statement beyond current incidence technology.
3. **Support energy.** Unchanged.
4. **Cold.** Criterion D needs control uniform over growing heights \(k<k_n\): the compact sup growth \(C_k\) against \(1/q_\rho\le1.9436\) (Prop. 6, given (ST↓)), or a Criterion D variant with an averaged counting rate (angular \(q_{\rm ang}(2.338)\le0.4627\), allowance \(\ge2.161\)), which needs a physical growing-height \(L^2\) decoupling. Plus D2–D4, (b4), (b-Jk), (b-T), the stationary domain and derivative transfer. Proved frozen rate stays 1.066.
5. **Bookkeeping.** Propagate \(\sup C=p^{4/3+o(1)}\) to the Round 176/180 fixed-\(a\) generic squared mass; record (HC′) as proved (Theorem 1, with \((\log p)^{20/3}\)); record the touch on `cand:slope-row-mass-x` (X form now \(4/3+o(1)\), still open at \(p^{1+1/1280}\)).

**Shared estimates.** `cand:slope-row-mass-x`: the one-match form is now at the point–line floor (\(\delta_C=1/24\)); the X / first-mass form moves from \(31/21\) to \(4/3+o(1)\) and stays open at its target. No new shared candidate: (HC′) is now proved and needs no ID. Given the size of the jump, a human read of Lemma M′ (one page, elementary from SdZ Thm 4) before the coordinator relies on it downstream would be prudent; I found no gap.

### 5.3 Recommended Round 188 calls (most valuable first)

**1. `cold-prime-compact-sup-growth` (cold; decides whether Criterion D in its stated form can hold).**
- **Question:** in the compact (subsequential) model at the real floor, does the sup of the increments \(R^{\rm comp}_{602+k}\) (equivalently, of the seed iterates \(\mathcal L_S^kd\) and the single-B words) decay at a rate below \(1.94\times0.2401\approx0.466\) per step, so that \(C_k=\|R^{\rm comp}\|_\infty/\|R^{\rm comp}\|_2\le\Lambda\gamma^k\) with \(\gamma<1/q_\rho\)? Or is there a sign-aligned family with sup \(\ge c\cdot0.50^k\)?
- **Why now:** COLD reduced the \(n\to\infty\) content of Criterion D to the growth of \(C_k\) (Prop. 6, given (ST↓)), proved the exact seed \(L^2\) rate \(\ell_S\), and its heuristic puts \(C_k\sim2^k\) within 3% of the allowance. A compact-model computation can decide it, unlike more floating searches at larger \(p\).
- **Scope:** compact model of Rounds 79/80/179 at \(t=a\), real segments; start from the Round 182 per-simple slot-count transfer matrix and the independence of transported factors; certified (outward) bounds for the rate; floating only for orientation. State (ST↓) and the Round 80 (4) reading as hypotheses. Include the angular-rate variant (allowance \(1/q_{\rm ang}(2.338)\ge2.161\)) as a second threshold.
- **If yes** (certified rate \(<0.466\)): Criterion D's \(\gamma\) fits in the \(n\to\infty\) regime; the remaining gap is (ST↓) plus uniformity in \(k<k_n\) at finite \(n\).
- **If no** (certified \(C_k\ge c\,\theta^k\), \(\theta>1.9436\)): Criterion D in its stated form fails asymptotically (given (ST↓)); move to the averaged-rate variant (if \(\theta<2.161\)) or to a price with rate \(<1\).
- **If inconclusive:** the certified two-sided range for the rate and the term that blocks.

**2. `ordinary-prime-beyond-point-plane` (ordinary; the one-match obstruction that remains).**
- **Question:** the Round 178 chain floors the one-match covariance at \(p^{7/4}\) (\(\mathcal E(\mu)\ge p^{5/2}\)), and Round 187 put every slope-row quantity (\(\sup C\), \(\max W\), \(X\)) at \(p^{4/3+o(1)}\). Is there an estimate on the twisted second norm \(\|H_\alpha\|_2\) (or on \(\sum w|H_\alpha|^2\)) that does not pass through the affine energy and can use these slope-row bounds to go below \(p^{7/4}\)? Return either a new exponent or a proof that every route through \(\mathcal E(\mu)\) or its known variants floors at \(7/4\), with the exact term that a new route must control.
- **Why now:** point–line pricing is exhausted (this round); further \(\sup C\) work can gain at most \(1/24\) and cannot reach \(3/2\). The value of the ordinary route now lies entirely in the step after the slope-row quantities.
- **Scope:** actual \(g\) with the cap; Rounds 173/178/180/184 chain as accepted; cite Round 187 Theorem 2 and Corollary 3; no (NC) input unless marked; exact exponent arithmetic; keep the generic six-word class separate.
- **If yes:** a one-match exponent below \(7/4\); the remaining obligation becomes the six-word class.
- **If no:** a method cap at \(7/4\) for affine-energy routes; the coordinator should then weigh the one-match route against the zero-match and generic J-sum obligations.
- **If inconclusive:** the binding term and its size in the models.

**3. (Lower value; a short call or coordinator bookkeeping) `ordinary-prime-height-one-structured-energy`.**
- **Question:** for level sets at heights \(e<1/15\) with \(K\le p^{2e}\) (Lemma S1), is there a BSG-free pair-energy bound below \(N^{8/3}\), e.g. through the \(T_k\) form of Lemma S1 (Round 185 Prop. 6) combined with Lemma M′'s popular-quotient device and a structured-product energy (MPRRS-type \(N^{5/2}\))? Combined with SdZ's quadrilinear price for light slots, what \(\sup C=p^{4/3-c}\) results?
- **Why now:** it is the only lever left inside point–line pricing; its maximal payoff is \(43/24\to7/4\) in the one-match exponent.
- **Bookkeeping in the same call:** propagate \(\sup C=p^{4/3+o(1)}\) to the Round 176/180 fixed-\(a\) generic squared mass.
- **If yes:** \(\delta_C>1/24\) and a covariance between \(7/4\) and \(43/24\). **If no:** a method cap at \(p^{4/3}\) for height-1 inputs of SdZ type. **If inconclusive:** the best exponent and binding configuration.

**Retire or do not renew:**
- **BSG-based (Reiher–Schoen) pricing of \(\sup C\)**, Lemma SE/Lemma M with BSG pieces, and the Round 186 Theorem B machinery: superseded by Lemma M′.
- **Further extraction-plus-Young pricing of \(E^\times(h)\), \(X\), \(\mathcal M_w\):** at its method cap \(p^{4/3}\) (Round 182 Prop. 4, now attained).
- **Searches for (HC′)-violating models:** excluded by Theorem 1 up to logarithms.
- **Floating searches for bounded sup/RMS at larger \(p\)** (cold): through \(n=5\cdot10^7\) the law is Gaussian, and Theorem 1 puts the bounded regime at ineffective, astronomically large \(n\).
- **Size-only or rotation-invariant arguments for Criterion D:** Theorem N (Round 186) and Prop. H (Round 187) show any bounded-ratio proof must use the arithmetic structure of \(K\).

## 6. Status of this audit

This is an agent audit, not human acceptance or certification.

**What I checked:**
- every claim the two reports label as proved;
- PAIR's Lemma C, Lemma M′, extraction, Prop. P′ and Theorems 1–2, re-derived by hand; the exponents re-derived as exact linear forms from the per-piece bound (not from PAIR's table) and a fresh vertex enumeration;
- Stevens–de Zeeuw Thm 4, re-read from arXiv:1609.06284v4 through a fetch subagent (hypotheses \(a\le b\), \(ab^2\le n^3\), \(an\ll p^2\) with \(a\) the smaller set and \(p\) the characteristic; lines a set; vertical lines removed in the proof);
- consistency with every accepted floor, lower bound and control I could find (Round 184 Props. 2 and 5, Round 183 \(g_H\), Round 182 Prop. 4, Round 185's scheme cap), with the \(\mathbb F_{r^2}\) obstruction located exactly and computed;
- Lemma M′'s combinatorial steps exactly at 27 primes (276 cases), with my own code and brute-force incidence counts; adversarial partners at \(p\le8009\);
- the chain to \(43/24\) through two independent routes (Round 184 Prop. 1(ii) and (iii));
- COLD's Prop. M, Prop. H's variance step, Lemma 3's constants (independent arb Riemann sums, 5× finer), Cor. 1.2's arithmetic, Theorem 1's scope against Round 179;
- all six report scripts (cold rows on a subset \(p\le2.01\cdot10^6\)).

**What I did not check:** listed under "Not checked" in §4.

**Files:** nothing was committed. Only this file and `research/paley-187-audit-pair-check.py`, `research/paley-187-audit-cold-check.py` were written. Replay outputs went to the session scratchpad, not the repository.
