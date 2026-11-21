# Round 190 native Claude draft: stocktake of the ordinary obligation map

- **Author:** Claude subagent started by the Round 190 coordinator (session/r190-stocktake). Call id `ordinary-obligation-map-stocktake`.
- **Status:** agent draft, written while the user was asleep. It is not an acceptance record, a human review or a mathematical certification. No new estimate is proved. A few steps compose accepted inequalities; each is marked **bookkeeping (unaudited)** and is not an accepted statement.
- **Mission:** `coordination/missions/round-190/ordinary-obligation-map-stocktake.md`, exported from `coordination/round-189.json` (SHA-256 `8901a11c…ce822`, matches).
- **Sources checked (SHA-256 all match the mission):** `research/round-188-acceptance.json` (`e0face6c…dcc6`), `research/round-189-acceptance.json` (`ad4e0b5a…6506`), `research/native-claude-audit-189.md` (`0bf8b1c3…7f508`), `research/native-claude-ordinary-prime-beyond-point-plane-188.md` (`cee51251…21919`), `research/ordinary-weighted-affine-vertical-saving-173.md` (`61e959f2…2023`), `research/ordinary-weighted-slope-product-incidence-178.md` (`9e4589c6…1d71`).
- **Also read:** acceptance records 152–154 and 162–189 (`proof_scope`, `failed_paths_and_open_bounds`), the ledger for Rounds 140–180, and the route notes of Rounds 152, 154, 160, 162–169, 171, 172, 179, 180, 183, 184, 187.
- **Script:** `research/paley-190-stock-exponents.py`. It uses exact Fractions and checks every exponent conversion below. Run it with `python3 research/paley-190-stock-exponents.py`.

Citations have the form "R*n* file:line". "acc" means `research/round-n-acceptance.json`. Exponents are powers of \(p\). Here \(G=\sum g\asymp\sqrt p\), \(w=g(1-g)\) and \(W=\sum_t w(t)\). A trailing \(+o(1)\) stands for the logarithmic factors that the source carries.

---

## 0. Answer in brief

1. **One-match \(O(p^{3/2})\) is a sufficient choice, not a requirement of the chain.** Its requirement first appears in Round 164/166. There, Cauchy–Schwarz converts the first-moment target \(O(p)\) for a fixed moderate slope block into a second-moment target \(O(p^{3/2})\) (R164 acc:194; R166 acc:207). The full physical diagonal \(\mathcal D=\sum_s w(s)P_s^2\) carries this second-moment target (R172 `ordinary-full-diagonal-affine-172.md`:3–7). It equals the ≥2-match, one-match and zero-match classes added together, up to \(O(p^{3/2})\). The zero-match class has no recorded sign. So the target constrains only the sum one + zero, not the one-match class alone.
2. **There is no power or logarithmic slack anywhere in the chain.**
   - At the top, the contradiction needs the block bound \(O(p)\) with no logarithm. The forced lower bound is \(\omega(p)\) with no recorded rate (R152 `ordinary-affine-correlations-152.md`:65–69).
   - The Cauchy–Schwarz step loses nothing in order, since \(W\asymp\sqrt p\) on (NC).
   - A one-match class at \(p^{3/2+\varepsilon}\), \(p^{7/4-\delta}\) or \(p^{43/24}\) could be absorbed only by a matching negative zero-match class. No accepted statement provides one.
3. **A single obligation closes the fixed moderate block on its own, without one-match, zero match or the generic J sum.** It is the **first mass \(\mathcal M_w=\sum_s w(s)P_s=O(p)\), with no logarithm** (bookkeeping, §2 L3).
   - Its proved value is \(p^{4/3+o(1)}\) (R187 acc:272, Corollary 4): a gap of \(1/3\) in its own units.
   - Every route through the diagonal is at \(p^{9/4}\) (R179 acc:248). Its gap is \(3/4\) in covariance units, or \(3/8\) in first-moment units.
   - The first-mass route is therefore the closest *closing* route, by \(1/24\) in first-moment units.
   - Taken alone, the one-match piece is the nearest individual piece: \(7/24\) in covariance units, \(7/48\) in first-moment units. But it closes nothing by itself.
4. **Zero match has no recorded exponent.**
   - The Katz bound used in Round 168 gives \(p^{5/2}\) implicitly.
   - Subtracting from the full diagonal gives \(-O(p^{43/24+o(1)})\le\text{zero}\le O(p^{9/4})\) (bookkeeping).
   - **The generic J sum** is recorded only as \(\mathcal D_{\rm gen}\le\mathcal D=O(p^{9/4})\) (R180 `ordinary-paired-J-cross-ratio-180.md`:78).
5. **Verdict: yes, with qualifications** (§8). The slack is structural only: one-match is not necessary, and the first mass is a closer closing obligation. There is no exponent slack. The first mass faces the same kinds of method barriers.

---

## 1. The accepted reduction, link by link

Each link reads "requirement above ⇐ requirement below". The label says whether the lower requirement is **necessary for this chain** (the chain fails without it) or a **sufficient choice**.

### L0. Contradiction: the deficit-weighted fourth moment must be \(O(p)\)

