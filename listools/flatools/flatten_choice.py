from .flatten import flatten
from random import choice as _choice
from typing import Any


def flatten_choice(input_list: list) -> Any:
    r"""flatools.flatten_choice(input_list)

    Randomly selects an element from a flattened list which can containing any
    number of nested subslists. Usage:

    >>> alist = [[1, 4], [5, 7], [2], [9, 6, 10], [8, 3]]
    >>> flatools.flatten_choice(alist)
    9

    >>> alist = [1, 5, [3, [2, 4]]]
    >>> flatools.flatten_choice(alist)
    4

    The list can also be made out of any types:

    >>> alist = [1, [2.2, True], ['foo', [(1, 4), None]], [3+2j, {'a': 1}]]
    >>> flatools.flatten_choice(alist)
    (1, 4)
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    return _choice(flatten(input_list))
