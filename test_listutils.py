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
    assert listutils.list_mask(alist, mask) == [1, 3, 5, 7, 9]

    alist = [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    mask = [True, False, True]
    assert listutils.list_mask(alist, mask) == [1, True, 'foo', None, 3+2j]

    alist = []
    mask = [True, False, True]
    assert listutils.list_mask(alist, mask) == []

    alist = [1, 2, 3]
    mask = []
    with pytest.raises(IndexError):
        listutils.list_mask(alist, mask)
