"""All-arity price for trees with only internal Jacobi-square edges."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
import runpy
from flint import arb

here = Path(__file__).parent
with redirect_stdout(StringIO()):
    source = runpy.run_path(str(here / "astra-histories-71-check.py"))
t = source['t']
D = source['radius']
assert ((D+1)**2+4*t).sqrt() < 20
h1 = source['unary'](2)
assert abs(h1)<arb('.002')
s = arb('7.1e-8')
nonempty = arb('.002')*s + 20*(4*s)**2/(1-4*s)
assert arb('7e-8')+nonempty < s
assert 2*nonempty < arb('3e-10')
with redirect_stdout(StringIO()):
    data = runpy.run_path(str(here / "astra-new-sectors-70-check.py"))
errors = data["errors"][:]
errors[0] += arb('3e-10')
height,binary = data['old']['previous']['escape'](data['rows'],data['costs'],errors)
print(json.dumps(dict(height=height,binary_1e9=data['prior']['q']['scaled'](binary,10**9),
                      per_bin_debit='3e-10',threshold=21)))
