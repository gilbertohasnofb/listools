listools
========

|PyPI| |Build| |Python versions| |License|  |Bug report|

`listools` is a Python 3 package of which provides utility functions for dealing with lists in Python 3. `listools` supports Python version 3.0 and newer. You can install it using `pip install listools`.

Bugs can be reported to https://github.com/gilbertohasnofb/listools/issues.

This package contains four modules: `flatools`, `iterz`, `llogic` and `listutils`. The complete list of functions available is:

* `flatools.flatten_index(element, input_list)`
* `flatools.flatten_join(*input_lists)`
* `flatools.flatten_len(input_list)`
* `flatools.flatten_max(input_list, *[, key, default])`
* `flatools.flatten_min(input_list, *[, key, default])`
* `flatools.flatten_mixed_type(input_list)`
* `flatools.flatten_reverse(input_list)`
* `flatools.flatten_single_type(input_list)`
* `flatools.flatten_sorted(input_list, *[, key, reverse])`
* `flatools.flatten_sum(input_list[, start])`
* `flatools.flatten_zip_cycle(*input_lists)`
* `flatools.flatten(input_list)`
* `flatools.pflatten(input_list[, depth])`

* `iterz.cycle_until_index(input_iter, i)`
* `iterz.inf_cycle(input_iter)`
* `iterz.ncycles(input_iter, n)`
* `iterz.zip_cycle(*input_iters)`
* `iterz.zip_each(*input_iters)`
* `iterz.zip_inf_cycle(*input_iters)`
* `iterz.zip_syzygy(*input_iters)`

* `llogic.difference(list_1, list_2)`
* `llogic.intersection(list_1, list_2)`
* `llogic.is_contained(list_1, list_2)`
* `llogic.mixed_type(input_list)`
* `llogic.single_type(input_list)`
* `llogic.symmetric_difference(list_1, list_2)`
* `llogic.union(list_1, list_2)`

* `listutils.list_lcm(input_list)`
* `listutils.list_mask(input_list, mask)`
* `listutils.list_gcd(input_list)`

All functions have a `__doc__` attribute with usage instructions.

This library is published under the MIT License.

.. |PyPI| image:: https://img.shields.io/pypi/v/listools.svg
   :target: https://pypi.python.org/pypi/listools
.. |Build| image:: https://travis-ci.org/gilbertohasnofb/listools.svg?branch=master
   :target: https://travis-ci.org/gilbertohasnofb/listools
.. |Python versions| image:: https://img.shields.io/pypi/pyversions/listools.svg
.. |License| image:: https://img.shields.io/github/license/gilbertohasnofb/listools.svg
   :target: https://github.com/gilbertohasnofb/listools/blob/master/LICENSE
.. |Bug report| image:: https://img.shields.io/badge/bug-report-red.svg
   :target: https://github.com/gilbertohasnofb/listools/issues
