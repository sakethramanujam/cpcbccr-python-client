import cpcbccr as cpcb
import pytest


def test_get_states():
    states = cpcb.get_states()
    assert len(states) > 0


def test_get_cities_success():
    cities = cpcb.get_cities('Assam')
    assert cities == ['Guwahati']


def test_get_cities_failure():
    with pytest.raises(Exception):
        cpcb.get_cities('qwerty')


def test_get_stations_success():
    stations = cpcb.get_stations('Guwahati')
    assert stations == [{'id': 'site_5073',
                         'live': True,
                         'name': 'Railway Colony, Guwahati - APCB'}]


def test_get_stations_failure():
    with pytest.raises(Exception):
        cpcb.get_stations('qwerty')
