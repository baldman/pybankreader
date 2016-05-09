import datetime
from six import StringIO
from pybankreader.formats.gpc.records import AccountRecord, ItemRecord, \
    ItemInfoRecord, ItemRemittance1Record, ItemRemittance2Record
from pybankreader.formats.gpc.reports import AccountReport, Account, \
    AccountItem


def test_account_report(gpc_report):
    file_like = StringIO(gpc_report)

    report = AccountReport()
    # We need to patch the account report not to screw plain record loading
    original_process = AccountReport.process_data
    AccountReport.process_data = lambda self, record: record

    # Load'n'test
    report.load(file_like)

    account_rec = report.data[0]
    item_rec = report.data[1]
    item_info_rec = report.data[2]
    item_remittance1_rec = report.data[3]
    item_remittance2_rec = report.data[4]

    # Assert basics
    assert isinstance(account_rec, AccountRecord)
    assert isinstance(item_rec, ItemRecord)
    assert isinstance(item_info_rec, ItemInfoRecord)
    assert isinstance(item_remittance1_rec, ItemRemittance1Record)
    assert isinstance(item_remittance2_rec, ItemRemittance2Record)

    # Some random asserts to verify correctness, since most of the failure
    # scenarios should be caught elsewhere
    assert account_rec.old_balance == 288683
    assert account_rec.new_balance == 491654
    assert account_rec.revenue_credit == 203414

    assert item_rec.account_no == u'0000000263847748'
    assert item_rec.constant_symbol == u'0055000000'
    assert item_rec.specific_symbol == u'4109388409'

    assert item_info_rec.comment == u'OP00140925501199'
    assert item_info_rec.date == datetime.datetime(year=2014, month=9, day=26)
    assert item_info_rec.transaction_id == u'00000000000000004109388409'

    assert item_remittance1_rec.av1 == u'34,11 GBP 1,000000'
    assert item_remittance1_rec.av2 == u'CZ6555000000005081107266'

    assert item_remittance2_rec.av3 == u'177714'
    assert item_remittance2_rec.av4 == u'ALBATROS MEDIA A.S.'

    assert len(report.data) == 21

    # Undo the patch
    AccountReport.process_data = original_process


def test_account_processing(gpc_report):

    file_like = StringIO(gpc_report)
    report = AccountReport(file_like)

    # Test coercing to accounts
    for account in report.data:
        assert isinstance(account, Account)

    # We know we have one
    test_acc = report.data[0]
    assert len(test_acc.items) == 6

    # Test the proxy
    assert test_acc.name == 'KRISTIN OLSON LITERA'

    for x in test_acc.items:
        assert isinstance(x, AccountItem)

    test_item = test_acc.items[0]

    # Test aggregation
    for x in ['info', 'rem1', 'rem2']:
        assert hasattr(test_item, x)

    assert test_item.currency_iso_code == '0826'
    assert test_item.constant_symbol == '0055000000'
    assert test_item.name == u'ALBATROS MEDIA A.S.'

    assert test_item.info.date == datetime.datetime(year=2014, day=26, month=9)
    assert test_item.info.comment == u'OP00140925501199'

    assert test_item.rem1.av1 == u'34,11 GBP 1,000000'
    assert test_item.rem1.av2 == u'CZ6555000000005081107266'
