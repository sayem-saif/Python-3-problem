import random

choices = ["Rock", "Paper", "Scissors"]

while True:
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user = int(input("Enter your choice: ")) - 1
    computer = random.randint(0, 2)

    print("You chose:", choices[user])
    print("Computer chose:", choices[computer])

    if user == computer:
        print("It's a tie")
    elif (user == 0 and computer == 2) or \
         (user == 1 and computer == 0) or \
         (user == 2 and computer == 1):
        print("You win!")
    else:
        print("Computer wins!")

    again = input("Play again? (y/n): ")
    if again.lower() != "y":
        break
