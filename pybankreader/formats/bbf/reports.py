from .records import HeaderRecord, LockRecord, AdvmulRecord, AdvmuzRecord, \
    AdvmulHeaderRecord
from ...reports import Report, CompoundRecord


class AdvmulReport(Report):

    header = HeaderRecord()
    data = CompoundRecord(AdvmulHeaderRecord, AdvmulRecord, AdvmuzRecord)
    lock = LockRecord()