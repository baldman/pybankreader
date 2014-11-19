Pybankreader
============

License
    BSD
Python Compatibility
    Python 2.7 & Python 3.4

What Is It
----------
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

How to Get It
-------------

Two options:

 * Use ``pip``: ``pip install pybankreader``
 * Or clone from Github if you want to: ``git clone https://github.com/baldman/pybankreader.git``

What Is the Projects Status
---------------------------

I'd say that library is in something like limited production use.

Currently, the library is capable of what it was initially intended to do, and
that is to read two bank formats:

 * GPC (v2)
 * BBF (not FINSTA records)

If needed, other formats will follow.

Mind that only one datasource was used for testing: CSOB a.s. If problems
arise, fill an issue and ideally, attach data that does not work with this.

On top of that, it's very simple to create your own custom records and reports,
since there is a un-healthy abundancy for bank export formats (see the docs for
that).

Where Is the Documentation
--------------------------
http://pybankreader.readthedocs.org/, read the docs of course.