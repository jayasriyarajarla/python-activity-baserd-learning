import string
import getpass

# Common weak passwords for educational checking
common_passwords = {
    "password", "password123", "12345678",
    "qwerty123", "admin123", "welcome123",
    "iloveyou", "123456789"
}

# Function to check password strength
def check_password_strength(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Check uppercase letters
    if any(ch.isupper() for ch in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    # Check lowercase letters
    if any(ch.islower() for ch in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    # Check digits
    if any(ch.isdigit() for ch in password):
        score += 1
    else:
        suggestions.append("Add a number.")

    # Check special characters
    if any(ch in string.punctuation for ch in password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    # Check repeated characters
    if len(password) >= 3 and len(set(password)) == 1:
        score = 0
        suggestions.append("Avoid using the same character repeatedly.")

    # Check common passwords
    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Avoid common or predictable passwords.")

    # Determine strength
    if password.lower() in common_passwords or not password:
        strength = "Very Weak"
    elif len(password) < 8:
        strength = "Weak"
    elif score >= 6 and len(password) >= 12:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, score, suggestions


# Function to audit a password
def audit_password():
    password = getpass.getpass(
        "Enter a test password (input will be hidden): "
    )

    if not password:
        print("Password cannot be empty.")
        return

    strength, score, suggestions = check_password_strength(password)

    print("\n--- Password Security Audit ---")
    print("Password length:", len(password))
    print("Uppercase letters:", any(ch.isupper() for ch in password))
    print("Lowercase letters:", any(ch.islower() for ch in password))
    print("Contains digits:", any(ch.isdigit() for ch in password))
    print(
        "Contains special characters:",
        any(ch in string.punctuation for ch in password)
    )
    print("Strength:", strength)
    print("Score:", score, "/ 6")

    if suggestions:
        print("\nSuggestions to improve security:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("No basic improvements suggested by this checker.")

    print("\nNote: This is a basic educational checker.")


# Function to display security tips
def security_tips():
    tips = (
        "Use long, unique passwords.",
        "Never reuse passwords across accounts.",
        "Use a trusted password manager.",
        "Enable multi-factor authentication.",
        "Never share passwords with others.",
        "Avoid personal information in passwords."
    )

    print("\n--- Password Security Tips ---")

    for number, tip in enumerate(tips, start=1):
        print(str(number) + ".", tip)


# Function to explain audit limitations
def audit_information():
    print("\n--- Security Auditor Information ---")
    print("1. Checks password length and character variety.")
    print("2. Detects a small list of common passwords.")
    print("3. Provides suggestions for improvement.")
    print("4. Does not test real accounts or websites.")
    print("5. Does not guarantee that a password is secure.")
    print("6. Does not store passwords in a file.")


# Main menu
def main():
    while True:
        print("\n===== PASSWORD SECURITY AUDITOR =====")
        print("1. Check Password Strength")
        print("2. View Security Tips")
        print("3. About the Security Auditor")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            audit_password()
        elif choice == "2":
            security_tips()
        elif choice == "3":
            audit_information()
        elif choice == "4":
            print("Thank you for using the Password Security Auditor!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
