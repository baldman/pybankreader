Reports Implemented in Pybankreader
===================================

Currently, the library implements two formats that are tested and work:

* BBF (Only remittance advice report)
* GPC (version 2)

You can use them by importing them from the library directly::

    from pybankreader import BBFAdvmul, GPCAccount


I will briefly touch on individual reports, but in general, since this is
modelled based on only one data source (CSOB a.s.), you should read the
official documentation for fields here_.

.. _here: http://www.csob.cz/WebCsob/Lide/Elektronicke-bankovnictvi/BB/CSOB_BB24_Formaty.zip

BBF
---

.. note:: This report **does not** use record processing

The BBF format has two basic categories. Advmul/Advmuz records for remittance
advices and such, and Finsta records for transactions. Currently, the report
supports only Advmul/Advmuz records in a single report calld ``BBFAdvmul``

The report is defined as such::


    class AdvmulReport(Report):
        header = HeaderRecord()
        data = CompoundRecord(AdvmulHeaderRecord, AdvmulRecord, AdvmuzRecord)
        lock = LockRecord()

``header`` and ``lock`` records contain some metadata, whereas the ``data``
list contains individual records. See
:py:mod:`pybankreader.formats.bbf.records` for detailed list of fields
available on each of those records and consult official field description from
the vendor.


GPC
---

.. note:: This report **does** use record processing


The GPC report is rather simplistic, it represents a transaction on an account.
Mind that you can have more than one account in the file. Also, one transaction
record can have up to 3 different additional records bound to them. Therefore,
this report uses recor processing to recreate this hierarchy in memory.

The report is defined as such::

    class AccountReport(Report):

        data = CompoundRecord(AccountRecord, ItemRecord, ItemInfoRecord,
                              ItemRemittance1Record, ItemRemittance2Record)

You can see that this report has everything in multiple occurences, so, we use
the ``process_data`` method to split it such that we have this hierarchy on the
``AccountReport`` instance::


    data[] <-- a list of Account objects (proxy to AccountRecord)
      - item  <-- AccountItem obejct (proxy to ItemRecord)
        - info <-- ItemInfoRecord
        - rem1 <-- ItemRemittance1Record
        - rem2 <-- ItemRemittance2Record
      - item
        - info
        - rem1
        - rem2
      - item
        - info
        - rem1
        - rem2


Since both ``Account`` and ``AccountItem`` classes use
:py:class:`pybankreader.utils.ProxyMixin` to proxy the access to their internal
records, you can still use the dot syntax to access their fields, like this::

    for account in report.data:
        print account.new_balance
        for transaction in account.items:
            print trasaction.amount
            # Accessing ItemInfoRecord...
            print transaction.info.date


See :py:mod:`pybankreader.formats.gpc.records` for detailed list of fields
available on each of those records and consult official field description from
the vendor.