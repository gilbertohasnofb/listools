"""`listools` is a Python 3 package of which provides utility functions for
dealing with lists in Python 3. `listools` supports Python version 3.0 and
newer. You can install it using `pip install listools`.

Bugs can be reported to https://github.com/gilbertohasnofb/listools/issues.

This package contains three modules: `flatools`, `iterz` and `llogic`. The
complete list of functions available is:

* `flattools.flatten_index(element, input_list)`
* `flattools.flatten_join(*input_lists)`
* `flattools.flatten_len(input_list)`
* `flattools.flatten_reverse(input_list)`
* `flattools.flatten_sorted(input_list)`
* `flattools.flatten_sum(input_list)`
* `flattools.flatten_zip_cycle(*input_lists)`
* `flattools.flatten(input_list)`
* `flattools.pflatten(input_list[, depth])`
* `iterz.zip_cycle(*input_iters)`

All functions have a `__doc__` attribute with usage instructions.

This library is published under the MIT License.
"""

from listools.flatools import *
from listools.iterz import *
from listools.llogic import *

__author__ = "Gilberto Agostinho <gilbertohasnofb@gmail.com>"
__version__ = "2.0.0"
__all__ = ['flatools', 'iterz', 'llogic']
