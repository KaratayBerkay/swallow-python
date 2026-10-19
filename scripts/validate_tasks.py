"""Read-only checks for coverage, links and curriculum order."""

from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
LEARNING_BLOCK = re.compile(
    r'\n<!-- (validation-links|learning-task|learning-milestone):start -->\n'
    r'.*?<!-- \1:end -->\n?', re.DOTALL)
SECTION_MENU = re.compile(r'^#{2,6} Sections\s*$', re.MULTILINE)


def clean_source(text):
    return LEARNING_BLOCK.sub('', text).rstrip() + '\n'


def embedded_text(checkpoint, source):
    """Rebase the standalone task's headings for its lesson page."""
    heading = re.search(r'^(#{1,6}) ', source, re.MULTILINE)
    level = min(len(heading.group(1)) + 1, 5) if heading else 2
    title, rest = checkpoint.split('\n', 1)
    is_milestone = title.startswith('# Milestone:')
    label = 'Klasör milestone görevi' if is_milestone else 'Bölüm görevi'
    title = title.removeprefix('# ')
    rest = re.sub(r'^## ', '#' * (level + 1) + ' ', rest, flags=re.MULTILINE)
    return '#' * level + ' ' + label + '\n\n**' + title + '**\n' + rest.rstrip() + '\n'


def number(section_id):
    prefix, value = section_id.split(':')
    return (prefix, () if value == 'root' else tuple(map(int, value.split('.'))))


def body(text):
    return '\n'.join(
        line for line in clean_source(text).splitlines()
        if line.strip() and not line.startswith('#')
        and not re.match(r'^- \[.*\]\(.*README.md\)', line)
    ).strip()


