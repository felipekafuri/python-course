# number = 7

# while True:
#     user_input = input("Would you like to play? (Y/n) ").lower()

#     if user_input == "n":
#         break

#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly!")
#     elif abs(number - user_number) == 1:
#         print("You were off by one.")
#     else:
#         print("Sorry, it's wrong!")


friends = ["Jim", "Karen", "Kevin", "Felipe"]

for friend in friends:
    print(f"{friend} is my friend")

print("\nUsing range for")
for firend in range(2):
    print(f"{friend} is my friend")
