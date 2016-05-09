from datetime import datetime
from decimal import Decimal
import re
from .exceptions import ValidationError


class Field(object):
    """
    Basic field superclass. We have mandatory length and required flags, and we
    hold the set value (if any). Also, the name of the field as defined in
    classes using these for reference reasons.
    """

    _creation_counter = 0

    _field_name = None
    _value = None
    _position = None

    length = None
    required = None

    def __init__(self, length, required):
        """
        Initialize the field and maintain the creation counter so we don't have
        to pass position argument

        :param int length: maximum length of the field
        :param bool required: field is required
        """
        # We set the position from the static attribute, since otherwise, we
        # would not have a way how to fetch the instance one
        self._position = Field._creation_counter
        Field._creation_counter += 1

        self.length = length
        self.required = required

    def __lt__(self, other):
        """
        Compare with other fields by position

        :param other: Field
        :return bool: True if self < other, False if self > other
        :raises RuntimeError: self == other (which should not ever happen)
        """
        if self._position == other._position:
            msg = "You cannot have two fields with the same position"
            raise RuntimeError(msg)

        return self._position < other._position

    def _set_value(self, value):
        """
        When the value is being set, we run validations!

        :param value: The value to be stored in the field
        :raises ValidationError: Value is not valid
        """
        value = value.strip()
        if self.required and not len(value):
            raise ValidationError(
                self._field_name, "A value is required for this field"
            )

        if len(value) > self.length:
            msg = u"Value '{}' exceeds maximum length of {}".format(
                value, self.length
            )
            raise ValidationError(self._field_name, msg)

        self._value = value if len(value) else None

    @property
    def value(self):
        """
        Just return the value, nothing special here

        :return: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Setter for the value. Uses inner method, since setters cannot call
        super in subclasses.

        :param value: The value to be stored in the field
        :raises ValidationError: Value is not valid
        """
        self._set_value(value)

    @property
    def field_name(self):
        """
        Return the name of the field it has been assigned to

        :return string: name of the field
        """
        return self._field_name

    @field_name.setter
    def field_name(self, value):
        """
        Sets the name of the field. If that has already been done, raises
        RuntimeError

        :param string value: name of the field
        :raises RuntimeError: you're trying to reassign the field name
        """
        if self._field_name:
            raise RuntimeError("You cannot reassign field name once it's set")
        self._field_name = value


class CharField(Field):
    """
    CharField just uses the Field superclass directly for now, nothing special
    """
    pass


class RegexField(Field):
    """
    Generic regex field. On top of basic checks, enforces a regex match
    """

    _regex = None

    def __init__(self, regex, *args, **kwargs):
        """
        Initialize the field

        :param regex: regular expression that the value is matched against
        :param list args: args
        :param dict kwargs: kwargs
        :return:
        """
        self._regex = regex
        super(RegexField, self).__init__(*args, **kwargs)

    def _set_value(self, value):
        """
        Setter for the value.

        :param strin value: The value to be stored in the field
        :raises ValidationError: Value is not valid
        """
        super(RegexField, self)._set_value(value)
        if self._value is None:
            return

        if re.match(self._regex, value) is None:
            msg = u"Value '{}' does not match the regex pattern '{}'".format(
                value, self._regex
            )
            self._value = None
            raise ValidationError(self._field_name, msg)


class IntegerField(RegexField):
    """
    Integer is just a special-case regex, so the field is implemented this way
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the parent RegexField with integer regex

        :param list args: args
        :param dict kwargs: kwargs
        """
        super(IntegerField, self).__init__("^\s*-?\d+\s*$", *args, **kwargs)

    def _set_value(self, value):
        """
        Setter for the value, typecasts to integer

        :param string value: The value to be stored in the field
        :raises ValidationError: Value is not valid
        """
        super(IntegerField, self)._set_value(value)
        if self._value is None:
            return
        self._value = int(self._value)


class DecimalField(RegexField):
    """
    Decimal is just a special-case regex, so the field is implemented this way.
    Mind that when you're using decimal, the overall length of the field must
    count with the decimal dot!
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the parent RegexField with integer regex

        :param list args: args
        :param dict kwargs: kwargs
        """
        super(DecimalField, self).__init__(
            "^\s*-?\d+(\.\d+)?\s*$", *args, **kwargs
        )

    def _set_value(self, value):
        """
        Setter for the value, creates a Decimal object

        :param string value: The value to be stored in the field
        :raises ValidationError: Value is not valid
        """
        super(DecimalField, self)._set_value(value)
        if self._value is None:
            return
        self._value = Decimal(self._value)


class TimestampField(Field):
    """
    Timestamp field takes on `format` parameter to be fed into `strptime`
    """

    _format = None

    def __init__(self, format, *args, **kwargs):
        """
        Initialize the field with datetime format mask

        :param format: datetime format mask that ``datetime.strptime`` can
            parse
        :param list args: args
        :param dict kwargs: kwargs
        :return:
        """
        super(TimestampField, self).__init__(*args, **kwargs)
        self._format = format

    def _set_value(self, value):
        """
        Setter for the value, parses the input to datetime object
        """
        super(TimestampField, self)._set_value(value)
        if self._value is None:
            return
        try:
            self._value = datetime.strptime(value, self._format)
        except ValueError as e:
            if not self.required:
                self._value = None
            else:
                msg = u"Value '{}' cannot be parsed to date using format '{}'. " \
                      u"Error is: {}".format(value, self._format, str(e))
                raise ValidationError(self._field_name, msg)