from pybankreader import fields, records


class HeaderRecord(records.Record):

    bank_app = fields.RegexField(position=1, regex="T", length=1,
                                 required=True)
    app_id = fields.CharField(position=2, length=8, required=True)
    edi_msg = fields.RegexField(position=3, regex="HEADER", length=6,
                                required=True)
    separator = fields.RegexField(position=4, reqex="\w", length=1,
                                  required=True)
    rec_typ = fields.RegexField(position=5, regex="00", length=2,
                                required=True)
    app_ver = fields.RegexField(position=6, regex="[0-9]{2}\.[0-9]{4}",
                                length=7, required=True)
    app_brand = fields.RegexField(position=8, regex="BBCSOB|XHBPS", length=6,
                                  required=True)


class LockRecord(records.Record):

    bank_app = fields.RegexField(position=1, regex="T", length=1,
                                 required=True)
    app_id = fields.CharField(position=2, length=8, required=True)
    edi_msg = fields.RegexField(position=3, regex="LOCK", length=6,
                                required=True)
    separator = fields.RegexField(position=4, regex="\w", length=1,
                                  required=True)
    rec_typ = fields.RegexField(position=5, regex="99", length=2,
                                required=True)
    count = fields.IntegerField(position=6, length=13, required=True)
    timestamp = fields.TimestampField(position=7, format="%y%m%d%H%M%S",
                                      length=12, required=True)
    seq_no = fields.IntegerField(position=8, length=9, required=True)