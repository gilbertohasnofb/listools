from .flatten import flatten


def flatten_zip_cycle(*input_lists) -> tuple:
    r"""flatools.flatten_zip_cycle(*input_lists)

    This function is nearly identical to iterz.zip_cycle except that it also
    flattens all lists before zipping and cycling them. Usage:

    >>> alist = [1, 2]
    >>> blist = [4, [5, 6, 7], 8]
    >>> for i, j in flatools.flatten_zip_cycle(alist, blist):
    ...     print(i, j)
    1 4
    2 5
    1 6
    2 7
    1 8

    It also works with multiple lists:

    >>> a = [1, 2]
    >>> b = [1, [2, 3]]
    >>> c = [[[1], 2, 3], 4]
    >>> d = [1, [2, [3, 4]], 5]
    >>> for i, j, k, l in flatools.flatten_zip_cycle(a, b, c, d):
    ...     print(i, j, k, l)
    1 1 1 1
    2 2 2 2
    1 3 3 3
    2 1 4 4
    1 2 1 5

    It also works with lists containing any datatypes:

    >>> alist = [1, 2.0, 'foo', True, None]
    >>> blist = [False, 'bar', (1, 4)]
    >>> for i, j in flatools.flatten_zip_cycle(alist, blist):
    ...     print(i, j)
    1 False
    2.0 bar
    foo (1, 4)
    True False
    None bar

    Note that unlike flatools.flatten_zip_cycle(), this function accepts only
    lists as input due to its flatenning function.
    """
    if not all(isinstance(input_list, list) for input_list in input_lists):
        raise TypeError('\'*input_lists\' must be one or more \'list\'')
    flatten_lists = []
    for input_list in input_lists:
        flatten_lists.append(flatten(input_list))
    max_length = max([len(flatten_list) for flatten_list in flatten_lists])
    for i in range(max_length):
        output_list = []
        for flatten_list in flatten_lists:
            output_list.append(flatten_list[i % len(flatten_list)])
        yield tuple(output_list)
