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


GPC
---