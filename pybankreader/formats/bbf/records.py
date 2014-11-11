from pybankreader import fields, records


class HeaderRecord(records.Record):
    """
    The HEADER record. This will be the first record in the source file.
    """

    bank_app = fields.RegexField(position=1, regex="T", length=1,
                                 required=True)
    app_id = fields.CharField(position=2, length=8, required=True)
    edi_msg = fields.RegexField(position=3, regex="HEADER", length=6,
                                required=True)
    separator = fields.CharField(position=4, length=1, required=False)
    rec_typ = fields.RegexField(position=5, regex="00", length=2,
                                required=True)
    app_ver = fields.RegexField(position=6, regex="[0-9]{2}\.[0-9]{4}",
                                length=7, required=True)
    app_brand = fields.RegexField(position=8, regex="BBCSOB|XHBPS", length=6,
                                  required=True)


class LockRecord(records.Record):
    """
    The LOCK record. This will be the last record in the source file.
    """

    bank_app = fields.RegexField(position=1, regex="T", length=1,
                                 required=True)
    app_id = fields.CharField(position=2, length=8, required=True)
    edi_msg = fields.RegexField(position=3, regex="LOCK", length=6,
                                required=True)
    separator = fields.CharField(position=4, length=1, required=False)
    rec_typ = fields.RegexField(position=5, regex="99", length=2,
                                required=True)
    count = fields.IntegerField(position=6, length=13, required=True)
    timestamp = fields.TimestampField(position=7, format="%y%m%d%H%M%S",
                                      length=12, required=True)
    seq_no = fields.IntegerField(position=8, length=9, required=True)


