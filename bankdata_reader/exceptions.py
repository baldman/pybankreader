class ValidationError(Exception):
    """
    Simple exception for field-level validation errors
    """

    field = None
    message = None

    def __init__(self, field, message):
        self.field = field
        self.message = message