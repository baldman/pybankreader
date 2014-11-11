

class Report(object):

    _source = None
    """
    The source file-like object to read from
    """

    data = None

    def __init__(self, file_like):
        self._source = file_like
        self.data = []

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        for record in self.data:
            yield record

    def __len__(self):
        return len(self.data)

    def _load(self):
        pass
