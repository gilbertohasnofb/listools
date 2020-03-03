def zip_cycle(*input_iters) -> tuple:
    r"""iterz.zip_cycle(*input_iters)

    Similar to zip but cycles smaller lists or iterables until the longest one
    is output. Usage:

    >>> alist = [1, 2]
    >>> blist = [4, 5, 6, 7, 8]
    >>> for i, j in iterz.zip_cycle(alist, blist):
    ...     print(i, j)
    1 4
    2 5
    1 6
    2 7
    1 8

    It also works with multiple lists:

    >>> alist = [1, 2]
    >>> blist = [1, 2, 3]
    >>> clist = [1, 2, 3, 4]
    >>> dlist = [1, 2, 3, 4, 5]
    >>> for i, j, k, l in iterz.zip_cycle(alist, blist, clist, dlist):
    ...     print(i, j, k, l)
    1 1 1 1
    2 2 2 2
    1 3 3 3
    2 1 4 4
    1 2 1 5

    In fact, it works with any iterable containing any datatypes:

    >>> a = (1, 2, 3)
    >>> b = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    >>> c = 'abcde'
    >>> for i, j, k in iterz.zip_cycle(a, b, c):
    ...     print(i, j, k)
    1 1.0 a
    2 2.0 b
    3 3.0 c
    1 4.0 d
    2 5.0 e
    3 6.0 a
    1 7.0 b
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
            output_list.append(input_iter[i % len(input_iter)])
        yield tuple(output_list)
