# 📧 Email Slicer

A simple Python **Email Slicer** that extracts useful information from an email address. The program separates an email into its **username, domain, and extension** while performing basic input validation.

## 📌 Features

* 📧 Accepts an email address from the user.
* 👤 Extracts the username.
* 🌐 Extracts the domain.
* 🔤 Extracts the email extension.
* ⚠️ Checks that the email contains exactly one `@`.
* 🔍 Checks that the domain contains a `.`.
* 🚫 Rejects incomplete email addresses.
* 🔁 Allows the user to slice multiple email addresses.
* 👋 Provides an option to exit the program.

## 🛠️ Technologies Used

* **Python 3**
* Python string methods

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/roshanyadav7/email-slicer.git
```

### 2. Navigate to the Project Folder

```bash
cd email-slicer
```

### 3. Run the Program

```bash
python email_slicer.py
```

## 💻 Example

```text
===== EMAIL SLICER =====

Enter your email: roshan@gmail.com

===== EMAIL DETAILS =====
Username: roshan
Domain: gmail
Extension: com

Do you want to slice another email? (yes/no): no
Goodbye! 👋
```

## ⚠️ Input Validation

The program performs several basic checks before slicing the email.

### Exactly One `@`

The program checks:

```python
if email.count("@") != 1:
```

For example:

```text
roshan@gmail.com       ✅
roshan@@gmail.com      ❌
roshan.gmail.com       ❌
```

### Domain Must Contain `.`

The program checks:

```python
if "." not in domain_part:
```

For example:

```text
roshan@gmail.com       ✅
roshan@gmailcom        ❌
```

### Complete Email Address

The program also checks that the username, domain, and extension are not empty:

```python
if not username or not domain or not extension:
```

This prevents incomplete addresses such as:

```text
@gmail.com
roshan@.com
roshan@gmail.
```

## 📖 How It Works

### 1. Get the Email

The program asks the user to enter an email address:

```python
email = input("Enter your email: ")
```

### 2. Validate `@`

It checks whether the email contains exactly one `@` symbol:

```python
if email.count("@") != 1:
```

### 3. Split the Email

The email is divided into two parts:

```python
username, domain_part = email.split("@")
```

For:

```text
roshan@gmail.com
```

the result is:

```text
username     → roshan
domain_part  → gmail.com
```

### 4. Separate Domain and Extension

The program uses `rsplit()` to separate the domain from the final extension:

```python
domain, extension = domain_part.rsplit(".", 1)
```

The `1` means that Python will make a maximum of one split, while `rsplit()` starts from the right.

For:

```text
mail.google.com
```

the result is:

```text
domain     → mail.google
extension  → com
```

This allows the program to handle domains containing multiple dots.

### 5. Display the Results

Finally, the extracted information is displayed:

```text
===== EMAIL DETAILS =====

Username: roshan
Domain: gmail
Extension: com
```

## 🎯 What I Learned

This project helped me practice:

* `while` loops
* `if` conditions
* `continue`
* `break`
* User input
* String manipulation
* `.count()`
* `.split()`
* `.rsplit()`
* `.lower()`
* `or`
* `not`
* Multiple assignment
* Basic input validation

## 📂 Project Structure

```text
Email-Slicer/
│
├── email_slicer.py
└── README.md
```

## 🔮 Future Improvements

Possible improvements for this project:

* 🔤 Convert uppercase emails to lowercase.
* ✂️ Remove unnecessary spaces using `.strip()`.
* 🌐 Validate common email domain formats.
* 📋 Process multiple emails at once.
* 📁 Read email addresses from a file.
* 📊 Add more detailed email validation.

## 👨‍💻 Author

**Roshan Kumar Yadav**

## 🎯 Purpose

This project was created as part of my journey to learn **Python programming from the basics** and practice **string manipulation and input validation**.

If you found this project useful, feel free to ⭐ the repository!