from typing import List

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


grades: List = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

print("Welcome to the average grade program.")

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e_message:
    print("There are no grades yet in your list.")
    print(e_message)
else:
    print(f"The average grade is {average:.3f}")
finally:
    print("Thank you for using the average grade program.")

