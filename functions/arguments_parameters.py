def add(x, y):
    result = x + y
    return result

print(add(1,2))


def divide(dividend = 10, divisor = 2):
    if divisor != 0:
        result = dividend / divisor
        return result

print(divide(100,10))
print(divide(dividend = 20, divisor = 4))
