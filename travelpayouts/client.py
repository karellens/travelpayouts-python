import functools
import urllib.request
import json
try: # Python 3
    from urllib.parse import urlencode
except ImportError: # Python 2
    from urllib import urlencode


class Client(object):
    """Performs requests to the Travel Payouts API."""

    def __init__(self, token=None):
        """
        :param token: Travel Payouts API token
        :type token: string
        """

        self.token = token

    def _request(self, url, params):
        params['token'] = self.token

        with urllib.request.urlopen(url) as r:
            return json.loads(r.read().decode())


from travelpayouts.common import whereami


def make_api_method(func):
    """
    Provides a single entry point for modifying all API methods.
    For now this is limited to allowing the client object to be modified
    with an `extra_params` keyword arg to each method, that is then used
    as the params for each web service request.

    Please note that this is an unsupported feature for advanced use only.
    It's also currently incompatibile with multiple threads, see GH #160.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args[0]._extra_params = kwargs.pop("extra_params", None)
        result = func(*args, **kwargs)
        try:
            del args[0]._extra_params
        except AttributeError:
            pass
        return result
    return wrapper

Client.whereami = make_api_method(whereami)
