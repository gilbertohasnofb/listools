from .zip_cycle import zip_cycle
def iter_mask(input_iter, mask: list):
    r"""iterz.iter_mask(input_iter, mask)

    This function takes an input iterator and applies a mask to it, yielding
    values according to the mastk. The mask should be a list containing 1's and
    0's, or alternatively True's and False's. Usage:

    >>> alist = [1, 2, 3]
    >>> mask = [True, False, True]
    >>> for item in iterz.iter_mask(alist, mask):
    ...     print(item)
    1
    3

    >>> alist = [1, 2, 3, 4, 5]
    >>> mask = [1, 0, 0, 1, 0]
    >>> for item in iterz.iter_mask(alist, mask):
    ...     print(item)
    1
    4

    If the mask is shorter than the input iterator, it loops:

    >>> alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> mask = [1, 0]
    >>> for item in iterz.iter_mask(alist, mask):
    ...     print(item)
    1
    3
    5
    7
    9

    The input iterator can contain any datatypes:

    >>> alist = [1, 2.2, True, 'foo', (1, 4), None, 3+2j, {'a': 1}]
    >>> mask = [True, False, True]
    >>> for item in iterz.iter_mask(alist, mask):
    ...     print(item)
    1
    True
    'foo'
    None
    3+2j
    """
    try:
        iterator = iter(input_iter)
    except:
        raise TypeError('\'input_iter\' must be \'iter\'')
    if not isinstance(mask, list):
        raise TypeError('\'mask\' must be \'list\'')
    if len(mask) == 0:
        raise IndexError('\'mask\' must have len > 0')
    if len(input_iter) == 0:
        return
    for item, mask_value in zip_cycle(input_iter, mask):
        if mask_value:
            yield item
