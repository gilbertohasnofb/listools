from .flatten import flatten


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
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    return sum(flatten(input_list), start)
