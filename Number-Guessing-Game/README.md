# Number Guessing Game 🎯

A simple number guessing game built using Python. The user chooses a range, and the program generates a random number within that range. The player then tries to guess the number with hints provided by the program.

## Features

* Allows the user to choose the lowest and highest numbers.
* Generates a random number within the selected range.
* Gives a **"Too low"** or **"Too high"** hint after each incorrect guess.
* Counts the number of attempts.
* Validates user input using exception handling.
* Prevents the user from guessing outside the selected range.
* Handles invalid ranges and invalid inputs.

## Technologies Used

* Python
* `random` module
* `while` loops
* `if-elif-else` statements
* `try-except` exception handling
* User input

## How to Run

Make sure Python is installed on your computer.

Open the project folder in a terminal and run:

```bash
python number_guessing_game.py
```

## How the Game Works

1. Enter the lowest number of the range.
2. Enter the highest number of the range.
3. The program generates a random number within that range.
4. Enter your guess.
5. The program tells you whether your guess is too high or too low.
6. Continue guessing until you find the correct number.
7. The program displays the number of attempts taken.

## Example

```text
Enter the lowest number of the range: 1
Enter the highest number of the range: 100

Welcome to the Number Guessing Game!
Guess a number between 1 and 100.

Enter your guess: 50
Too low! Try again.

Enter your guess: 75
Too high! Try again.

Enter your guess: 63
Congratulations! You guessed the number correctly in 3 attempts.
```

## Purpose

This project was created to practice basic Python programming concepts such as loops, conditional statements, user input, random number generation, and exception handling.
