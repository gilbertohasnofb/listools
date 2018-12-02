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
    with pytest.raises(StopIteration):
        zip_cycle_iter.__next__()

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
    with pytest.raises(StopIteration):
        zip_cycle_iter.__next__()

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
    with pytest.raises(StopIteration):
        zip_cycle_iter.__next__()

    alist = [1, 2, 3]
    zip_cycle_iter = iterz.zip_cycle(alist)
    assert zip_cycle_iter.__next__() == (1,)
    assert zip_cycle_iter.__next__() == (2,)
    assert zip_cycle_iter.__next__() == (3,)
    with pytest.raises(StopIteration):
        zip_cycle_iter.__next__()

    alist = []
    with pytest.raises(IndexError):
        iterz.zip_cycle(alist).__next__()


def test_zip_longest():
    alist = [1, 2]
    blist = [4, 5, 6, 7, 8]
    zip_longest_iter = iterz.zip_longest(alist, blist)
    assert zip_longest_iter.__next__() == (1, 4)
    assert zip_longest_iter.__next__() == (2, 5)
    assert zip_longest_iter.__next__() == (None, 6)
    assert zip_longest_iter.__next__() == (None, 7)
    assert zip_longest_iter.__next__() == (None, 8)

    alist = [1, 2]
    blist = [1, 2, 3]
    clist = [1, 2, 3, 4]
    dlist = [1, 2, 3, 4, 5]
    zip_longest_iter = iterz.zip_longest(alist, blist, clist, dlist)
    assert zip_longest_iter.__next__() == (1, 1, 1, 1)
    assert zip_longest_iter.__next__() == (2, 2, 2, 2)
    assert zip_longest_iter.__next__() == (None, 3, 3, 3)
    assert zip_longest_iter.__next__() == (None, None, 4, 4)
    assert zip_longest_iter.__next__() == (None, None, None, 5)

    a = (1, 2, 3)
    b = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    c = 'abcde'
    zip_longest_iter = iterz.zip_longest(a, b, c)
    assert zip_longest_iter.__next__() == (1, 1.0, 'a')
    assert zip_longest_iter.__next__() == (2, 2.0, 'b')
    assert zip_longest_iter.__next__() == (3, 3.0, 'c')
    assert zip_longest_iter.__next__() == (None, 4.0, 'd')
    assert zip_longest_iter.__next__() == (None, 5.0, 'e')
    assert zip_longest_iter.__next__() == (None, 6.0, None)
    assert zip_longest_iter.__next__() == (None, 7.0, None)

    alist = [1, 2, 3]
    zip_longest_iter = iterz.zip_longest(a)
    assert zip_longest_iter.__next__() == (1,)
    assert zip_longest_iter.__next__() == (2,)
    assert zip_longest_iter.__next__() == (3,)

    alist = []
    with pytest.raises(IndexError):
        iterz.zip_cycle(alist).__next__()


