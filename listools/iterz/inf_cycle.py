from itertools import count as _count


def inf_cycle(input_iter):
    r"""iterz.inf_cycle(input_iter)

    This will cycle an iterator indefinitely. Usage:

    >>> alist = [1, 2, 4, 8]
    >>> inf_cycle_iter = iterz.inf_cycle(alist)
    >>> for _ in range(9):
    ...     print(inf_cycle_iter.__next__())
    1
    2
    4
    8
    1
    2
    4
    8
    1

    In fact, it works with any iterable containing any datatypes:

    >>> atuple = (1, 'foo', 3.0)
    >>> inf_cycle_iter = iterz.inf_cycle(atuple)
    >>> for i in range(5):
    ...     print(inf_cycle_iter.__next__())
    1
    foo
    3.0
    1
    foo
    """
    try:
        iterator = iter(input_iter)
    except:
        raise TypeError('\'input_iter\' must be \'iter\'')
    if len(input_iter) < 1:
        return
    for i in _count():
        yield input_iter[i % len(input_iter)]
