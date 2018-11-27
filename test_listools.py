import listools


def test_flatten():
    alist = [[1, 2], [3, 4], [5], [6, 7, 8], [9, 10]]
    assert listools.flatten(alist) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    alist = [1, 2, [3, [[4], 5]]]
    assert listools.flatten(alist) == [1, 2, 3, [[4], 5]]
    assert listools.flatten(alist, depth=2) == [1, 2, 3, [4], 5]
    assert listools.flatten(alist, depth=3) == [1, 2, 3, 4, 5]
    assert listools.flatten(alist, depth=4) == [1, 2, 3, 4, 5]
    alist = [1, [2.2, True], ['foo', [(1, 4), None]], [(3+2j), {'a': 1}]]
    expected_result = [1, 2.2, True, 'foo', (1, 4), None, (3+2j), {'a': 1}]
    assert listools.flatten(alist, depth=3) == expected_result


def test_completely_flatten():
    alist = [[1, 2], [3, 4], [5], [6, 7, 8], [9, 10]]
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert listools.completely_flatten(alist) == expected_result
    alist = [1, 2, [3, [[4], 5]]]
    assert listools.completely_flatten(alist) == [1, 2, 3, 4, 5]
    alist = [1, [2.2, True], ['foo', [(1, 4), None]], [(3+2j), {'a': 1}]]
    expected_result = [1, 2.2, True, 'foo', (1, 4), None, (3+2j), {'a': 1}]
    assert listools.completely_flatten(alist) == expected_result


def test_concat_flatten():
    alist = [[1, 2], [3, 4]]
    blist = [[5, 6], [7, 8]]
    assert listools.concat_flatten(alist, blist) == [1, 2, 3, 4, 5, 6, 7, 8]
    alist = [1, [2, [3]]]
    blist = [[[4], 5], 6]
    assert listools.concat_flatten(alist, blist) == [1, 2, 3, 4, 5, 6]
    alist = [[1, 2], [3, 4]]
    blist = [[5, 6], [7, 8]]
    clist = [[[9], 10], 11]
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert listools.concat_flatten(alist, blist, clist) == expected_result
    alist = [1, [2.2, True]]
    blist = ['foo', [(1, 4), None]]
    clist = [(3+2j), {'a': 1}]
    expected_result = [1, 2.2, True, 'foo', (1, 4), None, (3+2j), {'a': 1}]
    assert listools.concat_flatten(alist, blist, clist) == expected_result
    alist = [[1, 2], [3, 4], [5], [6, 7, 8], [9, 10]]
    assert listools.concat_flatten(alist) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_sum_flatten():
    alist = [[1, 2], [3, 4], [5, 6]]
    assert listools.sum_flatten(alist) == 21
    alist = [1, [2, [3]]]
    assert listools.sum_flatten(alist) == 6
    alist = [1.1, [2.2, [3.3]]]
    assert listools.sum_flatten(alist) == 6.6
    alist = [1, [2.1, [3, [4.1]]]]
    assert listools.sum_flatten(alist) == 10.2