- R152 `ordinary-affine-correlations-152.md`:65–69 proves \(\frac1p\mathbb E_\nu\sum_{u\ne1}|C_a(u)|^2\to\infty\) on the critical branch. An \(O(p)\) upper bound excludes that branch. R152 acc:152 states the target in the same form.
- The divergence comes from \(L^2(1+D)\log(\cdots)\gg\min(\eta^{-1/2},p^{1/4})\) with \(\eta=O(d_a+L/\sqrt p)\) and \(d_a=o(1)\) (R152 `ordinary-affine-correlations-152.md`:8–13, 37–39, 65). No accepted record gives a rate for \(d_a\). R183 acc:270 and R184 acc:278 record the near-critical \(o(1)\)s as unquantified.
- **Necessary for this chain:** \(O(p)\), logarithm-free. Slack at this level would need a quantitative rate for \(d_a\), which cannot be recovered.

### L1. The favorable Legendre off-diagonal must be \(O(p)\), signed

- R153 acc:158: the moment equals \(p^{3/2}\) times a phase average, up to \(O(p)\). Its degeneracies cost \(O(p)\).
- R154 `ordinary-lift-and-gauss-kernel-154.md`:93: the wrong sign and the diagonal cost \(O(p)\), so "the actual remaining test is an \(O(p)\) signed upper on the favorable off-diagonal". R154 acc:155 states the same.
- **Necessary for this chain**, given that the other parts are paid at \(O(p)\).

### L2. Blocks: the fixed moderate slope block must be \(O(p)\)

- On a block with fixed squared vertex thresholds \(a,b\) and slope set \(D\), the absolute value is at most \(\sum_{t\in D}|f(t)|\,N_t\) (R162 `ordinary-physical-slope-fiber-count-162.md`:23–30; R164 `ordinary-physical-pair-slope-pinning-164.md`:47–54).
- Pieces already paid at \(O(p)\):
  - vertex sites with \(|F|\le C/\sqrt p\) (R160 `ordinary-matched-physical-truncation-160.md`:27);
  - quadratically small pair cuts (R160 `ordinary-matched-physical-truncation-160.md`:31–38);
  - three of the five amplitudes at or below \(p^{-1/2}\) (R160 `ordinary-rank-two-slope-orthogonality-160.md`:61);
  - low slope bands \(|f|^2\le p^{-\sigma}\) with \(\sigma\ge1-2\gamma\) at fixed vertex thresholds (R164 `ordinary-physical-pair-slope-pinning-164.md`:54), or \(\sigma\ge26/27\) when both thresholds exceed \(1/2\) (R163 `ordinary-shifted-layer-energy-saving-163.md`:80).
- R164 acc:206 records the remaining core as open: "The full O(p) moderate band remains open."
- **Necessary for this chain:** the fixed moderate block \(=O_{a,b,s_0,s_1}(p)\) for every fixed \(0<s_0\le s_1<1\) and fixed \(a,b>0\).
- **Cannot be recovered:** how the growing pieces are assembled, together with the fixed blocks, into the whole favorable off-diagonal. These are the slope bands \(p^{-(1-2\gamma)}<g<s_0\to0\), the near-unit slopes \(g\to1\) (R159 `ordinary-quantitative-near-unit-slope-159.md`:100: "does not control \(S_{\rho,1}\) at the required \(O(p)\) scale"), and vertex layers between \(C/\sqrt p\) and fixed thresholds. R163 `ordinary-shifted-layer-energy-saving-163.md`:66 says it "leaves fixed moderate slopes and the uncut ordinary target open". See §6.

### L3. Positive majorant and the first mass (bookkeeping composition)

- R166 `ordinary-regular-character-collisions-166.md`:9: \(N_t\le(a^2b^2)^{-1}P_t\) for \(t\in D\), where \(P_t\ge0\) is the completed four-\(g\) majorant.
- R166 `ordinary-regular-character-collisions-166.md`:44: on the band, \(w(t)\ge s_0(1-s_1)\).
- So, with \(|f|\le1\):
\[
\text{block}\le \frac{1}{a^2b^2\,s_0(1-s_1)}\sum_t w(t)P_t=\frac{\mathcal M_w}{a^2b^2s_0(1-s_1)},\qquad
\mathcal M_w=\sum_s w(s)P_s
\]
  as defined in R180 `ordinary-paired-J-cross-ratio-180.md`:52.
- **This composition is bookkeeping (unaudited).** It uses only the three cited accepted inequalities. No accepted record states it; the search in §6 found none.
- For the chain that passes through the R166 majorant:
  - **Necessary:** \(\sum_{t\in D}P_t=O(p)\) on every fixed band.
  - **Sufficient:** \(\mathcal M_w=O(p)\), with no logarithm.

### L4. Cauchy–Schwarz: the full diagonal must be \(O(p^{3/2})\)

- The accepted records choose the second moment.
  - R164 acc:194: "O(p^1.5) suffices by the true slope counting second norm."
  - R166 `ordinary-regular-character-collisions-166.md`:27, 44–46: "a sufficient next estimate is \(\sum_t g(1-g)|P_{\rm gen}(t)|^2=O(p^{3/2})\)".
  - R166 acc:207: "a sufficient weighted covariance reduction".
