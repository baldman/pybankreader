import inspect
import six

from .records import Record
from . import exceptions


class CompoundRecord(Record):
    """
    A wrapper for a record field that represents a list of records and possibly
    of multiple types of records. This is mainly required to control the
    position of individual record attributes in the given report.
    """

    _records = None
    _record_iter = 0

    _data = None

    def __init__(self, *args):
        """
        Same the records as a list

        :param list args: individual record types
        """
        super(CompoundRecord, self).__init__()
        self._records = args
        self._data = []

    def advance(self):
        try:
            self._records[self._record_iter+1]
        except IndexError:
            return False
        else:
            self._record_iter += 1
            return True

    def reset(self):
        self._record_iter = 0

    def get_record(self):
        return self._records[self._record_iter]()


class ReportBase(type):
    """
    The metaclass responsible for creating `hint_<record>` and
    `process_<record>` fields, as well as instantiating those in correct order
    and mapping them onto a Report instance.
    """

    def __new__(mcs, klazz, bases, attrs):
        # Do this only on subclasses of Report
        parents = [b for b in bases if isinstance(b, ReportBase)]
        if not parents:
            # It's something else, so go ahead
            return super(ReportBase, mcs).__new__(mcs, klazz, bases, attrs)

        # The filter for weeding out things that don't interest us
        def filter_records(x):
            """
            Filter out things that are not record fields. This applies to
            litst, that have instances of something else than Record
            """
            if isinstance(x[1], Record):
                return True
            if isinstance(x[1], list):
                for x in x[1]:
                    if not inspect.isclass(x) or not issubclass(x, Record):
                        return False
                return True
            return False

        real_attrs = filter(filter_records, six.iteritems(attrs))

        # Prepare the stub for `process_<field>_` methods
        def _process_stub(self, record):
            """
            Default process method just returning the record back

            :return Record: the record
            """
            return record

        # Add hint methods, so they can indicate that a field should advance
        def _field_hint(self, line):
            """
            Default hint method always returning True

            :return bool: Always True
            """
            return True

        methods = {}
        record_list = []
        records = {}

        for name, record_klazz in sorted(real_attrs, key=lambda x: x[1]):
            attrs.pop(name)
            methods["process_{}".format(name)] = _process_stub
            methods["hint_{}".format(name)] = _field_hint
            records[name] = record_klazz
            attrs[name] = None
            record_list.append(name)

        # Check that we have at least one record
        if not len(record_list):
            msg = "Your report '{}' must have at least one record". \
                format(klazz)

            raise exceptions.ConfigurationError(msg)

        # Create the class isntance
        klazz_inst = super(ReportBase, mcs).__new__(mcs, klazz, bases, attrs)

        # Add `process` and `hint` methods, if they're not defined
        for name, pointer in six.iteritems(methods):
            if not hasattr(klazz_inst, name):
                setattr(klazz_inst, name, pointer)

        # Add the assembled records
        setattr(klazz_inst, '_record_map', records)
        setattr(klazz_inst, '_record_list', record_list)
        return klazz_inst


class Report(six.with_metaclass(ReportBase, object)):

    _last_exception = None
    """
    This stores history of exceptions, so we can trace the error more
    accurately
    """

    data = None
    """
    The actual data field. All reports will have at least this one defined.
    """

    def __init__(self, file_like=None):
        """
        The constructor handles initialization of any list fields, that may be
        defined. Optionally, it can take the file-like to read from directly

        :param file_like: the file from which to read data
        """
        for key, record_klazz in six.iteritems(self._record_map):
            if isinstance(record_klazz, CompoundRecord):
                # Do not forget to reset bailed imports!
                record_klazz.reset()

        # If no data field is defined, make it a list anyway
        self.data = self.data or []
        if file_like:
            self.load(file_like)

    def load(self, file_like):
        """
        Read individual records and assign them to proper instance fields, as
        they go. When the system cannot parse a record, we advance to the next
        record type first, before we raise an exception indicating that the
        report is invalid.
        """
        curr_record_idx = 0
        while True:
            line = file_like.readline()
            if not line:
                break

            # We need to handle the iteration of the record classes
            while True:
                curr_record = self._record_list[curr_record_idx]
                record_obj = self._record_map[curr_record]
                is_list = isinstance(record_obj, CompoundRecord)
                if is_list:
                    compound_record = record_obj
                    record_obj = record_obj.get_record()
                try:
                    # First, check the hint method
                    okay = getattr(self, 'hint_{}'.format(curr_record))(line)

                    # The hint tells us, that we need to advance, so let's do
                    # that by raising ValidationError directly
                    if not okay:
                        msg = "{} hint says that I should advance".\
                            format(curr_record)
                        raise exceptions.ValidationError(
                            '__hint__', msg
                        )
                    record_obj.load(line.strip())
                except exceptions.ValidationError as val_error:
                    # Save the exception...
                    if self._last_exception:
                        val_error.parent = self._last_exception
                    self._last_exception = val_error

                    # And continue about our business
                    try:
                        if is_list and compound_record.advance():
                            # Okay, we may just need to switch to different
                            # record type in the compound record
                            continue
                        else:
                            self._record_list[curr_record_idx+1]
                    except IndexError:
                        # Nope, this is the end and we're out of here
                        raise val_error
                    else:
                        # Okay, there is hope, since there is another record
                        # in the record list
                        curr_record_idx += 1
                else:
                    break

            # Clear exception stack
            self._last_exception = None

            # Process hook
            process_method = getattr(self, 'process_{}'.format(curr_record))
            processed = process_method(record_obj)
            if processed is None:
                if is_list:
                    compound_record.reset()
                continue

            # If the datum is supposed to be in a list, we need to put it there
            # as such. Otherwise, just set the attribute
            if is_list:
                data_list = getattr(self, curr_record)
                data_list.append(processed)
                # The order of records in compound record is non-linear
                compound_record.reset()
            else:
                setattr(self, curr_record, processed)
