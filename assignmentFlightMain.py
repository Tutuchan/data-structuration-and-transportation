# Tilak Basnet  (tilak.basnet@epita.fr)

from airflow.decorators import dag, task
import requests
import json
from datetime import datetime, date
from time import mktime

@dag(
  schedule=None,
  start_date=datetime(2023, 1, 24),
  catchup=False
)
def assignment_of_main_flight():

  BASE_URL = "https://opensky-network.org/api"

  def sinceEpoch(dateOfInput: str) -> int:
    return int(mktime(date.fromisoformat(dateOfInput).timetuple()))


# Read data from the json file
  @task
  def read_data() -> str:
    params = {
        "airport": "LFPG", 
        "begin": sinceEpoch("2022-12-01"),
        "end": sinceEpoch("2022-12-02")
    }
    flightsCDG = f"{BASE_URL}/flights/departure"
    response = requests.get(flightsCDG, params=params)
    flights = json.dumps(response.json())
    print("Flights:"+flights)
    return flights

# Write the input data in the json file 
  @task
  def write_data(flights: str) -> None:
    data = json.loads(flights)
    with open("./dags/flightsMain.json", "w") as f:
      json.dump(data, f)

  write_data(read_data())

_ = assignment_of_main_flight()
