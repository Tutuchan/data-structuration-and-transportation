# Tilak Basnet  (tilak.basnet@epita.fr)
import requests
import json
from airflow.decorators import dag, task
from datetime import datetime, date
from time import mktime

@dag(
  start_date=datetime(2023, 1, 21),
  schedule_interval="0 1 * * *",  
)
def assignment_of_esay_flights():

  BASE_URL = "https://opensky-network.org/api"

  def sinceEpoch(inputDate: str) -> int:
    return int(mktime(date.fromisoformat(inputDate).timetuple()))

  # writing to file in flightseasy.json
  
  @task
  def write_data(flights: dict) -> None:
    with open("./dags/flightsEasy.json", "w") as f:
      json.dump(flights["flights"], f)


  # Reading data from  form the flights departure
  @task(multiple_outputs=True)
  def read_data() -> dict:
    params = {
        "airport": "LFPG", 
        "begin": sinceEpoch("2022-12-01"),
        "end": sinceEpoch("2022-12-02")
    }
    flightOfCDG = f"{BASE_URL}/flights/departure"
    response = requests.get(flightOfCDG, params=params)
    flights = response.json()
    print(json.dumps(flights))
    return {"flights": flights}

  flights = read_data()
  write_data(flights)

_ = assignment_of_esay_flights()