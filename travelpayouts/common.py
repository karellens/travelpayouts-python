BASE_URL = 'http://www.travelpayouts.com'
API_DATA_URL = 'http://api.travelpayouts.com/data'


def whereami(client, ip, locale='en', callback=None):
    locale = locale if locale in ['en', 'ru', 'de', 'fr', 'it', 'pl', 'th'] else 'en'

    params = {
        'ip': ip,
        'locale': locale
    }

    if callback:
        params["callback"] = callback

    return client._get(BASE_URL+"/whereami", params)


def countries(client):
    """Returns a file with a list of countries from the database.

    :rtype: list of countries
    """

    data = client._get(API_DATA_URL+"/countries.json")

    return data


def cities(client):
    """Returns a file with a list of cities from the database.

    :rtype: list of cities
    """

    data = client._get(API_DATA_URL+"/cities.json")

    return data


def airports(client):
    """Returns a file with a list of airports from the database.

    :rtype: list of airports
    """

    data = client._get(API_DATA_URL+"/airports.json")

    return data


def airlines(client):
    """Returns a file with a list of airlines from the database.

    :rtype: list of airports
    """

    data = client._get(API_DATA_URL+"/airlines.json")

    return data


def airlines_alliances(client):
    """Returns a file with a list of alliances from the database.

    :rtype: list of alliances
    """

    data = client._get(API_DATA_URL+"/airlines_alliances.json")

    return data


def planes(client):
    """Returns a file with a list of airplanes from the database.

    :rtype: list of airplanes
    """

    data = client._get(API_DATA_URL+"/planes.json")

    return data


def routes(client):
    """Returns a file with a list of routes from the database.

    :rtype: list of routes
    """

    data = client._get(API_DATA_URL+"/routes.json")

    return data
