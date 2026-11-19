# Truncated Picard references at the repair-tail scale

This note addresses the actual input of [Round 18](parallel-tail-18.md), for [ETH Problem 26](https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/). It does not prove the prime asymptotic. The new rigorous conclusions include a certified finite-prime failure of the first-reference upper-tail test, an explicit, width-improved perturbation bound for the complementarity-defined input, stability estimates for its repair and background injection, and a counterexample **using the actual square-field stationary input and actual first Picard iterate** to transferring small RMS error to small repair-tail error uniformly in the width. No generic random model is used.

The arithmetic fixed-width limit from [Round 13](parallel-fixed-width-13.md) is used as an existing input to the asymptotic square comparison; its sheaf-theoretic proof has not been independently re-audited here. The perturbation and stability lemmas below are elementary unconditional finite-dimensional statements.

## 1. Use complementarity, not projection, to build the truncated input

Put (d=(1-s)/(1+s)), (0<s<1), and let
\[
 v_{t+1}=dK\Phi(v_t),\quad v_0=0,\qquad z=dK\Phi(z),
 \qquad x_t=(\Phi(v_t)+\sigma v_t)/2,\quad
 y_t=(\Phi(v_t)-\sigma v_t)/2.
\]
Thus (x=x_\infty=A_\sigma(s)), (y=y_\infty=A_{-\sigma}(s)). Set (c_t=\langle j,y_t\rangle), (c=c_\infty), and (\beta=s/(1-s^2)). All iterates have zero mean, so the two members of each pair have the same mean. Define
\[
 D^{[t]}_i=\beta(\sqrt n(x_t)_i-(1-s)c_t)_+\quad(i\ne0),
 \qquad D^{[t]}_0=0.                                      \tag{1}
\]
At stationarity this is **exactly** the Round 17 cost (D=\sqrt n(-H)_+), provided (H_0>0), as in that construction. At finite depth it is a reference cost, not a claim that the truncated pair satisfies the reciprocal KKT equation. In particular, it usually differs from (\sqrt n(-(J+P)y_t)_+).

The scalar map (v\mapsto((\Phi(v)+v)/2,(\Phi(v)-v)/2)) is 1-Lipschitz into the product Euclidean space: off the mark it is the positive/negative splitting; at the mark the sum of squared derivatives is ((1+v^2/(v^2+4))/2\le1). Consequently
\[
 \|x-x_t\|_2^2+\|y-y_t\|_2^2\le\|z-v_t\|_2^2.
\]
Positive-part contraction, (|c-c_t|\le\|y-y_t\|_2), and Cauchy–Schwarz now give
\[
 \boxed{\ \frac{\|D-D^{[t]}\|_2}{\sqrt n}
 \le \beta\sqrt{1+(1-s)^2}\,\|z-v_t\|_2
 \le C_s d^t,\quad
 C_s=\frac{\sqrt{s}\sqrt{1+(1-s)^2}}{1+s}.\ }       \tag{2}
\]
For the second bound use (\|z-v_t\|_2\le d^t\|z\|_2\le 2d^{t+1}/\sqrt{1-d^2}). The identity (\|\Phi(z)\|_2^2=\|z\|_2^2+4) proves the last fixed-point norm bound. Zeroing the mark can only reduce the cost error. Thus (C_s\le\sqrt{2s}), uniformly in the order.

Directly projecting (y_t) only gives RMS error at most (\|y-y_t\|_2), without the factor (O(s)) in the first inequality of (2). Complementarity is therefore the preferable reference for this task. This improvement alone does not eliminate the tail-scale loss.

For any recipient set (T), (1) also gives the more useful *localized* estimate
\[
 \frac1h\sum_{i\in T}|D_i-D^{[t]}_i|
 \le\frac{\beta\sqrt n}{h}\sum_{i\in T\setminus\{0\}}|x_i-(x_t)_i|
       +\frac{\beta(1-s)|T|}{h}|c-c_t|.                 \tag{3}
\]
The localized row difference, rather than its global norm, is the remaining input here.

## 2. Repair stability and the two different scale losses

