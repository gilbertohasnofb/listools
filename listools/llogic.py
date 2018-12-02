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

* `llogic.mixed_type(input_list)`
* `llogic.single_type(input_list)`

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

    Note that llogic does not flatten the lists so nested lists are of type
    list:

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
    if not (isinstance(input_list, list)):
        raise TypeError('input_list should be a \'list\'')
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

    Note that llogic does not flatten the lists so nested lists are of type
    list:

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
    if not (isinstance(input_list, list)):
        raise TypeError('input_list should be a \'list\'')
    return len(set(map(type, input_list))) > 1
