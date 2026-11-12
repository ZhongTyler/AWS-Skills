"""Regression coverage for standalone reading vs nested evidence dependencies."""
import base64
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from audit_html_dependencies import audit_html


class DependencyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.page = self.root / 'index.html'

    def write(self, markup):
        self.page.write_text(markup, encoding='utf-8')

    def test_runtime_and_optional_links_are_separate(self):
        self.write('<img src="data:image/png;base64,AA=="><svg><use href="#icon"/></svg>'
                   '<a href="missing.md">source</a><a href="https://example.org">web</a>')
        result = audit_html(self.page)
        self.assertTrue(result['summary']['static_runtime_embedded_or_internal'])
        self.assertEqual(result['summary']['ordinary_link_kinds'], {'local': 1, 'network': 1})

    def test_runtime_attributes_and_css(self):
        self.write('<link rel="stylesheet" href="style.css"><script src="https://example.org/a.js"></script>'
                   '<style>@import "extra.css";p{background:url("photo.png")}</style>'
                   '<source srcset="one.webp 1x, two.webp 2x"><video poster="poster.jpg"></video>')
        result = audit_html(self.page)
        self.assertFalse(result['summary']['static_runtime_embedded_or_internal'])
        self.assertEqual(len(result['runtime']), 7)
        self.assertEqual(result['summary']['runtime_kinds'], {'local': 6, 'network': 1})

    def test_data_srcset_and_encoded_css_are_not_external(self):
        self.write('<img srcset="data:image/png;base64,AA== 1x, data:image/png;base64,AQ== 2x">'
                   '<style>p{background:url(data:image/svg+xml,%3Csvg%3E)}</style>')
        result = audit_html(self.page)
        self.assertEqual(result['summary']['runtime_kinds'], {'embedded': 3})

    def test_attachment_origins_deduplicate_and_keep_missing_evidence(self):
        folder = self.root / 'original'
        folder.mkdir()
        other = folder / 'other.md'
        other.write_text('Other source', encoding='utf-8')
        image = folder / 'photo.png'
        image.write_bytes(b'photo')
        first = b'![a](photo.png) [repeat](photo.png#crop) [other](other.md) [missing](run.json)'
        self.write(''.join('<a download="' + name + '" href="data:text/markdown;base64,'
                           + base64.b64encode(raw).decode() + '">download</a>'
                           for name, raw in [('one.md', first), ('two.md', other.read_bytes())]))
        origins = [{'download': name, 'path': str(folder / source),
                    'sha256': hashlib.sha256(raw).hexdigest()}
                   for name, source, raw in [('one.md', 'first.md', first),
                                             ('two.md', 'other.md', other.read_bytes())]]
        result = audit_html(self.page, origins, [self.root])
        self.assertEqual(result['summary']['attachment_local_link_occurrences'], 4)
        self.assertEqual(result['summary']['attachment_unique_resolved_targets'], 3)
        self.assertEqual(result['summary']['attachment_target_statuses'], {'exists': 2, 'missing': 1})
        self.assertEqual(result['summary']['attachment_targets_embedded_as_markdown'], 1)
        self.assertEqual(result['attachment_targets'][0]['occurrences'], 2)
        self.assertTrue(result['summary']['static_runtime_embedded_or_internal'])
        origins[0]['sha256'] = 'wrong'
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            audit_html(self.page, origins, [self.root])

    def test_unknown_origin_and_fenced_code(self):
        body = b'[real](evidence.json)\n```python\n[not link](code.json)\n```\n'
        self.write('<a download="note.md" href="data:text/markdown;base64,'
                   + base64.b64encode(body).decode() + '">note</a>')
        result = audit_html(self.page)
        self.assertEqual(result['summary']['attachment_local_link_occurrences'], 1)
        self.assertEqual(result['attachments'][0]['local_references'][0]['status'], 'origin_unknown')

    def test_outside_root_and_dynamic_flags(self):
        self.write('<img src="../private.png"><script>fetch(endpoint); image.src=generated;</script>'
                   '<iframe srcdoc="hello"></iframe><base href="https://example.org/">')
        result = audit_html(self.page)
        self.assertEqual(len(result['summary']['manual_review_flags']), 4)
        self.write('<img src="../private.png">')
        result = audit_html(self.page)
        self.assertEqual(result['runtime'][0]['status'], 'outside_allowed_roots')

    def test_cli_runtime_failure_preserves_receipt(self):
        self.write('<img src="not-bundled.png">')
        output = self.root / 'audit.json'
        command = [sys.executable, str(Path(__file__).with_name('audit_html_dependencies.py')),
                   str(self.page), '--output', str(output), '--check-runtime']
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(output.read_text())['runtime'][0]['status'], 'missing')

    def test_directory_reference_is_not_missing(self):
        (self.root / 'archive').mkdir()
        self.write('<img src="archive">')
        result = audit_html(self.page)
        self.assertEqual(result['runtime'][0]['status'], 'exists_directory')

    def test_report_cli_records_dependency_summary(self):
        spec = {'schema': 1, 'reader': 'Test reader', 'title': 'Test report',
                'subtitle': 'Fixture', 'sources': {'source': {'url': 'https://example.org'}},
                'sections': [{'id': 'section', 'title': 'Section', 'subtitle': 'Fixture',
                              'reader_goals': ['Understand fixture'], 'references': ['source'],
                              'blocks': [{'type': 'p', 'text': 'Explanation'}]}]}
        source = self.root / 'spec.json'
        source.write_text(json.dumps(spec), encoding='utf-8')
        output = self.root / 'rendered'
        result = subprocess.run([sys.executable,
                                 str(Path(__file__).with_name('render_report.py')),
                                 str(source), '--out', str(output), '--format', 'html'],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        receipt = json.loads((output / 'build-receipt.json').read_text('utf-8'))
        self.assertTrue(receipt['html_dependencies']['static_runtime_embedded_or_internal'])


if __name__ == '__main__':
    unittest.main()
