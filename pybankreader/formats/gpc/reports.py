from .records import AccountRecord, ItemRecord, ItemInfoRecord, \
    ItemRemittance1Record, ItemRemittance2Record
from ...reports import Report, CompoundRecord


class Account(Report):

    data = CompoundRecord(AccountRecord, ItemRecord, ItemInfoRecord,
                          ItemRemittance1Record, ItemRemittance2Record)