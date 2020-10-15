from .station import Station
from .config import API_URL
from .tools import get
from typing import List

class City:
    def __init__(self,city:str):
        self.city = city
    
    def __repr__(self):
        return f"<{self.city} object>"
    
    def get_stations(self) -> List[Station]:
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
        r = get(f'{API_URL}/city/{self.city}')
        status = r.status_code
        if status != 200:
            raise Exception(f'failed to fetch stations with status:{status}')
        stations = [Station(station['id'],station['name'],station['live']) for station in r.json()['stations']]
        return stations
