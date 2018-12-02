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
