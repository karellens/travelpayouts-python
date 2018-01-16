import datetime

BASE_URL = 'http://www.travelpayouts.com'
API_DATA_URL = 'http://api.travelpayouts.com/data'
API_V1_URL = 'http://api.travelpayouts.com/v1'
API_V2_URL = 'http://api.travelpayouts.com/v2'


def whereami(client, ip, locale='en', callback=None):
    locale = locale if locale in ['en', 'ru', 'de', 'fr', 'it', 'pl', 'th'] else 'en'

    params = {
        'ip': ip,
        'locale': locale
    }

    if callback:
        params["callback"] = callback

    return client._request(BASE_URL+"/whereami", params)


def prices_latest(client,
                  currency='usd',
                  origin=None,
                  destination=None,
                  beginning_of_period=None,
                  period_type='month',
                  one_way=False,
                  page=1,
                  limit=30, # max 1000
                  show_to_affiliates=True,
                  sorting='price',
                  trip_duration=None
                  ):
    params = {
        'currency': currency,
        'one_way': one_way,
        'page': page,
        'limit': limit,
        'show_to_affiliates': show_to_affiliates,
        'sorting': sorting
    }

    if trip_duration:
        params["trip_duration"] = trip_duration

    if origin:
        params["origin"] = origin

    if destination:
        params["destination"] = destination

    if beginning_of_period is None:
        if period_type == 'month':
            params["beginning_of_period"] = datetime.date.today().replace(day=1)
    else:
        params["beginning_of_period"] = beginning_of_period

    return client._request(API_V2_URL+"/prices/latest", params)

