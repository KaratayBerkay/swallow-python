"""Curriculum contract checks without modifying learner files."""

import contextlib
import io
import json
from pathlib import Path
import re
import unittest
from unittest.mock import patch

from validate_tasks import ROOT, validate
from place_tasks import place


class CurriculumValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((ROOT / 'tasks/manifest.json').read_text())
        cls.index_path = ROOT / 'TASKS.md'
        cls.lines = cls.index_path.read_text().splitlines(keepends=True)
        cls.checkpoints = [i for i, line in enumerate(cls.lines)
                           if re.match(r'^- \[[ xX]\] \[(?:Görev|Milestone) ', line)]

    def validate_file(self, target, text):
        read_text = Path.read_text

        def read(path, *args, **kwargs):
            if path == target:
                return text
            return read_text(path, *args, **kwargs)

        with patch.object(Path, 'read_text', read):
            errors, _ = validate(ROOT, self.manifest)
        return errors

    def test_progress_states_preserve_checkpoint_order(self):
        for states in (' ', 'x', 'X', ' xX'):
            with self.subTest(states=states):
                lines = self.lines.copy()
                for n, i in enumerate(self.checkpoints):
                    lines[i] = re.sub(r'^- \[[ xX]\]',
                                      '- [' + states[n % len(states)] + ']', lines[i])
                self.assertEqual(self.validate_file(self.index_path, ''.join(lines)), [])

    def assert_order_error(self, lines):
        self.assertIn('TASKS.md must list checkpoints once in numeric preorder/postorder.',
                      self.validate_file(self.index_path, ''.join(lines)))

    def test_missing_checkpoint_is_rejected(self):
        lines = self.lines.copy()
        del lines[self.checkpoints[0]]
        self.assert_order_error(lines)

    def test_duplicate_completed_checkpoint_is_rejected(self):
        lines = self.lines.copy()
        first = self.checkpoints[0]
        lines.insert(first, re.sub(r'^- \[[ xX]\]', '- [x]', lines[first]))
        self.assert_order_error(lines)

    def test_reordered_completed_checkpoints_are_rejected(self):
        lines = self.lines.copy()
        first, second = self.checkpoints[:2]
        lines[first], lines[second] = lines[second], lines[first]
        for i in (first, second):
            lines[i] = re.sub(r'^- \[[ xX]\]', '- [X]', lines[i])
        self.assert_order_error(lines)

    def test_missing_shared_evaluation_link_is_rejected(self):
        row = next(r for r in self.manifest['sections'] if r['status'] == 'task')
        path = ROOT / row['task']
        text = path.read_text().replace('[Değerlendirme yöntemi](', '[Başka bağlantı](')
        self.assertIn(f'{row["id"]}: missing shared evaluation method link.',
                      self.validate_file(path, text))

    def test_missing_acceptance_criteria_heading_is_rejected(self):
        row = next(r for r in self.manifest['sections'] if r['status'] == 'task')
        path = ROOT / row['task']
        text = path.read_text().replace('## Geçiş ölçütleri', '## Sonuçlar')
        self.assertIn(f'{row["id"]}: missing or repeated ## Geçiş ölçütleri.',
                      self.validate_file(path, text))

    def test_placement_preserves_current_lessons_and_grouped_index(self):
        written = {}

        def capture(path, text):
            written[path] = text
            return len(text)

        with patch.object(Path, 'write_text', capture), contextlib.redirect_stdout(io.StringIO()):
            place(ROOT)
        self.assertIn(self.index_path, written)
        self.assertGreater(len(written), 1)
        for path, text in written.items():
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertEqual(path.read_text(), text)


if __name__ == '__main__':
    unittest.main()