def test_zip_inf_cycle():
    alist = [1, 2]
    blist = [4, 5, 6, 7, 8]
    zip_inf_cycle_iter = iterz.zip_inf_cycle(alist, blist)
    assert zip_inf_cycle_iter.__next__() == (1, 4)
    assert zip_inf_cycle_iter.__next__() == (2, 5)
    assert zip_inf_cycle_iter.__next__() == (1, 6)
    assert zip_inf_cycle_iter.__next__() == (2, 7)
    assert zip_inf_cycle_iter.__next__() == (1, 8)
    assert zip_inf_cycle_iter.__next__() == (2, 4)
    assert zip_inf_cycle_iter.__next__() == (1, 5)
    assert zip_inf_cycle_iter.__next__() == (2, 6)
    assert zip_inf_cycle_iter.__next__() == (1, 7)

    alist = [1, 2]
    blist = [1, 2, 3]
    clist = [1, 2, 3, 4]
    dlist = [1, 2, 3, 4, 5]
    zip_inf_cycle_iter = iterz.zip_inf_cycle(alist, blist, clist, dlist)
    assert zip_inf_cycle_iter.__next__() == (1, 1, 1, 1)
    assert zip_inf_cycle_iter.__next__() == (2, 2, 2, 2)
    assert zip_inf_cycle_iter.__next__() == (1, 3, 3, 3)
    assert zip_inf_cycle_iter.__next__() == (2, 1, 4, 4)
    assert zip_inf_cycle_iter.__next__() == (1, 2, 1, 5)
    assert zip_inf_cycle_iter.__next__() == (2, 3, 2, 1)
    assert zip_inf_cycle_iter.__next__() == (1, 1, 3, 2)

    a = (1, 2, 3)
    b = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    c = 'abcde'
    zip_inf_cycle_iter = iterz.zip_inf_cycle(a, b, c)
    assert zip_inf_cycle_iter.__next__() == (1, 1.0, 'a')
    assert zip_inf_cycle_iter.__next__() == (2, 2.0, 'b')
    assert zip_inf_cycle_iter.__next__() == (3, 3.0, 'c')
    assert zip_inf_cycle_iter.__next__() == (1, 4.0, 'd')
    assert zip_inf_cycle_iter.__next__() == (2, 5.0, 'e')
    assert zip_inf_cycle_iter.__next__() == (3, 6.0, 'a')
    assert zip_inf_cycle_iter.__next__() == (1, 7.0, 'b')
    assert zip_inf_cycle_iter.__next__() == (2, 1.0, 'c')
    assert zip_inf_cycle_iter.__next__() == (3, 2.0, 'd')
    assert zip_inf_cycle_iter.__next__() == (1, 3.0, 'e')

    alist = [1, 2, 3]
    zip_inf_cycle_iter = iterz.zip_inf_cycle(a)
    assert zip_inf_cycle_iter.__next__() == (1,)
    assert zip_inf_cycle_iter.__next__() == (2,)
    assert zip_inf_cycle_iter.__next__() == (3,)

    alist = [1, 2]
    blist = [1, 2, 3, 4]
    clist = [1, 2, 3, 4, 5, 6]
    zip_inf_cycle_iter = iterz.zip_longest(alist, blist, clist, default=0)
    assert zip_inf_cycle_iter.__next__() == (1, 1, 1)
    assert zip_inf_cycle_iter.__next__() == (2, 2, 2)
    assert zip_inf_cycle_iter.__next__() == (0, 3, 3)
    assert zip_inf_cycle_iter.__next__() == (0, 4, 4)
    assert zip_inf_cycle_iter.__next__() == (0, 0, 5)
    assert zip_inf_cycle_iter.__next__() == (0, 0, 6)

    alist = []
    with pytest.raises(IndexError):
        iterz.zip_cycle(alist).__next__()


