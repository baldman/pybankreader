from six import StringIO
import datetime
from pybankreader.formats.bbf.records import AdvmulHeaderRecord, AdvmuzRecord,\
    AdvmulRecord
from pybankreader.formats.bbf.reports import AdvmulReport


def test_advmul_report(advmul_report):
    file_like = StringIO(advmul_report)
    report = AdvmulReport(file_like)

    # Header Record
    assert report.header.edi_msg == 'HEADER'
    assert report.header.app_id == '263310'
    assert report.header.app_ver == '01.0000'
    assert report.header.bank_app == 'T'
    assert report.header.app_brand == 'BBCSOB'
    assert report.header.rec_typ == '00'

    # Data
    assert len(report.data) == 4
    assert isinstance(report.data[0], AdvmulHeaderRecord)
    assert isinstance(report.data[1], AdvmulRecord)
    assert isinstance(report.data[2], AdvmuzRecord)
    assert isinstance(report.data[3], AdvmulRecord)

    # Lock Record
    assert report.lock.app_id == '263310'
    assert report.lock.bank_app == 'T'
    assert report.lock.rec_typ == '99'
    assert report.lock.seq_no == 0
    assert report.lock.count == 0
    assert report.lock.timestamp == \
           datetime.datetime(year=2014, month=10, day=2, hour=9, minute=10,
                             second=8)