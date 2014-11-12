from .records import HeaderRecord, LockRecord, AdvmulRecord, AdvmuzRecord, \
    AdvmulHeaderRecord
from pybankreader.reports import Report, CompoundRecord


class Advmul(Report):

    header = HeaderRecord()
    data = CompoundRecord(AdvmulHeaderRecord, AdvmulRecord, AdvmuzRecord)
    lock = LockRecord()