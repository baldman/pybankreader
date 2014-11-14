

class ProxyMixin(object):
    """
    A very simple proxy class that holds an object and proxies all attribute
    gets to that object. No setting of attributes allowed
    """

    _proxy = None

    def __init__(self, record):
        """
        Stores the object in the proxy

        :param object record:
        """
        self._proxy = record

    def __getattr__(self, item):
        """
        Proxy to the internal object record

        :param string item: the proxy attribute value
        :return:
        """
        return getattr(self._proxy, item)