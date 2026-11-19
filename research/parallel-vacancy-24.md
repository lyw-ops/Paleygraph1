# Nonsquare vacancies: an exact defect identity and an exhaustive finite range

This follows [Round 23](parallel-directions-23.md) for [ETH Randomstrasse101 Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/). **The uniform positive vacancy density along critical prime families remains unproved.** The new prime-field result here is an exhaustive finite calculation, with independent coverage and extremum audits:

* For every prime \(p\le10^6\) and every even-order \(B\le (\mathbb F_p^\times)^2\) with \(19/20\le |B|/\sqrt p\le21/20\), at least \(10/33\) of all nonsquares are vacant affine ratios.
* There are 4,887 subgroup cases on 2,554 distinct primes in this range. For the 4,833 cases with \(p\ge10^4\), either choice of the twist sign has at least \(9|B|/28\) mismatches away from the identity.

These are exact finite statements, not sampled diagnostics or asymptotic bounds. I also prove a cell-square identity sharpening the vacancy-to-twist transfer. That identity is field-uniform and vanishes on the norm-one square control; it is **not** a new prime-only obstruction.

## 1. An exact sum of squares

Let \(P\equiv1\pmod4\) be an odd field order, \(B\le Q\) have even order \(b\), and \(d:B\to\{\pm1\}\) be its nontrivial order-two character. Put
\[
Y=(1-B)\setminus\{0\},\qquad R(u)=|Y\cap uY|,
\]
\[
S=\sum_{x\in B\setminus\{1\}}d(x)\chi(1-x),\qquad
V=\#\{u:\chi(u)=-1,\ R(u)=0\}.
\]
Use the affine cells of Round 23. A cell \(C=(\alpha B,\beta B)\) has solutions \((\alpha_i,\beta_i)\) to \(\alpha_i+\beta_i=1\), and size \(N_C\). Restrict to cells with \(\chi(\alpha)\chi(\beta)=-1\). For a nonempty cell choose one solution \((\alpha_0,\beta_0)\) and set
\[
c_i=d(\alpha_i/\alpha_0)d(\beta_i/\beta_0),\qquad L_C=\sum_i c_i.
\]
Changing the reference changes all signs together, so \(L_C^2\) is well-defined. Empty cells have \(L_C=0\). Then
\[
\boxed{\quad S^2+2\sum_{C:\,\chi(\alpha\beta)=-1}L_C^2=P.\quad} \tag{1}
\]
Moreover a cell of size \(N_C\) supplies exactly \(N_C\) values of \(u\) with \(R(u)=N_C-1\). Consequently
\[
\boxed{\quad
V=\#\{C:N_C=1,\ \chi(\alpha\beta)=-1\},\qquad
S^2+2V\le P.
\quad} \tag{2}
\]
More precisely,
\[
P-S^2-2V=2\sum_{C:\,\chi(\alpha\beta)=-1,\ N_C\ge2}L_C^2. \tag{3}
\]

**Proof.** The correspondence \(u=-\beta_i/\alpha_i\) identifies the solutions in these cells with the \((P-1)/2\) nonsquares. Thus the diagonal contribution to \(\sum_C L_C^2\) is \((P-1)/2\). An ordered pair of distinct solutions is specified uniquely by
\[
x=\alpha_j/\alpha_i,\qquad y=\beta_j/\beta_i,
\]
where \(x,y\in B\setminus\{1\}\), \(x\ne y\). Indeed
\[
\alpha_i=\frac{1-y}{x-y},\qquad \beta_i=\frac{x-1}{x-y}.
\]
It belongs to the nonsquare cells precisely when \(\chi(1-x)\chi(1-y)=-1\), and its contribution is \(d(x)d(y)\). Since \(\sum_{x\ne1}d(x)=-1\), the off-diagonal contribution is
\[
\frac12\left((2-b)-\big(S^2-(b-1)\big)\right)=\frac{1-S^2}{2}.
\]
This proves (1). A size-one cell has \(L_C^2=1\), yielding (2) and (3). No incidence bound, characteristic restriction beyond the stated field hypotheses, or asymptotic error is used.

## 2. A sharper mismatch transfer, with the same limitation

For either \(\sigma=\pm1\), let
\[
r=\#\{x\in B\setminus\{1\}:\chi(1-x)\ne\sigma d(x)\}.
\]
Then \(S=\sigma(b-1-2r)\), and (2) gives
\[
\boxed{\qquad
2V\le P-(b-1-2r)^2
=P-(b-1)^2+4r(b-1-r).
\qquad} \tag{4}
\]
Here the identity is not counted as a mismatch. In particular the linear mismatch coefficient in the critical window is \(2br\) for \(V\), rather than a bound in terms of \(8b\) times an exceptional-set size that includes 1.

There is a direct sharpening of the cell argument. Split the mismatches according to \(d\), with counts \(r_+,r_-\); the matching counts are \(g_+=b/2-1-r_+\), \(g_-=b/2-r_-\). Same-label ordered pairs in nonsquare cells correspond **exactly** to relative ratios with equal \(d\)-labels and exactly one mismatch. Their total is
\[
A=2(r_+g_++r_-g_-).
\]
A cell of size \(N\ge3\) has at least \(N(N-2)/2\) same-label ordered pairs. Therefore the nonsquare excess satisfies
\[
\sum_{\chi(u)=-1}(R(u)-1)_+\le 2A.
\]
Together with the exact nonsquare mass this also gives (4), including its negative quadratic term. Counting all pairs with *at least one* exception loses the fact that two exceptions restore the expected sign.

