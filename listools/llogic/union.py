def union(list_1: list, list_2: list) -> list:
    r"""llogic.union(list_1, list_2)

    Returns the union of two lists (omitting repetitions). The order of the
    elements of the output depends on the order they are found in the first and
    then in the second lists. Usage:

    >>> alist = [1, 2, 3, 4, 5]
    >>> blist = [7, 6, 5, 4, 3]
    >>> llogic.union(alist, blist)
    [1, 2, 3, 4, 5, 7, 6]

    >>> alist = [1, 2, 3, 3, 4, 4, 5, 5, 5]
    >>> blist = [7, 6, 6, 5, 5, 5, 4]
    >>> llogic.union(alist, blist)
    [1, 2, 3, 4, 5, 7, 6]

    Note that llogic.union does not flatten the lists so nested lists
    are of type list:

    >>> alist = [3, 4, [1, [5, 2]]]
    >>> blist = [1, 2, 3, 4, 5]
    >>> llogic.union(alist, blist)
    [3, 4, [1, [5, 2]], 1, 2, 5]

    The lists can contain any datatype:

    >>> alist = [1, 2.3, 'foo', (3, 7)]
    >>> blist = ['foo', 7+3j, (3, 7)]
    >>> llogic.union(alist, blist)
    [1, 2.3, 'foo', (3, 7), 7+3j]
    """
    if not isinstance(list_1, list):
        raise TypeError('\'list_1\' must be \'list\'')
    if not isinstance(list_2, list):
        raise TypeError('\'list_2\' must be \'list\'')
    output_list = []
    for item in list_1 + list_2:
        if item not in output_list:
            output_list.append(item)
    return output_list
