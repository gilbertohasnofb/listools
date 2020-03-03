def cycle_until_index(input_iter, i: int):
    r"""iterz.cycle_until_index(input_iter, i)

    This will cycle an iterator up to a certain index (inclusive). Usage:

    >>> alist = [1, 2, 4, 8, 16, 32]
    >>> for item in iterz.cycle_until_index(atuple, 4):
    ...     print(item)
    1
    2
    4
    8
    16

    In fact, it works with any iterable containing any datatypes:

    >>> atuple = (1, 'foo', 3.0, 3+2j, [0.0])
    >>> for item in iterz.cycle_until_index(atuple, 3):
    ...     print(item)
    1
    foo
    3.0
    3+2j
    """
    try:
        iterator = iter(input_iter)
    except:
        raise TypeError('\'input_iter\' must be \'iter\'')
    if not isinstance(i, int):
        raise TypeError('\'i\' must be \'int\'')
    if len(input_iter) < 1:
        return
    for item in input_iter[: i + 1]:
        yield item
