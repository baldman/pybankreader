import datetime
from decimal import Decimal
import pytest
from pybankreader.exceptions import ValidationError
from pybankreader.fields import Field, IntegerField, CharField, RegexField, \
    TimestampField, DecimalField


def _generic_field_test(field_instance, ok_value, long_value, set_value=None):
    """
    As any field is based on the Field class, this can test the same basic
    behavior for all subclases

    :param Field field_instance: instance of a Field subclass
    :param string ok_value: value that should pass validation
    :param string long_value: value that is longer than allowed
    :param string set_value: value that should pass validation and be set
        instead of ok_value, since the value may be re-cast by the field
    :return:
    """
    field_instance.field_name = 'test_field'
    empty_value = ''

    # Test long value
    with pytest.raises(ValidationError) as e:
        field_instance.value = long_value

    assert e.value.field == "test_field"
    exp_message = "Value '{}' exceeds maximum length of {}". \
        format(long_value, field_instance.length)
    assert e.value.message == exp_message

    # Test ok value and non-required field value
    if set_value:
        field_instance.value = set_value
    else:
        field_instance.value = ok_value
    assert str(field_instance.value) == ok_value

    field_instance.value = empty_value
    assert field_instance.value is None

    # Test required field
    field_instance.required = True
    with pytest.raises(ValidationError) as e:
        field_instance.value = empty_value
    assert e.value.field == 'test_field'
    exp_message = "A value is required for this field"
    assert e.value.message == exp_message


def test_base_field():
    fld = Field(length=6, required=False)
    _generic_field_test(fld, "haha", "hahahaha")


def test_char_field():
    fld = CharField(length=6, required=False)
    _generic_field_test(fld, "haha", "hahahaha")


def test_regex_field():
    fld = RegexField('^0 1[a-f]+$', length=5, required=False)
    _generic_field_test(fld, '0 1ae', '0 1aefaea')
    with pytest.raises(ValidationError) as e:
        fld.value = '0 1az'
    assert e.value.field == 'test_field'
    msg = "Value '{}' does not match the regex pattern '{}'".format(
        '0 1az', fld._regex
    )
    assert e.value.message == msg


def test_integer_field():
    fld = IntegerField(length=3, required=False)
    _generic_field_test(fld, '19', '1999')
    fld.value = '-19'
    assert fld.value == -19


def test_decimal_field():
    fld = DecimalField(length=6, required=False)
    _generic_field_test(fld, '13.54', '1234.56')
    fld.value = '13.54'
    assert fld.value == Decimal('13.54')
    fld.value = '-13.54'
    assert fld.value == Decimal('-13.54')


def test_timestamp_field():
    fld = TimestampField("%y%m%d%H%M%S", length=12, required=False)

    ok_value = str(datetime.datetime(
        year=2014, month=9, day=2, hour=7, minute=9, second=22
    ))

    _generic_field_test(fld, ok_value, '1409020709222', '140902070922')
    with pytest.raises(ValidationError) as e:
        fld.value = "whatever"
    assert e.value.field == 'test_field'
    msg = "Value 'whatever' cannot be parsed to date using format " \
          "'%y%m%d%H%M%S'. Error is: time data 'whatever' does not match " \
          "format '%y%m%d%H%M%S'"
    assert e.value.message == msg
