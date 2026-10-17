
# Public Transport Route and Fare Calculator

# Route data: (route name, starting point, destination, distance in km)
routes = [
    ("Route 1", "Vijayawada", "Guntur", 40),
    ("Route 2", "Vijayawada", "Hyderabad", 275),
    ("Route 3", "Guntur", "Tenali", 30),
    ("Route 4", "Hyderabad", "Warangal", 150),
    ("Route 5", "Vijayawada", "Tenali", 35)
]

# Fare per kilometre for each transport type
fare_rates = {
    "Bus": 1.50,
    "Train": 1.20,
    "Metro": 2.00
}

# Function to display available routes
def display_routes():
    print("\n--- Available Routes ---")

    for route in routes:
        print(
            route[0], "| From:", route[1],
            "| To:", route[2],
            "| Distance:", route[3], "km"
        )


# Function to calculate fare
def calculate_fare():
    display_routes()

    route_number = input(
        "\nEnter route number (1-5): "
    ).strip()

    if not route_number.isdigit():
        print("Please enter a valid route number.")
        return

    route_index = int(route_number) - 1

    if route_index < 0 or route_index >= len(routes):
        print("Invalid route selection.")
        return

    route = routes[route_index]

    print("\nAvailable Transport Types:")
    for transport in fare_rates:
        print("-", transport)

    transport = input(
        "Choose transport type: "
    ).strip().title()

    if transport not in fare_rates:
        print("Invalid transport type.")
        return

    try:
        passengers = int(input("Enter number of passengers: "))

        if passengers <= 0:
            print("Passenger count must be greater than zero.")
            return

        distance = route[3]
        rate = fare_rates[transport]

        fare_per_person = distance * rate
        total_fare = fare_per_person * passengers

        print("\n--- Fare Details ---")
        print("Starting Point:", route[1])
        print("Destination:", route[2])
        print("Transport Type:", transport)
        print("Distance:", distance, "km")
        print("Fare per km: Rs.", rate)
        print("Fare per Person: Rs.", round(fare_per_person, 2))
        print("Number of Passengers:", passengers)
        print("Total Fare: Rs.", round(total_fare, 2))

    except ValueError:
        print("Please enter a valid whole number.")


# Function to compare route distances
def compare_routes():
    print("\n--- Route Distance Comparison ---")

    display_routes()

    try:
        first = int(input("Enter first route number (1-5): "))
        second = int(input("Enter second route number (1-5): "))

        if not (1 <= first <= len(routes)
                and 1 <= second <= len(routes)):
            print("Invalid route number.")
            return

        route1 = routes[first - 1]
        route2 = routes[second - 1]

        print("\nRoute 1:", route1[1], "to", route1[2])
        print("Distance:", route1[3], "km")

        print("\nRoute 2:", route2[1], "to", route2[2])
        print("Distance:", route2[3], "km")

        difference = abs(route1[3] - route2[3])

        print("Distance Difference:", difference, "km")

        if route1[3] < route2[3]:
            print("Route 1 is shorter.")
        elif route2[3] < route1[3]:
            print("Route 2 is shorter.")
        else:
            print("Both routes have equal distances.")

    except ValueError:
        print("Please enter valid route numbers.")


# Function to display unique destinations
def display_destinations():
    destinations = set()

    for route in routes:
        destinations.add(route[2])

    print("\n--- Unique Destinations ---")

    for destination in sorted(destinations):
        print(destination)


# Function to display transport options
def display_transport_types():
    print("\n--- Transport Types and Fare Rates ---")

    for transport, rate in fare_rates.items():
        print(transport, ": Rs.", rate, "per km")


# Main menu
def main():
    while True:
        print("\n===== PUBLIC TRANSPORT ROUTE AND FARE CALCULATOR =====")
        print("1. Display Available Routes")
        print("2. Calculate Ticket Fare")
        print("3. Compare Route Distances")
        print("4. Display Unique Destinations")
        print("5. Display Transport Types")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_routes()
        elif choice == "2":
            calculate_fare()
        elif choice == "3":
            compare_routes()
        elif choice == "4":
            display_destinations()
        elif choice == "5":
            display_transport_types()
        elif choice == "6":
            print("Thank you for using the calculator!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
