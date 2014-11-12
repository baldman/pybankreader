from six import StringIO
from pybankreader.formats.gpc.reports import Account


def test_account_report(gpc_report):
    file_like = StringIO(gpc_report.decode('windows-1250'))
    report = Account(file_like)
    #
    #
    # assert len(report.data) == 10