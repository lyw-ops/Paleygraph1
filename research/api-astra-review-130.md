# Review of the round-130 gateway draft

The [completion](api-astra-overflow-130.txt) returned with HTTP 200 and the requested Astra 6.2 response label. The [receipt](api-astra-130-receipt.json) records the reply and token usage.

The draft correctly recovers the old translated triangle majorant \(1.0628015736+O_{5000}(n^{-1/2})\) and the approximate \(1.04808\) middle-rate threshold needed at counting rate \(0.5145\). It adds the majorants for \(D_{600}\) and \(D_{601}-D_{600}\) separately. Its assertion that a successful estimate must cancel base mass does not follow. The bound \(m_0<0.002727\) does not give a lower bound on the base charge and a different majorant may avoid the second absolute price altogether. The proposed finite test at the center and four corners also leaves interior points unchecked.

The [coordinator derivation and full-square replay](cold-combined-height-130.md) expand the derivative at the actual \(V_{601}\) directly, reusing the nine-center kernels with one local residual envelope. They obtain a physical base rate below \(1.047425\) and an eventual translated rate below \(1.048\), including the two boundary coordinates. Thus the previous sufficient triangle bound fails, while the fixed-height transported kernels and signed quadratic sum retain exponent \(0.467\).

The gateway's useful next test was direct collective pricing on the physical prefix. That test is complete at \(601\). A sharper representation valid along an unbounded physical prefix, and the accompanying prime decay of the normalized residual, remain separate obligations.
