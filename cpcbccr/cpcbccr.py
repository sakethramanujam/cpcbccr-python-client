import os
from typing import List, Union
import requests
import pandas as pd


API_URL = "https://love-the-air.herokuapp.com/api"

def get_states() -> List[str]:
    """
    Returns a List of Available States

    Examples
    --------
    >>> states = client.get_states()
    >>> states
    ['Andhra Pradesh','Karnataka', 'Assam',....]
    """
    try:
        r = requests.get(f'{API_URL}/states')
        status = r.status_code
        if status != 200:
            raise Exception(f'failed to fetch states {r.status_code}')
        return r.json()['states']
    except Exception as e:
        print(e)


def get_cities(state: str) -> List[str]:
    """
    Return a list of cities in given state

    Parameters
    ----------
    state : string
            Name of the state for which, 
            the names of cities are required

    Examples
    --------
    Obtaining Cities using state name

    >>> cities = client.get_cities(state='Kerala')
    >>> cities
    ['Eloor', 'Ernakulam', 'Kannur', 'Kochi', 'Kollam', 'Kozhikode', 'Thiruvananthapuram']
    """
    try:
        r = requests.get(f'{API_URL}/state/{state}')
        status = r.status_code
        if status != 200:
            raise Exception(f'failed to fetch cities with status:{status}')
        return r.json()['cities']
    except Exception as e:
        print(e)


def get_stations(city: str) -> List[dict]:
    """
    Return list of dictionary for each station in a given city
    Parameters
    ----------
    city: str
          Name of the city for which, 
          the names of stations and station codes
          are required

    Examples
    --------
    Obtaining stations using city name
    >>> stations = client.get_stations('Kollam')
    >>> stations
    [{'id': 'site_5334', 'live': True, 'name': 'Polayathode, Kollam - Kerala PCB'}]
    """
    try:
        r = requests.get(f'{API_URL}/city/{city}')
        status = r.status_code
        if status != 200:
            raise Exception(f'failed to fetch stations with status:{status}')
        return r.json()['stations']
    except Exception as e:
        print(e)


def get_data(from_date: str, to_date: str,
             station_id: str, criteria: str) -> pd.DataFrame:
    """
    Return a pandas dataframe for selected station in given 
    time range.

    Parameters
    ----------
    from_date : str/ISO datetime
                Starting Date from which data is required
    to_date : str/ISO datetime
              End Date until which the date is required
    station_id : str
                 Station Id as listed in the station dictionary
    criteria: str
              Frequency of data required
              Supported Criteria
                - 24 Hours
                - 8 Hours
                - 4 Hours
                - 1 Hours
                - 30 Minute
                - 15 Minute 
    Examples
    --------
    >>> data = client.get_data(from_date='01-01-2020', 
                               to_date='01-01-2020',
                               criteria='24 Hours', 
                               station_id='site_273')  
    >>> data
     from date     AT      BP Benzene     NO    NO2    NOx  Ozone   PM2.5     RH    SO2     SR Toluene    VWS      WD    WS Xylene              to date
0  01-Jan-2020 - 00:00  15.57  732.58    8.03  21.52  59.95  30.89  28.57  274.89  76.24  17.72  58.18   15.94  -1.33  188.71  0.76   9.93  02-Jan-2020 - 00:00

    """
    payload = {
        "from_date": from_date,
        "to_date": to_date,
        "station_id": station_id,
        "criteria": criteria
    }
    try:
        r = requests.post(f'{API_URL}/data', json=payload)
        status = r.status_code
        if status == 422:
            print(r.json())
        elif status == 200:
            return _format(json=r.json())
    except Exception as e:
        print(e)


def _format(json: dict) -> pd.DataFrame:
    """
    Return a well formatted Dataframe from json

    Parameters
    ----------
    json: json response from request response
    """
    data = json['data']
    df = pd.DataFrame(data=data).drop('exceeding', axis=1)
    columns = []
    for _, col in enumerate(df.columns):
        if '_' in col:
            col = col.split('_')[-1]
        columns.append(col)
    df.columns = columns
    return df