def test_zip_syzygy():
    alist = [1, 2]
    blist = [4, 5, 6, 7, 8]
    zip_syzygy_iter = iterz.zip_syzygy(alist, blist)
    assert zip_syzygy_iter.__next__() == (1, 4)
    assert zip_syzygy_iter.__next__() == (2, 5)
    assert zip_syzygy_iter.__next__() == (1, 6)
    assert zip_syzygy_iter.__next__() == (2, 7)
    assert zip_syzygy_iter.__next__() == (1, 8)
    assert zip_syzygy_iter.__next__() == (2, 4)
    assert zip_syzygy_iter.__next__() == (1, 5)
    assert zip_syzygy_iter.__next__() == (2, 6)
    assert zip_syzygy_iter.__next__() == (1, 7)
    assert zip_syzygy_iter.__next__() == (2, 8)
    with pytest.raises(StopIteration):
        zip_syzygy_iter.__next__()

    alist = [1, 2]
    blist = [1, 2, 3]
    clist = [1, 2, 3, 4]
    dlist = [4, 5, 6]
    zip_syzygy_iter = iterz.zip_syzygy(alist, blist, clist, dlist)
    assert zip_syzygy_iter.__next__() == (1, 1, 1, 4)
    assert zip_syzygy_iter.__next__() == (2, 2, 2, 5)
    assert zip_syzygy_iter.__next__() == (1, 3, 3, 6)
    assert zip_syzygy_iter.__next__() == (2, 1, 4, 4)
    assert zip_syzygy_iter.__next__() == (1, 2, 1, 5)
    assert zip_syzygy_iter.__next__() == (2, 3, 2, 6)
    assert zip_syzygy_iter.__next__() == (1, 1, 3, 4)
    assert zip_syzygy_iter.__next__() == (2, 2, 4, 5)
    assert zip_syzygy_iter.__next__() == (1, 3, 1, 6)
    assert zip_syzygy_iter.__next__() == (2, 1, 2, 4)
    assert zip_syzygy_iter.__next__() == (1, 2, 3, 5)
    assert zip_syzygy_iter.__next__() == (2, 3, 4, 6)
    with pytest.raises(StopIteration):
        zip_syzygy_iter.__next__()

    a = (1, 2)
    b = [1.0, 2.0, 3.0]
    c = 'abc'
    zip_syzygy_iter = iterz.zip_syzygy(a, b, c)
    assert zip_syzygy_iter.__next__() == (1, 1.0, 'a')
    assert zip_syzygy_iter.__next__() == (2, 2.0, 'b')
    assert zip_syzygy_iter.__next__() == (1, 3.0, 'c')
    assert zip_syzygy_iter.__next__() == (2, 1.0, 'a')
    assert zip_syzygy_iter.__next__() == (1, 2.0, 'b')
    assert zip_syzygy_iter.__next__() == (2, 3.0, 'c')
    with pytest.raises(StopIteration):
        zip_syzygy_iter.__next__()

    alist = [1, 2, 3]
    zip_syzygy_iter = iterz.zip_syzygy(alist)
    assert zip_syzygy_iter.__next__() == (1,)
    assert zip_syzygy_iter.__next__() == (2,)
    assert zip_syzygy_iter.__next__() == (3,)
    with pytest.raises(StopIteration):
        zip_syzygy_iter.__next__()

    alist = []
    with pytest.raises(IndexError):
        iterz.zip_cycle(alist).__next__()


def test_inf_cycle():
    alist = [1, 2, 4, 8]
    inf_cycle_iter = iterz.inf_cycle(alist)
    assert inf_cycle_iter.__next__() == 1
    assert inf_cycle_iter.__next__() == 2
    assert inf_cycle_iter.__next__() == 4
    assert inf_cycle_iter.__next__() == 8
    assert inf_cycle_iter.__next__() == 1
    assert inf_cycle_iter.__next__() == 2
    assert inf_cycle_iter.__next__() == 4
    assert inf_cycle_iter.__next__() == 8
    assert inf_cycle_iter.__next__() == 1

    atuple = (1, 'foo', 3.0)
    inf_cycle_iter = iterz.inf_cycle(atuple)
    assert inf_cycle_iter.__next__() == 1
    assert inf_cycle_iter.__next__() == 'foo'
    assert inf_cycle_iter.__next__() == 3.0
    assert inf_cycle_iter.__next__() == 1
    assert inf_cycle_iter.__next__() == 'foo'
    assert inf_cycle_iter.__next__() == 3.0
    assert inf_cycle_iter.__next__() == 1

    alist = []
    inf_cycle_iter = iterz.inf_cycle(alist)
    with pytest.raises(StopIteration):
        inf_cycle_iter.__next__()


