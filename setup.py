# MIT License
#
# Copyright (c) 2018 Gilberto Agostinho
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import listools

listools_classifiers = [
    "Development Status :: 5 - Production/Stable",
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3 :: Only',
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    'Topic :: Software Development :: Libraries :: Python Modules',
    "Topic :: Utilities",
]

with open("README.rst", "r") as fp:
    listools_long_description = fp.read()

setup(
    name='listools',
    description='listools: a Python 3 package of list utilities',
    author='Gilberto Agostinho',
    author_email='gilbertohasnofb@gmail.com',
    version=listools.__version__,
    packages=find_packages(),
    url='https://github.com/gilbertohasnofb/listools',
    license='MIT',
    long_description=listools_long_description,
    tests_require=['pytest'],
    classifiers=listools_classifiers,
    python_requires='>=3.5',
)
