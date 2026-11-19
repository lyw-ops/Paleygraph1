"""Exact original unary prices and the signed old-group debit on exterior translates."""
from pathlib import Path
import runpy
from flint import arb, ctx
q=runpy.run_path(str(Path(__file__).with_name("astra-unary-69-check.py")))
tabs,marked,base=q["tables"](True)
project,scaled=q["project"],q["scaled"]
amp=arb(144291005,24500)/10**12
prices=[]
for r in range(4):
    for e in range(r%2==0,4,2):
        d=project(marked,base,r,e)
        pieces=[-(r+1)*amp*project(tab,base,r+1,e) for tab in tabs]
        orig=sum(map(abs,pieces),arb(0))
        unary=sum(pieces,arb(0))
        assert d+unary>0 or d+unary<0
        sign=1 if d+unary>0 else -1
        # On this certified half line the loss is twice the opposite-sign mass.
        def opposite(a):
            neg=-sign*a
            return arb(max(arb(0),neg.lower())).union(max(arb(0),neg.upper()))
        loss=2*sum((opposite(a) for a in [d]+pieces),arb(0))
        prices.append(dict(r=r,e=e,direct=scaled(d,10**12),
                    pieces=[scaled(x,10**12) for x in pieces],
                    original_price=scaled(orig,10**12),signed_unary=scaled(unary,10**12),
                    combined=scaled(d+unary,10**12),loss=scaled(loss,10**12)))
q["old"]["record"]("original_and_signed_unary_prices",precision=ctx.prec,
                   units="1e-12",floor="2031/128",prices=prices)