def test_ncycle():
    alist = [1, 2, 4, 8]
    ncycle_iter = iterz.ncycle(alist, 2)
    assert ncycle_iter.__next__() == 1
    assert ncycle_iter.__next__() == 2
    assert ncycle_iter.__next__() == 4
    assert ncycle_iter.__next__() == 8
    assert ncycle_iter.__next__() == 1
    assert ncycle_iter.__next__() == 2
    assert ncycle_iter.__next__() == 4
    assert ncycle_iter.__next__() == 8
    with pytest.raises(StopIteration):
        ncycle_iter.__next__()

    atuple = (1, 'foo', 3.0)
    ncycle_iter = iterz.ncycle(atuple, 3)
    assert ncycle_iter.__next__() == 1
    assert ncycle_iter.__next__() == 'foo'
    assert ncycle_iter.__next__() == 3.0
    assert ncycle_iter.__next__() == 1
    assert ncycle_iter.__next__() == 'foo'
    assert ncycle_iter.__next__() == 3.0
    assert ncycle_iter.__next__() == 1
    assert ncycle_iter.__next__() == 'foo'
    assert ncycle_iter.__next__() == 3.0
    with pytest.raises(StopIteration):
        ncycle_iter.__next__()

    alist = []
    ncycle_iter = iterz.ncycle(alist, 1)
    with pytest.raises(StopIteration):
        ncycle_iter.__next__()


def test_cycle_until_index():
    alist = [1, 2, 4, 8, 16, 32]
    cycle_until_index_iter = iterz.cycle_until_index(alist, 4)
    assert cycle_until_index_iter.__next__() == 1
    assert cycle_until_index_iter.__next__() == 2
    assert cycle_until_index_iter.__next__() == 4
    assert cycle_until_index_iter.__next__() == 8
    assert cycle_until_index_iter.__next__() == 16
    with pytest.raises(StopIteration):
        cycle_until_index_iter.__next__()

    atuple = (1, 'foo', 3.0, 3+2j, [0.0])
    cycle_until_index_iter = iterz.cycle_until_index(atuple, 3)
    assert cycle_until_index_iter.__next__() == 1
    assert cycle_until_index_iter.__next__() == 'foo'
    assert cycle_until_index_iter.__next__() == 3.0
    assert cycle_until_index_iter.__next__() == 3+2j
    with pytest.raises(StopIteration):
        cycle_until_index_iter.__next__()

    alist = []
    cycle_until_index_iter = iterz.cycle_until_index(alist, 1)
    with pytest.raises(StopIteration):
        cycle_until_index_iter.__next__()


def test_iter_mask():
    alist = [1, 2, 3]
    mask = [True, False, True]
    iter_mask_iter = iterz.iter_mask(alist, mask)
    assert iter_mask_iter.__next__() == 1
    assert iter_mask_iter.__next__() == 3
    with pytest.raises(StopIteration):
        iter_mask_iter.__next__()

    alist = [1, 2, 3, 4, 5]
    mask = [1, 0, 0, 1, 0]
    iter_mask_iter = iterz.iter_mask(alist, mask)
    assert iter_mask_iter.__next__() == 1
    assert iter_mask_iter.__next__() == 4
    with pytest.raises(StopIteration):
        iter_mask_iter.__next__()

    alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mask = [1, 0]
    iter_mask_iter = iterz.iter_mask(alist, mask)
    assert iter_mask_iter.__next__() == 1
    assert iter_mask_iter.__next__() == 3
    assert iter_mask_iter.__next__() == 5
    assert iter_mask_iter.__next__() == 7
    assert iter_mask_iter.__next__() == 9
    with pytest.raises(StopIteration):
        iter_mask_iter.__next__()

    alist = [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    mask = [True, False, True]
    iter_mask_iter = iterz.iter_mask(alist, mask)
    assert iter_mask_iter.__next__() == 1
    assert iter_mask_iter.__next__() == True
    assert iter_mask_iter.__next__() == 'foo'
    assert iter_mask_iter.__next__() == None
    assert iter_mask_iter.__next__() == 3+2j
    with pytest.raises(StopIteration):
        iter_mask_iter.__next__()

    alist = []
    mask = [True, False, True]
    iter_mask_iter = iterz.iter_mask(alist, mask)
    with pytest.raises(StopIteration):
        iter_mask_iter.__next__()

    alist = [1, 2, 3]
    mask = []
    iter_mask_iter = iterz.iter_mask(alist, mask)
    with pytest.raises(IndexError):
        iter_mask_iter.__next__()
