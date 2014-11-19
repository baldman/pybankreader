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
        print report.header.export_date
        print report.color.color_name

... which produces this output::

    "tomas.plesek"
    datetime.datetime(2014, 9, 31, 12, 32, 25)
    "bluish"

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

    for color in report.data:
        print color.color_name

... which produces this outout::

    >>> "tomas.plesek"
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

.. _advancement-hinting:

Validation Errors
-----------------
Of course, you will hit a situation where either the data does not conform to
your defined report, or you made a mistake when you constructed either the
report or individual records.

In such a case, instance of :py:exc:`pybankreader.exceptions.ValidationError`
will be thrown. To make the debugging easier, the validation does have a nice
``__str__`` method, that will print a wider context for you to debug, like so::

    ValidationError: header @ <0,3>: Value 'T26' does not match the regex pattern '079' for data: T263310  HEADER 0001.0000BBCSOB
    [0] >>> AccountRecord/header @ <0,3>: Value 'T26' does not match the regex pattern '074'
    [1] >>> ItemRecord/header @ <0,3>: Value 'T26' does not match the regex pattern '075'
    [2] >>> ItemInfoRecord/header @ <0,3>: Value 'T26' does not match the regex pattern '076'
    [3] >>> ItemRemittance1Record/header @ <0,3>: Value 'T26' does not match the regex pattern '078'
    [4] >>> ItemRemittance2Record/header @ <0,3>: Value 'T26' does not match the regex pattern '079'


This should give you enough information to hunt down the problem. The first
line is the last ValidationError that occured. The format is to be interpreted
as such::

 field_name @ <start_position,end_position>: 'Exception_message' for data: line_of_data_tried_to_be_loaded_into_a_record

You may stumble upon situations, as in our example, when there is a followup
printout of successive validation errors. This is to get you to the underlying
problem, because the system tries all record types in a report sequentially,
until it gives up. So, if the problem is in the first record, the system will
still complain about the *last* one, since that's where it finally decided it
cannot parse the source.

This stack is reset once every succesfull parsing of a record.


.. note:: The error message will be the *last* in the numbered stack trace, so
    in the example case, it's number 4.

Advancement Hinting
-------------------
There are rather unfortunate situations, when the library gets confused as to
whether it's on another record type. Imagine the situation, where you would
have two records like this::

    from pybankreader.records import Record
    from pybankreader import fields

    class CharRecord(Record):
        name = fields.CharField(length=10, required=True)


    class FooterRecord(Record)
        footer = fields.RegexField(length=10, required=True, regex="AAAAZZAAAA")

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

The last nice feature of pybankreader is the ability to custom-process data as
they're being parsed. This way, you can build complex parsed structures in
memory if you want to.

The best example would we a situation, where your data is either hierarchical
(yet presented in a linear fashion as multiple records), or multi-line. You
will still represent each line "type" as an individual record, but you have
the option to change, how the data is saved.

First, in a similar vein as :ref:`advancement-hinting`, there is a set of
default methods called ``process_<record>``. What these do is that they take a
parsed record and return it, nothing more. You are free to override those
methods and change the behavior. You can obviously do whatever you need with
the processed record, and you can either return an object
(or the record itself), if you wish it to be loaded in the ``report.record``
field, or you may return ``None`` and therefore, the record will **not** be
saved in the report.

So to go with an example using our colors, let's have a file like this::

    140931123225tomas.plesek
    #12aacc bluish
    #e50f2c redish


Suppose now that those two colors are not single colors, but they represent a
gradient together. How do we create a report for this?::

    class GradientReport(Report):

        header = HexNameRecord()
        data = CompoundRecord(ColorRecord)

        ticktock = True
        """
        This is a custom field. Since it's not a record, the libary will
        leave it alone
        """

        def process_data(self, record)
            """
            Just a stupid method of how to populate a custom class. Note
            that we're returning that custom class, not the ColorRecord!
            """
            if ticktock:
                gradient = Gradient()
                gradient.start = record
                ticktock = False
                return gradient
            else:
                self.data[-1].end = record
                ticktock = True
                return None

    class Gradient(object):

        start = None
        end = None

        def __str__(self):
            print("{} -> {}".format(
                self.start.hex_color, self.end_hex_color
            )

Okay, and now if you do this::

    report = GradientReport(file_like)
    for x in data:
        print(x)
        print(type(x))

You will get::

    "#12aacc -> #e50f2c"
    <class pybankreader.examples.Gradient>

Neat, huh?