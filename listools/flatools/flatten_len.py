from .flatten import flatten


def flatten_len(input_list: list) -> int:
    r"""flatools.flatten_len(input_list)

    Returns the length of a flatten list (that is, it counts all elements in
    all of its subslists). Usage:

    >>> alist = [[1, 2], [3, 4], [5, 6]]
    >>> flatools.flatten_len(alist)
    6

    The datatypes of the elements of the list do not matter:

    >>> alist = [1, [2.2, True], ['foo', [(1, 4), None]], [3+2j, {'a': 1}]]
    >>> flatools.flatten_len(alist)
    8
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    return len(flatten(input_list))
