from numbers import Number
from .flatten import flatten


def flatten_max(input_list: list,
                *,
                key: 'function' = None,
                default=None
                ) -> Number:
    r"""flatools.flatten_max(input_list, *[, key, default])

    Finds the largest element of a flattened list containing any number of
    nested subslists. Usage:

    >>> alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    >>> flatools.flatten_max(alist)
    10

    >>> alist = [3, 4, [1, [5, 2]]]
    >>> flatools.flatten_max(alist)
    5

    The list can also be made out of floats:

    >>> alist = [[1.73, -3.14, 9.41], [5.56, -1.03]]
    >>> flatools.flatten_max(alist)
    9.41

    Or it can be made out of a mixture of integers and floats:

    >>> alist = [[3, 1.4], [5, 7.8], [-3.1, 6.6]]
    >>> flatools.flatten_max(alist)
    7.8

    There are two optional arguments that can be used. The first is a called
    'key' and takes a function that serves as a key for the sort comparison.

    >>> alist = [-1, -5, [3, [-2, 4]]]
    >>> print(flatten_max(alist))
    4
    >>> print(flatten_max(alist, key=abs))
    -5

    The second is 'default', which is the value that the function defaults to
    when the input is an empty list:

    >>> alist = [1, 2, 3]
    >>> blist = []
    >>> print(flatten_max(alist, default=-100))
    3
    >>> print(flatten_max(blist, default=-100))
    -100
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    # not very elegant, but max(input, key=None) raises "TypeError: 'NoneType'
    # object is not callable. Other functions such as sorted(input, key=None)
    # work exactly as expected when key=None.
    if key:
        return max(flatten(input_list), key=key, default=default)
    else:
        return max(flatten(input_list), default=default)
