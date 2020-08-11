student_attendance = {"Rolf":96, "Bob":80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

people = [("Bob", 42, "Mechanic"),  ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

person = ("Bob", 42, "Mechanic")
name2, _, profession2 = person # _ will be skipped over.
print(name2, profession2)

head, *tail = [1, 2, 3, 4, 5]

print(head)
print(tail)
