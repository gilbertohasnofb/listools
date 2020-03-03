def is_descending(input_list: list, step: int = -1) -> bool:
    r"""llogic.is_descending(input_list[, step])

    This function returns True if the input list is descending with a fixed
    step, otherwise it returns False. Usage:

    >>> alist = [3, 2, 1, 0]
    >>> llogic.is_descending(alist)
    True

    The final value can be other than zero:

    >>> alist = [12, 11, 10]
    >>> llogic.is_descending(alist)
    True

    The list can also have negative elements:

    >>> alist = [2, 1, 0, -1, -2]
    >>> llogic.is_descending(alist)
    True

    It will return False if the list is not ascending:

    >>> alist = [6, 5, 9, 2]
    >>> llogic.is_descending(alist)
    False

    By default, the function uses steps of size 1 so the list below is not
    considered as ascending:

    >>> alist = [7, 5, 3, 1]
    >>> llogic.is_descending(alist)
    False

    But the user can set the step argument to any value less than one:

    >>> alist = [7, 5, 3, 1]
    >>> step = -2
    >>> llogic.is_descending(alist, step)
    True
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    if not isinstance(step, int):
        raise TypeError('\'step\' must be \'int\'')
    if step > 1:
        raise ValueError('\'step\' must be < 0')
    aux_list = list(range(max(input_list), min(input_list)-1, step))
    return input_list == aux_list
