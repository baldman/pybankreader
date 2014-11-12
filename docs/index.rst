Welcome to Pybankreader's documentation!
========================================

The `pybankreader` library is a toolkit to create model-based representation of
structured exported plain-text files.

The initial intention is to be able to load various exported repors, that you
get from internet banking applications.

Currently, there are two formats supported: GPC and BBF. However, as the
library was designed with generic application in mind, it's very easy to add
additional formats.

The data-format that the library expects is a text file, that is structured,
with one line per record (however, you can have any number of different records
in such a file). Together, individual records form a report. All of this is
handled transparently, so in the end, you can do something super-easy like
this::

 report = MyReport(initial_data=file_like)
 for x in report.data:
    x.name
    x.surname

You will find more information about how to use this library in the docs below.

Contents:

.. toctree::
   :maxdepth: 2

   tutorial/index
   api/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

