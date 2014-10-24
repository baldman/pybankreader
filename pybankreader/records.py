from . import types
import six


class RecordMeta(type):

    def __new__(mcs, *args, **kwargs):
        return mcs


class HeaderRecord(six.with_metaclass(RecordMeta, object)):

    bank_app = types.RegexField(regex="T", length=1, required=True)
    app_id = types.CharField(length=8, required=True)
    edi_msg = types.RegexField(regex="HEADER", length=6, required=True)
    separator = types.RegexField(reqex="\w", length=1, required=True)
    rec_typ = types.RegexField(regex="00", length=2, required=True)
    app_ver = types.RegexField(regex="[0-9]{2}\.[0-9]{4}", length=7,
                               required=True)
    app_brand = types.RegexField(regex="BBCSOB|XHBPS", length=6, required=True)


class LockRecord(six.with_metaclass(RecordMeta, object)):

    bank_app = types.RegexField(regex="T", length=1, required=True)
    app_id = types.CharField(length=8, required=True)
    edi_msg = types.RegexField(regex="LOCK", length=6, required=True)
    separator = types.RegexField(regex="\w", length=1, required=True)
    rec_typ = types.RegexField(regex="99", length=2, required=True)
    count = types.IntegerField(length=13, required=True)
    timestamp = types.TimestampField(format="%y%m%d%H%M%S", length=12,
                                     required=True)
    seq_no = types.IntegerField(length=9, required=True)