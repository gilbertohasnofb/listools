from .flatten import flatten


def flatten_join(*input_lists: list) -> list:
    r"""flatools.flatten_join(*input_lists)

    Completely flattens and concatenates an arbitrary number of input lists
    containing any number of nested subslists. Usage:

    >>> alist = [[1, 2], [3, 4]]
    >>> blist = [[5, 6], [7, 8]]
    >>> flatools.flatten_join(alist, blist)
    [1, 2, 3, 4, 5, 6, 7, 8]

    >>> alist = [1, [2, [3]]]
    >>> blist = [[[4], 5], 6]
    >>> flatools.flatten_join(alist, blist)
    [1, 2, 3, 4, 5, 6]

    >>> alist = [[1, 2], [3, 4]]
    >>> blist = [[5, 6], [7, 8]]
    >>> clist = [[[9], 10], 11]
    >>> flatools.flatten_join(alist, blist, clist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    Notice that the list themselves can be made out of any datatypes:

    >>> alist = [1, [2.2, True]]
    >>> blist = ['foo', [(1, 4), None]]
    >>> clist = [3+2j, {'a': 1}]
    >>> flatools.flatten_join(alist, blist, clist)
    [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    """
    if not all(isinstance(input_list, list) for input_list in input_lists):
        raise TypeError('\'*input_lists\' must be one or more \'list\'')
    output_list = []
    for input_list in input_lists:
        output_list += (flatten(input_list))
    return output_list
