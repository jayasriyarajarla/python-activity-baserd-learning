accounts = []
transactions = []

# Function to create an account
def create_account():
    name = input("Enter account holder name: ").strip().title()

    if not name:
        print("Account holder name cannot be empty.")
        return

    account_number = input("Enter account number: ").strip()

    if not account_number.isdigit():
        print("Account number must contain digits only.")
        return

    for account in accounts:
        if account[0] == account_number:
            print("Account number already exists.")
            return

    try:
        balance = float(input("Enter opening balance (Rs.): "))

        if balance < 0:
            print("Opening balance cannot be negative.")
            return

        account = (account_number, name, balance)
        accounts.append(account)

        print("Account created successfully!")

    except ValueError:
        print("Please enter a valid amount.")


# Function to find an account
def find_account(account_number):
    for i in range(len(accounts)):
        if accounts[i][0] == account_number:
            return i
    return -1


# Function to deposit money
def deposit_money():
    account_number = input("Enter account number: ").strip()
    index = find_account(account_number)

    if index == -1:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter deposit amount (Rs.): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        old_account = accounts[index]
        new_balance = old_account[2] + amount

        accounts[index] = (
            old_account[0], old_account[1], new_balance
        )

        transactions.append(
            (account_number, "Deposit", amount, new_balance)
        )

        print("Deposit successful!")
        print("Available balance: Rs.", round(new_balance, 2))

    except ValueError:
        print("Please enter a valid amount.")


# Function to withdraw money
def withdraw_money():
    account_number = input("Enter account number: ").strip()
    index = find_account(account_number)

    if index == -1:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter withdrawal amount (Rs.): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        old_account = accounts[index]

        if amount > old_account[2]:
            print("Insufficient balance.")
            return

        new_balance = old_account[2] - amount

        accounts[index] = (
            old_account[0], old_account[1], new_balance
        )

        transactions.append(
            (account_number, "Withdrawal", amount, new_balance)
        )

        print("Withdrawal successful!")
        print("Available balance: Rs.", round(new_balance, 2))

    except ValueError:
        print("Please enter a valid amount.")


# Function to check account balance
def check_balance():
    account_number = input("Enter account number: ").strip()
    index = find_account(account_number)

    if index == -1:
        print("Account not found.")
        return

    account = accounts[index]

    print("\n--- Account Details ---")
    print("Account Number:", account[0])
    print("Account Holder:", account[1])
    print("Balance: Rs.", round(account[2], 2))


# Function to display all accounts
def display_accounts():
    if not accounts:
        print("No accounts available.")
        return

    print("\n--- All Bank Accounts ---")

    for account in accounts:
        print(
            "Account:", account[0],
            "| Name:", account[1],
            "| Balance: Rs.", round(account[2], 2)
        )


# Function to display transaction history
def transaction_history():
    account_number = input("Enter account number: ").strip()
    index = find_account(account_number)

    if index == -1:
        print("Account not found.")
        return

    found = False
    print("\n--- Transaction History ---")

    for transaction in transactions:
        if transaction[0] == account_number:
            print(
                "Type:", transaction[1],
                "| Amount: Rs.", round(transaction[2], 2),
                "| Balance after transaction: Rs.",
                round(transaction[3], 2)
            )
            found = True

    if not found:
        print("No transactions recorded for this account.")


# Function to display unique transaction types
def transaction_summary():
    if not transactions:
        print("No transactions available.")
        return

    types = set()

    for transaction in transactions:
        types.add(transaction[1])

    print("\nTransaction types:", sorted(types))
    print("Total transactions:", len(transactions))


# Main menu
def main():
    while True:
        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display All Accounts")
        print("6. Transaction History")
        print("7. Transaction Summary")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            display_accounts()
        elif choice == "6":
            transaction_history()
        elif choice == "7":
            transaction_summary()
        elif choice == "8":
            print("Thank you for using the Bank Management System!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
