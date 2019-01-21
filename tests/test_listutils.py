import pytest
from listools import listutils


def test_list_lcm():
    alist = [1, 2, 3]
    assert listutils.list_lcm(alist) == 6

    alist = [7, 8, 4, 3]
    assert listutils.list_lcm(alist) == 168

    alist = [0, 0]
    assert listutils.list_lcm(alist) == 0

    alist = [3]
    assert listutils.list_lcm(alist) == 3

    alist = []
    with pytest.raises(IndexError):
        listutils.list_lcm(alist)


def test_list_gcd():
    alist = [1, 2, 3]
    assert listutils.list_gcd(alist) == 1

    alist = [8, 12]
    assert listutils.list_gcd(alist) == 4

    alist = [74, 259, 185, 333]
    assert listutils.list_gcd(alist) == 37

    alist = [0, 0]
    assert listutils.list_gcd(alist) == 0

    alist = [3]
    assert listutils.list_gcd(alist) == 3

    alist = []
    with pytest.raises(IndexError):
        listutils.list_gcd(alist)


def test_list_mask():
    alist = [1, 2, 3]
    mask = [True, False, True]
    assert listutils.list_mask(alist, mask) == [1, 3]

    alist = [1, 2, 3, 4, 5]
    mask = [1, 0, 0, 1, 0]
    assert listutils.list_mask(alist, mask) == [1, 4]

    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mask = [1, 0]
    assert listutils.list_mask(alist, mask) == [1]

    alist = [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    mask = [True, False, True]
    assert listutils.list_mask(alist, mask) == [1, True]

    alist = []
    mask = [True, False, True]
    assert listutils.list_mask(alist, mask) == []

    alist = [1, 2, 3]
    mask = []
    with pytest.raises(IndexError):
        listutils.list_mask(alist, mask)


def test_list_mask_cycle():
    alist = [1, 2, 3]
    mask = [True, False, True]
    assert listutils.list_mask_cycle(alist, mask) == [1, 3]

    alist = [1, 2, 3, 4, 5]
    mask = [1, 0, 0, 1, 0]
    assert listutils.list_mask_cycle(alist, mask) == [1, 4]

    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mask = [1, 0]
    assert listutils.list_mask_cycle(alist, mask) == [1, 3, 5, 7, 9]

    alist = [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    mask = [True, False, True]
    expected_result = [1, True, 'foo', None, 3+2j]
    assert listutils.list_mask_cycle(alist, mask) == expected_result

    alist = []
    mask = [True, False, True]
    assert listutils.list_mask_cycle(alist, mask) == []

    alist = [1, 2, 3]
    mask = []
    with pytest.raises(IndexError):
        listutils.list_mask_cycle(alist, mask)


def test_is_ascending():
    alist = [0, 1, 2, 3]
    assert listutils.is_ascending(alist)

    alist = [10, 11, 12]
    assert listutils.is_ascending(alist)

    alist = [-2, -1, 0, 1, 2]
    assert listutils.is_ascending(alist)

    alist = [6, 5, 9, 2]
    assert not listutils.is_ascending(alist)

    alist = [1, 3, 5, 7]
    assert not listutils.is_ascending(alist)

    alist = [1, 3, 5, 7]
    step = 2
    assert listutils.is_ascending(alist, step)

    alist = [1, 3, 5, 7]
    step = -2
    with pytest.raises(ValueError):
        listutils.is_ascending(alist, step)


def test_is_descending():
    alist = [3, 2, 1, 0]
    assert listutils.is_descending(alist)

    alist = [12, 11, 10]
    assert listutils.is_descending(alist)

    alist = [2, 1, 0, -1, -2]
    assert listutils.is_descending(alist)

    alist = [6, 5, 9, 2]
    assert not listutils.is_descending(alist)

    alist = [7, 5, 3, 1]
    assert not listutils.is_descending(alist)

    alist = [7, 5, 3, 1]
    step = -2
    assert listutils.is_descending(alist, step)

    alist = [7, 5, 3, 1]
    step = 2
    with pytest.raises(ValueError):
        listutils.is_descending(alist, step)


def test_period_len():
    alist = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    assert listutils.period_len(alist) == 3

    alist = [3, 1, 4, 1, 5, 9, 2, 6]
    assert listutils.period_len(alist) == 8

    alist = [1, 2, 3, 1, 2, 3, 1]
    assert listutils.period_len(alist) == 3

    alist = [1, 2, 3, 1, 2, 3, 1]
    assert listutils.period_len(alist, ignore_partial_cycles=True) == 7

    alist = [1, 2, 3, 1, 2, 3]
    assert listutils.period_len(alist, ignore_partial_cycles=True) == 3

    alist = [1, 2, 3, 1, 2, 3, 1, 5]
    assert listutils.period_len(alist) == 8


def test_scrambled():
    alist = [0, 1, 2, 3, 4, 5]
    blist = listutils.scrambled(alist)
    assert blist

    alist = []
    blist = listutils.scrambled(alist)
    assert blist == []
