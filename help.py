students = []

subjects = ("Python", "Mathematics", "English")

# Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# Function to add student details
def add_student():
    name = input("Enter student name: ").strip().title()

    if not name:
        print("Student name cannot be empty.")
        return

    marks = []

    for subject in subjects:
        try:
            mark = float(input(f"Enter marks in {subject} (0-100): "))

            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return

            marks.append(mark)

        except ValueError:
            print("Please enter valid numeric marks.")
            return

    total = sum(marks)
    percentage = total / len(subjects)
    grade = calculate_grade(percentage)

    student = (name, tuple(marks), total, percentage, grade)
    students.append(student)

    print("Student record added successfully!")


# Function to display all student records
def display_students():
    if not students:
        print("No student records available.")
        return

    print("\n--- Student Performance Report ---")

    for student in students:
        name, marks, total, percentage, grade = student

        print("\nStudent Name:", name)

        for i in range(len(subjects)):
            print(subjects[i], ":", marks[i])

        print("Total Marks:", total, "/", len(subjects) * 100)
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)


# Function to analyze class performance
def analyze_performance():
    if not students:
        print("No student records available.")
        return

    percentages = []

    for student in students:
        percentages.append(student[3])

    average = sum(percentages) / len(percentages)
    highest = max(percentages)
    lowest = min(percentages)

    print("\n--- Class Performance Analysis ---")
    print("Number of Students:", len(students))
    print("Class Average:", round(average, 2), "%")
    print("Highest Percentage:", round(highest, 2), "%")
    print("Lowest Percentage:", round(lowest, 2), "%")

    passed = 0
    failed = 0

    for percentage in percentages:
        if percentage >= 50:
            passed += 1
        else:
            failed += 1

    print("Students Passed:", passed)
    print("Students Failed:", failed)


# Function to display unique grades
def display_grades():
    if not students:
        print("No student records available.")
        return

    grades = set()

    for student in students:
        grades.add(student[4])

    print("Grades awarded:", sorted(grades))


# Function to search for a student
def search_student():
    name = input("Enter student name to search: ").strip().lower()

    if not name:
        print("Please enter a name.")
        return

    found = False

    for student in students:
        if student[0].lower() == name:
            print("\nStudent Found")
            print("Name:", student[0])
            print("Total:", student[2])
            print("Percentage:", round(student[3], 2), "%")
            print("Grade:", student[4])
            found = True
            break

    if not found:
        print("Student not found.")


# Main menu
def main():
    while True:
        print("\n===== STUDENT PERFORMANCE SYSTEM =====")
        print("1. Add Student")
        print("2. Display Student Records")
        print("3. Analyze Class Performance")
        print("4. Display Unique Grades")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            analyze_performance()
        elif choice == "4":
            display_grades()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
