import datetime
from formats.bbf.records import HeaderRecord, LockRecord


def test_header_record(header_record):
    """
    Try to load the header record and test that it actually loads it without
    exceptions
    """
    rec = HeaderRecord()
    rec.load(header_record)

    assert rec.bank_app == 'T'
    assert rec.app_id == '363914  '
    assert rec.separator == ' '
    assert rec.rec_typ == '00'
    assert rec.app_ver == '01.0000'
    assert rec.app_brand == 'BBCSOB'


def test_lock_record(lock_record):
    """
    Try to load the lock record and test that it actually loads it without
    exceptions
    """
    rec = LockRecord()
    rec.load(lock_record)

    assert rec.bank_app == 'T'
    assert rec.app_id == '363914  '
    assert rec.separator == ' '
    assert rec.rec_typ == '99'
    assert rec.count == 0
    assert rec.timestamp == datetime.datetime(year=2014, month=9, day=2,
                                              hour=7, minute=9, second=22)
    assert rec.seq_no == 11
