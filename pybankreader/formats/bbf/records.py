from ... import fields, records


class HeaderRecord(records.Record):
    """
    The HEADER record. This will be the first record in the source file.
    """

    bank_app = fields.RegexField(regex="T", length=1, required=True)
    app_id = fields.CharField(length=8, required=True)
    edi_msg = fields.RegexField(regex="HEADER", length=6, required=True)
    separator = fields.CharField(length=1, required=False)
    rec_typ = fields.RegexField(regex="00", length=2, required=True)
    app_ver = fields.RegexField(regex="[0-9]{2}\.[0-9]{4}", length=7,
                                required=True)
    app_brand = fields.RegexField(regex="BBCSOB|XHBPS", length=6,
                                  required=True)


class LockRecord(records.Record):
    """
    The LOCK record. This will be the last record in the source file.
    """

    bank_app = fields.RegexField(regex="T", length=1, required=True)
    app_id = fields.CharField(length=8, required=True)
    edi_msg = fields.RegexField(regex="LOCK", length=6, required=True)
    separator = fields.CharField(length=1, required=False)
    rec_typ = fields.RegexField(regex="99", length=2, required=True)
    count = fields.IntegerField(length=13, required=True)
    timestamp = fields.TimestampField(format="%y%m%d%H%M%S", length=12,
                                      required=True)
    seq_no = fields.IntegerField(length=9, required=True)


class AdvmulHeaderRecord(records.Record):
    """
    The AVDMUL header record. This will be the second record in the source
    file. Contrary to the docs, the record is identified by ADVMUL, but by
    ADVMUZ as well, so that's why the regex.
    """

    bank_app = fields.RegexField(regex="T", length=1, required=True)
    app_id = fields.CharField(length=8, required=True)
    edi_msg = fields.RegexField(regex="ADVMU(L|Z)", length=6, required=True)
    separator = fields.CharField(length=1, required=False)
    rec_typ = fields.RegexField(regex="01", length=2, required=True)
    msg_rno = fields.CharField(length=14, required=True)


class AdvmulRecord(records.Record):
    """
    The actual ADVMUL record. This signifies the actual remittance advice on
    the account.
    """

    MESSAGE_TYPE = {
        "01": 'charging order - priority',
        "11": 'charging order - priority',
        "12": 'collection order',
        "55": 'rejected collection',
    }

    TRANSACT_TYPE = {
        'C': 'credit transaction',
        'D': 'debit transaction',
        'CR': 'cancelled credit transaction',
        'DR': 'cancelled debit transaction',
    }

    bank_app = fields.RegexField(regex="T", length=1, required=True)
    app_id = fields.CharField(length=8, required=True)
    edi_msg = fields.RegexField(regex="ADVMUL", length=6, required=True)
    separator = fields.CharField(length=1, required=False)
    rec_typ = fields.RegexField(regex="02", length=2, required=True)
    message_type = fields.RegexField(length=2, required=False,
                                     regex='01|11|12|55')
    transact_no = fields.CharField(length=22, required=False)
    weight = fields.IntegerField(length=3, required=True)
    route_no = fields.RegexField(length=4, regex='0300|7500', required=False)
    client_no = fields.CharField(length=14, required=False)
    client_name = fields.CharField(length=35, required=False)
    client_account_no = fields.CharField(length=34, required=True)
    client_reference = fields.CharField(length=16, required=False)
    bank_reference = fields.CharField(length=16, required=False)
    date = fields.TimestampField(length=8, required=False, format='%Y%m%d')
    date_process = fields.TimestampField(length=8, required=True,
                                         format='%Y%m%d')
    date_process_other = fields.TimestampField(length=8, required=False,
                                               format='%Y%m%d')
    transact_type = fields.RegexField(length=2, required=True,
                                      regex='C|D|CR|DR')
    amount = fields.DecimalField(length=16, required=True)
    currency = fields.CharField(length=3, required=True)
    balance = fields.DecimalField(length=16, required=True)
    balance_code = fields.CharField(length=1, required=True)
    offset_account_bank_code = fields.CharField(length=11, required=False)
    offset_account_no = fields.CharField(length=34, required=False)
    offset_account_name = fields.CharField(length=35, required=False)
    constant_symbol = fields.IntegerField(length=4, required=False)
    variable_symbol = fields.IntegerField(length=10, required=False)
    specific_symbol = fields.IntegerField(length=10, required=False)
    variable_symbol_offset = fields.IntegerField(length=10, required=False)
    specific_symbol_offset = fields.IntegerField(length=10, required=False)
    message1 = fields.CharField(length=35, required=False)
    message2 = fields.CharField(length=35, required=False)
    message3 = fields.CharField(length=35, required=False)
    message4 = fields.CharField(length=35, required=False)
    note = fields.CharField(length=35, required=False)
    balance_final = fields.DecimalField(length=16, required=False)
    balance_final_code = fields.CharField(length=1, required=False)
    balance_time = fields.TimestampField(length=6, required=False,
                                         format="%h%m%s")


