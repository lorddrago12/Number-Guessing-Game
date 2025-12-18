import random

player_guesses = 0


def main():
    """Run one round of the number guessing game."""
    global player_guesses
    player_guesses = 0  # reset guesses each game

    print("***** Number Guessing Game! *****")
    print("Choose Your Difficulty")
    print("1. Easy   (1 - 100)")
    print("2. Medium (1 - 200)")
    print("3. Hard   (1 - 300)")

    # choose difficulty safely
    while True:
        try:
            player_difficulty = int(input("Enter your difficulty (1, 2, or 3): "))
            if player_difficulty in (1, 2, 3):
                break
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a number (1, 2, or 3).")

    # set range based on difficulty
    if player_difficulty == 1:
        secret_number = random.randint(1, 100)
    elif player_difficulty == 2:
        secret_number = random.randint(1, 200)
    else:
        secret_number = random.randint(1, 300)

    # guessing loop
    while True:
        try:
            player_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        player_guesses += 1

        if player_guess > secret_number:
            print("Your guess is too high, try again!")
        elif player_guess < secret_number:
            print("Your guess is too low, try again!")
        else:
            print(f"You guessed the correct number in {player_guesses} guesses.")
            break  # exit the guessing loop when correct


# main game loop with restart
while True:
    main()
    restart = input("Do you want to play again? Yes/No: ")

    if restart.lower() != "yes":
        break
