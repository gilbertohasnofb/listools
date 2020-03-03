def list_mask_cycle(input_list: list, mask: list) -> list:
    r"""listutils.list_mask_cycle(input_list, mask)

    This function takes an input list and applies a mask to it, outputting a
    new list. The mask should be a list containing 1's and 0's, or
    alternatively True's and False's. If the mask is shorter than the list,
    the mask is cycled. Usage:

    >>> alist = [1, 2, 3]
    >>> mask = [True, False, True]
    >>> listutils.list_mask_cycle(alist, mask)
    [1, 3]

    >>> alist = [1, 2, 3, 4, 5]
    >>> mask = [1, 0, 0, 1, 0]
    >>> listutils.list_mask_cycle(alist, mask)
    [1, 4]

    If the mask is shorter than the list, it loops:

    >>> alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> mask = [1, 0]
    >>> listutils.list_mask_cycle(alist, mask)
    [1, 3, 5, 7, 9]

    The input list can contain any datatypes:

    >>> alist = [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    >>> mask = [True, False, True]
    >>> listutils.list_mask_cycle(alist, mask)
    [1, True, 'foo', None, 3+2j]

    The input list can be empty, in which case an empty list is return. On the
    other hand, the mask argument cannot be an empty list.
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
    if not isinstance(mask, list):
        raise TypeError('\'mask\' must be \'list\'')
    if len(mask) == 0:
        raise IndexError('\'mask\' must have len > 0')
    if len(input_list) == 0:
        return []

    from ..iterz import zip_cycle  # avoiding a circular import

    output_list = []
    for item, mask_value in zip_cycle(input_list, mask):
        if mask_value:
            output_list.append(item)
    return output_list
