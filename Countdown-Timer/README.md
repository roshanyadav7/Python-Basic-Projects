# ⏱️ Countdown Timer

A beginner-friendly **Countdown Timer** built with Python. The program allows users to enter a custom duration in **hours, minutes, and seconds**, then counts down in real time until the timer reaches zero.

The program also includes **input validation** to prevent crashes when invalid or negative values are entered.

## 📌 Features

* ⏱️ Set a custom timer using hours, minutes, and seconds.
* 🕐 Displays the remaining time in `HH:MM:SS` format.
* 🔄 Counts down automatically every second.
* ⚠️ Handles invalid inputs without crashing.
* 🚫 Rejects negative time values.
* 🚫 Prevents the timer from starting with a total time of zero.
* 🔁 Allows users to start another timer after completion.
* 👋 Provides a simple exit option.

## 🛠️ Technologies Used

* **Python 3**
* **time module**

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/countdown-timer.git
```

### 2. Navigate to the Project Folder

```bash
cd countdown-timer
```

### 3. Run the Program

```bash
python countdown_timer.py
```

## 💻 Example

```text
===== COUNTDOWN TIMER =====

Enter hours: 0
Enter minutes: 1
Enter seconds: 10

⏱️ Timer started!

00:01:10
00:01:09
00:01:08
...
00:00:02
00:00:01
00:00:00
⏰ Time's up!

Do you want to start another timer? (yes/no): no
Goodbye! 👋
```

## ⚠️ Input Validation

The program handles invalid input using `try-except`.

For example, if the user enters:

```text
Enter hours: abc
```

The program displays:

```text
Invalid input! Please enter numbers only.
```

Negative values are also rejected:

```text
Enter hours: -1
Enter minutes: 20
Enter seconds: 30

Please enter non-negative numbers.
```

A timer with no duration is also rejected:

```text
Enter hours: 0
Enter minutes: 0
Enter seconds: 0

Please enter a time greater than 0.
```

## 📖 How It Works

### 1. Get User Input

The program asks the user for hours, minutes, and seconds.

```python
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
```

### 2. Validate the Input

A `try-except` block prevents the program from crashing when the user enters something that cannot be converted into an integer.

```python
try:
    hours = int(input("Enter hours: "))
except ValueError:
    print("Invalid input! Please enter numbers only.")
```

The program also checks for negative values.

### 3. Convert the Time to Seconds

All three values are converted into total seconds:

```python
total_seconds = hours * 3600 + minutes * 60 + seconds
```

For example:

```text
1 hour + 20 minutes + 30 seconds
```

becomes:

```text
3600 + 1200 + 30 = 4830 seconds
```

### 4. Start the Countdown

The program repeatedly calculates the remaining hours, minutes, and seconds:

```python
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
```

The result is displayed in:

```text
HH:MM:SS
```

format.

### 5. Wait One Second

The `time.sleep(1)` function pauses the program for one second:

```python
time.sleep(1)
```

Then the total remaining time is reduced by one second.

### 6. Timer Completion

When the countdown reaches zero, the program displays:

```text
00:00:00
⏰ Time's up!
```

The user can then choose whether to start another timer.

## 🎯 What I Learned

This project helped me practice:

* `while` loops
* `if` conditions
* `try-except`
* User input
* Type conversion
* Arithmetic operations
* Integer division (`//`)
* Modulo (`%`)
* f-string formatting
* The `time` module
* Input validation
* Program flow

## 📂 Project Structure

```text
Countdown-Timer/
│
├── countdown_timer.py
└── README.md
```

## 🔮 Future Improvements

Possible features that could be added:

* 🔔 Play a sound when the timer finishes.
* ⏸️ Add Pause and Resume functionality.
* 🔄 Add a Reset option.
* 🎨 Create a graphical user interface (GUI).
* ⌨️ Add keyboard controls.
* 💾 Save frequently used timer durations.
* 🕐 Add a countdown progress indicator.

## 👨‍💻 Author

**Roshan Kumar Yadav**

If you found this project useful, feel free to ⭐ the repository!