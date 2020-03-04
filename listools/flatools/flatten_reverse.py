from .flatten import flatten


def flatten_reverse(input_list: list) -> list:
    r"""flatools.flatten_reverse(input_list)

    Completely flattens a list containing any number of nested subslists into a
    reversed one dimensional list. Usage:

    >>> alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    >>> flatools.flatten_reverse(alist)
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    >>> alist = [1, 5, [3, [2, 4]]]
    >>> flatools.flatten_reverse(alist)
    [5, 4, 3, 2, 1]

    The list can also be made out of floats:

    >>> alist = [[1.73, -3.14, 9.41], [5.56, -1.03]]
    >>> flatools.flatten_reverse(alist)
    [9.41, 5.56, 1.73, -1.03, -3.14]

    Or it can be made out of a mixture of integers and floats:

    >>> alist = [[3, 1.4], [5, 7.8], [-3.1, 6.6]]
    >>> flatools.flatten_reverse(alist)
    [7.8, 6.6, 5, 3, 1.4, -3.1]
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    return sorted(flatten(input_list), reverse=True)
