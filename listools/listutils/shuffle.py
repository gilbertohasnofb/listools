from random import shuffle as _shuffle


def shuffle(input_list: list) -> list:
    r"""listutils.shuffle(input_list)

    This function returns a shuffled list with the same elements as the input
    list. Usage:

    >>> alist = [0, 1, 2, 3, 4]
    >>> listutils.shuffle(alist)
    [2, 1, 4, 0, 3]

    It differs from random.shuffle() since listutils.shuffle() outputs a new
    list, preserving the input one:

    >>> alist = [0, 1, 2, 3, 4]
    >>> listutils.shuffle(alist)
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
    shuffled_list = input_list[:]
    _shuffle(shuffled_list)
    return shuffled_list
