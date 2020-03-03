def single_type(input_list: list) -> bool:
    r"""llogic.single_type(input_list)

    Returns True if all elements of an input_list are of the same type and
    False if they are not. Usage:

    >>> alist = [3, 4, 1, 5, 2]
    >>> llogic.single_type(alist)
    True

    >>> alist = [3.1, 4, 1, 5, '2']
    >>> llogic.single_type(alist)
    False

    Note that llogic.single_type does not flatten the lists so nested lists are
    of type list:

    >>> alist = [3, 4, [1, [5, 2]]]
    >>> llogic.single_type(alist)
    False

    >>> alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    >>> llogic.single_type(alist)
    True

    Also note that empty lists return False:

    >>> alist = []
    >>> llogic.single_type(alist)
    False
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    return len(set(map(type, input_list))) == 1
