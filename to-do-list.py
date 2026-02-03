tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        if not tasks:
            print("No tasks")
        else:
            for i, t in enumerate(tasks, 1):
                print(i, t)

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