- R172 `ordinary-full-diagonal-affine-172.md`:3–7 restates this as \(\mathcal D=\sum_{s\ne0,1}w(s)P_s^2=O(p^{3/2})\), "independent of the matching split".
- R180 `ordinary-paired-J-cross-ratio-180.md`:54–56 contains the step \(\mathcal M_w\le W^{1/2}\mathcal D^{1/2}\), with \(W\le G\).
- **Sufficient choice.** \(\mathcal D=O(p^{3/2})\Rightarrow\mathcal M_w=O(p)\). The converse fails.
- **No order loss in this step on (NC).** \(W=G-\Gamma_{\rm tot}\) (R188 `native-claude-ordinary-prime-beyond-point-plane-188.md`:79). Also \(G=(1+o(1))\sqrt p\) and \(\Gamma_{\rm tot}\le(\frac12+o(1))\sqrt p\) (R183 acc:264, Propositions 1.2 and 1.4). So \(W\ge(\frac12-o(1))\sqrt p\). The script checks that \(\frac12\cdot\frac12+\frac12\cdot\frac32=1\).

### L5. The quadratic form splits by matches

- R166 `ordinary-regular-character-collisions-166.md`:40, 50–54:
  - \(P_t-P_{\rm gen}(t)=O(\sqrt p)\) for \(t\ne1\);
  - \(\sum_t w|P_{\rm gen}|^2\) equals the \(\ell\)-weighted quadratic form exactly, with \(\ell=\omega-\omega*\omega\).
- R167 `ordinary-Gauss-covariance-pair-cuts-167.md`:32–54 (acc:207):
  - the classes with 2, 3 and 4 matches cost \(O(p^{5/2}\kappa^2)\), \(O(p^2\kappa^3)\) and \(O(p^3\kappa^4)\), all \(O(p^{3/2})\);
  - deleted frequencies cost \(O(p^{3/2})\) (lines 56).
- R168 `ordinary-one-match-positive-form-168.md`:9, 26–29 (acc:209–210): the true one-match class is \((p^3/m)\mathcal P_1+O(p^{3/2})\) with \(\mathcal P_1\ge0\). This is the source of the one-match target \(\mathcal P_1=O(p^{-1/2})\), i.e. covariance \(O(p^{3/2})\).
- So, up to \(O(p^{3/2})\) and a cross term \(O(p^{3/4}\mathcal D^{1/2})\),
\[
\mathcal D=\underbrace{[\ge2\text{ matches}]}_{O(p^{3/2})}+\underbrace{\text{one}}_{\ge -O(p^{3/2})}+\text{zero}.
\]
- **Within the split route, one-match \(O(p^{3/2})\) is necessary only for an argument that bounds each class in absolute value.** For the target \(\mathcal D=O(p^{3/2})\) itself, only one + zero \(=O(p^{3/2})\) is needed, because zero match has no recorded sign.

### L6a. One-match: criterion, Theorem A, \(T_0\) and \(X\)

- R169 `ordinary-one-match-twisted-physical-169.md`:22–24: \(\mathcal P_1=O(p^{-1/2})\iff\sum_{s\ne1,t}w(t)|H_\sigma(s,t)|^2=O(p^{5/2})\). This is an equivalence at scale.
- R188 acc:275 (Theorem A), R188 `native-claude-ordinary-prime-beyond-point-plane-188.md`:31, 192–202, 237. Under \(\omega\ge0\) and (H3):
\[
\text{one-match}\ll p^{3/2}+\min(W\,T_0,\ \mathcal T/4)\le p^{3/2}+\min(W,\Gamma_{\rm tot}/4)\,X .
\]
- **Sufficient choices** for one-match \(O(p^{3/2})\): \(T_0=O(p)\), \(X=O(p)\) with no logarithm, \(\mathcal T=O(p^{3/2})\), \(\Gamma_{\rm tot}=O(p^{1/4})\), \(E_{\ne1}(\mu)=O(p^2)\), or the six-word class (R188 acc:279).
- Since \(W\asymp\sqrt p\) on (NC), the \(W T_0\) branch needs \(T_0=O(p)\) exactly, with no logarithm. \(X=O(p)\) is at its floor, because \(X\ge(2-o(1))p\) on (NC) (R184 acc:271, Proposition 2; R184 `native-claude-ordinary-prime-near-critical-slope-row-mass-184.md`:31, 131).

### L6b. The diagonal in J classes

