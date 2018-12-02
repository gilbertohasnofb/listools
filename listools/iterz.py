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

"""The module `iterz` contains functions that manipualte lists as iterators.
The full list of available functions is:

* `iterz.cycle_until_index(input_iter, i)`
* `iterz.inf_cycle(input_iter)`
* `iterz.ncycles(input_iter, n)`
* `iterz.zip_cycle(*input_iters)`
* `iterz.zip_each(*input_iters)`
* `iterz.zip_inf_cycle(*input_iters)`
* `iterz.zip_syzygy(*input_iters)`

All functions have a `__doc__` attribute with usage instructions.

This library is published under the MIT License.
"""

from itertools import count
from .listutils import list_lcm


def zip_cycle(*input_iters) -> tuple:
    r"""iterz.zip_cycle(*input_iters)

    Similar to zip but cycles smaller lists or iterables until the longest one
    is output. Usage:

    >>> alist = [1, 2]
    >>> blist = [4, 5, 6, 7, 8]
    >>> for i, j in iterz.zip_cycle(alist, blist):
    ...     print(i, j)
    1 4
    2 5
    1 6
    2 7
    1 8

    It also works with multiple lists:

    >>> alist = [1, 2]
    >>> blist = [1, 2, 3]
    >>> clist = [1, 2, 3, 4]
    >>> dlist = [1, 2, 3, 4, 5]
    >>> for i, j, k, l in iterz.zip_cycle(alist, blist, clist, dlist):
    ...     print(i, j, k, l)
    1 1 1 1
    2 2 2 2
    1 3 3 3
    2 1 4 4
    1 2 1 5

    In fact, it works with any iterable containing any datatypes:

    >>> a = (1, 2, 3)
    >>> b = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    >>> c = 'abcde'
    >>> for i, j, k in iterz.zip_cycle(a, b, c):
    ...     print(i, j, k)
    1 1.0 a
    2 2.0 b
    3 3.0 c
    1 4.0 d
    2 5.0 e
    3 6.0 a
    1 7.0 b
    """
    for input_iter in input_iters:
        try:
            iterator = iter(input_iter)
        except:
            raise TypeError('\'*input_iters\' must be one or more \'iter\'')
    if any(len(input_iter) == 0 for input_iter in input_iters):
        raise IndexError('all elements of \'*input_iters\' must have len > 0')
    max_length = max([len(input_iter) for input_iter in input_iters])
    for i in range(max_length):
        output_list = []
        for input_iter in input_iters:
            output_list.append(input_iter[i % len(input_iter)])
        yield tuple(output_list)


def zip_each(*input_iters) -> tuple:
    r"""iterz.zip_each(*input_iters)

    Similar to zip but cycles yields outputs until the longest one is
    completely output while any exhausted iter yield None. Usage:

    >>> alist = [1, 2]
    >>> blist = [4, 5, 6, 7, 8]
    >>> for i, j in iterz.zip_each(alist, blist):
    ...     print(i, j)
    1 4
    2 5
    None 6
    None 7
    None 8

    It also works with multiple lists:

    >>> alist = [1, 2]
    >>> blist = [1, 2, 3]
    >>> clist = [1, 2, 3, 4]
    >>> dlist = [1, 2, 3, 4, 5]
    >>> for i, j, k, l in iterz.zip_each(alist, blist, clist, dlist):
    ...     print(i, j, k, l)
    1 1 1 1
    2 2 2 2
    None 3 3 3
    None None 4 4
    None None None 5

    In fact, it works with any iterable containing any datatypes:

    >>> a = (1, 2, 3)
    >>> b = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    >>> c = 'abcde'
    >>> for i, j, k in iterz.zip_each(a, b, c):
    ...     print(i, j, k)
    1 1.0 a
    2 2.0 b
    3 3.0 c
    None 4.0 d
    None 5.0 e
    None 6.0 None
    None 7.0 None
    """
    for input_iter in input_iters:
        try:
            iterator = iter(input_iter)
        except:
            raise TypeError('\'*input_iters\' must be one or more \'iter\'')
    if any(len(input_iter) == 0 for input_iter in input_iters):
        raise IndexError('all elements of \'*input_iters\' must have len > 0')
    max_length = max([len(input_iter) for input_iter in input_iters])
    for i in range(max_length):
        output_list = []
        for input_iter in input_iters:
            if i < len(input_iter):
                output_list.append(input_iter[i])
            else:
                output_list.append(None)
        yield tuple(output_list)


