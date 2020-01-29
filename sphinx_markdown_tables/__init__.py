import re

from sphinx_markdown_tables import __version__


def setup(app):
    app.connect('source-read', process_tables)
    return {'version': __version__,
            'parallel_read_safe': True}


def process_tables(app, docname, source):
    """
    Convert markdown tables to html, since recommonmark can't. This requires 3 steps:
        Snip out table sections from the markdown
        Convert them to html
        Replace the old markdown table with an html table

    This function is called by sphinx for each document. `source` is a 1-item list. To update the document, replace
    element 0 in `source`.
    """
    import markdown
    md = markdown.Markdown(extensions=['markdown.extensions.tables'])
    table_processor = markdown.extensions.tables.TableProcessor(md.parser)

    raw_markdown = source[0]
    blocks = re.split(r'\n{2,}', raw_markdown)

    for i, block in enumerate(blocks):
        if table_processor.test(None, block):
            html = md.convert(
                replace_linked_filenames(block, app.config.source_suffix)
            )
            styled = html.replace('<table>', '<table border="1" class="docutils">', 1)  # apply styling
            blocks[i] = styled

    # re-assemble into markdown-with-tables-replaced
    # must replace element 0 for changes to persist
    source[0] = '\n\n'.join(blocks)
    

def replace_linked_filenames(block, source_suffix):
    """Replace linked filenames's extension inside the table block.
    Only the filenames which the extension figures in the source_suffix
    list are rendered so the extension is replaced by '.html'.
    """
    re_link_pattern = re.compile(
        "\[(?P<link_name>[^\]]*)\] *\( *(?P<link>.*)({}) *\)"
        "".format("|".join([ext.replace('.','\.') for ext in source_suffix]))
    )
    html_ref_block, n_sub = re_link_pattern.subn(
        "[\g<link_name>](\g<link>.html)", block)
    return html_ref_block
