# Round 191 native Claude draft: does the sector obstruction bind the first mass \(\mathcal M_w\)?

- **call_id:** `ordinary-first-mass-sector-obstruction`
- **Author:** Claude subagent started by the Round 191 coordinator (session/r191-mw-sector). This is an agent assessment. It is not an audit, not human acceptance and not a mathematical certification.
- **Mission:** `coordination/missions/round-191/ordinary-first-mass-sector-obstruction.md`, exported from `coordination/round-190.json` (SHA-256 `b8f6e40f…84c05cc`, matches the export).
- **Inputs read.** All six SHA-256 values listed in the mission match:
  - `research/round-189-acceptance.json` (`ad4e0b5a…6176506`) and `research/round-190-acceptance.json` (`11c42c0a…3409b`): the `proof_scope` entries citing Round 183 Prop. A/C, Round 189 Prop. 3 and Round 190 Theorem 4;
  - `research/native-claude-audit-190.md` (`6237bffb…7b80`): §§2–4 and §6 in full;
  - `research/native-claude-ordinary-nc-excludes-sector-laws-190.md` (`5081b11a…d817`): in full;
  - `research/native-claude-ordinary-prime-intercept-fibre-t0-189.md` (`2a586af8…b53b852`): in full;
  - `research/native-claude-ordinary-prime-first-mass-fibre-dilation-183.md` (`d1e835ad…6160`): in full.

  Also read: `AGENTS.md`, `docs/WORKFLOW.md`, `coordination/checkpoints/round-190.md`, §2.4 of `research/native-claude-audit-189.md` (the masked-to-unmasked step), and `research/paley-183-fibre-identity-check.py` (chart conventions).
- **Scripts (all new):**
  - `research/paley-191-mwsector-exact.py`: exact Fractions and integers (Parts I–III, V), plus one labelled floating part (IV);
  - `research/paley-191-mwsector-models.py`: floating models, evidence only, with a `--check` mode against a brute-force row form;
  - `research/paley-191-mwsector-exponents.py`: exact `Fraction` arithmetic for every exponent and rational constant here.
- **Nothing was committed.** I wrote only this file and the three scripts.

## Result summary

**Verdict: yes (supported), in the method-cap sense of the mission, with the scope stated in §5.** \(\mathcal M_w\) meets the same geometric-progression wall as \(T_0\) and \(X\). Below \(p^{16/13}\) (covariance-equivalent \(45/26\)), an argument for \(\mathcal M_w\) that uses only the admissible hypotheses, or only the sector-free (NC) consequences \(\mathcal H\) of Round 190 Cor. 4.1, must prove `cand:gp-shifted-energy` below \(|I'|^{32/13}\). No bound on \(\mathcal M_w\), \(X\) or \(T_0\) of the actual law is proved or changed.

1. **Restriction lemma for \(\mathcal M_w\) (Lemma 1; proved; \(w\) kept).** Let \(0\le g\le1\) on \(Q\) and \(I'\subset Q\). Put \(\Sigma(I')=I'I'I'^{-1}I'^{-1}\). If \(g\ge\tau'\) on \(I'\setminus\{1\}\) and \(w\ge\tau''\) on \(\Sigma(I')\setminus\{1\}\), then
   \[\mathcal M_w(g)\ \ge\ \tau'^4\,\tau''\,X_{\rm off}(\mathbf 1_{I'}),\qquad X_{\rm off}(\mathbf 1_{I'})=X(\mathbf 1_{I'})-\textstyle\sum_\kappa c_{I'}(\kappa)\ \ge\ X(\mathbf 1_{I'})-|I'|^2 .\]
   The proof is positivity in the row form of Round 183 Prop. A. The lemma is sharp: on Round 183's coset family \(g_H\) it holds with equality, \(\mathcal M_w(g_H)=\frac3{4096}E_{\rm off}(H)\). Unlike Round 189 Prop. 3(b), it needs \(g\) bounded away from **both** 0 and 1 on the four-fold ratio set \(\Sigma(I')\).
