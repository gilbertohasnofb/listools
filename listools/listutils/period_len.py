def period_len(input_list: list, ignore_partial_cycles: bool = False) -> int:
    r"""listutils.period_len(input_list[, ignore_partial_cycles])

    This function returns the length of the period of an input list. Usage:

    >>> alist = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    >>> listutils.period_len(alist)
    3

    If a list is not periodic, the period length equals to the list size:

    >>> alist = [3, 1, 4, 1, 5, 9, 2, 6]
    >>> listutils.period_len(alist)
    8

    This function detects periodicity in lists with partial cycles:

    >>> alist = [1, 2, 3, 1, 2, 3, 1]
    >>> listutils.period_len(alist)
    3

    To disable this behaviour, use the ignore_partial_cycles argument:

    >>> alist = [1, 2, 3, 1, 2, 3, 1]
    >>> listutils.period_len(alist, ignore_partial_cycles=True)
    7

    If a list does not contain partial cycles, the ignore_partial_cycles
    argument does not affect the result:

    >>> alist = [1, 2, 3, 1, 2, 3]
    >>> listutils.period_len(alist, ignore_partial_cycles=True)
    3
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    if not isinstance(ignore_partial_cycles, bool):
        raise TypeError('\'ignore_partial_cycles\' must be \'bool\'')
    for period in range(1, len(input_list)):
        if all(input_list[n] == input_list[n + period] \
               for n in range(len(input_list) - period)):
            if ignore_partial_cycles:
                if len(input_list) % period != 0:
                    return len(input_list)
            return period
    return len(input_list)
