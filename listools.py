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

"""The `listools` library provides utility functions for dealing with lists in
Python 3. `listools` supports Python version 3.0 and newer. It is contained in
only one Python file, so it can be easily copied into your project. (The
copyright and license notice must be retained.)

Bugs can be reported to https://github.com/gilbertohasnofb/listools. The code
can also be found there.

This library contains the following functions:

* `listools.flatten(input_list[, depth])`
* `listools.completely_flatten(input_list)`

All functions contain a `__doc__` attribute with usage instructions.
"""

__author__ = "Gilberto Agostinho <gilbertohasnofb@gmail.com>"
__version__ = "0.1.2"


def flatten(input_list: list, depth: int = 1) -> list:
    r"""listools.flatten(input_list[, depth])

    Flattens a list containing subslists as elements. Usage:

    >>> alist = [[1, 2], [3, 4], [5], [6, 7, 8], [9, 10]]
    >>> listools.flatten(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> alist = [1, 2, [3, [[4], 5]]]
    >>> listools.flatten(alist)
    [1, 2, 3, [[4], 5]]

    Use the depth argument (which should always be an integer) when any of the
    sublists themselves also contains sublists:

    >>> alist = [1, 2, [3, [4, 5]]]
    >>> listools.flatten(alist, depth=2)
    [1, 2, 3, [4], 5]

    >>> alist = [1, 2, [3, [4, 5]]]
    >>> listools.flatten(alist, depth=3)
    [1, 2, 3, 4, 5]

    >>> alist = [1, 2, [3, [4, 5]]]
    >>> listools.flatten(alist, depth=4)
    [1, 2, 3, 4, 5]

    Notice that the list themselves can be made out of any datatypes:

    >>> alist = [1, [2.2, True], ['foo', [(1, 4), None]], [(3+2j), {'a': 1}]]
    >>> listools.flatten(alist, depth=3)
    [1, 2.2, True, 'foo', (1, 4), None, (3+2j), {'a': 1}]
    """
    if not (isinstance(input_list, list) or isinstance(depth, int)):
        raise TypeError
    aux_list = input_list[:]
    for _ in range(depth):
        output_list = []
        for element in aux_list:
            if not isinstance(element, list):
                output_list.append(element)
            else:
                output_list += element
        aux_list = output_list[:]
    return output_list


def completely_flatten(input_list: list, _aux_list=None) -> list:
    r"""listools.completely_flatten(input_list)

    Completely flattens a list containing any number of nested subslists into a
    one dimensional list. It is equivalent to listools.flatten() with an
    infinitely large depth. Usage:

    >>> alist = [[1, 2], [3, 4], [5], [6, 7, 8], [9, 10]]
    >>> listools.completely_flatten(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> alist = [1, 2, [3, [4, 5]]]
    >>> listools.completely_flatten(alist)
    [1, 2, 3, 4, 5]

    Notice that the list themselves can be made out of any datatypes:

    >>> alist = [1, [2.2, True], ['foo', [(1, 4), None]], [(3+2j), {'a': 1}]]
    >>> listools.completely_flatten(alist)
    [1, 2.2, True, 'foo', (1, 4), None, (3+2j), {'a': 1}]
    """
    if not (isinstance(input_list, list)):
        raise TypeError
    if _aux_list is None:
        _aux_list = []
    for element in input_list:
        if isinstance(element, list):
            completely_flatten(element, _aux_list)
        else:
            _aux_list.append(element)
    return _aux_list


def concat_flatten(*input_lists: list) -> list:
    r"""listools.concat_flatten(*input_lists)

    Completely flattens and concatenates an arbitrary number of input lists
    containing any number of nested subslists. Usage:

    >>> alist = [[1, 2], [3, 4]]
    >>> blist = [[5, 6], [7, 8]]
    >>> listools.concat_flatten(alist, blist)
    [1, 2, 3, 4, 5, 6, 7, 8]

    >>> alist = [1, [2, [3]]]
    >>> blist = [[[4], 5], 6]
    >>> listools.concat_flatten(alist, blist)
    [1, 2, 3, 4, 5, 6]

    >>> alist = [[1, 2], [3, 4]]
    >>> blist = [[5, 6], [7, 8]]
    >>> clist = [[[9], 10], 11]
    >>> listools.concat_flatten(alist, blist, clist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    Notice that the list themselves can be made out of any datatypes:

    >>> alist = [1, [2.2, True]]
    >>> blist = ['foo', [(1, 4), None]]
    >>> clist = [(3+2j), {'a': 1}]
    >>> listools.concat_flatten(alist, blist, clist)
    [1, 2.2, True, 'foo', (1, 4), None, (3+2j), {'a': 1}]
    """
    if not all(isinstance(input_list, list) for input_list in input_lists):
        raise TypeError
    output_list = []
    for input_list in input_lists:
        output_list += (completely_flatten(input_list))
    return output_list


def sum_flatten(input_list: list):
    r"""listools.sum_flatten(input_list)

    Sums all values of the list, including any nested subslists. Usage:

    >>> alist = [[1, 2], [3, 4], [5, 6]]
    >>> sum_flatten(alist)
    21

    >>> alist = [1, [2, [3]]]
    >>> sum_flatten(alist)
    6

    The list can also be made out of floats:

    >>> alist = [1.1, [2.2, [3.3]]]
    >>> sum_flatten(alist)
    6.6

    Or it can contain a mix of integers and floats:

    >>> alist = [1, [2.1, [3, [4.1]]]]
    >>> sum_flatten(alist)
    10.2
    """
    if not (isinstance(input_list, list)):
        raise TypeError
    return sum(completely_flatten(input_list))
