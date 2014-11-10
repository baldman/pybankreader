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

    bank_app = fields.RegexField(position=1, regex="T", length=1,
                                 required=True)
    app_id = fields.CharField(position=2, length=8, required=True)
    edi_msg = fields.RegexField(position=3, regex="ADVMUL", length=6,
                                required=True)
    separator = fields.CharField(position=4, length=1, required=False)
    rec_typ = fields.RegexField(position=5, regex="02", length=2,
                                required=True)
    message_type = fields.CharField(position=6, length=2, required=False)
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
    date_process_other = fields.TimestampField(position=16, length=8,
                                               required=False,format='%Y%m%d')


class AdvmuzRecord(records.Record):
    pass