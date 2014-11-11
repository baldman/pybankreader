import pytest


@pytest.fixture
def header_record():
    return "T363914  HEADER 0001.0000BBCSOB"


@pytest.fixture
def lock_record():
    return "T363914  LOCK   99            0140902070922       11"


@pytest.fixture
def advmul_header_record():
    return "T363914  ADVMUL 0120140930925710"


@pytest.fixture
def advmuz_header_record():
    return "T363914  ADVMUZ 0120140930925710"


@pytest.fixture
def advmul_record():
    return "T363914  ADVMUL 02  IBATL58813            10003009903252820    " \
           "Whatever corp Inc.                 177148326                   " \
           "                      20623                   20141002        D" \
           " -000000006075.00CZK0000003608328.02C0100       100060018432071" \
           "                   PO                                 355800266" \
           "96797000000000000266967970000000000"


@pytest.fixture
def advmuz_record():
    return "T363914  ADVMUZ 02CRE9903252820    019938742626501A          40" \
           "83604409        090183861478                         Big Group " \
           "a.s.                     Na Pankraci 1620/1214000 Praha 4   CZ " \
           "                                                               " \
           "    CZ2155000000005081107282                                   " \
           "                                                               " \
           "                                                     /ROC/NOT P" \
           "ROVIDED//174914                                                " \
           "                                                               " \
           "    0000000000760.00EUR0000000000760.00EUR0001.0000000000000000" \
           "0070.00CZK0000000000000.00EUR0000000000000.00   201409192014091" \
           "9        /ROC/NOT PROVIDED//174914                             " \
           "                                                               " \
           "                                                          SHARZ" \
           "BCCZPP"