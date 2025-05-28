import random

random_computer_number = random.randint(1, 100)

while True:
    user_guess = input("Guess the number (1-100): ")
    if not user_guess.isdigit():
        print("Invalid input. Try again")
        continue

    if random_computer_number == int(user_guess):
        print("You guessed it!")
        break
    elif int(user_guess) > random_computer_number:
        print("Too high!")
    else:
        print("Too low!")