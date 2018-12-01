import pytest
from listools import iterz


def test_zip_cycle():
    alist = [1, 2]
    blist = [4, 5, 6, 7, 8]
    zip_cycle_iter = iterz.zip_cycle(alist, blist)
    assert zip_cycle_iter.__next__() == (1, 4)
    assert zip_cycle_iter.__next__() == (2, 5)
    assert zip_cycle_iter.__next__() == (1, 6)
    assert zip_cycle_iter.__next__() == (2, 7)
    assert zip_cycle_iter.__next__() == (1, 8)

    alist = [1, 2]
    blist = [1, 2, 3]
    clist = [1, 2, 3, 4]
    dlist = [1, 2, 3, 4, 5]
    zip_cycle_iter = iterz.zip_cycle(alist, blist, clist, dlist)
    assert zip_cycle_iter.__next__() == (1, 1, 1, 1)
    assert zip_cycle_iter.__next__() == (2, 2, 2, 2)
    assert zip_cycle_iter.__next__() == (1, 3, 3, 3)
    assert zip_cycle_iter.__next__() == (2, 1, 4, 4)
    assert zip_cycle_iter.__next__() == (1, 2, 1, 5)

    a = (1, 2, 3)
    b = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    c = 'abcde'
    zip_cycle_iter = iterz.zip_cycle(a, b, c)
    assert zip_cycle_iter.__next__() == (1, 1.0, 'a')
    assert zip_cycle_iter.__next__() == (2, 2.0, 'b')
    assert zip_cycle_iter.__next__() == (3, 3.0, 'c')
    assert zip_cycle_iter.__next__() == (1, 4.0, 'd')
    assert zip_cycle_iter.__next__() == (2, 5.0, 'e')
    assert zip_cycle_iter.__next__() == (3, 6.0, 'a')
    assert zip_cycle_iter.__next__() == (1, 7.0, 'b')

    alist = [1, 2, 3]
    zip_cycle_iter = iterz.zip_cycle(a)
    assert zip_cycle_iter.__next__() == (1,)
    assert zip_cycle_iter.__next__() == (2,)
    assert zip_cycle_iter.__next__() == (3,)
