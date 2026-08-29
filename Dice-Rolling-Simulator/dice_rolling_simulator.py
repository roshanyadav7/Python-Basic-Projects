import random

print("🎲 Welcome to Dice Rolling Simulator!")

while True:
    try:
        number_of_dice = int(input("\nHow many dice do you want to roll? "))

        if number_of_dice <= 0:
            print("Please enter a number greater than 0.")
            continue

        rolls = []

        for i in range(number_of_dice):
            roll = random.randint(1, 6)
            rolls.append(roll)

        print("Dice rolled:", rolls)
        print("Total:", sum(rolls))

        again = input("\nRoll again? (y/n): ").lower()

        if again == "n":
            print("Thanks for playing! 🎲")
            break

        elif again != "y":
            print("Invalid choice. Game ended.")
            break

    except ValueError:
        print("Please enter a valid number.")