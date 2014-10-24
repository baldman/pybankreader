class ValidationError(Exception):
    """
    Simple exception for field-level validation errors
    """

    field = None
    message = None

    def __init__(self, field, message):
        self.field = field
        self.message = message

    def __str__(self):
        return "{}: {}".format(self.field, self.message)


class InvalidRecordError(Exception):
    """
    Exception wrapping the situation
    """

    position = None
    record = None

    def __init__(self, position, record, field):
        pass