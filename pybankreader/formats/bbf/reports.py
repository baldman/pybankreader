from .records import HeaderRecord, LockRecord, AdvmulRecord, AdvmuzRecord
from pybankreader.reports import Report


class Advmul(Report):

    header = HeaderRecord()
    data = [AdvmulRecord(), AdvmuzRecord()]
    lock = LockRecord()

    def process_header(self, record):
        return record

    def process_data(self, record):
        return record

    def process_lock(self, record):
         return record