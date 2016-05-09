from ... import records, fields


class AccountRecord(records.Record):
    """
    The top-level record indicating an account. Usually, there will be only one
    in the file
    """

    BALANCE_SIGNUM = {
        '+': 1,
        '-': -1
    }

    REVENUE_SIGNUM = {
        '0': 1,
        '-': -1
    }

    header = fields.RegexField(length=3, required=True, regex='074')
    account_no = fields.CharField(length=16, required=True)
    name = fields.CharField(length=20, required=True)
    old_balance_date = fields.TimestampField(length=6, required=True,
                                             format='%d%m%y')
    old_balance = fields.IntegerField(length=14, required=True)
    old_balance_signum = fields.RegexField(length=1, required=True,
                                           regex='\+|\-')
    new_balance = fields.IntegerField(length=14, required=True)
    new_balance_signum = fields.RegexField(length=1, required=True,
                                           regex='\+|\-')
    revenue_debit = fields.IntegerField(length=14, required=True)
    revenue_debit_signum = fields.RegexField(length=1, required=True,
                                             regex='0|\-')
    revenue_credit = fields.IntegerField(length=14, required=True)
    revenue_credit_signum = fields.RegexField(length=1, required=True,
                                              regex='0|\-')
    seq_no = fields.IntegerField(length=3, required=True)
    clearance_date = fields.TimestampField(length=6, required=True,
                                           format='%d%m%y')
    fill = fields.CharField(length=14, required=False)


class ItemRecord(records.Record):
    """
    The item record represents the change of sum of money (i.e. money order)
    and associated information
    """

    CURRENCY_CODES = {
        '0030': 'AUD',
        '0124': 'CAD',
        '0756': 'CHF',
        '0203': 'CZK',
        '0208': 'DKK',
        '0978': 'EUR',
        '0826': 'GBP',
        '0191': 'HRK',
        '0348': 'HUF',
        '0392': 'JPY',
        '0578': 'NOK',
        '0554': 'NZD',
        '0616': 'PLN',
        '0810': 'RUR',
        '0752': 'SEK',
        '0703': 'SKK',
        '0840': 'USD',
        '0710': 'ZAR',
        '0949': 'TRY',
    }

    header = fields.RegexField(length=3, required=True, regex='075')
    account_no = fields.CharField(length=16, required=True)
    account_no_second = fields.CharField(length=16, required=True)
    record_type = fields.RegexField(length=1, required=True, regex='1|0')
    file_id = fields.IntegerField(length=3, required=True)
    file_seq_no = fields.IntegerField(length=3, required=True)
    seq_no = fields.IntegerField(length=6, required=True)
    amount = fields.IntegerField(length=12, required=True)
    accounting_code = fields.RegexField(length=1, required=True,
                                        regex='1|2|4|5')
    variable_symbol = fields.CharField(length=10, required=True)
    constant_symbol = fields.CharField(length=10, required=True)
    specific_symbol = fields.CharField(length=10, required=True)
    valuta = fields.IntegerField(length=6, required=True)
    name = fields.CharField(length=20, required=True)
    separator = fields.RegexField(length=1, required=True, regex='0')
    currency_iso_code = fields.CharField(length=4, required=True)
    clearance_date = fields.TimestampField(length=6, required=True,
                                           format='%d%m%y')


class ItemInfoRecord(records.Record):
    """
    An optional informational record for the money transfer
    """
    header = fields.RegexField(length=3, required=True, regex='076')
    transaction_id = fields.CharField(length=26, required=True)
    date = fields.TimestampField(length=6, required=False, format='%d%m%y')
    comment = fields.CharField(length=93, required=False)


class ItemRemittance1Record(records.Record):
    """
    An optional informational record (first) when a remmitance advice is issued
    """
    header = fields.RegexField(length=3, required=True, regex='078')
    av1 = fields.CharField(length=35, required=True)
    av2 = fields.CharField(length=35, required=False)
    fill = fields.CharField(length=55, required=False)


class ItemRemittance2Record(records.Record):
    """
    An optional informational record (second) when a remmitance advice is
    issued
    """
    header = fields.RegexField(length=3, required=True, regex='079')
    av3 = fields.CharField(length=35, required=False)
    av4 = fields.CharField(length=35, required=False)
    fill = fields.CharField(length=55, required=False)
