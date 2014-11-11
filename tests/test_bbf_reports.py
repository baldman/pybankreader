from StringIO import StringIO
import pytest
from formats.bbf.reports import Advmul


# @pytest.xfail
# def test_advmul_report(advmul_report):
#     file_like = StringIO(advmul_report)
#     report = Advmul(file_like)
#
#     # for x in report:
#     #     print x
#     assert False