def zip_inf_cycle(*input_iters) -> tuple:
    r"""iterz.zip_inf_cycle(*input_iters)

    Similar to zip but cycles all lists indefinitely. Usage:

    >>> alist = [1, 2]
    >>> blist = [4, 5, 6, 7, 8]
    >>> zip_inf_cycle_iter = iterz.zip_inf_cycle(alist, blist)
    >>> for i in range(9):
    ...     print(zip_inf_cycle_iter.__next__())
    1 4
    2 5
    1 6
    2 7
    1 8
    2 4
    1 5
    2 6
    1 7

    It also works with multiple lists:

    >>> alist = [1, 2]
    >>> blist = [1, 2, 3]
    >>> clist = [1, 2, 3, 4]
    >>> dlist = [1, 2, 3, 4, 5]
    >>> zip_inf_cycle_iter = iterz.zip_inf_cycle(alist, blist, clist, dlist)
    >>> for i in range(7):
    ...     print(zip_inf_cycle_iter.__next__())
    1 1 1 1
    2 2 2 2
    1 3 3 3
    2 1 4 4
    1 2 1 5
    1 3 2 1
    2 1 3 2

    In fact, it works with any iterable containing any datatypes:

    >>> a = (1, 2, 3)
    >>> b = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    >>> c = 'abcde'
    >>> zip_inf_cycle_iter = iterz.zip_inf_cycle(a, b, c)
    >>> for i in range(10):
    ...     print(zip_inf_cycle_iter.__next__())
    1 1.0 a
    2 2.0 b
    3 3.0 c
    1 4.0 d
    2 5.0 e
    3 6.0 a
    1 7.0 b
    2 1.0 c
    3 2.0 d
    1 3.0 e
    """
    for input_iter in input_iters:
        try:
            iterator = iter(input_iter)
        except:
            raise TypeError('\'*input_iters\' must be one or more \'iter\'')
    if any(len(input_iter) == 0 for input_iter in input_iters):
        raise IndexError('all elements of \'*input_iters\' must have len > 0')
    for i in count():
        output_list = []
        for input_iter in input_iters:
            output_list.append(input_iter[i % len(input_iter)])
        yield tuple(output_list)


def zip_syzygy(*input_iters) -> tuple:
    r"""iterz.zip_syzygy(*input_iters)

    Similar to zip but cycles lists until all of them are exhausted at the same
    time (that is, when the next output tuple would be the same as the very
    first yielded one). Usage:

    >>> alist = [1, 2]
    >>> blist = [4, 5, 6, 7, 8]
    >>> for i, j in iterz.zip_syzygy(alist, blist):
    ...     print(i, j)
    1 4
    2 5
    1 6
    2 7
    1 8
    2 4
    1 5
    2 6
    1 7
    2 8

    It also works with multiple lists:

    >>> alist = [1, 2]
    >>> blist = [1, 2, 3]
    >>> clist = [1, 2, 3, 4]
    >>> dlist = [4, 5, 6]
    >>> for i, j, k, l in iterz.zip_syzygy(alist, blist, clist, dlist):
    ...     print(i, j, k, l)
    1 1 1 4
    2 2 2 5
    1 3 3 6
    2 1 4 4
    1 2 1 5
    2 3 2 6
    1 1 3 4
    2 2 4 5
    1 3 1 6
    2 1 2 4
    1 2 3 5
    2 3 4 6

    In fact, it works with any iterable containing any datatypes:

    >>> a = (1, 2)
    >>> b = [1.0, 2.0, 3.0]
    >>> c = 'abc'
    >>> for i, j, k in iterz.zip_syzygy(a, b, c):
    ...     print(i, j, k)
    1 1.0 a
    2 2.0 b
    1 3.0 c
    2 1.0 a
    1 2.0 b
    2 3.0 c
    """
    for input_iter in input_iters:
        try:
            iterator = iter(input_iter)
        except:
            raise TypeError('\'*input_iters\' must be one or more \'iter\'')
    if any(len(input_iter) == 0 for input_iter in input_iters):
        raise IndexError('all elements of \'*input_iters\' must have len > 0')
    lcm = list_lcm([len(input_iter) for input_iter in input_iters])
    for i in range(lcm):
        output_list = []
        for input_iter in input_iters:
            output_list.append(input_iter[i % len(input_iter)])
        yield tuple(output_list)


