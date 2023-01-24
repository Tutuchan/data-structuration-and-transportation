import csv
import pandas as pd

class Station:

    def __init__(self, rank: int, network: str, name: str, number_of_users: int, connections: list[str], city: str,
                 district: int | None):
        self.rank = rank
        self.network = network
        self.name = name
        self.number_of_users = number_of_users
        self.connections = connections
        self.city = city
        self.district = district




df = pd.read_csv("/Users/shubhamrangadal/Desktop/Class course/data structuration/data-structuration-and-transportation/resources/csv/ratp.csv")
print(df)

# with open(
#         "/Users/shubhamrangadal/Desktop/Class course/data structuration/data-structuration-and-transportation/resources/csv/ratp.csv",
#         "r") as file:
#     csvreader = csv.DictReader(file)
#
#     for col in csvreader:
#         print(col)
#
#
#     # aList.pop(0)
#     #
#     # lstOfUsers = []
#     #
#     # for i in aList:
#     #     user = Users(id=i[0], name=i[1], city=i[2], school=i[3])
#     #     lstOfUsers.append(user)
#     #
#     # for j in lstOfUsers:
#     #     print(j.__str__())