For \(b\sim\sqrt P\), (4) still only says that \(r=o(b)\) forces \(V=o(P)\). It supplies **no lower bound on \(V\)**. Thus (1)–(4) sharpen the accounting and provide exact checkable certificates, but do not close the arithmetic step requested in Round 23.

## 3. Exhaustive prime calculation

The range is specified by integer inequalities:
\[
p\le10^6,\quad b\equiv0\pmod2,\quad 2b\mid p-1,
\qquad 19^2p\le20^2b^2\le21^2p.
\]
For a prime, there is one subgroup of each eligible order, so this covers every \(B\) in the stated range. The [scanner](parallel-vacancy-24-check.py) enumerates \(p=bk+1\) with even \(b,k\), proves primality by a sieve, constructs the subgroup from a primitive root, and constructs the full ratio histogram with exact int64 modular arithmetic. At \(p\le10^6\), every product is less than \(10^{12}\), far below the signed int64 limit. There are no floating-point transforms or sampled ratios. The summary extrema are checked by integer cross-multiplication.

The [independent standard-library audit](parallel-vacancy-24-audit.py) reverses the coverage enumeration: it sieves primes first, then tests every even \(b\) in the window by divisibility. Its case set matches all 4,887 rows. It directly reconstructs the subgroup by testing \(x^b=1\), and reconstructs the ratio histogram by a Python `Counter`, at all extrema and every case with \(p\le5000\): 34 cases in total. The scanner separately verifies (1) by explicit cell enumeration for those small cases.

| Prime range within the window | Cases | Minimum \(V/((p-1)/2)\) | Attaining \((p,b)\) | Minimum best-sign mismatch fraction \(\min_\sigma r_\sigma/b\) | Attaining \((p,b)\) |
|---|---:|---:|---:|---:|---:|
| \(p\le10^6\) | 4,887 | \(10/33\) | \((2113,48)\) | \(0\) | \((17,4)\) |
| \(10^3\le p\le10^6\) | 4,879 | \(10/33\) | \((2113,48)\) | \(9/35\) | \((4481,70)\) |
| \(10^4\le p\le10^6\) | 4,833 | \(5203/16093\) | \((64373,266)\) | \(9/28\) | \((13217,112)\) |
| \(10^5\le p\le10^6\) | 4,298 | \(6413/19665\) | \((157321,414)\) | \(39/103\) | \((185401,412)\) |

For the full range the maximum of \(S^2/p\) is \(9/17\), attained at \((17,4)\). Above \(10^4\), it is \(1521/13217\), attained at \((13217,112)\). These additional extrema are recorded and audited; they are finite bounds only. The mismatch fraction uses \((b-1-|S|)/(2b)\), so it covers both signs, not just the parity-forced candidate \(\sigma=(-1)^{b/2}\).

Outputs: [all exact rows](parallel-vacancy-24-certified.jsonl), [coverage and extrema audit](parallel-vacancy-24-audit.json). Reproduce from the repository root:

```sh
.venv/bin/python research/parallel-vacancy-24-check.py --max-prime 1000000
python3 research/parallel-vacancy-24-audit.py
python3 research/parallel-vacancy-24-square-check.py
```

The word “certificate” here means reproducible exact finite counts and integer inequalities. It does not mean a Lean proof or an independently trusted formal proof of the program.

## 4. Square control and the remaining obstacle

For \(P=\ell^2\) and the norm-one group \(B\), Round 23 gives \(S=\sigma\ell\) and \(V=0\). Equation (1) then says every nonsquare cell has \(L_C=0\). In fact every nonempty nonsquare cell has exactly two solutions with opposite labels. The [square check](parallel-vacancy-24-square-check.py) independently constructs \(\mathbb F_{\ell^2}\), the norm-one group, the ratio histogram and all labeled nonsquare cells for \(\ell=7,11,13,31\); it verifies zero vacancies and zero sum of squared label sums in every case. [Exact square output](parallel-vacancy-24-square-certified.json).

The polynomial and clique-extraction routes tested here did not yield a growing lower bound for the mismatch count. After the two-anchor change of variables, removing the anchor exceptions leaves a set of size \(b-O(r+1)\) with at most \(r\) bad partners per point. Greedy extraction guarantees only a clique of size about \(b/(r+1)\). Comparing this to the prime [Hanson–Petridis bound](https://arxiv.org/abs/1905.09134) forces at most a constant-size mismatch obstruction, which is insufficient when \(r=o(b)\). Requiring the auxiliary polynomial to vanish at all exceptional ratios with the needed multiplicity incurs the same factor in its degree. I obtained no stronger root-multiplicity estimate.

Thus the new quantified prime evidence is exhaustive over the explicit finite range. The missing asymptotic step is still an unconditional prime-only lower bound \(V\ge c p\), or another estimate that rules out \(r=o(b)\) without assuming the desired twist gap. Neither the cell-square identity nor the finite counts establish that step or Problem 26.
