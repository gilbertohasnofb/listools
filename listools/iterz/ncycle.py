def ncycle(input_iter, n: int):
    r"""iterz.ncycle(input_iter)

    This will cycle an iterator a certain number of times. Usage:

    >>> alist = [1, 2, 4, 8]
    >>> for item in iterz.ncycle(alist, 2)
    ...     print(item)
    1
    2
    4
    8
    1
    2
    4
    8

    In fact, it works with any iterable containing any datatypes:

    >>> atuple = (1, 'foo', 3.0)
    >>> for item in iterz.ncycle(atuple, 3):
    ...     print(item)
    1
    foo
    3.0
    1
    foo
    3.0
    1
    foo
    3.0
    """
    try:
        iterator = iter(input_iter)
    except:
        raise TypeError('\'input_iter\' must be \'iter\'')
    if not isinstance(n, int):
        raise TypeError('\'n\' must be \'int\'')
    if len(input_iter) < 1:
        return
    for i in range(n * len(input_iter)):
        yield input_iter[i % len(input_iter)]
