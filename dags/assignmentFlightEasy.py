# Tilak Basnet  (tilak.basnet@epita.fr)
# Note before execute the the this file install airfolw or run  docker and  docker composer file 

import requests
import json
from airflow.decorators import dag, task
from datetime import datetime, date
from time import mktime


@dag(
  dateOfStart=datetime(2023, 1, 21),
  scheduleOfinterval="0 1 * * *",  
)
def assignment_of_esay_flights():
  URL= "https://opensky-network.org/api"
  def sinceEpoch(inputDate: str) -> int:
    return int(mktime(date.fromisoformat(inputDate).timetuple()))

  # writing to file in flightseasy.json
  @task(multiple_outputs=True)
  @task
  def dataWrite(flights: dict) -> None:
    with open("./dags/flightsEasy.json", "w") as f:
      json.dump(flights["flights"], f)


  # Reading data from  form the flights departure
  @task(multiple_outputs=True)
  def dataRead() -> dict:
    params = {
        "airport": "LFPG", 
        "begin": sinceEpoch("2022-12-01"),
        "end": sinceEpoch("2022-12-02")
    }
    flightOfCDG = f"{URL}/flights/departure"
    response = requests.get(flightOfCDG, params=params)
    flights = response.json()
    print("Flights Json Data :"+ json.dumps(flights))
    return {"flights Data: ": flights}

  flights = dataRead()
  dataWrite(flights)

_ = assignment_of_esay_flights()
