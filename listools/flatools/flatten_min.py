from numbers import Number
from .flatten import flatten


def flatten_min(input_list: list,
                *,
                key: 'function' = None,
                default=None
                ) -> Number:
    r"""flatools.flatten_min(input_list, *[, key, default])

    Finds the smallest element of a  flattened list containing any number of
    nested subslists. Usage:

    >>> alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    >>> flatools.flatten_min(alist)
    1

    >>> alist = [3, 4, [1, [5, 2]]]
    >>> flatools.flatten_min(alist)
    1

    The list can also be made out of floats:

    >>> alist = [[1.73, -3.14, 9.41], [5.56, -1.03]]
    >>> flatools.flatten_min(alist)
    -3.14

    Or it can be made out of a mixture of integers and floats:

    >>> alist = [[3, 1.4], [5, 7.8], [-3.1, 6.6]]
    >>> flatools.flatten_min(alist)
    -3.1

    There are two optional arguments that can be used. The first is a called
    'key' and takes a function that serves as a key for the sort comparison.

    >>> alist = [-1, -5, [3, [-2, 4]]]
    >>> print(flatten_min(alist))
    -5
    >>> print(flatten_min(alist, key=abs))
    -1

    The second is 'default', which is the value that the function defaults to
    when the input is an empty list:

    >>> alist = [1, 2, 3]
    >>> blist = []
    >>> print(flatten_min(alist, default=-100))
    1
    >>> print(flatten_min(blist, default=-100))
    -100
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    # not very elegant, but min(input, key=None) raises "TypeError: 'NoneType'
    # object is not callable". Meanwhile, sorted(input, key=None) works exactly
    # as expected.
    if key:
        return min(flatten(input_list), key=key, default=default)
    else:
        return min(flatten(input_list), default=default)
