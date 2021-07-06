Installing
==========

**TL;DR**: Simply use *pip* (preferably inside virtualenv):

.. code-block:: shell

    $ pip install calleee

More detailed instructions and additional notes can be found below.


Compatibility
*************

*calleee* itself has no external depedencies: it only needs Python. Both Python 2 and Python 3 is supported,
with some caveats:

* you need at least version 3.6

The library is tested against both CPython (the standard Python implementation) and `PyPy`_.

.. _PyPy: http://pypy.org/


About the mock library
**********************

Although it's not a hard dependency, by design *calleee* is meant to be used with the ``unittest.mock`` module,
which implements *mock objects* for testing.

In Python 3.3 and later, this module is a part of `the standard library`_, and it's already available on any Python distribution.

You can use the mock classes in your tests by referring to them as |mock.Mock|_ or |mock.MagicMock|_.
Additionally, you'll also have a convenient access to the rest of the mocking functionality, like the |@mock.patch|_
decorator.

.. _the standard library: https://docs.python.org/3/library/unittest.mock.html
.. _backport: https://pypi.python.org/pypi/mock

.. |mock.Mock| replace:: ``mock.Mock``
.. _mock.Mock: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
.. |mock.MagicMock| replace:: ``mock.MagicMock``
.. _mock.MagicMock: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock
.. |@mock.patch| replace:: ``@mock.patch``
.. _@mock.patch: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch


Instructions
************

The preferred way to install *calleee* is through *pip*:

.. code-block:: shell

    $ pip install calleee

This will get you the most recent version available on `PyPI`_.

.. _PyPI: https://pypi.python.org/pypi/calleee/

Bleeding edge
-------------

If you want to work with the development version instead, you may either manually clone it using Git, or have *pip*
install it directly from the Git repository.

The first option is especially useful when you need to make some modifications to the library itself
(which you'll hopefully contribute back via a pull request!). If that's the case, clone the library
and install it in development mode:

.. code-block:: shell

    $ git clone https://github.com/untidy-hair/calleee.git
    Initialized empty Git repository in ~/dev/calleee/.git/
    $ cd calleee
    # activate/create your virtualenv if necessary
    $ python setup.py develop
    ...
    Finished processing dependencies for calleee

The second approach is adequate if you want to use some feature of the library that hasn't made it to a PyPI release yet
but don't need to make your own modifications. You can tell *pip* to pull the library directly from its Git repository:

.. code-block:: shell

    # activate/create your virtualenv if necessary
    $ pip install git+https://github.com/untidy-hair/calleee.git#egg=calleee
