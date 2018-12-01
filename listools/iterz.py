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

* `iterz.zip_cycle(*input_lists)`

All functions have a `__doc__` attribute with usage instructions.

This library is published under the MIT License.
"""


def zip_cycle(*input_iters) -> tuple:
    r"""listools.iterz.zip_cycle(*input_iters)

    Similar to zip but cycles smaller lists or iterables until the largerst one
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
            raise TypeError('*input_iters should a list of \'iter\' objects')
    aux = max([len(input_iter) for input_iter in input_iters])
    for i in range(aux):
        output_list = []
        for input_iter in input_iters:
            output_list.append(input_iter[i % len(input_iter)])
        yield tuple(output_list)
