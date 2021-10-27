def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(1,2,3,4))


def add(x, y):
    return x + y

# nums = [1, 2]
# print(add(*nums))

nums = {"x": 1, "y": 2}
print(add(**nums))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "Unknown operator"

print(apply(1,2,3,4, operator="+"))
