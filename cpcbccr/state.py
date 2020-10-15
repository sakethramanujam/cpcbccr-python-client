from .tools import get
from .city import City
from .config import API_URL
from typing import List


class State:
    def __init__(self, state: str):
        self.state = state

    def __repr__(self):
        return f"<object {self.state} from cpcbccr client>"

    def get_cities(self) -> List[City]:
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
        r = get(f'{API_URL}/state/{self.state}')
        status = r.status_code
        if status != 200:
            raise Exception(f'failed to fetch cities with status:{status}')
        if status == 200 and r.json() is None:
            r = get(f'{API_URL}/state/{self.state}')
        cities = [City(city) for city in r.json()['cities']]
        return cities
