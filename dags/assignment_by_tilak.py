# Tilak Basnet  (tilak.basnet@epita.fr)

import requests
import json
from airflow.decorators import dag, task 
from datetime import datetime, date
from time import mktime


@dag(
  schedule=None,
  start_date=datetime(2023, 1, 24),
  catchup=False
)
def assignment():

  FLIGHT_URL = "https://opensky-network.org/api"

  def to_seconds_since_epoch(input_date: str) -> int:
    return int(mktime(date.fromisoformat(input_date).timetuple()))

  @task
  def read_data():
    params = {
        "airport": "LFPG", 
        "begin": to_seconds_since_epoch("2022-12-01"),
        "end": to_seconds_since_epoch("2022-12-02")
    }
    cdg_flights = f"{FLIGHT_URL}/flights/departure"
    response = requests.get(cdg_flights, params=params)
    flights = json.dumps(response.json())
    print(flights)
    return flights

  @task
  def write_data(flights: str) -> None:
    
    data = json.loads(flights)
    with open("./dags/flights.json", "w") as f:
      json.dump(data, f)

  flights = read_data()
  write_data(flights)

_ = assignment()