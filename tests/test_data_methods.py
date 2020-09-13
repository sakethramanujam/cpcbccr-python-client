import cpcbccr as cpcb
import pandas as pd
import pytest

expected_data = {'from date': {0: '01-Jan-2020 - 00:00'},
                 'AT': {0: '15.57'},
                 'BP': {0: '732.58'},
                 'Benzene': {0: '8.03'},
                 'NO': {0: '21.52'},
                 'NO2': {0: '59.95'},
                 'NOx': {0: '30.89'},
                 'Ozone': {0: '28.57'},
                 'PM2.5': {0: '274.89'},
                 'RH': {0: '76.24'},
                 'SO2': {0: '17.72'},
                 'SR': {0: '58.18'},
                 'Toluene': {0: '15.94'},
                 'VWS': {0: '-1.33'},
                 'WD': {0: '188.71'},
                 'WS': {0: '0.76'},
                 'Xylene': {0: '9.93'},
                 'to date': {0: '02-Jan-2020 - 00:00'}}


def test_get_data_success():
    data = cpcb.get_data(from_date='01-01-2020', to_date='01-01-2020',
                         criteria='24 Hours', station_id='site_273')
    assert data.to_dict() == expected_data


def test_get_data_failure():
    with pytest.raises(Exception):
        cpcb.get_data(from_date='01-01-2020',
                      criteria='24 Hours', station_id='site_273')

    with pytest.raises(Exception):
        cpcb.get_data(to_date='01-01-2020',
                      criteria='24 Hours', station_id='site_273')
    with pytest.raises(Exception):
        cpcb.get_data(from_date='01-01-2020', to_date='01-01-2020',
                      criteria='24 Hours')
