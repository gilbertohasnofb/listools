listools
========

|PyPI| |Python versions| |License|

This library provides utility functions for dealing with lists in Python 3. `listools` supports Python version 3.0 and newer. It is contained in a single Python file, so it can be easily copied into your project (the copyright and license notice must be retained). Alternatively, to install it using `pip`, use the command below:

`pip install listools`

Note that you might need to use `pip3` instead of `pip`.

Bugs can be reported to https://github.com/gilbertohasnofb/listools. The code can also be found there.

This library contains the following functions:

* `listools.flatten(input_list)`
* `listools.partial_flatten(input_list[, depth])`
* `listools.concat_flatten(*input_lists)`
* `listools.sum_flatten(input_list)`
* `listools.len_flatten(input_list)`
* `listools.index_flatten(element, input_list)`
* `listools.zip_cycle(*input_iters)`
* `listools.zip_cycle_flatten(*input_lists)`

All functions have a `__doc__` attribute with usage instructions.

This library is published under the MIT License.

.. |PyPI| image:: https://img.shields.io/pypi/v/listools.svg
   :target: https://pypi.python.org/pypi/listools
.. |Python versions| image:: https://img.shields.io/pypi/pyversions/listools.svg
.. |License| image:: https://img.shields.io/github/license/gilbertohasnofb/listools.svg
   :target: https://github.com/gilbertohasnofb/listools/blob/master/LICENSE
