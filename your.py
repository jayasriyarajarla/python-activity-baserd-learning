patients = []
appointments = []

# Function to register a patient
def register_patient():
    patient_id = input("Enter patient ID: ").strip()

    if not patient_id:
        print("Patient ID cannot be empty.")
        return

    for patient in patients:
        if patient[0] == patient_id:
            print("Patient ID already exists.")
            return

    name = input("Enter patient name: ").strip().title()

    if not name:
        print("Patient name cannot be empty.")
        return

    age_text = input("Enter patient age: ").strip()

    if not age_text.isdigit():
        print("Please enter a valid age.")
        return

    age = int(age_text)

    if age <= 0 or age > 120:
        print("Please enter an age between 1 and 120.")
        return

    phone = input("Enter contact number: ").strip()

    if not phone.isdigit() or len(phone) != 10:
        print("Enter a valid 10-digit contact number.")
        return

    patient = (patient_id, name, age, phone)
    patients.append(patient)

    print("Patient registered successfully!")


# Function to search for a patient
def find_patient(patient_id):
    for i in range(len(patients)):
        if patients[i][0] == patient_id:
            return i
    return -1


# Function to book an appointment
def book_appointment():
    patient_id = input("Enter patient ID: ").strip()
    index = find_patient(patient_id)

    if index == -1:
        print("Patient not found. Register the patient first.")
        return

    date = input("Enter appointment date (DD-MM-YYYY): ").strip()
    time = input("Enter appointment time: ").strip()
    doctor = input("Enter doctor name: ").strip().title()
    department = input("Enter department: ").strip().title()

    if not date or not time or not doctor or not department:
        print("All appointment details are required.")
        return

    # Prevent the same doctor from being booked
    # for the same date and time twice.
    for appointment in appointments:
        if (appointment[2] == date
                and appointment[3] == time
                and appointment[4].lower() == doctor.lower()):
            print("This doctor already has an appointment at that time.")
            return

    appointment_id = "APT" + str(len(appointments) + 1)

    appointment = (
        appointment_id,
        patient_id,
        date,
        time,
        doctor,
        department,
        "Booked"
    )

    appointments.append(appointment)

    print("Appointment booked successfully!")
    print("Appointment ID:", appointment_id)


# Function to display patient records
def display_patients():
    if not patients:
        print("No patient records available.")
        return

    print("\n--- Patient Records ---")

    for patient in patients:
        print("Patient ID:", patient[0])
        print("Name:", patient[1])
        print("Age:", patient[2])
        print("Contact:", patient[3])
        print("------------------------")


# Function to display appointments
def display_appointments():
    if not appointments:
        print("No appointments available.")
        return

    print("\n--- Appointment Records ---")

    for appointment in appointments:
        print("Appointment ID:", appointment[0])
        print("Patient ID:", appointment[1])
        print("Date:", appointment[2])
        print("Time:", appointment[3])
        print("Doctor:", appointment[4])
        print("Department:", appointment[5])
        print("Status:", appointment[6])
        print("----------------------------")


# Function to search patient details
def search_patient():
    patient_id = input("Enter patient ID to search: ").strip()
    index = find_patient(patient_id)

    if index == -1:
        print("Patient not found.")
        return

    patient = patients[index]

    print("\n--- Patient Details ---")
    print("Patient ID:", patient[0])
    print("Name:", patient[1])
    print("Age:", patient[2])
    print("Contact:", patient[3])


# Function to cancel an appointment
def cancel_appointment():
    appointment_id = input("Enter appointment ID to cancel: ").strip()

    for i in range(len(appointments)):
        appointment = appointments[i]

        if appointment[0] == appointment_id:
            if appointment[6] == "Cancelled":
                print("This appointment is already cancelled.")
                return

            appointments[i] = (
                appointment[0],
                appointment[1],
                appointment[2],
                appointment[3],
                appointment[4],
                appointment[5],
                "Cancelled"
            )

            print("Appointment cancelled successfully!")
            return

    print("Appointment not found.")


# Function to display available departments
def display_departments():
    if not appointments:
        print("No department records available.")
        return

    departments = set()

    for appointment in appointments:
        departments.add(appointment[5])

    print("\nDepartments in appointment records:")
    for department in sorted(departments):
        print("-", department)


# Main menu
def main():
    while True:
        print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
        print("1. Register Patient")
        print("2. Book Appointment")
        print("3. Display Patient Records")
        print("4. Display Appointments")
        print("5. Search Patient")
        print("6. Cancel Appointment")
        print("7. Display Departments")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_patient()
        elif choice == "2":
            book_appointment()
        elif choice == "3":
            display_patients()
        elif choice == "4":
            display_appointments()
        elif choice == "5":
            search_patient()
        elif choice == "6":
            cancel_appointment()
        elif choice == "7":
            display_departments()
        elif choice == "8":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
