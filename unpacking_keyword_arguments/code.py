# Dictionary unpacking
def named(**kwargs):
    print(kwargs)

details = {"name": "Bob", "age": 45}


def print_nicely(**kwargs):
    named(**kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_nicely(name= "Bob", age= 45)


def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 2, 3, name="Bob", age="30")


def test(**kwargs):
    print(kwargs)


