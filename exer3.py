import csv


class Users:

    def __init__(self, id: str, name: str, city: str, school: str):
        self.id = id
        self.name = name
        self.city = city
        self.school = school

    def __str__(self):
        return self.id + " " + self.name + " " + self.city + " " + self.school



with open(
        "/Users/shubhamrangadal/Desktop/Class course/data structuration/data-structuration-and-transportation/resources/csv/users.csv",
        "r") as file:
    csvreader = csv.reader(file)
    aList = list(csvreader)
    aList.pop(0)

    lstOfUsers = []

    for i in aList:
        user = Users(id=i[0], name=i[1], city=i[2], school=i[3])
        lstOfUsers.append(user)

    for j in lstOfUsers:
        print(j.__str__())


