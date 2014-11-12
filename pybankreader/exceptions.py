class ValidationError(Exception):
    """
    Simple exception for field-level validation errors
    """

    field = None
    message = None
    context = None

    def __init__(self, field, message):
        self.field = field
        self.message = message

    def __str__(self):
        return "{}: {}\nCONTEXT: {}".format(self.field, self.message,
                                            self.context)


class ConfigurationError(Exception):
    """
    Exception signifies a programmers error in setting up the reports
    """