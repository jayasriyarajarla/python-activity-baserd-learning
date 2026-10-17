
# Weather Data Analysis and Forecast Summary

weather_records = []

# Function to add daily weather data
def add_weather_data():
    date = input("Enter date (DD-MM-YYYY): ").strip()

    if not date:
        print("Date cannot be empty.")
        return

    try:
        temperature = float(input("Enter temperature (Celsius): "))
        humidity = float(input("Enter humidity (0-100%): "))
        rainfall = float(input("Enter rainfall (mm): "))

        if humidity < 0 or humidity > 100:
            print("Humidity must be between 0 and 100.")
            return

        if rainfall < 0:
            print("Rainfall cannot be negative.")
            return

        # Store each day's data as a tuple
        record = (date, temperature, humidity, rainfall)
        weather_records.append(record)

        print("Weather data added successfully!")

    except ValueError:
        print("Please enter valid numeric values.")


# Function to display all weather records
def display_weather_data():
    if not weather_records:
        print("No weather data available.")
        return

    print("\n--- Weather Records ---")

    for record in weather_records:
        date, temperature, humidity, rainfall = record

        print("Date:", date)
        print("Temperature:", temperature, "C")
        print("Humidity:", humidity, "%")
        print("Rainfall:", rainfall, "mm")
        print("-----------------------")


# Function to analyze temperature
def analyze_temperature():
    if not weather_records:
        print("Add weather data first.")
        return

    temperatures = []

    for record in weather_records:
        temperatures.append(record[1])

    average = sum(temperatures) / len(temperatures)
    highest = max(temperatures)
    lowest = min(temperatures)

    print("\n--- Temperature Analysis ---")
    print("Average Temperature:", round(average, 2), "C")
    print("Highest Temperature:", highest, "C")
    print("Lowest Temperature:", lowest, "C")

    for record in weather_records:
        if record[1] == highest:
            print("Hottest Day:", record[0])

        if record[1] == lowest:
            print("Coldest Day:", record[0])


# Function to analyze rainfall
def analyze_rainfall():
    if not weather_records:
        print("Add weather data first.")
        return

    total_rainfall = 0
    rainy_days = 0

    for record in weather_records:
        total_rainfall += record[3]

        if record[3] > 0:
            rainy_days += 1

    average_rainfall = total_rainfall / len(weather_records)

    print("\n--- Rainfall Analysis ---")
    print("Total Rainfall:", round(total_rainfall, 2), "mm")
    print("Average Rainfall:", round(average_rainfall, 2), "mm")
    print("Number of Rainy Days:", rainy_days)


# Function to classify weather conditions
def classify_weather():
    if not weather_records:
        print("Add weather data first.")
        return

    print("\n--- Weather Classification ---")

    for record in weather_records:
        date, temperature, humidity, rainfall = record

        if rainfall >= 10:
            condition = "Rainy"
        elif temperature >= 35:
            condition = "Hot"
        elif temperature <= 15:
            condition = "Cold"
        else:
            condition = "Moderate"

        print(date, ":", condition)


# Function to generate a summary
def generate_summary():
    if not weather_records:
        print("Add weather data first.")
        return

    temperatures = [record[1] for record in weather_records]
    total_rainfall = sum(record[3] for record in weather_records)
    average_temperature = sum(temperatures) / len(temperatures)

    print("\n===== WEATHER SUMMARY =====")
    print("Days Recorded:", len(weather_records))
    print("Average Temperature:", round(average_temperature, 2), "C")
    print("Maximum Temperature:", max(temperatures), "C")
    print("Minimum Temperature:", min(temperatures), "C")
    print("Total Rainfall:", round(total_rainfall, 2), "mm")

    if average_temperature >= 35:
        print("Summary: The recorded period was very hot.")
    elif average_temperature <= 15:
        print("Summary: The recorded period was cold.")
    else:
        print("Summary: Temperatures were moderate on average.")

    if total_rainfall > 0:
        print("Rainfall was recorded during this period.")
    else:
        print("No rainfall was recorded.")


# Function to display unique weather conditions
def unique_conditions():
    if not weather_records:
        print("Add weather data first.")
        return

    conditions = set()

    for record in weather_records:
        temperature = record[1]
        rainfall = record[3]

        if rainfall >= 10:
            conditions.add("Rainy")
        elif temperature >= 35:
            conditions.add("Hot")
        elif temperature <= 15:
            conditions.add("Cold")
        else:
            conditions.add("Moderate")

    print("\nUnique Weather Conditions:")

    for condition in sorted(conditions):
        print("-", condition)


# Main menu
def main():
    while True:
        print("\n===== WEATHER DATA ANALYSIS SYSTEM =====")
        print("1. Add Weather Data")
        print("2. Display Weather Records")
        print("3. Analyze Temperature")
        print("4. Analyze Rainfall")
        print("5. Classify Weather")
        print("6. Generate Weather Summary")
        print("7. Display Unique Conditions")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_weather_data()
        elif choice == "2":
            display_weather_data()
        elif choice == "3":
            analyze_temperature()
        elif choice == "4":
            analyze_rainfall()
        elif choice == "5":
            classify_weather()
        elif choice == "6":
            generate_summary()
        elif choice == "7":
            unique_conditions()
        elif choice == "8":
            print("Thank you for using the Weather Analysis System!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
