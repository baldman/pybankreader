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
    return "T263310  ADVMUL 02  IBATL58813            10003009903252820    " \
           "Kristin Olson Literary Agency s.r.o177148326                   " \
           "                      20623                   20141002        D" \
           " -000000006075.00CZK0000003608328.02C0100       100060018432071" \
           "                   PO                                 355800266" \
           "96797000000000000266967970000000000"