class AdvmuzRecord(records.Record):
    """
    The actual ADVMUZ record. This signifies the actual remittance advice on
    the account.
    """

    MESSAGE_TYPE = {
        "CRE": 'incoming payment',
        "DBE": 'outgoing payment',
    }

    FEE_SETTLING = {
        'OUR': 'paid by creditor',
        'BEN': 'paid by beneficiary',
        'SHA': 'paid by each',
    }

    bank_app = fields.RegexField(regex="T", length=1, required=True)
    app_id = fields.CharField(length=8, required=True)
    edi_msg = fields.RegexField(regex="ADVMUZ", length=6, required=True)
    separator = fields.CharField(length=1, required=False)
    rec_typ = fields.RegexField(regex="02", length=2, required=True)
    message_type = fields.RegexField(length=3, required=True, regex='CRE|DBE')
    client_no = fields.CharField(length=14, required=False)
    order_reference = fields.CharField(length=16, required=True)
    reference_item = fields.CharField(length=28, required=True)
    weight = fields.IntegerField(length=3, required=True)
    client_account_no = fields.CharField(length=34, required=True)
    creditor_address1 = fields.CharField(length=35, required=True)
    creditor_address2 = fields.CharField(length=35, required=False)
    creditor_address3 = fields.CharField(length=35, required=False)
    creditor_address4 = fields.CharField(length=35, required=False)
    creditor_account_no = fields.CharField(length=35, required=False)
    creditor_bank1 = fields.CharField(length=35, required=False)
    creditor_bank2 = fields.CharField(length=35, required=False)
    creditor_bank3 = fields.CharField(length=35, required=False)
    creditor_bank4 = fields.CharField(length=35, required=False)
    payment_reason1 = fields.CharField(length=35, required=False)
    payment_reason2 = fields.CharField(length=35, required=False)
    payment_reason3 = fields.CharField(length=35, required=False)
    payment_reason4 = fields.CharField(length=35, required=False)
    amount = fields.DecimalField(length=16, required=False)
    currency = fields.CharField(length=3, required=False)
    amount_account_currency = fields.DecimalField(length=16, required=True)
    account_currency = fields.CharField(length=3, required=True)
    exchange_rate = fields.DecimalField(length=12, required=False)
    local_fee = fields.DecimalField(length=16, required=False)
    local_currency = fields.CharField(length=3, required=False)
    foreign_fee = fields.DecimalField(length=16, required=False)
    foreign_currency = fields.CharField(length=3, required=False)
    other_fees = fields.DecimalField(length=16, required=False)
    other_fees_currency = fields.CharField(length=3, required=False)
    date = fields.TimestampField(length=8, required=True, format='%Y%m%d')
    date_process = fields.TimestampField(length=8, required=True,
                                         format='%Y%m%d')
    date_due = fields.TimestampField(length=8, required=False, format='%Y%m%d')
    client_advice1 = fields.CharField(length=35, required=False)
    client_advice2 = fields.CharField(length=35, required=False)
    client_advice3 = fields.CharField(length=35, required=False)
    client_advice4 = fields.CharField(length=35, required=False)
    client_advice5 = fields.CharField(length=35, required=False)
    fee_settling = fields.RegexField(length=3, required=False,
                                     regex='OUR|BEN|SHA')
    swift_code = fields.CharField(length=11, required=False)
    payment_title = fields.CharField(length=3, required=False)
    routing_code = fields.CharField(length=34, required=False)