books = []
members = []
transactions = []

# Function to add a book
def add_book():
    book_id = input("Enter book ID: ").strip()

    if not book_id:
        print("Book ID cannot be empty.")
        return

    for book in books:
        if book[0] == book_id:
            print("Book ID already exists.")
            return

    title = input("Enter book title: ").strip().title()
    author = input("Enter author name: ").strip().title()

    if not title or not author:
        print("Book title and author are required.")
        return

    try:
        quantity = int(input("Enter number of copies: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        # Tuple: book ID, title, author, total copies, available copies
        books.append((book_id, title, author, quantity, quantity))
        print("Book added successfully!")

    except ValueError:
        print("Enter a valid whole number.")


# Function to register a library member
def register_member():
    member_id = input("Enter member ID: ").strip()

    if not member_id:
        print("Member ID cannot be empty.")
        return

    for member in members:
        if member[0] == member_id:
            print("Member ID already exists.")
            return

    name = input("Enter member name: ").strip().title()

    if not name:
        print("Member name cannot be empty.")
        return

    members.append((member_id, name))
    print("Member registered successfully!")


# Function to find a book
def find_book(book_id):
    for i in range(len(books)):
        if books[i][0] == book_id:
            return i
    return -1


# Function to find a member
def find_member(member_id):
    for i in range(len(members)):
        if members[i][0] == member_id:
            return i
    return -1


# Function to issue a book
def issue_book():
    book_id = input("Enter book ID: ").strip()
    member_id = input("Enter member ID: ").strip()

    book_index = find_book(book_id)
    member_index = find_member(member_id)

    if book_index == -1:
        print("Book not found.")
        return

    if member_index == -1:
        print("Member not found. Register the member first.")
        return

    book = books[book_index]

    if book[4] <= 0:
        print("No copies of this book are available.")
        return

    # Prevent issuing the same book twice to the same member
    for transaction in transactions:
        if (transaction[0] == book_id
                and transaction[1] == member_id
                and transaction[3] == "Issued"):
            print("This member already has this book issued.")
            return

    books[book_index] = (
        book[0], book[1], book[2], book[3], book[4] - 1
    )

    transactions.append(
        (book_id, member_id, book[1], "Issued")
    )

    print("Book issued successfully!")
    print("Book title:", book[1])
    print("Member name:", members[member_index][1])


# Function to return a book
def return_book():
    book_id = input("Enter book ID: ").strip()
    member_id = input("Enter member ID: ").strip()

    book_index = find_book(book_id)

    if book_index == -1:
        print("Book not found.")
        return

    if find_member(member_id) == -1:
        print("Member not found.")
        return

    # Find an active issue record
    transaction_index = -1

    for i in range(len(transactions) - 1, -1, -1):
        transaction = transactions[i]

        if (transaction[0] == book_id
                and transaction[1] == member_id
                and transaction[3] == "Issued"):
            transaction_index = i
            break

    if transaction_index == -1:
        print("No active issue record found for this member and book.")
        return

    book = books[book_index]

    books[book_index] = (
        book[0], book[1], book[2], book[3],
        min(book[3], book[4] + 1)
    )

    old_transaction = transactions[transaction_index]

    transactions[transaction_index] = (
        old_transaction[0],
        old_transaction[1],
        old_transaction[2],
        "Returned"
    )

    print("Book returned successfully!")


# Function to display all books
def display_books():
    if not books:
        print("No books available.")
        return

    print("\n--- Library Book Catalogue ---")

    for book in books:
        print("Book ID:", book[0])
        print("Title:", book[1])
        print("Author:", book[2])
        print("Total Copies:", book[3])
        print("Available Copies:", book[4])
        print("-----------------------------")


# Function to search for a book
def search_book():
    keyword = input("Enter book title or author: ").strip().lower()

    if not keyword:
        print("Please enter a search term.")
        return

    found = False

    for book in books:
        if keyword in book[1].lower() or keyword in book[2].lower():
            print(
                "ID:", book[0],
                "| Title:", book[1],
                "| Author:", book[2],
                "| Available:", book[4]
            )
            found = True

    if not found:
        print("No matching books found.")


# Function to display all members
def display_members():
    if not members:
        print("No members registered.")
        return

    print("\n--- Library Members ---")

    for member in members:
        print("Member ID:", member[0], "| Name:", member[1])


# Function to display transaction history
def display_transactions():
    if not transactions:
        print("No transactions recorded.")
        return

    print("\n--- Library Transaction History ---")

    for transaction in transactions:
        print(
            "Book ID:", transaction[0],
            "| Member ID:", transaction[1],
            "| Book:", transaction[2],
            "| Status:", transaction[3]
        )


# Function to display unique authors
def display_authors():
    if not books:
        print("No books available.")
        return

    authors = set()

    for book in books:
        authors.add(book[2])

    print("\n--- Unique Authors ---")

    for author in sorted(authors):
        print(author)


# Main menu
def main():
    while True:
        print("\n===== SMART LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Search Book")
        print("7. Display Members")
        print("8. Transaction History")
        print("9. Display Unique Authors")
        print("10. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            register_member()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            display_books()
        elif choice == "6":
            search_book()
        elif choice == "7":
            display_members()
        elif choice == "8":
            display_transactions()
        elif choice == "9":
            display_authors()
        elif choice == "10":
            print("Thank you for using the library system!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
