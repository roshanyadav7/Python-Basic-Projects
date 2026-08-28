import random

# List of famous quotes from the Marvel Cinematic Universe
quotes = [
    "I am Iron Man.",
        "I love you 3000.",
    "Avengers, assemble!",
    "With great power comes great responsibility.",
    "That's my secret, Captain. I'm always angry.",
    "I can do this all day.",
    "Wakanda Forever!",
    "We are Groot.",
    "I am inevitable.",
    "Part of the journey is the end.",
    "Whatever it takes.",
    "Dormammu, I've come to bargain.",
    "On your left.",
    "I'm with you till the end of the line, pal.",
    "I have been falling for thirty minutes!",
    "Language!",
    "We have a Hulk.",
    "I don't wanna go.",
    "You should have gone for the head.",
    "The hardest choices require the strongest wills.",
    "We're in the endgame now.",
    "I am Loki of Asgard, and I am burdened with glorious purpose.",
    "I assure you, brother, the sun will shine on us again.",
    "Love is a dagger.",
    "No amount of money ever bought a second of time.",
    "I've been playing along with you.",
    "I know what kind of god I need to be."
]

# Display the project title
print("================================")
print("   RANDOM MCU QUOTE GENERATOR")
print("================================")

# Keep running until the user chooses to exit
while True:

    choice = input('\nType "quote" for a random quote or "exit" to quit: ').strip().lower()

    # Generate a random quote
    if choice == "quote":
        quote = random.choice(quotes)
        print("\n>> " + quote)

    # Exit the program
    elif choice == "exit":
        print("\nThank you for using Random MCU Quote Generator!")
        break

    # Handle invalid input
    else:
        print('\nInvalid input! Please type "quote" or "exit".')