import random

# A simple number guessing game in Python.

# Get the range from the user
while True:
    try:
        lower_number = int(input("Enter the lowest number of the range: "))
        upper_number = int(input("Enter the highest number of the range: "))

        if lower_number >= upper_number:
            print("Invalid range! The lowest number must be smaller than the highest number.")
        else:
            break

    except ValueError:
        print("Please enter valid integer numbers.")

# Generate a random number
number = random.randint(lower_number, upper_number)

# Initialize attempts
attempts = 0

print("\nWelcome to the Number Guessing Game!")
print(f"Guess a number between {lower_number} and {upper_number}.")

# Guessing the number using a while loop
while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if guess < lower_number or guess > upper_number:
        print(f"Please guess a number between {lower_number} and {upper_number}.")
        continue

    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number correctly in {attempts} attempts.")
        break