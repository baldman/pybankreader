from pybankreader import fields, records


class HeaderRecord(records.Record):

    bank_app = fields.RegexField(regex="T", length=1, required=True)
    app_id = fields.CharField(length=8, required=True)
    edi_msg = fields.RegexField(regex="HEADER", length=6, required=True)
    separator = fields.RegexField(reqex="\w", length=1, required=True)
    rec_typ = fields.RegexField(regex="00", length=2, required=True)
    app_ver = fields.RegexField(regex="[0-9]{2}\.[0-9]{4}", length=7,
                               required=True)
    app_brand = fields.RegexField(regex="BBCSOB|XHBPS", length=6, required=True)


class LockRecord(records.Record):

    bank_app = fields.RegexField(regex="T", length=1, required=True)
    app_id = fields.CharField(length=8, required=True)
    edi_msg = fields.RegexField(regex="LOCK", length=6, required=True)
    separator = fields.RegexField(regex="\w", length=1, required=True)
    rec_typ = fields.RegexField(regex="99", length=2, required=True)
    count = fields.IntegerField(length=13, required=True)
    timestamp = fields.TimestampField(format="%y%m%d%H%M%S", length=12,
                                     required=True)
    seq_no = fields.IntegerField(length=9, required=True)