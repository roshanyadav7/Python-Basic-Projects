import random
import string

# A simple password generator in Python.

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("==============================")
print("     PASSWORD GENERATOR")
print("==============================")

# Get the desired password length from the user and validate it
while True:
    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password should be at least 4 characters long.")
        else:
            break

    except ValueError:
        print("Please enter a number.")


password = generate_password(length)

print("\nYour generated password is:")
print(password)