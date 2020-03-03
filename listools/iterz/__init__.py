"""The module `iterz` contains functions that manipualte lists as iterators.
All functions have a `__doc__` attribute with usage instructions.

Recommended import procedure is:

from listools import iterz

This library is published under the MIT License.
"""

from .cycle_until_index import cycle_until_index
from .inf_cycle import inf_cycle
from .iter_mask import iter_mask
from .ncycle import ncycle
from .zip_cycle import zip_cycle
from .zip_inf_cycle import zip_inf_cycle
from .zip_longest import zip_longest
from .zip_syzygy import zip_syzygy
