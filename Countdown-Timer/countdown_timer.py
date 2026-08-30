import time

while True:
    print("\n===== COUNTDOWN TIMER =====")

    try:
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))

        if hours < 0 or minutes < 0 or seconds < 0:
            print("Please enter non-negative numbers.")
            continue

        total_seconds = hours * 3600 + minutes * 60 + seconds

        if total_seconds <= 0:
            print("Please enter a time greater than 0.")
            continue

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    print("\n⏱️ Timer started!")

    while total_seconds > 0:
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")

        time.sleep(1)
        total_seconds -= 1

    print("00:00:00")
    print("⏰ Time's up!")

    again = input("\nDo you want to start another timer? (yes/no): ")

    if again.lower() != "yes":
        print("Goodbye! 👋")
        break