def is_ascending(input_list: list, step: int = 1) -> bool:
    r"""llogic.is_ascending(input_list[, step])

    This function returns True if the input list is ascending with a fixed
    step, otherwise it returns False. Usage:

    >>> alist = [0, 1, 2, 3]
    >>> llogic.is_ascending(alist)
    True

    The initial value can be other than zero:

    >>> alist = [10, 11, 12]
    >>> llogic.is_ascending(alist)
    True

    The list can also have negative elements:

    >>> alist = [-2, -1, 0, 1, 2]
    >>> llogic.is_ascending(alist)
    True

    It will return False if the list is not ascending:

    >>> alist = [6, 5, 9, 2]
    >>> llogic.is_ascending(alist)
    False

    By default, the function uses steps of size 1 so the list below is not
    considered as ascending:

    >>> alist = [1, 3, 5, 7]
    >>> llogic.is_ascending(alist)
    False

    But the user can set the step argument to any value greater than one:

    >>> alist = [1, 3, 5, 7]
    >>> step = 2
    >>> llogic.is_ascending(alist, step)
    True
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    if not isinstance(step, int):
        raise TypeError('\'step\' must be \'int\'')
    if step < 1:
        raise ValueError('\'step\' must be > 0')
    aux_list = list(range(min(input_list), max(input_list)+1, step))
    return input_list == aux_list
