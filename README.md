# Number Guessing Game 🎯

A polished terminal-based number guessing game written in Python. This version features **difficulty-based rules**, **dynamic guess limits**, **input validation**, **replay support**, and a **persistent best score system per difficulty** stored in a JSON file.


---

## 📌 What This Project Is

This is an interactive console game where:

* The player selects a difficulty level (Easy, Medium, Hard)
* A random secret number is generated based on the chosen difficulty
* Each difficulty has its own guess limit
* The player receives feedback after every guess
* Best scores are saved separately for each difficulty
* Scores persist even after closing the program
* The player can replay the game multiple times

This project demonstrates how game logic and persistent storage work together.

---

## 🎮 Difficulty Levels & Rules

Each difficulty changes both the number range **and** the allowed guesses:

| Difficulty | Number Range | Max Guesses |
| ---------- | ------------ | ----------- |
| Easy       | 1 – 100      | 7           |
| Medium     | 1 – 200      | 6           |
| Hard       | 1 – 300      | 5           |

Harder modes give fewer guesses, increasing the challenge.

---

## 🏆 Best Score System (Per Difficulty)

* Best scores are tracked **individually** for Easy, Medium, and Hard modes
* Scores are stored in:

  ```
  best score.json
  ```
* The file structure looks like this:

  ```json
  {
    "easy": null,
    "medium": null,
    "hard": null
  }
  ```
* When a player wins:

  * If no score exists, it is saved
  * If the new score uses fewer guesses, it replaces the old one

This introduces real **state persistence** using JSON.

---

## ✨ Features

* Difficulty-based gameplay rules
* Dynamic guess limits
* Input validation (no crashes on invalid input)
* Per-difficulty best score tracking
* Persistent storage using JSON
* Replay option after each round
* Clean and readable code structure

---

## 🧠 Concepts Demonstrated

* Functions and program structure
* Conditional logic and control flow
* Exception handling (`try / except`)
* Random number generation
* File I/O using JSON
* Persistent state across program runs

---

## 🏗️ How The Game Works

1. Display difficulty selection menu
2. Player selects a valid difficulty
3. Game sets number range and guess limit
4. Player enters guesses
5. Game provides feedback after each guess
6. Game ends with a win or loss
7. Best score is checked and updated per difficulty
8. Player chooses whether to replay

---

## 🔄 Example Gameplay

```
***** Number Guessing Game! *****
Choose Your Difficulty
1. Easy   (1 - 100)
2. Medium (1 - 200)
3. Hard   (1 - 300)

Enter your difficulty (1, 2, or 3): 3
Guesses remaining: 5
Enter your guess: 150
Your guess is too low, try again!

Guesses remaining: 4
Enter your guess: 225
You guessed the correct number in 2 guesses.
🎉 New BEST score for HARD mode: 2 guesses!
```

---

## 📚 Learning Value

This project teaches:

* How to design scalable game logic
* How to separate rules by difficulty
* How to persist and manage structured data
* How to write safer input-handling code
* How to build replayable terminal games

---

## 🚀 Ideas for Future Improvements

* Leaderboard across players
* Player name support
* Timed game mode
* Hint system
* GUI version using Tkinter or PySimpleGUI

---

This project is a strong example of transitioning from **basic Python scripts** to **structured, stateful applications**.
