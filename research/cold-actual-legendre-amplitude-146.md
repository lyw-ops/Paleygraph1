# Actual Legendre amplitude and an obstruction to repricing the direct envelope

Work on the original fully marked closed cold square. Use the actual nine-center predictors at heights \(601,602\), \(A_h=KD_h\) with \(D_h=\operatorname{diag}(d_{t_i}(V_{h,i}))\), and the selected \(B=K(D^{\rm J}+D^{\rm L})\) of [Round 145](cold-jacobi-linear-legendre-145.md). Here \(D^{\rm L}_i=\alpha(t)Y_i d'_{t_i}(S_i)\), \(D^{\rm J}_i=d_{t_i}(S_i)\) and \(t_0=n\). The same chosen coefficient \(\alpha(t)\) is part of the fixed nine-center row at both heights. It is the first magnitude \(a\) returned by the accepted Round 65 coefficient programme and used in the actual Round 130 center mass \(s+2a+\cdots\).

## Refining the actual selected baseline

The original square replay in Arb at 192 bits gives \(a<0.244\). Multiply the linear Legendre kernel and its tail in the exact Round 145 comparison by \(0.244\), leaving its Jacobi kernel unchanged. Sum the retained positive columns before taking their supremum, exactly as there. The resulting rational geometric upper is \(0.6333\). The Round 145 marked and compact lift repairs remain uniform \(O_{5000}(n^{-1/2})\), so eventually
\[
 \|B\|_{P_{5000}}<0.634,\qquad
 \|KD^{\rm L}\|_{P_{5000}}<0.119.
\]
The linear rate follows also by multiplying \(0.487\) in the unit-amplitude bound by \(0.244\). With the pure Jacobi bound \(0.528\), the actual selected mixed orders have sum of rates below \(0.126\), and \(\|B^2\|<0.402\). These bounds are on the full specified two-boundary-pair packet class.

In consequence the sufficient actual omitted budget is \(0.366\) per step, or \(0.598\) for \(\|A_{602}A_{601}-B^2\|\). The already proved height change below \(0.017\) and full \(601\) price below \(1.048\) show that a same-row signed bound \(\|A_{601}^2-B^2\|<0.580184\) would suffice for the second option. All three sufficient inequalities require strict bounds on the full actual omitted piece. The higher Legendre terms and other predictors have not been absorbed. Nonlinear invariance and marked half steps remain separate.

## Repricing the direct retained envelope is insufficient

The [Round 130 positive geometric comparison](cold-combined-height-130.md) uses the fixed outward folded multiplier \(\mu^{(h)}\) on the whole square. Consider only the retained part of that one positive comparison at \(h=601\), and at \(h=602\) after advancing its actual prefix envelope one step. Ignore its additional positive analytic and lift charges. For the base source mode \(j\), the retained output folded mass of mode \(i\ge1\) is
\[
 M^{(h)}_{ij}=(j-1)\mu^{(h)}_i+
      \widetilde\mu^{(h)}_{i-j}+\widetilde\mu^{(h)}_{i+j},
 \qquad
 \widetilde\mu_0=\mu_0,\quad
 \widetilde\mu_k=\tfrac12\mu_{|k|}\ (k\ne0).
\]
The first term comes from its \(j-1\) zero weights and the other two from convolution with the two opposite source weights. The formula prices the exact chosen positive comparison derived from the retained envelopes, including the rounding specified there.

On modes \(1,\ldots,12\), both matrices send the same strictly positive integer vector in the checker componentwise above \(1.035\) times that vector. The height-\(602\) input is advanced with the accepted tilted loss test and marked augmentation, exactly as in Round 136. The inequalities use Arb and are strict even with both matrices enclosed outward. The twelve entries of the vector can be checked directly by substituting the retained positive coefficients. The vector was first selected by a floating-point eigensolver at height 601; the rigorous conclusion uses the componentwise check only.

A positive homogeneous, coordinatewise monotone norm on this comparison therefore has one-step rate exceeding \(1.035\) at either height, and two-height rate exceeding \(1.035^2=1.071225\). Indeed the vector, extended by zero, is a subinvariant lower, and comparison of the two componentwise inequalities gives the corresponding product bound. This rules out making the same direct absolute positive comparison contract by changing its price alone. It is not a lower bound for the actual \(A_h\), which contains signs and identifications discarded in that comparison, nor for any differently collected envelope.

The [replay](cold-actual-legendre-amplitude-146-check.py) uses the accepted Round 130 and Round 145 checkers and writes [two records](cold-actual-legendre-amplitude-146-checks.jsonl). The amplitude and subinvariance comparisons are outward interval checks, the selected price and slack comparisons use rational arithmetic, and the mathematical transport and norm conclusions have the scopes above.
