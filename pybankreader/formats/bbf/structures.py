from .records import HeaderRecord, LockRecord, AdvmulRecord, AdvmuzRecord


class Report(object):
    pass


class Advmul(Report):

    header = HeaderRecord
    data = [AdvmulRecord, AdvmuzRecord]
    lock = LockRecord
