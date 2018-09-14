import functools
import requests
from urllib.parse import urlencode
from travelpayouts.exceptions import ApiError


class Client(object):
    """Performs requests to the Travel Payouts API."""

    def __init__(self, token=None, marker=None):
        """
        :param token: Travel Payouts API token
        :type token: string
        :param marker: The unique identifier of the affiliate
        :type marker: string
        """

        self.token = token
        self.marker = marker
        self.default_headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Content-Type': 'application/json',
            'X-Access-Token': self.token
        }

    def _get(self, url, params=None):

        full_url = url + '?' + urlencode(params) if params else url
        r = requests.get(full_url, headers=self.default_headers)

        return r.json()

    def _post(self, url, params=None, json=None):

        full_url = url + '?' + urlencode(params) if params else url
        r = requests.post(full_url, headers=self.default_headers, json=json)

        if not r.ok:
            raise ApiError(r.status_code, r.text)

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
from travelpayouts.v1 import prices_cheap
from travelpayouts.v1 import prices_direct
from travelpayouts.v1 import prices_calendar
from travelpayouts.v1 import airline_directions
from travelpayouts.v1 import city_directions
from travelpayouts.flights import search
from travelpayouts.flights import search_results


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
Client.prices_cheap = make_api_method(prices_cheap)
Client.prices_direct = make_api_method(prices_direct)
Client.prices_calendar = make_api_method(prices_calendar)
Client.airline_directions = make_api_method(airline_directions)
Client.city_directions = make_api_method(city_directions)
Client.search = make_api_method(search)
Client.search_results = make_api_method(search_results)
