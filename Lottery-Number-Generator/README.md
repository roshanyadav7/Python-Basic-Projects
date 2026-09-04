# 🎟️ Lottery Number Generator

A simple and interactive **Python Lottery Game** for beginners.

The program allows the player to select 6 unique numbers between 1 and 49, generates random winning numbers, checks the matching numbers, and awards a prize based on the result.

## 📌 Features

* 🎟️ Buy a lottery ticket
* 🔢 Choose 6 numbers between 1 and 49
* 🚫 Prevent duplicate numbers
* ⚠️ Validate invalid inputs
* 🎲 Generate random winning numbers
* 🔍 Find matching numbers
* 🏆 Prize system based on matches
* 🔄 Play multiple times
* 👋 Exit option

## 🎯 How the Game Works

1. Start the program.
2. Select **Buy Lottery Ticket**.
3. Enter 6 different numbers between **1 and 49**.
4. The program generates 6 random winning numbers.
5. Your numbers are compared with the winning numbers.
6. The program displays your matching numbers.
7. A prize is awarded based on the number of matches.

## 💰 Prize System

| Numbers Matched | Prize                               |
| --------------- | ----------------------------------- |
| 6               | 🏆 Jackpot — ₹1,00,000              |
| 5               | 🥳 Excellent — ₹10,000              |
| 4               | 🎉 Great — ₹1,000                   |
| 3               | 👏 Good Match — Free Lottery Ticket |
| 0–2             | 😔 No Prize                         |

> **Note:** The prizes are simulated for this Python project and do not represent real lottery payouts.

## 🛠️ Technologies Used

* **Python 3**
* `random` module

## 🧠 Python Concepts Used

This project is designed for beginners and demonstrates:

* Variables
* Lists
* `while` loops
* `for` loops
* `if`, `elif`, and `else`
* `try-except`
* `random.randint()`
* `append()`
* `sort()`
* `in` operator
* `len()`
* User input

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

### 2. Download or clone the project

```bash
git clone https://github.com/roshanyadav7/Python-Basic-Projects.git
```

### 3. Open the project folder

```bash
cd Python-Basic-Projects/Lottery-Number-Generator
```

### 4. Run the program

```bash
python lottery.py
```

## 💻 Example Output

```text
==================================================
           🎟️ LOTTERY GAME
==================================================

1. Buy Lottery Ticket
2. Exit

Enter your choice: 1

Choose 6 numbers between 1 and 49.

Enter number 1: 7
Enter number 2: 12
Enter number 3: 18
Enter number 4: 25
Enter number 5: 34
Enter number 6: 42

==================================================
              🎟️ YOUR TICKET
==================================================

Your numbers:    [7, 12, 18, 25, 34, 42]
Winning numbers: [5, 12, 18, 21, 34, 47]
Matching numbers: [12, 18, 34]

Numbers matched: 3

👏 GOOD MATCH!
🎟️ Prize: FREE LOTTERY TICKET

==================================================
```

## 📂 Project Structure

```text
lottery-number-generator/
│
├── lottery.py
└── README.md
```

## 🚀 Future Improvements

Some possible improvements for this project:

* Add a player name
* Add a virtual wallet and ticket cost
* Keep track of total winnings
* Add multiple lottery tickets
* Add different lottery modes
* Add a jackpot that increases after every game
* Save game results to a file
* Add a graphical user interface (GUI)

## 👨‍💻 Author

**Roshan Kumar Yadav**

Created as a **beginner Python project** to practice random numbers, loops, lists, conditions, and input validation.