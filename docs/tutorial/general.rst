Introduction
============

Pybankreader is actually two things in one:

 * rather generic structured text parser
 * implementation of select bank reports

This section is about the first part mainly, but it will also help you with
understanding how things work so you can use the existing reports easily.

First, let's introduce 3 main concepts, to be discussed later. The library uses
three distinct abstractions that build one on each other:


report
    The most high-level abstraction, representing usually one data file parsed
    by the library and loaded into memory. A report is constructed of multiple
    records, one record == one line in the file

record
    Is a abstraction over a line of data (in a file or string, provided it's
    delimited by ``\n`` characters. A record consists of multiple fields, that
    are taken sequentialy from the start of the string to the end.

field
    Represents basically a byte range in the record line with type and \
    therefore automatic conversion to that type. A field would be for instance
    a :py:class:`pybankreader.fields.TimestampField`


Now, whenever you want to use a report, you now know that it consist of a
number of records, which themselves parse the data to fields. What does that
mean is that you would usually invoke a report like this::

    import pybankreader

    with open('/file/path', 'r') as file:
        # Create the report instance, using one of the implemented reports
        report = pybankreader.GPCAccount(file)


    # Look and the record 'header' and print the value of field 'consumer_name'
    print report.header.consumer_name
    >>> "John Doe"

    for x in report.data:
       print x.ammount
    >>> 1546


And that is really all there is to it!