import json

FILE_NAME = "tasks.json"

try:
    with open(FILE_NAME, "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

while True:
    print("\nGOLDENROD")
    print("1. Add task")
    print("2. View tasks")
    print("3. Quit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)

        print("Task added and saved.")

    elif choice == "2":
        print("\nYour tasks:")

        if not tasks:
            print("No tasks yet.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == "3":
        print("Later.")
        break

    else:
        print("That is not a valid choice.")