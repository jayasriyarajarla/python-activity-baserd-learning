
# Intelligent File Organizer and Duplicate File Detector

import os
import hashlib

# Function to organize files by extension
def organize_files():
    folder_path = input("Enter folder path to organize: ").strip()
    folder_path = os.path.abspath(
        os.path.expanduser(folder_path.strip('"'))
    )

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    # Avoid reorganizing the same folder into itself
    files = [
        name for name in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, name))
    ]

    if not files:
        print("No files found in this folder.")
        return

    moved = 0

    for filename in files:
        file_path = os.path.join(folder_path, filename)

        # Skip this Python program itself
        if os.path.abspath(file_path) == os.path.abspath(__file__):
            continue

        extension = os.path.splitext(filename)[1].lower()

        if extension:
            folder_name = extension[1:].upper() + "_Files"
        else:
            folder_name = "No_Extension"

        destination_folder = os.path.join(folder_path, folder_name)

        # Do not move files that are already in the destination
        if os.path.abspath(file_path).startswith(
            os.path.abspath(destination_folder) + os.sep
        ):
            continue

        os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(
            destination_folder, filename
        )

        # Avoid overwriting an existing file
        if os.path.exists(destination_path):
            print("Skipped duplicate filename:", filename)
            continue

        try:
            os.rename(file_path, destination_path)
            print("Moved:", filename, "->", folder_name)
            moved += 1
        except OSError as error:
            print("Could not move", filename, ":", error)

    print("\nOrganization completed.")
    print("Files moved:", moved)


# Function to calculate a file's hash
def calculate_hash(file_path):
    hasher = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hasher.update(chunk)

        return hasher.hexdigest()

    except OSError:
        return None


# Function to detect duplicate files
def detect_duplicates():
    folder_path = input("Enter folder path to scan: ").strip()
    folder_path = os.path.abspath(
        os.path.expanduser(folder_path.strip('"'))
    )

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    hashes = {}
    duplicates_found = False

    # Walk through the selected folder and its subfolders
    for root, directories, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            file_hash = calculate_hash(file_path)

            if file_hash is None:
                print("Could not read:", file_path)
                continue

            if file_hash in hashes:
                if not duplicates_found:
                    print("\n--- Duplicate Files Found ---")
                    duplicates_found = True

                print("Original:", hashes[file_hash])
                print("Duplicate:", file_path)
                print("-----------------------------")
            else:
                hashes[file_hash] = file_path

    if not duplicates_found:
        print("No duplicate files found.")

    print("Duplicate detection completed.")
    print("No files were deleted.")


# Function to display file statistics
def file_statistics():
    folder_path = input("Enter folder path to analyze: ").strip()
    folder_path = os.path.abspath(
        os.path.expanduser(folder_path.strip('"'))
    )

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    extension_counts = {}
    total_files = 0
    total_size = 0

    for root, directories, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            try:
                size = os.path.getsize(file_path)
            except OSError:
                continue

            extension = os.path.splitext(filename)[1].lower()
            extension = extension if extension else "No extension"

            extension_counts[extension] = (
                extension_counts.get(extension, 0) + 1
            )

            total_files += 1
            total_size += size

    print("\n--- File Statistics ---")
    print("Total files:", total_files)
    print("Total size:", round(total_size / 1024, 2), "KB")

    for extension, count in sorted(extension_counts.items()):
        print(extension, ":", count, "files")


# Main menu
def main():
    while True:
        print("\n===== INTELLIGENT FILE ORGANIZER =====")
        print("1. Organize Files by Extension")
        print("2. Detect Duplicate Files")
        print("3. Display File Statistics")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            organize_files()
        elif choice == "2":
            detect_duplicates()
        elif choice == "3":
            file_statistics()
        elif choice == "4":
            print("Thank you for using the File Organizer!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
