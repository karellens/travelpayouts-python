import hashlib


API_V1_URL = 'http://api.travelpayouts.com/v1'
ECONOMY_CLASS = 'Y'
BUSINESS_CLASS = 'B'


def _sorted_glue(od):
    vals = list()
    for k, v in sorted(od.items()):
        if isinstance(v, dict):
            vals.append(_sorted_glue(v))
        elif isinstance(v, list):
            for one in v:
                vals.append(_sorted_glue(one))
        else:
            vals.append(v)

    return ':'.join(vals)


def _signature(body, token):
    m = hashlib.md5()
    m.update((token+':'+_sorted_glue(body)).encode('utf-8'))

    return m.hexdigest()


def search(client,
           segments,
           passengers,
           host,
           user_ip,
           locale='en',
           trip_class=ECONOMY_CLASS,
           currency='usd'
           ):

    passengers = {k: passengers[k] for k in passengers.keys() if k in ['adults', 'children', 'infants']}

    body = {
        'segments': segments,
        'passengers': passengers,
        'host': host,
        'user_ip': user_ip,
        'locale': locale,
        'trip_class': trip_class,
        'currency': currency,
        'marker': client.marker
    }

    body['signature'] = _signature(body, client.token)

    data = client._post(API_V1_URL + "/flight_search", json=body)

    return data


def search_results(client, search_uuid):
    params = {"uuid": search_uuid}

    data = client._get(API_V1_URL + "/flight_search_results", params)

    return data