def inf_cycle(input_iter):
    r"""iterz.inf_cycle(input_iter)

    This will cycle an iterator indefinitely. Usage:

    >>> alist = [1, 2, 4, 8]
    >>> inf_cycle_iter = iterz.inf_cycle(alist)
    >>> for i in range(9):
    ...     print(inf_cycle_iter.__next__())
    1
    2
    4
    8
    1
    2
    4
    8
    1

    In fact, it works with any iterable containing any datatypes:

    >>> atuple = (1, 'foo', 3.0)
    >>> inf_cycle_iter = iterz.inf_cycle(atuple)
    >>> for i in range(5):
    ...     print(inf_cycle_iter.__next__())
    1
    foo
    3.0
    1
    foo
    """
    try:
        iterator = iter(input_iter)
    except:
        raise TypeError('\'input_iter\' must be \'iter\'')
    if len(input_iter) < 1:
        return
    for i in count():
        yield input_iter[i % len(input_iter)]


def ncycle(input_iter, n: int):
    r"""iterz.ncycle(input_iter)

    This will cycle an iterator a certain number of times. Usage:

    >>> alist = [1, 2, 4, 8]
    >>> for item in iterz.ncycle(alist, 2)
    ...     print(item)
    1
    2
    4
    8
    1
    2
    4
    8

    In fact, it works with any iterable containing any datatypes:

    >>> atuple = (1, 'foo', 3.0)
    >>> for item in iterz.ncycle(atuple, 3):
    ...     print(item)
    1
    foo
    3.0
    1
    foo
    3.0
    1
    foo
    3.0
    """
    try:
        iterator = iter(input_iter)
    except:
        raise TypeError('\'input_iter\' must be \'iter\'')
    if not isinstance(n, int):
        raise TypeError('\'n\' must be \'int\'')
    if len(input_iter) < 1:
        return
    for i in range(n * len(input_iter)):
        yield input_iter[i % len(input_iter)]


def cycle_until_index(input_iter, i: int):
    r"""iterz.cycle_until_index(input_iter, i)

    This will cycle an iterator up to a certain index (inclusive). Usage:

    >>> alist = [1, 2, 4, 8, 16, 32]
    >>> for item in iterz.cycle_until_index(atuple, 4):
    ...     print(item)
    1
    2
    4
    8
    16

    In fact, it works with any iterable containing any datatypes:

    >>> atuple = (1, 'foo', 3.0, 3+2j, [0.0])
    >>> for item in iterz.cycle_until_index(atuple, 3):
    ...     print(item)
    1
    foo
    3.0
    3+2j
    """
    try:
        iterator = iter(input_iter)
    except:
        raise TypeError('\'input_iter\' must be \'iter\'')
    if not isinstance(i, int):
        raise TypeError('\'i\' must be \'int\'')
    if len(input_iter) < 1:
        return
    for item in input_iter[:i + 1]:
        yield item
