# Adjacent marked sensitivities at the original angular cutoff

On the [round-100 square](astra-mixed-100.md) the selected comparison has zero counting excess on every ray for every eligible prime with
\[
                    10^{30}\le n=(p-1)/2\le 1.7\cdot10^{304}.
\]
The former explicit no-activation ceiling was \(10^{296}\). The new estimate compares the derivative of the genuine stationary row to a sum of propagated physical marked columns at height 517. Its defect contains consecutive differences of one marked forcing coefficient. The construction below is finite-depth. It does not extend the round-100 stationary existence ceiling of \(10^{358}\) or settle the ordinary-theta limit.

## The signed adjacent differences

Let \(a=2031/128, h=2^{-17}, L=a-h\) and \(Q=\{|\Re t-a|,|\Im t|\le h\}\). Use the genuine nine-center rows \(V_{k+1}=K\Phi_t(V_k)\), with \(\Phi_i(v)=\sqrt{4t_i+v^2}\), \(t_0=n\) and \(t_i=t\) elsewhere. All roots are positive on the real diameter. Write \(D_k=\operatorname{diag}\Phi_i'(V_{k,i})\), \(R_k=V_{k+1}-V_k\), and
\[
             f(v)=-2n/(t\sqrt t\,\sqrt{4n+v^2}),\qquad F_k=f(V_{k,0}).
\]
The true \(P_k=\partial_t(V_k/\sqrt t)\) obeys \(P_{k+1}=KD_kP_k+F_kKe_0\). On these same rows take an additional direction \(J_0=0,\ J_{k+1}=KD_kJ_k+F_kKe_0\). It is the sensitivity with the initial **normalized** row held fixed at the evaluation floor. In particular
\[
                P_k-J_k=(KD_{k-1})\cdots(KD_0)P_0 .
\]
For either \(A=P\) or \(A=J\), write \(G_k=A_{k+1}-A_k\). Then, for \(k\ge1\),
\[
 G_k=KD_kG_{k-1}+K\{(D_k-D_{k-1})A_{k-1}+(F_k-F_{k-1})e_0\}.       \tag{1}
\]
Before taking absolute prices the marked coordinate of the braced term equals
\[
 R_{k-1,0}\int_0^1
  \frac{4n A_{k-1,0}+2n v_s/(t\sqrt t)}
       {(4n+v_s^2)^{3/2}}\,ds,\qquad
 v_s=V_{k-1,0}+s R_{k-1,0}.
\]
At any bulk site it is \(R_{k-1,i} A_{k-1,i}\int_0^1\Phi_i''(V_{k-1,i}+sR_{k-1,i})\,ds\). In particular the common order-one forcing in packet units cancels. On \(|v|\le4.8\), \(|f'(v)|<0.02/\sqrt n\). As \(Ke_0\) has packet price \(\sqrt p/n\), the packet cost of the surviving marked **forcing difference alone** is less than \(0.029|R_{k-1,0}|/n\). The marked multiplier change in (1) is included separately in the curvature bound.

For the rest take \(A=J\), with \(C_k\) an upper bound on \(\|J_k\|_\infty\). Write \(d_k\) for the [physical seed-disk derivative bound](astra-mixed-100.md#the-genuine-physical-segment-products) on the incoming segment to \(V_k\), and \(\rho_k=0.169724\prod_{j=1}^k d_j\), so \(\|R_k\|_{2,n}\le\rho_k\) in the counting mean. The initial difference is just \(F_0Ke_0\), giving \(\|G_0\|_{2,n}<0.016\) since \(\|Ke_0\|_2\le1\) in ordinary counting norm. On every prefix segment \(|\Phi_i''|<0.138\), by \(4(a+2h)/(4L-1.94^2)^{3/2}\) in the bulk and the smaller marked bound \(4n/(4n-1.94^2)^{3/2}\). Since \(|R_{k-1,0}|\le\sqrt n\,\|R_{k-1}\|_{2,n}\), (1) gives
\[
 \|G_k\|_{2,n}\le\rho_k b_k,\qquad
 b_0=0.016/0.169724,\qquad
 b_k=b_{k-1}+(0.138 C_{k-1}+0.02/10^{15})/d_k.                     \tag{2}
\]
This prices neither of the two uncanceled marked columns separately.

The [outward checker](astra-marked-101-check.py) uses the round-100 packet construction on \(Q\) to obtain each \(C_k\). Its only change to the propagation of the angular source is the zero initial scalar error for \(J\). At every step it keeps the length-50 array of nonzero packet caps and charges the escaped weights, derivative tails and finite-prime repairs exactly as in round 100. From the [Arb192 replay](astra-marked-101-checks.jsonl),
\[
 C_{517}<14.852559,\qquad \rho_{517}<2.291039\cdot10^{-156},
 \qquad b_{517}<438.907 .
\]

## Compare with the true derivative before integrating the angle

Write \(m=517, c=\sqrt n\rho_m\). A counting second-norm ball of radius \(0.01\) about \(V_m\) enlarges its seed disks of radius \(1.94\) to radius \(B=1.95\). The original seed bound \(s=2.828428\) and the inequality \(2s(4L-2B^2)>4B(s+B)^2\) from the [disk maximization](astra-source-88.md#the-seed-centered-disks-on-the-complex-square) give Lipschitz constant \(d_*=(s+B)/\sqrt{4L+(s+B)^2}\); let \(M=(1-d_*)^{-1}<2.07\). At the claimed size ceiling, \(Mc<0.000616\). The ball is invariant and contracts. Picard convergence produces the physical real-on-real holomorphic stationary row \(Y\) with counting distance \(\|Y-V_m\|_2\le Mc\). The strict margins also give local extension to boundary floors.

Let \(P_*=\partial_t(Y/\sqrt t),\ D_*=\operatorname{diag}\Phi_i'(Y_i)\). Subtract the two exact marked equations at the terminal floor to obtain
\[
 (I-KD_*)(P_*-J_m)=G_m+
       K\{(D_*-D_m)J_m+[f(Y_0)-F_m]e_0\}.                          \tag{3}
\]
The inverse costs at most \(M\) in counting second norm. The curvature on the enlarged disk is below \(0.139\), and the full segment to \(Y\) has modulus below 4.8. In counting second norm (2) and (3) therefore imply, uniformly on \(Q\),
\[
 \|P_*-J_m\|_\infty\le
 M\big[b_m c+(0.139 C_m+0.02/10^{15})Mc\big]<0.272589 .
\]
Reality on the diameter and vertical integration of the **true** derivative give
\[
 \|\Im(Y/\sqrt t)\|_\infty
 \le h(C_m+0.272589)<0.000115396<2\cdot10^{-4}/\sqrt3 .
\]
At a first activation its stationary unit-product row coincides with \(Y\) by the [physical secant uniqueness argument](astra-mixed-100.md#a-marked-only-angular-source-and-an-explicit-no-hit-interval). Indeed the predictor disks enlarged by \(0.01\) give \(|\Im\operatorname{arsinh}(Y_i/(2\sqrt{t_i}))|<0.4\), and the first-hit phase has modulus below \(0.001\). The hyperbolic midpoint secant has modulus strictly below one at every site of the finite field. The actual hitting bulk coordinate would have rotated imaginary part at least \(2\cdot10^{-4}/\sqrt3\), yielding the claimed exclusion with the original threshold.

1. At increasing depths, directly bound the signed sum \(J_m=\sum_{j<m}(KD_{m-1})\cdots(KD_{j+1})F_jKe_0\) on the physical square. If the prefix disk and contraction margins persist, a uniform terminal bound below \(2\cdot10^{-4}/(\sqrt3 h)\) by a fixed positive gap and \(\sqrt n\rho_m\to0\) suffice: the omitted homogeneous initial derivative has coordinate norm at most \(\sqrt n\|P_0\|_{2,n}\rho_m/\rho_0\) (use each next incoming disk), and the counting stationary displacement costs \(O(\sqrt n\rho_m)\). The round-100 Cauchy estimate bounds \(P_0\) uniformly. The finite packet table establishes neither growing-depth hypothesis.
2. In (1) retain the signed bulk products \(R_{k-1,i}J_{k-1,i}\) through their actual subsequent \(KD\) transports before taking coordinate bounds. Equation (2) charges each such term with the full \(C_{k-1}\). The remaining exceptional forcing difference already costs \(O(|R_{k-1,0}|/n)\) in packet units.