def validate(root, manifest):
    errors = []

    def require(condition, message):
        if not condition:
            errors.append(message)

    sections = manifest['sections']
    rows = {row['id']: row for row in sections}
    require(len(rows) == len(sections), 'Duplicate section identifier.')
    actual_sources = {
        str(path.relative_to(root))
        for folder in ('tutorial', 'language-reference')
        for path in (root / folder).rglob('README.md')
    }
    require(actual_sources == {row['source'] for row in sections},
            'README coverage differs from manifest; review new or removed sections.')
    paths = {sid: Path(row['source']) for sid, row in rows.items()}
    tasks = {row['id']: row for row in sections if row['status'] == 'task'}
    milestones = {row['section']: row for row in manifest['milestones']}
    require(len(milestones) == len(manifest['milestones']), 'Duplicate milestone.')
    ordered = []

    def walk(sid):
        if sid in tasks:
            ordered.append(sid)
        children = [other for other in rows
                    if paths[other].parent.parent == paths[sid].parent]
        for child in sorted(children, key=number):
            walk(child)
        if sid in milestones:
            ordered.append('milestone:' + sid)

    walk('t:root')
    walk('r:root')
    position = {sid: index for index, sid in enumerate(ordered)}
    require(len(position) == len(ordered), 'Traversal repeats a checkpoint.')

    def check_next(event_id, inserted, source):
        following = position[event_id] + 1
        if following == len(ordered):
            require('Bu öğrenme rotasındaki son kontrol.' in inserted,
                    f'{event_id}: final checkpoint needs an explicit route end.')
            return
        next_id = ordered[following]
        next_section = next_id.removeprefix('milestone:')
        target = rows[next_section]['source']
        expected_link = Path(os.path.relpath(target, Path(source).parent)).as_posix()
        if next_id.startswith('milestone:'):
            expected_link += '#klasör-milestone-görevi'
        next_line = re.search(r'^\*\*Sonraki adım:\*\* (.+)$', inserted, re.MULTILINE)
        require(bool(next_line) and LINK.findall(next_line.group(1)) == [expected_link],
                f'{event_id}: next-step link skips or misorders a checkpoint.')
    artifacts = {'README.md', 'TASKS.md', 'DEGERLENDIRME.md', 'tutorial/README.md'}
    for sid, row in rows.items():
        source = root / row['source']
        if not source.is_file():
            errors.append(f'Missing source: {source}')
            continue
        text = source.read_text()
        if 'sha256' in row:
            digest = hashlib.sha256(clean_source(text).encode()).hexdigest()
            require(digest == row['sha256'],
                    f'{sid}: lesson changed; review task and update source snapshot.')
        require(row['status'] in {'task', 'navigation', 'empty'},
                f'{sid}: invalid status.')
        if row['status'] == 'empty':
            require(not body(text), f'{sid}: content exists but section is marked empty.')
        if row['status'] == 'task':
            artifacts.add(row['task'])
            require(row['task'] == str(paths[sid].with_name('TASK.md')),
                    f'{sid}: task must be next to its source.')
            require(bool(body(text)), f'{sid}: task assigned without lesson content.')
            require('[bölüm görevi](TASK.md)' in text,
                    f'{sid}: source is missing its task link.')
            target = root / row['task']
            if target.is_file():
                task_text = target.read_text()
                for heading in ('## Önce', '## Tek görev', '## Geçiş ölçütleri'):
                    require(task_text.count(heading) == 1,
                            f'{sid}: missing or repeated {heading}.')
                evaluation = Path(os.path.relpath('DEGERLENDIRME.md',
                                                 paths[sid].parent)).as_posix()
                require(f'[Değerlendirme yöntemi]({evaluation})' in task_text,
                        f'{sid}: missing shared evaluation method link.')
                require(bool(re.search(r'^- \[[ xX]\] ', task_text, re.MULTILINE)),
                        f'{sid}: missing concrete criteria.')
                if row['python'] != '3.11':
                    require(row['python'] in task_text,
                            f'{sid}: version restriction is not visible.')
                blocks = list(re.finditer(
                    r'\n<!-- learning-task:start -->\n(.*?)<!-- learning-task:end -->\n?',
                    text, re.DOTALL))
                require(len(blocks) == 1, f'{sid}: task must appear inline exactly once.')
                if len(blocks) == 1:
                    base = clean_source(text)
                    menu = SECTION_MENU.search(base)
                    insertion = menu.start() if menu else len(base)
                    prefix = LEARNING_BLOCK.sub('', text[:blocks[0].start()])
                    require(prefix == base[:insertion],
                            f'{sid}: inline task must follow the lesson before child sections.')
                    require(blocks[0].group(1).startswith(embedded_text(task_text, base)),
                            f'{sid}: inline task differs from its standalone source.')
                    check_next(sid, blocks[0].group(1), row['source'])
            for dependency in row['prerequisites']:
                require(dependency in tasks,
                        f'{sid}: prerequisite has no taught task: {dependency}.')
                require(position.get(dependency, float('inf')) < position.get(sid, -1),
                        f'{sid}: prerequisite is not earlier: {dependency}.')
                if dependency in paths and target.is_file():
                    require(dependency in target.read_text(),
                            f'{sid}: prerequisite missing from learner-facing task.')
        else:
            require(bool(row.get('reason')), f'{sid}: omission needs a reason.')
            require(not source.with_name('TASK.md').exists(),
                    f'{sid}: task exists for a non-teaching section.')

        children = [other for other in rows
                    if paths[other].parent.parent == paths[sid].parent]
        subtree = [other for other in rows
                   if paths[other].is_relative_to(paths[sid].parent)]
        has_content = any(other in tasks for other in subtree)
        is_complete = all(rows[other]['status'] != 'empty' for other in subtree)
        expected = bool(children) and has_content and is_complete
        require((sid in milestones) == expected,
                f'{sid}: milestone coverage differs from teachable folder coverage.')

    for sid, row in milestones.items():
        artifacts.add(row['task'])
        mid = 'milestone:' + sid
        require(row['id'] == mid, f'{sid}: milestone identifier mismatch.')
        expected = {tid for tid in tasks
                    if paths[tid].is_relative_to(paths[sid].parent)}
        expected |= {'milestone:' + child for child in milestones
                     if child != sid and paths[child].is_relative_to(paths[sid].parent)}
        require(set(row['after']) == expected,
                f'{sid}: milestone must wait for all tasks and nested milestones.')
        for dependency in row['after']:
            require(position.get(dependency, float('inf')) < position.get(mid, -1),
                    f'{sid}: milestone scheduled before {dependency}.')
        if row['reuse']:
            require(row['reuse'] in row['after'],
                    f'{sid}: reused checkpoint must be inside this completed folder.')
        source_text = (root / paths[sid]).read_text()
        blocks = list(re.finditer(
            r'\n<!-- learning-milestone:start -->\n(.*?)<!-- learning-milestone:end -->\n?',
            source_text, re.DOTALL))
        require(len(blocks) == 1, f'{sid}: milestone must appear inline exactly once.')
        if len(blocks) == 1:
            base = clean_source(source_text)
            prefix = LEARNING_BLOCK.sub('', source_text[:blocks[0].start()])
            require(prefix == base, f'{sid}: milestone must follow all child navigation.')
            checkpoint = root / row['task']
            if checkpoint.is_file():
                require(blocks[0].group(1).startswith(embedded_text(checkpoint.read_text(), base)),
                        f'{sid}: inline milestone differs from its standalone source.')
            check_next(row['id'], blocks[0].group(1), str(paths[sid]))
        if sid != 't:root':
            require('[klasör milestone görevi](MILESTONE.md)' in source_text,
                    f'{sid}: missing folder milestone link.')

    expected_tasks = {row['task'] for row in tasks.values()}
    expected_tasks |= {row['task'] for row in milestones.values()}
    actual_tasks = {str(p.relative_to(root))
                    for name in ('TASK.md', 'MILESTONE.md')
                    for base in ('tutorial', 'language-reference')
                    for p in (root / base).rglob(name)}
    require(actual_tasks == expected_tasks, 'Orphan or missing task/milestone files.')
    builtin_folders = {str(p.parent.relative_to(root))
                       for p in (root / 'builtins').rglob('.gitkeep')}
    require(builtin_folders == set(manifest['empty_builtin_folders']),
            'Built-in placeholder inventory changed; review coverage.')
    for folder in builtin_folders:
        require(not any((root / folder).glob('*.md')),
                f'{folder}: placeholder now contains documentation; review coverage.')

    index = (root / 'TASKS.md').read_text()
    index_order = [link for line in index.splitlines()
                   if re.match(r'^- \[[ xX]\] \[(?:Görev|Milestone) ', line)
                   for link in LINK.findall(line)]
    event_paths = {**{sid: row['source'] for sid, row in tasks.items()},
                   **{row['id']: rows[sid]['source'] + '#klasör-milestone-görevi'
                      for sid, row in milestones.items()}}
    require(index_order == [event_paths[sid] for sid in ordered],
            'TASKS.md must list checkpoints once in numeric preorder/postorder.')
    # Inline tasks keep the original lesson's external citations. Validate local
    # links and hygiene inside the inserted blocks, without rewriting citations.
    for row in sections:
        text = (root / row['source']).read_text()
        for match in LEARNING_BLOCK.finditer(text):
            inserted = match.group()
            require('\u2014' not in inserted, f'{row["id"]}: prohibited inline punctuation.')
            for link in LINK.findall(inserted):
                target = (root / row['source']).parent / link.split('#')[0]
                require(target.resolve().is_relative_to(root.resolve()) and target.exists(),
                        f'{row["id"]}: broken inline link: {link}.')
    for name in sorted(artifacts):
        path = root / name
        if not path.is_file():
            errors.append(f'Missing artifact: {name}')
            continue
        text = path.read_text()
        require('\u2014' not in text, f'{name}: prohibited punctuation.')
        require(not re.search(r'(?i)(generated by|co-authored-by|as an ai|written by openai)', text),
                f'{name}: prohibited attribution.')
        link_text = LEARNING_BLOCK.sub('', text) if name == 'tutorial/README.md' else text
        for link in LINK.findall(link_text):
            require(not re.match(r'[a-z]+://', link),
                    f'{name}: learner-facing task has an unexpected remote dependency.')
            target = (path.parent / link.split('#')[0]).resolve()
            require(target.is_relative_to(root.resolve()) and target.exists(),
                    f'{name}: broken or outside-repository link: {link}.')
    return errors, Counter(row['status'] for row in sections)


def main():
    manifest = json.loads((ROOT / 'tasks/manifest.json').read_text())
    errors, counts = validate(ROOT, manifest)
    if errors:
        for error in errors:
            print('FAIL:', error)
        return 1
    print(f'PASS: {sum(counts.values())} source sections; {counts["task"]} tasks; '
          f'{len(manifest["milestones"])} milestone points; '
          f'{counts["empty"]} empty sections; {counts["navigation"]} navigation sections.')
    print('PASS: source snapshots, inline placement/content, next-step links, prerequisites and folder coverage.')
    print('Learner solutions and conceptual understanding require separate review.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
