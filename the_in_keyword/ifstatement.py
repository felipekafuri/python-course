number = 7
user_input = input("Would you like to play? (Y/n) ").lower()

if user_input == 'y':
    user_input = int(input("Guess our number: "))
    if user_input == number:
        print("You guessed correctly!")
    elif abs(number - user_input) == 1:
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!")

