tasks = []


def display_tasks():
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


while True:
    print("\n==============================")
    print("          TO-DO LIST")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ").strip()

        if task:
            tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        if not tasks:
            print("No tasks found.")
        else:
            display_tasks()

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            display_tasks()

            try:
                task_number = int(input("Enter task number to remove: "))

                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    print(f"Removed: {removed_task}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")