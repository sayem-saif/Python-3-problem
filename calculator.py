while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        break

    a, b = map(float, input("Enter two numbers: ").split())

    if choice == "1":
        print("Result =", a + b)
    elif choice == "2":
        print("Result =", a - b)
    elif choice == "3":
        print("Result =", a * b)
    elif choice == "4":
        if b != 0:
            print("Result =", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")
