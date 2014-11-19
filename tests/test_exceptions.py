from six import StringIO
import pytest
from pybankreader.formats.gpc.reports import AccountReport
from pybankreader.exceptions import ValidationError


def test_exception_history(advmul_report):
    file_like = StringIO(advmul_report)
    with pytest.raises(ValidationError) as err:
        AccountReport(file_like)

    expected_trace = \
        "header @ <0,3>: Value 'T26' does not match the regex pattern '079' " \
        "for data: T263310  HEADER 0001.0000BBCSOB\n" \
        "[0] >>> AccountRecord/header @ <0,3>: Value 'T26' does not match " \
        "the regex pattern '074'\n" \
        "[1] >>> ItemRecord/header @ <0,3>: Value 'T26' does not match the " \
        "regex pattern '075'\n" \
        "[2] >>> ItemInfoRecord/header @ <0,3>: Value 'T26' does not match " \
        "the regex pattern '076'\n" \
        "[3] >>> ItemRemittance1Record/header @ <0,3>: Value 'T26' does not " \
        "match the regex pattern '078'\n" \
        "[4] >>> ItemRemittance2Record/header @ <0,3>: Value 'T26' does not " \
        "match the regex pattern '079'\n"

    assert str(err.value) == expected_trace
