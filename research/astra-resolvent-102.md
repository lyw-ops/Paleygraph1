# The frozen marked column after subtracting the seed and dilation

At the original angular cutoff, the selected comparison has zero counting excess on every ray throughout the nominated square for every eligible prime with \(10^{30}\le n=(p-1)/2\le10^{310}\). This extends the [round-101](astra-marked-101.md) no-hit range. The proof bounds the physical frozen susceptibility itself at height 527. For growing heights there is an exact alternative involving a transported bulk source whose pure seed term starts in degree four.

## An exact elimination at one physical floor

Let \(a=2031/128, h=2^{-17}, L=a-h\) and \(Q=\{|\Re t-a|,|\Im t|\le h\}\). Take a physical nine-center Picard predictor \(V\) at this floor and its actual Jacobi seed \(S=2\sqrt n K e_0\). Write \(t_0=n, t_i=t\) otherwise, \(\Phi_i=\sqrt{4t_i+V_i^2}\) on the positive-real sheets, \(D_i=V_i/\Phi_i\), \(A=I-KD\), \(Z=A^{-1}K\), \(R=K\Phi-V\), and \(f=-2n/(t\sqrt t\,\Phi_0)\). Assume the physical disk bounds \(\|V\|_\infty<4.768,\ \|V-S\|_\infty<1.94\) from the [seed disk construction](astra-source-88.md); then \(A\) is invertible in counting second norm. Put \(P=fZe_0\), the genuine frozen marked susceptibility.

For \(i\ne0\) set \(x_i=V_i^2/(4t), u_i=\sqrt{1+x_i}\), and define the actual bulk preimage
\[
 b_i=\frac{1}{t}\left(\frac{x_i^2}{u_i(1+u_i)^2}
                    +\frac{(S_i-V_i)V_i}{4t u_i}\right),\qquad b_0=0.
\]
Then the following identity holds without representation-theoretic limits:
\[
 (1-\eta)P
 = Zb - \frac{2V-S}{2t\sqrt t}
          - \frac{A^{-1}R}{t\sqrt t},\qquad
 \eta=\frac{4n/\Phi_0-2\sqrt n+D_0 S_0-4\sqrt t}{2t\sqrt t\, f}.       \tag{1}
\]
Indeed, apply \(A\) to \(P+(2V-S)/(2t\sqrt t)\). Use \(AV=K(4t_i/\Phi_i)-R\), \(AS=S-KDS\), and subtract the constant \(4\sqrt t\) inside \(K\) before dividing by \(2t\sqrt t\). Off the mark the resulting expression equals \(((2+S_iV_i/(4t))/u_i-2)/t\). The identity \((2+x)/\sqrt{1+x}-2=x^2/[\sqrt{1+x}(1+\sqrt{1+x})^2]\) gives the stated formula. At the mark the remaining coefficient is exactly \(\eta f\); its transported column is \(\eta P\). This absorbs the exceptional feedback before taking any absolute prices.

On these disks \( |\eta|<9/\sqrt n\) for \(n\ge10^{30}\). Indeed \(|4n/\Phi_0-2\sqrt n|=|2\sqrt n\,V_0^2/[\Phi_0(2\sqrt n+\Phi_0)]|<12/\sqrt n\), \(|D_0 S_0|<7/\sqrt n\), and \(|2t\sqrt t f|=4n/|\Phi_0|\). The known coordinate shift in (1) is less than \(0.1\) in sup norm. Thus bounds \(\|Zb\|_\infty\le15\) and \(\|R\|_2=o(1)\) in **unnormalized** counting norm along increasing predictor heights, uniformly on \(Q\) with the same disks, would give a fixed gap below \(2\cdot10^{-4}/(\sqrt3 h)>15.13\). The counting contraction at the predictor then produces a stationary row with displacement \(O(\|R\|_2)\), and the zero-defect perturbation identity below transfers the gap. For \(V=S\) the quadratic term disappears exactly; for the true row the signed mixed term remains. No uniform estimate on its transported column follows from (1).

## The finite bound on the frozen susceptibility

Use the [round-101 signed arity kernels](astra-rank-101.md) at the **original** full complex square. Each debit was inside a single free arity. Thus the upper kernel at arity \(j\) bounds the corresponding signed coefficient before evaluation at the free argument, and multiplying it by \(j\) bounds its derivative coefficient. The distinguished subtractions at the root have arity zero. Keep the physical exceptional allowances, the tilt, the two truncations and the binomial derivative tail exactly as in [adjacent marked propagation](astra-marked-101.md). The physical initial residual upper \(0.169724\) still applies to the identical nine-center orbit. The [checker](astra-resolvent-102-check.py) uses the improved envelopes on each incoming segment, checking their monotonicity and seed-disk inequality. It propagates the marked direction \(J_0=0,\ J_{k+1}=KD_k J_k+f_kKe_0\) and the signed adjacent defect with the round-101 curvature and forcing-difference bounds.

Let \(m=527\), \(c=\sqrt n\rho_m\), where \(\rho_m\) bounds \(\|R_m\|_{2,n}\); write \(C_m\) for the computed coordinate cap of \(J_m\), and \(b_m\rho_m\) for the normalized second-norm bound on \(J_{m+1}-J_m\). With \(M=(1-d_*)^{-1}<2.07\) on the radius-0.01 enlarged terminal disks of round 101, \(Mc<0.01\). Counting Picard therefore yields the genuine real-on-real stationary row \(Y\), at counting distance at most \(Mc\). At the frozen predictor the exact equation
\[
 A(P-J_m)=J_{m+1}-J_m
\]
gives \(\|P\|_\infty\le C_m+M b_m c\). With \(P_* =\partial_t(Y/\sqrt t)\) the remaining transfer is
\[
 (I-KD_Y)(P_*-P)=K\{(D_Y-D)P+[f(Y_0)-f(V_0)]e_0\}.
\]
Consequently its counting second norm is at most \(M(0.139\|P\|_\infty+0.02/10^{15})Mc\). Both equations hold on the whole square, including the marked coordinate. The [outward replay](astra-resolvent-102-checks.jsonl) gives \(C_m<14.794860,\ \rho_m<2.364043\cdot10^{-159},\ b_m<451.324\), frozen cap \(15.014563\), and stationary motion below \(0.002093\). Thus \(h\|P_*\|_\infty<0.0001145680<2\cdot10^{-4}/\sqrt3\). Integration vertically from the real diameter bounds the normalized stationary imaginary part by the same upper. At first activation the selected unit-product row coincides with \(Y\) by the [physical midpoint secant](astra-mixed-100.md); its hitting coordinate would violate this strict inequality. This proves the stated no-hit interval. The finite calculation uses the propagated marked form, independently of (1). The existing separate stationary existence ceiling remains \(10^{358}\); the ordinary-theta limit stays open.

Replay from the repository root:

    PYTHONPATH=. .venv/bin/python -B research/astra-resolvent-102-check.py

1. At increasing predictor depths test the **combined** signed source \(b\) in (1), with the marked row erased exactly as specified and the true transported inverse. A uniform bound of 15 together with the stated disk and counting residual hypotheses excludes the first hit.
2. Resolve the mixed term by writing \(V-S=(V_0-S)+\sum_{k<m}R_k\), where \(V_0\) here denotes the initial **row** of the Picard orbit. Pool its known nine-center part with the quartic seed term before pricing any subsequent transported increment. Check whether this lowers the growing-depth surviving price at the actual bulk coordinates.