2. **What \(w\) does on the pure laws (Proposition 2; proved).**
   - (a) For the exact subgroup law \(g=\mathbf 1_H\), \(w\equiv0\), so \(\mathcal M_w=0\), while \(T_0=X(\mathbf 1_H)>0\). So for one individual law in the class "\(g\ge\tau\) on \(II^{-1}\)", \(w\) removes the sector piece **entirely**.
   - (b) For the pure interval law \(g_J\) (Round 189 Prop. 3(c)), \(w(\zeta^j)\asymp(Lj/n)^2\) near \(j=0\). Exactly,
     \[(4/\pi^2)^5\cdot\tfrac43\,\tfrac{L^2-1}{n^2}\,X_2(I')\ \le\ \mathcal M_w(g_J)\big|_{I'}\ \le\ \tfrac{\pi^2}3\,\tfrac{L^2-1}{n^2}\,X_2(I'),\]
     where \(X_2(I')\) is the energy of \(1-I'\) with each nontrivial quadruple weighted by \(j^2\), and \(j\) is the exponent of \(AD/(CY)\).
   - (c) The same holds up to \(o(1)\) for \(D_\theta\) on quadruples with \(|j|\ge\varepsilon K'\).
   - So on the **pure** laws \(w\) replaces \(X_{\rm off}\) by a second-moment-weighted energy.
3. **The \(\eta\)-mixtures defeat the weight (Theorems 3 and 4; proved).** Mix a spread component of mass \(\eta\in(0,1)\) into the law. This lowers the plateau of \(g\) from 1 to \((1-\eta)^2\) and keeps \(g\ge(1-\eta)^24/\pi^2\) on the whole window. Then \(w\ge w_0(\eta)>0\) on \(\Sigma(I')\setminus\{1\}\), and Lemma 1 gives
   \[\mathcal M_w\ \ge\ c(\eta)\,X_{\rm off}(\mathbf 1_{I'}),\qquad c(\eta)=a^4\min\{a(1-a),\,b(1-b)\},\quad a=\tfrac4{\pi^2}(1-\eta)^2,\ b=(1-\eta)^2 .\]
   - The mixed interval law \(g_{J,\eta}\) (Theorem 3) is admissible. It is the interval analogue of Round 183's \(g_H\).
   - The mixed diluted-interval law \(D_\theta^\eta\) (Theorem 4) satisfies every item of \(\mathcal H\), as \(D_\theta\) does (Round 190 Theorem 4). It also stays in the class "\(g\ge\tau\) on \(II^{-1}\)".
   - At \(\eta=\frac12\), \(c=(\pi^2-1)/\pi^{12}\approx9.6\cdot10^{-6}\).
4. **Method caps (Corollaries 3.1, 4.1; proved as implications).** Suppose an admissible-only argument, or an argument using only \(\mathcal H\), proves \(\mathcal M_w\le Cp^{16/13-\delta}\). Then it proves
   \[E^\times(I'-1)\ll|I'|^{32/13-2\delta}\]
   for every symmetric geometric progression \(I'=\{\zeta^k:|k|\le K'\}\subset Q\) with \(|I'|\asymp\sqrt p\) in the stated ranges, by the masked-to-unmasked step of the Round 189 audit (§2.4). MPRRS Theorem 37 gives only \(|I'|^{32/13+o(1)}\). For the target \(\mathcal M_w=O(p)\), such arguments must prove \(E^\times(I'-1)=O(|I'|^2)\) with no logarithm.
5. **The sector lever is the same as for \(T_0\) (Proposition 5; proved on (NC)).** On (NC), with fixed thresholds, the hypothesis of Lemma 1 forces \(\{\zeta^k:|k|\le2K'\}\) to be a Paley \(\rho\)-clique. So Round 190 Criteria 5.1–5.2 transfer verbatim: (GP-Sub\(_c\)) excludes the family, and (GP-Sub\(_\kappa\)) weakens it by \(p^{-5\kappa}\). Nothing quantitative follows.
6. **Evidence (floating models and exact integer counts; not certificates).**
   - For the symmetric progression \(I\) with \(K=\frac14\sqrt p\) and \(K=\frac12\sqrt p\), at \(10^5\le p\le3\cdot10^7\), the distribution of \(j\) over the nontrivial energy quadruples of \(1-I\) matches the four-uniform baseline (tail fractions within 0.01). So in these models \(X_2/K^2\approx1.34\,X_{\rm off}\): the pure-law weighting also loses only a constant.
   - The chain \(\mathcal M_w\ge\mathcal M_w|_{I'}\ge\tau'^4\tau''X_{\rm off}(\mathbf 1_{I'})\) holds in every model, and \(D_\theta^\eta\) shows the \(\mathcal H\) diagnostics of Theorem 4 up to \(p=4\cdot10^6\).

**\(X\), \(\Gamma_2\) and \(\mathcal M_w\), stated separately:** no new bound on any of them. \(\mathcal M_w\le(X-\mathrm{diag})/4\) (Round 182) and \(\mathcal M_w\ll p^{4/3+o(1)}\) (Round 187) are unchanged.

## Setup and hypotheses

Notation is that of Round 183 (fibre-dilation report, "Setup and hypotheses", lines 39–51), Round 189 (T₀ report, lines 64–90) and Round 190 (NC report, lines 70–90). Counting norms are used throughout.

- \(p\equiv1\pmod 4\) prime, \(n=(p-1)/2\), \(Q\) the squares, \(\chi\) the Legendre symbol. \(\zeta\) is a generator of \(Q\), and \(\psi\) is the character of \(Q\) with \(\psi(\zeta)=e(1/n)\), so \(\widehat Q\cong\mathbb Z/n\) through \(j\mapsto\psi^j\).
- \(\nu\) is a probability on \(\widehat Q\), \(f=\sum_j\nu_j\psi^j\) on \(Q\) (zero off \(Q\)), \(g=|f|^2\) and \(w=g(1-g)\). Then \(g(1)=1\) and \(0\le g\le1\).
- **Admissible** means probability plus the cap \(n\max\nu\le C_{\rm cap}\sqrt p\). This is (H1), (H2), (H4) of Round 183, and Round 189's "probability/cap" hypotheses, which give \(\omega\ge0\). (H3) holds whenever \(\nu\) is real, which is true for every law below.
- **Chart and fibre form (Round 183 Prop. A, accepted).**
  - Labels \((Y,D)\in(Q\setminus\{1\})^2\), \(Y\ne D\), with \(\mu(Y,D)=g(Y)g(D)\).
  - The fibre is \(R_\kappa=\{(Y,D):1-Y=\kappa(1-D)\}\) for \(\kappa\in Q\setminus\{1\}\).
  - Row form:
    \[\mathcal M_w=\sum_{\kappa\in Q\setminus\{1\}}\ \sum_{P=(Y,D),\,P'=(A,C)\in R_\kappa}\mu(P)\mu(P')\,w\!\Big(\frac{AD}{CY}\Big),\]
    with \(AD/(CY)=1\iff P=P'\) (A2).
- **Restricted energies.**
  - For \(I'\subset Q\): \(c_{I'}(\kappa)=\#\{(Y,D)\in(I'\setminus\{1\})^2:1-Y=\kappa(1-D)\}\), \(X(\mathbf 1_{I'})=\sum_{\kappa\in Q\setminus\{1\}}c_{I'}(\kappa)^2\) (Round 189 Prop. 3(b)), and \(X_{\rm off}(\mathbf 1_{I'})=\sum_\kappa(c_{I'}(\kappa)^2-c_{I'}(\kappa))\). The difference is at most \(|I'|^2\).
  - "Nontrivial \(I'\)-quadruples" are the ordered pairs \(P\ne P'\) in a common \(R_\kappa\) with all four labels in \(I'\setminus\{1\}\). There are \(X_{\rm off}(\mathbf 1_{I'})\) of them.
  - For \(I'=\{\zeta^k:|k|\le K'\}\), write \(Y=\zeta^y\), \(D=\zeta^d\), \(A=\zeta^a\), \(C=\zeta^c\) with \(|y|,|d|,|a|,|c|\le K'\), and \(j=j_{PP'}=a+d-c-y\in[-4K',4K']\), the exponent of \(AD/(CY)\).
  - \(X_2(I')=\sum j_{PP'}^2\) over nontrivial \(I'\)-quadruples. \(X^{(\varepsilon)}(I')\) is the number of nontrivial \(I'\)-quadruples with \(|j|\ge\varepsilon K'\).
- **Masked to unmasked (Round 189 audit §2.4, accepted):** \(E^\times(I'-1)\le16\,(X(\mathbf 1_{I'})+|I'|^2)\).
- **External input (as accepted in Round 190):** MPRRS arXiv:1702.01003v5 Theorem 37 gives \(E^\times(I-1)\ll|I|^{32/13}(\log|I|)^{18/13}\) for symmetric geometric progressions \(I\subset Q\), \(|I|\le p^{13/23}\). It is used only to state where the wall is.
- **\(\mathcal H\)** (Round 190 Cor. 4.1, accepted with corrections) is:
  - probability, \(\nu_0=0\), the cap, \(\omega\ge0\), (H3);
  - (NC1);
  - exact or approximate flatness;
  - the conclusions of (A2), (A4), (A5), (A6).

  The sector forms (NC2), (A3), Round 184 SRM Prop. 2, Round 184 Lemma 0 and \(d_\rho(S)\to0\) are not in \(\mathcal H\).
- **Fejér kernel:** \(F_L(j)=\bigl(\sin(\pi Lj/n)/(L\sin(\pi j/n))\bigr)^2=\frac1L\sum_{|t|<L}(1-\frac{|t|}L)e(tj/n)\), with \(F_L\ge4/\pi^2\) for \(|j|\le n/(2L)\) (Round 189 Prop. 3(c), audited).

## 1. The restriction lemma for \(\mathcal M_w\)

**Lemma 1.** Let \(0\le g\le1\) on \(Q\), \(w=g(1-g)\), \(I'\subset Q\), and \(\Sigma(I')=\{AD/(CY):A,C,D,Y\in I'\}\). Suppose \(g\ge\tau'\) on \(I'\setminus\{1\}\) and \(w\ge\tau''\) on \(\Sigma(I')\setminus\{1\}\). Then
\[\mathcal M_w(g)\ \ge\ \mathcal M_w(g)\big|_{I'}\ \ge\ \tau'^4\tau''\,X_{\rm off}(\mathbf 1_{I'}),\]
where \(\mathcal M_w|_{I'}\) is the sum of the row-form terms over nontrivial \(I'\)-quadruples. No symmetry of \(I'\) or of \(g\) is used.

*Proof.*
- Every term of the row form is \(\ge0\), because \(\mu\ge0\) and \(0\le w\le\frac14\). So \(\mathcal M_w\ge\mathcal M_w|_{I'}\).
- On a nontrivial \(I'\)-quadruple, \(\mu(P)\mu(P')\ge\tau'^4\).
- The ratio \(s=AD/(CY)\) lies in \(\Sigma(I')\), and \(s\ne1\) because \(P\ne P'\) (Round 183 Prop. A2). So \(w(s)\ge\tau''\).
- The number of such ordered pairs is \(\sum_\kappa c_{I'}(\kappa)(c_{I'}(\kappa)-1)=X_{\rm off}(\mathbf 1_{I'})\). \(\square\)

**Sharpness.** Take Round 183's coset law \(g_H=\delta_1+\frac14\mathbf 1_{H\setminus\{1\}}\) and \(I'=H\), so \(\Sigma(H)=H\). Then \(\tau'=\frac14\) and \(\tau''=\frac3{16}\), and the bound is \(\frac{3}{4096}X_{\rm off}(\mathbf 1_H)\). This is exactly Round 183 Prop. C(2), \(\mathcal M_w(g_H)=\frac3{4096}E_{\rm off}(H)\), since \(E_{\rm off}(H)=X_{\rm off}(\mathbf 1_H)\). Equality is checked exactly in Part III of the exact script for every subgroup of \(Q\) at \(p=101,109,113\).

**Comparison with Round 189 Prop. 3(b).** For \(T_0\), the extra factor is the triangle weight \(g(Y'/Y)\), which is **large** near the ratio 1. So \(g\ge\tau\) on \(II^{-1}\) suffices there. For \(\mathcal M_w\), the extra factor \(w=g(1-g)\) vanishes where \(g=1\). So the restriction needs \(g\) bounded away from 1 on the whole four-fold ratio set \(\Sigma(I')\setminus\{1\}\). This is the precise sense in which "\(w\) is small where \(g\approx1\)". Sections 2 and 3 show when it matters.

## 2. Pure laws: what keeping \(w\) does

**Proposition 2.**
- **(a) Subgroup laws.** Let \(H\le Q\) and \(g=\mathbf 1_H\) (admissible when \(|H|\le C_{\rm cap}\sqrt p\); Round 189 Prop. 3(a)). Then \(w\equiv0\) and \(\mathcal M_w(\mathbf 1_H)=0\), while \(T_0=X=X(\mathbf 1_H)\) (Round 189 Prop. 3(a)). So for this law in the class "\(g\ge\tau\) on \(II^{-1}\)" (with \(I=H\)), \(\mathcal M_w\ge cX(\mathbf 1_{I'})\) fails for every \(I'\) with \(X_{\rm off}(\mathbf 1_{I'})>0\).
- **(b) Pure interval law.** Let \(g_J\) be the interval law of Round 189 Prop. 3(c): \(\nu=\mathbf 1_J/L\), \(L\ge2\), so that \(g_J(\zeta^k)=F_L(k)\). Let \(K'\ge1\) satisfy \(4K'\le n/(2L)\), and \(I'=\{\zeta^k:|k|\le K'\}\). Then, exactly,
  \[\Big(\frac4{\pi^2}\Big)^5\frac43\,\frac{L^2-1}{n^2}\,X_2(I')\ \le\ \mathcal M_w(g_J)\big|_{I'}\ \le\ \frac{\pi^2}3\,\frac{L^2-1}{n^2}\,X_2(I').\]
  With \(K'=\lfloor n/(8L)\rfloor\), \((L^2-1)/n^2\le1/(64K'^2)\). So
  \[\mathcal M_w(g_J)|_{I'}\asymp X_2(I')/K'^2,\qquad \varepsilon^2X^{(\varepsilon)}(I')\le X_2(I')/K'^2\le16\,X_{\rm off}(\mathbf 1_{I'}).\]
- **(c) Diluted-interval laws.** For \(D_\theta\) (Round 190 Theorem 4, \(0<\theta<\frac12\)) and \(I'=\{\zeta^k:|k|\le\lfloor n/(8L')\rfloor\}\), for every fixed \(\varepsilon\in(0,4]\),
  \[\mathcal M_w(D_\theta)\ \ge\ \Big(\big(\tfrac4{\pi^2}\big)^5\frac{\varepsilon^2}{48}-o(1)\Big)\,X^{(\varepsilon)}(I').\]

**Lemma 3 (used in (b), (c)).** For \(L\ge1\) and \(1\le|j|\le n/(2L)\),
\[\tfrac43(L^2-1)(j/n)^2\ \le\ 1-F_L(j)\ \le\ \tfrac{\pi^2}3(L^2-1)(j/n)^2 .\]
*Proof.*
- From the Fejér form, \(1-F_L(j)=\frac2L\sum_{|t|<L}(1-\frac{|t|}L)\sin^2(\pi tj/n)\).
- Here \(|tj/n|\le\frac{L-1}{2L}<\frac12\). On \(|y|\le\frac12\), \(4y^2\le\sin^2(\pi y)\le\pi^2y^2\).
- Finally \(\sum_{|t|<L}(1-\frac{|t|}L)t^2=(L^3-L)/6\) (exact; `paley-191-mwsector-exponents.py` item 6). \(\square\)

*Proof of Proposition 2.*
- (a) \(g\in\{0,1\}\).
- (b) On a nontrivial \(I'\)-quadruple:
  - all labels lie in \(\{|k|\le K'\}\), where \(F_L\ge4/\pi^2\), and \(\mu\mu'\le1\);
  - \(s=\zeta^j\) with \(1\le|j|\le4K'\le n/(2L)\), so \(w(s)=F_L(j)(1-F_L(j))\);
  - use \(4/\pi^2\le F_L\le1\) and Lemma 3, then sum.
- (c) As in (b), using Round 190 Theorem 4's uniform approximation \(g=F_{L'}+o(1)\) on the window:
  - \(\mu\mu'\ge(4/\pi^2-o(1))^4\) and \(g(s)\ge4/\pi^2-o(1)\);
  - \(1-g(s)\ge\frac43(L'^2-1)\varepsilon^2K'^2/n^2-o(1)=\varepsilon^2/48-o(1)\) for \(|j|\ge\varepsilon K'\), since \((L'^2-1)K'^2/n^2\to1/64\). \(\square\)

**Reading.**
- On the pure laws (the exact Round 189 interval laws and the exact Round 190 \(D_\theta\)), the sector piece of \(\mathcal M_w\) is the **second-moment-weighted** energy \(X_2(I')/K'^2\), not \(X_{\rm off}(\mathbf 1_{I'})\).
- For these laws the question "does \(w\) remove the sector piece?" is therefore exactly whether the nontrivial energy of \(1-I'\) concentrates on quadruples with \(AD/(CY)\to1\) in exponent, \(|j|=o(K')\). I cannot prove that it does not.
- Exponent closeness is not an algebraic notion in \(\mathbb F_p\). In the models, the \(j\)-profile is the four-uniform one (§6.2), so \(X_2/K'^2\approx1.34X_{\rm off}\).
- **This individual-law question does not decide the method cap**, because of §3.

## 3. The \(\eta\)-mixtures: the weight cannot protect the hypothesis classes

**Theorem 3 (mixed interval laws; admissible).** Let \(0<\eta<1\), \(L\ge2\), \(J\subset\mathbb Z/n\) an interval of length \(L\), and
\[\nu=(1-\eta)\,\mathbf 1_J/L+\eta\,\mathrm{unif}(\widehat Q).\]
1. \(\nu\) is a probability, \(n\max\nu\le(1-\eta)n/L+\eta\), \(\nu\) is real (so (H3) holds), and \(\omega\ge0\).
2. \(g(1)=1\), and \(g(\zeta^k)=(1-\eta)^2F_L(k)\) for \(k\not\equiv0\).
3. On the window \(W=\{\zeta^k:1\le|k|\le n/(2L)\}\), \(a\le g\le b\) with \(a=\frac4{\pi^2}(1-\eta)^2\) and \(b=(1-\eta)^2\). Hence \(w\ge w_0:=\min\{a(1-a),b(1-b)\}>0\) on \(W\).
4. For \(K'=\lfloor n/(8L)\rfloor\ge1\) and \(I'=\{\zeta^k:|k|\le K'\}\):
   \[\mathcal M_w(g_{J,\eta})\ \ge\ c(\eta)\,X_{\rm off}(\mathbf 1_{I'}),\qquad c(\eta)=a^4w_0 .\]
   Also \(g_{J,\eta}\ge a\) on Round 189's \(II^{-1}\), so the law is in the class of the mission.

*Proof.*
1. Direct.
2. \(\sum_{\eta'\in\widehat Q}\eta'(x)=n\mathbf 1_{x=1}\), so \(f=(1-\eta)f_J+\eta\mathbf 1_{x=1}\) with \(|f_J(\zeta^k)|^2=F_L(k)\) and \(f_J(1)=1\).
3. \(F_L\in[4/\pi^2,1]\) on the window. \(w=g(1-g)\) is concave, so its minimum on \([a,b]\) is at an endpoint, and \(0<a<b<1\).
4. \(I'\setminus\{1\}\subseteq W\). \(\Sigma(I')\setminus\{1\}\subseteq\{\zeta^k:1\le|k|\le4K'\}\subseteq W\), since \(4K'\le n/(2L)<n/2\) and exponent 0 is the only representative of 1 in that range. Apply Lemma 1 with \(\tau'=a\), \(\tau''=w_0\). \(\square\)

At \(\eta=\frac12\): \(a=1/\pi^2\), \(w_0=a(1-a)=(\pi^2-1)/\pi^4\), and \(c=(\pi^2-1)/\pi^{12}\approx9.596\cdot10^{-6}\) (exponent script item 9). \(\eta=\frac12\) with a subgroup in place of \(J\) is Round 183's \(g_H\).

**Corollary 3.1 (method cap; admissible-only; proved as an implication).** Fix \(C_{\rm cap}\), \(\eta\in(0,1)\) and \(c_2>0\). Suppose an argument proves \(\mathcal M_w(g)\le Cp^{16/13-\delta}\) for every admissible law, using only probability, the cap and their consequences (H2), (H3), (H4), \(\omega\ge0\). Then, for all large \(p\), every generator \(\zeta\) of \(Q\) and every \(K'\) with \(c_2\sqrt p\le2K'+1\) and \(8(1-\eta)K'\le(C_{\rm cap}-\epsilon)\sqrt p\), the progression \(I'=\{\zeta^k:|k|\le K'\}\) satisfies
\[X_{\rm off}(\mathbf 1_{I'})\le\frac{C}{c(\eta)}\,p^{16/13-\delta},\qquad E^\times(I'-1)\le16\Big(\frac{C}{c(\eta)}p^{16/13-\delta}+2|I'|^2\Big)\ll|I'|^{32/13-2\delta}\quad(\delta<3/13).\]

*Proof.*
- Take \(L=\lfloor n/(8K')\rfloor\). Then \(\lfloor n/(8L)\rfloor\ge K'\), and the cap \((1-\eta)n/L+\eta\le C_{\rm cap}\sqrt p\) holds for large \(p\).
- Theorem 3(4) on the larger progression, together with the monotonicity of \(X_{\rm off}\) under inclusion (it counts pairs), gives the first bound.
- Then use the masked-to-unmasked step (Round 189 audit §2.4) and \(p\le c_2^{-2}|I'|^2\). The final \(\ll\) uses \(2<32/13-2\delta\iff\delta<3/13\) (exponent script item 10). \(\square\)

Because \(\eta\) is free, the covered lengths \(|I'|\) run over every fixed multiple of \(\sqrt p\), at the cost of the constant \(c(\eta)\).

**Theorem 4 (mixed diluted-interval laws \(D_\theta^\eta\); satisfy \(\mathcal H\)).** Fix \(0<\theta<\frac12\) and \(0<\eta<1\). Let:
- \(m=\mathrm{round}(m_0)\), \(m_1=\mathrm{round}((1-\eta)m)\), \(L'=\mathrm{round}(m_1/\theta)\);
- \(J'=[a_0,a_0+L')\subset\mathbb Z/n\setminus\{0\}\) and \(U=\mathbb Z/n\setminus(\{0\}\cup J')\);
- \(S_1\) a uniform random \(m_1\)-subset of \(J'\), and \(S_2\) an independent uniform random \((m-m_1)\)-subset of \(U\);
- \(S=S_1\sqcup S_2\) and \(\nu=\mathbf 1_S/m\).

With probability \(1-o(1)\):
1. **Admissibility.** \(\nu\) is a probability, \(\nu_0=0\), \(n\max\nu=n/m=(1+o(1))\sqrt p\), \(\omega\ge0\), (H3).
2. **(NC1).** \(m_{\rm eff}=m\), \(G=n/m\sim\sqrt p\).
3. **Flatness.** \(e=u_S\) exactly, with \(|S|=m\sim m_0\).
4. **(A2).** \(\mathcal E(S)\le(\theta(1-\eta)+o(1))|S|^3<\frac12|S|^3\), and \(\Gamma_{\rm tot}=G\,\mathcal E(S)/|S|^3<(\frac12+o(1))\sqrt p\).
5. **(A5).** \(\max_{a\ne0}|S\cap(S+a)|/|S|\le\theta(1-\eta)+o(1)<\frac12\). Hence the overlap dichotomy holds, \(H_*=\{0\}\), and \(\max_{a\ne0}\widehat g(a)/G\le\theta(1-\eta)+o(1)\).
6. **(A6).** Every coset of every subgroup of \(\mathbb Z/n\) of order \(\le2m_0\) contains at most \((1-\eta)/\theta+O(\log p)=o(|S|)\) points of \(S\).
7. **(A4).** For every bounded union \(B\) of cosets of multiplicative subgroups of order in \([c_1\sqrt p,c_2\sqrt p]\), \(\sum_Bg=o(G)\), i.e. \(t_B\to1\).
8. **The obstruction.** \(\sup_{k\not\equiv0}|g(\zeta^k)-(1-\eta)^2F_{L'}(k)|=o(1)\). Hence:
   - \(g\in[a-o(1),b+o(1)]\) on \(W'=\{1\le|k|\le n/(2L')\}\), with \(a,b\) as in Theorem 3;
   - for \(I'=\{\zeta^k:|k|\le\lfloor n/(8L')\rfloor\}\), with \(|I'|=(\frac{\theta}{4(1-\eta)}+o(1))\sqrt p\),
     \[\mathcal M_w(D_\theta^\eta)\ \ge\ (c(\eta)-o(1))\,X_{\rm off}(\mathbf 1_{I'});\]
   - also \(g\ge a-o(1)\) on Round 189's \(II^{-1}\), and \(T_0\ge(a-o(1))^5X(\mathbf 1_I)\) by Round 189 Prop. 3(b).
9. **\(\Gamma_{\rm tot}\asymp\sqrt p\).** \(\Gamma_{\rm tot}\ge(a-o(1))^2|W'|\asymp\sqrt p\).

*Proof.* Write \(f=\frac{m_1}mf_{S_1}+\frac{m-m_1}mf_{S_2}\), where \(f_{S_i}=|S_i|^{-1}\sum_{j\in S_i}\psi^j\) and \(m_1/m\to1-\eta\).
- **Items 1–3** are as in Round 190 Theorem 4.
- **Item 8.**
  - \(f_{S_1}\): Round 190 Theorem 4's concentration step (McDiarmid for uniform subsets of fixed size, union bound over \(n\) points) gives \(\sup_x|f_{S_1}-(\theta L'/m_1)D_{L'}|=O(\sqrt{\log p/m_1})\), with \(\theta L'/m_1=1+o(1)\) and \(|D_{L'}(\zeta^k)|^2=F_{L'}(k)\).
  - \(f_{S_2}\): for \(x\ne1\), \(\mathbb Ef_{S_2}(x)=|U|^{-1}\sum_{j\in U}\psi^j(x)=|U|^{-1}(-1-\sum_{j\in J'}\psi^j(x))=O(L'/n)=O(p^{-1/2})\). The same concentration (swap-Lipschitz constant \(2/|S_2|\)) gives \(\sup_{x\ne1}|f_{S_2}(x)|=O(\sqrt{\log p/m})=o(1)\).
  - Since \(|D|\le1\), \(|f|^2=(1-\eta)^2F_{L'}+o(1)\) uniformly off 1. The window bounds follow from \(F_{L'}\in[4/\pi^2,1]\). The \(\mathcal M_w\) bound is Lemma 1 with \(\tau'=a-o(1)\) and \(\tau''=\min_{[a-o(1),b+o(1)]}g(1-g)=w_0-o(1)\), since \(b<1\). The inclusions are as in Theorem 3. Also \(n/L'=\theta\sqrt p/(1-\eta)\cdot(1+o(1))\).
- **Items 4–5.**
  - \(|S\cap(S+a)|\le|S_1\cap(S_1+a)|+|S_1\cap(S_2+a)|+|S_2\cap(S_1+a)|+|S_2\cap(S_2+a)|\).
  - The first term is \(\le\theta^2(L'-|a|)_++O(\sqrt{m\log p})\le\theta m_1+o(m)\) (Round 190 Theorem 4).
  - Given \(S_1\), the other three are swap-Lipschitz (constant \(\le2\)) functions of \(S_2\) with means \(O(m^2/n)=O(1)\). So they are \(O(\sqrt{m\log p})=o(m)\) uniformly in \(a\) (McDiarmid, union bound over \(n\) shifts).
  - Then \(\mathcal E(S)\le m^2+\max_{a\ne0}|S\cap(S+a)|\cdot m^2\). \(\Gamma_{\rm tot}=n\,\mathcal E(S)/m^4\) is the Parseval identity of Round 183 Prop. 1.1, and \(\widehat g(a)/G=|S\cap(S+a)|/m\).
- **Item 6.**
  - A coset of order \(e\le2m_0\) is an arithmetic progression of step \(n/e\ge n/(2m_0)\). It meets \(J'\) in at most \(L'e/n+1\le(1-\eta)/\theta+2\) points for large \(p\), since \(2m_0m/n\to1\).
  - Its intersection with \(S_2\) is hypergeometric with mean \(\le2m_0(m-m_1)/|U|=O(1)\). Over the at most \(n\,d(n)\) cosets this is \(O(\log p)\) with probability \(1-o(1)\) (Chernoff and a union bound).
- **Item 7.**
  - \(\sum_Bg\le1+2\sum_{B\setminus1}|f_{S_1}|^2+2\sum_{B\setminus1}|f_{S_2}|^2\).
  - The first sum is \(O(1+c_2^2\theta^2)+o(\sqrt p)\): this is Round 190 Theorem 4 item 7, with the Dirichlet-kernel bound \(\min(1,n/(2L'|k|))\) summed over an arithmetic progression of step \(\ge\sqrt p/(2c_2)\).
  - The second sum is \(\le|B|\sup_{x\ne1}|f_{S_2}|^2=O(\sqrt p)\cdot o(1)\).
- **Item 9** is immediate from item 8. \(\square\)

**Corollary 4.1 (method cap for sector-free (NC) arguments; proved as an implication).** Suppose an argument uses only \(\mathcal H\) and proves \(\mathcal M_w\le Cp^{16/13-\delta}\). Then, for every \(\theta\in(0,\frac12)\) and \(\eta\in(0,1)\), every generator \(\zeta\) of \(Q\) and all large \(p\), the progression \(I'=\{\zeta^k:|k|\le\lfloor n/(8L')\rfloor\}\), of length \((\frac\theta{4(1-\eta)}+o(1))\sqrt p\), satisfies \(E^\times(I'-1)\ll|I'|^{32/13-2\delta}\).

As \((\theta,\eta)\) vary, these lengths cover every fixed multiple of \(\sqrt p\). The progression is taken in the coordinates \(\zeta\) that define \(\psi\). (Fix \(\zeta\) first, then choose \(\psi\) with \(\psi(\zeta)=e(1/n)\); the hypotheses in \(\mathcal H\) do not depend on that choice.) *Proof:* Theorem 4(8) as in Corollary 3.1. \(\square\)

**Remark (where the weight could still help).** The mixture lowers the plateau without touching any hypothesis in \(\mathcal H\) or the admissible list.
- So keeping \(w\) can remove the sector pieces only through a property of the actual law that forces \(g\approx1\) on the sector windows away from the point 1.
- No accepted statement supplies such a property. On (NC), Round 190 Theorem 1 constrains only \(T_{-\rho}\).
- The "plateau at 1" is a feature of the pure Fejér profile, not a consequence of the hypotheses.

## 4. The sector condition (NC2) acts on \(\mathcal M_w\) as on \(T_0\)

**Proposition 5 (on (NC); proved).** Fix \(\tau',\tau''>0\). Suppose that along the (NC) sequence the actual \(g\) satisfies the hypothesis of Lemma 1 for \(I'=\{\zeta^k:|k|\le K'\}\) with \(\operatorname{ord}\zeta>8K'\). Then for large \(p\):
- \(\{\zeta^k:1\le|k|\le4K'\}\subseteq T_\rho\);
- \(\{\zeta^k:|k|\le2K'\}\) is a Paley \(\rho\)-clique of size \(4K'+1\le\sqrt p\);
- \(R(\zeta)\ge4K'\).

Consequently:
- (i) under (GP-Sub\(_c\)) for all \(c>0\), the mixed families of §3 with fixed \((\theta,\eta)\) are excluded on (NC) (Criterion 5.1 of Round 190, verbatim);
- (ii) under (GP-Sub\(_\kappa\)) with \(K'\ge c_0\sqrt p\), both \(\tau'\) and \(\tau''\) are \(\le(1+o(1))p^{-\kappa}\). So the restriction bound is \(\le p^{-5\kappa}(1+o(1))X_{\rm off}(\mathbf 1_{I'})\), exactly the Round 190 Criterion 5.2 weakening.

*Proof.*
- \(w\ge\tau''\) gives \(g\ge\tau''\) on \(\Sigma(I')\setminus\{1\}=\{1\le|k|\le4K'\}\). This set contains \(I'\setminus\{1\}\), since \(D=C=Y=1\in I'\).
- Round 190 Theorem 1(4) puts it in \(T_\rho\). Round 190 Lemma 2 with \(K=2K'\) gives the clique and the bound \(\le\sqrt p\).
- (ii) is Round 190 Theorem 1(3) (Markov): \(p^\kappa\tau\le G_{-\rho}\le1+o(1)\). \(\square\)

So the (NC2) lever for \(\mathcal M_w\) is `cand:gp-sector-constancy`, exactly as for \(T_0\). The progressions must be twice as long, which makes the exclusion slightly easier: Hanson–Petridis already excludes \(4K'+1>(\sqrt{2p-1}+1)/2\). As for \(T_0\), this is qualitative.

## 5. Answer to the mission question, with scope

1. **Is \(\mathcal M_w(g)\ge c(\tau)X(\mathbf 1_{I'})\) for a comparable sub-progression?**
   - *For each pure law:* not proved.
     - It fails outright for the exact subgroup law (Prop. 2(a)).
     - For the exact interval law and \(D_\theta\), the restricted part is \(\asymp X_2(I')/K'^2\) (Prop. 2(b)) or \(\gtrsim\varepsilon^2X^{(\varepsilon)}(I')\) (Prop. 2(c)). These are comparable to \(X_{\rm off}(\mathbf 1_{I'})\) unless the nontrivial energy concentrates at \(|j|=o(K')\).
   - *For the hypothesis classes:* **yes.**
     - The \(\eta\)-mixtures are in the same class (\(g\ge\tau\) on \(II^{-1}\), \(\tau=a\)) and satisfy, respectively, the admissible hypotheses (Theorem 3) and \(\mathcal H\) (Theorem 4).
     - They have \(\mathcal M_w\ge c(\eta)X_{\rm off}(\mathbf 1_{I'})\ge c(\eta)(X(\mathbf 1_{I'})-|I'|^2)\) with \(|I'|\asymp\sqrt p\).
   - Hence (Corollaries 3.1 and 4.1) admissible-only and sector-free (NC) arguments for \(\mathcal M_w\le p^{16/13-\delta}\) must prove \(E^\times(I'-1)\ll|I'|^{32/13-2\delta}\).
2. **Does \(w(b/b')\) remove the sector pieces?** Only for individual laws whose plateau on the sector window sits at height 1 (exactly for subgroup laws, and possibly for pure Fejér profiles). Not for any hypothesis set now in use, because a spread component of mass \(\eta\) lowers the plateau and preserves every hypothesis listed. Keeping \(w\) costs the constant \(c(\eta)\) (\(\approx10^{-5}\) at \(\eta=\frac12\); models give about \(6.5\cdot10^{-4}\)) and no power.
3. **Is the pivot to \(\mathcal M_w\) easier in kind than \(T_0\)/\(X\)?** No.
   - On the obstruction families, \(\mathcal M_w\), \(X\) and \(T_0\) all dominate a constant times the same sector energy \(X_{\rm off}(\mathbf 1_{I'})\).
   - Each is, in turn, \(\le\) the full \(X\) (Round 182: \(\mathcal M_w\le(X-\mathrm{diag})/4\); Round 188: \(T_0\le X\)).
   - Between \(p^{16/13}\) and the current \(p^{4/3+o(1)}\) (length \(4/39\) of the remaining \(1/3\), exponent script item 4), the sector families do not obstruct any of the three. But the fixed-block target \(\mathcal M_w=O(p)\) lies below \(p^{16/13}\), so the wall is on its critical path.
   - For the target itself, admissible-only or \(\mathcal H\)-only arguments must prove the **sharp, logarithm-free** estimate \(E^\times(I'-1)=O(|I'|^2)\) for all symmetric geometric progressions of length \(\asymp\sqrt p\). Known: \(|I'|^{32/13+o(1)}\). The gap is \(6/13\) in \(|I'|\) and \(3/13\) in \(p\). The subgroup logarithm obstruction (Round 183 C1 with MSS: \(p\log p\)) also stands.

## 6. Evidence (floating models; exact integer counts; not certificates)

### 6.1 Laws (`paley-191-mwsector-models.py laws …`)

Notation:
- `int` is \(g_J\), \(L=\mathrm{round}(n/\sqrt p)\). `mix` is \(g_{J,1/2}\).
- `Dth` is \(D_{1/4}\). `Dmix` is \(D^{1/2}_{1/4}\). `Dmix9` is \(D^{0.1}_{0.45}\).
- \(K'=\lfloor n/(8L_{\rm eff})\rfloor\). Full \(\mathcal M_w\) via FFT is computed only for \(p\le3\cdot10^4\).
- LB is \(\tau'^4\tau''X_{\rm off}(\mathbf 1_{I'})\), with \(\tau',\tau''\) measured on the law.

| law | p | \(G/\sqrt p\) | \(\mathcal M_w/p\) | \(\mathcal M_w/X\) | \(K'\) | \(X_{\rm off}(\mathbf 1_{I'})\) | \(\tau'\) | \(\tau''\) | \(\mathcal M_w\vert_{I'}/X_{\rm off}\) | \(\langle(j/K')^2\rangle\) | \(\mathcal E/m^3\), maxov, coset, cmass |
|---|---|---|---|---|---|---|---|---|---|---|---|
| int | 20011 | 0.996 | 0.0368 | 0.056 | 17 | 4 | 0.953 | 0.0002 | 0.196 | 7.6 | — |
| mix | 20011 | 0.510 | 0.0021 | 0.059 | 35 | 432 | 0.238 | 0.0944 | 6.39e-4 | 1.80 | — |
| Dmix | 20011 | 0.996 | 0.0064 | 0.013 | 8 | 0 | 0.212 | 0.0909 | — | — | 0.053, 0.155, 0.042, 0.045 |
| int | 1000033 | 1.000 | — | — | 125 | 1876 | 0.950 | 0.0000 | 0.0482 | 1.32 | — |
| mix | 1000033 | 0.501 | — | — | 250 | 30040 | 0.237 | 0.0911 | 6.53e-4 | 1.32 | — |
| Dmix | 1000033 | 1.000 | — | — | 62 | 120 | 0.195 | 0.0767 | 7.35e-4 | 1.74 | 0.025, 0.148, 0.008, 0.008 |
| Dmix9 | 1000033 | 1.000 | — | — | 62 | 120 | 0.745 | 0.1272 | 0.0747 | 1.74 | 0.221, 0.438, 0.006, 0.008 |
| int | 4000037 | 1.000 | — | — | 250 | 8834 | 0.950 | 0.0000 | 0.0477 | 1.29 | — |
| mix | 4000037 | 0.500 | — | — | 500 | 125534 | 0.237 | 0.0911 | 6.54e-4 | 1.33 | — |
| Dth | 4000037 | 1.000 | — | — | 62 | 24 | 0.949 | 0.0000 | 0.0165 | 0.36 | 0.166, 0.272, 0.002, 0.003 |
| Dmix | 4000037 | 1.000 | — | — | 125 | 600 | 0.211 | 0.0803 | 6.43e-4 | 1.19 | 0.023, 0.144, 0.003, 0.004 |
| Dmix9 | 4000037 | 1.000 | — | — | 125 | 600 | 0.762 | 0.1370 | 0.0716 | 1.19 | 0.219, 0.418, 0.002, 0.003 |

Readings (models only):
- **Lemma 1's chain** \(\mathcal M_w\ge\mathcal M_w|_{I'}\ge\) LB holds in every row; the script asserts it. For `int`, Proposition 2(b)'s two-sided bound is asserted too: lower/actual \(\approx0.006\), upper/actual \(\approx1.4\)–\(1.9\).
- **The mixtures have the plateau the theorems predict.** \(\tau'\approx0.24\approx(1/4)(0.95)\) and \(\tau''\approx0.09\), against the pure laws' \(\tau''\to0\).
- **The restricted ratio is flat in \(p\).** For `mix` and `Dmix` it is \(\approx6.4\)–\(7.4\cdot10^{-4}\), about \(\tau'^4\) times a typical \(w\approx0.2\) on the window. For the pure `int` it is \(\approx0.048\). Neither decays.
- **\(D_\theta^\eta\) behaves as Theorem 4 says:**
  - \(G/\sqrt p=1.000\);
  - \(\mathcal E/m^3\) is 0.023 (Dmix) and 0.22 (Dmix9), both \(<\frac12\);
  - the maximal overlap is 0.14 and 0.42 (\(\theta(1-\eta)=0.125,0.405\)), both \(<\frac12\);
  - the coset fractions and coset masses tend to 0.
- **The sizes are small.** \(X_{\rm off}(\mathbf 1_{I'})\) is tiny at these \(K'\) (random size \(\approx|I'|^4/(2p)\)). The models test the inequality chain, not any exponent. They give no lower bound for any actual law (\(\mathcal M_w/p\) is flat, as in Round 183).
- Other rows (\(p=1009,5009,100049\)) are in the script output (replay below).

### 6.2 Where the nontrivial energy sits (`… jdist C p …`, exact integer counts)

\(I=\{\zeta^k:|k|\le K\}\), \(K=\mathrm{round}(C\sqrt p)\). The table gives the fraction of nontrivial masked quadruples of \(1-I\) with \(|j|\le\varepsilon K\), against the four-uniform baseline (\(j=a+d-c-y\), with \(a,c,d,y\) iid uniform on \([-K,K]\), \(j\ne0\)).

| p | C | \(\vert I\vert\) | \(X_{\rm off}/\vert I\vert^2\) | \(\varepsilon=\frac18\) obs / base | \(\varepsilon=\frac14\) | \(\varepsilon=\frac12\) | \(\varepsilon=1\) | \(\langle(j/K)^2\rangle\) obs / base |
|---|---|---|---|---|---|---|---|---|
| 100049 | 0.25 | 159 | 0.121 | 0.073 / 0.076 | 0.150 / 0.159 | 0.311 / 0.319 | 0.588 / 0.597 | 1.466 / 1.356 |
| 1000033 | 0.25 | 501 | 0.120 | 0.075 / 0.082 | 0.156 / 0.164 | 0.331 / 0.324 | 0.606 / 0.598 | 1.323 / 1.341 |
| 4000037 | 0.25 | 1001 | 0.125 | 0.086 / 0.083 | 0.169 / 0.165 | 0.327 / 0.324 | 0.603 / 0.599 | 1.329 / 1.337 |
| 10000121 | 0.25 | 1583 | 0.123 | 0.082 / 0.082 | 0.163 / 0.165 | 0.320 / 0.323 | 0.596 / 0.599 | 1.354 / 1.336 |
| 30000001 | 0.25 | 2739 | 0.125 | 0.084 / 0.083 | 0.166 / 0.165 | 0.322 / 0.324 | 0.597 / 0.599 | 1.342 / 1.335 |
| 1000033 | 0.5 | 1001 | 0.503 | 0.081 / 0.083 | 0.165 / 0.165 | 0.320 / 0.324 | 0.592 / 0.599 | 1.366 / 1.337 |
| 10000121 | 0.5 | 3163 | 0.497 | 0.083 / 0.083 | 0.165 / 0.165 | 0.323 / 0.324 | 0.598 / 0.599 | 1.338 / 1.335 |

Readings:
- \(X_{\rm off}/|I|^2\approx|I|^2/(2p)\), the random (masked) value. These progressions carry no excess energy at these \(p\), as in the Round 189 audit's Part D.
- The \(j\)-profile of the nontrivial quadruples matches the baseline: every tail fraction within 0.01, and the second moment within 0.03 except at \(p=100049\) (0.11). So in these models \(X^{(\varepsilon)}\approx(1-O(\varepsilon))X_{\rm off}\) and \(X_2/K^2\approx1.34X_{\rm off}\).
- If the hypothetical excess energy that the wall is about behaved like this, even the pure laws would carry the obstruction. This is finite evidence, not a statement about the hypothetical configurations.

### 6.3 Exact checks (`paley-191-mwsector-exact.py`)

- **Part I.** The fibre, row, four-variable and log-correlation forms of \(\mathcal M_w\) agree exactly at \(p=41,61,101\), with random rational \(g\) and no symmetry.
- **Part II.** Lemma 1's chain holds exactly at \(p=101,197,229\) for laws with a plateau in \([\frac1{10},\frac14]\) on the window and arbitrary values elsewhere.
- **Part III.**
  - \(\mathcal M_w(\mathbf 1_H)=0\) with \(X(\mathbf 1_H)>0\);
  - \(\mathcal M_w(g_H)=\frac3{4096}X_{\rm off}(\mathbf 1_H)\) is exactly Lemma 1's bound, for all subgroups at \(p=101,109,113\).
- **Part IV (floating).**
  - Lemma 3 and \(F_L\ge4/\pi^2\) hold for \(n\le5004\), \(L<40\);
  - Theorem 3(2) holds from \(\nu\) by character sums to \(10^{-14}\).
- **Part V.** \(E^\times(I'-1)\le16(X+|I'|^2)\) holds at four primes.

## Proved (a) / conditional (b) / evidence (c)

**(a) Proved.** Hypotheses are stated in each item.
- (a1) **Lemma 1:** \(0\le g\le1\) on \(Q\) and any \(I'\subset Q\). The bound \(\mathcal M_w\ge\tau'^4\tau''X_{\rm off}(\mathbf 1_{I'})\), \(w\) kept, is sharp on \(g_H\).
- (a2) **Proposition 2.**
  - Subgroup laws have \(\mathcal M_w=0\).
  - Pure interval law: \(\mathcal M_w|_{I'}\asymp(L^2-1)n^{-2}X_2(I')\), with explicit constants.
  - \(D_\theta\): \(\mathcal M_w\ge((4/\pi^2)^5\varepsilon^2/48-o(1))X^{(\varepsilon)}(I')\).
  - **Lemma 3:** the Fejér bounds.
- (a3) **Theorem 3 and Corollary 3.1** (admissible). The \(\eta\)-mixed interval laws give \(\mathcal M_w\ge c(\eta)X_{\rm off}(\mathbf 1_{I'})\), \(|I'|\asymp\sqrt p\). An admissible-only bound \(\mathcal M_w\le Cp^{16/13-\delta}\) implies \(E^\times(I'-1)\ll|I'|^{32/13-2\delta}\).
- (a4) **Theorem 4 and Corollary 4.1** (\(\mathcal H\)). The \(D_\theta^\eta\) laws satisfy every item of \(\mathcal H\) and carry the same bound. So do sector-free (NC) arguments.
- (a5) **Proposition 5** (on (NC), fixed thresholds). Lemma 1's hypothesis forces a geometric-progression Paley \(\rho\)-clique of size \(4K'+1\). Round 190 Criteria 5.1–5.2 transfer.

All are statements about laws in hypothesis classes and about methods. **None is a lower bound for the actual \(\mathcal M_w\)**, and none bounds \(\mathcal M_w\), \(X\), \(T_0\) or \(\Gamma_2\) from above.

**(b) Conditional.**
- (b1) If \(X^{(\varepsilon)}(I')\ge c_\varepsilon X_{\rm off}(\mathbf 1_{I'})\) for some fixed \(\varepsilon\) and all symmetric GPs of length \(\asymp\sqrt p\) (no near-diagonal concentration), then the pure laws \(g_J\), \(D_\theta\) also carry the obstruction, with constant \(\asymp\varepsilon^2c_\varepsilon\). This is not needed for the method cap.
- (b2) Under (GP-Sub\(_c\)) for all \(c\), the mixed families are excluded on (NC). Under (GP-Sub\(_\kappa\)), their obstruction to \(\mathcal M_w\le p^{16/13-\delta}\) disappears for \(\delta<5\kappa\) (Proposition 5 with Round 190 Criterion 5.2 and Theorem 37).
- (b3) External: a proof of `cand:gp-shifted-energy` below \(|I|^{32/13}\) at \(|I|\asymp\sqrt p\) removes the obstruction at the corresponding level. For \(\mathcal M_w=O(p)\) it would have to reach \(O(|I|^2)\).

**(c) Evidence.** §6: floating models at \(p\le4\cdot10^6\) (full \(\mathcal M_w\) at \(p\le2\cdot10^4\)), exact quadruple counts at \(p\le3\cdot10^7\), and exact identities at \(p\le229\).

## Remaining gap

1. **(F) for \(\mathcal M_w\).** \(\mathcal M_w=O(p)\) log-free per fixed block is unchanged: proved \(p^{4/3+o(1)}\) (Round 187). Below \(p^{16/13}\), every admissible-only or \(\mathcal H\)-only route needs `cand:gp-shifted-energy` below \(|I'|^{32/13}\). At the target it needs \(O(|I'|^2)\). Otherwise it needs (NC2) with `cand:gp-sector-constancy`, which is qualitative.
2. **Pure-law refinement** (not needed for the cap): whether the nontrivial energy of \(1-I'\) can concentrate at \(|j|=o(K')\). The exact quantity is \(X^{(\varepsilon)}(I')/X_{\rm off}(\mathbf 1_{I'})\), or equivalently \(X_2(I')/(K'^2X_{\rm off})\).
3. **Unchanged.** (A) assembly, one-match \(43/24\), \(X\), \(\Gamma_2\), the cold line and the original theta-limit target. **Nothing here proves or refutes the original target.**

## Shared estimates (for the coordinator)

- **`cand:gp-shifted-energy`: touched in use, value unchanged.** It now also binds \(\mathcal M_w\) (Corollaries 3.1 and 4.1), and not only \(T_0\) and \(X\).
- **`cand:gp-sector-constancy`: touched in use, value unchanged.** The \(\mathcal M_w\) restriction needs a clique of length \(4K'+1\) (Proposition 5).
- **`cand:slope-row-mass-x`: not touched in value.**
- No new candidate is proposed.

## Ranked next tests

1. **Record the outcome and hold.** Following the Round 190 audit's §6.5 recommendation: if call 3 (`ordinary-gp-sector-constancy-literature`) finds (GP-Sub) open, then the ordinary first-mass line rests on `cand:gp-shifted-energy` (sharp form \(O(|I|^2)\) for the target), `cand:gp-sector-constancy` and (A). This report supplies the \(\mathcal M_w\) part of that statement. Further method-cap rounds for \(\mathcal M_w\) would only re-derive it.
2. **Only if a positive (NC2) route is pursued:** price the non-progression part of \(\mathcal M_w\) on (NC) with \(w\) kept, assuming (GP-Sub\(_\kappa\)). This is Round 190's "lower-height sector laws" question with \(\mathcal M_w\) in place of \(T_0\). It needs \(E^\times(I-1)\) for \(|I|>\sqrt p\) (Theorem 37 covers \(|I|\le p^{13/23}\)).
3. **Optional, cheap (pure-law refinement):** a literature or structural check of whether a near-diagonal concentration of the energy of shifted geometric progressions (quadruples with \(AD/(CY)\) of small exponent) is excluded by any known argument. It would not change the method cap.

## Replay

```bash
.venv/bin/python -B research/paley-191-mwsector-exponents.py                 # exact Fractions; ALL OK (<1 s)
.venv/bin/python -B research/paley-191-mwsector-exact.py                     # exact; ALL EXACT CHECKS OK (~2 s)
.venv/bin/python -B research/paley-191-mwsector-models.py --check            # FFT form vs brute force; CHECK OK (<1 s)
.venv/bin/python -B research/paley-191-mwsector-models.py laws 1009 5009 20011 100049 1000033 4000037   # floating, ~15 s
.venv/bin/python -B research/paley-191-mwsector-models.py jdist 0.25 100049 1000033 4000037 10000121 30000001   # integers, ~2 s
.venv/bin/python -B research/paley-191-mwsector-models.py jdist 0.5 1000033 10000121                            # integers, ~2 s
```
numpy 2.3.5 (repository `.venv`), Python 3.12. Model seeds are deterministic in \(p\).

## Verdict

**Yes (supported), in the mission's sense, with this scope.**
- **What is proved.**
  - For the hypothesis classes that contain the Round 189 interval laws and the Round 190 laws \(D_\theta\), there are laws with \(\mathcal M_w\ge c(\eta)X_{\rm off}(\mathbf 1_{I'})\), \(|I'|\asymp\sqrt p\), \(w\) kept. These are the \(\eta\)-mixtures: admissible (Theorem 3), and satisfying every sector-free (NC) consequence (Theorem 4).
  - Hence admissible-only and sector-free (NC) arguments for \(\mathcal M_w\le p^{16/13-\delta}\) must prove \(E^\times(I'-1)\ll|I'|^{32/13-2\delta}\). For \(\mathcal M_w=O(p)\) they must prove \(E^\times(I'-1)=O(|I'|^2)\).
- **What the weight does.** \(w\) removes sector pieces only for laws with a plateau at height 1:
  - exact subgroup laws, completely;
  - pure Fejér profiles, down to a second-moment-weighted energy that models put at a constant fraction.

  No hypothesis now in use forces such a plateau.
- **Consequence.** The pivot from \(T_0\)/\(X\) to \(\mathcal M_w\) is not easier in kind: \(\mathcal M_w\) meets the same geometric-progression wall below \(p^{16/13}\) (covariance-equivalent \(45/26\)), and the same (NC2)/(GP-Sub) lever.
- **What is not shown.** Nothing here bounds or lower-bounds the actual \(\mathcal M_w\). The original target is untouched.

## Script hashes (final)

Final replay on 2026-11-21: exponents `ALL OK`; exact `ALL EXACT CHECKS OK`; models `CHECK OK`. The laws and jdist runs are as quoted in §6.

| script | SHA-256 |
|---|---|
| `research/paley-191-mwsector-exact.py` | `1cd6ffde2bb38a8b7bf3cf324a1a77856c584485036cb8e691ee32dd82ed8a2a` |
| `research/paley-191-mwsector-exponents.py` | `f9df0841491f7c29d6660ee791a17f6fb2049e436ed4141399e92594a1bab7f9` |
| `research/paley-191-mwsector-models.py` | `4b3582ea9a5a54e54e486eb05d2662637d38333a4af66c464add0f4dd8261912` |
