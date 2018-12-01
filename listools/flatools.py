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

"""The module `flatools` contains functions that deal with flatten lists. The
full list of available functions is:

* `flatools.flatten_index(element, input_list)`
* `flatools.flatten_join(*input_lists)`
* `flatools.flatten_len(input_list)`
* `flatools.flatten_reverse(input_list)`
* `flatools.flatten_sorted(input_list, *[, key][, reverse])`
* `flatools.flatten_sum(input_list[, start])`
* `flatools.flatten_zip_cycle(*input_lists)`
* `flatools.flatten(input_list)`
* `flatools.pflatten(input_list[, depth])`

All functions have a `__doc__` attribute with usage instructions.

This library is published under the MIT License.
"""


def flatten(input_list: list) -> list:
    r"""flatools.flatten(input_list)

    Completely flattens a list containing any number of nested subslists into a
    one dimensional list. It is equivalent to flatools.pflatten() with
    an infinitely large depth. Usage:

    >>> alist = [[1, 2], [3, 4], [5], [6, 7, 8], [9, 10]]
    >>> flatools.flatten(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> alist = [1, 2, [3, [4, 5]]]
    >>> flatools.flatten(alist)
    [1, 2, 3, 4, 5]

    Notice that the list themselves can be made out of any datatypes:

    >>> alist = [1, [2.2, True], ['foo', [(1, 4), None]], [(3+2j), {'a': 1}]]
    >>> flatools.flatten(alist)
    [1, 2.2, True, 'foo', (1, 4), None, (3+2j), {'a': 1}]
    """
    if not (isinstance(input_list, list)):
        raise TypeError('input_list should be a \'list\'')
    def _flatten_aux(input_list, aux_list=None):
        if aux_list is None:
            aux_list = []
        for element in input_list:
            if isinstance(element, list):
                _flatten_aux(element, aux_list)
            else:
                aux_list.append(element)
        return aux_list
    return _flatten_aux(input_list, aux_list=None)


def pflatten(input_list: list, depth: int = 1) -> list:
    r"""flatools.pflatten(input_list[, depth])

    Partially flattens a list containing subslists as elements. Usage:

    >>> alist = [[1, 2], [3, 4], [5], [6, 7, 8], [9, 10]]
    >>> flatools.pflatten(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> alist = [1, 2, [3, [[4], 5]]]
    >>> flatools.pflatten(alist)
    [1, 2, 3, [[4], 5]]

    Use the depth argument (which should always be an integer) when wanting to
    flatten nested sublists:

    >>> alist = [1, 2, [3, [4, 5]]]
    >>> flatools.pflatten(alist, depth=2)
    [1, 2, 3, [4], 5]

    >>> alist = [1, 2, [3, [4, 5]]]
    >>> flatools.pflatten(alist, depth=3)
    [1, 2, 3, 4, 5]

    >>> alist = [1, 2, [3, [4, 5]]]
    >>> flatools.pflatten(alist, depth=4)
    [1, 2, 3, 4, 5]

    Notice that the list themselves can be made out of any datatypes:

    >>> alist = [1, [2.2, True], ['foo', [(1, 4), None]], [(3+2j), {'a': 1}]]
    >>> flatools.flatten(alist, depth=3)
    [1, 2.2, True, 'foo', (1, 4), None, (3+2j), {'a': 1}]
    """
    if not isinstance(input_list, list):
        raise TypeError('input_list should be a \'list\'')
    if not isinstance(depth, int):
        raise TypeError('depth should be an \'int\'')
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


