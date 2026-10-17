
# Inventory Management and Low-Stock Alert System

inventory = []
LOW_STOCK_LIMIT = 5


# Function to add a new product
def add_product():
    product_id = input("Enter product ID: ").strip()

    if not product_id:
        print("Product ID cannot be empty.")
        return

    for product in inventory:
        if product[0] == product_id:
            print("Product ID already exists.")
            return

    name = input("Enter product name: ").strip().title()

    if not name:
        print("Product name cannot be empty.")
        return

    try:
        quantity = int(input("Enter initial quantity: "))
        price = float(input("Enter price per item (Rs.): "))

        if quantity < 0:
            print("Quantity cannot be negative.")
            return

        if price < 0:
            print("Price cannot be negative.")
            return

        # Tuple: ID, name, quantity, price
        product = (product_id, name, quantity, price)
        inventory.append(product)

        print("Product added successfully!")

        if quantity <= LOW_STOCK_LIMIT:
            print("LOW-STOCK ALERT: This product has low stock.")

    except ValueError:
        print("Enter a valid quantity and price.")


# Function to find a product
def find_product(product_id):
    for i in range(len(inventory)):
        if inventory[i][0] == product_id:
            return i
    return -1


# Function to display all products
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n--- INVENTORY REPORT ---")

    total_value = 0

    for product in inventory:
        product_id, name, quantity, price = product
        value = quantity * price
        total_value += value

        print("\nProduct ID:", product_id)
        print("Product Name:", name)
        print("Quantity:", quantity)
        print("Price per Item: Rs.", round(price, 2))
        print("Stock Value: Rs.", round(value, 2))

    print("\nTotal Inventory Value: Rs.", round(total_value, 2))


# Function to update stock
def update_stock():
    product_id = input("Enter product ID: ").strip()
    index = find_product(product_id)

    if index == -1:
        print("Product not found.")
        return

    try:
        quantity_change = int(
            input("Enter quantity to add or remove (+/-): ")
        )

        product = inventory[index]
        new_quantity = product[2] + quantity_change

        if new_quantity < 0:
            print("Insufficient stock. Update cancelled.")
            return

        inventory[index] = (
            product[0], product[1], new_quantity, product[3]
        )

        print("Stock updated successfully!")
        print("Available quantity:", new_quantity)

        if new_quantity <= LOW_STOCK_LIMIT:
            print("LOW-STOCK ALERT: Reorder this product.")

    except ValueError:
        print("Enter a valid whole number.")


# Function to sell products
def sell_product():
    product_id = input("Enter product ID: ").strip()
    index = find_product(product_id)

    if index == -1:
        print("Product not found.")
        return

    try:
        quantity_sold = int(input("Enter quantity to sell: "))

        if quantity_sold <= 0:
            print("Quantity sold must be greater than zero.")
            return

        product = inventory[index]

        if quantity_sold > product[2]:
            print("Insufficient stock!")
            return

        new_quantity = product[2] - quantity_sold
        amount = quantity_sold * product[3]

        inventory[index] = (
            product[0], product[1], new_quantity, product[3]
        )

        print("Sale completed successfully!")
        print("Amount: Rs.", round(amount, 2))
        print("Remaining stock:", new_quantity)

        if new_quantity <= LOW_STOCK_LIMIT:
            print("LOW-STOCK ALERT: Reorder this product.")

    except ValueError:
        print("Enter a valid whole number.")


# Function to search for a product
def search_product():
    keyword = input("Enter product ID or name: ").strip().lower()

    if not keyword:
        print("Enter a search term.")
        return

    found = False

    for product in inventory:
        if (keyword in product[0].lower()
                or keyword in product[1].lower()):

            print("\nProduct Found")
            print("ID:", product[0])
            print("Name:", product[1])
            print("Quantity:", product[2])
            print("Price: Rs.", round(product[3], 2))
            found = True

    if not found:
        print("No matching product found.")


# Function to display low-stock products
def low_stock_report():
    if not inventory:
        print("Inventory is empty.")
        return

    found = False

    print("\n--- LOW-STOCK ALERT REPORT ---")
    print("Low-stock limit:", LOW_STOCK_LIMIT)

    for product in inventory:
        if product[2] <= LOW_STOCK_LIMIT:
            print(
                "Product:", product[1],
                "| Quantity:", product[2],
                "| Reorder required"
            )
            found = True

    if not found:
        print("All products have sufficient stock.")


# Function to display unique product names
def unique_product_names():
    if not inventory:
        print("Inventory is empty.")
        return

    names = set()

    for product in inventory:
        names.add(product[1])

    print("\n--- PRODUCT NAMES ---")

    for name in sorted(names):
        print(name)


# Main menu
def main():
    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add Product")
        print("2. Display Inventory")
        print("3. Update Stock")
        print("4. Sell Product")
        print("5. Search Product")
        print("6. Low-Stock Alert Report")
        print("7. Display Unique Product Names")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            display_inventory()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            sell_product()
        elif choice == "5":
            search_product()
        elif choice == "6":
            low_stock_report()
        elif choice == "7":
            unique_product_names()
        elif choice == "8":
            print("Thank you for using the Inventory Management System!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

