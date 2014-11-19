Welcome to Pybankreader's documentation!
========================================

The `pybankreader` library is a toolkit to create model-based representation of
structured exported plain-text files.

The initial intention is to be able to load various exported repors, that you
get from internet banking applications.

Currently, there are two formats supported in the library itself, on top of the
framework for rolling your own: GPC and BBF. However, as stated, the library
was designed with generic application in mind, it's very easy to add additional
formats.

The data-format that the library expects is a text file, that is structured,
with one line per record (however, you can have any number of different records
in such a file). Together, individual records form a report. All of this is
handled transparently, so in the end, you can do something super-easy like
this (``report.custom_record`` and ``report.data`` are fields defined by a
report, not the library itself)::

 report = MyReport(initial_data=file_like)
 name_of_report = report.custom_record.name
 for x in report.data:
    x.name
    x.surname

You will find more information about how to use this library in the docs.

You can get the library as a package from PyPI or source from Github:

 * Using ``pip``: ``pip install pybankreader``
 * Source from Github: ``git clone https://github.com/baldman/pybankreader.git``

Contents:

.. toctree::
   :maxdepth: 2

   tutorial/index
   formats/index
   api/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

