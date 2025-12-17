import random

player_guesses = 0

print("*****Number Guessing Game!*****")
print("Choose Your Difficulty")
print("1. Easy 1-  100")
print("2. Medium 1 - 200")
print("3. Hard 1 - 300")

player_difficulty = int(input("Enter Your difficulty: "))
#choosing difficulty
if player_difficulty == 1:
    secret_number = random.randint(1, 100)

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

elif player_difficulty == 2:
    secret_number = random.randint(1, 200)
        
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

else:
    secret_number = random.randint(1, 300)
        
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
