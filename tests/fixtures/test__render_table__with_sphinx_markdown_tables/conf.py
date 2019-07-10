# -*- coding: utf-8 -*-

master_doc = 'index'
extensions = ['sphinx_markdown_tables']
source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

source_suffix = ['.rst', '.md']
