def intersection(list_1: list, list_2: list) -> list:
    r"""llogic.intersection(list_1, list_2)

    Returns the intersection of two lists (omitting repetitions). The order
    of the elements of the output depends on the order they are found in the
    first list. Usage:

    >>> alist = [1, 2, 3, 4, 5]
    >>> blist = [7, 6, 5, 4, 3]
    >>> llogic.intersection(alist, blist)
    [3, 4, 5]

    >>> alist = [1, 2, 3, 3, 4, 4, 5, 5, 5]
    >>> blist = [3, 3, 4, 5, 5, 6]
    >>> llogic.intersection(alist, blist)
    [3, 4, 5]

    Note that llogic.intersection does not flatten the lists so nested lists
    are of type list:

    >>> alist = [3, 4, [1, [5, 2]]]
    >>> blist = [1, 2, 3, 4, 5]
    >>> llogic.intersection(alist, blist)
    [3, 4]

    The lists can contain any datatype:

    >>> alist = [1, 2.3, 'foo', (3, 7)]
    >>> blist = ['foo', 7+3j, (3, 7)]
    >>> llogic.intersection(alist, blist)
    ['foo', (3, 7)]

    If either list is empty then the result is an empty list:

    >>> alist = [1, 2, 3, 4, 5]
    >>> blist = []
    >>> llogic.intersection(alist, blist)
    []
    """
    if not isinstance(list_1, list):
        raise TypeError('\'list_1\' must be \'list\'')
    if not isinstance(list_2, list):
        raise TypeError('\'list_2\' must be \'list\'')
    output_list = []
    for item in list_1:
        if item in list_2 and item not in output_list:
            output_list.append(item)
    return output_list
