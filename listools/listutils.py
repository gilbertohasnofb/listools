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
* `listutils.list_gcd(input_list)`

All functions have a `__doc__` attribute with usage instructions.

This library is published under the MIT License.
"""

from functools import reduce
from math import gcd as _gcd


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
    alternatively True's and False's. Usage:

    >>> alist = [1, 2, 3]
    >>> mask = [True, False, True]
    >>> listutils.list_mask(alist, mask)
    [1, 3]

    >>> alist = [1, 2, 3, 4, 5]
    >>> mask = [1, 0, 0, 1, 0]
    >>> listutils.list_mask(alist, mask)
    [1, 4]

    If the mask is shorter than the list, it loops:

    >>> alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> mask = [1, 0]
    >>> listutils.list_mask(alist, mask)
    [1, 3, 5, 7, 9]

    The input list can contain any datatypes:

    >>> alist = [1, 2.2, True, 'foo', (1, 4), None, (3+2j), {'a': 1}]
    >>> mask = [True, False, True]
    >>> listutils.list_mask(alist, mask)
    [1, True, 'foo', None, (3+2j)]

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
