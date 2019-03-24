.. begin_intro

TravelPayouts
=============

.. image:: https://badge.fury.io/py/travelpayouts.svg
    :target: https://badge.fury.io/py/travelpayouts

`TravelPayouts API <https://support.travelpayouts.com/hc/ru/categories/200358578-%D0%A0%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81-API>`__ wrapper.

.. end_intro

.. begin_installation

Installation
------------

The recommended way to install is via `pip <http://pypi.python.org/pypi/pip>`_

.. code-block:: bash

   $ pip install travelpayouts

.. end_installation

.. begin_usage

Usage
---------------

.. code-block:: python

    from travelpayouts import Client

    client = Client('TOKEN', 'MARKER')

    client.whereami('123.456.789.123')  # ip


Entrypoints
^^^^^^^^^^^^^^^

Common:

- `whereami <https://support.travelpayouts.com/hc/en-us/articles/205895898-How-to-determine-the-user-s-location-by-IP-address>`_

- `countries <https://support.travelpayouts.com/hc/en-us/articles/203956163-Travel-insights-with-Travelpayouts-Data-API#data_of_countries>`_

- `cities <https://support.travelpayouts.com/hc/en-us/articles/203956163-Travel-insights-with-Travelpayouts-Data-API#data_of_city>`_

- `airports <https://support.travelpayouts.com/hc/en-us/articles/203956163-Travel-insights-with-Travelpayouts-Data-API#data_of_airport>`_

- `airlines <https://support.travelpayouts.com/hc/en-us/articles/203956163-Travel-insights-with-Travelpayouts-Data-API#data_of_airline>`_

- `airlines_alliances <https://support.travelpayouts.com/hc/en-us/articles/203956163-Travel-insights-with-Travelpayouts-Data-API#data_of_alliance>`_

- `planes <https://support.travelpayouts.com/hc/en-us/articles/203956163-Travel-insights-with-Travelpayouts-Data-API#data_of_airplane>`_

- `routes <https://support.travelpayouts.com/hc/en-us/articles/203956163-Travel-insights-with-Travelpayouts-Data-API#data_of_routes>`_

V1:

- not implemented yet...

V2:

- `prices_latest <https://support.travelpayouts.com/hc/en-us/articles/203956163-Travel-insights-with-Travelpayouts-Data-API#the_prices_for_the_airline_tickets>`_

- `month_matrix <https://support.travelpayouts.com/hc/en-us/articles/203956163-Travel-insights-with-Travelpayouts-Data-API#the_calendar_of_prices_for_a_month>`_

- `week_matrix <https://support.travelpayouts.com/hc/en-us/articles/203956163-Travel-insights-with-Travelpayouts-Data-API#the_calendar_of_prices_for_a_week>`_

- `nearest_places_matrix <https://support.travelpayouts.com/hc/en-us/articles/203956163-Travel-insights-with-Travelpayouts-Data-API#the_prices_for_the_alternative_directions>`_

`Flights <https://support.travelpayouts.com/hc/en-us/articles/203956173-Flights-search-API-Real-time-and-multi-city-search#03>`_:

- search

- search_results

.. end_usage