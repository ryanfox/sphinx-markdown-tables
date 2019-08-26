"""sphinx markdown table extension module"""
import re

import markdown
import pkg_resources


# Get the version number from the package metadata
__version__: str = pkg_resources.get_distribution("sphinx-markdown-tables").version


def setup(app):
    """Sphinx extension setup for sphinx-markdown-table extention"""
    app.connect('source-read', process_tables)
    return {'version': __version__,
            'parallel_read_safe': True}


def process_tables(app, docname, source):
    """
    Convert markdown tables to html, since recommonmark can't.
    This requires 3 steps:
        Snip out table sections from the markdown
        Convert them to html
        Replace the old markdown table with an html table

    This function is called by sphinx for each document. `source` is a 1-item list.
    To update the document, replace element 0 in `source`.
    """
    md = markdown.Markdown(extensions=['markdown.extensions.tables'])
    table_processor = markdown.extensions.tables.TableProcessor(md.parser)

    raw_markdown = source[0]
    blocks = re.split(r'\n{2,}', raw_markdown)

    for i, block in enumerate(blocks):
        if table_processor.test(None, block):
            html = md.convert(block)

            # apply styling
            styled = html.replace('<table>', '<table border="1" class="docutils">', 1)
            blocks[i] = styled

    # re-assemble into markdown-with-tables-replaced
    # must replace element 0 for changes to persist
    source[0] = '\n\n'.join(blocks)
