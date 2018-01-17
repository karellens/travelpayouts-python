import datetime
import travelpayouts.exceptions

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
                  limit=30,
                  show_to_affiliates=True,
                  sorting='price',
                  trip_duration=None
                  ):
    """Returns the cheapest non-stop, one-stop, and two-stop flights for the selected route for each day of
     the selected month.

    :param origin:  the point of departure. The IATA city code or the country code. The length - from 2 to 3 symbols.
    :type origin: string

    :param destination: the point of destination. The IATA city code or the country code.
        The length - from 2 to 3 symbols.
    :type destination: string

        Note! If the point of departure and the point of destination are not specified, the API shall bring back 30
        of the cheapest tickets that have been found during the most recent 48 hours.

    :param currency: the airline ticket’s The default value - RUB.
    :type currency: string

    :param beginning_of_period: the beginning of the period, within which the dates of departure fall
        (in the YYYY-MM-DD format, for example, 2016-05-01). Must be specified if period_type is equal to month.
    :type beginning_of_period: datetime.date

    :param period_type: the period for which the tickets have been found (the required parameter):
        year — for the whole time;
        month — for a month.
    :type period_type: string

    :param one_way: true - one way, false - back-to-back. The default value - false.
    :type one_way: bool

    :param page: a page number. The default value - 1.
    :type page: int

    :param limit:  the total number of records on a page. The default value - 30. The maximum value - 1000.
    :type limit: int

    :param show_to_affiliates: false - all the prices, true - just the prices,
        found using the partner marker (recommended). The default value - true.
    :type show_to_affiliates: bool

    :param sorting: the assorting of prices:
        price — by the price (the default value). For the directions, only city -
            city assorting by the price is possible;
        route — by the popularity of a route;
        distance_unit_price — by the price for 1 km.
    :type sorting: string

    :param trip_duration: the length of stay in weeks or days (for period_type=day).
    :type trip_duration: int

    :rtype: list of prices
    """
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
        params["beginning_of_period"] = beginning_of_period.strftime('%Y-%m-%d')

    data = client._request(API_V2_URL+"/prices/latest", params)

    if data['success']:
        for v in data['data']:
            v['depart_date'] = datetime.datetime.strptime(v['depart_date'], "%Y-%m-%d").date()
            v['found_at'] = datetime.datetime.strptime(v['found_at'], "%Y-%m-%dT%H:%M:%S")
            v['return_date'] = datetime.datetime.strptime(v['return_date'], "%Y-%m-%d").date()

    else:
        raise travelpayouts.exceptions.ApiError(data['error'])

    return data

