"""`listools` is a Python 3 package of which provides utility functions for
dealing with lists in Python 3. `listools` supports Python version 3.5 and
newer. You can install it using `pip install listools`.

This package contains four modules: `flatools`, `iterz`, `listutils` and
`llogic`. The complete list of functions available is:

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
* `iterz.iter_mask(input_iter, mask)`
* `iterz.ncycles(input_iter, n)`
* `iterz.zip_cycle(*input_iters)`
* `iterz.zip_inf_cycle(*input_iters)`
* `iterz.zip_longest(*input_iters[, default])`
* `iterz.zip_syzygy(*input_iters)`

* `listutils.list_lcm(input_list)`
* `listutils.list_mask(input_list, mask)`
* `listutils.list_mask_cycle(input_list, mask)`
* `listutils.list_gcd(input_list)`

* `llogic.difference(list_1, list_2)`
* `llogic.intersection(list_1, list_2)`
* `llogic.is_contained(list_1, list_2)`
* `llogic.mixed_type(input_list)`
* `llogic.single_type(input_list)`
* `llogic.symmetric_difference(list_1, list_2)`
* `llogic.union(list_1, list_2)`

All functions have a `__doc__` attribute with usage instructions.

Documentation is available at https://gilbertohasnofb.github.io/listools-docs/.

A pdf version of the documentation is also available in the `docs` directory.

Bugs can be reported to https://github.com/gilbertohasnofb/listools/issues.

This library is published under the MIT License.
"""

from listools.flatools import *
from listools.iterz import *
from listools.llogic import *
from listools.listutils import *

__author__ = "Gilberto Agostinho <gilbertohasnofb@gmail.com>"
__version__ = "2.1.2"
__all__ = ['flatools', 'iterz', 'listutils', 'llogic']