Use the same (b,P,\alpha) for the true and reference repair. This is important: a finite Picard pair need not have a valid reserve, so do not replace (b) by a budget inferred from that pair. Write (A_0=A'_0=b\mathbf1), and update with (D,D'), respectively. Then
\[
 \|A_k-A'_k\|_2\le k\alpha\|D-D'\|_2,
 \qquad \|r_k-r'_k\|_2\le(1+k\alpha)\|D-D'\|_2.       \tag{4}
\]
Proof: for a fixed cost, (A\mapsto A+\alpha P(D-A)_+) is nonexpansive on (b\mathbf1+\operatorname{im}P). If (u=A-A'\in\operatorname{im}P) and (w=(D-A)_+-(D-A')_+), scalar firm nonexpansiveness gives (\langle u,w\rangle\le-\|w\|_2^2). Expansion gives
\(|u+\alpha Pw\|_2^2\le\|u\|_2^2-\alpha(2-\alpha)\|w\|_2^2\).
Changing the cost at a fixed shadow changes the update by at most (\alpha\|D-D'\|_2). Induction proves (4).

The fractional top-(h) functional has Euclidean Lipschitz constant (1/\sqrt h) after division by (h): use its variational representation with weights (0\le w_i\le1), (\sum w_i=h), hence (\|w\|_2\le\sqrt h). Therefore (2)–(4) imply
\[
 \left|\frac{T_h(r_k)}h-\frac{T_h(r'_k)}h\right|
 \le(1+k\alpha)\sqrt{n/h}\,C_s d^t.                    \tag{5}
\]
For (m=O(h)) fixed recipients, the same argument gives (\sqrt m/h) in place of (1/\sqrt h). Since (h\asymp\sqrt n), these estimates lose (n^{1/4}). They supply a rigorous approximation at (t=O_s(\log n+\log(1/\eta))), but not at a depth independent of the field.

The Round 18 **full bulk load** is harder still. With a common cutoff and common exceptions,
\[
 |L_k-L'_k|\le \frac{\sqrt n}{h}\|r_k-r'_k\|_2
 \le(1+k\alpha)\frac n h C_s d^t.                     \tag{6}
\]
Here the loss is (n^{1/2}), not (n^{1/4}). A bound on a signed top-(h) tail must not be silently used as a bound on the sum of *all* positive cutoff excesses. Fixed-depth normalized-(\ell_2) approximation from Round 13 supplies neither missing rate.

## 3. The exact background quantity a localized comparison needs

Fix a cutoff (u\ge0), an exception set (J), and a recipient set (T\subseteq J^c). Put
\[
 C(r)_i=\begin{cases}(r_i)_+&i\in J,\\\min((r_i)_+,u)&i\notin J,\end{cases}
 \quad g(r)=C(r)+\min(r,0),\quad f(r)=g(r)-\alpha PC(r)-u\mathbf1.
\]
Outside (J), (g(r)=\min(r,u)); on (J), (g(r)=r). Both (C) and (g) are coordinatewise 1-Lipschitz. The Round 18 injection on this fixed recipient set is
(I_T(r)=h^{-1}\sum_T(f(r)_i)_+). If (\Delta C=C(r)-C(r')), (\Delta g=g(r)-g(r')), then
\[
 |I_T(r)-I_T(r')|
 \le h^{-1}\big(\|\Delta g\|_{1,T}+\alpha\|P\Delta C\|_{1,T}\big). \tag{7}
\]
Since (P=(I-J-\sigma K)/2), the right side is at most
\[
 h^{-1}\left[\|\Delta g\|_{1,T}
 +\frac\alpha2\{\|\Delta C\|_{1,T}+|T|\,|\overline{\Delta C}|
                         +\|K\Delta C\|_{1,T}\}\right].          \tag{8}
\]
These are unconditional inequalities, including when (T) is chosen from the actual next residual. The reference injection must then be evaluated on **that same (T)**; comparing two differently selected supports introduces another unbounded term. With only global information (7) is at most ((1+\alpha)\sqrt{|T|}\|r-r'\|_2/h). Hence the prime arithmetic problem is explicit: control localized clipped-row differences and localized (K\Delta C), or control the reference injection on a valid guard. No small-injection theorem is claimed here.

## 4. A rigorous counterexample with the actual square input

The first Picard iterate is (v_1=2dKe_0). The Jacobi cap gives (|\sqrt n(v_1)_i|\le2d\sqrt{q/n}), so, because (c_1\ge0),
\[
 0\le D^{[1]}_i\le U_s(q):=\frac{2s}{(1+s)^2}\sqrt{q/n}
 \quad\text{at every coordinate}.                             \tag{9}
\]
Thus its initial top-(h) cost is (O(s)), uniformly in the order. The bound applies to prime inputs too.

Now take the actual plus row over (q=\ell^2) and the actual subfield annihilator (I), (|I|=h=(\ell+1)/2). Round 17's exact pairing gives
\[
 \frac1h\sum_I D_i\ge B+\frac a{m_0^{\rm sq}}-1,
 \qquad m_0^{\rm sq}=h/\sqrt n.
\]
Here (B\ge0): the reciprocal metric energy gives (c^2\le1). Combining with (9),
\[
 \frac1h\sum_I(D_i-D^{[1]}_i)
 \ge B+\frac a{m_0^{\rm sq}}-1-U_s(q).                         \tag{10}
\]
At each fixed (s), Round 13 gives (a\to1/(1+s)). Consequently
\[
 \liminf_{\ell\to\infty}\frac1h\sum_I(D_i-D^{[1]}_i)
 \ge\frac{\sqrt2}{1+s}-1-\frac{2\sqrt2s}{(1+s)^2}.             \tag{11}
\]
The right side tends to (sqrt2-1>0) as (s\downarrow0), whereas (2) gives RMS difference at most (\sqrt{2s}) for these **same actual/reference inputs**.

This disproves the specific sufficient shortcut: “a width-uniform modulus tending to zero converts normalized-(\ell_2) error between the stationary repair input and its Picard reference into error of its top-(h) average.” Indeed (T_h(D)/h\ge\operatorname{avg}_I D) and (T_h(D^{[1]})/h\le U_s(q)), so (11) lower-bounds the difference of the top-(h) averages as well. Subtracting a common initial mean (b) does not change their difference. Choosing a diagonal sequence of square orders at successively smaller fixed widths makes the RMS error vanish while the tail error stays positive.

This is **not** a counterexample to a prime-only transfer theorem, to fixed-(s) convergence as (t\to\infty), or to ETH Problem 26. It identifies the arithmetic distinction any usable transfer theorem must exploit. The square obstruction also survives every actual repair depth, because (P\mathbf1_I=0); a small reference cost cannot erase it.

## 5. A certified finite-prime failure of the first-reference upper test

There is also a rigorous finite-prime counterexample to the stronger shortcut
\(T_h(D)/h\le T_h(D^{[1]})/h\), and even to \(T_h(D)/h\le U_s(q)\).
At \(p=9413,s=1/64\), [the Arb replay](astra-background-19-certificate.py) and
[its two records](astra-background-19-certified.jsonl) certify:

| side | selected recipients \(m\ge h\) | actual selected mean, lower bound | reference pointwise cap, upper bound | certified tail gap, lower bound |
|---|---:|---:|---:|---:|
|plus|50|0.06256838|0.04284710|0.01972129|
|minus|49|0.06586254|0.04284710|0.02301545|

All displayed bounds are rounded outwards. The script rounds the numerical fixed-point seed to rational coordinates, uses 128-bit Arb DFTs and the contraction residual to enclose its distance to the exact stationary point (less than \(9.35\cdot10^{-12}\)), and computes lower bounds for (1) on the selected coordinates. It proves \(H_0>0\) separately. A single interval-certified off-diagonal Jacobi coefficient supplies a lower bound for \(\omega\), hence an upper bound for \(h\), below \(m\). The selected coordinates need not be certified to be the largest: the top-\(h\) average is at least the average on **any** \(m\)-set when \(h\le m\). Thus the certificate does not rely on floating-point sorting being exact. The cap (9) bounds every first-reference coordinate, so it bounds its top-\(h\) average as well.

These certificates apply to the actual prime initial cost. They do not refute a reference comparison with a sufficiently large explicit error term, or a deeper reference. Reproduce with `VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/astra-background-19-certificate.py > research/astra-background-19-certified.jsonl`.

## 6. Diagnostics on actual prime and square rows

[The replay](astra-background-19.py) computes actual reciprocal stationary rows with the existing numerical solver, constructs (1) from Picard depths (0,1,2,4,8,16,32,64,128), and uses the **actual** mean (b=3B/4) in both four-step repairs. It measures errors on actual top-(h) recipients and the depth-four background injection on the actual receiving set with cutoff (B/5), excepting only the mark. All output of this sweep is floating-point diagnostic data, distinct from the interval certificates in §5.

At (s=1/64), representative plus rows in [the 108-row sweep](astra-background-19.csv) are:

| order | Picard depth | cost RMS error | mean absolute error on initial top-(h) recipients | actual four-step tail | reference four-step tail |
|---|---:|---:|---:|---:|---:|
|153649|4|0.0075254|0.015333|0.0098420|0.0070541|
|153649|16|0.0032454|0.0045627|0.0098420|0.0095885|
|153649|64|0.00045932|0.00064093|0.0098420|0.0098167|
|389²|4|0.019643|0.35760|0.384671|0.027089|
|389²|16|0.012837|0.24404|0.384671|0.140636|
|389²|64|0.0027568|0.053304|0.384671|0.331374|

For the plus row at 153649, the actual depth-four injection is 0.00045550. Using the depth-16 Picard reference on the **same actual recipient set** gives 0.00032355, while the measured absolute forcing-difference bound from (7) is 0.00042364. At Picard depth 64 these become 0.00043935 and 0.00005694. The reference injection alone underestimates the actual injection; the localized comparison term is material.

The square error concentrates strongly on the relevant recipients; its small RMS is misleading. On the three prime orders 9413, 37253, 153649, the depth-16 localized initial-cost error is approximately 0.00515, 0.00484, 0.00456. At the additional prime 1000033 it is 0.0045721. This suggests testing a uniform **localized** estimate rather than paying the global (n^{1/4}) factor. Four orders do not prove uniformity or an asymptotic rate. A separate [million-order sweep](astra-background-19-million.csv) extends this diagnostic at (p=1000033).

Reproduce with `VECLIB_MAXIMUM_THREADS=1 OPENBLAS_NUM_THREADS=1 .venv/bin/python -B research/astra-background-19.py > research/astra-background-19.csv`; add `--primes 1000033 --roots` for the separate large-prime file. The code checks the conservative complementarity error bound, the four-step tail stability bound, and injection Lipschitz comparison on every row. It neither solves an endpoint LP nor establishes the unresolved prime localized-error or background-injection estimate.
