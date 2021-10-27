print(devide(10,5))

add = lambda x, y: x + y

print(add(1,4))


print((lambda x, y: x * y)(2,3))

def double(x):
    return x * 2

sequence = [1, 2, 3, 4, 5]
doubled = [double(x) for x in sequence]
doubled = map(double, sequence)
double_sequence = map((lambda x: x * 2), sequence)


