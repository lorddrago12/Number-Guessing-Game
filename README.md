# Number Guessing Game 🎯

A terminal-based number guessing game written in Python that includes **difficulty levels**, a **guess limit**, **input validation**, and a **replay system**. This version is more structured and polished, making it easy to understand, play, and extend.

---

## 📌 What This Project Is

This is an interactive console game where:

* The player chooses a difficulty level
* A random secret number is generated based on that difficulty
* The player has a limited number of guesses to find the number
* The game gives feedback after every guess
* The player can restart the game after each round

It’s a clean example of game logic, control flow, and user input handling in Python.

---

## 🎮 Difficulty Levels

The game offers three difficulty modes:

* **Easy** → 1 to 100
* **Medium** → 1 to 200
* **Hard** → 1 to 300

Higher difficulty increases the range, making the game more challenging.

---

## ⏱️ Guess Limit

* The player has a maximum of **7 guesses** per round
* Remaining guesses are displayed each turn
* If the limit is reached, the game ends and reveals the correct number

This adds pressure and makes the game more engaging.

---

## ✨ Features

* Difficulty selection system
* Guess limit enforcement
* Input validation for difficulty and guesses
* Feedback for each guess (too high / too low)
* Replay option after each game
* Clean, structured code using functions

---

## 🧠 Concepts Demonstrated

* Functions and return values
* Loops (`while True`)
* Conditional logic (`if / elif / else`)
* Exception handling (`try / except`)
* Random number generation
* State tracking with variables

---

## 🏗️ How The Game Works

1. The game displays a difficulty menu
2. The player selects a valid difficulty
3. A secret number is generated within the chosen range
4. The player makes guesses (up to 7)
5. The game provides hints after each guess
6. The game ends with a win or loss
7. The player is asked if they want to play again

This loop continues until the player chooses to stop.

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

Do you want to play again? Yes/No: no
```

---

## 📚 Learning Value

Someone studying this project can learn:

* How to design a complete console game
* How to validate user input properly
* How to limit attempts logically
* How to structure code using functions
* How to build replayable programs

---

## 🚀 Ideas for Future Improvements

* Difficulty-based guess limits
* Score system or leaderboard
* Timed mode
* Hint system
* GUI version using Tkinter or PySimpleGUI

---
