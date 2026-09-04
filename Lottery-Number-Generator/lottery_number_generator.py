import random

print("=" * 50)
print("           🎟️ LOTTERY GAME")
print("=" * 50)

while True:
    print("\n1. Buy Lottery Ticket")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "2":
        print("\nThank you for playing! 👋")
        break

    if choice != "1":
        print("Invalid choice! Please enter 1 or 2.")
        continue

    # Get 6 numbers from the player
    lottery_numbers = []

    print("\nChoose 6 numbers between 1 and 49.")

    while len(lottery_numbers) < 6:
        try:
            number = int(input(
                f"Enter number {len(lottery_numbers) + 1}: "
            ))

            if number < 1 or number > 49:
                print("Please enter a number between 1 and 49.")

            elif number in lottery_numbers:
                print("You already selected that number!")

            else:
                lottery_numbers.append(number)

        except ValueError:
            print("Please enter a valid number.")

    lottery_numbers.sort()

    # Generate 6 winning numbers
    winning_numbers = []

    while len(winning_numbers) < 6:
        number = random.randint(1, 49)

        if number not in winning_numbers:
            winning_numbers.append(number)

    winning_numbers.sort()

    # Find matching numbers
    matches = []

    for number in lottery_numbers:
        if number in winning_numbers:
            matches.append(number)

    # Display results
    print("\n" + "=" * 50)
    print("              🎟️ YOUR TICKET")
    print("=" * 50)

    print("Your numbers:   ", lottery_numbers)
    print("Winning numbers:", winning_numbers)
    print("Matching numbers:", matches)

    matched_count = len(matches)

    print("\nNumbers matched:", matched_count)

    # Prize system
    if matched_count == 6:
        print("🏆 JACKPOT!")
        print("💰 Prize: ₹1,00,000")

    elif matched_count == 5:
        print("🥳 EXCELLENT!")
        print("💰 Prize: ₹10,000")

    elif matched_count == 4:
        print("🎉 GREAT!")
        print("💰 Prize: ₹1,000")

    elif matched_count == 3:
        print("👏 GOOD MATCH!")
        print("🎟️ Prize: FREE LOTTERY TICKET")

    else:
        print("😔 No prize this time.")
        print("🍀 Better luck next time!")

    print("=" * 50)