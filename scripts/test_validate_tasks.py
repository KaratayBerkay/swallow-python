"""Curriculum contract checks without modifying learner files."""

import contextlib
import copy
import ast
import io
import json
from pathlib import Path
import re
import unittest
from unittest.mock import patch

from validate_tasks import ROOT, validate, markdown_links
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

    def validate_replaced_checkpoint(self, row, text):
        """Keep the inline copy in sync so content checks stand on their own."""
        original_read = Path.read_text
        rendered = {ROOT / row['task']: text}

        def read(path, *args, **kwargs):
            return rendered[path] if path in rendered else original_read(path, *args, **kwargs)

        def write(path, value):
            rendered[path] = value
            return len(value)

        with patch.object(Path, 'read_text', read), patch.object(Path, 'write_text', write):
            with contextlib.redirect_stdout(io.StringIO()):
                place(ROOT)
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

    def test_python_type_calls_are_not_markdown_links(self):
        self.assertEqual(markdown_links(
            '`list[int](["x"])`\n\n```python\nlist[int](["x"])\n```\n'
            '[Gerçek bağlantı](README.md)'), ['README.md'])

    def test_builtin_task_snippets_have_valid_markdown_and_base_syntax(self):
        for row in self.manifest['sections']:
            if not row['id'].startswith('b:') or row['status'] != 'task':
                continue
            text = (ROOT / row['task']).read_text()
            with self.subTest(section=row['id']):
                self.assertEqual(text.count('```') % 2, 0)
                if row['python'] == '3.11':
                    for block in re.findall(r'^```python\n(.*?)^```', text,
                                            re.MULTILINE | re.DOTALL):
                        ast.parse(block)

    def test_builtin_source_cannot_disappear_from_inventory(self):
        manifest = copy.deepcopy(self.manifest)
        manifest['sections'] = [r for r in manifest['sections']
                                if r['source'] != 'builtins/built-in-functions/abs/README.md']
        errors, _ = validate(ROOT, manifest)
        self.assertIn('README coverage differs from manifest; review new or removed sections.', errors)

    def test_alias_must_point_directly_to_a_teaching_task(self):
        manifest = copy.deepcopy(self.manifest)
        row = next(r for r in manifest['sections'] if r.get('covered_by'))
        row['covered_by'] = 'b:root'
        errors, _ = validate(ROOT, manifest)
        self.assertIn(f'{row["id"]}: canonical coverage must point directly to a task.', errors)

    def test_alias_cannot_lose_its_visible_task_link(self):
        row = next(r for r in self.manifest['sections'] if r.get('covered_by'))
        path = ROOT / row['source']
        text = path.read_text().replace('#bölüm-görevi)', ')')
        self.assertIn(f'{row["id"]}: alias must link to its canonical inline task.',
                      self.validate_file(path, text))

    def test_later_builtin_cannot_be_required_early(self):
        manifest = copy.deepcopy(self.manifest)
        tasks = [r for r in manifest['sections']
                 if r['id'].startswith('b:') and r['status'] == 'task']
        tasks[0]['prerequisites'].append(tasks[-1]['id'])
        errors, _ = validate(ROOT, manifest)
        self.assertIn(f'{tasks[0]["id"]}: prerequisite is not earlier: {tasks[-1]["id"]}.', errors)

    def test_new_api_cannot_hide_its_version_requirement(self):
        row = next(r for r in self.manifest['sections'] if r['source'] ==
                   'builtins/built-in-types/numeric-types-int-float-complex/int.is_integer/README.md')
        path = ROOT / row['task']
        self.assertIn(f'{row["id"]}: version restriction is not visible.',
                      self.validate_file(path, path.read_text().replace('3.12', '3.11')))

    def test_documented_builtin_changes_require_task_review(self):
        row = next(r for r in self.manifest['sections'] if r['source'] ==
                   'builtins/built-in-functions/abs/README.md')
        path = ROOT / row['source']
        self.assertIn(f'{row["id"]}: lesson changed; review task and update source snapshot.',
                      self.validate_file(path, path.read_text() + '\nYeni API sözleşmesi.\n'))

    def test_fixture_inventory_cannot_hide_new_learning_placeholders(self):
        manifest = copy.deepcopy(self.manifest)
        manifest['builtin_fixture_folders'] = []
        errors, _ = validate(ROOT, manifest)
        self.assertIn('Built-in placeholder inventory changed; review coverage.', errors)

    def test_milestone_without_an_assessment_is_rejected_even_when_inline_matches(self):
        row = next(r for r in self.manifest['milestones'] if r['section'] == 'b:root')
        errors = self.validate_replaced_checkpoint(
            row, '# Milestone: Ölçütsüz kontrol\n\nBu klasör tamamlandı.\n')
        self.assertIn(f'{row["id"]}: missing or repeated ## Geçiş ölçütleri.', errors)

    def test_milestone_with_empty_action_is_rejected(self):
        row = next(r for r in self.manifest['milestones'] if r['section'] == 'b:root')
        text = (ROOT / row['task']).read_text()
        text = re.sub(r'(## Tek görev\n).*?(?=## Geçiş ölçütleri)', r'\1\n',
                      text, flags=re.DOTALL)
        self.assertIn(f'{row["id"]}: empty ## Tek görev.',
                      self.validate_replaced_checkpoint(row, text))

    def test_milestone_without_concrete_criteria_is_rejected(self):
        row = next(r for r in self.manifest['milestones'] if r['section'] == 'b:root')
        text = (ROOT / row['task']).read_text()
        text = re.sub(r'^- \[[ xX]\] .+\n', '', text, flags=re.MULTILINE)
        self.assertIn(f'{row["id"]}: missing concrete criteria.',
                      self.validate_replaced_checkpoint(row, text))

    def test_milestone_needs_the_shared_evaluation_link(self):
        row = next(r for r in self.manifest['milestones'] if r['section'] == 'b:root')
        text = (ROOT / row['task']).read_text().replace('[Değerlendirme yöntemi](', '[Başka bağlantı](')
        self.assertIn(f'{row["id"]}: missing shared evaluation method link.',
                      self.validate_replaced_checkpoint(row, text))

    def test_reused_milestone_must_link_to_its_declared_evidence(self):
        row = next(r for r in self.manifest['milestones'] if r['section'] == 't:2.2')
        text = (ROOT / row['task']).read_text().replace(
            '(2.2.1-source-code-encoding/TASK.md)', '(../../../TASKS.md)')
        self.assertIn(f'{row["id"]}: missing link to reused checkpoint.',
                      self.validate_replaced_checkpoint(row, text))

    def test_original_lesson_links_are_validated(self):
        row = next(r for r in self.manifest['sections'] if r['source'] ==
                   'builtins/built-in-functions/abs/README.md')
        path = ROOT / row['source']
        self.assertIn(f'{row["id"]}: broken source link: absent-example.py.',
                      self.validate_file(path, path.read_text() +
                                         '\n[Örnek](absent-example.py)\n'))

    def test_method_summary_columns_preserve_type_families(self):
        path = ROOT / 'builtins/built-in-types/text-and-binary-sequence-type-methods-summary/README.md'
        table = [line for line in path.read_text().splitlines() if line.startswith('|')]
        self.assertGreater(len(table), 2)
        for line in table:
            cells = re.split(r'(?<!\\)\|', line.strip()[1:-1])
            with self.subTest(row=line):
                self.assertEqual(len(cells), 3)
                self.assertNotRegex(cells[1], r'\[(?:bytes|bytearray)\.')
                self.assertNotRegex(cells[2], r'\[str\.')


if __name__ == '__main__':
    unittest.main()
