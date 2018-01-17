import functools
import requests
from urllib.parse import urlencode


class Client(object):
    """Performs requests to the Travel Payouts API."""

    def __init__(self, token=None):
        """
        :param token: Travel Payouts API token
        :type token: string
        """

        self.token = token

    def _request(self, url, params=None):

        headers = {
            'Content-Type': 'application/json',
            'X-Access-Token': self.token,
            'Accept-Encoding': 'gzip,deflate,sdch'
        }

        full_url = url + '?' + urlencode(params) if params else url
        r = requests.get(full_url, headers=headers)

        return r.json()


from travelpayouts.common import whereami
from travelpayouts.common import countries
from travelpayouts.common import cities
from travelpayouts.common import airports
from travelpayouts.common import airlines
from travelpayouts.common import airlines_alliances
from travelpayouts.common import planes
from travelpayouts.common import routes
from travelpayouts.v2 import prices_latest
from travelpayouts.v2 import month_matrix
from travelpayouts.v2 import week_matrix
from travelpayouts.v2 import nearest_places_matrix


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
Client.countries = make_api_method(countries)
Client.cities = make_api_method(cities)
Client.airports = make_api_method(airports)
Client.airlines = make_api_method(airlines)
Client.airlines_alliances = make_api_method(airlines_alliances)
Client.planes = make_api_method(planes)
Client.routes = make_api_method(routes)
Client.prices_latest = make_api_method(prices_latest)
Client.month_matrix = make_api_method(month_matrix)
Client.week_matrix = make_api_method(week_matrix)
Client.nearest_places_matrix = make_api_method(nearest_places_matrix)