- R179 `ordinary-affine-triple-diagonal-179.md`:27–51 (acc:248): \(\mathcal D\le\sum_{h\in{\rm Aff}}m(h)^3=O(pG^2+G^{9/2}+G^6/p)=O(p^{9/4})\). Here \(D,D'\), the masks and \(w\) are bounded by one.
- R180 `ordinary-paired-J-cross-ratio-180.md`:5, 49–78 (acc:253): \(\mathcal D=\sum_c\mathcal D_c\) with every \(\mathcal D_J\ge0\), and
  - \(\mathcal D_0+\mathcal D_1\le4R_*\mathcal M_w\), with \(R_*=O(p^{1/2-1/1280})\) (R173 `ordinary-weighted-affine-vertical-saving-173.md`:12–40);
  - \(\mathcal D_J\le2G\mathcal M_w\) for each \(J\notin\{0,1\}\);
  - \(\mathcal D_{\rm gen}\le\mathcal D=O(p^{9/4})\).
- Because every \(\mathcal D_J\ge0\), both \(\mathcal D_0+\mathcal D_1=O(p^{3/2})\) and \(\mathcal D_{\rm gen}=O(p^{3/2})\) are **necessary for the diagonal route**.
- \(\mathcal M_w=O(p^{1+1/1280})\) is a **sufficient choice** for \(\mathcal D_0+\mathcal D_1\) given \(R_*\) (R180 `ordinary-paired-J-cross-ratio-180.md`:65).
- R183 acc:262 (Proposition B) shows that \(X=O(p^{1+1/1280})\) is equivalent to the rich-fibre criterion, which implies that sufficient choice.

---

## 2. Piece by piece

For each piece: **(a)** the size needed and its normalisation; **(b)** the best proved value, with round and file; **(c)** whether it is necessary or sufficient, and where it enters; **(d)** external inputs.

### P1. One-match covariance

- **(a)** \(O(p^{3/2})\) in the original covariance normalisation of R166/167. Equivalently \(\mathcal P_1=O(p^{-1/2})\) (R168 `ordinary-one-match-positive-form-168.md`:29), or \(\sum w|H_\alpha|^2=O(p^{5/2})\) (R169 `ordinary-one-match-twisted-physical-169.md`:24).
- **(b)** \(O(p^{43/24}(\log p)^{4/3})\) (R187 acc:272, Corollary; unchanged at R188 acc:279 and R189 acc:290). Theorem A alone gives \(p^{11/6+o(1)}\) (R188 acc:275).
- **History:**
  - \(15/8\) (R171 acc:218);
  - \(29/16\) with a logarithm (R172 acc:219);
  - \(29/16-1/5120\) (R173 acc:228; R173 `ordinary-weighted-affine-vertical-saving-173.md`:61);
  - \(29/16-3/3344\) (R178 acc:231; R178 `ordinary-weighted-slope-product-incidence-178.md`:62);
  - \(115/64\) (R180 acc:252);
  - \(1193/664\) (R185);
  - \(2125/1184\) with a logarithm (R186);
  - \(43/24\) (R187).
- **(c)** **Sufficient choice.** It enters only the split route of L5, and there only through the sum one + zero.
  - It is not needed on the first-mass route (L3).
  - It is not needed on the J route (L6b), which bounds \(\mathcal D\) directly.
  - Wording differs between records. R173 `ordinary-weighted-affine-vertical-saving-173.md`:61 calls the \(O(p^{3/2})\) bound "necessary"; R178 `ordinary-weighted-slope-product-incidence-178.md`:62 calls it "sufficient". The latter is accurate for the chain.
- **(d)** External inputs:
  - Round 187 lists Stevens–de Zeeuw arXiv:1609.06284v4 Theorem 4 as its only external theorem (Lemmas C, M′, P′). The audit advises a human read of Lemma M′ (R188 `native-claude-ordinary-prime-beyond-point-plane-188.md`:98).
  - It passes through the Round 178 chain: Petridis–Roche-Newton–Rudnev–Warren Lemmas 3.1–3.2 and (9), and Rudnev–Shkredov Theorem 8 and (22) (R178 `ordinary-weighted-slope-product-incidence-178.md`:11, 39–50).
  - It also uses the R184 output \(p^{1/8}E^{1/4}M_1\) (R184 acc:270).
  - Theorem A uses only Gauss sums and orthogonality, plus \(\omega\ge0\) and (H3).
  - Katz is used for the deletions (R168 `ordinary-one-match-positive-form-168.md`:7–9).

### P2. Zero-match class

- **(a)** \(O(p^{3/2})\) in the same normalisation, but only on the split route of L5, and only together with one-match.
- **(b)** **No exponent is recorded in any acceptance record.** R167 `ordinary-Gauss-covariance-pair-cuts-167.md`:54, 56 and R168 `ordinary-one-match-positive-form-168.md`:29 say it is separate. Every later record lists it as unchanged. Two bounds follow from accepted statements; neither is an accepted statement:
  - **Katz-implied \(O(p^{5/2})\).** The complete \(4+4\) normalised correlation is at most \(4m/\sqrt p\) (R168 `ordinary-one-match-positive-form-168.md`:7). The prefactor is \(p^3/m\) and \(\|\ell\|_1\le2\) (R167 `ordinary-Gauss-covariance-pair-cuts-167.md`:48). The zero-match class has no cap gain (line 56).
  - **Subtraction (bookkeeping, unaudited).** From L5, \(\sum w|P_{\rm gen}|^2\ge0\), \(\le2\mathcal D+O(p^{3/2})\), the one-match class is at least \(-O(p^{3/2})\), and the ≥2 classes are \(O(p^{3/2})\). Together these give
\[
-O(p^{43/24+o(1)})\ \le\ \text{zero}\ \le\ O(p^{9/4}).
\]
- **(c)** **Sufficient choice.** It is needed only on the split route. Even there, only one + zero must be \(O(p^{3/2})\).
- **(d)** Katz (from Clausen to Carlitz, §§2.1–2.3). The subtraction bound also inherits every input of R179.

### P3. Full diagonal \(\mathcal D=\sum_s w(s)P_s^2\) (the slope criterion)

- **(a)** \(O(p^{3/2})\) (R172 `ordinary-full-diagonal-affine-172.md`:7).
- **(b)** \(O(p^{9/4})\) with no logarithm (R179 acc:248; R179 `ordinary-affine-triple-diagonal-179.md`:5, 51).
- **History:**
  - \(19/8\) and \(37/16\) with a logarithm (R172);
  - \(37/16\) (R173);
  - \(37/16-1/4320\) (R176);
  - \(37/16-1/4320-1/512\) (R177);
  - \(3673/1600\) (R178);
  - \(9/4\) (R179).
- **(c)** **Sufficient choice** for L3, through Cauchy–Schwarz (L4).
  - **Method floor of the R179 route (bookkeeping).** The displayed terms \(pG^2\) and \(G^6/p\) of \(\sum_h m(h)^3\) (R179 `ordinary-affine-triple-diagonal-179.md`:43, 51) are each \(\asymp p^2\) on (NC).
  - By Hölder over the \(p(p-1)\) affine maps, \(\sum_h m(h)^3\ge(p-1)G^6/p^2\asymp p^2\), using \(\sum_h m(h)=(p-1)G^2\) from line 38.
  - So the route that bounds \(D,D'\), \(w\) and the masks by one cannot reach \(p^{3/2}\).
- **(d)** Rudnev–Shkredov (22) for the rich-line count; transitivity of the affine group; inversion symmetry of \(g\).

### P4. \(\mathcal D_0+\mathcal D_1\) (the J classes 0 and 1)

- **(a)** \(O(p^{3/2})\), necessary on the diagonal route.
- **(b)** \(O(p^{2399/1280})\) (R180 acc:253; R180 `ordinary-paired-J-cross-ratio-180.md`:60). R180 used \(\mathcal M_w=O(p^{11/8})\).
  - **Bookkeeping (unaudited).** Substituting R187's \(\mathcal M_w\ll p^{4/3+o(1)}\) into \(4R_*\mathcal M_w\) gives \(p^{11/6-1/1280+o(1)}=p^{7037/3840+o(1)}\).
  - Round 185 acc:264 says the downstream exponents of Rounds 176/180 were not re-derived.
- **(c)** \(\mathcal M_w=O(p^{1+1/1280})\) is a sufficient choice given \(R_*\). A better \(R_*\) would relax it, since only \(R_*\mathcal M_w=O(p^{3/2})\) is needed.
- **(d)** R173's \(R_*\): Reiher–Schoen Theorem 1.2 BSG (citation corrected at R183 acc:265), Zhelezov Theorem 1, and the cap/Jensen argument of R163.

### P5. Generic J sum \(\mathcal D_{\rm gen}=\sum_{J\notin\{0,1\}}\mathcal D_J\)

- **(a)** \(O(p^{3/2})\), necessary on the diagonal route because every \(\mathcal D_J\ge0\) (R180 `ordinary-paired-J-cross-ratio-180.md`:78).
- **(b)** Only \(\mathcal D_{\rm gen}\le\mathcal D=O(p^{9/4})\) (R180 `ordinary-paired-J-cross-ratio-180.md`:78; R182 acc:268).
  - Per class, \(\mathcal D_J\le2G\mathcal M_w=O(p^{15/8})\) (R180 line 76).
  - **Bookkeeping:** \(p^{11/6+o(1)}\) per class with R187's \(\mathcal M_w\). There are \(p-2\) classes, so this does not sum.
  - The open form is the bilinear Möbius kernel with all eight amplitudes and \(w\) kept (R180 lines 82–86).
- **(c)** **Sufficient choice** for the chain: it appears only on the diagonal route.
- **(d)** R179's inputs, plus absolute irreducibility of the fibre conic (R180 lines 69–74).

### P6. First mass \(\mathcal M_w=\sum_s w(s)P_s\)

- **(a)** Two requirements are recorded or implied:
  - \(O(p^{1+1/1280})\), sufficient for P4 (R180 `ordinary-paired-J-cross-ratio-180.md`:65; R183 acc:262);
  - **\(O(p)\) with no logarithm (bookkeeping, L3), which closes the fixed moderate block by itself.**
- **(b)** \(\mathcal M_w\le E^\times(h)/4\ll p^{4/3}(\log p)^{32/3}\) (R187 acc:272, Corollary 4; R187 `native-claude-ordinary-prime-level-pair-energy-187.md`:231). Earlier values: \(11/8\) (R180) and \(34/23\) via \(E^\times(h)\) (R182).
  - R187 acc:277: this is "at the extraction-plus-Young method cap".
  - There is no accepted lower bound for \(\mathcal M_w\) on (NC). Floating evidence shows \(\mathcal M_w/p\) flat in every model tested (R183 `native-claude-ordinary-prime-first-mass-fibre-dilation-183.md`:244). This is evidence, not proof.
- **(c)**
  - On the R166-majorant chain, the per-band form \(\sum_{t\in D}P_t=O(p)\) is **necessary**. The weighted form \(\mathcal M_w=O(p)\) is **sufficient**.
  - Admissible-only arguments face an obstruction. R183 `native-claude-ordinary-prime-first-mass-fibre-dilation-183.md`:113–128 (Proposition C, accepted at R183 acc:262) gives \(\mathcal M_w(g_H)=\frac3{4096}E_{\rm off}(H)\) exactly.
  - Hence an admissible-only proof of \(\mathcal M_w=O(p)\) must give \(E_{\rm off}(H)=O(p)\), with no logarithm, for every subgroup with \(|H|\le2C_{\rm cap}\sqrt p-1\). Known bounds have \(p\log p\) (R184 acc:271, Proposition 4; Shkredov Theorem 6 below \(\sqrt p\)).
  - The Corollary C1 of R183 is stated at exponent \(1+1/1280\); the same proof applies at exponent 1.
  - **Not recovered:** whether the R189 interval-law family also obstructs \(\mathcal M_w\) below \(p^{5/4}\). Round 189 states its cap for \(T_0\) and \(X\) only (R189 acc:286).
- **(d)** Stevens–de Zeeuw Theorem 4 (through R187 Theorem 2); R185 Lemma 5; R182 Proposition 1(iv).

### P7. Slope-row moment \(X=E_Q(h)=\sum_r m(r)^2\)

- **(a)** Requirements by use:
  - \(O(p)\) with no logarithm for one-match through Theorem A (R188 acc:275);
  - \(O(p)\) is also sufficient for \(\mathcal M_w=O(p)\), because \(\mathcal M_w\le(X-{\rm diag})/4\) (R182 acc:260; R188 `native-claude-ordinary-prime-beyond-point-plane-188.md`:84);
  - \(O(p^{1+1/1280})\) for P4 (R183 acc:262).
- **(b)** \(X\le E^\times(h)\ll p^{4/3}(\log p)^{32/3}\) (R187 acc:272). The floor is \(X\ge(2-o(1))p\) on (NC) (R184 acc:271).
- **(c)** **Sufficient choice** in every use.
  - **Bookkeeping:** \(X=O(p)\) alone closes the fixed block through \(\mathcal M_w\le X/4\). It needs neither the one-match nor the zero-match class.
  - Below \(p^{5/4}\), admissible-only arguments need (GP) (R189 acc:286).
- **(d)** As for P6. Primality is necessary: the square control over \(\mathbb F_{r^2}\) gives \(X\asymp q^{3/2}\) (R184 acc:271, Proposition 5).

### P8. \(T_0\) and \(\mathcal T\) (the Theorem A inputs)

- **(a)** \(T_0=O(p)\) or \(\mathcal T=O(p^{3/2})\), each sufficient for one-match (R188 acc:275).
- **(b)** \(T_0\le X\ll p^{4/3+o(1)}\).
- **(c)** **Sufficient**, for P1 only. Neither closes the block without zero match.
  - Below \(p^{5/4}\), admissible-only arguments need (GP), recorded as `cand:gp-shifted-energy` (R189 acc:286).
  - Beating \(43/24\) through this route needs the heavy-triangle sum below \(p^{31/24-\delta}\) (R189 acc:286, Proposition 5).
- **(d)** Gauss sums, orthogonality, (H3), \(\omega\ge0\). The obstruction uses MPRRS Lemma 33 (read at source).

### P9. Classes and pieces already paid at the target scale

These are closed, with their inputs:

- **≥2-match classes:** cap \(\kappa=O(p^{-1/2})\) and the exact \(r=2\) Jacobi evaluation (R167 acc:207).
- **Overlapping and \(h=1\) one-match subclasses:** Katz (R168 acc:209).
- **Same-\(z\) and argument-sharing collisions:** Young's inequality (R169 acc:214; R170 acc:214).
- **Endpoints and trivial-character loci:** the cap (R166 acc:206; R171 `ordinary-affine-line-energy-171.md`:82).

---

## 3. Is one-match \(O(p^{3/2})\) necessary? Where each requirement enters

The final inequality of the chain, for one fixed moderate block, is
\[
|\text{block}|\ \le\ C_{a,b,s_0,s_1}\,\mathcal M_w\ \le\ C\,W^{1/2}\,\mathcal D^{1/2},\qquad
\mathcal D=[\ge2]+\text{one}+\text{zero}+O(p^{3/2})=\mathcal D_0+\mathcal D_1+\mathcal D_{\rm gen}.
\]
The left side must be \(O(p)\) with no logarithm (L0–L2).

**Where each requirement enters:**

- \(\mathcal M_w=O(p)\) enters at the first inequality. It is the weakest requirement in this chain.
- \(\mathcal D=O(p^{3/2})\) enters at the second inequality, with \(W\asymp\sqrt p\). There is no slack: \(p^{3/2+\varepsilon}\) gives a block of size \(p^{1+\varepsilon/2}\).
- The one-match and zero-match classes enter only inside \(\mathcal D\), and only through their sum.
- \(\mathcal D_0+\mathcal D_1\) and \(\mathcal D_{\rm gen}\) enter inside \(\mathcal D\) as nonnegative summands. Each is necessary for \(\mathcal D=O(p^{3/2})\).

**Can a one-match class at \(p^{3/2+\varepsilon}\), \(p^{7/4-\delta}\) or \(p^{43/24}\) be absorbed?**

- On the **first-mass route**: the question does not arise, since one-match is not used.
- On the **diagonal route**: only if zero \(\le-\text{one}+O(p^{3/2})\), that is, with an exactly cancelling negative zero-match class.
  - No accepted record gives a sign or a size for zero match. So absorption cannot be verified.
  - Positivity alone does not forbid it: one-match \(\ge -O(p^{3/2})\), \(\mathcal D\ge0\), and zero match is unsigned.
- On the **split route with absolute values**: no. One-match must be \(O(p^{3/2})\).
- No accepted estimate elsewhere in the chain has headroom to absorb it:
  - the C-S factor \(W^{1/2}\) is tight in order;
  - the top-level \(O(p)\) has no recorded rate;
  - band constants are fixed.
- The answer is the same for all three sizes, \(p^{3/2+\varepsilon}\), \(p^{7/4-\delta}\) and \(p^{43/24}\).

---

## 4. Ranked table

The script `research/paley-190-stock-exponents.py` checks every entry.

- **Units.** "cov" is the covariance/diagonal normalisation, target \(p^{3/2}\). "fm" is the first-moment normalisation, target \(p\).
- **Conversion.** Under the tight C-S step, a covariance exponent \(3/2+\delta\) corresponds to a first-moment exponent \(1+\delta/2\).
- **"Closes alone?"** asks whether proving the target for this piece alone, given the pieces already paid, closes the fixed moderate block.

| rank by fm-gap | piece | target | current (round, file) | gap (own) | gap (fm) | closes alone? | status |
|---|---|---|---|---|---|---|---|
| 1 | one-match covariance | \(p^{3/2}\) | \(p^{43/24+o(1)}\) (R187 acc:272) | 7/24 | 7/48 | **no** (needs zero match too) | sufficient choice |
| 2 | \(\mathcal D_0+\mathcal D_1\) | \(p^{3/2}\) | \(p^{2399/1280}\) (R180 acc:253); bookkeeping \(p^{7037/3840+o(1)}\) | 479/1280 (1277/3840) | 479/2560 (1277/7680) | no (needs \(\mathcal D_{\rm gen}\)) | necessary on the diagonal route |
| 3 | **first mass \(\mathcal M_w\)** | \(p\), no log | \(p^{4/3+o(1)}\) (R187 acc:272, Corollary 4) | 1/3 | **1/3** | **yes** (bookkeeping, L3) | weakest sufficient form; per-band form necessary |
| 3 | \(X\) (for \(\mathcal M_w\) or one-match) | \(p\), no log | \(p^{4/3+o(1)}\) (R187 acc:272) | 1/3 | 1/3 | yes, through \(\mathcal M_w\le X/4\) (bookkeeping) | sufficient; at floor on (NC) |
| 5 | full diagonal \(\mathcal D\) | \(p^{3/2}\) | \(p^{9/4}\) (R179 acc:248) | 3/4 | 3/8 | yes | sufficient choice; R179 route floors at \(p^2\) |
| 5 | generic J sum | \(p^{3/2}\) | \(p^{9/4}\) via \(\le\mathcal D\) (R180:78) | 3/4 | 3/8 | no (needs \(\mathcal D_0+\mathcal D_1\)) | necessary on the diagonal route |
| 5 | zero match | \(p^{3/2}\) (with one) | not recorded; \(\le p^{9/4}\) bookkeeping, \(p^{5/2}\) Katz-implied | ≥3/4 | ≥3/8 | no | sufficient choice |
| — | \(T_0\) | \(p\), no log | \(\le X\ll p^{4/3+o(1)}\) | 1/3 | (one-match only) | no | sufficient for P1 |

**Route bottlenecks** (the largest gap among the pieces each route needs), in fm units:

| route | bottleneck |
|---|---|
| first mass \(\mathcal M_w\) | **1/3** |
| full diagonal | 3/8 |
| J split | 3/8 (\(\mathcal D_{\rm gen}\)) |
| one/zero split | 3/8 (zero match; no estimate of its own) |

**Closest:**

- The closest *individual* piece is the one-match covariance, at \(7/24\) in cov units. But closing it changes nothing on its own: the split route then waits on zero match, which has no estimate of its own.
- The closest *closing* obligation is the first mass \(\mathcal M_w=O(p)\) with no logarithm. It is ahead of the diagonal routes by \(1/24\) in fm units (\(11/8-4/3\), script line "M_w from C-S on D").

---

## 5. External inputs, consolidated

| input | used by |
|---|---|
| Stevens–de Zeeuw Theorem 4 (arXiv:1609.06284v4) | one-match, \(X\), \(\mathcal M_w\), \(T_0\) (R180, R182 Lemma SE, R185–R187) |
| Rudnev–Shkredov Theorem 8 and (22) | one-match (R178), full diagonal (R179) |
| Petridis–Roche-Newton–Rudnev–Warren Lemmas 3.1–3.2, (9) | one-match energy (R178) |
| Reiher–Schoen Theorem 1.2 BSG; Zhelezov Theorem 1 | \(R_*\) (R173), hence \(\mathcal D_0+\mathcal D_1\); no longer used in R187 |
| Katz, hypergeometric \((r,r)\) bound | ≥2-match subclasses and deletions (R168); implicit zero-match bound |
| Shkredov arXiv:1504.04522 Theorem 6 | \(\mathcal M_w\) on small coset supports only (R183, conditional input) |
| MPRRS Lemma 33 | the R189 method cap only (no proof uses it) |
| Gauss sums and orthogonality | Theorem A (R188) |
| near-critical (NC) facts (Round 20 gap theorem, Round 151 flattening) | floors \(X\ge2p\), \(W\asymp\sqrt p\), \(\Gamma_{\rm tot}\le(\frac12+o(1))\sqrt p\) |

---

## 6. What could not be recovered from the accepted files

1. **The zero-match class.** No accepted exponent, sign or positive form exists. The \(p^{5/2}\) and \(p^{9/4}\) values in §2 P2 are implied by accepted statements but are not stated in any record.
2. **Assembling the upstream blocks.** No accepted statement shows how the fixed moderate blocks, together with the closed cuts, cover the whole favorable off-diagonal at \(O(p)\). The gaps are:
   - slope bands with \(s_0\to0\) above \(p^{-(1-2\gamma)}\);
   - near-unit slopes;
   - vertex layers between \(C/\sqrt p\) and fixed thresholds.
   On such pieces, the \(w\)-weighted quantities of this chain lose a factor: \(p^{\sigma/2}\) on a slope band \(g\asymp p^{-\sigma}\), and \(1/(1-g)\) near unit slopes. So neither \(\mathcal M_w=O(p)\) nor \(\mathcal D=O(p^{3/2})\) covers these pieces as stated. Their requirements cannot be recovered.
3. **A rate for the top-level forcing** (\(d_a\to0\), R152). With such a rate the \(O(p)\) target could gain power slack. None is recorded.
4. **Whether the R189 obstruction applies to \(\mathcal M_w\).** In particular, whether interval or geometric-progression laws make \(\mathcal M_w\gg X(1_I)\).
5. **Whether the L3 composition (block \(\le C\mathcal M_w\)) is recorded anywhere.** A text search of the acceptance records, audits and route notes from Rounds 162–189 found no such statement. R180 `ordinary-paired-J-cross-ratio-180.md`:65 comes closest, but uses \(\mathcal M_w\) only for \(\mathcal D_0+\mathcal D_1\).

---

## 7. Bookkeeping observations in this note that need an audit

None of these is an accepted statement. Each composes or substitutes accepted ones.

- **B1 (L3).** The fixed moderate block is at most \((a^2b^2s_0(1-s_1))^{-1}\mathcal M_w\). It follows from R162:23–30 or R164:47–54, R166:9 and R166:44. So \(\mathcal M_w=O(p)\) closes the block without the one-match, zero-match or J obligations.
- **B2.** \(\mathcal M_w\le X/4\) together with B1: \(X=O(p)\) with no logarithm closes the block.
- **B3.** \(-O(p^{43/24+o(1)})\le\text{zero}\le O(p^{9/4})\), by subtraction (§2 P2).
- **B4.** With R187's \(\mathcal M_w\), the J-class bounds become \(\mathcal D_0+\mathcal D_1\ll p^{7037/3840+o(1)}\) and \(\mathcal D_J\ll p^{11/6+o(1)}\) per class.
- **B5.** The R179 majorant floors at \(p^2\) on (NC): its own terms \(pG^2\) and \(G^6/p\), and Hölder.
- **B6.** \(W\ge(\frac12-o(1))\sqrt p\) on (NC), so the C-S step and Theorem A's \(W\) branch have no order slack.

---

## 8. Verdict

**Yes, with qualifications.** The mission's "supported" condition is met in the structural sense.

- **One-match \(O(p^{3/2})\) is not necessary for the chain.** It is the second-moment form chosen in Rounds 164/166 and split by matches in Round 167. A one-match class at \(p^{3/2+\varepsilon}\), \(p^{7/4-\delta}\) or \(p^{43/24}\) could be absorbed only by a cancelling zero-match class. No accepted statement provides one, so in practice nothing absorbs it.
- **One obligation is closer than any complete route that uses the one-match class.** It is the first mass \(\mathcal M_w=O(p)\) with no logarithm (or \(X=O(p)\), which implies it). Current value \(p^{4/3+o(1)}\), gap \(1/3\) in its units. The diagonal, J and split routes are bottlenecked at \(3/8\) in the same units. Proving it would make the zero-match, generic J and one-match obligations unnecessary for the fixed moderate block (bookkeeping B1, to be audited).
- **There is no exponent slack anywhere.**
  - The top-level \(O(p)\) has no recorded forcing rate.
  - \(W\asymp\sqrt p\) makes the C-S step tight.
  - \(\mathcal M_w=O(p)\) and \(X=O(p)\) are sharp-order statements; \(X\ge2p\) on (NC).
- **The first-mass route meets the same kind of barrier as the one-match route.**
  - It is at the extraction-plus-Young cap \(p^{4/3}\) (R187).
  - Admissible-only arguments must bound \(E_{\rm off}(H)=O(p)\) with no logarithm for subgroups of size up to \(2C_{\rm cap}\sqrt p\). Known bounds have \(p\log p\).
  - Whether the (GP) obstruction of R189 also binds \(\mathcal M_w\) cannot be recovered.
  - Redirecting Round 191 to \(\mathcal M_w\) therefore changes which statement must be proved, not how hard it is in kind.
- **Pieces whose current statement cannot be recovered** (see §6):
  - zero match;
  - assembly of the growing slope and vertex bands into the whole favorable off-diagonal;
  - the top-level forcing rate;
  - whether the R189 family obstructs \(\mathcal M_w\).
