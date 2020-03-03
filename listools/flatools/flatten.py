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

    >>> alist = [1, [2.2, True], ['foo', [(1, 4), None]], [3+2j, {'a': 1}]]
    >>> flatools.flatten(alist)
    [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    """
    if not isinstance(input_list, list):
        raise TypeError('\'input_list\' must be \'list\'')
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
