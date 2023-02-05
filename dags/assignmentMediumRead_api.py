#Tilak Basnet
from datetime import datetime, date, timedelta
from time import mktime

import requests


def read_data_from_api():
    BASE_URL = "https://api.open-meteo.com/"
    # These are random data using for parametrs
    params = {
        "latitude": "52.55",
        "longitude": "6.45",
        "per_hour": "temperature"
    }
# BASE URL for the display data on browser https://api.open-meteo.com/v1/forcast
    forecast = f"{BASE_URL}/v1/forecast"
    response = requests.get(forecast, params=params)

    request = response.json();
    return request


def since_epoch(input_date: str) -> int:
    return int(mktime(date.fromisoformat(input_date).timetuple()))