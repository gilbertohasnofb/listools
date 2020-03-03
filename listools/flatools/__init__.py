"""The module `flatools` contains functions that deal with flatten lists. All
functions have a `__doc__` attribute with usage instructions.

Recommended import procedure is:

from listools import flatools

This library is published under the MIT License.
"""

from .flatten import flatten
from .flatten_index import flatten_index
from .flatten_join import flatten_join
from .flatten_len import flatten_len
from .flatten_max import flatten_max
from .flatten_min import flatten_min
from .flatten_mixed_type import flatten_mixed_type
from .flatten_reverse import flatten_reverse
from .flatten_single_type import flatten_single_type
from .flatten_sorted import flatten_sorted
from .flatten_sum import flatten_sum
from .flatten_zip_cycle import flatten_zip_cycle
from .pflatten import pflatten
