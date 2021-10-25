grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
total = 0
amount = len(grades)
avarage = 0

for grade in grades:
    total += grade

avarage = total / amount

print(f"Average: {avarage:.2f}")
