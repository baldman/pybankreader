import pytest
import six
from pybankreader import fields
from pybankreader.exceptions import ValidationError
from pybankreader.records import Record, FieldProxy


class TestRecord(Record):
    """
    A test class that uses `BaseRecord`, therefore having the metaclass magic
    available
    """

    first_field = fields.CharField(length=2, required=True)
    second_field = fields.IntegerField(length=4, required=True)


class TestRecord2(Record):
    """
    A test class that uses `BaseRecord`, therefore having the metaclass magic
    available. Also, note that we do NOT want inheritance, since we have to
    test class-level attributes descriptor
    """

    first_field = fields.CharField(length=2, required=True)
    second_field = fields.IntegerField(length=4, required=True)


def test_fields_available():
    """
    Test that the metaclass does it's thing
    """
    # The test record
    record = TestRecord()

    # Filter out private attributes
    flds = {
        key: val for (key, val) in six.iteritems(record.__class__.__dict__)
        if not key.startswith('_')
    }

    # Test that fields are loaded
    assert len(flds) == 2

    # Check for proper types
    for name, field in six.iteritems(flds):
        assert not isinstance(field, fields.Field)
        assert isinstance(field, FieldProxy)
        assert field._field_obj in record._fields

    # Assert we have defaults
    assert record.first_field is None
    assert record.second_field is None


def test_descriptor_proxy():
    """
    Test that the descriptor is properly "installed" in the class
    """
    # The test record
    record = TestRecord()

    # This must raise exception, since we're inputting wrong data
    with pytest.raises(ValidationError):
        record.first_field = 'AAAA'

    # Test assignment
    record.first_field = 'AA'
    assert record.first_field == 'AA'

    record.second_field = '123'
    assert record.second_field == 123


def test_descriptor_clash():
    """
    Test that the descriptor does not clash between different instances
    """
    record1 = TestRecord()
    record2 = TestRecord2()

    assert record1.first_field is None

    record1.second_field = '123'
    record2.second_field = '345'

    assert record1.second_field == 123
    assert record2.second_field == 345

    record1.second_field = '123'

    assert record1.second_field == 123
    assert record2.second_field == 345


def test_record_load():
    """
    Test the ability of the record instance to load data properly
    """
    record = TestRecord()

    # Default load
    assert record.first_field is None
    assert record.second_field is None

    # Valid load
    value = 'AA1234'
    record.load(value)

    # Invalid load
    value = 'whatever'
    with pytest.raises(ValidationError):
        record.load(value)

    # Test that previous values remain after failed validation
    assert record.first_field == 'AA'
    assert record.second_field == 1234
