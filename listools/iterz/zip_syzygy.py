from ..listutils import list_lcm as _list_lcm


def zip_syzygy(*input_iters) -> tuple:
    r"""iterz.zip_syzygy(*input_iters)

    Similar to zip but cycles lists until all of them are exhausted at the same
    time (that is, when the next output tuple would be the same as the very
    first yielded one). Usage:

    >>> alist = [1, 2]
    >>> blist = [4, 5, 6, 7, 8]
    >>> for i, j in iterz.zip_syzygy(alist, blist):
    ...     print(i, j)
    1 4
    2 5
    1 6
    2 7
    1 8
    2 4
    1 5
    2 6
    1 7
    2 8

    It also works with multiple lists:

    >>> alist = [1, 2]
    >>> blist = [1, 2, 3]
    >>> clist = [1, 2, 3, 4]
    >>> dlist = [4, 5, 6]
    >>> for i, j, k, l in iterz.zip_syzygy(alist, blist, clist, dlist):
    ...     print(i, j, k, l)
    1 1 1 4
    2 2 2 5
    1 3 3 6
    2 1 4 4
    1 2 1 5
    2 3 2 6
    1 1 3 4
    2 2 4 5
    1 3 1 6
    2 1 2 4
    1 2 3 5
    2 3 4 6

    In fact, it works with any iterable containing any datatypes:

    >>> a = (1, 2)
    >>> b = [1.0, 2.0, 3.0]
    >>> c = 'abc'
    >>> for i, j, k in iterz.zip_syzygy(a, b, c):
    ...     print(i, j, k)
    1 1.0 a
    2 2.0 b
    1 3.0 c
    2 1.0 a
    1 2.0 b
    2 3.0 c
    """
    for input_iter in input_iters:
        try:
            iterator = iter(input_iter)
        except:
            raise TypeError('\'*input_iters\' must be one or more \'iter\'')
    if any(len(input_iter) == 0 for input_iter in input_iters):
        raise IndexError('all elements of \'*input_iters\' must have len > 0')
    lcm = _list_lcm([len(input_iter) for input_iter in input_iters])
    for i in range(lcm):
        output_list = []
        for input_iter in input_iters:
            output_list.append(input_iter[i % len(input_iter)])
        yield tuple(output_list)
