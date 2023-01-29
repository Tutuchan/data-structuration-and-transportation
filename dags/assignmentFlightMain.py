# Tilak Basnet  (tilak.basnet@epita.fr)

from airflow.decorators import dag, task
import requests
import json
from datetime import datetime, date
from time import mktime


@dag(
  schedule=None,
  dateOfStart=datetime(2023, 1, 24),
  catchup=False
)
def assignment_of_main_flight():

  URL = "https://opensky-network.org/api"

  def sinceEpoch(dateOfInput: str) -> int:
    return int(mktime(date.fromisoformat(dateOfInput).timetuple()))

# Write the input data in the json file 
  @task
  def dataWrite(flights: str) -> None:
    data = json.loads(flights)
    with open("./dags/flightsMain.json", "w") as f:
      json.dump(data, f)

# Read data from the json file
  @task(multple_output= True)
  def dataRead() -> str:
    params = {
        "airport": "LFPG", 
        "begin": sinceEpoch("2022-12-01"),
        "end": sinceEpoch("2022-12-02")
    }
    flightsCDG = f"{URL}/flights/departure"
    response = requests.get(flightsCDG, params=params)
    flights = json.dumps(response.json())
    print(flights)
    return flights



  flights = dataRead()
  dataWrite(flights)

_ = assignment_of_main_flight()
