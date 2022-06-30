# programming_Dictionary = {
# "Bug": "An error in a program that prevents the program from running as expected",
# "Function": "A piece of code that you can easily call over and over again.",
# }

# # print(programming_Dictionary["Bug"])
# #adding to the dictionary
# programming_Dictionary["Loop"] = "Doing something over and over again"
# #wiping an existing dictionary
# # empty_Dictionary = {}
# # programming_Dictionary = empty_Dictionary
# # print(programming_Dictionary)

# #editing
# programming_Dictionary["Bug"] = "A moth in ur computer"
# print(programming_Dictionary)
# for key in programming_Dictionary:
#     print(key)
#     print(programming_Dictionary[key])

from dataclasses import asdict
from turtle import st


student_Scores = {
    "Harry":81,
    "Ron": 78,
    "Hermione": 99,
    "Draco":74,
    "Neville": 62,
}

student_Grades = {}

for student in student_Scores:
    print(student)
    score = student_Scores[student]
    if score > 90:
        student_Grades[student] = "Outstanding"
    elif score > 81:
        student_Grades[student] = "Exceeds expectations"
    elif score >71: 
        student_Grades[student] = "acceptable"
    elif score <70:
        student_Grades[student] = "fail"
print(student_Grades)