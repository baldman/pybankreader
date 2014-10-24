import six
from pybankreader.fields import Field


class FieldProxy(object):
    """
    A decriptor class for fields. This essentially creates a proxy to
    attributes. Beware of weird class-level like behavior of descriptors
    """

    _field_obj = None
    """
    The actual field object we're proxying to
    """

    _data = None
    """
    Dictionary of instance->value map
    """

    def __init__(self, field_obj):
        """
        Initialize the decriptor with pointer to the obejct.

        :param Field field_obj: The actual field object we're proxying to
        :return:
        """
        self._field_obj = field_obj
        self._data = {}

    def __get__(self, instance, owner):
        """
        Fetch the actual value from the data dictionary
        """
        return self._data.get(instance, None)

    def __set__(self, instance, value):
        """
        Use the field object to normalize the input and save it
        """
        self._field_obj.value = value
        self._data[instance] = self._field_obj.value


class RecordBase(type):
    """
    The record metaclass. Mainly sets up Field proxy descriptors on Field
    instances (class attributes)
    """

    def __new__(mcs, klazz, bases, attrs):
        """
        The metaclass method

        :return: class
        """
        # Do this only on subclasses of BaseRecord
        parents = [b for b in bases if isinstance(b, RecordBase)]
        if not parents:
            # It's something else, so go ahead
            return super(RecordBase, mcs).__new__(mcs, klazz, bases, attrs)

        # Do our magic with fields
        for name, field_obj in six.iteritems(attrs):
            if isinstance(field_obj, Field):
                attrs.pop(name)
                field_obj.field_name = name
                attrs[name] = FieldProxy(field_obj)

        klazz_inst = super(RecordBase, mcs).__new__(mcs, klazz, bases, attrs)
        return klazz_inst


class Record(six.with_metaclass(RecordBase)):
    """
    The base Record class. Any record definition should use this one, since
    it allows for the smooth definition via class attributes and adds some
    facade methods to load those records
    """

    def __init__(self):
        pass