def flatten_join(*input_lists: list) -> list:
    r"""flatools.flatten_join(*input_lists)

    Completely flattens and concatenates an arbitrary number of input lists
    containing any number of nested subslists. Usage:

    >>> alist = [[1, 2], [3, 4]]
    >>> blist = [[5, 6], [7, 8]]
    >>> flatools.flatten_join(alist, blist)
    [1, 2, 3, 4, 5, 6, 7, 8]

    >>> alist = [1, [2, [3]]]
    >>> blist = [[[4], 5], 6]
    >>> flatools.flatten_join(alist, blist)
    [1, 2, 3, 4, 5, 6]

    >>> alist = [[1, 2], [3, 4]]
    >>> blist = [[5, 6], [7, 8]]
    >>> clist = [[[9], 10], 11]
    >>> flatools.flatten_join(alist, blist, clist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    Notice that the list themselves can be made out of any datatypes:

    >>> alist = [1, [2.2, True]]
    >>> blist = ['foo', [(1, 4), None]]
    >>> clist = [(3+2j), {'a': 1}]
    >>> flatools.flatten_join(alist, blist, clist)
    [1, 2.2, True, 'foo', (1, 4), None, (3+2j), {'a': 1}]
    """
    if not all(isinstance(input_list, list) for input_list in input_lists):
        raise TypeError('*input_lists should be one or more \'list\' objects')
    output_list = []
    for input_list in input_lists:
        output_list += (flatten(input_list))
    return output_list


def flatten_sum(input_list: list, start=0):
    r"""flatools.flatten_sum(input_list[, start])

    Sums all values of the list, including any nested subslists. Usage:

    >>> alist = [[1, 2], [3, 4], [5, 6]]
    >>> flatools.flatten_sum(alist)
    21

    >>> alist = [1, [2, [3]]]
    >>> flatools.flatten_sum(alist)
    6

    The list can also be made out of floats:

    >>> alist = [1.1, [2.2, [3.3]]]
    >>> flatools.flatten_sum(alist)
    6.6

    Or it can contain a mix of integers and floats:

    >>> alist = [1, [2.1, [3, [4.1]]]]
    >>> flatools.flatten_sum(alist)
    10.2

    It can also take an optional argument named 'start' which defines the
    starting value of the sum.

    >>> alist = [1, [2, [3]]]
    >>> flatools.flatten_sum(alist, start=4)
    10
    """
    if not (isinstance(input_list, list)):
        raise TypeError('input_list should be a \'list\'')
    return sum(flatten(input_list), start)


def flatten_len(input_list: list) -> int:
    r"""flatools.flatten_len(input_list)

    Returns the flatten_length of a flatten list (that is, it counts all
    elements in all of its subslists). Usage:

    >>> alist = [[1, 2], [3, 4], [5, 6]]
    >>> flatools.flatten_len(alist)
    6

    The datatypes of the elements of the list do not matter:

    >>> alist = [1, [2.2, True], ['foo', [(1, 4), None]], [(3+2j), {'a': 1}]]
    >>> flatools.flatten_len(alist)
    8
    """
    if not (isinstance(input_list, list)):
        raise TypeError('input_list should be a \'list\'')
    return len(flatten(input_list))


def flatten_index(element, input_list: list) -> int:
    r"""flatools.flatten_index(input_list)

    Returns the length of a flatten list (that is, it counts all elements in
    all of its subslists). Usage:

    >>> alist = [[1, 2], [3, 4], [5, 6]]
    >>> flatools.flatten_index(3, alist)
    2

    The datatypes of the elements of the list do not matter:

    >>> alist = [1, [2.2, True], ['foo', [(1, 4), None]], [(3+2j), {'a': 1}]]
    >>> flatools.flatten_index(None, alist)
    5

    Just like the default behaviour of the flatten_index() method of a list,
    flatten_index raises a ValueError if an element is not found in a list:

    >>> alist = [[1, 2], [3, 4], [5, 6]]
    >>> flatools.flatten_index(7, alist)
    ValueError: 7 is not in list
    """
    if isinstance(element, list):
        raise TypeError('element cannot be a \'list\'')
    if not (isinstance(input_list, list)):
        raise TypeError('input_list should be a \'list\'')
    return flatten(input_list).index(element)


