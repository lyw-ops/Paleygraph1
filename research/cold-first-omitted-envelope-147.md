# Positive prices for the actual first omitted cold center and residual

Use the genuine height-\(h\) predictors \(V_h\) for \(h=601,602\), the original closed cold square with \(t_0=n\), and \(A_h=KD_h\). Write their inherited fixed nine-center row as \(\mathcal C=S+\alpha Y+\mathcal C_{\rm oth}\), and \(V_h=\mathcal C+Y_h\) with \(Y_h\) the actual Picard residual. This \(Y_h\) is distinct from the fixed Legendre center \(Y\). The selected contracting baseline is \(B=K(D^{\rm J}+D^{\rm L})\) with actual Legendre amplitude from [Round 146](cold-actual-legendre-amplitude-146.md). Define the first omission
\[
 O_h=K\,\operatorname{diag}\bigl(d'_{t_i}(S_i)(\mathcal C_{{\rm oth},i}+Y_{h,i})\bigr).
\]

Uniformly on the square for all sufficiently large eligible primes, the inherited translated \(P_{5000}\) norm satisfies
\[
 \|K\operatorname{diag}(d'_{t_i}(S_i)\mathcal C_{{\rm oth},i})\|<0.150,
 \qquad \|O_h\|<0.408 .
\]
The \(0.142\) bound of [Round 136](cold-resummed-136.md) on the part of the full derivative of nonseed degree at least two remains applicable. Thus \(\|A_h-B\|<0.550\) is a uniform physical upper at both heights. It still exceeds the sufficient omission ceiling \(0.366\). If the fixed-other-center rate \(0.150\) is charged separately, the first-order Picard-residual budget is \(0.074\), with preceding strict bounds, in order to reach \(0.224\) for the combined first-order target.

## Actual removal before taking absolute values

Use the Round 136 signed Laurent coefficients of \(d'_t(S)\), common to all factors at nonseed arity one. The stationary center comparison there contains the fixed Legendre kernel exactly as \(a(\delta_0+(\delta_{-2}+\delta_2)/2)\), with \(a\) the chosen upper on \(|\alpha|\). In the folded list it contributes \(a\) at zero and \(a\) at two. To bound the actual first omission remove the field \(\alpha Y\) in the representation, then build the unsigned majorant of \(\mathcal C_{\rm oth}+Y_h\) from the other center coefficients and the actual height-\(h\) residual. This deletes those two \(a\) entries of the prescribed positive center construction. It does not subtract the bound on a norm from another bound.

Convolve the remaining folded list with the Round 136 modulus list formed from the already collected coefficients at nonseed degree one. The retained row has support within the Round 136 finite cut. At the height-\(h\) residual use the original excess-zero bound and charge the omitted tilted part by \(10\varepsilon\|\gamma_1\|_{\rm tilt}\), where \(\gamma_1\) is the retained Laurent majorant and \(\varepsilon=5\cdot10^{-7}\). The entire inherited \(0.0000407\) analytic tail bounds this selected subset of mixed words. Both compact lift and actual marked-diagonal repairs are uniform \(O_{5000}(n^{-1/2})\) times the input price, by the same summable arity-one proof as [Round 137](cold-linear-split-137.md). The checked finite inequalities are strict and absorb these physical repairs eventually.

## Obstruction to repricing this first-omitted majorant

On its first twelve base weights the retained positive comparison just constructed has a common positive integer vector whose componentwise image exceeds \(0.356\) times the vector at each height. The matrix formula is the same folded-column formula as in [Round 146](cold-actual-legendre-amplitude-146.md), now with this first-omitted retained row. The check uses strict outward inequalities; the vector was chosen numerically before replay. Consequently no positive homogeneous coordinatewise monotone reprice of this particular envelope reaches \(0.224\). This rules out changing just the price in the isolated omission test. It leaves the actual signed omission and the signed same-row square difference open.

Separately, Round 146's full direct comparison replay is an independent reconstruction of the older [Round 131 obstruction](cold-positive-block-131.md), whose stronger lower constants were \(1.036\) per step and \(1.073296\) for the two-height product of that same type of retained direct envelope. The amplitude refinement of Round 146 and the omission comparison here concern different claims; use the stronger old lower constants for the full direct-envelope obstruction.

Replay the [checker](cold-first-omitted-envelope-147-check.py) in the existing python-flint environment. Its [two records](cold-first-omitted-envelope-147-checks.jsonl) contain the strict 192-bit comparisons; no floating-point output is used as a bound on the signed derivative.
