import inspect
import os
from unittest import TestCase, skip

import markdown
import sphinx_markdown_tables
import sphinx_testing


class AppMock(object):
    def connect(self, dest, destfunc):
        self.connect_dest = dest
        self.connect_destfunc = destfunc


class MarkdownTableTestCase(TestCase):

    @skip
    def test__setup(self):
        app = AppMock()
        result = sphinx_markdown_tables.setup(app)
        self.assertEqual(app.connect_dest, 'source-read')
        self.assertEqual(app.connect_destfunc, sphinx_markdown_tables.process_tables)
        self.assertIn('version', result.keys())

    @skip
    def test__process_tables__without_table(self):
        app = AppMock()
        source = ['# Test']
        sphinx_markdown_tables.process_tables(app, 'index', source)
        self.assertEqual('# Test', source[0])

    @skip
    def test__process_tables__with_table(self):
        app = AppMock()
        source = ['# Test\n\n| Header1 | Header2 |\n| ------- | ------- |\n| 1       | 2       |\n']
        sphinx_markdown_tables.process_tables(app, 'index', source)
        self.assertIn('<table', source[0])

    def test__render_table__without_sphinx_markdown_tables_enabled(self):
        """
        If the sphinx_markdown_tables extension isn't enabled, the content should not contain any tables
        """
        fixture_dir = f'{os.path.dirname(__file__)}/fixtures/{inspect.currentframe().f_code.co_name}'

        @sphinx_testing.with_app(srcdir=fixture_dir)
        def execute(app, status, warning):
            app.build()
            html = (app.outdir / 'index.html').read_text()
            self.assertNotIn('<table', html)

        execute()

    def test__render_table__with_sphinx_markdown_tables(self):
        """
        If the sphinx_markdown_tables extension is enabled, the content should contain tables
        """
        fixture_dir = f'{os.path.dirname(__file__)}/fixtures/{inspect.currentframe().f_code.co_name}'

        @sphinx_testing.with_app(srcdir=fixture_dir)
        def execute(app, status, warning):
            app.build()
            html = (app.outdir / 'index.html').read_text()
            self.assertIn('<table', html)

        execute()
