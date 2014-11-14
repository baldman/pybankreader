from .records import AccountRecord, ItemRecord, ItemInfoRecord, \
    ItemRemittance1Record, ItemRemittance2Record
from ...reports import Report, CompoundRecord
from ...utils import ProxyMixin


class AccountItem(ProxyMixin):
    """
    An AccountItem groups together all dependant records, and proxies to the
    main ItemRecord itself.
    """

    info = None
    rem1 = None
    rem2 = None

    def __init__(self, record):
        super(AccountItem, self).__init__(record)


class Account(ProxyMixin):
    """
    An Account wraps the AccountRecord using the proxy and prepares an empty
    list of items to be appended
    """

    items = None

    def __init__(self, record):
        super(Account, self).__init__(record)
        self.items = []


class AccountReport(Report):

    data = CompoundRecord(AccountRecord, ItemRecord, ItemInfoRecord,
                          ItemRemittance1Record, ItemRemittance2Record)

    _current_account = None
    """
    A helper pointer to the current account record (convenience, not necessity)
    """

    def _process_account(self, record):
        """
        Wrap an AccountRecord with a proxy. As we want to have this in the
        data list, we return the wrapped record. Also, we store the current
        account pointer for later convenience

        :param AccountRecord record:
        :return Account: The object proxy
        """
        self._current_account = Account(record)
        return self._current_account

    def _process_item(self, record):
        """
        Wraps the ItemRecord with a proxy, that aggregates all the other
        sub-records. Since this is subordinated to the Account instance, we
        don't return the object

        :param ItemRecord record:
        """
        self._current_account.items.append(AccountItem(record))
        return None

    def _process_iteminfo(self, record):
        """
        Add this record as an attribute of AccountItem object
        :param ItemInfoRecord record:
        """
        self._current_account.items[-1].info = record
        return None

    def _process_itemremittance1(self, record):
        """
        Add this record as an attribute of AccountItem object
        :param ItemRemittance1Record record:
        """
        self._current_account.items[-1].rem1 = record
        return None

    def _process_itemremittance2(self, record):
        """
        Add this record as an attribute of AccountItem object
        :param ItemRemittance2Record record:
        """
        self._current_account.items[-1].rem2 = record
        return None

    def process_data(self, record):
        """
        Handles the processing of the `data` field, when in this case all
        records are stored. Basically, we wrap the linear into a hierarchical
        structure for easier use later-on.

        :param Record record: The record to process
        :return Account: Either a new Account instance, or nothing at all, if
            the processing is happening internally
        """
        switch = {
            'AccountRecord': self._process_account,
            'ItemRecord': self._process_item,
            'ItemInfoRecord': self._process_iteminfo,
            'ItemRemittance1Record': self._process_itemremittance1,
            'ItemRemittance2Record': self._process_itemremittance2,
        }[record.__class__.__name__]

        return switch(record)