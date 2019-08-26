import inspect
import os
from unittest import TestCase, skip

import sphinx_testing


class MarkdownTableTestCase(TestCase):

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
