from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f'Could not find an element with {expected}')


friends = [
    {"name": "Rolf Smith", "age": 25},
    {"name": "Adam Wolf", "age": 30},
    {"name": "Anna", "age": 28}
]

def get_friend_name(friend):
    return friend["name"]

try:
    found_friend = search(friends, "Rolf Smith", itemgetter("name"))
except RuntimeError as err:
    print(err)
else:
    print(found_friend)
finally:
    print("Clean up code goes here")


