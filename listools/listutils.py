# MIT License
#
# Copyright (c) 2018 Gilberto Agostinho
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""The module `listutils` contains functions that apply simple mathematical
operations to lists. The full list of available functions is:

* `listutils.list_lcm(input_list)`
* `listutils.list_mask(input_list, mask)`
* `listutils.list_mask_cycle(input_list, mask)`
* `listutils.list_gcd(input_list)`
* `listutils.period_len(input_list[, ignore_partial_cycles])`
* `listutils.scrambled(input_list)`

All functions have a `__doc__` attribute with usage instructions.

This library is published under the MIT License.
"""

from functools import reduce
from math import gcd as _gcd
import random


def _lcm(i, j):
    r"""Return the least common multiple of two numbers
    """
    if (i, j) == (0, 0):
        return 0
    return int(i * j / _gcd(i, j))


def list_lcm(input_list: list) -> int:
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
    if len(input_list) == 0:
        raise IndexError('\'input_list\' must have len > 0')
    return reduce(_lcm, input_list)


def list_gcd(input_list: list) -> int:
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
    if len(input_list) == 0:
        raise IndexError('\'input_list\' must have len > 0')
    return reduce(_gcd, input_list)


def list_mask(input_list: list, mask: list) -> list:
    r"""listutils.list_mask(input_list, mask)

    This function takes an input list and applies a mask to it, outputting a
    new list. The mask should be a list containing 1's and 0's, or
    alternatively True's and False's. If the mask is shorter than the input
    list then the input list will be considered only up to the mask length.
    Usage:

    >>> alist = [1, 2, 3]
    >>> mask = [True, False, True]
    >>> listutils.list_mask(alist, mask)
    [1, 3]

    >>> alist = [1, 2, 3, 4, 5]
    >>> mask = [1, 0, 0, 1, 0]
    >>> listutils.list_mask(alist, mask)
    [1, 4]

    If the mask is shorter than the list, the :

    >>> alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> mask = [1, 0]
    >>> listutils.list_mask(alist, mask)
    [1]

    If the mask is shorter than the input list then the input list will be
    considered only up to the mask length:

    >>> alist = [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    >>> mask = [True, False, True]
    >>> listutils.list_mask(alist, mask)
    [1, True]

    The input list can be empty, in which case an empty list is return. On the
    other hand, the mask argument cannot be an empty list.
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    if not isinstance(mask, list):
        raise TypeError('\'mask\' must be \'list\'')
    if len(mask) == 0:
        raise IndexError('\'mask\' must have len > 0')
    if len(input_list) == 0:
        return []

    output_list = []
    for item, mask_value in zip(input_list, mask):
        if mask_value:
            output_list.append(item)
    return output_list


def list_mask_cycle(input_list: list, mask: list) -> list:
    r"""listutils.list_mask_cycle(input_list, mask)

    This function takes an input list and applies a mask to it, outputting a
    new list. The mask should be a list containing 1's and 0's, or
    alternatively True's and False's. If the mask is shorter than the list,
    the mask is cycled. Usage:

    >>> alist = [1, 2, 3]
    >>> mask = [True, False, True]
    >>> listutils.list_mask_cycle(alist, mask)
    [1, 3]

    >>> alist = [1, 2, 3, 4, 5]
    >>> mask = [1, 0, 0, 1, 0]
    >>> listutils.list_mask_cycle(alist, mask)
    [1, 4]

    If the mask is shorter than the list, it loops:

    >>> alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> mask = [1, 0]
    >>> listutils.list_mask_cycle(alist, mask)
    [1, 3, 5, 7, 9]

    The input list can contain any datatypes:

    >>> alist = [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    >>> mask = [True, False, True]
    >>> listutils.list_mask_cycle(alist, mask)
    [1, True, 'foo', None, 3+2j]

    The input list can be empty, in which case an empty list is return. On the
    other hand, the mask argument cannot be an empty list.
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    if not isinstance(mask, list):
        raise TypeError('\'mask\' must be \'list\'')
    if len(mask) == 0:
        raise IndexError('\'mask\' must have len > 0')
    if len(input_list) == 0:
        return []

    from .iterz import zip_cycle  # avoiding a circular import

    output_list = []
    for item, mask_value in zip_cycle(input_list, mask):
        if mask_value:
            output_list.append(item)
    return output_list


def period_len(input_list: list, ignore_partial_cycles: bool = False) -> int:
    r"""listutils.period_len(input_list[, ignore_partial_cycles])

    This function returns the length of the period of an input list. Usage:

    >>> alist = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    >>> listutils.period_len(alist)
    3

    If a list is not periodic, the period length equals to the list size:

    >>> alist = [3, 1, 4, 1, 5, 9, 2, 6]
    >>> listutils.period_len(alist)
    8

    This function detects periodicity in lists with partial cycles:

    >>> alist = [1, 2, 3, 1, 2, 3, 1]
    >>> listutils.period_len(alist)
    3

    To disable this behaviour, use the ignore_partial_cycles argument:

    >>> alist = [1, 2, 3, 1, 2, 3, 1]
    >>> listutils.period_len(alist, ignore_partial_cycles=True)
    7

    If a list does not contain partial cycles, the ignore_partial_cycles
    argument does not affect the result:

    >>> alist = [1, 2, 3, 1, 2, 3]
    >>> listutils.period_len(alist, ignore_partial_cycles=True)
    3
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    if not isinstance(ignore_partial_cycles, bool):
        raise TypeError('\'ignore_partial_cycles\' must be \'bool\'')
    for period in range(1, len(input_list)):
        if all(input_list[n] == input_list[n + period] \
               for n in range(len(input_list) - period)):
            if ignore_partial_cycles:
                if len(input_list) % period != 0:
                    return len(input_list)
            return period
    return len(input_list)


def scrambled(input_list: list) -> list:
    r"""listutils.scrambled(input_list)

    This function returns a scrambled list with the same elements as the input
    list. Usage:

    >>> alist = [0, 1, 2, 3, 4]
    >>> listutils.scrambled(alist)
    [2, 1, 4, 0, 3]

    It differs from random.shuffle() since listutils.scrambled() outputs a new
    list, preserving the input one:

    >>> alist = [0, 1, 2, 3, 4]
    >>> listutils.scrambled(alist)
    [2, 1, 4, 0, 3]
    >>> alist
    [0, 1, 2, 3, 4]
    >>> import random
    >>> random.shuffle(alist)
    >>> alist
    [3, 2, 1, 4, 0]
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    scrambled_list = input_list[:]
    random.shuffle(scrambled_list)
    return scrambled_list