class AdvmulHeaderRecord(records.Record):
    """
    The AVDMUL header record. This will be the second record in the source
    file. Contrary to the docs, the record is identified by ADVMUL, but by
    ADVMUZ as well, so that's why the regex.
    """

    bank_app = fields.RegexField(position=1, regex="T", length=1,
                                 required=True)
    app_id = fields.CharField(position=2, length=8, required=True)
    edi_msg = fields.RegexField(position=3, regex="ADVMU(L|Z)", length=6,
                                required=True)
    separator = fields.CharField(position=4, length=1, required=False)
    rec_typ = fields.RegexField(position=5, regex="01", length=2,
                                required=True)
    msg_rno = fields.CharField(position=6, length=14, required=True)


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

    TRASNACT_TYPE = {
        'C': 'credit transaction',
        'D': 'debit transaction',
        'CR': 'cancelled credit transaction',
        'DR': 'cancelled debit transaction',
    }

    bank_app = fields.RegexField(position=1, regex="T", length=1,
                                 required=True)
    app_id = fields.CharField(position=2, length=8, required=True)
    edi_msg = fields.RegexField(position=3, regex="ADVMUL", length=6,
                                required=True)
    separator = fields.CharField(position=4, length=1, required=False)
    rec_typ = fields.RegexField(position=5, regex="02", length=2,
                                required=True)
    message_type = fields.RegexField(position=6, length=2, required=False,
                                     regex='01|11|12|55')
    transact_no = fields.CharField(position=7, length=22, required=False)
    weight = fields.IntegerField(position=8, length=3, required=True)
    route_no = fields.RegexField(position=9, length=4, regex='0300|7500',
                                 required=False)
    client_no = fields.CharField(position=10, length=14, required=False)
    client_name = fields.CharField(position=11, length=35, required=False)
    client_account_no = fields.CharField(position=12, length=34, required=True)
    client_reference = fields.CharField(position=13, length=16, required=False)
    bank_reference = fields.CharField(position=14, length=16, required=False)
    date = fields.TimestampField(position=15, length=8, required=False,
                                 format='%Y%m%d')
    date_process = fields.TimestampField(position=16, length=8, required=True,
                                         format='%Y%m%d')
    date_process_other = fields.TimestampField(position=17, length=8,
                                               required=False, format='%Y%m%d')
    trasnact_type = fields.RegexField(position=18, length=2, required=True,
                                      regex='C|D|CR|DR')
    amount = fields.DecimalField(position=19, length=16, required=True)
    currency = fields.CharField(position=20, length=3, required=True)
    balance = fields.DecimalField(position=21, length=16, required=True)
    balance_code = fields.CharField(position=22, length=1, required=True)
    offset_account_bank_code = fields.CharField(position=23, length=11,
                                                required=False)
    offset_account_no = fields.CharField(position=24, length=34,
                                         required=False)
    offset_account_name = fields.CharField(position=25, length=35,
                                           required=False)
    constant_symbol = fields.IntegerField(position=26, length=4,
                                          required=False)
    variable_symbol = fields.IntegerField(position=27, length=10,
                                          required=False)
    specific_symbol = fields.IntegerField(position=28, length=10,
                                          required=False)
    variable_symbol_offset = fields.IntegerField(position=29, length=10,
                                                 required=False)
    specific_symbol_offset = fields.IntegerField(position=30, length=10,
                                                 required=False)
    message1 = fields.CharField(position=31, length=35, required=False)
    message2 = fields.CharField(position=32, length=35, required=False)
    message3 = fields.CharField(position=33, length=35, required=False)
    message4 = fields.CharField(position=34, length=35, required=False)
    note = fields.CharField(position=35, length=35, required=False)
    balance_final = fields.DecimalField(position=36, length=16, required=False)
    balance_final_code = fields.CharField(position=37, length=1,
                                          required=False)
    balance_time = fields.TimestampField(position=38, length=6, required=False,
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

    bank_app = fields.RegexField(position=1, regex="T", length=1,
                                 required=True)
    app_id = fields.CharField(position=2, length=8, required=True)
    edi_msg = fields.RegexField(position=3, regex="ADVMUZ", length=6,
                                required=True)
    separator = fields.CharField(position=4, length=1, required=False)
    rec_typ = fields.RegexField(position=5, regex="02", length=2,
                                required=True)
    message_type = fields.RegexField(position=6, length=3, required=True,
                                     regex='CRE|DBE')
    client_no = fields.CharField(position=7, length=14, required=False)
    order_reference = fields.CharField(position=8, length=16, required=True)
    reference_item = fields.CharField(position=9, length=28, required=True)
    weight = fields.IntegerField(position=10, length=3, required=True)
    client_account_no = fields.CharField(position=11, length=34, required=True)
    creditor_address1 = fields.CharField(position=12, length=35, required=True)
    creditor_address2 = fields.CharField(position=14, length=35,
                                         required=False)
    creditor_address3 = fields.CharField(position=15, length=35,
                                         required=False)
    creditor_address4 = fields.CharField(position=16, length=35,
                                         required=False)
    creditor_account_no = fields.CharField(position=17, length=35,
                                           required=False)
    creditor_bank1 = fields.CharField(position=18, length=35, required=False)
    creditor_bank2 = fields.CharField(position=19, length=35, required=False)
    creditor_bank3 = fields.CharField(position=20, length=35, required=False)
    creditor_bank4 = fields.CharField(position=21, length=35, required=False)
    payment_reason1 = fields.CharField(position=22, length=35, required=False)
    payment_reason2 = fields.CharField(position=23, length=35, required=False)
    payment_reason3 = fields.CharField(position=24, length=35, required=False)
    payment_reason4 = fields.CharField(position=25, length=35, required=False)
    amount = fields.DecimalField(position=26, length=16, required=False)
    currency = fields.CharField(position=27, length=3, required=False)
    amount_account_currency = fields.DecimalField(position=28, length=16,
                                                  required=True)
    account_currency = fields.CharField(position=29, length=3, required=True)
    exchange_rate = fields.DecimalField(position=30, length=12, required=False)
    local_fee = fields.DecimalField(position=31, length=16, required=False)
    local_currency = fields.CharField(position=32, length=3, required=False)
    foreign_fee = fields.DecimalField(position=33, length=16, required=False)
    foreign_currency = fields.CharField(position=34, length=3, required=False)
    other_fees = fields.DecimalField(position=35, length=16, required=False)
    other_fees_currency = fields.CharField(position=36, length=3,
                                           required=False)
    date = fields.TimestampField(position=37, length=8, required=True,
                                 format='%Y%m%d')
    date_process = fields.TimestampField(position=38, length=8, required=True,
                                         format='%Y%m%d')
    date_due = fields.TimestampField(position=39, length=8, required=False,
                                     format='%Y%m%d')
    client_advice1 = fields.CharField(position=40, length=35, required=False)
    client_advice2 = fields.CharField(position=41, length=35, required=False)
    client_advice3 = fields.CharField(position=42, length=35, required=False)
    client_advice4 = fields.CharField(position=43, length=35, required=False)
    client_advice5 = fields.CharField(position=44, length=35, required=False)
    fee_settling = fields.RegexField(position=45, length=3, required=False,
                                     regex='OUR|BEN|SHA')
    swift_code = fields.CharField(position=46, length=11, required=False)
    payment_title = fields.CharField(position=47, length=3, required=False)
    routing_code = fields.CharField(position=48, length=34, required=False)