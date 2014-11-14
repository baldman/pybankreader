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

