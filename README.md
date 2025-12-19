# Number Guessing Game 🎯

A feature-rich terminal-based number guessing game written in Python. This version includes **difficulty levels**, a **guess limit**, **input validation**, a **replay system**, and a persistent **best score tracker** saved using a JSON file.

---

## 📌 What This Project Is

This is an interactive console game where:

* The player selects a difficulty level
* A random secret number is generated
* The player has a limited number of guesses
* The game provides feedback after each guess
* The best (lowest) number of guesses is saved permanently
* The player can replay the game multiple times

It’s a complete example of combining game logic with file storage.

---

## 🎮 Difficulty Levels

The game offers three difficulty modes:

* **Easy** → Numbers between **1 and 100**
* **Medium** → Numbers between **1 and 200**
* **Hard** → Numbers between **1 and 300**

Each difficulty increases the guessing range, making the game more challenging.

---

## ⏱️ Guess Limit

* The player has a maximum of **7 guesses** per round
* Remaining guesses are displayed each turn
* If the limit is reached, the game ends and reveals the secret number

---

## 🏆 Best Score System

* The game tracks the **best score** (fewest guesses)
* The best score is saved in a file called:

  ```
  best score.json
  ```
* The score persists even after closing the program
* If a new best score is achieved, it replaces the old one

This introduces basic **file handling and persistence**.

---

## ✨ Features

* Difficulty selection
* Guess limit enforcement
* Input validation (no crashes on invalid input)
* Replay option
* Persistent best score tracking
* Clean, structured code using functions

---

## 🧠 Concepts Demonstrated

* Random number generation
* Functions and return values
* Loops and control flow
* Exception handling (`try / except`)
* File I/O using JSON
* State persistence across runs

---

## 🏗️ How The Game Works

1. The game displays a difficulty menu
2. The player selects a valid difficulty
3. A secret number is generated
4. The player makes guesses (up to 7)
5. Feedback is given after each guess
6. The game ends with a win or loss
7. Best score is checked and saved if needed
8. The player can choose to play again

---

## 🔄 Example Gameplay

```
***** Number Guessing Game! *****
Choose Your Difficulty
1. Easy   (1 - 100)
2. Medium (1 - 200)
3. Hard   (1 - 300)

Enter your difficulty (1, 2, or 3): 1
Guesses remaining: 7
Enter your guess: 50
Your guess is too high, try again!

Guesses remaining: 6
Enter your guess: 25
Your guess is too low, try again!

Guesses remaining: 5
Enter your guess: 37
You guessed the correct number in 3 guesses.
🎉 New best score: 3 guesses!

Do you want to play again? Yes/No: no
```

---

## 📚 Learning Value

From this project, someone can learn:

* How to design a full console game
* How to persist data using JSON
* How to handle invalid user input safely
* How to structure Python programs cleanly
* How to add replayable game mechanics

---

## 🚀 Ideas for Future Improvements

* Difficulty-based guess limits
* Separate best scores per difficulty
* Player name support
* Leaderboard system
* GUI version of the game

---
