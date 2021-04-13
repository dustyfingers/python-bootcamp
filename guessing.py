import random

random_number = random.randint(1, 10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!
guess = input("Im thinking of a num between 1 and 10, guess what it is!")

while True:
    guess = int(guess)
    if guess == random_number:
        print("you won!")
        break
    elif guess > random_number:
        print("You guessed too high, try again!")
        guess = input(
            "Im thinking of a num between 1 and 10, guess what it is!")
    elif guess < random_number:
        print("You guessed too low, try again!")
        guess = input(
            "Im thinking of a num between 1 and 10, guess what it is!")
