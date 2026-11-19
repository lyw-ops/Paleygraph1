"""Replay the round 70 rounded lower map after pricing the selected cross-list merge."""
from contextlib import redirect_stdout
from io import StringIO
import json
from pathlib import Path
import runpy
from flint import arb
with redirect_stdout(StringIO()):
    data = runpy.run_path(str(Path(__file__).with_name("astra-new-sectors-70-check.py")))
errors = data["errors"][:]
errors[0] += arb('4e-15')
height,binary = data['old']['previous']['escape'](data['rows'],data['costs'],errors)
print(json.dumps(dict(height=height,binary_1e9=data['prior']['q']['scaled'](binary,10**9),
                      per_bin_cross_list_debit='4e-15',threshold=21)))
