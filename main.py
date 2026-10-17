expenses = []
categories = ("Food", "Travel", "Education", "Shopping", "Others")


def add_expense():
    print("\n--- Add Expense ---")

    name = input("Enter expense name: ").strip().title()
    if not name:
        print("Expense name cannot be empty.")
        return

    print("Categories:", ", ".join(categories))
    category = input("Enter category: ").strip().title()

    if category not in categories:
        print("Invalid category! Please select from the list.")
        return

    try:
        amount = float(input("Enter expense amount (Rs.): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        expense = (name, category, amount)
        expenses.append(expense)

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid numeric amount.")


def view_expenses():
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("-" * 55)
    print(f"{'No.':<5}{'Name':<20}{'Category':<15}{'Amount':>12}")
    print("-" * 55)

    for i, expense in enumerate(expenses, start=1):
        name, category, amount = expense
        print(f"{i:<5}{name:<20}{category:<15}Rs.{amount:>8.2f}")

    print("-" * 55)
    print(f"Total Expenses: Rs.{calculate_total():.2f}")


def calculate_total():
    total = 0

    for expense in expenses:
        total += expense[2]

    return total


def analyze_budget():
    print("\n--- Budget Analyzer ---")

    try:
        budget = float(input("Enter your monthly budget (Rs.): "))

        if budget <= 0:
            print("Budget must be greater than zero.")
            return

        total = calculate_total()
        balance = budget - total

        print(f"\nMonthly Budget : Rs.{budget:.2f}")
        print(f"Total Expenses: Rs.{total:.2f}")

        if balance > 0:
            print(f"Remaining Budget: Rs.{balance:.2f}")
            print("Status: You are within your budget.")
        elif balance == 0:
            print("Remaining Budget: Rs.0.00")
            print("Status: You have used your entire budget.")
        else:
            print(f"Budget Exceeded: Rs.{abs(balance):.2f}")
            print("Status: You have exceeded your budget.")

        if total > 0:
            percentage = (total / budget) * 100
            print(f"Budget Used: {percentage:.2f}%")

    except ValueError:
        print("Please enter a valid budget amount.")


def category_analysis():
    print("\n--- Category-wise Analysis ---")

    if not expenses:
        print("No expenses available for analysis.")
        return

    # Set stores unique categories.
    used_categories = set(expense[1] for expense in expenses)

    for category in sorted(used_categories):
        total = sum(
            expense[2]
            for expense in expenses
            if expense[1] == category
        )
        print(f"{category}: Rs.{total:.2f}")


def search_expense():
    print("\n--- Search Expense ---")

    keyword = input("Enter expense name to search: ").strip().lower()

    if not keyword:
        print("Please enter a search term.")
        return

    found = False

    for expense in expenses:
        name, category, amount = expense

        if keyword in name.lower():
            print(
                f"Name: {name} | Category: {category} | "
                f"Amount: Rs.{amount:.2f}"
            )
            found = True

    if not found:
        print("No matching expense found.")


def main():
    while True:
        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Analyze Monthly Budget")
        print("4. Category-wise Analysis")
        print("5. Search Expense")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            analyze_budget()
        elif choice == "4":
            category_analysis()
        elif choice == "5":
            search_expense()
        elif choice == "6":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1 to 6.")


if __name__ == "__main__":
    main()
