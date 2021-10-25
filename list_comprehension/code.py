numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

print(doubled)
##########################
friends = ["Rolf", "Bob", "Jen", "John", "Jimmy"]
start_j = [friend for friend in friends if friend.startswith("J")]

print(start_j)

print(f"friends: {id(friends)}, start_j: {id(start_j)}," )
