from .flatten import flatten


def flatten_single_type(input_list: list) -> bool:
    r"""flatools.flatten_single_type(input_list)

    Returns True if all elements of the flattened input_list are of the same
    type and False if they are not. Usage:

    >>> alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    >>> flatools.flatten_single_type(alist)
    True

    >>> alist = [3, 4, [1, [5, 2]]]
    >>> flatools.flatten_single_type(alist)
    True

    >>> alist = [[1.73, -3.14, 9.41], [5.56, -1.03]]
    >>> flatools.flatten_single_type(alist)
    True

    >>> alist = [[3, 1.4], [5, 7.8], [-3.1, 6.6]]
    >>> flatools.flatten_single_type(alist)
    False

    >>> alist = ['foo', ['bar', ('foo', 'bar')]]
    >>> flatools.flatten_single_type(alist)
    False

    Note that empty lists return False:

    >>> alist = []
    >>> flatools.flatten_single_type(alist)
    False
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    return len(set(map(type, flatten(input_list)))) == 1
