# # original, simplest form
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

# sorted way
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         # We can combine this three lines of code into one line
#         # student = {}
#         # student['name'] = name
#         # student['house'] = house
#         student = {"name": name, "house": house}
#         students.append(student)

# # # original version
# # def get_house(student):
# #     return student["house"]

# # for student in sorted(students, key = get_house):
# #     print(f"{student['name']} is in {student['house']}")
# # lambda version
# for student in sorted(students, key = lambda student: student["house"]):
#     print(f"{student['name']} is in {student['house']}")

#write to csv file:
import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames= ["name", "home"] )
    writer.writerow({"name": name, "home": home})