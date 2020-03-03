def pflatten(input_list: list, depth: int = 1) -> list:
    r"""flatools.pflatten(input_list[, depth])

    Partially flattens a list containing subslists as elements. Usage:

    >>> alist = [[1, 2], [3, 4], [5], [6, 7, 8], [9, 10]]
    >>> flatools.pflatten(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> alist = [1, 2, [3, [[4], 5]]]
    >>> flatools.pflatten(alist)
    [1, 2, 3, [[4], 5]]

    Use the depth argument (which should always be an integer) when wanting to
    flatten nested sublists:

    >>> alist = [1, 2, [3, [4, 5]]]
    >>> flatools.pflatten(alist, depth=2)
    [1, 2, 3, [4], 5]

    >>> alist = [1, 2, [3, [4, 5]]]
    >>> flatools.pflatten(alist, depth=3)
    [1, 2, 3, 4, 5]

    >>> alist = [1, 2, [3, [4, 5]]]
    >>> flatools.pflatten(alist, depth=4)
    [1, 2, 3, 4, 5]

    Notice that the list themselves can be made out of any datatypes:

    >>> alist = [1, [2.2, True], ['foo', [(1, 4), None]], [3+2j, {'a': 1}]]
    >>> flatools.flatten(alist, depth=3)
    [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    if not isinstance(depth, int):
        raise TypeError('\'depth\' must be \'int\'')
    aux_list = input_list[:]
    for _ in range(depth):
        output_list = []
        for element in aux_list:
            if not isinstance(element, list):
                output_list.append(element)
            else:
                output_list += element
        aux_list = output_list[:]
    return output_list
