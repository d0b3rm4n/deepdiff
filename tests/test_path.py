import pytest
from deepdiff.path import _path_to_elements, GET, GETATTR


@pytest.mark.parametrize('path, expected', [
    ("root[4]['b'][3]", [(4, GET), ('b', GET), (3, GET)]),
    ("root[4].b[3]", [(4, GET), ('b', GETATTR), (3, GET)]),
    ("root[4].b['a3']", [(4, GET), ('b', GETATTR), ('a3', GET)]),
    ("root[4.3].b['a3']", [(4.3, GET), ('b', GETATTR), ('a3', GET)]),
    ("root.a.b", [('a', GETATTR), ('b', GETATTR)]),
    ("root.hello", [('hello', GETATTR)]),
    (r"root['a\rb']", [('a\rb', GET)]),
])
def test_path_to_elements(path, expected):
    result = _path_to_elements(path)
    assert expected == result