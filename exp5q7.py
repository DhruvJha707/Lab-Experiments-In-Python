'''Create a Todo list Manager where users can add, view, and remove tasks. Use List for storing 
tasks. '''


tasks = []

while True:
    print("\n--- Todo List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task to add: ")
        tasks.append(task)
        print("Task added!")

    elif choice == 2:
        print("\n--- Your Tasks ---")
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for i, t in enumerate(tasks, 1):
                print(i, "-", t)

    elif choice == 3:
        print("\n--- Remove Task ---")
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, t in enumerate(tasks, 1):
                print(i, "-", t)
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(tasks):
                tasks.pop(index - 1)
                print("Task removed!")
            else:
                print("Invalid task number.")

    elif choice == 4:
        print("Exiting Todo List Manager.")
        break

    else:
        print("Invalid choice. Try again.")
