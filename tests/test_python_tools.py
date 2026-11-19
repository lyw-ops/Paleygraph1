"""Exercise the published-code boundary and transparent program launcher."""

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ENTRY_POINT = Path(__file__).resolve().parents[1] / 'scripts' / 'paley.py'


class PythonToolsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='paley-tools-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / 'scripts').mkdir()
        (self.root / 'research').mkdir()
        shutil.copy2(ENTRY_POINT, self.root / 'scripts' / 'paley.py')
        self.theta_source = '''"""Fixture theta program."""
import json
from pathlib import Path
import sys
print(json.dumps({"args": sys.argv[1:], "cwd": str(Path.cwd())}))
if "--stderr" in sys.argv:
    print("fixture stderr", file=sys.stderr)
raise SystemExit(7 if "--fail" in sys.argv else 0)
'''
        (self.root / 'theta.py').write_text(self.theta_source)
        (self.root / 'smoothing.py').write_text('"""Fixture shared module."""\nVALUE = "root import succeeded"\n')
        (self.root / 'parallel_kernel_11.py').write_text('"""Fixture legacy round script."""\n')
        (self.root / 'research' / 'example-91-check.py').write_text(
            '"""Fixture round script."""\nfrom smoothing import VALUE\nprint(VALUE)\n')
        for folder in ['first', 'second']:
            target = self.root / 'research' / folder
            target.mkdir()
            (target / 'duplicate-91.py').write_text('raise RuntimeError("must not run")\n')
        self.git('init', '-q')
        self.git('config', 'user.name', 'Test fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.git('add', '.')
        self.git('commit', '-qm', 'Fixture snapshot')
        self.revision = self.git('rev-parse', 'HEAD').stdout.strip()
        self.invoke('index', '--ref', self.revision, '--write', check=True)

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.root), *args], capture_output=True, text=True, check=True)

    def invoke(self, *args, check=False):
        # Launch outside the checkout to test that caller cwd is irrelevant.
        return subprocess.run([sys.executable, '-B', str(self.root / 'scripts' / 'paley.py'), *args],
                              cwd=self.root.parent, capture_output=True, text=True, check=check)

    def test_catalog_reads_committed_objects_without_importing_programs(self):
        (self.root / 'theta.py').write_text('raise RuntimeError("dirty working file must not be imported")\n')
        draft = self.root / 'research' / 'local-only-92-check.py'
        draft.write_text('raise RuntimeError("local draft must not be imported")\n')
        self.invoke('index', '--ref', self.revision, '--write', check=True)
        catalog = json.loads((self.root / 'scripts' / 'python-tools.json').read_text())
        tools = {item['path']: item for item in catalog['tools']}
        self.assertNotIn('research/local-only-92-check.py', tools)
        self.assertEqual(tools['theta.py']['description'], 'Fixture theta program.')
        self.assertEqual(tools['theta.py']['sha256'], hashlib.sha256(self.theta_source.encode()).hexdigest())
        self.assertEqual(tools['parallel_kernel_11.py']['round'], 11)
        self.assertEqual(self.invoke('index', '--check').returncode, 0)
        self.assertIn('dirty working file', (self.root / 'theta.py').read_text())
        self.assertTrue(draft.exists())

    def test_launcher_forwards_arguments_stdout_and_nonzero_exit(self):
        result = self.invoke('run', 'theta', '--fail', '--help', '--stderr', 'path with spaces')
        self.assertEqual(result.returncode, 7)
        payload = json.loads(result.stdout)
        self.assertEqual(payload['args'], ['--fail', '--help', '--stderr', 'path with spaces'])
        self.assertEqual(payload['cwd'], str(self.root))
        self.assertEqual(result.stderr, 'fixture stderr\n')

    def test_round_script_can_import_root_modules_from_another_cwd(self):
        result = self.invoke('run', 'research/example-91-check.py')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, 'root import succeeded\n')

    def test_unknown_and_ambiguous_selectors_are_not_executed(self):
        marker = self.root / 'should-not-exist'
        (self.root / 'research' / 'unpublished-92.py').write_text(
            f'from pathlib import Path\nPath({str(marker)!r}).touch()\n')
        result = self.invoke('run', 'unpublished-92')
        self.assertEqual(result.returncode, 2)
        self.assertIn('Unknown published tool', result.stderr)
        self.assertFalse(marker.exists())
        result = self.invoke('run', 'duplicate-91')
        self.assertEqual(result.returncode, 2)
        self.assertIn('Ambiguous tool', result.stderr)
        self.assertNotIn('RuntimeError', result.stderr)

    def test_changed_guide_is_detected_and_show_does_not_execute_tool(self):
        guide = self.root / 'docs' / 'PYTHON.md'
        guide.write_text(guide.read_text() + 'changed\n')
        result = self.invoke('index', '--check')
        self.assertEqual(result.returncode, 1)
        self.assertIn('stale', result.stdout)
        # These tools deliberately raise at import time; inspection must stay passive.
        result = self.invoke('show', 'research/first/duplicate-91.py')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('research/first/duplicate-91.py', result.stdout)
        self.assertNotIn('RuntimeError', result.stderr)


if __name__ == '__main__':
    unittest.main()
