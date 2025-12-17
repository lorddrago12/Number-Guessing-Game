# Number Guessing Game 🎯

A terminal-based number guessing game written in Python that lets the player choose a difficulty level before playing. The game challenges the player to guess a randomly generated number while providing feedback and tracking the number of attempts.

---

## 📌 What This Project Is

This is an interactive console game where:

* The player selects a difficulty level
* A random number is generated based on the chosen difficulty
* The player keeps guessing until the correct number is found
* The game gives hints if the guess is too high or too low
* The total number of guesses is counted

It’s a simple but solid project that demonstrates control flow and game logic in Python.

---

## 🎮 Difficulty Levels

The game offers three difficulty modes:

* **Easy** → Guess a number between **1 and 100**
* **Medium** → Guess a number between **1 and 200**
* **Hard** → Guess a number between **1 and 300**

Choosing a higher difficulty increases the range and makes the game more challenging.

---

## ✨ Features

* Difficulty selection system
* Random number generation based on difficulty
* Unlimited guesses until success
* Helpful feedback for each guess
* Guess counter displayed at the end

---

## 🧠 Concepts Used

* `random.randint()` for number generation
* Conditional statements (`if / elif / else`)
* Infinite loops with `while True`
* User input handling
* State tracking using variables

---

## 🏗️ How The Game Works

1. The game displays a difficulty menu
2. The player selects a difficulty level
3. A secret number is generated within the chosen range
4. The player enters guesses
5. The game responds with hints
6. When guessed correctly, the game ends and shows total attempts

This loop continues until the correct number is guessed.

---

## 🔄 Example Gameplay

```
*****Number Guessing Game!*****
Choose Your Difficulty
1. Easy 1 - 100
2. Medium 1 - 200
3. Hard 1 - 300

Enter Your difficulty: 2
Enter Your Guess: 150
Your Guess is too high, Try again!

Enter Your Guess: 90
Your guess is too low, Try again!

Enter Your Guess: 120
You guessed the correct number in 3 guesses.
```

---

## 📚 Learning Value

Someone reading or modifying this project can learn:

* How to structure a simple game
* How difficulty systems work
* How loops control game flow
* How feedback improves user experience

---

## 🚀 Possible Improvements

* Input validation for non-numeric input
* Separate functions for each difficulty
* Add replay option
* Add score tracking or leaderboard
* Refactor repeated logic into reusable code

---

This project is a strong example of building **interactive logic-driven programs** in Python.
