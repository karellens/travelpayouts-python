import datetime
import travelpayouts.exceptions

API_V2_URL = 'http://api.travelpayouts.com/v2'


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
                  trip_class=0,
                  trip_duration=None
                  ):
    """Returns the cheapest non-stop, one-stop, and two-stop flights for the selected route for each day of
     the selected month.

    :param origin: the point of departure. The IATA city code or the country code. The length - from 2 to 3 symbols.
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

    :param limit: the total number of records on a page. The default value - 30. The maximum value - 1000.
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

    :param trip_class: trip class 0 - Economy, 1 - Business, 2 - First. Default value is 0. Should be in 0..2.
    :type trip_class: int

    :param trip_duration: the length of stay in weeks or days (for period_type=day).
    :type trip_duration: int

    :rtype: list of flights
    """
    params = {
        'currency': currency,
        'one_way': one_way,
        'page': page,
        'limit': limit,
        'show_to_affiliates': show_to_affiliates,
        'sorting': sorting,
        'trip_class': trip_class
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

    data = client._get(API_V2_URL+"/prices/latest", params)

    if 'success' in data:
        for v in data['data']:
            v['depart_date'] = datetime.datetime.strptime(v['depart_date'], "%Y-%m-%d").date()
            v['found_at'] = datetime.datetime.strptime('{:0<26.26}'.format(v['found_at'] + '.'), "%Y-%m-%dT%H:%M:%S.%f")
            v['return_date'] = datetime.datetime.strptime(v['return_date'], "%Y-%m-%d").date() \
                if v['return_date'] \
                else None

    else:
        raise travelpayouts.exceptions.ApiError(data['errors'])

    return data


def month_matrix(client,
                 currency='usd',
                 origin=None,
                 destination=None,
                 show_to_affiliates=True,
                 month=None
                 ):
    """Brings back the prices for each day of a month, grouped together by number of transfers.

    :param origin:  the point of departure. The IATA city code or the country code. The length - from 2 to 3 symbols.
    :type origin: string

    :param destination: the point of destination. The IATA city code or the country code.
        The length - from 2 to 3 symbols.
    :type destination: string

        Note! If the point of departure and the point of destination are not specified, the API shall bring back 30
        of the cheapest tickets that have been found during the most recent 48 hours.

    :param currency: the airline ticket’s The default value - RUB.
    :type currency: string

    :param month: the beginning of the month in the YYYY-MM-DD format.
    :type month: datetime.date

    :param show_to_affiliates: false - all the prices, true - just the prices,
        found using the partner marker (recommended). The default value - true.
    :type show_to_affiliates: bool

    :rtype: list of flights
    """
    params = {
        'currency': currency,
        'show_to_affiliates': show_to_affiliates,
    }

    if origin:
        params["origin"] = origin

    if destination:
        params["destination"] = destination

    if month is None:
        params["month"] = datetime.date.today().replace(day=1)
    else:
        params["month"] = month.strftime('%Y-%m-%d')

    data = client._get(API_V2_URL+"/prices/month-matrix", params)

    if 'success' in data:
        for v in data['data']:
            v['depart_date'] = datetime.datetime.strptime(v['depart_date'], "%Y-%m-%d").date()
            v['found_at'] = datetime.datetime.strptime('{:0<26.26}'.format(v['found_at'] + '.'), "%Y-%m-%dT%H:%M:%S.%f")
            v['return_date'] = datetime.datetime.strptime(v['return_date'], "%Y-%m-%d").date() \
                if v['return_date'] \
                else None

    else:
        raise travelpayouts.exceptions.ApiError(data['errors'])

    return data


def week_matrix(client,
                currency='usd',
                origin=None,
                destination=None,
                show_to_affiliates=True,
                depart_date=None,
                return_date=None,
                ):
    """Brings back the prices for the nearest dates to the target ones.

    :param origin:  the point of departure. The IATA city code or the country code. The length - from 2 to 3 symbols.
    :type origin: string

    :param destination: the point of destination. The IATA city code or the country code.
        The length - from 2 to 3 symbols.
    :type destination: string

        Note! If the point of departure and the point of destination are not specified, the API shall bring back 30
        of the cheapest tickets that have been found during the most recent 48 hours.

    :param currency: the airline ticket’s The default value - RUB.
    :type currency: string

    :param depart_date: (optional) day or month of departure (yyyy-mm-dd or yyyy-mm)..
    :type depart_date: string

    :param return_date: (optional) day or month of return (yyyy-mm-dd or yyyy-mm).
    :type return_date: string

    :rtype: list of flights
    """
    params = {
        'currency': currency,
        'show_to_affiliates': show_to_affiliates,
    }

    if origin:
        params["origin"] = origin

    if destination:
        params["destination"] = destination

    if depart_date:
        params["depart_date"] = depart_date

    if return_date:
        params["return_date"] = return_date

    data = client._get(API_V2_URL+"/prices/week-matrix", params)

    if 'success' in data:
        for v in data['data']:
            v['depart_date'] = datetime.datetime.strptime(v['depart_date'], "%Y-%m-%d").date()
            v['found_at'] = datetime.datetime.strptime('{:0<26.26}'.format(v['found_at'] + '.'), "%Y-%m-%dT%H:%M:%S.%f")
            v['return_date'] = datetime.datetime.strptime(v['return_date'], "%Y-%m-%d").date() \
                if v['return_date'] \
                else None

    else:
        raise travelpayouts.exceptions.ApiError(data['errors'])

    return data


def nearest_places_matrix(client,
                          currency='usd',
                          origin=None,
                          destination=None,
                          limit=1,
                          show_to_affiliates=True,
                          depart_date=None,
                          return_date=None,
                          flexibility=0,
                          distance=1,
                          ):
    """Brings back the prices for the directions between the nearest to the target cities.

    :param origin:  the point of departure. The IATA city code or the country code. The length - from 2 to 3 symbols.
    :type origin: string

    :param destination: the point of destination. The IATA city code or the country code.
        The length - from 2 to 3 symbols.
    :type destination: string

    :param currency: the airline ticket’s The default value - RUB.
    :type currency: string

    :param limit:  the number of variants entered, from 1 to 20, where 1 is just the variant with the specified points
        of departure and the points of destination.
    :type limit: int

    :param show_to_affiliates: false - all the prices, true - just the prices,
        found using the partner marker (recommended). The default value - true.
    :type show_to_affiliates: bool

    :param depart_date: (optional) month of departure (yyyy-mm-dd).
    :type depart_date: string

    :param return_date: (optional) month of return (yyyy-mm-dd).
    :type return_date: string

    :param flexibility: expansion of the range of dates upward or downward. The value may vary from 0 to 7,
        where 0 shall show the variants for the dates specified and 7 shall show all the variants
        found for a week prior to the specified dates and a week after.
    :type flexibility: int

    :param distance: the distance between the point of departure and the point of destination.
    :type distance: int

    :rtype: list of prices origins and destinations
    """
    params = {
        'currency': currency,
        'show_to_affiliates': show_to_affiliates,
        'origin': origin,
        'destination': destination,
        'limit': limit,
        'distance': distance,
        'flexibility': flexibility
    }

    if depart_date:
        params["depart_date"] = depart_date

    if return_date:
        params["return_date"] = return_date

    data = client._get(API_V2_URL+"/prices/nearest-places-matrix", params)

    try:
        for v in data['data']:
            v['depart_date'] = datetime.datetime.strptime(v['depart_date'], "%Y-%m-%d").date()
            v['found_at'] = datetime.datetime.strptime('{:0<26.26}'.format(v['found_at'] + '.'), "%Y-%m-%dT%H:%M:%S.%f")
            v['return_date'] = datetime.datetime.strptime(v['return_date'], "%Y-%m-%d").date() \
                if v['return_date'] \
                else None

    except KeyError:
        raise travelpayouts.exceptions.ApiError(data['errors'])

    return data
