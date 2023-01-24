class Users:
    id = ""
    name = ""
    city = ""
    school = ""

    def __str__(self):
        return self.id + " " + self.name + " " + self.city + " " + self.school

with open("/Users/shubhamrangadal/Desktop/Class course/data structuration/data-structuration-and-transportation/resources/fixed-length/users.txt", "r") as file:
    lines = file.read().splitlines()

lstOfUsers = []

for i in lines:
    user = Users()

    user.id = i[0:4].strip()
    user.name = i[4:30].strip()
    user.city = i[30:60].strip()
    user.school = i[60:].strip()

    lstOfUsers.append(user)

for j in lstOfUsers:
    print(j.__str__())



