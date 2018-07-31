from setuptools import setup
from codecs import open
from os import path

from sphinx_markdown_tables import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sphinx-markdown-tables',
    version=__version__.__version__,
    description='A Sphinx extension for rendering tables written in markdown',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ryanfox/sphinx-markdown-tables',
    author='Ryan Fox',
    author_email='ryan@foxrow.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='sphinx markdown tables',
    packages=['sphinx_markdown_tables'],
    install_requires=['markdown==2.6.11'],
    project_urls={
        'Bug Reports': 'https://github.com/ryanfox/sphinx-markdown-tables/issues',
        'Say Thanks!': 'https://foxrow.com',
        'Source': 'https://github.com/ryanfox/sphinx-markdown-tables/',
    },
)
