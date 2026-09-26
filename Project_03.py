balance = 500 
transaction_amount = []
while True:
    print("\nBank Account Management System")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5 Create Account")
    print("6 . Save Transaction History")
    print("6. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print(f"Current Balance: ${balance:.2f}")

    elif choice == '2':
        deposit_amount = float(input("Enter amount to deposit: "))
        balance += deposit_amount
        transaction_amount.append(f"Deposited: ${deposit_amount:.2f}")
        print(f"${deposit_amount:.2f} deposited successfully!")

    elif choice == '3':
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount > balance:
            print("Insufficient funds!")
        else:
            balance -= withdraw_amount
            transaction_amount.append(f"Withdrew: ${withdraw_amount:.2f}")
            print(f"${withdraw_amount:.2f} withdrawn successfully!")

    elif choice == '4':
        if not transaction_amount:
            print("No transactions yet.")
        else:
            print("\nTransaction History:")
            for transaction in transaction_amount:
                print(transaction)
    elif choice == '5':
        account_name = input("Enter your name to create an account: ")
        print(f"Account created successfully for {account_name}!")


    
    elif choice =='6':
        data_save = input("Do you want to save your transaction history? (yes/no): ")
        if data_save.lower() == 'yes':
            with open("transaction_history.txt", "w") as file:
                for transaction in transaction_amount:
                    file.write(transaction + "\n")
    elif choice == '7':
            print("Exiting the program. Goodbye!")
            print("Transaction history saved to 'transaction_history.txt'.")
            break
       
    else:
        print("Invalid choice! Please try again.")