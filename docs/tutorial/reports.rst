Reports
=======

A report is the ultimate thing we're after. A report is an abstraction over an
entire file. Important assumptions for the library to work and be usable are as
follows:

* The file is fixed size per line
* Each individual line can be inetpreted as a record

Also, you should take of encoding, since this may cause problems, if you badly
interpret unicode in ascii string for example. In that case, even if your
positions look right, you may get ValidationError errors.

.. warning:: Be sure that you are correctly loading the file with proper
    encoding!

A report is a custom class, that uses Record classes for it's assembly.

Basic Construction
------------------

Okay, so now you have a export file that you want to parse. Let's use our
example with ``hex`` nad ``header`` records from the previous chapter, and
build a parser for this "file"::

    140931123225tomas.plesek
    #12aacc bluish


For this, we create a report::

    from pybankreader import reports

    class ColorReport(reports.Report):
        header = HexNameRecord()
        color = ColorRecord()

Make sure that you're instantiating objects in the record definitions!
Otherwise, all hell will break loose

Now, when you're ready, you can load your data. Let's presume that our file is
named ``color_file.txt``::

    with open('color_file.txt', 'r') as fl:
        report = ColorReport(fl)

        print report.header.user_name

    >>> "tomas.plesek"

        print report.header.export_date
    >>> datetime.datetime(2014, 9, 31, 12, 32, 25)

        print report.color.color_name
    >>> "bluish"


Easy. Now, what if we would have our original file like this?::

    140931123225tomas.plesek
    #12aacc bluish
    #e50f2c redish
    #6ff660 greenish


Our report will still work, but you will get the same results as last time,
with the difference that the color would be the last record line ('greenish'),
since it's the last in the file. So how do we get around that? We use
:py:class:`pybankreader.reports.CompoundRecord`::

    class ColorReport(reports.Report)
        header = HexNameRecord()
        data = CompoundRecord(ColorRecord)


Now, with this, you can now access your data like this::

    report = ColorReport(fl)
    print report.header.user_name
    >>> "tomas.plesek"

    for color in report.data:
        print color.color_name

    >>> "bluish"
    >>> "redish"
    >>> "greenish"


In this manner, you can also take care of situations, where you have multiple
types of records, that are repeating::

    140931123225tomas.plesek
    #12aacc bluish
    140931123225tomas.plesek
    #e50f2c redish
    #6ff660 greenish

In this case, the report would look like this::

    class ColorReport(reports.Report)
        data = CompoundRecord(ColorRecord, HexNameRecord)

Now the library is able to pass everything as a sequence.

Advancement Hinting
-------------------
There are rather unfortunate situations, when the library gets confused as to
whether it's on another record type. Imagine the situation, where you would
have two records like this::

    class CharRecord(Record):

        name = fields.CharField(length=10, required=True)


    class FooterRecord(Record)

        footer = fields.RegexField(
            length=10, required=True, regex="AAAAZZAAAA"
        )

Now you create a report out of these like it's obvious::

    class MyReport(Report):

        name = CharRecord()
        footer = FooterRecord()


And you try to read this file::

    john
    AAAAZZAAAAA

What happens? You will have the string``AAAAZZAAAA` in the report.name.name
field and the footer will not have been loaded. Why? Because the footer is
parsed by the CharRecord, since it fits within it's constraints. To go around
this, you have two options. Either update your recrods such that they're more
strict, or you can use so called "advancement hinting".

Each report has set of default methods named ``hint_<record>`` that return
always True. So in your example, there are two methods automatically defined
for you:

    * hint_name(self, line)
    * hint_footer(self, line)

Now, whenever such method would return false, it will tell the library to stop
processing the current line as given record, and try the next one. Note that
the method receives single ``line`` parameter. This is the raw string read from
the source file. In our example, we would solve the problem by overriding the
``hint_name`` method, like this::

    def hint_name(self, line):
        return False if line == "AAAAZZAAAA" else True

And now the report will get parsed successfully.

Custom Processing
-----------------
