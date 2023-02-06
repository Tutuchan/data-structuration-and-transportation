# Tilak Basnet
from airflow.decorators import dag, task
from datetime import datetime
from assignmentMediumRead_api import read_data_from_api

@dag(
    start_date = datetime(2023, 1, 11),
    schedule_interval = "0 1 * * *",
    catchup = False
)
# Reading the data form the assignmentMediumRead_api file which are random data 
def assignment_medium():
    @task(multiple_outputs=True)
    def read() -> dict:
        return read_data_from_api() 

# Transfer the filter data and append the time and teperature every hour
    @task
    def transformation_data(req) -> list:
        request = req
        temper = request['per_hour']
        time = temper['time']
        temperature = temper['temperature']
        filtered_data = []
        for i in range(0, len(time)):
            if temperature[i] < 0.0:
                filtered_data.append(time[i] + " " + str(temperature[i]))

        return filtered_data
# Create assignment_medium_output.txt file if does not exit
    @task
    def write(write_instance):
        with open('./dags/assignment_medium_output.txt', "w") as fp:
            for item in write_instance:
                fp.write("%s\n" % item)

    request = read()
    read_instance = transformation_data(request)
    write(read_instance)

_ = assignment_medium()