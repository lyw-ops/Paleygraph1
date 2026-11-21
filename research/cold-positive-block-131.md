# A two-step obstruction for the retained positive packet comparison

Let \(Q\) and \(V_h\) be the original closed cold square and the genuine fully marked predictors of [Round 130](cold-combined-height-130.md). Write \(T(W)=K\Phi_t(W)\) on the physical sheets. Consider the nonnegative packet comparison used for \(T'(V_h)=KD_h\). Its positive matrix, before charging omitted weights and exceptional columns, is defined by the folded derivative masses \(\mu_{h,j}\) of the retained strip. An input packet of index \(k\) contributes \((k-1)\mu_{h,j}\) at output index \(j>0\) and \(\mu_{h,j}/2\) at each nonzero index \(k+j\) and \(|k-j|\). If two contributions coincide they are added. This is the price-column formula of [Round 82](astra-adjoint-82.md) in matrix form. Let \(L_h\) be its principal matrix on indices \(1,\dots,12\).

The [outward replay](cold-positive-block-131-check.py) uses the actual height-601 positive envelope of Round 130 and advances its verified recurrence once more. The depth-602 step keeps the dimension cap below \(4.8\) and omitted tilted activation mass below \(5\cdot10^{-7}\). For the integer vector
\[
 v=(1000000,420376,214684,114974,63462,35702,20352,11711,6779,3924,2235,1151)
\]
the replay gives \(L_{601}v>1.036v\) and \(L_{602}v>1.036v\), componentwise. The [saved records](cold-positive-block-131-checks.jsonl) are outward intervals. The witness was selected with a numerical eigensolver, and the componentwise inequalities are verified independently of that solver.

Consequently \(L_{602}L_{601}v>1.073296v\). The full nonnegative comparison obtained by multiplying the two separate majorants includes this principal product. For any strictly positive linear price vector \(\pi\), the estimate \(\pi^{\mathsf T}L_{602}L_{601}\le q_2\pi^{\mathsf T}\) would imply \(q_2>1.073296\), by testing against \(v\). This also obstructs every order-preserving homogeneous gauge on these packets that is positive at \(v\). The conclusion allows different prices at the intermediate half-step as long as the final price returns to the starting price. The scope is the product of these particular positive majorants of the exact two-step derivative at \(V_{601}\). The actual operator \(T'(V_{602})T'(V_{601})\) keeps its independent counting contraction. To price that operator in a packet ball, it remains possible to collect signed contributions jointly, use a smaller arithmetic comparison, or move the center.

## The signed residual and the half-step sheet

For any actual step based at \(V\), write \(R=T(V)-V\) and \(E_2=T^2(V)-V\). On the genuine segment from \(V\) to \(T(V)\) let \(B_{\rm sec}\) be \(K\) times the diagonal of averaged scalar derivatives along this segment. On the common sheets one has
\[
 E_2=(I+B_{\rm sec})R.
\]
If \(\|B_{\rm sec}\|_{2\to2}\le q<1\), then
\[
 (1-q)\|R\|_{2,n}\le \|E_2\|_{2,n}\le(1+q)\|R\|_{2,n}.
\]
This rules out a two-cycle on that segment. It also makes an actual signed two-step defect decay estimate at a moving starter equivalent to the one-step decay estimate when \(q\) is uniformly below one. At height 600 one may use \(q=0.515\) from [Round 126](cold-actual-first-insertion-126.md).

For a block invariance proof, an even-step ball \(B\) with \(T^2(B)\subset B\) also needs sheet and secant control on segments joining successive odd and even rows. A sufficient geometric hypothesis is that \(B\cup T(B)\) lies in common convex coordinate disks with a uniform scalar derivative bound \(q<1\). Then all successive increments of the actual orbit contract in counting second norm, starting from the actual initial residual. In particular if the ball test holds uniformly on \(Q\), the orbit converges at each prime uniformly on \(Q\) and the limit is stationary there, holomorphic on the interior. After choosing a logarithmically growing depth, the normalized residual satisfies \(o(n^{-0.2665})\). This block route would itself construct the stationary section. If using the varying-kernel comparisons further, the shifted-kernel price still needs verification at the relevant moving depth.

The signed block test remains open. A normalized second-norm residual cap at a fixed height gives no maximum-norm confinement on the growing fields. The frozen partial-residual input of [Round 122](cold-frozen-orbit-transfer-122.md) has precisely that missing norm.
