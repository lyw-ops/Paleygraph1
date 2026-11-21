# Round 187 native Claude draft: level-set pair energy without BSG

- **call_id:** `ordinary-prime-level-pair-energy`
- **Author:** Claude subagent started by the Round 187 coordinator (session/r187-pair-energy). This is an agent assessment: not an audit, not human acceptance, not a mathematical certification.
- **Mission:** `coordination/missions/round-187/ordinary-prime-level-pair-energy.md`, exported from `coordination/round-186.json` (SHA-256 `fc1582d2c07b0aacef5bbde79d30e880ef62e39d6e80fd74fe35c9b6e0c5fea0`, matches the export).
- **Inputs read.** All eight SHA-256 values listed in the mission match:
  - `research/round-185-acceptance.json` (`157de3b6…f59f9d`), `research/round-186-acceptance.json` (`9f1a0ccb…626ee`)
  - `research/native-claude-audit-186.md` (`2b61a763…bc48`), in full, with §2 and §5 read line by line
  - `research/native-claude-ordinary-prime-sup-c-heavy-price-186.md` (`9220d886…d0f3`), in full
  - `research/paley-186-supc-exponents.py` (`93debdd5…b8f`), `research/paley-186-audit-supc-check.py` (`3380c48f…521`)
  - `research/native-claude-ordinary-prime-near-critical-band-autocorrelation-185.md` (`4f0cd362…473`), lines 1–200 (setup, §1–§3, Lemmas 4–5)
  - `research/native-claude-ordinary-prime-shifted-level-energy-182.md` (`5c34d1fd…331`), lines 1–220 (setup, Prop. 1, Lemma S1, Lemma SE, Prop. 3, Prop. 4)

  Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-186.md`.
- **Scripts written (all new):**
  - `research/paley-187-pair-exponents.py`: exact Fractions; exact vertex enumeration; `--lp` adds a float LP cross-check.
  - `research/paley-187-pair-lemma-check.py`: exact integers / Fractions at small p; checks every combinatorial step of Lemma M′.
  - `research/paley-187-pair-models.py`: floating-point models at p ≈ 10^7 (evidence only).
- **Nothing was committed.** No coordination file, acceptance record or other agent's file was touched.

## Result summary

**Verdict: supported** (mission definition: "(HC′) gives sup C = O(p^{4/3+o(1)}) and one-match covariance p^{43/24+o(1)}"). The pair excess is κ = 0, i.e. δ_C = 1/24, the floor of point–line pricing. The bounds hold up to fixed powers of log p.

1. **New lemma (Lemma M′, popular-quotient form of Lemma M).** Let A, R ⊆ F_p∖{0,1} with |A| = α, |R| = m, E^×(R) = m³/K. There is a subset B ⊆ R, depending only on R, with |B| ≥ m/(4L₀√K) (L₀ = ⌊log₂m⌋+1), such that
   \[E(A;B)\ \ll\ L_0^{4/3}\alpha^{5/3}|B|^{2/3}K^{2/3}m^{1/3}+L_0K\alpha|B|+L_0\,\alpha^{2}|B|\,(Km)^{1/2}p^{-1/2}.\]
   - **No BSG and no doubling.** B is the set of y ∈ R that lie in many popular quotients y/y′ (a single dyadic popularity class F). The point set of the incidence argument is A × F, with |F| ≲ L₀²Kη²m, and the incidence count carries the same factor η. The η's cancel, so the effective doubling is K, not K⁴, and the size loss is K^{-1/2}.
   - **No characteristic hypothesis.** The third term comes from applying Stevens–de Zeeuw Theorem 4 to chunks of lines small enough for its hypothesis an ≪ p² (Lemma C). So the lemma holds at all sizes.
   - The only external theorem is Stevens–de Zeeuw Theorem 4, as already quoted and accepted (Rounds 180/182/185/186). **Reiher–Schoen BSG is no longer used anywhere.**
2. **Proposition P′ (pair price without BSG).** Run Round 186's uncapped extraction with Lemma M′ in place of Reiher–Schoen, to the end (no leftover). For two components s, g (heights p^{-e}, remainder sizes p^{1/2-μ}, u = 2e+μ), choose the structured side s with u_s ≤ u_g. Then
   \[a_sa_g\,E(X_s;X_g)^{1/2}\ \ll\ (\log p)^{4/3}\,p^{2/3}\qquad\text{whenever }e_s,e_g\le\tfrac16 .\]
   The three exponent excesses over 2/3 are exactly (u_s−u_g)/6 − (2/3)(e_g+μ_g), −1/6 + u_s/4 − u_g/2 and −1/24 − (e_g+μ_g) − μ_s/4, all ≤ 0 (exact; script). Round 186's Prop. P had excess (13/12)u_s − u_g/6; the difference is exactly (11/12)u_s, the BSG loss the audit located.
3. **Theorem 1 ((HC′) up to logarithms).** For the actual g = |f|² with the cap, every U ⊆ S_a and U′ ⊆ S_{a′} with a, a′ ∈ [c p^{-1/6}, 1] (any fixed c > 0) satisfy
   \[E(U;U')\ \ll\ p^{4/3}(aa')^{-2}(\log p)^{20/3}.\]
   This is the corrected criterion (HC′) of the Round 186 audit, on its full height range, with a (log p)^{20/3} loss. No model can violate (HC′) by a power of p.
4. **Theorem 2 (shifted energy of h).** For h(z) = g(1−z),
   \[E^\times(h)\ \ll\ p^{4/3}(\log p)^{32/3}.\]
   The light part g < p^{-1/6} is paid by Young's inequality, and all heavy pairs by Proposition P′. This reaches exactly the method cap p^{4/3} of Round 182 Proposition 4.
5. **Corollary 3 (sup C; one-match).** By Round 185 Lemma 5, C(λ) ≤ E^×(h) for every λ, so
   - \(\sup_{\lambda\ne1}C(\lambda)\ll p^{4/3}(\log p)^{32/3}=p^{11/8-1/24}(\log p)^{32/3}\) (δ_C = 1/24, against 5/296 in Round 186);
   - \(\sum_\xi W_\xi^{3/2},\ \mathcal E(\mu)\ll p^{8/3}(\log p)^{16/3}\);
   - **one-match covariance \(O(p^{43/24}(\log p)^{4/3})\)**, with 43/24 = 115/64 − 1/192 ≈ 1.791667, against 2125/1184 ≈ 1.794764.
6. **Corollary 4 (stated separately, as the mission asks: X and the first mass).** The same input gives X = C(1) ≤ E^×(h) ≪ p^{4/3}(log p)^{32/3}, against Round 186's 31/21. By Round 182 Proposition 1(iv) it also gives \(\mathcal M_w\le E^\times(h)/4\ll p^{4/3}(\log p)^{32/3}\), below Round 180's p^{11/8}. The first-mass target p^{1+1/1280} is untouched. Γ₂ is not touched. **This touches the X / first-mass form of `cand:slope-row-mass-x`**: it moves from 31/21 to 4/3 (log), and the shared estimate stays open at that target.
7. **No near-critical input.** The hypotheses are only (H1)/(H2) with the cap. The only structural input on g is Lemma S1.
8. **Evidence** (floating, p ≈ 10^7, tailored laws reaching heights p^{-e} with e up to 1/6): see §9. The (HC′) ratios are far below 1 and the Lemma M′ ratios are far below the bound shape. These are evidence only.

## Setup and hypotheses

Notation and normalisations are those of Rounds 171–186, with counting norms.

- **Field and law.** p ≡ 1 (mod 4) prime, n = (p−1)/2, Q the squares. ν is a probability on \(\widehat Q\), \(f=\sum_\eta\nu_\eta\eta\) on Q (zero off Q), g = |f|².
- **(H1)/(H2).** 0 ≤ g ≤ 1, g(1) = 1, supp g ⊆ Q, \(G=\sum_xg(x)\le n\max\nu\le C_{\rm cap}\sqrt p\). **No near-critical (NC) input is used anywhere in this report.**
- **Level sets.** \(S_t=\{x\ne1:g(x)\ge t\}\), \(|S_t|\le G/t\). Heights are written a = p^{-e}.
- **Shifted objects.** h(z) = g(1−z) for z ∈ F_p^×. For v, v′ ≥ 0 on F_p^×, \(c_{v,v'}(\kappa)=\sum_zv'(z)v(\kappa z)\) and \(E^\times(v)=\|c_{v,v}\|_2^2\). The map (v, v′) ↦ c_{v,v′} is bilinear, so \(\|c_{v,v'}\|_2\) obeys the triangle inequality in each argument and is monotone on nonnegative functions.
- **Pair energy** (Round 186). For A, B ⊆ F_p∖{0,1}: \(m_{A,B}(u)=\#\{(x,y)\in A\times B:1-y=u(1-x)\}\) and \(E(A;B)=\sum_{u\in\mathbb F_p^\times}m_{A,B}(u)^2=\|c_{1_{1-A},1_{1-B}}\|_2^2\). It is symmetric, and \(\sum_um_{A,B}(u)=|A||B|\).
- **Multiplicative energy.** \(E^\times(R)=\#\{(y_1,y_2,y_3,y_4)\in R^4:y_1y_2=y_3y_4\}=\sum_wr_R(w)^2\), where \(r_R(w)=\#\{(y',y)\in R^2:y/y'=w\}\) and \(\sum_wr_R(w)=|R|^2\).

**Inputs, each with its source.**

| input | statement | source |
|---|---|---|
| SdZ4 | Stevens–de Zeeuw Theorem 4 (quoted below) | arXiv:1609.06284v4; quoted verbatim in Round 182 (lines 118–122), re-read at source by the Round 185 and Round 186 audits |
| S1 | \(E^\times(W)\ge t^2|W|^4/(n\max\nu)\) for every W ⊆ {x ∈ Q : g(x) ≥ t}, any size | Round 182 lines 100–110 (Rounds 163/173); the Round 186 audit (§2.2) confirms there is no size restriction |
| R185-L5 | \(C(\lambda)\le C^\sharp_\lambda[g,g,g,g]\le\prod_i\mathcal N(v_i)=E^\times(h)\) for every λ, including λ = 1 (so X = C(1) ≤ E^×(h)) | Round 185 Lemma 5 and the remark after it; accepted (`round-185-acceptance.json` line 264) |
| R182-P1(iv) | \(\mathcal M_w\le\frac14E^\times(h)\) | Round 182 Proposition 1, accepted |
| R180/R184/R178 chain | \(E^\times(m)\le X^2+\sup_{\lambda\ne1}C\cdot M_1^2\), \(\sum W^{3/2}\le M_1E^\times(m)^{1/2}\), \(\mathcal E(\mu)\ll\sum_\xi(W_\xi^2/p+W_\xi^{3/2}+G\log p\,W_\xi)\), covariance \(O(p^{9/8}\mathcal E(\mu)^{1/4}+p^{3/2})\) | Round 180 (R180-sup), Round 178, Round 184 Prop. 1(iii); accepted, as used in Round 185 Cor. 3 and Round 186 Cor. C |

**External theorem.** Only Stevens–de Zeeuw Theorem 4, exactly as quoted in the accepted Round 182 report and re-read at source by the Round 186 audit (§2, "External sources"):

> "Let \(A,B\subset\mathbb F\) be sets with \(|A|=a\), \(|B|=b\), \(a\le b\) and \(ab^2\le n^3\). Let \(\mathcal L\) be a finite set of lines of size \(n\). If \(\mathbb F\) has positive characteristic \(p\), assume \(an\ll p^2\). Then \(I(A\times B,\mathcal L)\ll a^{3/4}b^{1/2}n^{3/4}+n\)."

Here an ≪ p² means an ≤ c₀p² for an absolute c₀ > 0, and the implied constant C₁ is absolute. The Round 186 audit notes that the proof removes vertical lines; our lines are never vertical or horizontal. **Reiher–Schoen BSG, Lemma SE, Lemma M and MPRRS Lemma 33 are not used.** No new external theorem is introduced.

## 1. Lemma C: Stevens–de Zeeuw without the characteristic hypothesis

**Lemma C.** Let X, Z ⊆ F_p with |X| = x, |Z| = z, and let \(\mathcal L\) be a set of n distinct lines in the (X, Z)-plane, none vertical or horizontal. Put s = min(x, z) and b = max(x, z). Then, for p larger than an absolute constant,
\[I(X\times Z,\mathcal L)\ \le\ C_2\big(s^{3/4}b^{1/2}n^{3/4}+s\,b^{1/2}\,n\,p^{-1/2}+n\big),\]
with C₂ absolute. There is no condition relating s, n and p.

*Proof.*
1. **Orientation.** If z < x, swap the two coordinates. A line that is neither vertical nor horizontal stays a line that is neither vertical nor horizontal, and distinct lines stay distinct. So assume x = s ≤ b = z, and every line is the graph of a function of the first coordinate.
2. **Chunks.** Put n₀ = ⌊c₀p²/s⌋. Since s ≤ p, n₀ ≥ c₀p/2 ≥ 1 for large p, and n₀ ≥ c₀p²/(2s). Split \(\mathcal L\) into k = ⌈n/n₀⌉ parts \(\mathcal L_j\) of sizes n_j ≤ n₀. For each part, s·n_j ≤ c₀p², which is the hypothesis an ≪ p² of SdZ4.
3. **Each part.** If s b² ≤ n_j³, SdZ4 gives \(I_j\le C_1(s^{3/4}b^{1/2}n_j^{3/4}+n_j)\). If s b² > n_j³, each line meets X × Z in at most s points (it is a graph over the first coordinate), so I_j ≤ s n_j. Also s n_j ≤ s^{3/4}b^{1/2}n_j^{3/4}, because \(n_j<s^{1/3}b^{2/3}\) gives \(sn_j<s^{4/3}b^{2/3}\le b^2\). (This is the Round 180 / Round 186 reduction, audited in Round 186 §2.1 step 3.)
4. **Sum.** By Hölder, \(\sum_jn_j^{3/4}\le k^{1/4}n^{3/4}\), and \(k^{1/4}\le(n/n_0+1)^{1/4}\le(n/n_0)^{1/4}+1\). Hence
\[I\le C_1\big(s^{3/4}b^{1/2}n^{3/4}+s^{3/4}b^{1/2}n\,n_0^{-1/4}+n\big),\qquad s^{3/4}n_0^{-1/4}\le(2/c_0)^{1/4}\,s\,p^{-1/2}.\ ∎\]

The middle term is the price of the chunking. `paley-187-pair-exponents.py` checks the exponent identity \(s^{3/4}b^{1/2}n(p^2/s)^{-1/4}=sb^{1/2}np^{-1/2}\).

## 2. Lemma M′ (pair energy against a set of large multiplicative energy, without BSG)

**Lemma M′.** Let A, R ⊆ F_p∖{0,1} with |A| = α ≥ 1 and |R| = m ≥ 1. Write E^×(R) = m³/K (so 1 ≤ K ≤ m), and L₀ = ⌊log₂m⌋+1. There is a set B = B(R) ⊆ R, **depending only on R**, such that
\[|B|\ \ge\ \frac{m}{4L_0\sqrt K},\]
and, for every such A,
\[E(A;B)\ \le\ C_3\Big(L_0^{4/3}\alpha^{4/3}|B|^{2/3}K^{2/3}m^{1/3}\mu_*^{1/3}+L_0K\alpha|B|+L_0\,\alpha|B|\,(\alpha Km\,\mu_*)^{1/2}p^{-1/2}\Big),\qquad \mu_*=\min(\alpha,4L_0^2Km),\]
with C₃ absolute. In particular, with \(\mu_*\le\alpha\) (form I):
\[E(A;B)\ \le\ C_3\Big(L_0^{4/3}\alpha^{5/3}|B|^{2/3}K^{2/3}m^{1/3}+L_0K\alpha|B|+L_0\,\alpha^{2}|B|\,(Km)^{1/2}p^{-1/2}\Big).\]

*Proof.*

*Step 1: a popular class of quotients.* The values of \(r=r_R\) lie in [1, m], so they fall into at most L₀ dyadic classes {2^j ≤ r < 2^{j+1}}. Since \(\sum_wr(w)^2=E:=E^\times(R)\), one class \(F=\{w:\rho\le r(w)<2\rho\}\) has \(\sum_{w\in F}r(w)^2\ge E/L_0\). Then:
- \(|F|\rho^2\le\sum_Fr^2\le E\), so \(|F|\le E/\rho^2\);
- \(P:=\sum_{w\in F}r(w)\ge\sum_Fr^2/(2\rho)\ge E/(2\rho L_0)\).

Put η = P/m². From ρ ≤ m we get \(P\ge E/(2mL_0)=m^2/(2KL_0)\), so 1/η ≤ 2L₀K. From \(\rho\ge E/(2PL_0)\) we get
\[|F|\ \le\ \frac{4P^2L_0^2}{E}\ =\ 4L_0^2K\eta^2m .\tag{2.1}\]

*Step 2: the subset B.* Let V = R^{-1} (|V| = m; 0 ∉ R) and d(y) = #{v ∈ V : vy ∈ F} for y ∈ R. Then \(\sum_{y\in R}d(y)=P\), because vy = y/y′ runs over the pairs counted by r. Also d(y) ≤ min(m, |F|), since v ↦ vy is injective. Put
\[B=\{y\in R:\ d(y)\ge P/(2m)\}.\]
The y ∉ B contribute less than m·P/(2m) = P/2, so \(\sum_{y\in B}d(y)\ge P/2\) and \(|B|\ge P/(2\min(m,|F|))\). Multiplying the two lower bounds P/(2m) and P/(2|F|) and using (2.1),
\[|B|^2\ \ge\ \frac{P^2}{4m|F|}\ \ge\ \frac{E}{16L_0^2m}\ =\ \frac{m^2}{16L_0^2K}.\]
B depends only on R. In particular B ≠ ∅, since \(\sum_Bd\ge P/2>0\).

*Step 3: incidences.* For (u, v) ∈ F_p^× × V let ℓ_{u,v} be the line Z = v(uX + 1 − u). Its slope vu and intercept v(1−u) sum to v, so these lines are pairwise distinct, and none is vertical or horizontal (Round 186 Lemma M, audited). Fix h ≥ 1, let \(T_h=\{u:m_{A,B}(u)\ge h\}\), t = |T_h|, and \(\mathcal L=\{\ell_{u,v}:u\in T_h,v\in V\}\), so \(|\mathcal L|=tm\).

For every u ∈ T_h, every (x, y) ∈ A × B with 1 − y = u(1 − x), and every v ∈ V with vy ∈ F, the point (x, vy) ∈ A × F lies on ℓ_{u,v}, because v(ux + 1 − u) = v(1 − (1 − y)) = vy. The map (u, v, x, y) ↦ (ℓ_{u,v}, (x, vy)) is injective, since y = (vy)/v. Hence
\[I(A\times F,\mathcal L)\ \ge\ \sum_{u\in T_h}\ \sum_{(x,y)\in\text{row }u}d(y)\ \ge\ h\,t\,\frac{P}{2m}\ =\ \frac{h\,t\,\eta\,m}{2}.\]

*Step 4: rich rows.* Let s′ = min(α, |F|) and b′ = max(α, |F|), so \(s'^{3/4}b'^{1/2}\) and \(s'b'^{1/2}\) are the Lemma C quantities for A × F. Lemma C gives
\[\frac{ht\eta m}{2}\le C_2\big(s'^{3/4}b'^{1/2}(tm)^{3/4}+s'b'^{1/2}\,tm\,p^{-1/2}+tm\big).\]
Suppose \(h\eta/2>3C_2\max(1,\ s'b'^{1/2}p^{-1/2})\). Then the right side is at most 3C₂ times its largest term, and that term cannot be the second or the third one. So \(ht\eta m/2\le3C_2s'^{3/4}b'^{1/2}(tm)^{3/4}\), i.e.
\[tm\ \le\ \frac{6^4C_2^4\,s'^3b'^2}{(h\eta)^4},\qquad s'^3b'^2=(\alpha|F|)^2s'\le\alpha^2|F|^2\mu_* .\]
By (2.1), \(|F|^2/\eta^4\le16L_0^4K^2m^2\). Therefore
\[t(h)\ \le\ C_4\,L_0^4\,\frac{\alpha^2K^2m\,\mu_*}{h^4}\qquad\text{for }h\ge H_*,\tag{2.2}\]
where H_* = (6C₂/η)·max(1, s′b′^{1/2}p^{-1/2}) + 1. Since 1/η ≤ 2L₀K and \(s'b'^{1/2}=(\alpha|F|)^{1/2}s'^{1/2}\le2L_0\eta(\alpha Km)^{1/2}\mu_*^{1/2}\) by (2.1),
\[H_*\ \le\ 12C_2L_0\max\big(K,\ (\alpha Km\mu_*)^{1/2}p^{-1/2}\big)+1 .\]

*Step 5: energy.* Put \(H=\max\big(H_*,\ L_0^{4/3}(\alpha K^2m\mu_*/|B|)^{1/3}\big)\). Rows with m_{A,B}(u) < H contribute at most \(H\sum_um_{A,B}(u)=H\alpha|B|\). The rows in the dyadic class [2^iH, 2^{i+1}H) contribute at most \(4\cdot4^iH^2t(2^iH)\), which by (2.2) is \(\le4C_4L_0^4\alpha^2K^2m\mu_*/(4^iH^2)\). Summing over i ≥ 0:
\[E(A;B)\ \le\ H\alpha|B|+\tfrac{16}3C_4L_0^4\frac{\alpha^2K^2m\mu_*}{H^2}.\]
With the second entry of H, both terms are \(\ll L_0^{4/3}\alpha^{4/3}|B|^{2/3}K^{2/3}m^{1/3}\mu_*^{1/3}\). With the first entry, \(H_*\alpha|B|\) gives the second and third terms of the lemma (and α|B| ≤ Kα|B|). ∎

**Why this is not a BSG statement.** B need not have small doubling; nothing about \(|B\cdot B^{-1}|\) is claimed. The incidence count only needs that each y ∈ B has many v with vy in one popular class F. Both the incidence count (factor η) and \(|F|^{1/2}\) (factor η, by (2.1)) scale the same way, so η cancels. The effective doubling is K (against K⁴ through Reiher–Schoen), and the size loss is K^{-1/2} (the same as Reiher–Schoen). Reiher–Schoen's lower bound \(c\ge\log4/\log(27/16)\approx2.649\) for the doubling exponent concerns subsets with \(|B-B|\) small; it does not apply here.

**Exact checks.** `paley-187-pair-lemma-check.py` checks, with exact integers at p = 13, …, 97 for random sets, geometric progressions, Q itself and "progression plus junk" sets (90 cases), every combinatorial step of Steps 1–3: \(\sum r=m^2\), \(\sum r^2=E^\times(R)\) (brute force), the class bounds, \(\sum_yd=P\), d ≤ min(m, |F|), \(\sum_Bd\ge P/2\), \(|B|^2\ge m^2/(16L_0^2K)\), line distinctness, the incidences, injectivity, and \(I(A\times F,\mathcal L)\ge htP/(2m)\) against a brute-force incidence count, for every h. Output: `EXACT CHECKS OK`. The constants C₂, C₃, C₄ come from SdZ4 and cannot be tested at small p.

## 3. Extraction without BSG and the pair price (Proposition P′)

**Extraction.** Let U ⊆ S_t (any t > 0). Put R ← U. While R ≠ ∅: let B = B(R) from Lemma M′, record it as a *piece*, and set R ← R∖B. Each piece is extracted from a remainder R with m = |R| ≥ 1; group the pieces by the dyadic size M ≤ m < 2M (M a power of 2) at the time of extraction. The union of the pieces of one group is a *component* X_M. Then:
- the components partition U, and there are at most log₂|U| + 1 of them;
- for each piece, Lemma S1 applied to R ⊆ S_t gives \(K(R)=m^3/E^\times(R)\le C_{\rm cap}\sqrt p/(t^2m)\le K_M:=C_{\rm cap}\sqrt p/(t^2M)\);
- each piece has \(|B|\ge m/(4L_0\sqrt{K(R)})\ge M/(4L_0\sqrt{K_M})\);
- the pieces of one group are disjoint subsets of the first remainder of the group, so \(\sum_{B\subseteq X_M}|B|<2M\).

This is Round 186's uncapped extraction (audit §2.2) with Lemma M′'s B in place of the Reiher–Schoen piece, and run to the end, so there is no leftover. No step uses a size cap: S1 holds for subsets of any size.

**Proposition P′.** Let X_M be a component of U ⊆ S_t, and D ⊆ F_p∖{0,1} any set with |D| = α. With L₀ = ⌊log₂p⌋ + 1,
\[E(X_M;D)^{1/2}\ \le\ C_5L_0^{4/3}\Big(\alpha^{5/6}M^{1/2}K_M^{2/3}+\alpha^{1/2}M^{1/2}K_M^{3/4}+\alpha M^{3/4}K_M^{1/2}p^{-1/4}\Big).\]

*Proof.* Use the triangle inequality for \(E(\cdot;D)^{1/2}=\|c_{1_{1-\cdot},1_{1-D}}\|_2\) over the pieces, then Lemma M′ (form I, symmetric E) for each piece B ⊆ R against A = D, with K(R) ≤ K_M and m < 2M (every term is nondecreasing in K and m):
- term 1: \(\sum_B(L_0^{4/3}\alpha^{5/3}|B|^{2/3}K_M^{2/3}(2M)^{1/3})^{1/2}\le L_0^{2/3}\alpha^{5/6}K_M^{1/3}(2M)^{1/6}\sum_B|B|^{1/3}\), and \(\sum_B|B|^{1/3}\le2M\,(\min|B|)^{-2/3}\le2(4L_0)^{2/3}M^{1/3}K_M^{1/3}\); total \(\le8L_0^{4/3}\alpha^{5/6}M^{1/2}K_M^{2/3}\);
- term 2: \(\sum_B(L_0K_M\alpha|B|)^{1/2}\le(L_0K_M\alpha)^{1/2}\cdot2M(\min|B|)^{-1/2}\le4L_0\alpha^{1/2}M^{1/2}K_M^{3/4}\);
- term 3: \(\sum_B(L_0\alpha^2|B|(2K_MM)^{1/2}p^{-1/2})^{1/2}\le L_0^{1/2}\alpha(2K_MM)^{1/4}p^{-1/4}\cdot4L_0^{1/2}M^{1/2}K_M^{1/4}\le6L_0\alpha M^{3/4}K_M^{1/2}p^{-1/4}\).

Since L₀ ≥ 1, all three are covered by \(C_5L_0^{4/3}(\cdots)\). ∎

**Pair exponents.** Take t = a_s/2 for a level component (or t = a_s for a subset of S_{a_s}), with a_s = p^{-e_s}, M = p^{1/2-μ_s}, so K_M ≤ C p^{u_s} with u_s = 2e_s + μ_s. Take the partner D = X_g, a component of another (or the same) slot, so α ≤ 2p^{1/2-μ_g}, at height a_g = p^{-e_g}. The pair price is a_s a_g E(X_s;X_g)^{1/2}. Its three exponents, minus 2/3, are (exact, `paley-187-pair-exponents.py`):

| term | exponent − 2/3 | rewritten (d = u_g−u_s, w_i = e_i+μ_i ≥ 0, z = 1/6−e_s) |
|---|---|---|
| T1 | \(\frac{u_s-u_g}6-\frac23(e_g+\mu_g)\) | \(-\frac d6-\frac23w_g\) |
| T2 | \(-\frac16+\frac{u_s}4-\frac{u_g}2\) | \(-\frac5{24}-\frac d2-\frac{w_s}4+\frac z4\ \le-\frac16\) |
| T3 | \(-\frac1{24}-(e_g+\mu_g)-\frac{\mu_s}4\) | \(-w_g-\frac{w_s}4-\frac z4\) |

The constraints are:
- **μ_i ≥ −e_i − O(1/log p)**, because \(|X|\le|U|\le G/t\le2C_{\rm cap}p^{1/2+e}\);
- **e_s ≤ 1/6 + O(1/log p)** for heights ≥ c p^{-1/6};
- **u_s ≤ u_g**, by choosing as the structured side the component with the smaller u (E is symmetric).

Under these constraints every coefficient in the last column is ≤ 0, so every excess is ≤ O(1/log p). Hence, for any two components at heights a_s, a_g ≥ c p^{-1/6},
\[a_sa_g\,E(X_s;X_g)^{1/2}\ \le\ C\,(\log p)^{4/3}\,p^{2/3}.\tag{3.1}\]
The script confirms this three ways:
- the identities and nonpositive rewritings, exactly;
- exact vertex enumeration of the polytope {0 ≤ e_i ≤ 1/6, −e_i ≤ μ_i ≤ 1/2, u_s ≤ u_g}: the maxima are 0, −1/6 and 0;
- 20 000 random rational points, plus a float LP.

**Where the gain over Round 186 comes from.** Round 186's Prop. P (form I) has pair exponent \(\frac23+\frac{13}6e_s+\frac{13}{12}\mu_s-e_g-\frac56\mu_g\). The difference from T1 is exactly \(\frac{11}{12}u_s\) (checked exactly). This is the "(11/12)e BSG doubling loss" that the Round 186 audit located; Lemma M′ removes all of it.
- T1 is attained with equality (excess 0) for whole level sets at a common height (μ = −e, u_s = u_g = e) at every e ∈ [0, 1/6], including Round 186's binding heights 1/37 and 1/74.
- T3 is attained with equality at e_s = e_g = 1/6. That is why the height range stops at p^{-1/6}.

## 4. Theorem 1: the criterion (HC′), up to logarithms

**Theorem 1.** Assume (H1)/(H2) with the cap. Fix c > 0. For all a, a′ ∈ [c p^{-1/6}, 1] and all U ⊆ S_a, U′ ⊆ S_{a′},
\[E(U;U')\ \le\ C\,p^{4/3}(aa')^{-2}(\log p)^{20/3},\]
with C depending only on C_cap and c.

*Proof.* Extract U with t = a and U′ with t = a′ (§3). Each has at most log₂p + 1 components, so
\[E(U;U')^{1/2}\le\sum_{X\subseteq U,\ X'\subseteq U'}E(X;X')^{1/2}.\]
For each pair, take as structured side the component with the smaller u. With heights a, a′ in the role of a_s, a_g, (3.1) gives \(aa'E(X;X')^{1/2}\le C(\log p)^{4/3}p^{2/3}\). Summing over at most (log₂p + 1)² pairs and squaring gives the bound. Inputs: S1 at t = a, a′ (so K ≤ C_cap√p/(a²m)), |U| ≤ G/a (so μ ≥ −e − O(1/log p)), and e ≤ 1/6 + log(1/c)/log p. ∎

**Remarks.**
- This is the corrected criterion (HC′) of the Round 186 audit (§2.4, §5.2), on its full range [c p^{-1/6}, 1], **with a (log p)^{20/3} loss**. The mission's (HC′) is stated with ≪ and no logarithm. Every consequence below absorbs the logarithm into p^{o(1)}.
- U and U′ are arbitrary subsets of the level sets, not only whole level sets or BSG pieces.
- The only property of g used is Lemma S1 (hereditary energy) and |S_t| ≤ G/t.
- **No admissible model can violate (HC′) by a power of p.** The mission's refutation branch ("a model with E(U;U′) ≥ p^{4/3+c}(aa′)^{-2} at some height in range") is excluded for all large p.

## 5. Theorem 2: the shifted energy of h

**Theorem 2.** Under (H1)/(H2) with the cap, for h(z) = g(1−z) on F_p^×,
\[E^\times(h)\ \le\ C\,p^{4/3}(\log p)^{32/3}.\]

*Proof.* Put τ₀ = p^{-1/6} and split h = h_< + h_≥ at g(1−z) < τ₀.
- **Light.** \(\|h_<\|_1\le G\) and \(\|h_<\|_2^2=\sum_{g<\tau_0}g^2\le\tau_0G\). By Minkowski, \(\|c_{v,v'}\|_2\le\|v\|_2\|v'\|_1\), and by \(c_{v,v'}(\kappa)=c_{v',v}(1/\kappa)\) also \(\le\|v\|_1\|v'\|_2\). Hence \(\|c_{h_<,h_<}\|_2\) and \(\|c_{h_<,h_\ge}\|_2\), \(\|c_{h_\ge,h_<}\|_2\) are all \(\le(\tau_0G)^{1/2}G\le C_{\rm cap}^{3/2}p^{2/3}\).
- **Heavy.** For k ≥ 0 with a_k = 2^{-k} ≥ τ₀, let \(U_k=\{x\ne1:\max(\tau_0,a_k/2)\le g(x)\le a_k\}\subseteq S_{a_k/2}\). Extract each U_k with t = a_k/2 (§3). So h_≥ ≤ Σ_k Σ_{X ⊆ U_k} a_k 1_{1−X} pointwise. (Consecutive U_k may share boundary points; this only enlarges the right side.) There are O(log p) levels and O(log p) components per level.
- **Heavy pairs.** By bilinearity, \(\|c_{h_\ge,h_\ge}\|_2\le\sum_{X,X'}a_Xa_{X'}E(X;X')^{1/2}\) over O((log p)⁴) ordered pairs. Each term is \(\le C(\log p)^{4/3}p^{2/3}\) by (3.1): all heights are ≥ τ₀, so e ≤ 1/6, and the structured side is chosen with the smaller u.
- Hence \(E^\times(h)^{1/2}=\|c_{h,h}\|_2\le C(\log p)^{16/3}p^{2/3}\). ∎

**Reading.**
- Round 182 Proposition 4 says that extraction of level-set pieces plus Young on the light levels cannot give better than E^×(h) = O(p^{4/3}), even with a sharp K-free piece lemma. Theorem 2 attains that cap, up to logarithms.
- The cap is reached at two places at once: the Young bound on g < p^{-1/6}, and the T3 term at heights p^{-1/6}.
- The previous unconditional values were E^×(h) ≪ p^{34/23} (Round 182) and ≪ p^{31/21}(log p)^8 (Round 186 Prop. X).

## 6. Consequences, stated separately

### Corollary 3 (one-match: sup C)

Under (H1)/(H2) with the cap, uniformly in λ ∈ F_p∖{0, 1}:
\[\sup_{\lambda\ne1}C(\lambda)\ \le\ E^\times(h)\ \ll\ p^{4/3}(\log p)^{32/3}=p^{11/8-1/24}(\log p)^{32/3}.\]
- The first inequality is Round 185 Lemma 5 with f_i = g (\(C(\lambda)\le C^\sharp_\lambda[g,g,g,g]\le\mathcal N(h)^4\)).
- So δ_C = 1/24 (up to logarithms): the scheme floor of the Round 186 audit, against 5/296.
- Propagation through the accepted chain:
  - \(E^\times(m)\le X^2+\sup_{\lambda\ne1}C\cdot M_1^2\ll p^{10/3}(\log p)^{32/3}\). The X² term is ≪ p^{8/3}(log p)^{64/3} by Corollary 4, which is smaller.
  - \(\sum_\xi W_\xi^{3/2}\le M_1E^\times(m)^{1/2}\ll p^{8/3}(\log p)^{16/3}\), and 8/3 = 43/16 − 1/48.
  - \(\mathcal E(\mu)\ll p^{8/3}(\log p)^{16/3}\). By R178, \(\sum W^2/p\ll p^{7/3+o(1)}\) and \(G\log p\sum W\ll p^{5/2}\log p\) are smaller.
  - **One-match covariance \(O(p^{9/8}\mathcal E(\mu)^{1/4}+p^{3/2})=O(p^{43/24}(\log p)^{4/3})\).** 43/24 = 115/64 − 1/192 ≈ 1.791667, against 2125/1184 ≈ 1.794764 (Round 186) and 1193/664 (Round 185).
  - The fixed-slope first mass C(a), a ≠ 1, improves the same way, to O(p^{4/3+o(1)}).
  - The Round 176/180 fixed-a generic squared mass is **not** re-derived here (bookkeeping).
- All exponents are checked with exact Fractions in `paley-187-pair-exponents.py`.

### Corollary 4 (X and the first mass; stated separately)

The same input bounds the λ = 1 quantities:
\[X=C(1)\ \le\ E^\times(h)\ \ll\ p^{4/3}(\log p)^{32/3},\qquad \mathcal M_w\ \le\ \tfrac14E^\times(h)\ \ll\ p^{4/3}(\log p)^{32/3}.\]
- The first uses Round 185 Lemma 5 at λ = 1; the second Round 182 Prop. 1(iv). Also \(\max_\xi W_\xi\le X\ll p^{4/3+o(1)}\).
- These improve X ≪ p^{31/21} (Round 186 Prop. X) and \(\mathcal M_w=O(p^{11/8})\) (Round 180).
- **The first-mass target X = O(p^{1+1/1280}) is untouched.** The Young barrier on the light levels g < p^{-1/6} is now the only obstruction inside this method. That is Round 182 Prop. 4's statement, now attained.
- Γ₂ = n𝓔(ν) − 1 is not touched.
- **Shared obligation:** this moves the X / first-mass form of `cand:slope-row-mass-x` from 31/21 to 4/3 (with logarithms). The shared estimate stays open at its target.

## 7. Why the Round 186 ceiling does not apply, and what is now the floor

- **The binding term is gone.** Round 186 priced a structured piece through |B/B| ≤ CK⁴|B| (Reiher–Schoen), which costs K^{4/3} in E^{1/2} per piece and K^{1/4} through the size loss. That gives excess (11/12)u against the SdZ gain (5/8)u. The audit showed that no BSG of Reiher–Schoen shape (doubling ≥ K^{2.649}) passes δ_C ≈ 0.0239.
- **Lemma M′ is not of BSG shape.** It never produces a set of small doubling. It uses the energy hypothesis directly, through one popular quotient class F and the subset B of y lying in many quotients from F. Per piece, its cost is K^{1/3} in E^{1/2}, and K^{1/3} through the size loss K^{-1/2} (via the m^{1/3}|B|^{2/3} shape). The excess becomes (u_s − u_g)/6 ≤ 0.
- **Is a piece lemma with K-free shape needed?** No. With the hereditary bound K ≤ C√p/(t²m) of Lemma S1, the K^{2/3} total in T1 is exactly compensated by the heights. Whole level sets at a common height sit exactly on the (HC′) line (excess 0).
- **What is now the floor (method statements, not lower bounds).**
  - (i) Height-1 pairs: Lemma M′ at K ≍ 1 and N ≍ √p gives E ≍ N^{8/3} = p^{4/3}.
  - (ii) The Young bound on g < p^{-1/6}.
  - (iii) T3 at height p^{-1/6}.
  - So point–line pricing cannot go below sup C, X, E^×(h) = p^{4/3} with these inputs.
  - Going lower would need, together:
    - a height-1 pair-energy bound below N^{8/3} for level sets (MPRRS Lemma 33 gives N^{5/2} only for structured products; Round 186 §6.3);
    - an input for light levels below p^{-1/6} (a prime-only input, as Round 182 Prop. 4 says).
  - The one-match target O(p^{3/2}) still needs a non-point–plane input (floor p^{7/4}), and the generic six-word class below p^{9/2}. Nothing here changes that.

## 8. Looking for an (HC′)-violating model

The mission asked for a model of admissible level sets violating (HC′). Theorem 1 rules out a violation by a power of p for every admissible law with the cap. What remains is the size of the logarithmic factor, which is not examined.

The evidence in §9 also shows the models sit far inside the bound. The tailored laws were:
- an interval of characters (level sets are log-intervals);
- a two-dimensional progression (Bohr-type level sets);
- r random translates of an interval (level sets of near-extremal size ≍ √p/a at heights ≍ 1/r, irregular subsets of a long log-interval);
- a half-random mixture.

In all of them:
- the (HC′) ratio E(S_a;S_{a′})(aa′)²/p^{4/3} is ≤ 1.2·10^{-3};
- the measured K of level sets is 1.3–34, below the S1 bound;
- the Lemma M′ subset B is the whole set (|B|/m ≈ 1), against the guaranteed m/(4L₀√K).

## 9. Evidence (floating point; tailored laws; not certificates)

`paley-187-pair-models.py 10000189` (p = 10 000 189, 377 s) computes g = |f|² by FFT for six laws, all with n max ν/√p ≤ 1. It works at heights a = p^{-e}, e ∈ {0.02, 0.05, 0.08, 0.11, 0.14, 1/6} (a from 0.72 down to 0.068), and computes every energy by FFT over Z/(p−1) in discrete-log coordinates.

| law | E^×(h)/p | E^×(h)/p^{4/3} | max over height pairs of E(S_a;S_{a′})(aa′)²/p^{4/3} | measured K(S_a) (S1 bound) | |B|/m | max E(A;B)/T1 |
|---|---|---|---|---|---|---|
| dir (log-interval level sets) | 1.880 | 0.0087 | 1.2·10^{-3} | 1.50 (3.1–138) | 1.000 | 1.2·10^{-2} |
| dir2d (Bohr-type) | 1.338 | 0.0062 | 2.4·10^{-4} | 2.18 (6.4–105) | 1.000 | 1.1·10^{-2} |
| blocks4 | 1.160 | 0.0054 | 8·10^{-5} | 2.1–4.4 (12–62) | ≥ 0.95 | 1.7·10^{-2} |
| blocks8 | 1.040 | 0.0048 | 5·10^{-5} | 2.8–14.1 (25–65) | ≥ 0.97 | 1.8·10^{-2} |
| blocks16 | 1.004 | 0.0047 | 3·10^{-5} | 5.1–33.9 (48–214) | ≥ 0.97 | 1.1·10^{-2} |
| dirmix | 0.066 | 0.0003 | < 10^{-5} | 1.50 (52–183) | 1.000 | 1.1·10^{-2} |

Here T1 is the first term of Lemma M′ without constants or logarithms, the partner A is the largest level set, and the guaranteed |B|/m = 1/(4L₀√K) is 0.005–0.11.

**Adversarial Lemma M′ test** (`--adversarial 100049 1000033`). R is a log-interval {g₀^k : k ≤ m} and 1 − A is the same log-interval, so the partner correlates multiplicatively with 1 − R as much as possible. At m = p^{0.50}, …, p^{0.65}:
- K = 1.5 and |B| = m;
- E(A;B)/(T1+T2+T3) lies in 0.012–0.069 and grows mildly with m (the generic |A|²|B|²/p term starts to matter);
- E(A;B)/(|A||B|min) ≤ 0.019.

**Readings.**
- Every measured K is below the Lemma S1 bound, as it must be.
- In every law the popular-quotient subset B is essentially all of R. The proof's guarantee |B| ≥ m/(4L₀√K) is very pessimistic for these laws.
- E^×(h) ≈ p in every law. The proved p^{4/3} is far from sharp in these models, as Round 182's evidence (shifted energies near N²) already suggested.
- The blocks laws give level sets of near-extremal size (|S_a|a/√p up to 0.31) at heights down to p^{-1/6}, and the largest measured K (34, at height p^{-0.08}).
- None of this tests an exponent. It shows no sign of a configuration near the proved bounds.

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved here.** These are ordinary arguments from accepted inputs plus Stevens–de Zeeuw Theorem 4. Exponent algebra is in exact Fractions. The combinatorial identities and inequalities of Lemma M′ are checked exactly at p ≤ 97.
- **(a1) Lemma C.** Stevens–de Zeeuw for Cartesian products with no characteristic hypothesis, at the cost of the term \(sb^{1/2}np^{-1/2}\). Elementary chunking.
- **(a2) Lemma M′.** For A, R ⊆ F_p∖{0,1} there is B = B(R) ⊆ R with |B| ≥ m/(4L₀√K) and
  \(E(A;B)\ll L_0^{4/3}\alpha^{5/3}|B|^{2/3}K^{2/3}m^{1/3}+L_0K\alpha|B|+L_0\alpha^2|B|(Km)^{1/2}p^{-1/2}\).
  Its hypotheses are only these: A and R are finite subsets of F_p∖{0,1} and K = m³/E^×(R). No size, doubling or characteristic condition.
- **(a3) Proposition P′.** The pair price of extraction components without BSG: \(a_sa_gE(X_s;X_g)^{1/2}\ll(\log p)^{4/3}p^{2/3}\) for heights ≥ c p^{-1/6}, with the structured side chosen by smaller u.
- **(a4) Theorem 1.** (HC′) on [c p^{-1/6}, 1] for arbitrary subsets of level sets, with a (log p)^{20/3} loss.
- **(a5) Theorem 2.** \(E^\times(h)\ll p^{4/3}(\log p)^{32/3}\).
- **(a6) Corollary 3.**
  - \(\sup_{\lambda\ne1}C(\lambda)\ll p^{4/3}(\log p)^{32/3}\);
  - \(\sum W^{3/2},\ \mathcal E(\mu)\ll p^{8/3}(\log p)^{16/3}\);
  - one-match covariance \(O(p^{43/24}(\log p)^{4/3})\).
- **(a7) Corollary 4** (stated separately): \(X,\ \max W,\ 4\mathcal M_w\ \le E^\times(h)\ll p^{4/3}(\log p)^{32/3}\).
- **(a8) Method statements** (§7): the excess identities; the exact (11/12)u_s difference from Round 186's Prop. P; the floor p^{4/3} of this pricing.

**Hypotheses for (a3)–(a7).** (H1)/(H2) with the cap n max ν ≤ C_cap√p, for large primes p ≡ 1 (mod 4); these are the hypotheses of the accepted Round 180/185/186 bounds. **No (NC) input.** Inherited inputs:
- Lemma S1 (Rounds 163/173/182);
- Round 185 Lemma 5 (for (a6), (a7));
- Round 182 Prop. 1(iv) (for \(\mathcal M_w\));
- the Round 178/180/184 chain (for (a6)).

**Not used:** Reiher–Schoen BSG, Lemma SE, Lemma M, Round 185 Lemma 4, the SdZ quadrilinear price, MPRRS Lemma 33, Γ₂, Lemma Y.

**(b) Conditional.** None of the headline statements is conditional.
- The mission's partial-target formula δ_C = (1/24)/(1 + 8κ/5) is superseded: the pair excess is κ = 0, so the formula's value is its maximum, 1/24.
- Statements beyond p^{4/3} would need inputs not available (§7).

**(c) Evidence.**
- Exact small-p checks of Lemma M′ (90 cases).
- Floating models at p ≈ 10^7 with heights p^{-e}, e ≤ 1/6 (§9), and an adversarial Lemma M′ test (1 − A a log-interval of the same ratio as R) at p ≈ 10^5, 10^6.
- The float LP cross-check of the excess polytope.

## Remaining gap

- **One-match.** Covariance \(p^{43/24+o(1)}\approx p^{1.791667}\). This is the floor of point–line pricing (scheme floor of the Round 186 audit). It remains above the point–plane floor p^{7/4} and the target p^{3/2}. Going below 43/24 inside this chain needs sup C below p^{4/3}, which needs both of the following (§7):
  - a height-1 pair-energy bound below N^{8/3};
  - an input for light levels below p^{-1/6}.

  Reaching O(p^{3/2}) still needs a non-point–plane input and the generic six-word class below p^{9/2}.
- **First mass.** X, \(\mathcal M_w\) = O(p^{4/3+o(1)}), against the target p^{1+1/1280}. The Young bound on light levels g < p^{-1/6} is the only remaining obstruction inside this method. A prime-only input at light levels is still needed.
- **Support energy** Γ₂: unchanged. The generic J sum, zero-match, and the Round 176/180 fixed-a generic squared mass (bookkeeping: propagate sup C = p^{4/3+o(1)}) are unchanged.
- **Logarithms.** All bounds carry (log p)^{O(1)}. The mission's (HC′) and "O(p^{4/3})" are reached only up to these factors (p^{o(1)}). Removing them was not attempted.
- **The original target** (the ordinary Lovász theta limit) is not proved or refuted by anything here.

**Review needed.** The auditor should check:
1. Lemma M′ Step 4, in particular the cancellation of η between the incidence count (factor η) and |F|^{1/2} (factor η via (2.1)), and the threshold H_*;
2. that B depends only on R, so that one extraction serves every partner;
3. Lemma C's chunking, including the orientation swap and the trivial branch s b² > n_j³ inside each chunk;
4. Lemma S1 for remainders of every size (Round 186 audit §2.2 already accepts this);
5. the piece sums in Proposition P′ (\(\sum|B|^{1/3}\), \(\sum|B|^{1/2}\) through min |B|) and the slack μ ≥ −e − O(1/log p), e ≤ 1/6 + O(1/log p);
6. the exact excess identities (script);
7. the use of Round 185 Lemma 5 to pass from E^×(h) to sup C and X.

## Replay

| script | SHA-256 |
|---|---|
| `research/paley-187-pair-exponents.py` | `4e217ec60a63afaeb2e94af3af3f4cc8c05e81203c83141631796d10b6a4780e` |
| `research/paley-187-pair-lemma-check.py` | `6a911ded24545ae6f677a0bd87cb02a1bb72f212dc28011e38b050bbc709fa36` |
| `research/paley-187-pair-models.py` | `01a8baca6f0c3d0ee401afb3cf05f2b3b2238c3c1ae0462a674341d96739321c` |

```bash
.venv/bin/python -B research/paley-187-pair-exponents.py --lp
```
Exact Fractions and exact vertex enumeration, plus a float LP (numpy, scipy). Under 2 s. The output ends `ALL OK`.

```bash
.venv/bin/python -B research/paley-187-pair-lemma-check.py
```
Exact integers at p = 13, …, 97, 90 cases. About 5 s. The output ends `EXACT CHECKS OK`.

```bash
.venv/bin/python -B research/paley-187-pair-models.py 10000189
.venv/bin/python -B research/paley-187-pair-models.py --adversarial 100049 1000033
```
Floating point; evidence only. The first takes about 6.5 minutes; the second about 6 s. The `--adversarial` mode was added after the p ≈ 10^7 run; the main-mode code it used is unchanged.

## What would change the proof plan

- **If an audit accepts Theorem 2 and Corollary 3:**
  - the one-match exponent moves from 2125/1184 to the point–line scheme floor 43/24 (up to logarithms), and δ_C to 1/24;
  - Round 186's Theorem B, its Reiher–Schoen dependence and the BSG-ceiling discussion become historical;
  - the mission's lever (a K-free or BSG-free level-set input) is closed: it gives exactly the floor;
  - the X / first-mass form of `cand:slope-row-mass-x` moves to 4/3, so the coordinator should record that this call touched it.
- **Next levers:**
  - for one-match below 43/24: a height-1 pair-energy input below N^{8/3} for level sets, together with a light-level input; or, below 7/4, a non-point–plane input;
  - for the first mass: a prime-only light-level input (the Young barrier at p^{-1/6} is now the only obstruction inside this method).
- **Recommended bookkeeping:**
  - propagate sup C = p^{4/3+o(1)} to the Round 176/180 fixed-a generic squared mass;
  - record (HC′) as proved up to logarithms (Theorem 1).

## Verdict

**Supported.**
- (HC′) holds for all a, a′ ∈ [c p^{-1/6}, 1] and all subsets U ⊆ S_a, U′ ⊆ S_{a′}, up to a (log p)^{20/3} factor (Theorem 1).
- Consequently \(\sup_{\lambda\ne1}C(\lambda)\ll p^{4/3}(\log p)^{32/3}\) and the one-match covariance is \(O(p^{43/24}(\log p)^{4/3})\): pair excess κ = 0, δ_C = 1/24 (against κ = 11/12, δ_C = 5/296 in Round 186).
- The input is a BSG-free popular-quotient form of Lemma M (Lemma M′) whose structured side uses Lemma S1 directly, plus an elementary chunked form of Stevens–de Zeeuw Theorem 4. **No new external theorem; Reiher–Schoen is no longer used; no near-critical input.**
- Separately: X, max W and \(4\mathcal M_w\) are ≪ p^{4/3}(log p)^{32/3}. The first-mass target is untouched.

This is an agent draft awaiting audit. It does not prove or refute the ordinary theta-limit target.
