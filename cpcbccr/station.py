import pandas as pd
from .tools import post
from .config import API_URL


class Station:
    def __init__(self, id:str, name:str, status:str):
        self.id = id
        self.name = name
        self.status = status
    
    def __repr__(self):
        return f"<{self.name} station object>"

    def get_data(self, from_date: str, to_date: str, criteria: str) -> pd.DataFrame:
        """
        Return a pandas dataframe for selected station in given 
        time range.

        Parameters
        ----------
        from_date : str/ISO datetime
                    Starting Date from which data is required
        to_date : str/ISO datetime
                End Date until which the date is required
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
        >>> data = station.get_data(from_date='01-01-2020', 
                                to_date='01-01-2020',
                                criteria='24 Hours', 
                                station_id='site_273')  
        >>> data
        from date     AT      BP Benzene ... to date
    0  01-Jan-2020 - 00:00  15.57  732.58 ... 02-Jan-2020 - 00:00

        """
        payload = {
            "from_date": from_date,
            "to_date": to_date,
            "station_id": self.id,
            "criteria": criteria
        }
        r = post(f'{API_URL}/data', json=payload)
        status = r.status_code
        if status == 422:
            print(r.json())
        elif status == 200:
            data = self._format(json_data=r.json())
            return data


    def _format(self,json_data: dict) -> pd.DataFrame:
        """
        Return a well formatted Dataframe from json

        Parameters
        ----------
        json_data: json response from request response
        """
        data = json_data['data']
        if not data:
            raise Exception("API returned empty data")
        else:
            df = pd.DataFrame(data=data).drop('exceeding', axis=1)
            columns = []
            for _, col in enumerate(df.columns):
                if '_' in col:
                    col = col.split('_')[-1]
                columns.append(col)
            df.columns = columns
            return df