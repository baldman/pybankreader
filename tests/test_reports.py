from six import StringIO
from pybankreader import fields, records
from pybankreader import reports


class TestRecord(records.Record):
    """
    First mock record
    """

    first = fields.CharField(length=2, required=True)
    second = fields.IntegerField(length=4, required=True)


class TestRecord2(records.Record):
    """
    Second mock record
    """

    third = fields.CharField(length=2, required=True)
    fourth = fields.IntegerField(length=4, required=True)


class TestRecord3(records.Record):
    """
    Third mock record
    """

    fifth = fields.CharField(length=10, required=True)


class BareTestReport(reports.Report):
    """
    The test report
    """

    header = TestRecord()
    data = reports.CompoundRecord(TestRecord3)
    footer = TestRecord2()

    def hint_data(self, line):
        """
        On a record that starts with ZZ, we hint that the we must advance with
        the internal record pointer.
        """
        return False if line.startswith('ZZ') else True


def test_default_values():
    """
    Test that the report class is properly initialized
    """
    report = BareTestReport()
    # Test default values
    assert report.data == []
    assert report.header is None
    assert report.footer is None
    # Test methods created
    assert callable(report.process_header)
    assert callable(report.process_footer)
    assert callable(report.process_data)
    assert callable(report.hint_header)
    assert callable(report.hint_footer)
    assert callable(report.hint_data)


def test_list_clash():
    """
    We don't want to poison class namespace with mutable objects...
    """

    report = BareTestReport()
    report2 = BareTestReport()
    report.data.append("whatever")

    assert BareTestReport.data is None
    assert report.data == ['whatever']
    assert report2.data == []


def test_load(mock_report):
    """
    Test we can successfully load a data set into a report
    """
    file_like = StringIO(mock_report)
    report = BareTestReport(file_like=file_like)

    # Header field
    assert isinstance(report.header, TestRecord)
    assert report.header.first == 'AB'
    assert report.header.second == 1234

    # Data field
    assert isinstance(report.data, list)
    assert len(report.data) == 2
    assert report.data[0].fifth == 'first'
    assert report.data[1].fifth == 'second'

    # Footer field
    assert isinstance(report.footer, TestRecord2)
    assert report.footer.third == 'ZZ'
    assert report.footer.fourth == 9911
