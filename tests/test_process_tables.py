# -*- coding: utf-8 -*-
import sphinx_markdown_tables as m


markdown_strings = [
'''# Test

|aaa|bbb|aaa|ddd|
|---|---|---|---|
|1|2|3|4|
''',

'''| First Header  | Second Header |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |
''',
# The next one fails with orig regex, but passes with the new regex
'''# Test
|aaa|bbb|aaa|ddd|
|---|---|---|---|
|1|2|3|4|''',
    ]


def test_process_tables(markdown_string):
    source = [markdown_string]
    m.process_tables(None, None, source)
    assert '<table' in source[0]


def pytest_generate_tests(metafunc):
    if 'markdown_string' in metafunc.fixturenames:
        metafunc.parametrize("markdown_string", markdown_strings)
