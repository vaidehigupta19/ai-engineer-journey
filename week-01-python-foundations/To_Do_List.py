tasks = []

def show_menu():
    print("---To_Do_List---")
    print("1. Add menu")
    print("2. View menu")
    print("3. Delete menu")
    print("4. Exit")

while True:
    show_menu()

    choice = input("Enter your choice (1-4)")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully !")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}. {task}")

            try:
                index = int(input("Enter task to remove: "))
                if 1 <= index <=len(tasks):
                    removed = tasks.pop(index - 1)
                    print(f"'{removed}' removed successfully")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number. ")

    elif choice == "4":
        print ("Thank you for using the To-Do-List!")
        break

else:
    print("Invalid choice. Please try again.")