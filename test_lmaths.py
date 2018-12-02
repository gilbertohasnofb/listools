import pytest
from listools import lmaths


def test_list_lcm():
    alist = [1, 2, 3]
    assert lmaths.list_lcm(alist) == 6

    alist = [7, 8, 4, 3]
    assert lmaths.list_lcm(alist) == 168

    alist = [0, 0]
    assert lmaths.list_lcm(alist) == 0

    alist = [3]
    assert lmaths.list_lcm(alist) == 3

    with pytest.raises(TypeError):
        alist = []
        lmaths.list_lcm(alist)


def test_list_gcd():
    alist = [1, 2, 3]
    assert lmaths.list_gcd(alist) == 1

    alist = [8, 12]
    assert lmaths.list_gcd(alist) == 4

    alist = [74, 259, 185, 333]
    assert lmaths.list_gcd(alist) == 37

    alist = [0, 0]
    assert lmaths.list_gcd(alist) == 0

    alist = [3]
    assert lmaths.list_gcd(alist) == 3

    with pytest.raises(TypeError):
        alist = []
        lmaths.list_gcd(alist)
