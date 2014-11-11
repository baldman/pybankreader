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


@pytest.fixture
def advmul_report():
    return "T263310  HEADER 0001.0000BBCSOB" \
           "T263310  ADVMUL 0120141002986310" \
           "T263310  ADVMUL 02  4009925410            10003009903252820    K" \
           "ristin Olson Literary Agency s.r.o183861478                     " \
           "    019938742757817A6135                    20141002        C 00" \
           "00000000121.33EUR0000000007162.57C                              " \
           "               019938742757817A                   00000000000000" \
           "400992541000000000000000000000121,33 EUR 1,000000               " \
           " CZ2155000000005081107282           /ROC/NOT PROVIDED//177914   " \
           "       Albatros Media a.s.                                      " \
           "                                    T263310  ADVMUZ 02CRE9903252" \
           "820    019938742757817A          4009925410        090183861478 " \
           "                        Albatros Media a.s.                Na Pa" \
           "nkraci 1618/3014000 Praha 4   CZ                                " \
           "                                    CZ2155000000005081107282    " \
           "                                                                " \
           "                                                                " \
           "                   /ROC/NOT PROVIDED//177914                    " \
           "                                                                " \
           "                               0000000000121.33EUR0000000000121." \
           "33EUR0001.00000000000000000070.00CZK0000000000000.00EUR000000000" \
           "0000.00   2014100220141002        /ROC/NOT PROVIDED//177914     " \
           "                                                                " \
           "                                                                " \
           "                 SHARZBCCZPP                                    " \
           "    T263310  ADVMUL 02  6136                  10003009903252820 " \
           "   Kristin Olson Literary Agency s.r.o183861478                 " \
           "                        6136                    20141002        " \
           "D -000000000002.55EUR0000000007160.02C                          " \
           "                   019938742757817A                   0000000000" \
           "0000400992541000000000000000000000121,33 EUR 1,000000           " \
           "     CZ2155000000005081107282           /ROC/NOT PROVIDED//17791" \
           "4          Albatros Media a.s.                                  " \
           "                                        T263310  LOCK   99      " \
           "      0141002091008        0"


@pytest.fixture
def mock_report():
    return "AB1234\nfirst     \nsecond    \nZZ9911"