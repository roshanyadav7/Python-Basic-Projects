# 🎯 Number Guessing Game

A simple Python game where the computer randomly selects a number within a range chosen by the user. The player then tries to guess the number with hints provided after each attempt.

## ✨ Features

* 🎲 Generates a random number using Python's `random` module
* 🔢 Allows the user to choose the number range
* 🎯 Gives hints when the guess is too high or too low
* 📊 Counts the number of attempts
* ✅ Validates the selected number range
* ⚠️ Handles invalid inputs using `try-except`
* 🚫 Prevents guesses outside the selected range

## ⚙️ How It Works

1. The user enters the **lowest** and **highest** numbers for the range.
2. The program validates the range.
3. A random number is generated using `random.randint()`.
4. The user enters a guess.
5. The program checks the guess and provides a hint:

   * ⬇️ **Too low** — the guess is smaller than the hidden number.
   * ⬆️ **Too high** — the guess is larger than the hidden number.
   * 🎉 **Correct** — the game ends.
6. The number of attempts is displayed when the player guesses correctly.

## 🖥️ Example

```text
Enter the lowest number of the range: 1
Enter the highest number of the range: 100

Welcome to the Number Guessing Game!
Guess a number between 1 and 100.
Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 37
Congratulations! You guessed the number correctly in 3 attempts.
```

## 📋 Requirements

* 🐍 Python 3.x
* No external libraries are required.

## 🚀 How to Run

1. Make sure Python is installed on your computer.
2. Open a terminal in the project folder.
3. Run the program:

```bash
python number_guessing_game.py
```

4. Enter the lowest and highest numbers for your desired range.
5. Start guessing!

## 📚 Project Level

**Beginner / Basic Python Project**

This project is useful for practicing:

* `while` loops
* `if-elif-else` statements
* Functions and user input
* `try-except` exception handling
* Variables
* `f-strings`
* Python modules
* Random number generation
* Input validation

## ⚠️ Note

This project is created for learning and practicing basic Python programming concepts.

## 👨‍💻 Author

**Roshan Kumar Yadav**

Created as a beginner Python project to practice basic Python programming concepts.
