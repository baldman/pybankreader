import datetime
from decimal import Decimal
from pybankreader.formats.bbf.records import HeaderRecord, LockRecord, \
    AdvmulHeaderRecord, AdvmulRecord, AdvmuzRecord


def test_header_record(header_record):
    """
    Try to load the header record and test that it actually loads it without
    exceptions
    """
    rec = HeaderRecord()
    rec.load(header_record)

    assert rec.bank_app == 'T'
    assert rec.app_id == '363914'
    assert rec.edi_msg == 'HEADER'
    assert rec.separator is None
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
    assert rec.app_id == '363914'
    assert rec.edi_msg == 'LOCK'
    assert rec.separator is None
    assert rec.rec_typ == '99'
    assert rec.count == 0
    assert rec.timestamp == datetime.datetime(year=2014, month=9, day=2,
                                              hour=7, minute=9, second=22)
    assert rec.seq_no == 11


def test_advmul_header_record(advmul_header_record, advmuz_header_record):
    """
    Try to load the advmul header record (in both variants) and test that it
    actually loads it without exceptions
    """
    rec = AdvmulHeaderRecord()
    rec.load(advmul_header_record)

    assert rec.bank_app == 'T'
    assert rec.app_id == '363914'
    assert rec.edi_msg == 'ADVMUL'
    assert rec.separator is None
    assert rec.rec_typ == '01'
    assert rec.msg_rno == '20140930925710'

    rec.load(advmuz_header_record)
    assert rec.bank_app == 'T'
    assert rec.app_id == '363914'
    assert rec.edi_msg == 'ADVMUZ'
    assert rec.separator is None
    assert rec.rec_typ == '01'
    assert rec.msg_rno == '20140930925710'


def test_advmul_record(advmul_record):
    """
    Try to load the advmul record and test that it actually loads it without
    exceptions
    """
    rec = AdvmulRecord()
    rec.load(advmul_record)

    assert rec.bank_app == 'T'
    assert rec.app_id == '363914'
    assert rec.edi_msg == 'ADVMUL'
    assert rec.separator is None
    assert rec.rec_typ == '02'
    assert rec.message_type is None
    assert rec.transact_no == 'IBATL58813'
    assert rec.weight == 100
    assert rec.route_no == '0300'
    assert rec.client_no == '9903252820'
    assert rec.client_name == 'Whatever corp Inc.'
    assert rec.client_account_no == '177148326'
    assert rec.client_reference is None
    assert rec.bank_reference == '20623'
    assert rec.date is None
    assert rec.date_process == datetime.datetime(2014, 10, 2, 0, 0)
    assert rec.date_process_other is None
    assert rec.amount == -6075
    assert rec.currency == 'CZK'
    assert rec.balance == Decimal('3608328.02')
    assert rec.balance_code == 'C'
    assert rec.offset_account_bank_code == '0100'
    assert rec.offset_account_no == '100060018432071'
    assert rec.offset_account_name == 'PO'
    assert rec.constant_symbol == 3558
    assert rec.variable_symbol == 26696797
    assert rec.specific_symbol == 0
    assert rec.variable_symbol_offset == 26696797
    assert rec.specific_symbol_offset == 0
    assert rec.message1 is None
    assert rec.message2 is None
    assert rec.message3 is None
    assert rec.message4 is None
    assert rec.note is None
    assert rec.balance_final is None
    assert rec.balance_final_code is None
    assert rec.balance_time is None


def test_advmuz_record(advmuz_record):
    """
    Try to load the advmuz record and test that it actually loads it without
    exceptions
    """
    rec = AdvmuzRecord()
    rec.load(advmuz_record)

    assert rec.bank_app == 'T'
    assert rec.app_id == '363914'
    assert rec.edi_msg == 'ADVMUZ'
    assert rec.separator is None
    assert rec.rec_typ == '02'
    assert rec.message_type == 'CRE'
    assert rec.client_no == '9903252820'
    assert rec.order_reference == '019938742626501A'
    assert rec.reference_item == '4083604409'
    assert rec.weight == 90
    assert rec.client_account_no == '183861478'
    assert rec.creditor_address1 == 'Big Group a.s.'
    assert rec.creditor_address2 == 'Na Pankraci 1620/1214000 Praha 4'
    assert rec.creditor_address3 == 'CZ'
    assert rec.creditor_address4 is None
    assert rec.creditor_account_no == 'CZ2155000000005081107282'
    assert rec.creditor_bank1 is None
    assert rec.creditor_bank2 is None
    assert rec.creditor_bank3 is None
    assert rec.creditor_bank4 is None
    assert rec.payment_reason1 == '/ROC/NOT PROVIDED//174914'
    assert rec.payment_reason2 is None
    assert rec.payment_reason3 is None
    assert rec.payment_reason4 is None
    assert rec.amount == Decimal('760.00')
    assert rec.currency == 'EUR'
    assert rec.amount_account_currency == Decimal('760.00')
    assert rec.account_currency == 'EUR'
    assert rec.exchange_rate == Decimal('1.0000000')
    assert rec.local_fee == Decimal('70.00')
    assert rec.local_currency == 'CZK'
    assert rec.foreign_fee == Decimal('0.00')
    assert rec.foreign_currency == 'EUR'
    assert rec.other_fees == Decimal('0.00')
    assert rec.other_fees_currency is None
    assert rec.date == datetime.datetime(2014, 9, 19, 0, 0)
    assert rec.date_process == datetime.datetime(2014, 9, 19, 0, 0)
    assert rec.date_due is None
    assert rec.client_advice1 == '/ROC/NOT PROVIDED//174914'
    assert rec.client_advice2 is None
    assert rec.client_advice3 is None
    assert rec.client_advice4 is None
    assert rec.client_advice5 is None
    assert rec.fee_settling == 'SHA'
    assert rec.swift_code == 'RZBCCZPP'
    assert rec.payment_title is None
    assert rec.routing_code is None
