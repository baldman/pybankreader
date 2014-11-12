import datetime
from pybankreader.formats.gpc.records import AccountRecord, ItemRecord


def test_account_record(gpc_account_record):
    """
    Try to load the account record and test that it actually loads it without
    exceptions
    """
    rec = AccountRecord()
    rec.load(gpc_account_record)

    assert rec.header == '074'
    assert rec.account_no == '0000000183861478'
    assert rec.name == 'KRISTIN OLSON LITERA'
    assert rec.old_balance_date == datetime.datetime(2014, 8, 31, 0, 0)
    assert rec.old_balance == 645770
    assert rec.old_balance_signum == '+'
    assert rec.new_balance == 814124
    assert rec.new_balance_signum == '+'
    assert rec.revenue_credit == 3234291
    assert rec.revenue_credit_signum == '0'
    assert rec.revenue_debit == 3065937
    assert rec.revenue_debit_signum == '0'
    assert rec.seq_no == 9
    assert rec.clearance_date == datetime.datetime(2014, 9, 30, 0, 0)
    assert rec.fill is None


def test_item_record(gpc_item_record):
    """
    Try to load the item record and test that it actually loads it without
    exceptions
    """
    rec = ItemRecord()
    rec.load(gpc_item_record)

    assert rec.header == '075'
    assert rec.account_no == '0000000183861478'
    assert rec.account_no_second == '0000000000000000'
    assert rec.record_type == '1'
    assert rec.file_id == 0
    assert rec.file_seq_no == 0
    assert rec.seq_no == 6061
    assert rec.amount == 225000
    assert rec.accounting_code == '1'
    assert rec.variable_symbol == 0
    assert rec.constant_symbol == 0
    assert rec.specific_symbol == 3108539408
    assert rec.valuta == 10914
    assert rec.name == 'Aitken Alexander Ass'
    assert rec.separator == '0'
    assert rec.currency_iso_code == 978
    assert rec.clearance_date == datetime.datetime(2014, 9, 1, 0, 0)
