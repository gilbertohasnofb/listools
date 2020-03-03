from functools import reduce as _reduce
from math import gcd as _gcd
from typing import List


def _lcm(i: int, j: int) -> int:
    r"""Return the least common multiple of two numbers
    """
    if (i, j) == (0, 0):
        return 0
    return int(i * j / _gcd(i, j))


def list_lcm(input_list: List[int]) -> int:
    r"""listutils.list_lcm(input_list)

    This function returns the least common multiple of a list of integers.
    Usage:

    >>> alist = [1, 2, 3]
    >>> listutils.list_lcm(alist)
    6

    >>> alist = [7, 8, 4, 3]
    >>> listutils.list_lcm(alist)
    168
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    if not all(isinstance(element, int) for element in input_list):
        raise TypeError('all elements of \'input_list\' must be \'int\'')
    if len(input_list) == 0:
        raise IndexError('\'input_list\' must have len > 0')
    return _reduce(_lcm, input_list)
