import json
import random
import os

player_guesses = 0
max_gusses = 7
BEST_SCORE_FILE = "best score.json"


def load_best_score():
    """Load best score from JSON file."""
    try:
        with open("best score.json", 'r') as f:  # Add quotes around the filename
            data = json.load(f)
            best_score = data.get("best_score", None)  # Use None instead of []
            return best_score
    except FileNotFoundError:
        return None  # Return None if file doesn't exist
    except json.JSONDecodeError:
        return None  # Return None if JSON is invalid


def save_best_score(score):
    """Save best score to JSON file."""
    data = {"best_score": score}
    with open("best score.json", 'w') as f:
        json.dump(data, f, indent=2)


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
        # Check if max guesses exceeded
        if player_guesses >= max_gusses:
            print(f"You've reached the maximum number of guesses ({max_gusses}). The number was {secret_number}.")
            return False  # Game lost
        
        remaining = max_gusses - player_guesses
        print(f"Guesses remaining: {remaining}")
        
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
            
            # Load the current best score
            best_score = load_best_score()
            
            # Check if this is a new best score (or if no best score exists yet)
            if best_score is None or player_guesses < best_score:
                # Save the new best score
                save_best_score(player_guesses)
                print(f"🎉 New best score: {player_guesses} guesses!")
            else:
                # Show the current best score
                print(f"Current Best score: {best_score} guesses")
            
            return True  # Game won


# main game loop with restart
while True:
    main()
    restart = input("Do you want to play again? Yes/No: ")
    if restart.lower() != "yes":
        break
