import json
import random
import os

# Global variables
player_guesses = 0
BEST_SCORE_FILE = "best score.json"


def load_best_scores():
    """Load best scores from JSON file. Returns default dict if file doesn't exist."""
    if not os.path.exists(BEST_SCORE_FILE):
        return {"easy": None, "medium": None, "hard": None}

    try:
        with open(BEST_SCORE_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"easy": None, "medium": None, "hard": None}


def save_best_scores(scores):
    """Save best scores to JSON file."""
    with open(BEST_SCORE_FILE, "w") as f:
        json.dump(scores, f, indent=2)


def main():
    """Run one round of the number guessing game."""
    global player_guesses
    player_guesses = 0  # Reset guesses each game

    # Display welcome message and difficulty options
    print("***** Number Guessing Game! *****")
    print("Choose Your Difficulty")
    print("1. Easy   (1 - 100)")
    print("2. Medium (1 - 200)")
    print("3. Hard   (1 - 300)")

    # Get difficulty choice from player
    while True:
        try:
            player_difficulty = int(input("Enter your difficulty (1, 2, or 3): "))
            if player_difficulty in (1, 2, 3):
                break
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a number (1, 2, or 3).")

    # Set range and max guesses based on difficulty
    if player_difficulty == 1:
        max_guesses = 7
        secret_number = random.randint(1, 100)
    elif player_difficulty == 2:
        max_guesses = 6
        secret_number = random.randint(1, 200)
    else:
        max_guesses = 5
        secret_number = random.randint(1, 300)

    # Main guessing loop
    while True:
        # Check if max guesses exceeded
        if player_guesses >= max_guesses:
            print(f"You've reached the maximum number of guesses ({max_guesses}). The number was {secret_number}.")
            return False  # Game lost

        remaining = max_guesses - player_guesses
        print(f"Guesses remaining: {remaining}")

        # Get player's guess
        try:
            player_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        player_guesses += 1

        # Check if guess is correct
        if player_guess > secret_number:
            print("Your guess is too high, try again!")
        elif player_guess < secret_number:
            print("Your guess is too low, try again!")
        else:
            print(f"You guessed the correct number in {player_guesses} guesses.")

            # Map difficulty number to difficulty name
            difficulty_name = {1: "easy", 2: "medium", 3: "hard"}[player_difficulty]

            # Load the current best score
            best_scores = load_best_scores()
            current_best = best_scores[difficulty_name]

            # Check if this is a new best score (or if no best score exists yet)
            if current_best is None or player_guesses < current_best:
                best_scores[difficulty_name] = player_guesses
                save_best_scores(best_scores)
                print(f"🎉 New BEST score for {difficulty_name.upper()} mode: {player_guesses} guesses!")
            else:
                print(f"Best score for {difficulty_name.upper()} mode: {current_best} guesses")

            return True  # Game won


# Main game loop with restart option
if __name__ == "__main__":
    while True:
        main()
        restart = input("Do you want to play again? Yes/No: ")
        if restart.lower() != "yes":
            break