def flatten_zip_cycle(*input_lists) -> tuple:
    r"""flatools.flatten_zip_cycle(*input_lists)

    This function is very nearly identical to flatools.flatten_zip_cycle except
    that it also flattens all lists before zipping and cycling them. Usage:

    >>> alist = [1, 2]
    >>> blist = [4, [5, 6, 7], 8]
    >>> for i, j in flatools.flatten_zip_cycle(alist, blist):
    ...     print(i, j)
    1 4
    2 5
    1 6
    2 7
    1 8

    It also works with multiple lists:

    >>> a = [1, 2]
    >>> b = [1, [2, 3]]
    >>> c = [[[1], 2, 3], 4]
    >>> d = [1, [2, [3, 4]], 5]
    >>> for i, j, k, l in flatools.flatten_zip_cycle(a, b, c, d):
    ...     print(i, j, k, l)
    1 1 1 1
    2 2 2 2
    1 3 3 3
    2 1 4 4
    1 2 1 5

    It also works with lists containing any datatypes:

    >>> alist = [1, 2.0, 'foo', True, None]
    >>> blist = [False, 'bar', (1, 4)]
    >>> for i, j in flatools.flatten_zip_cycle(alist, blist):
    ...     print(i, j)
    1 False
    2.0 bar
    foo (1, 4)
    True False
    None bar

    Note that unlike flatools.flatten_zip_cycle(), this function accepts only
    lists as input due to its flatenning function.
    """
    if not all(isinstance(input_list, list) for input_list in input_lists):
        raise TypeError('*input_lists should be one or more \'list\' objects')
    flatten_lists = []
    for input_list in input_lists:
        flatten_lists.append(flatten(input_list))
    aux = max([len(flatten_list) for flatten_list in flatten_lists])
    for i in range(aux):
        output_list = []
        for flatten_list in flatten_lists:
            output_list.append(flatten_list[i % len(flatten_list)])
        yield tuple(output_list)


def flatten_sorted(input_list: list,
                   *,
                   key: 'function' = None,
                   reverse: bool = False,
                   ) -> list:
    r"""flatools.flatten_sorted(input_list, *[, key][, reverse])

    Completely flattens a list containing any number of nested subslists into a
    flatten_sorted one dimensional list. Usage:

    >>> alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    >>> flatools.flatten_sorted(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> alist = [1, 5, [3, [2, 4]]]
    >>> flatools.flatten_sorted(alist)
    [1, 2, 3, 4, 5]

    The list can also be made out of floats:

    >>> alist = [[1.73, -3.14, 9.41], [5.56, -1.03]]
    >>> flatools.flatten_sorted(alist)
    [-3.14, -1.03, 1.73, 5.56, 9.41]

    Or it can be made out of a mixture of integers and floats:

    >>> alist = [[3, 1.4], [5, 7.8], [-3.1, 6.6]]
    >>> flatools.flatten_sorted(alist)
    [-3.1, 1.4, 3, 5, 6.6, 7.8]

    There are two optional arguments that can be used. The first is a called
    'key' and takes a function that serves as a key for the sort comparison.

    >>> alist = [-1, -5, [3, [-2, 4]]]
    >>> print(flatten_sorted(alist))
    [-5, -2, -1, 3, 4]
    >>> print(flatten_sorted(alist, key=abs))
    [-1, -2, 3, 4, -5]

    The second is 'reverse', which reverses the order of the output list:

    >>> alist = [1, 5, [3, [2, 4]]]
    >>> print(flatten_sorted(alist, reverse=True))
    [5, 4, 3, 2, 1]
    """
    if not (isinstance(input_list, list)):
        raise TypeError('input_list should be a \'list\'')
    return sorted(flatten(input_list), key=key, reverse=reverse)


def flatten_reverse(input_list: list) -> list:
    r"""flatools.flatten_reverse(input_list)

    Completely flattens a list containing any number of nested subslists into a
    flatten_reversely sorted one dimensional list. Usage:

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
    if not (isinstance(input_list, list)):
        raise TypeError('input_list should be a \'list\'')
    return sorted(flatten(input_list), reverse=True)
