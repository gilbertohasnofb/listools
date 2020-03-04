from .flatten import flatten


def flatten_sorted(input_list: list,
                   *,
                   key: 'function' = None,
                   reverse: bool = False
                   ) -> list:
    r"""flatools.flatten_sorted(input_list, *[, key, reverse])

    Completely flattens a list containing any number of nested subslists into a
    sorted one dimensional list. Usage:

    >>> alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    >>> flatools.flatten_sorted(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> alist = [1, 5, [3, [2, 4]]]
    >>> flatools.flatten_sorted(alist)
    [1, 2, 3, 4, 5]

    The list can also be made out of floats:

    >>> alist = [[1.73, -3.14, 9.41], [5.56, -1.03]]
    >>> flatools.flatten_sorted(alist)
    [-3.14, -1.03, 1.73, 5.56, 9.41]

    Or it can be made out of a mixture of integers and floats:

    >>> alist = [[3, 1.4], [5, 7.8], [-3.1, 6.6]]
    >>> flatools.flatten_sorted(alist)
    [-3.1, 1.4, 3, 5, 6.6, 7.8]

    There are two optional arguments that can be used. The first is a called
    'key' and takes a function that serves as a key for the sort comparison.

    >>> alist = [-1, -5, [3, [-2, 4]]]
    >>> print(flatten_sorted(alist))
    [-5, -2, -1, 3, 4]
    >>> print(flatten_sorted(alist, key=abs))
    [-1, -2, 3, 4, -5]

    The second is 'reverse', which reverses the order of the output list:

    >>> alist = [1, 5, [3, [2, 4]]]
    >>> print(flatten_sorted(alist, reverse=True))
    [5, 4, 3, 2, 1]
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    return sorted(flatten(input_list), key=key, reverse=reverse)
