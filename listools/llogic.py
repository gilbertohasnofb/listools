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

"""The module `llogic` contains functions that deal with logic operations on
lists. The full list of available functions is:

* `llogic.difference(list_1, list_2)`
* `llogic.intersection(list_1, list_2)`
* `llogic.is_contained(list_1, list_2)`
* `llogic.mixed_type(input_list)`
* `llogic.single_type(input_list)`
* `llogic.symmetric_difference(list_1, list_2)`
* `llogic.union(list_1, list_2)`

All functions have a `__doc__` attribute with usage instructions.

This library is published under the MIT License.
"""

def single_type(input_list: list) -> bool:
    r"""llogic.single_type(input_list)

    Returns True if all elements of an input_list are of the same type and
    False if they are not. Usage:

    >>> alist = [3, 4, 1, 5, 2]
    >>> llogic.single_type(alist)
    True

    >>> alist = [3.1, 4, 1, 5, '2']
    >>> llogic.single_type(alist)
    False

    Note that llogic.single_type does not flatten the lists so nested lists are
    of type list:

    >>> alist = [3, 4, [1, [5, 2]]]
    >>> llogic.single_type(alist)
    False

    >>> alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    >>> llogic.single_type(alist)
    True

    Also note that empty lists return False:

    >>> alist = []
    >>> llogic.single_type(alist)
    False
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    return len(set(map(type, input_list))) == 1


def mixed_type(input_list: list) -> bool:
    r"""llogic.mixed_type(input_list)

    Returns False if all elements of an input_list are of the same type and
    True if they are not. Usage:

    >>> alist = [3, 4, 1, 5, 2]
    >>> llogic.single_type(alist)
    False

    >>> alist = [3.1, 4, 1, 5, '2']
    >>> llogic.single_type(alist)
    True

    Note that llogic.mixed_type does not flatten the lists so nested lists are
    of type list:

    >>> alist = [3, 4, [1, [5, 2]]]
    >>> llogic.single_type(alist)
    True

    >>> alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    >>> llogic.single_type(alist)
    False

    Also note that empty lists return False:

    >>> alist = []
    >>> llogic.single_type(alist)
    False
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    return len(set(map(type, input_list))) > 1


def intersection(list_1: list, list_2: list) -> list:
    r"""llogic.intersection(list_1, list_2)

    Returns the intersection of two lists (omitting repetitions). The order
    of the elements of the output depends on the order they are found in the
    first list. Usage:

    >>> alist = [1, 2, 3, 4, 5]
    >>> blist = [7, 6, 5, 4, 3]
    >>> llogic.intersection(alist, blist)
    [3, 4, 5]

    >>> alist = [1, 2, 3, 3, 4, 4, 5, 5, 5]
    >>> blist = [3, 3, 4, 5, 5, 6]
    >>> llogic.intersection(alist, blist)
    [3, 4, 5]

    Note that llogic.intersection does not flatten the lists so nested lists
    are of type list:

    >>> alist = [3, 4, [1, [5, 2]]]
    >>> blist = [1, 2, 3, 4, 5]
    >>> llogic.intersection(alist, blist)
    [3, 4]

    The lists can contain any datatype:

    >>> alist = [1, 2.3, 'foo', (3, 7)]
    >>> blist = ['foo', 7+3j, (3, 7)]
    >>> llogic.intersection(alist, blist)
    ['foo', (3, 7)]

    If either list is empty then the result is an empty list:

    >>> alist = [1, 2, 3, 4, 5]
    >>> blist = []
    >>> llogic.intersection(alist, blist)
    []
    """
    if not isinstance(list_1, list):
        raise TypeError('\'list_1\' must be \'list\'')
    if not isinstance(list_2, list):
        raise TypeError('\'list_2\' must be \'list\'')
    output_list = []
    for item in list_1:
        if item in list_2 and item not in output_list:
            output_list.append(item)
    return output_list


def union(list_1: list, list_2: list) -> list:
    r"""llogic.union(list_1, list_2)

    Returns the union of two lists (omitting repetitions). The order of the
    elements of the output depends on the order they are found in the first and
    then in the second lists. Usage:

    >>> alist = [1, 2, 3, 4, 5]
    >>> blist = [7, 6, 5, 4, 3]
    >>> llogic.union(alist, blist)
    [1, 2, 3, 4, 5, 7, 6]

    >>> alist = [1, 2, 3, 3, 4, 4, 5, 5, 5]
    >>> blist = [7, 6, 6, 5, 5, 5, 4]
    >>> llogic.union(alist, blist)
    [1, 2, 3, 4, 5, 7, 6]

    Note that llogic.union does not flatten the lists so nested lists
    are of type list:

    >>> alist = [3, 4, [1, [5, 2]]]
    >>> blist = [1, 2, 3, 4, 5]
    >>> llogic.union(alist, blist)
    [3, 4, [1, [5, 2]], 1, 2, 5]

    The lists can contain any datatype:

    >>> alist = [1, 2.3, 'foo', (3, 7)]
    >>> blist = ['foo', 7+3j, (3, 7)]
    >>> llogic.union(alist, blist)
    [1, 2.3, 'foo', (3, 7), 7+3j]
    """
    if not isinstance(list_1, list):
        raise TypeError('\'list_1\' must be \'list\'')
    if not isinstance(list_2, list):
        raise TypeError('\'list_2\' must be \'list\'')
    output_list = []
    for item in list_1 + list_2:
        if item not in output_list:
            output_list.append(item)
    return output_list


