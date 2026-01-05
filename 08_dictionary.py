students = {
    10234: "Amitoz",
    10235: "Aman",
    10236: "Amar",
    11234: "Harmeet",
    11236: "Harkirat",
    14987: "Mandeep"
}

# print(students[11236])
# print(students[10236])

# students[28976] = "Palminder"
# print(students)
# print(students[28976])

# students[28976] = "Student"
# # print(students[3434234])
# print(students.get(3434234, "Sorry no student exists"))
# print("Hello World")

# del students[28976]
# print(students)

for k, v in students.items():
    print(f"Roll No: {k}, Name: {v}")

for key in sorted(students.keys()):
    print(key)

for value in students.values():
    print(value)