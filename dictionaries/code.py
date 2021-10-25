# Dictionaries are like objects

student_attendance = {
    "Rolf": 96,
    "Bob": 80,
    "Anne": 100,
}

# for student in student_attendance:
#     print(f"{student}: {student_attendance[student]}%")

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}%")


if "Bob" in student_attendance:
    print("Bob is in the class")
else:
    print("Bob is not in the class")

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))
