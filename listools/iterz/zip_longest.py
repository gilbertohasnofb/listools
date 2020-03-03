def zip_longest(*input_iters, default=None) -> tuple:
    r"""iterz.zip_longest(*input_iters[, default])

    Similar to zip_cycle but yields values until the longest of the input
    iterators is exhausted. Shorter iterators yields None when exhausted.
    Usage:

    >>> alist = [1, 2]
    >>> blist = [4, 5, 6, 7, 8]
    >>> for i, j in iterz.zip_longest(alist, blist):
    ...     print(i, j)
    1 4
    2 5
    None 6
    None 7
    None 8

    It also works with multiple lists:

    >>> alist = [1, 2]
    >>> blist = [1, 2, 3]
    >>> clist = [1, 2, 3, 4]
    >>> dlist = [1, 2, 3, 4, 5]
    >>> for i, j, k, l in iterz.zip_longest(alist, blist, clist, dlist):
    ...     print(i, j, k, l)
    1 1 1 1
    2 2 2 2
    None 3 3 3
    None None 4 4
    None None None 5

    In fact, it works with any iterable containing any datatypes:

    >>> a = (1, 2, 3)
    >>> b = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    >>> c = 'abcde'
    >>> for i, j, k in iterz.zip_longest(a, b, c):
    ...     print(i, j, k)
    1 1.0 a
    2 2.0 b
    3 3.0 c
    None 4.0 d
    None 5.0 e
    None 6.0 None
    None 7.0 None

    The value None can be changed using the keyword argument default:

    >>> alist = [1, 2]
    >>> blist = [1, 2, 3, 4]
    >>> clist = [1, 2, 3, 4, 5, 6]
    >>> for i, j, k, l in iterz.zip_longest(alist, blist, clist, default=0):
    ...     print(i, j, k, l)
    1 1 1
    2 2 2
    0 3 3
    0 4 4
    0 0 5
    0 0 6
    """
    for input_iter in input_iters:
        try:
            iterator = iter(input_iter)
        except:
            raise TypeError('\'*input_iters\' must be one or more \'iter\'')
    if any(len(input_iter) == 0 for input_iter in input_iters):
        raise IndexError('all elements of \'*input_iters\' must have len > 0')
    max_length = max([len(input_iter) for input_iter in input_iters])
    for i in range(max_length):
        output_list = []
        for input_iter in input_iters:
            if i < len(input_iter):
                output_list.append(input_iter[i])
            else:
                output_list.append(default)
        yield tuple(output_list)
