from itertools import count as _count


def zip_inf_cycle(*input_iters) -> tuple:
    r"""iterz.zip_inf_cycle(*input_iters)

    Similar to zip but cycles all lists indefinitely. Usage:

    >>> alist = [1, 2]
    >>> blist = [4, 5, 6, 7, 8]
    >>> zip_inf_cycle_iter = iterz.zip_inf_cycle(alist, blist)
    >>> for _ in range(9):
    ...     print(zip_inf_cycle_iter.__next__())
    1 4
    2 5
    1 6
    2 7
    1 8
    2 4
    1 5
    2 6
    1 7

    It also works with multiple lists:

    >>> alist = [1, 2]
    >>> blist = [1, 2, 3]
    >>> clist = [1, 2, 3, 4]
    >>> dlist = [1, 2, 3, 4, 5]
    >>> zip_inf_cycle_iter = iterz.zip_inf_cycle(alist, blist, clist, dlist)
    >>> for i in range(7):
    ...     print(zip_inf_cycle_iter.__next__())
    1 1 1 1
    2 2 2 2
    1 3 3 3
    2 1 4 4
    1 2 1 5
    1 3 2 1
    2 1 3 2

    In fact, it works with any iterable containing any datatypes:

    >>> a = (1, 2, 3)
    >>> b = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    >>> c = 'abcde'
    >>> zip_inf_cycle_iter = iterz.zip_inf_cycle(a, b, c)
    >>> for i in range(10):
    ...     print(zip_inf_cycle_iter.__next__())
    1 1.0 a
    2 2.0 b
    3 3.0 c
    1 4.0 d
    2 5.0 e
    3 6.0 a
    1 7.0 b
    2 1.0 c
    3 2.0 d
    1 3.0 e
    """
    for input_iter in input_iters:
        try:
            iterator = iter(input_iter)
        except:
            raise TypeError('\'*input_iters\' must be one or more \'iter\'')
    if any(len(input_iter) == 0 for input_iter in input_iters):
        raise IndexError('all elements of \'*input_iters\' must have len > 0')
    for i in _count():
        output_list = []
        for input_iter in input_iters:
            output_list.append(input_iter[i % len(input_iter)])
        yield tuple(output_list)
