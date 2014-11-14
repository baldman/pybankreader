Records
=======

A record represents one line in the document that the library is parsing. As
such, it does not make sense to have a 'built-in' records (apart from those
in the library reports).

.. note:: Currently, the library supports only fixed-length fields.

In records, you just define fields. You should not need to override anything
in the Record class. So without further ado, let's look at an example::

    class HexNameRecord(Record):
        hex_color = HexField(required=True, length=7)
        separator = CharField(required=False, length=1)
        color_name = CharField(rquired=True, length=10)


This records would then be able to parse a line of text like this::

    #12aacc bluish

Note that we used the `HexField` from our custom field example. Also, it's
obvious that the `HexField` should probably be defined with the length fixed.

One important thing to observe is that we're naming our fields by defining them
as attributes. Also, we're determining their position. This is important, since
that is how the library can figure out, which part on the line to read. To
really drive this home:

.. warning:: Position of the fields determines the byte range, where the field
    will look for it's data!



Let's have another record, that we'll use in reports later on, for header
information::

    class HeaderRecord(Record):
        export_date = TimestampField(required=True, length=12,"%y%m%d%h%M%s")
        user_name = CharField(required=True, length=130)


And this is basically all you need to know about records. They're very simple
to define and compact. Now, the meaty part is the next topic, which is building
entire reports.