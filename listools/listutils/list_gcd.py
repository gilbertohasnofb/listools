from functools import reduce as _reduce
from math import gcd as _gcd
from typing import List


def list_gcd(input_list: List[int]) -> int:
    r"""listutils.list_gcd(input_list)

    This function returns the greatest common divisor of a list of integers.
    Usage:

    >>> alist = [8, 12]
    >>> listutils.list_gcd(alist)
    4

    >>> alist = [74, 259, 185, 333]
    >>> listutils.list_gcd(alist)
    37
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    if not all(isinstance(element, int) for element in input_list):
        raise TypeError('all elements of \'input_list\' must be \'int\'')
    if len(input_list) == 0:
        raise IndexError('\'input_list\' must have len > 0')
    return _reduce(_gcd, input_list)
