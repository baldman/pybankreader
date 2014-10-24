
class BBFMetadata(object):
    """
    Class represents metadata of the entire BBF file.
    """

    _app_id = None
    """
    BusinessBanking client identifier
    """

    _version = None
    """
    Version of the data file
    """

    _brand = None
    """
    Branding string inside the file (either BBCSOB or XHBPS)
    """

    _record_count = None
    """
    Number of individual records in the data file
    """

    _timestamp = None
    """
    Timestamp of the wile -- when the report was generated
    """

    _seq_id = None
    """
    Sequential ID of the batch file
    """

    def __init__(self):
        pass


class BBFFile(object):
    """
    Class is a simple facade for reading BBF files. Only one file at a time can
    read through this class.
    """

    _header = None
    _footer = None
    _records = None

    _metadata = None
    """
    BBFMetadata instance
    """

    def __init__(self, filepath):
        with open(filepath, 'r') as source:
            pass

        self._metadata = BBFMetadata()

    def __iter__(self):
        pass
        # iterate over records

    @property
    def metadata(self):
        return self._metadata

