from .flatten import flatten


def flatten_index(element, input_list: list) -> int:
    r"""flatools.flatten_index(input_list)

    Returns the index of the first instance of an element in a flatten list.
    Usage:

    >>> alist = [[1, 2], [3, 4], [5, 6]]
    >>> flatools.flatten_index(3, alist)
    2

    The datatypes of the elements of the list do not matter:

    >>> alist = [1, [2.2, True], ['foo', [(1, 4), None]], [3+2j, {'a': 1}]]
    >>> flatools.flatten_index(None, alist)
    5

    Just like the default behaviour of the flatten_index() method of a list,
    flatten_index raises a ValueError if an element is not found in a list:

    >>> alist = [[1, 2], [3, 4], [5, 6]]
    >>> flatools.flatten_index(7, alist)
    ValueError: 7 is not in list
    """
    if isinstance(element, list):
        raise TypeError('\'element\' must not be \'list\'')
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    return flatten(input_list).index(element)
