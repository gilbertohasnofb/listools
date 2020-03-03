def difference(list_1: list, list_2: list) -> list:
    r"""llogic.difference(list_1, list_2)

    Returns the difference of two lists (omitting repetitions). The order
    of the elements of the output depends on their order in the lists. The
    order of the inputs lists does affect the result. Usage:

    >>> alist = [1, 2, 3, 4, 5]
    >>> blist = [7, 6, 5, 4, 3]
    >>> llogic.difference(alist, blist)
    [1, 2]
    >>> llogic.difference(blist, alist)
    [7, 6]

    >>> alist = [1, 2, 3, 3, 4, 4, 5, 5, 5]
    >>> blist = [3, 3, 4, 5, 5, 6]
    >>> llogic.difference(alist, blist)
    [1, 2]

    Note that llogic.difference does not flatten the lists so nested lists
    are of type list:

    >>> alist = [3, 4, 1, 5, 2]
    >>> blist = [1, 2, 3, 4, 5]
    >>> llogic.difference(alist, blist)
    []
    >>> alist = [3, 4, [1, [5, 2]]]
    >>> blist = [1, 2, 3, 4, 5]
    >>> llogic.difference(alist, blist)
    [[1, [5, 2]]]

    The lists can contain any datatype:

    >>> alist = [1, 2.3, 'foo', (3, 7)]
    >>> blist = ['foo', 7+3j, (3, 7)]
    >>> llogic.difference(alist, blist)
    [1, 2.3]
    """
    if not isinstance(list_1, list):
        raise TypeError('\'list_1\' must be \'list\'')
    if not isinstance(list_2, list):
        raise TypeError('\'list_2\' must be \'list\'')
    output_list = []
    for item in list_1:
        if item not in list_2 and item not in output_list:
            output_list.append(item)
    return output_list
