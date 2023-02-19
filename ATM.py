print("Welcome to the ATM")

balance = 1000  # initial balance

while True:
    print("1. Check balance")
    print("2. Withdraw money")
    print("3. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Your new balance is:", balance)

    elif choice == 3:
        print("Thank you for using the ATM")
        break

    else:
        print("Invalid choice")
