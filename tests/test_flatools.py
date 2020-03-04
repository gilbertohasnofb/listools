import pytest
from listools import flatools
import random


def test_flatten():
    alist = [[1, 2], [3, 4], [5], [6, 7, 8], [9, 10]]
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert flatools.flatten(alist) == expected_result

    alist = [1, 2, [3, [[4], 5]]]
    assert flatools.flatten(alist) == [1, 2, 3, 4, 5]

    alist = [1, [2.2, True], ['foo', [(1, 4), None]], [3+2j, {'a': 1}]]
    expected_result = [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    assert flatools.flatten(alist) == expected_result

    assert flatools.flatten([]) == []


def test_pflatten():
    alist = [[1, 2], [3, 4], [5], [6, 7, 8], [9, 10]]
    assert flatools.pflatten(alist) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    alist = [1, 2, [3, [[4], 5]]]
    assert flatools.pflatten(alist) == [1, 2, 3, [[4], 5]]
    assert flatools.pflatten(alist, depth=2) == [1, 2, 3, [4], 5]
    assert flatools.pflatten(alist, depth=3) == [1, 2, 3, 4, 5]
    assert flatools.pflatten(alist, depth=4) == [1, 2, 3, 4, 5]

    alist = [1, [2.2, True], ['foo', [(1, 4), None]], [3+2j, {'a': 1}]]
    expected_result = [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    assert flatools.pflatten(alist, depth=3) == expected_result

    assert flatools.pflatten([]) == []


def test_flatten_join():
    alist = [[1, 2], [3, 4]]
    blist = [[5, 6], [7, 8]]
    assert flatools.flatten_join(alist, blist) == [1, 2, 3, 4, 5, 6, 7, 8]

    alist = [1, [2, [3]]]
    blist = [[[4], 5], 6]
    assert flatools.flatten_join(alist, blist) == [1, 2, 3, 4, 5, 6]

    alist = [[1, 2], [3, 4]]
    blist = [[5, 6], [7, 8]]
    clist = [[[9], 10], 11]
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert flatools.flatten_join(alist, blist, clist) == expected_result

    alist = [1, [2.2, True]]
    blist = ['foo', [(1, 4), None]]
    clist = [3+2j, {'a': 1}]
    expected_result = [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    assert flatools.flatten_join(alist, blist, clist) == expected_result

    alist = [[1, 2], [3, 4], [5], [6, 7, 8], [9, 10]]
    assert flatools.flatten_join(alist) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    assert flatools.flatten_join([], []) == []


def test_flatten_sum():
    alist = [[1, 2], [3, 4], [5, 6]]
    assert flatools.flatten_sum(alist) == 21

    alist = [1, [2, [3]]]
    assert flatools.flatten_sum(alist) == 6

    alist = [1.1, [2.2, [3.3]]]
    assert flatools.flatten_sum(alist) == 6.6

    alist = [1, [2.1, [3, [4.1]]]]
    assert flatools.flatten_sum(alist) == 10.2

    alist = [1, [2, [3]]]
    assert flatools.flatten_sum(alist, start=4) == 10

    alist = []
    assert flatools.flatten_sum(alist) == 0


def test_flatten_len():
    alist = [[1, 2], [3, 4], [5, 6]]
    assert flatools.flatten_len(alist) == 6

    alist = [1, [2.2, True], ['foo', [(1, 4), None]], [3+2j, {'a': 1}]]
    assert flatools.flatten_len(alist) == 8

    alist = []
    assert flatools.flatten_len(alist) == 0


def test_flatten_index():
    alist = [[1, 2], [3, 4], [5, 6]]
    assert flatools.flatten_index(3, alist) == 2

    alist = [1, [2.2, True], ['foo', [(1, 4), None]], [3+2j, {'a': 1}]]
    assert flatools.flatten_index(None, alist) == 5

    with pytest.raises(ValueError):
        alist = [[1, 2], [3, 4], [5, 6]]
        flatools.flatten_index(7, alist)


def test_flatten_zip_cycle():
    alist = [1, 2]
    blist = [4, [5, 6, 7], 8]
    flatten_zip_cycle_iter = flatools.flatten_zip_cycle(alist, blist)
    assert flatten_zip_cycle_iter.__next__() == (1, 4)
    assert flatten_zip_cycle_iter.__next__() == (2, 5)
    assert flatten_zip_cycle_iter.__next__() == (1, 6)
    assert flatten_zip_cycle_iter.__next__() == (2, 7)
    assert flatten_zip_cycle_iter.__next__() == (1, 8)
    with pytest.raises(StopIteration):
        flatten_zip_cycle_iter.__next__()

    a = [1, 2]
    b = [1, [2, 3]]
    c = [[[1], 2, 3], 4]
    d = [1, [2, [3, 4]], 5]
    flatten_zip_cycle_iter = flatools.flatten_zip_cycle(a, b, c, d)
    assert flatten_zip_cycle_iter.__next__() == (1, 1, 1, 1)
    assert flatten_zip_cycle_iter.__next__() == (2, 2, 2, 2)
    assert flatten_zip_cycle_iter.__next__() == (1, 3, 3, 3)
    assert flatten_zip_cycle_iter.__next__() == (2, 1, 4, 4)
    assert flatten_zip_cycle_iter.__next__() == (1, 2, 1, 5)
    with pytest.raises(StopIteration):
        flatten_zip_cycle_iter.__next__()

    alist = [1, 2.0, 'foo', True, None]
    blist = [False, 'bar', (1, 4)]
    flatten_zip_cycle_iter = flatools.flatten_zip_cycle(alist, blist)
    assert flatten_zip_cycle_iter.__next__() == (1, False)
    assert flatten_zip_cycle_iter.__next__() == (2.0, 'bar')
    assert flatten_zip_cycle_iter.__next__() == ('foo', (1, 4))
    assert flatten_zip_cycle_iter.__next__() == (True, False)
    assert flatten_zip_cycle_iter.__next__() == (None, 'bar')
    with pytest.raises(StopIteration):
        flatten_zip_cycle_iter.__next__()

    alist = [1, [2, [3]]]
    flatten_zip_cycle_iter = flatools.flatten_zip_cycle(alist)
    assert flatten_zip_cycle_iter.__next__() == (1,)
    assert flatten_zip_cycle_iter.__next__() == (2,)
    assert flatten_zip_cycle_iter.__next__() == (3,)
    with pytest.raises(StopIteration):
        flatten_zip_cycle_iter.__next__()


def test_flatten_sorted():
    alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert flatools.flatten_sorted(alist) == expected_result

    alist = [1, 5, [3, [2, 4]]]
    assert flatools.flatten_sorted(alist) == [1, 2, 3, 4, 5]

    alist = [[1.73, -3.14, 9.41], [5.56, -1.03]]
    assert flatools.flatten_sorted(alist) == [-3.14, -1.03, 1.73, 5.56, 9.41]

    alist = [[3, 1.4], [5, 7.8], [-3.1, 6.6]]
    assert flatools.flatten_sorted(alist) == [-3.1, 1.4, 3, 5, 6.6, 7.8]

    alist = [-1, -5, [3, [-2, 4]]]
    assert flatools.flatten_sorted(alist, key=abs) == [-1, -2, 3, 4, -5]

    alist = [1, 5, [3, [2, 4]]]
    assert flatools.flatten_sorted(alist, reverse=True) == [5, 4, 3, 2, 1]

    assert flatools.flatten_sorted([]) == []


def test_flatten_reverse():
    alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    expected_result = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert flatools.flatten_reverse(alist) == expected_result

    alist = [1, 5, [3, [2, 4]]]
    assert flatools.flatten_reverse(alist) == [5, 4, 3, 2, 1]

    alist = [[1.73, -3.14, 9.41], [5.56, -1.03]]
    expected_result = [9.41, 5.56, 1.73, -1.03, -3.14]
    assert flatools.flatten_reverse(alist) == expected_result

    alist = [[3, 1.4], [5, 7.8], [-3.1, 6.6]]
    expected_result = [7.8, 6.6, 5, 3, 1.4, -3.1]
    assert flatools.flatten_reverse(alist) == expected_result

    assert flatools.flatten_reverse([]) == []


def test_flatten_max():
    alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    assert flatools.flatten_max(alist) == 10

    alist = [3, 4, [1, [5, 2]]]
    assert flatools.flatten_max(alist) == 5

    alist = [[1.73, -3.14, 9.41], [5.56, -1.03]]
    assert flatools.flatten_max(alist) == 9.41

    alist = [[3, 1.4], [5, 7.8], [-3.1, 6.6]]
    assert flatools.flatten_max(alist) == 7.8

    alist = [-1, -5, [3, [-2, 4]]]
    assert flatools.flatten_max(alist) == 4
    assert flatools.flatten_max(alist, key=abs) == -5

    alist = [1, 2, 3]
    assert flatools.flatten_max(alist, default=-100) == 3

    alist = []
    assert flatools.flatten_max(alist, default=-100) == -100


def test_flatten_min():
    alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    assert flatools.flatten_min(alist) == 1

    alist = [3, 4, [1, [5, 2]]]
    assert flatools.flatten_min(alist) == 1

    alist = [[1.73, -3.14, 9.41], [5.56, -1.03]]
    assert flatools.flatten_min(alist) ==-3.14

    alist = [[3, 1.4], [5, 7.8], [-3.1, 6.6]]
    assert flatools.flatten_min(alist) == -3.1

    alist = [-1, -5, [3, [-2, 4]]]
    assert flatools.flatten_min(alist) == -5
    assert flatools.flatten_min(alist, key=abs) == -1

    alist = [1, 2, 3]
    assert flatools.flatten_min(alist, default=-100) == 1

    alist = []
    assert flatools.flatten_min(alist, default=-100) == -100


def test_flatten_single_type():
    alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    assert flatools.flatten_single_type(alist) == True

    alist = [3, 4, [1, [5, 2]]]
    assert flatools.flatten_single_type(alist) == True

    alist = [[1.73, -3.14, 9.41], [5.56, -1.03]]
    assert flatools.flatten_single_type(alist) == True

    alist = [[3, 1.4], [5, 7.8], [-3.1, 6.6]]
    assert flatools.flatten_single_type(alist) == False

    alist = ['foo', ['bar', ('foo', 'bar')]]
    assert flatools.flatten_single_type(alist) == False

    alist = []
    assert flatools.flatten_single_type(alist) == False


def test_flatten_mixed_type():
    alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    assert flatools.flatten_mixed_type(alist) == False

    alist = [3, 4, [1, [5, 2]]]
    assert flatools.flatten_mixed_type(alist) == False

    alist = [[1.73, -3.14, 9.41], [5.56, -1.03]]
    assert flatools.flatten_mixed_type(alist) == False

    alist = [[3, 1.4], [5, 7.8], [-3.1, 6.6]]
    assert flatools.flatten_mixed_type(alist) == True

    alist = ['foo', ['bar', ('foo', 'bar')]]
    assert flatools.flatten_mixed_type(alist) == True

    alist = []
    assert flatools.flatten_mixed_type(alist) == False


def test_flatten_choice():
    random.seed(87452)
    alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    assert flatools.flatten_choice(alist) == 9

    alist = [1, 5, [3, [2, 4]]]
    assert flatools.flatten_choice(alist) == 4

    alist = [1, [2.2, True], ['foo', [(1, 4), None]], [3+2j, {'a': 1}]]
    assert flatools.flatten_choice(alist) == (1, 4)
