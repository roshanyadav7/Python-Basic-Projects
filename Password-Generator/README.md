# 🔐 Password Generator

A simple Python project that generates a random password based on the length entered by the user.

## ✨ Features

* 🔤 Generates passwords using uppercase and lowercase letters
* 🔢 Includes numbers
* 🔣 Includes special characters
* 📏 Allows the user to choose the password length
* ✅ Requires the password to be at least 4 characters long
* ⚠️ Handles invalid input using `try-except`

## ⚙️ How It Works

The program uses Python's built-in `random` and `string` modules.

* `string.ascii_letters` → Provides uppercase and lowercase letters
* `string.digits` → Provides numbers from `0` to `9`
* `string.punctuation` → Provides special characters
* `random.choice()` → Randomly selects characters to create the password

## 🖥️ Example

```text
==============================
     PASSWORD GENERATOR
==============================
Enter password length: 12

Your generated password is:
aB7@kP2!xQ9#
```

The generated password will be different each time the program runs.

## 📋 Requirements

* 🐍 Python 3.x
* No external libraries are required

## 🚀 How to Run

1. Make sure Python is installed on your computer.
2. Open a terminal in the project folder.
3. Run the program:

```bash
python password_generator.py
```

4. Enter the desired password length when prompted.

## 📚 Project Level

**Beginner / Basic Python Project**

This project is useful for practicing:

* Functions
* `while` loops
* `for` loops
* `try-except`
* User input
* String handling
* Python modules
* Random character generation

## ⚠️ Note

This project is intended for learning Python programming. For applications requiring strong security, use a cryptographically secure password generator rather than relying on the standard `random` module.

## 👨‍💻 Author

**Roshan Kumar Yadav**

Created as a beginner Python project to practice basic Python programming concepts.