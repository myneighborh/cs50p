students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# Uses list comprehension
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
print("----------")


# Uses enumerate
for i, gryffindor in enumerate(sorted(gryffindors)):
    print(i + 1, gryffindor)
print("----------")


# Uses filter
def is_gryffindor(s):
    return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key= lambda s: s["name"]):
    print(gryffindor["name"])
print("----------")


# Uses lambda
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key= lambda s: s["name"]):
    print(gryffindor["name"])
print("----------")


# Uses list comprehension to make list of dictionaries
students = ["Hermione", "Harry", "Ron"]
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors)
print("----------")


# Uses dictionary comprehension to make a dictionary
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)
