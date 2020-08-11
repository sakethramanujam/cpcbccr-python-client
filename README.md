# CPCB CCR client

An unofficial python client to obtain data from the [CPCB's CCR](https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing/caaqm-comparison-data) platform directly into your python environment.


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
> For more supported criteria check `doc-string.`

-  Save Data

```
>>> cpcb.save_data(path='/path/to/file.csv', 
                   from_date='01-01-2020',
                   end_date = '02-01-2020',
                   station_id = 'site_279',
                   criteria = '24 Hours')
```
> Supported Fileformats: `csv`, `xlsx`, `json`


## License

[MIT License](LICENSE)

## Contributing

If you find an issue please report/file an issue [here](https://github.com/sakethramanujam/cpcbccr-python-client/issues/new/choose) or file a pr [here](https://github.com/sakethramanujam/cpcbccr-python-client/compare)

## Credits
Made with [Python]('https://www.python.org/')
  - [requests](https://pypi.org/project/requests/)
  - [pandas](https://pypi.org/project/pandas/)
