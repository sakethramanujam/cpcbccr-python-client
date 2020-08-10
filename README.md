# :rocket: CPCB CCR client

An unofficial python client to obtain data from the CPCB's CCR platform directly into your python environment. 


## Installation

```bash
$ pip install cpcbccr
```
## Usage

- Importing

```
>>> import cpcbccr as cpcb
```

- Get States

```
>>> states = cpcb.get_states()
```
- Get Cities

```
>>> cities = cpcb.get_cities(state='Punjab')
```
-  Get Stations

```
>>> stations = cpcb.get_stations(city='Amritsar')
```

- Get Data
```
>>> data = cpcb.get_data(from_date='01-01-2020',
                         to_date='02-01-2020',
                         station_id='site_279',
                         criteria='24 Hours')

```
> For more supported criteria check `doc-strings`



Made with [Python]('https://www.python.org/')
  - [requests](https://pypi.org/project/requests/)
  - [pandas](https://pypi.org/project/pandas/)