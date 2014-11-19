class ValidationError(Exception):
    """
    Simple exception for field-level validation errors
    """

    data = None
    """
    One line of data, if available, that a record tried to load
    """

    record = None
    """
    The record class name, where the error occured
    """

    field = None
    """
    The field which raised the exception
    """

    message = None
    """
    Exception message
    """

    interval = (0, 0)
    """
    Interval in the source data string, that the field tried to parse in the
    format of a tuple (start, end)
    """

    parent = None
    """
    Optional pointer to previous ValidationError exception, as the parser
    progressed through the data and was trying sucessive records/fields.
    """

    def __init__(self, field, message):
        self.field = field
        self.message = message

    def __str__(self):
        """
        Display the exception with an enhanced context information
        """
        exc_stack = []
        current = self
        while True:
            exc_stack.append(current)
            if current.parent:
                current = current.parent
            else:
                break

        red_message = u"{} @ <{},{}>: {} for data: {}\n".format(
            self.field, self.interval[0], self.interval[1], self.message,
            self.data
        )
        for no, exc in enumerate(reversed(exc_stack)):
            start, end = exc.interval
            red_message += u"[{}] >>> {}/{} @ <{},{}>: {}\n".format(
                no, exc.record, exc.field, start, end, exc.message
            )
        return red_message


class ConfigurationError(Exception):
    """
    Exception signifies a programmers error in setting up the reports
    """