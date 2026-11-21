"""Test coordinator assessments without changing any real research files."""

from copy import deepcopy
from datetime import datetime
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'


class RoundReviewTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='paley-round-review-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / 'scripts').mkdir()
        (self.root / 'research').mkdir()
        for name in ['round_review.py', 'research_index.py', 'shared_obligations.py']:
            shutil.copy2(SCRIPTS / name, self.root / 'scripts' / name)
        self.note1 = self.root / 'research' / 'note-1.md'
        self.note2 = self.root / 'research' / 'note-2.md'
        self.note1.write_text('Earlier argument.\n')
        self.note2.write_text('Later argument with a remaining uniform estimate.\n')
        self.baseline = self.root / 'research' / 'round-1-acceptance.json'
        self.current = self.root / 'research' / 'round-2-acceptance.json'
        self.baseline.write_text(json.dumps({'round': 1, 'target_status': 'open',
            'proof_and_code_sha256': {'research/note-1.md': self.sha(self.note1)}}))
        self.current.write_text(json.dumps({'round': 2, 'target_status': 'open',
            'previous': 'research/round-1-acceptance.json', 'previous_sha256': self.sha(self.baseline),
            'proof_and_code_sha256': {'research/note-2.md': self.sha(self.note2)},
            'main_ranked_closeout': ['Test the unresolved uniform estimate.']}))
        self.research_before = {p.name: p.read_bytes() for p in (self.root / 'research').iterdir()}
        self.invoke('init', check=True)
        self.record = self.root / 'coordination' / 'round-2.json'

    @staticmethod
    def sha(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def ref(self, path):
        return {'path': path.relative_to(self.root).as_posix(), 'sha256': self.sha(path)}

    def invoke(self, *args, check=False):
        return subprocess.run([sys.executable, '-B', str(self.root / 'scripts' / 'round_review.py'), *args],
                              cwd=self.root.parent, capture_output=True, text=True, check=check)

    def ready(self):
        data = json.loads(self.record.read_text())
        data['record_status'] = 'ready'
        data['prepared_by'] = 'Fixture coordinator'
        data['changes'] = [{'id': 'uniform-bound', 'route': 'The chosen route', 'effect': 'unchanged',
            'before': 'A uniform bound is needed.', 'after': 'A uniform bound is needed.',
            'remaining': 'Bound the actual selected object uniformly in the order.',
            'evidence': [self.ref(self.note2)]}]
        data['decision_reason'] = 'The next test distinguishes a construction failure from a missing estimate.'
        data['next_calls'] = [{'id': 'next-test', 'priority': 1, 'change_id': 'uniform-bound',
            'question': 'Does the actual object satisfy this uniform bound?',
            'why_now': 'The new identity isolates one specific signed term.',
            'scope': 'Retain the original prime and depth hypotheses.',
            'if_yes': 'Apply the proved reduction and retain the remaining obligations.',
            'if_no': 'Set aside this sufficient bound within its exact scope.',
            'if_inconclusive': 'Return the precise unresolved signed estimate.',
            'inputs': [self.ref(self.note2)]}]
        self.write(data)
        return data

    def write(self, data):
        self.record.write_text(json.dumps(data, indent=2) + '\n')

    def test_init_is_a_draft_and_preserves_research(self):
        data = json.loads(self.record.read_text())
        self.assertEqual(data['record_status'], 'draft')
        self.assertEqual(data['changes'][0]['before'], '')
        self.assertEqual(self.research_before, {p.name: p.read_bytes() for p in (self.root / 'research').iterdir()})
        self.assertNotEqual(self.invoke('check').returncode, 0)
        self.assertNotEqual(self.invoke('mission', '--call', 'next-test').returncode, 0)

    def test_init_never_overwrites_an_existing_record(self):
        before = self.record.read_bytes()
        result = self.invoke('init')
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.record.read_bytes(), before)

    def test_unchanged_plan_is_valid_and_mission_has_exact_provenance(self):
        self.ready()
        self.assertEqual(self.invoke('check', '--current').returncode, 0)
        result = self.invoke('mission', '--call', 'next-test')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(self.sha(self.record), result.stdout)
        self.assertIn('The new identity isolates one specific signed term.', result.stdout)
        self.assertIn('If inconclusive:', result.stdout)
        self.assertIn('research/note-2.md', result.stdout)
        self.assertIn('does not launch an agent', result.stdout)

    def test_shared_candidate_uses_one_id_from_mission_to_closeout(self):
        data = self.ready()
        second = deepcopy(data['next_calls'][0])
        second.update(id='alternate-test', priority=2, question='Can a real formulation give this bound?')
        data['next_calls'].append(second)
        candidate = 'cand:actual-uniform-bound'
        data['shared_candidates'] = [{
            'id': candidate, 'statement': 'The shared bound through all eligible primes.',
            'calls': ['next-test', 'alternate-test'],
        }]
        self.write(data)
        for identifier in data['shared_candidates'][0]['calls']:
            mission = self.invoke('mission', '--call', identifier, check=True).stdout
            self.assertIn(candidate, mission)
        handoff = self.invoke('checkpoint', check=True).stdout
        self.assertIn(candidate, handoff.split('## What resists')[1].split('## Proposed next step')[0])

        def log(*args, check=True):
            return subprocess.run([sys.executable, '-B', str(self.root / 'scripts' / 'shared_obligations.py'), *args],
                                  cwd=self.root, capture_output=True, text=True, check=check)

        (self.root / 'coordination' / 'shared-obligations').mkdir()
        captured = json.loads(log('capture', '--batch', 'round-3', '--coordinator', 'coordination/round-2.json',
                                  '--call', 'next-test', '--call', 'alternate-test').stdout)
        snapshot = json.loads((self.root / captured['path']).read_text())
        self.assertEqual(snapshot['candidate_ids_by_call'], {'next-test': [candidate], 'alternate-test': [candidate]})
        launch = datetime.fromisoformat(snapshot['captured_at_utc']).timestamp() + 0.25
        dispatch = self.root / 'coordination' / 'round-3-inflight.json'
        dispatch.write_text(json.dumps({'coordinator': self.ref(self.record), 'shared_obligations_before': captured,
                                        'lanes': [{'call_id': call['id'], 'started_utc_epoch': launch}
                                                  for call in data['next_calls']]}))
        review = self.root / 'assessment.json'
        group = {'id': 'cand:alias', 'routes': list(snapshot['routes']), 'classification': 'recognized',
                 'math_evidence': 'Same statement in the same scope.', 'prior_evidence': 'Both calls cite the bound.',
                 'dispatch_effect': 'same', 'effect_reason': 'Different tests of the shared estimate.'}
        outcome = {'reviewed_by': 'Fixture', 'comparison': 'Compared both routes.', 'groups': [group]}
        review.write_text(json.dumps(outcome))
        args = ('closeout', '--batch', 'round-3', '--assessment', str(review))
        self.assertNotEqual(log(*args, check=False).returncode, 0)
        group['id'] = candidate
        review.write_text(json.dumps(outcome))
        closed = json.loads(log(*args).stdout)
        self.assertEqual(json.loads((self.root / closed['path']).read_text())['groups'][0]['id'], candidate)
        self.assertIn('Recognized: 1', log().stdout)

    def test_missing_rationale_and_outcome_decisions_block_export(self):
        original = self.ready()
        for field in ['why_now', 'scope', 'if_yes', 'if_no', 'if_inconclusive']:
            with self.subTest(field=field):
                data = deepcopy(original)
                data['next_calls'][0][field] = ' '
                self.write(data)
                result = self.invoke('mission', '--call', 'next-test')
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(field, result.stderr)
                self.assertNotIn('# Proposed research mission', result.stdout)

    def test_changed_evidence_blocks_check_and_export(self):
        self.ready()
        self.note2.write_text('The cited argument has changed.\n')
        for command in [('check',), ('mission', '--call', 'next-test')]:
            result = self.invoke(*command)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('source changed', result.stderr)

    def test_changed_current_or_baseline_acceptance_is_detected(self):
        self.ready()
        for path in [self.current, self.baseline]:
            with self.subTest(path=path.name):
                original = path.read_bytes()
                path.write_bytes(original + b'\n')
                result = self.invoke('check')
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('source changed', result.stderr)
                path.write_bytes(original)

    def test_unaccepted_file_cannot_be_used_as_accepted_evidence(self):
        data = self.ready()
        draft = self.root / 'research' / 'unaccepted.md'
        draft.write_text('A local draft.\n')
        data['changes'][0]['evidence'] = [self.ref(draft)]
        self.write(data)
        result = self.invoke('check')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('not bound by either acceptance', result.stderr)

    def test_unknown_change_link_and_duplicate_priorities_are_rejected(self):
        original = self.ready()
        data = deepcopy(original)
        data['next_calls'][0]['change_id'] = 'unknown'
        self.write(data)
        self.assertIn('unknown change_id', self.invoke('check').stderr)
        data = deepcopy(original)
        other = deepcopy(data['next_calls'][0])
        other['id'] = 'another-test'
        data['next_calls'].append(other)
        self.write(data)
        self.assertIn('must be unique', self.invoke('check').stderr)

    def test_new_acceptance_blocks_old_dispatch_but_keeps_history_readable(self):
        self.ready()
        later = self.root / 'research' / 'round-3-acceptance.json'
        later.write_text(json.dumps({'round': 3, 'target_status': 'open'}))
        self.assertEqual(self.invoke('check', '--round', '2').returncode, 0)
        self.assertEqual(self.invoke('show', '--round', '2').returncode, 0)
        result = self.invoke('mission', '--round', '2', '--call', 'next-test')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('newer acceptance', result.stderr)
        self.assertIn('init --round 3', self.invoke('status').stderr)

    def test_hold_records_a_decision_without_authorizing_a_call(self):
        data = self.ready()
        data['decision'] = 'hold'
        data['decision_reason'] = 'No next test is justified by the current evidence.'
        data['next_calls'] = []
        self.write(data)
        self.assertEqual(self.invoke('check').returncode, 0)
        self.assertNotEqual(self.invoke('mission', '--call', 'next-test').returncode, 0)

    def test_reference_cannot_escape_the_checkout(self):
        data = self.ready()
        data['next_calls'][0]['inputs'][0]['path'] = '../outside.md'
        self.write(data)
        result = self.invoke('check')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('repository-relative', result.stderr)


if __name__ == '__main__':
    unittest.main()
