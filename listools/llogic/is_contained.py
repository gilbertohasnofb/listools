def is_contained(list_1: list, list_2: list) -> list:
    r"""llogic.is_contained(list_1, list_2)

    Returns True if all unique elements of list_1 are also present in list_2
    and returns False when that's not the case. Usage:

    >>> alist = [1, 2, 3, 4, 5]
    >>> blist = [2, 3, 4]
    >>> llogic.is_contained(blist, alist)
    True
    >>> llogic.is_contained(alist, blist)
    False

    >>> alist = [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7]
    >>> blist = [3, 3, 4, 5, 5, 6]
    >>> llogic.is_contained(blist, alist)
    True

    Lists are not flattened, so sublists are considered as a single element:

    >>> alist = [3, 4, [1, [5, 2]]]
    >>> blist = [1, 2]
    >>> llogic.is_contained(blist, alist)
    False

    The lists can contain any datatype:

    >>> alist = [1, 2.3, 'foo', (3, 7), 7+3j]
    >>> blist = ['foo', 7+3j, (3, 7)]
    >>> llogic.is_contained(blist, alist)
    True
    """
    if not isinstance(list_1, list):
        raise TypeError('\'list_1\' must be \'list\'')
    if not isinstance(list_2, list):
        raise TypeError('\'list_2\' must be \'list\'')
    for item in list_1:
        if item not in list_2:
            return False
    return True
