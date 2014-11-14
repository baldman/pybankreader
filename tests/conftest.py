# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def mock_report():
    return "AB1234\nfirst     \nsecond    \nZZ9911"


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
    return "T263310  HEADER 0001.0000BBCSOB\n" \
           "T263310  ADVMUL 0120141002986310\n" \
           "T263310  ADVMUL 02  4009925410            10003009903252820    K" \
           "ristin Olson Literary Agency s.r.o183861478                     " \
           "    019938742757817A6135                    20141002        C 00" \
           "00000000121.33EUR0000000007162.57C                              " \
           "               019938742757817A                   00000000000000" \
           "400992541000000000000000000000121,33 EUR 1,000000               " \
           " CZ2155000000005081107282           /ROC/NOT PROVIDED//177914   " \
           "       Albatros Media a.s.                                      " \
           "                                    \n" \
           "T263310  ADVMUZ 02CRE9903252820    019938742757817A          400" \
           "9925410        090183861478                         Albatros Med" \
           "ia a.s.                Na Pankraci 1618/3014000 Praha 4   CZ    " \
           "                                                                " \
           "CZ2155000000005081107282                                        " \
           "                                                                " \
           "                                               /ROC/NOT PROVIDED" \
           "//177914                                                        " \
           "                                                           00000" \
           "00000121.33EUR0000000000121.33EUR0001.00000000000000000070.00CZK" \
           "0000000000000.00EUR0000000000000.00   2014100220141002        /R" \
           "OC/NOT PROVIDED//177914                                         " \
           "                                                                " \
           "                                             SHARZBCCZPP        " \
           "                                \n" \
           "T263310  ADVMUL 02  6136                  10003009903252820    K" \
           "ristin Olson Literary Agency s.r.o183861478                     " \
           "                    6136                    20141002        D -0" \
           "00000000002.55EUR0000000007160.02C                              " \
           "               019938742757817A                   00000000000000" \
           "400992541000000000000000000000121,33 EUR 1,000000               " \
           " CZ2155000000005081107282           /ROC/NOT PROVIDED//177914   " \
           "       Albatros Media a.s.                                      " \
           "                                    \n" \
           "T263310  LOCK   99            0141002091008        0"


@pytest.fixture
def gpc_account_record():
    return "0740000000183861478KRISTIN OLSON LITERA31081400000000645770+0000" \
           "0000814124+000000030659370000000032342910009300914"


@pytest.fixture
def gpc_item_record():
    return "0750000000183861478000000000000000010000000060610000002250001000" \
           "000000000000000003108539408010914Aitken Alexander Ass00978010914"


@pytest.fixture
def gpc_iteminfo_record():
    return "0760000000000000000IBASSR8486010914683, 684"


@pytest.fixture
def gpc_remittance1_record():
    return "0782.250,00 EUR 1,000000              GB85HOAB15980093333120"


@pytest.fixture
def gpc_remittance2_record():
    return "079Cause Celeb, Olivia Joules, Slovak Aitken Alexander Associates Ltd."


@pytest.fixture
def gpc_report():
    tst = u"0740000000263847748KRISTIN OLSON LITERA31081400000000288683+0000" \
          u"0000491654+000000000004430000000002034140008300914              " \
          u"\n" \
          u"0750000000263847748000000508110726610000000000580000000034112000" \
          u"000000000550000004109388409260914ALBATROS MEDIA A.S. 00826260914" \
          u"\n" \
          u"07600000000000000004109388409260914OP00140925501199            " \
          u"                                                               " \
          u"  \n" \
          u"07834,11 GBP 1,000000                 CZ6555000000005081107266 " \
          u"                                                               " \
          u"  \n" \
          u"079177714                             ALBATROS MEDIA A.S.      " \
          u"                                                               " \
          u"  \n" \
          u"075000000026384774800000000000000001000000000059000000000199100" \
          u"0000000000000000004109388409260914Poplatek za zahranič008262609" \
          u"14\n" \
          u"07600000000000000000000000059260914OP00140925501199            " \
          u"                                                               " \
          u"  \n" \
          u"07834,11 GBP 1,000000                 CZ6555000000005081107266 " \
          u"                                                               " \
          u"  \n" \
          u"079177714                             ALBATROS MEDIA A.S.      " \
          u"                                                               " \
          u"  \n" \
          u"075000000026384774800000001695721781000000000060000000200000200" \
          u"0000000000030000003108498409260914ARGO spol. s r.o.   008262609" \
          u"14\n" \
          u"0760000000000000000BOATHB691526091414.1.0801 0:00:0            " \
          u"                                                               " \
          u"  \n" \
          u"0782.000,00 GBP                       1,000000                 " \
          u"                                                               " \
          u"  \n" \
          u"07914.1.0801 0:00:00                  169572178/ARGO SPOL. S R." \
          u"O.                                                             " \
          u"  \n" \
          u"075000000026384774800000001695721781000000000061000000000017100" \
          u"0000000000030000003108498409260914Poplatek za zahranič008262609" \
          u"14\n" \
          u"0760000000000000000BOATHB691526091414.1.0801 0:00:0            " \
          u"                                                               " \
          u"  \n" \
          u"0782.000,00 GBP                       1,000000                 " \
          u"                                                               " \
          u"  \n" \
          u"07914.1.0801 0:00:00                  169572178/ARGO SPOL. S R." \
          u"O.                                                             " \
          u"  \n" \
          u"075000000026384774800000000000000001000000000062000000000227100" \
          u"0000000000000000000000000000270914Za vedení účtu, výpi008262709" \
          u"14\n" \
          u"07600000000000000000000000062270914                            " \
          u"                                                               " \
          u"  \n" \
          u"075000000026384774800000000000000001000000000065000000000003200" \
          u"0000000000000000000000000000300914Zúčtování kladných ú008263009" \
          u"14\n" \
          u"07600000000000000000000000065290914                            " \
          u"                                                               " \
          u"  \n"
    return tst