def difference(list_1: list, list_2: list) -> list:
    r"""llogic.difference(list_1, list_2)

    Returns the difference of two lists (omitting repetitions). The order
    of the elements of the output depends on their order in the lists. The
    order of the inputs lists does affect the result. Usage:

    >>> alist = [1, 2, 3, 4, 5]
    >>> blist = [7, 6, 5, 4, 3]
    >>> llogic.difference(alist, blist)
    [1, 2]
    >>> llogic.difference(blist, alist)
    [7, 6]

    >>> alist = [1, 2, 3, 3, 4, 4, 5, 5, 5]
    >>> blist = [3, 3, 4, 5, 5, 6]
    >>> llogic.difference(alist, blist)
    [1, 2]

    Note that llogic.difference does not flatten the lists so nested lists
    are of type list:

    >>> alist = [3, 4, 1, 5, 2]
    >>> blist = [1, 2, 3, 4, 5]
    >>> llogic.difference(alist, blist)
    []
    >>> alist = [3, 4, [1, [5, 2]]]
    >>> blist = [1, 2, 3, 4, 5]
    >>> llogic.difference(alist, blist)
    [[1, [5, 2]]]

    The lists can contain any datatype:

    >>> alist = [1, 2.3, 'foo', (3, 7)]
    >>> blist = ['foo', 7+3j, (3, 7)]
    >>> llogic.difference(alist, blist)
    [1, 2.3]
    """
    if not isinstance(list_1, list):
        raise TypeError('\'list_1\' must be \'list\'')
    if not isinstance(list_2, list):
        raise TypeError('\'list_2\' must be \'list\'')
    output_list = []
    for item in list_1:
        if item not in list_2 and item not in output_list:
            output_list.append(item)
    return output_list


def symmetric_difference(list_1: list, list_2: list) -> list:
    r"""llogic.symmetric_difference(list_1, list_2)

    Returns the symmetric difference of two lists (omitting repetitions). The
    order of the elements of the output depends on their order in the lists.
    The order of the inputs lists does affect the result. Usage:

    >>> alist = [1, 2, 3, 4, 5]
    >>> blist = [7, 6, 5, 4, 3]
    >>> llogic.symmetric_difference(alist, blist)
    [1, 2, 7, 6]
    >>> llogic.symmetric_difference(blist, alist)
    [7, 6, 1, 2]

    >>> alist = [1, 2, 3, 3, 4, 4, 5, 5, 5]
    >>> blist = [3, 3, 4, 5, 5, 6]
    >>> llogic.symmetric_difference(alist, blist)
    [1, 2, 6]

    Note that llogic.symmetric_difference does not flatten the lists so nested
    lists are of type list:

    >>> alist = [3, 4, 1, 5, 2]
    >>> blist = [1, 2, 3, 4, 5]
    >>> llogic.symmetric_difference(alist, blist)
    []
    >>> alist = [3, 4, [1, [5, 2]]]
    >>> blist = [1, 2, 3, 4, 5]
    >>> llogic.symmetric_difference(alist, blist)
    [[1, [5, 2]], 1, 2, 5]

    The lists can contain any datatype:

    >>> alist = [1, 2.3, 'foo', (3, 7)]
    >>> blist = ['foo', 7+3j, (3, 7)]
    >>> llogic.symmetric_difference(alist, blist)
    [1, 2.3, 7+3j]
    """
    if not isinstance(list_1, list):
        raise TypeError('\'list_1\' must be \'list\'')
    if not isinstance(list_2, list):
        raise TypeError('\'list_2\' must be \'list\'')
    output_list = []
    for item in list_1 + list_2:
        if item not in list_1 or item not in list_2:
            if item not in output_list:
                output_list.append(item)
    return output_list


def is_contained(list_1: list, list_2: list) -> list:
    r"""llogic.is_contained(list_1, list_2)

    Returns True if all unique elements of list_1 are also present in list_2
    and returns False when that's not the case. Usage:

    >>> alist = [1, 2, 3, 4, 5]
    >>> blist = [2, 3, 4]
    >>> llogic.is_contained(blist, alist)
    True
    >>> llogic.is_contained(alist, blist)
    False

    >>> alist = [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7]
    >>> blist = [3, 3, 4, 5, 5, 6]
    >>> llogic.is_contained(blist, alist)
    True

    Lists are not flattened, so sublists are considered as a single element:

    >>> alist = [3, 4, [1, [5, 2]]]
    >>> blist = [1, 2]
    >>> llogic.is_contained(blist, alist)
    False

    The lists can contain any datatype:

    >>> alist = [1, 2.3, 'foo', (3, 7), 7+3j]
    >>> blist = ['foo', 7+3j, (3, 7)]
    >>> llogic.is_contained(blist, alist)
    True
    """
    if not isinstance(list_1, list):
        raise TypeError('\'list_1\' must be \'list\'')
    if not isinstance(list_2, list):
        raise TypeError('\'list_2\' must be \'list\'')
    for item in list_1:
        if item not in list_2:
            return False
    return True
