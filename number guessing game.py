import random

secret_number = random.randint(1, 100)
player_guesses = 0

while True:
    player_guess = int(input("Enter Your Guess: "))
    player_guesses = player_guesses + 1

    if player_guess > secret_number:
        print("Your Guess is too high, Try again!")

    elif player_guess < secret_number:
        print("Your guess is too low, Try again!")

    else:
        print(f"You guessed the correct number in {player_guesses} gusses.")
        break