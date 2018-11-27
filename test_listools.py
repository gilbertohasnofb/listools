import listools


def test_flatten():
    alist = [[1, 2], [3, 4], [5], [6, 7, 8], [9, 10]]
    assert listools.flatten(alist) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    alist = [1, 2, [3, [[4], 5]]]
    assert listools.flatten(alist) == [1, 2, 3, [[4], 5]]
    assert listools.flatten(alist, depth=2) == [1, 2, 3, [4], 5]
    assert listools.flatten(alist, depth=3) == [1, 2, 3, 4, 5]
    alist = [1, [2.2, True], ['foo', [(1, 4), None]], [(3+2j), {'a': 1}]]
    assert listools.flatten(alist, depth=3) == [1, 2.2, True, 'foo', (1, 4), None, (3+2j), {'a': 1}]


def test_completely_flatten():
    alist = [[1, 2], [3, 4], [5], [6, 7, 8], [9, 10]]
    assert listools.completely_flatten(alist) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    alist = [1, 2, [3, [[4], 5]]]
    assert listools.completely_flatten(alist) == [1, 2, 3, 4, 5]
    alist = [1, [2.2, True], ['foo', [(1, 4), None]], [(3+2j), {'a': 1}]]
    assert listools.completely_flatten(alist) == [1, 2.2, True, 'foo', (1, 4), None, (3+2j), {'a': 1}]
