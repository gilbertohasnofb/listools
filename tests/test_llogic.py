import pytest
from listools import llogic

def test_single_type():
    alist = [3, 4, 1, 5, 2]
    assert llogic.single_type(alist) == True

    alist = [3.1, 4, 1, 5, '2']
    assert llogic.single_type(alist) == False

    alist = [3, 4, [1, [5, 2]]]
    assert llogic.single_type(alist) == False

    alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    assert llogic.single_type(alist) == True

    alist = []
    assert llogic.single_type(alist) == False


def test_mixed_type():
    alist = [3, 4, 1, 5, 2]
    assert llogic.mixed_type(alist) == False

    alist = [3.1, 4, 1, 5, '2']
    assert llogic.mixed_type(alist) == True

    alist = [3, 4, [1, [5, 2]]]
    assert llogic.mixed_type(alist) == True

    alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    assert llogic.mixed_type(alist) == False

    alist = []
    assert llogic.mixed_type(alist) == False


def test_intersection():
    alist = [1, 2, 3, 4, 5]
    blist = [7, 6, 5, 4, 3]
    assert llogic.intersection(alist, blist) == [3, 4, 5]

    alist = [1, 2, 3, 3, 4, 4, 5, 5, 5]
    blist = [3, 3, 4, 5, 5, 6]
    assert llogic.intersection(alist, blist) == [3, 4, 5]

    alist = [3, 4, [1, [5, 2]]]
    blist = [1, 2, 3, 4, 5]
    assert llogic.intersection(alist, blist) == [3, 4]

    alist = [1, 2.3, 'foo', (3, 7)]
    blist = ['foo', 7+3j, (3, 7)]
    assert llogic.intersection(alist, blist) == ['foo', (3, 7)]

    alist = [1, 2, 3, 4, 5]
    blist = []
    assert llogic.intersection(alist, blist) == []


def test_union():
    alist = [1, 2, 3, 4, 5]
    blist = [7, 6, 5, 4, 3]
    assert llogic.union(alist, blist) == [1, 2, 3, 4, 5, 7, 6]

    alist = [1, 2, 3, 3, 4, 4, 5, 5, 5]
    blist = [7, 6, 6, 5, 5, 5, 4]
    assert llogic.union(alist, blist) == [1, 2, 3, 4, 5, 7, 6]

    alist = [3, 4, [1, [5, 2]]]
    blist = [1, 2, 3, 4, 5]
    assert llogic.union(alist, blist) == [3, 4, [1, [5, 2]], 1, 2, 5]

    alist = [1, 2.3, 'foo', (3, 7)]
    blist = ['foo', 7+3j, (3, 7)]
    assert llogic.union(alist, blist) == [1, 2.3, 'foo', (3, 7), 7+3j]

def test_difference():
    alist = [1, 2, 3, 4, 5]
    blist = [7, 6, 5, 4, 3]
    assert llogic.difference(alist, blist) == [1, 2]
    assert llogic.difference(blist, alist) == [7, 6]

    alist = [1, 2, 3, 3, 4, 4, 5, 5, 5]
    blist = [3, 3, 4, 5, 5, 6]
    assert llogic.difference(alist, blist) == [1, 2]

    alist = [3, 4, 1, 5, 2]
    blist = [1, 2, 3, 4, 5]
    assert llogic.difference(alist, blist) == []
    alist = [3, 4, [1, [5, 2]]]
    blist = [1, 2, 3, 4, 5]
    assert llogic.difference(alist, blist) == [[1, [5, 2]]]

    alist = [1, 2.3, 'foo', (3, 7)]
    blist = ['foo', 7+3j, (3, 7)]
    assert llogic.difference(alist, blist) == [1, 2.3]

def test_symmetric_difference():
    alist = [1, 2, 3, 4, 5]
    blist = [7, 6, 5, 4, 3]
    assert llogic.symmetric_difference(alist, blist) == [1, 2, 7, 6]
    assert llogic.symmetric_difference(blist, alist) == [7, 6, 1, 2]

    alist = [1, 2, 3, 3, 4, 4, 5, 5, 5]
    blist = [3, 3, 4, 5, 5, 6]
    assert llogic.symmetric_difference(alist, blist) == [1, 2, 6]

    alist = [3, 4, 1, 5, 2]
    blist = [1, 2, 3, 4, 5]
    assert llogic.symmetric_difference(alist, blist) == []
    alist = [3, 4, [1, [5, 2]]]
    blist = [1, 2, 3, 4, 5]
    assert llogic.symmetric_difference(alist, blist) == [[1, [5, 2]], 1, 2, 5]

    alist = [1, 2.3, 'foo', (3, 7)]
    blist = ['foo', 7+3j, (3, 7)]
    assert llogic.symmetric_difference(alist, blist) == [1, 2.3, 7+3j]


def test_is_contained():
    alist = [1, 2, 3, 4, 5]
    blist = [2, 3, 4]
    assert llogic.is_contained(blist, alist) == True
    assert llogic.is_contained(alist, blist) == False

    alist = [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7]
    blist = [3, 3, 4, 5, 5, 6]
    assert llogic.is_contained(blist, alist) == True

    alist = [3, 4, [1, [5, 2]]]
    blist = [1, 2]
    assert llogic.is_contained(blist, alist) == False

    alist = [1, 2.3, 'foo', (3, 7), 7+3j]
    blist = ['foo', 7+3j, (3, 7)]
    assert llogic.is_contained(blist, alist) == True
