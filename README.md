# Number Guessing Game 🎯

This project is a classic **number guessing game** written in Python. It’s a simple terminal-based game that demonstrates core programming concepts like loops, conditionals, user input, and random number generation.

This README is written so **future you** and **anyone learning Python** can quickly understand what the game does and how the logic works.

---

## 📌 What This Project Is

A console game where:

* The computer randomly chooses a number between 1 and 100
* The player keeps guessing until they find the correct number
* The program gives hints if the guess is too high or too low
* The total number of guesses is counted and displayed

It’s a beginner-friendly project that still teaches important fundamentals.

---

## 🎯 Purpose of This Project

You built this game to:

* Practice loops (`while True`)
* Work with conditional logic (`if / elif / else`)
* Use the `random` module
* Handle user input and type conversion
* Track game state (number of guesses)

This is one of the best starter projects for understanding program flow.

---

## ✨ Features

* Random secret number each run
* Unlimited guesses until correct
* Helpful feedback (too high / too low)
* Guess counter
* Clean and simple logic

---

## 🧠 Core Concepts Used

* **Random number generation** (`random.randint`)
* **Infinite loop** with a break condition
* **User input handling**
* **Integer comparison**
* **State tracking** (guess count)

---

## 🏗️ How It Works

1. A random number between 1 and 100 is generated
2. The program asks the user to guess
3. Each guess is compared to the secret number
4. The program responds with a hint
5. When the guess is correct, the loop ends
6. The total number of guesses is displayed

This loop continues until the correct answer is found.

---

## 🔄 Example Game Flow

```
Enter Your Guess: 50
Your Guess is too high, Try again!

Enter Your Guess: 25
Your guess is too low, Try again!

Enter Your Guess: 37
You guessed the correct number in 3 guesses.
```

---

## 📚 What Someone Can Learn From This

* How loops keep programs running
* How decisions are made in code
* How to validate guesses logically
* How to build simple interactive games

This project is a great stepping stone toward more advanced games.

---

## 🚀 Possible Improvements

* Add input validation (handle non-numbers)
* Add difficulty levels (range changes)
* Limit the number of guesses
* Add replay option
* Add score tracking

---

This project is a clean and classic example of **learning Python through games**.
