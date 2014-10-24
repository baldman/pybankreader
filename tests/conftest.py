import pytest


@pytest.fixture
def header_record():
    return "T363914  HEADER 0001.0000BBCSOB"


@pytest.fixture
def lock_record():
    return "T263310  LOCK   99            0140902070922        0"